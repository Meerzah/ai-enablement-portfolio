# Endpoint AI Governance (portfolio module)

**Competency:** Endpoint & fleet management + AI enablement  
**Status:** Portfolio design + policy templates (not employer MDM deploy)

## Problem

Employees use AI tools outside governed paths (CLI agents, desktop apps, browser chat). IT needs **policy at the endpoint** aligned with identity and approved tool lists — without claiming a specific vendor rollout in this public repo.

## What you build (Weeks 17–18)

1. **Policy doc:** `POLICY.md` — approved vs prohibited AI tool categories
2. **MDM checklist:** `MDM-ROLLOUT-CHECKLIST.md` — generic Kandji/Intune-style rollout steps (no internal URLs)
3. **Identity link:** how device posture + user group gates agent access in capstone
4. **Offboarding tie-in:** pointer to `07-alius` design for device + access + SaaS sequence

## Architecture (conceptual)

```
MDM policy profile
    └── Approved AI tools list / block list
Endpoint agent or gateway (concept)
    └── Routes AI traffic through policy engine
Identity (Okta)
    └── Group membership → which tools/workflows allowed
Capstone agent
    └── Checks policy stub before executing tools
```

## Done when

- [ ] POLICY.md committed
- [ ] MDM checklist committed
- [ ] Capstone references endpoint policy module
- [ ] No employer-specific fleet data in public repo

See [CURRICULUM.md](../../CURRICULUM.md) pillar 2.
