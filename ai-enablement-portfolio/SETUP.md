# Setup guide

This repo is both a learning portfolio and a working codebase.
Projects are built week-by-week following the 12-month AI Enablement roadmap.

## Using this repo

### For hiring managers

Start with the root [README](./README.md), then dive into any project.
Each project has a `ROLLOUT.md` documenting real adoption outcomes — not just technical specs.

### For running the code yourself

Each project is self-contained. Navigate into the project folder and follow its README.

All projects require:
- Python 3.11+
- A GCP project with Vertex AI enabled
- Environment variables set (see each project's `.env.example`)

### Structure

```
ai-enablement-portfolio/
├── README.md                    # Portfolio overview (for hiring managers)
├── GITHUB_PROFILE_README.md     # Copy to your USERNAME/USERNAME repo
├── SETUP.md                     # This file
├── .gitignore
└── projects/
    ├── 01-it-helpdesk-agent/    # Week 8+12 capstone
    ├── 02-okta-mcp-server/      # Week 10–11
    ├── 03-agentspace-rollout/   # Week 13–20
    ├── 04-prompt-playbooks/     # Week 21
    └── 05-adoption-dashboard/   # Week 18
```

## Getting started locally

```bash
git clone https://github.com/YOUR_USERNAME/ai-enablement-portfolio
cd ai-enablement-portfolio

# Set up GCP credentials
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID

# Pick a project to start with
cd projects/01-it-helpdesk-agent
cp .env.example .env
# fill in your values
pip install -r requirements.txt
python agent.py
```

## Notes on the code

- Projects are scaffolded early in the learning process and filled in as skills develop
- Some files are intentionally incomplete placeholders for upcoming weeks
- ROLLOUT.md files are the most important docs — they tell the adoption story
