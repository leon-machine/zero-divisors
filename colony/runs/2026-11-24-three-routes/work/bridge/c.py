import json, subprocess, sys, re
LAB='/home/claude/leon-machine/zero-divisors'
def get(i):
    r = subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({'id':i})],cwd=LAB,capture_output=True,text=True)
    return json.loads(r.stdout)
# usage: c.py id [level|grep:pattern[:ctx]] ...
i=sys.argv[1]; d=get(i)
fm=d.get('front_matter',{}); lv=d.get('levels',{})
print('##',fm.get('id'),'v',fm.get('version'),'|',fm.get('status'),'|',fm.get('kind'),'|',fm.get('title'))
for a in sys.argv[2:]:
    if a.startswith('grep:'):
        parts=a.split(':'); pat=parts[1]; ctx=int(parts[2]) if len(parts)>2 else 300
        blob=json.dumps(d,ensure_ascii=False)
        for m in re.finditer(pat,blob,flags=re.I):
            s=max(0,m.start()-ctx); e=min(len(blob),m.end()+ctx)
            print('  ...'+blob[s:e].replace('\\n',' ')+'...'); print()
    elif a=='notes': print(json.dumps(d.get('notes'),ensure_ascii=False)[:4000])
    elif a=='derived':
        dv=d.get('derived',{}); print({k:dv.get(k) for k in ('rests_on','used_by','holds_given','effective_status')})
    elif a=='flags': print(fm.get('extraction',{}).get('flags'))
    else: print(f'[{a}]', lv.get(a))
