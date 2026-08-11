# CLAUDE.md — AI Systems / Agentic Ops Workspace

This file tells Cursor / VS Code Copilot / any AI assistant exactly who I am,
what I'm building, and how to help in this workspace.

---

## Who I Am

I'm a Systems Engineer at AppLovin with 8+ years of enterprise IT experience.
I manage a macOS-heavy endpoint fleet (~600 devices via Kandji MDM) and ship
identity-backed automation daily.

**Core stack (shipped):**

- **Identity:** Okta (SAML, OIDC, SCIM, ABAC, Device Trust, Workflows)
- **Access automation:** Lumos, n8n workflows
- **Cloud:** GCP — Cloud Run, Firestore, Secret Manager, BigQuery, IAM
- **Endpoint:** Kandji, osquery, Santa/Moroz (macOS)
- **Integrations:** Slack, Jira (applovin.atlassian.net), Python/Bash, Deno (Slack app)

**Building (portfolio):** Terraform for GCP + Okta Identity-as-Code, agent harness (MCP/HITL/evals), CI/CD, observability

**Career stage:** Move 1 target — AI Systems / Agentic Ops Engineer (systems + cloud engineering fluency)

**Positioning sentence:**
> Systems / automation engineer who builds identity-backed, agent-ready ops workflows (provisioning, triage, SaaS governance) with Python, Okta, Terraform, and AI tooling — including the cloud delivery plane underneath.

---

## Career stages (private comp notes live outside this public repo)

| Stage | Focus |
|-------|--------|
| Now | Systems / IT — identity + automation foundation |
| Move 1 | AI Systems / Agentic Ops + cloud delivery (primary 6–12 mo) |
| Stretch (this lane) | Senior IC at AI startups / internal AI platform teams |

---

## Platforms at AppLovin

**Status key:** Shipped = production · Planning = design only — do not overclaim.

| Project | Status | Notes |
|---------|--------|-------|
| Slack App Governance | Shipped | Slack→Jira ITOPS |
| n8n ops workflows | Shipped | Internal automation |
| Argus | Shipped | GCP Cloud Run endpoint control plane |
| CIPHER | In development | Identity provisioning — “architected” not “shipped” |
| ALIUS | Planning | Offboarding orchestration design |

---

## This Workspace: What It's For

**Primary path:** AI Systems / Agentic Ops — 36-week roadmap. Weekly **theme → mini-project → flagship capstone**. Cloud engineering (Docker, Terraform GCP + Okta, CI/CD, observability, K8s literacy) supports the spine — it does not replace it.

**Weekly spine (use this by default):**

1. **Friction** — What's the high-volume manual ops request?
2. **Workflow** — Automate intake → approval → action (HITL where needed)
3. **Identity** — Okta/OAuth/SCIM scoped correctly (incl. agent identities + Okta-as-code)
4. **Agent** — Where LLM/agent helps vs deterministic automation
5. **Measure** — Deflection, TTR, hours saved, failure/retry rate (real only)
6. **Prove** — Ship one artifact (workflow, bot, runbook, IaC, metrics screenshot)

**Time budget:** 12–15 hrs/week

**Weekly cadence:**
- Mon → Friction
- Tue → Workflow
- Wed → Identity
- Thu → Agent
- Fri → Measure
- Sat–Sun → Prove (weekly mini)
- Capstone weeks 21–24 → flagship Agentic Ops Control Plane
- Interview prep from Week 29+ (AI Systems / agentic ops / internal AI platform roles)

**Dashboard:** `./tracker/serve.sh` — meta in `tracker/progress.json`  
**Public URL:** https://meerzah.github.io/ai-systems-portfolio/tracker/

**Portfolio products:** M1–M8 minis → `projects/08-capstone-ops-agent/` flagship. See `CURRICULUM.md`.

---

## How to Help Me in This Workspace

**Framing:**
- I am becoming an **AI Systems / Agentic Ops engineer** with **cloud engineering** fluency.
- Okta/GCP topics should tie back to **workflow automation, agent-ready identity, and IaC**.
- Reframe IT-ops work as **platform/automation engineering** when reviewing answers.
- **Do not claim** production AI agent experience I don't have.
- **Do not invent** deflection %, CSAT, or other metrics.

**Code style:**
- Python: typed (Pydantic v2), async-first (FastAPI + httpx), structlog, pytest. Match ALIUS-style if present.
- GCP: Workload Identity Federation over SA keys. Least privilege. Cloud Run preferred.
- IaC: Terraform for GCP **and** Okta (sandbox). Okta TF owns access topology (groups/apps/policies); user lifecycle via SCIM/automation — not prod users as primary TF source of truth.
- n8n is in my stack for workflow prototyping — OK to reference.

**AI Systems work:**
- Focus: tool-use reliability, HITL approvals, evals/retries, knowledge bases for ops, identity for agents.
- When discussing agents: separate **deterministic automation** from **LLM-assisted triage/routing**.
- Frame portfolio around shipped Slack app, n8n, Argus, Okta/Lumos — plus Okta IaC, platform foundation, and flagship control plane.

**Identity (supporting spine):**
- Assume GCP project `prj-it-d-core-041e` when relevant.
- Human + non-human identity (NHI) for future agent credentials.
- Okta IaC lives in `projects/11-okta-iac/` (preview/sandbox org only).

**Study notes:**
- Format: **Friction → Workflow → Identity → Agent → Measure → Prove**
- Save under `/study-notes/` for active path work. Cloud notes under `/study-notes/cloud-platform/`.

**Interview prep:**
- Frame for **AI Systems**, agentic ops, internal AI platform / AI-ops — not a single company brand.
- Tie answers to **shipped** work: Slack governance, n8n, Argus, Okta/Lumos, Kandji — plus portfolio IaC/agent artifacts as they ship.
- CIPHER/ALIUS: accurate status only.

---

## Consulting (reference CONTEXT.md)

- (a) Okta JML/SSO audit — fixed fee (can include IaC/topology hygiene angle)
- (b) Access-request automation (Lumos/Okta-style)
- (c) AI-assisted triage / Slack approval bot

---

## What NOT to Suggest

- Generic IT Automation Engineer positioning (low-ceiling IT/QA automation)
- AWS services (GCP-native environment)
- LangChain (I work with Claude API + MCP directly)
- Leetcode grinding (targets use take-homes + system design)
- CISSP (not worth time right now)
- Owning multi-tenant Kubernetes as the primary career (K8s **literacy** + Cloud Run vs GKE tradeoffs are in-scope)
- Splitting study into unrelated tracks — cloud engineering **supports** the AI Systems spine; do not replace it with a pure platform-SRE curriculum
