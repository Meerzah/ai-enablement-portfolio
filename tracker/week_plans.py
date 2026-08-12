"""36-week curriculum: hard weekly builds that compound into the flagship control plane.

Assumes competent Okta/GCP/Python. No tutorial steps (tokens, venv, click-ops).
Each week ships an artifact a hiring manager can interrogate.
"""

from __future__ import annotations

# competency: harness | identity | endpoint | enablement | workflow | ops | platform | portfolio

MINI_PROJECTS: list[dict] = [
    # ── Phase 1: Agent foundation (W1–4) ──
    {
        "title": "Decision boundary for agentic IT ops",
        "theme": "Decision boundary for agentic IT ops",
        "learn": "Fail-closed scope design: when agents help vs when they create blast radius",
        "competency": "harness",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M1"],
        "build": [
            "Ship docs/decision-boundary.md: agent vs deterministic vs human for 8 real IT frictions with blast-radius rating",
            "Write 2 runbooks with machine-checkable escalation contracts (must cite policy; refuse writes)",
            "Prove log: 5 adversarial queries (social eng, out-of-scope, ambiguous) + expected fail-closed behavior",
        ],
        "doneWhen": [
            "decision-boundary.md has explicit deny list + rationale",
            "Runbooks encode escalation, not just how-to steps",
            "Prove log shows at least 2 intentional refusals",
        ],
    },
    {
        "title": "Identity tool surface for LLMs",
        "theme": "Identity tool surface for LLMs",
        "learn": "Design Okta read tools that are safe under LLM misuse — not 'how to make a token'",
        "competency": "identity",
        "path": "projects/02-okta-mcp-server/",
        "feeds": ["M2"],
        "build": [
            "Ship docs/tool-surface.md: allowed Okta reads, forbidden fields, PII redaction rules, rate/abuse limits",
            "Implement or harden MCP tools so responses strip high-risk attributes (e.g. factors, recovery, admin flags)",
            "Threat note: confused deputy + prompt-injection → data exfil via tool output",
        ],
        "doneWhen": [
            "tool-surface.md is reviewable by a security engineer",
            "Demo query shows redacted vs raw (sandbox)",
            "Threat note lists 3 concrete mitigations",
        ],
    },
    {
        "title": "Agent–identity contract under attack",
        "theme": "Agent–identity contract under attack",
        "learn": "Wire tools so writes are structurally impossible; prove adversarial cases fail closed",
        "competency": "harness",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M1", "M2"],
        "build": [
            "Enforce read-only identity path in code (not just prompt): no write tools registered",
            "Add 5 adversarial cases: 'add me to admin', 'disable MFA', 'export all users', ambiguous VIP, KB miss",
            "Document failure modes: tool schema rejection, escalation, and audit stub fields",
        ],
        "doneWhen": [
            "Write tools absent from tool registry",
            "Adversarial pack logged with pass/fail",
            "Architecture note: prompt vs structural controls",
        ],
    },
    {
        "title": "Guardrails as an enforceable product",
        "theme": "Guardrails as an enforceable product",
        "learn": "Escalation policy that can be tested — not a soft prompt suggestion",
        "competency": "harness",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M1"],
        "build": [
            "Ship docs/escalation-policy.md with severity matrix + examples tied to decision-boundary",
            "Add policy-citation requirement: agent must name rule ID on escalate/refuse",
            "Build mini eval: 6 cases (3 escalate / 3 answer) with honest results — no invented accuracy %",
        ],
        "doneWhen": [
            "Policy has rule IDs a test can assert",
            "Eval results committed with failures called out",
            "System prompt references rule IDs, not vibes",
        ],
    },
    # ── Phase 2: Okta IaC + agent identity (W5–8) ──
    {
        "title": "Access topology as a control plane",
        "theme": "Access topology as a control plane",
        "learn": "Model Okta groups/rules as the contract agents and automation must honor",
        "competency": "identity",
        "path": "projects/11-okta-iac/",
        "feeds": ["M8"],
        "build": [
            "Design group taxonomy for agentic ops: app access, approver roles, agent-read scopes",
            "Implement Terraform modules/groups (+ rules where useful) in sandbox; plan must be reviewable",
            "ACCESS-TOPOLOGY.md: sequence diagram for join/move/leave vs TF-owned topology",
        ],
        "doneWhen": [
            "Taxonomy explains why each group exists (blast radius)",
            "terraform plan shows intentional resources only",
            "Diagram makes TF vs SCIM ownership obvious",
        ],
    },
    {
        "title": "Apps & policies without click-ops drift",
        "theme": "Apps & policies without click-ops drift",
        "learn": "Encode OIDC/SAML assignments + auth policies; document API gaps honestly",
        "competency": "identity",
        "path": "projects/11-okta-iac/",
        "feeds": ["M8"],
        "build": [
            "Terraform apps module: at least one OIDC (or SAML) app + group assignments from taxonomy",
            "Policies module: sign-on/MFA resources that are API-manageable; gap list for console-only",
            "Drift playbook: how PR plan catches click-ops changes in sandbox",
        ],
        "doneWhen": [
            "App→group assignment is code-reviewed via plan",
            "Gap list is specific (resource names), not hand-wavy",
            "Drift playbook is 1 page and actionable",
        ],
    },
    {
        "title": "Lifecycle split: TF topology vs SCIM humans",
        "theme": "Lifecycle split: TF topology vs SCIM humans",
        "learn": "Draw the hard line: agents propose membership; TF owns structure; SCIM owns people",
        "competency": "identity",
        "path": "projects/11-okta-iac/",
        "feeds": ["M8"],
        "build": [
            "AGENT-CONTRACT.md: allow-listed groups for MCP read + HITL write proposals only",
            "Sandbox users module limited to tf-demo-* with explicit anti-pattern note for prod users-in-TF",
            "CIPHER design delta: where automation mutates membership without TF owning user records",
        ],
        "doneWhen": [
            "Contract is strict enough to reject invented group names",
            "README boundary section could survive a security review",
            "CIPHER note updated with honest architected status",
        ],
    },
    {
        "title": "Secrets & workload identity for agents",
        "theme": "Secrets & workload identity for agents",
        "learn": "No long-lived keys in git/CI; design WIF + Secret Manager for agent + Okta creds",
        "competency": "platform",
        "path": "projects/10-platform-foundation/",
        "feeds": ["M6"],
        "build": [
            "Terraform: runtime SA + Secret Manager placeholders + IAM bindings (least privilege table)",
            "WIF.md: CI → GCP trust path; contrast with SA JSON anti-pattern",
            "Threat model: leaked Okta token from agent logs — mitigations (redaction, short TTL, scope)",
        ],
        "doneWhen": [
            "IAM table maps principal → role → reason",
            "WIF path is concrete (pool/provider or explicit backlog)",
            "Threat model has 3 mitigations you'd defend in interview",
        ],
    },
    # ── Phase 3: Workflow + containers (W9–12) ──
    {
        "title": "HITL as a hard gate, not a UX nicety",
        "theme": "HITL as a hard gate, not a UX nicety",
        "learn": "Side effects are blocked in code until approval; proposals only against IaC-known groups",
        "competency": "workflow",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M3"],
        "build": [
            "Sequence diagram: propose → approve → execute with failure/timeout paths",
            "Implement mock HITL that structurally blocks group-add without approval token",
            "Negative tests: missing approval, expired approval, unknown group name",
        ],
        "doneWhen": [
            "Demo proves block without approval",
            "Unknown group rejected before any Okta call",
            "Timeout/deny path documented",
        ],
    },
    {
        "title": "Agent as a production-shaped API",
        "theme": "Agent as a production-shaped API",
        "learn": "Contracts, error budgets thinking, and response shapes for tool-using agents",
        "competency": "workflow",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M3"],
        "build": [
            "FastAPI /query with typed models: answer, tools_used, escalated, rule_ids, latency_ms",
            "Error taxonomy: 4xx client/policy vs 5xx model/tool failures",
            "OpenAPI snippet + curl examples for happy path and forced escalation",
        ],
        "doneWhen": [
            "Response always includes escalated + tools_used",
            "Error taxonomy documented",
            "Health endpoint separate from query path",
        ],
    },
    {
        "title": "Idempotent intake under retries",
        "theme": "Idempotent intake under retries",
        "learn": "At-least-once webhooks without double-executing side effects",
        "competency": "workflow",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M3"],
        "build": [
            "Idempotency-Key store for /hooks/ticket; duplicate returns same body",
            "reliability.md: retry storms, poison messages, partial failure after approval",
            "Chaos note: what happens if executor succeeds but ack is lost",
        ],
        "doneWhen": [
            "Duplicate POST test logged",
            "reliability.md covers approve-then-crash",
            "Idempotency key TTL policy stated",
        ],
    },
    {
        "title": "Container boundary for the control plane",
        "theme": "Container boundary for the control plane",
        "learn": "Ship a one-command local plane without baking secrets; multi-stage hardening",
        "competency": "platform",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M1", "M6"],
        "build": [
            "Multi-stage Dockerfile; non-root user; no secrets in layers",
            "compose: agent API + MCP with env-injected creds only",
            "Supply-chain note: pin base image digest or document why not yet",
        ],
        "doneWhen": [
            "compose up documented and works (or blocker logged)",
            "`docker history` / scan notes show no secret bake-in",
            "README one-command path for reviewers",
        ],
    },
    # ── Phase 4: Evals, events, CI (W13–16) ──
    {
        "title": "Eval harness that can fail you",
        "theme": "Eval harness that can fail you",
        "learn": "Goldens for tool-use and policy — evals that block ship, not vanity metrics",
        "competency": "ops",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M4"],
        "build": [
            "eval_cases.csv: 8 cases spanning runbook, identity read, escalate, refuse",
            "Runner script or makefile target that produces pass/fail without invented %",
            "results.md: which cases you expect to still fail and why",
        ],
        "doneWhen": [
            "Runner is deterministic enough to re-run",
            "At least one intentional failing case documented",
            "No accuracy marketing numbers",
        ],
    },
    {
        "title": "Adversarial eval suite (15)",
        "theme": "Adversarial eval suite (15)",
        "learn": "Privilege escalation, jailbreaks, KB poisoning, ambiguous VIP paths",
        "competency": "ops",
        "path": "projects/01-it-helpdesk-agent/",
        "feeds": ["M4"],
        "build": [
            "Expand to 15 cases: escalation, PII fishing, tool arg injection, KB miss, conflicting runbooks",
            "Top-3 failure analysis with fix plan before capstone",
            "Regression rule: prompt/model change requires suite green or waiver note",
        ],
        "doneWhen": [
            "15 rows committed",
            "Failure analysis is specific (not 'improve prompt')",
            "Regression rule written in evals/README",
        ],
    },
    {
        "title": "Ops event plane for agent actions",
        "theme": "Ops event plane for agent actions",
        "learn": "Unify query/tool/approve/fail into an auditable stream (Pub/Sub or log sink)",
        "competency": "ops",
        "path": "projects/05-adoption-dashboard/",
        "feeds": ["M5"],
        "build": [
            "events-schema.md with required fields for security review (actor, action, resource, approved_by)",
            "Publisher stub emitting sample lifecycle for one HITL flow",
            "Dashboard/query that answers: escalation rate + tool error rate on sample data",
        ],
        "doneWhen": [
            "Schema forbids silent side effects (no event = bug)",
            "Sample pipeline runs locally",
            "Metrics defined without fake baselines",
        ],
    },
    {
        "title": "CI as a change-control plane",
        "theme": "CI as a change-control plane",
        "learn": "PR gates for Okta TF plan + agent tests — identity changes are code review",
        "competency": "platform",
        "path": "projects/11-okta-iac/",
        "feeds": ["M6", "M8"],
        "build": [
            "Harden GitHub Actions: fmt/validate/plan for Okta IaC; fail on drift format issues",
            "Agent CI job: lint + eval subset (or document blocker with risk)",
            "CODEOWNERS-style note: who must approve identity TF vs agent harness PRs",
        ],
        "doneWhen": [
            "Workflow files committed and explained",
            "Plan artifact path documented for reviewers",
            "Approval note exists even if CODEOWNERS not enabled",
        ],
    },
    # ── Phase 5: Endpoint + K8s literacy + assemble prep (W17–20) ──
    {
        "title": "Endpoint AI risk tied to identity tiers",
        "theme": "Endpoint AI risk tied to identity tiers",
        "learn": "Map Okta groups → AI tool tiers on MDM; shadow-AI controls with teeth",
        "competency": "endpoint",
        "path": "projects/09-endpoint-ai-governance/",
        "feeds": ["capstone"],
        "build": [
            "POLICY.md with risk tiers linked to M8 groups (not generic 'be careful')",
            "Exception process: time-bounded allow with audit fields",
            "Detection ideas: unsanctioned AI domains / binary allowlists (conceptual, sanitized)",
        ],
        "doneWhen": [
            "Every tier maps to a group from topology",
            "Exception process has owner + expiry",
            "No employer-internal URLs/data",
        ],
    },
    {
        "title": "Offboarding as distributed systems",
        "theme": "Offboarding as distributed systems",
        "learn": "Ordering, retries, and agent assist vs deterministic revoke of TF-managed access",
        "competency": "endpoint",
        "path": "projects/07-alius/",
        "feeds": ["capstone"],
        "build": [
            "Architecture: ordered revoke graph with compensations",
            "Failure modes: Okta down, MDM wipe delayed, SaaS without SCIM",
            "Where an agent may triage vs must never auto-revoke",
        ],
        "doneWhen": [
            "Diagram includes compensations",
            "Agent boundary is explicit",
            "Honest planning status retained",
        ],
    },
    {
        "title": "Hosting tradeoff: Cloud Run vs GKE for agents",
        "theme": "Hosting tradeoff: Cloud Run vs GKE for agents",
        "learn": "Defend a hosting choice with identity, scale, and progressive delivery constraints",
        "competency": "platform",
        "path": "study-notes/cloud-platform/",
        "feeds": ["M6"],
        "build": [
            "run-vs-gke.md as an ADR: decision, forces, consequences",
            "Optional micro-lab notes only if they strengthen the ADR",
            "Map WIF + revisions/traffic split to HITL release strategy",
        ],
        "doneWhen": [
            "ADR recommends default for THIS portfolio with reasons",
            "Counter-argument section included",
            "Link to platform foundation deploy path",
        ],
    },
    {
        "title": "Freeze the control plane architecture",
        "theme": "Freeze the control plane architecture",
        "learn": "Integrate M1–M8 into one narrative a hiring manager can attack",
        "competency": "harness",
        "path": "projects/08-capstone-ops-agent/",
        "feeds": ["capstone"],
        "build": [
            "ARCHITECTURE.md: component diagram + trust boundaries + data flows",
            "demo-script.md: 2-min path that surfaces IaC → agent → HITL → audit → deploy",
            "Risk register: top 5 residual risks for the POC",
        ],
        "doneWhen": [
            "Every Mi maps to a box on the diagram",
            "Demo script is timed",
            "Risks are honest (not 'none')",
        ],
    },
]

CAPSTONE_WEEKS = [
    {
        "title": "Capstone W1 — Integrate under eval pressure",
        "theme": "Integrate under eval pressure",
        "learn": "Assemble only what evals prove; MCP reads TF-managed groups",
        "competency": "harness",
        "path": "projects/08-capstone-ops-agent/",
        "feeds": ["capstone"],
        "build": [
            "Merge agent + MCP + API into one runnable plane",
            "Port eval suite; require 5 core cases green before feature polish",
            "Bind identity reads to sandbox groups that exist in Okta TF",
        ],
        "doneWhen": [
            "Single start command",
            "5 core evals green",
            "Group allow-list enforced",
        ],
    },
    {
        "title": "Capstone W2 — Enforce trust boundaries",
        "theme": "Enforce trust boundaries",
        "learn": "HITL + audit are non-optional control points",
        "competency": "identity",
        "path": "projects/08-capstone-ops-agent/",
        "feeds": ["capstone"],
        "build": [
            "HITL gate before any side effect",
            "Audit event on every query (incl. refusals)",
            "Reject privilege-escalation + unknown-group proposals",
        ],
        "doneWhen": [
            "Unapproved writes impossible in demo",
            "Audit samples committed",
            "Escalation evals still hold",
        ],
    },
    {
        "title": "Capstone W3 — Observe agent behavior",
        "theme": "Observe agent behavior",
        "learn": "SLOs, traces, and LLM cost/latency as first-class ops signals",
        "competency": "ops",
        "path": "projects/08-capstone-ops-agent/",
        "feeds": ["M7", "capstone"],
        "build": [
            "Emit structured logs + minimal trace/metric fields for tool calls",
            "SLO sketch: availability + escalation correctness (define measurement, no fake %)",
            "Wire endpoint policy stub into demo path",
        ],
        "doneWhen": [
            "One failed tool call is diagnosable from logs",
            "SLO note states numerator/denominator",
            "Policy check visible in demo",
        ],
    },
    {
        "title": "Capstone W4 — Deliver identity + cloud as code",
        "theme": "Deliver identity + cloud as code",
        "learn": "Show CI/TF path for GCP deploy and Okta plan; case study with limits",
        "competency": "platform",
        "path": "projects/08-capstone-ops-agent/",
        "feeds": ["M6", "M8", "capstone"],
        "build": [
            "Cloud Run deploy via platform foundation (or fully documented equivalent)",
            "Okta IaC plan still part of the story",
            "capstone-case-study.md: architecture, tradeoffs, what is NOT production",
        ],
        "doneWhen": [
            "Deploy path reproducible by a stranger",
            "Case study lists honest limits",
            "Portfolio README links the flagship",
        ],
    },
]

PORTFOLIO_WEEKS = [
    {
        "title": "Pressure-test the 2-minute demo",
        "theme": "Pressure-test the 2-minute demo",
        "learn": "Hiring-manager interruptions: security, identity, delivery questions mid-demo",
        "competency": "portfolio",
        "path": "projects/08-capstone-ops-agent/",
        "feeds": ["capstone"],
        "build": [
            "Rehearse demo with 5 interrupt questions written + answered",
            "Fix top eval failures blocking confidence",
            "Architecture diagram suitable for screen share",
        ],
        "doneWhen": ["Interrupt Q&A committed", "Demo under 2:30 including one interrupt"],
    },
    {
        "title": "Narrative: systems + cloud + agents",
        "theme": "Narrative: systems + cloud + agents",
        "learn": "One story from shipped AppLovin work to portfolio control plane",
        "competency": "portfolio",
        "path": "study-notes/platform-projects/platform-bridge.md",
        "feeds": ["capstone"],
        "build": [
            "Update platform-bridge.md with M1–M8 → flagship map",
            "Draft LinkedIn/about blurb without overclaiming AI production",
        ],
        "doneWhen": ["Narrative distinguishes shipped vs portfolio POC"],
    },
    {
        "title": "Recruiter technical one-pager",
        "theme": "Recruiter technical one-pager",
        "learn": "30-second scan: problem, architecture, proof artifacts",
        "competency": "portfolio",
        "path": "study-notes/",
        "feeds": ["capstone"],
        "build": ["recruiter-one-pager.md with links to dashboard, Okta IaC, capstone, evals"],
        "doneWhen": ["One-pager linked from README"],
    },
    {
        "title": "Metrics without fiction",
        "theme": "Metrics without fiction",
        "learn": "Define formulas from real volume only; refuse vanity KPIs",
        "competency": "ops",
        "path": "projects/05-adoption-dashboard/",
        "feeds": ["M5"],
        "build": ["metrics-baseline.md with formulas + data sources you actually have"],
        "doneWhen": ["No invented deflection/CSAT"],
    },
    {
        "title": "System design: Okta-as-code + SCIM + agents",
        "theme": "System design: Okta-as-code + SCIM + agents",
        "learn": "45-min design defending TF/SCIM/HITL split under drift and abuse",
        "competency": "portfolio",
        "path": "interview-prep/",
        "feeds": ["M8"],
        "build": ["Timed design → answers/okta-iac-scim-boundary.md with failure modes"],
        "doneWhen": ["Design includes sequence + abuse cases"],
    },
    {
        "title": "System design: agent hosting + identity",
        "theme": "System design: agent hosting + identity",
        "learn": "WIF, Cloud Run vs GKE, progressive delivery with HITL",
        "competency": "portfolio",
        "path": "interview-prep/",
        "feeds": ["M6"],
        "build": ["Timed design doc with explicit tradeoff table"],
        "doneWhen": ["Hosting recommendation defended with constraints"],
    },
    {
        "title": "STAR + resume for this lane",
        "theme": "STAR + resume for this lane",
        "learn": "Bullets that sell AI Systems + cloud delivery without lying",
        "competency": "portfolio",
        "path": "interview-prep/answers/behavioral-star.md",
        "feeds": ["capstone"],
        "build": ["STAR for automation, Okta-as-code, agent guardrails", "Resume bullets"],
        "doneWhen": ["Each bullet maps to an artifact link"],
    },
    {
        "title": "Mock loop under pressure",
        "theme": "Mock loop under pressure",
        "learn": "Design aloud + STAR + demo with self-score",
        "competency": "portfolio",
        "path": "interview-prep/",
        "feeds": ["capstone"],
        "build": ["Record notes from mock: gaps → next fixes"],
        "doneWhen": ["Self-score in wave-1-checklist.md"],
    },
    {
        "title": "Target map (AI Systems / agentic ops)",
        "theme": "Target map (AI Systems / agentic ops)",
        "learn": "Companies/teams where this portfolio is a fit",
        "competency": "portfolio",
        "path": "interview-prep/answers/wave-1-checklist.md",
        "feeds": ["capstone"],
        "build": ["3 targets with why-fit + which artifact you'd lead with"],
        "doneWhen": ["3 companies documented"],
    },
    {
        "title": "Apply with proof links",
        "theme": "Apply with proof links",
        "learn": "Applications that open dashboard + flagship + Okta IaC",
        "competency": "portfolio",
        "path": "interview-prep/",
        "feeds": ["capstone"],
        "build": ["1+ applications", "Outreach with portfolio URLs"],
        "doneWhen": ["Apply log updated"],
    },
    {
        "title": "Program retro: raise the bar",
        "theme": "Program retro: raise the bar",
        "learn": "What still feels basic; next-quarter hardening list",
        "competency": "portfolio",
        "path": "study-notes/",
        "feeds": ["capstone"],
        "build": ["program-retro.md with keep/kill/raise decisions"],
        "doneWhen": ["Next quarter challenges listed"],
    },
    {
        "title": "Keep-alive: evals + TF plan",
        "theme": "Keep-alive: evals + TF plan",
        "learn": "Portfolio rot is a bug — re-run proofs monthly",
        "competency": "portfolio",
        "path": "projects/08-capstone-ops-agent/",
        "feeds": ["capstone", "M8"],
        "build": ["Re-run evals", "terraform plan on Okta sandbox", "Note drift"],
        "doneWhen": ["Capstone still runnable", "Drift notes committed if any"],
    },
]


def get_week_plan(week: int) -> dict | None:
    if 1 <= week <= 20:
        p = MINI_PROJECTS[week - 1]
        return {
            "title": p["title"],
            "theme": p.get("theme", p["title"]),
            "learn": p.get("learn", ""),
            "miniProject": p,
            "phase": "mini",
            "competency": p["competency"],
            "feeds": p.get("feeds", []),
        }
    if 21 <= week <= 24:
        p = CAPSTONE_WEEKS[week - 21]
        return {
            "title": p["title"],
            "theme": p.get("theme", p["title"]),
            "learn": p.get("learn", ""),
            "miniProject": p,
            "phase": "capstone",
            "competency": p["competency"],
            "feeds": p.get("feeds", []),
        }
    if 25 <= week <= 36:
        p = PORTFOLIO_WEEKS[week - 25]
        return {
            "title": p["title"],
            "theme": p.get("theme", p["title"]),
            "learn": p.get("learn", ""),
            "miniProject": p,
            "phase": "portfolio",
            "competency": p["competency"],
            "feeds": p.get("feeds", []),
        }
    return None
