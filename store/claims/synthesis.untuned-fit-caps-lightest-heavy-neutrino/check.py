"""synthesis.untuned-fit-caps-lightest-heavy-neutrino: exact checks.

(a) The norm inequality, in its trace form, on exact instances: integer 3x3 Dirac matrices and
    diagonal Majorana matrices (Takagi form); equality on a rank-one instance.
(b) The numbers: untuned fit e = 0.045 GeV, m_3(M_I) >= 25 meV, against the seeding constant
    A = c T_seed^4 rederived from the imported rate, with kappa_s from its formula, and against
    M_I = 1.9e10 GeV. Record inputs (Planck 2018 densities, rho_c/h^2 and s_0 from the PDG) are
    taken at the ends that weaken the conclusion.
(c) Which contents meet c <= 1, at the coefficients of clause (v) of the pair-production theorem
    (premise; per creation event of two quanta), computed from its closed form at the bath (4, 45, 12):
    16087 pi^3/20736000 per real massless vector, 1519247 pi^3/82944000 for a Standard-Model content.
    pi^3 is not approximated by a decimal: pi is taken between 333/106 (the bound part (b) already
    uses) and 355/113, at the end that weakens each statement. The factor 2 in A/2 is the two quanta of
    each creation event.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def floor(x):
    return x.numerator // x.denominator


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def transpose(X):
    return [list(r) for r in zip(*X)]


def frob2(X):
    return sum(x * x for r in X for x in r)


def alpha_over_pi3(cj, tj, n_s=4, n_w=45, n_v=12):
    """alpha/pi^3 of the pair-production theorem's clause (v) for one produced species, per creation event:
    (1/17280)[(c_j (N_s + 12 N_v) + 5 tau_j N_s)/225 + 49 c_j N_w/4800], bath scalars at zero curvature coupling."""
    return (F(cj * (n_s + 12 * n_v) + 5 * tj * n_s, 225) + F(49 * cj * n_w, 4800)) / 17280


def check_untuned_fit_caps_lightest_heavy_neutrino():
    premise("standard-model.fits-record-level")
    premise("standard-model.chain")
    premise("synthesis.gravitational-pair-production-from-the-operator-source-at-first-order")
    premise("dark-matter.imported-massless-graviton-production-rate")
    premise("neutrino.r-descent-reheats-below-lower-heavy")
    E = F(10)

    # (a) tr(M_D^T R^-1 M_D) = sum_i |row_i|^2 / d_i <= ||M_D||_F^2 / min d
    MDs = [[[1, 2, 0], [0, 1, 3], [2, 0, 1]], [[3, 1, 1], [1, 3, 1], [1, 1, 3]],
           [[0, 0, 1], [0, 0, 0], [0, 0, 0]]]
    MRs = [[2, 5, 7], [1, 1, 9], [4, 6, 3]]
    hits = 0
    for MD in MDs:
        MD = [[F(x) for x in r] for r in MD]
        for d in MRs:
            Rinv = [[F(1, d[i]) if i == j else F(0) for j in range(3)] for i in range(3)]
            mnu = matmul(matmul(transpose(MD), Rinv), MD)
            tr = sum(mnu[i][i] for i in range(3))
            alpha = min(F(x) for x in d)
            assert tr <= frob2(MD) / alpha
            if tr == frob2(MD) / alpha:
                hits += 1
    assert hits == 2                      # the rank-one instance, row 0 lightest in two of three

    # (b) kappa_s^2 = (pi^2 g/90)(2 pi^2 g_s/45)^2 at g = g_s = 100, with pi > 333/106
    pi_lo = F(333, 106)
    k2 = pi_lo ** 2 * 100 / 90 * (2 * pi_lo ** 2 * 100 / 45) ** 2
    kappa = F(1452, 10)
    assert kappa ** 2 < k2 < (kappa + F(1, 10)) ** 2
    # remainder: Omega_c h^2 - Omega_b h^2 at the lower ends, mass per unit entropy
    om = F(1188, 10000) - F(2252, 100000)
    mY = om * F(105371, 10 ** 10) / F(28912, 10)
    assert floor(mY * E ** 13) == 3508
    MP = F(2435, 1000) * E ** 18
    A = 3 * kappa * MP ** 3 * mY          # Y = c T^3 / (3 kappa M_P^3), m <= T
    assert floor(A / E ** 44) == 22068

    e = F(45, 1000)
    m3_run = F(25, 1000) / E ** 9
    alpha_max = 9 * e ** 2 / m3_run
    assert floor(alpha_max / E ** 6) == 729
    assert floor(A / (2 * alpha_max ** 4) / E ** 11) == 39
    assert A / 2 > (1400 * alpha_max) ** 4                 # c <= 1: more than a thousandfold
    # (c) which contents meet c <= 1, at the derived coefficients
    pi_hi = F(355, 113)
    r_v = alpha_over_pi3(12, 0)
    r_sm = 4 * alpha_over_pi3(1, 1) + 45 * alpha_over_pi3(3, 0) + 12 * r_v
    assert r_v == F(16087, 20736000) and r_sm == F(1519247, 82944000)
    a_vec_lo, a_vec_hi = r_v * pi_lo ** 3, r_v * pi_hi ** 3
    assert F(2405, 10 ** 5) < a_vec_lo < a_vec_hi < F(2406, 10 ** 5)
    assert 41 * a_vec_hi < 1 < 42 * a_vec_lo               # forty-one vector species, not forty-two
    assert F(5291, 10 ** 4) < 22 * a_vec_lo < 22 * a_vec_hi < F(5293, 10 ** 4)     # the odd towers' vectors
    c_sm_lo, c_sm_hi = r_sm * pi_lo ** 3, r_sm * pi_hi ** 3
    assert F(5678, 10 ** 4) < c_sm_lo < c_sm_hi < F(568, 10 ** 3) < 1              # one Standard-Model content
    assert F(2271, 1000) < 4 * c_sm_lo < 4 * c_sm_hi < F(2272, 1000)               # four: 2.27, above 1
    assert A / (2 * F(2272, 1000)) > (1100 * alpha_max) ** 4                       # still more than 1100-fold
    M_I = F(19, 10) * E ** 10
    assert floor(M_I / alpha_max) == 26
    m3 = F(494, 10) / E ** 12
    assert [floor(9 * F(x, 10) ** 2 / m3 / E ** 10) for x in (22, 29, 40)] == [88, 153, 291]
    for x in (22, 29, 40):
        assert (9 * F(x, 10) ** 2 / m3_run) ** 4 > A / 2   # undecided even at c = 1
    return True
