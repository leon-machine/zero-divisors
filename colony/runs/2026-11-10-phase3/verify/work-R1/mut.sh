#!/bin/bash
# usage: mut.sh <check.py> <tag> <sed-expr>
d=$W/mut-$2; mkdir -p $d; sed -e "$3" "$1" > $d/check.py
if cmp -s "$1" $d/check.py; then echo "MUTATION $2: NO CHANGE"; exit; fi
out=$(PYTHONDONTWRITEBYTECODE=1 nice python3 colony/runcheck.py $d/check.py 2>&1); rc=$?
echo "MUTATION $2: rc=$rc; failing functions: $(echo "$out" | grep -c '^FAIL check_') ; $(echo "$out" | grep '^FAIL check_' | cut -c1-90 | head -4 | tr '\n' ';')"
