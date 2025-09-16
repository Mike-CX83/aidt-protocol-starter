#!/usr/bin/env bash
set -euo pipefail
# Detect if PRD.yaml or BUILDPLAN.yaml changed without including any A3.decision.yaml in the diff.
BASE="${GITHUB_BASE_REF:-origin/HEAD}"
if git rev-parse --verify "$BASE" >/dev/null 2>&1; then
  git fetch origin +refs/heads/*:refs/remotes/origin/* >/dev/null 2>&1 || true
  DIFF=$(git diff --name-only "$BASE"...HEAD || git diff --name-only HEAD~1)
else
  DIFF=$(git diff --name-only HEAD~1)
fi

PLAN_CHANGED=$(echo "$DIFF" | grep -E '(PRD.yaml|BUILDPLAN.yaml)' || true)
HAS_DECISION=$(echo "$DIFF" | grep -E 'handoff/handshakes/.+/A3.decision.yaml' || true)

if [[ -n "$PLAN_CHANGED" && -z "$HAS_DECISION" ]]; then
  echo "[guard] PRD/BUILDPLAN changed without a matching A3.decision.yaml in diff."
  echo "$DIFF"
  exit 1
fi
echo "[guard] OK"
