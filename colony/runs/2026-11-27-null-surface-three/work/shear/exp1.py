"""K3: is the Kerr-Schild plane wave an exact vacuum field in the stored conventions? timing of jets."""
import sys, time
sys.path.insert(0, 'lib')
from fractions import Fraction as F
import GA, gtg
from GA import add, gen, mul, scal, sub
D = 4; S = GA.sig(1, 3); ETA = [1, -1, -1, -1]
E = [gen(i) for i in range(D)]
REC = [scal(ETA[i], E[i]) for i in range(D)]
def vec(c): return {(i,): F(x) for i, x in enumerate(c) if x}
N = vec([1, 0, 0, 1]); NBAR = vec([1, 0, 0, -1])
def dot(a, b): return GA.dot(a, b, S)

def wave(prof, x0, order=1, sign=-1):
    """hb^{-1}(a) = a + sign * H (a.n) n, H = 1/2 w_ij(u) y^i y^j, u = n.x = t - z"""
    def hbinv(X):
        t, x, y, z = X
        u = t - z
        w11, w12, w22 = prof(u)
        H = F(1, 2) * (w11 * x * x + 2 * w12 * x * y + w22 * y * y)
        nlow = [1, 0, 0, -1]   # a.n for a = e_mu
        nup = [1, 0, 0, 1]
        # rows g[mu][a]: hb^{-1}(e_mu) components
        return [[(1 if mu == a else 0) + sign * H * nlow[mu] * nup[a] for a in range(D)] for mu in range(D)]
    return gtg.field_from_hbinv(hbinv, x0, S, order=order)

x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
for name, prof in [("tf big", lambda u: (3 + 2 * u + u * u, F(5, 2) - u, -(3 + 2 * u + u * u))),
                   ("not tf", lambda u: (3 + 2 * u, F(5, 2) - u, 1 + u * u))]:
    t0 = time.time()
    fld = wave(prof, x0, order=1)
    Rop = gtg.as_op(fld.curvature())
    print(name, "torsion free", fld.torsion_free(), "ricci flat", gtg.ricci_flat(Rop, S), time.time() - t0)
    for m in range(D):
        print("  Ric(e%d) =" % m, gtg.ricci(Rop, E[m], S))
    print("  R(n^e1)", Rop(gtg.wedge(N, E[1], S)), " R(nbar^e1)", Rop(gtg.wedge(NBAR, E[1], S)))
for order in (2, 4, 6):
    t0 = time.time()
    fld = wave(lambda u: (3 + 2 * u + u * u, F(5, 2) - u, -(3 + 2 * u + u * u)), x0, order=order)
    print("order", order, time.time() - t0, "terms in om:", sum(len(c.c) for o in fld.om for c in o.values()))
