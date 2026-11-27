import sys, time
sys.path.insert(0, 'colony/runs/2026-11-27-null-surface-three/work/shear')
import pw
from pw import *

def wave_field(w, x0, order):
    """analytic Omega(a) = (a.n) grad H ^ n; returns field, X, du"""
    u0 = x0[0] - x0[3]
    X = [Jet.var(i, x0[i], D, order + 1) for i in range(D)]
    t, x, y, z = X
    du = t - z - u0
    wj = [[series_jet(w[i][j], du) for j in range(2)] for i in range(2)]
    H = F(1, 2) * (wj[0][0] * x * x + 2 * wj[0][1] * x * y + wj[1][1] * y * y)
    TH = [[(1 if mu == a else 0) - H * NLOW[mu] * NUP[a] for mu in range(D)] for a in range(D)]
    gradH = {(mu,): H.d(mu) * ETA[mu] for mu in range(D) if H.d(mu)}
    Nv = {(0,): F(1), (3,): F(1)}
    Bv = gtg.wedge(gradH, Nv, S)
    om = [gtg.m_scal(NLOW[c], Bv) if NLOW[c] else {} for c in range(D)]
    return gtg.Field(TH, om, S), X, du

def torsion_jets_zero(fld):
    ok = True
    for mu in range(D):
        for nu in range(mu + 1, D):
            tj = gtg.m_add(gtg.m_d(fld.g[nu], mu), gtg.m_neg(gtg.m_d(fld.g[mu], nu)),
                           gtg.comm(fld.Om[mu], fld.g[nu], S), gtg.m_neg(gtg.comm(fld.Om[nu], fld.g[mu], S)))
            ok = ok and not tj
    return ok

x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
w = [[[F(3), F(2), F(1)], [F(5, 2), F(-1)]], [[F(5, 2), F(-1)], [F(-3), F(-2), F(-1)]]]
for order in (2, 8, 9):
    t0 = time.time()
    fld, X, du = wave_field(w, x0, order)
    t1 = time.time()
    print(order, "field", t1 - t0, "torsion jets zero", torsion_jets_zero(fld), time.time() - t1,
          "orders", fld.Om[0][(0, 1)].order, fld.TH[0][0].order)
    if order == 2:
        ref = pw.Wave(w, [[0, 0], [0, 0]], x0, order).fld
        same = all(not gtg.m_sub(fld.Om[m], ref.Om[m]) for m in range(D))
        print("analytic Omega equals solved Omega as jets:", same, ref.Om[0][(0, 1)].order)
