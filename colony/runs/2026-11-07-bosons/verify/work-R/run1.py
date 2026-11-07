"""Run selected check_* functions of a (possibly perturbed) check module. usage: run1.py module.py fn [fn...]"""
import importlib.util, os, sys
LAB = "/home/claude/phys-graph"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
spec = importlib.util.spec_from_file_location("m", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for fn in sys.argv[2:]:
    n0 = len(GA.FAILURES)
    try:
        r = getattr(m, fn)()
        print("PASS" if (r is not False and len(GA.FAILURES) == n0) else "FAIL", fn)
    except Exception as e:
        print("FAIL(exc)", fn, repr(e)[:200])
