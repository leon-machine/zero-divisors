"""rungs.imported-mass-symplectic-area: exact checks.

(1) Null momentum and the two-spinor mass: for Gaussian-rational spinors a single P = pi pi^dagger has
    det P = 0, tr P > 0; for two, p^2 = 2 det(P1 + P2) = 2 |<pi1 pi2>|^2 with <pi1 pi2> = eps^AB pi1_A pi2_B
    (fifteen pairs), zero for proportional spinors; the Minkowski reading p.p = det(p^a sigma_a) on rational p.
(2) Flat chart of the conformal model (Cl(2,4): e_+ (+1), g0 (+1), e_- (-1), g1, g2, g3 (-1);
    n0 = (e_+ + e_-)/2, n_inf = e_+ - e_-): I_Lambda = n_inf + (Lambda/6) n0 has Q = Lambda/3 for six values
    of Lambda and is n_inf (null) at Lambda = 0; its scale function <X(x), I_Lambda> is
    sigma = 1 - Lambda Q(x)/12 at seven points; for n_inf + lam n0 the scale function is 1 - lam Q(x)/2, equal to
    sigma only at lam = Lambda/6; the points X(x) span the ambient space (rank 6), so the constant vector with
    scale function sigma is unique.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# Two-component spinors over Q(i): momentum P = sum pi pi^dagger (P_AA' = pi_A conj(pi_A')), the
# bracket <pi1 pi2> = eps^AB pi1_A pi2_B = pi1_0 pi2_1 - pi1_1 pi2_0, and the Minkowski reading
# P = p^a sigma_a / sqrt 2, under which p.p = det(p^a sigma_a) = 2 det P.
# ---------------------------------------------------------------------------
QI = GA.QI
ZQ = QI(0)


def sp2(a, b):
    return (a if isinstance(a, QI) else QI(a), b if isinstance(b, QI) else QI(b))


def outer(p):
    return [[p[A] * p[B].conj() for B in range(2)] for A in range(2)]


def m2add(*Ms):
    return [[sum((M[i][j] for M in Ms), ZQ) for j in range(2)] for i in range(2)]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def tr2(M):
    return M[0][0] + M[1][1]


def momentum(*spinors):
    return m2add(*[outer(p) for p in spinors])


def bracket(p, q):
    return p[0] * q[1] - p[1] * q[0]


def absq(z):
    return z.re * z.re + z.im * z.im


def pauli_matrix(p):
    """p^a sigma_a for a rational 4-vector p."""
    p0, p1, p2, p3 = [QI(x) for x in p]
    return [[p0 + p3, p1 - QI(0, 1) * p2], [p1 + QI(0, 1) * p2, p0 - p3]]


def mink(p):
    return p[0] * p[0] - p[1] * p[1] - p[2] * p[2] - p[3] * p[3]


def mix(U, spinors):
    """pi'^i = sum_j U^i_j pi^j."""
    n = len(spinors)
    return [tuple(sum((U[i][j] * spinors[j][A] for j in range(n)), ZQ) for A in range(2)) for i in range(n)]

SPINORS = [sp2(1, 0), sp2(0, 1), sp2(1, QI(0, 1)), sp2(QI(2, -1), 3), sp2(F(1, 2), QI(-1, 4)), sp2(QI(0, 3), QI(5, 2))]
RVECS = [(1, 0, 0, 0), (2, 1, -1, 3), (F(1, 2), F(3, 4), 0, -2), (5, 3, 4, 0)]
SQR = (1, 1, -1, -1, -1, -1)
LAMBDAS = [F(0), F(1), F(-2), F(3, 5), F(6), F(-1, 7)]
POINTS = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 1, 0, 0), (0, 1, 0, 0), (F(3, 2), -1, 2, F(1, 3)), (-5, 2, F(7, 4), -1),
          (1, 1, 1, 1)]


def rvec(c):
    return {(a,): F(v) for a, v in enumerate(c) if v != 0}


N0 = rvec((F(1, 2), 0, F(1, 2), 0, 0, 0))
NINF = rvec((1, 0, -1, 0, 0, 0))


def dot(x, y):
    return GA.dot(x, y, SQR)


def point(x):
    xv = rvec((0, x[0], 0, x[1], x[2], x[3]))
    Q = dot(xv, xv)
    return GA.add(N0, xv, GA.scal(-Q / 2, NINF)), Q


def check_single_null_and_two_spinor_mass():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    ok = True
    for p in RVECS:
        ok = ok and det2(pauli_matrix(p)) == QI(mink(p))
    for p in SPINORS:
        P = momentum(p)
        ok = ok and det2(P) == ZQ and tr2(P).re > 0
    n = 0
    for p, q in combinations(SPINORS, 2):
        ok = ok and 2 * det2(momentum(p, q)) == QI(2 * absq(bracket(p, q)))
        n += 1
    ok = ok and n == 15
    for p in SPINORS:
        q = (QI(3, 1) * p[0], QI(3, 1) * p[1])
        ok = ok and det2(momentum(p, q)) == ZQ
    _tp_rv = (ok); assert _tp_rv is not False, "check_single_null_and_two_spinor_mass"; return _tp_rv


def check_frozen_point_in_the_flat_chart():
    premise("mass.de-sitter-scale-frozen-point")
    premise("standard-model.imported-frozen-point-dictionary")
    ok = True
    ok = ok and dot(N0, N0) == 0 and dot(NINF, NINF) == 0 and dot(N0, NINF) == 1
    for L in LAMBDAS:
        I = GA.add(NINF, GA.scal(L / 6, N0))
        ok = ok and dot(I, I) == L / 3
        if L == 0:
            ok = ok and GA.eq(I, NINF)
        for x in POINTS:
            X, Q = point(x)
            ok = ok and dot(X, X) == 0
            ok = ok and dot(X, I) == 1 - L * Q / 12
            for lam in (F(0), F(1), F(-1, 2), L / 6):
                J = GA.add(NINF, GA.scal(lam, N0))
                ok = ok and dot(X, J) == 1 - lam * Q / 2
        # only lam = Lambda / 6 reproduces sigma at a point with Q != 0
        X, Q = point((2, 1, 0, 0))
        ok = ok and Q == 3
        sols = [lam for lam in (L / 6, L / 6 + 1, L / 6 - F(1, 2), -L / 6 - 1) if dot(X, GA.add(NINF, GA.scal(lam, N0))) == 1 - L * Q / 12]
        ok = ok and sols == [L / 6]
    blades = [(a,) for a in range(6)]
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(point(x)[0], blades) for x in POINTS]) == 6
    _tp_rv = (ok); assert _tp_rv is not False, "check_frozen_point_in_the_flat_chart"; return _tp_rv
