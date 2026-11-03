"""state-selection.partner-purification-are-canonical: exact checks.

The mode factor A = Mat_2(C) with a faithful diagonal state rho = diag(l0^2, l1^2). Exact samples use
Pythagorean amplitudes (l0, l1) = (3/5, 4/5), (5/13, 12/13), (8/17, 15/17), (20/29, 21/29), so every
square root that occurs is rational. Matrices over Q(i) (GA.QI), states on C^2 (x) C^2 as 4-vectors
indexed 2i + j for |ij>.
(1) Omega = sum_i l_i |ii> reproduces omega(a) = tr(rho a) on all 16 Gaussian matrix-unit multiples;
    {(a (x) 1) Omega} and {(1 (x) b) Omega} both span C^4 (cyclic and separating).
(2) The commutant of A (x) 1 in Mat_4(C), computed as a kernel, is four-dimensional and equals 1 (x) A;
    with the modular conjugation J|ij> = |ji> (antilinear) of the premise, J (a (x) 1) J = 1 (x) a-bar on
    every unit, and J Delta^{1/2} (a (x) 1) Omega = (a* (x) 1) Omega (Tomita) with Delta^{1/2}|ij> = l_i/l_j |ij>.
(3) Every purification (1 (x) U) Omega with U unitary (real rotations and Gaussian-rational unitaries) has
    marginal rho, and conversely for psi = sum M_ij |ij> with M M^dagger = rho the matrix U = M0^{-1} M
    (M0 = diag(l)) is unitary and psi = (1 (x) U^T) Omega; a non-unitary U changes the marginal.
(4) For the Gibbs state diag(1, x)/(1 + x), x = e^{-omega_k/T} in (0, 1) (samples whose roots are rational),
    the GNS vector built from the exact roots is the thermofield double l0 = cos theta, l1 = sin theta with
    tan^2 theta = x; it reproduces the Gibbs marginal (l0 > l1, the samples above with the roles swapped).
"""
from fractions import Fraction as F

import GA
import series
from tp_premise import premise

QI = GA.QI
Z0, ONE = QI(0), QI(1)
AMPS = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)), (F(20, 29), F(21, 29))]
GIBBS_X = [F(16, 9) ** -1, F(144, 25) ** -1, F(225, 64) ** -1, F(441, 400) ** -1]
UNITARIES = [
    [[QI(F(3, 5)), QI(F(-4, 5))], [QI(F(4, 5)), QI(F(3, 5))]],
    [[QI(F(3, 5)), QI(0, F(4, 5))], [QI(0, F(4, 5)), QI(F(3, 5))]],
    [[QI(0, 1), QI(0)], [QI(0), QI(F(5, 13), F(12, 13))]],
    [[QI(F(5, 13)), QI(0, F(12, 13))], [QI(F(12, 13)), QI(0, F(-5, 13))]],
]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Z0) for j in range(len(B[0]))]
            for i in range(len(A))]


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def app(M, v):
    return [sum((M[i][k] * v[k] for k in range(len(v))), Z0) for i in range(len(M))]


def eye(n):
    return [[ONE if i == j else Z0 for j in range(n)] for i in range(n)]


UNITS2 = [[[ONE if (i, j) == (a, b) else Z0 for j in range(2)] for i in range(2)]
          for a in range(2) for b in range(2)]


def omega_vec(l0, l1):
    return [QI(l0), Z0, Z0, QI(l1)]


def inner(u, v):
    return sum((a.conj() * b for a, b in zip(u, v)), Z0)


def marginal(psi):
    """Reduced density matrix on the first factor of the vector psi."""
    return [[sum((psi[2 * i + k] * psi[2 * j + k].conj() for k in range(2)), Z0) for j in range(2)]
            for i in range(2)]


def check_gns_vector_cyclic_and_separating():
    for (l0, l1) in AMPS:
        assert l0 * l0 + l1 * l1 == 1
        Om = omega_vec(l0, l1)
        rho = [[QI(l0 * l0), Z0], [Z0, QI(l1 * l1)]]
        for u in UNITS2:
            for c in (ONE, QI(2, -3)):
                a = [[c * e for e in row] for row in u]
                lhs = inner(Om, app(kron(a, eye(2)), Om))
                rhs = sum((mm(rho, a)[i][i] for i in range(2)), Z0)
                assert lhs == rhs
        cyc = [app(kron(u, eye(2)), Om) for u in UNITS2]
        sep = [app(kron(eye(2), u), Om) for u in UNITS2]
        assert GA.field_rank(cyc) == 4 and GA.field_rank(sep) == 4
        assert marginal(Om) == rho
    return True


def check_commutant_is_partner_copy_via_modular_conjugation():
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    # commutant of Mat_2 (x) 1 in Mat_4, as a kernel of X -> [X, u (x) 1] over all units u
    gens = [kron(u, eye(2)) for u in UNITS2]
    basis16 = [[[ONE if (i, j) == (a, b) else Z0 for j in range(4)] for i in range(4)]
               for a in range(4) for b in range(4)]
    rows = []
    for G in gens:
        cols = []
        for X in basis16:
            C = mm(X, G)
            D = mm(G, X)
            cols.append([C[i][j] - D[i][j] for i in range(4) for j in range(4)])
        rows += [[cols[k][r] for k in range(16)] for r in range(16)]
    ker = GA.field_kernel(rows)
    assert len(ker) == 4
    partner = [[e for row in kron(eye(2), u) for e in row] for u in UNITS2]
    assert GA.field_rank(ker) == GA.field_rank(partner) == GA.field_rank(ker + partner) == 4

    def J(v):
        return [v[2 * (k % 2) + k // 2].conj() for k in range(4)]

    def apply_JMJ(M, v):
        return J(app(M, J(v)))

    for u in UNITS2:
        for c in (ONE, QI(1, 2)):
            a = [[c * e for e in row] for row in u]
            abar = [[e.conj() for e in row] for row in a]
            for k in range(4):
                e = [ONE if r == k else Z0 for r in range(4)]
                assert apply_JMJ(kron(a, eye(2)), e) == app(kron(eye(2), abar), e)
    for (l0, l1) in AMPS:
        lam = [l0, l1]
        Om = omega_vec(l0, l1)
        for u in UNITS2:
            for c in (ONE, QI(-2, 1)):
                a = [[c * e for e in row] for row in u]
                v = app(kron(a, eye(2)), Om)
                half = [v[2 * i + j] * QI(lam[i] / lam[j]) for i in range(2) for j in range(2)]
                assert J(half) == app(kron(dag(a), eye(2)), Om)
    return True


def check_purifications_differ_by_partner_unitary():
    for (l0, l1) in AMPS:
        Om = omega_vec(l0, l1)
        rho = marginal(Om)
        M0 = [[QI(l0), Z0], [Z0, QI(l1)]]
        M0i = [[QI(1 / l0), Z0], [Z0, QI(1 / l1)]]
        for U in UNITARIES:
            assert mm(U, dag(U)) == eye(2)
            psi = app(kron(eye(2), U), Om)
            assert marginal(psi) == rho and psi != Om
            # converse: read psi as a matrix M, recover the unitary on the purifying factor
            M = [[psi[2 * i + j] for j in range(2)] for i in range(2)]
            assert mm(M, dag(M)) == rho
            V = mm(M0i, M)
            assert mm(V, dag(V)) == eye(2)
            VT = [[V[j][i] for j in range(2)] for i in range(2)]
            assert app(kron(eye(2), VT), Om) == psi
        bad = [[QI(1), QI(1)], [QI(0), QI(1)]]
        assert marginal(app(kron(eye(2), bad), Om)) != rho
    return True


qsqrt = series.qsqrt   # exact square root of a rational perfect square


def check_gibbs_state_gives_thermofield_double():
    for x in GIBBS_X:
        assert 0 < x < 1
        gibbs = [[QI(1 / (1 + x)), Z0], [Z0, QI(x / (1 + x))]]
        l0, l1 = qsqrt(gibbs[0][0].re), qsqrt(gibbs[1][1].re)
        Om = omega_vec(l0, l1)
        assert marginal(Om) == gibbs and inner(Om, Om) == ONE
        # (cos theta, sin theta) with tan theta = e^{-omega/2T}: tan^2 theta = x
        assert l0 * l0 + l1 * l1 == 1 and (l1 / l0) * (l1 / l0) == x
        assert l0 > l1 and (l1, l0) in AMPS
    return True
