# Week 10 — DFIR: Digital Forensics & Incident Response
**Program:** TKH IFCS Phase One
**Sessions:** S28 "The Crime Scene" · S29 "The Digital Autopsy" · S30 "The Central Nervous System"
**Week Topic:** Chain of custody & live triage · Disk forensics · Memory forensics

---

## Session 28 — "The Crime Scene": Chain of Custody & Live Triage

### Summary

Session 28 opened with a scenario drawn directly from real incident response practice: a TitanCorp server was suspected of hosting an active Command-and-Control beacon, and the task was to perform rapid triage on the live system without destroying volatile data. The constraint matters — volatile data (active network connections, running processes, open file handles) exists only in memory and disappears the moment a system is shut down or restarted. A first responder who powers down the machine before collecting volatile evidence has destroyed evidence that cannot be recovered.

The compromised container (`compromised_host`) was entered via `docker exec -it compromised_host /bin/sh`. `netstat -antp` was used to list all active TCP connections and their associated process IDs, revealing a suspicious process listening on port 4444 — a port commonly associated with reverse shells and C2 frameworks. The process name and PID were recorded.

After exiting the container, the forensic evidence locker (`~/DFIR_Evidence/`) was accessed, containing a memory dump and an artifact package staged by the TA. Cryptographic hashes were computed: `md5sum memory_dump.raw` produced an MD5 fingerprint of the memory dump, and `sha256sum system_artifacts.zip` produced a SHA256 fingerprint of the artifact package. Both hashes were recorded in `collection_log.txt`. These hashes are the chain of custody: any future modification of the evidence files will change their hash values, providing tamper detection and legal defensibility.

### Key Concepts

- Volatile vs. non-volatile evidence: collection order and priority
- `netstat -antp` for active connection and PID enumeration
- Port 4444 as a common C2/reverse shell indicator
- MD5 and SHA256 cryptographic hashing for evidence integrity
- Chain of custody: what it is, why it matters, how it is established
- `collection_log.txt` as a legal and operational evidence record

### Artifact

`collection_log.txt` — chain of custody log documenting malicious process name, PID, MD5 hash of memory dump, and SHA256 hash of artifact package

### References

NIST. (2012). *Computer security incident handling guide* (SP 800-61 Rev. 2). National Institute of Standards and Technology. https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

SANS Institute. (2021). *FOR508: Advanced incident response, threat hunting, and digital forensics*. SANS. https://www.sans.org/cyber-security-courses/advanced-incident-response-threat-hunting-training/

---

## Session 29 — "The Digital Autopsy": Disk Forensics

### Summary

Session 29 performed a two-phase forensic investigation — first into memory, then into raw disk sectors — to reconstruct a malware infection from its artifacts after the fact. The scenario: an employee had opened a file named `Resume.exe` that subsequently disappeared. The attacker believed that deleting the file was sufficient to destroy the evidence. The session proved them wrong.

**Phase 1 — Memory Carving:** The `strings` utility was used to extract all human-readable text from `memdump.raw`, and `grep -i "HIDDEN"` filtered the output for anomalous process references. This simulated the behavior of the Volatility `pslist` plugin — surfacing a hidden process that had no visible window and had not appeared in a standard `ps` listing. The process ID and executable name were recorded.

**Phase 2 — Disk Forensics with The Sleuth Kit:** `fls -r compromised_drive.dd` recursively listed all files on the raw disk image — both active and deleted. Deleted files were identified by an asterisk preceding their inode number. The inode number for the deleted `Resume.exe` was located, and `icat compromised_drive.dd [INODE] > recovered_malware.txt` extracted the raw file data by reading directly from the disk sectors, bypassing the filesystem's deletion record entirely. The recovered payload was inspected to determine its function.

All findings were compiled in `forensic_findings.md` using a WHO / WHAT / WHEN / HOW reporting structure — the same format used in real forensic investigation reports.

### Key Concepts

- Memory carving: extracting process artifacts from raw memory dumps
- `strings` + `grep` as a lightweight Volatility substitute
- The Sleuth Kit: `fls` for file listing, `icat` for inode-based data extraction
- Deleted file recovery: why deletion does not destroy data
- Inode numbers as file system pointers
- WHO / WHAT / WHEN / HOW forensic reporting structure

### Artifacts

`forensic_findings.md` — forensic investigation report documenting hidden process, deleted malware recovery, and infection analysis

### References

Carrier, B. (2005). *File system forensic analysis*. Addison-Wesley.

The Sleuth Kit. (2023). *The Sleuth Kit documentation*. https://www.sleuthkit.org/sleuthkit/docs.php

NIST. (2012). *Computer security incident handling guide* (SP 800-61 Rev. 2). National Institute of Standards and Technology. https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

---

## Session 30 — "The Central Nervous System": Memory Forensics & SIEM Log Correlation

### Summary

Session 30 introduced the Security Information and Event Management (SIEM) platform as the central nervous system of enterprise security operations — the tool that aggregates log data from across the entire environment and makes it searchable, correlatable, and actionable. A local ELK stack (Elasticsearch, Logstash, Kibana) was deployed and fully booted from a provisioning script, and a `enterprise_logs*` index pattern was configured in Kibana's Stack Management.

The practical work was a three-stage attack timeline reconstruction using only SIEM queries — no direct access to the compromised systems, only the logs they generated. Each stage required a different search strategy and a different log source:

**Stage 1 — Initial Access:** A `Failed Login` query in Kibana's Discover tab surfaced the attacker's external source IP. Querying that IP against web server logs revealed the exact command the attacker executed once they gained access.

**Stage 2 — Lateral Movement:** Searching for `"Domain Admin"` in Windows Security logs showed the attacker escalating privileges and moving to an internal host. The internal IP used for lateral movement was recorded.

**Stage 3 — Exfiltration:** Querying firewall logs with the internal IP identified anomalous outbound traffic volume — a timestamp and data transfer amount that fell far outside normal baseline behavior.

All three rows were documented in `attack_timeline.csv`, producing a minute-by-minute breach timeline of the kind presented to stakeholders and regulators following a real incident.

### Key Concepts

- ELK stack architecture: Elasticsearch (storage/search), Logstash (ingestion), Kibana (visualization)
- Index patterns and log ingestion configuration
- Kibana Discover: KQL query syntax, field filtering, log expansion
- Log correlation: linking events across disparate sources by IP and timestamp
- Attack timeline reconstruction: Initial Access → Lateral Movement → Exfiltration
- SIEM as the operational center of a mature security program

### Artifacts

`attack_timeline.csv` · `Incident_Response_Report.md`

### References

Elastic. (2023). *Kibana guide*. Elastic. https://www.elastic.co/guide/en/kibana/current/index.html

NIST. (2012). *Computer security incident handling guide* (SP 800-61 Rev. 2). National Institute of Standards and Technology. https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

SANS Institute. (2021). *FOR508: Advanced incident response, threat hunting, and digital forensics*. SANS. https://www.sans.org/cyber-security-courses/advanced-incident-response-threat-hunting-training/

---

*AaX3 · TKH IFCS Phase One · Week 10 · 2026*