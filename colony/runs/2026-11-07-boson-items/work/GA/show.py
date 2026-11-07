import json, subprocess, sys
LAB="/home/claude/phys-graph"
full = '--full' in sys.argv
for i in [a for a in sys.argv[1:] if not a.startswith('--')]:
    r = subprocess.run(["python3","colony/labcli.py","get_claim",json.dumps({"id":i})],cwd=LAB,capture_output=True,text=True)
    try: d=json.loads(r.stdout)
    except Exception: print("ERR",i,r.stderr[-300:]); continue
    fm=d["front_matter"]; lv=d.get("levels",{})
    print("=====",i,"v",fm.get("version"),"|",fm.get("status"),"|",fm.get("title"))
    print("uses:", [u for dv in fm.get("derivations",[]) for u in dv.get("uses",[])])
    if fm.get("outside_ga"): print("outside_ga:", fm["outside_ga"])
    print("FORMAL:", lv.get("formal","")[: (20000 if full else 3500)])
    if full:
        for k,v in d.get("proofs",{}).items(): print("PROOF",k,":",str(v)[:20000])
