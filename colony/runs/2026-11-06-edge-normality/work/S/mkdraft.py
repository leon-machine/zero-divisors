"""Build a validate_draft / propose_claim JSON from a draft folder: mkdraft.py <folder> <out.json>"""
import json
import os
import sys

d = sys.argv[1]
out = {"entity_md": open(os.path.join(d, "entity.md")).read(), "proofs": {}}
for name in sorted(os.listdir(d)):
    if name.endswith(".tex"):
        out["proofs"][name] = open(os.path.join(d, name)).read()
if os.path.exists(os.path.join(d, "check.py")):
    out["check_py"] = open(os.path.join(d, "check.py")).read()
json.dump(out, open(sys.argv[2], "w"))
