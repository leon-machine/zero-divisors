#!/bin/bash
# Gate one T2 proposal: runcheck, check4, validate_one, then register with propose_claim
# (hand-made folder moved aside, files compared, extra files such as coverage.yaml copied back).
# Usage: gate.sh <id> [noregister]
set -u
cd /home/claude/phys-graph
R=colony/runs/2026-11-08-frozen-point-datum
V=$R/verify/final
id=$1
P=proposals/$id
rm -rf $P/__pycache__
if [ -f $P/check.py ]; then
  python3 colony/runcheck.py $P/check.py > $V/T2-$id.runcheck.log 2>&1; echo "runcheck exit=$?"; cat $V/T2-$id.runcheck.log | grep -v "^PASS" | head -20
  grep -c "^PASS" $V/T2-$id.runcheck.log
fi
python3 colony/check4.py $P > $V/T2-$id.check4.log 2>&1; echo "check4 exit=$?"
grep -E "^(E|W)[0-9]+" $V/T2-$id.check4.log; tail -1 $V/T2-$id.check4.log
python3 colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py $P $V
[ "${2:-}" = noregister ] && exit 0
rm -rf $P/__pycache__
A=$R/work/T2/aside/$id
rm -rf $A; mkdir -p $R/work/T2/aside; mv $P $A
python3 colony/labcli.py propose_claim @$PWD/$V/$id.draft.json > $V/T2-$id.propose.log 2>&1
python3 -c "import json,sys;d=json.load(open('$V/T2-$id.propose.log'));print('propose accepted_for_review=',d.get('accepted_for_review'),'replaces_existing=',d.get('replaces_existing'),[f['code'] for f in d.get('findings',[]) if f['code'][0] in 'EW'])"
if [ ! -d $P ]; then echo "NOT REGISTERED: restoring folder"; mv $A $P; exit 1; fi
for f in $(cd $A && ls); do
  if [ -f $P/$f ]; then cmp -s $A/$f $P/$f && echo "same $f" || echo "DIFF $f"; else cp $A/$f $P/$f; echo "copied back $f"; fi
done
[ -f $P/coverage.yaml ] && python3 -c "import yaml;yaml.safe_load(open('$P/coverage.yaml'));print('coverage.yaml parses')"
exit 0
