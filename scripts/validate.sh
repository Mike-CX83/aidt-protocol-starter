#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob
echo "[validate] checking basic structure..."
need_dirs=(handoff handoff/handshakes templates scripts docs)
for d in "${need_dirs[@]}"; do
  [[ -d "$d" ]] || { echo "[validate] missing dir: $d"; exit 1; }
done
echo "[validate] OK (basic)"

python3 scripts/schema_validate.py || { echo "[validate] schema checks failed"; exit 1; }
