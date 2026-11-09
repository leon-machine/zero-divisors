import json, sys, os
sys.path.insert(0, '/home/claude/phys-graph'); os.chdir('/home/claude/phys-graph')
from tp.mcp_server import Lab
lab = Lab('store')
ids = sys.argv[1:]
allc = {}
for i in ids:
    for e in lab.cone(id=i):
        allc[e['id']] = e
prem = {k: v for k, v in allc.items() if v['status'] in ('postulate', 'imported') or v['kind'] not in ('claim',)}
print('cone size', len(allc))
for k, v in sorted(prem.items()):
    print(v['status'], v['kind'], k, '|', (v.get('one_liner') or '')[:150].replace('\n',' '))
