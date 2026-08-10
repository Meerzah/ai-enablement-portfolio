#!/usr/bin/env python3
"""Generate tracker/workbooks/week-NN.html — fill-in worksheets linked from the dashboard."""

from __future__ import annotations

import html
import json
from pathlib import Path

WEEKS_JSON = Path(__file__).parent / "weeks.json"
OUT_DIR = Path(__file__).parent / "workbooks"

# Concrete fill-in prompts per week/day (Mon–Sun keys). Fallback: generic notes field.
WORKBOOK_FIELDS: dict[int, dict[str, list[dict[str, str]]]] = {
    1: {
        "mon": [
            {"id": "f1", "label": "Friction #1 — category", "placeholder": "Access requests"},
            {"id": "f1vol", "label": "Volume (last 30 days)", "placeholder": "48 tickets"},
            {"id": "f1min", "label": "Avg minutes each", "placeholder": "15"},
            {"id": "f2", "label": "Friction #2 — category", "placeholder": "SaaS onboarding"},
            {"id": "f2vol", "label": "Volume", "placeholder": ""},
            {"id": "f3", "label": "Friction #3 — category", "placeholder": "MDM / device issues"},
            {"id": "f3vol", "label": "Volume", "placeholder": ""},
            {"id": "pick", "label": "Chosen automation candidate (one only)", "placeholder": "Access requests — high volume, clear approval path"},
        ],
        "tue": [
            {"id": "trigger", "label": "Intake trigger", "placeholder": "Slack modal / form / email"},
            {"id": "approval", "label": "Who approves?", "placeholder": "Manager + app owner"},
            {"id": "action", "label": "Automated action", "placeholder": "Okta group add via access governance API"},
            {"id": "hitl", "label": "HITL gate (before any write)", "placeholder": "IT approves in Slack before Okta change"},
            {"id": "diagram", "label": "Workflow diagram (Mermaid OK)", "placeholder": "flowchart LR\n  intake --> validate --> approve --> execute"},
        ],
        "wed": [
            {"id": "groups", "label": "Okta groups / policies involved", "placeholder": "app-foo-users, app-foo-admins"},
            {"id": "approvers", "label": "Approver roles", "placeholder": "Manager, app owner, IT"},
            {"id": "audit", "label": "Audit log fields", "placeholder": "requester, approver, ticket_id, groups_before, groups_after, timestamp"},
            {"id": "agent_scope", "label": "Future agent scope (read vs write)", "placeholder": "Read-only Okta MCP; writes via approved workflow only"},
        ],
        "thu": [
            {"id": "deterministic", "label": "Deterministic steps (no LLM)", "placeholder": "Group add, Jira transition, webhook calls"},
            {"id": "agent", "label": "Agent-suitable steps", "placeholder": "Intent classification, KB lookup, routing"},
            {"id": "escalate", "label": "Must escalate (3 examples)", "placeholder": "Privilege escalation, offboarding, exec access"},
            {"id": "handle", "label": "Agent can handle (3 examples)", "placeholder": "VPN how-to, password reset policy, SSO FAQ"},
        ],
        "fri": [
            {"id": "weekly_count", "label": "Current weekly ticket count (chosen category)", "placeholder": "48"},
            {"id": "avg_minutes", "label": "Avg manual minutes (sample of 5)", "placeholder": "15"},
            {"id": "data_source", "label": "Where metrics will live", "placeholder": "Jira custom field + BigQuery export"},
            {"id": "metrics_plan", "label": "Metrics you'll track (no fake %)", "placeholder": "volume, approval_latency, reopen_rate"},
        ],
        "sat": [
            {"id": "q1", "label": "Helpdesk query 1 + result", "placeholder": "How do I reset MFA? → answered / escalated"},
            {"id": "q2", "label": "Query 2 + result", "placeholder": ""},
            {"id": "q3", "label": "Query 3 + result", "placeholder": ""},
            {"id": "q4", "label": "Okta MCP query 1 + result", "placeholder": ""},
            {"id": "q5", "label": "Okta MCP query 2 + result", "placeholder": ""},
        ],
        "sun": [
            {"id": "summary", "label": "Friction inventory summary (top 3 + pick)", "placeholder": ""},
            {"id": "narrative", "label": "Why this fits your AI Systems portfolio (1 paragraph)", "placeholder": ""},
        ],
    },
    2: {
        "mon": [{"id": "tickets", "label": "5 anonymized ticket examples + tags", "placeholder": "Ticket A: access — automatable\nTicket B: ..."}],
        "tue": [{"id": "slack_ref", "label": "Slack intake pattern notes + gaps", "placeholder": ""}],
        "wed": [{"id": "access_path", "label": "Access governance flow documentation", "placeholder": ""}],
        "thu": [{"id": "handoff", "label": "Agent → HITL → execution sequence", "placeholder": ""}],
        "fri": [{"id": "latency", "label": "Approval latency baseline (5 tickets)", "placeholder": ""}],
        "sat": [{"id": "diagram_v2", "label": "Workflow diagram v2 with reuse callouts", "placeholder": ""}],
        "sun": [{"id": "intake_fields", "label": "Draft intake form fields", "placeholder": ""}],
    },
    3: {
        "mon": [{"id": "mdm_saas", "label": "MDM + SaaS friction additions", "placeholder": ""}],
        "tue": [{"id": "onboarding", "label": "Multi-step onboarding workflow", "placeholder": ""}],
        "wed": [{"id": "scim", "label": "SCIM vs manual provisioning notes", "placeholder": ""}],
        "thu": [{"id": "routing", "label": "Agent routing rules draft", "placeholder": ""}],
        "fri": [{"id": "overlap", "label": "Overlap analysis with Unit 1 pick", "placeholder": ""}],
        "sat": [{"id": "compare", "label": "Compare 3 ticket types side-by-side", "placeholder": ""}],
        "sun": [{"id": "decision", "label": "Confirm or change automation candidate", "placeholder": ""}],
    },
}

DAY_ORDER = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_LABELS = {
    "mon": "Monday — Friction",
    "tue": "Tuesday — Workflow",
    "wed": "Wednesday — Identity",
    "thu": "Thursday — Agent",
    "fri": "Friday — Measure",
    "sat": "Saturday — Prove",
    "sun": "Sunday — Prove",
}

STYLE = """
:root {
  --bg:#0d1117;--surface:#161b22;--surface2:#1c2129;--border:#30363d;
  --text:#e6edf3;--muted:#8b949e;--accent:#58a6ff;--success:#3fb950;
  --font:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.55}
.wrap{max-width:760px;margin:0 auto;padding:20px 16px 64px}
.top{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:16px}
.top a{color:var(--accent);text-decoration:none;font-size:.9rem}
.top a:hover{text-decoration:underline}
h1{font-size:1.35rem;margin:6px 0 4px}
.sub{color:var(--muted);font-size:.92rem;margin-bottom:18px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 16px;margin-bottom:14px}
.card h2{font-size:.95rem;margin-bottom:8px;color:var(--accent)}
.steps{margin:0 0 12px 18px;color:var(--muted);font-size:.88rem}
.steps li{margin-bottom:4px}
.field{margin-bottom:12px}
.field label{display:block;font-size:.85rem;margin-bottom:4px;color:var(--muted)}
.field input,.field textarea{width:100%;background:var(--surface2);border:1px solid var(--border);
  border-radius:8px;color:var(--text);padding:8px 10px;font:inherit;font-size:.9rem}
.field textarea{min-height:88px;resize:vertical}
.links{margin-top:10px;font-size:.85rem}
.links a{color:var(--accent);margin-right:12px}
.actions{display:flex;gap:10px;flex-wrap:wrap;margin:16px 0}
button{background:var(--surface2);border:1px solid var(--border);color:var(--text);
  padding:8px 14px;border-radius:8px;cursor:pointer;font:inherit;font-size:.88rem}
button:hover{border-color:var(--accent)}
button.primary{border-color:var(--accent);color:var(--accent)}
.saved{font-size:12px;color:var(--success);margin-left:8px}
"""


def resolve_href(path: str, pages_base: str) -> str | None:
    path = path.strip()
    if not path or "(" in path:
        return None
    if path.startswith("http"):
        return path
    path = path.split()[0]
    if path.endswith((".md", ".html", ".json")):
        return f"{pages_base}/{path}"
    if "/" in path:
        return f"{pages_base}/{path.rstrip('/')}/README.md"
    if path.endswith(".md"):
        return f"{pages_base}/{path}"
    return None


def field_html(week: int, day: str, field: dict[str, str]) -> str:
    fid = html.escape(field["id"])
    label = html.escape(field["label"])
    ph = html.escape(field.get("placeholder", ""))
    return f"""<div class="field">
  <label for="{fid}">{label}</label>
  <textarea id="{fid}" data-key="w{week}-{day}-{fid}" placeholder="{ph}"></textarea>
</div>"""


def day_section(week: int, day: str, day_data: dict, pages_base: str) -> str:
    fields = WORKBOOK_FIELDS.get(week, {}).get(day)
    if not fields:
        fields = [{"id": "notes", "label": "Your output for today", "placeholder": "Write findings, diagrams, and decisions here."}]

    steps = day_data.get("steps") or []
    steps_html = "".join(f"<li>{html.escape(s)}</li>" for s in steps)
    resources = day_data.get("resources") or []
    links = []
    for r in resources:
        href = resolve_href(r, pages_base)
        if href:
            links.append(f'<a href="{html.escape(href)}" target="_blank" rel="noopener">{html.escape(r)}</a>')
    prove = day_data.get("proveLink")
    if prove:
        href = resolve_href(prove, pages_base)
        if href:
            links.append(f'<a href="{html.escape(href)}" target="_blank" rel="noopener">→ Prove: {html.escape(prove)}</a>')

    fields_html = "".join(field_html(week, day, f) for f in fields)
    guide = html.escape(day_data.get("guide") or "")

    return f"""<section class="card" id="{day}">
  <h2>{DAY_LABELS[day]}</h2>
  <p class="sub" style="margin-bottom:10px">{guide}</p>
  {"<ul class='steps'>" + steps_html + "</ul>" if steps_html else ""}
  {fields_html}
  {"<div class='links'><strong style='color:var(--muted);font-size:12px'>Open: </strong>" + " ".join(links) + "</div>" if links else ""}
</section>"""


def render_week(week_data: dict, pages_base: str) -> str:
    week = week_data["week"]
    title = html.escape(week_data.get("title") or f"Week {week}")
    cap = week_data.get("capstoneTitle")
    cap_html = f"<p class='sub'>Capstone: {html.escape(cap)}</p>" if cap else ""

    days_html = "".join(
        day_section(week, d, week_data["days"][d], pages_base)
        for d in DAY_ORDER
        if d in week_data.get("days", {})
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Week {week} workbook — AI Systems roadmap</title>
  <style>{STYLE}</style>
</head>
<body>
  <div class="wrap">
    <div class="top">
      <a href="../index.html">← Dashboard</a>
      <a href="../../phases/phase-{min(3, (week - 1) // 12 + 1)}/README.md" target="_blank" rel="noopener">Phase guide</a>
    </div>
    <p style="font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)">Week {week} workbook</p>
    <h1>{title}</h1>
    {cap_html}
    <p class="sub">Fill in each section below. Progress auto-saves in this browser. Copy finished output into <code>study-notes/weeks/</code> when ready to commit.</p>
    <div class="actions">
      <button type="button" class="primary" id="copy-md">Copy as Markdown</button>
      <button type="button" id="clear-week">Clear saved draft</button>
      <span class="saved" id="save-status"></span>
    </div>
    {days_html}
  </div>
  <script>
    const WEEK = {week};
    const PREFIX = `workbook-w${{WEEK}}-`;
    const status = document.getElementById('save-status');

    document.querySelectorAll('[data-key]').forEach(el => {{
      const key = PREFIX + el.id;
      const saved = localStorage.getItem(key);
      if (saved) el.value = saved;
      el.addEventListener('input', () => {{
        localStorage.setItem(key, el.value);
        status.textContent = 'Saved';
        setTimeout(() => {{ status.textContent = ''; }}, 1500);
      }});
    }});

    document.getElementById('clear-week').onclick = () => {{
      if (!confirm('Clear all saved fields for week ' + WEEK + '?')) return;
      document.querySelectorAll('[data-key]').forEach(el => {{
        localStorage.removeItem(PREFIX + el.id);
        el.value = '';
      }});
    }};

    document.getElementById('copy-md').onclick = () => {{
      const lines = ['# Week {week}: {title}', ''];
      document.querySelectorAll('[data-key]').forEach(el => {{
        const label = el.previousElementSibling?.textContent || el.id;
        lines.push('## ' + label, el.value || '(empty)', '');
      }});
      navigator.clipboard.writeText(lines.join('\\n')).then(() => {{
        status.textContent = 'Copied to clipboard';
      }});
    }};
  </script>
</body>
</html>
"""


def main() -> None:
    weeks_data = json.loads(WEEKS_JSON.read_text())
    pages_base = "https://meerzah.github.io/ai-systems-portfolio"
    OUT_DIR.mkdir(exist_ok=True)

    for w in weeks_data["weeks"]:
        num = w["week"]
        out = OUT_DIR / f"week-{num:02d}.html"
        out.write_text(render_week(w, pages_base))
        w["workbook"] = f"workbooks/week-{num:02d}.html"

    weeks_data["schema"] = "ai-systems-spine-v3-workbooks"
    WEEKS_JSON.write_text(json.dumps(weeks_data, indent=2) + "\n")
    print(f"Wrote {len(list(OUT_DIR.glob('week-*.html')))} workbooks + updated weeks.json")


if __name__ == "__main__":
    main()
