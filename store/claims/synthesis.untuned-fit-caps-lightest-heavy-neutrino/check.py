"""synthesis.untuned-fit-caps-lightest-heavy-neutrino: exact checks.

(a) The norm inequality, in its trace form, on exact instances: integer 3x3 Dirac matrices and
    diagonal Majorana matrices (Takagi form); equality on a rank-one instance.
(b) The numbers: untuned fit e = 0.045 GeV, m_3(M_I) >= 25 meV, against the seeding constant
    A = c T_seed^4 rederived from the imported rate, with kappa_s from its formula, and against
    M_I = 1.9e10 GeV. Record inputs (Planck 2018 densities, rho_c/h^2 and s_0 from the PDG) are
    taken at the ends that weaken the conclusion.
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


def check_untuned_fit_caps_lightest_heavy_neutrino():
    premise("standard-model.fits-record-level")
    premise("standard-model.chain")
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
    M_I = F(19, 10) * E ** 10
    assert floor(M_I / alpha_max) == 26
    m3 = F(494, 10) / E ** 12
    assert [floor(9 * F(x, 10) ** 2 / m3 / E ** 10) for x in (22, 29, 40)] == [88, 153, 291]
    for x in (22, 29, 40):
        assert (9 * F(x, 10) ** 2 / m3_run) ** 4 > A / 2   # undecided even at c = 1
    return True
