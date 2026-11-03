"""neutrino.invariant-symmetric-matrices: exact checks (rational 3 x 3 matrices).

(1) Characterisation: the conditions P S P^T = S over all six permutation matrices, written as a
linear system in the six independent entries of a symmetric S, have a solution space of dimension
exactly 2, and it is span{1, J}: the "only if" direction. Every alpha 1 + beta J on a sample grid is
invariant ("if"); a symmetric matrix with unequal diagonal or unequal off-diagonal entries is not.
(2) Spectrum and determinant on a 4 x 4 grid of (alpha, beta) (det is a polynomial of degree 3 in
alpha and 1 in beta, so the grid fixes the identity): J u' = 3 u', S u' = (alpha + 3 beta) u',
the kernel of S - alpha 1 is u'^perp (dimension 2 when beta != 0), det S = alpha^2 (alpha + 3 beta)
by cofactor expansion, and the rank of S drops exactly on alpha = 0 or alpha = -3 beta.
(3) Inverse and projector forms: the stated S^-1 agrees with the inverse found by Gaussian
elimination; Pi = 1 - J/3 is the projector on u'^perp (Pi^2 = Pi, Pi J = 0, Pi u' = 0, (J/3)^2 = J/3);
S = alpha Pi + M_3 J/3 and S^-1 = Pi/alpha + J/(3 M_3).
Self-contained lemma: no premises.
"""
from fractions import Fraction as F
from itertools import permutations

import GA

ALPHAS = (F(2), F(-1), F(7, 2), F(1, 5))
BETAS = (F(1), F(5, 3), F(-3), F(2, 7))
GENERIC = [[F(1), F(2), F(2)], [F(2), F(1), F(3)], [F(2), F(3), F(1)]]
GENERIC2 = [[F(1), F(2), F(2)], [F(2), F(5), F(2)], [F(2), F(2), F(1)]]
U = [F(1), F(1), F(1)]


def ident():
    return [[F(int(i == j)) for j in range(3)] for i in range(3)]


def jmat():
    return [[F(1)] * 3 for _ in range(3)]


def lin(a, A, b, B):
    return [[a * A[i][j] + b * B[i][j] for j in range(3)] for i in range(3)]


def mv(A, x):
    return [sum((A[i][k] * x[k] for k in range(3)), F(0)) for i in range(3)]


def tr(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def perm_matrix(p):
    return [[F(int(p[i] == j)) for j in range(3)] for i in range(3)]


def invariant(S):
    return all(GA.mat_mul(GA.mat_mul(perm_matrix(p), S), tr(perm_matrix(p))) == S
               for p in permutations(range(3)))


IDX = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def sym_from(x):
    S = [[F(0)] * 3 for _ in range(3)]
    for (i, j), val in zip(IDX, x):
        S[i][j] = S[j][i] = val
    return S


def check_characterisation():
    rows = []
    for p in permutations(range(3)):
        P = perm_matrix(p)
        for (i, j) in IDX:
            row = []
            for k in range(6):
                e = [F(int(k == m)) for m in range(6)]
                Sk = sym_from(e)
                PSP = GA.mat_mul(GA.mat_mul(P, Sk), tr(P))
                row.append(PSP[i][j] - Sk[i][j])
            rows.append(row)
    ker = GA.field_kernel(rows)
    ok = len(ker) == 2
    ok = ok and all(invariant(sym_from(k)) for k in ker)
    I_vec = [F(1), F(1), F(1), F(0), F(0), F(0)]
    J_vec = [F(1)] * 6
    ok = ok and GA.rank_of_vectors(ker + [I_vec, J_vec]) == 2
    ok = ok and all(invariant(lin(a, ident(), b, jmat())) for a in ALPHAS for b in BETAS)
    ok = ok and invariant(lin(F(0), ident(), F(4), jmat()))
    ok = ok and not invariant(GENERIC) and not invariant(GENERIC2)
    GA.check("S3-invariant symmetric 3x3 matrices: solution space of dimension 2 equal to span{1, J}", ok)
    return ok


def check_spectrum_and_determinant():
    ok = True
    perp = [[F(1), F(-1), F(0)], [F(1), F(1), F(-2)]]
    for a in ALPHAS:
        for b in BETAS:
            S = lin(a, ident(), b, jmat())
            M3 = a + 3 * b
            ok = ok and mv(jmat(), U) == [3 * x for x in U]
            ok = ok and mv(S, U) == [M3 * x for x in U]
            ok = ok and all(mv(S, x) == [a * c for c in x] for x in perp)
            ker = GA.field_kernel(lin(F(1), S, -a, ident()))
            ok = ok and len(ker) == 2 and all(sum(k) == 0 for k in ker)
            ker3 = GA.field_kernel(lin(F(1), S, -M3, ident()))
            ok = ok and len(ker3) == 1 and ker3[0][0] == ker3[0][1] == ker3[0][2]
            ok = ok and det3(S) == a * a * (a + 3 * b)
            ok = ok and GA.mat_rank(S) == 3
    for b in BETAS:
        ok = ok and det3(lin(F(0), ident(), b, jmat())) == 0 and GA.mat_rank(lin(F(0), ident(), b, jmat())) == 1
        ok = ok and det3(lin(-3 * b, ident(), b, jmat())) == 0 and GA.mat_rank(lin(-3 * b, ident(), b, jmat())) == 2
    GA.check("eigenvalue alpha + 3 beta on u', alpha on u'^perp, det = alpha^2 (alpha + 3 beta), singular loci", ok)
    return ok


def check_inverse_and_projector_forms():
    ok = True
    I3, J = ident(), jmat()
    Pi = lin(F(1), I3, F(-1, 3), J)
    ok = ok and GA.mat_mul(Pi, Pi) == Pi and GA.mat_mul(Pi, J) == [[F(0)] * 3] * 3
    ok = ok and mv(Pi, U) == [F(0)] * 3 and GA.mat_mul(lin(F(1, 3), J, F(0), J), lin(F(1, 3), J, F(0), J)) == lin(F(1, 3), J, F(0), J)
    for a in ALPHAS:
        for b in BETAS:
            S = lin(a, I3, b, J)
            M3 = a + 3 * b
            Sinv = lin(1 / a, I3, -b / (a * M3), J)
            cols = [GA.field_solve(S, [F(int(i == c)) for i in range(3)]) for c in range(3)]
            elim = [[cols[c][r] for c in range(3)] for r in range(3)]
            ok = ok and Sinv == elim and GA.mat_mul(S, Sinv) == I3
            ok = ok and lin(a, Pi, M3 / 3, J) == S
            ok = ok and lin(1 / a, Pi, 1 / (3 * M3), J) == Sinv
    GA.check("S^-1 = 1/alpha - beta/(alpha(alpha + 3 beta)) J = Pi/alpha + J/(3 M_3); S = alpha Pi + M_3 J/3", ok)
    return ok
