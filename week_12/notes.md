# Week 12 — The Final Reckoning
**Program:** TKH IFCS Phase One
**Sessions:** S34 (Memorial Day — no class) · S35 "Portfolio Audit" · S36 "The Final Reckoning — TEPP"
**Week Topic:** Portfolio audit & artifact verification · Phase One Final Reckoning — full-spectrum solo operation

---

## Session 34 — Memorial Day Observed

No class held. Session 34 was not observed in accordance with the Memorial Day holiday.

---

## Session 35 — Portfolio Audit

### Summary

Session 35 was a structured portfolio audit — a methodical review of the entire Phase One repository to verify that every week's folder contained the correct artifacts, that file names matched submission requirements, that commit messages followed the established convention, and that weekly reflections were present and substantive. The audit produced `portfolio_audit.md` as a formal record of the repository's completeness and any items requiring follow-up before the final submission window closed.

This session made explicit a professional reality: the work only counts if it is documented, organized, and findable. A completed lab with no artifact in the repo is indistinguishable from a lab that was never started. The portfolio audit is the quality control pass that transforms a collection of files into a professional portfolio.

### Key Concepts

- Repository hygiene: folder structure, naming conventions, commit messages
- Artifact verification: confirming each session's deliverable is present and correctly placed
- Git log review: commit history as a record of progression
- Portfolio as a professional deliverable — not just evidence for the program but for employers

### Artifact

`portfolio_audit.md` — formal audit record documenting artifact placement, completeness status, and any outstanding items across all 12 weeks

### References

GitHub. (2023). *About Git*. GitHub Docs. https://docs.github.com/en/get-started/using-git/about-git

---

## Session 36 — "The Final Reckoning": TEPP Full-Spectrum Solo Operation

### Summary

Session 36 was the Phase One capstone: the TitanCorp Enterprise Penetration Project (TEPP), a full-spectrum solo penetration and response operation conducted across three isolated Docker networks simultaneously. Every skill developed across Weeks 01–11 was in play — reconnaissance, exploitation, triage, remediation, documentation — without guided steps, worked answers, or collaborative support.

---

### Phase 0 — Reconnaissance

A full Nmap scan of all three target networks identified the following:

- `172.100.0.11` — Redis (port 6379, no authentication required)
- `172.100.0.12` — vsftpd 3.0.2 (port 21, FTP)
- `172.100.0.13` — Apache/web server with `/var/www/html` set to `chmod 777` (world-writable)
- `172.80.0.10` — OpenSSH (port 22, credentials: `root:admin123`)
- `172.60.0.10` — Python web application (port 80, command injection vulnerability)

Each finding was documented with IP, port, service, version, and identified vulnerability, establishing the baseline intelligence for all subsequent phases.

---

### Phase 1 — Rapid Triage

Each of the three broken servers in the triage network was entered via `docker exec`, its misconfiguration confirmed, a remediation applied, and the before/after state documented:

- **`broken_server_1` (Redis):** Redis running with `--protected-mode no` and `--bind 0.0.0.0` — accepting unauthenticated connections from any IP. Remediation: enable authentication and restrict bind address.
- **`broken_server_2` (vsftpd):** FTP service running without enforced authentication controls. Remediation: disable anonymous access, enforce authenticated sessions.
- **`broken_server_3` (Web server):** `/var/www/html` set to `chmod 777`, allowing any process to write files to the web root — a direct path to web shell deployment. Remediation: `chmod 755 /var/www/html`, restrict write access to the web server process only.

---

### Phase 2 — The Breach (SSH Brute-Force via Hydra)

Phase 2 targeted the midterm network's SSH service on `172.80.0.10:22`. Hydra was installed inside the `midterm_target` container and configured to run a credential brute-force attack against the local SSH service using a custom wordlist (`~/wordlist.txt`). The real wordlist was distinguished from the decoy (`passwords.txt`) based on prior intelligence.

> **Note:** Phase 2 was blocked by ARM/M1 Docker networking constraints. Cross-container SSH connections via Hydra failed due to binfmt/QEMU limitations in the M1 environment — the networking layer could not establish the required inter-container SSH path. This was not a procedural error but an architectural limitation of the lab environment on Apple Silicon hardware. The constraint was researched, documented, and noted in the postmortem.

---

### Phase 3 — Full Spectrum (Command Injection & Reverse Shell)

Phase 3 targeted the capstone network's Python web application on `172.60.0.10:80`. The application accepted user input and passed it directly to a system shell without sanitization — a command injection vulnerability. The exploitation path was: craft a payload that appends a malicious command to the expected input, deliver it via the web interface, and establish a reverse shell callback to a netcat listener.

> **Note:** Phase 3 was not completed due to the same ARM/M1 provisioning constraints that blocked Phase 2. The capstone target's `server.py` required manual injection into the container after startup, and the networking environment did not support the required callback connections in this configuration. Phases 0 and 1 are fully documented and complete.

---

### Postmortem

All completed phases (0 and 1) were fully documented in `tepp_postmortem.md` in APA-formatted report style, including: Phase 0 recon findings organized by target network, Phase 1 triage documentation with before/after remediation state for each server, the technical root cause of the Phase 2 and 3 ARM/M1 failures, and a reflective analysis of what was learned across the full operation. Attacker IPs identified during reconnaissance were logged to `threat_ips.txt`.

### Key Concepts

- Multi-environment penetration lab: simultaneous operation across three isolated Docker networks
- Full lifecycle: recon → triage → breach → exploitation → documentation
- Rapid triage: identify, confirm, remediate, document
- SSH brute-force methodology: Hydra, wordlist selection, credential enumeration
- Command injection: input sanitization failure, payload crafting, reverse shell delivery
- ARM/M1 Docker networking constraint: documented as a known architectural limitation
- Professional postmortem writing: structured narrative with technical precision and honest scope assessment

### Artifacts

`tepp_postmortem.md` · `portfolio_audit.md` · `threat_ips.txt`

### References

Van Hauser & Mora, D. (2023). *THC Hydra*. GitHub. https://github.com/vanhauser-thc/thc-hydra

OWASP. (2023). *Command injection*. OWASP Foundation. https://owasp.org/www-community/attacks/Command_Injection

NetworkChuck. (2020, July 9). *Nmap tutorial to find network vulnerabilities* [Video]. YouTube. https://www.youtube.com/watch?v=4t4kBkMsDbQ

Redis. (2023). *Security*. Redis Documentation. https://redis.io/docs/management/security/

---

*AaX3 · TKH IFCS Phase One · Week 12 · 2026*