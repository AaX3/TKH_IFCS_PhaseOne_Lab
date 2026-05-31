# Week 05 — Identity, Access & Active Directory
**Program:** TKH IFCS Phase One
**Sessions:** S13 · S14 · S15
**Week Topic:** Security policy design, IAM & MFA · Group Policy & access control enforcement · Linux-Windows domain join & identity unification

---

## Session 13 — Security Policy Design, IAM & MFA

### Summary

Session 13 introduced enterprise Identity and Access Management (IAM) — the discipline governing who can access what, under what conditions, and with what level of verification. The session centered on Windows Active Directory as the dominant enterprise identity platform, and PowerShell as the tool for scripting and automating identity operations at scale.

The practical work involved writing `onboard_engineers.ps1` — a PowerShell script automating the process of provisioning new user accounts, assigning them to the appropriate security groups, and enforcing MFA enrollment as part of the onboarding workflow. Automating onboarding ensures that every new user starts in a known, policy-compliant state rather than relying on manual steps that can be skipped or misconfigured under time pressure.

### Key Concepts

- Identity and Access Management (IAM) principles
- Active Directory: users, groups, organizational units (OUs)
- Multi-factor authentication (MFA) enforcement
- PowerShell for AD user provisioning and policy automation
- Principle of least privilege applied to identity

### Artifact

`onboard_engineers.ps1` — PowerShell script automating user provisioning with MFA enforcement

### References

Microsoft. (2023). *Active Directory documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services

Microsoft. (2023). *Get started with PowerShell*. Microsoft Learn. https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started

---

## Session 14 — Group Policy & Access Control Enforcement

### Summary

Session 14 focused on Group Policy Objects (GPOs) — the mechanism by which Windows domain administrators enforce security configuration across every machine in the domain simultaneously. Rather than hardening each workstation individually, a GPO defines the desired state and Active Directory pushes it to every joined machine automatically. This is the Windows equivalent of the bash hardening scripts written in Week 01, operating at enterprise scale.

The session involved auditing existing GPO configurations to identify gaps in access control enforcement — settings that were missing, misconfigured, or too permissive — and documenting the findings in `gpo_audit.txt`. The audit perspective matters: understanding how Group Policy works is equally valuable for defenders enforcing it and for attackers seeking to understand what controls they will encounter in a real environment.

### Key Concepts

- Group Policy Objects (GPOs): scope, inheritance, and enforcement
- Common security GPOs: password policy, account lockout, screen lock, USB restriction
- GPO auditing and gap analysis
- Domain-level vs. OU-level policy application
- `gpresult` and `rsop.msc` for policy inspection

### Artifact

`gpo_audit.txt` — structured audit of Group Policy configurations documenting enforcement state and identified gaps

### References

Microsoft. (2023). *Group Policy overview*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview

Microsoft. (2023). *Active Directory documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services

---

## Session 15 — Linux-Windows Domain Join & Identity Unification

### Summary

Session 15 demonstrated Linux-Windows identity integration — joining an Ubuntu Server to a Windows Active Directory domain so that AD user accounts can authenticate directly on the Linux machine. This is a common enterprise configuration that eliminates the need for separate local accounts on each Linux host, centralizes identity management in Active Directory, and allows GPO-level controls to extend to Linux systems.

The domain join process was completed using standard tooling, and the configuration was verified by authenticating to the Linux system using Active Directory credentials. The completed unified identity state was captured as `unified_identity.png`. This session made concrete the concept that identity is the new perimeter: in a modern enterprise, controlling who can authenticate — and from where, and with what factors — is more foundational than controlling which ports are open.

> **Note:** Technical difficulties were encountered during parts of this week's lab environment setup. The concepts introduced here are reinforced and applied in the access control and hardening work of subsequent weeks.

### Key Concepts

- Linux-Windows domain join using `realmd` and `sssd`
- Kerberos authentication across OS boundaries
- Centralized identity management via Active Directory
- Identity as a security perimeter
- Cross-platform account verification

### Artifact

`unified_identity.png` — screenshot confirming successful Linux-Windows domain join and AD authentication

### References

Microsoft. (2023). *Active Directory documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services

Ubuntu. (2023). *Active Directory integration*. Ubuntu Server Guide. https://ubuntu.com/server/docs/service-sssd-ad

---

*AaX3 · TKH IFCS Phase One · Week 05 · 2026*