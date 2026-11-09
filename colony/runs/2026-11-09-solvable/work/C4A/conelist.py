import json, subprocess, sys
def cone(i):
    out = subprocess.run(['python3','colony/labcli.py','cone',json.dumps({'id':i})],capture_output=True,text=True,cwd='/home/claude/phys-graph').stdout
    return json.loads(out)
for i in sys.argv[1:]:
    c = cone(i)
    print('#####', i, len(c))
    for e in c:
        if e['status'] in ('postulate','imported','conjectured','argued','live') or e['effective_status'] not in ('proved',):
            print(' ', e['status'], e['effective_status'], e['id'], '|', e['one_liner'][:160])
