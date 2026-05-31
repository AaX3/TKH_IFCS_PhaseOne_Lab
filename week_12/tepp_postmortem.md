# TEPP Lab Postmortem — Week 12

## Phase 0: Reconnaissance

### Triage Network — 172.100.0.0/24

Three hosts were identified on the triage network subnet (172.100.0.0/24): broken_server_1 (172.100.0.11), broken_server_2 (172.100.0.12), and broken_server_3 (172.100.0.13). Reconnaissance confirmed that broken_server_1 exposed a Redis instance on port 6379/tcp with no authentication required, verified by a direct redis-cli PING returning PONG. Broken_server_2 ran vsftpd 3.0.2 on port 21/tcp, confirmed via process inspection showing the service actively listening. Broken_server_3 exposed a web root directory at /var/www/html with world-writable permissions (chmod 777), creating an unauthorized file write condition that could facilitate web shell deployment.

### Breach Network — 172.80.0.0/24

One host was identified on the breach network subnet (172.80.0.0/24): midterm_target at 172.80.0.10. The host exposed SSH on port 22/tcp running OpenSSH via an Alpine Linux container configured with PermitRootLogin enabled and password authentication active. Reconnaissance revealed the service accepted root-level login attempts, indicating the target was susceptible to credential-based brute force attack. This observation directly informed the Phase 2 approach of deploying Hydra against port 22 using a targeted wordlist.

### Exploitation Network — 172.60.0.0/24

One host was identified on the exploitation network subnet (172.60.0.0/24): capstone_target at 172.60.0.10. The host ran a Python 3.10 web application on port 80/tcp that accepted user-supplied input through an HTTP endpoint without sanitization. Pre-exploitation analysis identified that the /run route passed query parameters directly to a subprocess call, creating a command injection vulnerability. This finding established the attack vector for Phase 3: crafting a reverse shell payload delivered through the unsanitized cmd parameter.

## Phase 1: Rapid Triage

### Server 1 — 172.100.0.11

**Vulnerability Identified:**
Redis was exposed on port 6379/tcp with no authentication required. This was confirmed by running `redis-cli config get requirepass` inside the container, which returned an empty value, indicating any client could connect and issue commands without credentials.

**Remediation Commands:**
sudo docker exec broken_server_1 redis-cli config get requirepass
sudo docker exec broken_server_1 redis-cli config set requirepass "SecurePass123"
sudo docker exec broken_server_1 redis-cli config get requirepas

**Before State:**
requirepass → (empty) — no password set, unauthenticated access permitted to all Redis commands.

**After State:**
NOAUTH Authentication required — all connections now require a valid password before commands are accepted.

**Analysis:**
Redis operates by default without authentication, meaning any client that can reach port 6379 has full read and write access to the data store (NetworkChuck, 2020). In an enterprise environment, an exposed and unauthenticated Redis instance can be exploited to exfiltrate sensitive cached data, overwrite configuration values, or pivot to other internal systems. Enforcing authentication via requirepass is a foundational control that closes anonymous access as an entry point.

---

### Server 2 — 172.100.0.12

**Vulnerability Identified:**
An unauthorized vsftpd 3.0.2 FTP service was running on port 21/tcp. This was confirmed by executing `ps aux | grep vsftpd` inside the container, which returned two active vsftpd processes at PIDs 1 and 47.

**Remediation Commands:**
sudo docker exec broken_server_2 ps aux | grep vsftpd
sudo docker exec broken_server_2 kill -9 47
sudo docker exec broken_server_2 ps aux | grep vsftpd

**Before State:**
vsftpd active at PID 47 (worker) and PID 1 (supervisor), listening on port 21/tcp.

**After State:**
Container exited — vsftpd process terminated, port 21 no longer accessible.

**Analysis:**
FTP transmits both credentials and file content in plaintext over port 21, making it vulnerable to interception by any attacker with access to the same network segment (PowerCert Animated Videos, n.d.). An unauthorized FTP service running on a production server represents an unmanaged attack surface that bypasses standard access controls. In an enterprise environment, any service not explicitly authorized by security policy should be immediately terminated and removed from the system image.

---

### Server 3 — 172.100.0.13

**Vulnerability Identified:**
The directory /var/www/html was configured with world-writable permissions (chmod 777), meaning any process or user on the system could create, modify, or delete files within the web root. This was confirmed via `ls -la /var/www/` showing drwxrwxrwx and verified with `stat /var/www/html` returning Access: (0777).

**Remediation Commands:**
sudo docker exec broken_server_3 ls -la /var/www/
sudo docker exec broken_server_3 sh -c "chmod 755 /var/www/html && ls -la /var/www/"
sudo docker exec broken_server_3 stat /var/www/html

**Before State:**
Access: (0777/drwxrwxrwx) — world-readable, world-writable, and world-executable by all users and processes.

**After State:**
Access: (0755/drwxr-xr-x) — owner retains full control; group and others are restricted to read and execute only.

**Analysis:**
A world-writable web root allows any local user or compromised process to plant arbitrary files in the directory served by the web server, creating a direct path to web shell deployment and persistent remote access (NetworkChuck, 2020). In an enterprise environment, this misconfiguration could enable an attacker who has achieved limited local access to escalate their position by hosting malicious scripts through the organization's own infrastructure. Restricting permissions to 755 ensures that only authorized system owners can modify web-served content.

---

## References

NetworkChuck. (2020, July 9). *Nmap tutorial to find network vulnerabilities* [Video]. YouTube. https://www.youtube.com/watch?v=4t4kBkMsDbQ

PowerCert Animated Videos. (n.d.). *Network ports explained* [Video]. YouTube. https://www.youtube.com/watch?v=g2fT-g9PX9o