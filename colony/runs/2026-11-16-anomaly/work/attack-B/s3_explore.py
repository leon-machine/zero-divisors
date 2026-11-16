"""S3 exploration: phase symmetries of the covariant coupling Y on c plus Y-tilde on c*, n families.
Exact arithmetic over the Gaussian rationals (numbers read in span{1, I_4}); real-linear systems over Q."""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
import GA
from GA import QI

I = QI(0, 1)


def zeros(r, c):
    return [[QI(0) for _ in range(c)] for _ in range(r)]


def unknown_basis(n):
    """Real basis of anti-Hermitian n x n matrices (generators of unitary family rotations)."""
    out = []
    for a in range(n):
        M = zeros(n, n); M[a][a] = I; out.append(M)
    for a in range(n):
        for b in range(a + 1, n):
            M = zeros(n, n); M[a][b] = QI(1); M[b][a] = QI(-1); out.append(M)
            M = zeros(n, n); M[a][b] = I; M[b][a] = I; out.append(M)
    return out


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), QI(0))


def T(A):
    return [list(r) for r in zip(*A)]


def add(A, B):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(A, B)]


def scal(c, A):
    return [[c * x for x in r] for r in A]


def conjm(A):
    return [[x.conj() for x in r] for r in A]


def system(Y, Yt, n):
    """Columns: K_Q, K_u, K_d (anti-Hermitian n x n), K_Phi (anti-Hermitian 2 x 2).
    Up term sum_k Phi_k Q^T A_k u, A = (Y, Yt); down term sum_k conj(Phi_k) Q^T B_k d, B = (Yt, Y),
    Phi = (alpha, conj beta). Rows: real and imaginary parts of each matrix entry of each condition."""
    bn, b2 = unknown_basis(n), unknown_basis(2)
    A, B = (Y, Yt), (Yt, Y)
    cols = []
    for s in range(3):
        for K in bn:
            col = []
            for j in range(2):
                up = zeros(n, n); dn = zeros(n, n)
                if s == 0:
                    up = mm(T(K), A[j]); dn = mm(T(K), B[j])
                if s == 1:
                    up = mm(A[j], K)
                if s == 2:
                    dn = mm(B[j], K)
                col += [up, dn]
            cols.append(col)
    for K in b2:
        col = []
        for j in range(2):
            up = zeros(n, n); dn = zeros(n, n)
            for k in range(2):
                up = add(up, scal(K[k][j], A[k]))
                dn = add(dn, scal(K[k][j].conj(), B[k]))
            col += [up, dn]
        cols.append(col)
    rows = []
    for blk in range(4):
        for i in range(n):
            for j in range(n):
                rows.append([c[blk][i][j].re for c in cols])
                rows.append([c[blk][i][j].im for c in cols])
    # colour coefficient functional: (2 tr K_Q + tr K_u + tr K_d)/I, real
    coef = []
    for s in range(3):
        for K in bn:
            t = tr(K)
            assert t.re == 0
            coef.append((2 if s == 0 else 1) * t.im)
    coef += [F(0)] * len(b2)
    # doublet weights: q1 - q2 = (K_11 - K_22)/I
    dq = [F(0)] * (3 * len(bn)) + [(K[0][0] - K[1][1]).im for K in b2]
    return rows, coef, dq


def report(name, Y, Yt):
    n = len(Y)
    rows, coef, dq = system(Y, Yt, n)
    ker = GA.field_kernel([[F(x) for x in r] for r in rows])
    vals = [sum(c * k for c, k in zip(coef, v)) for v in ker]
    dqs = [sum(c * k for c, k in zip(dq, v)) for v in ker]
    print(name, "n =", n, "solution space dim", len(ker), "colour coefficients", vals, "q1-q2", dqs)
    return ker, vals, dqs


def qm(rows):
    return [[x if isinstance(x, QI) else QI(F(x)) for x in r] for r in rows]


if __name__ == "__main__":
    # generic invertible pairs
    Y3 = qm([[2, QI(1, 1), 0], [QI(1, 1), 3, QI(0, 2)], [0, QI(0, 2), 5]])
    Yt3 = qm([[1, 0, QI(2, -1)], [0, QI(0, 3), 1], [QI(2, -1), 1, 7]])
    report("generic symmetric invertible", Y3, Yt3)
    Z3 = zeros(3, 3)
    report("Yt = 0", Y3, Z3)
    report("Yt = Y", Y3, Y3)
    report("Yt = 2Y", Y3, scal(QI(2), Y3))
    report("Yt = I Y", Y3, scal(I, Y3))
    # flavoured counter-models
    one2 = qm([[1, 0], [0, 1]]); E12 = qm([[0, 1], [0, 0]])
    report("Y = 1, Yt = E12", one2, E12)
    report("split Y=diag(1,1,0), Yt=diag(0,0,1)", qm([[1, 0, 0], [0, 1, 0], [0, 0, 0]]), qm([[0, 0, 0], [0, 0, 0], [0, 0, 1]]))
    report("Y inv, Yt rank one generic", Y3, qm([[1, 2, 3], [2, 4, 6], [3, 6, 9]]))
    report("Y inv diag, Yt rank 2 diag", qm([[1, 0, 0], [0, 2, 0], [0, 0, 3]]), qm([[1, 0, 0], [0, 1, 0], [0, 0, 0]]))
    report("Y inv diag, Yt nilpotent", qm([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), qm([[0, 1, 0], [0, 0, 1], [0, 0, 0]]))
