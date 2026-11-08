"""neutrino.seesaw-what-gauge-invariance-proves-what: exact checks of clauses (1) to (3).

Premise (M) itself is a premise (no computable content); clause (3) is checked under it.

(1) Magnitudes. Irrationals are handled exactly: sqrt(2) through the field Q(sqrt 2) (pairs a + b r,
r^2 = 2), and every length bound by squaring both sides. From Fact mass.exact-join with
<pi pi> = 0 and C = 0, m = sqrt(2) (Lambda/6) |[omega omega]|, and |[omega omega]| = l^2 p:
  - the cosmological-to-flat ratio (Lambda/6) l^2 p / p equals 1 exactly at l^2 = 6/Lambda = 2 L_H^2
    (L_H^2 = 3/Lambda), at several Lambda;
  - with p = m, (l/L_H)^2 = sqrt(2) in Q(sqrt 2) for several (Lambda, m), so (l/L_H)^4 = 2 and
    l/L_H = 2^(1/4), in (1.189, 1.190) (fourth powers);
  - with p = 100 GeV, m = 0.05 eV and Lambda in (1.0, 1.2)e-52 m^-2, l^2 = 3 sqrt(2) (m/p)/Lambda
    lies in ((1.3e20)^2, (1.5e20)^2) m^2 (compared through 18 (m/p)^2 against (l^2 Lambda)^2);
  - the Casimir branch C = 3 m^2/Lambda at 0.05 eV (1 eV = (5.0676, 5.0678)e6 m^-1) is in
    (1.6, 2.0)e63.
(2) The bilinear census over the derived hypercharges (Q, u^c, d^c, L, e^c, N) =
(1/6, -2/3, 1/3, -1/2, 1, 0): of the 21 unordered pairs exactly one, (N, N), is neutral; L N carries
-1/2, which a condensate of hypercharge +1/2 absorbs.
(3) Block inversion: for rational m_D (2 x 2 and 3 x 3) and invertible symmetric M_R, with
y = -M_R^-1 m_D^T x found by Gaussian elimination, [[0, m_D], [m_D^T, M_R]] (x, y) =
(-m_D M_R^-1 m_D^T x, 0), and the light block is symmetric. Scalar case: the small eigenvalue mu of
[[0, m], [m, M]] is the negative root of f(mu) = mu^2 - M mu - m^2; with t = -m^2/M and
e = m^4/M^3, f(t - e) > 0 > f(t + e) and f(t) != 0 on samples with m << M, so |mu - t| < e and
mu != t; f(t + e) = -2 m^6/M^4 + m^8/M^6 identically (checked on a grid fixing the polynomial).
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

import GA
from tp_premise import premise

LAMBDAS = (F(1, 10 ** 52), F(11, 10 ** 52), F(3, 7))
MASSES = (F(5, 100), F(1, 3), F(7))
LAM_BRACKET = (F(10, 10 ** 53), F(12, 10 ** 53))       # m^-2
EV_PER_M = (F(50676, 10 ** 4) * 10 ** 6, F(50678, 10 ** 4) * 10 ** 6)
NAMES = ("Q", "u^c", "d^c", "L", "e^c", "N")
HYPER = (F(1, 6), F(-2, 3), F(1, 3), F(-1, 2), F(1), F(0))
MD2 = [[F(1), F(2)], [F(3), F(6)]]
MR2 = [[F(10) ** 3, F(7)], [F(7), F(2) * 10 ** 3]]
MD3 = [[F(1), F(2), F(-1)], [F(0), F(3), F(1, 2)], [F(2), F(-1), F(4)]]
MR3 = [[F(500), F(3), F(-1)], [F(3), F(800), F(2)], [F(-1), F(2), F(1200)]]
XS = ([F(1), F(0), F(2)], [F(2), F(-5), F(1, 3)], [F(1, 3), F(7), F(0)])
SCALARS = ((F(3), F(1000)), (F(7), F(250)), (F(1), F(10 ** 6)), (F(246), F(10) ** 12))
# the grid on which the identities for f(t + e) and f(t - e) are checked (fixes the polynomials)
GRID_M = (F(1), F(2), F(-3), F(1, 2), F(5))
GRID_MR = (F(1), F(3), F(-2), F(7, 3), F(10), F(1, 4), F(9), F(-5), F(11))


class Q2(object):
    """a + b sqrt(2) with rational a, b."""

    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)

    def __mul__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - 2 * self.b * self.b
        return Q2(self.a / n, -self.b / n)

    def __eq__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return self.a == o.a and self.b == o.b


def check_cosmological_term_magnitudes():
    premise("mass.exact-join")
    ok = True
    r2 = Q2(0, 1)
    for lam in LAMBDAS:
        LH2 = 3 / lam
        l2 = 6 / lam
        ok = ok and lam * l2 / 6 == 1 and l2 == 2 * LH2
        for m in MASSES:
            # |[omega omega]| = 6 m / (sqrt2 Lambda) = l^2 p with p = m
            ww = Q2(6 * m / lam) * r2.inv()
            l2_q = ww * Q2(1 / m)
            ratio = l2_q * Q2(1 / LH2)
            ok = ok and ratio == Q2(0, 1) and ratio * ratio == Q2(2)
            # m = sqrt2 (Lambda/6) |[ww]| recovered
            ok = ok and r2 * Q2(lam / 6) * ww == Q2(m)
    ok = ok and F(1189, 1000) ** 4 < 2 < F(1190, 1000) ** 4
    # weak-scale constituents: l^2 = 3 sqrt2 (m/p)/Lambda; l^2 > L^2 iff 18 (m/p)^2 > (L^2 Lambda)^2
    mp = F(5, 100) / 10 ** 11
    lo, hi = F(13, 10) * 10 ** 20, F(15, 10) * 10 ** 20
    ok = ok and 18 * mp * mp > (lo * lo * LAM_BRACKET[1]) ** 2
    ok = ok and 18 * mp * mp < (hi * hi * LAM_BRACKET[0]) ** 2
    # Casimir branch C = 3 m^2/Lambda, m = 0.05 eV in m^-1
    C_lo = 3 * (F(5, 100) * EV_PER_M[0]) ** 2 / LAM_BRACKET[1]
    C_hi = 3 * (F(5, 100) * EV_PER_M[1]) ** 2 / LAM_BRACKET[0]
    ok = ok and F(16, 10) * 10 ** 63 < C_lo and C_hi < 2 * 10 ** 63
    GA.check("Lambda term: ratio 1 at l = sqrt2 L_H; l/L_H = 2^(1/4); l in (1.3, 1.5)e20 m; C ~ 1e63", ok)
    return ok


def check_unique_neutral_bilinear():
    premise("neutrino.imported-derived-content-singlets")
    pairs = list(combinations_with_replacement(range(6), 2))
    neutral = [(NAMES[i], NAMES[j]) for i, j in pairs if HYPER[i] + HYPER[j] == 0]
    ok = len(pairs) == 21 and neutral == [("N", "N")]
    yLN = HYPER[3] + HYPER[5]
    ok = ok and yLN == F(-1, 2) and yLN + F(1, 2) == 0
    ok = ok and all(HYPER[i] + HYPER[j] != 0 for i, j in pairs if (i, j) != (5, 5))
    GA.check("of the 21 fermion bilinears only N N is neutral; L N carries -1/2", ok)
    return ok


def solve(M, b):
    return GA.field_solve([row[:] for row in M], list(b))


def check_block_elimination():
    premise("neutrino.m-framework-realises-majorana-term-scale")
    ok = True
    for mD, MR in ((MD2, MR2), (MD3, MR3)):
        k = len(mD)
        mDT = [[mD[j][i] for j in range(k)] for i in range(k)]
        cols = [solve(MR, [F(int(i == c)) for i in range(k)]) for c in range(k)]
        MRinv = [[cols[c][r] for c in range(k)] for r in range(k)]
        light = GA.mat_mul(GA.mat_mul(mD, MRinv), mDT)
        ok = ok and light == [[light[j][i] for j in range(k)] for i in range(k)]
        big = [[F(0)] * k + mD[i] for i in range(k)] + [mDT[i] + MR[i] for i in range(k)]
        for x in XS:
            x = x[:k]
            y = [-c for c in solve(MR, [sum(mDT[i][j] * x[j] for j in range(k)) for i in range(k)])]
            out = [sum(big[i][j] * (x + y)[j] for j in range(2 * k)) for i in range(2 * k)]
            want = [-sum(light[i][j] * x[j] for j in range(k)) for i in range(k)] + [F(0)] * k
            ok = ok and out == want
    GA.check("[[0, m_D], [m_D^T, M_R]] (x, -M_R^-1 m_D^T x) = (-m_D M_R^-1 m_D^T x, 0), light block symmetric", ok)
    return ok


def fpoly(mu, m, M):
    return mu * mu - M * mu - m * m


def check_scalar_seesaw_bound():
    premise("neutrino.m-framework-realises-majorana-term-scale")
    ok = True
    for m, M in SCALARS:
        t = -m * m / M
        e = m ** 4 / M ** 3
        ok = ok and fpoly(t - e, m, M) > 0 and fpoly(t + e, m, M) < 0
        # f(t) = m^4/M^2 + m^2 - m^2 = m^4/M^2, nonzero, so mu != t
        ok = ok and fpoly(t, m, M) == m ** 4 / M ** 2
        # the bound is sharp to a factor two: mu = t + e - 2 m^6/M^5 + ..., so f(t + e/2) > 0 and
        # |mu - t| > e/2
        ok = ok and fpoly(t + e / 2, m, M) > 0
        # both on the decreasing branch, left of the vertex M/2 (f symmetric about it): the root found
        # is the small one
        vertex = M / 2
        ok = ok and t + e < vertex and fpoly(vertex + m, m, M) == fpoly(vertex - m, m, M)
    for m in GRID_M:
        for M in GRID_MR:
            t = -m * m / M
            e = m ** 4 / M ** 3
            ok = ok and fpoly(t + e, m, M) == -2 * m ** 6 / M ** 4 + m ** 8 / M ** 6
            ok = ok and fpoly(t - e, m, M) == 2 * m ** 4 / M ** 2 + 2 * m ** 6 / M ** 4 + m ** 8 / M ** 6
    GA.check("scalar seesaw: the small eigenvalue lies within m^4/M^3 of -m^2/M and is not equal to it", ok)
    return ok
