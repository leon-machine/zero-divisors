import json,sys,subprocess
cid=sys.argv[1]; lev=sys.argv[2] if len(sys.argv)>2 else 'formal'
out=subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({'id':cid})],capture_output=True,text=True).stdout
d=json.loads(out)
fm=d['front_matter']
print('STATUS',fm.get('status'),'v',fm.get('version'),'kind',fm.get('kind'))
for k in ('derivations','checked_by','flags','amendments','extraction','lineage'):
    if k in fm and lev!='formalonly': print(k,':',json.dumps(fm[k])[:3000])
if lev=='all':
    for k,v in d['levels'].items(): print('=====',k); print(v)
else:
    print(d['levels'].get(lev.replace('only','')))
print([k for k in d.keys()])
