"""synthesis.seeding-remainder-excludes-perturbative-pati-salam: exact checks.

All quantities in GeV, as exact rationals. Inputs are the stored record-level values, each
taken at the end of its rounding or error interval that weakens the conclusion:
remainder over the baryons 4.364 - 0.065, baryons per unit entropy 8.65e-11 (8.7e-11 rounded),
kappa_s = 145.3, reduced Planck mass 2.435e18, v_R = 4.25e10 (4.2e10 rounded), 4 pi with
pi < 355/113, m_3 = 49.4 meV, m_b = 4.23 GeV. The proton mass 0.938272 GeV is the PDG value.
Square and fourth roots are never taken: every comparison is made between fourth powers,
and the stated values are pinned by exact floors.
The production coefficients are those of clause (v) of the pair-production theorem (premise), per
creation event of two quanta, computed here from its closed form at the bath (4, 45, 12):
16087 pi^3/20736000 per real massless vector and 1519247 pi^3/82944000 for a Standard-Model content
(the earlier 2.3e-3 and 0.078 of the imported Fact were too small). pi^3 is not approximated by a
decimal: as elsewhere in this check pi is taken between 333/106 and 355/113, and each coefficient is
used at the end of that bracket that weakens the conclusion being tested. The factor 2 in A/(2c) is
the two quanta of each creation event.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def floor(x):
    return x.numerator // x.denominator


def gauge_dimension(a, b, over_c):
    return a * a + b * b - 1 if over_c else (a * (a - 1) + b * (b - 1)) // 2


def alpha_over_pi3(cj, tj, n_s=4, n_w=45, n_v=12):
    """alpha/pi^3 of the pair-production theorem's clause (v) for one produced species, per creation event:
    (1/17280)[(c_j (N_s + 12 N_v) + 5 tau_j N_s)/225 + 49 c_j N_w/4800], bath scalars at zero curvature coupling."""
    return (F(cj * (n_s + 12 * n_v) + 5 * tj * n_s, 225) + F(49 * cj * n_w, 4800)) / 17280


def check_seeding_remainder_excludes_perturbative_pati_salam():
    premise("dark-matter.seeding-gravity-floor-dark-towers-temperature")
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    premise("dark-matter.imported-massless-graviton-production-rate")
    premise("dark-matter.population-count-one-share-half-percent")
    premise("dark-matter.coefficients-floors-they-give-what-gravity")
    premise("standard-model.what-angle-asks-neutrino-sector")
    premise("standard-model.chain")
    premise("dark-matter.ceiling-valued-inherited-success")
    premise("neutrino.r-descent-reheats-below-lower-heavy")
    premise("synthesis.gauge-algebra-by-tower")
    E = F(10)
    rem = F(4364, 1000) - F(65, 1000)
    eta = F(865, 100) / E ** 11
    mp = F(938272, 10 ** 6)
    kappa = F(1453, 10)
    MP = F(2435, 1000) * E ** 18
    vR = F(425, 100) * E ** 10
    pi_hi = F(355, 113)
    m3 = F(494, 10) / E ** 12
    mb = F(423, 100)

    # kappa_s from its formula at g = g_s = 100: kappa^2 = (pi^2 g/90)(2 pi^2 g_s/45)^2
    for pi in (F(333, 106), pi_hi):
        k2 = pi ** 2 * 100 / 90 * (2 * pi ** 2 * 100 / 45) ** 2
        assert (k2 - kappa ** 2) ** 2 < 400

    # A = c T_seed^4 (no factor 2): 3 kappa M_P^3 times the remainder's mass per unit entropy
    A = 3 * kappa * MP ** 3 * rem * mp * eta
    assert floor(A / E ** 44) == 21958
    assert (F(1217, 1000) * E ** 12) ** 4 < A < (F(1218, 1000) * E ** 12) ** 4

    # (i) Pati-Salam chain, f_J <= 4 pi, T_desc <= M_3
    M3_ps = 4 * pi_hi * vR
    assert floor(M3_ps / E ** 8) == 5340
    c_star = A / (2 * M3_ps ** 4)
    assert floor(c_star * 10 ** 4) == 134949

    # the derived coefficients over pi^3 (exact), and their two ends from 333/106 < pi < 355/113
    pi_lo = F(333, 106)
    r_s, r_w, r_v = alpha_over_pi3(1, 1), alpha_over_pi3(3, 0), alpha_over_pi3(12, 0)
    r_sm = 4 * r_s + 45 * r_w + 12 * r_v
    assert r_v == F(16087, 20736000) and r_sm == F(1519247, 82944000)
    a_vec_lo, a_vec_hi = r_v * pi_lo ** 3, r_v * pi_hi ** 3
    assert F(24052, 10 ** 6) < a_vec_lo < a_vec_hi < F(24056, 10 ** 6)       # 2.4055e-2 per vector
    assert F(5678, 10 ** 4) < r_sm * pi_lo ** 3 < r_sm * pi_hi ** 3 < F(568, 10 ** 3)   # 0.568 per content
    # c* in vector species and in Standard-Model contents
    assert 560 < c_star / a_vec_hi < c_star / a_vec_lo < 562
    assert floor(c_star / (r_sm * pi_hi ** 3)) == floor(c_star / (r_sm * pi_lo ** 3)) == 23

    dims = [gauge_dimension(2, 2, False), gauge_dimension(2, 2, False),
            gauge_dimension(1, 3, True), gauge_dimension(1, 3, True)]
    assert dims == [2, 2, 9, 9]
    c_vec_lo, c_vec_hi = sum(dims) * a_vec_lo, sum(dims) * a_vec_hi
    c_four_sm_lo, c_four_sm_hi = 4 * r_sm * pi_lo ** 3, 4 * r_sm * pi_hi ** 3
    assert F(5291, 10 ** 4) < c_vec_lo < c_vec_hi < F(5293, 10 ** 4)          # 0.529
    assert F(2271, 1000) < c_four_sm_lo < c_four_sm_hi < F(2272, 1000) < F(228, 100)    # 2.27
    # the exclusion, at the larger end of each c (the end that weakens it)
    assert A / (2 * c_four_sm_hi) > (F(156, 100) * M3_ps) ** 4
    assert A / (2 * c_vec_hi) > (F(224, 100) * M3_ps) ** 4
    assert A / (2 * F(228, 100)) > (F(83, 10) * E ** 11) ** 4
    assert A / (2 * c_four_sm_hi) > (F(196, 10) * vR) ** 4
    assert (F(64, 10) ** 2 / m3) ** 4 < A / (2 * c_four_sm_hi)
    assert m3 * M3_ps < F(52, 10) ** 2
    # the form of T14's signpost (central inputs, no factor 2) at the vectors' c: 1.22e12 c^(-1/4) in
    # (1.43, 1.44)e12 GeV, below the 2e12 GeV it gives for c <= 0.14
    for c in (c_vec_lo, c_vec_hi):
        assert (F(143, 100) * E ** 12) ** 4 * c < (F(122, 100) * E ** 12) ** 4 < (F(144, 100) * E ** 12) ** 4 * c
    # one-loop M_I of the same chain over the two-loop value exceeds the tolerance 2.56
    assert floor(F(32, 10) * E ** 11 / (F(19, 10) * E ** 10)) == 16

    # (ii) bottom end of (U): M_3 = m_b^2 / m_3
    M3_b = mb ** 2 / m3
    assert floor(M3_b / E ** 8) == 3622
    assert floor(A / (2 * M3_b ** 4) * 1000) == 63789

    # (iii) top end of (U), low-scale reading
    M3_t = F(17228, 100) ** 2 / (F(505, 10) / E ** 12)
    assert floor(M3_t / E ** 11) == 5877
    assert (M3_t / 66) ** 4 > A / c_vec_lo
    assert M3_t / vR > 4 * pi_hi * 1000
    # ceiling reading (both ends lowered by 10): T_desc <= M_3 still met, the /66 clause fails at the
    # vectors' c
    assert (M3_t / 10) ** 4 > A / c_vec_lo
    M3_t_hi = F(17286, 100) ** 2 / m3
    assert M3_t_hi < F(61, 10) * E ** 14
    assert (M3_t_hi / 660) ** 4 < A / (2 * c_vec_hi)
    # but it holds at four Standard-Model contents' c (lower ends of c and of M_3); the inequality
    # changes direction between c = 1.5 (fails over the whole range of M_3) and c = 1.8 (holds over it)
    assert (M3_t / 660) ** 4 > A / (2 * c_four_sm_lo)
    # the margin is thin: with the ceiling reading lowering M_3 by 11 in place of 10 the clause fails again,
    # even at the upper end of c and of M_3 (66 x 11 = 726)
    assert (M3_t_hi / 726) ** 4 < A / (2 * c_four_sm_hi)
    assert (M3_t / 726) ** 4 < A / (2 * c_four_sm_lo)
    assert (M3_t_hi / 660) ** 4 < A / (2 * F(15, 10)) and (M3_t / 660) ** 4 > A / (2 * F(18, 10))

    # the chain's Dirac mass at f_J = 1: m_D^2 = m_3 v_R at 50 meV and 4.2e10 lies in (1.44^2, 1.45^2)
    md2 = F(50, 1000) / E ** 9 * F(42, 10) * E ** 10
    assert F(144, 100) ** 2 < md2 < F(145, 100) ** 2
    return True
