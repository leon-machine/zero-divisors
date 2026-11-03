"""synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands: exact checks.

Model (the sourcing rule's setting of dark-matter.projection-every-towers-content-dilutes-ones):
shared scale factor a, hidden-direction scale b = a^beta of a five-dimensional tower (beta = 1
co-expanding, beta = 0 static), quanta conserved per comoving volume, matter homogeneous along
the hidden extent; three-dimensional towers' sheets comoving, one per unit comoving length.
With N = 1 quanta per comoving cell: our density n_b ~ a^-3, the sheet tower's own density
n_3 ~ a^-2, the five-dimensional tower's own density n_5 ~ (a^3 b)^-1. Cell radii r_D^D ~ 1/n_D.
The check, at exact rational scale factors and exponents (fourth powers to avoid roots):
  (a) R2's ratio of cell radii to ours: (r_3 / r_b) is constant for every beta; (r_5 / r_b)^4 is
      constant across samples iff beta = 1; the exponent of r_5 / r_b is (beta - 1)/4;
  (b) with R3 as a standing clause (thickness = current r_5), the projected density rho has
      rho^4 a^12 constant iff beta = 1, and the effective w = (beta - 1)/4, so -1/4 when static;
      the five-dimensional share then changes by (1 + z)^(3/4), between 189 and 190 for
      1 + z = 1090, and between 1.68 and 1.69 for 1 + z = 2;
  (c) with R3 as a deposit clause (thickness fixed and comoving with b), rho a^3 is constant for
      every beta (dust), the share is preserved;
  (d) the static deposit reading's counted thickness today is d_b,0 a_dep <= d_b,0 T_0 / T_desc;
      with d_b,0 < 1.02 m (dark-matter.thickness-not-gravitational-quantity), T_0 < 2.35e-13 GeV
      and T_desc >= 1e-3 GeV it is below 2.4e-10 m, under the 40 micrometre extra-dimension bound
      by more than 10^5;
  (e) the static standing reading's dark fraction in five-dimensional towers, 16/(11 pi + 16),
      lies between 0.316 and 0.317 (pi bracketed by 333/106 and 355/113).
Bounds are checked as integer parts (fourth roots, decimal orders, thousandths) so that
perturbing a literal breaks the check.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SAMPLES = [F(1), F(2), F(3), F(7, 2)]
BETAS = [F(0), F(1, 2), F(1), F(2)]


def power(x, k):
    """x^k for rational x > 0 and integer k."""
    return x ** k


def scale_b(a, beta):
    """b = a^beta for the sample exponents used (beta in {0, 1/2, 1, 2}): returns b^2 exactly."""
    return a ** int(2 * beta)


def densities(a, beta):
    b2 = scale_b(a, beta)               # b^2
    nb = 1 / power(a, 3)
    n3 = 1 / power(a, 2)
    n5_sq = 1 / (power(a, 6) * b2)      # n_5^2
    return nb, n3, n5_sq, b2


def ratio_r5_rb_pow24(a, beta):
    """(r_5 / r_b)^24 = n_b^8 / n_5^6 with r_5 = n_5^(-1/4), r_b = n_b^(-1/3)."""
    nb, _, n5_sq, _ = densities(a, beta)
    return power(nb, 8) / power(n5_sq, 3)        # ((r_5/r_b)^8)^3 = (r5/rb)^24


def ratio_r3_rb_pow6(a):
    nb, n3, _, _ = densities(a, F(0))
    return power(nb, 2) / power(n3, 3)           # (r_3/r_b)^6 = n_b^2 / n_3^3


def standing_rho_pow8(a, beta):
    """rho = n_5 r_5 with r_5 = n_5^(-1/4): rho^4 = n_5^3, so rho^8 = (n_5^2)^3."""
    _, _, n5_sq, _ = densities(a, beta)
    return power(n5_sq, 3)


def deposit_rho_sq(a, beta):
    """rho = n_5 t with t = b (fixed comoving thickness, unit at a = 1): rho^2 = n_5^2 b^2."""
    _, _, n5_sq, b2 = densities(a, beta)
    return n5_sq * b2


def iroot4(n):
    k = 0
    while (k + 1) ** 4 <= n:
        k += 1
    return k


def iroot_log10(x):
    """largest k with 10^k <= x, for rational x >= 1."""
    k = 0
    while 10 ** (k + 1) <= x:
        k += 1
    return k


def constant(vals):
    return len(set(vals)) == 1


def check_unit_ball_clauses_epoch():
    premise("dark-matter.projection-every-towers-content-dilutes-ones")
    premise("dark-matter.unit-ball-rule")
    premise("dark-matter.thickness-not-gravitational-quantity")
    premise("dark-matter.imported-inverse-square-law-short-range")

    # (a) R2's common radius across epochs
    assert constant([ratio_r3_rb_pow6(a) for a in SAMPLES])
    co = [beta for beta in BETAS if constant([ratio_r5_rb_pow24(a, beta) for a in SAMPLES])]
    assert co == [F(1)]
    for beta in BETAS:
        for a in SAMPLES[1:]:
            assert ratio_r5_rb_pow24(a, beta) == a ** int(6 * (beta - 1)) * ratio_r5_rb_pow24(F(1), beta)

    # (b) R3 as a standing clause: dust iff co-expanding, effective w = (beta - 1)/4
    dust = [beta for beta in BETAS
            if constant([standing_rho_pow8(a, beta) * power(a, 24) for a in SAMPLES])]
    assert dust == [F(1)]
    ws = []
    for beta in BETAS:
        w = (beta - 1) / 4
        ws.append(w)
        for a in SAMPLES[1:]:
            assert standing_rho_pow8(a, beta) * a ** int(24 * (1 + w)) == standing_rho_pow8(F(1), beta)
    assert ws == [F(-1, 4), F(-1, 8), F(0), F(1, 4)]
    # share drift (1 + z)^(3/4) as the integer part of a fourth root
    assert iroot4(1090 ** 3) == 189 and iroot4(100 ** 4 * 2 ** 3) == 168

    # (c) R3 as a deposit clause: dust for every beta
    for beta in BETAS:
        assert constant([deposit_rho_sq(a, beta) * power(a, 6) for a in SAMPLES])

    # (d) counted thickness today under the static deposit reading (metres, GeV)
    d_b0 = F(102, 100)
    T0 = F(235, 100) * F(1, 10 ** 13)
    T_desc_min = F(1, 1000)
    t0 = d_b0 * T0 / T_desc_min
    assert t0 == F(2397, 10 ** 13)
    bound = F(40) * F(1, 10 ** 6)
    assert iroot_log10(bound / t0) == 5

    # (e) five-dimensional fraction of the dark matter at the unit-ball value
    lo, hi = F(333, 106), F(355, 113)
    f5_lo, f5_hi = F(16) / (11 * hi + 16), F(16) / (11 * lo + 16)
    assert int(1000 * f5_lo) == 316 and int(1000 * f5_hi) == 316
    return True
