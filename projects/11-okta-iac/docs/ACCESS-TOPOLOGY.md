# Access topology (Okta IaC)

Sandbox diagram for portfolio demos. Apply only to Okta **preview/developer** org.

## Intended groups (Week 5+)

| Group | Purpose |
|-------|---------|
| `tf-app-*` | App access groups assigned to OIDC/SAML apps in Terraform |
| `role-it-approvers` | Humans who may approve HITL write proposals |
| `agent-read-identity` | Scope marker for read-only agent/MCP identity queries |

## Flow

```
HRIS / SCIM (user lifecycle)
        │
        ▼
   Okta users ──────────► group rules (optional attributes)
        │
        ▼
   Terraform-managed groups ──► app assignments ──► policies (sign-on / MFA)
        │
        ▼
   Agent MCP (read) + HITL (propose membership changes)
```

## Boundary

- **Terraform:** groups, rules, apps, assignments, policies, sandbox `tf-demo-*` users  
- **Not TF primary:** production employee lifecycle (use SCIM / CIPHER-style automation)
