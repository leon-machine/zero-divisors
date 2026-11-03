#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T13.py: exact-arithmetic verification of the computational identities of
"Quark and Lepton Families: Condensation, Democracy, and the Koide Relation" (Transport Papers, T13).

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rationals, Gaussian rationals, cyclotomic
rationals Q(zeta_3) and quadratic rationals Z[sqrt(2)] via small local
representations, and rational interval arithmetic for the square roots of the
measured masses.  No floating point in any check; the only floating point
is the RECORD lines of Part G, printed and not checked.  Statement tags refer to the
compiled paper.  The Wick evaluation of Theorem thm:skeleton is performed here
exactly in Q(zeta_3) at rational hyperbolic points; the scan-based clauses of
prop:classification(2)-(3) are flagged preliminary computation in the paper and
are NOT checked here, as the verification section itemises.

v1.1 (2026-09-07): Parts F and G added.  F: the 126 doublet direction of
prop:126 with the module, pairing and Yukawa forms rebuilt (the
four-programmes note's Part D, tags mapped to this paper), including the
family no-go recomputed as Fact 8.2's content.  G: the covariance argument of
prop:covariance as exact monomial identities, with the six logarithmic ratios
printed as RECORD lines (floating point, not checked).  No floating point in
any check.
v1.2 (2026-09-08): review-repair pass against T13_review_v6.md.  Part F: the
Clebsch check made sign-sensitive (exact signed sets); the grade-five label
says purity is what is tested (membership in the 126 is the imported Fact
8.5); the identity label reads w_4 chi; the up-type check tests symmetry, the
exact signed entries and the magnitude ratio; the family no-go check rebuilt
on an invertible non-symmetric F, distinguishing M_e from M_d and the 10 from
the 126; mag() returns None instead of asserting.  Part G: the weights are
computed by applying the substitution H -> kappa H (M_P, m fixed) to monomials
built from the generators, not read back from literals.  Count 72 -> 73.
"""

from fractions import Fraction as F
from itertools import permutations, combinations
from math import isqrt, comb

from fractions import Fraction
import GA as g

# ---------------------------------------------------------------------------
# small exact fields
# ---------------------------------------------------------------------------

class CY(object):
    """a + b*zeta with zeta^2 = -1 - zeta (zeta a primitive cube root)."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(s, o):
        o = o if isinstance(o, CY) else CY(o)
        return CY(s.a + o.a, s.b + o.b)

    __radd__ = __add__

    def __mul__(s, o):
        o = o if isinstance(o, CY) else CY(o)
        # (a1 + b1 z)(a2 + b2 z) = a1a2 + (a1b2 + a2b1) z + b1b2 z^2
        return CY(s.a * o.a - s.b * o.b,
                  s.a * o.b + s.b * o.a - s.b * o.b)

    __rmul__ = __mul__

    def __sub__(s, o):
        o = o if isinstance(o, CY) else CY(o)
        return CY(s.a - o.a, s.b - o.b)

    def __rsub__(s, o):
        return CY(o) - s

    def __neg__(s):
        return CY(-s.a, -s.b)

    def conj(s):
        """conj(zeta) = zeta^2 = -1 - zeta, so conj(a + b zeta) = (a - b) - b zeta."""
        return CY(s.a - s.b, -s.b)

    def re(s):
        """Real part: Re(zeta) = -1/2."""
        return s.a - s.b / 2

    def __eq__(s, o):
        o = o if isinstance(o, CY) else CY(o)
        return s.a == o.a and s.b == o.b

    def __repr__(s):
        return "CY(%s, %s)" % (s.a, s.b)


ZETA = CY(0, 1)
Z2 = ZETA * ZETA          # zeta^2 = -1 - zeta


class R2(object):
    """p + q*sqrt(2), exact."""
    __slots__ = ("p", "q")

    def __init__(self, p=0, q=0):
        self.p, self.q = F(p), F(q)

    def __add__(s, o):
        o = o if isinstance(o, R2) else R2(o)
        return R2(s.p + o.p, s.q + o.q)

    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, R2) else R2(o)
        return R2(s.p - o.p, s.q - o.q)

    def __mul__(s, o):
        o = o if isinstance(o, R2) else R2(o)
        return R2(s.p * o.p + 2 * s.q * o.q, s.p * o.q + s.q * o.p)

    __rmul__ = __mul__

    def __eq__(s, o):
        o = o if isinstance(o, R2) else R2(o)
        return s.p == o.p and s.q == o.q

    def positive(s):
        """Exact sign of p + q sqrt(2)."""
        if s.q == 0:
            return s.p > 0
        if s.p == 0:
            return s.q > 0
        if s.p > 0 and s.q > 0:
            return True
        if s.p < 0 and s.q < 0:
            return False
        # opposite signs: compare p^2 vs 2 q^2 with the sign of p
        return (s.p > 0) == (s.p * s.p > 2 * s.q * s.q)


def sqrt_bounds(m, digits=9):
    """Rational lo, hi with lo^2 <= m <= hi^2, to ~10^-digits."""
    m = F(m)
    scale = 10 ** digits
    n = m.numerator * scale * scale
    d = m.denominator
    # integer sqrt of n/d scaled: floor(sqrt(n/d)) via isqrt(n*d)/d
    lo_int = isqrt(n * d)
    lo = F(lo_int, d * scale)
    hi = F(lo_int + 1, d * scale)
    assert lo * lo <= m <= hi * hi
    return lo, hi

# ---------------------------------------------------------------------------
# Part A: faces (conj:faces, prop:identical, prop:alignment)
# ---------------------------------------------------------------------------

FACES = [frozenset(c) for c in combinations((1, 2, 3), 2)]
g.check("prop:identical: the two-element subsets of three slots number "
      "comb(3,2) = 3, computed, and every pair of faces intersects in exactly "
      "one slot",
      len(FACES) == comb(3, 2) == 3 and all(len(a & b) == 1
                              for i, a in enumerate(FACES)
                              for b in FACES[i + 1:]))

orbit = set()
for p in permutations((1, 2, 3)):
    m = dict(zip((1, 2, 3), p))
    orbit.add(frozenset(m[x] for x in FACES[0]))
g.check("prop:identical: S3 acts transitively on the faces (the orbit of one "
      "face is all three)", orbit == set(FACES))

# the democratic rank-one texture: uu^T has spectrum (3, 0, 0)
U3 = [[F(1)] * 3 for _ in range(3)]
g.check("prop:alignment(3): the democratic texture u'u'^T, u' = (1,1,1), has rank one, "
      "trace 3, and eigenvector u' with eigenvalue 3: one heavy family, two "
      "light, exactly",
      g.rank_of_vectors([r[:] for r in U3]) == 1
      and sum(U3[i][i] for i in range(3)) == 3
      and all(sum(U3[i][j] for j in range(3)) == 3 for i in range(3)))

# ---------------------------------------------------------------------------
# Part B: condensation (prop:condensation, prop:source, prop:ordered)
# ---------------------------------------------------------------------------

Lam = g.RF.var()
# the pinned bracket: with m^2 = (nu^2 + 9/4) Lambda/3 (dictionary, principal
# series) and the exact join m^2 = 2|B|^2 + Lambda C/3,
#   |B|^2 = m^2/2 - Lambda C/6 = (Lambda/6)(nu^2 + 9/4 - C)
ok = True
for nu_ in (F(7, 2), F(1000)):
    for C_ in (F(0), F(1), F(5, 3)):
        m2 = g.RF.const(nu_ * nu_ + F(9, 4)) * Lam / g.RF.const(3)
        lhs = m2 / g.RF.const(2) - Lam * g.RF.const(C_) / g.RF.const(6)
        rhs = Lam / g.RF.const(6) * g.RF.const(nu_ * nu_ + F(9, 4) - C_)
        ok = ok and lhs.eqrf(rhs)
g.check("prop:condensation: the fixed bracket |B_Lambda|^2 = m^2/2 - Lambda C/6 "
      "= (Lambda/6)(nu^2 + 9/4 - C) as an RF identity in formal Lambda at "
      "rational nu and C", ok)

# the sign of the dictionary: for w = -3/2 + i nu, -w(w+3) = nu^2 + 9/4 > 0
# while +w(w+3) is negative: m^2 = -w(w+3)H^2 is the physical sign
ok = True
for nu_ in (F(1), F(7, 2), F(10 ** 6)):
    w = g.qi(F(-3, 2), nu_)
    prod = w * (w + g.qi(3))
    minus = g.qi(-1) * prod
    ok = ok and minus == g.qi(nu_ * nu_ + F(9, 4)) and prod == g.qi(-(nu_ * nu_ + F(9, 4)))
g.check("fact:dictionary/prop:condensation: on the principal series w = -3/2 + i nu, "
      "-w(w+3) = nu^2 + 9/4 > 0 exactly and w(w+3) < 0: the dictionary's sign "
      "m^2 = -w(w+3)H^2 is the one with positive mass", ok)

# the source expansion at exact Gaussian-rational instances with rational Lam
ok = True
for lam_v in (F(3), F(1, 7)):
    for b in (g.qi(2, 1), g.qi(F(-1, 2), F(1, 3))):
        for Om in (g.qi(1, -1), g.qi(F(3), F(2))):
            B = b + g.qi(lam_v / 6) * Om
            lhs_v = g.qi(2) * B * B.conj()
            re_bOm = (b.conj() * Om + b * Om.conj())  # 2 Re(conj(b) Om)
            rhs_v = g.qi(2) * b * b.conj() \
                + g.qi(lam_v / 3) * re_bOm \
                + g.qi(lam_v * lam_v / 18) * Om * Om.conj()
            ok = ok and lhs_v == rhs_v
g.check("prop:source: the expansion 2|b + (Lambda/6)Omega|^2 = 2|b|^2 + "
      "(2Lambda/3)Re(conj(b)Omega) + (Lambda^2/18)|Omega|^2 exactly on "
      "Gaussian-rational instances (the Lambda-linear source term)", ok)

# prop:source(1): the linear term is (Lambda/3)(conj(b) Omega + b conj(Omega)),
# so its conj(b)-coefficient (the Wirtinger derivative at b = 0) is (Lambda/3) Omega:
# read off as the coefficient of conj(b) by evaluating at b and at i b
ok = True
for lam_v in (F(3), F(1, 7)):
    for Om in (g.qi(1, -1), g.qi(F(3), F(2))):
        for b in (g.qi(2, 1), g.qi(F(-1, 2), F(1, 3))):
            lin = lambda bb: g.qi(2) * (bb + g.qi(lam_v / 6) * Om) * (bb + g.qi(lam_v / 6) * Om).conj() \
                - g.qi(2) * bb * bb.conj() - g.qi(lam_v * lam_v / 18) * Om * Om.conj()
            # lin(b) = c conj(b) + conj(c) b  with c = (Lambda/3) Omega; then
            # lin(b) + i lin(i b) = 2 c conj(b)
            ib = g.qi(0, 1) * b
            two_c_bbar = lin(b) + g.qi(0, 1) * lin(ib)
            ok = ok and two_c_bbar == g.qi(2) * g.qi(lam_v / 3) * Om * b.conj()
g.check("prop:source(1): the conj(b)-coefficient of the Lambda-linear term is exactly "
      "(Lambda/3) Omega on Gaussian-rational instances: the printed Wirtinger "
      "derivative, gradient (2Lambda/3) Omega", ok)

# the thirteenth refutation: Lambda Omega_vac between H^2/M_P and H, against
# the weak scale, from the stated inputs in eV
H_eV, MP_eV, WEAK_eV = F(1, 10 ** 33), F(10 ** 28), F(10 ** 11)
lo_ratio = (H_eV * H_eV / MP_eV) / WEAK_eV
hi_ratio = H_eV / WEAK_eV
g.check("prop:alignment(1): the thirteenth refutation's window formed from the "
      "inputs H = 10^-33 eV, M_P = 10^28 eV, weak scale 10^11 eV: "
      "(H^2/M_P)/weak = 10^-105 and H/weak = 10^-44 exactly, both far below 1",
      lo_ratio == F(1, 10 ** 105) and hi_ratio == F(1, 10 ** 44) and hi_ratio < 1)

# Cabibbo: sqrt(m_d/m_s) in (0.215, 0.235), percent-level pass against 0.225
md, ms = F(470, 100), F(935, 10)
r = md / ms
g.check("prop:ordered(2): the Cabibbo square root with m_d = 4.70, m_s = 93.5 MeV (PDG 2024): "
      "0.215^2 < m_d/m_s < 0.235^2 as exact inequalities (sqrt = 0.2242 against "
      "0.225, the percent-level pass)",
      F(215, 1000) ** 2 < r < F(235, 1000) ** 2)

# ---------------------------------------------------------------------------
# Part C: the Koide numerics (prop:linearkill, prop:nullity)
# ---------------------------------------------------------------------------

hadron3 = MP_eV * MP_eV * H_eV                      # (M_P^2 H), eV^3
g.check("obs:absolute: (M_P^2 H)^{1/3} on the stated inputs lies in (4, 5) x 10^7 eV "
      "(cubes compared exactly): the pion-scale coincidence",
      F(4 * 10 ** 7) ** 3 < hadron3 < F(5 * 10 ** 7) ** 3)


# PDG 2024 charged-lepton pole masses (MeV): m_e = 0.51099895, m_mu = 105.6583755,
# m_tau = 1776.93 +/- 0.09; MT_ERR is the tau uncertainty used by obs:instrument
ME, MU, MT = F(51099895, 10 ** 8), F(1056583755, 10 ** 7), F(177693, 100)
MT_ERR = F(9, 100)
Qm = (ME ** 2 + MU ** 2 + MT ** 2) / (ME + MU + MT) ** 2
g.check("prop:linearkill: Q_m = 0.89357... exactly (bracketed in "
      "(0.893, 0.894)), refuted against the predicted 2/3 at the first decimal",
      F(893, 1000) < Qm < F(894, 1000) and Qm - F(2, 3) > F(1, 5))

# prop:linearkill: cos^2 theta_m = 1/(3 Q_m), bracketed; theta_m = 52.35 degrees follows
cos2m = 1 / (3 * Qm)
g.check("prop:linearkill: cos^2 theta_m = 1/(3 Q_m) lies in (0.37303, 0.37304), "
      "whence theta_m = 52.35 degrees (52.4 as printed)",
      F(37303, 10 ** 5) < cos2m < F(37304, 10 ** 5))

# sqrt bounds and the Koide quotient interval
bounds = [sqrt_bounds(m) for m in (ME, MU, MT)]
S_lo = sum(b[0] for b in bounds)
S_hi = sum(b[1] for b in bounds)
Msum = ME + MU + MT
Q_lo = Msum / (S_hi * S_hi)
Q_hi = Msum / (S_lo * S_lo)
g.check("prop:linearkill: Q_sqrt(m) lies in (2/3 - 1e-5, 2/3 + 1e-5) by exact "
      "rational interval arithmetic on the pole masses: the Koide relation "
      "(deviation two parts in 10^6 absolute, three relative; the certified "
      "interval is the coarser 10^-5)",
      F(2, 3) - F(1, 10 ** 5) < Q_lo and Q_hi < F(2, 3) + F(1, 10 ** 5))

# obs:instrument: dQ/Q = 2 tan(theta) dtheta, so at 45 degrees
# dtheta = (1/2)|Q - 2/3|/(2/3); bracketed from the certified Q interval
dth_lo = F(1, 2) * (F(2, 3) - Q_hi) / F(2, 3)
dth_hi = F(1, 2) * (F(2, 3) - Q_lo) / F(2, 3)
g.check("obs:instrument: the angular pin d(theta) = (1/2) dQ/Q at 45 degrees lies in "
      "(1.6, 1.7) x 10^-6 radians on the certified Q interval",
      F(16, 10 ** 7) < dth_lo and dth_hi < F(17, 10 ** 7))

# obs:instrument resolution: Q at m_tau +/- 0.09 MeV, dtheta = (1/2)(Q - 2/3)/(2/3);
# half-spread of the two endpoint offsets, bracketed in (3.7, 3.9) x 10^-6
def q_interval(mt):
    bt = sqrt_bounds(mt)
    lo = sum(b[0] for b in bounds[:2]) + bt[0]
    hi = sum(b[1] for b in bounds[:2]) + bt[1]
    tot = ME + MU + mt
    return tot / (hi * hi), tot / (lo * lo)


qp = q_interval(MT + MT_ERR)
qm = q_interval(MT - MT_ERR)
dth = lambda q: F(1, 2) * (q - F(2, 3)) / F(2, 3)
spread_lo = (dth(qp[0]) - dth(qm[1])) / 2
spread_hi = (dth(qp[1]) - dth(qm[0])) / 2
g.check("obs:instrument: the angular resolution from m_tau = 1776.93 +/- 0.09 MeV, "
      "half the spread of the endpoint offsets, lies in (3.7, 3.9) x 10^-6 radians",
      F(37, 10 ** 7) < spread_lo and spread_hi < F(39, 10 ** 7))

# rem:withdrawn: the split s^2 : |d|^2 = 941.55 : 941.55, both bracketed, equal to 1e-5
s2_lo, s2_hi = S_lo * S_lo / 3, S_hi * S_hi / 3
d2_lo, d2_hi = Msum - s2_hi, Msum - s2_lo
g.check("rem:withdrawn: s^2 and |d|^2 both lie in (941.54, 941.56) and their relative "
      "difference is below 10^-5: the 941.55 : 941.55 split",
      F(94154, 100) < s2_lo and s2_hi < F(94156, 100)
      and F(94154, 100) < d2_lo and d2_hi < F(94156, 100)
      and (s2_hi - d2_lo) / d2_lo < F(1, 10 ** 5))

# prop:chart(3): the phase delta for the labelling (tau, e, mu): tan^2 delta =
# 3 (v_mu - v_e)^2 / (2 v_tau - v_e - v_mu)^2, bracketed so that delta in (0.2215, 0.2225)
# (tan^2 0.2215 = 0.050719..., tan^2 0.2225 = 0.051189...; bracket by rationals inside)
num_lo, num_hi = 3 * (bounds[1][0] - bounds[0][1]) ** 2, 3 * (bounds[1][1] - bounds[0][0]) ** 2
den_lo = 2 * bounds[2][0] - bounds[0][1] - bounds[1][1]
den_hi = 2 * bounds[2][1] - bounds[0][0] - bounds[1][0]
t2_lo, t2_hi = num_lo / (den_hi * den_hi), num_hi / (den_lo * den_lo)
g.check("prop:chart(3): tan^2 delta for the labelling (tau, e, mu) lies in "
      "(0.05072, 0.05118), so delta lies in (0.2215, 0.2225): delta = 0.222",
      F(5072, 10 ** 5) < t2_lo and t2_hi < F(5118, 10 ** 5))

# nullity: q(v) = 2 (Sum sqrt m)^2 / 3 - Sum m, relative to |v|^2 = Sum m
q_lo = 2 * S_lo * S_lo / 3 - Msum
q_hi = 2 * S_hi * S_hi / 3 - Msum
g.check("prop:nullity: q(v) = 2s^2 - |v|^2 lies in (0, 0.02) with "
      "|q|/|v|^2 < 1e-5: the family vector is null to three parts in 10^6",
      0 < q_lo and q_hi < F(2, 100) and q_hi / Msum < F(1, 10 ** 5))

# the m_tau prediction: solve 2(s_e + s_mu + t)^2 = 3(m_e + m_mu + t^2)
# => t^2 - 4(s_e+s_mu) t + (3(m_e+m_mu) - 2(s_e+s_mu)^2)... rearranged:
# t^2 - 4 S t + 3 M - 2 S^2 = 0 with S = s_e + s_mu, M = m_e + m_mu;
# take the larger root and bracket it with the sqrt bounds
ok = True
for pick in (0, 1):
    se = bounds[0][pick]
    smu = bounds[1][pick]
    S = se + smu
    M = ME + MU
    disc = 16 * S * S - 4 * (3 * M - 2 * S * S)   # = 24 S^2 - 12 M
    dlo, dhi = sqrt_bounds(disc)
    t = (4 * S + (dlo if pick == 0 else dhi)) / 2
    mtau_pred = t * t
    ok = ok and F(17769, 10) < mtau_pred < F(17770, 10)
g.check("prop:linearkill: the Koide-predicted tau mass lies in "
      "(1776.9, 1777.0) MeV by exact interval arithmetic, against the "
      "measured 1776.93 +/- 0.09: agreement at half a standard deviation", ok)

# prop:chart(2): the bracket form C(v) = sum v_k^2 on the real lepton vector is
# the Euclidean norm, sum m_k = 1883.099, and it exceeds the Minkowski q(v) by
# 2|d|^2 > 0: the lepton vector is NOT C-null
C_lep = ME + MU + MT                       # sum v_k^2 = sum m_k exactly
g.check("prop:chart(2): on the lepton vector the bracket form C(v) = sum_k m_k "
      "= 1883.099 MeV, not zero, and C(v) - q(v) = 2|d|^2 > 0: C is Euclidean "
      "on real vectors and the lepton vector is not C-null",
      C_lep == F(188309937445, 10 ** 8) and C_lep - q_hi > F(1800))

# prop:chart(3): the Fourier ratio |Gamma|^2/a^2 = 6Q - 2 (identity in the
# masses), bracketed against 2 on the lepton data
ratio_lo, ratio_hi = 6 * Q_lo - 2, 6 * Q_hi - 2
g.check("prop:chart(3): the Fourier ratio |Gamma|^2/a^2 = 6 Q_sqrt(m) - 2 lies "
      "inside 2 +/- 10^-4 on the lepton data: Koide is |Gamma|^2 = 2a^2, "
      "the one number the parametrisation carries",
      2 - F(1, 10 ** 4) < ratio_lo and ratio_hi < 2 + F(1, 10 ** 4))

# ---------------------------------------------------------------------------
# Part D: the chart (prop:chart)
# ---------------------------------------------------------------------------

# cyclotomic checks: C(f+-) = 0, C(f+, f-) = 3, C(a f+ + b f-) = 6ab
f_plus = [CY(1), ZETA, Z2]
f_minus = [CY(1), Z2, ZETA]


def C_form(v, w=None):
    w = v if w is None else w
    tot = CY(0)
    for x, y in zip(v, w):
        tot = tot + x * y
    return tot


g.check("prop:chart(2): C(f+) = C(f-) = 0 and C(f+, f-) = 3 in exact "
      "cyclotomic arithmetic (zeta^2 + zeta + 1 = 0): the doublet is "
      "exactly a hyperbolic plane with the Fourier vectors as its null "
      "lines", C_form(f_plus) == CY(0) and C_form(f_minus) == CY(0)
      and C_form(f_plus, f_minus) == CY(3))

a_, b_ = F(2), F(-5, 3)
v_mix = [CY(a_) * x + CY(b_) * y for x, y in zip(f_plus, f_minus)]
g.check("prop:chart(2): C(a f+ + b f-) = 6ab exactly, so the null vectors of "
      "the doublet are exactly the two Fourier lines",
      C_form(v_mix) == CY(6 * a_ * b_))

# the sign twist: for a transposition of twistor labels, Omega -> -P Omega
def face_vec(arr):
    """arr: 3 rows (twistors) x 2 cols (spinor comps), QI entries."""
    def minor(i, j):
        return arr[i][0] * arr[j][1] - arr[i][1] * arr[j][0]
    return [minor(1, 2), minor(2, 0), minor(0, 1)]


arr = [[g.qi(1), g.qi(2, 1)], [g.qi(0, 1), g.qi(3)], [g.qi(2), g.qi(-1, 2)]]
sw = [arr[1], arr[0], arr[2]]       # transposition (1 2)
Om0 = face_vec(arr)
Om1 = face_vec(sw)
# under (1 2): face {2,3} <-> face {1,3}, face {1,2} fixed; sign flips all
g.check("prop:chart(1): under a transposition of twistor labels the face "
      "vector transforms as Omega -> -P Omega exactly (the 3 x sgn twist)",
      Om1[0] == g.qi(-1) * Om0[1] and Om1[1] == g.qi(-1) * Om0[0]
      and Om1[2] == g.qi(-1) * Om0[2])

# prop:chart(2): the S3-invariant symmetric tensors on family indices are
# two-dimensional: delta and the all-ones J are both invariant under every
# permutation matrix and are linearly independent
def perm_mat(p):
    return [[F(1) if p[i] == j else F(0) for j in range(3)] for i in range(3)]


def conj_by(P, X):
    Pt = [[P[j][i] for j in range(3)] for i in range(3)]
    return g.mat_mul(g.mat_mul(P, X), Pt)


DELTA = [[F(1) if i == j else F(0) for j in range(3)] for i in range(3)]
J_ALL = [[F(1)] * 3 for _ in range(3)]
ok = True
for p in permutations((0, 1, 2)):
    P = perm_mat(p)
    ok = ok and g.mat_eq(conj_by(P, DELTA), DELTA) and g.mat_eq(conj_by(P, J_ALL), J_ALL)
indep = g.rank_of_vectors([[x for row in DELTA for x in row],
                           [x for row in J_ALL for x in row]]) == 2
# the space of invariant symmetric forms EXACTLY: symmetric 3x3 matrices are a
# six-dimensional space with basis E_ab (a <= b); the constraints P X P^T = X
# for the two generators (0 1) and (0 1 2) are linear in X; the invariant
# subspace has dimension 6 - rank(constraints)
SYM_BASIS = []
for a_ in range(3):
    for b_ in range(a_, 3):
        X = [[F(0)] * 3 for _ in range(3)]
        X[a_][b_] = F(1)
        X[b_][a_] = F(1)
        SYM_BASIS.append(X)
rows = []
for p in ((1, 0, 2), (1, 2, 0)):
    P = perm_mat(p)
    for X in SYM_BASIS:
        D = conj_by(P, X)
        rows.append([D[i][j] - X[i][j] for i in range(3) for j in range(3)])
# rows[k] is the image of basis element k under (X -> P X P^T - X); stack per generator
cols = []
for k in range(6):
    cols.append(rows[k] + rows[6 + k])          # constraints for both generators
rank_constraints = g.rank_of_vectors(cols)
g.check("prop:chart(2)/prop:nullity: delta and the all-ones J are S3-invariant and "
      "independent, and the space of S3-invariant symmetric forms on R^3 has "
      "dimension EXACTLY 6 - %d = 2 (kernel of the invariance constraints): "
      "the two-parameter family, so C = sum Omega_k^2 is not singled out by S3 alone"
      % rank_constraints, ok and indep and 6 - rank_constraints == 2)

# prop:chart(3): the Fourier map Gamma -> (Re(Gamma zeta^k))_k lands in the
# doublet plane and is a bijection onto it (images of 1 and zeta independent)
def fourier_image(Gam):
    return [(Gam * z).re() for z in (CY(1), ZETA, Z2)]


img1, imgz = fourier_image(CY(1)), fourier_image(ZETA)
g.check("prop:chart(3): the Fourier images of Gamma = 1 and Gamma = zeta, "
      "(1, -1/2, -1/2) and (-1/2, -1/2, 1), each sum to zero and are linearly "
      "independent: the map is a bijection of C onto the real doublet plane, "
      "so every real face vector has the Koide form a + |Gamma| cos(delta + 2 pi k/3)",
      sum(img1) == 0 and sum(imgz) == 0
      and img1 == [F(1), F(-1, 2), F(-1, 2)] and imgz == [F(-1, 2), F(-1, 2), F(1)]
      and g.rank_of_vectors([img1[:], imgz[:]]) == 2)

# the parametrisation at the rational-cosine point: v = (a+b, a-b/2, a-b/2)
# has Q = 1/3 + b^2/(6a^2), equal to 2/3 iff b^2 = 2a^2
av = F(3)
ok = True
for bv in (F(0), F(1), F(3), F(6), F(-2)):
    # the explicit triple v = (a+b, a-b/2, a-b/2) = a + b cos(2 pi k/3): Q from it
    v3 = [av + bv, av - bv / 2, av - bv / 2]
    Q = sum(x * x for x in v3) / sum(v3) ** 2
    ok = ok and Q == (3 * av * av + F(3, 2) * bv * bv) / (9 * av * av)
    ok = ok and (Q == F(2, 3)) == (bv * bv == 2 * av * av)
# and the rational point b^2 = 2a^2 itself, in Z[sqrt2]: v = (a + a sqrt2, a - a sqrt2/2, ...)
b_r2 = R2(0, av)                       # b = a sqrt2 with a = 3: b = 3 sqrt2
v_r2 = [R2(av) + b_r2, R2(av) - b_r2 * R2(F(1, 2)), R2(av) - b_r2 * R2(F(1, 2))]
num = v_r2[0] * v_r2[0] + v_r2[1] * v_r2[1] + v_r2[2] * v_r2[2]
S3_ = v_r2[0] + v_r2[1] + v_r2[2]
ok = ok and (num * R2(3) == S3_ * S3_ * R2(2))      # Q = 2/3 exactly
# the bridge to prop:crossing: (a+b)/(a-b/2) = (1+sqrt2)(2+sqrt2) = 4 + 3 sqrt2 at b = a sqrt2
ok = ok and v_r2[0] == v_r2[1] * R2(4, 3)
g.check("prop:crossing/prop:chart(3): on the explicit triple (a+b, a-b/2, a-b/2) the "
      "Koide quotient is 1/3 + b^2/(6a^2), equal to 2/3 iff b^2 = 2a^2 (rational "
      "b on both sides of the condition, and exactly 2/3 at b = a sqrt2 in Z[sqrt2]); "
      "and at b = a sqrt2 the heavy-to-light ratio (a+b)/(a-b/2) is exactly 4 + 3 sqrt2, "
      "prop:crossing's root", ok)

# ---------------------------------------------------------------------------
# Part E: the Gaussian theorems (prop:rigidity, thm:skeleton, prop:crossing)
# ---------------------------------------------------------------------------

def cross_mat(a):
    return [[g.qi(0), g.qi(-1) * a[2], a[1]],
            [a[2], g.qi(0), g.qi(-1) * a[0]],
            [g.qi(-1) * a[1], a[0], g.qi(0)]]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def dagger(A):
    return [[A[j][i].conj() for j in range(3)] for i in range(3)]


ok_id = ok_ker = ok_rank = True
for a in ([g.qi(1), g.qi(2, 1), g.qi(0, -1)], [g.qi(F(1, 2)), g.qi(3), g.qi(1, 1)]):
    G = cross_mat(a)
    GGd = mm(G, dagger(G))
    a2 = sum(x * x.conj() for x in a)
    # identity GG+ = |a|^2 I - conj(a) a^T
    for i in range(3):
        for j in range(3):
            expect_v = (a2 if i == j else g.qi(0)) - a[i].conj() * a[j]
            ok_id = ok_id and GGd[i][j] == expect_v
    # kernel: GG+ conj(a) = 0
    for i in range(3):
        val = sum(GGd[i][j] * a[j].conj() for j in range(3))
        ok_ker = ok_ker and val == g.qi(0)
    # rank 2: the matrix GG+ has rank 2 (double eigenvalue |a|^2, one zero)
    ok_rank = ok_rank and g.field_rank([row[:] for row in GGd]) == 2
g.check("prop:rigidity: GG^dag = |a|^2 I - conj(a) a^T exactly on "
      "Gaussian-rational instances", ok_id)
g.check("prop:rigidity: conj(a) spans the exact kernel (GG^dag conj(a) = 0) "
      "and the rank is exactly 2: spectrum {|a|^2, |a|^2, 0} identically "
      "in a, the sector closure", ok_ker and ok_rank)

# ---- the channels, in exact cyclotomic arithmetic (prop:rigidity) ----
def cy_cross(p, q):
    return [p[1] * q[2] - p[2] * q[1], p[2] * q[0] - p[0] * q[2], p[0] * q[1] - p[1] * q[0]]


def cy_hdot(p, q):
    """Hermitian inner product sum conj(p_k) q_k."""
    tot = CY(0)
    for x, y in zip(p, q):
        tot = tot + x.conj() * y
    return tot


U_ALL = [CY(1), CY(1), CY(1)]
Z2mZ = Z2 - ZETA                     # zeta^2 - zeta = -i sqrt3
cAB = cy_cross(f_plus, f_minus)
cB = cy_cross(U_ALL, f_plus)
g.check("prop:rigidity: f+ x f- = (zeta^2 - zeta)(1,1,1) and u' x f+ = "
      "(zeta^2 - zeta) f+ exactly, with |zeta^2 - zeta|^2 = 3, so the normalised "
      "channel vectors are a_A = (zeta^2 - zeta)(1,1,1)/3 and a_B = (zeta^2 - zeta) f+/3, "
      "Hermitian-orthogonal with unit norm: |a|^2 = 1 + lambda^2",
      cAB == [Z2mZ * x for x in U_ALL] and cB == [Z2mZ * x for x in f_plus]
      and Z2mZ.conj() * Z2mZ == CY(3)
      and cy_hdot([x * F(1, 3) for x in cAB], [x * F(1, 3) for x in cB]) == CY(0)
      and cy_hdot([x * F(1, 3) for x in cAB], [x * F(1, 3) for x in cAB]) == CY(1)
      and cy_hdot([x * F(1, 3) for x in cB], [x * F(1, 3) for x in cB]) == CY(1))

# ---- the exact Wick engine (thm:skeleton) ----
# six modes p = (i, A) -> 2i + A; Theta_k = (1/2) E_k (x) eps with (E_k)_ij = eps_kij;
# Gaussian data of the squeezed vacuum with fourfold-degenerate Takagi value:
#   xi_hat = (G (x) eps)/|a|,  Pi = xi_hat xi_hat^dag = R (x) 1,  R = 1 - conj(n) n^T,
#   N = s^2 conj(Pi),  M = -s c xi_hat  (Fact fact:gaussian);
# H_kl = conj(w_k) w_l + tr(Th_l Th_k) + tr(Th_k Th_l N^T) + tr(Th_l Th_k N) + 2 tr(Th_k N Th_l N^T).
EPS3 = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
EPS2 = [[F(0), F(1)], [F(-1), F(0)]]


def cy_zeros(n, m):
    return [[CY(0) for _ in range(m)] for _ in range(n)]


def cy_mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), CY(0)) for j in range(p)] for i in range(n)]


def cy_tr(A):
    return sum((A[i][i] for i in range(len(A))), CY(0))


def cy_T(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def cy_conjm(A):
    return [[x.conj() for x in row] for row in A]


def cy_dag(A):
    return cy_conjm(cy_T(A))


def cy_scale(c, A):
    return [[x * c for x in row] for row in A]


def cy_add(A, B):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def cy_eqm(A, B):
    return all(x == y for ra, rb in zip(A, B) for x, y in zip(ra, rb))


def kron(A, B):
    n, m = len(A), len(B)
    out = cy_zeros(n * m, n * m)
    for i in range(n):
        for j in range(n):
            for a in range(m):
                for b in range(m):
                    out[m * i + a][m * j + b] = A[i][j] * B[a][b]
    return out


def cy_cross_mat(a):
    return [[CY(0), -a[2], a[1]], [a[2], CY(0), -a[0]], [-a[1], a[0], CY(0)]]


THETA = []
for k in range(3):
    Ek = [[CY(EPS3.get((k, i, j), 0)) for j in range(3)] for i in range(3)]
    THETA.append(cy_scale(F(1, 2), kron(Ek, [[CY(x) for x in row] for row in EPS2])))

ID6 = [[CY(1) if i == j else CY(0) for j in range(6)] for i in range(6)]
ID3 = [[CY(1) if i == j else CY(0) for j in range(3)] for i in range(3)]

ok_pieces = ok_total = ok_coh = ok_no = ok_pi = True
points = 0
aA_n = [x * F(1, 3) for x in cAB]
aB_n = [x * F(1, 3) for x in cB]
for (sv, cv) in ((F(3, 4), F(5, 4)), (F(12, 5), F(13, 5))):
    xv_ = sv * sv
    assert cv * cv - sv * sv == 1
    for (lam_, amod) in ((F(0), F(1)), (F(3, 4), F(5, 4)), (F(4, 3), F(5, 3))):
        for phase in (CY(1), ZETA, Z2):
            a_vec = [x + y * lam_ * phase for x, y in zip(aA_n, aB_n)]
            assert cy_hdot(a_vec, a_vec) == CY(amod * amod)
            n_vec = [x * (1 / amod) for x in a_vec]
            R3 = [[(CY(1) if i == j else CY(0)) - n_vec[i].conj() * n_vec[j] for j in range(3)] for i in range(3)]
            G = cy_cross_mat(a_vec)
            xi_hat = cy_scale(1 / amod, kron(G, [[CY(x) for x in row] for row in EPS2]))
            Pi = cy_mm(xi_hat, cy_dag(xi_hat))
            ok_pi = ok_pi and cy_eqm(Pi, kron(R3, [[CY(1), CY(0)], [CY(0), CY(1)]]))
            N = cy_scale(sv * sv, cy_conjm(Pi))
            NT = cy_T(N)
            M = cy_scale(-sv * cv, xi_hat)
            omega = [cy_tr(cy_mm(Th, M)) for Th in THETA]
            ok_coh = ok_coh and all(omega[k] == n_vec[k] * (2 * sv * cv) for k in range(3))
            H = cy_zeros(3, 3)
            for k in range(3):
                for l in range(3):
                    Thk, Thl = THETA[k], THETA[l]
                    nkl = n_vec[k].conj() * n_vec[l]
                    p1 = cy_tr(cy_mm(Thl, Thk))
                    p2 = cy_tr(cy_mm(cy_mm(Thk, Thl), NT)) + cy_tr(cy_mm(cy_mm(Thl, Thk), N))
                    p3 = cy_tr(cy_mm(cy_mm(cy_mm(Thk, N), Thl), NT)) * 2
                    p4 = omega[k].conj() * omega[l]
                    dkl = CY(1) if k == l else CY(0)
                    ok_pieces = (ok_pieces and p1 == dkl
                                 and p2 == dkl * (sv * sv) + nkl * (sv * sv)
                                 and p3 == nkl * (2 * sv ** 4)
                                 and p4 == nkl * (4 * sv * sv * cv * cv))
                    ok_no = ok_no and (p3 + p4) == nkl * (2 * xv_ * (2 + 3 * xv_))
                    H[k][l] = p1 + p2 + p3 + p4
                    ok_total = ok_total and H[k][l] == dkl * (cv * cv) + nkl * (xv_ * (5 + 6 * xv_))
            points += 1
g.check("prop:rigidity: xi_hat xi_hat^dag = R (x) 1 with R = 1 - conj(n) n^T exactly "
      "at every strength/ratio/phase point: the Gaussian data of the fourfold-"
      "degenerate pairing (%d points)" % points, ok_pi)
g.check("prop:rigidity: the coherent vector <Omega_k> = tr(Theta_k M) = 2 sinh r cosh r n_k "
      "exactly at every point", ok_coh)
g.check("thm:skeleton: the four Wick pieces equal delta_kl, s^2 delta_kl + s^2 conj(n_k) n_l, "
      "2 s^4 conj(n_k) n_l and 4 s^2 c^2 conj(n_k) n_l exactly, in Q(zeta_3) at the rational "
      "hyperbolic points (3/4, 5/4), (12/5, 13/5), ratios 0, 3/4, 4/3 and phases 1, zeta, zeta^2",
      ok_pieces)
g.check("thm:skeleton: H = cosh^2 r 1 + x(5+6x) P_[conj v] exactly at every point, from the "
      "Wick formula and the Gaussian data (the closed form of eq. (6), eq:H)", ok_total)
g.check("thm:skeleton(1): the normal-ordered form <Omega_k^dag Omega_l> (the M-bar M and "
      "NN pieces alone) = 2x(2+3x) P_[conj v] exactly: rank one, the light pair strictly massless", ok_no)

# thm:skeleton: trace identity and the rank-one normal-ordered form
xv = g.RF.var()
tr_lhs = g.RF.const(3) * (g.RF1 + xv) + xv * (g.RF.const(5) + g.RF.const(6) * xv)
tr_rhs = g.RF.const(3) + g.RF.const(8) * xv + g.RF.const(6) * xv * xv
g.check("thm:skeleton: the trace identity 3 cosh^2 r + x(5+6x) = 3 + 8x + "
      "6x^2 as a rational-function identity in the depth", tr_lhs.eqrf(tr_rhs))
g.check("thm:skeleton: the heavy eigenvalue 1 + 6x + 6x^2 = cosh^2 r + "
      "x(5+6x) as an RF identity (the coherent ray carries the excess)",
      (g.RF1 + g.RF.const(6) * xv + g.RF.const(6) * xv * xv)
      .eqrf((g.RF1 + xv) + xv * (g.RF.const(5) + g.RF.const(6) * xv)))

# prop:crossing: rho = 4 + 3 sqrt2 solves rho^2 - 8 rho - 2 = 0; fourth power
rho = R2(4, 3)
g.check("prop:crossing: rho = 4 + 3 sqrt(2) satisfies rho^2 - 8 rho - 2 = 0 exactly "
      "in Z[sqrt(2)]",
      rho * rho - R2(8) * rho - R2(2) == R2(0))
R4 = rho * rho * rho * rho
g.check("prop:crossing: (4 + 3 sqrt(2))^4 = 2308 + 1632 sqrt(2) exactly",
      R4 == R2(2308, 1632))


def g_of(xq):
    """g(x) = 6x^2 + 6x + 1 - R4 (1 + x), in Z[sqrt2], at rational x."""
    xq = F(xq)
    return R2(6 * xq * xq + 6 * xq + 1) - R4 * R2(1 + xq)


g.check("prop:crossing: the crossing is bracketed exactly: g(769.332) < 0 < "
      "g(769.333) in exact Z[sqrt(2)] sign arithmetic, so "
      "x* = 769.3325 to the stated precision",
      (not g_of(F(769332, 1000)).positive())
      and g_of(F(769333, 1000)).positive())

# the identity (1+6x+6x^2)/(1+x) = 6x + 1/(1+x), hence x* = K/6 - 1/(6(1+x*)),
# and the displacement bracketed from the crossing bracket
xq = g.RF.var()
g.check("prop:crossing: (1 + 6x + 6x^2)/(1 + x) = 6x + 1/(1 + x) as an RF identity, "
      "so x* = K/6 - 1/(6(1 + x*)): the depth is K/6 up to the skeleton's own tail",
      ((g.RF1 + g.RF.const(6) * xq + g.RF.const(6) * xq * xq) / (g.RF1 + xq))
      .eqrf(g.RF.const(6) * xq + g.RF1 / (g.RF1 + xq)))
disp_lo = 1 / (6 * (1 + F(769333, 1000)))
disp_hi = 1 / (6 * (1 + F(769332, 1000)))
g.check("prop:crossing: the displacement K/6 - x* = 1/(6(1 + x*)) lies in "
      "(2 x 10^-4, 3 x 10^-4): x* agrees with K/6 to three decimals and not four",
      F(2, 10 ** 4) < disp_lo and disp_hi < F(3, 10 ** 4))

# the nominated canonical depth fails: at x = 1 the ratio is 13/2
def ratio_fn(xq):
    xq = F(xq)
    return (1 + 6 * xq + 6 * xq * xq) / (1 + xq)


r1 = ratio_fn(1)
g.check("prop:crossing: the ratio function (1+6x+6x^2)/(1+x) evaluated at the nominated "
      "canonical depth x = 1 (tanh^2 r = 1/2) is exactly 13/2, and K exceeds it by a "
      "factor above 700 in exact Z[sqrt2] sign arithmetic: no canonical depth marks "
      "the crossing",
      r1 == F(13, 2) and (R4 - R2(700) * R2(r1)).positive())

# monotonicity witness for the single crossing: g increasing differences
g.check("prop:crossing: the left side (1+6x+6x^2)/(1+x) is strictly "
      "increasing on exact sample chain x = 1, 10, 100, 769, 1000",
      all((F(1 + 6 * a + 6 * a * a, 1 + a) < F(1 + 6 * b + 6 * b * b, 1 + b))
          for a, b in ((1, 10), (10, 100), (100, 769), (769, 1000))))


# ---------------------------------------------------------------------------
# Part F: the 126 doublet direction (prop:126), with the module, the pairing
# and the Yukawa forms rebuilt from scratch (sparse exact matrices on
# Lambda^*(C^5)); the family no-go and the e^c charge are the Standard-Model
# paper's Thm 9.31 and Prop 9.15, recomputed here as Fact 8.2's content.
# ---------------------------------------------------------------------------

def part_F():
    from fractions import Fraction as F
    from itertools import combinations
    _RETAG = [
        ("[D] FAMILY NO-GO", "fact:nogos(i) (T12 Thm 9.31 recomputed) FAMILY NO-GO"),
        ("[D] the family matrix F", "fact:nogos(i) (T12 Thm 9.31 recomputed): the family matrix F"),
        ("[D] on the 126 direction |M_e| = 3 |M_d|", "prop:126(ii)/fact:nogos(i): on the 126 direction |M_e| = 3 |M_d|"),
        ("[D] the e^c state", "rem:bracket (T12 Prop 9.15 recomputed): the e^c state"),
        ("[D] T = w_4 (B - L) chi is odd", "prop:126(i): T = w_4 (B - L) chi is odd"),
        ("[D] the grade-1 (10) part", "prop:126(i): the grade-1 (10) part"),
        ("[D] T = w_4 (B - L) chi is PURE grade five", "prop:126(i): T = w_4 (B - L) chi is PURE grade five"),
        ("[D] the grade-5 (126) part", "prop:126(ii): the grade-5 (126) part"),
        ("[D] the symmetric part of Y_T", "prop:126(ii): the symmetric part of Y_T"),
        ("[D] T = w_4 (B - L) chi: symmetric", "prop:126(ii): T = w_4 (B - L) chi: symmetric"),
        ("[D] the one-sided weighting", "prop:126(iii): the one-sided weighting"),
        ("[D] up-type", "prop:126(iv): up-type"),
        ("[D] B - L = -(2/3)", "prop:126(i): B - L = -(2/3)"),
        ("[D] closed form", "prop:126(i): closed form"),
        ("[D] w_4 anticommutes", "prop:126(i): w_4 anticommutes"),
        ("[D] the ratio |Y(L e^c)|", "prop:126(ii): the ratio |Y(L e^c)|"),
        ("[D] every nonzero entry", "prop:126(ii): every nonzero entry"),
        ("[D] B - L = 1 - (2/3) N_W", "sec:weights: B - L = 1 - (2/3) N_W"),
        ("[D]", "sec:weights (the module rebuilt):"),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)
    NM = 5                                 # modes 0,1,2 = pairs W (colour), 3,4 = rungs (slots)
    PAIRS, RUNGS = (0, 1, 2), (3, 4)
    STATES = [frozenset(S) for k in range(NM + 1) for S in combinations(range(NM), k)]
    IDX = {S: i for i, S in enumerate(STATES)}
    DIM = len(STATES)                      # 32

    # sparse matrices: dict {(row, col): Fraction}
    def sp_from_action(act):
        """act(state frozenset) -> dict{frozenset: Fraction}; returns sparse matrix."""
        M = {}
        for S in STATES:
            for T, c in act(S).items():
                if c != 0:
                    M[(IDX[T], IDX[S])] = M.get((IDX[T], IDX[S]), F(0)) + c
        return {k: v for k, v in M.items() if v != 0}

    def sp_mul(A, B):
        Bc = {}
        for (i, j), b in B.items():
            Bc.setdefault(i, []).append((j, b))
        C = {}
        for (i, k), a in A.items():
            for j, b in Bc.get(k, ()):
                C[(i, j)] = C.get((i, j), F(0)) + a * b
        return {k: v for k, v in C.items() if v != 0}

    def sp_add(*Ms):
        C = {}
        for M in Ms:
            for k, v in M.items():
                C[k] = C.get(k, F(0)) + v
        return {k: v for k, v in C.items() if v != 0}

    def sp_scal(c, M):
        return {k: c * v for k, v in M.items() if c * v != 0}

    def sp_eq(A, B):
        return sp_add(A, sp_scal(F(-1), B)) == {}

    def sp_apply(M, vec):
        out = {}
        for (i, j), a in M.items():
            if j in vec:
                out[i] = out.get(i, F(0)) + a * vec[j]
        return {k: v for k, v in out.items() if v != 0}

    def sp_trace(M):
        return sum(v for (i, j), v in M.items() if i == j)

    ID = {(i, i): F(1) for i in range(DIM)}

    def wedge_act(i):
        return lambda S: g.ext_wedge(i, {S: F(1)})

    def contract_act(i):
        fv = [F(1) if j == i else F(0) for j in range(NM)]
        return lambda S: g.ext_contract(fv, {S: F(1)})

    V = [sp_from_action(wedge_act(i)) for i in range(NM)]      # creation  v_i
    Wm = [sp_from_action(contract_act(i)) for i in range(NM)]  # annihilation w_i

    # CAR: {v_i, w_j} = delta_ij, {v_i, v_j} = {w_i, w_j} = 0
    ok = True
    for i in range(NM):
        for j in range(NM):
            ac = sp_add(sp_mul(V[i], Wm[j]), sp_mul(Wm[j], V[i]))
            ok = ok and sp_eq(ac, ID if i == j else {})
            ok = ok and sp_add(sp_mul(V[i], V[j]), sp_mul(V[j], V[i])) == {}
            ok = ok and sp_add(sp_mul(Wm[i], Wm[j]), sp_mul(Wm[j], Wm[i])) == {}
    _chk("[D] five mode pairs: {v_i, w_j} = delta_ij, {v_i, v_j} = {w_i, w_j} = 0 on the 32-dimensional module", ok)

    # number operators, hypercharge, T_3, B-L
    def num(i):
        return sp_mul(V[i], Wm[i])
    N_W = sp_add(*[num(i) for i in PAIRS])
    N_R = sp_add(*[num(i) for i in RUNGS])
    Y = sp_add(sp_scal(F(1, 2), N_R), sp_scal(F(-1, 3), N_W))          # Y = N_R/2 - N_W/3
    T3 = sp_scal(F(1, 2), sp_add(num(3), sp_scal(F(-1), num(4))))
    BmL = sp_add(ID, sp_scal(F(-2, 3), N_W))                              # B - L = 1 - (2/3) N_W

    def species(S):
        nr, nw = len(S & set(RUNGS)), len(S & set(PAIRS))
        return {(0, 0): "nu^c", (2, 0): "e^c", (1, 1): "Q", (1, 3): "L", (0, 2): "u^c", (2, 2): "d^c",
                (1, 0): "slot", (0, 1): "pair", (1, 2): "(1,2)", (2, 1): "(2,1)", (0, 3): "(0,3)", (2, 3): "(2,3)"}[(nr, nw)]

    SIXTEEN = [S for S in STATES if len(S) % 2 == 0]
    _chk("[D] the even states number sixteen: nu^c (1), e^c (1), Q (6), L (2), u^c (3), d^c (3)",
            len(SIXTEEN) == 16 and sorted(species(S) for S in SIXTEEN) ==
            sorted(["nu^c", "e^c"] + ["Q"] * 6 + ["L"] * 2 + ["u^c"] * 3 + ["d^c"] * 3))
    Yval = {"nu^c": F(0), "e^c": F(1), "Q": F(1, 6), "L": F(-1, 2), "u^c": F(-2, 3), "d^c": F(1, 3)}
    BLval = {"nu^c": F(1), "e^c": F(1), "Q": F(1, 3), "L": F(-1), "u^c": F(-1, 3), "d^c": F(-1, 3)}
    def diag_val(M, S):
        v = sp_apply(M, {IDX[S]: F(1)})
        return v.get(IDX[S], F(0)) if set(v) <= {IDX[S]} else None
    _chk("[D] Y = N_R/2 - N_W/3 gives the Standard-Model hypercharges on the sixteen",
            all(diag_val(Y, S) == Yval[species(S)] for S in SIXTEEN))
    _chk("[D] B - L = 1 - (2/3) N_W gives (nu^c, e^c, Q, L, u^c, d^c) = (1, 1, 1/3, -1, -1/3, -1/3): "
            "B - L is an affine function of the pair number",
            all(diag_val(BmL, S) == BLval[species(S)] for S in SIXTEEN))

    # the invariant pairing B(psi, phi) = sum_S (-1)^{|S|(|S|-1)/2} eps(S, S^c) psi_S phi_{S^c}
    FULL = frozenset(range(NM))
    def eps_sign(S):
        """sign of e_S wedge e_{S^c} = eps e_{01234}."""
        seq = sorted(S) + sorted(FULL - S)
        inv = sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[a] > seq[b])
        return F(-1) ** inv
    Bcoef = {S: F(-1) ** (len(S) * (len(S) - 1) // 2) * eps_sign(S) for S in STATES}
    def Bpair(psi, phi):
        return sum(Bcoef[S] * psi.get(IDX[S], F(0)) * phi.get(IDX[FULL - S], F(0)) for S in STATES)

    def basis(S):
        return {IDX[S]: F(1)}
    # so(10) generators: 45 bivectors
    GENS = []
    for i in range(NM):
        for j in range(NM):
            if i != j:
                GENS.append(sp_mul(V[i], Wm[j]))
    for i, j in combinations(range(NM), 2):
        GENS.append(sp_mul(V[i], V[j]))
        GENS.append(sp_mul(Wm[i], Wm[j]))
    for i in range(NM):
        GENS.append(sp_add(num(i), sp_scal(F(-1, 2), ID)))
    _chk("[D] forty-five bivector generators", len(GENS) == 45)
    inv_ok = True
    for X in GENS:
        for S in STATES:
            Xs = sp_apply(X, basis(S))
            for T in STATES:
                if Bpair(Xs, basis(T)) + Bpair(basis(S), sp_apply(X, basis(T))) != 0:
                    inv_ok = False
    _chk("[D] the pairing B is so(10)-invariant on all 45 x 32 x 32 basis identities (T12 Lem. 9.23, recomputed)", inv_ok)

    def yukawa(Top):
        """Y_T(psi, phi) = B(psi, T phi) on the sixteen, returned as {(species_S, species_T): set of values}
        together with the full matrix over basis pairs."""
        mat = {}
        for S in SIXTEEN:
            for T in SIXTEEN:
                val = Bpair(basis(S), sp_apply(Top, basis(T)))
                if val != 0:
                    mat[(S, T)] = val
        return mat

    def clebsch(mat):
        """collect the nonzero values by species pair, unordered."""
        out = {}
        for (S, T), v in mat.items():
            key = tuple(sorted((species(S), species(T))))
            out.setdefault(key, set()).add(v)
        return out

    def is_symmetric(mat):
        return all(mat.get((T, S), F(0)) == v for (S, T), v in mat.items())

    # --- the 10: x = w_3 (a rung annihilation vector, Y = -1/2): couples (L, e^c) and (Q, d^c)
    Y10 = yukawa(Wm[3])
    c10 = clebsch(Y10)
    _chk("[D] the 10 (x = w_4): Y_x nonzero exactly on (L, e^c) and (Q, d^c), symmetric, all entries +-1",
            set(c10) == {("L", "e^c"), ("Q", "d^c")} and is_symmetric(Y10)
            and all(abs(v) == 1 for vs in c10.values() for v in vs))

    # --- the B-L weighted rung coupling.  The Standard-Model Yukawas conserve B - L, so a weighting by the
    # B - L of one argument alone is antisymmetric on every coupled pair; the symmetric weighting is by the
    # B - L of the DOUBLET member of the pair, which is chi (B - L) with chi = +1 on the doublet sector N_R = 1
    # and -1 on the singlet sectors N_R = 0, 2, i.e. chi = -(-1)^{N_R}.
    PARITY_R = sp_mul(sp_add(ID, sp_scal(F(-2), num(3))), sp_add(ID, sp_scal(F(-2), num(4))))   # (-1)^{N_R}
    CHI = sp_scal(F(-1), PARITY_R)
    T_GJ = sp_mul(Wm[3], sp_mul(BmL, CHI))
    YGJ = yukawa(T_GJ)
    cGJ = clebsch(YGJ)
    _chk("[D] T = w_4 (B - L) chi: symmetric, entries exactly {-1} on (L, e^c) and exactly {+1/3, -1/3} on (Q, d^c) "
            "(sign-sensitive: flipping chi fails), in the normalisation where the 10 form has entries +-1: the "
            "Georgi-Jarlskog ratio |y_e/y_d| = 3 is the ratio of the lepton doublet's to the quark doublet's B - L",
            set(cGJ) == {("L", "e^c"), ("Q", "d^c")} and cGJ[("L", "e^c")] == {F(-1)}
            and cGJ[("Q", "d^c")] == {F(1, 3), F(-1, 3)} and is_symmetric(YGJ))
    # the unsymmetrised weighting is antisymmetric on every coupled pair (B - L conservation)
    Yraw = yukawa(sp_mul(Wm[3], BmL))
    _chk("[D] the one-sided weighting w_4 (B - L) is ANTISYMMETRIC on every coupled pair: the Yukawa pairs are "
            "B - L neutral, (B-L)(L) + (B-L)(e^c) = 0 = (B-L)(Q) + (B-L)(d^c)",
            Yraw != {} and all(Yraw.get((T, S), F(0)) == -v for (S, T), v in Yraw.items())
            and BLval["L"] + BLval["e^c"] == 0 and BLval["Q"] + BLval["d^c"] == 0)
    def mag(c, key):
        """the common magnitude of the entries on a species pair, or None if there is none (a FAIL, not an abort)."""
        vals = {abs(v) for v in c.get(key, ())}
        return vals.pop() if len(vals) == 1 else None
    def ratio_is(c, k1, k2, r):
        a, b = mag(c, k1), mag(c, k2)
        return a is not None and b is not None and b != 0 and a / b == r
    _chk("[D] the ratio |Y(L e^c)| / |Y(Q d^c)| is 1 for the 10 and 3 for the B-L weighted coupling",
            ratio_is(c10, ("L", "e^c"), ("Q", "d^c"), 1) and ratio_is(cGJ, ("L", "e^c"), ("Q", "d^c"), 3))

    # --- grade decomposition of T_GJ in the Clifford algebra of the ten.
    # Orthonormal basis: a_i = v_i + w_i (square +1), b_i = v_i - w_i (square -1); blades = products.
    Aon = [sp_add(V[i], Wm[i]) for i in range(NM)]
    Bv = [sp_add(V[i], sp_scal(F(-1), Wm[i])) for i in range(NM)]
    _chk("[D] a_i = v_i + w_i square to +1, b_i = v_i - w_i to -1, and all ten anticommute pairwise: Cl(5,5)",
            all(sp_eq(sp_mul(Aon[i], Aon[i]), ID) and sp_eq(sp_mul(Bv[i], Bv[i]), sp_scal(F(-1), ID)) for i in range(NM))
            and all(sp_add(sp_mul(Aon[i], Bv[j]), sp_mul(Bv[j], Aon[i])) == {} for i in range(NM) for j in range(NM))
            and all(sp_add(sp_mul(Aon[i], Aon[j]), sp_mul(Aon[j], Aon[i])) == {} for i in range(NM) for j in range(NM) if i != j)
            and all(sp_add(sp_mul(Bv[i], Bv[j]), sp_mul(Bv[j], Bv[i])) == {} for i in range(NM) for j in range(NM) if i != j))
    TEN = Aon + Bv
    SQ = [F(1)] * NM + [F(-1)] * NM

    def blade(idx):
        M = ID
        for k in idx:
            M = sp_mul(M, TEN[k])
        return M

    def blade_inverse_sign(idx):
        """Gamma_idx^{-1} = sign * Gamma_idx reversed... compute Gamma_idx * Gamma_idx = s * ID, so inverse = Gamma/s."""
        k = len(idx)
        s = F(-1) ** (k * (k - 1) // 2)
        for t in idx:
            s *= SQ[t]
        return s

    # grade projection by the trace formula: coefficient of Gamma_A in M is tr(Gamma_A^{-1} M)/32
    def grade_parts(M):
        parts = {}
        for k in range(0, 2 * NM + 1):
            acc = {}
            for idx in combinations(range(2 * NM), k):
                G = blade(idx)
                s = blade_inverse_sign(idx)
                coef = sp_trace(sp_mul(G, M)) / s / DIM
                if coef != 0:
                    acc = sp_add(acc, sp_scal(coef, G))
            if acc:
                parts[k] = acc
        return parts

    parts = grade_parts(T_GJ)
    _chk("[D] T = w_4 (B - L) chi is odd (grades among 1, 3, 5 only) and the grade parts sum back to T",
            set(parts) <= {1, 3, 5} and sp_eq(sp_add(*parts.values()), T_GJ))
    Y1, Y3, Y5 = (yukawa(parts.get(k, {})) for k in (1, 3, 5))
    c1, c3, c5 = clebsch(Y1), clebsch(Y3), clebsch(Y5)
    _chk("[D] the grade-1 (10) part of T contributes NOTHING on the sixteen: its Yukawa form is identically zero",
            Y1 == {})
    _chk("[D] T = w_4 (B - L) chi is PURE grade five (what is tested: no grade-1 and no grade-3 component, so no 10 and "
            "no 120; that the induced form is the 126 component is the imported Fact 8.5, not tested)",
            set(parts) == {5} and Y3 == {})
    _chk("[D] the grade-5 (126) part is symmetric and carries the whole Georgi-Jarlskog pattern: "
            "|Y(L e^c)| / |Y(Q d^c)| = 3 on the 126 alone",
            is_symmetric(Y5) and set(c5) == {("L", "e^c"), ("Q", "d^c")}
            and ratio_is(c5, ("L", "e^c"), ("Q", "d^c"), 3))
    _chk("[D] the symmetric part of Y_T is exactly Y_126 (the 120 drops out of any one-family mass term): "
            "(Y_T + Y_T^t)/2 = Y_5",
            all(F(1, 2) * (YGJ.get((S, T), F(0)) + YGJ.get((T, S), F(0))) == Y5.get((S, T), F(0))
                for S in SIXTEEN for T in SIXTEEN))

    # the analogous statement for the up-type doublet direction v_4 (Y = +1/2): (L nu^c), (Q u^c)
    T_GJu = sp_mul(V[3], sp_mul(BmL, CHI))
    Yu = yukawa(T_GJu)
    cu = clebsch(Yu)
    _chk("[D] up-type: T' = v_4 (B - L) chi has a SYMMETRIC form (chi is what makes it so) nonzero exactly on (L, nu^c) "
            "with signed entries {+1} and on (Q, u^c) with signed entries {+1/3, -1/3} (colour-dependent sign): "
            "|m_nu^D| = 3 |m_u| on the 126 direction, a relation of magnitudes only",
            is_symmetric(Yu) and set(cu) == {("L", "nu^c"), ("Q", "u^c")}
            and cu[("L", "nu^c")] == {F(1)} and cu[("Q", "u^c")] == {F(1, 3), F(-1, 3)}
            and ratio_is(cu, ("L", "nu^c"), ("Q", "u^c"), 3))

    # --- the family no-go: a vev in the 10 tensored with ANY family matrix gives identical charged-lepton
    # and down spectra, family by family.
    def charpoly_invariants(M3):
        """trace, sum of principal 2-minors, determinant of a 3x3 Fraction matrix."""
        t = M3[0][0] + M3[1][1] + M3[2][2]
        m2 = sum(M3[i][i] * M3[j][j] - M3[i][j] * M3[j][i] for i, j in combinations(range(3), 2))
        d = (M3[0][0] * (M3[1][1] * M3[2][2] - M3[1][2] * M3[2][1])
             - M3[0][1] * (M3[1][0] * M3[2][2] - M3[1][2] * M3[2][0])
             + M3[0][2] * (M3[1][0] * M3[2][1] - M3[1][1] * M3[2][0]))
        return (t, m2, d)

    def mt(A):
        return [[A[j][i] for j in range(3)] for i in range(3)]
    def mmul3(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    def scal3(c, A):
        return [[c * A[i][j] for j in range(3)] for i in range(3)]
    def sing_inv(M):
        """the singular spectrum in magnitude: the characteristic invariants of M M^T."""
        return charpoly_invariants(mmul3(M, mt(M)))
    Ffam = [[F(2), F(1, 3), F(-1)], [F(0), F(5, 7), F(4)], [F(-1), F(3), F(1, 2)]]      # any family matrix
    disc_ok = (Ffam != mt(Ffam) and charpoly_invariants(Ffam)[2] != 0
               and len(set(charpoly_invariants(mmul3(Ffam, mt(Ffam))))) == 3)
    _chk("[D] the family matrix F is non-symmetric and invertible, with three distinct characteristic invariants of "
            "F F^T (the no-go is tested on a non-degenerate F, not on 0 or 1)", disc_ok)
    # the 10: for every signed entry y_e on (L, e^c) and y_d on (Q, d^c), M_e = y_e F and M_d = y_d F have the same
    # singular spectrum; the check is discriminating because the same construction on the 126 entries fails.
    def spectra_agree(c, ratio):
        return all(sing_inv(scal3(ye, Ffam)) == sing_inv(scal3(ratio * yd, Ffam))
                   for ye in c[("L", "e^c")] for yd in c[("Q", "d^c")])
    _chk("[D] FAMILY NO-GO: with the vev in the 10, M_e = y_e F and M_d = y_d F for every signed pair of entries "
            "(y_e, y_d) in ({+1}, {+1, -1}) have the same singular spectrum on the non-degenerate F, while the 126 "
            "entries (-1, +-1/3) on the same F do NOT: no family-space breaking separates m_e from m_d at tree level",
            disc_ok and spectra_agree(c10, F(1)) and not spectra_agree(c5, F(1)))
    _chk("[D] on the 126 direction |M_e| = 3 |M_d| family by family: the singular spectrum of y_e F equals that of "
            "3 y_d F for every signed pair of 126 entries on the same F (singular values in the ratio 3, whatever F)",
            disc_ok and spectra_agree(c5, F(3)) and not spectra_agree(c10, F(3)))

    # --- the bracket cannot serve: the e^c direction of Lambda^2(5) carries hypercharge +1
    ec = [S for S in SIXTEEN if species(S) == "e^c"][0]
    _chk("[D] the e^c state (both rungs occupied, no pairs) has Y = 1: a mass form B(psi, T phi) conserving "
            "hypercharge needs Y(T) = -(Y(psi) + Y(phi)); a direction of charge +1 is not a neutral vev",
            diag_val(Y, ec) == 1)
    # hypercharge conservation of the Yukawa forms computed: Y(S) + Y(T) + Y(x) = 0 on every nonzero entry
    def conserves(mat, yx):
        return all(Yval[species(S)] + Yval[species(T)] + yx == 0 for (S, T) in mat)
    _chk("[D] every nonzero entry of Y_x (x = w_4, Y = -1/2) and of Y_T (T = w_4 (B-L) chi) conserves hypercharge",
            conserves(Y10, F(-1, 2)) and conserves(YGJ, F(-1, 2)))


    # --- the closed form of the 126 direction: T_GJ = (4/3) w_4 ^ (v_5 ^ w_5) ^ sum_i (v_i ^ w_i)
    def wedge2(v, w):
        """v ^ w = (v w - w v)/2 for vectors."""
        return sp_scal(F(1, 2), sp_add(sp_mul(v, w), sp_scal(F(-1), sp_mul(w, v))))
    area5 = wedge2(V[4], Wm[4])
    pairbiv = sp_add(*[wedge2(V[i], Wm[i]) for i in PAIRS])
    _chk("[D] B - L = -(2/3) sum_{pairs} v_i ^ w_i (pure grade two) and w_4 chi = w_4 (1 - 2 n_5) = -2 w_4 (v_5 ^ w_5)",
            sp_eq(BmL, sp_scal(F(-2, 3), pairbiv))
            and sp_eq(sp_mul(Wm[3], CHI), sp_scal(F(-2), sp_mul(Wm[3], area5))))
    closed = sp_scal(F(4, 3), sp_mul(sp_mul(Wm[3], area5), pairbiv))
    _chk("[D] closed form: T_GJ = (4/3) w_4 (v_5 ^ w_5) (sum_i v_i ^ w_i), and since the three factors are mutually "
            "orthogonal the product is the wedge: the rung vector, wedged with the other rung's area bivector and with "
            "the pair-sector u(1) generator", sp_eq(T_GJ, closed))
    # orthogonality of the factors: w_4 anticommutes with every vector of the other rung and of the pairs
    _chk("[D] w_4 anticommutes with v_5, w_5 and with every pair vector (the factors are orthogonal)",
            all(sp_add(sp_mul(Wm[3], x), sp_mul(x, Wm[3])) == {} for x in [V[4], Wm[4]] + [V[i] for i in PAIRS] + [Wm[i] for i in PAIRS]))




part_F()

# ---------------------------------------------------------------------------
# Part G: the covariance of the absolute scale (prop:covariance).  Exact
# monomials in (H, M_P, m): a triple of exponents; the rescaling Lambda ->
# kappa^2 Lambda at fixed M_P is H -> kappa H, m fixed.
# ---------------------------------------------------------------------------

# a monomial in (H, M_P, m, kappa) is a 4-tuple of Fraction exponents; the generators and the
# rescaling substitution are the only inputs, and N, m/M_P, Im w are BUILT from the generators.
def _mono(h, mp, m, k=0):
    return (Fraction(h), Fraction(mp), Fraction(m), Fraction(k))
def _mmul(a, b):
    return tuple(x + y for x, y in zip(a, b))
def _minv(a):
    return tuple(-x for x in a)
_H, _MP, _m, _kappa = _mono(1, 0, 0), _mono(0, 1, 0), _mono(0, 0, 1), _mono(0, 0, 0, 1)
def _rescale(mono):
    """the substitution H -> kappa H with M_P and m fixed (the premise of prop:covariance, observation level):
    a monomial H^h M_P^p m^q picks up kappa^h."""
    h, p, q, k = mono
    return (h, p, q, k + h)
def _kappa_weight(mono):
    """the power of kappa that the substitution produces, computed by applying it."""
    return _rescale(mono)[3] - mono[3]
_N = _mmul(_MP, _minv(_H))           # N = M_P / H
_ratio = _mmul(_m, _minv(_MP))       # m / M_P
_Imw = _mmul(_m, _minv(_H))          # Im w = m / H
g.check("prop:covariance: Im w = m/H = N (m/M_P) as an exact monomial identity in the "
        "exponents of (H, M_P, m), the three monomials built from the generators", _mmul(_N, _ratio) == _Imw)
g.check("prop:covariance: applying the substitution H -> kappa H with M_P and m fixed (the premise) to the built "
        "monomials, N -> N/kappa (weight -1), m/M_P is unchanged (weight 0), and Im w -> Im w/kappa (weight -1, "
        "the product of the two): m/M_P is the rescaling-invariant content",
        _rescale(_N) == _mmul(_N, _minv(_kappa)) and _kappa_weight(_N) == -1
        and _rescale(_ratio) == _ratio and _kappa_weight(_ratio) == 0
        and _rescale(_Imw) == _mmul(_rescale(_N), _rescale(_ratio)) and _kappa_weight(_Imw) == -1)
# covariance f(N/kappa) = f(N)/kappa for a power law f = c N^a: as exact monomials in
# (N, kappa), f(N/kappa) = c N^a kappa^{-a} and f(N)/kappa = c N^a kappa^{-1}; equal iff a = 1.
def _lhs(a): return (a, -a)
def _rhs(a): return (a, Fraction(-1))
_as = (Fraction(1, 3), Fraction(2, 3), Fraction(1), Fraction(2), Fraction(-1, 3))
g.check("prop:covariance: for a power law c N^a the two sides of f(N/kappa) = f(N)/kappa are "
        "the monomials c N^a kappa^{-a} and c N^a kappa^{-1}, equal exactly when a = 1 "
        "(a = 1/3, 2/3, 1, 2, -1/3 tested; N^{2/3} and Zel'dovich-Weinberg's N^{-1/3} fail)",
        all((_lhs(a) == _rhs(a)) == (a == 1) for a in _as))
# and numerically exact at integer a on rational N, kappa: (N/kappa)^a == N^a / kappa iff a = 1
g.check("prop:covariance: at a = 1 and a = 2 on N = 7/3, kappa = 2 the identity (N/kappa)^a = N^a/kappa "
        "holds and fails respectively, as exact rationals",
        (Fraction(7, 3) / 2) ** 1 == Fraction(7, 3) ** 1 / 2 and (Fraction(7, 3) / 2) ** 2 != Fraction(7, 3) ** 2 / 2)
# RECORD: the six logarithmic ratios log(Im w)/log N on H_0 = 67.4 km/s/Mpc (floating point, not checked)
try:
    from math import log
    _H0_eV = 67.4 * 1000 / 3.0857e22 * 6.5821e-16          # H_0 in eV (hbar H_0)
    _MP_eV = 1.2209e28
    _masses = [("electron", float(ME) * 1e6), ("muon", float(MU) * 1e6), ("tau", float(MT) * 1e6),
               ("pion", 139.57e6), ("proton", 938.27e6), ("weak scale v", 246.22e9)]
    _Nf = _MP_eV / _H0_eV
    for _name, _m in _masses:
        _imw = _m / _H0_eV
        print("RECORD  %-13s Im w = %.3g, log(Im w)/log N = %.3f" % (_name, _imw, log(_imw) / log(_Nf)))
    print("RECORD  N = M_P/H_0 = %.3g" % _Nf)
except Exception as _e:
    print("RECORD lines skipped:", _e)

# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------

print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    raise SystemExit(1)
print("All checks pass.")
