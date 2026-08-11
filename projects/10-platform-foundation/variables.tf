variable "project_id" {
  type        = string
  description = "GCP project for sandbox agent platform"
  default     = ""
}

variable "region" {
  type        = string
  description = "Default region for Cloud Run / Artifact Registry"
  default     = "us-west1"
}

variable "environment" {
  type        = string
  default     = "sandbox"
}
