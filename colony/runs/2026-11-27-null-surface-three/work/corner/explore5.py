import sys, os, importlib.util
LAB = "/home/claude/zero-divisors"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("r1", os.path.join(LAB, "store/claims/synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators/check.py"))
r1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r1)
globals().update({k: v for k, v in vars(r1).items() if not k.startswith("__")})
import gtg
fld = gauge_field_not_weak()
print(fld.torsion_free())
K = N
Bj = [gtg.comm(fld.om[c], K, S) for c in range(D)]
Bv = [gtg.m_val(b) for b in Bj]
theta = gtg.Jet.const(0, D)
for c in range(D):
    theta = theta + Bj[c].get((c,), gtg.Jet.const(0, D))
print("theta", theta.v, "order", theta.order)
# area density squared a^2 = det(-G), G_ij = g_i . g_j, i, j in {1, 2}
TH = fld.TH
def G(i, j):
    return sum((ETA[c] * TH[c][i] * TH[c][j] for c in range(D)), gtg.Jet.const(0, D))
a2 = G(1, 1) * G(2, 2) - G(1, 2) * G(1, 2)
print("a2 order", a2.order, a2.v)
dn = lambda f: f.d(0) + f.d(3)
print("theta = 1/2 d_n(a^2)/a^2:", theta.v == F(1, 2) * dn(a2).v / a2.v)
# bivector form: |hb^{-1}(e1) ^ hb^{-1}(e2)|^2 = -(g1^g2)^2
g1v, g2v = gtg.m_val(fld.g[1]), gtg.m_val(fld.g[2])
w = wedge(g1v, g2v)
print("-(g1^g2)^2 = a^2:", -mul(w, w, S).get((), F(0)) == a2.v, mul(w,w,S))
# g_i . n = 0
print([dot(g1v, N), dot(g2v, N)])
# exact: (a^2)''/(2 a^2) - 2 theta^2 = theta' = -1/2 theta^2 - sig2 + n.R(n)
dd = dn(dn(a2)).v
th = theta.v
thp = dd / (2 * a2.v) - 2 * th * th
Rop = gtg.as_op(fld.curvature())
kRk = dot(K, gtg.ricci(Rop, K, S))
Sc = [[dot(REC[a], Bv[b]) for b in (1, 2)] for a in (1, 2)]
print("Sc", Sc)
trS2 = Sc[0][0] ** 2 + 2 * Sc[0][1] * Sc[1][0] + Sc[1][1] ** 2
sig2 = trS2 - F(1, 2) * th * th
print("theta' from area:", thp, " from focusing:", -F(1, 2) * th * th - sig2 + kRk, thp == -F(1, 2) * th * th - sig2 + kRk)
print("theta jet derivative:", dn(theta).v)
