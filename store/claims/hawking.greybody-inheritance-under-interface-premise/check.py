"""hawking.greybody-inheritance-under-interface-premise: exact checks of joint (ii), the horizon occupancies.

Joints (i) (transmission coefficients inherited from the exterior metric) and (iii) (under Premise (I) the flux
formula is the definition of filtered thermal flux) are a literature import and a definition and are not
checked; Premise (I) is a non-theorem joint.
(ii-a) Fermionic species (Theorem hawking.i-state-continuum, window case): on a two-mode window with
    h = U diag(w) U^T (U a rational rotation) and Boltzmann factors q_j = e^{-w_j/T}, the two-point KMS identity
    forces the symbol A = (1 + e^{h/T})^{-1}, whose eigenvalue on the eigenmode U e_j is
    n_+(w_j) = 1/(e^{w_j/T} + 1) = q_j/(1 + q_j): the upper sign.
(ii-b) Bosonic sector (Fact hawking.imported-s-wave-bosonic-sector, conditional half): the current occupancy per
    unit charge, sum_k n_{k+m}(1 - n_k)/m, approaches 1/(x^{-m} - 1) = n_-(m kappa) from below within the tail
    bound 2 x^{K-m}/(1 - x), x = e^{-kappa/T}: the lower sign.
(ii-c) The two signs are distinct and related by n_- - n_+ = 2 n_+ n_-, at every sample point.
(ii-d) Both at T_H with the geometric coefficient (Fact
    hawking.imported-modular-descent-premises-geometric-normalisation): kappa = f'(2M)/2 = 1/(4M), so
    T_H = kappa/(2 pi) = 1/(8 pi M): coefficient at sample M.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

U = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
QS = [F(1, 2), F(1, 5)]
XS = [F(1, 2), F(1, 3)]
KS = [20, 30]
MASSES = [F(1, 2), F(4)]


mm = GA.mat_mul


def tr(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def check_fermionic_occupancy_is_upper_sign():
    premise("hawking.i-state-continuum")
    g = mm(mm(U, [[QS[0], F(0)], [F(0), QS[1]]]), tr(U))          # e^{-h/T}
    M = [[1 + g[0][0], g[0][1]], [g[1][0], 1 + g[1][1]]]
    rows, rhs = [], []
    for i in range(2):
        for j in range(2):
            row = [F(0)] * 4
            for k in range(2):
                row[2 * i + k] += M[k][j]
            rows.append(row)
            rhs.append(g[i][j])
    sol = GA.field_solve(rows, rhs)
    A = [sol[0:2], sol[2:4]]
    ok = True
    for j, q in enumerate(QS):
        vec = [[U[0][j]], [U[1][j]]]
        Av = mm(A, vec)
        n_plus = 1 / (1 / q + 1)
        ok = ok and Av == [[n_plus * vec[0][0]], [n_plus * vec[1][0]]] and n_plus == q / (1 + q)
    _tp_rv = (ok); assert _tp_rv is not False, "check_fermionic_occupancy_is_upper_sign"; return _tp_rv


def check_bosonic_occupancy_is_lower_sign():
    premise("hawking.imported-s-wave-bosonic-sector")
    ok = True
    for x in XS:
        def n(k):
            return 1 / (x ** (-k) + 1)
        for m in (1, 2):
            n_minus = 1 / (x ** (-m) - 1)
            for K in KS:
                S = sum(n(k + m) * (1 - n(k)) for k in range(-K, K - m + 1)) / m
                ok = ok and 0 < n_minus - S <= 2 * x ** (K - m) / (1 - x)
            n_plus = 1 / (x ** (-m) + 1)
            ok = ok and n_minus - n_plus == 2 * n_plus * n_minus and n_minus > n_plus
    _tp_rv = (ok); assert _tp_rv is not False, "check_bosonic_occupancy_is_lower_sign"; return _tp_rv


def check_hawking_temperature_coefficient():
    premise("hawking.imported-modular-descent-premises-geometric-normalisation")
    ok = True
    for M in MASSES:
        kappa = (2 * M / (2 * M) ** 2) / 2
        ok = ok and kappa == 1 / (4 * M) and 1 / (2 / kappa) == 1 / (8 * M)
    _tp_rv = (ok); assert _tp_rv is not False, "check_hawking_temperature_coefficient"; return _tp_rv
