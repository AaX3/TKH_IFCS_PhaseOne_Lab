# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 (172.88.0.10):** [1. Service Name: http 2. Version: nginx 1.14.2]
* **Host 2 (172.88.0.15):** [1. Service Name: redis 2. Version: Redis key-value store 8.6.2]
* **Host 3 (172.88.0.20):** [1. Service Name: http 2. Version: Apache httpd 2.4.66 ((Unix))]

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
* **Web Server 1 Finding:** [Nginx 1.14.2 (2018) is running on this host, an outdated version with publicly known CVEs that has not received security patches in over 8 years, making remote exploitation highly likely.]
* **Web Server 2 Finding:** [HTTP TRACE method is enabled on this Apache server, making it vulnerable to Cross-Site Tracing (XST/OSVDB-877), which allows attackers to steal session cookies and user credentials from authenticated users.]

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** [Outdated nginx 1.14.2 web server on 172.88.0.10]
* **Justification:** [This is the highest priority finding because both likelihood and impact are high; nginx 1.14.2 has been unpatched since 2018, meaning years of publicly documented CVEs and available exploit code exist for this exact version, making exploitation highly likely. If successfully exploited, an attacker could gain remote code execution on an internet-facing host, 
compromising the entire subnet.]
