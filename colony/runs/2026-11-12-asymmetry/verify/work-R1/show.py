import sys,json,subprocess
for cid in sys.argv[1:]:
    out=subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({'id':cid})],capture_output=True,text=True).stdout
    d=json.loads(out)
    fm=d.get('front_matter',{})
    print('#####',cid,'| version',fm.get('version'),'| status',fm.get('status'),'| kind',fm.get('kind'))
    print('TITLE:',fm.get('title'))
    print('FORMAL:',d.get('levels',{}).get('formal'))
    print('PROOFS:',[ (p.get('name'),len(p.get('text','') or '')) if isinstance(p,dict) else p for p in (d.get('proofs') or [])] if isinstance(d.get('proofs'),list) else list((d.get('proofs') or {}).keys()))
    print()
