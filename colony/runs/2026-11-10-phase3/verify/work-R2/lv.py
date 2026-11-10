import sys,json,subprocess
for i in sys.argv[1:]:
    full = i.startswith('+'); i=i.lstrip('+')
    r=json.loads(subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({"id":i})],capture_output=True,text=True).stdout)
    fm=r.get('front_matter',{})
    print('#####',i,'v',fm.get('version'),fm.get('status'),'|',fm.get('title'))
    for d in fm.get('derivations',[]) or []:
        print('  deriv',d.get('name'),'uses',d.get('uses'),'assumes',d.get('assumes'))
    lv=r.get('levels',{})
    print('FORMAL:',lv.get('formal'))
    if full:
        print('TECH:',lv.get('technical')); print('LAY:',lv.get('lay')); print('ONE:',lv.get('one-liner'))
        for k,v in (r.get('proofs') or {}).items(): print('PROOF',k,':',v)
    print()
