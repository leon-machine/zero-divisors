# (vi) off solutions: generic symmetric H1 with H1(n) = 0, not a solution
from engine import *
from sol import *
from t4 import EPSP, EPSX, pairm, dn, nn, NV, NB, M1, M2
X = labels(X0, 2)
t, x, y, z = X
basis = [const_mat(outer_map(u, v)) for u, v in ((NV, NV), (NV, M1), (M1, NV), (NV, M2), (M2, NV), (M1, M1), (M1, M2), (M2, M1), (M2, M2))]
# symmetric combos killing n: n(x)n, n(x)m1 + m1(x)n, n(x)m2 + m2(x)n, m1m1, m1m2+m2m1, m2m2
syms = [basis[0], madd(basis[1], basis[2]), madd(basis[3], basis[4]), basis[5], madd(basis[6], basis[7]), basis[8]]
polys = [t*x*F(1,3) + z*z*F(1,5) + y, x*y*F(1,4) - t*t*F(1,6) + z, z*t*F(2,5) + x*x*F(1,7), y*y*F(1,6) + t*z*F(1,5) + t, t*t*F(1,2) + x*z*F(1,3) - y*z, z*z*F(1,4) + t*y*F(1,3) + x]
h = [[jz() for _ in range(D)] for _ in range(D)]
for P, Sm in zip(polys, syms):
    h = madd(h, [[Sm[m][k] * P for k in range(D)] for m in range(D)])
print("h(n)=0:", all(not sum((h[k][a] * NV[a] for a in range(D)), jz()) for k in range(D)), "symmetric:", all(ETA[k]*h[k][c] == ETA[c]*h[c][k] for k in range(D) for c in range(D)))
print("solution?", all(not v for row in first_order_einstein(h) for v in row))
hp, hx, tau = pairm(h, EPSP) * F(1, 2), pairm(h, EPSX) * F(1, 2), mtrace(h)
sig2 = ((dn(hp) * dn(hp) + dn(hx) * dn(hx)) * F(1, 2)).v
theta = (dn(tau) * F(1, 2)).v
d2 = dn(dn(pairm(h, h))).v
H1 = mscal(F(-1, 2), h)
for r, coef in ((F(0), F(1, 8)), (F(1), F(-1, 8)), (F(1, 2), F(0))):
    G1, G2, _ = einstein_orders(H1, mscal(r, mmul(H1, H1)))
    print(r, nn(G2).v == sig2 + theta * theta * F(1, 2) + coef * d2, "dn theta = n.G1(n):", nn(G1).v, sig2, theta)
