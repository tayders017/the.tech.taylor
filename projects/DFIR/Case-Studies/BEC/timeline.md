# Investigation Timeline

## Incident Summary

This timeline documents the sequence of events identified during the Business Email Compromise (BEC) investigation involving unauthorized access to a Microsoft 365 account.

---

## Timeline of Events

| Timestamp (UTC) | Event |
|---|---|
| 2019-12-13 08:12 | User received phishing email impersonating Microsoft 365 password expiration notice |
| 2019-12-13 08:17 | User submitted credentials to spoofed login page |
| 2019-12-13 08:19 | Successful Azure AD sign-in from foreign IP address |
| 2019-12-13 08:21 | MFA prompt approved by compromised user |
| 2019-12-13 08:24 | Attacker created inbox forwarding rule |
| 2019-12-13 08:27 | Multiple finance-related emails accessed |
| 2019-12-13 08:33 | Suspicious outbound emails sent to internal finance team |
| 2019-12-13 08:40 | OAuth consent grant observed for suspicious application |
| 2019-12-13 08:48 | Forcepoint ONE detected abnormal SaaS session behavior |
| 2019-12-13 09:02 | User reported suspicious activity to IT/Security |
| 2019-12-13 09:07 | Incident response initiated |
| 2019-12-13 09:14 | Active sessions revoked |
| 2019-12-13 09:21 | Password reset enforced |
| 2019-12-13 09:39 | Malicious inbox rules removed |
| 2019-12-13 09:52 | IOC sweep initiated across tenant |
| 2019-12-13 10:44 | No additional compromised accounts identified |
| 2019-12-13 11:23 | Incident moved to monitoring/recovery phase |

---

## Observations

### Initial Access
Investigation determined the attacker gained access through a credential phishing campaign targeting Microsoft 365 users.

### Persistence
Persistence was established through:
- Mail forwarding rules
- OAuth application consent grants

### Defense Evasion
The attacker attempted to conceal activity by:
- Deleting security notification emails
- Leveraging valid user credentials
- Operating from residential proxy infrastructure

---

## Scope of Impact

### Impacted Assets
- 1 Microsoft 365 user account
- Finance department mailbox data
- Internal email communications

### Potentially Accessed Data
- Invoice discussions
- Vendor communications
- Internal contact lists

### Confirmed Actions
- Internal phishing attempts
- Attempted invoice fraud
- Email monitoring via forwarding rules

---

## Incident Status

| Category | Status |
|---|---|
| Containment | Completed |
| Credential Reset | Completed |
| Session Revocation | Completed |
| Threat Hunt | Completed |
| Monitoring | Ongoing |

---

## Lessons Learned

- Conditional Access policies required strengthening
- MFA fatigue-resistant methods should be enforced
- Mailbox forwarding rule alerts required tuning
- OAuth application monitoring needed improvement
