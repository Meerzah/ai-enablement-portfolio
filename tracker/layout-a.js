function layoutBanner(label) {
  return `<div class="preview-banner">
    <div><strong>${label}</strong> · live preview with real roadmap data</div>
    <div class="links">
      <a href="choose-layout.html">Compare all layouts</a>
      <a href="index.html">Current dashboard</a>
    </div>
  </div>`;
}

function renderLayoutA() {
  const meta = TD.renderProgressMeta();
  const links = TD.footerLinks();
  document.body.innerHTML =
    layoutBanner("Layout A · Sidebar") +
    `<div class="a-shell">
      <aside class="a-sidebar">
        <div class="a-brand"><span>Roadmap</span><h2>${TD.escapeHtml(TD.progress.title)}</h2></div>
        <div class="a-progress">
          <label id="a-progress-label">${meta.shipped} of ${meta.total} weeks shipped</label>
          <div class="a-bar"><i id="a-progress-bar" style="width:${meta.pct}%"></i></div>
        </div>
        <div class="a-weeks" id="a-weeks"></div>
        <div class="a-foot">
          <a href="${links.curriculum}">Curriculum</a> ·
          <a href="${links.capstone}">Capstone</a> ·
          <a href="${links.home}">Home</a>
        </div>
      </aside>
      <main class="a-main" id="a-main"></main>
    </div>`;

  renderSidebarWeeks();
  TD.onWeekChange((n) => {
    renderSidebarWeeks();
    renderAMain(n);
  });
  renderAMain(TD.currentWeek);
}

function renderSidebarWeeks() {
  let html = "";
  for (const phase of TD.progress.program || []) {
    html += `<div class="a-phase">${TD.escapeHtml(phase.label)} · W${phase.weeks}</div>`;
    for (const w of TD.weeksInPhase(phase)) {
      const on = w.week === TD.currentWeek;
      const done = TD.loadWeekDone(w.week);
      html += `<button type="button" class="a-week${on ? " on" : ""}${done ? " done" : ""}" data-week="${w.week}">
        <span class="a-week-num">${w.week}</span>
        <span>${TD.escapeHtml(TD.weekShortTitle(w))}</span>
      </button>`;
    }
  }
  const el = document.getElementById("a-weeks");
  el.innerHTML = html;
  el.querySelectorAll(".a-week").forEach((btn) => {
    btn.onclick = () => TD.goWeek(+btn.dataset.week);
  });
  const meta = TD.renderProgressMeta();
  document.getElementById("a-progress-label").textContent = `${meta.shipped} of ${meta.total} weeks shipped`;
  document.getElementById("a-progress-bar").style.width = `${meta.pct}%`;
}

function renderAMain(n) {
  const w = TD.getWeek(n);
  if (!w) return;
  const phase = TD.phaseForWeek(n);
  const mp = w.miniProject;
  const done = TD.loadWeekDone(n);
  const { build, doneWhen } = TD.renderBuildLists(w);
  const capstone =
    w.phase === "capstone"
      ? `<div class="capstone-note"><strong>Month 6 capstone</strong> — integrate into ${TD.linkHtml("projects/08-capstone-ops-agent/", "projects/08-capstone-ops-agent/")}</div>`
      : "";

  document.getElementById("a-main").innerHTML = `
    <div class="a-overview">
      ${(TD.progress.program || [])
        .map(
          (p) =>
            `<div class="a-overview-item"><strong>${TD.escapeHtml(p.label)}</strong> W${p.weeks} · ${TD.escapeHtml((p.competencies || []).join(" · "))}</div>`
        )
        .join("")}
    </div>
    <div class="a-crumb">Week <span>${n}</span> · ${TD.escapeHtml(phase ? phase.label : "")} · ${TD.escapeHtml(w.competency || "")}</div>
    <h1>${TD.escapeHtml(w.title)}</h1>
    <div class="a-tags">
      <span class="tag tag-accent">${TD.escapeHtml(TD.phaseLabel(w))}</span>
      <span class="tag">${TD.escapeHtml(TD.competencyLabel(w.competency || mp?.competency))}</span>
      <span class="tag">${TD.escapeHtml(TD.progress.hoursPerWeek || "12–15")} hrs/wk</span>
    </div>
    ${capstone}
    <div class="a-actions">${TD.renderWeekActions(w)}</div>
    <div class="a-cols">
      <div class="col-box"><h3>Build this week</h3><ul>${build || "<li>See project README</li>"}</ul></div>
      <div class="col-box"><h3>Done when</h3><ul>${doneWhen || "<li>Artifact committed</li>"}</ul></div>
    </div>
    <label class="ship-row"><input type="checkbox" id="week-done" ${done ? "checked" : ""} /> Week ${n} shipped — committed to repo</label>`;

  TD.bindWeekDoneCheckbox(document.getElementById("a-main"), n);
}

TD.load()
  .then(renderLayoutA)
  .catch((err) => {
    document.body.innerHTML = `<div style="padding:24px;color:#fca5a5">Failed to load: ${TD.escapeHtml(err.message)}</div>`;
  });
