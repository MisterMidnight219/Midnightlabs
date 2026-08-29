# MidnightLabs — Public Roadmap

MidnightLabs is an evolving cybersecurity homelab and proof-of-work project focused on infrastructure, defensive security, observability, recovery, automation, and applied learning.

This repository is the **public portfolio layer**. Operational documentation, sensitive architecture, credentials, access-control details, unresolved vulnerabilities, and internal AI/operator procedures are intentionally maintained outside the public repository.

## Current Direction

The lab is being rebuilt and documented through a staged lifecycle:

1. **Rediscover** — inventory the environment and reconcile technical debt.
2. **Foundation** — establish durable storage, backups, recovery, and clean infrastructure roles.
3. **Credential Management** — formalize identity, secrets, MFA, and recovery practices.
4. **Fortify** — harden hosts, networks, management surfaces, applications, and trust.
5. **Observe** — centralize useful telemetry, detection, dashboards, and investigation workflows.
6. **Controlled Automation** — develop narrow, auditable tooling with human approval for state-changing actions.
7. **Services** — rebuild applications on the hardened and recoverable platform.
8. **Validation** — test segmentation, recovery, detection, credentials, and operational assumptions.
9. **Edge Readiness** — promote the environment only after the preceding controls have been demonstrated.

## Publication Boundary

Material published here should be useful as proof of work without becoming an operations manual for the live environment.

Public artifacts may include:

- sanitized architecture diagrams;
- project retrospectives and lab journals;
- defensive-security methodology;
- scripts safe for general reuse;
- sanitized configuration examples;
- recovery and hardening lessons;
- evidence of completed tests with sensitive details removed.

The following remain private:

- credentials, tokens, keys, recovery material, or secrets;
- detailed management paths and privileged-access procedures;
- unnecessary internal addressing or identifying infrastructure details;
- unresolved vulnerabilities and exploitable configuration weaknesses;
- operational AI/agent permission boundaries and control procedures;
- full internal configuration exports;
- private investigation evidence or logs containing sensitive data.

## Proof-of-Work Standard

Projects are documented around a simple arc:

**before-state → problem/discovery → reasoning/action → measurable after-state → lesson**

The goal is not to publish every configuration change. The goal is to demonstrate how the system was understood, tested, improved, and verified.

---

**Public repository:** portfolio and sanitized proof of work.  
**Internal operations:** maintained separately in private version control.
