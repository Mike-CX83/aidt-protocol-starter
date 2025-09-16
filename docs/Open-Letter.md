# An Open Letter: Run AI Agents Like a Real Dev Team

**AIDT / HHP v1.0 — The AI Agent Dev Team System**  
Date: 2025-09-16

Friends, builders, educators — this project started with a simple question:
> *How can a single person orchestrate multiple AI agents to build real software — reliably, transparently, and without writing code?*

The **AI Agent Dev Team (AIDT)** protocol — also called the **Handshake & Handoff Protocol (HHP)** — is our answer.
It turns stateless LLM sessions into a **process-first team**. Instead of ephemeral chats and forgotten context, we use
files (not memory) to create continuity, accountability, and teachable steps that anyone can follow.

---

## Why this exists

- **Non‑developers** should be able to open a repo, describe an idea in plain English, and let agents do the rest.
- **Developers** should have a minimal, vendor‑agnostic way to run multiple agents like teammates — with
  traceable decisions and small, reversible steps.
- **Educators** should be able to teach orchestration as a skill — not a black box.

---

## The core idea

We use three roles:

- **Agent‑1 (Logic):** language/spec/knowledge — the *what* and *why* in executable form.  
- **Agent‑2 (Build):** infra/code/tools — the *how* and *ship it*.  
- **Agent‑3 (Review):** planning, adjudication, and **bootstrap** — the *scope, decisions, and guardrails*.

Two rituals keep them aligned:

- **Handoff:** Each agent drops a small `STATE.yaml` “memory capsule” and an append‑only delta note.  
- **Handshake:** A1 and A2 exchange reports/responses; **A3** produces a binding decision (`A3.decision.yaml`) —
  plan changes only happen through this gate. An ADR is auto‑generated for the record.

The result is a **repeatable, auditable workflow**. You can read it, teach it, and run it anywhere.

---

## Agent‑Only Mode (zero‑code onboarding)

A non‑dev can do three things:
1. Open the repo in an IDE (e.g., Cursor).  
2. Edit `handoff/brief.md` in plain English.  
3. Run the prompt in `prompts/agent3-autoboot.md` as **Agent‑3**.

Agent‑3 will create Agents 1 & 2, write real plans (not placeholders), open the first handshake,
issue a decision, and prepare both agents’ `STATE.yaml` files so work can begin immediately.

---

## What makes this work

- **Files, not memory** — `STATE.yaml`, deltas, handshakes, and decisions live in the repo. Chats come and go; artifacts remain.
- **Decision gate** — Only A3 changes PRDs and plans; CI can enforce this.
- **Small, reversible steps** — Every change is a delta; plans evolve through handshakes.
- **Vendor‑agnostic** — Works with any LLMs/IDEs; identities are declarative.
- **Teachability** — “Start Here,” trigger commands, and role prompts make orchestration learnable.

---

## What this is not

- A monolithic framework. It’s a **protocol** and a **starter** — you can adopt or adapt any piece.  
- A magic button. Someone still provides intent (your idea), reviews outcomes, and steers the work.

---

## Getting started (tl;dr)

- **Read:** `start/START-HERE.md` and `docs/Agent-Only-Mode.md`.  
- **Say:** “Agent‑3, bootstrap from `handoff/brief.md` and prepare A1/A2 to proceed.”  
- **Then:** Tell A1 or A2, “Load your `STATE.yaml` and execute your `next_actions`.”  
- **When plans change:** Open a handshake; A3 makes a decision; an ADR is generated.

If you prefer terminals: `make validate`, `make new-handshake`, and `A=A1 make rollup` are available too.

---

## Governance & trust

- **A3** is the only gate for plan edits.  
- **CI guard** blocks unapproved PRD/BUILDPLAN changes.  
- **Schemas** keep YAMLs consistent.  
- **ADRs** record the why, not just the what.  
- **Metrics** (optional) summarize cadence and follow‑ups.

---

## The road to open source

This repo includes a license, contribution guide, code of conduct, issue/PR templates, schemas, and CI checks.
As we grow, we’ll ship **presets** (web app, data pipeline, OS stub), a **demo target**, and simple dashboards.
The protocol will remain **free, vendor‑agnostic, and teachable**.

If you improve it — docs, templates, prompts, validators — please share back.
Let’s help more people run **AI teams that build real things**.

— *AIDT / HHP Maintainers*  
v1.0.0 (proposed)
