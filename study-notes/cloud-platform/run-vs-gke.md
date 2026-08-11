# Cloud Run vs GKE for agent workloads

**Week 19 theme.** Fill during the lab; default recommendation for this portfolio: **Cloud Run**.

## Decision criteria

| Factor | Cloud Run | GKE / Kubernetes |
|--------|-----------|------------------|
| Ops overhead | Low | Higher (cluster, upgrades, networking) |
| Scale-to-zero | Native | Possible, more config |
| Identity | Easy WIF + SA per service | Workload Identity; more moving parts |
| Progressive delivery | Revisions + traffic split | Native (and richer) with mesh/GitOps |
| When agents need it | Request/response APIs, webhooks | Long-running workers, complex mesh, multi-tenant cluster product |

## Lab notes

- Optional: `kind` local cluster hello deploy — notes below  
- Optional: GKE Autopilot touch — notes below  

(Add commands and screenshots as you complete Week 19.)

## Capstone default

**Host the Agentic Ops Control Plane API on Cloud Run** via `projects/10-platform-foundation/`. Keep K8s literacy for interviews; do not make cluster operations the spine.
