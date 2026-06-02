# IT Helpdesk Agent

> An AI agent that answers IT questions from internal runbooks using Google ADK and Vertex AI.

---

## Problem

IT teams spend a disproportionate amount of time answering the same questions repeatedly — VPN setup, MDM enrollment, SSO troubleshooting, access requests. The answers exist in runbooks. Nobody reads the runbooks.

## Solution

A RAG-powered agent that ingests Markdown runbooks and answers natural language queries via CLI. Built on Google ADK, deployed on Vertex AI, with an MCP server exposing Okta read tools so it can answer identity-specific questions in context.

## Architecture

```
User query (CLI)
      │
      ▼
Google ADK Agent
      │
      ├── RAG Tool ──► Vertex AI Vector Search ──► Runbook chunks
      │
      ├── Okta MCP Tool ──► Okta API (read-only)
      │                     └── list users, get groups, check status
      │
      └── Gemini 1.5 Pro (reasoning + response generation)
```

## Stack

- **Google ADK** — agent framework, tool orchestration
- **Vertex AI** — model hosting, vector search for RAG
- **Gemini 1.5 Pro** — reasoning model
- **MCP** — Okta integration layer
- **Python 3.11+**

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/ai-enablement-portfolio
cd projects/01-it-helpdesk-agent
pip install -r requirements.txt

# Set env vars
export GOOGLE_CLOUD_PROJECT=your-project-id
export OKTA_DOMAIN=yourorg.okta.com
export OKTA_API_TOKEN=your-token

# Ingest runbooks
python ingest.py --source ./runbooks/

# Run agent
python agent.py
```

## Example queries

```
> Who is in the IT admin group?
  → Okta MCP tool called → returns current group members

> How do I enroll my Mac in MDM?
  → RAG retrieval → MDM enrollment runbook → step-by-step response

> My SSO login is failing, what should I check?
  → RAG retrieval → SSO troubleshooting runbook → diagnosis steps
```

## Adoption notes

See [ROLLOUT.md](./ROLLOUT.md) for how this was deployed internally, what friction looked like, and what usage metrics resulted.

## Files

```
01-it-helpdesk-agent/
├── agent.py          # Main agent entrypoint
├── ingest.py         # Runbook ingestion + vector indexing
├── tools/
│   ├── rag_tool.py   # Vertex AI vector search wrapper
│   └── okta_tool.py  # Okta MCP tool definitions
├── runbooks/         # Sample runbooks (sanitized)
├── requirements.txt
└── ROLLOUT.md        # Adoption story + metrics
```
