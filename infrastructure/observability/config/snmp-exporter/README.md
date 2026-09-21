# Midgar-SW SNMP Modules

`generator.midgar-sw.yml` defines the additional LLDP, bridge, VLAN, PoE, entity, and sensor walks used beside the standard interface module. `snmp.midgar-sw.yml` is the generated exporter configuration captured from the verified deployment.

SNMPv3 authentication and privacy values are intentionally stored in a separate, untracked file and are not present here.

The MIB source bundle used during generation is excluded from this repository because it is third-party material and not required to understand the resulting module contract. Regeneration should use the matching Prometheus SNMP exporter generator and the applicable vendor/standards MIBs in a private build workspace.
