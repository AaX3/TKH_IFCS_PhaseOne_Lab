# Week 06 — The Forge: Sprint Midterm Finale
**Program:** TKH IFCS Phase One
**Sessions:** S16 · S17 · S18
**Week Topic:** OSI troubleshooting & break/fix diagnostics · Technical diagnostic exam · Solo full-stack enterprise deployment — Titan Small Business Services

---

## Session 16 — OSI Troubleshooting & Break/Fix Diagnostics

### Summary

Session 16 opened the Sprint Midterm week with a break/fix diagnostic challenge — a set of intentionally misconfigured or broken network and system states that had to be identified, traced to their source layer in the OSI model, and resolved using the tools and knowledge built over the preceding five weeks. This is a practitioner skill that written knowledge cannot fully substitute: real troubleshooting requires the ability to form a hypothesis about which layer the problem lives on, select the right tool to test that hypothesis, interpret the output, and iterate.

Each fault was traced through the OSI stack from the bottom up — checking physical and link layer connectivity before assuming application layer misconfiguration. Findings, tools used, fault locations, and resolutions were logged in `readiness_check.log`, producing a structured diagnostic record that mirrors the runbooks used in real SOC and NOC environments.

### Key Concepts

- OSI-layer fault isolation methodology
- Bottom-up vs. top-down troubleshooting approaches
- Tool selection by OSI layer: `ping`, `traceroute`, `netstat`, `curl`, `dig`, `ss`
- Diagnostic logging and structured runbook documentation
- Network fault categories: connectivity, routing, DNS, application, authentication

### Artifact

`readiness_check.log` — structured diagnostic log documenting fault identification, tool usage, and resolution for each break/fix scenario

### References

NetworkChuck. (2021, May 14). *Free CCNA — OSI model* [Video]. YouTube. https://www.youtube.com/watch?v=We3qE8phJWA

LabEx. (n.d.). *Network basics*. LabEx. https://labex.io/lesson/network-basics

---

## Session 17 — Technical Diagnostic Exam

### Summary

Session 17 was the timed practical examination — a cumulative assessment covering Linux administration, networking, Python scripting, Docker containerization, and Active Directory identity management simultaneously, without reference material. The exam format placed all five domains in a single timed session, requiring not just knowledge of each area in isolation but the ability to move between them fluidly under pressure.

This format mirrors real incident response: a practitioner responding to a live incident cannot pause to look up syntax or reread documentation. The exam tested whether the skills from Weeks 01–05 had been internalized as applied competency rather than surface familiarity. Findings and outputs from the exam were compiled in `practical_exam_report.txt`.

### Key Concepts

- Integrated assessment across Linux, Networking, Python, Docker, and Active Directory
- Applied competency under timed conditions
- Cross-domain problem solving without reference material
- Professional documentation of exam findings

### Artifact

`practical_exam_report.txt` — compiled output and findings from the timed technical diagnostic examination

### References

Red Hat. (2022, January 18). *Linux file permissions explained*. Red Hat. https://www.redhat.com/en/blog/linux-file-permissions-explained

Docker. (2023). *Docker Compose overview*. Docker Documentation. https://docs.docker.com/compose/

---

## Session 18 — Solo Full-Stack Enterprise Deployment: Titan Small Business Services

### Summary

Session 18 was the capstone of the Sprint Midterm — a solo, full-stack enterprise deployment for a fictional client organization, Titan Small Business Services. Working independently and without step-by-step guidance, a complete hardened server environment was built from a bare Ubuntu Server VM. Every component was configured from scratch: SSH was hardened to disable root login and enforce key-based authentication; UFW firewall rules were written to drop all traffic by default and allow only explicitly authorized ports; a Python auditing script was written to verify system health and configuration state; a Docker Compose environment was deployed with explicit network segmentation between services; and the entire architecture was formally documented in a Systems Architecture Document.

The SAD (`HardenedOutpost_SAD.pdf`) captured the design rationale, network topology, security controls applied, and any accepted risk — the same format used in professional security architecture deliverables. This session produced the most complete and employer-facing artifact of Phase One's first half.

### Key Concepts

- End-to-end hardened server deployment from bare OS
- SSH hardening: `PermitRootLogin no`, `PasswordAuthentication no`, `AllowUsers`
- UFW default-deny policy with explicit allow rules
- Python system auditing script for configuration verification
- Docker Compose network segmentation
- Systems Architecture Documentation (SAD) standards

### Artifact

`HardenedOutpost_SAD.pdf` — formal Systems Architecture Document covering network topology, applied security controls, and design rationale for the Titan Small Business Services deployment

### References

SSH.com. (2022). *SSH key-based authentication*. SSH Academy. https://www.ssh.com/academy/ssh/keygen

Ubuntu. (2023). *UFW — uncomplicated firewall*. Ubuntu Documentation. https://help.ubuntu.com/community/UFW

Docker. (2023). *Docker Compose overview*. Docker Documentation. https://docs.docker.com/compose/

---

*AaX3 · TKH IFCS Phase One · Week 06 · 2026*