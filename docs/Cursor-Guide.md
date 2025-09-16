# Using the AIDT Protocol with Cursor (or any IDE)

1) Open the repo in Cursor.
2) Pin `handoff/agents/A1/STATE.yaml` to the context and tell Cursor to use it as the first file.
3) Run `make new-handshake` from the terminal to start a new exchange.
4) After your work, generate a delta file under `LOG/changes/` and run `A=A1 make rollup`.
5) Switch to Agent 2 tab/workspace and repeat with its `STATE.yaml`.
6) Have Agent 3 review the handshake and produce `A3.decision.yaml`.
7) Run `H=<path> make apply-decision` to update the ledger; update plans accordingly.
