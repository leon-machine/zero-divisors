"""synthesis.charged-vaidya-cauchy-horizon-tractor-threshold: exact checks.

Derived metric (signature (1,3), coordinates (v, r, x, y), stereographic sphere)
    g = f dv^2 - 2 dv dr - r^2 q (dx^2 + dy^2),  q = 4 / (1 + x^2 + y^2)^2,
    f = 1 - 2 m(v)/r + e2/r^2 - L r^2/3,
the charged Vaidya(-de Sitter) field with ingoing null dust of mass function m(v) (e2 = e^2, L = Lambda).
Curvature is computed exactly at rational points from second-order Taylor jets (m given by its jet
m0 + m1 dv + m2 dv^2/2), with the formula convention of the stored plane-wave check
(R^a_bcd = d_c G^a_db - d_d G^a_cb + G^a_ce G^e_db - G^a_de G^e_cb, Ric_bd = R^a_bad) and the store sign
Ric_store = -Ric_formula (calibrated in check_store_sign: Ric_store = L g on de Sitter).

  check_store_sign:       m = e = 0: Ric_store = L g at three points and two values of L.
  check_vaidya_schouten:  P_store = (L/6) g - (m'/r^2) dv dv + (e2/(2 r^4)) (-h2 + hS) exactly, R_store = 4L,
                          at four points / jets (h2 = (v,r) block of g, hS = sphere block).
  check_crossing_ray:     xi = d_v + (f/2) d_r is null; the outgoing radial null geodesic k = w xi obeys
                          w'/w = -f_r/2 (Gamma^v(xi,xi) = f_r/2) with the r-equation then satisfied; n = dv/w is
                          parallel along k and n(k) = 1; k^flat is parallel; P(k, .) = S n + c k^flat with
                          S = -(m'/r^2) w^2 and c = L/6 - e2/(2 r^4); P(k, e_x) = P(k, e_y) = 0.
  check_inner_horizon:    RN (m = 5/4, e2 = 1: r_- = 1/2, r_+ = 2) and RNdS (L = 3/25, m = 6/5, e2 = 36/25, kappa_- = 7/25:
                          roots 1, 2, 3, -6): f(r_-) = 0, kappa_- := -f_r(r_-)/2 > 0 equals (r_+ - r_-)/(2 r_-^2)
                          for RN; the outgoing-ray flow r' = f/2 has derivative -kappa_- at r_- (attracting).
  check_threshold_bookkeeping: in units with kappa_- = kappa and the model w = exp(kappa v):
                          for m' = exp(-2 alpha v) the L^1 integrand m' w is exp((kappa - 2 alpha) v) and the
                          Tipler integrand (lambda_c - lambda) w m' equals m'/kappa exactly; in affine distance
                          t = exp(-kappa v)/kappa, |S| = m' w^2 r^-2 is a constant times t^(2 beta - 2) with
                          beta = alpha/kappa; tail integrals int_V^oo are finite exactly when 2 alpha > kappa.
"""
from fractions import Fraction as F
import itertools
import GA
from tp_premise import premise

NV = 4
ORDER = 2
ZERO_E = (0,) * NV


class J(object):
    """Taylor jet of total order <= 2 in four variables, exact coefficients."""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {k: v for k, v in (c or {}).items() if v != 0}

    @staticmethod
    def const(a):
        return J({ZERO_E: F(a)})

    @staticmethod
    def coord(i, base):
        e = [0] * NV
        e[i] = 1
        return J({ZERO_E: F(base), tuple(e): F(1)})

    def _lift(self, o):
        return o if isinstance(o, J) else J.const(o)

    def __add__(self, o):
        o = self._lift(o)
        d = dict(self.c)
        for k, v in o.c.items():
            d[k] = d.get(k, F(0)) + v
        return J(d)

    __radd__ = __add__

    def __neg__(self):
        return J({k: -v for k, v in self.c.items()})

    def __sub__(self, o):
        return self + (-self._lift(o))

    def __rsub__(self, o):
        return self._lift(o) - self

    def __mul__(self, o):
        o = self._lift(o)
        d = {}
        for k1, v1 in self.c.items():
            for k2, v2 in o.c.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                if sum(k) <= ORDER:
                    d[k] = d.get(k, F(0)) + v1 * v2
        return J(d)

    __rmul__ = __mul__

    def c0(self):
        return self.c.get(ZERO_E, F(0))

    def inv(self):
        a0 = self.c0()
        assert a0 != 0
        h = (self - a0) * (F(1) / a0)
        out = J.const(1)
        p = J.const(1)
        for _ in range(ORDER):
            p = p * (-h)
            out = out + p
        return out * (F(1) / a0)

    def over(self, o):
        return self * self._lift(o).inv()

    def d(self, i):
        d = {}
        for k, v in self.c.items():
            if k[i] > 0:
                kk = list(k)
                kk[i] -= 1
                d[tuple(kk)] = d.get(tuple(kk), F(0)) + v * k[i]
        return J(d)

    def lower(self):
        return J({k: v for k, v in self.c.items() if sum(k) < ORDER})


def mat_inv(M):
    n = len(M)
    A = [[M[i][j] for j in range(n)] + [J.const(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c].c0() != 0)
        A[c], A[p] = A[p], A[c]
        piv = A[c][c].inv()
        A[c] = [x * piv for x in A[c]]
        for i in range(n):
            if i != c and A[i][c].c:
                fct = A[i][c]
                A[i] = [x - fct * y for x, y in zip(A[i], A[c])]
    return [row[n:] for row in A]


def curvature(g):
    n = NV
    ginv = mat_inv(g)
    dg = [[[g[i][j].d(k) for k in range(n)] for j in range(n)] for i in range(n)]
    Gam = [[[None] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = J()
                for d in range(n):
                    s = s + ginv[a][d] * (dg[d][c][b] + dg[d][b][c] - dg[b][c][d])
                Gam[a][b][c] = (s * F(1, 2)).lower()
    Riem = {}
    for a, b, c, d in itertools.product(range(n), repeat=4):
        s = Gam[a][d][b].d(c).c0() - Gam[a][c][b].d(d).c0()
        for e in range(n):
            s += Gam[a][c][e].c0() * Gam[e][d][b].c0() - Gam[a][d][e].c0() * Gam[e][c][b].c0()
        Riem[(a, b, c, d)] = s
    Ric = [[sum(Riem[(a, b, a, d)] for a in range(n)) for d in range(n)] for b in range(n)]
    g0inv = [[ginv[i][j].c0() for j in range(n)] for i in range(n)]
    G0 = [[[Gam[a][b][c].c0() for c in range(n)] for b in range(n)] for a in range(n)]
    return g0inv, G0, Ric


def vaidya(pt, mj, e2, L):
    v0, r0, x0, y0 = pt
    v = J.coord(0, v0)
    r = J.coord(1, r0)
    x = J.coord(2, x0)
    y = J.coord(3, y0)
    dv = v - v0
    m = J.const(mj[0]) + dv * mj[1] + dv * dv * (F(mj[2]) * F(1, 2))
    f = 1 - (2 * m).over(r) + J.const(e2).over(r * r) - r * r * (F(L) * F(1, 3))
    s = 1 + x * x + y * y
    q = J.const(4).over(s * s)
    z = J()
    g = [[f, J.const(-1), z, z], [J.const(-1), z, z, z], [z, z, -(r * r * q), z], [z, z, z, -(r * r * q)]]
    return g, f


def store_schouten(g):
    g0inv, G0, Ric = curvature(g)
    Rs = [[-Ric[i][j] for j in range(NV)] for i in range(NV)]
    g0 = [[g[i][j].c0() for j in range(NV)] for i in range(NV)]
    R = sum(g0inv[i][j] * Rs[i][j] for i in range(NV) for j in range(NV))
    P = [[(Rs[i][j] - R * g0[i][j] * F(1, 6)) * F(1, 2) for j in range(NV)] for i in range(NV)]
    return P, R, Rs, g0, G0


POINTS = [((F(1, 3), F(3, 2), F(1, 5), F(-2, 7)), (F(5, 4), F(2, 9), F(-1, 3)), F(1), F(3, 25)),
          ((F(2), F(3, 4), F(0), F(1, 2)), (F(6, 5), F(1, 7), F(4)), F(36, 25), F(3, 25)),
          ((F(-1, 2), F(5, 7), F(3, 4), F(1, 3)), (F(5, 4), F(3), F(-2)), F(1), F(0)),
          ((F(7), F(2, 5), F(-1), F(-1)), (F(1), F(1, 11), F(1, 2)), F(1, 4), F(-1, 3))]


def check_store_sign():
    premise("interior.imported-tractor-connection")
    # tabulated store-sign values Ric_vv = L f = L (1 - L r^2/3) and Ric_xx = -L r^2 q at the sample points
    table = {(F(3), F(1, 2)): (F(9, 4), F(-3)), (F(3), F(1, 4)): (F(45, 16), F(-1500625, 2517168)),
             (F(3), F(1, 7)): (F(144, 49), F(-1, 147)), (F(3, 25), F(1, 2)): (F(297, 2500), F(-3, 25)),
             (F(3, 25), F(1, 4)): (F(1197, 10000), F(-60025, 2517168)),
             (F(3, 25), F(1, 7)): (F(3672, 30625), F(-1, 3675))}
    for L in (F(3), F(3, 25)):
        for pt in ((F(0), F(1, 2), F(0), F(0)), (F(1, 3), F(1, 4), F(1, 5), F(-2, 7)), (F(2), F(1, 7), F(1), F(2))):
            g, _ = vaidya(pt, (F(0), F(0), F(0)), F(0), L)
            P, R, Rs, g0, _ = store_schouten(g)
            for i in range(NV):
                for j in range(NV):
                    assert Rs[i][j] == L * g0[i][j]
            assert R == 4 * L
            assert (Rs[0][0], Rs[2][2]) == table[(L, pt[1])]
            # the formula convention itself gives the opposite sign (Ric_formula = -L g)
            assert -Rs[0][0] == -L * g0[0][0]
    # control: a nonzero m' breaks Ric = L g
    g, _ = vaidya((F(0), F(1, 2), F(0), F(0)), (F(0), F(1), F(0)), F(0), F(3))
    P, R, Rs, g0, _ = store_schouten(g)
    assert Rs[0][0] != F(3) * g0[0][0]
    return True


def check_vaidya_schouten():
    premise("interior.imported-tractor-connection")
    premise("synthesis.tractor-transport-weak-null-crossing")
    for pt, mj, e2, L in POINTS:
        g, f = vaidya(pt, mj, e2, L)
        P, R, Rs, g0, _ = store_schouten(g)
        r0 = pt[1]
        assert R == 4 * L
        h2 = [[g0[i][j] if (i < 2 and j < 2) else F(0) for j in range(NV)] for i in range(NV)]
        hS = [[g0[i][j] if (i >= 2 and j >= 2) else F(0) for j in range(NV)] for i in range(NV)]
        for i in range(NV):
            for j in range(NV):
                dust = -mj[1] / (r0 * r0) if (i, j) == (0, 0) else F(0)
                maxw = e2 / (2 * r0 ** 4) * (-h2[i][j] + hS[i][j])
                assert P[i][j] == L * F(1, 6) * g0[i][j] + dust + maxw
    return True


def check_crossing_ray():
    premise("interior.imported-tractor-connection")
    premise("synthesis.tractor-transport-weak-null-crossing")
    for pt, mj, e2, L in POINTS:
        g, f = vaidya(pt, mj, e2, L)
        P, R, Rs, g0, G0 = store_schouten(g)
        r0 = pt[1]
        f0, fv, fr = f.c0(), f.d(0).c0(), f.d(1).c0()
        xi = [F(1), f0 * F(1, 2), F(0), F(0)]
        assert sum(g0[a][b] * xi[a] * xi[b] for a in range(NV) for b in range(NV)) == 0     # null

        def Gxx(a):
            return sum(G0[a][b][c] * xi[b] * xi[c] for b in range(NV) for c in range(NV))
        assert Gxx(0) == fr * F(1, 2)
        lw = -Gxx(0)                                                    # w'/w along the ray (d/dv)
        # r-equation: d(w f/2)/dlambda + Gamma^r(k,k) = 0, divided by w^2, with d f/dv = f_v + f_r f/2
        assert lw * f0 * F(1, 2) + (fv + fr * f0 * F(1, 2)) * F(1, 2) + Gxx(1) == 0
        assert Gxx(2) == 0 and Gxx(3) == 0
        for w in (F(1), F(7, 3), F(40)):
            k = [w * c for c in xi]
            # n = dv / w is parallel: (nabla_k n)_a = k(1/w) delta_a^v - Gamma^v_{ba} k^b / w, k(1/w) = -lw
            for a in range(NV):
                assert -lw * (1 if a == 0 else 0) - sum(G0[0][b][a] * xi[b] for b in range(NV)) == 0
            n = [F(1) / w, F(0), F(0), F(0)]
            assert sum(n[a] * k[a] for a in range(NV)) == 1                                      # nu = 1
            kflat = [sum(g0[a][b] * k[b] for b in range(NV)) for a in range(NV)]
            # k^flat parallel: d/dlambda (k_a) - Gamma^c_{ba} k^b k_c, with k_a = w * xi_a(v, r):
            # d/dlambda xi_v = w (d/dv along ray of f/2) = w (fv + fr f/2)/2 ; xi_r = -1 constant
            xflat = [sum(g0[a][b] * xi[b] for b in range(NV)) for a in range(NV)]
            assert xflat == [f0 * F(1, 2), F(-1), F(0), F(0)]
            dxi = [(fv + fr * f0 * F(1, 2)) * F(1, 2), F(0), F(0), F(0)]
            for a in range(NV):
                lhs = lw * xflat[a] + dxi[a] - sum(G0[c][b][a] * xi[b] * xflat[c] for b in range(NV) for c in range(NV))
                assert lhs == 0
            Pk = [sum(P[a][b] * k[b] for b in range(NV)) for a in range(NV)]
            S = -mj[1] / (r0 * r0) * w * w
            c = L * F(1, 6) - e2 / (2 * r0 ** 4)
            assert Pk == [S * n[a] + c * kflat[a] for a in range(NV)]
            assert Pk[2] == 0 and Pk[3] == 0
    return True


def check_inner_horizon():
    premise("synthesis.tractor-transport-weak-null-crossing")
    # f as a Laurent polynomial in r: coefficients of r^-2, r^-1, r^0, r^2
    def fpoly(m, e2, L):
        return {-2: F(e2), -1: -2 * F(m), 0: F(1), 2: -F(L) * F(1, 3)}

    def ev(p, r):
        return sum(c * F(r) ** e for e, c in p.items())

    def dr(p):
        return {e - 1: c * e for e, c in p.items() if e != 0}
    rn = fpoly(F(5, 4), F(1), F(0))
    assert ev(rn, F(1, 2)) == 0 and ev(rn, F(2)) == 0
    kap = -ev(dr(rn), F(1, 2)) * F(1, 2)
    assert kap == F(3) and kap == (F(2) - F(1, 2)) / (2 * F(1, 2) ** 2)
    assert ev(rn, F(1)) < 0                                      # f < 0 between the horizons (region II)
    # outgoing-ray flow r' = f/2: derivative at r_- is f_r/2 = -kappa < 0, so r_- attracts
    assert ev(dr(rn), F(1, 2)) * F(1, 2) == -kap
    ds = fpoly(F(6, 5), F(36, 25), F(3, 25))
    for root in (F(1), F(2), F(3), F(-6)):
        assert ev(ds, root) == 0
    kap2 = -ev(dr(ds), F(1)) * F(1, 2)
    assert kap2 == F(7, 25) and kap2 > 0
    assert ev(ds, F(3, 2)) < 0                                   # region II between r_- = 1 and r_+ = 2
    return True


# generalised exponentials: dict a -> coefficient, standing for sum c exp(a v)
def ex_mul(p, q):
    out = {}
    for a1, c1 in p.items():
        for a2, c2 in q.items():
            out[a1 + a2] = out.get(a1 + a2, F(0)) + c1 * c2
    return {a: c for a, c in out.items() if c != 0}


def ex_tail(p):
    """int_V^oo of sum c exp(a v) dv, as a generalised exponential in V; None if some a >= 0 (divergent)."""
    if any(a >= 0 for a in p):
        return None
    return {a: -c / a for a, c in p.items()}


def check_threshold_bookkeeping():
    premise("synthesis.crossing-transport-tipler-threshold-sharp")
    premise("synthesis.tractor-transport-weak-null-crossing")
    for kap in (F(1), F(3), F(2, 5)):
        w = {kap: F(1)}
        winv = {-kap: F(1)}
        lam_gap = ex_tail(winv)                                 # lambda_c - lambda = int_v^oo dv/w
        assert lam_gap == {-kap: F(1) / kap}
        for alpha in (kap / 4, kap / 2, kap * F(3, 5), kap * 2):
            mp = {-2 * alpha: F(1)}
            l1 = ex_tail(ex_mul(mp, w))                          # int |S| dlambda = int m' w dv / r^2
            assert (l1 is not None) == (2 * alpha > kap)
            beta = alpha / kap
            assert (l1 is not None) == (beta > F(1, 2))
            tip = ex_mul(ex_mul(lam_gap, w), mp)                 # (lambda_c - lambda) w m'
            assert tip == {-2 * alpha: F(1) / kap}
            assert ex_tail(tip) == {-2 * alpha: 1 / (kap * 2 * alpha)}   # finite: total mass / kappa
            # |S| = m' w^2 as a power of t = exp(-kappa v)/kappa: exponent of exp(v) is kappa (2 - 2 beta)
            Sx = ex_mul(mp, ex_mul(w, w))
            (a_S, c_S), = Sx.items()
            assert a_S == -kap * (2 * beta - 2)
    return True
