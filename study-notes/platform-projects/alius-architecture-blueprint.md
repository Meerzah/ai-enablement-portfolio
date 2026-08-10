# ALIUS — Architecture blueprint (planning)

> **Status:** Planning / not confirmed for production. Do not claim "shipped" in interviews until live.

AppLovin Lifecycle Identity & Unified System — event-driven offboarding orchestration.

## Problem

Manual offboarding across Okta, Google, devices, and apps creates access drift and NHI orphans when employees leave.

## Proposed architecture

```
Okta user.lifecycle.deactivate
        │
        ▼
Cloud Run (FastAPI) ──► Firestore state machine
        │                      │
        ├── Google 6-step sequence
        ├── Okta group/app cleanup
        ├── Reftab device lookup
        ├── Jira JQL (lookup only)
        └── BigQuery audit trail
        │
        ▼
Cloud Scheduler (retries) · Slack summary
```

## Threat → Detect → Enforce → Prove

| Threat | Detect | Enforce | Prove |
|--------|--------|---------|-------|
| Incomplete offboarding (orphan NHI) | Okta + GCP audit: active SA/API key after deactivate | ALIUS state machine + KeySentinel revoke | BigQuery audit: 100% terminal states |
| ASI03: agent/service account retains access | Credential still used post-offboard | Scoped revoke in sequence step | Integration test on deactivate hook |
| Retry storm / partial failure | Firestore stuck states, Scheduler metrics | Idempotent steps + DLQ pattern | Runbook + alert on stuck > N hours |

## Design questions to answer (Week 7 mini project)

- [ ] Firestore state schema (steps, status, retry count, actor)
- [ ] Idempotency for each downstream system
- [ ] How this connects to CIPHER joiner/mover (same Okta event patterns)
- [ ] Blast radius if ALIUS Cloud Run SA is compromised
- [ ] 2-min interview pitch: "why Firestore over Postgres for long-running sequences"

## References

- CIPHER Cloud Run + Okta Event Hook patterns (from ship plan — in development)
- [WIF agent identity design](../wif-agent-identity-design.md)
- Interview SD #2: [offboarding-pipeline.md](../../interview-prep/answers/offboarding-pipeline.md)
