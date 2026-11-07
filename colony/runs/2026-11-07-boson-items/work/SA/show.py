import json,sys,subprocess
for id in sys.argv[2:]:
    out=subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({'id':id})],capture_output=True,text=True).stdout
    try: d=json.loads(out)
    except Exception: print(id,'ERR',out[:300]); continue
    fm=d['front_matter']; print('#####',id,'v',fm.get('version'),fm.get('status'),fm.get('kind'))
    print('uses:',[x.get('uses') for x in fm.get('derivations',[]) if isinstance(x,dict)])
    lv=d.get('levels',{})
    for k in sys.argv[1].split(','):
        if k in lv: print('--',k,':',lv[k][:6000])
        elif k=='proof': print('-- proofs:',json.dumps(d.get('proofs',{}))[:6000])
        elif k=='extraction': print('-- extraction:',json.dumps(fm.get('extraction',{}))[:3000])
