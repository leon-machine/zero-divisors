import sys, time, os, cProfile, pstats
LAB='/home/claude/zero-divisors'
sys.path.insert(0, LAB+'/lib')
import tp_premise, GA, gtg
tp_premise.configure(LAB+'/store')
import importlib.util
path=LAB+'/store/claims/synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated/check.py'
spec = importlib.util.spec_from_file_location("chk", path)
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
F = c.F
t0=time.time()
pr = cProfile.Profile(); pr.enable()
wave = c.Wave(c.profile(c.W_BOTH, F(3,2)), c.S_ZERO, c.X0, c.HIGH)
t1=time.time()
cs = c.congruence_series(wave, c.HIGH-1)
pr.disable()
print(t1-t0, time.time()-t1)
pstats.Stats(pr).sort_stats('cumulative').print_stats(18)
