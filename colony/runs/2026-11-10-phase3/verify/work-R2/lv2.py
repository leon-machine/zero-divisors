import sys,json
sys.path.insert(0,'.')
from tp.mcp_server import Lab
lab=Lab('store')
P=set(l.strip() for l in open('colony/runs/2026-11-10-phase3/verify/work-R2/postulates.txt'))
for i in sys.argv[1:]:
    full = i.startswith('+'); i=i.lstrip('+')
    r=lab.get_claim(id=i)
    fm=r.get('front_matter',{})
    print('#####',i,'v',fm.get('version'),fm.get('status'),'|',fm.get('title'))
    for d in fm.get('derivations',[]) or []:
        print('  deriv',d.get('name'),'uses',d.get('uses'),'assumes',d.get('assumes'))
    try:
        c=lab.cone(id=i,direction='past',limit=100000)
        print('  cone',len(c),'postulates:',sorted(x['id'] for x in c if x.get('status')=='postulate'))
    except Exception as e: print('  cone err',e)
    lv=r.get('levels',{})
    print('FORMAL:',lv.get('formal'))
    if full:
        print('TECH:',lv.get('technical')); print('ONE:',lv.get('one-liner'))
        for k,v in (r.get('proofs') or {}).items(): print('PROOF',k,':',v)
    print()
