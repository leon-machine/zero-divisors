import sys, json, subprocess
def get(tool, arg):
    r = subprocess.run(['python3','colony/labcli.py',tool,json.dumps(arg)],capture_output=True,text=True,cwd='/home/claude/phys-graph')
    try: return json.loads(r.stdout)
    except Exception: return r.stdout + r.stderr
for cid in sys.argv[1:]:
    lim = 6000
    if ':' in cid: cid, lim = cid.split(':'); lim=int(lim)
    d = get('get_claim', {'id': cid})
    if isinstance(d,str): print(cid, d[:500]); continue
    fm = d.get('front_matter', {})
    print('=====', fm.get('id'), 'v', fm.get('version'), fm.get('status'), fm.get('subject'))
    print('title:', fm.get('title'))
    print('keys:', list(d.keys()), list(d.get('levels',{}).keys()))
    for k in ('uses','premises','depends','assumes'):
        if k in fm: print(k, ':', json.dumps(fm[k])[:1500])
    print((d.get('levels',{}).get('formal') or '')[:lim])
