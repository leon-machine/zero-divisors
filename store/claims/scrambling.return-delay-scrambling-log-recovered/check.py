"""scrambling.return-delay-scrambling-log-recovered: exact checks of the arithmetic of the return delay.

Quantities are Laurent polynomials in pi with rational coefficients ({power of pi: Fraction}), so
pi is an exact indeterminate. For several masses M:
(1) The clock. kappa = 1/(4M), beta = 2 pi/kappa = 8 pi M (the epoch of the premise, the dwell floor),
    and the round duration beta/(2 pi) = 1/kappa = 4M exactly: the coefficient 4M of the display.
(2) The epidemic count. Spreading by one pairwise operation per informed mode per round, support
    starting on one mode reaches N modes after exactly ceil(log2 N) rounds (simulated for every
    N <= 4100 and compared with the bit length of N - 1); for N = 2^j it is j rounds, so
    T_return = (rounds) beta/(2 pi) = 4M log2 S, which is (4M/ln 2) ln S: the display up to the
    constant ln 2 the statement absorbs into "approximately".
Not checked: the rate-model premises themselves (the dwell floor's (IC) condition) and the claim that
genuine chaotic dynamics is beyond the model.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MASSES = (F(1), F(5, 2), F(1000))
NMAX = 4100


def lmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, F(0)) + x * y
    return {k: v for k, v in out.items() if v != 0}


def linv_monomial(a):
    (i, x), = a.items()
    return {-i: 1 / x}


def check_round_duration_is_4m():
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    premise("scrambling.spreading-law-chaos-bound-saturated")
    ok = True
    two_pi = {1: F(2)}
    for M in MASSES:
        kappa = {0: 1 / (4 * M)}
        beta = lmul(two_pi, linv_monomial(kappa))
        ok = ok and beta == {1: 8 * M}
        round_len = lmul(beta, linv_monomial(two_pi))
        ok = ok and round_len == {0: 4 * M} and round_len == linv_monomial(kappa)
    GA.check("beta = 2 pi/kappa = 8 pi M and beta/(2 pi) = 1/kappa = 4M exactly", ok)
    return ok


def rounds_to_cover(n):
    informed, t = 1, 0
    while informed < n:
        informed = min(2 * informed, n)
        t += 1
    return t


def check_epidemic_doubling_count():
    premise("scrambling.spreading-law-chaos-bound-saturated")
    ok = True
    for n in range(1, NMAX + 1):
        ok = ok and rounds_to_cover(n) == (n - 1).bit_length()
    ok = ok and [rounds_to_cover(2 ** j) for j in range(13)] == list(range(13))
    ok = ok and rounds_to_cover(4097) == 13
    for M in MASSES:
        S = 2 ** 10
        T = rounds_to_cover(S) * 4 * M
        ok = ok and T == 40 * M
    GA.check("one pairwise operation per informed mode per round covers N modes in ceil(log2 N) rounds; "
             "T_return = 4M log2 S", ok)
    return ok
