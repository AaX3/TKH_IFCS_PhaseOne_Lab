# Week 08 — Exploitation & Post-Exploitation
**Program:** TKH IFCS Phase One
**Sessions:** S22 · S23 · S24
**Week Topic:** Exploitation frameworks & gaining a shell · Web application attacks & traffic interception · SQL injection & XSS session theft

---

## Session 22 — Exploitation Frameworks & Gaining a Shell

### Summary

Session 22 introduced the Metasploit Framework — the industry-standard exploitation platform used by both professional penetration testers and threat actors — within a fully authorized lab environment. The session moved from the reconnaissance output of Week 07 into active exploitation: taking a known vulnerability identified during scanning and using it to gain unauthorized access to a target system.

A known CVE was selected from the scan findings and a corresponding Metasploit module was configured with the target IP, payload type, and listener settings. The module was executed, delivering the payload to the target and establishing an interactive shell session. From within that shell, the target system was explored: user accounts, running processes, sensitive files, and network connections were enumerated. The privilege escalation path from the initial low-privilege shell to elevated access was documented step-by-step in `escalation_path.txt`, and successful exploitation was captured as `exploit_verification.png`.

This session established the exploitation lifecycle as a mental model: reconnaissance → vulnerability identification → module selection → payload delivery → session handling → post-exploitation enumeration.

> **Note:** A Day 3 screenshot confirming the final submission state could not be transferred from the VM to VS Code Explorer at time of commit. This artifact will be appended when the file transfer issue is resolved.

### Key Concepts

- Metasploit Framework architecture: modules, payloads, handlers, sessions
- Module types: exploit, auxiliary, post, payload
- Payload types: staged vs. stageless, Meterpreter vs. shell
- `msfconsole` workflow: `search`, `use`, `set`, `run`
- Post-exploitation enumeration: users, processes, files, network
- Privilege escalation path documentation

### Artifacts

`escalation_path.txt` · `exploit_verification.png`

### References

HackerSploit. (2021, May 6). *Metasploit framework tutorial* [Video]. YouTube. https://www.youtube.com/watch?v=8lR27r8Y_ik

Offensive Security. (2023). *Metasploit unleashed*. Offensive Security. https://www.offsec.com/metasploit-unleashed/

---

## Session 23 — Web Application Attacks & Traffic Interception

### Summary

Session 23 shifted focus from network-layer exploitation to web application attacks, introducing Burp Suite as the primary tool for intercepting and manipulating HTTP/HTTPS traffic between a browser and a web application. The proxy intercept model was configured — all browser traffic routed through Burp's listener — allowing each request to be paused, inspected, and modified before it reaches the server.

The session demonstrated how web application attacks fundamentally depend on the ability to manipulate requests that the application trusts: changing parameter values, replaying requests with modified headers, and injecting payloads into fields the developer assumed would contain clean user input. Burp Suite's Repeater and Intercept features were used to craft and replay modified requests, building an understanding of the request-response cycle as an attack surface.

> **Note:** The terminal-only VM environment (no GUI) required curl-based substitutes for certain Burp Suite GUI workflows. This constraint was documented and alternative approaches were applied where needed.

### Key Concepts

- HTTP/HTTPS request-response cycle as an attack surface
- Burp Suite proxy: intercept, forward, drop, modify
- Repeater for manual request crafting and replay
- Parameter tampering and header manipulation
- Web application trust boundaries

### References

PortSwigger. (2023). *Burp Suite documentation*. PortSwigger. https://portswigger.net/burp/documentation

PortSwigger. (2023). *Web security academy*. PortSwigger. https://portswigger.net/web-security

---

## Session 24 — SQL Injection & XSS Session Theft

### Summary

Session 24 introduced two of the most impactful web application vulnerability classes — SQL injection and Cross-Site Scripting — and demonstrated how they can be chained together in a real attack sequence. SQLi was used to extract database contents by injecting malicious SQL syntax into input fields that the application passed directly to the database without sanitization. XSS was used to inject JavaScript payloads into persistent application fields, enabling session cookie theft from any user whose browser rendered the affected page.

The session established the exploitation chain: SQLi provides database access and potentially credential exposure; XSS provides client-side code execution and session hijacking. Together, they represent a complete account takeover pathway that bypasses authentication entirely. Both attack classes stem from the same root cause — insufficient input validation — making input sanitization and parameterized queries the foundational defenses for the entire web application attack surface.

### Key Concepts

- SQL injection: syntax, boolean-based, union-based, error-based
- Parameterized queries as the primary SQLi defense
- Cross-Site Scripting (XSS): reflected vs. stored vs. DOM-based
- Session cookies: `HttpOnly`, `Secure` flags and their absence
- Attack chaining: SQLi → credential extraction → XSS → session theft

### References

PortSwigger. (2023). *SQL injection*. Web Security Academy. https://portswigger.net/web-security/sql-injection

OWASP. (2023). *Cross-site scripting (XSS)*. OWASP Foundation. https://owasp.org/www-community/attacks/xss/

HackerSploit. (2022, March 14). *Cross-site scripting (XSS) explained* [Video]. YouTube. https://www.youtube.com/watch?v=EoaDgUgS6QA

---

*AaX3 · TKH IFCS Phase One · Week 08 · 2026*