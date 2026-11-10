import json,subprocess,sys
i=sys.argv[1]; lv=sys.argv[2:] or ['formal']
d=json.loads(subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({"id":i})],capture_output=True,text=True).stdout)
fm=d['front_matter']; print('##',i,'v',fm.get('version'),fm.get('status'),'|',fm.get('title'))
for l in lv:
    if l=='fm': print(json.dumps({k:fm[k] for k in fm if k in('derivations','extraction')})[:3000])
    else: print('['+l+']',d['levels'].get(l))
