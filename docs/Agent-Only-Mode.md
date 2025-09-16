# Agent-Only Mode (Zero-Code Onboarding)

**Goal:** A human drops this repo into an IDE (e.g., Cursor), enters a plain-English idea,
and the **agents do the rest**. Agent-3 (Review) acts as the **bootstrapper**:
it converts the idea into a build, assigns roles, and kicks off work.

## Steps for a Non-Developer (Human)
1. Open the repo in your IDE.
2. Edit `handoff/brief.md` (or leave the example) to describe your idea in plain words.
3. Open `prompts/agent3-autoboot.md` and ask your IDE to run it as Agent-3 (Review).
4. Agent-3 will:
   - Create agents (A1 Logic, A2 Build) if missing
   - Fill real `PRD.yaml` and `BUILDPLAN.yaml` (no placeholders)
   - Assign division of labor and timelines
   - Create the first handshake packet (HH-*) and a decision
   - Update `STATE.yaml` for A1 and A2 so they can start immediately
5. Open A1 and A2 folders in separate IDE agent sessions and say: **Proceed with your STATE**.

No bash required. If you prefer the CLI, see the project README for `make` commands.
