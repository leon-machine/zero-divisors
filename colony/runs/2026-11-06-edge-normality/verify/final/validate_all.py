import json, os, sys, subprocess, glob
lab = os.path.abspath('.')
out = sys.argv[1]
for d in sorted(glob.glob('proposals/*/')):
    pid = os.path.basename(d.rstrip('/'))
    draft = {'entity_md': open(d+'entity.md').read()}
    proofs = {os.path.basename(p): open(p).read() for p in glob.glob(d+'proof-*.tex')}
    if proofs: draft['proofs'] = proofs
    if os.path.exists(d+'check.py'): draft['check_py'] = open(d+'check.py').read()
    jp = os.path.abspath(f'{out}/{pid}.draft.json'); json.dump(draft, open(jp,'w'))
    r = subprocess.run(['python3','colony/labcli.py','validate_draft','@'+jp],capture_output=True,text=True)
    open(f'{out}/{pid}.validate.json','w').write(r.stdout+r.stderr)
    try:
        v=json.loads(r.stdout); print(pid, 'ok=',v.get('ok'), [f.get('code') for f in v.get('findings',[]) if str(f.get('code','')).startswith(('E','W'))])
    except Exception as e: print(pid,'parse error',r.stdout[:200],r.stderr[-300:])
