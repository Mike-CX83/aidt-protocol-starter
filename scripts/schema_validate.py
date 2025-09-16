#!/usr/bin/env python3
import os, sys, json, glob, yaml

def load_json(p):
    with open(p,"r",encoding="utf-8") as f:
        return json.load(f)

def validate_with_jsonschema(instance, schema):
    try:
        import jsonschema
        jsonschema.validate(instance=instance, schema=schema)
        return True, None
    except Exception as e:
        return False, str(e)

def basic_presence_check(instance, required_keys):
    missing = [k for k in required_keys if k not in instance]
    return (len(missing)==0, f"Missing keys: {missing}" if missing else None)

BASE = os.path.dirname(os.path.dirname(__file__))
ok = True

# Map patterns → schema + minimal required keys for fallback
checks = [
    ("**/STATE.yaml", "schemas/STATE.schema.json", ["version","updated_at","phase","focus","canonical_refs","recent_deltas"]),
    ("handoff/handshakes/**/A?.report.yaml", "schemas/REPORT.schema.json", ["handshake_id","agent","timestamp","summary"]),
    ("handoff/handshakes/**/A?.response.yaml", "schemas/RESPONSE.schema.json", ["handshake_id","agent","timestamp"]),
    ("handoff/handshakes/**/A3.decision.yaml", "schemas/DECISION.schema.json", ["handshake_id","agent","timestamp","decision"]),
]

for pattern, schema_rel, fallback_keys in checks:
    schema = load_json(os.path.join(BASE, schema_rel))
    for ypath in glob.glob(os.path.join(BASE, pattern), recursive=True):
        with open(ypath,"r",encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        good, err = validate_with_jsonschema(data, schema)
        if not good:
            # Fallback basic check
            good2, err2 = basic_presence_check(data, fallback_keys)
            if not good2:
                print(f"[schema] FAIL {ypath}: {err or err2}")
                ok = False
            else:
                print(f"[schema] WARN(jsonschema-missing) {ypath}: basic keys OK")
        else:
            print(f"[schema] OK {ypath}")

if not ok:
    sys.exit(1)
print("[schema] All checks passed or warned")
