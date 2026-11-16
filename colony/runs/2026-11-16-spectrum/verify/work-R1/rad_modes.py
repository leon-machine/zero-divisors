"""R1 independent derivation: radiation-era scalar perturbations, exact Laurent series in y = k tau.

Conventions (my own): ds^2 = a^2[(1+2A)dtau^2 - 2 dB_i dx^i dtau - ((1-2psi)delta + 2 dd E)dx dx],
a ~ tau, calH = 1/tau.  Newtonian gauge Phi = Psi (no anisotropic stress), M&B equations:
  00: k^2 Phi + 3 calH (Phi' + calH Phi) = -(3/2) calH^2 delta_N
  0i: k^2 (Phi' + calH Phi) = 2 calH^2 theta_N   (theta = velocity divergence, (rho+p) = 4/3 rho)
Exact solutions: Phi_g = 3(sin x - x cos x)/x^3, Phi_d = 3^{-3/2} * 3(cos x + x sin x)/x^3 (rescaled), x = y/sqrt3.
Slice change tau -> tau + T:  psi += calH T, delta += 4 calH T, theta_rel -= k^2 T, delta_theta += (1/a)(6/tau^2+k^2)T.
Uniform expansion:  T = 3(calH Phi + Phi')/(6/tau^2 + k^2).   Flat: T = -tau Phi.
zeta := -psi + delta/4 (curvature on uniform-density slices), conserved growing amplitude zeta_g = -(3/2) C_g.
"""
from fractions import Fraction as F
from math import factorial

N = 14  # number of terms


class L:
    """Laurent series sum c[n] y^n, n from lo to lo+N-1."""
    def __init__(self, d):
        self.d = {k: F(v) for k, v in d.items() if v != 0}

    def __add__(s, o):
        o = o if isinstance(o, L) else L({0: o})
        r = dict(s.d)
        for k, v in o.d.items():
            r[k] = r.get(k, 0) + v
        return L(r).trunc()

    __radd__ = __add__

    def __neg__(s):
        return L({k: -v for k, v in s.d.items()})

    def __sub__(s, o):
        return s + (-(o if isinstance(o, L) else L({0: o})))

    def __rsub__(s, o):
        return (-s) + o

    def __mul__(s, o):
        if not isinstance(o, L):
            return L({k: v * F(o) for k, v in s.d.items()})
        r = {}
        for a, u in s.d.items():
            for b, v in o.d.items():
                r[a + b] = r.get(a + b, 0) + u * v
        return L(r).trunc()

    __rmul__ = __mul__

    def lo(s):
        return min(s.d) if s.d else 10**6

    def trunc(s):
        if not s.d:
            return s
        lo = min(s.d)
        return L({k: v for k, v in s.d.items() if k < lo + N})

    def inv(s):
        lo = s.lo(); c0 = s.d[lo]
        # s = c0 y^lo (1 + u)
        u = L({k - lo: v / c0 for k, v in s.d.items() if k != lo})
        r = L({0: 1}); p = L({0: 1})
        for _ in range(N):
            p = p * (-u)
            r = r + p
        return r * L({-lo: 1 / c0})

    def __truediv__(s, o):
        return s * (o.inv() if isinstance(o, L) else F(1) / F(o))

    def dy(s):
        return L({k - 1: k * v for k, v in s.d.items() if k != 0})

    def show(s, m=5):
        ks = sorted(s.d)[:m]
        return " + ".join(f"({s.d[k]})y^{k}" for k in ks)


Y = L({1: 1})
# Phi_g in x^2 = y^2/3
Pg = L({2 * n - 2: F(3 * (-1) ** (n + 1) * 2 * n, factorial(2 * n + 1)) / F(3) ** (n - 1) for n in range(1, N + 2)})
# Phi_d: 3 sum (-1)^m (1-2m) x^{2m-3}/(2m)!, x^{2m-3} = y^{2m-3} 3^{3/2} 3^{-m}; drop 3^{3/2}
Pd = L({2 * m - 3: F(3 * (-1) ** m * (1 - 2 * m), factorial(2 * m)) / F(3) ** m for m in range(0, N + 2)})


def newton(P):
    Py = P.dy()
    delta = F(-2, 3) * (Y * Y * P + 3 * Y * Py + 3 * P)
    u = F(1, 2) * (Y * P + Y * Y * Py)  # theta/k
    return P, Py, delta, u


def check_eom(P):
    # Newtonian radiation eq: Phi'' + 4 calH Phi' + (k^2/3) Phi = 0 -> in y: P_yy + (4/y)P_y + P/3 = 0
    r = P.dy().dy() + 4 * Y.inv() * P.dy() + F(1, 3) * P
    return all(v == 0 for v in r.d.values()) or r.lo() > N - 6


def slices(P):
    P_, Py, dN, u = newton(P)
    out = {}
    # uniform expansion
    TovT = 3 * (P + Y * Py) / (6 + Y * Y)      # T/tau
    kT = 6 * u / (6 + Y * Y)
    out['ue'] = dict(psi=P + TovT, delta=dN + 4 * TovT, th=u - kT)
    # flat
    out['fl'] = dict(psi=P - P, delta=dN - 4 * P, th=u + Y * P)
    # comoving orthogonal (theta_rel = 0): kT = u
    TovT_c = u * Y.inv()  # T/tau = kT/(k tau)
    out['co'] = dict(psi=P + TovT_c, delta=dN + 4 * TovT_c, th=u - u)
    # newtonian
    out['N'] = dict(psi=P, delta=dN, th=u)
    for k, v in out.items():
        v['zeta'] = -v['psi'] + F(1, 4) * v['delta']
    return out


if __name__ == '__main__':
    print('EOM ok:', check_eom(Pg), check_eom(Pd))
    Sg, Sd = slices(Pg), slices(Pd)
    for name in ['ue', 'fl']:
        g, d = Sg[name], Sd[name]
        print(f'--- slice {name}')
        for q in ['psi', 'delta', 'th', 'zeta']:
            print(f'  growing {q}:', g[q].show(3))
            print(f'  decay   {q}:', d[q].show(3))
        # data D = Cg*g + Cd*d for (delta, th); solve for Cg; zeta_g = -(3/2) Cg
        det = g['delta'] * d['th'] - g['th'] * d['delta']
        # Cg = (delta*d_th - th*d_delta)/det
        alpha = d['th'] / det * F(-3, 2)
        beta = -d['delta'] / det * F(-3, 2)
        print('  zeta_g = alpha*delta + beta*(theta/k)')
        print('   alpha =', alpha.show(4))
        print('   beta  =', beta.show(4))
        # contamination: the decaying mode amplitude from pure delta data
        cd_alpha = -g['th'] / det
        print('   Cd per unit delta =', cd_alpha.show(3))
