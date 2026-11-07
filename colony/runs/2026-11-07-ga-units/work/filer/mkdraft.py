import json, os, sys
folder = os.path.abspath(sys.argv[1])
d = {"entity_md": open(os.path.join(folder, "entity.md")).read(), "proofs": {}}
for f in sorted(os.listdir(folder)):
    if f.endswith(".tex") or f == "coverage.yaml":
        d["proofs"][f] = open(os.path.join(folder, f)).read()
if os.path.exists(os.path.join(folder, "check.py")):
    d["check_py"] = open(os.path.join(folder, "check.py")).read()
out = os.path.join(os.path.dirname(folder), os.path.basename(folder) + ".draft.json")
json.dump(d, open(out, "w"))
print(out)
