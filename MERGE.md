# Merge summary — Meerzah portfolio + Ai-Systems roadmap

Comparison of what was combined, kept, and removed when merging into **Meerzah/ai-systems-portfolio**.

## Sources

| Repo | Role before merge |
|------|-------------------|
| [Meerzah/ai-enablement-portfolio](https://github.com/Meerzah/ai-enablement-portfolio) | Runnable portfolio projects (ADK, MCP, Agentspace) |
| [hujjati/Ai-Systems-roadmap](https://github.com/hujjati/Ai-Systems-roadmap) | 36-week tracker, phases, interview prep, CIPHER/ALIUS design notes |

## Kept

| From Meerzah | From Ai-Systems |
|--------------|---------------|
| `projects/01–05` code + READMEs | `tracker/` dashboard + 36-week spine |
| Badge-style README layout (updated copy) | `phases/`, `interview-prep/`, `study-notes/` |
| Per-project setup patterns | `CONTEXT.md`, `CLAUDE.md`, GitHub Pages workflow |

## Added

| Item | Location |
|------|----------|
| CIPHER design | `projects/06-cipher/` |
| ALIUS design | `projects/07-alius/` |
| Landing page | `index.html` → Projects \| Dashboard \| Interview prep |
| Merge doc | This file |
| Week 1 Prove link | Dashboard → `projects/01-it-helpdesk-agent/` |

## Removed / archived

| Item | Action |
|------|--------|
| Duplicate 12-month SETUP week map | Replaced with `tracker/` as source of truth |
| `hujjati/Ai-Systems-roadmap` | Archived — README points here |
| Old enablement-only positioning | Unified under AI Systems / Agentic Ops |
| Salary figures | Not in public docs |

## Unified positioning

**AI Systems / Agentic Ops Engineer** — identity-backed automation and agent-ready internal ops workflows.

Portfolio proof: Google ADK · Vertex · MCP · Agentspace + AppLovin shipped automation (Slack, n8n, Argus, Okta/Lumos).

## URLs

| Resource | URL |
|----------|-----|
| Repo | https://github.com/Meerzah/ai-systems-portfolio |
| Landing | https://meerzah.github.io/ai-systems-portfolio/ |
| Dashboard | https://meerzah.github.io/ai-systems-portfolio/tracker/ |

## Project ↔ tracker mapping

| Tracker | Portfolio artifact |
|---------|-------------------|
| Week 1 Prove | `projects/01-it-helpdesk-agent/` |
| Unit 3 (W9–12) | `01-it-helpdesk-agent` + `02-okta-mcp-server` |
| Month 2 capstone | `projects/06-cipher/` |
| Month 3 capstone | Agentic triage case (projects 01+02) |
| Unit 7 (W25–28) | `05-adoption-dashboard` + consulting menu |
| Month 4+ | `projects/07-alius/` design |
