# MidnightLabs Public Documentation Standard

This standard governs material published from the MidnightLabs environment. Its purpose is to preserve useful technical evidence without exposing operational access, private infrastructure details, or other people's information.

Public-facing interpretation must also pass the [MidnightLabs Voice and Authorship Standard](./VOICE-STANDARD.md).

## Never publish

- Passwords, passphrases, API tokens, cookies, private keys, recovery codes, or VPN material
- Public IP addresses, dynamic-DNS names, or externally reachable management endpoints
- Exact firewall exports, unredacted backup files, or complete access-control rules
- Personal email addresses, phone numbers, account identifiers, or information belonging to household members
- Device serial numbers, service tags, license keys, or purchase records
- Screenshots containing unrelated browser tabs, notifications, session data, or credentials
- Logs that identify people or expose authentication material

## Publish only after review

- Private addressing, VLAN identifiers, hostnames, and MAC addresses
- Network diagrams
- Firewall and IDS excerpts
- Authentication and authorization designs
- Logs, packet captures, alerts, and screenshots
- AI-generated commands or configuration recommendations

These details may be published when they are necessary to explain the work and have been sanitized or replaced with documentation values.

## Evidence labels

Every substantial artifact should distinguish:

- **Operational evidence** — captured from an implemented system and sanitized
- **Training evidence** — captured from an isolated course or simulation environment
- **Reconstruction** — recreated later from verified notes or configuration
- **Planned** — proposed work that has not been completed
- **Historical** — accurate to an earlier phase but not the present system

## Publication gate

Before merging infrastructure documentation into `main`:

1. Confirm the technical claim against current evidence.
2. Remove or replace sensitive values.
3. Inspect every included screenshot at full resolution.
4. Check Git history when sensitive material may have been committed previously.
5. Verify links and filenames.
6. State the artifact's status and date.
7. Preserve the reason, outcome, failure, and lesson—not merely the final configuration.
8. Pass public-facing interpretation through the Authorship Gate in `VOICE-STANDARD.md`.

If sanitization would destroy the value of the evidence, keep the artifact private.
