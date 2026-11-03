"""families.classification-displaced-gaussian-class-solved-level: exact checks of clause (1).

Clauses (2) and (3) are preliminary computations (a displaced-Gaussian scan checked against Fock
evaluation) that the statement itself says are not reproduced by the paper's script; they have no
exact content to recompute here beyond the consistency of the figures quoted, which is checked
(206.77 / 1.2032 rounds to the stated factor 172). Clause (1), closed by theorem, is checked
exactly over Q(i) (GA.QI), with Gaussian-rational 3-vectors a and rational x = sinh^2 r >= 0:
(a) Proposition families.rigidity-pairing-sector-one-event: the family factor G = [a]_x of every
    antisymmetric pairing has G G^dagger = |a|^2 1 - conj(a) a^T, with characteristic polynomial
    t (t - |a|^2)^2 (trace, principal-minor sum and determinant computed) and
    rank(G G^dagger - |a|^2 1) = 1: doubly degenerate identically in a;
(b) Theorem families.skeleton-rank-one-plus-ordering-shift: with P = conj(n) n^T = conj(a) a^T / |a|^2
    (a rank-one projector, rational in Q(i) although |a| is not), the mass form
    H = cosh^2 r 1 + x (5 + 6x) P has characteristic polynomial (t - cosh^2 r)^2 (t - (1 + 6x + 6x^2))
    with cosh^2 r = 1 + x, trace 3 + 8x + 6x^2, rank(H - cosh^2 r) = 1 (the light pair exactly
    degenerate for every pairing and depth), heavy direction conj(a), and the split
    H = 2x(2 + 3x) P (rank one) + (cosh^2 r 1 + x P) whose restriction to the light plane is
    cosh^2 r: no antisymmetric pairing splits the light pair.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
A_SAMPLES = [(QI(1), QI(0, 1), QI(2, -1)), (QI(3, 2), QI(-1), QI(0, 4)), (QI(1, 1), QI(1, -1), QI(F(1, 2))),
             (QI(0), QI(0), QI(5)), (QI(2), QI(-3), QI(7))]
X_SAMPLES = [F(0), F(1, 3), F(2), F(7, 5)]


def cross_matrix(a):
    a1, a2, a3 = a
    z = QI(0)
    return [[z, -a3, a2], [a3, z, -a1], [-a2, a1, z]]


def dagger(M):
    return [[M[j][i].conj() for j in range(3)] for i in range(3)]


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), QI(0)) for j in range(3)] for i in range(3)]


def norm2(a):
    return sum((x * x.conj() for x in a), QI(0))


def char_coeffs(M):
    """(trace, sum of principal 2-minors, determinant)."""
    tr = M[0][0] + M[1][1] + M[2][2]
    m2 = sum((M[i][i] * M[j][j] - M[i][j] * M[j][i] for i, j in ((0, 1), (0, 2), (1, 2))), QI(0))
    det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
           + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return tr, m2, det


def shift(M, lam):
    return [[M[i][j] - (lam if i == j else QI(0)) for j in range(3)] for i in range(3)]


def check_family_factor_doubly_degenerate():
    premise("families.rigidity-pairing-sector-one-event")
    ok = True
    for a in A_SAMPLES:
        G = cross_matrix(a)
        GG = matmul(G, dagger(G))
        s = norm2(a)
        want = [[(s if i == j else QI(0)) - a[i].conj() * a[j] for j in range(3)] for i in range(3)]
        ok = ok and GG == want
        ok = ok and char_coeffs(GG) == (2 * s, s * s, QI(0))
        ok = ok and GA.field_rank(shift(GG, s)) == 1 and GA.field_rank(GG) == 2
    GA.check("G G^dagger = |a|^2 1 - conj(a) a^T, spectrum {|a|^2, |a|^2, 0} for every a", ok)
    return ok


def check_light_pair_exactly_degenerate():
    premise("families.skeleton-rank-one-plus-ordering-shift")
    premise("families.rigidity-pairing-sector-one-event")
    ok = True
    for a in A_SAMPLES:
        s = norm2(a)
        P = [[a[i].conj() * a[j] / s for j in range(3)] for i in range(3)]
        ok = ok and matmul(P, P) == P and GA.field_rank(P) == 1 and char_coeffs(P)[0] == QI(1)
        for x in X_SAMPLES:
            c2 = 1 + x
            heavy = 1 + 6 * x + 6 * x * x
            H = [[(QI(c2) if i == j else QI(0)) + x * (5 + 6 * x) * P[i][j] for j in range(3)] for i in range(3)]
            tr, m2, det = char_coeffs(H)
            # (t - c2)^2 (t - heavy) = t^3 - (2 c2 + heavy) t^2 + (c2^2 + 2 c2 heavy) t - c2^2 heavy
            ok = ok and tr == 2 * c2 + heavy and m2 == c2 * c2 + 2 * c2 * heavy and det == c2 * c2 * heavy
            ok = ok and tr == 3 + 8 * x + 6 * x * x
            ok = ok and (GA.field_rank(shift(H, QI(c2))) == (1 if x != 0 else 0))
            abar = [z.conj() for z in a]
            ok = ok and [sum((H[i][j] * abar[j] for j in range(3)), QI(0)) for i in range(3)] == [heavy * z for z in abar]
            no = [[2 * x * (2 + 3 * x) * P[i][j] for j in range(3)] for i in range(3)]
            sh = [[(QI(c2) if i == j else QI(0)) + x * P[i][j] for j in range(3)] for i in range(3)]
            ok = ok and [[no[i][j] + sh[i][j] for j in range(3)] for i in range(3)] == H
            # the shift on the light plane (the kernel of P) is cosh^2 r
            for u in GA.field_kernel(P):
                ok = ok and [sum((sh[i][j] * u[j] for j in range(3)), QI(0)) for i in range(3)] == [c2 * z for z in u]
    GA.check("H = cosh^2 r 1 + x(5+6x) P: light pair exactly degenerate at cosh^2 r for every pairing", ok)
    return ok


QUOTED_MU_E = F(20677, 100)       # quoted input: the physical ratio m_mu / m_e = 206.77 of clause (2)
QUOTED_CAP = F(12032, 10000)      # quoted input: the equal-amplitude cap 1.2032 of clause (3)


def check_quoted_figures_consistent():
    ratio = QUOTED_MU_E / QUOTED_CAP
    ok = round(ratio) == 172 and ratio != round(ratio)      # nearest integer 172, and a rounding (not exact)
    GA.check("206.77 / 1.2032 rounds to the stated factor 172", ok)
    return ok
