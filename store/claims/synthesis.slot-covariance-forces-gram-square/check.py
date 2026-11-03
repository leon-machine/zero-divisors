"""synthesis.slot-covariance-forces-gram-square: exact checks.

Complex numbers are Gaussian rationals (re, im) of Fractions; the unit is checked to be the
field theory's I4 of Cl(1,3) (I4^2 = -1, central in the even algebra), whose span{1, I4} the
store reads physical numbers in. Conformal spinors Z = (omega, pi) are pairs of 2-spinors; the
face vector is beta_k = B^{ij}_Lambda for (i, j) the cyclic successors of k, with
B^{il}_Lambda = [pi^i pi^l] + lam [omega^i omega^l] (lam = Lambda/6) and h = t + t^dagger,
t_il = conj(pi^i) . omega^l, as in the many-twistor join.
"""
from fractions import Fraction as F
import itertools
import GA
from GA import mul, gen
from tp_premise import premise

Z0 = (F(0), F(0)); ONE = (F(1), F(0)); IU = (F(0), F(1))


def cm(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def ca(*xs): return (sum((x[0] for x in xs), F(0)), sum((x[1] for x in xs), F(0)))
def cc(a): return (a[0], -a[1])
def cn(a): return (-a[0], -a[1])
def cr(q): return (F(q), F(0))
def ab2(a): return a[0] * a[0] + a[1] * a[1]


def unit_is_I4():
    sq = (1, -1, -1, -1)
    I4 = mul(mul(gen(0), gen(1), sq), mul(gen(2), gen(3), sq), sq)
    assert mul(I4, I4, sq) == {(): F(-1)}
    e01 = mul(gen(0), gen(1), sq)
    assert mul(I4, e01, sq) == mul(e01, I4, sq)          # central in the even algebra
    assert cm(IU, IU) == (F(-1), F(0))


def mat(M, N):
    return [[ca(*[cm(M[i][k], N[k][j]) for k in range(3)]) for j in range(3)] for i in range(3)]
def dag(M): return [[cc(M[j][i]) for j in range(3)] for i in range(3)]
def tr_(M): return [[M[j][i] for j in range(3)] for i in range(3)]
def det3(M):
    s = Z0
    for p in itertools.permutations(range(3)):
        sg = 1
        for a in range(3):
            for b in range(a + 1, 3):
                if p[a] > p[b]: sg = -sg
        t = cr(sg)
        for i in range(3): t = cm(t, M[i][p[i]])
        s = ca(s, t)
    return s


def br(x, y): return ca(cm(x[0], y[1]), cn(cm(x[1], y[0])))          # [x y] = eps_AB x^A y^B
def hp(x, y): return ca(cm(cc(x[0]), y[0]), cm(cc(x[1]), y[1]))      # conj(x) . y


def face_data(Zs, lam):
    B = [[ca(br(Zs[i][1], Zs[l][1]), cm(cr(lam), br(Zs[i][0], Zs[l][0]))) for l in range(3)] for i in range(3)]
    beta = [B[(k + 1) % 3][(k + 2) % 3] for k in range(3)]
    t = [[hp(Zs[i][1], Zs[l][0]) for l in range(3)] for i in range(3)]
    h = [[ca(t[i][l], cc(t[l][i])) for l in range(3)] for i in range(3)]
    return B, beta, h


def mix(Zs, U):
    return [tuple(tuple(ca(*[cm(Zs[j][s][A], U[j][i]) for j in range(3)]) for A in range(2))
                  for s in range(2)) for i in range(3)]


def g(re, im=0): return (F(re), F(im))
CONFIGS = [
    [((g(1), g(0, 1)), (g(2), g(-1))), ((g(0), g(1, 1)), (g(3), g(1, -2))), ((g(-1), g(2)), (g(1, 1), g(0)))],
    [((g(1, 2), g(3)), (g(0, -1), g(1))), ((g(2), g(-1, 1)), (g(1), g(2, 1))), ((g(1), g(1)), (g(-2), g(0, 3)))],
    [((g(F(1, 2)), g(0)), (g(1), g(1, 1))), ((g(1), g(-1)), (g(0, 2), g(3))), ((g(0, 1), g(2)), (g(1), g(-1, -1)))],
    [((g(3), g(1)), (g(1, -1), g(2))), ((g(0), g(0, 1)), (g(1), g(0))), ((g(2, 1), g(-1)), (g(0), g(1, 2)))],
]
LAMS = [F(0), F(1, 6), F(-2, 3), F(5)]
H2 = [[g(F(1, 2), F(1, 2)), g(F(1, 2), F(-1, 2))], [g(F(1, 2), F(-1, 2)), g(F(1, 2), F(1, 2))]]
UNITARIES = [
    [[g(0), g(1), g(0)], [g(1), g(0), g(0)], [g(0), g(0), g(1)]],                 # odd permutation
    [[g(0), g(0), g(1)], [g(1), g(0), g(0)], [g(0), g(1), g(0)]],                 # 3-cycle
    [[g(0, 1), g(0), g(0)], [g(0), g(1), g(0)], [g(0), g(0), g(-1)]],             # phases
    [[g(F(3, 5)), g(F(-4, 5)), g(0)], [g(F(4, 5)), g(F(3, 5)), g(0)], [g(0), g(0), g(1)]],
    [[g(1), g(0), g(0)], [g(0), H2[0][0], H2[0][1]], [g(0), H2[1][0], H2[1][1]]],
]


def check_face_vector_cofactor():
    premise("synthesis.many-twistor-join")
    premise("standard-model.internal-symmetry-ladder")
    premise("families.chart-computation-sign-twist-bracket-form")
    unit_is_I4()
    for U in UNITARIES:
        Id = mat(dag(U), U)
        assert Id == [[ONE if i == j else Z0 for j in range(3)] for i in range(3)]
        d = det3(U)
        R = [[cm(d, x) for x in row] for row in dag(U)]                         # det(U) U^{-1}
        for Zs in CONFIGS:
            for lam in LAMS:
                B, beta, h = face_data(Zs, lam)
                B2, beta2, h2 = face_data(mix(Zs, U), lam)
                assert B2 == mat(mat(tr_(U), B), U)                             # B -> U^T B U
                assert beta2 == [ca(*[cm(R[k][m], beta[m]) for m in range(3)]) for k in range(3)]
                assert h2 == mat(mat(dag(U), h), U)                             # h -> U^dag h U
        if U is UNITARIES[0]:                                                   # sign twist: Omega -> -P Omega
            assert d == cr(-1)
    return True


# ---- invariant tensors A[k][l][m][n] of forms M_kl = sum A conj(beta_m) beta_n ----
def idx(k, l, m, n): return ((k * 3 + l) * 3 + m) * 3 + n


def nullity(rows, ncols=81):
    Mx = [[r.get(j, Z0) for j in range(ncols)] for r in rows]
    rank = 0
    for c in range(ncols):
        p = next((i for i in range(rank, len(Mx)) if Mx[i][c] != Z0), None)
        if p is None: continue
        Mx[rank], Mx[p] = Mx[p], Mx[rank]
        a = Mx[rank][c]; dd = ab2(a); iv = (a[0] / dd, -a[1] / dd)
        Mx[rank] = [cm(iv, x) for x in Mx[rank]]
        for i in range(len(Mx)):
            if i != rank and Mx[i][c] != Z0:
                f = Mx[i][c]; Mx[i] = [ca(x, cn(cm(f, y))) for x, y in zip(Mx[i], Mx[rank])]
        rank += 1
    return ncols - rank


def lie_rows(X):
    rows = []
    for k, l, a, b in itertools.product(range(3), repeat=4):
        r = {}
        def add(col, v): r[col] = ca(r.get(col, Z0), v)
        for m in range(3): add(idx(k, l, m, b), cc(X[m][a]))
        for n in range(3): add(idx(k, l, a, n), X[n][b])
        for p in range(3): add(idx(p, l, a, b), cn(cc(X[k][p])))
        for p in range(3): add(idx(k, p, a, b), cn(X[l][p]))
        r = {c: v for c, v in r.items() if v != Z0}
        if r: rows.append(r)
    return rows


def grp_rows(R):
    rows = []
    for k, l, a, b in itertools.product(range(3), repeat=4):
        r = {}
        for m in range(3):
            for n in range(3):
                c = R[m][a] * R[n][b]
                if c: r[idx(k, l, m, n)] = ca(r.get(idx(k, l, m, n), Z0), cr(c))
                c = R[k][m] * R[l][n]
                if c: r[idx(m, n, a, b)] = ca(r.get(idx(m, n, a, b), Z0), cr(-c))
        r = {c: v for c, v in r.items() if v != Z0}
        if r: rows.append(r)
    return rows


def u3_generators():
    gens = []
    def E(a, b, v):
        X = [[Z0] * 3 for _ in range(3)]; X[a][b] = v; return X
    for a in range(3):
        gens.append(E(a, a, IU))
        for b in range(a + 1, 3):
            X = E(a, b, ONE); X[b][a] = cr(-1); gens.append(X)
            X = E(a, b, IU); X[b][a] = IU; gens.append(X)
    return gens


def zero_diag_rows():
    return [{idx(k, k, m, n): ONE} for k in range(3) for m in range(3) for n in range(3)]


def tensor_ok(rows, A):
    return all(ca(*[cm(v, A.get(c, Z0)) for c, v in r.items()]) == Z0 for r in rows)


def check_invariant_forms():
    premise("standard-model.internal-symmetry-ladder")
    premise("families.chart-computation-sign-twist-bracket-form")
    U3 = [r for X in u3_generators() for r in lie_rows(X)]
    T = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]]          # sgn(P) P, P a transposition
    C = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    S3 = grp_rows(T) + grp_rows(C)
    assert nullity(U3) == 2                            # Schur: two covariant forms
    assert nullity(U3 + zero_diag_rows()) == 0         # the face-wise diagonal fixes the form
    assert nullity(S3) == 14
    assert nullity(S3 + zero_diag_rows()) == 9         # S3 alone leaves nine directions free
    gram = {idx(k, l, k, l): ONE for k in range(3) for l in range(3)}
    ident = {idx(k, k, m, m): ONE for k in range(3) for m in range(3)}
    facewise = {idx(k, k, k, k): ONE for k in range(3)}
    jminus = {idx(k, l, m, m): ONE for k in range(3) for l in range(3) if k != l for m in range(3)}
    for A in (gram, ident):
        assert tensor_ok(U3, A) and tensor_ok(S3, A)
    for A in (facewise, jminus):
        assert tensor_ok(S3, A) and not tensor_ok(U3, A)
    # 2 gram + c (J - 1)|beta|^2 at beta = e_1: the lower 2x2 block [[0, c], [c, 0]] has det -c^2 < 0
    for c in (F(1), F(-1, 3)):
        M = [[F(2), c, c], [c, F(0), c], [c, c, F(0)]]
        assert M[1][1] * M[2][2] - M[1][2] * M[2][1] < 0
    return True


def form_from(A, beta):
    return [[ca(*[cm(A.get(idx(k, l, m, n), Z0), cm(cc(beta[m]), beta[n]))
                  for m in range(3) for n in range(3)]) for l in range(3)] for k in range(3)]


def check_gram_square_on_configurations():
    premise("synthesis.many-twistor-join")
    premise("standard-model.internal-symmetry-ladder")
    gram2 = {idx(k, l, k, l): cr(2) for k in range(3) for l in range(3)}
    for Zs in CONFIGS:
        for lam in LAMS:
            B, beta, h = face_data(Zs, lam)
            M = form_from(gram2, beta)
            n2 = sum((ab2(b) for b in beta), F(0))
            # diagonal: each face's two-spinor bracket term 2|B^{ij}|^2
            assert all(M[k][k] == cr(2 * ab2(beta[k])) for k in range(3))
            # trace: the bracket part of the three-spinor join, 2 sum_{i<l} |B^{il}|^2
            assert ca(*[M[k][k] for k in range(3)]) == cr(2 * sum(ab2(B[i][l]) for i in range(3) for l in range(i + 1, 3)))
            assert M == dag(M)
            for a, b in itertools.combinations(range(3), 2):              # rank one
                for c, d in itertools.combinations(range(3), 2):
                    assert ca(cm(M[a][c], M[b][d]), cn(cm(M[a][d], M[b][c]))) == Z0
            vb = [cc(x) for x in beta]                                     # eigenvector conj(beta)
            assert [ca(*[cm(M[k][l], vb[l]) for l in range(3)]) for k in range(3)] == [cm(cr(2 * n2), x) for x in vb]
            for U in UNITARIES:
                d = det3(U); R = [[cm(d, x) for x in row] for row in dag(U)]
                _, beta2, _ = face_data(mix(Zs, U), lam)
                assert form_from(gram2, beta2) == mat(mat([[cc(x) for x in row] for row in R], M), tr_(R))
    return True


def casimir2(h, i, j):
    a, d, c = h[i][i][0], h[j][j][0], h[i][j]
    return (a - d) * (a - d) / 4 + ab2(c)


def rank_q(rows):
    Mx = [list(r) for r in rows]; rank = 0
    for c in range(len(Mx[0])):
        p = next((i for i in range(rank, len(Mx)) if Mx[i][c] != 0), None)
        if p is None: continue
        Mx[rank], Mx[p] = Mx[p], Mx[rank]
        Mx[rank] = [x / Mx[rank][c] for x in Mx[rank]]
        for i in range(len(Mx)):
            if i != rank and Mx[i][c] != 0:
                f = Mx[i][c]; Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[rank])]
        rank += 1
    return rank


def check_lambda_obstruction():
    premise("synthesis.many-twistor-join")
    premise("standard-model.internal-symmetry-ladder")
    rows = []
    for Zs in CONFIGS:
        for lam in LAMS[1:]:
            B, beta, h = face_data(Zs, lam)
            Lam3 = 2 * lam                                                  # Lambda/3 = 2 lam
            assert all(x[1] == 0 for x in (h[0][0], h[1][1], h[2][2]))
            hb = [[cc(x) for x in row] for row in h]
            for U in UNITARIES:                                               # conj(h) is covariant
                _, _, hU = face_data(mix(Zs, U), lam)
                assert [[cc(x) for x in row] for row in hU] == mat(mat(tr_(U), hb), [[cc(x) for x in row] for row in U])
            trh = sum((h[i][i][0] for i in range(3)), F(0))
            h2 = mat(h, h)
            trh2 = sum((h2[i][i][0] for i in range(3)), F(0))
            C3 = trh2 / 2 - trh * trh / 4
            Ck = [casimir2(h, (k + 1) % 3, (k + 2) % 3) for k in range(3)]
            assert sum(Ck, F(0)) - C3 == sum((h[i][i][0] ** 2 for i in range(3)), F(0)) / 4
            n2 = sum((ab2(b) for b in beta), F(0))
            for k in range(3):
                # unknowns a, b, al1..al4 of a conj(beta)beta^T + b|beta|^2 + al1 conj(h)^2 + al2 trh conj(h)
                # + al3 tr(h^2) + al4 (trh)^2 ; target 2|beta_k|^2 + (Lambda/3) C_k
                rows.append([ab2(beta[k]), n2, h2[k][k][0], trh * h[k][k][0], trh2, trh * trh,
                             2 * ab2(beta[k]) + Lam3 * Ck[k]])
    A = [r[:-1] for r in rows]
    assert rank_q(A) == 6 and rank_q(rows) == 7                             # inconsistent
    # at Lambda = 0 the same system is solved by a = 2 and nothing else
    rows0 = []
    for Zs in CONFIGS:
        B, beta, h = face_data(Zs, F(0))
        n2 = sum((ab2(b) for b in beta), F(0))
        trh = sum((h[i][i][0] for i in range(3)), F(0)); h2 = mat(h, h)
        trh2 = sum((h2[i][i][0] for i in range(3)), F(0))
        for k in range(3):
            rows0.append([ab2(beta[k]), n2, h2[k][k][0], trh * h[k][k][0], trh2, trh * trh, 2 * ab2(beta[k])])
    assert rank_q([r[:-1] for r in rows0]) == rank_q(rows0) == 6
    return True
