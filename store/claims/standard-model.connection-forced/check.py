"""standard-model.connection-forced: exact checks of the two Lie-algebra reductions.

(1) The S factor, in Cl(2,4) (e0 (+1), e1..e3 (-1), e+ (+1), e- (-1), n0 = (e+ + e-)/2, ninf = e+ - e-).
    The tangent algebra of Spin(2,4) at 1: the even, reverse-odd multivectors X (grades 2 and 6) whose
    commutator with every vector is a vector are exactly the 15 bivectors, so(2,4). Acting on the
    conformal spinor space CS = Cl^+(2,4) P (P = (1 + e0e1)(1 + e2e+)/4, complex unit I6) by X/2 they
    commute with I6 and are faithful (operator rank 15); the conformal spinor connection of a
    gravitational field, Omega_T(a)/2 with Omega_T(a) = Omega(a) - ninf ^ A + n0 ^ P(A), lies in this
    span. So a Spin(2,4)-connection on S has connection form valued in so(2,4).
(2) The H factor, C^2 (x) C^3 = C^6. The infinitesimal maps X that keep the set of decomposable tensors
    (tangent condition X(u (x) v) in u (x) C^3 + C^2 (x) v, imposed at 15 rational points) form a space of
    dimension 12, which is gl(2) (x) 1 + 1 (x) gl(3) (rank 12 of those 13 generators, all satisfying the
    conditions). Its anti-Hermitian part (preserving the Hermitian structure) is X = Xr + i Xi with Xr
    antisymmetric and Xi symmetric, both in that space: dimensions 4 + 8 = 12 = 3 + 8 + 1, the algebra
    su(2) + su(3) + u(1) (traceless parts 3 + 8, centre i 1). Conversely every A (x) 1 + 1 (x) B with A, B
    anti-Hermitian satisfies the tangent condition and is anti-Hermitian, so each such pair gives a
    connection with the stated properties.
Real rational points suffice: the conditions have real coefficients, so the complex solution space is
the complexification of the real one.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
BLADES = GA.all_blades(6)
VB = [(i,) for i in range(6)]


def mul(*xs):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, S)
    return r


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def rank(xs):
    return GA.rank_of_vectors([GA.basis_vector_of(x, BLADES) for x in xs]) if xs else 0


I6 = mul(*E)
PID = GA.scal(F(1, 4), mul(GA.add(GA.sc(1), mul(E[0], E[1])), GA.add(GA.sc(1), mul(E[2], E[4]))))


def _cs():
    out = []
    for b in BLADES:
        if len(b) % 2 == 0:
            c = GA.mul({b: F(1)}, PID, S)
            if rank(out + [c]) == len(out) + 1:
                out.append(c)
    return out


CS = _cs()
HINV = [[2, 1, 0, 0], [0, 1, 0, -1], [1, 0, 3, 0], [0, 0, 1, 1]]
PSYM = [[2, 1, 0, -3], [1, -1, 4, 0], [0, 4, 5, 2], [-3, 0, 2, 7]]
OMEGA = [mul(E[0], E[1]), GA.add(mul(E[1], E[2]), mul(E[0], E[3])), mul(E[2], E[3]), mul(E[0], E[2])]
DIRS = ([1, 0, 0, 0], [3, 1, -2, 5])
POINTS = [([1, 2], [1, 0, 3]), ([2, -1], [3, 1, 1]), ([0, 1], [1, 2, -1]), ([1, 1], [2, -3, 1]),
          ([3, 1], [1, 1, 1]), ([1, -2], [4, 0, 1]), ([2, 3], [1, -1, 2]), ([1, 0], [5, 2, 3]),
          ([1, 3], [2, 1, 0]), ([4, 1], [1, 3, 2]), ([2, 1], [3, -2, 5]), ([1, 4], [1, 1, -3]),
          ([3, -1], [2, 2, 1]), ([1, 5], [3, 0, -1]), ([5, 2], [1, 4, 1])]


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def lin(M, A, out):
    return GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), out[n]) for n in range(4)])


def check_spin_connection_form_is_so24():
    premise("standard-model.imported-tractor-bundle-spinor-bundle-their")
    # even, reverse-odd candidates: grade 2 and grade 6 blades
    cand = [{b: F(1)} for b in BLADES if len(b) in (2, 6)]
    ok = len(cand) == 16
    rows = []
    for v in E:
        cols = [comm(X, v) for X in cand]
        nonvec = sorted({b for c in cols for b in c if len(b) != 1})
        rows += [[c.get(b, F(0)) for c in cols] for b in nonvec]
    ker = GA.field_kernel(rows)
    ok = ok and len(ker) == 15
    ok = ok and all(k[-1] == 0 for k in ker)                 # the pseudoscalar is excluded
    ops = []
    for b in BLADES:
        if len(b) == 2:
            B = {b: F(1)}
            row = []
            for p in CS:
                img = GA.scal(F(1, 2), mul(B, p))
                ok = ok and GA.eq(mul(I6, img), GA.scal(F(1, 2), mul(B, I6, p)))
                ok = ok and rank(CS + [img]) == 8
                row += GA.basis_vector_of(img, BLADES)
            ops.append(row)
    ok = ok and len(CS) == 8 and GA.rank_of_vectors(ops) == 15
    for a in DIRS:
        av = vec(a)
        A = lin(HINV, av, E)
        om = GA.add(*[GA.scal(dot(av, ER[m]), OMEGA[m]) for m in range(4)])
        omT = GA.add(om, GA.neg(comm(NI, A)), comm(N0, lin(PSYM, A, ER)))
        ok = ok and all(len(b) == 2 for b in omT)
    GA.check("Spin(2,4) connection form: the tangent algebra is the 15 bivectors, faithful on CS", ok)
    assert ok


def kron_rows(u, v):
    """Two tangent conditions at u (x) v: (alpha (x) beta)(X (u (x) v)) = 0, alpha . u = 0, beta . v = 0."""
    w = [F(u[i] * v[j]) for i in range(2) for j in range(3)]
    alpha = [-u[1], u[0]]
    betas = [[v[1], -v[0], 0], [v[2], 0, -v[0]]]
    out = []
    for beta in betas:
        ab = [F(alpha[i] * beta[j]) for i in range(2) for j in range(3)]
        out.append([ab[r] * w[c] for r in range(6) for c in range(6)])
    return out


def kron(A, B):
    return [[F(A[i][k] * B[j][l]) for k in range(len(A)) for l in range(len(B))]
            for i in range(len(A)) for j in range(len(B))]


def unit(n, i, j):
    return [[1 if (r, c) == (i, j) else 0 for c in range(n)] for r in range(n)]


def flat(M):
    return [x for row in M for x in row]


def check_factorisation_preserving_unitary_algebra():
    premise("standard-model.segre-lemma-automorphisms-preserving-decomposable-tensors")
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    rows = [r for (u, v) in POINTS for r in kron_rows(u, v)]
    ok = 36 - GA.mat_rank(rows) == 12
    one2 = [[1, 0], [0, 1]]
    one3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    gens = ([flat(kron(unit(2, i, j), one3)) for i in range(2) for j in range(2)]
            + [flat(kron(one2, unit(3, i, j))) for i in range(3) for j in range(3)])
    ok = ok and GA.mat_rank(gens) == 12
    ok = ok and all(sum(r[k] * g[k] for k in range(36)) == 0 for r in rows for g in gens)
    anti = []
    sym = []
    for r in range(6):
        for c in range(r, 6):
            e = [F(0)] * 36
            e[6 * r + c] += 1
            e[6 * c + r] += 1                                 # X + X^T = 0
            anti.append(e)
            if r != c:
                d = [F(0)] * 36
                d[6 * r + c], d[6 * c + r] = F(1), F(-1)      # X - X^T = 0
                sym.append(d)
    dim_anti = 36 - GA.mat_rank(rows + anti)
    dim_sym = 36 - GA.mat_rank(rows + sym)
    ok = ok and dim_anti == 4 and dim_sym == 8 and dim_anti + dim_sym == 3 + 8 + 1
    # the kernels are spanned by (so(2) (x) 1 + 1 (x) so(3)) and (sym(2) (x) 1 + 1 (x) sym(3)): the real and
    # imaginary parts of u(2) (x) 1 + 1 (x) u(3)
    def msub(A, B):
        return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

    def madd(A, B):
        return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]
    so_g = ([flat(kron(msub(unit(2, 0, 1), unit(2, 1, 0)), one3))]
            + [flat(kron(one2, msub(unit(3, i, j), unit(3, j, i)))) for i in range(3) for j in range(i + 1, 3)])
    sym_g = ([flat(kron(madd(unit(2, i, j), unit(2, j, i)), one3)) for i in range(2) for j in range(i, 2)]
             + [flat(kron(one2, madd(unit(3, i, j), unit(3, j, i)))) for i in range(3) for j in range(i, 3)])
    ok = ok and GA.mat_rank(so_g) == 4 and GA.mat_rank(sym_g) == 8
    ok = ok and all(sum(r[k] * g[k] for k in range(36)) == 0 for r in rows + anti for g in so_g)
    ok = ok and all(sum(r[k] * g[k] for k in range(36)) == 0 for r in rows + sym for g in sym_g)
    GA.check("factorisation- and Hermitian-preserving algebra on C^2 (x) C^3 is su(2) + su(3) + u(1)", ok)
    assert ok
