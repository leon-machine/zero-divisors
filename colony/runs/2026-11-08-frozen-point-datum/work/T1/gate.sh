#!/bin/bash
# gate one proposal: runcheck (if a check), check4 (if a check), validate_one; logs in verify/final
cd /home/claude/phys-graph
ID=$1
P=proposals/$ID
OUT=colony/runs/2026-11-08-frozen-point-datum/verify/final
if [ -f $P/check.py ]; then
  python3 colony/runcheck.py $P/check.py > $OUT/T1-$ID.runcheck.log 2>&1
  echo "runcheck: $(grep -c '^PASS check_' $OUT/T1-$ID.runcheck.log) pass, $(grep -c '^FAIL' $OUT/T1-$ID.runcheck.log) fail"
  python3 colony/check4.py $P > $OUT/T1-$ID.check4.log 2>&1
  echo "check4 exit $?: $(tail -1 $OUT/T1-$ID.check4.log)"
  grep -E "^(E|W)[0-9]|W413" $OUT/T1-$ID.check4.log | head -5
fi
python3 colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py $P $OUT
