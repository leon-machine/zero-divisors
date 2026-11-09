import json, subprocess, sys
def cone(i):
    out = subprocess.run(['python3','colony/labcli.py','cone',json.dumps({'id':i})],capture_output=True,text=True,cwd='/home/claude/phys-graph').stdout
    return json.loads(out)
seen={}
for i in sys.argv[1:]:
    for e in cone(i):
        if e['status'] in ('postulate','imported') or e['effective_status'] in ('postulate','imported','conjectured','argued'):
            seen.setdefault(e['id'],(e['status'],e['one_liner'][:130],set()))[2].add(i.split('.')[-1][:25])
for k,(s,o,w) in sorted(seen.items()):
    print(s,k,'|',o,'|',sorted(w))
