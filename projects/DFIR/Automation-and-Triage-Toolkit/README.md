# DFIR Automation and Triage Toolkit

## Overview

This repository contains a collection of scripts and utilities developed to support digital forensics, incident response, and threat hunting activities across Windows and Linux environments.

The toolkit focuses on:
- Rapid evidence collection
- IOC extraction
- Log analysis
- Windows triage automation
- Browser artifact collection
- Hash analysis
- Threat hunting support

---

## Languages Used

- Bash
- PowerShell
- Python

---

## Toolkit Categories

| Category | Description |
|---|---|
| Evidence Collection | Rapid host triage and artifact acquisition |
| Log Parsing | Windows/Linux log analysis utilities |
| IOC Extraction | Automated IOC parsing and enrichment |
| Hash Analysis | File hashing and comparison utilities |
| Browser Artifacts | Browser history and credential artifact parsing |
| Windows Triage | Endpoint triage automation scripts |

---

## Example Tools

| Tool | Purpose |
|---|---|
| evi-collect-triage-basic.ps1 | Windows incident response triage collection, basic script, collects: processes, network connections, scheduled tasks, local users, and startup programs |
| evi-collect-triage-enhanced.ps1 | Windows incident response triage collection, enhanced script, uses the highly efficient -FilterHashtable method to reduce memory consumption|
| parse_evtx.py | EVTX log parsing and filtering, basic script, parses failed log on events |
| parse_evtx_enhanced.py | EVTX log parsing and filtering |
| parse_evtx_enhanced.ps1 | EVTX log parsing and filtering |
| win_triage_collector.ps1 | Endpoint triage automation scripts, collect Defender logs |


---

## Example Use Cases

- Ransomware investigations
- Business Email Compromise investigations
- Malware triage
- Threat hunting operations
- Endpoint compromise analysis
- Insider threat investigations

---

## Sample Output

See:
- `/sample-output/`
- `/docs/`

---

## Disclaimer

All scripts are intended for authorized security testing, incident response, and educational purposes only.
