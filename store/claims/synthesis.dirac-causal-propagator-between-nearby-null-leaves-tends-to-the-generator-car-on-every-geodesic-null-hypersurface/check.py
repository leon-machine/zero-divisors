"""Generator anticommutation relations from the causal propagator: exact checks.

Setting: x = X(u, y' + eta) on the null hypersurface H, x' = X_w(u', y') on the leaf H_w of a null foliation.
The solution radiated by null data Psi on H_w is Phi_w(x) = int S(x, x') k(x') Psi(x') a' du' d^2y', with
S = D_x E, E = (1/4 pi) sgn(t - t') [U delta(sigma) + V theta(sigma)], U = Delta^(1/2) R. Projected:
  Lambda(x) D[U delta(sigma)] k(x') = N1 delta(sigma) + N2 delta'(sigma),
  N1 = Lambda (D U) k(x'),  N2 = Lambda (grad_x sigma) U k(x').
After the transverse integral (Morse lemma with parameters) the kernel is
  sgn (a'/4 pi) [theta(sigma*) (alpha1 + alpha2') + delta(sigma*) alpha2(0)],  sigma* = w b~(u, u'),
with step coefficient proportional to c~ = N1(0) + tr(M^-1 Q) (Q the eta^2 part of N2 at w = 0) and the
delta coefficient (1/2) d_w N2 / (k.l) at coincidence. Checks:
(1) projector algebra (Lambda p k = 2 (p.k) Lambda, Lambda k = 0, tail and mass terms projected out, the
    projected transverse connection);
(2) generic jets in the adapted gauge: N2 = O(eta^2) and c~ = 2 [d' - d tr(M^-1 M')/2 + theta d/2] Lambda,
    independent of the first-order transport; zero under the half-density law;
(3) first principles on the plane-wave field (curved, non-commuting tidal and deviation maps; and its flat
    member with an expanding, shearing hypersurface): N2 = O(eta^2), c~ = 0;
(4) flat field, null hypersurface with cubic jets: N2 = O(eta^2), c~ = 0;
(5) the layer displacement: d_w sigma = u' - u (so b = (u' - u)(k.l)), d_w N2 = -Lambda l R k(x'), and the
    coincidence coefficient is exactly Lambda; the flat null plane kernel is exact.
Exact arithmetic only (Fractions; truncated polynomials and power series with first-order dual variables).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S4 = (1, -1, -1, -1)
E = [GA.gen(i) for i in range(4)]


def mulv(a, b):
    return GA.mul(a, b, S4)


def wedge(a, b):
    return GA.scal(F(1, 2), GA.sub(mulv(a, b), mulv(b, a)))


def dotv(a, b):
    return GA.dot(a, b, S4)


# ------------------------------------------------------------------ Clifford-valued polynomials
class CP(object):
    def __init__(self, d=None, nv=3):
        self.nv = nv
        self.d = {kk: v for kk, v in (d or {}).items() if v}

    @staticmethod
    def const(mv, nv=3):
        return CP({(0,) * nv: mv}, nv)

    @staticmethod
    def scal(c, nv=3):
        return CP({(0,) * nv: GA.sc(c)}, nv)

    @staticmethod
    def var(i, nv=3):
        ee = [0] * nv
        ee[i] = 1
        return CP({tuple(ee): GA.sc(1)}, nv)

    def __add__(self, o):
        if not isinstance(o, CP):
            o = CP.scal(o, self.nv)
        r = dict(self.d)
        for kk, v in o.d.items():
            r[kk] = GA.add(r.get(kk, {}), v)
        return CP(r, self.nv)

    __radd__ = __add__

    def __neg__(self):
        return CP({kk: GA.neg(v) for kk, v in self.d.items()}, self.nv)

    def __sub__(self, o):
        if not isinstance(o, CP):
            o = CP.scal(o, self.nv)
        return self + (-o)

    def __mul__(self, o):
        if not isinstance(o, CP):
            if isinstance(o, dict):
                o = CP.const(o, self.nv)
            else:
                return CP({kk: GA.scal(o, v) for kk, v in self.d.items()}, self.nv)
        r = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                kk = tuple(a + b for a, b in zip(k1, k2))
                r[kk] = GA.add(r.get(kk, {}), mulv(v1, v2))
        return CP(r, self.nv)

    def __rmul__(self, o):
        if isinstance(o, dict):
            return CP.const(o, self.nv) * self
        return self * o

    def deriv(self, i):
        r = {}
        for kk, v in self.d.items():
            if kk[i] > 0:
                k2 = list(kk)
                k2[i] -= 1
                r[tuple(k2)] = GA.add(r.get(tuple(k2), {}), GA.scal(kk[i], v))
        return CP(r, self.nv)

    def subs0(self, i, val):
        r = {}
        for kk, v in self.d.items():
            k2 = list(kk)
            p = k2[i]
            k2[i] = 0
            r[tuple(k2)] = GA.add(r.get(tuple(k2), {}), GA.scal(F(val) ** p, v))
        return CP(r, self.nv)

    def trunc(self, idx, N):
        return CP({kk: v for kk, v in self.d.items() if sum(kk[i] for i in idx) <= N}, self.nv)

    def homog(self, idx, N):
        return CP({kk: v for kk, v in self.d.items() if sum(kk[i] for i in idx) == N}, self.nv)

    def coef(self, kk):
        return self.d.get(tuple(kk), {})

    def is_zero(self):
        return not self.d


def minv(X):
    dd = X[0][0] * X[1][1] - X[0][1] * X[1][0]
    return [[X[1][1] / dd, -X[0][1] / dd], [-X[1][0] / dd, X[0][0] / dd]]


def trace_against(Mi, Q):
    return GA.add(*[GA.scal(Mi[i][j], Q[j][i]) for i in range(2) for j in range(2)])


# ------------------------------------------------------------------ (2) generic jets, adapted gauge
KA = GA.add(E[0], E[3])
NA = GA.scal(F(1, 2), GA.sub(E[0], E[3]))
FA = [E[1], E[2]]
FREC = [GA.neg(E[1]), GA.neg(E[2])]
LAMA = GA.scal(F(1, 2), mulv(NA, KA))


def jets_step(P, u0, mutate=None):
    """N1(0) + tr(M^-1 Q) on jets; returns (N2 weight 0 zero, N2 weight 1/2 zero, c~, d, d', theta, tr M^-1 M')."""
    M0, M1, cub, d0, d1, dl, R1, R2, B0, B1, junk, junkl, J0, J1, Jl, al = P
    u_, ETA = CP.var(0), [CP.var(1), CP.var(2)]
    C = CP.scal
    M = [[C(M0[i][j]) + u_ * M1[i][j] for j in range(2)] for i in range(2)]
    sig = CP()
    for i in range(2):
        for j in range(2):
            sig = sig - ETA[i] * ETA[j] * M[i][j] * F(1, 2)
    for (a, b, c, co) in cub:
        sig = sig + ETA[a] * ETA[b] * ETA[c] * (C(co[0]) + u_ * co[1])
    d = C(d0) + u_ * d1 + ETA[0] * dl[0] + ETA[1] * dl[1] + u_ * ETA[0] * dl[2]
    R = C(1)
    if mutate != 'notransport':
        for b in range(2):
            R = R + ETA[b] * (CP.const(R1[b][0]) + u_ * CP.const(R1[b][1]))
        for (a, b, mv) in R2:
            R = R + ETA[a] * ETA[b] * CP.const(mv)
    U = d * R
    B = [[C(B0[i][j]) + u_ * B1[i][j] for j in range(2)] for i in range(2)]
    if mutate == 'antisymB':
        B[0][1] = B[0][1] + C(F(1, 3))
    Om = []
    for c in range(2):
        o = CP()
        for dd in range(2):
            o = o + B[dd][c] * wedge(FA[dd], NA)
        o = o + CP.const(junk[c]) + ETA[0] * CP.const(junkl[c][0]) + ETA[1] * CP.const(junkl[c][1])
        Om.append(o)
    if mutate == 'noconn':
        Om = [CP(), CP()]
    at = lambda X: X.subs0(0, u0)
    dU_u, dU_e = at(U.deriv(0)), [at(U.deriv(1)), at(U.deriv(2))]
    ds_u, ds_e = at(sig.deriv(0)), [at(sig.deriv(1)), at(sig.deriv(2))]
    U0 = at(U)
    Om = [at(o) for o in Om]
    J00 = [[J0[i][j] + u0 * J1[i][j] for j in range(2)] for i in range(2)]
    Ji = minv(J00)
    L = [[ETA[0] * Jl[i][j][0] + ETA[1] * Jl[i][j][1] for j in range(2)] for i in range(2)]
    X = [[sum((L[r][j] * Ji[i][r] for r in range(2)), CP()) for j in range(2)] for i in range(2)]
    X2 = [[sum((X[i][r] * X[r][j] for r in range(2)), CP()) for j in range(2)] for i in range(2)]
    Qm = [[C(1 if i == j else 0) - X[i][j] + X2[i][j] for j in range(2)] for i in range(2)]
    Jinv = [[sum((Qm[i][r] * Ji[r][j] for r in range(2)), CP()) for j in range(2)] for i in range(2)]
    alpha = [C(al[b][0]) + ETA[0] * al[b][1] + ETA[1] * al[b][2] for b in range(2)]

    def dfc(dX_e, dX_u, c):
        out = CP()
        for b in range(2):
            out = out + Jinv[b][c] * (dX_e[b] - alpha[b] * dX_u)
        return out

    DU = CP.const(NA) * dU_u
    grad = CP.const(NA) * ds_u
    for c in range(2):
        DU = DU + CP.const(FREC[c]) * (dfc(dU_e, dU_u, c) + Om[c] * U0 * F(1, 2))
        grad = grad + CP.const(FREC[c]) * dfc(ds_e, ds_u, c)
    N1 = (CP.const(LAMA) * DU * CP.const(KA)).trunc((1, 2), 2)
    N2 = (CP.const(LAMA) * grad * U0 * CP.const(KA)).trunc((1, 2), 2)
    Mu = [[M0[i][j] + u0 * M1[i][j] for j in range(2)] for i in range(2)]
    Mi = minv(Mu)
    Q = [[N2.coef((0, 2, 0)), GA.scal(F(1, 2), N2.coef((0, 1, 1)))],
         [GA.scal(F(1, 2), N2.coef((0, 1, 1))), N2.coef((0, 0, 2))]]
    ctil = GA.add(N1.coef((0, 0, 0)), trace_against(Mi, Q))
    trMiMp = sum(Mi[i][j] * M1[j][i] for i in range(2) for j in range(2))
    theta = B0[0][0] + B0[1][1] + u0 * (B1[0][0] + B1[1][1])
    return (N2.homog((1, 2), 0).is_zero(), N2.homog((1, 2), 1).is_zero(), ctil,
            d0 + u0 * d1, d1, theta, trMiMp)


def jet_data():
    bv = wedge
    k, n, f = KA, NA, FA
    M0 = [[F(3), F(1, 2)], [F(1, 2), F(2)]]
    M1 = [[F(1, 3), F(-1, 5)], [F(-1, 5), F(2, 7)]]
    cub = [(0, 0, 0, (F(1, 4), F(1, 2))), (0, 1, 1, (F(-2, 3), F(1))), (1, 1, 1, (F(5), F(-1, 3)))]
    R1 = [[GA.add(GA.scal(F(1, 3), bv(f[0], n)), GA.scal(F(2), bv(f[1], k)), GA.scal(F(-1, 2), bv(f[0], f[1]))),
           GA.add(GA.scal(F(1, 7), bv(f[1], n)), GA.scal(F(3), bv(k, n)))],
          [GA.add(GA.scal(F(-2, 5), bv(f[1], n)), GA.scal(F(1, 4), bv(f[0], n)), bv(k, n)),
           GA.add(GA.scal(F(1, 9), bv(f[0], k)), GA.scal(F(-3, 2), bv(f[0], n)))]]
    R2 = [(0, 1, GA.add(GA.sc(F(1, 5)), GA.scal(F(2), bv(f[0], n)))), (1, 1, GA.scal(F(-1, 3), bv(f[1], f[0])))]
    B0 = [[F(1, 4), F(1, 6)], [F(1, 6), F(-1, 5)]]
    B1 = [[F(2, 3), F(-1, 7)], [F(-1, 7), F(1, 2)]]
    junk = [GA.add(GA.scal(F(2), bv(f[0], f[1])), GA.scal(F(-1, 3), bv(f[0], k)), GA.scal(F(5), bv(k, n))),
            GA.add(GA.scal(F(1, 2), bv(f[1], k)), GA.scal(F(-4), bv(f[0], f[1])))]
    junkl = [[GA.scal(F(1, 3), bv(f[0], n)), GA.scal(F(2), bv(f[1], k))],
             [GA.scal(F(-1), bv(f[1], n)), GA.scal(F(1, 5), bv(f[0], f[1]))]]
    J0 = [[F(1), F(1, 3)], [F(-1, 4), F(2)]]
    J1 = [[F(1, 5), F(0)], [F(1, 2), F(-1, 3)]]
    Jl = [[(F(1, 2), F(1)), (F(0), F(-1, 3))], [(F(2), F(1, 7)), (F(1, 4), F(0))]]
    al = [(F(1, 3), F(2), F(-1)), (F(-5, 2), F(1, 3), F(1, 4))]
    return [M0, M1, cub, F(2), F(-3, 4), (F(1, 3), F(-1, 2), F(1)), R1, R2, B0, B1, junk, junkl, J0, J1, Jl, al]


# ------------------------------------------------------------------ truncated series for the plane wave
class Ser(object):
    """Series in eta1, eta2 (vars 0, 1; degree <= 3) and duals du, dv, dx1, dx2 (vars 2..5; degree <= 1)."""
    NV = 6

    def __init__(self, d=None):
        self.d = {}
        for kk, v in (d or {}).items():
            if v != 0 and kk[0] + kk[1] <= 3 and kk[2] + kk[3] + kk[4] + kk[5] <= 1:
                self.d[kk] = F(v)

    @staticmethod
    def c(a):
        return Ser({(0,) * 6: F(a)})

    @staticmethod
    def var(i, a=0):
        ee = [0] * 6
        ee[i] = 1
        return Ser({(0,) * 6: F(a), tuple(ee): F(1)})

    def _s(self, o):
        return o if isinstance(o, Ser) else Ser.c(o)

    def __add__(self, o):
        o = self._s(o)
        r = dict(self.d)
        for kk, v in o.d.items():
            r[kk] = r.get(kk, F(0)) + v
        return Ser(r)

    __radd__ = __add__

    def __neg__(self):
        return Ser({kk: -v for kk, v in self.d.items()})

    def __sub__(self, o):
        return self + (-self._s(o))

    def __rsub__(self, o):
        return self._s(o) - self

    def __mul__(self, o):
        if not isinstance(o, Ser):
            o = F(o)
            return Ser({kk: v * o for kk, v in self.d.items()})
        r = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                kk = tuple(a + b for a, b in zip(k1, k2))
                if kk[0] + kk[1] <= 3 and kk[2] + kk[3] + kk[4] + kk[5] <= 1:
                    r[kk] = r.get(kk, F(0)) + v1 * v2
        return Ser(r)

    __rmul__ = __mul__

    def val(self):
        return self.d.get((0,) * 6, F(0))

    def inv(self):
        a0 = self.val()
        x = (self - a0) * (1 / a0)
        out, p = Ser.c(1), Ser.c(1)
        for _ in range(8):
            p = p * x * (-1)
            if not p.d:
                break
            out = out + p
        return out * (1 / a0)

    def __truediv__(self, o):
        return self * (o.inv() if isinstance(o, Ser) else Ser.c(1 / F(o)))

    def __rtruediv__(self, o):
        return Ser.c(o) * self.inv()

    def coef(self, kk):
        return self.d.get(tuple(kk), F(0))

    def dual(self, j):
        r = {}
        for kk, v in self.d.items():
            if kk[j] == 1:
                k2 = list(kk)
                k2[j] = 0
                r[tuple(k2)] = v
        return Ser(r)

    def nodual(self):
        return Ser({kk: v for kk, v in self.d.items() if kk[2] + kk[3] + kk[4] + kk[5] == 0})


class CS(object):
    """Clifford-valued series: blade -> Ser."""

    def __init__(self, d=None):
        self.d = {b: s for b, s in (d or {}).items() if s.d}

    @staticmethod
    def from_mv(mv, s=None):
        s = s if s is not None else Ser.c(1)
        return CS({b: s * c for b, c in mv.items()})

    def __add__(self, o):
        r = dict(self.d)
        for b, s in o.d.items():
            r[b] = r[b] + s if b in r else s
        return CS(r)

    def __mul__(self, o):
        if isinstance(o, CS):
            r = {}
            for b1, s1 in self.d.items():
                for b2, s2 in o.d.items():
                    sg, b = GA.blade_mul(b1, b2, S4)
                    if sg == 0:
                        continue
                    t = s1 * s2 * sg
                    r[b] = r[b] + t if b in r else t
            return CS(r)
        if isinstance(o, Ser):
            return CS({b: s * o for b, s in self.d.items()})
        return CS({b: s * F(o) for b, s in self.d.items()})

    def coef_mv(self, kk):
        return {b: s.coef(kk) for b, s in self.d.items() if s.coef(kk) != 0}

    def val_mv(self):
        return {b: s.val() for b, s in self.d.items() if s.val() != 0}

    def map(self, fn):
        return CS({b: fn(s) for b, s in self.d.items()})


# ------------------------------------------------------------------ (3) plane-wave field, Kerr-Schild gauge
KP = GA.add(E[0], E[3])                  # image of d_v (the leaf displacement l)
MP = GA.scal(F(1, 2), GA.sub(E[0], E[3]))
EP = [E[1], E[2]]
EK = [wedge(EP[0], KP), wedge(EP[1], KP)]


def mm(X, Y):
    return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)] for i in range(2)]


def madd(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(2)] for i in range(2)]


def mvv(X, y):
    return [X[i][0] * y[0] + X[i][1] * y[1] for i in range(2)]


class Model(object):
    """ds^2 = 2 du dv + x^T h(u) x du^2 - dx^2, h = -ROT diag(c) ROT^T/(1+u)^2; null hypersurface v = x^T S x/2."""

    def __init__(self, roots, rot, B0):
        self.roots, self.rot, self.B0 = roots, rot, B0
        self.cs = [F(r1 * (r1 - 1)) for r1, r2 in roots]

    def basis(self, i, u):
        r1, r2 = self.roots[i]
        s = 1 + u
        return s ** r1, s ** r2, s ** (r1 - 1) * r1, s ** (r2 - 1) * r2

    def jac(self, i, u, up):
        f, g, fp, gp = self.basis(i, u)
        f0, g0, fp0, gp0 = self.basis(i, up)
        w = f0 * gp0 - fp0 * g0
        return ((g * f0 - f * g0) / w, (gp * f0 - fp * g0) / w, (f * gp0 - g * fp0) / w, (fp * gp0 - gp * fp0) / w)

    def rmaps(self, u, up):
        R = self.rot
        Rt = [[R[j][i] for j in range(2)] for i in range(2)]
        j0, j1 = self.jac(0, u, up), self.jac(1, u, up)
        return [mm(mm(R, [[j0[idx], 0], [0, j1[idx]]]), Rt) for idx in range(4)]

    def h(self, u):
        R = self.rot
        Rt = [[R[j][i] for j in range(2)] for i in range(2)]
        return mm(mm(R, [[-self.cs[0] / (1 + u) ** 2, 0], [0, -self.cs[1] / (1 + u) ** 2]]), Rt)

    def congruence(self, u):
        A, Ap, K, Kp = self.rmaps(u, F(0))
        return madd(K, mm(A, self.B0)), madd(Kp, mm(Ap, self.B0))


def maps_dual(md, u0, up):
    A, Ap, K, Kp = md.rmaps(u0, up)
    h = md.h(u0)
    du = Ser.var(2)
    lift = lambda X, Xd: [[Ser.c(X[i][j]) + du * Xd[i][j] for j in range(2)] for i in range(2)]
    neg = lambda X: [[-x for x in row] for row in X]
    return (lift(A, Ap), lift(Ap, neg(mm(h, A))), lift(K, Kp), lift(Kp, neg(mm(h, K))))


def pw_kernel(md, u0, up, yp, w=F(0), transport=True, frozen=False, dlog_factor=1):
    """N1~ = Lambda (D U)/Delta^(1/2) k(x'), N2~ = Lambda (grad sigma) R k(x'); x' shifted by w along d_v."""
    J, Jp = md.congruence(u0)
    Jq, Jqp = md.congruence(up)
    eta = [Ser.var(0), Ser.var(1)]
    y = [yp[0] + eta[0], yp[1] + eta[1]]
    xperp = mvv(J, y)
    S = mm([[J[j][i] for j in range(2)] for i in range(2)], Jp)
    v = (y[0] * mvv(S, y)[0] + y[1] * mvv(S, y)[1]) * F(1, 2)
    xq = mvv(Jq, list(yp))
    Sq = mm([[Jq[j][i] for j in range(2)] for i in range(2)], Jqp)
    vq = (yp[0] * mvv(Sq, list(yp))[0] + yp[1] * mvv(Sq, list(yp))[1]) / 2 + w
    X1, X2, V = xperp[0] + Ser.var(4), xperp[1] + Ser.var(5), v + Ser.var(3)
    A, Ap, K, Kp = maps_dual(md, u0, up)
    dU = Ser.c(u0 - up) + Ser.var(2)
    Ai = minv(A)
    ww = mvv(Ai, [X1 - (K[0][0] * xq[0] + K[0][1] * xq[1]), X2 - (K[1][0] * xq[0] + K[1][1] * xq[1])])
    t = [Kp[i][0] * xq[0] + Kp[i][1] * xq[1] + Ap[i][0] * ww[0] + Ap[i][1] * ww[1] for i in range(2)]
    sigma = dU * (V - vq) - dU * F(1, 2) * (X1 * t[0] + X2 * t[1] - xq[0] * ww[0] - xq[1] * ww[1])
    Rs = CS.from_mv(GA.sc(1))
    if transport:
        for i in range(2):
            Rs = Rs + CS.from_mv(EK[i], (t[i] - ww[i]) * F(1, 2))
    nd = lambda s: s.nodual()
    sig0 = nd(sigma)
    dsig = [nd(sigma.dual(j)) for j in (2, 3, 4, 5)]
    R0 = Rs.map(nd)
    dR = [Rs.map(lambda s, j=j: nd(s.dual(j))) for j in (2, 3, 4, 5)]
    h = md.h(u0)
    H = xperp[0] * (h[0][0] * xperp[0] + h[0][1] * xperp[1]) + xperp[1] * (h[1][0] * xperp[0] + h[1][1] * xperp[1])
    hx = mvv(h, xperp)
    Om_u = CS({})
    for i in range(2):
        Om_u = Om_u + CS.from_mv(EK[i], hx[i])
    gu = CS.from_mv(KP)
    gv = CS.from_mv(MP) + CS.from_mv(KP, H * F(-1, 2))
    gi = [CS.from_mv(GA.neg(EP[0])), CS.from_mv(GA.neg(EP[1]))]
    Av, Apv = md.rmaps(u0, up)[0], md.rmaps(u0, up)[1]
    trAiAp = sum(minv(Av)[i][j] * Apv[j][i] for i in range(2) for j in range(2))
    dlogD = (F(2) / (u0 - up) - trAiAp) * dlog_factor
    DR = gu * (dR[0] + Om_u * R0 * F(1, 2)) + gv * dR[1] + gi[0] * dR[2] + gi[1] * dR[3]
    DUt = gu * R0 * (dlogD / 2) + DR
    grad = gu * dsig[0] + gv * dsig[1] + gi[0] * dsig[2] + gi[1] * dsig[3]
    kx = [Jp[0][0] * y[0] + Jp[0][1] * y[1], Jp[1][0] * y[0] + Jp[1][1] * y[1]]
    kq_ = mvv(Jqp, list(yp))
    if frozen:
        kx = [Ser.c(kq_[0]), Ser.c(kq_[1])]
    lamx = CS.from_mv(KP) * (CS.from_mv(MP) + CS.from_mv(EP[0], kx[0]) + CS.from_mv(EP[1], kx[1])) * F(1, 2)
    kq = GA.add(MP, GA.scal((kq_[0] ** 2 + kq_[1] ** 2) / 2, KP), GA.scal(kq_[0], EP[0]), GA.scal(kq_[1], EP[1]))
    rk = CS.from_mv(kq)
    return lamx * DUt * rk, lamx * grad * R0 * rk, sig0, lamx, R0, kq


def pw_raw(md, pt, **kw):
    """eta-Taylor coefficients: N1 and N2 as multivector-valued functions of (a, b), sigma as a scalar one."""
    N1, N2, sig0, lamx, R0, kq = pw_kernel(md, pt[0], pt[1], pt[2], **kw)
    z = (0, 0, 0, 0)
    return (lambda a, b: N1.coef_mv((a, b) + z), lambda a, b: N2.coef_mv((a, b) + z),
            lambda a, b: sig0.coef((a, b) + z))


PW_PTS = ((F(1, 2), F(-1, 3), (F(0), F(0))), (F(1, 5), F(3, 4), (F(1), F(-2))), (F(-1, 4), F(2, 3), (F(-3, 2), F(1, 2))))
DOUBLE = F(2)
FLAT_PTS = ((F(1, 2), F(-1, 3), (F(1, 5), F(-2, 7))), (F(3), F(1, 4), (F(-1, 2), F(1, 3))), (F(-1, 4), F(2), (F(0), F(0))))
CUBIC = (F(1, 3), F(-1, 5), F(2, 7), F(1, 4), F(-2, 3))
JET_US = (F(1, 2), F(-2, 3))
NS = (GA.scal(F(1, 2), GA.sub(E[0], E[3])), E[0], GA.add(E[0], GA.scal(F(1, 3), E[1]), GA.scal(F(-1, 5), E[2])))
PS = (GA.add(GA.scal(F(2), E[0]), GA.scal(F(-3), E[1]), GA.scal(F(1, 7), E[3])),
      GA.add(GA.scal(F(-1, 4), E[0]), GA.scal(F(5), E[2]), GA.scal(F(2, 3), E[3])))
VGEN = GA.add(GA.sc(F(3)), E[1], GA.scal(F(2), wedge(E[0], E[2])), GA.scal(F(-1, 3), mulv(mulv(E[1], E[2]), E[3])),
              GA.scal(F(5), mulv(mulv(E[0], E[1]), mulv(E[2], E[3]))))
BSYM = [[F(1, 4), F(1, 6)], [F(1, 6), F(-1, 5)]]
BANTI = [[F(1, 4), F(1, 3)], [F(-1, 3), F(-1, 5)]]
JUNK = (F(2), F(-3), F(5))
LS = (GA.scal(F(1, 2), GA.sub(E[0], E[3])), GA.add(GA.scal(F(5, 4), E[0]), GA.scal(F(3, 4), E[1]), GA.neg(E[3])))
NS2 = (GA.scal(F(1, 2), GA.sub(E[0], E[3])), GA.add(E[0], GA.scal(F(1, 3), E[2])))
FLATPLANE = ((F(1, 2), F(1, 3), F(-2), F(1, 5)), (F(-3), F(0), F(1, 4), F(-2, 7)))
ZETAS = ({}, GA.add(GA.scal(F(1, 3), E[1]), GA.scal(F(-2), E[2])), GA.scal(F(7, 5), E[1]))
TS = (E[0], GA.add(GA.scal(F(5, 3), E[0]), GA.scal(F(4, 3), E[2])), GA.add(GA.scal(F(13, 12), E[0]), GA.scal(F(5, 12), E[3])))
WS = (F(1, 3), F(-2, 5), F(1, 7), F(-1, 9))


def pw_models():
    ROT = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
    B0 = ((F(1, 4), F(1, 6)), (F(1, 6), F(-1, 5)))
    return Model(((2, -1), (3, -2)), ROT, B0), Model(((1, 0), (1, 0)), ROT, B0)


# ------------------------------------------------------------------ (4) flat field, cubic null hypersurface
KF = GA.add(E[0], E[3])
MF = GA.scal(F(1, 2), GA.sub(E[0], E[3]))


def flat_step(u, up, yp, cubic, mutate=None):
    AL, BE, GAM, C3, C4 = cubic
    P = lambda c: CP.scal(c, 2)

    def gradf(y1, y2):
        return (y1 * AL + y2 * BE + y1 * y1 * (3 * C3) + y2 * y2 * C4, y1 * BE + y2 * GAM + y1 * y2 * (2 * C4))

    def X(uu, y1, y2):
        g1, g2 = gradf(y1, y2)
        f0 = (y1 * y1 * AL + y1 * y2 * (2 * BE) + y2 * y2 * GAM) * F(1, 2) + y1 * y1 * y1 * C3 + y1 * y2 * y2 * C4
        return (CP.const(KF, 2) * uu + CP.const(MF, 2) * (f0 + (g1 * g1 + g2 * g2) * (F(uu) / 2))
                + CP.const(E[1], 2) * (y1 + g1 * uu) + CP.const(E[2], 2) * (y2 + g2 * uu))

    def kv(y1, y2):
        g1, g2 = gradf(y1, y2)
        return (CP.const(KF, 2) + CP.const(MF, 2) * ((g1 * g1 + g2 * g2) * F(1, 2)) + CP.const(E[1], 2) * g1
                + CP.const(E[2], 2) * g2)

    y1, y2 = P(yp[0]) + CP.var(0, 2), P(yp[1]) + CP.var(1, 2)
    dx = X(u, y1, y2) - X(up, P(yp[0]), P(yp[1]))
    sig = (dx * dx) * F(1, 2)
    kq = kv(P(yp[0]), P(yp[1]))
    lam = (CP.const(MF, 2) * (kq if mutate == 'frozen' else kv(y1, y2))) * F(1, 2)
    N2 = (lam * dx * kq).trunc((0, 1), 2)
    s = lambda a, b: sig.coef((a, b)).get((), F(0))
    return (lambda a, b: N2.coef((a, b))), s


# ================================================================== checks
def check_projector_algebra_of_the_null_trace():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    k = KA
    ok = True
    for n in NS:
        assert dotv(n, k) == 1
        lam = GA.scal(F(1, 2), mulv(n, k))
        ok &= GA.eq(mulv(lam, lam), lam)
        ok &= GA.is_zero(mulv(lam, k)) and GA.eq(mulv(k, lam), k)
        for p in PS:
            # Lambda p k = 2 (p.k) Lambda: only the derivative along the generator survives
            ok &= GA.eq(mulv(mulv(lam, p), k), GA.scal(2 * dotv(p, k), lam))
        # tail and mass numerators on the generator: Lambda (c k) V k = 0 for any multivector V
        ok &= GA.is_zero(mulv(mulv(mulv(lam, GA.scal(JUNK[1], k)), VGEN), k))
    # projected transverse connection: Lambda f^c Omega(f_c) k = 2 theta Lambda when Omega(f_c) = B(f_c)^n
    lam = GA.scal(F(1, 2), mulv(NA, KA))
    for (B, sym) in ((BSYM, True), (BANTI, False)):
        tot = {}
        for c in range(2):
            Om = GA.add(*[GA.scal(B[d][c], wedge(FA[d], NA)) for d in range(2)])
            Om = GA.add(Om, GA.scal(JUNK[0], wedge(FA[c], KA)), GA.scal(JUNK[1], wedge(FA[0], FA[1])),
                        GA.scal(JUNK[2], wedge(KA, NA)))
            tot = GA.add(tot, mulv(mulv(mulv(lam, GA.neg(FA[c])), Om), KA))
        theta = B[0][0] + B[1][1]
        ok &= GA.eq(tot, GA.scal(2 * theta, lam)) == sym
    GA.check("projector algebra: Lambda p k = 2(p.k) Lambda, tail and mass numerators vanish, connection gives theta", ok)
    return ok


def check_step_coefficient_formula_on_generic_jets():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.imported-gtg-dictionary")
    P = jet_data()
    ok = True
    for u0 in JET_US:
        w0, w12, ctil, d, dp, theta, trMiMp = jets_step(P, u0)
        ok &= w0 and w12
        pred = GA.scal(2 * (dp - d * trMiMp / 2 + theta * d / 2), LAMA)
        ok &= GA.eq(ctil, pred) and not GA.is_zero(ctil)
        # the first-order transport does not enter the step coefficient
        ok &= GA.eq(jets_step(P, u0, mutate='notransport')[2], ctil)
        # half-density law: d/sqrt(det M) = (a a')^(-1/2) gives d' = d (tr(M^-1 M') - theta)/2, and c~ = 0
        P2 = list(P)
        P2[4] = d * (trMiMp - theta) / 2
        P2[3] = d - u0 * P2[4]
        r = jets_step(P2, u0)
        ok &= GA.is_zero(r[2]) and r[0] and r[1]
        for mut in ('antisymB', 'noconn'):
            w0, w12, ctil, d, dp, theta, trMiMp = jets_step(P, u0, mutate=mut)
            ok &= not GA.eq(ctil, GA.scal(2 * (dp - d * trMiMp / 2 + theta * d / 2), LAMA))
    GA.check("generic jets: N2 = O(eta^2), c~ = 2[d' - d tr(M^-1 M')/2 + theta d/2] Lambda, zero by the half-density law", ok)
    return ok


def check_step_coefficient_vanishes_on_the_plane_wave_field():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces")
    curved, flat = pw_models()

    def ctil(n1, n2, s):
        M = [[-2 * s(2, 0), -s(1, 1)], [-s(1, 1), -2 * s(0, 2)]]
        Q = [[n2(2, 0), GA.scal(F(1, 2), n2(1, 1))], [GA.scal(F(1, 2), n2(1, 1)), n2(0, 2)]]
        return GA.add(n1(0, 0), trace_against(minv(M), Q))

    ok = True
    for md in (curved, flat):
        for pt in PW_PTS:
            n1, n2, s = pw_raw(md, pt)
            ok &= not n2(0, 0) and not n2(1, 0) and not n2(0, 1)
            ok &= s(0, 0) == 0 and s(1, 0) == 0 and s(0, 1) == 0
            ok &= GA.is_zero(ctil(n1, n2, s)) and (md is flat or not GA.is_zero(n1(0, 0)))
    pt = PW_PTS[1]
    ok &= not GA.is_zero(ctil(*pw_raw(curved, pt, dlog_factor=DOUBLE)))
    ok &= not GA.is_zero(ctil(*pw_raw(curved, pt, frozen=True)))
    n1, n2, s = pw_raw(curved, pt, transport=False)
    ok &= bool(n2(1, 0) or n2(0, 1))
    GA.check("plane wave (curved and flat-shear): N2 = O(eta^2) and the step coefficient N1(0) + tr(M^-1 Q) = 0", ok)
    return ok


def check_step_coefficient_vanishes_on_a_flat_cubic_null_hypersurface():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces")

    def trq(n2, s):
        M = [[-2 * s(2, 0), -s(1, 1)], [-s(1, 1), -2 * s(0, 2)]]
        Q = [[n2(2, 0), GA.scal(F(1, 2), n2(1, 1))], [GA.scal(F(1, 2), n2(1, 1)), n2(0, 2)]]
        return trace_against(minv(M), Q), M

    ok = True
    for (u, up, yp) in FLAT_PTS:
        n2, s = flat_step(u, up, yp, CUBIC)
        ok &= not n2(0, 0) and not n2(1, 0) and not n2(0, 1)
        ok &= s(0, 0) == 0 and s(1, 0) == 0 and s(0, 1) == 0
        t, M = trq(n2, s)
        ok &= GA.is_zero(t) and not GA.is_zero(n2(2, 0))
    u, up, yp = FLAT_PTS[0]
    ok &= not GA.is_zero(trq(*flat_step(u, up, yp, CUBIC, mutate='frozen'))[0])
    # coincidence: the transverse Hessian at u = u' is the screen metric, det = a^2
    AL, BE, GAM, C3, C4 = CUBIC
    y1, y2 = yp
    hess = [[AL + 6 * C3 * y1, BE + 2 * C4 * y2], [BE + 2 * C4 * y2, GAM + 2 * C4 * y1]]
    Jm = [[1 + u * hess[0][0], u * hess[0][1]], [u * hess[1][0], 1 + u * hess[1][1]]]
    a = Jm[0][0] * Jm[1][1] - Jm[0][1] * Jm[1][0]
    Mc = trq(*flat_step(u, u, yp, CUBIC))[1]
    ok &= Mc[0][0] * Mc[1][1] - Mc[0][1] * Mc[1][0] == a * a
    GA.check("flat field, cubic null hypersurface: N2 = O(eta^2), zero step coefficient, coincidence det M = a^2", ok)
    return ok


def check_layer_displacement_and_coincidence_coefficient():
    premise("synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field")
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    curved, flat = pw_models()
    ok = True
    for (u0, up, yp) in PW_PTS[:2]:
        a = pw_kernel(curved, u0, up, yp, w=F(0))
        b = pw_kernel(curved, u0, up, yp, w=F(1))
        # sigma on H x H_w: sigma_w = sigma - w (u - u'), so b(u, u') = (u' - u)(k.l), k.l = 1 here
        ok &= b[2].val() - a[2].val() == up - u0
        ok &= dotv(a[5], KP) == 1
        dN2 = GA.sub(b[1].val_mv(), a[1].val_mv())
        pred = GA.neg(mulv(mulv(mulv(a[3].val_mv(), KP), a[4].val_mv()), a[5]))
        ok &= GA.eq(dN2, pred) and not GA.is_zero(dN2)
    # coincidence: (1/2) d_w N2 / (k.l) = -(1/2) Lambda l k/(k.l) = -Lambda for every null l and n with n.k = 1;
    # with sgn(t - t') sgn(w) = -1 the delta coefficient is +Lambda
    k = KA
    for l in LS:
        assert dotv(l, l) == 0
        for n in NS2:
            lam = GA.scal(F(1, 2), mulv(n, k))
            coeff = GA.scal(F(-1, 2) / dotv(l, k), GA.neg(mulv(mulv(lam, l), k)))
            ok &= GA.eq(coeff, lam)
    # flat null plane, exact: sigma_w = -w (u - u')... = w(u' - u) - |eta|^2/2 and N2 = -2 w Lambda
    lam = GA.scal(F(1, 2), mulv(NA, k))
    for (du, e1, e2, w) in FLATPLANE:
        dx = GA.add(GA.scal(du, k), GA.scal(-w, NA), GA.scal(e1, E[1]), GA.scal(e2, E[2]))
        ok &= dotv(dx, dx) / 2 == -w * du - (e1 * e1 + e2 * e2) / 2
        ok &= GA.eq(mulv(mulv(lam, dx), k), GA.scal(-2 * w, lam))
    GA.check("layer: sigma_w = sigma - w(u - u'), d_w N2 = -Lambda l R k, coincidence coefficient exactly Lambda", ok)
    return ok


def check_layer_wightman_term_has_one_i0_for_both_leaf_sides():
    premise("synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard")
    premise("synthesis.imported-microlocal-hadamard-condition")
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    # the i0 of G_par^+ sits where sigma = 0; there x' - x = w (l + rho k + zeta) is null (rho fixed by that),
    # and the regulator eps (t(x) - t(x')) = -eps (x' - x).T has the sign of -w for every future timelike T:
    # sigma*/w = (u' - u)(k.l)/w + O(w) and Im/w < 0 for both signs of w, so both sides give (u' - u - i0)^-1
    k = KA
    ok = True
    for l in LS:
        for zeta in ZETAS:
            rho = -(2 * dotv(l, zeta) + dotv(zeta, zeta)) / (2 * dotv(l, k))
            for T in TS:
                assert dotv(T, T) == 1 and dotv(T, E[0]) > 0 and dotv(l, l) == 0 and dotv(l, E[0]) > 0
                for w in WS:
                    d = GA.scal(w, GA.add(l, GA.scal(rho, k), zeta))
                    ok &= dotv(d, d) == 0
                    ok &= -dotv(d, T) / w < 0
    GA.check("the regulator at the light cone has the sign of -v on both sides of the leaf", ok)
    return ok
