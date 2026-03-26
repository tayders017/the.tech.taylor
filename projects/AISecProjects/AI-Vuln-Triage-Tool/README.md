# 🛡️ AI-Powered Vulnerability Triage & Remediation Tool

> A context-aware, AI-assisted risk prioritization and remediation intelligence platform designed to reduce vulnerability noise and accelerate security operations.

---

## 🚀 Overview

Traditional vulnerability management platforms like Qualys and Tenable Nessus generate large volumes of findings, often prioritized primarily by CVSS scores.

This approach does not reflect **real-world risk**.

This project introduces an **AI-powered risk engine** that:
- Enriches vulnerabilities with contextual signals
- Prioritizes findings based on **true exploitability and business impact**
- Generates **actionable remediation strategies**
- Produces **analyst-ready and executive-ready outputs**

---

## 🎯 Problem Statement

Security teams face:
- Thousands of vulnerabilities with limited remediation capacity
- Over-reliance on CVSS (lacks environmental context)
- Alert fatigue and inefficient prioritization
- Lack of clear, actionable remediation guidance

---

## 💡 Solution

This platform transforms raw scan data into **prioritized, explainable, and actionable intelligence**.

### Key Capabilities:
- 🔍 Context-aware risk scoring (beyond CVSS)
- 🧠 AI-generated remediation guidance
- 📊 Intelligent prioritization of vulnerabilities
- 📄 Executive-level reporting
- ⚙️ Extensible architecture for enterprise environments

---

## 🏗️ Architecture

                      +----------------------+
                      | Vulnerability Scans  |
                      |(Qualys / Nessus /etc)|
                      +----------+-----------+
                                 |
                                 v
                      +----------------------+
                      | Data Normalization   |
                      +----------+-----------+
                                 |
                                 v
                      +----------------------+
                      | Context Enrichment   |
                      | - Asset criticality  |
                      | - Internet exposure  |
                      | - Exploit availability|
                      +----------+-----------+
                                 |
                                 v
                      +----------------------+
                      | Risk Scoring Engine  |
                      | (Deterministic + AI) |
                      +----------+-----------+
                                 |
                                 v
                      +----------------------+
                      | AI Remediation Engine|
                      +----------+-----------+
                                 |
              +------------------+------------------+
              |                                     |
              v                                     v
    +---------------------+         +---------------------------+
    |   Analyst Output    |         |   Executive Reporting     |
    +---------------------+         +---------------------------+

---

## ⚙️ Tech Stack

| Layer        | Technology |
|--------------|----------|
| Backend      | Python, FastAPI |
| Data         | Pandas |
| AI/LLM       | OpenAI API (or local LLM) |
| Storage      | SQLite / PostgreSQL |
| Deployment   | Docker |
| Optional UI  | React |

---

## 📦 Features

### 1. Vulnerability Ingestion
- Supports CSV/JSON exports from scanners
- Normalizes:
  - CVE
  - CVSS
  - Asset metadata
  - Ports/services

---

### 2. Context Enrichment

Adds environmental intelligence:
- Internet exposure detection
- Asset criticality mapping
- Known exploit availability
- Business context tagging

---

### 3. Risk Scoring Engine

Moves beyond CVSS by incorporating:

- Exposure (external vs internal)
- Exploitability
- Asset value
- Environmental risk

#### Example Logic:
```python
score = cvss

if internet_exposed:
    score += 2

if exploit_available:
    score += 3

if asset_criticality == "high":
    score += 2
```

---

### 4. AI Remediation Engine

Generates:
- Recommended fixes
- Patch prioritization
- Compensating controls
- Business impact explanations

---

### 5. Executive Reporting

Produces:
- Top critical risks
- Prioritized remediation roadmap
- Risk trends
- Business impact summaries

---

## 📊 Example Output

```json
{
  "cve": "CVE-2023-1234",
  "risk_score": 9.5,
  "priority": "Critical",
  "reason": "Internet-facing asset with known exploit",
  "remediation": "Apply vendor patch immediately or isolate system",
  "business_impact": "Potential remote code execution on production workload"
}
```

---

## 🔌 API Usage

### Analyze Vulnerabilities

```bash
POST /analyze
```

---

## 🧪 Running Locally

### 1. Clone Repo
```bash
git clone https://github.com/yourusername/ai-vuln-triage.git
cd ai-vuln-triage
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Set Environment Variables
```bash
export OPENAI_API_KEY=your_key_here
```
### 4. Run Application
```bash
uvicorn app.main:app --reload
```

---

## 🐳 Docker Setup

```bash
docker build -t ai-vuln-engine .
docker run -p 8000:8000 ai-vuln-engine
```

---

## 🧠 AI Design Considerations

### Why AI?
AI is used to:
- Translate technical findings into actionable guidance
- Reduce analyst cognitive load
- Generate human-readable summaries

---

## ⚠️ Limitations & Guardrails

### 1. Hallucination Risk
- AI outputs are **validated against deterministic scoring**
- Critical decisions should not rely solely on LLM output

### 2. Deterministic Fallback
- Risk scoring engine operates independently of AI
- Ensures consistent prioritization

### 3. Confidence Scoring (Planned)
- Future enhancement: attach confidence levels to AI outputs

---

## ⚖️ Tradeoffs

| Tradeoff | Description |
|--------|-------------|
| Accuracy vs Cost | LLM calls introduce cost; batching recommended |
| Real-time vs Batch | Batch processing preferred for large datasets |
| Simplicity vs Depth | More context improves accuracy but increases complexity |

---

## 📉 Impact (Example)

| Metric | Before | After |
|------|--------|------|
| Total Vulnerabilities | 5,000 | 5,000 |
| Actionable Findings | ~5,000 | ~200 |
| Analyst Triage Time | High | Reduced significantly |
| Prioritization Accuracy | Low | High |

---

## 🔒 Security Considerations

- No sensitive data is stored by default
- API keys handled via environment variables
- Designed for secure deployment in internal environments

---

## 🤖 Responsible AI Usage

This project incorporates AI/LLM capabilities to assist with vulnerability prioritization and remediation guidance. While AI enhances efficiency and insight, it must be used responsibly within defined boundaries.

### Intended Use
This tool is designed to:
- Assist security teams in triaging and prioritizing vulnerabilities
- Provide recommended remediation guidance
- Improve operational efficiency and reduce alert fatigue

It is **not intended to replace human judgment** in security decision-making.

---

### ⚠️ Limitations of AI Output
- AI-generated recommendations may be incomplete or inaccurate
- Outputs may lack full environmental or organizational context
- The system may produce inconsistent results across similar inputs

All AI outputs should be **validated by a qualified security professional** before implementation.

---

### 🛡️ Security & Safety Considerations
- Do not input sensitive data (e.g., credentials, PHI, proprietary system details) into AI prompts unless operating in a secure, approved environment
- Ensure API keys and secrets are properly secured
- Validate remediation actions before applying them to production systems

---

### 🔍 Transparency & Explainability
Where possible, this project:
- Combines deterministic risk scoring with AI-generated insights
- Provides reasoning for prioritization decisions
- Avoids “black box” decision-making

---

### 🚫 Prohibited Use
This project must not be used to:
- Automate offensive security activities without authorization
- Generate or distribute exploit code
- Make unverified security changes in production environments
- Replace formal risk management or compliance processes

---

### 🔄 Continuous Improvement
AI models and outputs should be:
- Regularly evaluated for accuracy and bias
- Tuned based on real-world feedback
- Monitored for failure modes and edge cases

---

## 🧩 Future Enhancements

- MITRE ATT&CK mapping
- Integration with SIEM tools
- Integration with EDR platforms
- SLA-based remediation tracking
- Slack / Teams alerting
- Multi-tenant support

---

## 📄 License

MIT License

---

## 👤 Author

Security Engineer focused on:
- Detection & response
- Vulnerability management
- AI-driven security automation

---

## ⭐ Final Note

This project is designed to demonstrate:
- Real-world security engineering challenges
- Practical application of AI in security workflows
- Architect-level thinking in risk prioritization and system design
