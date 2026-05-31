# Week 01 — Linux Fundamentals
**Program:** TKH IFCS Phase One
**Sessions:** S01 · S02 · S03
**Week Topic:** Filesystem navigation & enumeration · File permission hardening & security automation · Stream editing & log parsing

---

## Session 01 — Filesystem Navigation & Enumeration

### Summary

Session 01 established the Ubuntu Server VM as the primary working environment for the program. Using VS Code Remote-SSH to access the terminal-only machine, the Linux filesystem hierarchy was explored and enumerated using foundational CLI commands. Directory structure was navigated from the root (`/`) downward, with attention paid to security-relevant paths including `/etc`, `/var/log`, and `/home`. The `ls`, `cd`, `pwd`, `find`, and `cat` commands were used to locate and inspect files of interest. Findings from the enumeration — including notable files, directory permissions, and potential points of exposure — were recorded in `discovery.txt`.

This session introduced the practitioner mindset of treating every filesystem as a source of intelligence: what files exist, who owns them, what permissions they carry, and what they reveal about the system's configuration and history.

### Key Concepts

- Linux filesystem hierarchy (`/etc`, `/var`, `/home`, `/tmp`, `/root`)
- File and directory enumeration using `ls -la`, `find`, `cat`, `less`
- Navigating absolute vs. relative paths
- Reading system files as a first-responder triage technique

### Artifact

`discovery.txt` — enumeration findings documenting directory structure, notable files, and observed permission states

### References

NetworkChuck. (2021, January 7). *Linux for hackers* [Video]. YouTube. https://www.youtube.com/watch?v=VbEx7B_PTOE

TryHackMe. (2021, March 5). *Linux fundamentals* [Video]. YouTube. https://www.youtube.com/watch?v=We3qE8phJWA

LabEx. (n.d.). *The shell*. LabEx. https://labex.io/lesson/the-shell

---

## Session 02 — File Permission Hardening & Security Automation

### Summary

Session 02 focused on Linux file permission architecture and its role as a first line of defense. The permission model — owner, group, and other — was examined through the lens of least privilege: every file and process should have only the access it needs to function, nothing more. `chmod` and `chown` were used to audit and correct insecure permission states on system files and directories. A bash script (`harden.sh`) was then written to automate these hardening steps, enabling repeatable enforcement without manual intervention.

The automation angle is significant for a security practitioner: a hardening checklist that lives only in someone's head is a single point of failure. A script that enforces the same configuration every time removes human error from the equation and creates a documented, auditable artifact.

### Key Concepts

- Linux permission model: read (4), write (2), execute (1)
- `chmod` symbolic and octal notation
- `chown` for ownership reassignment
- Principle of least privilege
- Bash scripting for security automation

### Artifact

`harden.sh` — bash script automating file permission hardening across target paths

### References

NetworkChuck. (2021, January 14). *Linux for hackers part 2* [Video]. YouTube. https://www.youtube.com/watch?v=42iQKuQodW4

Red Hat. (2022, January 18). *Linux file permissions explained*. Red Hat. https://www.redhat.com/en/blog/linux-file-permissions-explained

---

## Session 03 — Stream Editing & Log Parsing

### Summary

Session 03 introduced the command-line text processing tools that security analysts use daily to extract signal from noisy system logs. `grep` was used to search for specific patterns — such as failed login attempts or suspicious process names — within large log files. `sed` was used to transform and clean log output, and `awk` was used to extract specific fields (such as IP addresses or timestamps) from structured log lines. These tools were chained together using pipes (`|`) to build one-liner workflows capable of parsing thousands of lines of log data in seconds.

The practical output was `bash_onliners.sh` — a collection of documented one-liners demonstrating real log parsing scenarios. This session established the pattern of treating raw logs as structured data sources and CLI pipelines as lightweight forensic tools, a skill that reappears directly in Week 03's Python scripting and Week 10's DFIR sessions.

### Key Concepts

- `grep` for pattern matching and log filtering
- `sed` for stream substitution and text transformation
- `awk` for field extraction from structured output
- Pipe chaining (`|`) for multi-stage data processing
- Log files as forensic evidence sources

### Artifact

`bash_onliners.sh` — documented collection of stream editing and log parsing one-liners

### References

NetworkChuck. (2020, October 15). *Linux commands for beginners* [Video]. YouTube. https://www.youtube.com/watch?v=_TlK0-5EJ-Y

RoboJackets. (2019, September 3). *Intro to Git and GitHub* [Video]. YouTube. https://www.youtube.com/watch?v=RGOj5yH7evk

LabEx. (n.d.). *The shell*. LabEx. https://labex.io/lesson/the-shell

---

*AaX3 · TKH IFCS Phase One · Week 01 · 2026*