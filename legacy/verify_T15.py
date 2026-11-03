#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T15.py: exact-arithmetic verification of the computational identities of
"Neutrino Masses: The Empty Twistor, the Seesaw Scale, and the Bet at the Floor"
(Transport Papers, T15; printed Version 2.0).

v2.0 (2026-10-07): three checks added to Part B (B5), on the Standard-Model
paper's Pati-Salam branch, whose record values enter as brackets: the
requirement's coefficient sqrt(m_3 v_R), the coupling a top-like Dirac mass
would need, and the ordering of M_I between the two alpha values. 53 checks.

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rationals, Gaussian rationals, and
certified rational interval arithmetic (integer square roots with proved
brackets) for the measured splittings and angles, the quark masses, the
equilibrium mass and the physical constants.  No floating point anywhere.
Statement tags refer to the compiled paper.  Every observational input enters
as a bracket, printed in the paper where it is used, so that a refresh changes
the inputs, not the logic.
"""

from fractions import Fraction as F
from math import isqrt, comb
from itertools import permutations

import GA as g


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def sqrt_bounds(m, digits=14):
    """Rational lo, hi with lo^2 <= m <= hi^2."""
    m = F(m)
    scale = 10 ** digits
    lo_int = isqrt(m.numerator * scale * scale * m.denominator)
    lo = F(lo_int, m.denominator * scale)
    hi = F(lo_int + 1, m.denominator * scale)
    assert lo * lo <= m <= hi * hi
    return lo, hi


def isqrt_lo(m):
    return sqrt_bounds(m)[0]


def isqrt_hi(m):
    return sqrt_bounds(m)[1]


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)]
            for i in range(n)]


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def mat_vec(A, v):
    return [sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A))]


def scale(c, v):
    return [c * x for x in v]


def identity(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def det3(M):
    a, b, c = M[0]; d, e, f = M[1]; gg, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * gg) + c * (d * h - e * gg)


def inv3(M):
    a, b, c = M[0]; d, e, f = M[1]; gg, h, i = M[2]
    det = det3(M)
    adj = [[e * i - f * h, -(b * i - c * h), b * f - c * e],
           [-(d * i - f * gg), a * i - c * gg, -(a * f - c * d)],
           [d * h - e * gg, -(a * h - b * gg), a * e - b * d]]
    return [[x / det for x in row] for row in adj]


def inv2(M):
    (a, b), (c, d) = M
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]


J = [[F(1)] * 3 for _ in range(3)]
I3 = identity(3)
PI = [[I3[i][j] - F(1, 3) for j in range(3)] for i in range(3)]      # projector on u'^perp
u = [F(1), F(1), F(1)]
e2 = [F(1), F(-1), F(0)]
e3 = [F(1), F(1), F(-2)]


def aI_bJ(al, be):
    return [[al * I3[i][j] + be * J[i][j] for j in range(3)] for i in range(3)]


# ---------------------------------------------------------------------------
# Part A: the empty twistor (prop:empty)
# ---------------------------------------------------------------------------

dims = [comb(3, k) for k in range(4)]
g.check("prop:empty(1): Lambda^*(C^3) has graded dimensions 1, 3, 3, 1: exactly "
        "two one-dimensional (colour-singlet) grades, zero and three",
        dims == [1, 3, 3, 1] and [k for k in range(4) if dims[k] == 1] == [0, 3])

Ygrade = {k: F(-2 * k, 6) for k in range(4)}
g.check("prop:empty(1): under the weight rule Y = -k/3 the hypercharge-zero "
        "singlet is grade ZERO (the empty twistor) and grade three has Y = -1 "
        "(e^c after conjugation)",
        Ygrade[0] == 0 and Ygrade[3] == -1)


def anomaly_sums(a, b, c, d, e, f):
    """(Q, u^c, d^c, L, e^c, N) with multiplicities 6, 3, 3, 2, 1, 1."""
    s3 = 2 * a + b + c
    s2 = 3 * a + d
    sg = 6 * a + 3 * b + 3 * c + 2 * d + e + f
    sc = 6 * a ** 3 + 3 * b ** 3 + 3 * c ** 3 + 2 * d ** 3 + e ** 3 + f ** 3
    return (s3, s2, sg, sc)


def anomaly_sums_noN(a, b, c, d, e):
    return anomaly_sums(a, b, c, d, e, F(0))


Y = (F(1, 6), F(-2, 3), F(1, 3), F(-1, 2), F(1), F(0))
BL = (F(1, 3), F(-1, 3), F(-1, 3), F(-1), F(1), F(1))
mult = (6, 3, 3, 2, 1, 1)

g.check("prop:empty(2): the derived spectrum with Y_N = 0 satisfies all four "
        "anomaly conditions exactly", all(x == 0 for x in anomaly_sums(*Y)))

# the closed-form solution set (a, 2a - f, f - 4a, -3a, 6a - f, f)
ok = True
for a, f in ((F(1, 6), F(0)), (F(1, 6), F(1)), (F(1, 6), F(-5, 7)), (F(2), F(3, 4)),
             (F(-1, 3), F(1, 9)), (F(5), F(-2))):
    pt = (a, 2 * a - f, f - 4 * a, -3 * a, 6 * a - f, f)
    ok = ok and all(x == 0 for x in anomaly_sums(*pt))
g.check("prop:empty(2): every point of the closed form (a, 2a - f, f - 4a, -3a, "
        "6a - f, f) satisfies all four anomaly sums, at six (a, f) including "
        "a != 1/6", ok)

# the cubic reduces to 18 a (8a^2 + p - 6af + f^2) once the linear conditions hold
ok = True
for a, f, p in ((F(1, 6), F(1), F(2, 7)), (F(3), F(-1), F(5)), (F(-2, 5), F(1, 3), F(0))):
    # b, c with b + c = -2a and bc = p (need not be real; use the symmetric form)
    s = -2 * a
    b3c3 = s ** 3 - 3 * p * s
    cubic = 6 * a ** 3 + 3 * b3c3 + 2 * (-3 * a) ** 3 + (6 * a - f) ** 3 + f ** 3
    ok = ok and cubic == 18 * a * (8 * a ** 2 + p - 6 * a * f + f ** 2)
g.check("prop:empty(2): with the linear conditions imposed the cubic sum equals "
        "18 a (8a^2 + bc - 6af + f^2) identically in (a, f, bc)", ok)

g.check("prop:empty(2): all four anomaly sums vanish on B - L itself",
        all(x == 0 for x in anomaly_sums(*BL)))
mixed1 = sum(n * y * y * bl for n, y, bl in zip(mult, Y, BL))
mixed2 = sum(n * y * bl * bl for n, y, bl in zip(mult, Y, BL))
g.check("prop:empty(2): the two mixed cubic coefficients sum n Y^2 (B-L) and "
        "sum n Y (B-L)^2 vanish, so the cubic sum is zero identically along "
        "Y + t(B-L)", mixed1 == 0 and mixed2 == 0)
fam = True
for t in (F(1), F(-1), F(2), F(5, 7)):
    pt = tuple(y + t * bl for y, bl in zip(Y, BL))
    fam = fam and all(x == 0 for x in anomaly_sums(*pt)) and pt[5] == t
    # and it lies in the closed form after the u^c/d^c swap
    a, b, c, d, e, f = pt
    fam = fam and {b, c} == {2 * a - f, f - 4 * a} and d == -3 * a and e == 6 * a - f
g.check("prop:empty(2): Y + t(B-L) at t = 1, -1, 2, 5/7 (the values T12 runs) is "
        "anomaly-free with Y_N = t and lies in the closed form: anomaly "
        "cancellation leaves the fourth singlet's hypercharge FREE", fam)

# the linear decomposition of the closed form: a (1,2,-4,-3,6,0) + f (0,-1,1,0,-1,1),
# with the first vector 6Y (b, c swapped) and the second (B-L) - 2Y (b, c swapped)
def swap_bc(v):
    return (v[0], v[2], v[1], v[3], v[4], v[5])


v_a = (F(1), F(2), F(-4), F(-3), F(6), F(0))
v_f = (F(0), F(-1), F(1), F(0), F(-1), F(1))
ok = swap_bc(v_a) == tuple(6 * y for y in Y)
ok = ok and swap_bc(v_f) == tuple(bl - 2 * y for y, bl in zip(Y, BL))
for a_, f_ in ((F(1, 6), F(2)), (F(3), F(-1, 4)), (F(-2), F(7))):
    closed = (a_, 2 * a_ - f_, f_ - 4 * a_, -3 * a_, 6 * a_ - f_, f_)
    ok = ok and closed == tuple(a_ * x + f_ * yv for x, yv in zip(v_a, v_f))
    s_, t_ = 6 * a_ - 2 * f_, f_
    ok = ok and swap_bc(closed) == tuple(s_ * y + t_ * bl for y, bl in zip(Y, BL))
g.check("prop:empty(2): the closed form is linear in (a, f) and equals "
        "s Y + t (B-L) with s = 6a - 2f, t = f (after the u^c/d^c swap): the "
        "solution set is the two-dimensional span of Y and B - L", ok)

# the ray B-L itself: anomaly-free, Y_Q = 1/3 != 0, Y_N/Y_Q = 3, not in the family
ray_ok = all(x == 0 for x in anomaly_sums(*BL)) and BL[0] != 0 and BL[5] / BL[0] == 3
fam_ratio_ok = True
for t in (F(1), F(-1), F(2), F(5, 7), F(100), F(-1000)):
    pt = tuple(y + t * bl for y, bl in zip(Y, BL))
    fam_ratio_ok = fam_ratio_ok and pt[5] / pt[0] == 6 * t / (1 + 2 * t) and pt[5] / pt[0] != 3
g.check("prop:empty(2): the ray B - L is anomaly-free with Y_Q = 1/3 != 0 and "
        "Y_N/Y_Q = 3, while along the family Y + t(B-L) the ratio is "
        "6t/(1 + 2t), never 3: the ray is a solution outside the "
        "one-parameter family, the s = 0 member of the span", ray_ok and fam_ratio_ok)

# collapse at Y_N = 0
a = F(1, 6); f = F(0)
b_c = {2 * a - f, f - 4 * a}
g.check("prop:empty(2): with Y_N = 0 imposed the closed form collapses to "
        "Y_L = -1/2, Y(e^c) = 1, {Y(u^c), Y(d^c)} = {-2/3, 1/3}",
        -3 * a == F(-1, 2) and 6 * a - f == 1 and b_c == {F(-2, 3), F(1, 3)})

# prop:empty(3): delete N from an EXPLICIT spectrum (list of (name, colour dim,
# isospin dim, hypercharge)); the four sums are recomputed from the list
SPECTRUM = [("Q", 3, 2, F(1, 6)), ("u^c", 3, 1, F(-2, 3)), ("d^c", 3, 1, F(1, 3)),
            ("L", 1, 2, F(-1, 2)), ("e^c", 1, 1, F(1)), ("N", 1, 1, F(0))]


def sums_from_spectrum(spec):
    s3 = sum(ni * yy for (_, nc, ni, yy) in spec if nc == 3)         # [SU(3)]^2 U(1): triplets, weighted by isospin dim
    s2 = sum(nc * yy for (_, nc, ni, yy) in spec if ni == 2)         # [SU(2)]^2 U(1): doublets, weighted by colour dim
    sg = sum(nc * ni * yy for (_, nc, ni, yy) in spec)
    sc = sum(nc * ni * yy ** 3 for (_, nc, ni, yy) in spec)
    return (s3, s2, sg, sc)


six = sums_from_spectrum(SPECTRUM)
five = sums_from_spectrum([st for st in SPECTRUM if st[0] != "N"])
six_pert = sums_from_spectrum([st if st[0] != "N" else ("N", 1, 1, F(1, 2)) for st in SPECTRUM])
g.check("prop:empty(3): the four anomaly sums recomputed over the explicit "
        "five-state spectrum with N deleted equal the six-state sums at Y_N = 0 "
        "(and agree with the closed-form sums), while a singlet at Y_N = 1/2 "
        "changes the gravitational and cubic sums",
        len(SPECTRUM) == 6 and five == six == anomaly_sums(*Y)
        and six_pert != five and six_pert[2] != five[2] and six_pert[3] != five[3])


def on_Z6(triality, isoparity, Yval):
    return (F(triality, 3) + F(isoparity, 2) + Yval).denominator == 1


content = {"Q": (1, 1, F(1, 6)), "u^c": (-1, 0, F(-2, 3)), "d^c": (-1, 0, F(1, 3)),
           "L": (0, 1, F(-1, 2)), "e^c": (0, 0, F(1)), "N": (0, 0, F(0))}
g.check("prop:empty(3): the Z6 condition tau/3 + iota/2 + Y in Z holds for every "
        "state of the derived content, N at (0, 0, 0) included, and fails for "
        "an off-lattice singlet at Y = 1/2",
        all(on_Z6(*v) for v in content.values()) and not on_Z6(0, 0, F(1, 2)))

# ---------------------------------------------------------------------------
# Part B: the seesaw (prop:seesaw, lem:s3, prop:rankone, lem:breaking, rem:valuation)
# ---------------------------------------------------------------------------

# physical inputs, all bracketed
eV_per_m = (F(50676, 10 ** 4) * 10 ** 6, F(50678, 10 ** 4) * 10 ** 6)   # m^-1 per eV
Lam = (F(10, 10 ** 53), F(12, 10 ** 53))                                # m^-2
sqrt2 = sqrt_bounds(2)

# prop:seesaw(1): (l/L_H)^4 = 2 exactly for p = m: l^2 = 6/(sqrt2 Lambda), L_H^2 = 3/Lambda
ratio_sq_lo = F(6) / (sqrt2[1] * 3)      # = l^2 / L_H^2 lower
ratio_sq_hi = F(6) / (sqrt2[0] * 3)
g.check("prop:seesaw(1): for constituents at the neutrino's own scale the "
        "Lambda-term neutrino has (l/L_H)^2 = 2/sqrt2 = sqrt2, so l/L_H = 2^(1/4) "
        "exactly, independent of Lambda and m; and Lambda l^2/6 = 1 at l^2 = 2 L_H^2",
        ratio_sq_lo ** 2 <= 2 <= ratio_sq_hi ** 2)

# l for p = 100 GeV: l^2 = 6 m / (sqrt2 Lambda p) with m/p = 0.05 eV / 1e11 eV
m_over_p = F(5, 100) / 10 ** 11
l2_lo = 6 * m_over_p / (sqrt2[1] * Lam[1])
l2_hi = 6 * m_over_p / (sqrt2[0] * Lam[0])
l_lo, l_hi = isqrt_lo(l2_lo), isqrt_hi(l2_hi)
g.check("prop:seesaw(1): with weak-scale constituents (p = 100 GeV) the "
        "Lambda-term neutrino has extent l in (1.3e20, 1.5e20) m, by interval "
        "arithmetic on Lambda in (1.0, 1.2)e-52 m^-2",
        F(13, 10) * 10 ** 20 < l_lo and l_hi < F(15, 10) * 10 ** 20)

# the Casimir branch: C = 3 m^2 / Lambda
m_lo, m_hi = F(5, 100) * eV_per_m[0], F(5, 100) * eV_per_m[1]
C_lo, C_hi = 3 * m_lo ** 2 / Lam[1], 3 * m_hi ** 2 / Lam[0]
g.check("prop:seesaw(1): the Casimir branch m^2 = (Lambda/3) C at 0.05 eV needs "
        "C in (1.6e63, 2.0e63)", F(16, 10) * 10 ** 63 < C_lo and C_hi < 2 * 10 ** 63)

# prop:seesaw(2): the neutral bilinear census
names = ("Q", "u^c", "d^c", "L", "e^c", "N")
charges = {(names[i], names[j]): Y[i] + Y[j] for i in range(6) for j in range(i, 6)}
zeros = [k for k, v in charges.items() if v == 0]
g.check("prop:seesaw(2): of the 21 fermion bilinears of the derived content "
        "exactly one is hypercharge-neutral, N N; the Dirac bilinear L N carries "
        "-1/2", zeros == [("N", "N")] and charges[("L", "N")] == F(-1, 2))

# prop:seesaw(3): the block elimination, assembled
mD = [[F(1), F(2)], [F(3), F(6)]]
MR2 = [[F(10) ** 3, F(7)], [F(7), F(2) * 10 ** 3]]
MRinv = inv2(MR2)
light = mat_mul(mat_mul(mD, MRinv), transpose(mD))
ok = light == transpose(light)


def solve2(M, b):
    """Gaussian elimination with pivoting, independent of inv2."""
    (p, q), (r, t) = M
    if p == 0:
        (p, q), (r, t) = (r, t), (p, q); b = [b[1], b[0]]
    m = r / p
    t2 = t - m * q; b1 = b[1] - m * b[0]
    y1 = b1 / t2
    y0 = (b[0] - q * y1) / p
    return [y0, y1]


for x in ([F(1), F(0)], [F(2), F(-5)], [F(1, 3), F(7)]):
    rhs = mat_vec(transpose(mD), x)
    yv = scale(F(-1), solve2(MR2, rhs))                       # -M_R^-1 m_D^T x by elimination
    ok = ok and yv == scale(F(-1), mat_vec(MRinv, rhs))        # agrees with the adjugate inverse
    top = [sum(mD[i][k] * yv[k] for k in range(2)) for i in range(2)]
    bottom = [sum(transpose(mD)[i][k] * x[k] for k in range(2))
              + sum(MR2[i][k] * yv[k] for k in range(2)) for i in range(2)]
    ok = ok and top == scale(F(-1), mat_vec(light, x)) and bottom == [F(0), F(0)]
g.check("prop:seesaw(3): with y = -M_R^-1 m_D^T x computed by Gaussian "
        "elimination (independently of the adjugate inverse), the assembled "
        "block matrix [[0, m_D], [m_D^T, M_R]] applied to (x, y) gives "
        "(-m_D M_R^-1 m_D^T x, 0) exactly, and the light block is symmetric: "
        "the elimination identity", ok)

ok = True
for mDs, M in ((F(3), F(1000)), (F(7), F(250)), (F(1), F(10 ** 6))):
    disc = M * M + 4 * mDs * mDs
    r = sqrt_bounds(disc, digits=30)
    small_lo, small_hi = (M - r[1]) / 2, (M - r[0]) / 2
    target = -mDs * mDs / M
    err = mDs ** 4 / M ** 3
    ok = ok and abs(small_lo - target) < err and abs(small_hi - target) < err
    # and the exact eigenvalue is NOT the leading formula (the correction is real)
    ok = ok and not (small_lo <= target <= small_hi)
g.check("prop:seesaw(3): in the scalar case the small exact eigenvalue of "
        "[[0, m_D], [m_D, M_R]] lies within m_D^4/M_R^3 of -m_D^2/M_R (and is "
        "not equal to it), by exact square-root brackets", ok)

# lem:s3
def perm_matrix(p):
    return [[F(1) if p[i] == j else F(0) for j in range(3)] for i in range(3)]


def s3_invariant(M):
    return all(mat_mul(mat_mul(perm_matrix(p), M), transpose(perm_matrix(p))) == M
               for p in permutations(range(3)))


ok = all(s3_invariant(aI_bJ(al, be))
         for al, be in ((F(2), F(1)), (F(-1), F(5, 3)), (F(7, 2), F(0)), (F(0), F(4))))
ok = ok and not s3_invariant([[F(1), F(2), F(2)], [F(2), F(1), F(3)], [F(2), F(3), F(1)]])
ok = ok and not s3_invariant([[F(1), F(2), F(2)], [F(2), F(5), F(2)], [F(2), F(2), F(1)]])
for M in ([[F(3), F(1), F(1)], [F(1), F(3), F(1)], [F(1), F(1), F(3)]],
          [[F(0), F(-2), F(-2)], [F(-2), F(0), F(-2)], [F(-2), F(-2), F(0)]]):
    ok = ok and s3_invariant(M) and M[0][0] == M[1][1] == M[2][2] \
        and M[0][1] == M[0][2] == M[1][2]
g.check("lem:s3: alpha 1 + beta J is invariant under all six permutations "
        "(alpha = 0 included); symmetric matrices with unequal off-diagonals or "
        "unequal diagonals are not; invariant instances have equal diagonals "
        "and equal off-diagonals", ok)

ok = True
for al, be in ((F(2), F(1)), (F(-1), F(5, 3)), (F(7, 2), F(0)), (F(1, 5), F(-3))):
    M = aI_bJ(al, be)
    ok = ok and mat_vec(M, u) == scale(al + 3 * be, u)
    ok = ok and mat_vec(M, e2) == scale(al, e2) and mat_vec(M, e3) == scale(al, e3)
    ok = ok and det3(M) == al * al * (al + 3 * be)
    if al != 0 and al + 3 * be != 0:
        Minv = aI_bJ(1 / al, -be / (al * (al + 3 * be)))
        ok = ok and mat_mul(M, Minv) == I3 and inv3(M) == Minv
        proj = [[PI[i][j] / al + J[i][j] / (3 * (al + 3 * be)) for j in range(3)] for i in range(3)]
        ok = ok and proj == Minv
        proj_M = [[al * PI[i][j] + (al + 3 * be) * J[i][j] / 3 for j in range(3)] for i in range(3)]
        ok = ok and proj_M == M
g.check("lem:s3: u' has eigenvalue alpha + 3 beta, (1,-1,0) and (1,1,-2) have "
        "eigenvalue alpha, det = alpha^2 (alpha + 3 beta), the inverse formula "
        "agrees with the adjugate inverse, and the projector forms "
        "S = alpha Pi + M_3 J/3 and S^-1 = Pi/alpha + J/(3 M_3) hold", ok)

g.check("lem:s3: the two singular loci: det = 0 at alpha = 0 (the rank-one "
        "democratic case) and at alpha = -3 beta",
        det3(aI_bJ(F(0), F(4))) == 0 and det3(aI_bJ(F(-3), F(1))) == 0
        and det3(aI_bJ(F(2), F(1))) != 0)

# prop:rankone(0): the block decomposition and the scalar seesaw
ok = True
for al, be, dd in ((F(0), F(1), F(3)), (F(2), F(1), F(3)), (F(-1), F(5, 3), F(1, 2)),
                   (F(10) ** 6, F(10) ** 5, F(100))):
    M3 = al + 3 * be
    mDm = [[dd * x for x in row] for row in J]
    M = aI_bJ(al, be)
    # m_D annihilates u'^perp on the right; m_D u' = 3 d u'; M_R u' = M_3 u'; M_R on u'^perp = alpha
    ok = ok and mat_vec(mDm, e2) == [F(0)] * 3 and mat_vec(mDm, e3) == [F(0)] * 3
    ok = ok and mat_vec(mDm, u) == scale(3 * dd, u) and mat_vec(M, u) == scale(M3, u)
    ok = ok and mat_vec(M, e2) == scale(al, e2)
    # the democratic 2x2 block's light eigenvalue: -(3d)^2/M_3 at leading order
    if al != 0:
        Minv = inv3(M)
        ok = ok and mat_mul(mat_mul(J, Minv), J) == [[3 / M3] * 3 for _ in range(3)]
        lt = mat_mul(mat_mul(mDm, Minv), transpose(mDm))
        ok = ok and lt == [[3 * dd * dd / M3] * 3 for _ in range(3)]
        ok = ok and g.rank_of_vectors([r[:] for r in lt]) == 1
        ok = ok and mat_vec(lt, u) == scale((3 * dd) ** 2 / M3, u)
g.check("prop:rankone(0): m_D = dJ annihilates u'^perp, the democratic block is "
        "[[0, 3d], [3d, M_3]] with M_R = alpha on u'^perp (alpha = 0 included), "
        "and for alpha != 0 the full inversion gives J M_R^-1 J = 3 J/M_3 and "
        "the light matrix (3d^2/M_3) J, rank one with eigenvalue (3d)^2/M_3 "
        "along u'", ok)

mD3 = [[F(1), F(2), F(-1)], [F(2), F(4), F(-2)], [F(3), F(6), F(-3)]]
ok = g.rank_of_vectors([r[:] for r in mD3]) == 1
for MRv in ([[F(1), F(0), F(0)], [F(0), F(3), F(0)], [F(0), F(0), F(5)]],
            [[F(2), F(1), F(0)], [F(1), F(5), F(1)], [F(0), F(1), F(4)]],
            [[F(7), F(-2), F(1)], [F(-2), F(11), F(0)], [F(1), F(0), F(3)]]):
    lt = mat_mul(mat_mul(mD3, inv3(MRv)), transpose(mD3))
    ok = ok and g.rank_of_vectors([r[:] for r in lt]) == 1
g.check("prop:rankone(0): the seesaw of a rank-one m_D is rank one for every "
        "invertible M_R tested, S3-invariant or not", ok)

# obs:mixing: the charged-lepton Gram square c^2 J J^T and the light matrix
# (3d^2/M_3) J are both multiples of J: shared heavy eigenvector, and the
# requirement the data impose on the angle between the two heavy eigenvectors
charged = [[F(7, 2) * x for x in row] for row in mat_mul(J, transpose(J))]
lightJ = [[F(3, 100) * x for x in row] for row in J]
ok = mat_vec(charged, u) == scale(F(7, 2) * 9, u) and mat_vec(lightJ, u) == scale(F(9, 100), u)
ok = ok and all(mat_vec(M, v) == [F(0)] * 3 for M in (charged, lightJ) for v in (e2, e3))
s23sq = (F(44, 100), F(60, 100))
Utau3sq = ((1 - F(227, 10 ** 4)) * (1 - s23sq[1]), (1 - F(216, 10 ** 4)) * (1 - s23sq[0]))
g.check("obs:mixing: the charged-lepton Gram square and the light neutrino matrix "
        "are both multiples of J with the same heavy eigenvector u' and the same "
        "null plane (no leading-order mixing); the data require |U_tau3|^2 = "
        "c13^2 c23^2 in (0.39, 0.55) at sin^2 th23 in (0.44, 0.60), so the two "
        "heavy eigenvectors must separate by cos^2 in that bracket",
        ok and F(39, 100) < Utau3sq[0] and Utau3sq[1] < F(55, 100))

# lem:breaking: the exact identity
def outer(v, w):
    return [[v[i] * w[j] for j in range(3)] for i in range(3)]


ok = True
instances = (
    (F(2), F(1), F(3), F(1, 10), [[F(0), F(0), F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(1)]]),
    (F(1, 7), F(5), F(1, 2), F(3, 4), [[F(1), F(2), F(0)], [F(-1), F(3), F(1, 2)], [F(0), F(5), F(-2)]]),
    (F(10) ** 3, F(10) ** 6, F(100), F(6, 100), [[F(0), F(0), F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(1)]]),
)
for al, be, dd, delta, A in instances:
    M3 = al + 3 * be
    M = aI_bJ(al, be)
    Minv = inv3(M)
    JdA = [[J[i][j] + delta * A[i][j] for j in range(3)] for i in range(3)]
    mDm = [[dd * x for x in row] for row in JdA]
    lhs = mat_mul(mat_mul(mDm, Minv), transpose(mDm))
    APA = mat_mul(mat_mul(A, PI), transpose(A))
    w = mat_vec(JdA, u)
    rhs = [[dd * dd * delta * delta / al * APA[i][j] + dd * dd / (3 * M3) * w[i] * w[j]
            for j in range(3)] for i in range(3)]
    ok = ok and lhs == rhs
    ok = ok and w == [3 + delta * sum(A[i][k] * u[k] for k in range(3)) for i in range(3)]
# J X J = (sum X) J
X = [[F(1), F(2), F(-3)], [F(5), F(0), F(1, 2)], [F(-1), F(7), F(4)]]
ok = ok and mat_mul(mat_mul(J, X), J) == [[sum(sum(r) for r in X)] * 3 for _ in range(3)]
g.check("lem:breaking: m_D M_R^-1 m_D^T = (d^2 delta^2/alpha) A Pi A^T + "
        "(d^2/3M_3) w w^T exactly on three instances (one with a general A), "
        "w = (J + delta A) u', and J X J = (sum of entries of X) J", ok)

# the compression eigenvalues for A = e3 e3^T: A Pi A^T = (2/3) e3 e3^T has
# eigenvalue 2/3, but the compression Pi A Pi A^T Pi = (2/3)(Pi e3)(Pi e3)^T has
# eigenvalue (2/3)|Pi e3|^2 = 4/9 and a second eigenvalue 0 (rank one on u'^perp)
A = [[F(0), F(0), F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(1)]]
APA = mat_mul(mat_mul(A, PI), transpose(A))
comp = mat_mul(mat_mul(PI, APA), PI)
Pe3 = mat_vec(PI, [F(0), F(0), F(1)])
g.check("lem:breaking: for A = e_3 e_3^T, A Pi A^T = (2/3) e_3 e_3^T (eigenvalue "
        "2/3, range not orthogonal to u') while the compression Pi A Pi A^T Pi "
        "= (2/3)(Pi e_3)(Pi e_3)^T has eigenvalues 4/9 and 0: lambda_A = 4/9, "
        "lambda'_A = 0, so m_1 = 0 at this order (Premise (H) holds at this "
        "direction) and the two objects differ by the factor 2/3 exactly",
        APA == [[F(0)] * 3, [F(0)] * 3, [F(0), F(0), F(2, 3)]]
        and comp == [[F(2, 3) * Pe3[i] * Pe3[j] for j in range(3)] for i in range(3)]
        and sum(x * x for x in Pe3) * F(2, 3) == F(4, 9)
        and g.rank_of_vectors([r[:] for r in comp]) == 1)


def light_matrix(delta, R, A, dd=F(1)):
    """m_D M_R^-1 m_D^T with alpha = 1, M_3 = R, m_D = d(J + delta A)."""
    Minv = [[PI[i][j] + J[i][j] / (3 * R) for j in range(3)] for i in range(3)]
    mDm = [[dd * (J[i][j] + delta * A[i][j]) for j in range(3)] for i in range(3)]
    return mat_mul(mat_mul(mDm, Minv), transpose(mDm))


def eig_brackets_rank2(L):
    """L symmetric PSD of rank <= 2: charpoly = -lam (lam^2 - tr lam + e2) with e2
    the sum of principal 2x2 minors; the two nonzero eigenvalues by exact
    square-root brackets."""
    tr = L[0][0] + L[1][1] + L[2][2]
    e2 = (L[0][0] * L[1][1] - L[0][1] * L[1][0]) + (L[0][0] * L[2][2] - L[0][2] * L[2][0]) \
        + (L[1][1] * L[2][2] - L[1][2] * L[2][1])
    assert det3(L) == 0                                     # rank <= 2
    disc = tr * tr - 4 * e2
    r = sqrt_bounds(disc, digits=30)
    big = ((tr + r[0]) / 2, (tr + r[1]) / 2)
    small = ((tr - r[1]) / 2, (tr - r[0]) / 2)
    return small, big


# the charged-sector calibration of delta in the same texture: m_l = c(J + delta_c A),
# m_mu/m_tau = sigma_2/sigma_1 with sigma^2 the eigenvalues of m_l m_l^T (rank two)
def charged_ratio_sq(delta_c):
    ml = [[J[i][j] + delta_c * A[i][j] for j in range(3)] for i in range(3)]
    small, big = eig_brackets_rank2(mat_mul(ml, transpose(ml)))
    return small[0] / big[1], small[1] / big[0]


rc = charged_ratio_sq(F(286, 1000))
rc_lo, rc_hi = isqrt_lo(rc[0]), isqrt_hi(rc[1])
rc006 = charged_ratio_sq(F(6, 100))
g.check("rem:branch: in the paper's own texture m_l = c(J + delta_c e_3 e_3^T), "
        "delta_c = 0.286 gives m_mu/m_tau in (0.0590, 0.0600) by exact singular "
        "values (the measured 0.0595), while delta_c = 0.06 gives only 0.013; "
        "the leading-order relation (2/9) delta_c is within 7 percent",
        F(590, 10 ** 4) < rc_lo and rc_hi < F(600, 10 ** 4)
        and isqrt_hi(rc006[1]) < F(14, 1000)
        and abs(F(2, 9) * F(286, 1000) / rc_lo - 1) < F(7, 100))

ok = True
results = {}
for delta, R in ((F(286, 1000), 66), (F(6, 1000), 1284)):
    L = light_matrix(delta, F(R), A)
    small, big = eig_brackets_rank2(L)
    ratio = (small[0] / big[1], small[1] / big[0])
    results[(delta, R)] = ratio
    # the leading-order formula with lambda_A = 4/9 and with the wrong 2/3
    results[("lead", delta, R)] = (delta * delta * F(4, 9) / 9 * R, delta * delta * F(2, 3) / 9 * R)
r1 = results[(F(286, 1000), 66)]; r3 = results[(F(6, 1000), 1284)]
lead1 = results[("lead", F(286, 1000), 66)]; lead3 = results[("lead", F(6, 1000), 1284)]
g.check("lem:breaking / rem:branch: the light matrix diagonalised exactly at "
        "A = e_3 e_3^T (rank two, characteristic polynomial lambda times a "
        "quadratic): m_2/m_3 in (0.168, 0.172) at delta = 0.286, M_3/alpha = 66 "
        "(the instance chosen to land on the measured ratio), against 0.267 "
        "from the leading-order formula there (an overestimate of more than "
        "half); at delta = 0.006, M_3/alpha = 1284, the exact ratio is within "
        "4 percent of the lambda_A = 4/9 formula and about 2/3 of the "
        "A Pi A^T formula",
        F(168, 1000) < r1[0] and r1[1] < F(172, 1000)
        and F(26, 100) < lead1[0] < F(275, 1000) and lead1[0] > r1[1] * F(3, 2)
        and abs(r3[0] / lead3[0] - 1) < F(4, 100) and abs(r3[1] / lead3[0] - 1) < F(4, 100)
        and F(64, 100) < r3[0] / lead3[1] < F(69, 100))

# rem:branch: the exact ratio is not monotone in M_3/alpha at delta = 0.286: its value
# at 176 exceeds those at 66 and at 500, so m_2/m_3 = 0.17 has a second root past the peak
ratios_R = {}
for R_ in (66, 176, 500):
    small, big = eig_brackets_rank2(light_matrix(F(286, 1000), F(R_), A))
    ratios_R[R_] = (small[0] / big[1], small[1] / big[0])
g.check("rem:branch: at delta = 0.286 the exact m_2/m_3 is 0.17 at M_3/alpha = 66, "
        "above 0.23 at 176, and back below 0.17 at 500: not monotone, with a "
        "second root between 176 and 500 where the lemma's remainders dominate",
        ratios_R[176][0] > F(23, 100) and ratios_R[176][0] > ratios_R[66][1]
        and ratios_R[500][1] < ratios_R[176][0] and ratios_R[500][1] < F(17, 100))

# the leading-order relation of rem:branch at its own values: delta' = alpha/M_3
lead_dprime = F(286, 1000) ** 2 * F(4, 9) / (9 * F(17, 100))     # delta' forcing the formula to 0.17
g.check("rem:branch: forcing the leading-order relation delta^2 lambda_A/(9 delta') "
        "to 0.17 at delta = 0.286 gives delta' = 0.024, against the "
        "diagonalised 1/66 = 0.015: an overestimate by more than a half, as the "
        "remark says",
        F(23, 1000) < lead_dprime < F(25, 1000) and F(15, 10) < lead_dprime * 66 < F(17, 10))

# the splittings, bracketed (NuFIT 6.0 / PDG 2024, refresh at submission)
dm21 = (F(73, 10 ** 6), F(77, 10 ** 6))
dm31 = (F(245, 10 ** 5), F(255, 10 ** 5))
s21 = (isqrt_lo(dm21[0]), isqrt_hi(dm21[1]))
s31 = (isqrt_lo(dm31[0]), isqrt_hi(dm31[1]))

ratio_lo = isqrt_lo(1 - dm21[1] / dm31[0])
g.check("prop:rankone(1): inverted ordering needs m_1/m_2 >= sqrt(1 - dm21/dm31) "
        "> 0.98 at the measured splittings: its two heaviest states degenerate "
        "to two percent", ratio_lo > F(98, 100))


def sum_bracket(m1):
    """(lo, hi) of m1 + sqrt(m1^2 + dm21) + sqrt(m1^2 + dm31)."""
    lo = m1 + isqrt_lo(m1 * m1 + dm21[0]) + isqrt_lo(m1 * m1 + dm31[0])
    hi = m1 + isqrt_hi(m1 * m1 + dm21[1]) + isqrt_hi(m1 * m1 + dm31[1])
    return lo, hi


floor = sum_bracket(F(0))
g.check("prop:rankone(2): the kinematic floor sqrt(dm21^2) + sqrt(dm31^2) lies in "
        "(0.0580, 0.0593) eV by exact rational interval arithmetic",
        F(580, 10 ** 4) < floor[0] and floor[1] < F(593, 10 ** 4))

s_01 = sum_bracket(F(1, 10 ** 4)); s_1 = sum_bracket(F(1, 1000))
s_3 = sum_bracket(F(3, 1000)); s_10 = sum_bracket(F(1, 100)); s_m2 = sum_bracket(F(87, 10 ** 4))
s_35 = sum_bracket(F(35, 10 ** 4)); s_46 = sum_bracket(F(46, 10 ** 4))
g.check("prop:rankone(2) / prem:H / prediction table: the sum at m_1 = 0.1 meV exceeds the "
        "floor by 0.1007 meV (pinned inside (0.1005, 0.1010) at both ends of the bracket), lies in (0.0591, 0.0604) eV at 1 meV, exceeds "
        "0.0616 eV at 3 meV, exceeds 0.0736 eV (past the 0.064 eV bound) at "
        "10 meV, and exceeds 0.07 eV at m_1 = 8.7 meV (m_1 of order m_2)",
        F(1005, 10 ** 7) < s_01[0] - floor[0] < F(1010, 10 ** 7) and F(1005, 10 ** 7) < s_01[1] - floor[1] < F(1010, 10 ** 7)
        and F(591, 10 ** 4) < s_1[0] and s_1[1] < F(604, 10 ** 4)
        and s_3[0] > F(616, 10 ** 4) and s_10[0] > F(736, 10 ** 4) and s_10[0] > F(64, 1000)
        and s_m2[0] > F(7, 100))

g.check("prediction table: the sum crosses the 0.064 eV bound between m_1 = 3.5 meV (still "
        "below across the whole bracket) and 4.6 meV (above across the whole "
        "bracket): the refutation threshold on m_1 is about 4 meV, not 3",
        s_35[1] < F(64, 1000) and s_46[0] > F(64, 1000) and s_3[1] < F(64, 1000))

IO_lo = isqrt_lo(dm31[0] - dm21[1]) + s31[0]
IO_hi = isqrt_hi(dm31[1] - dm21[0]) + s31[1]
g.check("rem:currency(ii): the inverted-ordering floor from the same splittings "
        "lies in (0.097, 0.102) eV, above the normal floor",
        F(97, 1000) < IO_lo and IO_hi < F(102, 1000) and IO_lo > floor[1])

r_lo = isqrt_lo(dm21[0] / dm31[1]); r_hi = isqrt_hi(dm21[1] / dm31[0])
g.check("prop:rankone(2) / rem:branch: m_2/m_3 lies in (0.16, 0.18)",
        F(16, 100) < r_lo and r_hi < F(18, 100))

g.check("prop:doublebet: the quoted 0.052 eV bound (zero-extending prior) lies "
        "strictly below the floor: the arithmetic behind the prior-artefact "
        "reading", F(52, 1000) < floor[0])

# prop:rankone(3): m_bb with bracketed angles
s12sq = (F(295, 1000), F(319, 1000))
s13sq = (F(216, 10 ** 4), F(227, 10 ** 4))


def mbb_terms(m1):
    """brackets of the three terms c12^2 c13^2 m1, c13^2 s12^2 m2, s13^2 m3."""
    m2 = (isqrt_lo(m1 * m1 + dm21[0]), isqrt_hi(m1 * m1 + dm21[1]))
    m3 = (isqrt_lo(m1 * m1 + dm31[0]), isqrt_hi(m1 * m1 + dm31[1]))
    c13 = (1 - s13sq[1], 1 - s13sq[0])
    c12 = (1 - s12sq[1], 1 - s12sq[0])
    t1 = (c12[0] * c13[0] * m1, c12[1] * c13[1] * m1)
    t2 = (c13[0] * s12sq[0] * m2[0], c13[1] * s12sq[1] * m2[1])
    t3 = (s13sq[0] * m3[0], s13sq[1] * m3[1])
    return t1, t2, t3


t1, t2, t3 = mbb_terms(F(0))
plus = (t2[0] + t3[0], t2[1] + t3[1])
minus = (t2[0] - t3[1], t2[1] - t3[0])
g.check("prop:rankone(3): at m_1 = 0 the effective double-beta mass is in "
        "(3.5, 3.9) meV at relative phase 0 and (1.3, 1.7) meV at phase pi, "
        "from the angle brackets sin^2 th12 in (0.295, 0.319), sin^2 th13 in "
        "(0.0216, 0.0227) and the splitting brackets",
        F(35, 10 ** 4) < plus[0] and plus[1] < F(39, 10 ** 4)
        and F(13, 10 ** 4) < minus[0] and minus[1] < F(17, 10 ** 4))

t1, t2, t3 = mbb_terms(F(1, 10 ** 4))
shift_max = t1[1] + (t2[1] - mbb_terms(F(0))[1][1]) + (t3[1] - mbb_terms(F(0))[2][1])
g.check("prem:H: at m_1 = 0.1 meV each double-beta value moves by less than "
        "0.1 meV (the m_1 term is below 0.08 meV and the m_2, m_3 terms move "
        "negligibly)", shift_max < F(1, 10 ** 4) and t1[1] < F(8, 10 ** 5))

t1, t2, t3 = mbb_terms(F(1, 1000))
patterns = []
for sb in (1, -1):
    for sc in (1, -1):
        lo = t1[0] + (t2[0] if sb > 0 else -t2[1]) + (t3[0] if sc > 0 else -t3[1])
        hi = t1[1] + (t2[1] if sb > 0 else -t2[0]) + (t3[1] if sc > 0 else -t3[0])
        patterns.append((min(abs(lo), abs(hi)) if lo * hi > 0 else F(0), max(abs(lo), abs(hi))))
span_lo = min(p[0] for p in patterns); span_hi = max(p[1] for p in patterns)
g.check("prem:H: at m_1 = 1 meV the four real sign patterns already span "
        "0.6-4.6 meV (the low end below 0.7, the high end above 4.5), so the "
        "two-value statement needs m_1 well below 1 meV",
        span_lo < F(7, 10 ** 4) and span_hi > F(45, 10 ** 4)
        and span_lo > F(6, 10 ** 4) and span_hi < F(47, 10 ** 4))

# rem:valuation: M_3 at both ends of Hypothesis (U), from brackets
GeV = 10 ** 9
m3_eV = s31                                                    # (49.4975, 50.4975) meV, printed as (49.4, 50.5)
m3_GeV = (m3_eV[0] / GeV, m3_eV[1] / GeV)
mt = (F(17228, 100), F(17286, 100)); mb = (F(413, 100), F(423, 100))
MR_top = (mt[0] ** 2 / m3_GeV[1], mt[1] ** 2 / m3_GeV[0])
MR_bot = (mb[0] ** 2 / m3_GeV[1], mb[1] ** 2 / m3_GeV[0])
MU = 2 * 10 ** 16
sq_ratio = ((mt[0] / mb[1]) ** 2, (mt[1] / mb[0]) ** 2)
g.check("rem:valuation: M_3 = m_t^2/m_3 in (5.8e14, 6.2e14) GeV at the top of "
        "(U) and m_b^2/m_3 in (3.3e11, 3.7e11) GeV at the bottom, from bracketed "
        "m_t in (172.28, 172.86) (PDG 2024, 172.57 +/- 0.29), m_b, m_3; (m_t/m_b)^2 in "
        "(1.6e3, 1.8e3); M_U/M_3 at 2e16 GeV in (33.1, 34.1) at the top (printed "
        "as 33 to 34) and (5.5e4, 6.0e4) at the bottom (the quoted 5.7e4)",
        F(58, 10) * 10 ** 14 < MR_top[0] and MR_top[1] < F(62, 10) * 10 ** 14
        and F(33, 10) * 10 ** 11 < MR_bot[0] and MR_bot[1] < F(37, 10) * 10 ** 11
        and F(16, 10) * 10 ** 3 < sq_ratio[0] and sq_ratio[1] < F(18, 10) * 10 ** 3
        and F(331, 10) < MU / MR_top[1] and MU / MR_top[0] < F(341, 10)
        and F(55, 10) * 10 ** 4 < MU / MR_bot[1] and MU / MR_bot[0] < 6 * 10 ** 4)

# the charged-sector ratios quoted in the text (PDG 2024 central values, refresh at submission)
me, mmu, mtau = F(511, 10 ** 6), F(10566, 10 ** 5), F(17769, 10 ** 4)      # GeV
mu_q, mc = F(216, 10 ** 5), F(127, 100)
g.check("rem:branch / prem:H: the charged-sector ratios the paper prints, at "
        "central values: m_mu/m_tau in (0.055, 0.065), m_e/m_mu in (0.004, "
        "0.006), m_u/m_c in (0.0015, 0.0025)",
        F(55, 1000) < mmu / mtau < F(65, 1000)
        and F(4, 1000) < me / mmu < F(6, 1000) and F(15, 10 ** 4) < mu_q / mc < F(25, 10 ** 4))

g.check("rem:branch: the calibration target of delta_c is the script's own "
        "m_mu/m_tau = 0.10566/1.7769 = 0.0595 (PDG central values), inside the "
        "(0.0590, 0.0600) window, and delta_c = 0.286 reproduces it to better "
        "than one part in a thousand",
        F(590, 10 ** 4) < mmu / mtau < F(600, 10 ** 4)
        and abs(mmu / mtau - rc_lo) < mmu / mtau / 1000 and abs(mmu / mtau - rc_hi) < mmu / mtau / 1000)

# B4: the factor at the unconditional unification-condition scale 7e14 GeV
MU_uncond = 7 * 10 ** 14
g.check("rem:valuation: at the Standard-Model-coefficient unification scale 7e14 GeV "
        "the factor M_U/M_3 at the top of (U) lies in (1.159, 1.192), whose "
        "endpoints round to the printed 1.16 and 1.19",
        F(1159, 1000) < MU_uncond / MR_top[1] and MU_uncond / MR_top[0] < F(1192, 1000)
        and round(MU_uncond / MR_top[1], 2) == F(116, 100)
        and round(MU_uncond / MR_top[0], 2) == F(119, 100))

alpha_top = (MR_top[0] / 66, MR_top[1] / 66)
alpha_bot = (MR_bot[0] / 66, MR_bot[1] / 66)
g.check("rem:branch: on the branch M_3/alpha = 66 the pair N_perp lies in "
        "(8.9e12, 9.2e12) GeV at the top of (U) and (5.1e9, 5.5e9) GeV at the "
        "bottom (the quoted 9e12 and 5.1e9), nearly two orders (log10 66 = 1.8) below M_3; "
        "against the top of T14's range, 6e14 GeV, that is between 1.8 and 5.1 "
        "orders (about two to five)",
        F(89, 10) * 10 ** 12 < alpha_top[0] and alpha_top[1] < F(92, 10) * 10 ** 12
        and F(51, 10) * 10 ** 9 < alpha_bot[0] and alpha_bot[1] < F(55, 10) * 10 ** 9
        and 10 ** 1 * 6 < 6 * 10 ** 14 / alpha_top[0] < 10 ** 2
        and 10 ** 5 < 6 * 10 ** 14 / alpha_bot[0] < F(13, 10) * 10 ** 5)

# B5: the Standard-Model paper's Pati-Salam branch (rem:valuation, rem:branch),
# on that paper's record values entered as brackets (T12 Props 10.10, 11.2):
# v_R = M_I / g_R(M_I), M_I, M_U, and the top mass run to M_I.
vR = (F(41, 10) * 10 ** 10, F(42, 10) * 10 ** 10)
MI = (F(19, 10) * 10 ** 10, F(20, 10) * 10 ** 10)
MU_ps = F(336, 100) * 10 ** 16
mt_MI = F(92)
m3vR = (m3_GeV[0] * vR[0], m3_GeV[1] * vR[1])          # GeV^2, = m_D^2 / f_J
g.check("rem:valuation (Pati-Salam branch): m_D^2/f_J = m_3 v_R lies in "
        "(1.42^2, 1.46^2) GeV^2 for m_3 in (49.4, 50.5) meV and v_R in "
        "(4.1, 4.2)e10 GeV, so sqrt(m_3 v_R) is the requirement's coefficient 1.44",
        F(142, 100) ** 2 < m3vR[0] and m3vR[1] < F(146, 100) ** 2)
fJ_top = (mt_MI ** 2 / m3vR[1], mt_MI ** 2 / m3vR[0])
g.check("rem:valuation (Pati-Salam branch): a top-like Dirac mass, m_t(M_I) = 92 "
        "GeV, would need f_J = m_t^2/(m_3 v_R) in (3900, 4200), the quoted 'near 4000'",
        F(3900) < fJ_top[0] and fJ_top[1] < F(4200))
g.check("rem:valuation (Pati-Salam branch): alpha at the bottom of (U) < M_I < "
        "alpha at the top, and M_U = 3.36e16 GeV lies above M_3 at both ends",
        alpha_bot[1] < MI[0] and MI[1] < alpha_top[0]
        and MU_ps > MR_top[1] and MU_ps > MR_bot[1])

# ---------------------------------------------------------------------------
# Part C: leptogenesis (prop:leptogenesis)
# ---------------------------------------------------------------------------

def qmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)]
            for i in range(n)]


def qdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def qmat(rows):
    return [[g.qi(x) for x in row] for row in rows]


QJ = qmat([[1, 1, 1]] * 3)
bases = (
    qmat([[1, 1, 1], [1, -1, 0], [1, 1, -2]]),
    qmat([[1, 1, 1], [0, 1, -1], [2, -1, -1]]),
)

# (1) the alignment result in two eigenbases
ok = True
for E in bases:
    Et = [[E[j][i] for j in range(3)] for i in range(3)]
    for y in (g.qi(2, 3), g.qi(-1, 1), g.qi(5)):
        Yq = [[y * g.qi(1) for _ in range(3)] for _ in range(3)]
        YdY = qmul(qdag(Yq), Yq)
        T = qmul(qmul(E, YdY), Et)
        ok = ok and all(T[i][j] == g.qi(0) for i in range(3) for j in range(3) if i != j)
        ok = ok and T[1][1] == g.qi(0) and T[2][2] == g.qi(0) and T[0][0] != g.qi(0)
        YE = qmul(Yq, Et)
        ok = ok and all(YE[i][j] == g.qi(0) for i in range(3) for j in (1, 2))
        ok = ok and YdY == [[g.qi(3) * y.conj() * y for _ in range(3)] for _ in range(3)]
g.check("prop:leptogenesis(1): for Y_D = y J with complex y, in two exact "
        "eigenbases of u'^perp the representation of Y_D^dag Y_D = 3|y|^2 J has "
        "all six off-diagonal entries zero and only the u' diagonal entry nonzero, "
        "and Y_D annihilates u'^perp: the alignment result, basis-independent", ok)

# (2) the degenerate pair is resonant: the normalised (2,3) combination is O(1) in delta
E = bases[0]
Et = [[E[j][i] for j in range(3)] for i in range(3)]
Ac = qmat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
Ac = [[Ac[i][j] + (g.qi(0, 1) if (i, j) in ((1, 2), (2, 1)) else g.qi(0)) for j in range(3)] for i in range(3)]
norms = [g.qi(3), g.qi(2)]                  # |e_1|^2, |e_2|^2


def qabs2(z):
    return z * z.conj()


vals23 = []
vals12 = []
for delta in (F(1, 10), F(1, 100), F(1, 1000)):
    dq = g.qi(delta)
    Yq = [[QJ[i][j] + dq * Ac[i][j] for j in range(3)] for i in range(3)]
    T = qmul(qmul(E, qmul(qdag(Yq), Yq)), Et)
    r23 = qabs2(T[1][2]) / (T[1][1] * T[2][2])                # normalisation-invariant
    r12 = qabs2(T[0][1]) / (T[0][0] * T[0][0]) * norms[0] / norms[1]   # orthonormalised
    vals23.append(r23); vals12.append(r12 / g.qi(delta * delta))
# closed form: on u'^perp, T_ij = |y|^2 delta^2 <A e_i, A e_j>, so the pair's
# combination is cos^2 of the angle between A e_2 and A e_3, exactly, for every A
def pair_combination_closed(Amat):
    Ae2 = [sum(Amat[i][k] * g.qi(e2[k]) for k in range(3)) for i in range(3)]
    Ae3 = [sum(Amat[i][k] * g.qi(e3[k]) for k in range(3)) for i in range(3)]
    inner = sum(Ae2[i].conj() * Ae3[i] for i in range(3))
    n2 = sum(Ae2[i].conj() * Ae2[i] for i in range(3)); n3 = sum(Ae3[i].conj() * Ae3[i] for i in range(3))
    return qabs2(inner) / (n2 * n3)


A2c = qmat([[1, 0, 2], [0, 3, 1], [2, 1, -1]])
A2c = [[A2c[i][j] + (g.qi(0, 2) if (i, j) in ((0, 2), (2, 0)) else g.qi(0)) for j in range(3)] for i in range(3)]
vals23b = []
for delta in (F(1, 10), F(1, 1000)):
    dq = g.qi(delta)
    Yq = [[QJ[i][j] + dq * A2c[i][j] for j in range(3)] for i in range(3)]
    T = qmul(qmul(E, qmul(qdag(Yq), Yq)), Et)
    vals23b.append(qabs2(T[1][2]) / (T[1][1] * T[2][2]))
g.check("prop:leptogenesis(2): with Y_D = J + delta A (A complex symmetric) the "
        "degenerate pair's combination |T23|^2/(T22 T33) is exactly the same at "
        "delta = 1e-1, 1e-2, 1e-3 and equals its closed form cos^2(A e_2, A e_3) "
        "for two structurally different A (O(1) in delta, the resonant "
        "configuration), while |T12|^2/T11^2 scales as delta^2 (its quotient by "
        "delta^2 stays inside a fixed bracket)",
        vals23[0] == vals23[1] == vals23[2] and vals23[0] != g.qi(0)
        and vals23[0] == pair_combination_closed(Ac)
        and vals23b[0] == vals23b[1] == pair_combination_closed(A2c) and vals23b[0] != vals23[0]
        and all(v.im == 0 and F(1, 100) < v.re < F(5, 100) for v in vals12)
        and abs(vals12[0].re - vals12[2].re) < vals12[2].re / 2)

# the washout strength
m_star = (F(106, 10 ** 5), F(115, 10 ** 5))
K = (s31[0] / m_star[1], s31[1] / m_star[0])
g.check("prop:leptogenesis(2): K = m_3/m_* lies in (43, 48) for bracketed m_3 "
        "and m_* in (1.06, 1.15) meV, containing the quoted 45",
        F(43) < K[0] and K[1] < F(48) and K[0] < 45 < K[1])

# (3) the interference term with a complex breaking phase
Ar = qmat([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
results = {}
for label, ph in (("theta = 0", g.qi(1)), ("theta = pi", g.qi(-1)), ("(3+4i)/5", g.qi(F(3, 5), F(4, 5)))):
    dq = g.qi(F(1, 10)) * ph
    Yq = [[QJ[i][j] + dq * Ar[i][j] for j in range(3)] for i in range(3)]
    T = qmul(qmul(E, qmul(qdag(Yq), Yq)), Et)
    t13 = T[0][2]
    results[label] = (t13 * t13).im
g.check("prop:leptogenesis(3): with Y_D = J + delta e^{i theta} A the interference "
        "term Im[((Y_D^dag Y_D)_{1j})^2] between N_u' and the pair, in the heavy "
        "eigenbasis, is exactly zero at theta = 0 and theta = pi and nonzero at "
        "e^{i theta} = (3 + 4i)/5",
        results["theta = 0"] == 0 and results["theta = pi"] == 0 and results["(3+4i)/5"] != 0)

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
