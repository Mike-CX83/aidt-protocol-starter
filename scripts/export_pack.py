#!/usr/bin/env python3
import os, zipfile, datetime

ROOT = os.path.dirname(os.path.dirname(__file__))
OUT = os.path.join(ROOT, "deliverables")
os.makedirs(OUT, exist_ok=True)
ts = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

fname = os.path.join(OUT, f"aidt-export-{ts}.zip")
with zipfile.ZipFile(fname, "w", zipfile.ZIP_DEFLATED) as z:
    include = [
        "handoff/DECISIONS.md",
        "docs/adr/",
        "handoff/handshakes/",
        "handoff/agents/A1/STATE.yaml",
        "handoff/agents/A2/STATE.yaml",
        "handoff/agents/A1/PRD.yaml",
        "handoff/agents/A2/PRD.yaml",
        "handoff/agents/A1/BUILDPLAN.yaml",
        "handoff/agents/A2/BUILDPLAN.yaml",
    ]
    for item in include:
        path = os.path.join(ROOT, item)
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for f in files:
                    full = os.path.join(root, f)
                    z.write(full, os.path.relpath(full, ROOT))
        elif os.path.isfile(path):
            z.write(path, os.path.relpath(path, ROOT))

print("[export] wrote", fname)
