import re,json,subprocess,glob
ids=set()
for f in glob.glob('proposals/synthesis.*/entity.md'):
    if not any(k in f for k in ('born-weights','positivity-of-values-is','splits-adapted','local-weights','records-keep','no-two-valued')): continue
    t=open(f).read(); fm=t.split('## formal')[0]
    uses=re.findall(r'^\s+- ([a-z\-]+\.[A-Za-z0-9\-\.]+)@(\d+)',fm,re.M)
    refs=set(re.findall(r'claimref\{([^}]+)\}',t+open(f.replace('entity.md','proof-main.tex')).read()))
    print('==',f.split('/')[1][10:50]); 
    for i,v in uses:
        d=json.loads(subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({"id":i})],capture_output=True,text=True).stdout)
        cur=d['front_matter']['version']; print('  ',i,'pinned',v,'current',cur,d['front_matter']['status'],'' if str(cur)==v else '  <-- MISMATCH')
    print('   claimrefs not in uses/assumes:',sorted(refs-{i for i,_ in uses}))
