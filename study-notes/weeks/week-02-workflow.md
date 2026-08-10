# Week 2 — Workflow diagram

## Current manual path

- **Trigger:**
- **Submitter:**
- **Approver(s):**
- **Executor:**

## HITL gate

What must be human-approved before any Okta write or ticket state change:

## Reuse from shipped patterns

What you can reuse from Slack intake / workflow automation:

## Diagram

```mermaid
flowchart TD
  A[Intake] --> B{Valid?}
  B -->|yes| C[Approval]
  B -->|no| D[Reject + notify]
  C --> E[HITL check]
  E --> F[Execute action]
```

## Gap analysis

What's missing vs your chosen candidate from Week 1:
