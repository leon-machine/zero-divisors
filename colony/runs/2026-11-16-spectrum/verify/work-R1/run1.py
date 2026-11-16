import importlib.util, os, sys
LAB = "/home/claude/phys-graph"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
path, fn = os.path.abspath(sys.argv[1]), sys.argv[2]
sys.path.insert(0, os.path.dirname(path))
spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
try:
    r = getattr(m, fn)()
    print(fn, "returned", r, "failures:", GA.FAILURES[:5])
except Exception as e:
    print(fn, "RAISED", type(e).__name__, str(e)[:300])
