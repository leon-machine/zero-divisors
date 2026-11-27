from dev import *
from fractions import Fraction as F
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
import gtg
t0 = time.time()
# first order: hb^{-1} = id + eps s, s a generic symmetric map (no gauge): a^2 = -(g1^g2)^2 = det of minus Gram
sm = sym(SYM[0])
eps = gtg.Jet.var(0, 0, 1, None)
one = gtg.Jet.const(1, 1)
def gvec(i):
    # g_i = e_i + eps s(e_i), components on e_k as jets in eps
    img = apply(sm, E[i])
    return [one * (1 if k == i else 0) + eps * F(ETA[k]) * dot(img, E[k]) for k in range(D)]
def gdot(u, v):
    out = gtg.Jet.const(0, 1)
    for k in range(D):
        out = out + u[k] * v[k] * ETA[k]
    return out
g1_, g2_ = gvec(1), gvec(2)
a2 = gdot(g1_, g1_) * gdot(g2_, g2_) - gdot(g1_, g2_) * gdot(g1_, g2_)
trperp_s = dot(REC[1], apply(sm, E[1])) + dot(REC[2], apply(sm, E[2]))
print("a^2 =", a2.c, " 2 tr_perp s =", 2 * trperp_s)
# so a = 1 + eps tr_perp s + O(eps^2) = 1 + 1/2 tr_perp h, h = 2 eps s
# derived metric to first order: g(a,b) = a.b + 2 eps s(a).b
print("h = 2 s:", [ (gdot(gvec(i), gvec(j)).c.get((1,), 0)) == 2 * dot(apply(sm, E[i]), E[j]) for i in range(D) for j in range(D)].count(True))
# not weak
fld = not_weak_field()
Kv = N
Bj = [gtg.comm(fld.om[c], Kv, S) for c in range(D)]
Bv = [gtg.m_val(b) for b in Bj]
theta = gtg.Jet.const(0, D)
for c in range(D):
    theta = theta + Bj[c].get((c,), gtg.Jet.const(0, D))
TH = fld.TH
def G(i, j):
    return sum((ETA[c] * TH[c][i] * TH[c][j] for c in range(D)), gtg.Jet.const(0, D))
A2 = G(1, 1) * G(2, 2) - G(1, 2) * G(1, 2)
gv = [gtg.m_val(x) for x in fld.g]
w = wedge(gv[1], gv[2])
print("a^2 = -(g1^g2)^2:", -mul(w, w, S).get((), F(0)) == A2.v, " g_i.n = 0:", dot(gv[1], N) == 0 and dot(gv[2], N) == 0, "a^2 =", A2.v)
d1 = A2.d(0).v + A2.d(3).v
d2 = A2.d(0).d(0).v + 2 * A2.d(0).d(3).v + A2.d(3).d(3).v
th = theta.v
print("theta = 1/2 (a^2)'/a^2:", 2 * th * A2.v == d1, th)
Rop = gtg.as_op(fld.curvature())
nRn = dot(Kv, gtg.ricci(Rop, Kv, S))
Sc = [[dot(REC[a], Bv[b]) for b in (1, 2)] for a in (1, 2)]
sig2 = Sc[0][0] ** 2 + 2 * Sc[0][1] * Sc[1][0] + Sc[1][1] ** 2 - F(1, 2) * th * th
# a'' = a (1/2 theta^2 - <sigma,sigma> + n.R(n))  <=>  (a^2)'' = 2 a^2 (1/2 th^2 - sig2 + nRn) + 2 a'^2, a' = th a
print("area form of focusing:", d2 == 2 * A2.v * (F(1, 2) * th * th - sig2 + nRn) + 2 * th * th * A2.v, " sig2 =", sig2, " nRn =", nRn)
print(time.time() - t0)
# G: rotors
I4 = mul(mul(E[0], E[1], S), mul(E[2], E[3], S), S)
B = mul(E[0], E[3], S)
Bs = mul(I4, B, S)
print("B^2:", mul(B, B, S), " I4 B:", Bs, " (I4B)^2:", mul(Bs, Bs, S))
# boost rotor 2 - B (unnormalised): R R~ = 3 ; n -> 3 n, nbar -> nbar/3
R = sub(GA.sc(2), B); Rt = GA.reverse(R)
print("R R~:", mul(R, Rt, S))
bo = lambda v: g1(scal(F(1, 3), mul(mul(R, v, S), Rt, S)))
print(bo(N), bo(NBAR), bo(M1), bo(M2))
# x.B generator: d/dchi (R x R~) = x.B  : check x.B on basis: e0 -> e3, e3 -> e0
xB = lambda v: GA.neg(vdotB(v, B))  # v.B = -(B.v)... vdotB(a,B) = a.B
print("e0.B, e3.B, n.B, nbar.B:", vdotB(E[0], B), vdotB(E[3], B), vdotB(N, B), vdotB(NBAR, B))
# rotation rotor of the corner plane, unnormalised 2 - B*: angle phi with cos = 3/5
Rr = sub(GA.sc(2), Bs); Rrt = GA.reverse(Rr)
print("Rr Rr~:", mul(Rr, Rrt, S))
ro = lambda v: g1(scal(F(1, 5), mul(mul(Rr, v, S), Rrt, S)))
print(ro(N), ro(NBAR), ro(M1), ro(M2))
# half turn: R(pi) = -B*: conjugation by B*
half = lambda v: g1(mul(mul(Bs, v, S), GA.reverse(Bs), S))
print(half(N), half(M1), half(M2))
