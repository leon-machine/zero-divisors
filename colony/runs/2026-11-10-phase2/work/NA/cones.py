import json, os, sys
LAB = "/home/claude/phys-graph"
sys.path.insert(0, LAB); os.chdir(LAB)
from tp.mcp_server import Lab
lab = Lab("store")
rows = json.load(open("colony/runs/2026-11-10-phase2/work/NA/n_mentions.json"))
ids = [r[0] for r in rows] + ["tower.fock-module-one-qubit-per-rung", "tower.witt-index-quantum-capacity", "tower.ladder-pairs-satisfy-car-vectors", "tower.answers-iteration-question"]
allc = {}
per = {}
for i in ids:
    try:
        res = lab.cone(id=i, limit=5000)
    except Exception as e:
        print("ERR", i, e); continue
    if isinstance(res, dict): res = res.get("past") or res.get("cone") or res.get("entities") or []
    per[i] = [x["id"] for x in res if isinstance(x, dict)]
    for x in res:
        if isinstance(x, dict): allc[x["id"]] = (x.get("status"), x.get("title"))
json.dump({"per": per, "all": allc}, open("colony/runs/2026-11-10-phase2/work/NA/cones.json", "w"), indent=0)
print(len(allc))
from collections import Counter
print(Counter(v[0] for v in allc.values()))
for k, v in sorted(allc.items()):
    if v[0] == "postulate": print("POST", k, "|", v[1])
print({k: len(v) for k, v in per.items()})
