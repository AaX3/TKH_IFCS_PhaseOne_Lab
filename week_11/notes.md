# Week 11 — Active Defense
**Program:** TKH IFCS Phase One
**Sessions:** S31 "The Barricade" · S32 "The Tripwire" · S33 "The Last Mile" · TLAB-11 "Operation Fortress"
**Week Topic:** Firewall rules & traffic filtering · Intrusion detection & alert analysis · Endpoint detection & response

---

## Session 31 — "The Barricade": Firewall Rules & Traffic Filtering

### Summary

Session 31 ("The Barricade") introduced layered firewall engineering — first using UFW as the human-readable management layer, then dropping down to raw `iptables` rules to enforce DMZ segmentation at the packet filter level. The scenario was drawn from a real attack pattern: a web server in the DMZ has been compromised, and the attacker is attempting to use it as a pivot point to reach the internal database subnet. The firewall must stop that lateral movement even if the web server itself is no longer trustworthy.

UFW was configured with a default-deny policy: all incoming and outgoing traffic is blocked unless explicitly permitted. Authorized ports (SSH on 22, HTTP on 80, HTTPS on 443) were added as explicit allow rules. This default-deny posture means that any new service or connection must be deliberately authorized — unknown traffic fails closed rather than open.

Raw `iptables` rules were then written to enforce the DMZ boundary. A rule was added to the `FORWARD` chain blocking all traffic from the web server's network segment to the internal database subnet (`10.0.5.0/24`). This rule operates at the packet level, below UFW's abstraction, and cannot be bypassed by reconfiguring UFW alone. The complete ruleset was written to `firewall_config.sh` for repeatable deployment.

### Key Concepts

- UFW default-deny policy: `ufw default deny incoming`, `ufw default deny outgoing`
- Explicit allow rules by port and protocol
- `iptables` chains: INPUT, OUTPUT, FORWARD
- DMZ segmentation: blocking lateral movement between network zones
- `iptables -A FORWARD` rules for inter-subnet traffic control
- `firewall_config.sh` as a deployable hardening artifact

### Artifact

`firewall_config.sh` — complete UFW and iptables ruleset enforcing default-deny posture and DMZ segmentation blocking lateral movement to `10.0.5.0/24`

### References

Debian Wiki. (2023). *Iptables*. Debian. https://wiki.debian.org/iptables

Ubuntu. (2023). *UFW — uncomplicated firewall*. Ubuntu Documentation. https://help.ubuntu.com/community/UFW

NIST. (2009). *Guidelines on firewalls and firewall policy* (SP 800-41 Rev. 1). National Institute of Standards and Technology. https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final

---

## Session 32 — "The Tripwire": Intrusion Detection & Alert Analysis

### Summary

Session 32 ("The Tripwire") deployed Suricata — an open-source, high-performance Network Intrusion Detection System (IDS) — inside a Docker container on a custom bridge network, and then wrote custom detection rules to trigger on specific network signatures. Where firewalls block traffic based on rules, IDS systems watch traffic and alert when it matches a known threat pattern, providing visibility into attacks that the firewall permits or that originate from inside the network.

Suricata was configured to run in IDS mode (detect and alert, not block), monitoring traffic on the container's network interface. A custom Suricata rule was written following the rule syntax: action, protocol, source IP/port, direction, destination IP/port, and rule options including `msg`, `content`, `sid`, and `rev`. The rule was written to match a specific network signature and saved to `custom_ids.rules`. Suricata's `fast.log` was monitored to confirm that the rule fired correctly when matching traffic was observed.

The session established the IDS as the network's early warning system: it cannot prevent an attack that the firewall permits, but it records it — creating the audit trail that enables post-incident investigation.

### Key Concepts

- Suricata IDS: architecture, rule syntax, alert modes
- Rule structure: action · protocol · src · direction · dst · options
- Rule options: `msg`, `content`, `nocase`, `sid`, `rev`
- `fast.log` format and alert verification
- IDS vs. IPS: detection vs. prevention modes
- Docker-based IDS deployment on a custom bridge network

### Artifacts

`custom_ids.rules` · `fast.log`

### References

Suricata Project. (2023). *Suricata user guide*. Open Information Security Foundation. https://suricata.readthedocs.io/en/latest/

Suricata Project. (2023). *Rule management*. Open Information Security Foundation. https://suricata.readthedocs.io/en/latest/rules/index.html

---

## Session 33 — "The Last Mile": Endpoint Detection & Response

### Summary

Session 33 ("The Last Mile") moved the defensive perimeter from the network to the endpoint itself — deploying SysmonForLinux and PowerShell Core from the Microsoft repository, then using Sysmon's process creation telemetry to unmask an obfuscated malicious script before writing an XML detection policy to trap its behavior automatically.

**Phase 1 — The Sysmon Eye:** Sysmon was initialized with `sudo sysmon -accepteula -i`, beginning continuous endpoint monitoring. A suspicious script (`invoice_macro.ps1`) was executed using PowerShell Core (`pwsh ~/invoice_macro.ps1`). The script presented itself as a routine invoice download — but Sysmon Event ID 1 (Process Creation) logs told a different story. `sudo tail -n 50 /var/log/syslog | grep -i sysmon` revealed that `pwsh` had launched a child process with a hidden, obfuscated `CommandLine` argument that was not visible from the script's surface behavior. This is the mechanism by which malware persists on endpoints: it hides inside processes that look legitimate.

**Phase 2 — The Ransomware Trap:** An XML EDR detection policy (`edr_policy.xml`) was opened and a `<CommandLine condition="contains">delete shadows</CommandLine>` rule was confirmed inside the `<ProcessCreate>` block. The `delete shadows` command — which deletes Windows Volume Shadow Copies — is the canonical ransomware precursor behavior: ransomware runs this before encrypting files to prevent recovery from backups. The policy was loaded into the running Sysmon instance with `sudo sysmon -c ~/edr_policy.xml`, and the script was re-executed to confirm the alert fired: `sudo tail -n 20 /var/log/syslog | grep -i "delete shadows"`.

### Key Concepts

- SysmonForLinux: installation from Microsoft repository, EULA acceptance, initialization
- Sysmon Event ID 1 (Process Creation): fields, CommandLine visibility
- PowerShell obfuscation and child process spawning as evasion techniques
- XML EDR policy structure: `<EventFiltering>`, `<ProcessCreate>`, `<CommandLine>` conditions
- `delete shadows` as ransomware precursor behavior indicator
- EDR policy deployment and live alert verification

### Artifact

`edr_policy.xml` — Sysmon XML detection policy targeting `delete shadows` ransomware precursor behavior, verified against a live endpoint

### References

Microsoft. (2023). *Sysmon*. Microsoft Learn. https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

Microsoft. (2023). *Sysmon configuration*. Microsoft Learn. https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#configuration-files

MITRE ATT&CK. (2023). *T1490 — inhibit system recovery*. MITRE Corporation. https://attack.mitre.org/techniques/T1490/

---

## TLAB-11 — "Operation Fortress": Defense-in-Depth Report

### Summary

TLAB-11 ("Operation Fortress") synthesized all three defensive layers deployed during Week 11 — firewall engineering, intrusion detection, and endpoint detection — into a unified Defense-in-Depth report (`Operation_Fortress_Report.md`). The report documented how each layer contributes to a security posture that remains resilient even when individual controls are bypassed or compromised.

The Defense-in-Depth model holds that no single control is sufficient: a firewall can be misconfigured; malware can enter through an authorized channel; a user can be socially engineered. Each additional layer — IDS watching the network, EDR watching the endpoint, firewall blocking the pivot — means an attacker must defeat multiple independent controls rather than a single point of failure. The report articulated this model in terms of the specific tools deployed during Week 11 and their collective contribution to the TitanCorp lab environment's defensive posture.

### Key Concepts

- Defense-in-Depth: layered security controls and their collective resilience
- Network layer: iptables DMZ segmentation
- Detection layer: Suricata IDS alert analysis
- Endpoint layer: Sysmon EDR process telemetry and policy enforcement
- Writing a technical defense-in-depth narrative for a professional audience

### Artifact

`Operation_Fortress_Report.md` — Defense-in-Depth report synthesizing firewall, IDS, and EDR controls deployed during Week 11

### References

NIST. (2009). *Guidelines on firewalls and firewall policy* (SP 800-41 Rev. 1). National Institute of Standards and Technology. https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final

Suricata Project. (2023). *Suricata user guide*. Open Information Security Foundation. https://suricata.readthedocs.io/en/latest/

Microsoft. (2023). *Sysmon*. Microsoft Learn. https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

---

*AaX3 · TKH IFCS Phase One · Week 11 · 2026*