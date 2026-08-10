# System Design Interview Template
## AI Systems / internal ops automation framing

Use this structure for every system design practice session (AI Systems roles, AI startups with ops teams).

---

## Template

### Problem statement
*[Paste the question here]*

### Clarifying questions I'd ask (2–3 max)
1.
2.
3.

### Scale / constraints I'm assuming
- Users / entities:
- Events per second:
- Data retention:
- Latency SLA:
- Compliance surface (SOC2, etc.):

### High-level design (draw first, explain second)
```
[ASCII diagram here]
```

### Component breakdown
**[Component 1]:**
- What it does
- Why this choice vs. alternatives
- GCP service if applicable

### Data model
*Key entities and their relationships*

### Identity & access considerations
- Who/what authenticates (human, service, future agent)
- NHI surface: service accounts / OAuth scopes created
- Least privilege: IAM scope per component
- Audit trail: what gets logged and where

### Workflow & HITL
- Which steps are deterministic vs LLM-assisted
- Human approval gates before destructive actions (Okta writes, deletes)

### Trade-offs I'm making
| Decision | Alternative | Why I chose this |
|----------|-------------|-----------------|
| | | |

### How I'd connect this to shipped work + platform projects
*Accurate status: Slack app, n8n, Argus shipped; CIPHER in development; ALIUS planning; agentic ops case study POC.*

### What I'd do differently at 10x scale

---

## Practice questions (AI Systems / agentic ops)

1. **Design internal IT ticket automation** — Slack/Jira intake, triage routing, HITL approval, Okta group grant, audit log. 500 tickets/week.

2. **Design a scalable NHI governance system** — inventory, lifecycle, auto-revoke on offboarding, dormant detection. 10K service accounts, 500 engineers.

3. **Design an event-driven offboarding pipeline** — HR deactivation trigger, 20+ downstream systems, retries, full audit trail. 50 offboardings/day peak.

4. **Design an agent identity broker** — short-lived scoped credentials for AI agents at runtime. Cloud Run. 1000 concurrent agents.

5. **Design an access-request automation platform** — Lumos/Okta-style intake → approval → provision with metrics and failure handling.
