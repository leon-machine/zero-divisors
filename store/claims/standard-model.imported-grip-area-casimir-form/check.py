"""standard-model.imported-grip-area-casimir-form: exact checks.

Conventions: R^{2,4} with orthonormal e_+ (+1), g0 (+1), e_- (-1), g1, g2, g3 (-1); n0 = (e_+ + e_-)/2,
n_inf = e_+ - e_-. A moment is an antisymmetric bilinear form M on V (M_{U ^ I} = M(U, I)); the grip P = M(I) is
the vector with <P, U> = M(U, I); for a nondegenerate subspace S with basis e_alpha and inverse Gram g^{ab},
C_2(S) = (1/2) g^{aa'} g^{bb'} M_ab M_a'b'.
(i), (iv) For four rational antisymmetric M and seven non-null I (the frozen points n_inf + (Lambda/6) n0 for
    Lambda = 3, -2, 6/5 and four others), <P, I> = 0 and Q(P) = Q(I) (C_2(V) - C_2(I^perp)); for
    Q(I) = Lambda/3 > 0 the complement I^perp has signature (1,4) (de Sitter) and for Lambda < 0 (2,3).
(ii) At Lambda = 0, I = n_inf: the grip has no n0 component (<P, n_inf> = 0), so P = p + c n_inf with p its
    x-slot (spacetime) part, and Q(P) = p^2, the Poincare Casimir of the momentum p_a = M(e_a, n_inf).
(iii) For Gaussian-rational spinors: P = pi pi^dagger is null and future-directed; for two spinors
    p^2 = 2 det(P1 + P2) = 2 |det(pi^i_A)|^2 (the bracket is the determinant over the slot index), on fifteen
    pairs; the Minkowski reading p.p = det(p^a sigma_a) on rational p.
The dual-spinor case is the same computation through the conjugation and is not repeated; the level
statements of (ii) are not computable.
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

SQR = (1, 1, -1, -1, -1, -1)
G = [[F(SQR[a]) if a == b else F(0) for b in range(6)] for a in range(6)]
N0 = [F(1, 2), F(0), F(1, 2), F(0), F(0), F(0)]
NINF = [F(1), F(0), F(-1), F(0), F(0), F(0)]
ST = (1, 3, 4, 5)


def antisym(entries):
    M = [[F(0)] * 6 for _ in range(6)]
    for (a, b), v in entries.items():
        M[a][b] = F(v)
        M[b][a] = -F(v)
    return M


MOMENTS = [antisym({(0, 1): 1, (2, 3): 2, (4, 5): -1, (0, 5): 3}),
           antisym({(a, b): (a + 2 * b) % 5 - 2 for a, b in combinations(range(6), 2)}),
           antisym({(0, 2): F(1, 2), (1, 3): -3, (1, 4): 2, (3, 5): F(7, 3), (2, 4): 1}),
           antisym({(a, b): F(1, a + b + 1) for a, b in combinations(range(6), 2)})]
OTHER_I = [[F(1), F(0), F(0), F(0), F(0), F(0)], [F(0), F(0), F(0), F(1), F(0), F(0)], [F(1), F(2), F(0), F(1), F(1), F(0)],
           [F(0), F(1), F(3), F(0), F(-1), F(2)]]
LAMBDAS = [F(3), F(-2), F(6, 5)]
SPINORS = [sp2(1, 0), sp2(0, 1), sp2(1, QI(0, 1)), sp2(QI(2, -1), 3), sp2(F(1, 2), QI(-1, 4)), sp2(QI(0, 3), QI(5, 2))]
RVECS = [(1, 0, 0, 0), (2, 1, -1, 3), (F(1, 2), F(3, 4), 0, -2), (5, 3, 4, 0)]


def bil(M, u, v):
    return sum((u[a] * M[a][b] * v[b] for a in range(6) for b in range(6)), F(0))


def ip(u, v):
    return bil(G, u, v)


def grip(M, I):
    """P with <P, U> = M(U, I): P^a = g^aa M(e_a, I)."""
    return [F(SQR[a]) * sum((M[a][b] * I[b] for b in range(6)), F(0)) for a in range(6)]


def casimir(M, basis):
    gram = [[ip(x, y) for y in basis] for x in basis]
    n = len(basis)
    inv = [GA.field_solve(gram, [F(1) if i == j else F(0) for i in range(n)]) for j in range(n)]
    inv = [[inv[j][i] for j in range(n)] for i in range(n)]
    Mb = [[bil(M, x, y) for y in basis] for x in basis]
    return F(1, 2) * sum((inv[a][a2] * inv[b][b2] * Mb[a][b] * Mb[a2][b2]
                          for a in range(n) for a2 in range(n) for b in range(n) for b2 in range(n)), F(0))


def perp_basis(I):
    return [[F(x) for x in k] for k in GA.field_kernel([[F(SQR[a]) * I[a] for a in range(6)]])]


def check_grip_is_the_casimir_difference():
    premise("mass.casimir-form-join")
    ok = True
    Is = [[NINF[a] + L / 6 * N0[a] for a in range(6)] for L in LAMBDAS] + OTHER_I
    E = [[F(1) if a == b else F(0) for a in range(6)] for b in range(6)]
    for I in Is:
        QIv = ip(I, I)
        ok = ok and QIv != 0
        perp = perp_basis(I)
        ok = ok and len(perp) == 5
        for M in MOMENTS:
            P = grip(M, I)
            ok = ok and all(ip(P, u) == bil(M, u, I) for u in E)
            ok = ok and ip(P, I) == 0
            ok = ok and ip(P, P) == QIv * (casimir(M, E) - casimir(M, perp))
    for L, I in zip(LAMBDAS, Is):
        ok = ok and ip(I, I) == L / 3
        sig = GA.congruence_signature([[ip(x, y) for y in perp_basis(I)] for x in perp_basis(I)])
        ok = ok and sig == ((1, 4, 0) if L > 0 else (2, 3, 0))
    _tp_rv = (ok); assert _tp_rv is not False, "check_grip_is_the_casimir_difference"; return _tp_rv


def check_flat_grip_is_the_momentum():
    premise("mass.casimir-form-join")
    ok = True
    for M in MOMENTS:
        P = grip(M, NINF)
        ok = ok and ip(P, NINF) == 0
        p = [P[a] if a in ST else F(0) for a in range(6)]
        rest = [P[a] - p[a] for a in range(6)]
        # the rest is a multiple of n_inf
        ok = ok and GA.rank_of_vectors([rest, NINF]) <= 1
        ok = ok and ip(P, P) == ip(p, p)
        # p_a = M(e_a, n_inf) on the spacetime slots
        ok = ok and all(ip(P, [F(1) if c == a else F(0) for c in range(6)]) == M[a][0] * NINF[0] + M[a][2] * NINF[2]
                        for a in ST)
    _tp_rv = (ok); assert _tp_rv is not False, "check_flat_grip_is_the_momentum"; return _tp_rv


def check_spinor_momenta_and_area():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    ok = True
    for p in RVECS:
        ok = ok and det2(pauli_matrix(p)) == QI(mink(p))
    for p in SPINORS:
        P = momentum(p)
        ok = ok and det2(P) == ZQ and tr2(P).re > 0
    n = 0
    for p, q in combinations(SPINORS, 2):
        slot_matrix = [[p[0], p[1]], [q[0], q[1]]]
        ok = ok and bracket(p, q) == det2(slot_matrix)
        ok = ok and 2 * det2(momentum(p, q)) == QI(2 * absq(det2(slot_matrix)))
        n += 1
    ok = ok and n == 15
    _tp_rv = (ok); assert _tp_rv is not False, "check_spinor_momenta_and_area"; return _tp_rv
