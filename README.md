# TKH IFCS Phase One — Cybersecurity Lab Portfolio

**Learner:** Aamari Green (AaX3)
**Instructors:** George Robbins, Jane Pierre
**Program:** The Knowledge House — Integrated Fellowship in Cybersecurity (IFCS), Phase One
**Repository:** `TKH_IFCS_PhaseOne_Lab`
**Branch:** `main`
**Duration:** February 2026 – May 2026

---

## Overview

This repository documents the completed lab work, scripts, configuration files, and written assessments produced during Phase One of TKH's IFCS cybersecurity training program. Each weekly folder corresponds to a live evening session (5:30–8:30 PM EST) and contains the portfolio artifacts submitted via `session-submit` and pushed to GitHub as evidence of applied learning.

The curriculum progresses from foundational Linux and Python scripting through network reconnaissance, web application exploitation, incident response, digital forensics, firewall engineering, and endpoint detection — building toward an integrated practitioner skill set aligned with Security Operations Center (SOC), GRC, and entry-level security engineering roles.

**Environment:** M1 MacBook Pro · UTM (Ubuntu Server 22.04 VM) · VS Code Remote-SSH · Docker/Docker Compose · ARM/x86 QEMU binfmt emulation

---

## Repository Structure

```
TKH_IFCS_PhaseOne_Lab/
├── week_01/    # Linux Fundamentals — filesystem, permissions, stream editing & log parsing
├── week_02/    # Networking & Protocol Analysis — OSI, TCP/IP, subnetting, DNS, Wireshark
├── week_03/    # Python for Security — scripting, system interrogation, TCP port connection
├── week_04/    # Docker & Containers — multi-container architecture, secure config, Compose
├── week_05/    # Identity, Access & Active Directory — IAM, Group Policy, domain join
├── week_06/    # The Forge: Sprint Midterm — OSI diagnostics, practical exam, solo enterprise deployment
├── week_07/    # Reconnaissance & Vulnerability Analysis — OSINT, Nmap, CVE/CVSS triage
├── week_08/    # Exploitation & Post-Exploitation — Metasploit, web attacks, SQLi, XSS
├── week_09/    # Exploitation & Post-Exploitation (continued) — BOLA/IDOR, chained web exploits
├── week_10/    # DFIR — chain of custody, disk forensics, memory forensics
├── week_11/    # Active Defense — firewall rules, Suricata IDS, EDR policy deployment
├── week_12/    # The Final Reckoning — portfolio audit & TEPP full-spectrum solo operation
└── README.md
```

---

## Weekly Lab Summaries

---

### Week 01 — Linux Fundamentals

**Sessions:** S01 · S02 · S03
**Topics:** Filesystem navigation & enumeration · File permission hardening & security automation · Stream editing & log parsing
**Key Skills:** Linux CLI, filesystem traversal, `chmod`/`chown`, bash scripting, `grep`/`sed`/`awk`, log analysis

Week 01 established the foundational Linux operating environment inside an Ubuntu Server VM accessed via VS Code Remote-SSH. In S01, the filesystem was navigated and enumerated to understand directory structure and identify files of interest, with findings recorded in `discovery.txt`. In S02, file permission hardening was introduced — using `chmod`, `chown`, and bash scripting to automate the enforcement of least-privilege access controls, producing `harden.sh`. In S03, stream editing and log parsing were practiced using command-line tools (`grep`, `sed`, `awk`) to extract meaningful security data from raw system logs, with workflows captured in `bash_onliners.sh`.

**Artifacts:** `discovery.txt` · `harden.sh` · `bash_onliners.sh`

**References:**

NetworkChuck. (2021, January 7). *Linux for hackers* [Video]. YouTube. https://www.youtube.com/watch?v=VbEx7B_PTOE

NetworkChuck. (2021, January 14). *Linux for hackers part 2* [Video]. YouTube. https://www.youtube.com/watch?v=42iQKuQodW4

TryHackMe. (2021, March 5). *Linux fundamentals* [Video]. YouTube. https://www.youtube.com/watch?v=We3qE8phJWA

RoboJackets. (2019, September 3). *Intro to Git and GitHub* [Video]. YouTube. https://www.youtube.com/watch?v=RGOj5yH7evk

LabEx. (n.d.). *The shell*. LabEx. https://labex.io/lesson/the-shell

---

### Week 02 — Networking & Protocol Analysis

**Sessions:** S04 · S05 · S06
**Topics:** OSI model & TCP/IP fundamentals · IP subnetting & CIDR notation · DNS & protocol interrogation
**Key Skills:** OSI layers, TCP/IP stack, Wireshark, TLS handshake analysis, subnetting, CIDR, DNS, protocol auditing

Week 02 focused on the networking foundations that underlie every security operation. In S04, the OSI model and TCP/IP stack were examined through Wireshark — capturing and analyzing a live TLS handshake to observe how encryption is negotiated at the transport layer. In S05, IP subnetting and CIDR notation were applied practically, designing a subnetting scheme that segments network traffic and reduces attack surface. In S06, DNS behavior and protocol-level communication were interrogated using command-line tools, with findings recorded in `protocol_audit.txt`.

**Artifacts:** `protocol_audit.txt` · Wireshark TLS capture · CIDR subnetting scheme

**References:**

PowerCert Animated Videos. (2019, June 12). *Subnetting mastery* [Video]. YouTube. https://www.youtube.com/watch?v=s_Ntt6eTn94

NetworkChuck. (2021, May 14). *Free CCNA — OSI model* [Video]. YouTube. https://www.youtube.com/watch?v=vv4y_uOneC0

LabEx. (n.d.). *Network basics*. LabEx. https://labex.io/lesson/network-basics

---

### Week 03 — Python for Security

**Sessions:** S07 "The Sentry" · S08 "The Paper Trail" · S09 "The Conductor" · TLAB-03 "Operation Automated Hunt"
**Topics:** Security scripting & service enumeration · System interrogation with Python · Network scripting & TCP port connection
**Key Skills:** Python `socket`, `subprocess`, file I/O, JSON export, automated log parsing, incident response scripting

Week 03 built Python scripting skills across three progressive sessions, each producing a reusable security tool. In S07 ("The Sentry"), `port_check.py` was built using Python's `socket` library — probing multiple target IPs across specified ports using a loop and demonstrating how access control logic gates operate at the network layer. In S08 ("The Paper Trail"), `brute_detector.py` used Python file I/O to open an authentication log in read mode, loop through every line, match on the `"Failed password"` signature, write flagged entries to a clean threat report, and print a count of extracted attack signatures. In S09 ("The Conductor"), `system_auditor.py` used Python's `subprocess` module to execute `ps aux`, scan the running process list for an unauthorized cryptominer, and export a structured JSON security alert using `json.dump`.

The week culminated in TLAB-03 ("Operation Automated Hunt"), an independent lab synthesizing all three skills. `incident_response.py` used `subprocess.run()` to grep a simulated auth log, extracted attacker IP addresses by field index, and exported a structured JSON threat report — replicating the core workflow of an automated SOC detection pipeline.

**Artifacts:** `port_check.py` · `brute_detector.py` · `system_auditor.py` · `incident_response.py` · `threat_report.json` · `s09reflection.md`

**References:**

Real Python. (2022, March 1). *Python sockets tutorial* [Video]. YouTube. https://www.youtube.com/watch?v=LnKoncbQBsM

NetworkChuck. (2021, July 22). *Python for cybersecurity* [Video]. YouTube. https://www.youtube.com/watch?v=4N4Q576i3zA

Red Hat. (2022, January 18). *Linux file permissions explained*. Red Hat. https://www.redhat.com/en/blog/linux-file-permissions-explained

---

### Week 04 — Docker & Containers

**Sessions:** S10 · S11 · S12 "The Conductor & the Fleet" · TLAB-04 "Operation Hyper-Stack"
**Topics:** Virtualization concepts & multi-container architecture · Secure container configuration · Docker Compose deployment
**Key Skills:** Docker, Dockerfile hardening, Docker Compose, multi-container networking, container security, audit logging

Week 04 introduced Docker as the core infrastructure deployment tool used throughout the remainder of the program. In S10, virtualization concepts and multi-container architecture were explored by writing a `docker-compose.yml` to define and connect multiple services within an isolated network. In S11, a Dockerfile was written and hardened — applying security best practices including non-root user execution, minimal base images, and explicit port exposure. In S12 ("The Conductor & the Fleet"), a complete multi-container deployment was orchestrated using Docker Compose, connecting services across defined network segments. TLAB-04 ("Operation Hyper-Stack") synthesized the week into a full stack deployment and audit, with findings exported to `hyperstack_audit.json`.

> **Note:** On M1/ARM hardware, Docker image compatibility required QEMU binfmt emulation to run x86 containers. This constraint recurs throughout subsequent weeks.

**Artifacts:** `docker-compose.yml` · `hyperstack_audit.json` · `sandbox_report.txt` · `deploy_web.sh`

**References:**

NetworkChuck. (2021, April 2). *Docker tutorial for beginners* [Video]. YouTube. https://www.youtube.com/watch?v=42iQKuQodW4

TechWorld with Nana. (2020, November 17). *Docker crash course* [Video]. YouTube. https://www.youtube.com/watch?v=_TlK0-5EJ-Y

---

### Week 05 — Identity, Access & Active Directory

**Sessions:** S13 · S14 · S15
**Topics:** Security policy design, IAM & MFA · Group Policy & access control enforcement · Linux-Windows domain join & identity unification
**Key Skills:** PowerShell, IAM, MFA, Active Directory, Group Policy Objects (GPO), domain join, identity management

Week 05 introduced enterprise identity and access management concepts centered on Windows Active Directory and cross-platform identity unification. In S13, security policy was designed and IAM controls were configured using PowerShell, including MFA enforcement and user onboarding automation (`onboard_engineers.ps1`). In S14, Group Policy Objects (GPOs) were audited and access control rules were enforced across the simulated domain (`gpo_audit.txt`). In S15, a Linux system was joined to a Windows domain to demonstrate identity unification across operating system boundaries, with the completed configuration captured as `unified_identity.png`.

> **Note:** This week presented technical difficulties in the lab environment. Concepts introduced here are reinforced and applied in subsequent weeks' hardening and access control work.

**Artifacts:** `onboard_engineers.ps1` · `gpo_audit.txt` · `unified_identity.png`

**References:**

Microsoft. (2023). *Active Directory documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services

Microsoft. (2023). *Group Policy overview*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview

---

### Week 06 — The Forge: Sprint Midterm Finale

**Sessions:** S16 · S17 · S18
**Topics:** OSI troubleshooting & break/fix diagnostics · Technical diagnostic exam · Solo full-stack enterprise deployment
**Key Skills:** OSI-layer troubleshooting, timed diagnostic assessment, SSH hardening, UFW, Python auditing, Docker Compose, network segmentation, Systems Architecture Documentation (SAD)

Week 06 was the Sprint Midterm — a cumulative practical examination of every skill developed in Phase One's first five weeks, completed under timed conditions. In S16, OSI-layer break/fix diagnostics were performed: network faults were traced to their source layer and resolved, with results logged in `readiness_check.log`. In S17, a timed technical diagnostic assessed Linux, Networking, Python, Docker, and Active Directory competency simultaneously, with findings compiled in `practical_exam_report.txt`. In S18, a solo full-stack enterprise deployment was completed for the fictional organization "Titan Small Business Services" — hardening SSH, configuring UFW firewall rules, writing a Python system auditor, deploying a segmented Docker Compose environment, and producing a formal Systems Architecture Document (`HardenedOutpost_SAD.pdf`).

**Artifacts:** `readiness_check.log` · `practical_exam_report.txt` · `HardenedOutpost_SAD.pdf`

**References:**

SSH.com. (2022). *SSH key-based authentication*. SSH Academy. https://www.ssh.com/academy/ssh/keygen

Ubuntu. (2023). *UFW — uncomplicated firewall*. Ubuntu Documentation. https://help.ubuntu.com/community/UFW

---

### Week 07 — Reconnaissance & Vulnerability Analysis

**Sessions:** S19 · S20 · S21
**Topics:** Passive reconnaissance & OSINT · Active reconnaissance & Nmap scanning · CVE research & CVSS triage
**Key Skills:** OSINT, passive recon, Nmap, active scanning, CVE research, CVSS scoring, risk triage, remediation planning

Week 07 moved from defensive posture into the attacker's perspective — learning to see the network as an adversary sees it. In S19, passive reconnaissance and OSINT techniques were applied against a fictional target organization ("CloudNano"), building an intelligence profile from publicly available sources without touching the target network directly (`ThreatProfile_CloudNano.md`). In S20, active reconnaissance was performed using Nmap to sweep live hosts, enumerate open ports, and fingerprint running services, with results saved to `nmap_scan_results.txt`. In S21, discovered vulnerabilities were mapped to CVEs and scored using the CVSS framework, producing a prioritized remediation plan (`remediation_plan.md`) that ranks findings by Likelihood × Impact.

**Artifacts:** `ThreatProfile_CloudNano.md` · `nmap_scan_results.txt` · `remediation_plan.md`

**References:**

NetworkChuck. (2020, July 9). *Nmap tutorial to find network vulnerabilities* [Video]. YouTube. https://www.youtube.com/watch?v=4t4kBkMsDbQ

HackerSploit. (2021, February 18). *Nikto web scanner tutorial* [Video]. YouTube. https://www.youtube.com/watch?v=K78YOmbuT48

NIST. (2023). *National Vulnerability Database*. National Institute of Standards and Technology. https://nvd.nist.gov/

---

### Week 08 — Exploitation & Post-Exploitation

**Sessions:** S22 · S23 · S24
**Topics:** Exploitation frameworks & gaining a shell · Web application attacks & traffic interception · SQL injection & XSS session theft
**Key Skills:** Metasploit Framework, CVE exploitation, shell access, Burp Suite, traffic interception, SQLi, XSS, session cookie theft

Week 08 introduced active exploitation within a fully authorized lab environment across three escalating sessions. In S22, the Metasploit Framework was used to exploit a known vulnerability on a target host, establishing an initial shell — demonstrating the full exploitation lifecycle from module selection through payload delivery to session handling. In S23, web application attacks were introduced using Burp Suite to intercept and manipulate HTTP traffic between browser and server, revealing how requests can be modified in transit. In S24, SQL injection and cross-site scripting (XSS) were combined: SQLi was used to extract database contents, and XSS was used to steal session cookies — demonstrating how web vulnerabilities chain together in real attacks.

> **Note:** A screenshot confirming the Day 3 submission state could not be transferred from the VM to VS Code Explorer at time of commit. This artifact will be appended when the file transfer issue is resolved.

**Artifacts:** `escalation_path.txt` · `exploit_verification.png`

**References:**

HackerSploit. (2021, May 6). *Metasploit framework tutorial* [Video]. YouTube. https://www.youtube.com/watch?v=8lR27r8Y_ik

Offensive Security. (2023). *Metasploit unleashed*. Offensive Security. https://www.offsec.com/metasploit-unleashed/

PortSwigger. (2023). *Burp Suite documentation*. PortSwigger. https://portswigger.net/burp/documentation

---

### Week 09 — Exploitation & Post-Exploitation (Continued)

**Sessions:** S25 · S26 · S27 "The Invisible Logic" · TLAB-09 "Operation Omni-Portal"
**Topics:** BOLA/IDOR, chained web exploitation, business logic abuse
**Key Skills:** Broken Object Level Authorization (BOLA), IDOR, API exploitation, chained SQLi → XSS → BOLA, business logic bypass

Week 09 continued web exploitation with a focus on API-layer vulnerabilities and chained attack sequences. In S27 ("The Invisible Logic"), Broken Object Level Authorization (BOLA) and IDOR vulnerabilities were exploited — demonstrating how insufficient access controls allow an authenticated user to access objects belonging to other users by manipulating API parameters. A brute-force approach enumerated valid resource IDs across the target API. API behavior was analyzed and logged in `api_audit.log`.

TLAB-09 ("Operation Omni-Portal") chained all three attack classes into a single continuous exploitation sequence against a purpose-built vulnerable application. SQL injection using the payload `admin'--` bypassed the login form entirely by commenting out the password validation query. A Stored XSS payload was then injected into a persistent field, executing in any browser that rendered the affected page. Finally, BOLA was used to access other users' account data through unauthorized API calls. All findings were documented in `OmniPortal_Assessment.md`.

**Artifacts:** `OmniPortal_Assessment.md` · `api_audit.log` · `sqli_report.txt` · `xss_payloads.txt`

**References:**

PortSwigger. (2023). *SQL injection*. Web Security Academy. https://portswigger.net/web-security/sql-injection

OWASP. (2023). *OWASP API security top 10*. OWASP Foundation. https://owasp.org/www-project-api-security/

HackerSploit. (2022, March 14). *Cross-site scripting (XSS) explained* [Video]. YouTube. https://www.youtube.com/watch?v=EoaDgUgS6QA

---

### Week 10 — DFIR: Digital Forensics & Incident Response

**Sessions:** S28 "The Crime Scene" · S29 "The Digital Autopsy" · S30 "The Central Nervous System"
**Topics:** Chain of custody & live triage · Disk forensics · Memory forensics
**Key Skills:** Live triage, MD5/SHA256 hashing, chain of custody, The Sleuth Kit (`fls`/`icat`), disk image analysis, memory carving, ELK stack, Kibana log correlation

Week 10 was a three-session DFIR immersion covering the full first-responder workflow from live triage through forensic analysis to SIEM-based timeline reconstruction.

In S28 ("The Crime Scene"), a quarantined Docker container simulating an active Command-and-Control beacon was accessed via `docker exec`. `netstat -antp` identified a suspicious process listening on port 4444. Forensic evidence was then cryptographically fingerprinted: MD5 hash of a memory dump and SHA256 hash of an artifact package were computed and recorded in `collection_log.txt` — establishing chain of custody, the legal and operational standard ensuring evidence integrity between collection and analysis.

In S29 ("The Digital Autopsy"), disk forensics were performed using The Sleuth Kit. `fls -r` listed all active and deleted files on a raw disk image; a deleted `Resume.exe` malware payload was located by its asterisked inode entry and recovered using `icat`. Memory was also carved using `strings memdump.raw | grep -i "HIDDEN"` to surface a hidden process with no visible window. All findings were documented in `forensic_findings.md` using a WHO / WHAT / WHEN / HOW reporting structure.

In S30 ("The Central Nervous System"), a local ELK stack was deployed and a `enterprise_logs*` index pattern was configured in Kibana. Log correlation queries reconstructed a full breach timeline across three attack stages: initial access (failed login → web server command execution), lateral movement (attacker pivoting to Domain Admin on an internal host), and data exfiltration (anomalous outbound firewall traffic). Findings were documented in `attack_timeline.csv`.

**Artifacts:** `collection_log.txt` · `forensic_findings.md` · `attack_timeline.csv` · `Incident_Response_Report.md`

**References:**

NIST. (2012). *Computer security incident handling guide* (SP 800-61 Rev. 2). National Institute of Standards and Technology. https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

Carrier, B. (2005). *File system forensic analysis*. Addison-Wesley.

Elastic. (2023). *Kibana guide*. Elastic. https://www.elastic.co/guide/en/kibana/current/index.html

---

### Week 11 — Active Defense

**Sessions:** S31 "The Barricade" · S32 "The Tripwire" · S33 "The Last Mile" · TLAB-11 "Operation Fortress"
**Topics:** Firewall rules & traffic filtering · Intrusion detection & alert analysis · Endpoint detection & response
**Key Skills:** UFW, raw iptables, DMZ segmentation, Suricata IDS, custom detection rules, SysmonForLinux, PowerShell obfuscation analysis, XML EDR policy

Week 11 deployed three distinct defensive layers across four sessions — each building on the last to form a complete active defense stack.

In S31 ("The Barricade"), UFW was hardened to default-deny and explicit allow rules were added for authorized ports. Raw `iptables` rules were written to enforce DMZ segmentation, blocking lateral movement from a compromised web server to the internal database subnet (`10.0.5.0/24`). The full ruleset was saved to `firewall_config.sh`.

In S32 ("The Tripwire"), Suricata IDS was deployed inside a Docker container on a custom bridge network. A custom detection rule was written to target a specific network signature and saved to `custom_ids.rules`. Suricata's `fast.log` confirmed alert triggers, providing evidence of the IDS operating correctly.

In S33 ("The Last Mile"), SysmonForLinux and PowerShell Core were installed from the Microsoft repository. A disguised script (`invoice_macro.ps1`) was executed — claiming to download an invoice while launching a hidden child process. Sysmon Event ID 1 (Process Creation) logs surfaced the obfuscated `CommandLine`. An XML EDR detection policy (`edr_policy.xml`) was then authored and loaded into Sysmon, targeting the `delete shadows` command — the canonical ransomware precursor behavior — and verified by re-triggering the script.

TLAB-11 ("Operation Fortress") synthesized all three layers into a Defense-in-Depth report (`Operation_Fortress_Report.md`).

**Artifacts:** `firewall_config.sh` · `custom_ids.rules` · `fast.log` · `edr_policy.xml` · `Operation_Fortress_Report.md`

**References:**

Suricata Project. (2023). *Suricata user guide*. Open Information Security Foundation. https://suricata.readthedocs.io/en/latest/

Microsoft. (2023). *Sysmon*. Microsoft Learn. https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

Debian Wiki. (2023). *Iptables*. Debian. https://wiki.debian.org/iptables

---

### Week 12 — The Final Reckoning: Portfolio Audit & TEPP

**Sessions:** S34 (Memorial Day — no class) · S35 "Portfolio Audit" · S36 "The Final Reckoning"
**Topics:** Portfolio audit & artifact verification · Phase One Final Reckoning — full-spectrum solo operation
**Key Skills:** Portfolio documentation, artifact organization, multi-environment triage, server remediation, SSH brute-force, command injection, reverse shell, iptables lockdown, forensic postmortem writing

Week 12 closed Phase One across two active sessions. S34 was not held in observance of Memorial Day. In S35, a full portfolio audit was conducted — verifying folder structure, confirming artifact placement, and reviewing weekly reflections across all 11 completed weeks. The audit findings were documented in `portfolio_audit.md`.

S36 was the Phase One Final Reckoning: the TitanCorp Enterprise Penetration Project (TEPP), a full-spectrum solo operation across three isolated Docker networks. Phase 0 (Recon) mapped all target environments using Nmap, identifying Redis on `172.100.0.11` (unauthenticated), vsftpd on `172.100.0.12`, a world-writable web directory on `172.100.0.13`, SSH on `172.80.0.10`, and a Python web application on `172.60.0.10` susceptible to command injection. Phase 1 (Triage) remediated each broken server and documented before/after state. Phase 2 (Breach) attempted SSH brute-forcing using Hydra. Phase 3 (Full Spectrum) targeted the command injection endpoint for reverse shell delivery.

> **Note:** Phases 2 and 3 encountered provisioning failures specific to the M1/ARM Docker networking environment — cross-container SSH via Hydra failed due to binfmt/QEMU constraints, not procedural error. Phases 0 and 1 are fully documented. The ARM/M1 constraint was researched and noted in the postmortem as a known architectural limitation.

**Artifacts:** `tepp_postmortem.md` · `portfolio_audit.md` · `threat_ips.txt`

**References:**

Van Hauser & Mora, D. (2023). *THC Hydra*. GitHub. https://github.com/vanhauser-thc/thc-hydra

OWASP. (2023). *Command injection*. OWASP Foundation. https://owasp.org/www-community/attacks/Command_Injection

NetworkChuck. (2020, July 9). *Nmap tutorial to find network vulnerabilities* [Video]. YouTube. https://www.youtube.com/watch?v=4t4kBkMsDbQ

---

## Skills Demonstrated

| Domain | Tools & Concepts |
|---|---|
| Linux Administration | bash, chmod, UFW, iptables, SSH hardening, stream editing |
| Python Scripting | socket, subprocess, file I/O, json, automated reporting |
| Networking | OSI model, TCP/IP, Wireshark, subnetting, CIDR, DNS, protocol auditing |
| Identity & Access Management | Active Directory, PowerShell, Group Policy, MFA, domain join |
| Network Reconnaissance | Nmap, OSINT, passive recon, CVE/CVSS triage, risk scoring |
| Web Application Security | SQLi, Stored XSS, BOLA/IDOR, Burp Suite, API exploitation |
| Penetration Testing | Metasploit, Hydra, command injection, reverse shell, session theft |
| Containerization | Docker, Dockerfile hardening, Docker Compose, QEMU binfmt |
| Digital Forensics | MD5/SHA256 hashing, The Sleuth Kit (fls/icat), memory carving, chain of custody |
| SIEM & Log Analysis | ELK stack, Kibana, log correlation, attack timeline reconstruction |
| Intrusion Detection | Suricata, custom IDS rules, fast.log analysis |
| Endpoint Detection | SysmonForLinux, PowerShell Core, Event ID 1, XML EDR policy |
| Documentation | APA 7th edition, SAD, postmortem writing, SOC-style reporting |

---

## Program Context

TKH's Integrated Fellowship in Cybersecurity (IFCS) is a live, instructor-led evening program running on a 12-week Phase One curriculum. All labs were completed on personal hardware (M1 MacBook Pro) using a UTM-hosted Ubuntu Server 22.04 VM accessed via VS Code Remote-SSH. ARM/x86 Docker image compatibility was addressed throughout using QEMU binfmt emulation. All artifacts were submitted via `session-submit` and versioned to this repository.

---

*Repository maintained by AaX3 · TKH IFCS Phase One · 2026*