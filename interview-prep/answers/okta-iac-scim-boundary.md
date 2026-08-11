# System design — Okta-as-code + SCIM boundary

**Prompt:** Design how an organization should manage Okta with Terraform while still running joiner/mover/leaver at scale. Where do agents and HITL fit?

**Target week:** 29 (portfolio phase)  
**Platform tie:** `projects/11-okta-iac/`, CIPHER design, capstone HITL

## Sketch (fill in timed practice)

### Goals

- Declarative access topology (reviewable, drift-detectable)  
- Automated user lifecycle from HR  
- Agents propose changes; humans approve privileged writes  

### Split of ownership

| Concern | System of record |
|---------|------------------|
| Users / lifecycle | HRIS → SCIM / workflow automation |
| Groups, apps, policies, assignments | Terraform (Okta provider) |
| Exception / break-glass | Documented; time-bounded |
| Agent identity reads | MCP read-only token |
| Membership changes from tickets | Deterministic executor after HITL |

### Failure modes

- Drift: click-ops vs TF state → CI plan + ownership  
- Agent invents non-existent group → allow-list IaC-known groups only  
- Token sprawl → Secret Manager / short-lived creds  

### Honest limits for portfolio

Sandbox Okta only; no employer prod state in public repo.
