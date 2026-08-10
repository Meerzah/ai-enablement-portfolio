/** Shared data + helpers for live dashboard layout previews */
(() => {
  function parseWeekRange(str) {
    const m = String(str || "").match(/(\d+)\s*[–-]\s*(\d+)/);
    return m ? [+m[1], +m[2]] : [1, 36];
  }

  const TD = {
    progress: {},
    weeksData: {},
    monthsData: {},
    currentWeek: 1,
    pagesBase: "",
    githubBase: "",
    _listeners: [],

    parseWeekRange,

    weekStorageKey(week) {
      return `aisystems-week-${week}-done`;
    },
    loadWeekDone(week) {
      return localStorage.getItem(this.weekStorageKey(week)) === "1";
    },
    saveWeekDone(week, val) {
      localStorage.setItem(this.weekStorageKey(week), val ? "1" : "0");
    },
    countShipped() {
      return (this.weeksData.weeks || []).filter((w) => this.loadWeekDone(w.week)).length;
    },

    linkBase() {
      const local = location.hostname === "localhost" || location.hostname === "127.0.0.1";
      return local ? ".." : this.pagesBase;
    },

    resolveHref(raw) {
      if (!raw) return null;
      let p = raw.trim();
      if (p.includes("(") && !p.includes("/")) return null;
      if (p.startsWith("http")) return p;
      p = p.split(/\s+\+/)[0].split(/\s+/)[0];
      const base = this.linkBase();
      if (/\.(md|html|json|py|tsx?|csv)$/i.test(p)) return `${base}/${p}`;
      if (p.startsWith("tracker/")) return `${base}/${p}`;
      if (p.includes("/")) return `${base}/${p.replace(/\/$/, "")}/README.md`;
      if (p.endsWith(".md")) return `${base}/${p}`;
      return null;
    },

    linkHtml(raw, label) {
      const href = this.resolveHref(raw);
      const text = label || raw;
      if (!href) return `<span>${escapeHtml(text)}</span>`;
      return `<a href="${href}" target="_blank" rel="noopener">${escapeHtml(text)}</a>`;
    },

    async load() {
      [this.progress, this.weeksData, this.monthsData] = await Promise.all([
        fetch("progress.json").then((r) => r.json()),
        fetch("weeks.json").then((r) => r.json()),
        fetch("months.json").then((r) => r.json()),
      ]);
      this.currentWeek = this.progress.currentWeek || 1;
      this.pagesBase = (this.progress.pagesBase || "..").replace(/\/$/, "");
      this.githubBase = `https://github.com/${this.progress.repoName || "Meerzah/ai-systems-portfolio"}/blob/main`;
    },

    getWeek(n) {
      return (this.weeksData.weeks || []).find((x) => x.week === n);
    },

    phaseForWeek(n) {
      for (const p of this.progress.program || []) {
        const [start, end] = parseWeekRange(p.weeks);
        if (n >= start && n <= end) return p;
      }
      return null;
    },

    weeksInPhase(phase) {
      const [start, end] = parseWeekRange(phase.weeks);
      const out = [];
      for (let w = start; w <= end; w++) {
        const row = this.getWeek(w);
        if (row) out.push(row);
      }
      return out;
    },

    onWeekChange(fn) {
      this._listeners.push(fn);
    },

    goWeek(n) {
      n = Math.max(1, Math.min(36, n));
      this.currentWeek = n;
      this._listeners.forEach((fn) => fn(n));
    },

    phaseLabel(w) {
      if (w.phase === "capstone") return "Capstone build";
      if (w.phase === "portfolio") return "Portfolio lane";
      return "Mini-project";
    },

    competencyLabel(id) {
      const c = (this.progress.competencies || []).find((x) => x.id === id);
      return c ? c.label : id || "build";
    },

    weekShortTitle(w) {
      const t = w.title || "";
      return t.length > 28 ? t.slice(0, 26) + "…" : t;
    },

    renderWeekActions(w) {
      const mp = w.miniProject;
      if (!mp) return "";
      const projectHref = this.resolveHref(mp.path);
      let html = "";
      if (projectHref) {
        html += `<a class="btn btn-primary" href="${projectHref}" target="_blank" rel="noopener">Open project →</a>`;
      }
      if (w.workbook) {
        html += `<a class="btn btn-ghost" href="${w.workbook}">Build sheet</a>`;
      }
      return html;
    },

    renderBuildLists(w) {
      const mp = w.miniProject;
      if (!mp) return { build: "", doneWhen: "" };
      const build = (mp.build || []).map((s) => `<li>${escapeHtml(s)}</li>`).join("");
      const doneWhen = (mp.doneWhen || []).map((s) => `<li>${escapeHtml(s)}</li>`).join("");
      return { build, doneWhen };
    },

    bindWeekDoneCheckbox(root, n) {
      const cb = root.querySelector("#week-done");
      if (!cb) return;
      cb.addEventListener("change", (e) => {
        this.saveWeekDone(n, e.target.checked);
        this.goWeek(n);
      });
    },

    renderProgressMeta() {
      const shipped = this.countShipped();
      return {
        shipped,
        total: 36,
        pct: Math.round((shipped / 36) * 100),
        current: this.currentWeek,
      };
    },

    footerLinks() {
      const base = this.linkBase();
      return {
        home: `${base}/`,
        curriculum: `${base}/${this.progress.curriculum || "CURRICULUM.md"}`,
        capstone: this.resolveHref("projects/08-capstone-ops-agent/"),
      };
    },
  };

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  TD.escapeHtml = escapeHtml;
  window.TD = TD;
})();
