"""scratch: radiation-era dynamics in the zero-shear gauge; exact series; the growing-mode projection"""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, gtg
from pert2 import build, components

k = F(3, 2); s0, c0 = F(3, 5), F(4, 5)
for eta0 in (F(2), F(5, 3)):
    a_c = [eta0, F(1), F(0), F(0)]
    A = [F(7, 3), F(1, 2), F(-2, 5), F(1, 7)]     # A, A', A''/2, A'''/6
    z = [F(0)] * 4
    fld = build(a_c, A, A, z, k, s0, c0)
    out = components(fld, F(0))
    a2 = eta0 ** 2
    Hc = 1 / eta0
    nn = out['nn'][1]; g11 = out['11'][1]; g22 = out['22'][1]; n1 = out['n1'][1]
    App = 2 * A[2]
    print("eta0", eta0, "nn", nn, "pred", (2 / a2) * (k * k * A[0] + 3 * Hc * (A[1] + Hc * A[0])) * c0)
    print("  n1", n1, "pred", (2 / a2) * k * (A[1] + Hc * A[0]) * s0)
    print("  11", g11, "22", g22, "pred", -(2 / a2) * (App + 3 * Hc * A[1] + (2 * (-Hc * Hc) + Hc * Hc) * A[0]) * c0)
    op = App + 4 * A[1] / eta0 + k * k * A[0] / 3
    print("  11 - nn/3 =", g11 - nn / 3, " -(2/a^2) op c =", -(2 / a2) * op * c0)
    # anisotropic stress with phi != psi
    P = [F(1, 3), F(2), F(1, 5), F(0)]
    out2 = components(build(a_c, P, A, z, k, s0, c0), F(0))
    print("  phi != psi: 11 - 22 =", out2['11'][1] - out2['22'][1], " k^2 (phi - psi) c /a^2 =", k * k * (P[0] - A[0]) * c0 / a2)

# exact series in x: g = 3 (sin x - x cos x)/x^3 ; d = (cos x + x sin x)/x^3
N = 12
def fact(n):
    r = 1
    for i in range(2, n + 1): r *= i
    return r
sinc = {n: F((-1) ** ((n - 1) // 2), fact(n)) for n in range(1, 2 * N + 8, 2)}
cosc = {n: F((-1) ** (n // 2), fact(n)) for n in range(0, 2 * N + 8, 2)}
# power series as dict exponent -> coeff (Laurent)
def add(*ps):
    o = {}
    for p in ps:
        for e, c in p.items():
            o[e] = o.get(e, 0) + c
    return {e: c for e, c in o.items() if c}
def sh(p, m, c=1): return {e + m: v * c for e, v in p.items()}
def mul(p, q, top):
    o = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            if e1 + e2 <= top:
                o[e1 + e2] = o.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in o.items() if c}
def der(p): return {e - 1: c * e for e, c in p.items() if e}
TOP = 2 * N
g = add(sh(sinc, -3, 3), sh(sh(cosc, 1), -3, -3)); g = {e: c for e, c in g.items() if e <= TOP}
d = add(sh(cosc, -3), sh(sh(sinc, 1), -3)); d = {e: c for e, c in d.items() if e <= TOP}
print("g:", sorted(g.items())[:5]); print("d:", sorted(d.items())[:5])
def ode(p):  # p'' + 4 p'/x + p
    return add(der(der(p)), sh(der(p), -1, 4), p)
print("ode g residual low orders:", {e: c for e, c in ode(g).items() if e <= TOP - 4})
print("ode d residual low orders:", {e: c for e, c in ode(d).items() if e <= TOP - 4})
def Rof(p): return add(sh(p, 0, F(3, 2)), sh(der(p), 1, F(1, 2)))
def zof(p):  # zeta = -(3/2) p - (x/2) p' - (x^2/2) p
    return add(sh(p, 0, F(-3, 2)), sh(der(p), 1, F(-1, 2)), sh(p, 2, F(-1, 2)))
print("R_g:", sorted(Rof(g).items())[:4]); print("R_d:", sorted(Rof(d).items())[:4])
print("zeta_g:", sorted(zof(g).items())[:4]); print("zeta_d:", sorted(zof(d).items())[:4])
cc = {e: c for e, c in cosc.items()}
print("R_d - cos/(2x):", {e: c for e, c in add(Rof(d), sh(cc, -1, F(-1, 2))).items() if e <= TOP - 4})
