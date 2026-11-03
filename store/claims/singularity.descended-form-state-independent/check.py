"""singularity.descended-form-state-independent: exact checks.

States on 1, 2 and 3 boundary modes with coherences (density matrices over Q and Q(i), pure and
mixed, odd and even) are given at module level. For each, every single-mode marginal rho_k is
computed by partial trace, the descent of the premise E_k(x) = (x + sigma x sigma)/2 is applied,
and: (1) E_k(rho_k) is diagonal; (2) with p_k the vacancy probability and x_k = (1 - p_k)/p_k
(x_k = e^{-beta_k omega_k}, i.e. beta_k omega_k = log(p_k/(1 - p_k))), E_k(rho_k) equals the Gibbs
matrix diag(1, x_k)/(1 + x_k) of e^{-beta_k omega_k N} exactly; (3) uniqueness: p = 1/(1 + x) is
strictly monotone, p(x1) - p(x2) = (x2 - x1)/((1 + x1)(1 + x2)) at rational samples, and the
endpoints p = 1, 0 are the Gibbs matrices at x = 0 and at 1/x = 0 (beta = +-infinity);
(4) zero weight: at omega_k = 0 the Gibbs matrix is id/2 for every beta, so existence holds only at
p_k = 1/2 (a sample with p != 1/2 is not of that form).
No hypothesis on the state is used: the sample states are arbitrary.
"""
from fractions import Fraction as F

import GA
from GA import QI
from tp_premise import premise


def ket(n, amps):
    D = 2 ** n
    rho = [[QI(0)] * D for _ in range(D)]
    for i, a in amps.items():
        for j, b in amps.items():
            rho[i][j] = rho[i][j] + QI(a) * QI(b).conj()
    return rho


def mix(w, A, B):
    return [[w * A[i][j] + (1 - w) * B[i][j] for j in range(len(A))] for i in range(len(A))]


def norm(amps):
    s = sum((QI(a) * QI(a).conj() for a in amps.values()), QI(0))
    assert s == 1
    return amps


# arbitrary states (unit vectors with rational amplitudes; complex phases included)
STATES = [
    (1, ket(1, norm({0: F(3, 5), 1: QI(0, 4) / 5}))),
    (1, [[QI(F(1, 3)), QI(0, F(1, 5))], [QI(0, F(-1, 5)), QI(F(2, 3))]]),
    (2, ket(2, norm({0: F(1, 2), 1: F(1, 2), 2: QI(0, 1) / 2, 3: F(-1, 2)}))),
    (2, mix(F(1, 3), ket(2, norm({0: F(3, 5), 3: F(4, 5)})), ket(2, norm({1: F(5, 13), 2: F(12, 13)})))),
    (3, ket(3, norm({0: F(2, 7), 3: F(3, 7), 5: QI(0, 6) / 7}))),
    (3, ket(3, norm({1: F(1, 3), 2: F(2, 3), 4: F(2, 3)}))),
]
XS = [F(9, 16), F(16, 9), F(1), F(1, 7)]


def bit(b, k, n):
    return (b >> (n - 1 - k)) & 1


def marginal(rho, k, n):
    out = [[QI(0), QI(0)], [QI(0), QI(0)]]
    for b in range(2 ** n):
        for c in range(2 ** n):
            if all(bit(b, t, n) == bit(c, t, n) for t in range(n) if t != k):
                out[bit(b, k, n)][bit(c, k, n)] = out[bit(b, k, n)][bit(c, k, n)] + rho[b][c]
    return out


SIGMA = [[F(-1), F(0)], [F(0), F(1)]]


mm = GA.field_mat_mul


def parity_avg(x):
    sxs = mm(mm(SIGMA, x), SIGMA)
    return [[(x[i][j] + sxs[i][j]) / 2 for j in range(2)] for i in range(2)]


def gibbs(x):
    return [[1 / (1 + x), F(0)], [F(0), x / (1 + x)]]


def check_descended_marginal_is_diagonal_gibbs():
    premise("singularity.descent-parity-average")
    count = 0
    for n, rho in STATES:
        assert sum((rho[i][i] for i in range(2 ** n)), QI(0)) == 1
        for k in range(n):
            rk = marginal(rho, k, n)
            Ek = parity_avg(rk)
            assert Ek[0][1] == 0 and Ek[1][0] == 0
            p = Ek[0][0].re
            assert Ek[0][0].im == 0 and 0 < p < 1
            x = (1 - p) / p
            g = gibbs(x)
            assert all(Ek[i][j] == g[i][j] for i in range(2) for j in range(2))
            # beta omega = log(p/(1-p)) <=> e^{-beta omega} = (1 - p)/p = x
            assert x * p == 1 - p
            count += 1
    # some marginals carried coherences that the descent removed
    coh = sum(1 for n, rho in STATES for k in range(n) if marginal(rho, k, n)[0][1] != 0)
    assert count == 12 and coh >= 4, (count, coh)


def check_beta_unique_and_endpoints():
    premise("singularity.descent-parity-average")
    pofx = lambda x: 1 / (1 + x)
    for x1 in XS:
        for x2 in XS:
            assert pofx(x1) - pofx(x2) == (x2 - x1) / ((1 + x1) * (1 + x2))
            if x1 < x2:
                assert pofx(x1) > pofx(x2)
    # the endpoints: p = 1 is diag(1, 0) = Gibbs at x = 0; p = 0 is the y = 1/x -> 0 limit diag(y, 1)/(1 + y)
    assert gibbs(F(0)) == [[F(1), F(0)], [F(0), F(0)]]
    y = F(0)
    assert [[y / (1 + y), F(0)], [F(0), 1 / (1 + y)]] == [[F(0), F(0)], [F(0), F(1)]]
    # the descended form of a state with p = 1 or p = 0 is still diagonal
    for amps, p in (({0: F(1)}, F(1)), ({1: QI(0, 1)}, F(0))):
        Ek = parity_avg(ket(1, amps))
        assert Ek[0][0] == p and Ek[0][1] == 0


def check_zero_weight_mode():
    premise("singularity.descent-parity-average")
    # omega = 0: e^{-beta * 0 * N} = id for every beta, so the Gibbs matrix is id/2 whatever beta is
    for x_any in XS:
        x = x_any ** 0
        assert gibbs(x) == [[F(1, 2), F(0)], [F(0), F(1, 2)]]
    half = parity_avg(ket(1, {0: F(3, 5), 1: F(4, 5)}))
    assert half[0][0] == F(9, 25) and half[0][0] != F(1, 2)
    even = parity_avg([[QI(F(1, 2)), QI(F(1, 3))], [QI(F(1, 3)), QI(F(1, 2))]])
    assert even[0][0] == F(1, 2) and even[1][1] == F(1, 2) and even[0][1] == 0
