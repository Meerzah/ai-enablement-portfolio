"""
Okta MCP Tool — read-only Okta API tools exposed as ADK FunctionTools
Week 11 project: MCP server wrapping Okta read APIs
"""

import os
import requests
from typing import Optional


OKTA_DOMAIN = os.environ.get("OKTA_DOMAIN", "")
OKTA_API_TOKEN = os.environ.get("OKTA_API_TOKEN", "")

HEADERS = {
    "Authorization": f"SSWS {OKTA_API_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_okta_group_members(group_name: str) -> dict:
    """
    Returns the list of active members in a named Okta group.

    Args:
        group_name: The display name of the Okta group to look up.

    Returns:
        A dict with 'group' (name) and 'members' (list of display names + emails).
    """
    # Search for the group by name
    search_url = f"https://{OKTA_DOMAIN}/api/v1/groups?q={group_name}&limit=5"
    groups_resp = requests.get(search_url, headers=HEADERS)
    groups_resp.raise_for_status()
    groups = groups_resp.json()

    if not groups:
        return {"error": f"No group found matching '{group_name}'"}

    group = groups[0]
    group_id = group["id"]
    group_display = group["profile"]["name"]

    # Fetch members
    members_url = f"https://{OKTA_DOMAIN}/api/v1/groups/{group_id}/users?limit=100"
    members_resp = requests.get(members_url, headers=HEADERS)
    members_resp.raise_for_status()
    users = members_resp.json()

    members = [
        {
            "name": f"{u['profile'].get('firstName','')} {u['profile'].get('lastName','')}".strip(),
            "email": u["profile"].get("email", ""),
            "status": u.get("status", ""),
        }
        for u in users
        if u.get("status") == "ACTIVE"
    ]

    return {"group": group_display, "members": members, "count": len(members)}


def get_user_status(email: str) -> dict:
    """
    Returns the account status of a user by email address.

    Args:
        email: The user's email address.

    Returns:
        A dict with name, email, status, and last login info.
    """
    search_url = f"https://{OKTA_DOMAIN}/api/v1/users/{email}"
    resp = requests.get(search_url, headers=HEADERS)

    if resp.status_code == 404:
        return {"error": f"No user found with email '{email}'"}

    resp.raise_for_status()
    user = resp.json()
    profile = user.get("profile", {})

    return {
        "name": f"{profile.get('firstName','')} {profile.get('lastName','')}".strip(),
        "email": profile.get("email", ""),
        "status": user.get("status", ""),
        "last_login": user.get("lastLogin", "never"),
        "created": user.get("created", ""),
    }
