# AIDT Protocol v1.0 — Handshake & Handoff Protocol (HHP)

## Goals
- Vendor-agnostic, project-agnostic multi-agent dev process.
- Turn stateless LLM sessions into **file-based continuity**.
- Enforce **decision gates** and **auditability**.

## Core Concepts
- **Agent**: A role with a folder of artifacts (IDENTITY, SOP, PRD, BUILDPLAN, STATE, REGISTRY, LOG).
- **Handoff**: The file-based state capsule an agent leaves behind (STATE + deltas).
- **Handshake**: A bidirectional exchange between agents + a binding decision by Review.
- **Decision Gate**: Only A3-approved changes may modify plans and PRDs.
- **Delta**: Append-only YAML describing a change.

## Lifecycle
1. **Plan** → Update BUILDPLAN via A3 decisions.
2. **Do** → Produce code/docs and a delta file.
3. **Check** → New handshake; Review adjudicates.
4. **Act** → Apply decision; roll up STATE; repeat.

## Minimal Compliance (L1)
- Each agent has: IDENTITY.yaml, SOP.yaml, PRD.yaml, BUILDPLAN.yaml, STATE.yaml.
- Handshake folders: A1.report, A2.report, A1.response, A2.response, A3.decision.
- Decisions ledger (`handoff/DECISIONS.md`) is append-only.

## Strong Compliance (L2)
- Validators in CI block plan edits without matching decision references.
- Automated state rollups run on each PR.

## Full Compliance (L3)
- Metrics (lead time, delta throughput), risk registry, retro reports, provenance tagging.
