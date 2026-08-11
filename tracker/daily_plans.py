"""Build Mon–Sun daily step plans from weekly mini-project tasks."""

from __future__ import annotations

DAY_ORDER = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_LABELS = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday",
}
DAY_SHORT = {
    "mon": "Mon",
    "tue": "Tue",
    "wed": "Wed",
    "thu": "Thu",
    "fri": "Fri",
    "sat": "Sat",
    "sun": "Sun",
}

WRAP_STEP = {
    "id": "wrap",
    "text": "Review the week, then mark it complete on the dashboard",
    "kind": "wrap",
}


def build_daily_plan(mini_project: dict) -> list[dict]:
    """Spread build + done-when tasks across Mon–Sat; Sunday is wrap-up."""
    build = mini_project.get("build") or []
    done = mini_project.get("doneWhen") or []

    steps: list[dict] = []
    for i, text in enumerate(build):
        steps.append({"id": f"build-{i}", "text": text, "kind": "build"})
    for i, text in enumerate(done):
        steps.append({"id": f"done-{i}", "text": text, "kind": "done"})

    work_days = DAY_ORDER[:6]
    by_day: dict[str, list[dict]] = {d: [] for d in DAY_ORDER}

    for i, step in enumerate(steps):
        by_day[work_days[i % 6]].append(step)

    by_day["sun"] = [WRAP_STEP]

    return [
        {
            "day": day,
            "label": DAY_LABELS[day],
            "short": DAY_SHORT[day],
            "steps": by_day[day],
        }
        for day in DAY_ORDER
    ]
