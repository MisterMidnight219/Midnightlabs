#!/usr/bin/env python3

import datetime
import hashlib
import json
import os
import re
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from zoneinfo import ZoneInfo

OPTIONS_FILE = Path("/data/options.json")
STATE_FILE = Path("/data/state.json")
SUPERVISOR_TOKEN = os.environ["SUPERVISOR_TOKEN"]

with OPTIONS_FILE.open(encoding="utf-8") as stream:
    OPTIONS = json.load(stream)

LOKI_URL = OPTIONS["loki_url"]
POLL_INTERVAL = int(OPTIONS["poll_interval"])

LOCK = threading.Lock()
METRICS = ""
STATE = {
    "log_snapshot": [],
    "log_lines_forwarded_total": 0,
    "log_lines_dropped_total": 0,
    "log_push_failures_total": 0,
}


def load_state():
    global STATE

    if not STATE_FILE.exists():
        return

    try:
        with STATE_FILE.open(encoding="utf-8") as stream:
            saved = json.load(stream)

        for key in STATE:
            if key in saved:
                STATE[key] = saved[key]
    except Exception as exc:
        print(f"state_load_error={exc}", flush=True)


def save_state():
    temporary = STATE_FILE.with_suffix(".tmp")

    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(STATE, stream, separators=(",", ":"))

    temporary.replace(STATE_FILE)


def supervisor_request(path, text=False):
    request = urllib.request.Request(
        f"http://supervisor{path}",
        headers={"Authorization": f"Bearer {SUPERVISOR_TOKEN}"},
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        body = response.read().decode("utf-8", errors="replace")

    if text:
        return body

    payload = json.loads(body)

    if payload.get("result") != "ok":
        raise RuntimeError(f"Supervisor API failure for {path}")

    return payload["data"]


def escape_label(value):
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace('"', '\\"')
    )


def metric(name, value, labels=None):
    label_text = ""

    if labels:
        label_text = "{" + ",".join(
            f'{key}="{escape_label(labels[key])}"'
            for key in sorted(labels)
        ) + "}"

    return f"{name}{label_text} {value}"


def boolean(value):
    return 1 if value else 0


def parse_timestamp(value):
    if not value:
        return 0

    return datetime.datetime.fromisoformat(
        value.replace("Z", "+00:00")
    ).timestamp()


def log_delta(previous, current):
    if not previous:
        return current

    maximum = min(len(previous), len(current))

    for overlap in range(maximum, 0, -1):
        if previous[-overlap:] == current[:overlap]:
            return current[overlap:]

    return current


HA_TIMEZONE = ZoneInfo("America/New_York")
ANSI_ESCAPE = re.compile(
    r"\x1b\[[0-?]*[ -/]*[@-~]"
)
LOG_TIMESTAMP = re.compile(
    r"^(\d{4}-\d{2}-\d{2} "
    r"\d{2}:\d{2}:\d{2}[.,]\d+)"
)


def clean_log_line(line):
    return ANSI_ESCAPE.sub("", line)


def source_timestamp_ns(line, fallback_ns):
    match = LOG_TIMESTAMP.match(line)

    if not match:
        return fallback_ns

    timestamp_text = match.group(1).replace(",", ".")

    try:
        parsed = datetime.datetime.fromisoformat(timestamp_text)
        parsed = parsed.replace(tzinfo=HA_TIMEZONE)
        return int(parsed.timestamp() * 1_000_000_000)
    except ValueError:
        return fallback_ns


def detect_level(line):
    match = re.search(
        r"\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b",
        line,
    )

    return match.group(1).lower() if match else "unknown"


def push_logs(lines):
    if not lines:
        return True

    grouped = {}
    fallback_ns = time.time_ns()
    timestamp_occurrences = {}

    for offset, line in enumerate(lines):
        cleaned = clean_log_line(line)
        timestamp = source_timestamp_ns(
            cleaned,
            fallback_ns + offset,
        )

        occurrence_key = (detect_level(cleaned), timestamp)
        occurrence = timestamp_occurrences.get(occurrence_key, 0)
        timestamp_occurrences[occurrence_key] = occurrence + 1
        timestamp += occurrence

        grouped.setdefault(
            detect_level(cleaned),
            [],
        ).append([str(timestamp), cleaned])

    streams = []

    for level, values in grouped.items():
        streams.append(
            {
                "stream": {
                    "environment": "production",
                    "host": "ha-core",
                    "job": "midnightlabs-ha-observability",
                    "level": level,
                    "log_type": "core",
                    "node": "ha-core",
                    "role": "home-automation",
                    "service": "home-assistant",
                    "service_name": "home-assistant",
                    "site": "midnightlabs",
                    "source": "supervisor-api",
                    "vlan": "SERVERS",
                },
                "values": values,
            }
        )

    body = json.dumps({"streams": streams}).encode("utf-8")
    request = urllib.request.Request(
        LOKI_URL,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        if response.status not in (200, 204):
            raise RuntimeError(
                f"Loki returned HTTP {response.status}"
            )

    return True


def collect():
    global METRICS

    lines = []
    success = 1
    log_delivery_success = 1

    try:
        supervisor = supervisor_request("/supervisor/info")
        core = supervisor_request("/core/info")
        operating_system = supervisor_request("/os/info")
        host = supervisor_request("/host/info")
        resolution = supervisor_request("/resolution/info")
        backup_data = supervisor_request("/backups")

        lines.extend(
            [
                "# HELP midnightlabs_ha_collector_success Whether the collector completed successfully.",
                "# TYPE midnightlabs_ha_collector_success gauge",
                metric("midnightlabs_ha_collector_success", 1),
                "# HELP midnightlabs_ha_collector_timestamp_seconds Collector completion time.",
                "# TYPE midnightlabs_ha_collector_timestamp_seconds gauge",
                metric(
                    "midnightlabs_ha_collector_timestamp_seconds",
                    int(time.time()),
                ),
                "# HELP midnightlabs_ha_supervisor_healthy Supervisor health state.",
                "# TYPE midnightlabs_ha_supervisor_healthy gauge",
                metric(
                    "midnightlabs_ha_supervisor_healthy",
                    boolean(supervisor.get("healthy")),
                ),
                "# HELP midnightlabs_ha_supervisor_supported Supervisor support state.",
                "# TYPE midnightlabs_ha_supervisor_supported gauge",
                metric(
                    "midnightlabs_ha_supervisor_supported",
                    boolean(supervisor.get("supported")),
                ),
                "# HELP midnightlabs_ha_component_update_available Component update state.",
                "# TYPE midnightlabs_ha_component_update_available gauge",
                metric(
                    "midnightlabs_ha_component_update_available",
                    boolean(core.get("update_available")),
                    {"component": "core"},
                ),
                metric(
                    "midnightlabs_ha_component_update_available",
                    boolean(supervisor.get("update_available")),
                    {"component": "supervisor"},
                ),
                metric(
                    "midnightlabs_ha_component_update_available",
                    boolean(operating_system.get("update_available")),
                    {"component": "haos"},
                ),
                "# HELP midnightlabs_ha_component_info Home Assistant component version information.",
                "# TYPE midnightlabs_ha_component_info gauge",
                metric(
                    "midnightlabs_ha_component_info",
                    1,
                    {
                        "component": "core",
                        "version": core.get("version", ""),
                        "version_latest": core.get("version_latest", ""),
                    },
                ),
                metric(
                    "midnightlabs_ha_component_info",
                    1,
                    {
                        "component": "supervisor",
                        "version": supervisor.get("version", ""),
                        "version_latest": supervisor.get(
                            "version_latest", ""
                        ),
                    },
                ),
                metric(
                    "midnightlabs_ha_component_info",
                    1,
                    {
                        "component": "haos",
                        "version": operating_system.get("version", ""),
                        "version_latest": operating_system.get(
                            "version_latest", ""
                        ),
                    },
                ),
                "# HELP midnightlabs_ha_resolution_issue_count Supervisor resolution issue count.",
                "# TYPE midnightlabs_ha_resolution_issue_count gauge",
                metric(
                    "midnightlabs_ha_resolution_issue_count",
                    len(resolution.get("issues", [])),
                ),
                "# HELP midnightlabs_ha_resolution_unhealthy_count Supervisor unhealthy condition count.",
                "# TYPE midnightlabs_ha_resolution_unhealthy_count gauge",
                metric(
                    "midnightlabs_ha_resolution_unhealthy_count",
                    len(resolution.get("unhealthy", [])),
                ),
                "# HELP midnightlabs_ha_resolution_unsupported_count Supervisor unsupported condition count.",
                "# TYPE midnightlabs_ha_resolution_unsupported_count gauge",
                metric(
                    "midnightlabs_ha_resolution_unsupported_count",
                    len(resolution.get("unsupported", [])),
                ),
                "# HELP midnightlabs_ha_host_disk_bytes HAOS host disk capacity.",
                "# TYPE midnightlabs_ha_host_disk_bytes gauge",
                metric(
                    "midnightlabs_ha_host_disk_bytes",
                    float(host.get("disk_total", 0)) * 1_000_000_000,
                    {"state": "total"},
                ),
                metric(
                    "midnightlabs_ha_host_disk_bytes",
                    float(host.get("disk_used", 0)) * 1_000_000_000,
                    {"state": "used"},
                ),
                metric(
                    "midnightlabs_ha_host_disk_bytes",
                    float(host.get("disk_free", 0)) * 1_000_000_000,
                    {"state": "free"},
                ),
            ]
        )

        backups = backup_data.get("backups", [])

        lines.extend(
            [
            ]
        )

        lines.extend(
            [
                "# HELP midnightlabs_ha_backup_count Number of native backups by type.",
                "# TYPE midnightlabs_ha_backup_count gauge",
                "# HELP midnightlabs_ha_backup_latest_timestamp_seconds Latest native backup timestamp.",
                "# TYPE midnightlabs_ha_backup_latest_timestamp_seconds gauge",
                "# HELP midnightlabs_ha_backup_latest_size_bytes Latest native backup size.",
                "# TYPE midnightlabs_ha_backup_latest_size_bytes gauge",
                "# HELP midnightlabs_ha_backup_latest_protected Whether the latest backup is protected.",
                "# TYPE midnightlabs_ha_backup_latest_protected gauge",
            ]
        )

        for backup_type in ("full", "partial"):
            matching = [
                backup
                for backup in backups
                if backup.get("type") == backup_type
            ]

            lines.append(
                metric(
                    "midnightlabs_ha_backup_count",
                    len(matching),
                    {"type": backup_type},
                )
            )

            if matching:
                latest = max(
                    matching,
                    key=lambda item: parse_timestamp(item.get("date")),
                )

                lines.append(
                    metric(
                        "midnightlabs_ha_backup_latest_timestamp_seconds",
                        parse_timestamp(latest.get("date")),
                        {"type": backup_type},
                    )
                )
                lines.append(
                    metric(
                        "midnightlabs_ha_backup_latest_size_bytes",
                        latest.get("size_bytes", 0),
                        {"type": backup_type},
                    )
                )
                lines.append(
                    metric(
                        "midnightlabs_ha_backup_latest_protected",
                        boolean(latest.get("protected")),
                        {"type": backup_type},
                    )
                )

        full_backups = [
            backup
            for backup in backups
            if backup.get("type") == "full"
            and backup.get("content", {}).get("homeassistant")
        ]

        lines.extend(
            [
                "# HELP midnightlabs_ha_full_backup_present Whether a full Home Assistant backup exists.",
                "# TYPE midnightlabs_ha_full_backup_present gauge",
                metric(
                    "midnightlabs_ha_full_backup_present",
                    boolean(full_backups),
                ),
            ]
        )

        recovery_backups = [
            backup
            for backup in backups
            if backup.get("content", {}).get("homeassistant")
        ]

        lines.extend(
            [
                "# HELP midnightlabs_ha_recovery_backup_present Whether a recovery-capable Home Assistant backup exists.",
                "# TYPE midnightlabs_ha_recovery_backup_present gauge",
                "# HELP midnightlabs_ha_recovery_backup_latest_timestamp_seconds Latest recovery-capable Home Assistant backup timestamp.",
                "# TYPE midnightlabs_ha_recovery_backup_latest_timestamp_seconds gauge",
                "# HELP midnightlabs_ha_recovery_backup_latest_size_bytes Latest recovery-capable Home Assistant backup size.",
                "# TYPE midnightlabs_ha_recovery_backup_latest_size_bytes gauge",
                "# HELP midnightlabs_ha_recovery_backup_latest_protected Whether the latest recovery-capable Home Assistant backup is protected.",
                "# TYPE midnightlabs_ha_recovery_backup_latest_protected gauge",
                metric(
                    "midnightlabs_ha_recovery_backup_present",
                    boolean(recovery_backups),
                ),
            ]
        )

        if recovery_backups:
            latest_recovery = max(
                recovery_backups,
                key=lambda item: parse_timestamp(item.get("date")),
            )

            recovery_labels = {
                "type": latest_recovery.get("type", "unknown"),
            }

            lines.append(
                metric(
                    "midnightlabs_ha_recovery_backup_latest_timestamp_seconds",
                    parse_timestamp(latest_recovery.get("date")),
                    recovery_labels,
                )
            )
            lines.append(
                metric(
                    "midnightlabs_ha_recovery_backup_latest_size_bytes",
                    latest_recovery.get("size_bytes", 0),
                    recovery_labels,
                )
            )
            lines.append(
                metric(
                    "midnightlabs_ha_recovery_backup_latest_protected",
                    boolean(latest_recovery.get("protected")),
                    recovery_labels,
                )
            )

        current_logs = supervisor_request(
            "/core/logs",
            text=True,
        ).splitlines()

        previous_logs = STATE.get("log_snapshot", [])
        new_logs = log_delta(previous_logs, current_logs)

        try:
            push_logs(new_logs)
            STATE["log_snapshot"] = current_logs
            STATE["log_lines_forwarded_total"] += len(new_logs)
        except Exception as exc:
            log_delivery_success = 0
            STATE["log_push_failures_total"] += 1
            print(f"log_push_error={exc}", flush=True)

        save_state()

    except Exception as exc:
        success = 0
        print(f"collection_error={exc}", flush=True)
        lines = [
            "# HELP midnightlabs_ha_collector_success Whether the collector completed successfully.",
            "# TYPE midnightlabs_ha_collector_success gauge",
            metric("midnightlabs_ha_collector_success", 0),
        ]

    lines.extend(
        [
            "# HELP midnightlabs_ha_log_delivery_success Whether the latest Loki delivery succeeded.",
            "# TYPE midnightlabs_ha_log_delivery_success gauge",
            metric(
                "midnightlabs_ha_log_delivery_success",
                log_delivery_success,
            ),
            "# HELP midnightlabs_ha_log_lines_forwarded_total Core log lines delivered to Loki.",
            "# TYPE midnightlabs_ha_log_lines_forwarded_total counter",
            metric(
                "midnightlabs_ha_log_lines_forwarded_total",
                STATE["log_lines_forwarded_total"],
            ),
            "# HELP midnightlabs_ha_log_lines_dropped_total Core log lines not delivered.",
            "# TYPE midnightlabs_ha_log_lines_dropped_total counter",
            metric(
                "midnightlabs_ha_log_lines_dropped_total",
                STATE["log_lines_dropped_total"],
            ),
            "# HELP midnightlabs_ha_log_push_failures_total Loki push failures.",
            "# TYPE midnightlabs_ha_log_push_failures_total counter",
            metric(
                "midnightlabs_ha_log_push_failures_total",
                STATE["log_push_failures_total"],
            ),
        ]
    )

    with LOCK:
        METRICS = "\n".join(lines) + "\n"

    return success


def collector_loop():
    while True:
        collect()
        time.sleep(POLL_INTERVAL)


class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/metrics"):
            self.send_error(404)
            return

        with LOCK:
            body = METRICS.encode("utf-8")

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/plain; version=0.0.4; charset=utf-8",
        )
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_args):
        return


load_state()
collect()

thread = threading.Thread(
    target=collector_loop,
    daemon=True,
)
thread.start()

print(
    f"metrics_listener=0.0.0.0:9101 poll_interval={POLL_INTERVAL}",
    flush=True,
)

ThreadingHTTPServer(
    ("0.0.0.0", 9101),
    MetricsHandler,
).serve_forever()
