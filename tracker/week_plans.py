"""36-week curriculum: competency-aligned mini-projects → capstone → portfolio."""

from __future__ import annotations

# competency: harness | identity | endpoint | enablement | workflow | ops | portfolio

MINI_PROJECTS: list[dict] = [
    # ── Phase 1: Agent harness foundation (W1–4) ──
    {
        "title": "Run helpdesk agent + extend runbook corpus",
        "competency": "harness",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Set up Python venv; install requirements.txt",
            "Add 2 Markdown runbooks (VPN, SSO, or MDM)",
            "Run 5 test queries; log results",
        ],
        "doneWhen": [
            "Agent starts (or document blocker + workaround in prove log)",
            "2 runbooks committed",
            "study-notes/weeks/week-01-prove-log.md filled",
        ],
    },
    {
        "title": "Okta MCP — read-only identity tools",
        "competency": "identity",
        "path": "projects/02-okta-mcp-server/",
        "build": [
            "Configure read-only Okta API token (preview/sandbox org)",
            "Verify list_users + get_group_members tools",
            "Document 3 sample queries (redact PII)",
        ],
        "doneWhen": ["MCP server runs", "3 queries logged in project README or notes"],
    },
    {
        "title": "Connect agent → Okta MCP (read-only)",
        "competency": "harness",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Wire agent to Okta MCP tools",
            "System prompt: identity lookups read-only; escalate writes",
            "Test group membership + user status queries",
        ],
        "doneWhen": ["2+ identity query types work", "Write attempt triggers escalation"],
    },
    {
        "title": "Escalation policy + agent guardrails",
        "competency": "harness",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Write docs/escalation-policy.md",
            "3 must-escalate + 3 safe-to-answer examples",
            "Update agent system prompt to cite policy",
        ],
        "doneWhen": ["escalation-policy.md committed", "6 examples tested and logged"],
    },
    # ── Phase 2: Identity depth (W5–8) ──
    {
        "title": "Agent identity design (WIF / SPIFFE concepts)",
        "competency": "identity",
        "path": "study-notes/wif-agent-identity-design.md",
        "build": [
            "Read GCP Agent Identity overview",
            "Update wif-agent-identity-design.md: human vs NHI vs agent principal",
            "Diagram: read-only MCP vs write via approved workflow",
        ],
        "doneWhen": ["Design doc updated", "Least-privilege table for capstone tools"],
    },
    {
        "title": "Audit log schema for automated actions",
        "competency": "identity",
        "path": "projects/05-adoption-dashboard/",
        "build": [
            "Define audit event: actor, action, resource, ticket_id, approved_by, timestamp",
            "Add schema.md + sample JSON events",
            "Map fields to future capstone audit writer",
        ],
        "doneWhen": ["schema.md committed", "3 sample events from mock approval flow"],
    },
    {
        "title": "Access automation design (CIPHER Phase 1)",
        "competency": "identity",
        "path": "projects/06-cipher/",
        "build": [
            "Read SHIP-PLAN.md; complete Phase 1 checklist items you can do in design",
            "Document intake → HITL → Okta write boundary",
            "Honest status: architected, not production shipped",
        ],
        "doneWhen": ["Phase 1 section updated in SHIP-PLAN or design note", "Sequence diagram added"],
    },
    {
        "title": "IT intake prompt playbook",
        "competency": "enablement",
        "path": "projects/04-prompt-playbooks/",
        "build": [
            "Complete teams/it-ops.md: access, device, how-to prompts",
            "Slack/form field labels for non-technical requesters",
            "Link from project README",
        ],
        "doneWhen": ["3 prompt templates committed", "Usable by a non-engineer"],
    },
    # ── Phase 3: Workflow automation (W9–12) ──
    {
        "title": "HITL approval gate — mock implementation",
        "competency": "workflow",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "docs/hitl-flow.md with sequence diagram",
            "Mock approval: CLI y/n or Slack Block Kit draft",
            "Block side-effect without approval",
        ],
        "doneWhen": ["Demo: action blocked without approval", "Diagram committed"],
    },
    {
        "title": "HTTP API wrapper for the agent",
        "competency": "workflow",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "FastAPI POST /query with Pydantic models",
            "Return answer + tools_used + escalated flag",
            "curl example in README",
        ],
        "doneWhen": ["/query works locally", "Health check endpoint"],
    },
    {
        "title": "Idempotent webhook handler",
        "competency": "workflow",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "POST /hooks/ticket with Idempotency-Key header",
            "docs/reliability.md: retry + duplicate handling",
            "Test duplicate POST returns same response",
        ],
        "doneWhen": ["Reliability doc + test log"],
    },
    {
        "title": "Tool schemas + manifest",
        "competency": "harness",
        "path": "projects/01-it-helpdesk-agent/tools/",
        "build": [
            "tools/README.md with JSON schemas for each tool",
            "Happy path + error path test per tool",
            "Agent handles malformed args gracefully",
        ],
        "doneWhen": ["Schema doc committed", "Error path logged"],
    },
    # ── Phase 4: Enablement + ops (W13–16) ──
    {
        "title": "Eval harness — 5 cases",
        "competency": "ops",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "evals/eval_cases.csv: query, expected_behavior, pass/fail",
            "5 rows: runbook + identity read",
            "evals/results.md with honest outcomes",
        ],
        "doneWhen": ["CSV + results committed", "No invented accuracy %"],
    },
    {
        "title": "Eval harness — expand to 15 cases",
        "competency": "ops",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "Add edge cases: privilege escalation, ambiguous user, KB miss",
            "Top 3 failures → fix plan before capstone",
        ],
        "doneWhen": ["15 rows in CSV", "Failure analysis in results.md"],
    },
    {
        "title": "Agentspace / team rollout checklist",
        "competency": "enablement",
        "path": "projects/03-agentspace-rollout/",
        "build": [
            "Rollout checklist: identity scope, data boundaries, pilot criteria",
            "Risk register: 3 items + mitigations",
            "Success metrics you can actually measure",
        ],
        "doneWhen": ["checklist.md committed", "Pilot scope documented"],
    },
    {
        "title": "Adoption metrics + usage dashboard stub",
        "competency": "enablement",
        "path": "projects/05-adoption-dashboard/",
        "build": [
            "events-schema.md: query_submitted, tool_called, escalated, approved",
            "Script: queries/day + escalation rate from sample logs only",
            "README: how to run on test data",
        ],
        "doneWhen": ["Schema + script run on your test logs", "Screenshot or terminal output saved"],
    },
    # ── Phase 5: Endpoint + integration (W17–20) ──
    {
        "title": "Endpoint AI governance policy",
        "competency": "endpoint",
        "path": "projects/09-endpoint-ai-governance/",
        "build": [
            "POLICY.md: approved vs prohibited AI tool categories",
            "MDM-ROLLOUT-CHECKLIST.md (generic, no employer URLs)",
            "Link identity groups → allowed tool tiers",
        ],
        "doneWhen": ["Both docs committed", "No internal employer data"],
    },
    {
        "title": "Offboarding orchestration design (ALIUS)",
        "competency": "endpoint",
        "path": "projects/07-alius/",
        "build": [
            "Review ARCHITECTURE.md",
            "Add diagram: device wipe + Okta deactivate + SaaS revoke order",
            "Note where agent assists vs deterministic steps",
        ],
        "doneWhen": ["Updated architecture section", "Honest planning status"],
    },
    {
        "title": "Ops KB index + grounding rules",
        "competency": "enablement",
        "path": "projects/01-it-helpdesk-agent/",
        "build": [
            "study-notes/ops-kb-index.md listing runbooks + owners",
            "Agent cites source in 2 test answers",
            "Fallback behavior when KB miss",
        ],
        "doneWhen": ["KB index committed", "Citation examples logged"],
    },
    {
        "title": "E2E demo + capstone scaffold",
        "competency": "harness",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "ARCHITECTURE.md: all 7 competencies mapped to components",
            "demo-script.md: runbook Q → identity Q → HITL → audit",
            "Repo layout scaffold (folders + README)",
        ],
        "doneWhen": ["Architecture + demo script committed", "Eval failures from W14 addressed in plan"],
    },
]

CAPSTONE_WEEKS = [
    {
        "title": "Capstone W1 — Assemble platform",
        "competency": "harness",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "Merge agent + MCP + FastAPI into capstone layout",
            "One local run script or docker-compose",
            "Port eval suite",
        ],
        "doneWhen": ["Single start command", "5 eval cases pass in capstone repo"],
    },
    {
        "title": "Capstone W2 — Identity + HITL enforcement",
        "competency": "identity",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "HITL gate before side effects",
            "Audit log on every query",
            "Reject privilege escalation eval cases",
        ],
        "doneWhen": ["Unapproved writes blocked", "Audit samples logged"],
    },
    {
        "title": "Capstone W3 — Endpoint policy + observability",
        "competency": "endpoint",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "Wire endpoint policy stub from projects/09",
            "Adoption events + failure alerts",
            "Dashboard script reads capstone logs",
        ],
        "doneWhen": ["Policy check in demo flow", "Metrics emitted"],
    },
    {
        "title": "Capstone W4 — Deploy POC + case study",
        "competency": "ops",
        "path": "projects/08-capstone-ops-agent/",
        "build": [
            "Cloud Run deploy POC (or documented deploy script)",
            "study-notes/capstone-case-study.md",
            "Update portfolio README",
        ],
        "doneWhen": ["Deploy instructions", "Case study with honest limits"],
    },
]

PORTFOLIO_WEEKS = [
    {"title": "Capstone demo polish (2 min)", "competency": "portfolio", "path": "projects/08-capstone-ops-agent/", "build": ["Rehearse demo-script.md", "Fix top 3 eval failures"], "doneWhen": ["Demo under 2 minutes", "README diagram"]},
    {"title": "Portfolio narrative", "competency": "portfolio", "path": "study-notes/platform-projects/platform-bridge.md", "build": ["Update platform-bridge.md", "LinkedIn draft"], "doneWhen": ["Narrative links shipped work + capstone"]},
    {"title": "Consulting one-pager", "competency": "portfolio", "path": "CONTEXT.md", "build": ["study-notes/consulting-one-pager.md from offers (a)(b)(c)"], "doneWhen": ["3 offers scoped with deliverables"]},
    {"title": "Metrics baseline doc", "competency": "ops", "path": "projects/05-adoption-dashboard/", "build": ["study-notes/metrics-baseline.md from real volume only"], "doneWhen": ["Formula documented, no fake %"]},
    {"title": "System design #1 — access automation", "competency": "portfolio", "path": "interview-prep/", "build": ["45-min timed design → interview-prep/answers/"], "doneWhen": ["Written design committed"]},
    {"title": "System design #2 — agent identity platform", "competency": "portfolio", "path": "interview-prep/", "build": ["Timed design: WIF + MCP + HITL"], "doneWhen": ["Design doc committed"]},
    {"title": "STAR stories + resume", "competency": "portfolio", "path": "interview-prep/answers/behavioral-star.md", "build": ["STAR: automation, capstone, identity", "Resume bullets"], "doneWhen": ["behavioral-star.md updated"]},
    {"title": "Mock interview block", "competency": "portfolio", "path": "interview-prep/", "build": ["1 design aloud", "1 STAR aloud", "Capstone demo"], "doneWhen": ["Self-score in wave-1-checklist.md"]},
    {"title": "Apply tracker — 3 targets", "competency": "portfolio", "path": "interview-prep/answers/wave-1-checklist.md", "build": ["Company research", "Tailored resume bullets"], "doneWhen": ["3 companies documented"]},
    {"title": "Submit applications", "competency": "portfolio", "path": "interview-prep/", "build": ["1+ applications", "Outreach"], "doneWhen": ["Apply log updated"]},
    {"title": "Program retro", "competency": "portfolio", "path": "study-notes/", "build": ["study-notes/program-retro.md"], "doneWhen": ["Retro + next quarter plan"]},
    {"title": "Maintain cadence", "competency": "portfolio", "path": "projects/08-capstone-ops-agent/", "build": ["Re-run evals monthly", "Keep capstone runnable"], "doneWhen": ["Capstone runs", "Next milestone set"]},
]


def get_week_plan(week: int) -> dict | None:
    if 1 <= week <= 20:
        p = MINI_PROJECTS[week - 1]
        return {"title": p["title"], "miniProject": p, "phase": "mini", "competency": p["competency"]}
    if 21 <= week <= 24:
        p = CAPSTONE_WEEKS[week - 21]
        return {"title": p["title"], "miniProject": p, "phase": "capstone", "competency": p["competency"]}
    if 25 <= week <= 36:
        p = PORTFOLIO_WEEKS[week - 25]
        return {"title": p["title"], "miniProject": p, "phase": "portfolio", "competency": p["competency"]}
    return None
