# Week 1 — Decision boundary (not a how-to)

**Challenge:** Design a fail-closed decision boundary for an IT ops agent that can see identity data — under social-engineering pressure.

**Project:** `projects/01-it-helpdesk-agent/`  
**Ship also:** `docs/decision-boundary.md` in that project (or link from here).

## Blast-radius matrix (fill 8)

| # | Friction / request | Blast radius (L/M/H) | Agent | Deterministic | Human | Why |
|---|--------------------|----------------------|-------|---------------|-------|-----|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |

## Explicit deny list (must have ≥4)

Requests the agent must never fulfill even if the runbook exists:

1.  
2.  
3.  
4.  

## Adversarial prove set (expected = refuse / escalate)

| Query (sanitized) | Attack type | Expected control | Result |
|-------------------|-------------|------------------|--------|
| | Social eng | | |
| | Privilege escalation | | |
| | Out of scope | | |
| | Ambiguous VIP | | |
| | Conflicting policy | | |

## Structural vs prompt

| Control | Prompt-only? | Code / policy artifact |
|---------|--------------|------------------------|
| No identity writes | | |
| Cite escalation rule ID | | |
| Refuse high blast-radius asks | | |

## Done when

- [ ] Deny list is specific enough to test  
- [ ] ≥2 intentional refusals in prove log  
- [ ] Runbooks include escalation contracts, not just steps  
