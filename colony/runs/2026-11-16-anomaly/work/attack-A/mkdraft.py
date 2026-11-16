import json, sys, os
d = sys.argv[1].rstrip("/")
proofs = {"proof-main.tex": open(os.path.join(d, "proof-main.tex")).read()}
out = {"entity_md": open(os.path.join(d, "entity.md")).read(), "proofs": proofs,
       "check_py": open(os.path.join(d, "check.py")).read()}
json.dump(out, open(d + ".draft.json", "w"))
print("wrote", d + ".draft.json")
