#!/usr/bin/env python3
"""Generate tracker/workbooks/week-NN.html — mini-project build sheets."""

from __future__ import annotations

import html
import json
from pathlib import Path

WEEKS_JSON = Path(__file__).parent / "weeks.json"
OUT_DIR = Path(__file__).parent / "workbooks"
PAGES_BASE = "https://meerzah.github.io/ai-systems-portfolio"

STYLE = """
:root{--bg:#0d1117;--surface:#161b22;--surface2:#1c2129;--border:#30363d;--text:#e6edf3;--muted:#8b949e;--accent:#58a6ff;--success:#3fb950;--warn:#d29922;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.55}
.wrap{max-width:760px;margin:0 auto;padding:20px 16px 64px}
.top a{color:var(--accent);text-decoration:none;font-size:.9rem;margin-right:14px}
h1{font-size:1.35rem;margin:8px 0}
.sub{color:var(--muted);font-size:.92rem;margin-bottom:16px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 16px;margin-bottom:14px}
.card h2{font-size:.95rem;color:var(--accent);margin-bottom:8px}
ul{margin:0 0 10px 18px;color:var(--muted);font-size:.88rem}
.done li{margin-bottom:4px}
.field{margin-bottom:12px}
.field label{display:block;font-size:.85rem;color:var(--muted);margin-bottom:4px}
.field textarea{width:100%;min-height:72px;background:var(--surface2);border:1px solid var(--border);border-radius:8px;color:var(--text);padding:8px 10px;font:inherit}
.phase{display:inline-block;font-size:11px;padding:2px 8px;border-radius:999px;border:1px solid var(--border);color:var(--warn);margin-bottom:8px}
.phase.capstone{color:#a371f7;border-color:#a371f7}
.phase.portfolio{color:var(--success);border-color:var(--success)}
.btnrow{display:flex;gap:10px;flex-wrap:wrap;margin:12px 0}
button{background:var(--surface2);border:1px solid var(--border);color:var(--text);padding:8px 14px;border-radius:8px;cursor:pointer}
button.primary{border-color:var(--accent);color:var(--accent)}
.project-link{display:inline-block;margin:8px 0;padding:10px 14px;border:1px solid var(--accent);border-radius:8px;color:var(--accent);text-decoration:none;font-weight:600}
"""


def project_href(path: str) -> str:
    p = path.rstrip("/")
    if p.endswith((".md", ".html")):
        return f"{PAGES_BASE}/{p}"
    return f"{PAGES_BASE}/{p}/README.md"


def render(week: dict) -> str:
    n = week["week"]
    mp = week["miniProject"]
    phase = week.get("phase", "mini")
    phase_class = phase
    title = html.escape(week["title"])
    path = mp["path"]
    build = "".join(f"<li>{html.escape(s)}</li>" for s in mp["build"])
    done = "".join(f"<li>{html.escape(s)}</li>" for s in mp["doneWhen"])
    href = html.escape(project_href(path))

    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Week {n} — {title}</title>
<style>{STYLE}</style>
</head><body><div class="wrap">
<div class="top"><a href="../index.html">← Dashboard</a></div>
<span class="phase {phase_class}">{html.escape(phase)} · week {n}</span>
<h1>{title}</h1>
<p class="sub">Ship one concrete artifact this week in the repo. Check each item, commit, then mark the week done on the dashboard.</p>
<a class="project-link" href="{href}" target="_blank" rel="noopener">Open {html.escape(path)} →</a>
<div class="card"><h2>Build this week</h2><ul>{build}</ul></div>
<div class="card"><h2>Done when</h2><ul class="done">{done}</ul></div>
<div class="card"><h2>Ship notes</h2>
<div class="field"><label>What I committed (paths + PR/commit hash)</label>
<textarea id="ship" data-key="w{n}-ship" placeholder="e.g. projects/01-it-helpdesk-agent/runbooks/vpn.md — commit abc123"></textarea></div>
<div class="field"><label>Blockers / next week prep</label>
<textarea id="blockers" data-key="w{n}-blockers"></textarea></div>
</div>
<div class="btnrow">
<button type="button" class="primary" id="copy">Copy ship summary</button>
<button type="button" id="clear">Clear draft</button>
</div>
</div>
<script>
const PREFIX='workbook-';
document.querySelectorAll('[data-key]').forEach(el=>{{
  const k=PREFIX+el.dataset.key; if(localStorage.getItem(k)) el.value=localStorage.getItem(k);
  el.addEventListener('input',()=>localStorage.setItem(k,el.value));
}});
document.getElementById('copy').onclick=()=>{{
  const t=document.getElementById('ship').value;
  navigator.clipboard.writeText('# Week {n}\\n\\n'+t);
}};
document.getElementById('clear').onclick=()=>{{
  if(confirm('Clear?')) document.querySelectorAll('[data-key]').forEach(el=>{{localStorage.removeItem(PREFIX+el.dataset.key);el.value='';}});
}};
</script></body></html>"""


def main() -> None:
    weeks_data = json.loads(WEEKS_JSON.read_text())
    OUT_DIR.mkdir(exist_ok=True)
    for w in weeks_data["weeks"]:
        (OUT_DIR / f"week-{w['week']:02d}.html").write_text(render(w))
    print(f"Wrote {len(weeks_data['weeks'])} workbooks")


if __name__ == "__main__":
    main()
