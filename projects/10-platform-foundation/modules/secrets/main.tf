# Placeholder pattern: store Okta API token / agent secrets in Secret Manager.
# Do not put secret values in Terraform variables committed to git.
#
# resource "google_secret_manager_secret" "okta_api_token" {
#   secret_id = "okta-api-token-${var.environment}"
#   replication {
#     auto {}
#   }
# }

variable "environment" {
  type    = string
  default = "sandbox"
}

output "placeholder" {
  value = "Week 8: uncomment Secret Manager resources; add secret versions out-of-band."
}
