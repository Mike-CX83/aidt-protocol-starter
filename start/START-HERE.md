# START HERE — AI Agent Dev Team System (AIDT / HHP)

## Quickstart: Only Four Things


1) **Write the idea** → `handoff/brief.md`  
2) **Run Agent‑3** → open `prompts/agent3-autoboot.md` and execute it  
3) **Tell A1/A2** → “Proceed with your `STATE.yaml`”  
4) **When plans change** → “Agent‑3, open a handshake and decide it.”

That’s it. Everything else is optional.

**Who this is for:** People with *no coding background* who want AI agents to do the setup and work.

## What you'll do (3 steps)
1) Open this repo in your IDE (e.g., Cursor).  
2) Open and edit `handoff/brief.md` — describe your idea in plain English.  
3) Open `prompts/agent3-autoboot.md` and run it as Agent‑3; follow the on‑screen guidance.

**After that:** Agent‑3 creates Agents 1 & 2, writes plans, opens the first handshake, and prepares their `STATE.yaml` files so they can start immediately.

---

## How the system works (in one minute)
- **Agents:** A1 (Logic) builds specs and language/knowledge artifacts; A2 (Build) implements infra/tools/code; A3 (Review) plans, adjudicates, and bootstraps.
- **Handoff:** Each agent leaves a short `STATE.yaml` as the “memory” for the next session.
- **Handshake:** A1 and A2 report and respond; **A3** makes a binding decision.
- **Decision Gate:** Plans change *only* via A3’s decision file.

See: `docs/Agent-Only-Mode.md` for the zero‑code flow.

---

## Where to click first
- `handoff/brief.md` — write your idea here.  
- `prompts/agent3-autoboot.md` — paste this into Agent‑3 and run.  
- `handoff/BOOTSTRAP_DONE.md` — check this after A3 finishes.

---

## Repo map (annotated)
- `start/` — these beginner docs.
- `handoff/` — working area: agents, handshakes, decisions, brief.
- `docs/` — specs, guides, compliance, ADRs, metrics docs.
- `schemas/` — JSON Schemas for key YAML files.
- `scripts/` — helpers (validation, rollups, metrics).
- `templates/` — blueprints for new agents and handshakes.
- `.github/` — CI and issue/PR templates (open‑source ready).

Open‑source notes: see `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.

---

## Common actions (copy‑paste prompts)
- **Start the project:** “Agent‑3, bootstrap from `handoff/brief.md`, create Agents 1 & 2, produce plans, open HH‑01, decide, and prepare STATEs.”
- **Resume work:** “Agent‑1 (or 2), load your `STATE.yaml` and proceed with `next_actions`.”
- **Propose a change to the plan:** “Open a new handshake; draft A1/A2 reports; request A3 decision.”
- **Troubleshoot:** “Run `make validate` in the terminal or ask Agent‑3 to run validation.”

---

## FAQ (short)
- **Do I need to code?** No — just write the idea and run Agent‑3.
- **What files matter most?** `handoff/brief.md`, the handshake folder, each agent’s `STATE.yaml`.
- **Why so many YAMLs?** They act as memory and audit trail for stateless AI sessions.
- **Can I use different models?** Yes — set each agent’s `IDENTITY.yaml` in its folder.

If you get stuck, open `docs/Cursor-Guide.md` or ask Agent‑3 to guide you step‑by‑step.

**When you open a new chat window:** copy prompts from `start/Trigger-Commands.md` or use the per‑agent files in `prompts/` (agent1‑load‑proceed.md, agent2‑load‑proceed.md, agent3‑oversight‑cycle.md).


See also: the **Open Letter** at `docs/Open-Letter.md` for the why and the big picture.



## Simple Mode
- Read `start/START-HERE.md#quickstart-only-four-things` — the one‑page version.
- Use the **Onboarding Wizard**: `prompts/agent3-onboarding-wizard.md` (keeps questions to 3).
- Pin files via `handoff/pinset.json` (agents can read this automatically).
- When in doubt, run `python3 scripts/self_test.py`.

## Wrap‑up
- Export the important artifacts with `python3 scripts/export_pack.py`.
- See `start/Reset-Uninstall.md` if you want to clean up the starter later.

## Learn More (Deeper Help)
- **First Hour Walkthrough:** `start/First-Hour.md`
- **New Context Window Checklist:** `start/New-Window-Checklist.md`
- **Troubleshooting:** `start/Troubleshooting-Guide.md`
- **Examples & Scenarios:** `start/Scenarios.md`
