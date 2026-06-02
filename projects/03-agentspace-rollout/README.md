# Agentspace Team Rollout

> A documented playbook for deploying Google Agentspace to internal teams — including the adoption friction, what worked, and the metrics that resulted.

---

## What this is

Not just a technical setup guide. A full rollout playbook: how to onboard a non-technical team to an AI knowledge agent, how to handle resistance, how to measure success, and how to present outcomes to leadership.

Deployed to 2 internal teams. Documented honestly.

---

## Rollout structure

```
Week 1   Setup + data connectors (Google Drive, internal docs)
Week 2   Access control config (IAM, who sees what)
Week 3   Pilot with Team 1 (3–5 people) — soft launch
Week 4   Feedback collection + prompt playbook published
Week 5   Expand to Team 2
Week 6   Metrics review + leadership deck
```

---

## What was connected

| Data source | Content | Access scope |
|-------------|---------|--------------|
| Google Drive (IT folder) | Runbooks, SOPs, policy docs | IT team only |
| Google Drive (HR shared) | Onboarding guides, benefits FAQ | All employees |
| Confluence (sanitized) | Engineering architecture docs | Engineering only |

---

## Access control approach

Used GCP IAM groups to mirror existing Okta groups — employees only see data sources their group is permitted to access. No custom code required; native Agentspace + IAM handles the boundary enforcement.

See [`access-control.md`](./access-control.md) for the full config.

---

## Adoption metrics (6 weeks)

| Metric | Team 1 | Team 2 |
|--------|--------|--------|
| Weekly active users | 4/5 (80%) | 3/6 (50%) |
| Queries per user/week | ~8 | ~4 |
| Positive feedback rate | 74% | 61% |
| Docs surfaced per query (avg) | 2.3 | 2.1 |
| Escalated to human (%) | 18% | 26% |

---

## What drove adoption (and what killed it)

**Drove adoption:**
- Pre-written prompt playbook handed out on day 1
- Short 20-min intro session with live demo before access was granted
- Slack reminder in the team channel with a "try asking..." tip each Monday

**Killed momentum:**
- Docs that hadn't been updated in 18+ months — surfaced bad answers
- No feedback mechanism in first 2 weeks — fixed by week 3
- Team 2 never got the live intro session — adoption noticeably lower

---

## Leadership deck

See [`assets/adoption-deck.md`](./assets/adoption-deck.md) for the slide outline used to present outcomes to leadership. Structured around: problem → solution → metrics → next steps.

---

## Files

```
03-agentspace-rollout/
├── README.md              # This file
├── setup-guide.md         # Step-by-step Agentspace configuration
├── access-control.md      # IAM config for data source boundaries
├── prompt-playbook.md     # Starter prompts shared with both teams
├── feedback-template.md   # Survey used at week 2 and week 6
└── assets/
    └── adoption-deck.md   # Leadership presentation outline
```
