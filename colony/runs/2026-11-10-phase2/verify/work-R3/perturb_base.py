import sys,os,importlib.util
LAB='/home/claude/phys-graph'; sys.path.insert(0,LAB+'/lib'); sys.dont_write_bytecode=True
import tp_premise,GA
tp_premise.configure(LAB+'/store')
from fractions import Fraction as F
def load():
    p=LAB+'/proposals/synthesis.antiperiodic-array-against-the-light-ray-continuum-at-window-length-r/check.py'
    s=importlib.util.spec_from_file_location('c',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def run(m,names):
    out={}
    for nm in names:
        nf=len(GA.FAILURES)
        try: r=getattr(m,nm)(); out[nm]=not(r is False or len(GA.FAILURES)>nf)
        except Exception as e: out[nm]='EXC '+repr(e)[:60]
    return out
names=['check_self_duality_of_the_partition_function','check_energy_matches_only_at_the_fixed_point','check_entropy_difference_as_a_function_of_window_length','check_energy_variance_against_the_continuum','check_residue_if_the_continuum_value_were_counted']
import io,contextlib
def quiet(fn):
    with contextlib.redirect_stdout(io.StringIO()): return fn()
# P1: sea energy pi/(13 r) instead of pi/(12 r)
m=load(); o=m.pi_times
m.pi_times=lambda c: o(F(c)*F(12,13)) if F(c) in (F(1,24),F(1,12),F(1,48),F(1,6)) and False else o(c)
m.f_direct=lambda r: m.iadd(o(F(1)/(13*F(r))), m.iscale(2,m.array(r)[0]))
print('P1 sea pi/(13r) in f:',quiet(lambda:run(m,names[:1])))
# P2: offset changed: modes 2k+1 -> use quarter offset (2k+1/2): patch array
m=load()
def arr(r):
    r=F(r); tot=[[F(0),F(0)] for _ in range(3)]; k=0
    while True:
        mm=F(m.BASE)*(4*k+1)/(2*r) ; 
        if mm.denominator!=1: raise SystemExit('nonint')
        mi=mm.numerator
        if mi>30*m.BASE: break
        for t,q in zip(tot,m.mode(mi)): t[0]+=q[0]; t[1]+=q[1]
        k+=1
    return tuple((t[0],t[1]+F(1,10**33)) for t in tot)
m.array=arr
print('P2 twist 1/4 half-sum in place of 1/2:',quiet(lambda:run(m,names[:4])))
# P3: mode energy en perturbed by factor (1+1e-20)
m=load(); om=m.mode
m.mode=lambda mi:(om(mi)[0], tuple(x*(1+F(1,10**20)) for x in om(mi)[1]), om(mi)[2])
print('P3 en*(1+1e-20):',quiet(lambda:run(m,names)))
# P4: continuum entropy pi r/5 in delta check -> change pi bounds? instead perturb ln2 by 1e-25
m=load(); ol=m.ln2_bounds
m.ln2_bounds=lambda: tuple(x+F(1,10**25) for x in ol())
print('P4 ln2+1e-25:',quiet(lambda:run(m,names)))
