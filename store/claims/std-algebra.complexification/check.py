from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def to_mat(M):
    return S.mat(M)


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def right_matrix(x, sq):
    n = len(sq)
    blades = GA.all_blades(n)
    cols = [S.coords(GA.mul({b: F(1)}, x, sq), n) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


def flat(M):
    return [a for row in M for a in row]


I_ = GA.QI(0, 1)
S1 = [[0, 1], [1, 0]]
S2 = [[GA.QI(0), -I_], [I_, GA.QI(0)]]
S3 = [[1, 0], [0, -1]]
ONE2 = [[1, 0], [0, 1]]


def complex_gens(n):
    """Generators of Cl_n(C), all squaring to 1, on C^2 (n <= 2) or C^4 (n = 3, 4)."""
    s1, s2, s3, one = to_mat(S1), S2, to_mat(S3), to_mat(ONE2)
    if n == 1:
        return [s3]
    if n == 2:
        return [s3, s1]
    return [kron(s1, one), kron(s2, one), kron(s3, s1), kron(s3, s2)][:n]


def complex_dim(Ms):
    prods = []
    n = len(Ms)
    d = len(Ms[0])
    for k in range(n + 1):
        for idx in combinations(range(n), k):
            P = S.mat_id(d)
            for i in idx:
                P = S.mat_mul(P, Ms[i])
            prods.append(P)
            prods.append(S.mat_scal(I_, P))
    return S.real_span_rank(prods)


def check_complex_forms():
    premise("std-algebra.tensor-rules")
    premise("std-algebra.periodicity")
    ok = True
    dims = []
    for n in range(1, 5):
        g = complex_gens(n)
        ok = ok and S.check_matrix_rep(g, GA.sig(n, 0), 2 ** n)
        dims.append((len(g[0]), complex_dim(g)))
        # every real form Cl(p, q) sits inside: multiply q generators by i
        for q in range(n + 1):
            gq = [S.mat_scal(I_, M) if i >= n - q else M for i, M in enumerate(g)]
            ok = ok and S.check_matrix_rep(gq, GA.sig(n - q, q), 2 ** n)
            ok = ok and complex_dim(gq) == complex_dim(g)
    # (matrix size, real dimension of the complex span): M_2(C)+..., i.e. complex dim 2^n
    ok = ok and dims == [(2, 4), (2, 8), (4, 16), (4, 32)]
    GA.check("Cl_n(C) is M_2(C), M_2(C)+M_2(C), M_4(C) for n = 2, 3, 4; every Cl(p,q) is a real form", ok)
    return ok


ODD_NS = (1, 3, 5)
SEEDS = (2, 5, 3, 4)


def check_odd_dimension_split():
    premise("std-algebra.z2-grading")
    premise("primer.centre")
    premise("primer.sign")
    ok = True
    kinds = []
    ranks = []
    for n in ODD_NS:
        for q in range(n + 1):
            p = n - q
            sq = GA.sig(p, q)
            om = S.pseudoscalar(n)
            ok = ok and all(GA.commutes(om, GA.gen(i), sq) for i in range(n))
            w2 = GA.mul(om, om, sq).get((), F(0))
            evens = [{b: F(1)} for b in GA.all_blades(n) if len(b) % 2 == 0]
            ev = range(0, n + 1, 2)
            a, b, c, d = [S.sample(n, t, grades_=ev) for t in SEEDS]
            if w2 == 1:
                P = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
                Pm = GA.scal(F(1, 2), GA.sub(GA.sc(1), om))
                ok = ok and GA.eq(GA.mul(P, P, sq), P) and GA.is_zero(GA.mul(P, Pm, sq))
                ok = ok and GA.eq(GA.mul(GA.mul(a, b, sq), P, sq), GA.mul(GA.mul(a, P, sq), GA.mul(b, P, sq), sq))
                rk = S.span_rank([GA.mul(x, P, sq) for x in evens], n)
                ranks.append(rk)
                kinds.append(1)
            else:
                ok = ok and w2 == -1
                lhs = GA.mul(GA.add(a, GA.mul(b, om, sq)), GA.add(c, GA.mul(d, om, sq)), sq)
                re = GA.sub(GA.mul(a, c, sq), GA.mul(b, d, sq))
                im = GA.add(GA.mul(a, d, sq), GA.mul(b, c, sq))
                ok = ok and GA.eq(lhs, GA.add(re, GA.mul(im, om, sq)))
                rk = S.span_rank(evens + [GA.mul(x, om, sq) for x in evens], n)
                ranks.append(rk)
                kinds.append(-1)
    ok = ok and kinds == [1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1]
    ok = ok and ranks == [1, 2, 8, 4, 8, 4, 16, 32, 16, 32, 16, 32]
    GA.check("odd n: omega central; Cl = Cl+ + Cl+ when omega^2 = 1, Cl = Cl+ (x) C when omega^2 = -1", ok)
    return ok
