"""neutrino.empty-twistor: exact checks of statements (1) to (3).

Hypercharges are listed in the order (Q, u^c, d^c, L, e^c, N) with multiplicities (6, 3, 3, 2, 1, 1);
the four anomaly sums are [SU(3)]^2 U(1) = 2a + b + c, [SU(2)]^2 U(1) = 3a + d, gravitational
6a + 3b + 3c + 2d + e + f and cubic 6a^3 + 3b^3 + 3c^3 + 2d^3 + e^3 + f^3.

(1) (imported identification, its computable core) The grades of the exterior algebra of C^3,
counted on the blades of three generators in GA, have dimensions 1, 3, 3, 1; the one-dimensional
(colour-singlet) grades are exactly 0 and 3, matching the two singlets of 3bar + 3bar + 1 + 1; the
weight rule Y = -k/3 gives Y = 0 at grade 0 and -1 at grade 3, whose conjugate +1 is Y(e^c).
(2) The solution set. Every point (a, 2a-f, f-4a, -3a, 6a-f, f) solves all four sums (25 points).
With the linear conditions imposed the cubic sum is 18 a (8a^2 + p - 6af + f^2), p = bc, on a grid
fixing the polynomial (degrees 3, 3, 1 in a, f, p); the quadratic y^2 + 2ay + p at that p has
roots 2a-f and f-4a (sum -2a, product p, discriminant 4(3a-f)^2). Completeness on a grid: for
a != 0, once the linear conditions hold, all four sums vanish exactly when b is one of the two roots
(15 trial values of b plus the roots at each of 9 (a, f): 18 hits, two per (a, f)). The closed form is a (1,2,-4,-3,6,0) + f (0,-1,1,0,-1,1),
which after the u^c/d^c swap is s Y + t (B - L) with s = 6a - 2f, t = f, and Y_Q = a. Y_Q != 0 is
needed: at a = 0 the anomaly-free point (0, 1, -1, 0, 0, 0) is not in the span. The family
Y + t(B-L) has Y_N = t and Y_N/Y_Q = 6t/(1+2t), never 3 (6t - 3(1+2t) = -3), while the ray B - L is
anomaly-free with Y_N/Y_Q = 3; the mixed cubic coefficients vanish. At Y_N = 0 the closed form is
the derived spectrum. The SU(2) doublet count (colours of Q plus L) is 4, even.
(3) Recomputing the four sums over an explicit state list with N deleted leaves them unchanged at
Y_N = 0 and changes the gravitational and cubic sums at Y_N = 1/2; tau/3 + iota/2 + Y is an integer on
every derived state, N at (0, 0, 0) included, and not at Y = 1/2. The orientation clause is the
imported flag covariance (no computable content).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

Y = (F(1, 6), F(-2, 3), F(1, 3), F(-1, 2), F(1), F(0))
BL = (F(1, 3), F(-1, 3), F(-1, 3), F(-1), F(1), F(1))
MULT = (6, 3, 3, 2, 1, 1)
AF_POINTS = [(a, f) for a in (F(1, 6), F(2), F(-1, 3), F(5), F(3, 4))
             for f in (F(0), F(1), F(-5, 7), F(3, 4), F(1, 9))]
A_GRID = (F(1), F(2), F(-1, 3), F(1, 6))
F_GRID = (F(0), F(1), F(-2), F(5, 7))
P_GRID = (F(2, 7), F(-3))
COMPLETE_AF = [(a, f) for a in (F(1, 6), F(1), F(-2, 3)) for f in (F(0), F(1), F(-5, 7))]
B_TRIALS = [F(k, 6) for k in range(-7, 8)]
FAMILY_T = (F(1), F(-1), F(2), F(5, 7), F(100), F(-1000))


def sums(a, b, c, d, e, f):
    return (2 * a + b + c, 3 * a + d, 6 * a + 3 * b + 3 * c + 2 * d + e + f,
            6 * a ** 3 + 3 * b ** 3 + 3 * c ** 3 + 2 * d ** 3 + e ** 3 + f ** 3)


def free(pt):
    return all(x == 0 for x in sums(*pt))


def swap(v):
    return (v[0], v[2], v[1], v[3], v[4], v[5])


def in_span(pt):
    """Is pt (or its u^c/d^c swap) s Y + t (B-L)? Solve from Y_N = t and Y_Q = s/6 + t/3."""
    for v in (pt, swap(pt)):
        t = v[5]
        s = 6 * (v[0] - t / 3)
        if v == tuple(s * y + t * bl for y, bl in zip(Y, BL)):
            return True
    return False


def check_single_spinor_singlets():
    premise("neutrino.imported-derived-content-singlets")
    dims = [sum(1 for b in GA.all_blades(3) if len(b) == k) for k in range(4)]
    ok = dims == [1, 3, 3, 1]
    singlet_grades = [k for k in range(4) if dims[k] == 1]
    ok = ok and singlet_grades == [0, 3]
    column = (3, 3, 1, 1)
    ok = ok and len(singlet_grades) == sum(1 for x in column if x == 1)
    hyper = {k: F(-k, 3) for k in range(4)}
    ok = ok and hyper[0] == 0 and hyper[3] == -1 and -hyper[3] == Y[4]
    GA.check("Lambda(C^3) grades 1, 3, 3, 1: singlets at grades 0 (Y = 0) and 3 (Y = -1, e^c)", ok)
    return ok


def check_anomaly_solution_set_is_the_span():
    ok = True
    for a, f in AF_POINTS:
        pt = (a, 2 * a - f, f - 4 * a, -3 * a, 6 * a - f, f)
        ok = ok and free(pt) and in_span(pt)
        ok = ok and pt == tuple(a * x + f * z for x, z in zip((1, 2, -4, -3, 6, 0), (0, -1, 1, 0, -1, 1)))
        s, t = 6 * a - 2 * f, f
        ok = ok and swap(pt) == tuple(s * y + t * bl for y, bl in zip(Y, BL)) and pt[0] == a
    for a in A_GRID:
        for f in F_GRID:
            for p in P_GRID:
                s = -2 * a
                b3c3 = s ** 3 - 3 * p * s
                cubic = 6 * a ** 3 + 3 * b3c3 + 2 * (-3 * a) ** 3 + (6 * a - f) ** 3 + f ** 3
                ok = ok and cubic == 18 * a * (8 * a * a + p - 6 * a * f + f * f)
            p0 = -8 * a * a + 6 * a * f - f * f
            r1, r2 = 2 * a - f, f - 4 * a
            ok = ok and r1 + r2 == -2 * a and r1 * r2 == p0 and 4 * a * a - 4 * p0 == 4 * (3 * a - f) ** 2
    hits = 0
    for a, f in COMPLETE_AF:
        roots = {2 * a - f, f - 4 * a}
        for b in sorted(set(B_TRIALS) | roots):
            pt = (a, b, -2 * a - b, -3 * a, 6 * a - f, f)
            ok = ok and free(pt) == (b in roots)
            hits += free(pt)
    ok = ok and hits == 18
    control = (F(0), F(1), F(-1), F(0), F(0), F(0))
    ok = ok and free(control) and not in_span(control)
    GA.check("the anomaly solutions with Y_Q != 0 are exactly the span of Y and B - L (up to u^c <-> d^c)", ok)
    return ok


def check_ray_family_and_collapse():
    premise("neutrino.imported-derived-content-singlets")
    ok = free(Y) and free(BL)
    ok = ok and sum(n * y * y * bl for n, y, bl in zip(MULT, Y, BL)) == 0
    ok = ok and sum(n * y * bl * bl for n, y, bl in zip(MULT, Y, BL)) == 0
    for t in FAMILY_T:
        pt = tuple(y + t * bl for y, bl in zip(Y, BL))
        ok = ok and free(pt) and pt[5] == t
        ok = ok and pt[5] / pt[0] == 6 * t / (1 + 2 * t) and 6 * t - 3 * (1 + 2 * t) == -3
    ok = ok and BL[5] / BL[0] == 3 and BL[0] != 0
    a = F(1, 6)
    collapsed = (a, 2 * a, -4 * a, -3 * a, 6 * a, F(0))
    ok = ok and swap(collapsed) == Y
    doublets = (MULT[0] + MULT[3]) // 2      # SU(2) doublets: colours of Q, plus L
    ok = ok and doublets == 4 and doublets % 2 == 0
    GA.check("Y + t(B-L) has Y_N = t, ratio 6t/(1+2t) != 3; ray B-L has ratio 3; Y_N = 0 is the derived spectrum", ok)
    return ok


def check_anomaly_invisible_on_the_lattice():
    premise("neutrino.imported-derived-content-singlets")
    spectrum = [("Q", 3, 2, Y[0]), ("u^c", 3, 1, Y[1]), ("d^c", 3, 1, Y[2]),
                ("L", 1, 2, Y[3]), ("e^c", 1, 1, Y[4]), ("N", 1, 1, Y[5])]

    def from_list(spec):
        s3 = sum(ni * yy for (_, nc, ni, yy) in spec if nc == 3)
        s2 = sum(nc * yy for (_, nc, ni, yy) in spec if ni == 2)
        sg = sum(nc * ni * yy for (_, nc, ni, yy) in spec)
        scb = sum(nc * ni * yy ** 3 for (_, nc, ni, yy) in spec)
        return (s3, s2, sg, scb)

    six = from_list(spectrum)
    five = from_list([s for s in spectrum if s[0] != "N"])
    moved = from_list([s if s[0] != "N" else ("N", 1, 1, F(1, 2)) for s in spectrum])
    ok = six == five == sums(*Y) == (0, 0, 0, 0)
    ok = ok and moved[2] != five[2] and moved[3] != five[3] and moved[:2] == five[:2]
    lattice = {"Q": (1, 1), "u^c": (-1, 0), "d^c": (-1, 0), "L": (0, 1), "e^c": (0, 0), "N": (0, 0)}
    ok = ok and all((F(lattice[nm][0], 3) + F(lattice[nm][1], 2) + yy).denominator == 1
                    for nm, _, _, yy in spectrum)
    ok = ok and (F(0, 3) + F(0, 2) + F(1, 2)).denominator != 1
    GA.check("deleting N at Y_N = 0 changes no anomaly sum; N sits on the Z6 lattice", ok)
    return ok
