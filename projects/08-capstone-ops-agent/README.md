# Flagship — Agentic Ops Control Plane

**Competencies:** harness · identity · endpoint · enablement · workflow · ops · platform  
**Timeline:** Weeks 21–24 · See [CURRICULUM.md](../../CURRICULUM.md)

## What this is

One integrated platform that demonstrates **AI Systems + cloud delivery** for internal ops — not a chatbot demo.

**Recruiter one-liner:** Identity-scoped ops agent platform: tool-using agent + Okta MCP (read) + Okta/GCP Terraform IaC + HITL before writes + audit trail + eval harness + event stream + CI deploy to Cloud Run with SLOs and LLM cost/latency observability.

```
         ┌─────────────────────────────────────────┐
         │  Okta IaC (M8) + GCP IaC / CI (M6)       │
         └───────────────────┬─────────────────────┘
                             │ topology + deploy
         ┌───────────────────▼─────────────────────┐
         │  HTTP API + webhook intake (M3)           │
         └───────────────────┬─────────────────────┘
                             │
         ┌───────────────────▼─────────────────────┐
         │  Agent harness (M1)                       │
         │  · RAG runbooks · Okta MCP read (M2)     │
         │  · HITL before writes · Endpoint policy  │
         └───────────────────┬─────────────────────┘
                             │
     ┌───────────────┬───────┴────────┬──────────────┐
     ▼               ▼                ▼              ▼
  Audit log     Event plane (M5)   Eval suite (M4)  Observability (M7)
```

## Pillar integration

| Product | Source | Capstone module |
|---------|--------|-----------------|
| M1 Ops Agent | `01-it-helpdesk-agent` | Core agent + tools |
| M2 Okta MCP | `02-okta-mcp-server` | Read-only identity tools |
| M3 HITL Gate | Weeks 9–11 | Approval before side effects |
| M4 Evals | Weeks 13–14 | Regression suite |
| M5 Event plane | `05-adoption-dashboard` | Adoption / audit events |
| M6 Platform | `10-platform-foundation` | Terraform + CI → Cloud Run |
| M7 Observability | W23 | Logs, traces, SLO note |
| M8 Okta IaC | `11-okta-iac` | Groups/apps/policies MCP reads |

## Capstone weeks

| Week | Theme | Ship |
|------|-------|------|
| 21 | Assemble control plane | One-command local run; 5 evals; MCP reads TF-managed groups |
| 22 | Enforce identity + HITL | Unapproved writes blocked; audit on every query |
| 23 | Observability + policy | Endpoint policy + metrics + SLO sketch |
| 24 | Deliver cloud + identity | Cloud Run via M6; Okta plan in CI; case study |

## Demo script (2 min)

1. Okta topology is code (`11-okta-iac`)  
2. Intake → agent triages (runbook + Okta read)  
3. Propose write → HITL approve/deny  
4. Audit + metrics/trace visible  
5. Mention CI/Terraform path to Cloud Run  

## Definition of done

- [ ] M1–M8 represented in ARCHITECTURE.md  
- [ ] Eval suite with logged pass/fail (no fake accuracy)  
- [ ] Honest status: portfolio POC, not employer production  
- [ ] 2-minute demo script rehearsed  

## Start (Week 21)

1. Read [CURRICULUM.md](../../CURRICULUM.md) skills checklist  
2. Copy patterns from `01-it-helpdesk-agent`  
3. Port `eval_cases.csv` first — tests drive integration  
4. Point MCP at sandbox groups created by `11-okta-iac`  
