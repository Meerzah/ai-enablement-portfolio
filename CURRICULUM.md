# AI Systems Engineering — Competency Model & Curriculum

Research-backed map for this portfolio. Sources: OpenAI/Kindo/Kepler agent-systems roles, Serval/MYOB/Harvey AI enablement postings, GCP Agent Identity docs, enterprise GenAI stack frameworks (2025–2026).

---

## What the market actually hires for

**AI Systems / Agentic Ops** is not ML research. It is **production infrastructure around LLMs and agents**:

| You are building | You are not building |
|------------------|----------------------|
| Agent harness (tools, evals, HITL) | Training custom models |
| Identity-scoped tool access | Generic chatbots |
| Workflow automation with agents | One-off prompt demos |
| Enablement + adoption at scale | Slide decks about AI |

Job postings converge on **seven competency areas** (below). Your edge: you already ship **identity + endpoint + automation** in production — this curriculum turns that into **agent-ready platform engineering**.

---

## Seven competencies

### 1. Identity & access for humans and agents (your strength)

**What employers want**

- SAML/OIDC/SCIM, RBAC, group-based access, joiner/mover/leaver
- **Agent credentials**: per-agent identity (SPIFFE/GCP Agent Identity), WIF, read vs write separation
- MCP and API integrations with **least privilege**
- Audit: who/what/when/approved_by on every automated action

**Portfolio projects:** `02-okta-mcp-server`, `06-cipher` (design), WIF study note, capstone HITL gate

---

### 2. Endpoint & fleet management (your strength)

**What employers want**

- MDM at scale (macOS fleet), device lifecycle tied to identity
- **AI on the endpoint**: approved tools, shadow-AI risk, policy via MDM
- Visibility: inventory, compliance, osquery-style telemetry
- Offboarding: device + access + SaaS in one orchestration story

**Portfolio projects:** `09-endpoint-ai-governance`, `07-alius` (design), endpoint module in capstone

---

### 3. AI enablement & internal platform (your target lane)

**What employers want**

- Roll out AI tools to teams with **playbooks**, not ad hoc access
- Adoption metrics (usage, not fake CSAT)
- Self-service internal platform: KB, prompt libraries, golden paths
- Partner with teams to find high-friction workflows

**Portfolio projects:** `03-agentspace-rollout`, `04-prompt-playbooks`, `05-adoption-dashboard`

---

### 4. Agent harness engineering (core technical skill)

**What employers want**

- Tool calling design (schemas, guardrails, escalation)
- RAG for ops KB — when **not** to use RAG
- **Evals** + regression suites before ship
- Context management, retries, non-deterministic failure handling

**Portfolio projects:** `01-it-helpdesk-agent`, eval harness, capstone core

---

### 5. Workflow & integration automation (your strength)

**What employers want**

- Intake → approval → action (Slack, tickets, webhooks)
- Idempotency, retries, alerting on failure
- Connect agents to **deterministic** execution (don't let LLM write to prod directly)
- n8n-style orchestration + Cloud Run services

**Portfolio projects:** patterns from shipped Slack→Jira + n8n; webhook/HITL mini-projects; capstone execution layer

---

### 6. Observability, evals & operations (required, often missing)

**What employers want**

- Structured logs, tracing (OpenTelemetry), audit trails
- Eval datasets + pass/fail logs (**no invented accuracy %**)
- Cost/latency awareness, failure runbooks
- LLMOps: prompt versioning, regression on model changes

**Portfolio projects:** logging in `01`, `05-adoption-dashboard`, eval CSV, capstone observability

---

### 7. Delivery, governance & narrative (interview lane)

**What employers want**

- System design for internal ops automation
- Responsible AI: HITL, data boundaries, honest POC status
- Case study: problem → architecture → limits → what's shipped vs designed
- Consulting packaging (access audit, automation, triage bot)

**Portfolio projects:** `interview-prep/`, capstone case study, consulting one-pager

---

## How your three focus areas map

```
                    ┌─────────────────────────────┐
                    │   CAPSTONE (Week 21–24)      │
                    │   Agentic IT Ops Platform    │
                    └──────────────┬──────────────┘
                                   │
     ┌─────────────────────────────┼─────────────────────────────┐
     │                             │                             │
┌────▼────┐                  ┌─────▼─────┐                 ┌─────▼─────┐
│Identity │◄─── MCP/HITL ───►│  Agent    │◄─── KB/RAG ───►│ Enablement│
│ + IAM   │                  │  harness  │                 │ + metrics │
└────┬────┘                  └─────┬─────┘                 └─────┬─────┘
     │                             │                             │
     └──────────────┬──────────────┴──────────────┬──────────────┘
                    │                             │
              ┌─────▼─────┐                 ┌─────▼─────┐
              │ Endpoint  │                 │ Workflow  │
              │ + fleet   │                 │ automation│
              └───────────┘                 └───────────┘
```

---

## 36-week coursework structure

| Phase | Weeks | Focus | Outcome |
|-------|-------|-------|---------|
| **Foundation** | 1–4 | Agent harness + MCP read tools | Runnable agent + identity queries |
| **Identity depth** | 5–8 | Agent credentials, audit, access patterns | Audit schema + CIPHER Phase 1 design |
| **Workflow** | 9–12 | HITL, API, webhooks, reliability | Approval gate + FastAPI + idempotency |
| **Enablement** | 13–16 | Rollout, playbooks, adoption metrics | Team rollout + dashboard on real logs |
| **Endpoint** | 17–20 | Fleet AI policy, offboarding design, integration demo | Endpoint governance doc + E2E demo |
| **Capstone** | 21–24 | Merge pillars into one platform | `08-capstone-ops-agent` deploy POC |
| **Portfolio** | 25–36 | Case study, interview, apply | Job-ready narrative |

**Rule:** Every week ships **one artifact in `projects/` or `study-notes/`** — code, doc, eval file, or runbook. No abstract-only weeks.

---

## Capstone definition

**Project:** `projects/08-capstone-ops-agent/`

**One sentence:** Internal IT ops agent with read-only identity tools, HITL before writes, endpoint-aware policy checks, adoption logging, and eval suite — deployed as a Cloud Run POC.

**Integrates:**

| Pillar | Capstone component |
|--------|-------------------|
| Identity | Okta MCP read + audit log + HITL |
| Endpoint | Policy check module (approved AI tools / device posture stub) |
| Enablement | Usage events → adoption dashboard script |
| Harness | ADK agent + tools + 15 eval cases |
| Workflow | HTTP API + webhook intake pattern |
| Ops | Structured logs + failure alerts |

---

## Skills checklist (self-assess quarterly)

- [ ] Can demo agent calling MCP tools with read-only Okta token
- [ ] Can explain agent identity vs shared service account (WIF/SPIFFE)
- [ ] Can show HITL blocking an unauthorized write
- [ ] Can run eval suite and show raw pass/fail log
- [ ] Can describe MDM + AI governance rollout without exposing employer internals
- [ ] Can draw intake→approval→action for access request in 5 minutes
- [ ] Can walk capstone architecture in under 2 minutes

---

## References (research)

- [OpenAI — AI Systems Engineer, Codex Agents](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/)
- [GCP — Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
- [Serval — MCP server docs](https://docs.serval.com/sections/api-reference/mcp-server)
- [Augment Code — AI Platform Engineering Leader job spec (2026)](https://www.augmentcode.com/guides/ai-platform-engineering-leader-job-spec)
- [MYOB — Senior AI Enablement Engineer](https://jobs.lever.co/myob-2/b1fa14bd-a953-4e9b-a131-29b904dbb550)
- [Harvey — Sr. AI Enablement Engineer](https://jobs.ashbyhq.com/harvey/393b91ff-9966-4a22-a39b-f49014965693)
