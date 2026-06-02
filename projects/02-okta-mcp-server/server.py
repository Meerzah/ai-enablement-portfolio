"""
Okta MCP Server
Exposes read-only Okta operations as MCP tools for AI agents.

Week 10–11 project: MCP server wrapping Okta read APIs
"""

import asyncio
import os
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types
from src.tools import (
    list_users,
    get_user,
    list_groups,
    get_group_members,
    get_user_groups,
    check_app_assignment,
)

app = Server("okta-mcp-server")

TOOLS = [
    types.Tool(
        name="list_users",
        description="List Okta users, optionally filtered by status (ACTIVE, DEPROVISIONED) or group name.",
        inputSchema={
            "type": "object",
            "properties": {
                "status": {"type": "string", "description": "Filter by status: ACTIVE, STAGED, DEPROVISIONED"},
                "group_name": {"type": "string", "description": "Filter users in a specific group"},
                "limit": {"type": "integer", "description": "Max users to return (default 25, max 100)"},
            },
        },
    ),
    types.Tool(
        name="get_user",
        description="Get a user's profile, account status, and last login by email address.",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "The user's email address"},
            },
            "required": ["email"],
        },
    ),
    types.Tool(
        name="list_groups",
        description="List Okta groups, optionally filtered by name.",
        inputSchema={
            "type": "object",
            "properties": {
                "name_filter": {"type": "string", "description": "Partial group name to search for"},
                "limit": {"type": "integer", "description": "Max groups to return (default 25)"},
            },
        },
    ),
    types.Tool(
        name="get_group_members",
        description="Get the active members of a named Okta group.",
        inputSchema={
            "type": "object",
            "properties": {
                "group_name": {"type": "string", "description": "The group display name to look up"},
            },
            "required": ["group_name"],
        },
    ),
    types.Tool(
        name="get_user_groups",
        description="Get all Okta groups a user belongs to.",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "The user's email address"},
            },
            "required": ["email"],
        },
    ),
    types.Tool(
        name="check_app_assignment",
        description="Check if a user is assigned to a specific Okta application.",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "The user's email address"},
                "app_name": {"type": "string", "description": "The application label to check"},
            },
            "required": ["email", "app_name"],
        },
    ),
]


@app.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return TOOLS


@app.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    handlers = {
        "list_users": list_users,
        "get_user": get_user,
        "list_groups": list_groups,
        "get_group_members": get_group_members,
        "get_user_groups": get_user_groups,
        "check_app_assignment": check_app_assignment,
    }

    if name not in handlers:
        raise ValueError(f"Unknown tool: {name}")

    result = handlers[name](**arguments)
    return [types.TextContent(type="text", text=str(result))]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
