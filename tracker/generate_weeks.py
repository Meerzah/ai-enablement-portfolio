#!/usr/bin/env python3
"""Generate tracker/weeks.json — 36 weeks, Friction→Prove spine."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).parent / "weeks.json"

MONTH_THEMES = [
    ("Ops friction inventory", "access requests, ticket triage, SaaS onboarding"),
    ("Identity-backed access workflow", "Okta groups, Lumos, SCIM, audit logs"),
    ("Agentic triage POC", "LLM routing vs deterministic steps, HITL"),
    ("Workflow reliability", "retries, idempotency, alerting, runbooks"),
    ("Agent tool-use + evals", "tool schemas, guardrails, eval sets"),
    ("Ops knowledge base", "grounding, KB structure, fallback"),
    ("Metrics + consulting", "TTR, hours saved, consulting offers"),
    ("Interview prep — AI Systems", "Serval-shaped system design, STAR stories"),
    ("Program capstone", "portfolio, apply tracker, iterate"),
]

CAPSTONE_WEEKS = {4, 8, 12, 16, 20, 24, 28, 32, 36}

# Week → optional prove artifact folder (shown as link in dashboard)
PROVE_LINKS: dict[int, str] = {
    1: "projects/01-it-helpdesk-agent/",
    9: "projects/01-it-helpdesk-agent/",
    10: "projects/02-okta-mcp-server/",
    11: "projects/01-it-helpdesk-agent/",
    12: "projects/02-okta-mcp-server/",
    5: "projects/06-cipher/",
    6: "projects/06-cipher/",
    7: "projects/06-cipher/",
    8: "projects/06-cipher/",
    13: "projects/07-alius/",
    25: "projects/05-adoption-dashboard/",
}


def day_friction(week: int, theme: str, detail: str) -> dict:
    return {
        "section": "friction",
        "label": "Friction",
        "guide": f"Week {week}: Map manual ops friction — {theme}.",
        "steps": [
            f"List high-volume requests related to {detail}",
            "Quantify frequency (ticket counts, Slack pings — real data only)",
            "Note approval bottlenecks and identity touchpoints",
            "Pick one friction point to deepen Tue–Sun",
        ],
        "resources": ["CONTEXT.md", "phases/phase-1/README.md"],
    }


def day_workflow(week: int, theme: str) -> dict:
    return {
        "section": "workflow",
        "label": "Workflow",
        "guide": f"Design intake → approval → action for {theme}.",
        "steps": [
            "Draw workflow: trigger, intake form/Slack, approvers, actions",
            "Mark human-in-the-loop gates before destructive actions",
            "Compare to existing n8n or Slack app patterns you shipped",
            "List integrations needed (Jira, Okta, Lumos)",
        ],
        "resources": ["Shipped: Slack App Governance", "n8n internal workflows"],
    }


def day_identity(week: int) -> dict:
    return {
        "section": "identity",
        "label": "Identity",
        "guide": "Scope Okta/OAuth/SCIM correctly; plan for future agent service accounts.",
        "steps": [
            "Map groups/apps touched by this workflow",
            "Apply least privilege — no standing admin grants",
            "Define audit fields (who, what, when, ticket id)",
            "Note agent identity pattern: WIF or scoped OAuth vs long-lived keys",
        ],
        "resources": ["Okta SCIM docs", "CONTEXT.md consulting (a)(b)"],
    }


def day_agent(week: int, theme: str) -> dict:
    return {
        "section": "agent",
        "label": "Agent",
        "guide": f"Where LLM/agent helps for {theme} — vs deterministic automation.",
        "steps": [
            "List steps that must stay deterministic (Okta writes, deletes)",
            "Identify triage/KB/routing suitable for LLM assist",
            "Define escalation when confidence is low",
            "Do not claim production agent experience — label POC",
        ],
        "resources": ["Claude API tool use docs", "MCP patterns"],
    }


def day_measure(week: int) -> dict:
    return {
        "section": "measure",
        "label": "Measure",
        "guide": "Define metrics you can actually measure — no invented KPIs.",
        "steps": [
            "Baseline: manual time-to-resolve or ticket volume (real)",
            "Target metrics: hours saved, retry rate, approval latency",
            "How you'll capture data (Jira, BigQuery, workflow logs)",
            "Skip deflection % unless you have a measurement plan",
        ],
        "resources": ["tracker/progress.json counters"],
    }


def day_prove(week: int, mini: str, prove_link: str | None = None) -> dict:
    resources = ["README.md portfolio section"]
    if prove_link:
        resources.insert(0, prove_link)
    d: dict = {
        "section": "prove",
        "label": "Prove",
        "guide": f"Weekly mini: {mini}",
        "steps": [
            "Ship one artifact (diagram, bot stub, runbook, screenshot)",
            "Commit or save to study-notes/ with date",
            "Update dashboard prove counter if tracking",
            "1-paragraph learnings for interview stories",
        ],
        "resources": resources,
    }
    if prove_link:
        d["proveLink"] = prove_link
        d["steps"][0] = f"Review or extend prove artifact: {prove_link}"
    return d


def capstone_days(month: int, title: str, rubric: list[str]) -> dict:
    return {
        "mon": {
            "section": "friction",
            "label": "Review",
            "guide": f"Month {month} capstone prep: {title}",
            "steps": ["Review Mon–Wed notes from weeks this month", "Gap list for capstone"],
            "resources": ["tracker/months.json"],
        },
        "tue": {
            "section": "workflow",
            "label": "Review",
            "guide": "Consolidate workflow drafts",
            "steps": ["Merge best workflow diagram", "Confirm HITL gates"],
            "resources": [],
        },
        "wed": {
            "section": "identity",
            "label": "Review",
            "guide": "Identity + audit checklist",
            "steps": ["Verify least privilege", "Audit log schema ready"],
            "resources": [],
        },
        "thu": {
            "section": "prove",
            "label": "Capstone build",
            "guide": f"Build: {title}",
            "steps": rubric[:2],
            "resources": ["tracker/months.json rubric"],
        },
        "fri": {
            "section": "prove",
            "label": "Capstone build",
            "guide": "Continue capstone build",
            "steps": rubric[2:4] if len(rubric) > 2 else rubric,
            "resources": [],
        },
        "sat": {
            "section": "prove",
            "label": "Capstone ship",
            "guide": "Ship capstone artifact",
            "steps": ["Demo or doc walkthrough", "Honest status label"],
            "resources": [],
        },
        "sun": {
            "section": "prove",
            "label": "Capstone retro",
            "guide": "Retro + next month preview",
            "steps": ["What shipped vs planned", "Update portfolio bullets"],
            "resources": [],
        },
    }


def interview_friday(week: int) -> dict:
    return {
        "section": "measure",
        "label": "Interview prep",
        "guide": f"Week {week}: Serval-shaped interview practice",
        "steps": [
            "One system design: internal ops automation (45 min timed)",
            "One STAR from shipped work (Slack app, n8n, Argus, Okta)",
            "Research one target company (Serval or AI ops team)",
            "Update portfolio narrative from mock feedback",
        ],
        "resources": ["CONTEXT.md target companies", "interview-prep/system-design-template.md"],
    }


def build_week(week: int) -> dict:
    month_idx = (week - 1) // 4
    month_num = min(month_idx + 1, 9)
    theme, detail = MONTH_THEMES[min(month_idx, 8)]

    w: dict = {
        "week": week,
        "month": month_num,
        "title": theme,
        "capstoneWeek": week in CAPSTONE_WEEKS,
        "interviewPrep": week >= 30,
    }

    if week in CAPSTONE_WEEKS:
        months_path = Path(__file__).parent / "months.json"
        months_data = json.loads(months_path.read_text())
        m = months_data["months"][month_num - 1]
        w["days"] = capstone_days(month_num, m["title"], m["rubric"])
        w["capstoneTitle"] = m["capstone"]
        return w

    mini = f"Artifact for {theme.lower()}"
    link = PROVE_LINKS.get(week)
    w["days"] = {
        "mon": day_friction(week, theme, detail),
        "tue": day_workflow(week, theme),
        "wed": day_identity(week),
        "thu": day_agent(week, theme),
        "fri": interview_friday(week) if week >= 30 else day_measure(week),
        "sat": day_prove(week, mini, link),
        "sun": day_prove(week, "Polish + notes for portfolio", link),
    }
    return w


def main() -> None:
    data = {
        "schema": "ai-systems-spine-v1",
        "spine": ["friction", "workflow", "identity", "agent", "measure", "prove"],
        "weeks": [build_week(w) for w in range(1, 37)],
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT} ({len(data['weeks'])} weeks)")


if __name__ == "__main__":
    main()
