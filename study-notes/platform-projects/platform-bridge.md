# Platform bridge — CIPHER · ALIUS · agentic ops

> **Month 6+ capstone artifact.** One interview-ready narrative for AI Systems roles.

## The stack

| Layer | Project | Status | Role |
|-------|---------|--------|------|
| Identity automation | CIPHER | In development | Joiner/mover ABAC, Okta + Cloud Run |
| Lifecycle orchestration | ALIUS | Planning | Offboarding state machine, access revoke |
| Agentic ops case study | Portfolio | In progress | Ticket triage + Okta grant + audit log (POC) |
| Shipped automation | Slack app, n8n, Argus | Production | Intake→action patterns to extend |

## Unified workflow story (example)

1. **Friction:** High-volume access-request tickets in Slack/Jira
2. **Workflow:** Intake → manager approval → Lumos/Okta grant with HITL before writes
3. **Identity:** Least-privilege groups; audit fields in BigQuery/Firestore
4. **Agent:** LLM triage/routing only — deterministic Okta steps
5. **Measure:** Baseline TTR before automation (real numbers only)

## Interview 5-min talk track (outline)

- Hook: internal ops automation with identity scoped correctly
- Shipped (60s): Slack governance, n8n, Argus — concrete outcomes
- CIPHER (30s): architecting ABAC mover automation — in development
- ALIUS (30s): designed offboarding orchestration
- Agentic case (60s): POC triage workflow — honest status, HITL gates
- Close: targeting AI Systems / AI Systems roles

## Deliverables checklist

- [ ] This doc complete and sanitized
- [ ] Links to cipher-ship-plan.md and alius-architecture-blueprint.md
- [ ] Agentic workflow case study draft linked
- [ ] Rehearsed out loud once
