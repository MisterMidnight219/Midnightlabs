# Observatory Source Matrix

**Evidence label:** Operational evidence, sanitized  
**Verified:** 2026-09-21

| Node | Role | Prometheus targets | Metrics evidence | Log evidence |
|---|---|---:|---|---|
| Observatory | Central telemetry | 5 | Prometheus, node exporter, Grafana, Loki, Alloy | Local journald through Alloy |
| Ellie | Proxmox compute | 1 | Host health, guest expectations, backup jobs/tasks/artifacts | Journald |
| Index | TrueNAS storage | 1 | Graphite ingestion, storage and disk-health verdicts | Network syslog |
| Midgar | OPNsense gateway | 1 | Netdata system and network metrics | RFC5424 system logs and Suricata EVE |
| Midgar-SW | Managed switching | 4 | Interfaces, LLDP/bridge topology, PoE/sensors, entity inventory | RFC3164 syslog |
| UniFi Controller | Network control | 1 | Host state, service/dependency state, HTTPS reachability, native backup evidence | Application server log |
| HA-Core | Home automation | 2 | Native entity metrics plus Supervisor/HAOS/recovery telemetry | Core log through Supervisor API |
| Domestic-Ops | Household applications | 1 | Host, service, container, HTTP, and recovery-source state | Journald and selected application files |
| **Total** |  | **16** |  |  |

## Common identity contract

Central series use the labels `site`, `node`, `role`, `service`, and `environment`. Network placement is represented by a sanitized `vlan` label. Sources with multiple scrape purposes add `telemetry_lane`, such as `platform`, `topology`, `power`, or `inventory`.

This makes generic fleet rules possible while preserving enough source identity for investigation.

## Recovery evidence

Observatory treats backups as observable recovery artifacts rather than assuming that a product's backup-type label proves recoverability.

For Home Assistant, a backup is recovery-capable when its Supervisor inventory says it contains Home Assistant. This accommodates modern automatic backups classified as `partial` while still recording the product-reported type. Proxmox, UniFi, and Domestic-Ops each expose source-appropriate evidence rather than sharing a false universal backup model.

## Evidence boundary

Central configurations and the Home Assistant app are included in this package. The source-host collectors for Ellie, Index, Midgar, UniFi, and Domestic-Ops remain private operational artifacts pending separate sanitization and publication review. Their emitted series and central policy are documented here, but this repository does not claim that every source-side implementation is yet reproducible from public files alone.
