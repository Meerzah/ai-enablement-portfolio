"""Weekly mini-projects (W1–20) → capstone build (W21–24) → portfolio lane (W25–36)."""

from __future__ import annotations

# Each entry: title, project path, build steps, done_when, optional notes
MINI_PROJECTS: list[dict] = [
    {
        "title": "Run the helpdesk agent + extend runbook corpus",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Clone repo; run agent locally per README",
            "Add 2 new Markdown runbooks (VPN + SSO or MDM)",
            "Run 5 test queries; log pass vs escalate in README or notes",
        ],
        "doneWhen": [
            "Agent runs without errors",
            "2 runbooks committed under runbooks/ or docs/",
            "5-query log saved in study-notes/weeks/week-01-prove-log.md",
        ],
    },
    {
        "title": "Okta MCP server — read-only identity queries",
        "path": "projects/02-okta-mcp-server/",
        "build": [
            "Configure read-only Okta API token (preview org or sandbox)",
            "Implement or verify list_users + get_user_groups tools",
            "Run 3 MCP queries from Claude/Cursor or MCP inspector",
        ],
        "doneWhen": [
            "MCP server starts and registers tools",
            "3 sample queries documented with outputs (redact PII)",
        ],
    },
    {
        "title": "Wire agent → Okta MCP for identity-aware answers",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Connect helpdesk agent to Okta MCP tools",
            "Add system prompt rule: identity lookups are read-only",
            "Test: group membership question + user status question",
        ],
        "doneWhen": [
            "Agent calls Okta tool for at least 2 query types",
            "Escalation when write/action requested",
        ],
    },
    {
        "title": "Escalation policy + agent guardrails doc",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Write escalation-policy.md: when agent must refuse or hand off",
            "Add 3 must-escalate + 3 safe-to-answer examples",
            "Update agent prompt to cite policy",
        ],
        "doneWhen": [
            "escalation-policy.md committed",
            "1 test query per category logged",
        ],
    },
    {
        "title": "IT intake prompt playbook",
        "path": "projects/04-prompt-playbooks/",
        "build": [
            "Draft teams/it-ops.md intake prompts for non-technical requesters",
            "Cover access request + device issue + how-to question",
            "Add copy-paste Slack/form field labels",
        ],
        "doneWhen": [
            "it-ops.md committed with 3 prompt templates",
            "Linked from project README",
        ],
    },
    {
        "title": "Structured query logging for the agent",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Log each query: timestamp, query, tools_used, outcome, latency_ms",
            "JSON lines to logs/queries.jsonl (gitignore secrets)",
            "Add README section on log format",
        ],
        "doneWhen": [
            "10 sample log lines from real test runs",
            "No PII or tokens in committed logs",
        ],
    },
    {
        "title": "Tool JSON schemas + agent tool manifest",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Document JSON schema for rag_tool and okta_tool inputs/outputs",
            "Add tools/README.md with contract for each tool",
            "Validate one happy-path + one error-path call",
        ],
        "doneWhen": [
            "tools/README.md with schemas",
            "Agent respects schema on malformed tool args",
        ],
    },
    {
        "title": "Eval harness — first 5 cases",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Create evals/eval_cases.csv: query, expected_behavior, pass/fail",
            "Add 5 rows: 3 runbook, 2 identity read",
            "Run manually; log results in evals/results.md",
        ],
        "doneWhen": [
            "eval_cases.csv committed (5 rows)",
            "results.md with honest pass/fail — no invented accuracy %",
        ],
    },
    {
        "title": "Eval harness — expand to 15 cases",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Add 10 edge cases: ambiguous, OOO approver, privilege escalation attempt",
            "Update results.md after full run",
            "Note top 3 failures to fix before capstone",
        ],
        "doneWhen": [
            "15 rows in eval_cases.csv",
            "Failure list with fix plan",
        ],
    },
    {
        "title": "HITL approval gate — mock implementation",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Design flow: agent proposes action → human approves → execute",
            "Mock with CLI y/n or Slack Block Kit draft (no prod webhook required)",
            "Sequence diagram in docs/hitl-flow.md",
        ],
        "doneWhen": [
            "docs/hitl-flow.md with diagram",
            "Mock demo: blocked action without approval",
        ],
    },
    {
        "title": "HTTP API wrapper for the agent",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "FastAPI POST /query endpoint wrapping agent",
            "Request/response Pydantic models",
            "curl example in README",
        ],
        "doneWhen": [
            "/query returns answer + tools_used",
            "Health check endpoint",
        ],
    },
    {
        "title": "Audit log schema + write path",
        "path": "projects/05-adoption-dashboard/",
        "build": [
            "Define audit event: actor, action, resource, ticket_id, timestamp, approved_by",
            "Implement file or Firestore stub writer",
            "Wire one mock approved action to audit log",
        ],
        "doneWhen": [
            "schema.md committed",
            "Sample audit events from test run",
        ],
    },
    {
        "title": "Idempotent webhook handler pattern",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Add webhook stub POST /hooks/ticket with idempotency key header",
            "Document retry behavior in docs/reliability.md",
            "Test duplicate delivery returns same response",
        ],
        "doneWhen": [
            "docs/reliability.md",
            "Duplicate POST test logged",
        ],
    },
    {
        "title": "Failure alerts — design + test payload",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Define Slack alert JSON for agent/tool failures",
            "Simulate failure path; print alert payload",
            "Runbook snippet: what on-call does",
        ],
        "doneWhen": [
            "docs/failure-alerts.md with sample payload",
            "Runbook linked from alert template",
        ],
    },
    {
        "title": "Agentspace rollout checklist v1",
        "path": "projects/03-agentspace-rollout/",
        "build": [
            "Complete rollout checklist for 1 team (identity + data scope)",
            "Pilot success criteria (adoption, not fake CSAT)",
            "Risk register: 3 items + mitigations",
        ],
        "doneWhen": [
            "checklist.md committed",
            "Pilot scope documented",
        ],
    },
    {
        "title": "Adoption metrics event schema",
        "path": "projects/05-adoption-dashboard/",
        "build": [
            "Define events: query_submitted, tool_called, escalated, approved",
            "Map to BigQuery-friendly fields",
            "Emit sample events from agent logging",
        ],
        "doneWhen": [
            "events-schema.md",
            "Sample JSONL aligned with Week 6 logs",
        ],
    },
    {
        "title": "Usage dashboard stub",
        "path": "projects/05-adoption-dashboard/",
        "build": [
            "Simple script or SQL: queries per day, escalation rate (from logs)",
            "No invented numbers — use your test log data only",
            "Screenshot or terminal output in docs/",
        ],
        "doneWhen": [
            "Query script runs on sample logs",
            "README updated with how to run",
        ],
    },
    {
        "title": "Ops KB index + grounding rules",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "study-notes/ops-kb-index.md listing runbooks + owners",
            "Grounding rules: cite source, say when KB miss",
            "Update agent prompt with citation format",
        ],
        "doneWhen": [
            "ops-kb-index.md committed",
            "Agent cites runbook in 2 test answers",
        ],
    },
    {
        "title": "End-to-end integration demo",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Scripted demo: runbook Q → identity Q → escalation → HITL mock → audit log",
            "Record terminal session or write demo-script.md step-by-step",
            "2-minute talk track",
        ],
        "doneWhen": [
            "demo-script.md",
            "All components touched in one flow",
        ],
    },
    {
        "title": "Capstone scaffold + architecture",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "Create capstone repo folder with ARCHITECTURE.md",
            "Diagram: API + agent + MCP + HITL + audit + metrics",
            "List what migrates from mini-projects 01–05",
        ],
        "doneWhen": [
            "projects/08-capstone-ops-agent/ committed",
            "Architecture reviewed against eval failures from W9",
        ],
    },
]

CAPSTONE_WEEKS = [
    {
        "title": "Capstone W1 — Core platform assembly",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "Merge agent + MCP + FastAPI into capstone service layout",
            "Single docker-compose or local run script",
            "Port eval suite to capstone repo",
        ],
        "doneWhen": [
            "One command starts API + agent",
            "5 eval cases pass in capstone repo",
        ],
    },
    {
        "title": "Capstone W2 — HITL + policy enforcement",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "Implement approval gate before any side-effect tool",
            "Load escalation-policy.md as enforced rules",
            "Reject privilege escalation test cases",
        ],
        "doneWhen": [
            "Unapproved writes blocked in tests",
            "Approval flow in ARCHITECTURE.md updated",
        ],
    },
    {
        "title": "Capstone W3 — Audit trail + observability",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "Wire audit log + adoption events on every query",
            "Failure alert hook on tool errors",
            "Dashboard script reads capstone logs",
        ],
        "doneWhen": [
            "Audit + metrics emitted for full demo flow",
            "Reliability docs ported from mini-projects",
        ],
    },
    {
        "title": "Capstone W4 — Deploy POC + case study draft",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "Cloud Run deploy POC (or documented deploy script)",
            "study-notes/capstone-case-study.md — honest POC status",
            "Update portfolio README with capstone link",
        ],
        "doneWhen": [
            "Deploy instructions in capstone README",
            "Case study: problem → architecture → eval results → limits",
        ],
    },
]

PORTFOLIO_WEEKS = [
    {
        "title": "Capstone demo polish + 2-min walkthrough",
        "path": "projects/08-capstone-ops-agent/",
        "build": ["Record or script demo", "Fix top 3 eval failures", "README hero section"],
        "doneWhen": ["demo-script.md updated", "README has architecture diagram"],
    },
    {
        "title": "Portfolio narrative + LinkedIn post draft",
        "path": "study-notes/",
        "build": ["Write platform-bridge.md update", "Link shipped work + capstone", "Draft LinkedIn post"],
        "doneWhen": ["platform-bridge.md committed", "Post draft in study-notes/"],
    },
    {
        "title": "Consulting one-pager (offers a/b/c)",
        "path": "CONTEXT.md",
        "build": ["study-notes/consulting-one-pager.md", "Scope fixed-fee offers from CONTEXT", "No invented client metrics"],
        "doneWhen": ["One-pager committed", "3 offers scoped"],
    },
    {
        "title": "Metrics baseline documentation",
        "path": "projects/05-adoption-dashboard/",
        "build": ["study-notes/metrics-baseline.md", "Hours-saved formula with YOUR volume only", "Tie to capstone logs"],
        "doneWhen": ["Baseline doc with real numbers or TBD placeholders"],
    },
    {
        "title": "System design practice #1 — access automation",
        "path": "interview-prep/",
        "build": ["45-min timed design: access request automation", "Use system-design-template.md", "Save to interview-prep/answers/"],
        "doneWhen": ["Written design doc committed"],
    },
    {
        "title": "System design practice #2 — agent identity",
        "path": "interview-prep/",
        "build": ["Timed design: agent service accounts + WIF", "Reference wif-agent-identity-design.md", "Save answer"],
        "doneWhen": ["Design doc committed"],
    },
    {
        "title": "STAR stories + resume bullets",
        "path": "interview-prep/answers/behavioral-star.md",
        "build": ["Fill STAR for Slack automation, capstone, identity work", "Update resume bullets", "Align to AI Systems framing"],
        "doneWhen": ["behavioral-star.md updated"],
    },
    {
        "title": "Mock interview block",
        "path": "interview-prep/",
        "build": ["1 system design aloud", "1 STAR aloud", "1 capstone demo rehearsal"],
        "doneWhen": ["Self-score rubric in wave-1-checklist.md"],
    },
    {
        "title": "Apply tracker + 3 targets",
        "path": "interview-prep/answers/wave-1-checklist.md",
        "build": ["Company research notes", "Tailor resume per target", "Apply tracker spreadsheet or md table"],
        "doneWhen": ["3 companies researched", "Tracker started"],
    },
    {
        "title": "Submit applications + outreach",
        "path": "interview-prep/",
        "build": ["Submit 1+ applications", "1 LinkedIn outreach", "Refine case study from any feedback"],
        "doneWhen": ["Apply log updated", "Case study v2 if needed"],
    },
    {
        "title": "Portfolio retro + next quarter plan",
        "path": "study-notes/",
        "build": ["study-notes/program-retro.md", "What shipped vs planned", "Next 90-day focus"],
        "doneWhen": ["Retro committed", "README counters honest"],
    },
    {
        "title": "Program complete — maintain cadence",
        "path": "projects/08-capstone-ops-agent/",
        "build": ["Keep capstone runnable", "Monthly eval re-run", "Iterate from interview feedback"],
        "doneWhen": ["Capstone still runs", "Next milestone defined"],
    },
]


def get_week_plan(week: int) -> dict | None:
    if 1 <= week <= 20:
        p = MINI_PROJECTS[week - 1]
        return {
            "title": p["title"],
            "miniProject": p,
            "phase": "mini",
        }
    if 21 <= week <= 24:
        p = CAPSTONE_WEEKS[week - 21]
        return {
            "title": p["title"],
            "miniProject": p,
            "phase": "capstone",
        }
    if 25 <= week <= 36:
        p = PORTFOLIO_WEEKS[week - 25]
        return {
            "title": p["title"],
            "miniProject": p,
            "phase": "portfolio",
        }
    return None
