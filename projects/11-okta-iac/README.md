# M8 — Okta Identity-as-Code

**Competency:** Identity & access  
**Curriculum weeks:** 5–7, 16, 24, 36  
**Feeds:** Flagship [`../08-capstone-ops-agent/`](../08-capstone-ops-agent/), MCP reads in [`../02-okta-mcp-server/`](../02-okta-mcp-server/)

## Elevator pitch

Okta **access topology** managed with Terraform: groups, group rules, app integrations, assignments, and policies — reviewable PRs, sandbox applies, CI `terraform plan`. Agents and HITL flows operate against groups that exist in code, not shadow click-ops.

## Boundary (interview gold)

| Manage in Terraform | Not primary TF source of truth |
|---------------------|--------------------------------|
| Groups, group rules | Production joiner/mover/leaver **users** (HRIS → SCIM / CIPHER-style) |
| App integrations + group assignments | Employer production Okta |
| Sign-on / MFA / auth policies (API-manageable) | Secrets or API tokens in `.tf` / git |
| Small set of **sandbox** `tf-demo-*` users for portfolio demos | Real employee PII |

> Users lifecycle via SCIM/workflows; **access topology** (groups/apps/policies) via Terraform.

## Prereq

- Free Okta **preview/developer** org (never employer prod)  
- Okta API token with least privilege for Terraform — stored outside git (env / Secret Manager pattern from M6)

## Target layout

```
projects/11-okta-iac/
  README.md
  versions.tf
  providers.tf
  modules/
    groups/
    apps/
    policies/
    users_sandbox/
  envs/
    sandbox/
  docs/
    ACCESS-TOPOLOGY.md
    AGENT-CONTRACT.md
```

## Week ships (curriculum)

| Week | Ship |
|------|------|
| 5 | Groups (+ rules) module; `ACCESS-TOPOLOGY.md`; plan/apply sandbox |
| 6 | Apps + policies modules; document console-only gaps |
| 7 | Sandbox demo users; `AGENT-CONTRACT.md`; CIPHER boundary note |
| 16 | GitHub Actions: `terraform fmt/validate/plan` on PR |
| 24+ | Capstone demo opens with “identity topology is code” |

## Definition of done

- [ ] `terraform plan` succeeds against sandbox  
- [ ] Groups/apps/policies modules present  
- [ ] Boundary documented (this README)  
- [ ] No tokens or PII in git  
- [ ] AGENT-CONTRACT lists groups MCP may read; writes require HITL  

## Demo script (30–45s)

1. Show `ACCESS-TOPOLOGY.md` + TF group/app resources  
2. `terraform plan` clean (or intentional drift note)  
3. MCP/agent lists a `tf-demo` user / group membership from sandbox  
4. Propose group add → blocked without HITL  

## Related

- Platform / secrets: [`../10-platform-foundation/`](../10-platform-foundation/)  
- CIPHER design: [`../06-cipher/`](../06-cipher/)  
- Curriculum: [`../../CURRICULUM.md`](../../CURRICULUM.md)
