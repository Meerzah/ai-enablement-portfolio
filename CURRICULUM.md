# AI Systems Engineering — Competency Model & Curriculum

**Bar:** Experienced Okta/GCP/systems engineer leveling into **AI Systems / Agentic Ops**.  
**Not in scope:** API-token tutorials, venv walkthroughs, “what is Terraform,” click-ops checklists.

Primary brand: identity-backed agent platforms with cloud delivery (GCP IaC, CI/CD, observability) and **Okta Identity-as-Code**.

---

## What you are training for

Hiring managers in this lane interrogate **decision boundaries, failure modes, and enforceable controls** — not whether you can create an Okta token.

| You are building | You are not building |
|------------------|----------------------|
| Fail-closed agent harnesses with evals + HITL | Chatbots and prompt demos |
| Identity tool surfaces safe under LLM misuse | Admin-console how-tos |
| Okta topology as a reviewed control plane | Users-as-TF anti-patterns in prod |
| CI/TF delivery + observability for agents | Pure K8s operator career track |

**Rule of difficulty:** If a competent Okta/GCP engineer already knows the step cold, it does not belong as a weekly learning objective. Setup is assumed; **design and proof** are the work.

---

## Eight competencies

1. **Agent harness** — tools, RAG limits, structural guardrails, adversarial evals  
2. **Identity & access** — Okta/SCIM, agent NHI, audit, HITL, **Okta Terraform topology**  
3. **Endpoint & fleet** — AI policy tiers tied to identity, offboarding graphs  
4. **AI enablement** — rollout with measurable adoption (real metrics only)  
5. **Workflow automation** — propose/approve/execute, idempotency under retries  
6. **Observability & ops** — audit streams, SLOs, LLM cost/latency, eval gates  
7. **Cloud platform & delivery** — Docker hardening, GCP TF, WIF, CI as change control  
8. **Portfolio & interview** — attackable architecture narrative  

Weekly spine: **Friction → Workflow → Identity → Agent → Measure → Prove**

---

## Portfolio products (compound into one flagship)

| ID | Product | Path |
|----|---------|------|
| M1 | Ops Agent Harness | `projects/01-it-helpdesk-agent/` |
| M2 | Okta MCP Identity Server | `projects/02-okta-mcp-server/` |
| M3 | HITL Approval Gate | module in `01` → capstone |
| M4 | Adversarial Eval Suite | `01/evals/` → capstone |
| M5 | Ops Event Plane | `projects/05-adoption-dashboard/` |
| M6 | Platform Foundation (GCP IaC + CI) | `projects/10-platform-foundation/` |
| M7 | LLMOps Observability | capstone `observability/` |
| M8 | Okta Identity-as-Code | `projects/11-okta-iac/` |
| **Flagship** | **Agentic Ops Control Plane** | `projects/08-capstone-ops-agent/` |

Each week is a **hard mini-build** that feeds one of these. Capstone weeks assemble — they do not invent a new toy.

---

## How a week works

1. **Challenge** — one sentence a staff engineer would respect  
2. **Study** — tradeoffs, abuse cases, architecture (not tool UIs)  
3. **Build** — artifacts with blast radius, tests, or ADRs  
4. **Prove** — adversarial or failure-path evidence in repo  

Source of truth: [`tracker/week_plans.py`](tracker/week_plans.py) + [`tracker/week_guides.py`](tracker/week_guides.py) → [dashboard](tracker/).

| Phase | Weeks | Pressure | Outcome |
|-------|-------|----------|---------|
| Foundation | 1–4 | Decision boundaries, tool surface, adversarial wiring, testable guardrails | M1 + M2 with teeth |
| Identity-as-code | 5–8 | Topology control plane, drift, TF/SCIM/agent contract, WIF/secrets threat model | M8 + M6 |
| Workflow | 9–12 | HITL hard gates, API contracts, idempotency, container boundaries | M3 |
| Evals + CI | 13–16 | Eval gates, adversarial 15, event plane, change control | M4 + M5 + CI |
| Endpoint + freeze | 17–20 | Identity-tied AI policy, offboarding graph, Run vs GKE ADR, architecture freeze | Capstone-ready |
| **Capstone** | **21–24** | Integrate under eval pressure → trust → observe → deliver | **Flagship** |
| Portfolio | 25–36 | Demo under interrupt, designs, apply | Hire loop |

---

## Capstone (hiring-manager demo)

**One sentence:** Identity-scoped ops agent platform — tool-using agent + Okta MCP (read) + Okta/GCP Terraform + HITL before writes + audit + adversarial evals + event stream + CI deploy to Cloud Run with SLOs and LLM cost/latency signals.

**Demo:** IaC topology → agent triage → propose write → HITL → audit/telemetry → deploy path.  
**Honest status:** Portfolio POC — never claim employer production AI agents.

---

## Skills checklist (raise the bar)

- [ ] Decision boundary doc with blast-radius deny list  
- [ ] Okta tool surface hardened against LLM misuse  
- [ ] Structural (not prompt-only) block on identity writes  
- [ ] Okta TF topology + drift story  
- [ ] HITL hard gate + unknown-group rejection  
- [ ] Adversarial eval suite that can fail a ship  
- [ ] CI plan for Okta IaC + agent tests  
- [ ] Capstone demo survives interrupt questions  
