from engine import *
from sol import *
from t1 import generic_H

def eqm(A, B):
    return all(A[k][c] == B[k][c] for k in range(D) for c in range(D))

def advect(xi, M):
    """(xi.grad) M"""
    return [[sum((xi[m] * M[k][c].d(m) for m in range(D)), jz()) for c in range(D)] for k in range(D)]

def trunc(M, o):
    return [[M[k][c].trunc(o) for c in range(D)] for k in range(D)]

X = labels(X0, 3); X4 = labels(X0, 4)
for name, H1 in (("generic", generic_H(X, 5)), ("solution", solution(X0, COEFFS[0], 0, 0))):
    G1, G2, _ = einstein_orders(H1)
    # displacement
    xi = xi_field(X4, 2)
    xb = grad_map(xi)
    H1p = madd(H1, xb, -1)
    G1p, G2p, _ = einstein_orders(H1p)
    Xq = madd(madd(advect(xi, H1), mmul(xb, H1), -1), mmul(xb, xb))      # (xi.grad)H1 - xi_ H1 + xi_ xi_
    pred = madd(madd(G2, advect(xi, G1)), G1_of(Xq), -1)
    print(name, "displacement: G1 unchanged", eqm(trunc(G1p,0), trunc(G1,0)), "G2 law", eqm(trunc(G2p, 0), trunc(pred, 0)),
          "change nonzero", sum(1 for k in range(D) for c in range(D) if (G2p[k][c] - G2[k][c]).v != 0))
    # rotation
    B = biv_field(X, 1)
    be = biv_map(B)
    H1r = madd(H1, be)
    G1r, G2r, _ = einstein_orders(H1r)
    Xr = madd(mmul(H1, be), mscal(F(1, 2), mmul(be, be)))
    comm_ = madd(mmul(G1, be), mmul(be, G1), -1)
    pred = madd(madd(G2, G1_of(Xr), -1), comm_)
    print(name, "rotation: G1 unchanged", eqm(trunc(G1r,0), trunc(G1,0)), "G2 law", eqm(trunc(G2r, 0), trunc(pred, 0)),
          "change nonzero", sum(1 for k in range(D) for c in range(D) if (G2r[k][c] - G2[k][c]).v != 0))
