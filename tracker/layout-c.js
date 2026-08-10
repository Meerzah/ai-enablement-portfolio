function layoutBanner(label) {
  return `<div class="preview-banner">
    <div><strong>${label}</strong> · live preview with real roadmap data</div>
    <div class="links">
      <a href="choose-layout.html">Compare all layouts</a>
      <a href="index.html">Current dashboard</a>
    </div>
  </div>`;
}

function renderLayoutC() {
  const meta = TD.renderProgressMeta();
  const links = TD.footerLinks();

  document.body.innerHTML =
    layoutBanner("Layout C · Week grid") +
    `<div class="c-shell">
      <div class="c-left">
        <h2>36-week map</h2>
        <p>All weeks at a glance · click to open build details</p>
        <div class="c-stats">
          <div><strong>${meta.current}</strong>current</div>
          <div><strong>${meta.shipped}</strong>shipped</div>
          <div><strong>${meta.total - meta.shipped}</strong>remaining</div>
        </div>
        <div class="c-grid" id="c-grid"></div>
        <div class="c-legend">
          <span><i style="background:#431407;border:1px solid #f97316"></i>Current</span>
          <span><i style="background:#14532d;border:1px solid #22c55e"></i>Shipped</span>
          <span><i style="background:#3b0764;border:1px solid #a855f7"></i>Capstone</span>
        </div>
        <div class="c-phases">
          <h3>Program phases</h3>
          ${(TD.progress.program || [])
            .map(
              (p) =>
                `<div class="c-phase-row"><span>${TD.escapeHtml(p.label)}</span><span>W${p.weeks}</span></div>`
            )
            .join("")}
        </div>
      </div>
      <div class="c-right" id="c-right"></div>
    </div>`;

  renderGrid();
  TD.onWeekChange((n) => {
    renderGrid();
    renderCRight(n);
  });
  renderCRight(TD.currentWeek);
}

function renderGrid() {
  document.getElementById("c-grid").innerHTML = (TD.weeksData.weeks || [])
    .map((w) => {
      const on = w.week === TD.currentWeek;
      const done = TD.loadWeekDone(w.week);
      const cap = w.phase === "capstone" || w.capstoneWeek;
      let cls = "c-tile";
      if (cap) cls += " cap";
      if (on) cls += " on";
      if (done) cls += " done";
      const sub = on ? "now" : done ? "✓" : cap ? "★" : "";
      return `<button type="button" class="${cls}" data-week="${w.week}">${w.week}${sub ? `<small>${sub}</small>` : ""}</button>`;
    })
    .join("");
  document.querySelectorAll(".c-tile").forEach((btn) => {
    btn.onclick = () => TD.goWeek(+btn.dataset.week);
  });
}

function renderCRight(n) {
  const w = TD.getWeek(n);
  if (!w) return;
  const mp = w.miniProject;
  const done = TD.loadWeekDone(n);
  const { build, doneWhen } = TD.renderBuildLists(w);
  const links = TD.footerLinks();

  document.getElementById("c-right").innerHTML = `
    <div class="label">Week ${n} · ${TD.escapeHtml(w.competency || "")}</div>
    <h1>${TD.escapeHtml(w.title)}</h1>
    <div class="a-tags" style="margin-bottom:16px">
      <span class="tag tag-accent">${TD.escapeHtml(TD.phaseLabel(w))}</span>
      <span class="tag">${TD.escapeHtml(TD.competencyLabel(w.competency))}</span>
    </div>
    <div class="a-actions" style="margin-bottom:16px">${TD.renderWeekActions(w)}</div>
    <div class="col-box" style="margin-bottom:12px"><h3>Build</h3><ul>${build || "<li>See README</li>"}</ul></div>
    <div class="col-box" style="margin-bottom:12px"><h3>Done when</h3><ul>${doneWhen || "<li>Committed</li>"}</ul></div>
    <label class="ship-row"><input type="checkbox" id="week-done" ${done ? "checked" : ""} /> Week ${n} shipped</label>
    <div class="c-nav-links">
      <a href="${links.curriculum}">Curriculum</a>
      <a href="${links.capstone}">Capstone spec</a>
      ${w.workbook ? `<a href="${w.workbook}">Build sheet</a>` : ""}
    </div>`;

  TD.bindWeekDoneCheckbox(document.getElementById("c-right"), n);
}

TD.load()
  .then(renderLayoutC)
  .catch((err) => {
    document.body.innerHTML = `<div style="padding:24px;color:#fca5a5">Failed to load: ${TD.escapeHtml(err.message)}</div>`;
  });
