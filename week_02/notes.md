# Week 02 — Networking & Protocol Analysis
**Program:** TKH IFCS Phase One
**Sessions:** S04 · S05 · S06
**Week Topic:** OSI model & TCP/IP fundamentals · IP subnetting & CIDR notation · DNS & protocol interrogation

---

## Session 04 — OSI Model & TCP/IP Fundamentals

### Summary

Session 04 built the networking foundation that underlies every security operation in the program. The OSI model's seven layers were examined not as an abstract framework but as a diagnostic map: when something breaks or is being attacked, knowing which layer the problem lives on determines which tool you reach for. TCP/IP's four-layer model was mapped against the OSI stack, and the behavior of packets as they travel from application to wire was traced.

The practical work centered on Wireshark — capturing live network traffic and dissecting a TLS handshake packet by packet. The handshake sequence (ClientHello → ServerHello → Certificate → Key Exchange → Finished) was observed in real time, revealing how two systems negotiate encryption before any application data is exchanged. This session made visible the mechanics that are normally invisible to users and established Wireshark as a core analysis tool for understanding what is actually moving across a network.

### Key Concepts

- OSI model: 7 layers and their security relevance
- TCP/IP four-layer model and packet encapsulation
- Wireshark: capture filters, protocol dissection, packet inspection
- TLS handshake: ClientHello, ServerHello, certificate exchange, session key negotiation
- TCP three-way handshake: SYN → SYN-ACK → ACK

### Artifact

Wireshark TLS handshake capture — annotated packet capture documenting handshake sequence

### References

PowerCert Animated Videos. (2018, December 5). *OSI model explained* [Video]. YouTube. https://www.youtube.com/watch?v=vv4y_uOneC0

NetworkChuck. (2021, May 14). *Free CCNA — OSI model* [Video]. YouTube. https://www.youtube.com/watch?v=We3qE8phJWA

LabEx. (n.d.). *Network basics*. LabEx. https://labex.io/lesson/network-basics

---

## Session 05 — IP Subnetting & CIDR Notation

### Summary

Session 05 focused on IP addressing and subnetting — the skill that determines how network traffic is segmented, routed, and controlled. CIDR (Classless Inter-Domain Routing) notation was introduced as the standard method for expressing network ranges, and binary-to-decimal IP address conversion was practiced to build intuition for how subnet masks carve address space into usable ranges.

The practical output was a subnetting scheme designed to logically segment a simulated enterprise network — separating web-facing services, internal databases, and administrative systems into distinct subnets. This segmentation is a direct security control: an attacker who compromises a host in one subnet cannot automatically reach hosts in another if the routing and firewall rules are properly configured. This concept recurs directly in Week 11's iptables DMZ work.

### Key Concepts

- IPv4 address structure and binary representation
- Subnet masks and CIDR notation (`/24`, `/16`, `/8`)
- Network address, broadcast address, usable host range calculation
- Network segmentation as a security control
- Subnetting a larger address space into smaller segments

### Artifact

CIDR subnetting scheme — network diagram and address table documenting the segmented lab topology

### References

PowerCert Animated Videos. (2019, June 12). *Subnetting mastery* [Video]. YouTube. https://www.youtube.com/watch?v=s_Ntt6eTn94

NetworkChuck. (2019, October 28). *Subnetting is simple* [Video]. YouTube. https://www.youtube.com/watch?v=4N4Q576i3zA

---

## Session 06 — DNS & Protocol Interrogation

### Summary

Session 06 examined DNS — the protocol that translates human-readable domain names into IP addresses — and demonstrated how it can be interrogated both for legitimate network diagnostics and as a reconnaissance tool. DNS query types (A, AAAA, MX, NS, TXT, CNAME) were explored, and command-line tools including `dig`, `nslookup`, and `host` were used to query DNS records directly. The behavior of DNS over UDP port 53 was observed, and the absence of encryption in standard DNS was noted as a significant privacy and security consideration.

Protocol-level analysis was extended to other common services using tools like `netstat` and `ss` to inspect active connections and listening ports on the local system. Findings from all protocol interrogation activities were compiled in `protocol_audit.txt`, establishing the habit of documenting network observations in a structured, reviewable format.

### Key Concepts

- DNS resolution process: recursive vs. authoritative queries
- DNS record types: A, AAAA, MX, NS, TXT, CNAME, PTR
- `dig`, `nslookup`, `host` for DNS interrogation
- `netstat` and `ss` for active connection enumeration
- Protocol auditing as a network visibility practice

### Artifact

`protocol_audit.txt` — structured documentation of DNS queries, record findings, and active connection state

### References

PowerCert Animated Videos. (2019, August 14). *DNS explained* [Video]. YouTube. https://www.youtube.com/watch?v=72snZctFFtA

NetworkChuck. (2021, February 4). *DNS — the internet's phone book* [Video]. YouTube. https://www.youtube.com/watch?v=LnKoncbQBsM

---

*AaX3 · TKH IFCS Phase One · Week 02 · 2026*