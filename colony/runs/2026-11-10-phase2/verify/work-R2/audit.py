import json,subprocess,re,sys,collections
def call(tool,args):
    r=subprocess.run(['python3','colony/labcli.py',tool,json.dumps(args)],capture_output=True,text=True)
    return json.loads(r.stdout)
pats=[r"N\^\{?-?\d", r"M_\{?P\}?\s*/\s*H", r"G\s*\\Lambda", r"\\pi\s*N\^", r"v\s*/\s*H", r"10\^\{6[01]\}", r"10\^\{12[02]\}", r"N\s*=\s*M", r"\\sqrt\{3/\\Lambda\}", r"\\ln N", r"\\log_\{?2\}?\s*N", r"N\^\{2/3\}",r"N\^\{1/2\}", r"\\sqrt\{N\}"]
hits=collections.defaultdict(set)
for p in pats:
    try:
        res=call('find_text',{"pattern":p,"regex":True,"limit":400,"where":"formal"})
    except Exception as e:
        print('ERR',p,e); continue
    if isinstance(res,dict): res=res.get('results',res.get('hits',[]))
    for h in res: hits[h['id']].add(p)
print(len(hits),'entities')
ids=sorted(hits)
out=[]
for i in range(0,len(ids),150):
    r=call('get_claims',{"ids":ids[i:i+150],"fields":["status","kind","title"]})
    if isinstance(r,dict): r=r.get('claims',r.get('results',r))
    out+=r if isinstance(r,list) else list(r.values())
json.dump({'hits':{k:sorted(v) for k,v in hits.items()},'meta':out},open(sys.argv[1],'w'),indent=0)
for m in out:
    print(m.get('id'),'|',m.get('status'),'|',m.get('kind'),'|',(m.get('title') or '')[:70])
