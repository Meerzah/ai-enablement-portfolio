# AI Systems Engineering — Competency Model & Curriculum

Research-backed map for this portfolio. Primary brand: **AI Systems / Agentic Ops** with a deliberate **cloud engineering** layer (GCP IaC, CI/CD, containers, observability) and **Okta Identity-as-Code**.

---

## What the market actually hires for

**AI Systems / Agentic Ops** is not ML research. It is **production infrastructure around LLMs and agents**, plus the identity and delivery plane that makes them safe:

| You are building | You are not building |
|------------------|----------------------|
| Agent harness (tools, evals, HITL) | Training custom models |
| Identity-scoped tool access + Okta-as-code | Click-ops-only Okta |
| Workflow automation with agents | One-off prompt demos |
| Cloud delivery (Terraform, CI, Cloud Run) | Pure K8s cluster-operator career |
| Enablement + adoption at scale | Slide decks about AI |

---

## Eight competencies

1. **Agent harness** — tools, RAG, guardrails, evals, ADK/MCP  
2. **Identity & access** — Okta, SCIM, agent credentials, audit, HITL, **Okta Terraform**  
3. **Endpoint & fleet** — MDM, AI tool policy, offboarding orchestration  
4. **AI enablement** — rollout, playbooks, KB, adoption metrics  
5. **Workflow automation** — intake → approval → action, APIs, webhooks  
6. **Observability & ops** — logs, traces, evals, alerts, honest metrics, LLM cost/latency  
7. **Cloud platform & delivery** — Docker, Terraform (GCP), CI/CD, Cloud Run, K8s literacy  
8. **Portfolio & interview** — case study, system design, apply  

Weekly spine (unchanged): **Friction → Workflow → Identity → Agent → Measure → Prove**

---

## Portfolio products (hiring-manager view)

| ID | Product | Path |
|----|---------|------|
| M1 | Ops Agent Harness | `projects/01-it-helpdesk-agent/` |
| M2 | Okta MCP Identity Server | `projects/02-okta-mcp-server/` |
| M3 | HITL Approval Gate | module in `01` → capstone |
| M4 | Agent Eval & Guardrails | `01/evals/` → capstone |
| M5 | Ops Event Plane | `projects/05-adoption-dashboard/` |
| M6 | Platform Foundation (GCP IaC + CI) | `projects/10-platform-foundation/` |
| M7 | LLMOps Observability | capstone `observability/` + M6 |
| M8 | Okta Identity-as-Code | `projects/11-okta-iac/` |
| **Flagship** | **Agentic Ops Control Plane** | `projects/08-capstone-ops-agent/` |

**Okta IaC boundary:** Terraform owns **access topology** (groups, apps, policies, assignments) + sandbox demo users. Production user lifecycle stays SCIM / automation (CIPHER-style). Never commit tokens; use Okta preview/sandbox only.

---

## 36-week map (theme → mini ship)

Source of truth: [`tracker/week_plans.py`](tracker/week_plans.py) → dashboard [`tracker/`](tracker/).

| Phase | Weeks | Themes (summary) | Outcome |
|-------|-------|------------------|---------|
| Foundation | 1–4 | Friction, Okta MCP, wiring, guardrails | M1 + M2 runnable |
| Identity-as-code | 5–8 | Okta TF groups/apps/policies, SCIM boundary, GCP secrets stub | M8 + M6 skeleton |
| Workflow + containers | 9–12 | HITL, FastAPI, webhooks, Docker compose | M3 + containerized agent |
| Evals + events + CI | 13–16 | 15 evals, event stream, CI for Okta TF + agent | M4 + M5 + CI |
| Endpoint + prep | 17–20 | Endpoint AI policy, ALIUS, Run vs GKE, architecture freeze | Capstone ready |
| **Capstone** | **21–24** | Assemble → HITL → observability → deploy | **Flagship control plane** |
| Portfolio | 25–36 | Demo, narrative, designs, apply | Job-ready story |

**Rule:** Every week ships **one artifact** in `projects/` or `study-notes/`. No abstract-only weeks.

---

## Capstone definition

**Project:** `projects/08-capstone-ops-agent/`

**One sentence:** Identity-scoped ops agent platform — tool-using agent + Okta MCP (read) + Okta/GCP Terraform + HITL before writes + audit + evals + event stream + CI deploy to Cloud Run with SLOs and LLM cost/latency observability.

**Demo (2 min):** Okta groups/apps in Terraform → agent triages (runbook + Okta read) → proposes write → HITL → audit → metrics/trace → mention CI/Terraform path.

**Honest status:** Portfolio POC on sandbox Okta + dev GCP — not employer production AI agents.

---

## Skills checklist (self-assess quarterly)

- [ ] Demo agent calling MCP tools with read-only Okta token  
- [ ] Show Okta groups/apps/policies declared in Terraform (sandbox)  
- [ ] Explain TF topology vs SCIM user lifecycle boundary  
- [ ] Show HITL blocking an unauthorized write  
- [ ] Run eval suite with raw pass/fail log  
- [ ] Build/push via CI; deploy agent path via Terraform to Cloud Run  
- [ ] Explain Cloud Run vs GKE for an agent workload in 3 minutes  
- [ ] Walk flagship architecture in under 2 minutes  

---

## References (research)

- [GCP — Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
- [Okta Terraform provider](https://registry.terraform.io/providers/okta/okta/latest/docs)
- [OpenAI — AI Systems Engineer roles](https://openai.com/careers/)
- [Augment Code — AI Platform Engineering Leader job spec (2026)](https://www.augmentcode.com/guides/ai-platform-engineering-leader-job-spec)
