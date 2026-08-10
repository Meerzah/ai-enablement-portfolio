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

**Career stage:** Move 1 target — AI-native Automation / AI Systems Engineer  

**Positioning sentence:**
> Systems / automation engineer who builds identity-backed, agent-ready ops workflows (provisioning, triage, SaaS governance) with Python, Okta, and AI tooling.

**Resume for this lane:** `Kamaal_Mirza_Resume_Serval.docx`

---

## Career stages (private comp notes live outside this public repo)

| Stage | Focus |
|-------|--------|
| Now | Systems / IT — identity + automation foundation |
| Move 1 | AI Systems (primary 6–12 mo) |
| Stretch (this lane) | Senior IC at AI startups |

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

**Primary path:** AI Systems / Agentic Ops — 36-week roadmap with 90-day sprint focus.

**Weekly spine (use this by default):**

1. **Friction** — What's the high-volume manual ops request?
2. **Workflow** — Automate intake → approval → action (HITL where needed)
3. **Identity** — Okta/OAuth/SCIM scoped correctly (incl. agent identities)
4. **Agent** — Where LLM/agent helps vs deterministic automation
5. **Measure** — Deflection, TTR, hours saved, failure/retry rate (real only)
6. **Prove** — Ship one artifact (workflow, bot, runbook, metrics screenshot)

**Time budget:** 12–15 hrs/week

**Weekly cadence:**
- Mon → Friction
- Tue → Workflow
- Wed → Identity
- Thu → Agent
- Fri → Measure
- Sat–Sun → Prove (weekly mini)
- Capstone weeks (4, 8, 12 …) → monthly build
- Interview prep from Week 30+ (AI Systems roles)

**Dashboard:** `./tracker/serve.sh` — meta in `tracker/progress.json`  
**Public URL:** https://meerzah.github.io/ai-systems-portfolio/tracker/

---

## How to Help Me in This Workspace

**Framing:**
- I am becoming an **AI Systems / Agentic Ops engineer**.
- Okta/GCP topics should tie back to **workflow automation and agent-ready identity**.
- Reframe IT-ops work as **platform/automation engineering** when reviewing answers.
- **Do not claim** production AI agent experience I don't have.
- **Do not invent** deflection %, CSAT, or other metrics.

**Code style:**
- Python: typed (Pydantic v2), async-first (FastAPI + httpx), structlog, pytest. Match ALIUS-style if present.
- GCP: Workload Identity Federation over SA keys. Least privilege. Cloud Run preferred.
- n8n is in my stack for workflow prototyping — OK to reference.

**AI Systems work:**
- Focus: tool-use reliability, HITL approvals, evals/retries, knowledge bases for ops, identity for agents.
- When discussing agents: separate **deterministic automation** from **LLM-assisted triage/routing**.
- Frame portfolio around shipped Slack app, n8n, Argus, Okta/Lumos — plus one agentic workflow case study.

**Identity (supporting spine):**
- Assume GCP project `prj-it-d-core-041e` when relevant.
- Human + non-human identity (NHI) for future agent credentials.

**Study notes:**
- Format: **Friction → Workflow → Identity → Agent → Measure → Prove**
- Save under `/study-notes/` for active path work.

**Interview prep:**
- Frame for **AI-native internal ops AI automation**, AI Systems, Internal Tools / AI Ops — Staff-level at AI startups with ops automation teams.
- Tie answers to **shipped** work: Slack governance, n8n, Argus, Okta/Lumos, Kandji.
- CIPHER/ALIUS: accurate status only.

---

## Consulting (reference CONTEXT.md)

- (a) Okta JML/SSO audit — fixed fee
- (b) Access-request automation (Lumos/Okta-style)
- (c) AI-assisted triage / Slack approval bot

---

## What NOT to Suggest

- Generic IT Automation Engineer positioning (low-ceiling IT/QA automation)
- AWS services (GCP-native environment)
- LangChain (I work with Claude API + MCP directly)
- Leetcode grinding (targets use take-homes + system design)
- CISSP (not worth time right now)
- Kubernetes (not in current stack)
- Splitting study into unrelated tracks — use the 6-unit spine
