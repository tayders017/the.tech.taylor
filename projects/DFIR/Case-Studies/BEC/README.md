# Business Email Compromise (BEC) Investigation

## Overview
This repository documents a simulated Business Email Compromise (BEC) investigation involving a compromised Microsoft 365 account used to conduct internal phishing and attempted financial fraud.

The objective of this investigation was to:
- Identify the initial compromise vector
- Analyze attacker activity within the tenant
- Determine impacted accounts and overall scope of compromise
- Contain unauthorized access
- Develop detection and hardening recommendations

---

## Scenario Summary

A finance department employee reported suspicious outbound emails requesting urgent wire transfers. Investigation revealed unauthorized access to the user's Microsoft 365 account originating from an overseas IP address.

The attacker:
- Established mailbox forwarding rules
- Deleted security alert emails
- Conducted internal reconnaissance
- Attempted invoice fraud via email impersonation

---

## Skills Demonstrated

- Microsoft 365 incident response
- Azure AD log analysis
- Email security investigations
- Threat hunting
- IOC analysis
- Timeline reconstruction
- Containment and recovery
- MITRE ATT&CK mapping
- Secure Access Service Edge (SASE) monitoring
- Data loss prevention (DLP) analysis

---

## Tools Used

- Microsoft Defender for Office 365
- Azure AD Sign-In Logs
- Microsoft Purview Audit Logs
- PowerShell
- KQL
- VirusTotal
- WHOIS / Passive DNS
- Forcepoint ONE Suite
  - CASB
  - SWG
  - DLP
  - ZTNA
  - SaaS security monitoring

---

## Investigation Workflow

1. Initial alert triage
2. Review Forcepoint ONE alerts and email/web activity
3. Account activity review
4. Mailbox rule analysis
5. Authentication log review
6. Threat hunting for lateral movement
7. IOC extraction and enrichment
8. Containment actions
9. Password reset + MFA enforcement
10. Post-incident hardening recommendations

See also:
* [Timeline](https://github.com/tayders017/the.tech.taylor/tree/main/projects/DFIR/Case-Studies/BEC/timeline.md)

---

## Key Findings

| Finding | Description |
|---|---|
| Initial Access | Credential phishing |
| Persistence | Mail forwarding rules |
| Defense Evasion | Deleted security notifications |
| Impact | Attempted invoice fraud |
| Data Accessed | Internal finance communications |
| Additional Findings | Suspicious SaaS access from unmanaged device |

---

## MITRE ATT&CK Mapping

| Technique | ID |
|---|---|
| Phishing | T1566 |
| Valid Accounts | T1078 |
| Email Collection | T1114 |
| Inbox Rule Manipulation | T1114.003 |
| Cloud Account Discovery | T1087 |
| Proxy / SaaS Access Abuse | T1090 |

---

## Indicators of Compromise

See:
* [IOC Analysis](https://github.com/tayders017/the.tech.taylor/tree/main/projects/DFIR/Case-Studies/BEC/ioc_analysis.md)

---

## Detection Opportunities

- Impossible travel sign-ins
- New inbox forwarding rules
- MFA disabled events
- Suspicious OAuth consent grants
- High-risk sign-in alerts
- Unmanaged device SaaS access
- Abnormal outbound email behavior
- DLP policy violations

---

## Containment Actions

- Disabled compromised account
- Revoked active sessions
- Removed mailbox rules
- Reset credentials
- Enabled Conditional Access policies
- Forced MFA registration
- Blocked malicious domains via Forcepoint ONE
- Reviewed SaaS access posture and session controls

---

## Lessons Learned

- Legacy authentication remained enabled
- MFA fatigue resistance policies were absent
- Alert tuning for mailbox rule creation was insufficient
- SaaS application visibility required additional tuning
- Conditional access policies needed stricter unmanaged device enforcement

---

## Disclaimer

This investigation is a simulated lab scenario created for educational and portfolio purposes only. No real organizational data is included (including timestamps). 
