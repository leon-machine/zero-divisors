import sys, time, os
LAB='/home/claude/zero-divisors'
sys.path.insert(0, LAB+'/lib')
import tp_premise, GA
tp_premise.configure(LAB+'/store')
import importlib.util
path=LAB+'/store/claims/synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated/check.py'
spec = importlib.util.spec_from_file_location("chk", path)
chk = importlib.util.module_from_spec(spec); spec.loader.exec_module(chk)
names = sys.argv[1:] or sorted(n for n in dir(chk) if n.startswith("check_"))
for nme in names:
    t0=time.time()
    try:
        r = getattr(chk, nme)()
    except Exception as ex:
        import traceback; traceback.print_exc(); r = 'EXC'
    print(nme, r, round(time.time()-t0,2))
