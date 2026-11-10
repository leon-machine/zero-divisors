import sys, json, subprocess
# print status + statement (truncated) of claims
n = int(sys.argv[1])
for cid in sys.argv[2:]:
    out = subprocess.run(["python3","colony/labcli.py","get_claim",json.dumps({"id":cid})],capture_output=True,text=True).stdout
    try:
        d = json.loads(out)
    except Exception:
        print(cid, "ERR", out[:300]); continue
    fm = d.get("front_matter",{}); lv = d.get("levels",{})
    st = lv.get("statement") or lv.get("technical") or ""
    print("==", cid, "|", fm.get("status"), "| v", fm.get("version"), "| subj", fm.get("subject"))
    if not st:
        print("levels:", list(lv.keys()))
    print(str(st)[:n]); print()
