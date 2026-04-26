# CLOUDNANO REMEDIATION PLAN
**Operator:** ## TOP 5 CRITICAL FIXES
*(From the 20 raw findings, select the 5 that pose the greatest ACTUAL risk. Explain your reasoning.)*

1. **#10 — Unauthenticated AWS S3 Bucket (CVSS 9.8)**
   * **Justification:** This is publicly reachable with zero authentication required and directly exposes customer PII, making both likelihood and impact maximally high. I would not choose 2. CVSS 10.0 as high priority because the air-gapped router with no physical access has maximum severity but near-zero likelihood, therefore, an attacker can't reach it.
2. **#1 — RCE in Apache Struts (CVSS 9.8)**
   * **Justification:** Remote code execution on an internet-facing server means an attacker can take full control of the system from anywhere on the internet with no internal access required.

3. **#4 — SQL Injection in Login Page (CVSS 8.3)**
   * **Justification:** The customer database portal is likely internet-facing and holds sensitive records; SQL injection here gives an attacker direct read/write access to customer data.

4. **#8 — XSS on Support Forum (CVSS 8.8)**
   * **Justification:** The support forum is a public-facing surface where customers actively interact, making it highly likely to be targeted and enabling attackers to steal session tokens or redirect users to malicious sites.

5. **#3 — Outdated PHP 5.4 on Public Marketing Blog (CVSS 7.5)**
   * **Justification:** PHP 5.4 has numerous unpatched CVEs and the marketing blog is publicly accessible, creating a realistic attack path even without a specific exploit chain identified.

