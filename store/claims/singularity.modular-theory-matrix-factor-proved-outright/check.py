"""singularity.modular-theory-matrix-factor-proved-outright: exact checks over Q(i).

H = C^n (x) C^n with |ij> at index n i + j, M = Mat_n (x) 1, Omega = sum_i lambda_i |ii> with rational
lambda_i > 0, sum lambda_i^2 = 1 (n = 2, 3, 4; equal and unequal weights).
(1) Omega is cyclic and separating for M: the n^2 vectors (E_ab (x) 1) Omega are independent; with a
zero weight the rank drops to n (#nonzero) (control).
(2) The Tomita operator is computed from its definition S(a Omega) = a* Omega: written as
S v = A conj(v), A is determined on the real basis (E_ab (x) 1) Omega and then tested on complex
elements a (antilinearity). A = J D with J|ij> = |ji> (J = swap, real symmetric, J^2 = 1, so the
antilinear J is an antiunitary involution) and D = diag(lambda_i/lambda_j) > 0. The modular operator
Delta = S* S, i.e. (A^dagger A)^T, equals rho (x) conj(rho)^{-1} with rho = diag(lambda_i^2), and
equals D^2: the polar decomposition S = J Delta^{1/2}.
(3) Modular flow: Delta^z (a (x) 1) Delta^{-z} = (rho^z a rho^{-z}) (x) 1 for z = 1, 2, -1 and complex a
(the exponents of the eigenvalue ratios match, so the identity holds for every complex z, in
particular z = it).
(4) KMS: omega(ab) = omega(b rho a rho^{-1}) for all matrix units a, b, with omega = <Omega, . Omega>
= tr(rho .).
"""
from fractions import Fraction as F

import GA
from GA import QI

WEIGHTS = [[F(3, 5), F(4, 5)], [F(5, 13), F(12, 13)], [F(2, 3), F(2, 3), F(1, 3)],
           [F(1, 2), F(1, 2), F(1, 2), F(1, 2)]]
COEFFS = [QI(1, 2), QI(-3, 1), QI(0, 5), QI(2, -7), QI(4, 0), QI(1, 1), QI(-2, -3), QI(3, 5),
          QI(6, -1), QI(0, -2), QI(5, 5), QI(-1, 4), QI(2, 2), QI(7, 0), QI(0, 1), QI(-4, 3)]


def zeros(r, c):
    return [[QI(0)] * c for _ in range(r)]


mm = GA.field_mat_mul


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def tp(A):
    return [list(r) for r in zip(*A)]


def conjv(v):
    return [x.conj() for x in v]


def mv(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v))), QI(0)) for i in range(len(A))]


def left(a, n):
    """a (x) 1 on C^n (x) C^n."""
    M = zeros(n * n, n * n)
    for i in range(n):
        for k in range(n):
            for j in range(n):
                M[n * i + j][n * k + j] = QI(a[i][k])
    return M


def unit(n, a, b):
    M = [[QI(0)] * n for _ in range(n)]
    M[a][b] = QI(1)
    return M


def omega_vec(lam):
    n = len(lam)
    return [QI(lam[i]) if i == j else QI(0) for i in range(n) for j in range(n)]


def generic(n, shift):
    return [[COEFFS[(shift + n * i + j) % len(COEFFS)] for j in range(n)] for i in range(n)]


def tomita_matrix(lam):
    """A with S v = A conj(v), from S((E_ab (x) 1) Omega) = (E_ba (x) 1) Omega on the real basis."""
    n = len(lam)
    Om = omega_vec(lam)
    W = [mv(left(unit(n, a, b), n), Om) for a in range(n) for b in range(n)]       # columns
    SW = [mv(left(unit(n, b, a), n), Om) for a in range(n) for b in range(n)]
    # A W = SW (W real): solve column by column for A^T rows: W^T A^T = SW^T
    WT = [[W[c][r] for r in range(n * n)] for c in range(n * n)]
    AT_cols = []
    for r in range(n * n):
        rhs = [SW[c][r] for c in range(n * n)]
        AT_cols.append(GA.field_solve(WT, rhs))
    return [[AT_cols[r][c] for c in range(n * n)] for r in range(n * n)]


def check_cyclic_and_separating_iff_weights_positive():
    for lam in WEIGHTS:
        n = len(lam)
        assert sum((l * l for l in lam), F(0)) == 1
        Om = omega_vec(lam)
        vecs = [mv(left(unit(n, a, b), n), Om) for a in range(n) for b in range(n)]
        assert GA.field_rank(vecs) == n * n
    # a zero weight: rank n * (number of nonzero weights)
    for lam, rk in (([F(1), F(0)], 2), ([F(3, 5), F(0), F(4, 5)], 6)):
        n = len(lam)
        Om = omega_vec(lam)
        vecs = [mv(left(unit(n, a, b), n), Om) for a in range(n) for b in range(n)]
        assert GA.field_rank(vecs) == rk


def check_tomita_polar_decomposition():
    for lam in WEIGHTS:
        n = len(lam)
        A = tomita_matrix(lam)
        Om = omega_vec(lam)
        # antilinear definition on complex elements: S(a Omega) = a^dagger Omega
        for shift in (0, 5):
            a = generic(n, shift)
            aO = mv(left(a, n), Om)
            assert mv(A, conjv(aO)) == mv(left(dag(a), n), Om)
        Jm = [[QI(1) if (r // n, r % n) == (c % n, c // n) else QI(0) for c in range(n * n)]
              for r in range(n * n)]
        D = [[QI(lam[r // n] / lam[r % n]) if r == c else QI(0) for c in range(n * n)] for r in range(n * n)]
        assert A == mm(Jm, D)
        assert mm(Jm, Jm) == [[QI(1) if r == c else QI(0) for c in range(n * n)] for r in range(n * n)]
        assert tp(Jm) == Jm and all(x.im == 0 for r in Jm for x in r)
        Delta = tp(mm(dag(A), A))
        rho = [lam[i] * lam[i] for i in range(n)]
        want = [[QI(rho[r // n] / rho[r % n]) if r == c else QI(0) for c in range(n * n)] for r in range(n * n)]
        assert Delta == want and Delta == mm(D, D)
        assert all(D[r][r].re > 0 for r in range(n * n))


def check_modular_flow_and_kms():
    for lam in WEIGHTS:
        n = len(lam)
        rho = [lam[i] * lam[i] for i in range(n)]
        delta = [rho[r // n] / rho[r % n] for r in range(n * n)]
        a = generic(n, 3)
        for z in (1, 2, -1):
            Dz = [[QI(delta[r] ** z) if r == c else QI(0) for c in range(n * n)] for r in range(n * n)]
            Dmz = [[QI(delta[r] ** (-z)) if r == c else QI(0) for c in range(n * n)] for r in range(n * n)]
            rz = [[QI(rho[i] ** z) if i == j else QI(0) for j in range(n)] for i in range(n)]
            rmz = [[QI(rho[i] ** (-z)) if i == j else QI(0) for j in range(n)] for i in range(n)]
            assert mm(mm(Dz, left(a, n)), Dmz) == left(mm(mm(rz, a), rmz), n)
        Om = omega_vec(lam)

        def omega(x):
            v = mv(left(x, n), Om)
            return sum((Om[i].conj() * v[i] for i in range(n * n)), QI(0))

        R = [[QI(rho[i]) if i == j else QI(0) for j in range(n)] for i in range(n)]
        Ri = [[QI(1 / rho[i]) if i == j else QI(0) for j in range(n)] for i in range(n)]
        count = 0
        for p in range(n):
            for q in range(n):
                a = unit(n, p, q)
                assert omega(a) == (QI(rho[p]) if p == q else QI(0))
                for s in range(n):
                    for t in range(n):
                        b = unit(n, s, t)
                        assert omega(mm(a, b)) == omega(mm(b, mm(mm(R, a), Ri)))
                        count += 1
        assert count == n ** 4
    # control: the reversed flow (rho^{-1} . rho) breaks the identity at a = E_01, b = E_10 for the
    # weights (3/5, 4/5): omega(ab) = 9/25 while omega(b rho^{-1} a rho) = (16/9)(16/25)
    n, lam = 2, WEIGHTS[0]
    rho = [lam[i] * lam[i] for i in range(n)]
    Om = omega_vec(lam)

    def omega2(x):
        v = mv(left(x, n), Om)
        return sum((Om[i].conj() * v[i] for i in range(4)), QI(0))

    a, b = unit(2, 0, 1), unit(2, 1, 0)
    R = [[QI(rho[i]) if i == j else QI(0) for j in range(n)] for i in range(n)]
    Ri = [[QI(1 / rho[i]) if i == j else QI(0) for j in range(n)] for i in range(n)]
    assert omega2(mm(a, b)) == QI(F(9, 25))
    assert omega2(mm(b, mm(mm(Ri, a), R))) == QI(F(16, 9) * F(16, 25))
