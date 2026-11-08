#!/bin/bash
# move the gated hand-made folder aside, register it with propose_claim, copy coverage.yaml back, compare
cd /home/claude/phys-graph
ID=$1
R=colony/runs/2026-11-08-frozen-point-datum
A=$R/work/T1/aside
mkdir -p $A
rm -rf $A/$ID
mv proposals/$ID $A/
python3 colony/labcli.py propose_claim @$PWD/$R/verify/final/$ID.draft.json > $R/verify/final/T1-$ID.propose.log 2>&1
python3 -c "import json,sys;v=json.load(open('$R/verify/final/T1-$ID.propose.log'));print('$ID registered:',v.get('accepted_for_review'),'replaces_existing:',v.get('replaces_existing'),[f['code'] for f in v.get('findings',[]) if f['code'][0] in 'EW'])"
for f in $(ls $A/$ID); do
  [ "$f" = "__pycache__" ] && continue
  if [ -f proposals/$ID/$f ]; then cmp -s $A/$ID/$f proposals/$ID/$f || echo "DIFFERS: $f"; else cp $A/$ID/$f proposals/$ID/ && echo "copied back $f"; fi
done
[ -f proposals/$ID/coverage.yaml ] && python3 -c "import yaml;yaml.safe_load(open('proposals/$ID/coverage.yaml'))" && echo "coverage parses"
