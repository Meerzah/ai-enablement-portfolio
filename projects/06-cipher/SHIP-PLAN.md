# CIPHER — Ship plan (in development)

> **Status:** Not shipped. This doc is your checklist to get CIPHER to production at AppLovin.

Cross-team Identity Provisioning, Health & Entitlement Reconciliation — ABAC mover/joiner automation via Okta + Cloud Run + Jira.

## Target architecture

```
Jira Role Base / Employee Conversion ticket
        │
        ▼
Cloud Run (CIPHER) ──► Okta API (read profile, compute group delta)
        │
        ├── Slack + Jira summary (before apply)
        └── Apply functionalTeam ABAC group changes
```

## Ship phases

| Phase | Goal | Done when |
|-------|------|-----------|
| 1 | Design doc + threat model | `cipher-architecture.md` reviewed |
| 2 | MVP: read Okta + compute delta (no apply) | Dry-run logs correct deltas for 5 test users |
| 3 | Slack/Jira preview post | Stakeholders approve format |
| 4 | Apply in staging Okta | Zero unintended group changes in test |
| 5 | Production with rollback | Runbook + on-call doc; first real mover succeeds |

## Week 5 study integration

Use the roadmap Week 5 mini project to complete **Phase 1** here. Phases 2–5 are AppLovin work outside study hours — track in this checklist.

## Threat → Detect → Enforce

| Threat | Detect | Enforce |
|--------|--------|---------|
| Wrong groups applied on mover | Audit log: unexpected group adds | Human-in-loop Slack approve before apply |
| Over-privileged CIPHER SA | IAM audit: roles on Cloud Run SA | Least-privilege SA + WIF |
| ABAC drift | Weekly reconciliation job | Alert on ft_ baseline mismatch |

## Interview framing (until shipped)

"I architected CIPHER — ABAC-native mover automation on Okta and Cloud Run. Currently in active development; MVP dry-run is [status]."

Do **not** say "shipped" until Phase 5 is complete.
