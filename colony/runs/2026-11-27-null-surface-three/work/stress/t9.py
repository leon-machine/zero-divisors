# Kerr-Schild plane wave: hb(a) = a + 1/2 W (a.l) l, l = 1/2 nbar, W = -y.w_lam(y), lam = l.x
from engine import *
from sol import *
from t3 import advect
from t4 import EPSP, EPSX, pairm, dn, nn, NV, NB, M1, M2
L = (F(1, 2), 0, 0, F(-1, 2))
def build(order, tracefree=True):
    X = labels(X0, order + 2)
    t, x, y, z = X
    lam = (t + z) * F(1, 2)                 # l.x = 1/2 (t - (-z))... l.x = l^0 t - l^3 z = 1/2 t + 1/2 z
    fp = lam * lam * F(2, 3) + lam * lam * lam * F(1, 5) - lam * F(1, 2) + lam * lam * lam * lam * F(1, 7)
    fx = lam * lam * F(-1, 4) + lam * lam * lam * F(2, 7) + lam * F(1, 3)
    Fm = madd(mscal(fp, EPSP), mscal(fx, EPSX))            # h_TT = F_lam
    if not tracefree:
        Fm = madd(Fm, mscal(lam * lam * F(1, 3), const_mat(outer_map(M1, M1))))
    d1 = lambda f: (f.d(0) + f.d(3))                        # d/dlam = n.grad (n.l = 1)
    F1 = [[d1(Fm[k][a]) for a in range(D)] for k in range(D)]
    F2 = [[d1(F1[k][a]) for a in range(D)] for k in range(D)]
    yv = [jz(), x, y, jz()]
    def quad(M):                                            # y . M(y)
        return sum((yv[k] * M[k][a] * yv[a] * ETA[k] for k in range(D) for a in range(D)), jz())
    def app(M):                                             # M(y)
        return [sum((M[k][a] * yv[a] for a in range(D)), jz()) for k in range(D)]
    W = quad(F2) * F(-1, 2)                                 # W = -y.w(y), w = 1/2 F''
    ll = const_mat(outer_map(L, L))
    HKS = [[ll[k][a] * W * F(1, 2) for a in range(D)] for k in range(D)]
    Fy, q1 = app(Fm), quad(F1)
    xi = [Fy[k] * F(-1, 2) + q1 * F(L[k], 4) for k in range(D)]
    return Fm, HKS, xi
Fm, HKS, xi = build(2)
tr = lambda M, o: [[M[k][a].trunc(o) for a in range(D)] for k in range(D)]
HKS2 = tr(HKS, 2)
G1, G2, fld = einstein_orders(HKS2)
print("KS: torsion", fld.torsion_free(), "H1H1=0", all(not v for r in mmul(HKS2, HKS2) for v in r), "H1 nonzero", sum(1 for r in HKS2 for v in r if v.v), "G1=0", all(not v for r in G1 for v in r), "G2=0", all(not v for r in G2 for v in r))
HTT = tr(mscal(F(-1, 2), Fm), 2)
G1t, G2t, _ = einstein_orders(HTT)
print("TT: G1=0", all(not v for r in G1t for v in r), "G2 nonzero", sum(1 for r in G2t for v in r if v.v), "n.G2(n)", nn(G2t).v)
xb = grad_map(xi)
sym = madd(xb, transpose(xb))
print("KS = TT - 1/2 (xi_ + xi_^T):", all(HKS[k][a].trunc(2) == (HTT[k][a] - sym[k][a] * F(1, 2)).trunc(2) for k in range(D) for a in range(D)))
be = mscal(F(1, 2), madd(xb, transpose(xb), -1))            # antisymmetric part of xi_
HTT3 = mscal(F(-1, 2), Fm)
Xxi = madd(madd(mmul(xb, HTT3), advect(xi, HTT3), -1), mmul(xb, xb), -1)
Hp = madd(HTT3, xb, -1)
XB = mscal(-1, madd(mmul(Hp, be), mscal(F(1, 2), mmul(be, be))))
tot = G1_of(madd(Xxi, XB))
print("G2_KS - G2_TT = G1[X]:", all(tot[k][a].v == -G2t[k][a].v for k in range(D) for a in range(D)))
print("xi second transverse derivative nonzero:", any(xi[k].d(1).d(1).v or xi[k].d(2).d(2).v or xi[k].d(1).d(2).v for k in range(D)))
# not trace-free: G1 = (tr w)(a.l) l, G2 = 0 still
Fm, HKS, xi = build(2, tracefree=False)
G1, G2, fld = einstein_orders(tr(HKS, 2))
print("non-TF: G1 nonzero", sum(1 for r in G1 for v in r if v.v), "G2=0", all(not v for r in G2 for v in r))
# other parametrisations: H1H1 = 0 so same
