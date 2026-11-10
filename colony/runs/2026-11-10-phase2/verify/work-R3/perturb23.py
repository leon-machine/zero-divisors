import sys,importlib.util,io,contextlib
LAB='/home/claude/phys-graph'; sys.path.insert(0,LAB+'/lib'); sys.dont_write_bytecode=True
import tp_premise,GA
tp_premise.configure(LAB+'/store')
from fractions import Fraction as F
def load(p):
    s=importlib.util.spec_from_file_location('c',LAB+'/proposals/'+p+'/check.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def run(m,nm):
    nf=len(GA.FAILURES)
    with contextlib.redirect_stdout(io.StringIO()):
        try: r=getattr(m,nm)(); return not(r is False or len(GA.FAILURES)>nf)
        except Exception as e: return 'EXC '+repr(e)[:80]
P2='synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages'
P3='synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter'
# 2a: wrong twists for the product decomposition: use 1/5 instead of 1/4
m=load(P2); ot=m.twisted
m.twisted=lambda d,r: ot(F(1,5),r) if (F(d),F(r))==(F(1,4),F(1)) else ot(d,r)
print('2a twist 1/5 in place of 1/4 (product):',run(m,'check_long_window_is_a_product_of_twisted_arrays'), ' circle:',run(m,'check_entropy_across_the_twist_circle'))
# 2b: continuum value pi/6 -> 0.52 (pi_times perturbed) in averages
m=load(P2); op=m.pi_times
m.pi_times=lambda c: tuple(x*(1+F(1,10**6)) for x in op(c))
print('2b pi*(1+1e-6) in averages:',run(m,'check_twist_averages_reach_the_continuum_values'))
# 2c: bern2 with 1/5 instead of 1/6
m=load(P2); m.bern2=lambda a:a*a-a+F(1,5)
print('2c B2 const 1/5:',run(m,'check_twist_averages_reach_the_continuum_values'))
# 2d: ladder union with twists (2j+1)/(2M) replaced: handled inside; perturb RANGE? skip
# 3a: third point r^2 = 0.66 instead of 2/3
m=load(P3); m.POINTS=((F(1),F(1,2)),(F(1,4),F(1,4)),(F(66,100),F(1,3)))
print('3a r^2=0.66:',run(m,'check_thermal_test_holds_at_three_points'),run(m,'check_ground_test_is_a_conic'))
# 3b: twist 3/10 at r=1/2
m=load(P3); m.POINTS=((F(1),F(1,2)),(F(1,4),F(3,10)),(F(2,3),F(1,3)))
print('3b twist 0.3 at r=1/2:',run(m,'check_thermal_test_holds_at_three_points'),run(m,'check_entropies_at_the_three_points'))
# 3c: B2 const
m=load(P3); m._B2=lambda a:a*a-a+F(1,6)+F(1,10**9)
print('3c B2+1e-9:',run(m,'check_ground_test_is_a_conic'),run(m,'check_thermal_test_holds_at_three_points'))
# 3d: entropy with r^2=2/3 but delta 1/4
m=load(P3); oe=m._entropy
m._entropy=lambda r2,d,K=14: oe(r2,F(1,4),K) if F(r2)==F(2,3) else oe(r2,d,K)
print('3d entropy at wrong twist:',run(m,'check_entropies_at_the_three_points'))
