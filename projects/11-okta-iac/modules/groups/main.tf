# Example group resources — enable when sandbox credentials are configured.
# resource "okta_group" "agent_read_identity" {
#   name        = "agent-read-identity"
#   description = "Marker group: MCP/agent may read identity for these scopes"
# }
#
# resource "okta_group" "role_it_approvers" {
#   name        = "role-it-approvers"
#   description = "Humans who may approve HITL write proposals"
# }

output "placeholder" {
  value = "Uncomment okta_group resources after provider credentials are set (Week 5)."
}
