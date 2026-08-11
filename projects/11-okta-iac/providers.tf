# Sandbox / preview Okta org only. Never point at employer production.
# Credentials via env: OKTA_ORG_NAME, OKTA_BASE_URL, OKTA_API_TOKEN

provider "okta" {
  # org_name  = var.okta_org_name
  # base_url  = var.okta_base_url
  # api_token = var.okta_api_token
}
