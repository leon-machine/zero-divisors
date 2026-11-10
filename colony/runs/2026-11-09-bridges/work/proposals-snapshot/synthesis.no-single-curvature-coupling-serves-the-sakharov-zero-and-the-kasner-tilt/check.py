"""synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt: exact checks.

(1) The attachment's helicity-0 module (conformal energies k = l + 1, multiplicity k^2) against the operator
    Box + xi R on the unit three-sphere (R = 6, Laplace eigenvalues l(l + 2) on harmonic polynomials of degree l in
    four variables, built here in Cl(4,0) coordinates by counting): equal spectra exactly at xi = 1/6.
(2) The induced quadratic coefficient B over the stored tilt window at gauge parameter one, and the counter-statement
    with the gauge parameter free (heat-kernel cut-off): zero and tilt together at alpha = 1/3 + 4 xi.
(3) Elimination of xi between B = 0 and the index 3 - sqrt(6 xi) at the isotropic Kasner point: no integer
    generation number in the three-sigma window; all comparisons of square roots are done on squares.
(4) The stored tree-level values and the matching clause.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ4 = GA.sig(4, 0)
TILT = F(-351, 10000)
SIGMA = F(42, 10000)
XI_WINDOW = (F(15225, 10000), F(15481, 10000))       # the stored window of the tilt fit
LEVELS = range(0, 12)
GENERATIONS = range(1, 200)
DOUBLETS = range(1, 17)
FIRST_HIT = (14, 32)


def harmonic_dimension(l):
    """Dimension of the harmonic polynomials of degree l in the four coordinates of Cl(4,0) vectors."""
    n = len(SQ4)

    def monomials(deg):
        count = 1
        for j in range(1, n):
            count = count * (deg + j) // j
        return count
    return monomials(l) - (monomials(l - 2) if l >= 2 else 0)


def B_feynman(n_g, n_s, xi):
    return 16 * n_g - 48 + n_s * (1 - 6 * xi)


def check_attachment_scalar_spectrum_is_the_conformal_one_only():
    premise("synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations")
    premise("synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike")
    premise("synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point")
    v = GA.add(GA.gen(0), GA.scal(F(2), GA.gen(1)), GA.scal(F(-1), GA.gen(3)))
    GA.check("Q(v) is the Euclidean square in Cl(4,0)", GA.eq(GA.mul(v, v, SQ4), GA.sc(6)))
    R = 6
    for l in LEVELS:
        k = l + 1
        GA.check("harmonic polynomials of degree l have dimension (l+1)^2", harmonic_dimension(l) == k * k)
        GA.check("attachment multiplicity k^2 - s^2 at s = 0", (l + 1) * (l + 2 * 0 + 1) == k * k)
        # squared frequency l(l+2) + xi R equals k^2 exactly when xi = 1/6
        for xi in (F(1, 6), F(0), F(1, 2), F(3, 2), XI_WINDOW[0], XI_WINDOW[1]):
            same = l * (l + 2) + xi * R == k * k
            GA.check("spectra agree only at conformal coupling", same == (xi == F(1, 6)))
        GA.check("the coupling is fixed by any one level", (k * k - l * (l + 2)) == F(1, 6) * R)
    # the stored dictionary at the conformal weight w = 1 - n/2 = -1 in four dimensions
    w = F(-1)
    GA.check("first reading -w/6", -w / 6 == F(1, 6))
    GA.check("second reading -w(w+3)/12", -w * (w + 3) / 12 == F(1, 6))
    return True


def check_induced_coefficient_is_negative_over_the_tilt_window():
    premise("synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off")
    premise("synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike")
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    premise("synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free")
    lo, hi = XI_WINDOW
    GA.check("B = 0 at conformal coupling, three generations", B_feynman(3, 8, F(1, 6)) == 0)
    GA.check("B = 8 at minimal coupling, three generations", B_feynman(3, 8, F(0)) == 8)
    GA.check("B at the lower end", B_feynman(3, 8, lo) == F(-6508, 100))
    GA.check("B at the upper end", B_feynman(3, 8, hi) == F(-663088, 10000))
    # zero in the generation number: 16 n_g - 48 + 8 (1 - 6 xi) = 0  <=>  n_g = 5/2 + 3 xi
    for xi, want in ((lo, F(70675, 10000)), (hi, F(71443, 10000))):
        n_zero = F(5, 2) + 3 * xi
        GA.check("zero of B in n_g", 16 * n_zero - 48 + 8 * (1 - 6 * xi) == 0 and n_zero == want)
        GA.check("between seven and eight", 7 < n_zero < 8)
    GA.check("the stored zero xi = 1/6 + (n_g - 3)/3 at seven generations is 3/2",
             F(1, 6) + F(7 - 3, 3) == F(3, 2) and B_feynman(7, 8, F(3, 2)) == 0)
    # gauge parameter free: vector weight alpha - 5 (heat-kernel cut-off)
    for xi in (lo, hi):
        alpha_zero = F(1, 3) + 4 * xi
        GA.check("zero in alpha", 48 + 12 * (alpha_zero - 5) + 8 * (1 - 6 * xi) == 0)
        GA.check("alpha at the zero exceeds 6", alpha_zero > 6)
        for alpha in (F(0), F(1), F(3), F(6)):
            GA.check("B < 0 for alpha <= 6", 48 + 12 * (alpha - 5) + 8 * (1 - 6 * xi) < 0)
    # counter-statement: gauge parameter free, zero and tilt together
    xi = F(153, 100)
    alpha = F(1, 3) + 4 * xi
    six_lo, six_hi = (3 - (TILT + 3 * SIGMA)) ** 2, (3 - (TILT - 3 * SIGMA)) ** 2
    GA.check("at alpha = 1/3 + 4 xi the coefficient vanishes inside the tilt window",
             48 + 12 * (alpha - 5) + 8 * (1 - 6 * xi) == 0 and six_lo <= 6 * xi <= six_hi and alpha == F(1936, 300))
    GA.check("and is positive for larger alpha", 48 + 12 * (alpha + F(1, 10) - 5) + 8 * (1 - 6 * xi) > 0)
    GA.check("the bounds 6.4233 and 6.5257 to four places",
             abs(F(1, 3) + 4 * lo - F(64233, 10000)) < F(1, 10000) and abs(F(1, 3) + 4 * hi - F(65257, 10000)) < F(1, 10000))
    GA.check("at alpha = 1 the same coupling gives a negative coefficient", B_feynman(3, 8, xi) < 0)
    return True


def check_no_generation_number_has_zero_coefficient_and_the_measured_tilt():
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    premise("synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point")
    premise("synthesis.capacity-and-sakharov-readings-leave-the-generation-number-free")
    # index n - 1 = 3 - sqrt(6 xi); three-sigma window on sqrt(6 xi), compared on squares
    root_lo = 3 - (TILT + 3 * SIGMA)
    root_hi = 3 - (TILT - 3 * SIGMA)
    GA.check("window on the root", (root_lo, root_hi) == (F(30225, 10000), F(30477, 10000)))
    sq_lo, sq_hi = root_lo ** 2, root_hi ** 2
    GA.check("the stored xi window is this one, rounded to four places",
             abs(sq_lo / 6 - XI_WINDOW[0]) < F(1, 10000) and abs(sq_hi / 6 - XI_WINDOW[1]) < F(1, 10000))
    hits = []
    for n_h in DOUBLETS:
        for n_g in GENERATIONS:
            six_xi = 1 + F(16 * n_g - 48, 4 * n_h)          # B = 0 with N_S = 4 n_h
            GA.check("B vanishes there", B_feynman(n_g, 4 * n_h, six_xi / 6) == 0)
            if sq_lo <= six_xi <= sq_hi:
                hits.append((n_h, n_g))
    GA.check("no content with at most thirteen doublets meets the window",
             [h for h in hits if h[0] < FIRST_HIT[0]] == [])
    GA.check("the first content meeting it has fourteen doublets and thirty-two generations",
             min(hits) == FIRST_HIT and 1 + F(16 * 32 - 48, 4 * 14) == F(65, 7))
    # two doublets: 6 xi = 2 n_g - 5, index 3 - sqrt(2 n_g - 5)
    for n_g in GENERATIONS:
        GA.check("two doublets", 1 + F(16 * n_g - 48, 8) == 2 * n_g - 5)
    GA.check("three generations: index 2", (3 - 2) ** 2 == 2 * 3 - 5)
    GA.check("seven generations: index exactly 0", (3 - 0) ** 2 == 2 * 7 - 5)
    GA.check("seven is below the window, eight above", 2 * 7 - 5 < sq_lo and 2 * 8 - 5 > sq_hi)
    GA.check("scale invariance is more than eight standard deviations from the measured tilt",
             8 * SIGMA < -TILT < 9 * SIGMA)
    # the stored tree-level values stay blue: 6 xi <= 3 for xi in [0, 1/2], and sqrt(3) < 3
    for xi in (F(0), F(1, 6), F(3, 16), F(1, 2)):
        GA.check("tree-level couplings are below the window", 6 * xi <= 3 and 6 * xi < sq_lo and 3 < 3 ** 2)
    # matching needs B > 0: xi < 1/6 at three generations and two doublets, disjoint from the window
    GA.check("B > 0 iff xi < 1/6", all((B_feynman(3, 8, xi) > 0) == (xi < F(1, 6))
                                      for xi in (F(0), F(1, 7), F(1, 6), F(1, 5), XI_WINDOW[0], XI_WINDOW[1])))
    return True
