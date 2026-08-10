# Capstone — Integrated Ops Agent Platform

**Status:** Portfolio capstone (POC) · builds on mini-projects 01–05  
**Timeline:** Weeks 21–24 of the [36-week roadmap](https://meerzah.github.io/ai-systems-portfolio/tracker/)

## What this is

The capstone merges your weekly mini-projects into one demo-ready platform:

```
HTTP API (FastAPI)
    └── ADK helpdesk agent
            ├── RAG (runbooks)
            ├── Okta MCP (read-only identity)
            ├── HITL approval gate (before side effects)
            ├── Audit log + adoption events
            └── Eval suite (15+ cases)
```

This is **not** production deployment at your employer — honest POC for portfolio and interviews.

## What migrates from mini-projects

| Source | Capstone component |
|--------|-------------------|
| `01-it-helpdesk-agent` | Agent core, RAG, evals, escalation policy |
| `02-okta-mcp-server` | Identity tools (read-only) |
| `05-adoption-dashboard` | Event schema + usage metrics script |
| Weeks 10–14 docs | HITL flow, reliability, failure alerts |

## Capstone weeks (21–24)

| Week | Focus |
|------|--------|
| 21 | Assemble services; one local start command |
| 22 | HITL enforcement; block unapproved writes |
| 23 | Audit + observability wired end-to-end |
| 24 | Deploy POC (Cloud Run) + case study draft |

## Definition of done

- [ ] Single README with architecture diagram
- [ ] `docker compose up` or `./scripts/run-local.sh` works
- [ ] Eval suite runs with logged pass/fail (no fake accuracy %)
- [ ] `study-notes/capstone-case-study.md` published
- [ ] Demo script under 2 minutes

## Getting started (Week 21)

1. Copy patterns from `projects/01-it-helpdesk-agent/` into this folder
2. Add `ARCHITECTURE.md` before writing code
3. Port eval_cases.csv first — tests drive integration

See [dashboard Week 21](https://meerzah.github.io/ai-systems-portfolio/tracker/workbooks/week-21.html).
