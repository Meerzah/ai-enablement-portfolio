<div align="center">

# AI Systems / Agentic Ops Portfolio

**Systems engineer → AI-native automation, identity-as-code & cloud delivery**

Identity-backed agents · Okta Terraform · GCP · MCP · HITL · CI/CD · observability

<br/>

[![Dashboard](https://img.shields.io/badge/Dashboard-36--week_roadmap-58a6ff?style=flat-square)](./tracker/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-meerzah-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/meerzah)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-Vertex_AI-4285F4?style=flat-square&logo=googlecloud&logoColor=white)](https://cloud.google.com/vertex-ai)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white)](https://www.terraform.io)
[![MCP](https://img.shields.io/badge/Protocol-MCP-7F77DD?style=flat-square)](https://modelcontextprotocol.io)
[![Okta](https://img.shields.io/badge/Identity-Okta-007DC1?style=flat-square&logo=okta&logoColor=white)](https://okta.com)

**Live:** [Landing](https://meerzah.github.io/ai-systems-portfolio/) · [Weekly dashboard](https://meerzah.github.io/ai-systems-portfolio/tracker/)

</div>

---

```python
profile = {
    "target":    "AI Systems / Agentic Ops Engineer",
    "stack":     ["Okta", "Terraform", "GCP", "MCP", "Python", "Cloud Run", "CI/CD"],
    "shipped":   "Slack governance, n8n, Argus, Lumos/Okta at AppLovin",
    "building":  "Agentic ops control plane + Okta/GCP IaC + HITL + evals",
    "location":  "San Francisco Bay Area, CA",
}
```

---

### Shipped at AppLovin (production)

| Work | Stack | Interview frame |
|------|-------|-----------------|
| Slack App Governance → Jira | Deno, Slack API, Jira | "I shipped intake→ticket automation…" |
| n8n ops workflows | n8n, webhooks | "I automate approval flows…" |
| Argus endpoint control | GCP Cloud Run | "I built a Cloud Run control plane…" |
| Okta + Lumos access automation | Okta, SCIM, Lumos | "I operate identity-backed access requests…" |

---

### Portfolio products (mini → flagship)

| ID | Project | Stack | Status | Outcome |
|----|---------|-------|--------|---------|
| M1 | [IT Helpdesk Agent](./projects/01-it-helpdesk-agent) | ADK · Vertex · RAG | Portfolio demo | Tool-using ops agent + guardrails |
| M2 | [Okta MCP Server](./projects/02-okta-mcp-server) | MCP · Okta API | Portfolio demo | Read-only identity tools for agents |
| M3 | HITL Approval Gate | FastAPI · webhooks | Weeks 9–11 | Side effects blocked without approval |
| M4 | Agent Eval & Guardrails | eval CSV | Weeks 13–14 | 15-case regression suite |
| M5 | [Ops Event Plane](./projects/05-adoption-dashboard) | schema · Pub/Sub stub | In progress | Unified query/tool/approve events |
| M6 | [Platform Foundation](./projects/10-platform-foundation) | Terraform · GCP · Actions | Scaffold | Cloud Run + secrets + CI |
| M7 | LLMOps Observability | OTel · SLOs | Capstone | Cost/latency + error-budget notes |
| M8 | [Okta Identity-as-Code](./projects/11-okta-iac) | Terraform · Okta | Scaffold | Groups, apps, policies as code |
| **Flagship** | [**Agentic Ops Control Plane**](./projects/08-capstone-ops-agent) | All of the above | Weeks 21–24 | Hiring-manager end-to-end demo |

Supporting: [Agentspace Rollout](./projects/03-agentspace-rollout) · [Prompt Playbooks](./projects/04-prompt-playbooks) · [CIPHER](./projects/06-cipher) · [ALIUS](./projects/07-alius) · [Endpoint AI Governance](./projects/09-endpoint-ai-governance)

**Status key:** *Portfolio demo* = runnable · *Scaffold* = curriculum-ready stubs · *In development/planning* = AppLovin work (honest labels)

**Okta IaC boundary:** Terraform owns access topology (groups/apps/policies) + sandbox demo users. Production user lifecycle → SCIM/automation.

---

### Study roadmap

**[CURRICULUM.md](./CURRICULUM.md)** — weekly **theme → mini-project → flagship**. Eight competencies:

**Harness · Identity (+ Okta IaC) · Endpoint · Enablement · Workflow · Ops · Cloud platform · Portfolio**

| Phase | Weeks | What you ship |
|-------|-------|---------------|
| Foundation | 1–4 | Agent + Okta MCP + guardrails |
| Identity-as-code | 5–8 | Okta TF groups/apps/policies + GCP secrets stub |
| Workflow + containers | 9–12 | HITL, API, webhooks, Docker |
| Evals + events + CI | 13–16 | 15 evals, event stream, CI for Okta TF + agent |
| Endpoint + prep | 17–20 | Endpoint AI policy, Run vs GKE, architecture freeze |
| **Capstone** | **21–24** | **Flagship Agentic Ops Control Plane** |
| Portfolio | 25–36 | Demo, narrative, system design, apply |

| Resource | Link |
|----------|------|
| Competency model | [`CURRICULUM.md`](./CURRICULUM.md) |
| Weekly dashboard | [`tracker/`](./tracker/) |
| Interview prep | [`interview-prep/`](./interview-prep/) |

---

### Repo layout

```
projects/          # M1–M8 minis + flagship capstone
tracker/           # GitHub Pages dashboard + weeks.json
phases/            # Phase guides
interview-prep/    # System design templates + answers
study-notes/       # Active notes (+ cloud-platform/)
CONTEXT.md         # Targets, consulting offers
SETUP.md           # Run projects + tracker locally
```

---

### Contact

<div align="center">

Open to **AI Systems**, **agentic ops**, and **internal AI platform** roles.

[![LinkedIn](https://img.shields.io/badge/Connect-meerzah-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/meerzah)

</div>
