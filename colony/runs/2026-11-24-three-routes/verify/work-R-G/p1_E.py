# Is there a quadratic displacement equal to 2 x_l delta + constant?  (lemma: compact curvature => no dipole of D f')
import sys; sys.path.insert(0,'/home/claude/leon-machine/zero-divisors/colony/runs/2026-11-24-three-routes/verify/work-R-G')
from p1_lat import *
L=15
x=np.indices((L,L,L)).astype(np.int64)-7
inner=(slice(2,-2),)*3        # avoid wrap-around of roll
for l in range(3):
    r2=(x**2).sum(0)
    xi=[2*x[l]*x[i]-(r2 if i==l else 0) for i in range(3)]       # 2*(x_l x_i - 1/2 delta_il |x|^2)
    d=disp(xi)
    dev=[ (d[c]-(4*x[l] if c<3 else 0))[inner] for c in range(6)]
    print('l',l,'deviation from 4 x_l delta (=2*2x_l delta), per component: unique values',[np.unique(v).tolist() for v in dev])
