import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet
from lin import lin_ricci_jet

def legendre(l, cs):
    return (3*cs*cs - 1)/2 if l == 2 else (5*cs*cs*cs - 3*cs)/2

def functionals(r0, w, s0, c0, l, fn, mono):
    """fn in 0..3 (H0,H1,H2,K), mono (i,j): the function t^i R^j, others zero."""
    M = gtg.mass_for_root(r0, w); f = gtg.f_static(M)
    fld = gtg.static_field(r0, s0, c0, f, order=2)
    K_ = 3
    t = Jet.var(0, F(0), 4, K_); r = Jet.var(1, r0, 4, K_)
    sn, cs = gtg.sincos(2, s0, c0, 4, K_)
    fj = f(r); sf = fj.pw(F(1, 2)); R = r - r0
    P = legendre(l, cs)
    Z = Jet.const(0, 4)
    H = [Z, Z, Z, Z]
    H[fn] = (t ** mono[0]) * (R ** mono[1]) if (mono[0] or mono[1]) else Jet(1, None, 4, K_)
    H0, H1, H2, K = H
    TH1 = [[Z]*4 for _ in range(4)]
    TH1[0][0] = -sf * H0 * P / 2
    TH1[1][0] = sf * H1 * P
    TH1[1][1] = H2 * P / (2 * sf)
    TH1[2][2] = r * K * P / 2
    TH1[3][3] = r * sn * K * P / 2
    ric = lin_ricci_jet(fld, TH1)
    rows = []
    for b in range(4):
        for a in range(4):
            c = ric[b].get((a,), Z)
            if not isinstance(c, Jet): c = Jet.const(c, 4)
            rows += [c.v, c.d(0).v if c.order else 0, c.d(1).v if c.order else 0]
    lam = F((l-1)*(l+2), 2)
    Psi = r * (K + (fj * r / (lam * r + 3 * M)) * (H2 - r * K.d(1))) if True else None
    VZ = fj * (2*lam*lam*(lam+1)*r**3 + 6*lam*lam*M*r*r + 18*lam*M*M*r + 18*M**3) / (r**3 * (lam*r + 3*M)**2)
    # Psi has order 2 (K.d(1)); need 2 more derivatives -> K jets must be order 4. handled by caller order.
    return rows, Psi, VZ, fj

if __name__ == '__main__':
    print('placeholder')
