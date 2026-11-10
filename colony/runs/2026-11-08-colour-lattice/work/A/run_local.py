import sys, time, traceback
sys.path.insert(0, '/home/claude/phys-graph/lib'); sys.path.insert(0, '/home/claude/phys-graph/tp')
import types
tpp = types.ModuleType('tp_premise'); tpp.premise = lambda x: None; sys.modules['tp_premise'] = tpp
sys.path.insert(0, sys.argv[1])
import check
names = [n for n in dir(check) if n.startswith('check_')] if len(sys.argv) < 3 else sys.argv[2:]
for n in names:
    t = time.time()
    try:
        getattr(check, n)(); print('OK  ', n, round(time.time() - t, 1))
    except Exception:
        print('FAIL', n, round(time.time() - t, 1)); traceback.print_exc()
