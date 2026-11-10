import json,subprocess,sys
def cone(i):
    o=subprocess.run(['python3','colony/labcli.py','cone',json.dumps({'id':i})],capture_output=True,text=True).stdout
    return json.loads(o)
allp={}
for i in sys.argv[1:]:
    for e in cone(i):
        if e.get('kind') in ('premise','postulate','hypothesis') or e.get('status') in ('imported','postulate','premise','assumed','conjectured','argued','computed','hypothesis'):
            allp.setdefault((e.get('kind'),e.get('status'),e['id']),set()).add(i.split('.')[-1][:25])
for k in sorted(allp): print(k[0],'|',k[1],'|',k[2],'  <-',len(allp[k]))
