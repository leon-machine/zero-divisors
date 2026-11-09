"""R2 helper: union of past cones of a proposal's premises; list postulates in it with versions.

usage: python3 cone_audit.py <proposal-folder>   (reads uses/assumes from entity.md front matter)
"""
import os
import re
import sys

LAB = "/home/claude/phys-graph"
sys.path.insert(0, LAB)
os.chdir(LAB)
import yaml  # noqa: E402
from tp.mcp_server import Lab  # noqa: E402

lab = Lab("store")
folder = sys.argv[1]
txt = open(os.path.join(folder, "entity.md")).read()
fm = yaml.safe_load(txt.split("---")[1])
direct = []
for d in fm.get("derivations", []):
    for key in ("uses", "assumes"):
        for x in d.get(key, []) or []:
            direct.append((key, x))
print("DIRECT PREMISES:")
seen = {}
for key, x in direct:
    i, _, v = x.partition("@")
    c = lab.get_claim(id=i)
    cur = c["front_matter"].get("version")
    st = c["front_matter"].get("status")
    print(f"  [{key}] {i} pinned@{v} current@{cur} status={st}")
    seen[i] = 1
# also claimrefs in the formal/technical and proof
refs = set(re.findall(r"\\claimref\{([^}]+)\}", txt))
for f in os.listdir(folder):
    if f.endswith(".tex"):
        refs |= set(re.findall(r"\\claimref\{([^}]+)\}", open(os.path.join(folder, f)).read()))
extra = sorted(r for r in refs if r not in seen)
print("CLAIMREFS NOT IN uses/assumes:", extra)
post = {}
allc = set()
for i in list(seen) + extra:
    try:
        cone = lab.cone(id=i, direction="past", limit=5000)
    except Exception as e:  # noqa: BLE001
        print("  cone fail", i, e)
        continue
    items = cone if isinstance(cone, list) else cone.get("entities", cone)
    for e in items:
        allc.add(e["id"])
        if e.get("status") == "postulate":
            post.setdefault(e["id"], set()).add(i)
    c = lab.get_claim(id=i)
    if c["front_matter"].get("status") == "postulate":
        post.setdefault(i, set()).add("(direct)")
print(f"PAST CONE SIZE (union): {len(allc)}")
print("POSTULATES IN CONE:")
for p in sorted(post):
    c = lab.get_claim(id=p)
    fnd = " FOUNDATION" if c["front_matter"].get("foundation") else ""
    print(f"  {p} @{c['front_matter'].get('version')}{fnd} via {sorted(post[p])[:3]}")
