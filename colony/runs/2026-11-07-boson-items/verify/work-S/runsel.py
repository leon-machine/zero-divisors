"""Run selected check_* functions of a (possibly perturbed) check file. Usage: runsel.py file.py name [name...]"""
import importlib.util, os, sys
LAB = "/home/claude/phys-graph"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
path = os.path.abspath(sys.argv[1])
sys.path.insert(0, os.path.dirname(path))
spec = importlib.util.spec_from_file_location("cut", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
names = sys.argv[2:] or sorted(n for n in dir(mod) if n.startswith("check_"))
for n in names:
    k = len(GA.FAILURES)
    try:
        r = getattr(mod, n)()
        bad = r is False or len(GA.FAILURES) > k
        print(("FAIL " if bad else "PASS ") + n)
    except Exception as e:
        print("RAISE " + n + ": " + repr(e)[:200])
