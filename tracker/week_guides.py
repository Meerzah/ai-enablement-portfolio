"""Per-week curriculum: design challenges, hard study, task cards.

Audience: experienced Okta/GCP/systems engineer leveling into AI Systems.
Ban: token tutorials, venv walkthroughs, 'what is an API' content.
"""

from __future__ import annotations

GUIDES: dict[int, dict] = {
    1: {
        "challenge": "Design a fail-closed decision boundary for an IT ops agent that can see identity data — under social-engineering pressure.",
        "objectives": [
            "Produce a blast-radius matrix for 8 real IT frictions (agent / deterministic / human)",
            "Encode escalation contracts inside runbooks, not only in prose",
            "Prove the agent refuses adversarial asks (not just answers happy paths)",
        ],
        "study": [
            "When tool-using agents increase blast radius vs reduce toil (write your own criteria)",
            "RAG failure modes: stale policy, conflicting runbooks, confident wrong answers",
            "Structural controls vs prompt hopes — what belongs in code",
            "Map 3 AppLovin-style frictions (sanitized) into the matrix without leaking internals",
        ],
        "resources": [
            {"title": "Flagship target architecture", "url": "projects/08-capstone-ops-agent/README.md"},
            {"title": "M1 agent project", "url": "projects/01-it-helpdesk-agent/README.md"},
            {"title": "Curriculum bar", "url": "CURRICULUM.md"},
            {"title": "GCP Agent Identity overview", "url": "https://docs.cloud.google.com/iam/docs/agent-identity-overview"},
            {"title": "Week 1 decision-boundary worksheet", "url": "study-notes/weeks/week-01-friction-inventory.md"},
        ],
        "timeHint": "12–15 hrs · design-heavy week",
    },
    2: {
        "challenge": "Specify an Okta read tool surface that remains safe when the LLM is manipulated.",
        "objectives": [
            "Define allowed/denied Okta fields and redaction rules for tool output",
            "Document confused-deputy + exfil paths via tool responses",
            "Harden MCP responses in sandbox to match the spec",
        ],
        "study": [
            "Least privilege for machine callers vs human admins (scopes as product decisions)",
            "PII minimization in tool payloads — what an agent never needs",
            "Rate limits / pagination abuse as availability attacks",
            "MCP tool schema design: strict inputs, explicit errors",
        ],
        "resources": [
            {"title": "M2 Okta MCP", "url": "projects/02-okta-mcp-server/README.md"},
            {"title": "MCP specification", "url": "https://modelcontextprotocol.io/specification"},
            {"title": "GCP Agent Identity overview", "url": "https://docs.cloud.google.com/iam/docs/agent-identity-overview"},
        ],
        "timeHint": "12–15 hrs · security design week",
    },
    3: {
        "challenge": "Make identity writes structurally impossible for the agent — then try to break your own design.",
        "objectives": [
            "Prove write tools are absent from the registry (code review artifact)",
            "Ship an adversarial pack with expected fail-closed outcomes",
            "Separate prompt instructions from enforceable controls in an architecture note",
        ],
        "study": [
            "Prompt injection → tool invocation chains",
            "Allow-list vs deny-list for tool registration",
            "Audit fields you wish you had when something goes wrong",
        ],
        "resources": [
            {"title": "M1 agent", "url": "projects/01-it-helpdesk-agent/README.md"},
            {"title": "M2 MCP", "url": "projects/02-okta-mcp-server/README.md"},
            {"title": "MCP specification — tools", "url": "https://modelcontextprotocol.io/specification"},
            {"title": "GCP Agent Identity overview", "url": "https://docs.cloud.google.com/iam/docs/agent-identity-overview"},
        ],
        "timeHint": "12–15 hrs · red-team yourself",
    },
    4: {
        "challenge": "Turn escalation into a testable product with rule IDs — not 'be careful' text.",
        "objectives": [
            "Severity matrix with rule IDs an eval can assert",
            "Agent must cite rule IDs on refuse/escalate",
            "Mini-eval with honest failures documented",
        ],
        "study": [
            "Policy-as-code mental models applied to LLM guardrails",
            "Social engineering via helpdesk channels",
            "What 'eval-driven development' means for agents",
        ],
        "resources": [
            {"title": "M1 agent", "url": "projects/01-it-helpdesk-agent/README.md"},
            {"title": "Capstone definition", "url": "projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    5: {
        "challenge": "Design Okta group topology as the control plane agents and automation must not violate.",
        "objectives": [
            "Taxonomy with blast-radius rationale per group",
            "Terraform groups(+rules) with a clean plan",
            "Diagram: TF topology vs SCIM lifecycle ownership",
        ],
        "study": [
            "IdP as infrastructure — drift, review, promotion across envs",
            "Group explosion failure mode and how taxonomy prevents it",
            "How agents invent group names if allow-lists are missing",
        ],
        "resources": [
            {"title": "M8 Okta IaC", "url": "projects/11-okta-iac/README.md"},
            {"title": "ACCESS-TOPOLOGY", "url": "projects/11-okta-iac/docs/ACCESS-TOPOLOGY.md"},
            {"title": "Okta Terraform provider", "url": "https://registry.terraform.io/providers/okta/okta/latest/docs"},
        ],
        "timeHint": "12–15 hrs · identity architecture",
    },
    6: {
        "challenge": "Eliminate click-ops as the source of truth for app assignments and auth policies.",
        "objectives": [
            "App + assignment in TF from your taxonomy",
            "Honest API-gap inventory for policies",
            "One-page drift detection playbook for sandbox",
        ],
        "study": [
            "OIDC/SAML assignment models worth encoding",
            "Which MFA/sign-on knobs are actually API-manageable",
            "PR review standards for identity changes",
        ],
        "resources": [
            {"title": "M8 Okta IaC", "url": "projects/11-okta-iac/README.md"},
            {"title": "Okta provider docs", "url": "https://registry.terraform.io/providers/okta/okta/latest/docs"},
        ],
        "timeHint": "12–15 hrs",
    },
    7: {
        "challenge": "Write the contract that keeps TF, SCIM, and agents from stepping on each other.",
        "objectives": [
            "AGENT-CONTRACT allow-list for reads/proposals",
            "Explicit anti-pattern: prod users as primary TF resources",
            "CIPHER design delta with honest status",
        ],
        "study": [
            "Joiner/mover/leaver ownership boundaries",
            "Break-glass vs steady-state automation",
            "How HITL proposals reference IaC-known groups only",
        ],
        "resources": [
            {"title": "AGENT-CONTRACT", "url": "projects/11-okta-iac/docs/AGENT-CONTRACT.md"},
            {"title": "CIPHER ship plan", "url": "projects/06-cipher/SHIP-PLAN.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    8: {
        "challenge": "Design credential flow for agents as if a token leak is inevitable.",
        "objectives": [
            "Least-privilege IAM table for runtime SA + secrets",
            "WIF path for CI (or concrete backlog)",
            "Threat model for Okta token leakage from agent logs",
        ],
        "study": [
            "WIF vs SA keys — interview-grade tradeoffs",
            "Secret Manager access patterns for Cloud Run",
            "Log redaction for tool arguments/results",
        ],
        "resources": [
            {"title": "M6 platform foundation", "url": "projects/10-platform-foundation/README.md"},
            {"title": "WIF notes", "url": "projects/10-platform-foundation/docs/WIF.md"},
            {"title": "GCP WIF docs", "url": "https://cloud.google.com/iam/docs/workload-identity-federation"},
        ],
        "timeHint": "12–15 hrs · platform security",
    },
    9: {
        "challenge": "Implement HITL so side effects are impossible without an approval token — including unknown groups.",
        "objectives": [
            "Sequence with timeout/deny/failure paths",
            "Code-level block without approval",
            "Negative tests for missing/expired/unknown group",
        ],
        "study": [
            "Two-person control patterns for identity changes",
            "Approval TTL and replay attacks",
            "Propose/execute separation in agent platforms",
        ],
        "resources": [
            {"title": "AGENT-CONTRACT", "url": "projects/11-okta-iac/docs/AGENT-CONTRACT.md"},
            {"title": "M1 agent", "url": "projects/01-it-helpdesk-agent/README.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    10: {
        "challenge": "Shape the agent HTTP API like an internal platform service, not a chatbot wrapper.",
        "objectives": [
            "Typed response with tools_used, escalated, rule_ids, latency_ms",
            "Error taxonomy that ops can page on",
            "OpenAPI + curls for escalate path",
        ],
        "study": [
            "SLI candidates for agent APIs (latency vs correctness)",
            "Idempotent clients calling non-deterministic models",
            "Why health must not invoke the model",
        ],
        "resources": [
            {"title": "FastAPI docs", "url": "https://fastapi.tiangolo.com/"},
            {"title": "M1 agent", "url": "projects/01-it-helpdesk-agent/README.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    11: {
        "challenge": "Survive retry storms after approval without double-executing identity changes.",
        "objectives": [
            "Idempotency-Key behavior with tests",
            "reliability.md covering approve-then-crash",
            "TTL policy for idempotency keys",
        ],
        "study": [
            "At-least-once delivery realities",
            "Exactly-once illusions in distributed systems",
            "Poison message handling for ticket webhooks",
        ],
        "resources": [
            {"title": "Idempotent request patterns", "url": "https://stripe.com/docs/api/idempotent_requests"},
            {"title": "M1 agent", "url": "projects/01-it-helpdesk-agent/README.md"},
        ],
        "timeHint": "12–15 hrs · reliability",
    },
    12: {
        "challenge": "Containerize the control plane with supply-chain and secret-boundary discipline.",
        "objectives": [
            "Multi-stage, non-root image",
            "compose without secret bake-in",
            "Pinning/digest note or explicit risk acceptance",
        ],
        "study": [
            "Image provenance basics for internal tools",
            "Attack surface of local compose demos vs Cloud Run",
            "What hiring managers look for in Dockerfiles",
        ],
        "resources": [
            {"title": "Docker multi-stage", "url": "https://docs.docker.com/build/building/multi-stage/"},
            {"title": "M6 platform", "url": "projects/10-platform-foundation/README.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    13: {
        "challenge": "Build an eval harness that can block a ship — including cases you expect to fail.",
        "objectives": [
            "8 goldens across answer/escalate/refuse",
            "Runnable pass/fail producer",
            "Honest failure narrative",
        ],
        "study": [
            "Eval-driven agent development",
            "Why accuracy % is usually a lie for tool-use",
            "Flaky evals vs flaky models",
        ],
        "resources": [
            {"title": "M1 agent / evals", "url": "projects/01-it-helpdesk-agent/README.md"},
            {"title": "Curriculum ops competency", "url": "CURRICULUM.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    14: {
        "challenge": "Red-team your agent with 15 adversarial cases and a concrete fix plan.",
        "objectives": [
            "15-case suite including PII fishing and tool-arg injection",
            "Top-3 failures with specific fixes",
            "Regression rule for prompt/model changes",
        ],
        "study": [
            "Jailbreak patterns relevant to IT ops agents",
            "KB poisoning / conflicting sources",
            "Privilege escalation via 'urgent VIP' narratives",
        ],
        "resources": [
            {"title": "M1 agent / evals", "url": "projects/01-it-helpdesk-agent/README.md"},
            {"title": "Flagship control plane", "url": "projects/08-capstone-ops-agent/README.md"},
            {"title": "AGENT-CONTRACT (allow-listed groups)", "url": "projects/11-okta-iac/docs/AGENT-CONTRACT.md"},
        ],
        "timeHint": "12–15 hrs · adversarial",
    },
    15: {
        "challenge": "Make silent side effects a detectable bug via an ops event schema.",
        "objectives": [
            "Security-reviewable event schema",
            "Sample HITL lifecycle published",
            "Queries for escalation rate + tool errors on samples",
        ],
        "study": [
            "Audit vs product analytics — field requirements differ",
            "Pub/Sub vs log sinks for control-plane events",
            "What you'd page on at 2am",
        ],
        "resources": [
            {"title": "Event plane project", "url": "projects/05-adoption-dashboard/README.md"},
            {"title": "Pub/Sub overview", "url": "https://cloud.google.com/pubsub/docs/overview"},
        ],
        "timeHint": "12–15 hrs",
    },
    16: {
        "challenge": "Treat Okta Terraform and agent changes as change-controlled production.",
        "objectives": [
            "CI plan gate for Okta IaC",
            "Agent lint/eval CI (or risk-documented blocker)",
            "Approval ownership note for identity vs harness PRs",
        ],
        "study": [
            "Identity changes as high-risk deploys",
            "Plan artifacts in PR review culture",
            "Break-glass when CI cannot reach Okta sandbox",
        ],
        "resources": [
            {"title": "okta-iac-plan workflow", "url": ".github/workflows/okta-iac-plan.yml"},
            {"title": "M8 Okta IaC", "url": "projects/11-okta-iac/README.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    17: {
        "challenge": "Bind endpoint AI controls to identity tiers from your Okta topology.",
        "objectives": [
            "Risk tiers mapped to M8 groups",
            "Time-bounded exception process with audit fields",
            "Sanitized detection ideas with owners",
        ],
        "study": [
            "Shadow AI as an identity + endpoint problem",
            "Exception debt and how it becomes permanent access",
            "How agents should read device posture (stub vs real)",
        ],
        "resources": [
            {"title": "Endpoint AI governance", "url": "projects/09-endpoint-ai-governance/README.md"},
            {"title": "ACCESS-TOPOLOGY", "url": "projects/11-okta-iac/docs/ACCESS-TOPOLOGY.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    18: {
        "challenge": "Design offboarding as a distributed revoke graph with compensations.",
        "objectives": [
            "Ordered revoke + compensation diagram",
            "Failure modes when Okta/MDM/SaaS disagree",
            "Hard line: agent triage vs never auto-revoke",
        ],
        "study": [
            "Saga/compensation thinking for identity",
            "Partial offboarding as a security incident",
            "Where TF-managed app groups fit in revoke order",
        ],
        "resources": [
            {"title": "ALIUS architecture", "url": "projects/07-alius/ARCHITECTURE.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    19: {
        "challenge": "Write an ADR that a staff engineer would argue with — Cloud Run vs GKE for this agent.",
        "objectives": [
            "ADR with forces, decision, consequences, dissent",
            "Map WIF + progressive delivery to HITL releases",
            "Link deploy path in platform foundation",
        ],
        "study": [
            "Scale-to-zero vs always-on agent workers",
            "Multi-tenant cluster ops cost vs Cloud Run constraints",
            "When GKE becomes the right answer later",
        ],
        "resources": [
            {"title": "Run vs GKE memo", "url": "study-notes/cloud-platform/run-vs-gke.md"},
            {"title": "Cloud Run docs", "url": "https://cloud.google.com/run/docs"},
            {"title": "M6 platform", "url": "projects/10-platform-foundation/README.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    20: {
        "challenge": "Freeze an architecture a hiring manager can attack for 30 minutes.",
        "objectives": [
            "Component + trust-boundary diagram covering M1–M8",
            "Timed demo script",
            "Top-5 residual risks for the POC",
        ],
        "study": [
            "How to present portfolio vs production without overclaim",
            "Trust boundaries reviewers always poke",
            "What 'agent identity' means in your diagram",
        ],
        "resources": [
            {"title": "Flagship README", "url": "projects/08-capstone-ops-agent/README.md"},
            {"title": "Curriculum", "url": "CURRICULUM.md"},
        ],
        "timeHint": "12–15 hrs",
    },
    21: {
        "challenge": "Integrate only what evals prove — no feature theater.",
        "objectives": ["One runnable plane", "5 core evals green", "TF group allow-list enforced"],
        "study": ["Integration order: tests first", "Binding MCP to IaC-known groups"],
        "resources": [{"title": "Capstone", "url": "projects/08-capstone-ops-agent/README.md"}],
        "timeHint": "12–15 hrs · capstone",
    },
    22: {
        "challenge": "Make trust boundaries non-optional in the running system.",
        "objectives": ["HITL hard gate", "Audit on refusals too", "Escalation evals still hold"],
        "study": ["Audit completeness", "Unknown-group rejection paths"],
        "resources": [
            {"title": "AGENT-CONTRACT", "url": "projects/11-okta-iac/docs/AGENT-CONTRACT.md"},
            {"title": "Capstone", "url": "projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "12–15 hrs · capstone",
    },
    23: {
        "challenge": "Diagnose a failed tool call from telemetry alone; define an SLO without fake numbers.",
        "objectives": ["Structured logs/metrics for tools", "SLO measurement definition", "Policy stub in demo"],
        "study": ["LLM cost/latency fields worth emitting", "Error budgets for agent correctness"],
        "resources": [
            {"title": "OpenTelemetry concepts", "url": "https://opentelemetry.io/docs/concepts/"},
            {"title": "Capstone", "url": "projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "12–15 hrs · capstone",
    },
    24: {
        "challenge": "Ship a stranger-reproducible deliver path and a case study that refuses to overclaim.",
        "objectives": ["Cloud Run path", "Okta plan in the story", "Honest limits case study"],
        "study": ["Portfolio POC vs production language", "What proof links to put on a resume"],
        "resources": [
            {"title": "M6 platform", "url": "projects/10-platform-foundation/README.md"},
            {"title": "Capstone", "url": "projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "12–15 hrs · capstone",
    },
    25: {
        "challenge": "Survive interrupt questions mid-demo without losing the narrative.",
        "objectives": ["5 interrupt Q&As written", "Timed demo", "Screen-share diagram"],
        "study": ["Security and identity questions hiring managers ask"],
        "resources": [{"title": "Capstone", "url": "projects/08-capstone-ops-agent/README.md"}],
        "timeHint": "8–12 hrs",
    },
    26: {
        "challenge": "Write the career narrative that connects shipped work to the control plane without lying.",
        "objectives": ["platform-bridge updated", "Shipped vs POC clearly split"],
        "study": ["Positioning for AI Systems / agentic ops"],
        "resources": [{"title": "Platform bridge", "url": "study-notes/platform-projects/platform-bridge.md"}],
        "timeHint": "8–12 hrs",
    },
    27: {
        "challenge": "One page a recruiter actually forwards.",
        "objectives": ["recruiter-one-pager with proof links"],
        "study": ["30-second scan hierarchy"],
        "resources": [{"title": "README", "url": "README.md"}],
        "timeHint": "8–12 hrs",
    },
    28: {
        "challenge": "Define metrics you'd defend under cross-examination.",
        "objectives": ["Formulas + real data sources only"],
        "study": ["Vanity KPI failure modes"],
        "resources": [{"title": "Event plane", "url": "projects/05-adoption-dashboard/README.md"}],
        "timeHint": "8–12 hrs",
    },
    29: {
        "challenge": "45-minute design: Okta-as-code + SCIM + agent HITL under drift and abuse.",
        "objectives": ["Full design with abuse cases"],
        "study": ["TF/SCIM split interview answers"],
        "resources": [
            {"title": "Answer draft", "url": "interview-prep/answers/okta-iac-scim-boundary.md"},
            {"title": "System design template", "url": "interview-prep/system-design-template.md"},
        ],
        "timeHint": "8–12 hrs",
    },
    30: {
        "challenge": "45-minute design: agent hosting + WIF + progressive delivery with HITL.",
        "objectives": ["Tradeoff table + recommendation"],
        "study": ["Cloud Run vs GKE under identity constraints"],
        "resources": [
            {"title": "Run vs GKE", "url": "study-notes/cloud-platform/run-vs-gke.md"},
            {"title": "Questions", "url": "interview-prep/questions.json"},
        ],
        "timeHint": "8–12 hrs",
    },
    31: {
        "challenge": "STAR + resume bullets that map to artifacts, not adjectives.",
        "objectives": ["STAR set + resume lines with links"],
        "study": ["Anti-overclaim language"],
        "resources": [{"title": "Behavioral STAR", "url": "interview-prep/answers/behavioral-star.md"}],
        "timeHint": "8–12 hrs",
    },
    32: {
        "challenge": "Mock loop that surfaces real gaps.",
        "objectives": ["Self-score + fix list"],
        "study": ["Feedback conversion into backlog"],
        "resources": [{"title": "Wave checklist", "url": "interview-prep/answers/wave-1-checklist.md"}],
        "timeHint": "8–12 hrs",
    },
    33: {
        "challenge": "Pick targets where this portfolio is a weapon, not a stretch.",
        "objectives": ["3 targets with lead artifact each"],
        "study": ["AI Systems / internal platform role mapping"],
        "resources": [{"title": "CONTEXT", "url": "CONTEXT.md"}],
        "timeHint": "8–12 hrs",
    },
    34: {
        "challenge": "Apply with proof URLs that open the control plane story.",
        "objectives": ["Applications + outreach log"],
        "study": ["What to lead with in first email"],
        "resources": [
            {"title": "Live dashboard", "url": "https://meerzah.github.io/ai-systems-portfolio/tracker/"},
            {"title": "Capstone", "url": "projects/08-capstone-ops-agent/README.md"},
        ],
        "timeHint": "8–12 hrs",
    },
    35: {
        "challenge": "Kill anything still basic; raise next-quarter difficulty.",
        "objectives": ["Retro with keep/kill/raise"],
        "study": ["What still wouldn't impress a staff interviewer"],
        "resources": [{"title": "Curriculum", "url": "CURRICULUM.md"}],
        "timeHint": "6–10 hrs",
    },
    36: {
        "challenge": "Prove the portfolio hasn't rotted.",
        "objectives": ["Evals re-run", "Okta plan clean or drift explained"],
        "study": ["Portfolio maintenance as engineering"],
        "resources": [
            {"title": "Capstone", "url": "projects/08-capstone-ops-agent/README.md"},
            {"title": "Okta IaC", "url": "projects/11-okta-iac/README.md"},
        ],
        "timeHint": "6–10 hrs",
    },
}


def _tasks_from_build(build: list[str], path: str, challenge: str) -> list[dict]:
    """Default task cards: each build step is a design/build challenge, not a tutorial."""
    tasks = []
    for step in build or []:
        tasks.append(
            {
                "title": step,
                "detail": (
                    f"{challenge} Execute this artifact in `{path}`. "
                    "Assume Okta/GCP/Python fundamentals. Optimize for something a hiring manager can interrogate: "
                    "tradeoffs, failure modes, and enforceable controls — not setup steps."
                ),
                "docs": [
                    {
                        "title": "Project brief",
                        "url": path.rstrip("/") + "/README.md" if str(path).endswith("/") else path,
                    }
                ],
            }
        )
    return tasks


def get_guide(week: int, build: list[str] | None = None, path: str = "") -> dict:
    g = GUIDES.get(week) or {
        "challenge": "Ship a portfolio artifact that compounds into the flagship control plane.",
        "objectives": ["Complete this week's build with enforceable controls documented"],
        "study": ["Read CURRICULUM.md and the target project architecture"],
        "resources": [{"title": "Curriculum", "url": "CURRICULUM.md"}],
        "timeHint": "12–15 hrs",
    }
    challenge = g.get("challenge") or "Raise the bar on this week's artifact."
    tasks = list(g.get("tasks") or [])
    if not tasks:
        tasks = _tasks_from_build(build or [], path or "projects/", challenge)

    resources = []
    for r in g.get("resources") or []:
        url = (r.get("url") or "").replace("../", "")
        resources.append({"title": r.get("title", "Resource"), "url": url})

    return {
        "challenge": challenge,
        "objectives": list(g.get("objectives") or []),
        "study": list(g.get("study") or []),
        "resources": resources,
        "tasks": tasks,
        "timeHint": g.get("timeHint") or "12–15 hrs",
    }
