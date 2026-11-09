import sys
sys.path.insert(0,'/home/claude/phys-graph/lib'); sys.path.insert(0,'synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets')
import tp_premise; tp_premise.configure('/home/claude/phys-graph/store')
from check import *
f = pot(1, 1, -1, F(3, 2))
v_off = [F(1), F(0), F(0), F(0), F(0), F(1, 2), F(0), F(0)]
g=grad(f,v_off); print('grad',[str(x) for x in g]); print('V',f(from_vec(v_off)))
for a in range(4):
    print(a,[str(sum(x*y for x,y in zip(g,vec(act(a,from_vec(unit(i))))))) for i in range(8)])
