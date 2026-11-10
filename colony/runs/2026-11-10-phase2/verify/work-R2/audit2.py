import json,subprocess
def call(tool,args):
    r=subprocess.run(['python3','colony/labcli.py',tool,json.dumps(args)],capture_output=True,text=True)
    return json.loads(r.stdout)
d=json.load(open('colony/runs/2026-11-10-phase2/verify/work-R2/audit.json'))
strong=[r"M_\{?P\}?\s*/\s*H", r"G\s*\\Lambda", r"\\pi\s*N\^", r"v\s*/\s*H", r"N\s*=\s*M", r"\\sqrt\{3/\\Lambda\}", r"\\ln N", r"10\^\{6[01]\}", r"10\^\{12[02]\}",r"N\^\{2/3\}",r"N\^\{1/2\}", r"\\sqrt\{N\}",r"\\log_\{?2\}?\s*N"]
ids={k for k,v in d['hits'].items() if set(v)&set(strong)}
tg=call('list_entities',{"tag":"the-number-n","limit":300,"fields":["id","status","kind"]})
tg=tg.get('entities',tg.get('results',tg)) if isinstance(tg,dict) else tg
tagged={e['id'] for e in tg}
print('strong pattern hits',len(ids),'tagged',len(tagged),'union',len(ids|tagged))
allids=sorted(i for i in ids|tagged if not i.startswith('note.'))
r=call('get_claims',{"ids":allids,"fields":["status","kind","one_liner","title"]})
r=r.get('claims',r) if isinstance(r,dict) else r
for m in r:
    print('*',m.get('id'),'|',m.get('status'),'|',m.get('kind'),'|T' if m.get('id') in tagged else '|', (m.get('one-liner') or m.get('one_liner') or m.get('title') or '')[:330])
