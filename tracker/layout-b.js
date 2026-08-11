function layoutBanner(label) {
  return `<div class="preview-banner">
    <div><strong>${label}</strong> · live preview with real roadmap data</div>
    <div class="links">
      <a href="choose-layout.html">Compare all layouts</a>
      <a href="index.html">Current dashboard</a>
    </div>
  </div>`;
}

let activePhaseId = null;

function renderLayoutB() {
  const meta = TD.renderProgressMeta();
  const phase = TD.phaseForWeek(TD.currentWeek);
  activePhaseId = phase ? phase.id : TD.progress.program[0].id;

  document.body.innerHTML =
    layoutBanner("Layout B · Phase tabs") +
    `<div class="b-shell">
      <div class="b-top">
        <div class="b-top-row">
          <div>
            <h2>${TD.escapeHtml(TD.progress.title)}</h2>
            <p>${TD.escapeHtml(TD.progress.subtitle)}</p>
          </div>
          <div class="b-stats">
            <div class="b-stat"><strong>${meta.current}</strong><span>current week</span></div>
            <div class="b-stat"><strong>${meta.shipped}</strong><span>shipped</span></div>
          </div>
        </div>
        <div class="b-phases" id="b-phases"></div>
      </div>
      <div class="b-program" id="b-program"></div>
      <div class="b-chips" id="b-chips"></div>
      <div class="b-body" id="b-body"></div>
    </div>`;

  renderPhases();
  renderProgramCards();
  renderChips();
  TD.onWeekChange((n) => {
    const p = TD.phaseForWeek(n);
    if (p) activePhaseId = p.id;
    renderPhases();
    renderChips();
    renderBBody(n);
  });
  renderBBody(TD.currentWeek);
}

function renderPhases() {
  document.getElementById("b-phases").innerHTML = (TD.progress.program || [])
    .map((p) => {
      const on = p.id === activePhaseId;
      return `<button type="button" class="b-phase${on ? " on" : ""}" data-phase="${p.id}">${TD.escapeHtml(p.label)} W${p.weeks}</button>`;
    })
    .join("");
  document.querySelectorAll(".b-phase").forEach((btn) => {
    btn.onclick = () => {
      activePhaseId = btn.dataset.phase;
      const phase = TD.progress.program.find((p) => p.id === activePhaseId);
      if (phase) {
        const [start] = TD.parseWeekRange(phase.weeks);
        TD.goWeek(start);
      }
      renderPhases();
      renderChips();
    };
  });
}

function renderProgramCards() {
  document.getElementById("b-program").innerHTML = (TD.progress.competencies || [])
    .slice(0, 7)
    .map((c) => `<div class="b-program-card"><strong>${TD.escapeHtml(c.label)}</strong>${TD.escapeHtml(c.summary)}</div>`)
    .join("");
}

function renderChips() {
  const phase = TD.progress.program.find((p) => p.id === activePhaseId) || TD.progress.program[0];
  document.getElementById("b-chips").innerHTML = TD.weeksInPhase(phase)
    .map((w) => {
      const on = w.week === TD.currentWeek;
      const done = TD.loadWeekDone(w.week);
      return `<button type="button" class="b-chip${on ? " on" : ""}${done ? " done" : ""}" data-week="${w.week}">${w.week}</button>`;
    })
    .join("");
  document.querySelectorAll(".b-chip").forEach((btn) => {
    btn.onclick = () => TD.goWeek(+btn.dataset.week);
  });
}

function renderBBody(n) {
  const w = TD.getWeek(n);
  if (!w) return;
  const mp = w.miniProject;
  const done = TD.loadWeekDone(n);
  const { build, doneWhen } = TD.renderBuildLists(w);
  const buildText = (mp?.build || []).join("; ") || "See project README";
  const doneText = (mp?.doneWhen || []).join("; ") || "Artifact committed";

  document.getElementById("b-body").innerHTML = `
    <div class="b-hero">
      <h1>${TD.escapeHtml(w.title)}</h1>
      <p>Week ${n} · ${TD.escapeHtml(TD.competencyLabel(w.competency))} · ${TD.escapeHtml(mp?.path || "")}</p>
      ${w.theme ? `<p style="margin-top:6px">Theme: ${TD.escapeHtml(w.theme)}</p>` : ""}
      ${w.learn ? `<p style="margin-top:4px;opacity:.85">Learn: ${TD.escapeHtml(w.learn)}</p>` : ""}
      <div class="a-actions">${TD.renderWeekActions(w)}</div>
    </div>
    <div class="b-list">
      <div class="b-item"><div class="b-item-icon">1</div><div><h4>Build this week</h4><p>${TD.escapeHtml(buildText)}</p></div></div>
      <div class="b-item"><div class="b-item-icon">2</div><div><h4>Done when</h4><p>${TD.escapeHtml(doneText)}</p></div></div>
      <div class="b-item"><div class="b-item-icon">3</div><div><h4>Detailed checklist</h4><ul style="margin-top:6px;margin-left:16px;color:#71717a;font-size:12px">${build}${doneWhen}</ul></div></div>
    </div>
    <label class="ship-row"><input type="checkbox" id="week-done" ${done ? "checked" : ""} /> Week ${n} shipped — committed to repo</label>`;

  TD.bindWeekDoneCheckbox(document.getElementById("b-body"), n);
}

TD.load()
  .then(renderLayoutB)
  .catch((err) => {
    document.body.innerHTML = `<div style="padding:24px;color:#fca5a5">Failed to load: ${TD.escapeHtml(err.message)}</div>`;
  });
