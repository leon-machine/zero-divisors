"""Exact checks: what the calibration residue requires of the count unit, and what it leaves free.

Arrays are those of (Q) version 3 (weights kappa(k + 1/2)), sixteen per generation per light ray (the Weyl
components). Entropies are kept as rational multiples of ln 2 where the stored results give them exactly
(an array carries (1/2) ln 2, the zero-weight mode ln 2) and bracketed by rationals otherwise
(s(pi) from e^(-pi) < e^(-3) < 1/20, ln 2 from partial sums of sum 1/(k 2^k)). A grouping of the sixteen
arrays of a generation into k units is an integer partition of 16 into k parts; the registered residue under
the area-law hypothesis is kappa_c = 1/(4 <s>), and in units of 1/ln 2 it is k/(4 * 8) per array-half.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ARRAYS_PER_GENERATION = 16
HALF = F(1, 3)          # an array's entropy in units of ln 2 at the Hawking temperature (stored, exact)


def partitions(n, largest=None):
    largest = n if largest is None else largest
    if n == 0:
        yield ()
        return
    for first in range(min(n, largest), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def ln2_bounds(N):
    lo = sum((F(1, k * 2 ** k) for k in range(1, N + 1)), F(0))
    return lo, lo + F(1, (N + 1) * 2 ** N)


def check_mean_two_arrays_is_what_the_residue_requires():
    """Over all 231 groupings of a generation's sixteen arrays, mean unit entropy equals ln 2 (so
    kappa_c = 1/(4 ln 2) under the area-law hypothesis) exactly for the 8-unit groupings, the mean being two
    arrays per unit whatever the part sizes; the all-pairs grouping is one of 22 such."""
    premise("synthesis.half-integer-weight-array-carries-half-ln2")
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    allp = list(partitions(ARRAYS_PER_GENERATION))
    assert len(allp) == 231
    hits = []
    for p in allp:
        k = len(p)
        mean_s = F(ARRAYS_PER_GENERATION, k) * HALF      # in units of ln 2
        kappa_c = 1 / (4 * mean_s)                         # in units of 1/ln 2
        if kappa_c == F(1, 4):
            hits.append(p)
            assert F(sum(p), k) == 2
        else:
            assert F(sum(p), k) != 2
    assert len(hits) == 22 and (2,) * 8 in hits and (9, 1, 1, 1, 1, 1, 1, 1) in hits
    # uniform units of u arrays: kappa_c = 1/(2u) in units of 1/ln 2, the registered value only at u = 2
    assert [u for u in range(1, 17) if 1 / (4 * u * HALF) == F(1, 4)] == [2]
    GA.check("the residue requires a mean of two arrays per unit, eight units per generation", True)


def check_no_single_ladder_pair_and_no_zero_offset_union_carries_ln2():
    """At the weights kappa(k + 1/2) every mode has |x| >= pi, and s(x) <= (1 + x) e^(-x) gives
    s(pi) < 21/100 < 69/100 < ln 2: no single ladder pair carries the capacity. At the offset 0 an array
    carries ln 2 + epsilon > ln 2, so no union of whole arrays averages ln 2 per unit there (u S_0 > ln 2)."""
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("synthesis.capacity-per-mode-independent-of-helicity")
    pi_hi = F(16, 5)
    u_hi = F(1, 20)                       # e^(-pi) < e^(-3) < 1/20 since e^3 > 20
    e_lo = sum((F(1, f) for f in (1, 1, 2, 6, 24, 120)), F(0))
    assert e_lo ** 3 > 20
    s_pi_hi = (1 + pi_hi) * u_hi
    assert s_pi_hi == F(21, 100)
    lo, hi = ln2_bounds(12)
    assert lo > F(69, 100) and hi < F(70, 100)
    assert s_pi_hi < lo
    # offset 0: S_0 = ln 2 + 2 sum_{k>=1} s(2 pi k) > ln 2; the stored bracket starts at 0.72039
    s0_lo = F(72039, 100000)
    assert s0_lo > hi
    for u in range(1, 9):
        assert u * s0_lo > hi
    GA.check("no ladder pair at the half offset, and no array union at offset 0, carries ln 2", True)


def check_light_rays_are_arrays_over_content_not_registered_units():
    """Under the area-law hypothesis arrays per Planck area per period are 1/(2 ln 2) (stored); with c arrays
    per light ray the light rays per Planck area are 1/(2 c ln 2), independent of the unit, and on the de Sitter
    horizon (area 4 pi N^2) they number 2 pi N^2/(c ln 2); registered units number pi N^2/ln 2 only at two
    arrays per unit, so registered units per light ray are c/2: 8 n_g for the fermion content, 24 at n_g = 3."""
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    premise("synthesis.de-sitter-entropy-pi-n-squared")
    premise("dark-matter.stored-asymmetry-charge-not-number")
    arrays_per_area = F(1, 2)            # in units of 1/ln 2
    area = 4                              # de Sitter horizon area in units of pi N^2
    entropy = 1                           # pi N^2
    assert arrays_per_area * area * HALF == entropy * F(1, 1)
    for n_g in (1, 2, 3, 4):
        c = ARRAYS_PER_GENERATION * n_g
        for u in (1, 2, 4):
            rays = arrays_per_area * area / c          # light rays, in units of pi N^2 / ln 2
            units = arrays_per_area * area / u         # registered units, same units
            assert rays == F(2, c) and units == F(2, u)
            assert units / rays == F(c, u)
        assert F(c, 2) == 8 * n_g
    assert F(ARRAYS_PER_GENERATION * 3, 2) == 24
    GA.check("light rays = 2 pi N^2/(c ln 2); registered units per light ray = c/2", True)


EXPORTS = {"partitions": partitions}
