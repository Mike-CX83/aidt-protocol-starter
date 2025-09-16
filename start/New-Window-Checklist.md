# New Context Window Checklist

**For any agent (A1/A2/A3):** copy/paste this at the start of a fresh chat.

1) Identify yourself (A1/A2/A3) and your role.
2) Load files in this order:
   - For A1: `handoff/agents/A1/STATE.yaml` → `handoff/DECISIONS.md` → `handoff/agents/A1/BUILDPLAN.yaml` → `handoff/agents/A1/PRD.yaml`
   - For A2: `handoff/agents/A2/STATE.yaml` → `handoff/DECISIONS.md` → `handoff/agents/A2/BUILDPLAN.yaml` → `handoff/agents/A2/PRD.yaml`
   - For A3: `handoff/brief.md` → `handoff/DECISIONS.md` → latest `handoff/handshakes/HH-*/*` → A1 & A2 `STATE.yaml`
3) Summarize “where we are” in 3 bullets.
4) Execute the first `next_action` (A1/A2) or open a handshake/decision (A3).
5) Create or update a delta (DL-*.yaml) and **refresh `STATE.yaml`** (≤ 8 KB).
