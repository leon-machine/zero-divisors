"""Local mutation probe (work tool): mimics the evidence layer's literal perturbation for one check file."""
import sys, os, types, time
LAB = "/home/claude/phys-graph"
sys.path.insert(0, LAB)
sys.path.insert(0, LAB + "/lib")
from tp import evidence
import tp_premise
tp_premise.configure(LAB + "/store")
src = open(sys.argv[1]).read()
only = sys.argv[2:] 
for func in sorted(evidence.function_names(src)):
    if not func.startswith("check_") or (only and func not in only):
        continue
    n = evidence.int_literal_count(src, func)
    ks = sorted({round(i * (n - 1) / 7) for i in range(8)}) if n > 8 else range(n)
    surv = []
    t0 = time.time()
    for k in ks:
        mut = evidence.mutate(src, func, k)
        mod = types.ModuleType("m")
        try:
            exec(compile(mut, "mut", "exec"), mod.__dict__)
            r = getattr(mod, func)()
            ok = r is not False
        except BaseException as e:
            ok = False
        if ok:
            surv.append(k)
    print(func, "literals", n, "tried", len(list(ks)), "survived", surv, "time %.1f" % (time.time() - t0))
