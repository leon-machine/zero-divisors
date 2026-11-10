import json, sys, os
d = sys.argv[1]
out = {"entity_md": open(os.path.join(d, "entity.md")).read(),
       "proofs": {"proof-main.tex": open(os.path.join(d, "proof-main.tex")).read()},
       "check_py": open(os.path.join(d, "check.py")).read()}
json.dump(out, open(d + ".draft.json", "w"))
