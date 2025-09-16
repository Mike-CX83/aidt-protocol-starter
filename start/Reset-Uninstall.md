# Reset / Uninstall (Safe Cleanup)

- **Reset states:** delete `handoff/handshakes/HH-*` and `handoff/agents/*/LOG/changes/*` (keep plans/PRDs if you want).
- **Export before removing:** run `python3 scripts/export_pack.py` to save decisions, ADRs, plans, and states.
- **Remove the starter:** delete the `start/`, `templates/`, and `scripts/` folders if you want a clean project tree.
