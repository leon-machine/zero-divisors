import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
from t2_odd import run
hcs = [((1,2,3,-1,5,7,2,-3,1,4), (2,-1,1,3,-2,5,1,1,-2,3)), ((0,1,-2,4,1,-3,5,2,2,-1), (3,2,-5,1,4,1,-2,3,1,1))]
for (r0, w, s0, c0) in [(F(3), F(1,2), F(3,5), F(4,5)), (F(5), F(2,3), F(5,13), F(12,13)), (F(2), F(1,3), F(4,5), F(3,5))]:
  for l in (2, 3):
    for hc in hcs:
        M, fld, ric, (h0, h1, fj, r, S, sn, cs) = run(r0, w, s0, c0, l, hc)
        ll = l*(l+1); f0 = fj.v
        Ex = (h0.d(0)/fj - (fj*h1).d(1)).v
        Er = (h1.d(0).d(0) - h0.d(0).d(1) + 2*h0.d(0)/r + (ll-2)*fj*h1/(r*r)).v
        Et = (fj*(h0.d(1).d(1) - h1.d(0).d(1) - 2*h1.d(0)/r) - (ll/(r*r) - 4*M/(r*r*r))*h0).v
        Sv, sv = S.v, sn.v
        # theta factor for x-eq: dS/dth - 2 cot S
        dS = S.d(2).v - 2*cs.v/sv*Sv
        k = -Sv/(r0*sv)
        print(l, f0, 'c0', ric[3].get((0,),0)/Et/k, 'c1', ric[3].get((1,),0)/Er/k, 'c2', ric[3].get((2,),0)/Ex/(dS/(r0*r0*sv)))
