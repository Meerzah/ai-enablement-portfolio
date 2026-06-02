# AI Adoption Dashboard

> Tracks usage metrics for internal AI tools — queries, users, feedback signals — using GCP Cloud Logging and Python.

---

## Problem

Rolling out an AI tool is easy. Knowing whether people are actually using it, and whether it's helping, is hard. This dashboard answers:

- How many people used the tool this week?
- What are they asking? What topics come up most?
- What percentage of responses needed human follow-up?
- Is adoption growing, flat, or dropping?

---

## Architecture

```
AI tool (ADK agent / Agentspace)
        │
        ▼ structured logs
GCP Cloud Logging
        │
        ▼ log sink
BigQuery dataset
        │
        ▼
Python ETL (daily)
        │
        ▼
Metrics CSV / Google Sheets
        │
        ▼
Leadership report (weekly)
```

---

## Metrics tracked

| Metric | Source | Frequency |
|--------|--------|-----------|
| Total queries | Cloud Logging | Daily |
| Unique active users | Cloud Logging | Weekly |
| Query topic distribution | LLM classification | Weekly |
| Thumbs up / thumbs down rate | Agent feedback log | Daily |
| Human escalation rate | Ticket system | Weekly |
| Response latency (p50, p95) | Cloud Logging | Daily |

---

## Setup

```bash
cd projects/05-adoption-dashboard
pip install -r requirements.txt

export GOOGLE_CLOUD_PROJECT=your-project-id
export BIGQUERY_DATASET=ai_adoption_metrics

# Run ETL
python src/etl.py --date 2025-01-15

# Generate weekly report
python src/report.py --week 2025-W03
```

---

## Sample output

```
Week 3 summary — IT Helpdesk Agent
──────────────────────────────────
Active users:        12 (↑ 4 from last week)
Total queries:       94
Avg queries/user:    7.8
Positive feedback:   71%
Escalation rate:     14% (↓ from 21%)

Top query topics:
  MDM enrollment     34%
  SSO / access       28%
  VPN setup          18%
  Other              20%
```

---

## Files

```
05-adoption-dashboard/
├── src/
│   ├── etl.py          # Pulls logs from BigQuery, writes metrics
│   ├── report.py       # Generates weekly summary
│   └── classify.py     # LLM-based query topic classification
├── requirements.txt
└── README.md
```
