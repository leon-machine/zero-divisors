#!/usr/bin/env python3
"""Run every check_* function in a check.py against the cloud copy of the store.

  python3 colony/runcheck.py path/to/check.py

premise() resolves ids against /home/claude/lab/transport_lab/store, and GA.py and
tp_premise.py come from the lab's lib/. Reports pass/fail per function (a function fails if it raises, returns False,
or records a GA.check failure, as the evidence layer counts it) and the
premises each check touched.
"""
import importlib.util
import os
import sys
import traceback

LAB = os.environ.get("TP_LAB") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise  # noqa: E402
import GA  # noqa: E402

tp_premise.configure(os.path.join(LAB, "store"))
path = os.path.abspath(sys.argv[1])
sys.path.insert(0, os.path.dirname(path))
spec = importlib.util.spec_from_file_location("check_under_test", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
fails = 0
for name in sorted(n for n in dir(mod) if n.startswith("check_") and callable(getattr(mod, n))):
    tp_premise.TOUCHED.clear()
    nfail = len(GA.FAILURES)
    try:
        r = getattr(mod, name)()
        bad = r is False or len(GA.FAILURES) > nfail
        if bad:
            fails += 1
            why = "returned False" if r is False else "GA.check failure: " + "; ".join(GA.FAILURES[nfail:])
            print(f"FAIL {name}   ({why})")
        else:
            print(f"PASS {name}   premises touched: {sorted(tp_premise.TOUCHED)}")
    except Exception:
        fails += 1
        print(f"FAIL {name}")
        traceback.print_exc()
sys.exit(1 if fails else 0)
