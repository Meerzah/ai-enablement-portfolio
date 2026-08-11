# Workload Identity Federation (preferred)

Do **not** commit GCP service account JSON keys.

## Pattern for this portfolio

1. GitHub Actions authenticates to GCP via WIF (pool + provider).  
2. Cloud Run runtime SA has least privilege (Secret Manager accessor, logging).  
3. Okta API token lives in Secret Manager; mounted or fetched at runtime — never in git.

## Week 8 deliverable

Document the intended SA roles and secret names even if WIF pool is created later.
