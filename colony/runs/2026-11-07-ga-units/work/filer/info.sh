#!/bin/bash
# usage: info.sh id1 id2 ...
cd /home/claude/phys-graph
for id in "$@"; do
python3 colony/labcli.py get_claim "{\"id\": \"$id\"}" | python3 -c "
import json,sys; d=json.load(sys.stdin); fm=d.get('front_matter',{}); dv=d.get('derived',{})
print('$id', 'v', fm.get('version'), fm.get('status'), '| ledger', dv.get('ledger'), '| eff', dv.get('effective_status'), '| holds_given', dv.get('holds_given'))"
done
