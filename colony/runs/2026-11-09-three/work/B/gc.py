import json,subprocess,sys
def gc(i,n=6000,proof=0):
    o=json.loads(subprocess.run(["python3","colony/labcli.py","get_claim",json.dumps({"id":i})],capture_output=True,text=True).stdout)
    fm=o["front_matter"]
    print("#####",i,"|",fm.get("status"),"v",fm.get("version"),"|",fm.get("title"))
    print("-- uses:",[ (u.get("id") if isinstance(u,dict) else u) for u in fm.get("uses",[])], "assumes:",fm.get("assumes"))
    lv=o["levels"]
    print("-- levels keys:",list(lv.keys()) if isinstance(lv,dict) else type(lv))
    for k in (["formal"] if isinstance(lv,dict) else []):
        print("--",k,":",str(lv.get(k))[:n])
    if proof:
        print("-- proofs:",json.dumps(o["proofs"],ensure_ascii=False)[:proof])
    if o.get("notes"): print("-- notes:",json.dumps(o["notes"],ensure_ascii=False)[:1500])
n=int(sys.argv[1]);p=int(sys.argv[2])
for i in sys.argv[3:]: gc(i,n,p)
