"""mass.imported-flat-model-twistor-chart-infinity: exact checks.

T11's twistor model of the flat ambient space: CS = C^4 (Gaussian rationals, GA.QI) with e1, e2 spanning the
omega-plane and e3, e4 the pi-plane; V_C = Lambda^2 CS (six coordinates on e_i ^ e_j, i < j) with pairing
<U, U'> = eps(U ^ U'), the coefficient of e1 e2 e3 e4; n_inf = e1 ^ e2, n0 = e3 ^ e4; the x-slot is spanned
by e_a ^ e_a' (a = 1, 2; a' = 3, 4), x = sum x^{aa'} e_a ^ e_a'.
(a) n0, n_inf are null with <n0, n_inf> = +1, the x-slot is orthogonal to both, Q(x) = -2 det x, and
    X(x) = n0 + x - (1/2) Q(x) n_inf is null at real and Gaussian samples; with c in place of -1/2,
    Q(X) = Q(x)(1 + 2c), so nullity for all x forces c = -1/2.
(b) Simplicity: for every sample bivector P, P is a wedge of two vectors (rank 2 as an antisymmetric
    matrix) iff <P, P> = 0 (null samples, including every X(x), and non-null controls of rank 4); the
    Pluecker bivector of the omega-plane is n_inf and that of the pi-plane is n0.
(c) The scale function of a constant vector is its sigma-slot: <X(x), n_inf + l n0> = 1 - l Q(x)/2 (for
    l = Lambda/6 the de Sitter scale 1 - Lambda Q/12), and <X(x), n0> = -Q(x)/2.
(d) A . (u ^ v) = Au ^ v + u ^ Av: for the 15 traceless matrix units and diagonals it preserves the pairing
    (<A.U, U'> + <U, A.U'> = 0 on all basis pairs), is a Lie homomorphism on sample pairs, and is injective
    on sl(4) (rank 15 = dim so(6)): an isomorphism onto so(Lambda^2 CS, eps).
(e) The infinity bivector of the scale n_inf + l n0 has norm 2 l, so it is simple iff l = 0 (Lambda = 0),
    where it is n_inf, the Pluecker bivector of the infinity line; constant vectors are parallel for the
    flat connection, so it is covariantly constant.
The identification of this Lambda^2 C^4 with Lambda^2 of the Fock model's conformal spinor space (and its
equivariance) is checked in correspondence.spinor-identification; here the model is T11's own.
"""
from fractions import Fraction as F
from itertools import combinations

import GA

QI = GA.QI
Z0, ONE = QI(0), QI(1)
PAIRS4 = list(combinations(range(4), 2))
XS = [(1, 0, 0, 0), (1, 2, -1, 3), (F(0), F(1, 2), F(1, 3), F(-2)), (QI(0, 1), 2, QI(1, 1), -1)]


def q(x):
    return x if isinstance(x, QI) else QI(x)


def wedge2(z1, z2):
    return [z1[i] * z2[j] - z1[j] * z2[i] for (i, j) in PAIRS4]


def psign(idx):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if idx[i] > idx[j]:
                s = -s
    return s


def pair(P, Qv):
    tot = Z0
    for a, (i, j) in enumerate(PAIRS4):
        for b, (k, l) in enumerate(PAIRS4):
            if len({i, j, k, l}) == 4:
                tot = tot + QI(psign((i, j, k, l))) * P[a] * Qv[b]
    return tot


def biv(i, j):
    return [ONE if p == (i, j) else Z0 for p in PAIRS4]


def vadd(*vs):
    return [sum((v[k] for v in vs), Z0) for k in range(len(vs[0]))]


def vscal(c, v):
    return [q(c) * a for a in v]


NINF, N0 = biv(0, 1), biv(2, 3)
XSLOT = [biv(0, 2), biv(0, 3), biv(1, 2), biv(1, 3)]


def xvec(co):
    return vadd(*[vscal(c, v) for c, v in zip(co, XSLOT)])


def Xpt(x, c=F(-1, 2)):
    return vadd(N0, x, vscal(q(c) * pair(x, x), NINF))


def asym(P):
    M = [[Z0] * 4 for _ in range(4)]
    for a, (i, j) in enumerate(PAIRS4):
        M[i][j], M[j][i] = P[a], -P[a]
    return M


def check_null_embedding_and_forced_coefficient():
    assert pair(N0, NINF) == ONE and pair(NINF, NINF) == Z0 and pair(N0, N0) == Z0
    for co in XS:
        x = xvec(co)
        co = [q(c) for c in co]
        assert pair(x, x) == QI(-2) * (co[0] * co[3] - co[1] * co[2])
        assert pair(x, N0) == Z0 and pair(x, NINF) == Z0
        Qx = pair(x, x)
        for c in (F(-1, 2), F(0), F(1, 2), F(3)):
            X = Xpt(x, c)
            assert pair(X, X) == Qx * q(1 + 2 * c)
        assert pair(Xpt(x), Xpt(x)) == Z0
    return True


def check_simple_iff_null_and_planes():
    nulls = [Xpt(xvec(co)) for co in XS] + [NINF, N0, wedge2([1, 2, 0, QI(0, 1)], [0, 1, 3, 1])]
    nonnull = [vadd(NINF, N0), vadd(biv(0, 2), biv(1, 3)), vadd(Xpt(xvec(XS[1])), vscal(2, N0))]
    for P in nulls:
        assert pair(P, P) == Z0 and GA.field_rank(asym(P)) == 2
    for P in nonnull:
        assert pair(P, P) != Z0 and GA.field_rank(asym(P)) == 4
    e = [[ONE if r == c else Z0 for r in range(4)] for c in range(4)]
    assert wedge2(e[0], e[1]) == NINF and wedge2(e[2], e[3]) == N0
    return True


# Sample values of l = Lambda/6 for the sigma-slot identity.
L_SCALE = (F(1, 2), F(-1), F(3), F(1, 7))
# Sample values of l for the simplicity test: the flat value 0 and three non-flat ones (no repeats).
L_INF = (F(0), F(1, 2), F(-1), F(1, 6))


def check_scale_function_is_sigma_slot():
    for co in XS:
        x = xvec(co)
        Qx = pair(x, x)
        for l in L_SCALE:
            I = vadd(NINF, vscal(l, N0))
            assert pair(Xpt(x), I) == ONE - q(l) * Qx / QI(2)
        assert pair(Xpt(x), N0) == -Qx / QI(2)
    return True


def act(A, P):
    out = [Z0] * 6
    for a, (i, j) in enumerate(PAIRS4):
        if P[a]:
            Ai = [A[r][i] for r in range(4)]
            Aj = [A[r][j] for r in range(4)]
            ei = [ONE if r == i else Z0 for r in range(4)]
            ej = [ONE if r == j else Z0 for r in range(4)]
            out = vadd(out, vscal(P[a], vadd(wedge2(Ai, ej), wedge2(ei, Aj))))
    return out


def mcomm(A, B):
    return [[sum((A[i][k] * B[k][j] - B[i][k] * A[k][j] for k in range(4)), Z0) for j in range(4)]
            for i in range(4)]


def check_sl_action_is_isomorphism_onto_so():
    gens = []
    for r in range(4):
        for c in range(4):
            if r != c:
                gens.append([[ONE if (i, j) == (r, c) else Z0 for j in range(4)] for i in range(4)])
    for k in range(3):
        gens.append([[(ONE if i == k else (QI(-1) if i == k + 1 else Z0)) if i == j else Z0 for j in range(4)]
                     for i in range(4)])
    assert len(gens) == 15
    basis = [biv(i, j) for (i, j) in PAIRS4]
    for A in gens:
        for U in basis:
            for U2 in basis:
                assert pair(act(A, U), U2) + pair(U, act(A, U2)) == Z0
    images = [[c for U in basis for c in act(A, U)] for A in gens]
    assert GA.field_rank(images) == 15
    for A in gens[::4]:
        for B in gens[1::5]:
            C = mcomm(A, B)
            for U in basis:
                assert act(C, U) == vadd(act(A, act(B, U)), vscal(-1, act(B, act(A, U))))
    # the identity acts by 2 (not traceless, not in so): the kernel of the action on gl(4) is zero
    I4 = [[ONE if i == j else Z0 for j in range(4)] for i in range(4)]
    assert all(act(I4, U) == vscal(2, U) for U in basis)
    return True


def check_infinity_bivector_simple_iff_flat():
    simple = []
    for l in L_INF:
        I = vadd(NINF, vscal(l, N0))
        assert pair(I, I) == q(2 * l)
        if GA.field_rank(asym(I)) == 2:
            simple.append(l)
    assert simple == [0]                    # of the samples, exactly the flat one (l = 0) is simple
    assert vadd(NINF, vscal(0, N0)) == wedge2([ONE, Z0, Z0, Z0], [Z0, ONE, Z0, Z0])
    return True
