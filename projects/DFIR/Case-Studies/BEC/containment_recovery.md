# Containment and Recovery Actions

## Overview

This document outlines the containment, eradication, and recovery actions performed during the BEC investigation.

---

# Immediate Containment Actions

## Account Security

### Compromised User Account
Actions performed:
- Disabled account temporarily
- Forced password reset
- Revoked active Azure AD sessions
- Revoked refresh tokens
- Re-registered MFA methods

---

## Mailbox Security

### Inbox Rules
Removed malicious:
- Auto-forwarding rules
- Hidden mailbox rules
- Suspicious delegated access permissions

### Email Review
Reviewed:
- Outbound phishing attempts
- Deleted items folder
- Sent items activity
- Mail forwarding configuration

---

# OAuth Containment

## Suspicious OAuth Application

Actions performed:
- Revoked user consent
- Disabled malicious application
- Reviewed enterprise application permissions
- Restricted future user consent permissions

---

# Forcepoint ONE Response Actions

## SaaS Session Controls

Actions performed:
- Terminated suspicious cloud sessions
- Blocked risky unmanaged device access
- Reviewed CASB alerts for related accounts
- Investigated abnormal SaaS activity

## SWG/DLP Controls

Implemented:
- Domain blocking for phishing infrastructure
- DLP monitoring for financial communications
- Enhanced web access restrictions

---

# Tenant-Wide Threat Hunting

## Investigative Queries

Threat hunting focused on:
- Additional inbox forwarding rules
- Similar OAuth application grants
- Impossible travel events
- High-risk sign-ins
- Shared IOC matches

---

# Recovery Activities

## User Recovery

Completed:
- Verified account ownership
- Restored secure mailbox access
- Re-enabled account access
- Educated user on phishing indicators

---

# Security Improvements

## Identity Hardening

Implemented:
- Conditional Access policy updates
- MFA enforcement improvements
- Legacy authentication blocking
- Risk-based sign-in monitoring

---

## Monitoring Improvements

Enhanced detection coverage for:
- Mailbox rule creation
- OAuth abuse
- Suspicious sign-ins
- Internal phishing attempts
- SaaS access anomalies

---

# Post-Incident Recommendations

## Recommended Actions

- Enforce phishing-resistant MFA
- Restrict OAuth consent permissions
- Implement stronger session controls
- Increase mailbox auditing retention
- Conduct additional phishing awareness training

---

# Final Incident Status

| Category | Status |
|---|---|
| Containment | Successful |
| Persistence Removed | Confirmed |
| Additional Impacted Accounts | None Identified |
| Monitoring | Enabled |
| Recovery | Completed |

---

# Conclusion

Containment and recovery operations successfully removed attacker access, eliminated persistence mechanisms, and restored secure user operations within the Microsoft 365 environment.
