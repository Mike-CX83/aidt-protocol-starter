#!/usr/bin/env python3
import os, glob, yaml, json, sys
ROOT = os.path.dirname(os.path.dirname(__file__))

def fail(msg):
    print("[self-test] FAIL:", msg); sys.exit(1)

# Check critical files
for path in ["aidt.config.yaml","handoff/brief.md","handoff/pinset.json"]:
    if not os.path.exists(os.path.join(ROOT, path)):
        fail(f"missing {path}")

# Check STATE sizes and presence if agents exist
for agent in ["A1","A2"]:
    st = os.path.join(ROOT,"handoff","agents",agent,"STATE.yaml")
    if os.path.exists(st):
        if os.path.getsize(st) > 8*1024:
            fail(f"{agent} STATE.yaml is over 8KB; please rollup.")
print("[self-test] OK")
