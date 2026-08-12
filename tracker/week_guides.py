"""Per-week curriculum: objectives, study/prep, resources. Merged into weeks.json."""

from __future__ import annotations

# Each guide: objectives[], study[], resources[{title, url}], timeHint (optional)

GUIDES: dict[int, dict] = {
    1: {
        "objectives": [
            "Define which IT questions an agent should answer vs escalate",
            "Run the helpdesk agent locally (or document the blocker)",
            "Ship 2 runbooks and a prove log with 5 test queries",
        ],
        "study": [
            "Read project README end-to-end — problem, architecture, setup",
            "Agent vs chatbot: tools + grounding vs free-form chat",
            "When RAG helps (stable runbooks) vs when it fails (policy changes)",
            "Friction inventory: list 5 high-volume IT questions from your world",
            "Skim Google ADK / agent tool-calling concepts (high level)",
        ],
        "resources": [
            {"title": "Project README — IT Helpdesk Agent", "url": "../projects/01-it-helpdesk-agent/README.md"},
            {"title": "Week 1 friction inventory template", "url": "../study-notes/weeks/week-01-friction-inventory.md"},
            {"title": "Week 1 prove log", "url": "../study-notes/weeks/week-01-prove-log.md"},
            {"title": "Curriculum overview", "url": "../CURRICULUM.md"},
            {"title": "Google ADK docs", "url": "https://google.github.io/adk-docs/"},
            {"title": "MCP intro", "url": "https://modelcontextprotocol.io"},
        ],
        "timeHint": "12–15 hrs · Mon study · Tue–Thu build · Fri–Sun prove",
    },
    2: {
        "objectives": [
            "Run Okta MCP with a read-only sandbox token",
            "Verify list_users + get_group_members",
            "Log 3 redacted sample queries",
        ],
        "study": [
            "MCP servers vs direct API wrappers",
            "Okta API tokens: least privilege, read-only scopes",
            "Never commit tokens; sandbox/preview org only",
            "How agents consume tools (schemas, errors)",
        ],
        "resources": [
            {"title": "Okta MCP project README", "url": "../projects/02-okta-mcp-server/README.md"},
            {"title": "Okta API docs", "url": "https://developer.okta.com/docs/reference/"},
            {"title": "MCP specification", "url": "https://modelcontextprotocol.io/specification"},
        ],
        "timeHint": "12–15 hrs",
    },
    3: {
        "objectives": [
            "Wire agent to Okta MCP for identity lookups",
            "Prove write attempts escalate (no direct Okta writes)",
        ],
        "study": [
            "Read vs write tool boundaries for agents",
            "System prompt patterns for escalation",
            "Failure modes: malformed tool args, API errors",
        ],
        "resources": [
            {"title": "Helpdesk agent tools", "url": "../projects/01-it-helpdesk-agent/"},
            {"title": "Okta MCP server", "url": "../projects/02-okta-mcp-server/README.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    4: {
        "objectives": [
            "Ship escalation-policy.md as a product artifact",
            "Test 3 must-escalate + 3 safe-to-answer cases",
        ],
        "study": [
            "Guardrails as policy docs agents must cite",
            "Privilege escalation / social engineering via tickets",
            "Human-in-the-loop triggers",
        ],
        "resources": [
            {"title": "Helpdesk agent project", "url": "../projects/01-it-helpdesk-agent/"},
            {"title": "Curriculum — harness competency", "url": "../CURRICULUM.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    5: {
        "objectives": [
            "Apply (or plan) Okta groups module in sandbox",
            "Document ACCESS-TOPOLOGY.md",
        ],
        "study": [
            "Okta Terraform provider basics",
            "Groups + group rules as access topology",
            "TF state, plan, apply workflow for IdP",
        ],
        "resources": [
            {"title": "Okta Identity-as-Code (M8)", "url": "../projects/11-okta-iac/README.md"},
            {"title": "ACCESS-TOPOLOGY", "url": "../projects/11-okta-iac/docs/ACCESS-TOPOLOGY.md"},
            {"title": "Okta Terraform provider", "url": "https://registry.terraform.io/providers/okta/okta/latest/docs"},
        ],
        "timeHint": "12–15 hrs",
    },
    6: {
        "objectives": [
            "Scaffold apps + policies modules",
            "Document API-manageable vs console-only gaps",
        ],
        "study": [
            "OIDC/SAML app resources in Terraform",
            "Group assignments to apps",
            "Sign-on / MFA policy resources",
        ],
        "resources": [
            {"title": "M8 Okta IaC", "url": "../projects/11-okta-iac/README.md"},
            {"title": "Okta apps (TF docs)", "url": "https://registry.terraform.io/providers/okta/okta/latest/docs"},
        ],
        "timeHint": "12–15 hrs",
    },
    7: {
        "objectives": [
            "Sandbox tf-demo users module",
            "AGENT-CONTRACT.md + CIPHER boundary note",
        ],
        "study": [
            "Why TF should not own production user lifecycle",
            "SCIM / HRIS vs Terraform topology",
            "Agent contract: read vs HITL write",
        ],
        "resources": [
            {"title": "AGENT-CONTRACT", "url": "../projects/11-okta-iac/docs/AGENT-CONTRACT.md"},
            {"title": "CIPHER ship plan", "url": "../projects/06-cipher/SHIP-PLAN.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    8: {
        "objectives": [
            "GCP Terraform stub: SA + Secret Manager pattern",
            "Document WIF / no SA keys",
        ],
        "study": [
            "GCP Secret Manager for Okta tokens",
            "Workload Identity Federation overview",
            "Least-privilege runtime SA for Cloud Run",
        ],
        "resources": [
            {"title": "Platform foundation (M6)", "url": "../projects/10-platform-foundation/README.md"},
            {"title": "WIF notes", "url": "../projects/10-platform-foundation/docs/WIF.md"},
            {"title": "GCP WIF docs", "url": "https://cloud.google.com/iam/docs/workload-identity-federation"},
        ],
        "timeHint": "12–15 hrs",
    },
    9: {
        "objectives": [
            "HITL flow diagram + mock approval",
            "Demo: group-add blocked without approval",
        ],
        "study": [
            "Human-in-the-loop patterns for agents",
            "Propose vs execute separation",
            "Slack Block Kit / CLI approval UX",
        ],
        "resources": [
            {"title": "Helpdesk agent", "url": "../projects/01-it-helpdesk-agent/"},
            {"title": "AGENT-CONTRACT", "url": "../projects/11-okta-iac/docs/AGENT-CONTRACT.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    10: {
        "objectives": [
            "Ship FastAPI POST /query + health",
            "Document curl examples",
        ],
        "study": [
            "Pydantic v2 request/response models",
            "Agent-as-a-service API design",
            "escalated / tools_used response fields",
        ],
        "resources": [
            {"title": "FastAPI docs", "url": "https://fastapi.tiangolo.com/"},
            {"title": "Helpdesk agent", "url": "../projects/01-it-helpdesk-agent/"},
        ],
        "timeHint": "12–15 hrs",
    },
    11: {
        "objectives": [
            "Idempotent /hooks/ticket",
            "reliability.md with retry/duplicate rules",
        ],
        "study": [
            "Idempotency-Key header patterns",
            "Webhook retries and at-least-once delivery",
            "Idempotent stores (memory → later Firestore)",
        ],
        "resources": [
            {"title": "Stripe idempotency guide (pattern)", "url": "https://stripe.com/docs/api/idempotent_requests"},
            {"title": "Helpdesk agent", "url": "../projects/01-it-helpdesk-agent/"},
        ],
        "timeHint": "12–15 hrs",
    },
    12: {
        "objectives": [
            "Dockerfile + docker-compose for agent (+ MCP stub)",
            "One-command local run documented",
        ],
        "study": [
            "Multi-stage Docker builds",
            "Secrets: env files vs bake-into-image",
            "Compose networking basics",
        ],
        "resources": [
            {"title": "Docker multi-stage", "url": "https://docs.docker.com/build/building/multi-stage/"},
            {"title": "Helpdesk agent", "url": "../projects/01-it-helpdesk-agent/"},
        ],
        "timeHint": "12–15 hrs",
    },
    13: {
        "objectives": [
            "5 eval cases CSV + honest results.md",
        ],
        "study": [
            "Eval harnesses for tool-using agents",
            "Why not invent accuracy percentages",
            "Golden vs adversarial cases",
        ],
        "resources": [
            {"title": "Helpdesk agent evals folder", "url": "../projects/01-it-helpdesk-agent/"},
            {"title": "Curriculum — ops competency", "url": "../CURRICULUM.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    14: {
        "objectives": [
            "Expand to 15 cases; top-3 failure plan",
        ],
        "study": [
            "Privilege escalation eval design",
            "KB miss / ambiguous user cases",
            "Regression before model or prompt changes",
        ],
        "resources": [
            {"title": "Helpdesk agent", "url": "../projects/01-it-helpdesk-agent/"},
        ],
        "timeHint": "12–15 hrs",
    },
    15: {
        "objectives": [
            "Event schema + publisher stub + dashboard on samples",
        ],
        "study": [
            "Unified logs/metrics/events schema",
            "Pub/Sub vs structured logging for ops events",
            "Adoption metrics you can actually measure",
        ],
        "resources": [
            {"title": "Adoption / event plane", "url": "../projects/05-adoption-dashboard/README.md"},
            {"title": "GCP Pub/Sub overview", "url": "https://cloud.google.com/pubsub/docs/overview"},
        ],
        "timeHint": "12–15 hrs",
    },
    16: {
        "objectives": [
            "CI: terraform plan path for Okta IaC + agent lint/build",
        ],
        "study": [
            "GitHub Actions basics for Terraform",
            "Secrets in CI (never log tokens)",
            "fmt / validate / plan gates on PR",
        ],
        "resources": [
            {"title": "okta-iac-plan workflow", "url": "../.github/workflows/okta-iac-plan.yml"},
            {"title": "M8 Okta IaC", "url": "../projects/11-okta-iac/README.md"},
            {"title": "setup-terraform action", "url": "https://github.com/hashicorp/setup-terraform"},
        ],
        "timeHint": "12–15 hrs",
    },
    17: {
        "objectives": [
            "Endpoint AI POLICY + MDM rollout checklist",
            "Map Okta groups to tool tiers",
        ],
        "study": [
            "Shadow AI risk on managed endpoints",
            "MDM policy tiers by identity group",
            "Approved vs prohibited AI tools",
        ],
        "resources": [
            {"title": "Endpoint AI governance", "url": "../projects/09-endpoint-ai-governance/README.md"},
            {"title": "M8 groups topology", "url": "../projects/11-okta-iac/docs/ACCESS-TOPOLOGY.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    18: {
        "objectives": [
            "ALIUS architecture update with revoke order + agent vs deterministic",
        ],
        "study": [
            "Offboarding orchestration sequencing",
            "Idempotent revoke of TF-managed app groups",
            "Where agents assist vs deterministic pipelines",
        ],
        "resources": [
            {"title": "ALIUS architecture", "url": "../projects/07-alius/ARCHITECTURE.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    19: {
        "objectives": [
            "Cloud Run vs GKE tradeoff memo + hosting recommendation",
        ],
        "study": [
            "Cloud Run revisions / scale-to-zero",
            "K8s literacy: pod, service, deployment",
            "WIF on Cloud Run for agent identity",
        ],
        "resources": [
            {"title": "Run vs GKE memo", "url": "../study-notes/cloud-platform/run-vs-gke.md"},
            {"title": "Platform foundation", "url": "../projects/10-platform-foundation/README.md"},
            {"title": "Cloud Run docs", "url": "https://cloud.google.com/run/docs"},
        ],
        "timeHint": "12–15 hrs",
    },
    20: {
        "objectives": [
            "Capstone ARCHITECTURE.md + demo-script.md",
        ],
        "study": [
            "Map M1–M8 into one control plane",
            "2-minute hiring-manager demo narrative",
            "Honest POC vs production claims",
        ],
        "resources": [
            {"title": "Flagship capstone", "url": "../projects/08-capstone-ops-agent/README.md"},
            {"title": "Curriculum", "url": "../CURRICULUM.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    21: {
        "objectives": [
            "Assemble control plane; one-command run; 5 evals green",
        ],
        "study": [
            "Integration order: evals first, then wiring",
            "MCP against TF-managed sandbox groups",
        ],
        "resources": [
            {"title": "Capstone README", "url": "../projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "12–15 hrs · capstone",
    },
    22: {
        "objectives": [
            "HITL + audit enforced; IaC-known groups only",
        ],
        "study": [
            "Audit fields: actor, action, resource, approved_by",
            "Reject privilege-escalation eval cases",
        ],
        "resources": [
            {"title": "AGENT-CONTRACT", "url": "../projects/11-okta-iac/docs/AGENT-CONTRACT.md"},
            {"title": "Capstone", "url": "../projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "12–15 hrs · capstone",
    },
    23: {
        "objectives": [
            "Endpoint policy stub + metrics/SLO note + event plane",
        ],
        "study": [
            "SLOs / error budgets for agent APIs (honest sketches)",
            "Structured logs + basic OTel concepts",
            "LLM cost/latency fields worth emitting",
        ],
        "resources": [
            {"title": "Capstone", "url": "../projects/08-capstone-ops-agent/README.md"},
            {"title": "OpenTelemetry overview", "url": "https://opentelemetry.io/docs/concepts/"},
        ],
        "timeHint": "12–15 hrs · capstone",
    },
    24: {
        "objectives": [
            "Cloud Run deploy path + case study with honest limits",
        ],
        "study": [
            "Terraform apply vs documented deploy script tradeoffs",
            "Case study structure: problem → architecture → limits",
        ],
        "resources": [
            {"title": "Platform foundation", "url": "../projects/10-platform-foundation/README.md"},
            {"title": "Capstone", "url": "../projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "12–15 hrs · capstone",
    },
    25: {
        "objectives": ["2-minute demo rehearsed; README diagram"],
        "study": ["Demo scripting: open with Okta IaC, close with deploy path"],
        "resources": [{"title": "Capstone demo script", "url": "../projects/08-capstone-ops-agent/README.md"}],
        "timeHint": "8–12 hrs",
    },
    26: {
        "objectives": ["Platform-bridge narrative linking shipped work + M1–M8"],
        "study": ["Positioning: AI Systems + cloud delivery, not generic automation"],
        "resources": [{"title": "Platform bridge", "url": "../study-notes/platform-projects/platform-bridge.md"}],
        "timeHint": "8–12 hrs",
    },
    27: {
        "objectives": ["Recruiter technical one-pager"],
        "study": ["What hiring managers scan in 30 seconds"],
        "resources": [{"title": "README portfolio grid", "url": "../README.md"}],
        "timeHint": "8–12 hrs",
    },
    28: {
        "objectives": ["Metrics baseline from real volume only"],
        "study": ["Never invent deflection/CSAT"],
        "resources": [{"title": "Adoption dashboard", "url": "../projects/05-adoption-dashboard/README.md"}],
        "timeHint": "8–12 hrs",
    },
    29: {
        "objectives": ["Timed Okta-as-code + SCIM design writeup"],
        "study": ["TF topology vs SCIM lifecycle; agent HITL"],
        "resources": [
            {"title": "Answer draft", "url": "../interview-prep/answers/okta-iac-scim-boundary.md"},
            {"title": "System design template", "url": "../interview-prep/system-design-template.md"},
        ],
        "timeHint": "8–12 hrs",
    },
    30: {
        "objectives": ["Timed Cloud Run vs GKE + WIF/HITL design"],
        "study": ["Hosting tradeoffs for agent platforms"],
        "resources": [
            {"title": "Run vs GKE", "url": "../study-notes/cloud-platform/run-vs-gke.md"},
            {"title": "Questions list", "url": "../interview-prep/questions.json"},
        ],
        "timeHint": "8–12 hrs",
    },
    31: {
        "objectives": ["STAR stories + resume bullets for Okta TF / MCP / HITL"],
        "study": ["STAR tied to shipped + portfolio artifacts"],
        "resources": [{"title": "Behavioral STAR", "url": "../interview-prep/answers/behavioral-star.md"}],
        "timeHint": "8–12 hrs",
    },
    32: {
        "objectives": ["Mock: design + STAR + capstone demo aloud"],
        "study": ["Self-score honestly; fix top gaps"],
        "resources": [{"title": "Wave checklist", "url": "../interview-prep/answers/wave-1-checklist.md"}],
        "timeHint": "8–12 hrs",
    },
    33: {
        "objectives": ["3 target companies researched"],
        "study": ["AI Systems / agentic ops / internal AI platform roles"],
        "resources": [{"title": "CONTEXT targets", "url": "../CONTEXT.md"}],
        "timeHint": "8–12 hrs",
    },
    34: {
        "objectives": ["Submit 1+ applications with portfolio links"],
        "study": ["Link dashboard + capstone + Okta IaC"],
        "resources": [
            {"title": "Live dashboard", "url": "https://meerzah.github.io/ai-systems-portfolio/tracker/"},
            {"title": "Capstone", "url": "../projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "8–12 hrs",
    },
    35: {
        "objectives": ["Program retro + next-quarter plan"],
        "study": ["What elevated positioning; what to harden"],
        "resources": [{"title": "Curriculum checklist", "url": "../CURRICULUM.md"}],
        "timeHint": "6–10 hrs",
    },
    36: {
        "objectives": ["Re-run evals; Okta terraform plan; keep capstone runnable"],
        "study": ["Portfolio keep-alive cadence"],
        "resources": [
            {"title": "Capstone", "url": "../projects/08-capstone-ops-agent/README.md"},
            {"title": "Okta IaC", "url": "../projects/11-okta-iac/README.md"},
        ],
        "timeHint": "6–10 hrs",
    },
}


# Optional richer task cards: title should match (or prefix) a build step when possible.
TASKS: dict[int, list[dict]] = {
    1: [
        {
            "title": "Set up Python venv; install requirements.txt",
            "detail": "Clone the repo locally, create a venv in projects/01-it-helpdesk-agent, install deps, and confirm imports work. If GCP/Vertex blocks you, write the blocker in the prove log and continue with runbooks.",
            "docs": [
                {"title": "Project README — setup", "url": "projects/01-it-helpdesk-agent/README.md"},
            ],
        },
        {
            "title": "Add 2 Markdown runbooks (VPN, SSO, or MDM)",
            "detail": "Write two short, realistic runbooks an agent can ground on. Prefer steps you know from IT ops. Keep PII out; use generic org language.",
            "docs": [
                {"title": "Friction inventory template", "url": "study-notes/weeks/week-01-friction-inventory.md"},
            ],
        },
        {
            "title": "Run 5 test queries; log results in prove log",
            "detail": "Ask the agent five questions (mix of in-scope and out-of-scope). Log query, expected behavior, actual result, and whether you’d escalate.",
            "docs": [
                {"title": "Prove log", "url": "study-notes/weeks/week-01-prove-log.md"},
            ],
        },
    ],
    2: [
        {
            "title": "Configure read-only Okta API token (preview/sandbox org)",
            "detail": "Use an Okta preview/developer org only. Create a least-privilege read token. Store it in env — never commit.",
            "docs": [{"title": "Okta MCP README", "url": "projects/02-okta-mcp-server/README.md"}],
        },
        {
            "title": "Verify list_users + get_group_members tools",
            "detail": "Run the MCP server and exercise both tools. Note required scopes and failure modes.",
            "docs": [{"title": "Okta MCP README", "url": "projects/02-okta-mcp-server/README.md"}],
        },
        {
            "title": "Document 3 sample queries (redact PII)",
            "detail": "Capture three natural-language → tool call examples with redacted output for the portfolio README or notes.",
            "docs": [{"title": "Okta MCP README", "url": "projects/02-okta-mcp-server/README.md"}],
        },
    ],
    5: [
        {
            "title": "Scaffold providers.tf + modules/groups for sandbox Okta org",
            "detail": "Wire the Okta provider for sandbox, open modules/groups, and prepare your first terraform plan.",
            "docs": [{"title": "Okta IaC README", "url": "projects/11-okta-iac/README.md"}],
        },
        {
            "title": "Define app-access + role groups",
            "detail": "Create groups such as agent-read-identity and role-it-approvers that the agent/HITL story will use later.",
            "docs": [{"title": "ACCESS-TOPOLOGY", "url": "projects/11-okta-iac/docs/ACCESS-TOPOLOGY.md"}],
        },
        {
            "title": "Write docs/ACCESS-TOPOLOGY.md diagram",
            "detail": "Document the intended group → app → policy topology and the TF vs SCIM boundary.",
            "docs": [{"title": "ACCESS-TOPOLOGY", "url": "projects/11-okta-iac/docs/ACCESS-TOPOLOGY.md"}],
        },
    ],
}


def _default_tasks(build: list[str], path: str) -> list[dict]:
    tasks = []
    for step in build or []:
        tasks.append(
            {
                "title": step,
                "detail": f"Complete this step in `{path}`. Open the project brief for context, then commit when done.",
                "docs": [{"title": "Project brief", "url": path.rstrip("/") + "/README.md" if path.endswith("/") else path}],
            }
        )
    return tasks


def get_guide(week: int, build: list[str] | None = None, path: str = "") -> dict:
    g = GUIDES.get(week) or {
        "objectives": ["Complete this week's mini-project build and done-when checks"],
        "study": ["Read the project README and CURRICULUM.md for this phase"],
        "resources": [{"title": "Curriculum", "url": "CURRICULUM.md"}],
        "timeHint": "12–15 hrs",
    }
    tasks = list(g.get("tasks") or TASKS.get(week) or [])
    if not tasks:
        tasks = _default_tasks(build or [], path or "projects/")
    # Normalize resource urls to repo-relative (no ../) for the doc viewer
    resources = []
    for r in g.get("resources") or []:
        url = (r.get("url") or "").replace("../", "")
        resources.append({"title": r.get("title", "Resource"), "url": url})
    return {
        "objectives": list(g.get("objectives") or []),
        "study": list(g.get("study") or []),
        "resources": resources,
        "tasks": tasks,
        "timeHint": g.get("timeHint") or "12–15 hrs",
    }
