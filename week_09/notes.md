# Week 09 — Exploitation & Post-Exploitation (Continued)
**Program:** TKH IFCS Phase One
**Sessions:** S25 · S26 · S27 "The Invisible Logic" · TLAB-09 "Operation Omni-Portal"
**Week Topic:** BOLA/IDOR exploitation · Business logic abuse · Chained web application attacks

---

## Session 25 — API Security & Access Control Concepts

### Summary

Session 25 introduced the API security layer as a distinct attack surface from the traditional web application front end. Modern applications increasingly expose their functionality through APIs — and those APIs carry the same vulnerability classes as any other code, often with less visibility and less rigorous testing. The session covered how APIs communicate, how authentication tokens are passed in headers, and how the absence of proper server-side authorization checks creates exploitable conditions even when the front end hides or disables the relevant UI elements.

The key concept introduced was that client-side controls are not security controls. Hiding a button, disabling a field, or removing a menu item does not prevent a determined user from sending the underlying API request directly. True access control must be enforced on the server side, on every request, regardless of what the client presents.

### Key Concepts

- REST API architecture: endpoints, methods, headers, status codes
- Authentication vs. authorization: verifying identity vs. verifying permission
- Client-side controls as non-controls
- API testing methodology: enumerate endpoints, manipulate parameters, test authorization
- Token-based authentication: Bearer tokens, JWTs

### References

OWASP. (2023). *OWASP API security top 10*. OWASP Foundation. https://owasp.org/www-project-api-security/

PortSwigger. (2023). *API testing*. Web Security Academy. https://portswigger.net/web-security/api-testing

---

## Session 26 — Business Logic Exploitation

### Summary

Session 26 covered business logic vulnerabilities — a class of flaws that exist not in the code's syntax or library dependencies but in the assumptions the developer made about how users would interact with the application. A business logic flaw cannot be caught by a generic vulnerability scanner because it requires understanding what the application is supposed to do and identifying where the actual behavior diverges from the intended behavior.

The session demonstrated examples such as: price manipulation by modifying quantity or discount fields in requests; workflow bypass by skipping steps the application assumes will happen in sequence; and authorization bypass by submitting requests to endpoints the front end never links to. These vulnerabilities require the same active curiosity and manual testing methodology introduced in Week 08's Burp Suite sessions — automated tools alone cannot find them.

### Key Concepts

- Business logic flaws: definition and why scanners miss them
- Price and quantity manipulation via parameter tampering
- Workflow sequencing assumptions and bypass techniques
- Forced browsing: accessing endpoints not linked in the UI
- Manual testing methodology for logic flaws

### References

PortSwigger. (2023). *Business logic vulnerabilities*. Web Security Academy. https://portswigger.net/web-security/logic-flaws

OWASP. (2023). *Testing for business logic errors*. OWASP Testing Guide. https://owasp.org/www-project-web-security-testing-guide/

---

## Session 27 — "The Invisible Logic": BOLA/IDOR

### Summary

Session 27 ("The Invisible Logic") focused on Broken Object Level Authorization (BOLA) — ranked the number one API vulnerability by OWASP — and its closely related cousin, Insecure Direct Object Reference (IDOR). Both describe the same fundamental failure: an application verifies that a user is authenticated but fails to verify whether that authenticated user is authorized to access the specific object they are requesting.

The practical attack involved identifying an API endpoint that accepted a user or resource ID as a parameter — for example, `/api/user/1042/profile` — and systematically incrementing or modifying that ID to access records belonging to other users. A brute-force loop enumerated valid IDs, and each successful response confirmed that the application was returning data it should have refused. API behavior across the enumeration was logged in `api_audit.log` and the full assessment was written up in `OmniPortal_Assessment.md`.

### Key Concepts

- BOLA (Broken Object Level Authorization) and IDOR: definitions and distinction
- Object ID enumeration: sequential integers, UUIDs, encoded strings
- Authorization failure modes: missing check, client-side check only, reference-based trust
- OWASP API Security Top 10: API1:2023 — Broken Object Level Authorization
- Brute-force enumeration for ID discovery

### Artifacts

`OmniPortal_Assessment.md` · `api_audit.log`

### References

OWASP. (2023). *OWASP API security top 10*. OWASP Foundation. https://owasp.org/www-project-api-security/

PortSwigger. (2023). *Insecure direct object references (IDOR)*. Web Security Academy. https://portswigger.net/web-security/access-control/idor

---

## TLAB-09 — "Operation Omni-Portal"

### Summary

TLAB-09 ("Operation Omni-Portal") was the week's independent take-home lab, chaining all three web attack classes from Weeks 08 and 09 into a single continuous exploitation sequence against a purpose-built vulnerable application. The lab required operating independently across three sequential phases.

**Phase 1 — SQL Injection:** The login form was bypassed entirely using the payload `admin'--`, which injected a comment character into the SQL query, causing the password validation condition to be ignored. Authentication was achieved without valid credentials.

**Phase 2 — Stored XSS:** A JavaScript payload was injected into a persistent application field — one that is rendered back to any user who views the affected page. This established a persistent attack vector: every future visitor to that page would execute the injected script in their browser, enabling session cookie theft or browser-based actions performed in their context.

**Phase 3 — BOLA:** Authenticated as the initial user, API calls were made with manipulated resource IDs to access data belonging to other users. The application returned those records without performing any authorization check beyond confirming that a valid session token was present.

XSS payloads were documented in `xss_payloads.txt`, SQLi findings in `sqli_report.txt`, and the full chained exploitation sequence in `OmniPortal_Assessment.md`.

### Key Concepts

- Chained exploitation: SQLi → Stored XSS → BOLA as a sequential attack
- `admin'--` SQL comment injection for authentication bypass
- Stored XSS persistence: payload survives across sessions and affects all viewers
- BOLA exploitation via API parameter manipulation after authentication
- Multi-phase attack documentation

### Artifacts

`OmniPortal_Assessment.md` · `sqli_report.txt` · `xss_payloads.txt` · `api_audit.log`

### References

PortSwigger. (2023). *SQL injection*. Web Security Academy. https://portswigger.net/web-security/sql-injection

OWASP. (2023). *Cross-site scripting (XSS)*. OWASP Foundation. https://owasp.org/www-community/attacks/xss/

OWASP. (2023). *OWASP API security top 10*. OWASP Foundation. https://owasp.org/www-project-api-security/

---

*AaX3 · TKH IFCS Phase One · Week 09 · 2026*