# 🌑 MidnightLabs

**A living record of cybersecurity, infrastructure building, and proof-of-work learning.**

> "You'll know us by the lab light."

MidnightLabs connects formal cybersecurity education, hands-on systems work, and clear documentation. The repository began in 2025 as a lab journal for networking fundamentals, Packet Tracer, Windows Server, and Active Directory. It now serves as the foundation for a larger locally controlled home-lab ecosystem.

The early work remains here deliberately. It shows the starting point, the mistakes, and the mental models that later shaped how MidnightLabs approaches real infrastructure.

---

## Current Direction

MidnightLabs is evolving from isolated classroom labs into a persistent systems environment built around four roles:

| System | Role | Status |
|---|---|---|
| **Midgar** | OPNsense gateway, routing, segmentation, and policy enforcement | Active development |
| **Ellie** | Proxmox compute and virtualization host | Active development |
| **Index Prime** | TrueNAS/ZFS persistence, storage, and planned centralized log retention | Active development |
| **AIDA** | Planned investigation and orchestration layer with human-approved actions | Research and architecture |

The operating principle is simple:

> **Observable over magical. Conquerable over convenient.**

Systems should be locally controllable, understandable, recoverable, and capable of producing evidence about their own behavior.

---

## Foundation Era — 2025

The first MidnightLabs build cycle focused on network fundamentals and a small simulated enterprise environment.

### Enterprise simulation

- Windows Server 2019 domain controller
- Active Directory Domain Services
- DNS and DHCP configuration
- Windows client domain onboarding
- PowerShell user-provisioning experiments
- Kali Linux prepared for future security exercises

Start with the [Foundation Era index](./FOUNDATION-ERA.md) or [Domain Dawn — From VM Chaos to Order](./Lab-journal/Entry1-InitialSetup.md).

### Networking foundations

- [Physical Mode Orientation](./Lab-journal/Entry1.1-RackSimulation.md)
- [Network Representations](./Lab-journal/Entry1.2-NetworkRepresentations.md)
- [Core Network Design Principles](./Lab-journal/Entry1.3NetworkCharacteristics.md)
- [Navigating Cisco IOS](./Lab-journal/Entry1.4Navigating%20The%20IOS.md)
- [MidnightLabs Glossary](./Glossary.md)

These entries are retained as historical learning artifacts. They document the reasoning that preceded the current physical lab; they are not presented as the final state of the environment.

---

## What the Repository Proves

MidnightLabs is designed to capture more than completed configurations. Each substantial project should eventually answer:

1. What problem were we solving?
2. What constraints shaped the design?
3. What did we build?
4. Where did it fail?
5. How did we recover?
6. What changed in our operating doctrine?
7. What evidence supports the result?

That structure turns individual labs into a record of systems thinking.

---

## Project Status

| Project | Evidence currently published | Status |
|---|---|---|
| Foundation networking labs | Journal entries and screenshots | Complete historical series |
| EnterpriseSim v1 | AD, DNS, DHCP, client onboarding, and PowerShell screenshots | Foundation build documented |
| Midgar | Documentation package in preparation | Active development |
| Centralized observability | Architecture and persistence design in progress | Active development |
| Red/blue simulations | Placeholder exercises retained for future development | Planned |
| AIDA | Security boundaries and architecture under research | Planned |

Files under [configs](./configs/) and [incidents](./incidents/) currently include early placeholders. They remain visible as part of the original repository history but should not be interpreted as completed production artifacts.

---

## Documentation and Security

Public documentation is sanitized before publication. Real credentials, VPN material, public addresses, serial numbers, and sensitive management details do not belong in this repository.

Some Foundation Era screenshots contain intentionally disposable training credentials or private lab addressing. These are historical simulation artifacts and must never be reused as operational credentials.

See the [MidnightLabs Public Documentation Standard](./PUBLICATION-STANDARD.md) for the sanitization and evidence rules used before material reaches `main`.

---

## MidnightLabs Doctrine

The current lab is guided by a growing set of principles:

- **Truth before appearance** — document the system that exists.
- **Explicit intent** — every meaningful change should have a reason.
- **Traceability** — decisions, failures, and recoveries should leave evidence.
- **Rollback is law** — preserve a known path back.
- **Protect the management lifeline** — administrative access should survive ordinary mistakes.
- **Persistent memory before intelligence** — logging and provenance precede agentic action.
- **Human approval for consequential actions** — automation should not outrun accountability.

Read the original [Midnight Manifesto](./Manifesto.md) for the philosophy that started the project.

---

## About the Builder

MidnightLabs is built by **David / Mister Midnight**, a U.S. military veteran and cybersecurity student developing practical capability across networking, infrastructure, defensive security, and AI-assisted systems investigation.

- [LinkedIn](https://www.linkedin.com/in/david-dunbar-605a70242)
- YouTube publishing is in development

---

> "You'll know us by the lab light."  
> — Mr. Midnight
