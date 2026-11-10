import json, os, sys, collections
LAB="/home/claude/phys-graph"; sys.path.insert(0,LAB); os.chdir(LAB)
from tp.mcp_server import Lab
lab=Lab("store")
roots=["synthesis.field-space-premise-parallel-frozen-point","dark-energy.vacuum-region-registration-condition",
"dark-energy.frozen-point-makes-stelle-west-vector","dark-energy.imported-frozen-point-geometry",
"dark-energy.imported-henneaux-teitelboim-promotion","dark-energy.under-action-written-norm-parameter-laws",
"synthesis.number-n-registered-free-input","programme.n-parameter-of-the-laws","dark-energy.imported-macdowell-mansouri-theorem-stelle-west",
"synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part","dark-matter.p1-single-frozen-point","pred.dark-energy-w-minus-one"]
out={}
for r in roots:
    try:
        c=lab.cone(id=r,direction="future",limit=3000)
    except Exception as e:
        out[r]="ERR %r"%e; continue
    out[r]=[(x["id"],x.get("subject"),x.get("status"),x.get("kind")) for x in c] if isinstance(c,list) else c
json.dump(out,open(W:=LAB+"/colony/runs/2026-11-10-phase3/work/DA/cones_future.json","w"),indent=1)
for r,c in out.items():
    if isinstance(c,str): print(r,c); continue
    cnt=collections.Counter(x[1] for x in c)
    print(r,len(c),dict(cnt))
