#!/usr/bin/env python3
"""Generate tracker/weeks.json — 36 weeks with portfolio + study tasks."""

from __future__ import annotations

import json
from pathlib import Path

from week_plans import get_week_plan

OUT = Path(__file__).parent / "weeks.json"
CAPSTONE_WEEKS = {4, 8, 12, 16, 20, 24, 28, 32, 36}


def capstone_days(month: int, title: str, rubric: list[str]) -> dict:
    return {
        "mon": {
            "section": "friction",
            "label": "Review",
            "guide": f"Month {month} capstone prep: {title}",
            "steps": [
                "Review study-notes from weeks 1–3 of this month",
                "Check tracker/months.json rubric — gap list",
            ],
            "resources": ["tracker/months.json"],
        },
        "tue": {
            "section": "workflow",
            "label": "Review",
            "guide": "Consolidate workflow artifacts from this month",
            "steps": [
                "Merge best workflow diagram from study-notes/",
                "Confirm every Okta write has HITL gate marked",
            ],
            "resources": ["study-notes/"],
        },
        "wed": {
            "section": "identity",
            "label": "Review",
            "guide": "Identity + audit checklist before capstone ship",
            "steps": [
                "Verify least privilege on all designed workflows",
                "Audit log schema complete (who, what, when, ticket_id)",
            ],
            "resources": ["study-notes/prod-iam-audit.md"],
        },
        "thu": {
            "section": "prove",
            "label": "Capstone build",
            "guide": f"Build capstone: {title}",
            "steps": rubric[:2],
            "resources": ["tracker/months.json rubric"],
        },
        "fri": {
            "section": "prove",
            "label": "Capstone build",
            "guide": "Continue capstone — ship-quality draft",
            "steps": rubric[2:4] if len(rubric) > 2 else rubric,
            "resources": [],
        },
        "sat": {
            "section": "prove",
            "label": "Capstone ship",
            "guide": "Ship capstone artifact to study-notes/ or projects/",
            "steps": [
                "Commit artifact with date in filename",
                "Honest status label (POC / design / shipped)",
            ],
            "resources": [],
        },
        "sun": {
            "section": "prove",
            "label": "Capstone retro",
            "guide": "Retro + update portfolio README if needed",
            "steps": [
                "What shipped vs planned — write 5 bullets",
                "Update README or case study links",
            ],
            "resources": ["README.md"],
        },
    }


def interview_friday(week: int) -> dict:
    return {
        "section": "measure",
        "label": "Interview prep",
        "guide": f"Week {week}: AI Systems interview practice",
        "steps": [
            "One timed system design (45 min) — see Tue/Wed this week",
            "One STAR aloud from behavioral-star.md (shipped work first)",
            "Research one target company from CONTEXT.md",
        ],
        "resources": [
            "CONTEXT.md target companies",
            "interview-prep/system-design-template.md",
            "interview-prep/answers/behavioral-star.md",
        ],
    }


def build_week(week: int) -> dict:
    month_idx = (week - 1) // 4
    month_num = min(month_idx + 1, 9)

    w: dict = {
        "week": week,
        "month": month_num,
        "capstoneWeek": week in CAPSTONE_WEEKS,
        "interviewPrep": week >= 30,
    }

    if week in CAPSTONE_WEEKS:
        months_path = Path(__file__).parent / "months.json"
        months_data = json.loads(months_path.read_text())
        m = months_data["months"][month_num - 1]
        w["title"] = m["title"]
        w["days"] = capstone_days(month_num, m["title"], m["rubric"])
        w["capstoneTitle"] = m["capstone"]
        return w

    plan = get_week_plan(week)
    if plan:
        w["title"] = plan["title"]
        w["days"] = plan["days"]
        return w

    raise ValueError(f"No week plan for week {week}")


def main() -> None:
    data = {
        "schema": "ai-systems-spine-v2-real",
        "spine": ["friction", "workflow", "identity", "agent", "measure", "prove"],
        "weeks": [build_week(w) for w in range(1, 37)],
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT} ({len(data['weeks'])} weeks)")


if __name__ == "__main__":
    main()
