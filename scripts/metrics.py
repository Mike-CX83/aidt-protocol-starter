#!/usr/bin/env python3
import os, glob, yaml, csv, datetime

ROOT = os.path.dirname(os.path.dirname(__file__))

def parse_ts(ts):
    try:
        # naive: keep original string if parsing fails
        return datetime.datetime.fromisoformat(ts.replace("Z","+00:00"))
    except Exception:
        return None

def main():
    handshakes = sorted(glob.glob(os.path.join(ROOT, "handoff", "handshakes", "HH-*")))
    rows = []
    for hh in handshakes:
        decf = os.path.join(hh, "A3.decision.yaml")
        if not os.path.exists(decf): continue
        with open(decf,"r",encoding="utf-8") as f:
            dec = yaml.safe_load(f) or {}
        ts = parse_ts(dec.get("timestamp",""))
        rows.append({
            "handshake": os.path.basename(hh),
            "decision": dec.get("decision",""),
            "timestamp": dec.get("timestamp",""),
            "followups": len(dec.get("followups",[]) or [])
        })
    # Weekly CSV
    today = datetime.date.today()
    week = today.isocalendar().week
    outdir = os.path.join(ROOT, "metrics")
    os.makedirs(outdir, exist_ok=True)
    outcsv = os.path.join(outdir, f"weekly-{today.year}{week:02d}.csv")
    with open(outcsv,"w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["handshake","decision","timestamp","followups"])
        w.writeheader()
        w.writerows(rows)
    print(f"[metrics] wrote {outcsv} ({len(rows)} rows)")

if __name__ == "__main__":
    main()
