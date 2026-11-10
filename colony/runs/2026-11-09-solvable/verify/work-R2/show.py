"""R2 helper: print an entity's version, status, formal (and optionally other levels / proof).

usage: python3 show.py <id> [levels comma list, default formal] [proof]
"""
import os
import sys

LAB = "/home/claude/phys-graph"
sys.path.insert(0, LAB)
os.chdir(LAB)
from tp.mcp_server import Lab  # noqa: E402

lab = Lab("store")
i = sys.argv[1]
levels = (sys.argv[2] if len(sys.argv) > 2 else "formal").split(",")
c = lab.get_claim(id=i)
fm = c["front_matter"]
print(f"== {i} v{fm.get('version')} status={fm.get('status')} title={fm.get('title')}")
for d in fm.get("derivations", []) or []:
    print("  uses:", d.get("uses"), "assumes:", d.get("assumes"))
for lv in levels:
    print(f"-- {lv}:")
    print(c["levels"].get(lv, ""))
if len(sys.argv) > 3:
    for p in c.get("proofs", []) if isinstance(c.get("proofs"), list) else c.get("proofs", {}).items():
        print("-- proof:", str(p)[:20000])
