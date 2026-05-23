# FORENSIC FINDINGS REPORT (THE MALWARE AUTOPSY)

### WHO:
* [rootkit_beacon.exe, da hidden process (PID: 4444) with no visible desktop window, consistent with a remote access trojan beacon]

### WHAT:
* [Resume.exe, deleted from inode 582 in the Downloads/ directory of the FAT disk image; payload signature: malicious_payload_signature_0x992]

### WHEN:
* [2026-05-22, consistent with the provisioning date of the disk image and the timestamp of compromised_drive.dd as observed in the evidence locker]

### HOW:
* [The malware executed as a hidden background process after the victim opened Resume.exe. The file was deleted post-execution to evade detection while rootkit_beacon.exe remained active in memory with no visible window]
