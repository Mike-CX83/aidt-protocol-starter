# Workflows

## Agent‑Only (No Terminal Needed)
1) Edit `handoff/brief.md`.
2) Run `prompts/agent3-autoboot.md` as Agent‑3.
3) Wait for `handoff/BOOTSTRAP_DONE.md`.
4) Tell A1 and A2: “Proceed with your STATE.”

## Power‑User (Optional Terminal)
- `make validate` — structure & schema checks.
- `make new-agent N=A4` — add another agent.
- `make new-handshake` — stamp a new handshake.
- `A=A1 make rollup` — refresh an agent’s `STATE.yaml`.
