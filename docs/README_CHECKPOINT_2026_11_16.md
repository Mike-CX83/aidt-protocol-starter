# Historical README checkpoint

Preserved before the November 16, 2026 source review. Use the root README for the current distinction between the manual protocol, implemented helpers, and known command line defects.

# AIDT Protocol v1.0 — AI Agent Dev Team System (Universal)

A reusable, **vendor-agnostic** protocol and scaffold for running multi-agent dev teams
inside IDEs like Cursor — with **handoffs**, **handshakes**, and **decision gates** that
turn stateless context windows into a cohesive, auditable build process.

- Protocol codename: **HHP — Handshake & Handoff Protocol**
- Version: v1.0
- License: MIT (see `LICENSE`)

## TL;DR (for facilitators)
```bash
make validate          # sanity checks
make new-agent N=A1    # create agent A1 (or A2/A3...)
make new-handshake     # stamp a new HH folder with templates
A=A1 make rollup       # roll up Agent A1 state from deltas+decisions
H=handshakes/<HH-id> make apply-decision   # append A3 decision to ledger
```
Works on macOS/Linux. Windows users can run: `python3 scripts/aidt.py <command>`

## Why this exists
- Teach devs to **operate multiple LLM agents like a real team**
- Keep work **consistent** across context windows (no hidden memory)
- Make decisions **traceable** and **enforceable** (A3 review gate)
- Fit **any project**: OS build, web app, research system, etc.


## Compliance Levels
- **L1** Minimal — manual discipline, schema checks optional.
- **L2** Strong — CI enforces schema + plan-edit guard.
- **L3** Full — metrics, ADRs, permissions, provenance.

## Metrics
Run `python3 scripts/metrics.py` to output weekly CSV for dashboards.


## Agent-Only Mode (Zero-Code)
- Edit `handoff/brief.md` with your idea.
- Open `prompts/agent3-autoboot.md` in an Agent-3 session and run it.
- A3 will create A1/A2 plans, open the first handshake, decide it, and prepare STATEs.
- Then open A1 and A2 and say, “Proceed with your STATE.”

**New users:** Open `start/START-HERE.md` first.

- Read the **Open Letter**: `docs/Open-Letter.md`
