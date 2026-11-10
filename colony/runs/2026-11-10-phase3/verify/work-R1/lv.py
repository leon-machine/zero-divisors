import sys, json, subprocess
cid = sys.argv[1]; lv = sys.argv[2:] or ['formal']
o = subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({"id":cid})],capture_output=True,text=True).stdout
d = json.loads(o)
fm = d.get('front_matter',{})
print('ID',fm.get('id'),'v',fm.get('version'),'status',fm.get('status'),'|',fm.get('title'))
for dv in fm.get('derivations',[]): print(' uses',dv.get('uses'))
for l in lv:
    print('##',l); print(d.get('levels',{}).get(l))
