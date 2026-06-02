"""
IT Helpdesk Agent — Google ADK + Vertex AI RAG + Okta MCP
Week 8 / Week 12 capstone project
"""

import os
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from tools.rag_tool import search_runbooks
from tools.okta_tool import get_okta_group_members, get_user_status

SYSTEM_PROMPT = """
You are an IT helpdesk assistant. You help employees with IT questions by:
1. Searching internal runbooks for step-by-step guidance
2. Looking up identity and access information from Okta when asked about users or groups

Always be concise. If you are not confident in an answer, say so and recommend
the employee open a ticket with the IT team.

You have access to:
- search_runbooks: search internal IT documentation
- get_okta_group_members: list members of an Okta group
- get_user_status: check if a user account is active
"""

def build_agent() -> Agent:
    tools = [
        FunctionTool(search_runbooks),
        FunctionTool(get_okta_group_members),
        FunctionTool(get_user_status),
    ]

    agent = Agent(
        name="it-helpdesk",
        model="gemini-1.5-pro",
        instruction=SYSTEM_PROMPT,
        tools=tools,
    )
    return agent


def main():
    agent = build_agent()
    print("IT Helpdesk Agent ready. Type your question or 'exit' to quit.\n")

    while True:
        query = input("> ").strip()
        if query.lower() in ("exit", "quit"):
            break
        if not query:
            continue

        response = agent.run(query)
        print(f"\n{response.text}\n")


if __name__ == "__main__":
    main()
