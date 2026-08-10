#!/usr/bin/env python3
"""Generate tracker/weeks.json — weekly mini-projects + 6-month capstone."""

from __future__ import annotations

import json
from pathlib import Path

from week_plans import get_week_plan

OUT = Path(__file__).parent / "weeks.json"


def build_week(week: int) -> dict:
    plan = get_week_plan(week)
    if not plan:
        raise ValueError(f"No plan for week {week}")

    month = min((week - 1) // 4 + 1, 9)
    mp = plan["miniProject"]

    w: dict = {
        "week": week,
        "month": month,
        "phase": plan["phase"],
        "capstoneWeek": week in {21, 22, 23, 24},
        "interviewPrep": week >= 29,
        "title": plan["title"],
        "workbook": f"workbooks/week-{week:02d}.html",
        "miniProject": {
            "name": plan["title"],
            "path": mp["path"],
            "build": mp["build"],
            "doneWhen": mp["doneWhen"],
        },
    }
    return w


def main() -> None:
    data = {
        "schema": "mini-project-roadmap-v1",
        "program": {
            "weeks1to20": "Weekly mini-projects — shippable portfolio artifacts",
            "weeks21to24": "Capstone — integrated ops agent platform",
            "weeks25to36": "Demo, case study, interview, apply",
        },
        "weeks": [build_week(w) for w in range(1, 37)],
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT} ({len(data['weeks'])} weeks)")


if __name__ == "__main__":
    main()
