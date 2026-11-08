import json,subprocess,sys
for id in sys.argv[1:]:
    out=subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({'id':id})],capture_output=True,text=True).stdout
    try: d=json.loads(out)
    except Exception: print(out[:3000]); continue
    fm=d['front_matter']
    print('#####',id,'v',fm.get('version'),fm.get('status'))
    print('uses:',[x for der in fm.get('derivations',[]) for x in der.get('uses',[])])
    print(d['levels'].get('formal',''))
    print()
