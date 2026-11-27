import random
from poly import *
random.seed(7)

def rpoly(deg, nterms=5):
    f = ZJ
    for _ in range(nterms):
        m = ONE
        for i in range(D):
            m = m * X[i] ** random.randint(0, deg)
        f = f + m * F(random.randint(-4, 4), random.randint(1, 3))
    return f

def rsym(deg):
    H = zeros()
    for m in range(D):
        for k in range(m, D):
            H[m][k] = H[k][m] = rpoly(deg)
    return H

def vzero(v):
    return all(not bool(c) for c in v)

H = rsym(2)
xi = [rpoly(2) for _ in range(D)]
lhs = pomega(H, displacement(xi))
rhs = vadd(vscal(2, papply(peinstein(H), xi)), bdiv(superpotential(H, xi)))
print("identity generic xi:", vzero(vadd(lhs, rhs, -1)), "nonzero lhs:", not vzero(lhs))
# divergence identity of R1 for polynomials
H2 = rsym(2)
print("div omega:", (vdiv(pomega(H, H2)) - (ppair(peinstein(H), H2) - ppair(H, peinstein(H2)))) == 0)
# boost
t, x, y, z = X
xiB = [z, ZJ, ZJ, t]
print("D_boost zero:", all(not bool(c) for r in displacement(xiB) for c in r))
K = superpotential(H, xiB)
print("conservation:", vzero(vadd(bdiv(K), vscal(2, papply(peinstein(H), xiB)))))
# corner: t = z = 0
def at_corner(f):
    out = {}
    for e, c in f.c.items():
        if e[0] == 0 and e[3] == 0:
            out[e] = c
    return J(c=out, nv=D, order=None)
trperp = H[1][1] * (-1) + H[2][2] * (-1)      # e^1.h(e_1) + e^2.h(e_2) = eta_1 H11 + eta_2 H22
print("B.K at corner = -tr_perp h:", at_corner(K[(0, 3)] + trperp) == 0, bool(at_corner(trperp)))
