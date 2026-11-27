# dust at rest falling in its own first-order field: flat div T2 != 0, flat div (T2 + G2/kappa) = 0
from engine import *
from sol import X0
from t2 import om1_of

KAPPA = F(3)                              # stands for 8 pi G
X = labels(X0, 3); X5 = labels(X0, 5)
t, x, y, z = X5
phi = x * x * F(1, 2) + y * y * z * F(1, 3) - x * z * z * z * F(1, 4) + x * y * F(1, 5) + z * z * F(2, 3) + x * x * y * y * F(1, 6)
lap = phi.d(1).d(1) + phi.d(2).d(2) + phi.d(3).d(3)
rho0 = lap * (1 / KAPPA)                  # Delta phi = kappa rho0
# h(a) = phi (2 (a.e0) e0 - a): h[k][a] = phi (2 d_k0 d_a0 - d_ka)
h = [[phi * ((2 if (k == 0 and a == 0) else 0) - (1 if k == a else 0)) for a in range(D)] for k in range(D)]
H1 = mscal(F(-1, 2), h)
H1 = [[H1[k][a].trunc(3) for a in range(D)] for k in range(D)]
G1, G2, fld = einstein_orders(H1)
T1 = [[rho0 * (1 if (k == 0 and a == 0) else 0) for a in range(D)] for k in range(D)]
print("G1 = -kappa T1:", all(G1[k][a] == (T1[k][a] * (-KAPPA)).trunc(1) for k in range(D) for a in range(D)), "rho0", rho0.v)
# geodesic at first order: d_t v1 = -Omega1(e0).e0 ; Omega1 static
om1 = om1_of(fld)
acc = gtg.m_neg(gtg.bdot(om1[0], GA.gen(0), S))             # jets (order 2), static
print("acceleration:", {b: str(c.v) for b, c in acc.items()}, " -1/2 d_k phi:", [str(-phi.d(k).v * F(1, 2)) for k in (1, 2, 3)])
# use the closed form to keep full jet order: v1^k = -1/2 t d_k phi + w^k (static w)
w = [jz(), y * F(1, 3) + x * z * F(1, 4), z * z * F(1, 5) - x * F(1, 2), x * y * F(1, 6) + y * F(1, 7)]
v1 = [jz()] + [t * phi.d(k) * F(-1, 2) + w[k] for k in (1, 2, 3)]
print("closed form matches engine acceleration:", all((v1[k].d(0)).trunc(2) == acc.get((k,), jz()) for k in (1, 2, 3)))
# continuity at second order: d_t rho1 = -div(rho0 v1) ; rho1 = -int dt
flux_div = sum(((rho0 * v1[k]).d(k) for k in (1, 2, 3)), jz())
# integrate in t exactly: flux_div = A t + B with A, B static
A = flux_div.d(0)
B = flux_div - t * A
rho1 = -(t * t * A * F(1, 2) + t * B) + x * y * F(1, 3) + z * F(1, 4)
print("continuity:", (rho1.d(0) + flux_div) == 0)
T2 = [[jz() for _ in range(D)] for _ in range(D)]
for k in range(D):
    for c in range(D):
        v = jz()
        if k == 0 and c == 0:
            v = v + rho1
        if k == 0:
            v = v + rho0 * v1[c] * ETA[c]
        if c == 0:
            v = v + rho0 * v1[k]
        T2[k][c] = v
dT = [d.v for d in flat_div(T2)]
dG = [d.v for d in flat_div(G2)]
print("flat div T2:", [str(q) for q in dT])
print("flat div G2/kappa:", [str(q / KAPPA) for q in dG])
print("sum zero:", all(a + b / KAPPA == 0 for a, b in zip(dT, dG)))
