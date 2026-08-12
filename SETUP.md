# Setup guide

## For hiring managers

1. Start at [README](./README.md) — shipped AppLovin work + portfolio projects table
2. Open the [project gallery](./projects/) or any brief via the [doc viewer](./site/doc.html?path=projects/01-it-helpdesk-agent/README.md)
3. Use the [weekly dashboard](./tracker/) for study, resources, sub-tasks, and ship checks

## For self-study

```bash
git clone https://github.com/Meerzah/ai-systems-portfolio.git
cd ai-systems-portfolio
./tracker/serve.sh
# → http://127.0.0.1:8765/tracker/
```

The dashboard tracks **one mini-project per week** aligned to [CURRICULUM.md](./CURRICULUM.md). Progress saves in browser localStorage.

## For running portfolio code

Each project under `projects/` is self-contained. Navigate in and follow its README.

**Requirements (typical):**

- Python 3.11+
- GCP project with Vertex AI enabled (for ADK projects)
- Environment variables (see each project's README)

```bash
cd projects/01-it-helpdesk-agent
# follow project README for .env setup
pip install -r requirements.txt
python agent.py
```

## Structure

```
ai-systems-portfolio/
├── index.html              # Landing: Projects | Dashboard | Interview prep
├── README.md               # Portfolio overview
├── MERGE.md                # What was merged from both source repos
├── tracker/                # 36-week dashboard (GitHub Pages)
├── projects/01–07/         # Code + design docs
├── phases/                 # Phase READMEs
├── interview-prep/         # System design practice
└── study-notes/            # Active notes
```

## GitHub Pages

Dashboard deploys automatically on push to `main` via `.github/workflows/pages.yml`.

- Landing: https://meerzah.github.io/ai-systems-portfolio/
- Tracker: https://meerzah.github.io/ai-systems-portfolio/tracker/
