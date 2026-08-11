# CONTEXT — AI Systems / Agentic Ops

Background and framing for agents, interview prep, and consulting. Read with [`CLAUDE.md`](CLAUDE.md) and [`README.md`](README.md).

---

## Background

**Name:** Kamaal Mirza  
**Location:** Bay Area (SF onsite roles are realistic)  
**Current role:** Systems / IT Engineer, AppLovin  

**Shipped platform work (accurate status):**

| Project | Status | Interview frame |
|---------|--------|-----------------|
| Okta JML / SSO / SCIM | Production | “I operate and extend…” |
| Lumos access automation | Production | “I built access-request flows…” |
| Slack→Jira governance app | Production | “I shipped a Slack workflow…” |
| n8n internal workflows | Production | “I automate intake→action…” |
| Argus (GCP Cloud Run endpoint control) | Production | “I built a Cloud Run control plane…” |
| Kandji / macOS fleet (~600 devices) | Production | “I manage MDM at scale…” |
| CIPHER (identity provisioning) | In development | “I architected…” not “I shipped…” |
| ALIUS (offboarding orchestration) | Planning | “I designed…” |

**Do not claim:** production AI agent deployments, deflection percentages, or CSAT numbers you haven’t measured.

---

## Primary target

**Role brand:** AI Systems / Agentic Ops Engineer (systems + cloud engineering fluency)  
**Positioning sentence:**

> Systems / automation engineer who builds identity-backed, agent-ready ops workflows (provisioning, triage, SaaS governance) with Python, Okta, Terraform, and AI tooling — including the cloud delivery plane underneath.

**Avoid positioning as:** generic Automation Engineer (low-ceiling IT/QA automation) or pure K8s cluster operator.

---

## Career stages

| Stage | Focus |
|-------|--------|
| Now | Systems / IT — identity + automation foundation |
| Move 1 | AI Systems / Agentic Ops + cloud delivery |
| Stretch (this lane) | Senior IC at AI startups / internal AI platform teams |

---

## Target companies (framing)

**Primary (Wave 1–2):**

- AI startups with **internal ops / AI systems / agentic ops** teams
- **Forward Deployed Automation** or Internal Tools at LLM/API companies
- Identity-heavy SaaS where Okta + workflow automation + IaC is core
- Internal AI platform / AI-ops roles that need systems + cloud fluency

(Company names are research targets, not the portfolio brand.)

---

## Consulting menu

Billable now; upgrade path to AI-native consulting as agent workflow case studies ship.

| Offer | Scope | Deliverable |
|-------|-------|-------------|
| **(a) Okta JML/SSO / topology audit** | Joiner/mover/leaver, SAML/OIDC apps, group hygiene, optional IaC readiness | Fixed-fee report + remediation checklist |
| **(b) Access-request automation** | Lumos/Okta-style intake → approval → provision | Workflow design + implementation plan or build |
| **(c) AI-assisted triage / Slack approval bot** | Ticket routing, KB lookup, human-in-loop approvals | POC workflow + metrics plan (no invented KPIs) |

---

## Portfolio pieces (honest status)

**Shipped at AppLovin (production):**

- Slack App Governance → Jira ITOPS
- n8n ops workflows
- Argus GCP Cloud Run endpoint control
- Okta + Lumos access automation

**Public portfolio repo:** [Meerzah/ai-systems-portfolio](https://github.com/Meerzah/ai-systems-portfolio)

| Project | Path | Status |
|---------|------|--------|
| IT Helpdesk Agent (M1) | `projects/01-it-helpdesk-agent/` | Portfolio demo |
| Okta MCP Server (M2) | `projects/02-okta-mcp-server/` | Portfolio demo |
| Agentspace Rollout | `projects/03-agentspace-rollout/` | Supporting |
| Prompt Playbooks | `projects/04-prompt-playbooks/` | Supporting |
| Ops Event Plane (M5) | `projects/05-adoption-dashboard/` | In progress |
| CIPHER | `projects/06-cipher/` | In development (AppLovin) |
| ALIUS | `projects/07-alius/` | Planning (AppLovin) |
| **Flagship — Agentic Ops Control Plane** | `projects/08-capstone-ops-agent/` | Weeks 21–24 |
| Endpoint AI Governance | `projects/09-endpoint-ai-governance/` | Weeks 17–18 |
| Platform Foundation (M6) | `projects/10-platform-foundation/` | Scaffold (W8+) |
| Okta Identity-as-Code (M8) | `projects/11-okta-iac/` | Scaffold (W5–7) |

**Dashboard:** https://meerzah.github.io/ai-systems-portfolio/tracker/

---

## Study spine (primary)

1. **Friction** — high-volume manual ops request  
2. **Workflow** — intake → approval → action  
3. **Identity** — Okta/OAuth/SCIM + agent identities + Okta-as-code  
4. **Agent** — LLM triage/KB/routing vs deterministic steps  
5. **Measure** — deflection, TTR, hours saved, retry rate (real metrics only)  
6. **Prove** — ship artifact weekly  

Cloud engineering (Docker, Terraform GCP + Okta, CI/CD, observability, K8s literacy) is woven into weekly themes — see `CURRICULUM.md`.

---

## Certs (checkpoints, not spine)

| Cert | Role | Status |
|------|------|--------|
| Okta Certified Professional | Identity credibility | Done |
| GCP Associate Cloud Engineer | Agent hosting + IAM basics | Optional checkpoint |
| Okta Certified Administrator | Deeper IdP | Month 5+ optional |
