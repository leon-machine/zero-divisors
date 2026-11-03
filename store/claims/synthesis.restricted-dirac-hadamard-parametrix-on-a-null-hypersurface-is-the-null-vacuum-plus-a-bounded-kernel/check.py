"""Remainder bound for the restricted Dirac Hadamard parametrix on a null hypersurface: exact checks.

Kernel numerator N = Lambda(x) [ (D U~) sigma - (grad sigma) R ] e0 Lambda(x')^dagger, U = Delta^(1/2) R,
U~ = U/Delta^(1/2)(eta = 0), expanded in the label difference eta of x = X(u, y' + eta), x' = X(u', y').
The restricted kernel is (canonical factor) Delta^(1/2) N/sigma^2 plus the i0 term, the mass term and V log sigma.
Its coefficient of log(eps) is -2 pi tr(M^-1 X)/sqrt(det M), X the quadratic form of the degree-2 part N2
(sigma = -(1/2) eta^T M eta + ...). Checks:
(1) projector algebra: only the f^n components of a bivector survive Lambda f^c (.) e0 Lambda; mass and
    transverse leading terms are projected out;
(2) generic jets (adapted gauge, arbitrary sigma, Delta, transport, connection and frame data): N0 = N1 = 0 and
    tr(M^-1 X) = -[d' - d tr(M^-1 M')/2 + theta d/2] Lambda exactly;
(3) on the plane-wave model the bracket vanishes: d_u log Delta - tr(M^-1 d_u M) + theta(u) = 0;
(4) first principles on the plane-wave field (Kerr-Schild GTG gauge, tidal and deviation maps not commuting):
    N0 = N1 = 0 and tr(M^-1 X) = 0, also off the central generator; (5) the same on the flat field with an
    expanding and shearing null hypersurface; (6) the model's transport rotor and connection;
(7) mass and V log sigma terms have degree >= -1; (8) the regularised model integrals.
Exact arithmetic only (Fractions; truncated power series with first-order dual variables).
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


# ------------------------------------------------------------------ truncated series
class Ser(object):
    """Series in eta1, eta2 (vars 0, 1; total degree <= 3) and duals du, dv, dx1, dx2 (vars 2..5; degree <= 1)."""
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
            out = out + p
        return out * (1 / a0)

    def __truediv__(self, o):
        return self * (o.inv() if isinstance(o, Ser) else 1 / F(o))

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

    def deta(self, i):
        r = {}
        for kk, v in self.d.items():
            if kk[i] > 0:
                k2 = list(kk)
                k2[i] -= 1
                r[tuple(k2)] = r.get(tuple(k2), F(0)) + kk[i] * v
        return Ser(r)

    def nodual(self):
        return Ser({kk: v for kk, v in self.d.items() if kk[2] + kk[3] + kk[4] + kk[5] == 0})


class CS(object):
    """Clifford-valued series: blade -> Ser."""

    def __init__(self, d=None):
        self.d = {b: s for b, s in (d or {}).items() if s.d}

    @staticmethod
    def mv(mvec, s=None):
        s = s if s is not None else Ser.c(1)
        return CS({b: s * c for b, c in mvec.items()})

    def __add__(self, o):
        r = dict(self.d)
        for b, s in o.d.items():
            r[b] = r[b] + s if b in r else s
        return CS(r)

    def __neg__(self):
        return CS({b: -s for b, s in self.d.items()})

    def __sub__(self, o):
        return self + (-o)

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

    def at(self, kk):
        return {b: s.coef(kk) for b, s in self.d.items() if s.coef(kk) != 0}

    def map(self, fn):
        return CS({b: fn(s) for b, s in self.d.items()})


Z6 = (0, 0, 0, 0, 0, 0)


def quad_parts(N, sig):
    """N0, (N1 components), tr(M^-1 X) with X the quadratic form of N2 and M from sigma's eta-quadratic part."""
    N0 = N.at(Z6)
    N1 = [N.at((1, 0, 0, 0, 0, 0)), N.at((0, 1, 0, 0, 0, 0))]
    x11, x22 = N.at((2, 0, 0, 0, 0, 0)), N.at((0, 2, 0, 0, 0, 0))
    x12 = GA.scal(F(1, 2), N.at((1, 1, 0, 0, 0, 0)))
    M = [[-2 * sig.coef((2, 0, 0, 0, 0, 0)), -sig.coef((1, 1, 0, 0, 0, 0))],
         [-sig.coef((1, 1, 0, 0, 0, 0)), -2 * sig.coef((0, 2, 0, 0, 0, 0))]]
    Mi = minv(M)
    tr = GA.add(GA.scal(Mi[0][0], x11), GA.scal(2 * Mi[0][1], x12), GA.scal(Mi[1][1], x22))
    return N0, N1, tr, M


# ------------------------------------------------------------------ 2x2 helpers
def mm(X, Y):
    return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)] for i in range(2)]


def madd(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(2)] for i in range(2)]


def mvec(X, y):
    return [X[i][0] * y[0] + X[i][1] * y[1] for i in range(2)]


def tp(X):
    return [[X[j][i] for j in range(2)] for i in range(2)]


def minv(X):
    d = X[0][0] * X[1][1] - X[0][1] * X[1][0]
    return [[X[1][1] / d, -X[0][1] / d], [-X[1][0] / d, X[0][0] / d]]


# ------------------------------------------------------------------ adapted frame (store convention)
KV = GA.add(E[0], E[3])                      # generator tangent k
NV = GA.scal(F(1, 2), GA.sub(E[0], E[3]))    # transverse null partner n, k.n = 1
FV = [E[1], E[2]]
FREC = [GA.neg(E[1]), GA.neg(E[2])]
LAM = GA.scal(F(1, 2), mulv(NV, KV))


def generic_jets(u0, data, mutate=None):
    """Adapted gauge: Lambda constant on H, Omega(k) = 0 on H, f^n part of Omega(f_c) = B(f_c)^n."""
    (M0, M1, cub, d0, d1, dl, R1, R2, B0, B1, junk, junkl, J0, J1, Jl, al) = data
    eta = [Ser.var(0), Ser.var(1)]
    U_ = Ser.var(2, u0)                      # u = u0 + du
    dU = Ser.var(2)
    sig = Ser()
    for i in range(2):
        for j in range(2):
            sig = sig - eta[i] * eta[j] * (Ser.c(M0[i][j] + u0 * M1[i][j]) + dU * M1[i][j]) * F(1, 2)
    for (a, b, c, coef) in cub:
        sig = sig + eta[a] * eta[b] * eta[c] * (U_ * coef[1] + coef[0])
    d = U_ * d1 + d0 + eta[0] * dl[0] + eta[1] * dl[1] + U_ * eta[0] * dl[2]
    R = CS.mv(GA.sc(1))
    for b in range(2):
        R = R + CS.mv(R1[b][0], eta[b]) + CS.mv(R1[b][1], eta[b] * U_)
    for (a, b, mvx) in R2:
        R = R + CS.mv(mvx, eta[a] * eta[b])
    U = R * d
    B = [[Ser.c(B0[i][j]) + U_ * B1[i][j] for j in range(2)] for i in range(2)]
    if mutate == 'antisymmetric B':
        B[0][1] = B[0][1] + F(1, 3)
    Om = []
    for c in range(2):
        o = CS.mv(junk[c]) + CS.mv(junkl[c][0], eta[0]) + CS.mv(junkl[c][1], eta[1])
        for dd in range(2):
            o = o + CS.mv(wedge(FV[dd], NV), B[dd][c])
        Om.append(o.map(lambda s: s.nodual()))
    if mutate == 'no connection':
        Om = [CS(), CS()]
    J00 = [[J0[i][j] + u0 * J1[i][j] for j in range(2)] for i in range(2)]
    Ji = minv(J00)
    L = [[eta[0] * Jl[i][j][0] + eta[1] * Jl[i][j][1] for j in range(2)] for i in range(2)]
    X = [[Ji[i][0] * L[0][j] + Ji[i][1] * L[1][j] for j in range(2)] for i in range(2)]
    X2 = [[X[i][0] * X[0][j] + X[i][1] * X[1][j] for j in range(2)] for i in range(2)]
    Q = [[Ser.c(1 if i == j else 0) - X[i][j] + X2[i][j] for j in range(2)] for i in range(2)]
    Jinv = [[Q[i][0] * Ji[0][j] + Q[i][1] * Ji[1][j] for j in range(2)] for i in range(2)]
    alpha = [Ser.c(al[b][0]) + eta[0] * al[b][1] + eta[1] * al[b][2] for b in range(2)]
    nd = lambda s: s.nodual()
    U0, sig0 = U.map(nd), sig.nodual()
    Uu, sigu = U.map(lambda s: s.dual(2)), sig.dual(2)
    Ue = [U.map(lambda s, i=i: s.deta(i).nodual()) for i in range(2)]
    sige = [sig.deta(i).nodual() for i in range(2)]

    def dfc_cs(Xe, Xu, c):
        out = CS()
        for b in range(2):
            out = out + (Xe[b] - Xu * alpha[b]) * Jinv[b][c]
        return out

    def dfc_s(Xe, Xu, c):
        out = Ser()
        for b in range(2):
            out = out + (Xe[b] - Xu * alpha[b]) * Jinv[b][c]
        return out

    DU = CS.mv(NV) * Uu
    grad = CS.mv(NV, sigu)
    for c in range(2):
        DU = DU + CS.mv(FREC[c]) * (dfc_cs(Ue, Uu, c) + Om[c] * U0 * F(1, 2))
        grad = grad + CS.mv(FREC[c], dfc_s(sige, sigu, c))
    N = CS.mv(LAM) * (DU * sig0 - grad * U0) * CS.mv(mulv(E[0], LAM))
    N0, N1, tr, M = quad_parts(N, sig0)
    Mu = [[M0[i][j] + u0 * M1[i][j] for j in range(2)] for i in range(2)]
    Mi = minv(Mu)
    trMiMp = sum(Mi[i][j] * M1[j][i] for i in range(2) for j in range(2))
    theta = B0[0][0] + B0[1][1] + u0 * (B1[0][0] + B1[1][1])
    dd0 = d0 + u0 * d1
    pred = GA.scal(-(d1 - dd0 * trMiMp / 2 + theta * dd0 / 2), LAM)
    return N0, N1, tr, pred, M == Mu


def jet_data(variant):
    bv = wedge
    k, n, f = KV, NV, FV
    M0 = [[F(3), F(1, 2)], [F(1, 2), F(2)]]
    M1 = [[F(1, 3), F(-1, 5)], [F(-1, 5), F(2, 7)]]
    cub = [(0, 0, 0, (F(1, 4), F(1, 2))), (0, 1, 1, (F(-2, 3), F(1))), (1, 1, 1, (F(5), F(-1, 3)))]
    R1 = [[GA.add(GA.scal(F(1, 3), bv(f[0], n)), GA.scal(F(2), bv(f[1], k)), GA.scal(F(-1, 2), bv(f[0], f[1]))),
           GA.add(GA.scal(F(1, 7), bv(f[1], n)), GA.scal(F(3), bv(k, n)))],
          [GA.add(GA.scal(F(-2, 5), bv(f[1], n)), GA.scal(F(1, 4), bv(f[0], n)), GA.scal(F(1), bv(k, n))),
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
    d0, d1, dl = F(2), F(-3, 4), (F(1, 3), F(-1, 2), F(1))
    if variant == 1:
        M0 = [[F(5, 2), F(-1)], [F(-1), F(7, 3)]]
        M1 = [[F(-1, 2), F(1, 3)], [F(1, 3), F(4)]]
        B0 = [[F(-2, 3), F(1, 2)], [F(1, 2), F(3, 4)]]
        B1 = [[F(1, 9), F(2)], [F(2), F(-1)]]
        d0, d1, dl = F(5, 3), F(7, 2), (F(-2), F(0), F(1, 5))
        R1 = [[R1[1][1], R1[0][0]], [R1[0][1], R1[1][0]]]
    return (M0, M1, cub, d0, d1, dl, R1, R2, B0, B1, junk, junkl, J0, J1, Jl, al)


# ------------------------------------------------------------------ plane-wave model (Kerr-Schild GTG gauge)
# hb^{-1}(a) = a + (1/2) H (a.K) K, K = e0 + e3; coordinates u = x.K, v = x.Mv, x_i = -x.e_i; position
# x = u Mv + v K + x_i e_i (Mv = (e0 - e3)/2), g = 2 du dv + H du^2 - dx^2, H = x^T h(u) x,
# h(u) = -ROT diag(c) ROT^T/(1+u)^2. Generators of H have tangent image Mv + ... ; transverse partner n = K.
KK = GA.add(E[0], E[3])
MM = GA.scal(F(1, 2), GA.sub(E[0], E[3]))
EK = [wedge(E[1], KK), wedge(E[2], KK)]
ROT = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
B0PW = ((F(1, 4), F(1, 6)), (F(1, 6), F(-1, 5)))


class Model(object):
    def __init__(self, roots):
        self.roots = roots
        self.cs = [F(r1 * (r1 - 1)) for r1, r2 in roots]

    def basis(self, i, u):
        r1, r2 = self.roots[i]
        s = 1 + u
        return s ** r1, s ** r2, s ** (r1 - 1) * r1, s ** (r2 - 1) * r2

    def jac(self, i, u, up):
        f, g, fp, gp = self.basis(i, u)
        f0, g0, fp0, gp0 = self.basis(i, up)
        w = f0 * gp0 - fp0 * g0
        return ((g * f0 - f * g0) / w, (gp * f0 - fp * g0) / w,
                (f * gp0 - g * fp0) / w, (fp * gp0 - gp * fp0) / w)

    def rmaps(self, u, up):
        j0, j1 = self.jac(0, u, up), self.jac(1, u, up)
        return [mm(mm(ROT, [[j0[i], 0], [0, j1[i]]]), tp(ROT)) for i in range(4)]

    def h(self, u):
        return mm(mm(ROT, [[-self.cs[0] / (1 + u) ** 2, 0], [0, -self.cs[1] / (1 + u) ** 2]]), tp(ROT))

    def congruence(self, u):
        A, Ap, K, Kp = self.rmaps(u, F(0))
        return madd(K, mm(A, B0PW)), madd(Kp, mm(Ap, B0PW))


CURVED = Model(((2, -1), (3, -2)))
FLAT = Model(((1, 0), (1, 0)))
PAIRS = ((F(1, 2), F(-1, 3), (F(0), F(0))), (F(1, 5), F(3, 4), (F(1), F(-2))),
         (F(-1, 4), F(2, 3), (F(-3, 2), F(1, 2))))


def maps_dual(md, u0, up):
    A, Ap, K, Kp = md.rmaps(u0, up)
    h = md.h(u0)
    du = Ser.var(2)
    lift = lambda X, Xd: [[Ser.c(X[i][j]) + du * Xd[i][j] for j in range(2)] for i in range(2)]
    neg = lambda X: [[-x for x in row] for row in X]
    return lift(A, Ap), lift(Ap, neg(mm(h, A))), lift(K, Kp), lift(Kp, neg(mm(h, K)))


OMEGA_SCALE = F(1)   # Omega(d_u) = OMEGA_SCALE (h x)_i e_i ^ K, i.e. (1/2) dH/dx_i e_i ^ K


def omega_u(hx, scale=None):
    sc = OMEGA_SCALE if scale is None else scale
    return [hx[0] * sc, hx[1] * sc]


def synge_and_transport(md, u0, up, X1, X2, V, xq, vq, scale=None):
    A, Ap, K, Kp = maps_dual(md, u0, up)
    dU = Ser.var(2, u0 - up)
    w = mvec(minv(A), [X1 - (K[0][0] * xq[0] + K[0][1] * xq[1]), X2 - (K[1][0] * xq[0] + K[1][1] * xq[1])])
    t = [Kp[i][0] * xq[0] + Kp[i][1] * xq[1] + Ap[i][0] * w[0] + Ap[i][1] * w[1] for i in range(2)]
    sigma = dU * (V - vq) - dU * F(1, 2) * (X1 * t[0] + X2 * t[1] - xq[0] * w[0] - xq[1] * w[1])
    # R = 1 - (1/2) int Omega(gamma') with Omega(d_u) = omega_u(h x) and int h x du = -(t - w) along the
    # geodesic; the null rotations e_i ^ K commute and square to zero, so R = 1 + (1/2) sum c_i (t_i - w_i) e_i ^ K
    cvec = omega_u([t[0] - w[0], t[1] - w[1]], scale)
    R = CS.mv(GA.sc(1))
    for i in range(2):
        R = R + CS.mv(EK[i], cvec[i] * F(1, 2))
    return sigma, R


def plane_wave_numerator(md, u0, up, yp, mutate=None):
    J, Jp = md.congruence(u0)
    Jq, Jqp = md.congruence(up)
    eta = [Ser.var(0), Ser.var(1)]
    y = [yp[0] + eta[0], yp[1] + eta[1]]
    xperp = mvec(J, y)
    S = mm(tp(J), Jp)
    v = (y[0] * mvec(S, y)[0] + y[1] * mvec(S, y)[1]) * F(1, 2)
    xq = mvec(Jq, list(yp))
    Sq = mm(tp(Jq), Jqp)
    vq = (yp[0] * mvec(Sq, list(yp))[0] + yp[1] * mvec(Sq, list(yp))[1]) / 2
    scale = -OMEGA_SCALE if mutate == 'flipped connection' else None
    sigma, R = synge_and_transport(md, u0, up, xperp[0] + Ser.var(4), xperp[1] + Ser.var(5), v + Ser.var(3), xq, vq,
                                   scale=scale)
    if mutate == 'no transport':
        R = CS.mv(GA.sc(1))
    nd = lambda s: s.nodual()
    sig0 = sigma.nodual()
    ds = [sigma.dual(j).nodual() for j in (2, 3, 4, 5)]
    R0 = R.map(nd)
    dR = [R.map(lambda s, j=j: s.dual(j).nodual()) for j in (2, 3, 4, 5)]
    h = md.h(u0)
    hx = mvec(h, xperp)
    H = xperp[0] * hx[0] + xperp[1] * hx[1]
    om = omega_u(hx, scale)
    Om_u = CS.mv(EK[0], om[0]) + CS.mv(EK[1], om[1])          # Omega(d_u) = (1/2) dH/dx_i e_i ^ K
    gu, gv = CS.mv(KK), CS.mv(MM) - CS.mv(KK, H * F(1, 2))      # reciprocal frame hb(e^mu)
    gi = [CS.mv(GA.neg(E[1])), CS.mv(GA.neg(E[2]))]
    A, Ap = md.rmaps(u0, up)[0], md.rmaps(u0, up)[1]
    dlogD = 2 / (u0 - up) - sum(minv(A)[i][j] * Ap[j][i] for i in range(2) for j in range(2))
    if mutate == 'doubled d log Delta':
        dlogD = 2 * dlogD
    DR = gu * (dR[0] + Om_u * R0 * F(1, 2)) + gv * dR[1] + gi[0] * dR[2] + gi[1] * dR[3]
    DU = gu * R0 * (dlogD / 2) + DR
    grad = gu * ds[0] + gv * ds[1] + gi[0] * ds[2] + gi[1] * ds[3]
    vel = mvec(Jp, y)
    lamx = CS.mv(KK) * (CS.mv(MM) + CS.mv(E[1], vel[0]) + CS.mv(E[2], vel[1])) * F(1, 2)
    if mutate == 'frozen Lambda':
        lamx = CS.mv(lamx.at(Z6))
    vq_ = mvec(Jqp, list(yp))
    lamq = GA.scal(F(1, 2), mulv(KK, GA.add(MM, GA.scal(vq_[0], E[1]), GA.scal(vq_[1], E[2]))))
    e0lqd = CS.mv(mulv(E[0], mulv(mulv(E[0], GA.reverse(lamq)), E[0])))   # e0 Lambda(x')^dagger
    N = lamx * (DU * sig0 - grad * R0) * e0lqd
    return N, sig0, lamx, grad, R0, e0lqd


# ------------------------------------------------------------------ checks
def check_projector_keeps_only_the_screen_null_components():
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    premise("synthesis.imported-gtg-dictionary")
    k, n, f, frec, lam = KV, NV, FV, FREC, LAM
    sand = lambda X: mulv(lam, mulv(X, mulv(E[0], lam)))
    ok = GA.is_zero(mulv(lam, k)) and GA.is_zero(sand(GA.sc(1)))        # Lambda k = 0; Lambda e0 Lambda = 0
    for c in range(2):
        ok &= GA.is_zero(sand(frec[c]))                                  # Lambda f e0 Lambda = 0
        for Bv in (wedge(f[0], f[1]), wedge(f[0], k), wedge(f[1], k), wedge(k, n)):
            ok &= GA.is_zero(sand(mulv(frec[c], Bv)))                    # only f^n components survive
        for w in (GA.add(GA.scal(F(2, 3), f[0]), GA.scal(F(-5), f[1])), f[1]):
            ok &= GA.eq(sand(mulv(frec[c], wedge(w, n))), mulv(mulv(frec[c], w), lam))
    for p in (GA.add(GA.scal(F(3), E[0]), E[1], GA.scal(F(-2), E[3])), GA.add(GA.scal(F(1, 2), E[2]), E[3])):
        ok &= GA.eq(sand(p), GA.scal(GA.dot(p, k, S4), lam))             # Lambda p e0 Lambda = (p.k) Lambda
    # f^c (B f_c) Lambda: trace for symmetric B, a nonzero f1 f2 part for antisymmetric B
    for Bm, sym in ((((F(1, 3), F(2, 7)), (F(2, 7), F(-5, 4))), True), (((F(0), F(1)), (F(-1), F(0))), False)):
        X = GA.add(*[mulv(frec[c], GA.add(*[GA.scal(Bm[d][c], f[d]) for d in range(2)])) for c in range(2)])
        tr = Bm[0][0] + Bm[1][1]
        ok &= GA.eq(mulv(X, lam), GA.scal(tr, lam)) == sym
    GA.check("Lambda f^c (.) e0 Lambda keeps only the f^n components; Lambda k = 0, Lambda e0 Lambda = 0, Lambda f e0 Lambda = 0", ok)
    return ok


def check_log_coefficient_formula_on_generic_jets():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    vals = []
    for variant in (0, 1):
        data = jet_data(variant)
        for u0 in (F(1, 2), F(-2, 3)):
            N0, N1, tr, pred, Mok = generic_jets(u0, data)
            ok &= N0 == {} and N1 == [{}, {}] and Mok and GA.eq(tr, pred) and tr != {}
            vals.append(tr.get((), F(0)))
        for mut in ('antisymmetric B', 'no connection'):
            N0, N1, tr, pred, Mok = generic_jets(F(1, 2), data, mutate=mut)
            ok &= not GA.eq(tr, pred)
    ok &= vals[0] == F(504887, 2226240)
    GA.check("generic jets: no degree -4, -3 parts; log(eps) coefficient = 2 pi (d_u + theta/2)(Delta^(1/2)/sqrt det M) Lambda", ok)
    return ok


def check_log_coefficient_vanishes_by_the_van_vleck_identity():
    premise("synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for md in (CURVED, FLAT):
        for u0, up, yp in PAIRS:
            # Delta = du^2/det A; M = du J(u')^T A^-1 J(u); theta = tr(J' J^-1) at u
            A, Ap = md.rmaps(u0, up)[0], md.rmaps(u0, up)[1]
            J, Jp = md.congruence(u0)
            Jq = md.congruence(up)[0]
            du = u0 - up
            M = [[du * x for x in row] for row in mm(mm(tp(Jq), minv(A)), J)]
            # d_u M = Jq^T [A^-1 J - du A^-1 A' A^-1 J + du A^-1 J']
            Ai = minv(A)
            Mp = mm(tp(Jq), madd(madd(mm(Ai, J), [[-du * x for x in row] for row in mm(mm(mm(Ai, Ap), Ai), J)]),
                                 [[du * x for x in row] for row in mm(Ai, Jp)]))
            dlogD = 2 / du - sum(Ai[i][j] * Ap[j][i] for i in range(2) for j in range(2))
            trMiMp = sum(minv(M)[i][j] * Mp[j][i] for i in range(2) for j in range(2))
            B = mm(Jp, minv(J))
            theta = B[0][0] + B[1][1]
            ok &= dlogD - trMiMp + theta == 0 and theta != 0
            ok &= B[0][1] == B[1][0]                       # twist-free: B self-adjoint
    GA.check("the bracket vanishes: d_u log(Delta/det M) + theta(u) = 0, so the log(eps) coefficient is zero", ok)
    return ok


def check_first_principles_plane_wave_kernel():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for u0, up, yp in PAIRS:
        N, sig0, lamx, grad, R0, e0l = plane_wave_numerator(CURVED, u0, up, yp)
        N0, N1, tr, M = quad_parts(N, sig0)
        ok &= N0 == {} and N1 == [{}, {}] and tr == {}
        ok &= N.at((2, 0, 0, 0, 0, 0)) != {}                     # the degree -2 part itself is nonzero
        ok &= sig0.val() == 0 and sig0.coef((1, 0, 0, 0, 0, 0)) == 0 and sig0.coef((0, 1, 0, 0, 0, 0)) == 0
    for mut in ('frozen Lambda', 'doubled d log Delta', 'no transport', 'flipped connection'):
        N, sig0 = plane_wave_numerator(CURVED, PAIRS[1][0], PAIRS[1][1], PAIRS[1][2], mutate=mut)[:2]
        N0, N1, tr, M = quad_parts(N, sig0)
        ok &= not (N0 == {} and N1 == [{}, {}] and tr == {})
    GA.check("plane wave (Weyl and Ricci nonzero, non-commuting maps): no degree -4, -3 parts and zero log(eps) coefficient", ok)
    return ok


def check_flat_field_shearing_hypersurface():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    ok = True
    for u0, up, yp in PAIRS:
        N, sig0 = plane_wave_numerator(FLAT, u0, up, yp)[:2]
        N0, N1, tr, M = quad_parts(N, sig0)
        ok &= N0 == {} and N1 == [{}, {}] and tr == {}
        J, Jp = FLAT.congruence(u0)
        B = mm(Jp, minv(J))
        ok &= B[0][0] + B[1][1] != 0 and B[0][0] != B[1][1]   # expansion and shear nonzero
    N, sig0 = plane_wave_numerator(FLAT, PAIRS[2][0], PAIRS[2][1], PAIRS[2][2], mutate='frozen Lambda')[:2]
    ok &= quad_parts(N, sig0)[2] != {}
    GA.check("flat field, expanding and shearing null hypersurface: zero log(eps) coefficient (the -pi theta log term cancels)", ok)
    return ok


def check_model_transport_rotor_and_connection():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    md = CURVED
    pts = (((F(1, 3), F(2), F(1, 2), F(-1)), (F(-1, 4), F(1, 5), F(3), F(2, 7))),
           ((F(1, 2), F(-1), F(1, 3), F(1, 9)), (F(-1, 5), F(0), F(-2), F(1))))
    for x, xq in pts:
        u0, v0, a1, a2 = x
        sigma, R = synge_and_transport(md, u0, xq[0], Ser.c(a1) + Ser.var(4), Ser.c(a2) + Ser.var(5),
                                       Ser.c(v0) + Ser.var(3), [xq[2], xq[3]], xq[1])
        ds = [sigma.dual(j).val() for j in (2, 3, 4, 5)]
        h = md.h(u0)
        hx = mvec(h, [a1, a2])
        H = a1 * hx[0] + a2 * hx[1]
        T = [ds[1], ds[0] - H * ds[1], -ds[2], -ds[3]]          # geodesic tangent g^-1 d sigma at x
        om = omega_u(hx)
        Om = GA.add(GA.scal(om[0], EK[0]), GA.scal(om[1], EK[1]))
        R0 = {b: s.val() for b, s in R.d.items() if s.val() != 0}
        dR = [{b: s.dual(j).val() for b, s in R.d.items() if s.dual(j).val() != 0} for j in (2, 3, 4, 5)]
        res = GA.add(GA.scal(T[0], GA.add(dR[0], GA.scal(F(1, 2), mulv(Om, R0)))),
                     GA.scal(T[1], dR[1]), GA.scal(T[2], dR[2]), GA.scal(T[3], dR[3]))
        ok &= GA.is_zero(res) and len(R0) > 1                    # D_T R = 0: spin transport along the geodesic
        ok &= GA.eq(mulv(R0, GA.reverse(R0)), GA.sc(1))
        # Omega(e_mu).g_nu = Gamma^rho_{mu nu} g_rho - d_mu g_nu for the Kerr-Schild frame
        Hu, Hi = -2 * H / (1 + u0), [2 * hx[0], 2 * hx[1]]
        g = [GA.add(MM, GA.scal(H / 2, KK)), KK, E[1], E[2]]
        dg = {0: GA.scal(Hu / 2, KK), 2: GA.scal(Hi[0] / 2, KK), 3: GA.scal(Hi[1] / 2, KK)}
        Gam = {(1, 0, 0): Hu / 2}
        for i in range(2):
            Gam[(1, 0, 2 + i)] = Gam[(1, 2 + i, 0)] = Gam[(2 + i, 0, 0)] = Hi[i] / 2
        Oms = [Om, {}, {}, {}]
        for mu in range(4):
            for nu in range(4):
                lhs = GA.scal(F(1, 2), GA.sub(mulv(Oms[mu], g[nu]), mulv(g[nu], Oms[mu])))
                rhs = GA.add(*[GA.scal(Gam.get((r, mu, nu), F(0)), g[r]) for r in range(4)])
                if nu == 0:
                    rhs = GA.sub(rhs, dg.get(mu, {}))
                ok &= GA.eq(lhs, rhs)
    GA.check("model: R = 1 + (1/2)(t - w).e ^ K is the spin transport (D_T R = 0) and Omega matches its coordinate reading (Christoffel symbols)", ok)
    return ok


def check_mass_and_log_terms_are_below_the_log_order():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard")
    ok = True
    for u0, up, yp in PAIRS:
        N, sig0, lamx, grad, R0, e0l = plane_wave_numerator(CURVED, u0, up, yp)
        mass = lamx * R0 * e0l                                   # m U/sigma: numerator O(eta), degree >= -1
        ok &= mass.at(Z6) == {} and mass.at((1, 0, 0, 0, 0, 0)) != {}
        lg = lamx * grad                                         # V d log sigma: Lambda grad sigma = O(eta)
        ok &= lg.at(Z6) == {} and lg.at((0, 1, 0, 0, 0, 0)) != {}
    GA.check("mass term and V log sigma: Lambda U e0 Lambda'^dagger and Lambda grad sigma vanish on the generator (degree >= -1)", ok)
    return ok


def check_regularised_model_integrals():
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    ok = True
    # in zeta = L eta (L^T L = M): tr(M^-1 X) = tr(L^-T X L^-1), the zeta-trace that weights log(eps)
    L = [[F(2), F(1, 3)], [F(0), F(3, 2)]]
    M = mm(tp(L), L)
    X = [[F(5), F(-1, 2)], [F(-1, 2), F(1, 7)]]
    Y = mm(mm(tp(minv(L)), X), minv(L))
    trw = sum(minv(M)[i][j] * X[j][i] for i in range(2) for j in range(2))
    ok &= trw == Y[0][0] + Y[1][1] and trw == F(3287, 2268)
    # radial integrands, q = |zeta|^2/2, c = i eps s - eps^2/2 (any c off [0, inf)):
    # q/(q - c)^2 - 1/(q - c) = c/(q - c)^2 = d/dq[-c/(q - c)]: the two log weights agree, no log in the difference;
    # 1/(q - c)^2 = d/dq[-1/(q - c)], integral over [0, inf) is -1/c: the i0 term, eps-independent ratio s'/s
    # (real negative c stands in for the complex one: the identities are rational in c)
    pinned = ((F(-3, 49), F(9, 49)), (F(-490, 1369), F(196, 1369)), (F(-100, 90601), F(10000, 90601)))
    for (c, q), (pl, pi) in zip(((F(-1, 3), F(2)), (F(-5, 2), F(1, 7)), (F(-1, 100), F(3))), pinned):
        lhs = q / (q - c) ** 2 - 1 / (q - c)
        ok &= lhs == c / (q - c) ** 2 and lhs == pl and 1 / (q - c) ** 2 == pi
        Q = Ser.var(2, q)                                        # dual number: exact first derivative
        ok &= ((Q - c).inv() * (-c)).dual(2).val() == lhs
        ok &= ((Q - c).inv() * (-1)).dual(2).val() == 1 / (q - c) ** 2
        ok &= (0 - (-1 / (0 - c))) == -1 / c                     # [-1/(q - c)] from 0 to infinity
    # the log weights themselves: int_0^R q dq/(q - c)^2 and int_0^R dq/(q - c) both grow as log R; the
    # first minus the second equals -c/(R - c) + 1 = c/(q-c) primitive difference, bounded uniformly in c
    diffs = []
    for c in (F(-1, 3), F(-1, 10 ** 6)):
        for R in (F(10), F(10 ** 6)):
            diffs.append((-c / (R - c)) - (-c / (0 - c)))
    ok &= all(abs(x) <= 1 for x in diffs) and diffs[0] == F(-30, 31) and diffs[3] == F(-10 ** 12, 10 ** 12 + 1)
    GA.check("model integrals: log weights of eta eta/sigma^2 and 1/sigma agree (difference log-free); i0 integral is -1/c", ok)
    return ok


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("check_"):
            print(name, fn())
