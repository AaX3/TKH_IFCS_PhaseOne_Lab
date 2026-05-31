# Week 07 — Reconnaissance & Vulnerability Analysis
**Program:** TKH IFCS Phase One
**Sessions:** S19 · S20 · S21
**Week Topic:** Passive reconnaissance & OSINT · Active reconnaissance & Nmap scanning · CVE research & CVSS triage

---

## Session 19 — Passive Reconnaissance & OSINT

### Summary

Session 19 marked the program's transition from defensive to offensive perspective — learning to see a target the way an attacker sees it, using only publicly available information. Passive reconnaissance means gathering intelligence without touching the target's systems: no packets sent, no connections made, no footprint left. The target organization was a fictional company ("CloudNano"), and the goal was to build as complete a picture as possible using open-source intelligence (OSINT) techniques alone.

Sources examined included domain registration records (WHOIS), DNS records, public-facing web infrastructure, job postings (which reveal technology stack details), social media, and any leaked or indexed documents. All findings were structured into a threat profile (`ThreatProfile_CloudNano.md`) that a real attacker would use to plan their approach and that a defender can use to understand what their organization exposes before any active testing begins.

### Key Concepts

- Passive reconnaissance: intelligence gathering without active network contact
- OSINT sources: WHOIS, DNS, Shodan, LinkedIn, job postings, Google dorking
- Attack surface mapping from public information alone
- Threat profiling: technology stack, personnel, exposed services
- Attacker perspective as a defensive tool

### Artifact

`ThreatProfile_CloudNano.md` — structured OSINT threat profile for the CloudNano target organization

### References

NetworkChuck. (2020, September 15). *OSINT — finding information on anyone* [Video]. YouTube. https://www.youtube.com/watch?v=qwA6MmbeGNo

HackerSploit. (2021, January 12). *Passive reconnaissance tutorial* [Video]. YouTube. https://www.youtube.com/watch?v=LSUlaE3zy1w

---

## Session 20 — Active Reconnaissance & Nmap Scanning

### Summary

Session 20 moved from passive to active reconnaissance — making direct network contact with the target to enumerate live hosts, open ports, running services, and operating system fingerprints. Nmap (Network Mapper) was used as the primary tool, with scan types selected based on the intelligence objective: ping sweeps to identify live hosts, SYN scans to enumerate open TCP ports without completing the handshake, version detection (`-sV`) to fingerprint service versions, and OS detection (`-O`) to identify the operating system.

Scan results were saved to `nmap_scan_results.txt` using Nmap's output options. The session established a key operational principle: active reconnaissance produces a much richer intelligence picture than passive methods, but it also leaves traces in target logs — making scan technique selection and timing strategically significant. Understanding what Nmap reveals is equally important for attackers planning an intrusion and defenders monitoring for reconnaissance activity against their own infrastructure.

### Key Concepts

- Nmap scan types: ping sweep, SYN scan (`-sS`), full connect (`-sT`), UDP scan (`-sU`)
- Service version detection (`-sV`) and OS fingerprinting (`-O`)
- Nmap output formats: normal, XML, grepable (`-oN`, `-oX`, `-oG`)
- Aggressive scan (`-A`) combining multiple detection methods
- Scan speed and timing templates (`-T0` through `-T5`)

### Artifact

`nmap_scan_results.txt` — Nmap scan output documenting live hosts, open ports, service versions, and OS fingerprints for the target network

### References

NetworkChuck. (2020, July 9). *Nmap tutorial to find network vulnerabilities* [Video]. YouTube. https://www.youtube.com/watch?v=4t4kBkMsDbQ

HackerSploit. (2021, February 18). *Nikto web scanner tutorial* [Video]. YouTube. https://www.youtube.com/watch?v=K78YOmbuT48

---

## Session 21 — CVE Research & CVSS Triage

### Summary

Session 21 translated the vulnerability findings from active reconnaissance into a prioritized risk analysis using the Common Vulnerabilities and Exposures (CVE) framework and the Common Vulnerability Scoring System (CVSS). Each identified service version from the Nmap results was cross-referenced against the National Vulnerability Database (NVD) to find applicable CVEs. CVSS scores (0.0–10.0) provided a standardized severity rating, but the session established that raw CVSS score alone is insufficient for prioritization — exploitability, asset criticality, and compensating controls must all factor into the final risk rating.

A Likelihood × Impact matrix was applied to rank findings by actual risk to the target environment, and a remediation plan was written (`remediation_plan.md`) that assigned priority tiers and recommended remediation actions for each finding. This is the deliverable that translates a technical scan into business-relevant risk communication — the format that gets read by stakeholders who don't speak Nmap.

### Key Concepts

- CVE and NVD: structure, search, and interpretation
- CVSS v3.1 scoring: Base, Temporal, and Environmental metrics
- Likelihood × Impact risk matrix for prioritization
- Compensating controls as a modifier for risk rating
- Remediation planning: priority tiers and recommended actions

### Artifact

`remediation_plan.md` — risk-prioritized remediation plan mapping CVE findings to Likelihood × Impact scores and recommended mitigations

### References

NIST. (2023). *National Vulnerability Database*. National Institute of Standards and Technology. https://nvd.nist.gov/

FIRST. (2023). *CVSS v3.1 specification document*. Forum of Incident Response and Security Teams. https://www.first.org/cvss/specification-document

---

*AaX3 · TKH IFCS Phase One · Week 07 · 2026*