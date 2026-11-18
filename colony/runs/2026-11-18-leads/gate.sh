#!/bin/bash
# central gate for one proposal: validate_draft, then check4. usage: gate.sh <id> <tag>
cd /home/claude/phys-graph
id=$1; tag=${2:-fix}; V=colony/runs/2026-11-18-leads/verify
mkdir -p /tmp/gate/$id
python3 - "$id" <<'P'
import json,sys,os
i=sys.argv[1]; d='proposals/'+i
j={"entity_md":open(d+'/entity.md').read(),"proofs":{}}
for f in os.listdir(d):
    if f.endswith('.tex') and not f.startswith('orig-'): j["proofs"][f]=open(d+'/'+f).read()
if os.path.exists(d+'/check.py'): j["check_py"]=open(d+'/check.py').read()
json.dump(j,open('/tmp/gate/%s/draft.json'%i,'w'))
P
python3 colony/labcli.py validate_draft @/tmp/gate/$id/draft.json > $V/validate_${tag}_$id.log 2>&1
nice -n 5 python3 colony/check4.py proposals/$id > $V/check4_${tag}_$id.log 2>&1
echo "$tag $id check4 EXIT $? validate: $(grep -o '"ok": *[a-z]*' $V/validate_${tag}_$id.log | head -1) $(grep -c '"code"' $V/validate_${tag}_$id.log) findings" >> $V/gate_summary.txt
