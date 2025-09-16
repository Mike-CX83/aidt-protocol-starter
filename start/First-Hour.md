# Your First Hour (Step-by-Step)

**Goal:** Go from idea → plans → first decision → Agents 1 & 2 ready to work.

## 0–10 min: Describe your idea
- Open `handoff/brief.md`
- Write 3 bullets: What you want, who it's for, first success (what “done” looks like)

## 10–25 min: Let Agent‑3 bootstrap
- Open `prompts/agent3-onboarding-wizard.md`
- Paste it into your Agent‑3 chat and run it
- Agent‑3 will ask up to 3 short questions and then:
  - Create A1/A2 (if needed)
  - Fill real `PRD.yaml` and `BUILDPLAN.yaml` (no placeholders)
  - Create `HH-<timestamp>-01` and issue `A3.decision.yaml`
  - Update A1/A2 `STATE.yaml` with next actions

## 25–45 min: Start A1 and A2
- Open two new chats/tabs: one for **Agent‑1**, one for **Agent‑2**
- Copy prompts from `start/Trigger-Commands.md` → “Load & Proceed” for each agent
- Each agent executes the first `next_action` and writes a delta (DL-*.yaml)

## 45–60 min: Validate and recap
- Ask Agent‑3 to run a health check:
  - schemas valid, `STATE.yaml` ≤ 8 KB, plan vs. decision is aligned
- Read `handoff/BOOTSTRAP_DONE.md` and your latest handshake SUMMARY
- Decide whether to start the next handshake or continue execution
