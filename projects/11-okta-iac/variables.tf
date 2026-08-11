variable "okta_org_name" {
  type        = string
  description = "Okta org subdomain (preview/sandbox only)"
  default     = ""
}

variable "okta_base_url" {
  type        = string
  description = "Okta base URL host (e.g. okta.com or oktapreview.com)"
  default     = "oktapreview.com"
}

variable "okta_api_token" {
  type        = string
  description = "API token — set via TF_VAR_okta_api_token or env; never commit"
  sensitive   = true
  default     = ""
}

variable "environment" {
  type        = string
  description = "Logical environment label"
  default     = "sandbox"
}
