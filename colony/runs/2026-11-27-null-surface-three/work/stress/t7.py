# dust, then a displacement and a rotation gauge change: T2' = T2 + (xi.grad)T1 + [T1, beta], H1' = H1 - xi_ + beta
import time
from engine import *
from sol import X0, xi_field, biv_field, grad_map, biv_map
from t3 import advect

KAPPA = F(3)
def dust(order=3):
    X5 = labels(X0, order + 2)
    t, x, y, z = X5
    phi = x * x * F(1, 2) + y * y * z * F(1, 3) - x * z * z * z * F(1, 4) + x * y * F(1, 5) + z * z * F(2, 3)
    lap = phi.d(1).d(1) + phi.d(2).d(2) + phi.d(3).d(3)
    rho0 = lap * (1 / KAPPA)
    h = [[phi * ((2 if (k == 0 and a == 0) else 0) - (1 if k == a else 0)) for a in range(D)] for k in range(D)]
    H1 = [[(h[k][a] * F(-1, 2)).trunc(order) for a in range(D)] for k in range(D)]
    w = [jz(), y * F(1, 3) + x * z * F(1, 4), z * z * F(1, 5) - x * F(1, 2), x * y * F(1, 6) + y * F(1, 7)]
    v1 = [jz()] + [t * phi.d(k) * F(-1, 2) + w[k] for k in (1, 2, 3)]
    fd = sum(((rho0 * v1[k]).d(k) for k in (1, 2, 3)), jz())
    A = fd.d(0); B = fd - t * A
    rho1 = -(t * t * A * F(1, 2) + t * B) + x * y * F(1, 3) + z * F(1, 4)
    T1 = [[rho0 * (1 if (k == 0 and a == 0) else 0) for a in range(D)] for k in range(D)]
    T2 = [[jz() for _ in range(D)] for _ in range(D)]
    for k in range(D):
        for c in range(D):
            v = jz()
            if k == 0 and c == 0: v = v + rho1
            if k == 0: v = v + rho0 * v1[c] * ETA[c]
            if c == 0: v = v + rho0 * v1[k]
            T2[k][c] = v
    return H1, T1, T2

t0 = time.time()
H1, T1, T2 = dust()
X = labels(X0, 3); X4 = labels(X0, 4)
xi = xi_field(X4, 1); xb = grad_map(xi); be = biv_map(biv_field(X, 2))
H1p = madd(madd(H1, xb, -1), be)
T2p = madd(madd(T2, advect(xi, T1)), madd(mmul(T1, be), mmul(be, T1), -1))
G1, G2, _ = einstein_orders(H1p)
print("G1' = -kappa T1:", all(G1[k][a] == (T1[k][a] * (-KAPPA)).trunc(1) for k in range(D) for a in range(D)))
dT = [d.v for d in flat_div(T2p)]; dG = [d.v for d in flat_div(G2)]
print([str(q) for q in dT]); print("sum zero:", all(a + b / KAPPA == 0 for a, b in zip(dT, dG)), time.time() - t0)
print("H1' symmetric?", all(ETA[k] * H1p[k][c] == ETA[c] * H1p[c][k] for k in range(D) for c in range(D)))
