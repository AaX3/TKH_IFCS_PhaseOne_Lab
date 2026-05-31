# Week 03 — Python for Security
**Program:** TKH IFCS Phase One
**Sessions:** S07 "The Sentry" · S08 "The Paper Trail" · S09 "The Conductor" · TLAB-03 "Operation Automated Hunt"
**Week Topic:** Security scripting & service enumeration · System interrogation with Python · Network scripting & TCP port connection

---

## Session 07 — "The Sentry": Security Scripting & Service Enumeration

### Summary

Session 07 introduced Python as a security automation language, beginning with the foundational concept that every firewall, every access control system, and every intrusion detection tool is built on the same logic gates a beginner writes in their first script. The micro-lab built a simple identity checker using Python lists and conditional logic — demonstrating that `if current_user in users` is the conceptual ancestor of every allowlist in production security infrastructure.

The main lab built `port_check.py` using Python's `socket` library. The script defined a list of target IP addresses, looped through each one using a `for` loop, opened a TCP socket connection to port 22 (SSH), and reported whether the port was open or closed based on the return code of `connect_ex()`. The script demonstrated three core automation principles: looping over a list of targets eliminates manual repetition; a 1-second timeout prevents the script from hanging indefinitely; and closing the socket after each check maintains clean resource management. The completed script was committed to GitHub and submitted via `session-submit`.

### Key Concepts

- Python `socket` library for TCP connection testing
- `for` loops as the "efficiency engine" of security automation
- `socket.connect_ex()` return codes: 0 = open, non-zero = closed
- Socket timeout configuration to prevent blocking
- Access control logic: allowlists and conditional gates

### Artifact

`port_check.py` — multi-target TCP port scanner using Python socket programming

### References

Real Python. (2022, March 1). *Python sockets tutorial* [Video]. YouTube. https://www.youtube.com/watch?v=LnKoncbQBsM

NetworkChuck. (2021, July 22). *Python for cybersecurity* [Video]. YouTube. https://www.youtube.com/watch?v=4N4Q576i3zA

---

## Session 08 — "The Paper Trail": System Interrogation with Python

### Summary

Session 08 introduced Python file I/O — the mechanism by which scripts read from and write to files — and applied it directly to a forensic use case: parsing authentication logs for evidence of brute-force attacks. The micro-lab established the `with open()` context manager as the correct pattern for file access, ensuring the file is properly closed even if the script crashes. The deliberate triggering of a `FileNotFoundError` demonstrated why production security tools must handle missing files gracefully using `try/except` rather than crashing silently.

The main lab built `brute_detector.py` — a script that opens `auth_audit.log` in read mode, loops through every line using a `for` loop, checks each line for the signature string `"Failed password"`, writes matching lines to a clean output report (`brute_report.txt`), and increments a counter tracking the total number of attack signatures extracted. The final print statement reports the count. This script embodies a core forensic principle: if an event is not recorded, it never happened. The script's output is the beginnings of a chain of custody document.

### Key Concepts

- Python file I/O: `open()`, read mode (`"r"`), write mode (`"w"`)
- `with open()` context manager for safe file handling
- `try/except` for graceful error handling
- String matching with `in` for log signature detection
- Counter variables and final summary reporting

### Artifact

`brute_detector.py` — authentication log parser that extracts failed login signatures and exports a structured threat report

### References

Real Python. (2021, November 15). *Reading and writing files in Python* [Video]. YouTube. https://www.youtube.com/watch?v=Uh2ebFW8OYM

Red Hat. (2022, January 18). *Linux file permissions explained*. Red Hat. https://www.redhat.com/en/blog/linux-file-permissions-explained

---

## Session 09 — "The Conductor": Network Scripting & TCP Port Connection

### Summary

Session 09 introduced Python's `subprocess` module — the mechanism by which a Python script can reach outside itself and execute system commands, capturing their output as text. The micro-lab used `subprocess.run(["uptime"], capture_output=True, text=True)` to demonstrate the pattern: wrap the command in a list, capture stdout, and use `text=True` to receive human-readable output instead of raw bytes.

The main lab built `system_auditor.py` — a script that runs `ps aux` via subprocess to capture the full running process list, searches the output for the string `"unauthorized_cryptominer"`, and if found, constructs a Python dictionary containing the event type, severity, and process name, then exports it as formatted JSON using `json.dump`. The `import json` requirement alongside `import subprocess` established the pattern of combining multiple libraries to produce machine-readable security alerts — the same pattern used in production SIEM integrations.

The session's reflection (`s09reflection.md`) documented the conceptual connection between subprocess-based interrogation and real SOC tooling.

### Key Concepts

- Python `subprocess.run()` for executing system commands
- `capture_output=True` and `text=True` for readable stdout
- `ps aux` process list interrogation
- Python dictionaries as structured data containers
- `json.dump()` for machine-readable alert export
- `import json` and `import subprocess` as a combined security toolkit

### Artifacts

`system_auditor.py` · `s09reflection.md`

### References

Real Python. (2022, January 10). *Python subprocess module* [Video]. YouTube. https://www.youtube.com/watch?v=2Fp1N6dof0Y

NetworkChuck. (2021, July 22). *Python for cybersecurity* [Video]. YouTube. https://www.youtube.com/watch?v=4N4Q576i3zA

---

## TLAB-03 — "Operation Automated Hunt"

### Summary

TLAB-03 was an independent take-home lab synthesizing the skills from all three sessions of Week 03 into a single automated incident response pipeline. The scenario: a simulated brute-force attack had occurred against a TitanCorp server, and the task was to write a Python script that reads the security logs, extracts the attacking IP addresses, and exports a structured JSON threat report — operating independently, without guided steps.

`incident_response.py` was written from scratch. `subprocess.run()` executed a `grep "Failed password"` command against `/var/log/titan_sim/auth_sim.log`, capturing all matching lines as a single block of text. The block was split on newlines into a list of individual lines, and a `for` loop processed each line — extracting the attacker IP address by splitting on spaces and selecting index 10, the field position of the IP in standard syslog auth entries. Each extracted IP was appended to an `attacker_ips` list. The final dictionary structured the alert with an `alert_type` of `"Brute Force"` and the complete IP list, which was then exported to `threat_report.json` via `json.dump()`.

This lab demonstrated the full automated SOC detection pipeline: ingest → parse → extract → structure → export.

### Key Concepts

- Full pipeline automation: subprocess → file parsing → IP extraction → JSON export
- `grep` via subprocess for targeted log filtering
- String splitting for structured field extraction from syslog format
- List construction and JSON serialization
- Independent operation under mission parameters

### Artifacts

`incident_response.py` · `threat_report.json`

### References

NetworkChuck. (2021, July 22). *Python for cybersecurity* [Video]. YouTube. https://www.youtube.com/watch?v=4N4Q576i3zA

Real Python. (2022, March 1). *Python sockets tutorial* [Video]. YouTube. https://www.youtube.com/watch?v=LnKoncbQBsM

Red Hat. (2022, January 18). *Linux file permissions explained*. Red Hat. https://www.redhat.com/en/blog/linux-file-permissions-explained

---

*AaX3 · TKH IFCS Phase One · Week 03 · 2026*