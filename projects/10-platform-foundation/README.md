# M6 — Platform Foundation (GCP IaC + CI)

**Competency:** Cloud platform & delivery  
**Curriculum weeks:** 8, 12, 16, 24 (and supporting work)  
**Feeds:** Flagship [`../08-capstone-ops-agent/`](../08-capstone-ops-agent/)

## Elevator pitch

Terraform + GitHub Actions for the agent control plane on GCP: Cloud Run, IAM, Secret Manager, Artifact Registry — so the ops agent is **delivered as infrastructure**, not a laptop demo.

## Scope

| In | Out |
|----|-----|
| Cloud Run service module | Multi-cluster Kubernetes platform |
| Service accounts + least-privilege IAM | Long-lived SA JSON keys in git |
| Secret Manager placeholders (Okta/agent tokens) | Real secrets committed |
| Artifact Registry + CI build/push | Kafka / full observability stack zoo |
| Documented WIF pattern | AWS |

## Target layout

```
projects/10-platform-foundation/
  README.md
  versions.tf
  providers.tf
  modules/
    cloud_run/
    iam/
    secrets/
    artifact_registry/
  envs/
    sandbox/
  docs/
    WIF.md
    DEPLOY.md
  .github/workflows/   # or repo-root workflow referencing this path
```

## Definition of done (curriculum)

- [ ] `terraform init` + `validate` on sandbox env  
- [ ] Secrets pattern documented (Okta API token → Secret Manager)  
- [ ] CI builds/pushes image or documents blocker  
- [ ] Capstone can point deploy instructions here  

## Related

- Okta Identity-as-Code: [`../11-okta-iac/`](../11-okta-iac/)  
- Capstone: [`../08-capstone-ops-agent/`](../08-capstone-ops-agent/)  
- Tradeoff memo: `study-notes/cloud-platform/run-vs-gke.md` (Week 19)
