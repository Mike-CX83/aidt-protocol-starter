#!/usr/bin/env python3
import os, sys, argparse, shutil, datetime, json, textwrap

ROOT = os.path.dirname(os.path.dirname(__file__))
TZSTAMP = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S%z")

def ensure(p):
    os.makedirs(p, exist_ok=True)

def write(path, content):
    ensure(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(textwrap.dedent(content).lstrip("\n"))

def new_agent(agent_id: str):
    agdir = os.path.join(ROOT, "handoff", "agents", agent_id)
    ensure(agdir)
    # Seed from template
    tmpl = os.path.join(ROOT, "templates", "AGENT")
    for root, dirs, files in os.walk(tmpl):
        rel = os.path.relpath(root, tmpl)
        target_root = os.path.join(agdir, rel) if rel != "." else agdir
        ensure(target_root)
        for d in dirs:
            ensure(os.path.join(target_root, d))
        for f in files:
            src = os.path.join(root, f)
            dst = os.path.join(target_root, f.replace("AGENT", agent_id))
            with open(src, "r", encoding="utf-8") as rf:
                content = rf.read().replace("AGENT", agent_id)
            with open(dst, "w", encoding="utf-8") as wf:
                wf.write(content)
    print(f"[new-agent] created {agdir}")

def new_handshake(seq: str):
    hh = os.path.join(ROOT, "handoff", "handshakes", f"HH-{TZSTAMP}-{seq}")
    ensure(hh)
    for name in ["A1.report.yaml","A2.report.yaml","A1.response.yaml","A2.response.yaml","A3.decision.yaml"]:
        src = os.path.join(ROOT, "templates", name)
        dst = os.path.join(hh, name)
        shutil.copyfile(src, dst)
    with open(os.path.join(hh, "SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write(f"# Handshake {os.path.basename(hh)}\n")
    print(f"[new-handshake] created {hh}")

def rollup(agent: str):
    agdir = os.path.join(ROOT, "handoff", "agents", agent)
    stpath = os.path.join(agdir, "STATE.yaml")
    # naive rollup: capture last 10 deltas
    changes_dir = os.path.join(agdir, "LOG", "changes")
    deltas = sorted([os.path.join(changes_dir, f) for f in os.listdir(changes_dir) if f.endswith(".yaml")])[-10:]
    version = 1
    updated = TZSTAMP
    # minimal state update
    state = f\"""
version: {version}
updated_at: {updated}
recent_deltas:
- {chr(10).join([f"path: {os.path.relpath(p, agdir)}" for p in deltas]) if deltas else ""}
\"""
    with open(stpath, "w", encoding="utf-8") as f:
        f.write(state.strip()+"\n")
    print(f"[rollup] updated {stpath}")

def next_adr_number(adr_dir):
    nums = []
    for name in os.listdir(adr_dir):
        m = re.match(r"(\d{4})-", name)
        if m: nums.append(int(m.group(1)))
    return (max(nums)+1 if nums else 1)

def slugify(s):
    return re.sub(r'[^a-z0-9]+','-', s.lower()).strip('-')

def apply_decision(hh_path: str):
    ledger = os.path.join(ROOT, "handoff", "DECISIONS.md")
    # Append to decisions ledger
    with open(ledger, "a", encoding="utf-8") as f:
        f.write(f"## {datetime.date.today()} {hh_path}\n- See {hh_path}/A3.decision.yaml\n\n")
    print(f"[apply-decision] appended to {ledger}")

    # Generate ADR
    adr_dir = os.path.join(ROOT, "docs", "adr")
    os.makedirs(adr_dir, exist_ok=True)
    # Read decision file
    dec_path = os.path.join(hh_path, "A3.decision.yaml")
    try:
        import yaml
        with open(dec_path,"r",encoding="utf-8") as df:
            dec = yaml.safe_load(df) or {}
    except Exception:
        dec = {}

    n = next_adr_number(adr_dir)
    title = dec.get("decision","PENDING") + " " + os.path.basename(hh_path)
    fname = f"{n:04d}-{slugify(title)}.md"
    body = f\"\"\"# ADR {n:04d}: {title}

Date: {datetime.date.today()}

## Status
Accepted (from handshake {os.path.basename(hh_path)})

## Context
See {hh_path}/A1.report.yaml and {hh_path}/A2.report.yaml for background.

## Decision
- Decision: {dec.get("decision","PENDING")}
- Binding: {dec.get("binding",[])}
- Rationale: {dec.get("rationale","")}

## Consequences
- Followups: {dec.get("followups",[])}
- Plans/PRDs touched must reference this ADR.
\"\"\"
    with open(os.path.join(adr_dir, fname),"w",encoding="utf-8") as outf:
        outf.write(body)

    # Update ADR index
    index_path = os.path.join(adr_dir, "index.md")
    with open(index_path, "a", encoding="utf-8") as idx:
        idx.write(f"- {n:04d}: {fname}\\n")

    print(f"[apply-decision] ADR created docs/adr/{fname}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("new-agent"); p1.add_argument("--id", required=True)
    p2 = sub.add_parser("new-handshake"); p2.add_argument("--seq", default="01")
    p3 = sub.add_parser("rollup"); p3.add_argument("--agent", required=True)
    p4 = sub.add_parser("apply-decision"); p4.add_argument("--handshake", required=True)

    a = ap.parse_args()
    if a.cmd == "new-agent": new_agent(a.id)
    elif a.cmd == "new-handshake": new_handshake(a.seq)
    elif a.cmd == "rollup": rollup(a.agent)
    elif a.cmd == "apply-decision": apply_decision(a.handshake)

if __name__ == "__main__":
    main()
