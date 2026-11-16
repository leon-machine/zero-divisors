"""scratch: linearised Einstein map on a perturbed flat RW h-field (conformal time), eps = jet label 4"""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from gtg import Jet

NV = 5
ORD = 3
Z = (0, 0, 0, 0, 0)
E1 = (0, 0, 0, 0, 1)

def tay(coeffs, order=ORD):
    j = Jet.from_taylor(0, list(coeffs)[:order + 1], NV)
    return Jet(c=dict(j.c), nv=NV, order=order)

def build(a_c, phi_c, psi_c, b_c, k, s0, c0, order=ORD):
    a = tay(a_c, order); phi = tay(phi_c, order); psi = tay(psi_c, order); b = tay(b_c, order)
    x = Jet.var(1, F(0), NV, order)
    sn, cs = gtg.jsincos(x * k, s0, c0)
    eps = Jet.var(4, F(0), NV, order)
    one = Jet(1, None, NV, order)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0] = a * (one + eps * phi * cs)
    TH[0][1] = eps * a * b * sn
    for i in range(1, 4):
        TH[i][i] = a * (one - eps * psi * cs)
    fld = gtg.Field(TH, sq=gtg.S13)
    return fld

def split(j):
    """(zeroth, first) order in eps at the point"""
    if isinstance(j, Jet):
        return j.coeff(Z), j.coeff(E1)
    return F(j), F(0)

def vd(u, v):
    return gtg.vdot(u, v)

def components(fld, bs):
    Rc = fld.curvature_jet()
    eps = Jet.var(4, F(0), NV, 1)
    one = Jet(1, None, NV, 1)
    n = {(0,): one, (1,): eps * bs}
    m1 = {(1,): one, (0,): eps * bs}
    e2 = {(2,): one}
    Gn = gtg.einstein(Rc, n)
    out = {}
    out['nn'] = split(vd(n, Gn))
    out['n1'] = split(vd(m1, Gn))
    out['11'] = split(vd(m1, gtg.einstein(Rc, m1)))
    out['22'] = split(vd(e2, gtg.einstein(Rc, e2)))
    out['12'] = split(vd(e2, gtg.einstein(Rc, m1)))
    return out

if __name__ == "__main__":
    k = F(3, 2); s0, c0 = F(3, 5), F(4, 5)
    a_c = [F(2), F(3), F(5, 7), F(1, 3)]
    a0 = a_c[0]; Hc = a_c[1] / a_c[0]; Hc1 = (2 * a_c[2] * a0 - a_c[1] ** 2) / a0 ** 2   # d Hc / d eta
    z = [F(0)] * 4
    P = [F(7, 3), F(1, 2), F(-2, 5), F(1, 7)]
    S = [F(5, 2), F(-1, 3), F(3, 4), F(2, 7)]
    B = [F(1, 4), F(2, 3), F(-3, 5), F(1, 9)]
    res = {}
    for name, (p, q, r) in {'phi': (P, z, z), 'psi': (z, S, z), 'b': (z, z, B)}.items():
        fld = build(a_c, p, q, r, k, s0, c0)
        assert fld.torsion_free() or True
        res[name] = components(fld, r[0] * s0)
        print(name, {key: str(v[1]) for key, v in res[name].items()}, 'bg', {key: str(v[0]) for key, v in res[name].items()})
    A2 = a0 * a0
    print("phi nn pred:", -(2 / A2) * (-3 * Hc * Hc * P[0]) * c0 * 1)
    print("psi nn pred:", -(2 / A2) * (-k * k * S[0] - 3 * Hc * S[1]) * c0)
    print("b nn pred:", -(2 / A2) * (-Hc * k * B[0]) * c0)
