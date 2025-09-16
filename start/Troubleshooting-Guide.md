# Troubleshooting (Decision Tree)

**Problem:** “I’m lost / I don’t know what’s next.”  
→ Open `handoff/DECISIONS.md` and the latest handshake SUMMARY; ask Agent‑3 to summarize status and propose the next handshake or next actions.

**Problem:** “Plan changes didn’t stick.”  
→ A3 must issue an `A3.decision.yaml`. Open a new handshake; have A3 decide; verify an ADR was created.

**Problem:** “STATE.yaml is too long or token issues.”  
→ Ask the agent to roll up: keep `STATE.yaml` ≤ 8 KB and move narrative to a delta file in `LOG/changes`.

**Problem:** “Agents disagree.”  
→ Run a handshake: A1/A2 reports + responses; A3 decides. Only decisions can change plans.

**Problem:** “Where do I click?”  
→ Follow `start/START-HERE.md` → Quickstart section (first three links).
