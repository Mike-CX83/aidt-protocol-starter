# Trigger Commands (Copy/Paste Prompts)

Use these exact prompts in a **new context window** to keep agents aligned.

## A3 — Bootstrap / Oversight
**Resume Oversight (new tab/window):**
> You are Agent‑3 (Review + Bootstrap). Load and follow in order: `handoff/brief.md`, `handoff/DECISIONS.md`, latest `handoff/handshakes/HH-*/*`, and each agent `STATE.yaml` (A1 then A2). Summarize status, detect plan/PRD drift, and if needed open a new handshake with reports/responses. If any plan change is required, produce `A3.decision.yaml` and an ADR. Finish with a checklist of next actions for A1 and A2.

**Start a New Feature/Change:**
> Agent‑3, open a new handshake (HH‑now‑NN). Draft A1/A2 reports with concrete artifacts and tests, then request/produce a decision. Update both `STATE.yaml` files with 1–3 next actions and pin sets.

## A1 — Logic / Language / Knowledge
**Load & Proceed (new window):**
> You are Agent‑1. Load files in this order: `handoff/agents/A1/STATE.yaml` → `handoff/DECISIONS.md` → `handoff/agents/A1/BUILDPLAN.yaml` → `handoff/agents/A1/PRD.yaml`. Read the last handshake and decision. Confirm `next_actions` and execute step 1 now. When done, write a delta file under `handoff/agents/A1/LOG/changes/` (DL‑*.yaml), then propose whether a handshake is required. If any conflict with `DECISIONS.md`, HOLD and ask Agent‑3.

**Health Check & Rollup:**
> Agent‑1, validate schemas and roll up state. Ensure `STATE.yaml` ≤8KB and includes `ingest_order` and `pin_set`. If it’s larger, move narrative to a DL file.

## A2 — Infra / Build / Tools
**Load & Proceed (new window):**
> You are Agent‑2. Load files in this order: `handoff/agents/A2/STATE.yaml` → `handoff/DECISIONS.md` → `handoff/agents/A2/BUILDPLAN.yaml` → `handoff/agents/A2/PRD.yaml`. Read the last handshake and decision. Execute the first `next_action`, write artifacts, then create a DL file in `handoff/agents/A2/LOG/changes/`. If your change touches PRD/BUILDPLAN, request a handshake and A3 decision.

**Validation & Packaging:**
> Agent‑2, run validation and ensure headers/specs/tooling are updated. Suggest CI updates if needed.

## Universal (Any Agent)
**State Refresh (token hygiene):**
> Roll up your state: summarize today’s changes into `STATE.yaml` (≤8KB), list recent delta paths, and pin the 3 most important files to load next session.

**Drift Watch:**
> Compare BUILDPLAN and PRD with DECISIONS. If different, HOLD and alert Agent‑3 to adjudicate.
