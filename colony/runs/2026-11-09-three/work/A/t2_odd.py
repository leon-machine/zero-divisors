import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet
from lin import lin_ricci

def run(r0, w, s0, c0, l, hc):
    M = gtg.mass_for_root(r0, w)      # f(r0) = w^2
    f = gtg.f_static(M)
    order = 2
    fld = gtg.static_field(r0, s0, c0, f, order=order)   # TH jets of order 3
    K = order + 1
    t = Jet.var(0, F(0), 4, K); r = Jet.var(1, r0, 4, K)
    sn, cs = gtg.sincos(2, s0, c0, 4, K)
    fj = f(r); sf = fj.pw(F(1, 2))
    R = r - r0
    def gen(c):
        return (c[0] + c[1]*t + c[2]*R + c[3]*t*t + c[4]*t*R + c[5]*R*R + c[6]*t*t*R + c[7]*t*R*R + c[8]*R*R*R + c[9]*t*t*t)
    h0, h1 = gen(hc[0]), gen(hc[1])
    if l == 2: dP = 3 * cs
    elif l == 3: dP = (15 * cs * cs - 3) / 2
    S = -sn * sn * dP
    Z = Jet.const(0, 4)
    TH1 = [[Z]*4 for _ in range(4)]
    TH1[0] = [Z, Z, Z, h0 * S / sf]
    TH1[1] = [Z, Z, Z, -h1 * S * sf]
    ric, _ = lin_ricci(fld, TH1)
    return M, fld, ric, (h0, h1, fj, r, S, sn, cs)

if __name__ == '__main__':
    t0 = time.time()
    hc = ((1,2,3,-1,5,7,2,-3,1,4), (2,-1,1,3,-2,5,1,1,-2,3))
    M, fld, ric, (h0, h1, fj, r, S, sn, cs) = run(F(3), F(1,2), F(3,5), F(4,5), 2, hc)
    print('M', M, 'time', time.time()-t0)
    for b in range(4): print(b, ric[b])
    f0 = fj.v; r0 = r.v; ll = 6
    Sv = S.v; sv = sn.v
    # candidate closed forms
    Ex = (h0.d(0)/fj - (fj*h1).d(1)).v
    Er = (h1.d(0).d(0) - h0.d(0).d(1) + 2*h0.d(0)/r + (ll-2)*fj*h1/(r*r)).v
    Et = (fj*(h0.d(1).d(1) - h1.d(0).d(1) - 2*h1.d(0)/r) - (ll/(r*r) - 4*M/(r*r*r))*h0).v
    print('Ex', Ex, 'Er', Er, 'Et', Et)
    print('ratios', ric[3].get((0,),0)/Et if Et else None, ric[3].get((1,),0)/Er, ric[3].get((2,),0)/Ex)
