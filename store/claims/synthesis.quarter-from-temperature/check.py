"""synthesis.quarter-from-temperature: exact checks on polynomials in M.

pi is a formal symbol: quantities are kept as rational coefficients of pi^k.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

MS = [F(1), F(1, 2), F(3), F(7, 5)]


def check_quarter():
    premise("singularity.rate-discharge-hypothesis-iii")
    premise("singularity.plane-rate")
    premise("singularity.p-univalence")
    premise("singularity.r-regularity-fixed-locus")
    # 1/T = 8 pi M: coefficient of pi is 8M. S(M) = integral of 8 pi M dM = 4 pi M^2.
    # the antiderivative of c M is c M^2 / 2; check S'(M) = 1/T
    c = F(8)                                    # 1/T = c pi M
    S_coeff = c / 2                             # S = S_coeff pi M^2
    assert S_coeff == 4
    for M in MS:
        A_over_pi = 4 * (2 * M) ** 2            # A = 4 pi (2M)^2
        assert A_over_pi == 16 * M * M
        assert S_coeff * M * M == A_over_pi / 4  # S = A / 4
        # dM = (kappa / 8 pi) dA with kappa = 1/(4M): (kappa/8)(dA/dM)/pi... in pi units:
        kappa = 1 / (4 * M)
        dA_dM_over_pi = 32 * M
        assert kappa / 8 * dA_dM_over_pi == 1     # (kappa / 8 pi) * (32 pi M) = 1
        # a different period p (in units of 2 pi / kappa): S scales by the same factor
        for t in (F(1, 2), F(3)):
            # 1/T = t (2 pi / kappa) = t * 8 pi M: S = t * 4 pi M^2 = t * A/4
            assert (t * c / 2) * M * M == t * A_over_pi / 4
    return True
