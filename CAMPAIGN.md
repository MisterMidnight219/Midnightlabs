# MidnightLabs Main Campaign --- The Road to the Edge

> **Fresh-chat recovery:** Read this file before proposing campaign
> work. Treat its doctrine, gates, ledger, and checkpoints as
> authoritative. Verify completion before awarding XP. Reopen objectives
> if later changes invalidate earlier evidence.

## Campaign Identity

-   **Project:** MidnightLabs
-   **Owner/final authority:** Mr. Midnight
-   **Agent role:** Aion --- investigator, technical co-pilot,
    documentation partner
-   **Current phase:** I --- Rediscover
-   **Final unlock:** Midgar promoted to the actual Internet edge
-   **Final achievement:** **Keeper of the Edge**
-   **Watchtower:** absorbed into Phase V --- Eyes; action-oriented
    expansions move to Phase VI --- The Bridge

## Mission

Transform MidnightLabs from an organically grown homelab into a **known,
recoverable, hardened, observable, documented, and deliberately operated
environment** capable of supporting controlled AI-assisted investigation
and action.

The campaign ends only when the systems behind Midgar have earned
promotion to production-edge status.

## End-State Roles

| Component | Role |
|---|---|
| Midgar | Edge router/firewall, routing, segmentation, VPN, policy |
| Midgar-SW | Core switching, VLAN/trunk transport |
| Fusion Core | Managed access-layer switching |
| Ellie | Primary virtualization/application compute |
| Index Prime | Durable storage, backups, logs, archives, protected state |
| Observatory | Telemetry, analysis, dashboards, alerting |
| Watchtower | Restricted read-only investigation capability |
| The Bridge | Controlled execution plane for approved tools/actions |
| AIDA | Future persistent reasoning/operator layer |
| Mr. Midnight | Authority over intent, risk, credentials, privileged actions |

## Architectural Laws

1. Compute is not durable state.
2. A snapshot is not automatically a backup.
3. A backup never restored is a hypothesis.
4. Observation does not imply authority.
5. Human and machine credentials remain distinct.
6. Least privilege applies to users, services, agents, VLANs, and APIs.
7. Management connectivity is sacred.
8. Meaningful changes require impact and rollback plans.
9. Prevent where practical; detect where prevention fails; observe both.
10. Production capability must pass **BUILD → HARDEN → OBSERVE → RECOVER → PROVE**.
11. Secrets do not enter Git/public documentation/sanitized reports/chat intentionally.
12. The Edge remains locked until the environment earns promotion.

## Evidence and XP

XP is awarded only for verified completion. Evidence may include command
output, sanitized configs, hashes/timestamps, screenshots, API
responses, diagrams, access-control tests, restore tests, packet
captures, telemetry, investigation reports, and revocation tests.

Discussion earns no XP. Installation alone earns no XP. Public evidence
must be sanitized and must distinguish confirmed fact, inference, and
hypothesis.

## Publishing Doctrine

**Build once. Capture evidence while working. Publish at milestones.**

- **GitHub = proof:** architecture, decisions, incidents, runbooks,
  scripts, sanitized configs, restore/hardening/investigation evidence.
- **LinkedIn = professional narrative:** meaningful phase completions
  and lessons, not every config change.
- **YouTube = story + understanding:** only quests with a genuine
  narrative arc.

### Continuous Content Threshold Protocol

During all campaign work, Aion continuously evaluates whether the work has crossed a meaningful **publishing/story threshold**. This is separate from XP or technical quest completion: a technical objective may advance the campaign without being worth publishing, while a failure, discovery, investigation, or partial milestone may become a strong story before a boss gate is complete.

A strong threshold usually contains some useful portion of: **before-state → problem/discovery → reasoning/action → measurable after-state → lesson**.

When a threshold is crossed, especially before temporary evidence is changed or destroyed, Aion should briefly interrupt the technical flow and:

1. Flag the threshold to Mr. Midnight.
2. Classify it as **GitHub / LinkedIn / YouTube / Bank for Later** (one or more may apply).
3. Inventory useful evidence already present in the working conversation: screenshots, command output, configs, diagrams, logs, packet captures, dashboards, errors, before/after states, and verification results.
4. Identify missing evidence worth capturing **before continuing**, prioritizing ephemeral before-states that cannot be recreated honestly later.
5. Ask for only the additional screenshots/output needed to strengthen the artifact.
6. When useful, ask Mr. Midnight a short reflection question about what he expected, what surprised him, what failed, why he chose the approach, what he learned, or how his mental model changed.
7. Preserve the milestone for later packaging if stopping to publish would disrupt the technical sprint.

Content should emerge as a by-product of real MidnightLabs work. Aion should not wait for Mr. Midnight to remember to ask whether something is publishable, and should not manufacture significance where the technical/story delta is weak.

## Academic Crossover

Coursework advances the campaign only when learned concepts are applied
and verified in MidnightLabs.

- **NWIT 245:** Fortify/Eyes --- layered defense, firewalls, VPN, IDS, Windows/Linux hardening, risk/policy.
- **Python/Scripting:** health checks, backup verification, reporting, APIs, eventual Bridge tools.
- Future red-team work may feed Audit II; incident-response work may feed recovery/telemetry.

# Campaign Map

```text
I. REDISCOVER
      ↓
II. FOUNDATION
      ↓
III. THE VAULT
      ↓
IV. FORTIFY
      ↓
V. EYES
      ↓
VI. THE BRIDGE
      ↓
VII. SERVICES
      ↓
VIII. AUDIT II
      ↓
IX. THE EDGE
```

**Phase IX is hard-locked until I--VIII pass.**

# Current Quest Ledger --- 2026-08-29

**Current phase:** I --- Rediscover  
**Primary work:** Index Prime validation + Ellie guest archaeology

### Confirmed

- [x] Midgar substantially audited; VLAN/firewall ancestry reconstructed.
- [x] Fusion Core/controller connectivity restored; addressing/aliases reconciled; Core updated.
- [x] Ellie host, Proxmox, networking, storage, VM/CT inventory captured.
- [x] Ellie root exhaustion traced to `/var/lib/vz/dump`; bad backup job disabled; obsolete archives removed.
- [x] Index network, RAIDZ2 topology, datasets, shares, services, scrub config, ACL baseline captured.
- [x] Extended SMART testing completed across the six current Index data drives.
- [x] Four current 500-GB members passed extended SMART testing.
- [x] Two current members (`sdd` and `sdf`) failed extended SMART and are marked for replacement.
- [x] Index hardware confirmed: Dell PowerEdge T330, 8-bay SAS/SATA backplane, PERC H730 exposing disks individually as JBOD to ZFS.
- [ ] **BLOCKED — Awaiting Reinforcements:** eight HGST HUS724030ALS640 3-TB SAS drives purchased for Index Prime Generation II; expected Sept. 2–9, 2026.
- [ ] Finish Ellie guest archaeology: keep/rebuild/merge/archive/retire.
- [ ] Close remaining inventory gaps.
- [ ] Capture final Phase-I known-state baseline.

### Active Side Quests

- **Old Soldiers — BLOCKED: Awaiting Reinforcements.** Four current members passed extended SMART; two failed and are marked for replacement. Eight HGST HUS724030ALS640 3-TB SAS drives are inbound.
- **Ghosts of Ellie:** unfinished VM/CT archaeology.
- **Broken Window:** SPICE/clipboard workflow if still useful.

---

# PHASE I --- REDISCOVER

> **Do not improve what we have not understood.**

### Quests

**The Old Queen --- Midgar**
- [x] Inspect current config/policy.
- [x] Reconstruct VLAN110/default-LAN history.
- [x] Inspect aliases/firewall behavior.
- [ ] Preserve final sanitized baseline and unresolved findings.

**The Roads Between --- Switching**
- [x] Reconstruct active switching/controller topology.
- [x] Restore Fusion Core ↔ controller.
- [ ] Preserve final running configs/topology and hardening debt.

**The Machine That Dreams --- Ellie**
- [x] Host/network/storage/guest inventory.
- [x] Root-storage incident resolved.
- [ ] Audit every guest's purpose, dependencies, data, and fate.

**The Archive Before Memory --- Index Prime**
- [x] RAIDZ2/datasets/shares/tasks/ACLs/SMART baseline.
- [x] Finish extended SMART tests.
- [x] Decide keep/watch/replace: four current members passed; `sdd` and `sdf` failed and are marked for replacement.
- [x] Confirm 8-bay SAS-capable T330/PERC H730 JBOD architecture and slot visibility.
- [ ] **BLOCKED — Awaiting Reinforcements:** receive, inventory, and validate eight HGST HUS724030ALS640 3-TB SAS drives.
- [ ] Preserve serial/slot mapping and migration evidence during replacement/migration.

### Boss Gate --- **Name the Kingdom**

Produce one known-state inventory answering what exists, what it does,
where it lives, what data/services are active, what projects are
unfinished, and what debt remains.

**Reward:** 1,000 XP --- **Archaeologist of MidnightLabs**  
**Unlock:** Phase II

**Content:** GitHub sanitized audit/topology/incidents; LinkedIn
technical-debt retrospective; YouTube candidate: *I Audited My Own
Cybersecurity Homelab---and Found Months of Technical Debt.*

---

# PHASE II --- FOUNDATION

> **Give every important thing a home, recovery path, and owner.**

### Durable Memory

- [ ] Resolve Index disk health and complete Generation-II migration.
- [ ] SMART short/long schedule, scrubs, alerts, cold-spare doctrine.
- [ ] Define dataset purposes, quotas, ACLs, ZFS snapshots.
- [ ] Classify data: replaceable / rebuildable / important / irreplaceable.

### Ellie Reforged

- [ ] Define NVMe performance tier and 1TB Bulk tier.
- [ ] Resolve duplicate storage presentation.
- [ ] Establish root free-space policy and bounded backup behavior.
- [ ] Place/retire guest storage intentionally.

### Lifeboats

- [ ] Present Index backup storage to Proxmox with dedicated identity.
- [ ] Configure snapshot-mode VM/CT backups to Index.
- [ ] Define recent/monthly/yearly retention and quota.
- [ ] Verify backups.
- [ ] Destroy/isolate a test workload and restore solely from Index.

### The Record

- [ ] Protect Midgar, switch, UniFi, TrueNAS, and Proxmox configs.
- [ ] Hash/timestamp baselines.
- [ ] Separate infrastructure-config backups from whole-VM backups.

### Sacred Ground

- [ ] Reconcile management addressing/naming.
- [ ] Define approved management sources and WireGuard path.
- [ ] Document emergency access and dependencies.

### Boss Gate --- **Burn the Boat**

Recover a deliberately removed/isolated test workload from Index using
documented procedure.

**Reward:** 1,250 XP --- **Nothing Important Lives Once**  
**Unlock:** Phase III

**Content:** GitHub storage/restore doctrine; LinkedIn verified recovery;
YouTube: *What Happens If My Proxmox Server Dies?*

---

# PHASE III --- THE VAULT

> **Every key has an owner. Every owner has a boundary.**

### Choose the Vault

Evaluate personal+lab organization, hosted/self-hosted threat model,
offline behavior, export/recovery, MFA/passkeys, sharing, emergency
access, clients, APIs, and failure when Ellie/Index/Internet are
unavailable.

### Divide the Keys

- [ ] Separate personal and infrastructure collections.
- [ ] Inventory privileged accounts.
- [ ] Identify reused/legacy/mystery credentials.
- [ ] Define admin/everyday/service identities.
- [ ] Define SSH keys, API tokens, MFA/passkeys, recovery codes, break-glass.
- [ ] Define what Aion/AIDA may never retrieve.

### Rotation Day

- [ ] Rotate selected legacy credentials.
- [ ] Revoke superseded credentials.
- [ ] Verify dependent services.
- [ ] Test vault recovery and one revoke/reissue workflow.

### Boss Gate --- **Break the Old Keys**

Prove an old credential fails, its replacement works, recovery exists,
and services remain healthy.

**Reward:** 1,000 XP --- **Keeper of Keys**  
**Unlock:** Phase IV

---

# PHASE IV --- FORTIFY

> **Assume an experienced red teamer is looking for the little edges.**

### Harden the Hosts

Patching, unnecessary services, local firewalls, root/admin/SSH policy,
accounts/groups, filesystem permissions, scheduled tasks, repositories,
security logging.

### Harden the Roads

VLAN boundaries, native/default VLANs, trunk restriction, unused ports,
management reachability, inter-VLAN least privilege, client/guest/IoT
isolation, SNMP.

### Harden the Gates

Midgar management exposure, WireGuard permissions, stale firewall
aliases/rules, DNS/DHCP exposure, brute-force/rate controls, plaintext
management, source limiting.

### Forge Trust

- [ ] Inventory HTTP/HTTPS surfaces and untrusted/self-signed certs.
- [ ] Define internal CA/certificate strategy.
- [ ] Define renewal and private-key rules.
- [ ] Disable obsolete TLS/protocols where supported.
- [ ] Validate trusted HTTPS for selected management services.

### Seal the Applications

Default credentials, admin exposure, API scopes, service/database
permissions, session security, backup/export protections.

### Side Quest --- **Seal the Scrolls**

Secret scanner + pre-commit check + fake-secret validation.

### Boss Gate --- **The Hard Edge Review**

For each major system record attack surface, likely entry points,
controls, unresolved/accepted risk, and expected telemetry.

**Reward:** 1,250 XP --- **No Soft Corners**  
**Unlock:** Phase V

**Content:** GitHub hardening/cert baselines; LinkedIn NWIT 245
crossover; YouTube: *I Hardened My Homelab Before Putting It on the
Internet.*

---

# PHASE V --- EYES

> **A control that fires silently is only half alive.**

### Light the Beacons

- [ ] Define log sources/transport/retention.
- [ ] Bound Index `Logs` growth.
- [ ] Centralize selected infrastructure logs.
- [ ] Preserve high-value security events.
- [ ] Verify time synchronization.

### Awaken Observatory

- [ ] Reconcile current Observatory state.
- [ ] Select/validate analysis/visualization stack.
- [ ] Build initial health/security views and alerts.
- [ ] Ensure Ellie loss does not erase all durable logs.

### Tune the Sentinel

- [ ] Finish Suricata IDS-first.
- [ ] Tune noise/flowbits.
- [ ] Validate intended traffic visibility.
- [ ] Generate benign test detections and centralize events.
- [ ] Define IPS promotion criteria.

## Major Quest --- BUILD THE WATCHTOWER

**Mission:** Give Aion controlled, read-only, auditable visibility
without broad authority.

### Raise the Watchtower
- [ ] Create/validate operations VM, identity, addressing, updates.

### Divide the Keys
- [ ] Human admin identity + restricted Aion runtime.
- [ ] No unrestricted sudo.
- [ ] `/srv/midnightlabs` workspace.
- [ ] Secrets outside agent-readable space; prove denial.

### Draw the Boundary
- [ ] Source-limit management.
- [ ] Deny USERS/IOT/GUEST/LAB.
- [ ] Permit only required destinations; log/verify denies.

### Equip the Investigator
- [ ] Git/GitHub, Python/pipx, SSH, jq/yq/curl/rsync/tmux, network/SNMP diagnostics, secret scanner, operations repo, `AGENTS.md`, investigation packet format.

### Open the Eyes
Progressively grant read-only access to:
- [ ] Ellie
- [ ] Index
- [ ] Switching
- [ ] Midgar
- [ ] Observatory telemetry

Every target requires narrow role, dedicated credential where possible,
source restriction, permission record, failed-write proof, and revocation
proof.

### Watchtower Final Trial --- **Exorcise the Ghost**

Aion completes a timestamped cross-system investigation without
screenshot/command ferrying; evidence is retained, findings/hypotheses
separated, no state changed, sanitized report produced, and access
revocation is visible in telemetry.

**Watchtower reward:** 1,500 XP --- **Keeper of the Watchtower**

### Boss Gate --- **Make Noise in the Dark**

Prove `event → control/detection → log → transport → storage → analysis → alert/investigation`.

**Reward:** 1,500 XP --- **Eyes Open**  
**Unlock:** Phase VI

**Content:** GitHub telemetry + Watchtower model; LinkedIn first
cross-system investigation; YouTube: *I Gave AI Eyes Into My Network---but No Hands.*

---

# PHASE VI --- THE BRIDGE

> **Sight becomes action only through a narrow door.**

### Build the Bridge

- [ ] Reimage/prepare dedicated execution host.
- [ ] Define network/management boundaries, audit trail, updates/recovery.
- [ ] Keep it distinct from firewall, NAS, and primary compute.

### Tools, Not Shells

Begin with narrow tools such as `check_index_health()`,
`get_vm_status()`, `check_backup_age()`, `get_firewall_blocks()`,
`collect_config_backup()`, `generate_health_report()`.

Each defines inputs, targets, credential, output schema, timeout/failure
behavior, audit event, and rollback if state-changing.

### Hands Behind Glass

- [ ] Classify actions: read-only / low-risk / approval-required / forbidden.
- [ ] Implement first human-approved state change.
- [ ] Verify post-state, audit trail, and kill switch.

### Seat of AIDA

- [ ] Provider-neutral tool interface.
- [ ] Reasoning separated from credentials.
- [ ] Persistent context/evidence without unrestricted secrets.
- [ ] Approval flow, incident behavior, forbidden autonomous actions.

### Python Apprenticeship

`student script → tested utility → structured tool → Bridge capability`

### Boss Gate --- **Move One Piece**

Aion/AIDA proposes one low-risk action; Mr. Midnight approves; Bridge
executes with scoped identity; telemetry records it; state is verified;
identity is revoked and repeat action fails.

**Reward:** 1,500 XP --- **Hands Behind Glass**  
**Unlock:** Phase VII

**Content:** GitHub Bridge/Python tools; LinkedIn human-in-loop AI ops;
YouTube: *I Built an AI Operator Without Giving It Root.*

---

# PHASE VII --- SERVICES

> **Applications inherit the platform; they do not invent their own civilization.**

### Domestic Ops

Reconcile/rebuild Grocy + Barcode Buddy with explicit compute/state
homes, backups, hardening, telemetry, and recovery.

### Home Assistant

Reconcile HA-Core, dependencies, durable state backup, access hardening,
telemetry, and restore.

### Service Template

Every future service records purpose, owner, compute, state,
VLAN/network, authentication, backup, logging, updates, hardening,
recovery, and retirement.

### Boss Gate --- **Kill a Service, Keep the State**

Rebuild/restore a selected service onto clean compute while preserving
durable state and validating auth, logging, and policy.

**Reward:** 1,000 XP --- **The City Lives**  
**Unlock:** Phase VIII

---

# PHASE VIII --- AUDIT II

> **Attack our assumptions before someone else does.**

### Boss Rush

1. **Forbidden Roads:** USERS→MGMT, IoT→unauthorized SERVERS, Guest→internal, LAB→production, unauthorized management, WireGuard permissions.
2. **Dead Keys:** revoked/stale credentials, MFA, service-account scope, break-glass.
3. **Blind Spots:** firewall denies, auth failures, IDS events, service failures; find silent paths.
4. **The Bridge Betrays Us:** unauthorized tool/action, scope escape, privilege escalation within approved lab boundaries, audit protection, kill switch.
5. **Machines Disappear:** Ellie, Index, Observatory, controller, selected service failures.
6. **Burn the Backups:** deletion/modification protection, retained-generation restore, ZFS recovery, off-host recovery.
7. **Experienced Red Teamer Review:** exposed services, cert/trust weaknesses, stale rules, unnecessary privilege, defaults, BMC/firmware, management assumptions, agentic-AI attack surface, logging blind spots, recovery dependencies.

Every attack test records expected result, actual result, and telemetry.

### Boss Gate --- **Red Midnight**

Produce a final readiness report: controls, failures, remediations,
accepted risks, blockers, restore evidence, telemetry evidence,
credential state, and **READY / NOT READY FOR EDGE**.

**NOT READY keeps Phase IX locked.**

**Reward:** 2,000 XP --- **Red Midnight**  
**Unlock:** Phase IX

**Content:** GitHub audit methodology; LinkedIn adversarial lessons;
YouTube: *I Attacked My Own Network Before Making It My Router.*

---

# PHASE IX --- THE EDGE

> **Everything behind the gate has earned the right to depend on it.**

### Pre-Edge Lock

- [ ] Foundation/Vault/Fortify/Eyes/Bridge/Services passed.
- [ ] Audit II = READY.
- [ ] Documentation current.
- [ ] Backups and restores verified.
- [ ] Credentials intentionally rotated.
- [ ] Rollback ready.
- [ ] Known-good configs exported.
- [ ] Management lifeline verified.

### Credential Day

Rotate remaining sensitive infrastructure credentials as appropriate,
revoke superseded secrets/tokens, verify MFA/passkeys and machine
identities, confirm vault recovery, confirm no secrets in public
artifacts.

### Crown Midgar

Validate WAN, fail/recovery, NAT, DNS, DHCP, VLAN policy, WireGuard,
management, IDS, telemetry, and rollback.

### Final Trial --- **Open the Gate**

Promote Midgar to the production Internet edge. Observe live and verify
clients, services, segmentation, management, VPN, logging, IDS,
DNS/DHCP, controller reachability, and rollback readiness.

Critical failure means rollback.

**Reward:** 3,000 XP --- **Keeper of the Edge**  
**Campaign:** COMPLETE

**Content:** GitHub final architecture/retrospective; LinkedIn campaign
completion; YouTube finale: *I Replaced My Home Router With the
Cybersecurity Lab I Built.*

---

# Campaign Side Quests

- **The Scribe:** reusable audit/incident/investigation/change reports.
- **The Canary:** harmless deviations/events for detection testing.
- **Seal the Scrolls:** secret scanning/public-artifact hygiene.
- **Old Soldiers:** Index disk lifecycle/spares/slot mapping.
- **Ghosts of Ellie:** unfinished VM/CT reconciliation.
- **Broken Window:** SPICE/clipboard repair if useful.
- **Chronicle the Build:** maintain sanitized portfolio evidence.

# Rank Progression

| Rank | Requirement |
|---|---|
| Archaeologist | Phase I |
| Steward | Phase II |
| Keeper of Keys | Phase III |
| Warden | Phase IV |
| Watcher | Phase V |
| Operator | Phase VI |
| Systems Keeper | Phase VII |
| Red Sentinel | Phase VIII |
| Keeper of the Edge | Phase IX |

# XP Ledger

| Date | Objective | Evidence | XP | Total |
|---|---|---|---:|---:|
| 2026-08-29 | Campaign packet created | This file | 0 | 0 |

Retroactive XP requires reconciliation against this campaign's gates.

# Decision Log

### 2026-08-29 --- The Edge moves last
Midgar's actual Internet-edge promotion is the final deployment phase.

### 2026-08-29 --- Credential management is infrastructure
Password management, MFA/passkeys, recovery, SSH/API identities,
human/machine separation, and intentional rotation receive a dedicated phase.

### 2026-08-29 --- Hardening is explicit
Hosts, protocols, certificates, management surfaces, network boundaries,
applications, and permissions receive a dedicated phase.

### 2026-08-29 --- Watchtower is absorbed
Foundation work moves earlier; read-only investigation becomes a Phase-V
major quest; controlled action becomes Phase VI.

### 2026-08-29 --- Content is part of the campaign
GitHub proves, LinkedIn interprets, YouTube tells the strongest stories.

### 2026-08-29 --- Education feeds the build
Course concepts advance quests only when applied and verified.

### 2026-08-29 --- Publishing thresholds are detected during the work
Aion proactively watches for meaningful story/publishing thresholds during campaign execution, flags them before ephemeral evidence disappears, identifies the appropriate medium, inventories existing evidence, requests missing captures, and gathers operator reflection when useful. Technical milestones and publishing milestones are related but not identical.

### 2026-08-29 --- Nothing goes to waste
MidnightLabs treats displaced hardware as a capability resource rather than automatic e-waste. Hardware is audited, classified, and reassigned to a meaningful role when its remaining reliability and operating cost justify that role. Token uses do not count. Failed hardware is not trusted with important data merely to avoid disposal; it may be retained for testing, teardown, training, or retired responsibly when genuinely spent.

# Checkpoint Log

### 2026-08-29 --- Main campaign accepted

- Nine-phase campaign established.
- Watchtower absorbed.
- Current phase remains **I --- Rediscover**.
- Ellie host/storage discovery is substantially complete.
- Ellie guest archaeology remains incomplete.
- No XP awarded for creating the packet.

### 2026-08-29 --- Old Soldiers blocked awaiting Index Generation II drives

- Extended SMART testing completed across the six current 500-GB Index data drives.
- Four members completed extended SMART without error.
- `sdd` (`WD-WCC2E0ZHEATE`) failed with 63 pending sectors, 51 offline-uncorrectable sectors, and 3 reallocations.
- `sdf` (`55T78WVAS`) failed extended SMART with 32 pending sectors.
- Index hardware confirmed as Dell PowerEdge T330 with 8-bay SAS/SATA backplane and PERC H730 exposing drives individually as JBOD to ZFS.
- Eight HGST HUS724030ALS640 3-TB 3.5-inch SAS drives purchased for Generation-II Index storage; expected Sept. 2–9, 2026.
- **Old Soldiers status: BLOCKED — Awaiting Reinforcements.**
- **Resume trigger:** Mr. Midnight presents/confirms arrival of the eight HGST drives.
- **Immediate resume sequence:** inventory all eight by serial → inspect SMART history → extended/burn-in testing → disposition each drive → plan/execute safe migration to validated 8-drive storage → verify ZFS health/scrub → classify displaced 500-GB drives under the Nothing Goes to Waste doctrine.
- **Cash-in condition:** Generation-II Index storage is healthy, validated, documented, and displaced hardware is classified for meaningful reuse or retirement.
- Campaign work may continue elsewhere while this branch is blocked; next recommended work is **Ghosts of Ellie**.

# Fresh-Chat Resumption Protocol

When Mr. Midnight asks **"Where are we?"** or **"What quest are we on?"**:

1. Read this file.
2. Report current phase/quest, first incomplete required objective, blockers, side quests, XP/rank, and next locked phase.
3. Consult supporting evidence when needed.
4. Verify work before checking objectives or awarding XP.
5. Update checkpoint/decision logs after meaningful progress.
6. Reopen invalidated objectives.
7. Do not skip ahead because a later phase is more exciting.
8. Never unlock The Edge without **READY** from Audit II.
9. Throughout resumed campaign work, apply the **Continuous Content Threshold Protocol**: proactively detect publishable story deltas, protect ephemeral evidence before it disappears, classify the medium, request missing captures, and gather reflection when useful.

# Final Campaign Statement

MidnightLabs is complete when it is not merely functional, but
**understood, recoverable, hardened, observable, controllable, testable,
and intentionally exposed**.

The campaign begins by asking:

> **What did we actually build?**

It ends by answering:

> **We know what it is. We know how it fails. We know how to see it. We
> know how to recover it. We know who can touch it. We tried to break
> it. Now we are willing to put it on the Edge.**
