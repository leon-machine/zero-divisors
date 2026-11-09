"""Exact checks: the counted thickness of R3 is free under every other premise, and no rule P2 licenses gives it.

The family: five-dimensional towers count through lam cell radii of the extra direction, three-dimensional
towers' sheets are mu cell radii apart (common within each reversal pair), R1, R2 and the sourcing rule as
stored; R3 is lam = mu = 1. Shares per unit of our three-volume: f5 = lam V3/V4 = 8 lam/(3 pi),
f3 = V3/(mu V2) = 4/(3 mu), mirror 1, so T(lam, mu) = 1 + 8/(3 mu) + 16 lam/(3 pi). pi is bracketed by
rationals (333/106, 355/113) and (3, 16/5); intervals are carried as (lo, hi) pairs of Fractions.
The tower spaces' metrics are read off GA generators (Gram matrices of the space directions) to show that a
tower's own cells and ours are balls of different dimension, so no isometry relates them.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI = (F(333, 106), F(355, 113))
PI_WIDE = (F(3), F(16, 5))

# representatives under P3 (time, space): this world, mirror, 3D pair, 5D pair; space dimension D
TOWERS = {6: ((1, 3), 3), 2: ((3, 1), 3), 1: ((2, 1), 2), 7: ((1, 2), 2), 3: ((3, 1), 4), 5: ((1, 4), 4)}
ORBITS = [(2, 6), (1, 7), (3, 5)]


def iv_mul(a, b):
    xs = [x * y for x in a for y in b]
    return (min(xs), max(xs))


def iv_add(*xs):
    return (sum((x[0] for x in xs), F(0)), sum((x[1] for x in xs), F(0)))


def iv_inv(a):
    assert a[0] > 0
    return (1 / a[1], 1 / a[0])


def pt(c):
    return (F(c), F(c))


def share(r, lam, mu, pi=PI):
    D = TOWERS[r][1]
    if D == 3:
        return pt(1)
    if D == 4:
        return iv_mul(pt(F(8, 3) * lam), iv_inv(pi))
    return pt(F(4, 3) / mu)


def ratio(lam, mu, pi=PI):
    return iv_add(*[share(r, lam, mu, pi) for r in TOWERS if r != 6])


def own_density(r, pi=PI):
    """R2: one quantum per unit ball of the tower's own space, 1/V_D (V_2 = pi, V_3 = 4 pi/3, V_4 = pi^2/2)."""
    D = TOWERS[r][1]
    v = {2: iv_mul(pt(1), pi), 3: iv_mul(pt(F(4, 3)), pi), 4: iv_mul(pt(F(1, 2)), iv_mul(pi, pi))}[D]
    return iv_inv(v)


def labels(r, eps):
    """Sector labels the descent deposits: residue, orientability (n = 0 mod 4), stored charge per common
    count (eps for the oriented pair, 0 for the odd towers, which carry no asymmetry)."""
    (p, q), D = TOWERS[r]
    oriented = (p + q) % 4 == 0
    return ((p - q) % 8, oriented, eps if oriented else F(0))


def space_signature(r):
    """Signature of the space directions of a tower (all generators but the single time, the one of the
    minority sign), from the GA Gram matrix of those generators."""
    (p, q), D = TOWERS[r]
    sq = GA.sig(p, q)
    time = 0 if p == 1 else p
    space = [i for i in range(p + q) if i != time]
    gram = [[GA.dot(GA.gen(i), GA.gen(j), sq) for j in space] for i in space]
    return GA.congruence_signature(gram)


def check_every_other_premise_is_blind_to_the_thickness():
    """Two members of the family, (1, 1) and (2, 1/2): R2's own-space densities, R1's common mass, every sector
    label and P2's within-orbit equalities are the same; the ratios differ ((5.36, 5.37) against (9.7, 9.8))."""
    premise("dark-matter.projection-every-towers-content-dilutes-ones")
    premise("dark-matter.total-function-thickness")
    premise("dark-matter.stored-asymmetry-charge-not-number")
    eps = F(1, 10 ** 9)
    models = [(F(1), F(1)), (F(2), F(1, 2))]
    for lam, mu in models:
        for a, b in ORBITS:
            assert share(a, lam, mu) == share(b, lam, mu)
            assert labels(a, eps)[1:] == labels(b, eps)[1:]
            assert labels(a, eps)[0] == (-labels(b, eps)[0]) % 8
    # R2's densities and the labels take no thickness argument; their values, for the record
    assert own_density(1) == (1 / PI[1], 1 / PI[0])
    assert own_density(3) == (2 / PI[1] ** 2, 2 / PI[0] ** 2)
    assert [labels(r, eps) for r in (6, 2, 1, 3)] == [(6, True, eps), (2, True, eps), (1, False, 0), (3, False, 0)]
    t1, t2 = ratio(*models[0]), ratio(*models[1])
    assert F(536, 100) < t1[0] and t1[1] < F(537, 100)
    assert F(97, 10) < t2[0] and t2[1] < F(98, 10)
    # the diagonal lam = mu = c is the stored T(c) = 1 + 8/(3c) + 16c/(3 pi)
    for c in (F(1, 2), F(1), F(3)):
        lo = 1 + F(8, 3) / c + F(16, 3) * c / PI[1]
        hi = 1 + F(8, 3) / c + F(16, 3) * c / PI[0]
        assert ratio(c, c) == (lo, hi)
    GA.check("the family leaves every premise but R3 unchanged and moves the ratio", True)


def check_family_reaches_every_ratio_above_one():
    """T is affine in lam with slope 16/(3 pi) > 0 and decreasing in mu, tends to 1 as lam -> 0 and mu grows,
    and is unbounded in lam: by continuity every value above 1 is some T(lam, mu). Exact values at a fixed pi."""
    premise("dark-matter.total-function-thickness")
    for pi, slope in ((F(3), F(16, 9)), (F(16, 5), F(5, 3))):
        one = (pi, pi)
        for mu in (F(1, 3), F(1), F(7)):
            t1, t2 = ratio(F(1), mu, one), ratio(F(2), mu, one)
            assert t2[0] - t1[0] == slope
        assert ratio(F(1), F(1), one)[0] - ratio(F(1), F(2), one)[0] == F(4, 3)
    assert ratio(F(1, 2), F(1, 3), PI_WIDE) == (F(59, 6), F(89, 9))
    small = ratio(F(1, 1000), F(1000), PI_WIDE)
    assert small == (F(1) + F(1, 375) + F(1, 600), F(1) + F(1, 375) + F(2, 1125))
    big = ratio(F(10), F(1), PI_WIDE)
    assert big[0] > F(20)
    GA.check("T covers (1, infinity)", True)


def check_own_cells_are_not_isometric_across_dimensions():
    """The space of a five-dimensional tower is definite of rank 4, ours of rank 3, a three-dimensional
    tower's of rank 2: balls of different rank, so no isometry carries one tower's cell to another's; members
    of one reversal orbit have spaces of the same rank."""
    premise("dark-matter.projection-every-towers-content-dilutes-ones")
    ranks = {}
    for r in TOWERS:
        pos, neg, zero = space_signature(r)
        assert zero == 0 and min(pos, neg) == 0
        ranks[r] = pos + neg
    assert ranks == {6: 3, 2: 3, 1: 2, 7: 2, 3: 4, 5: 4}
    for a, b in ORBITS:
        assert ranks[a] == ranks[b]
    GA.check("own cells: ranks 3, 2, 4; equal only within reversal orbits", True)


def check_licensed_shares_miss_r3():
    """Licensed cross-tower rules give share 1 (equal filling per common object) or 1/eps (charge reading,
    eps in (0, 1]); R3's five-dimensional share 8/(3 pi) lies in (5/6, 8/9), below 1, so it is neither. The
    licensed thicknesses are lam = 3 pi/8 in (9/8, 6/5) or 3 pi/(8 eps) >= 3 pi/8, never 1; the
    three-dimensional share 4/3 equals 1/eps only at eps = 3/4."""
    premise("dark-matter.stored-asymmetry-charge-not-number")
    premise("dark-matter.parallel-boundary-mode-spaces-one-wall")
    premise("dark-matter.no-coupling-rule-odd-towers-follows")
    f5 = share(3, F(1), F(1), PI_WIDE)
    assert f5 == (F(5, 6), F(8, 9))
    f5t = share(3, F(1), F(1), PI)
    assert f5t[1] < 1
    for eps in (F(1), F(3, 4), F(1, 2), F(1, 10 ** 9)):
        assert 1 / eps >= 1 > f5t[1]
    lam_lic = iv_mul(pt(F(3, 8)), PI_WIDE)
    assert lam_lic == (F(9, 8), F(6, 5))
    assert lam_lic[0] > 1
    assert share(1, F(1), F(1)) == pt(F(4, 3))
    assert [e for e in (F(1, 2), F(3, 4), F(1)) if 1 / e == F(4, 3)] == [F(3, 4)]
    GA.check("no licensed rule gives R3's five-dimensional share", True)


EXPORTS = {"T": ratio}
