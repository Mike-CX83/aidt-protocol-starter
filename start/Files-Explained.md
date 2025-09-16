# Files Explained (What They Mean & Do)

- `handoff/brief.md` — your plain‑English idea.
- `handoff/agents/<Agent>/IDENTITY.yaml` — agent name, model, role.
- `handoff/agents/<Agent>/STATE.yaml` — the agent’s short memory; load this first.
- `handoff/agents/<Agent>/PRD.yaml` — goals & scope for that agent’s lane.
- `handoff/agents/<Agent>/BUILDPLAN.yaml` — step‑by‑step plan for that agent.
- `handoff/handshakes/HH-*/` — meeting packets between agents + A3 decision.
- `handoff/DECISIONS.md` — ledger of binding choices.
- `docs/adr/` — architecture decision records (auto‑generated).
- `schemas/*.json` — rules that keep the YAMLs consistent.
