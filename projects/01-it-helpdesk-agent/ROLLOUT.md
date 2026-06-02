# Rollout — IT Helpdesk Agent

## Context

Deployed internally to an IT team of ~5 people as a first test of whether a RAG agent could meaningfully reduce repetitive helpdesk load.

## What we did

1. Ingested 3 core runbooks: MDM enrollment, SSO troubleshooting, VPN setup
2. Ran a 30-minute intro session showing example queries
3. Shared a prompt playbook with 10 starter questions
4. Checked back after 2 weeks with a short survey

## What worked

- MDM enrollment queries had a high hit rate — the runbook was well-structured
- Team members used it unprompted after the first week
- One person said it saved them from escalating a ticket

## What didn't work

- Okta queries with ambiguous names ("the John in IT") needed disambiguation — added a clarify step
- Long runbooks chunked poorly at first — improved chunking strategy in v2

## Metrics (first 30 days)

| Metric | Value |
|--------|-------|
| Total queries | ~85 |
| Unique users | 4 |
| Queries needing human follow-up | ~12% |
| Runbooks ingested | 3 |
| Avg response time | ~3s |

## What I'd do differently

- Add thumbs up/down feedback per response from day one
- Ingest runbooks as structured YAML, not raw Markdown — retrieval quality improves
- Build a Slack interface earlier; CLI was a barrier for less technical teammates
