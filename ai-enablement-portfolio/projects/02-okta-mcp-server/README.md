# Okta MCP Server

> A Model Context Protocol server that exposes Okta read operations as AI-callable tools.

---

## What this does

Wraps the Okta API in MCP so any MCP-compatible AI agent (Claude, Gemini via ADK, Antigravity) can query your identity system in natural language without direct API access.

**Read-only by design.** No write operations. Safe to connect to production Okta.

## Tools exposed

| Tool | Description |
|------|-------------|
| `list_users` | List users with optional filter by status or group |
| `get_user` | Get a user's profile and account status by email |
| `list_groups` | List groups, optionally filtered by name |
| `get_group_members` | Get active members of a named group |
| `get_user_groups` | Get all groups a user belongs to |
| `check_app_assignment` | Check if a user is assigned to a specific app |

## Setup

```bash
cd projects/02-okta-mcp-server
pip install -r requirements.txt

export OKTA_DOMAIN=yourorg.okta.com
export OKTA_API_TOKEN=your-readonly-api-token

python server.py
```

## Connecting to an agent

```python
# Google ADK example
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

mcp_tools = MCPToolset(
    connection_params=StdioServerParameters(
        command="python",
        args=["path/to/02-okta-mcp-server/server.py"],
    )
)
```

## Example queries (via agent)

```
"Who is in the engineering-leads group?"
"Is sarah@company.com active in Okta?"
"What groups does john@company.com belong to?"
"Is the Slack app assigned to the IT team group?"
```

## Security notes

- Uses a read-only Okta API token — scope to read permissions only
- No user data is stored or logged by this server
- Intended for internal use by authorized IT/ops tooling

## Files

```
02-okta-mcp-server/
├── server.py         # MCP server entrypoint
├── src/
│   ├── tools.py      # Tool definitions
│   └── okta_client.py # Okta API wrapper
├── requirements.txt
└── ROLLOUT.md
```
