#!/bin/bash
# usage: gate.sh <proposal id> ...   (run from the lab root)
R=colony/runs/2026-11-10-phase2; export PYTHONDONTWRITEBYTECODE=1
for id in "$@"; do
  timeout 1500 python3 colony/check4.py proposals/$id > $R/verify/final/check4-$id.log 2>&1
  echo "exit $? $(tail -n 1 $R/verify/final/check4-$id.log | cut -c1-150)"
  python3 colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py proposals/$id $R/verify/final | cut -c1-200
done
