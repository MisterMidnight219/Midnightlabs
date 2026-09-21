# Home Assistant Observatory Source

**Status:** Operational evidence, sanitized  
**App version:** 0.1.2

Home Assistant contributes two complementary targets:

1. the native `/api/prometheus` endpoint for entity and process telemetry;
2. a local Supervisor-aware app on port 9101 for platform, update, resolution, disk, backup, and log-delivery evidence.

The local app also reads Core logs through the Supervisor API and forwards new lines to Loki. It removes ANSI control sequences, preserves recognizable Home Assistant source timestamps in the configured timezone, labels severity, and persists its log snapshot and counters under `/data`.

## Recovery-capable backup model

Supervisor reports backups as `full` or `partial`, but current automatic backups can contain Home Assistant while still being classified as `partial`. Version 0.1.2 therefore preserves the reported type while separately selecting the newest backup whose `content.homeassistant` value is true.

That produces the policy-facing metrics:

- `midnightlabs_ha_recovery_backup_present`
- `midnightlabs_ha_recovery_backup_latest_timestamp_seconds`
- `midnightlabs_ha_recovery_backup_latest_size_bytes`
- `midnightlabs_ha_recovery_backup_latest_protected`

This distinction corrected two false warnings against an older legacy `full` backup after a new protected automatic backup completed.

## Security boundary

- The Supervisor token is injected by the add-on runtime; it is not stored in source.
- The Loki URL is an add-on option and is replaced with a documentation hostname here.
- Prometheus authentication uses a separately mounted bearer-token file.
- Entity privacy filtering remains part of the Home Assistant native Prometheus configuration, not this app.

The app currently requests the Supervisor `manager` role. Least-privilege reduction remains an audit item and must be tested against every required read endpoint before changing it.
