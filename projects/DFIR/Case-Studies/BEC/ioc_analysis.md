# IOC Analysis

## Overview

This document contains indicators of compromise (IOCs) identified during the BEC investigation.

The indicators below were collected from:
- Azure AD logs
- Microsoft Defender alerts
- Forcepoint ONE telemetry
- Email header analysis
- Threat intelligence enrichment

---

# Malicious IP Addresses

| IOC | Description |
|---|---|
| 110.191.xx.xx | Foreign login source associated with residential proxy service |
| 96.213.xx.xx | Suspicious OAuth activity |
| 45.82.xx.xx | Web session associated with attacker mailbox access |

---

# Malicious Domains

| Domain | Purpose |
|---|---|
| microsoft.authsecure[.com] | Credential phishing |
| office365-loginverify[.com] | Fabricated authentication portal |
| securemail.msft.auth[.net] | Redirect infrastructure |

---

# Suspicious User Agents

| User Agent | Notes |
|---|---|
| python-requests/2.21 | Automated OAuth interaction |
| Mozilla/5.0 (Linux; Android 9) | Unusual device profile for affected user |

---

# Email Artifacts

## Malicious Subject Lines

```
URGENT: Updated Vendor Payment Instructions
ACTION REQUIRED: Invoice Processing Delay
Microsoft 365 Password Expiration Notice
```

---

## Malicious Attachment Names

```
Invoice_Review_Required.pdf.html
Payment_Confirmation.htm
M365_Security_Update.html
```

---

# Threat Intelligence Correlation

## MITRE ATT&CK Techniques

| Technique | ID |
|---|---|
| Phishing | T1566 |
| Valid Accounts | T1078 |
| Email Collection | T1114 |
| Inbox Rule Manipulation | T1114.003 |

---

## Threat Intelligence Findings

The phishing infrastructure showed overlap with known BEC campaigns targeting:
- Financial services organizations
- SaaS providers
- Enterprise Microsoft 365 tenants

Several domains resolved to infrastructure previously associated with credential harvesting activity.

---

# Forcepoint ONE Findings

Forcepoint ONE telemetry identified:
- Access attempts from unmanaged devices
- Abnormal SaaS authentication patterns
- Suspicious outbound email behavior
- Risky session activity inconsistent with baseline user behavior

---

# Detection Opportunities

## Recommended Detections

- Impossible travel sign-ins
- OAuth application consent monitoring
- Inbox forwarding rule creation alerts
- High-risk authentication alerts
- Unmanaged device SaaS access alerts

---

# Recommended Blocking Actions

## Domains
- Block phishing domains at SWG/email gateway level

## IP Addresses
- Add confirmed malicious IPs to deny lists where appropriate

## OAuth Applications
- Remove unauthorized consent grants
- Restrict user OAuth approval permissions

---

# Conclusion

The indicators identified during this investigation strongly support a credential phishing-driven BEC campaign leveraging legitimate Microsoft 365 access for persistence and internal fraud attempts.
