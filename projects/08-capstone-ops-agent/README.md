# Capstone — Agentic IT Ops Platform

**Competencies:** harness + identity + endpoint + enablement + workflow + ops  
**Timeline:** Weeks 21–24 · See [CURRICULUM.md](../CURRICULUM.md)

## What this is

One integrated platform that demonstrates **AI Systems Engineering** for internal IT — not a chatbot demo.

```
                    ┌─────────────────────────────────┐
                    │  HTTP API + webhook intake       │
                    └───────────────┬─────────────────┘
                                    │
                    ┌───────────────▼─────────────────┐
                    │  ADK agent (harness)             │
                    │  · RAG runbooks                  │
                    │  · Okta MCP (read-only)          │
                    │  · HITL before writes            │
                    │  · Endpoint policy stub (09)     │
                    └───────────────┬─────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
   Audit log (identity)    Adoption events (enablement)   Eval suite (ops)
```

## Pillar integration

| Pillar | Source mini-projects | Capstone module |
|--------|---------------------|-----------------|
| Agent harness | 01, evals W13–14 | Core agent + tools |
| Identity | 02, 06, W5–7 | MCP + audit + HITL |
| Endpoint | 09, 07 | Policy check stub |
| Enablement | 03, 04, 05 | Metrics + KB index |
| Workflow | W9–11 | API + webhooks |
| Ops | W13–14, logging | Evals + alerts |

## Capstone weeks

| Week | Ship |
|------|------|
| 21 | One-command local run; 5 evals pass |
| 22 | HITL + audit on every query |
| 23 | Endpoint policy + metrics wired |
| 24 | Cloud Run POC + `capstone-case-study.md` |

## Definition of done

- [ ] All seven competencies represented in ARCHITECTURE.md
- [ ] Eval suite with logged pass/fail (no fake accuracy)
- [ ] Honest status: portfolio POC, not employer production
- [ ] 2-minute demo script rehearsed

## Start (Week 21)

1. Read [CURRICULUM.md](../CURRICULUM.md) skills checklist  
2. Copy patterns from `01-it-helpdesk-agent`  
3. Port `eval_cases.csv` first — tests drive integration  
