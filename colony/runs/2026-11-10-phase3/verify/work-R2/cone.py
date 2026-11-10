import sys,json,os
sys.path.insert(0,'.')
from tp.mcp_server import Lab
lab=Lab('store')
import subprocess
P=set(l.strip() for l in open('colony/runs/2026-11-10-phase3/verify/work-R2/postulates.txt'))
for i in sys.argv[1:]:
    c=lab.cone(id=i,direction='past',limit=100000)
    ids=[x['id'] for x in c] if isinstance(c,list) else c
    if not isinstance(c,list): print(i,str(c)[:300]); continue
    allp=sorted(x['id'] for x in c if x.get('status')=='postulate')
    print('##',i,'cone size',len(ids)); print('  DM postulates:',sorted(set(ids)&P)); print('  other postulates:',[p for p in allp if p not in P])
