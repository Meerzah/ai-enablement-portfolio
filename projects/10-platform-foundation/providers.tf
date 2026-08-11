# Dev/sandbox GCP project. Prefer WIF over SA keys.
# export GOOGLE_PROJECT=... or set var.project_id

provider "google" {
  project = var.project_id
  region  = var.region
}
