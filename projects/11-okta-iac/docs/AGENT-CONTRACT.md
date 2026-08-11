# Agent contract (identity)

What the ops agent / Okta MCP may do against the sandbox topology in `11-okta-iac`.

## Allowed (read)

- List/get users (prefer `tf-demo-*` in demos; redact PII in logs)  
- List group members for Terraform-managed groups  
- Read app assignment status for demo apps  

## Denied without HITL

- Add/remove group membership  
- Assign/unassign apps  
- Change policies  
- Create/deactivate users  

## Writes (future / capstone)

1. Agent proposes change against an **IaC-known** group/app only  
2. HITL approver in `role-it-approvers` (or mock CLI)  
3. Deterministic executor applies change  
4. Audit event: actor, action, resource, approved_by, timestamp  

## Token posture

- MCP: read-only Okta API token  
- Terraform: separate least-privilege token; never in git  
- Prefer Secret Manager pattern from `10-platform-foundation`  
