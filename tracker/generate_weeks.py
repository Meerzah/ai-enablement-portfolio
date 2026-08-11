#!/usr/bin/env python3
"""Generate tracker/weeks.json — weekly themes + mini-projects + flagship capstone."""

from __future__ import annotations

import json
from pathlib import Path

from daily_plans import build_daily_plan
from week_guides import get_guide
from week_plans import get_week_plan

OUT = Path(__file__).parent / "weeks.json"


def build_week(week: int) -> dict:
    plan = get_week_plan(week)
    if not plan:
        raise ValueError(f"No plan for week {week}")

    month = min((week - 1) // 4 + 1, 9)
    mp = plan["miniProject"]
    guide = get_guide(week)

    w: dict = {
        "week": week,
        "month": month,
        "competency": plan.get("competency", mp.get("competency")),
        "phase": plan["phase"],
        "theme": plan.get("theme", plan["title"]),
        "learn": plan.get("learn", ""),
        "feeds": plan.get("feeds", mp.get("feeds", [])),
        "objectives": guide["objectives"],
        "study": guide["study"],
        "resources": guide["resources"],
        "timeHint": guide["timeHint"],
        "capstoneWeek": week in {21, 22, 23, 24},
        "interviewPrep": week >= 29,
        "title": plan["title"],
        "workbook": f"workbooks/week-{week:02d}.html",
        "miniProject": {
            "name": plan["title"],
            "path": mp["path"],
            "competency": mp.get("competency", plan.get("competency", "harness")),
            "theme": mp.get("theme", plan.get("theme", plan["title"])),
            "learn": mp.get("learn", plan.get("learn", "")),
            "feeds": mp.get("feeds", []),
            "build": mp["build"],
            "doneWhen": mp["doneWhen"],
        },
        "days": build_daily_plan(mp),
    }
    return w


def main() -> None:
    data = {
        "schema": "competency-roadmap-v3",
        "competencies": [
            "harness",
            "identity",
            "endpoint",
            "enablement",
            "workflow",
            "ops",
            "platform",
            "portfolio",
        ],
        "products": ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "capstone"],
        "program": {
            "weeks1to4": "Agent harness + Okta MCP foundation",
            "weeks5to8": "Okta Identity-as-Code + GCP platform stub",
            "weeks9to12": "HITL + API + webhooks + containers",
            "weeks13to16": "Evals + event stream + CI (Okta TF + agent)",
            "weeks17to20": "Endpoint governance + Run vs GKE + architecture freeze",
            "weeks21to24": "Flagship — Agentic Ops Control Plane",
            "weeks25to36": "Portfolio, interview, apply",
        },
        "weeks": [build_week(w) for w in range(1, 37)],
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT} ({len(data['weeks'])} weeks)")


if __name__ == "__main__":
    main()
