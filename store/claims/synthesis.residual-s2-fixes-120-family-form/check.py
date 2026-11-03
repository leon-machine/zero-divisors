"""synthesis.residual-s2-fixes-120-family-form: exact checks.

Family matrices are 3 x 3 over the rationals (and Q(i) for the Clebsch part). S_3 acts by
X -> P X P^T on the democratic basis e_1, e_2, e_3; u' = (1,1,1), s = (1,1,-2), a = (1,-1,0).
The breaking direction is e_3 e_3^T (the store's S_3 -> S_2 reference direction); its stabiliser
S_2 is the swap of e_1 and e_2.
"""
import GA
from GA import QI, qi, field_kernel
from tp_premise import premise
from fractions import Fraction as F
from itertools import permutations

N3 = range(3)
ZERO = qi(0)


def perm_mat(p):
    return [[F(1) if p[i] == j else F(0) for j in N3] for i in N3]


def conj(P, X):
    return [[sum((P[i][k] * X[k][l] * P[j][l] for k in N3 for l in N3), X[0][0] * 0)
             for j in N3] for i in N3]


def outer(x, y):
    return [[x[i] * y[j] for j in N3] for i in N3]


def wedge(x, y):
    return [[x[i] * y[j] - y[i] * x[j] for j in N3] for i in N3]


def lin(A, B, a, b):
    return [[a * A[i][j] + b * B[i][j] for j in N3] for i in N3]


def mv(A, x):
    return [sum((A[i][j] * x[j] for j in N3), A[0][0] * 0) for i in N3]


def basis_antisym():
    out = []
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        X = [[F(0)] * 3 for _ in N3]
        X[i][j], X[j][i] = F(1), F(-1)
        out.append(X)
    return out


def basis_sym():
    out = []
    for i in N3:
        for j in N3:
            if i <= j:
                X = [[F(0)] * 3 for _ in N3]
                X[i][j] = X[j][i] = F(1)
                out.append(X)
    return out


def invariant_dim(basis, group):
    """Dimension of the span of basis matrices fixed by every P in group (exact kernel)."""
    rows = []
    for P in group:
        for (i, j) in [(i, j) for i in N3 for j in N3]:
            rows.append([conj(P, X)[i][j] - X[i][j] for X in basis])
    return len(field_kernel(rows))


S3 = [perm_mat(p) for p in permutations(N3)]
S2 = [perm_mat((0, 1, 2)), perm_mat((1, 0, 2))]
UP, SV, AV = [F(1)] * 3, [F(1), F(1), F(-2)], [F(1), F(-1), F(0)]
E3 = [F(0), F(0), F(1)]


def mat(rows):
    return [[x if isinstance(x, QI) else qi(x) for x in r] for r in rows]


def qmat(A):
    return [[qi(x) for x in r] for r in A]


def madd(*Ms):
    return [[sum((M[i][j] for M in Ms), ZERO) for j in N3] for i in N3]


def msc(c, A):
    return [[c * A[i][j] for j in N3] for i in N3]


def tr(A):
    return [[A[j][i] for j in N3] for i in N3]


def sym(A):
    return msc(qi(F(1, 2)), madd(A, tr(A)))


TEN = mat([[qi(2, 1), qi(-1), qi(3, -2)], [qi(-1), qi(5), qi(0, 1)], [qi(3, -2), qi(0, 1), qi(-4, 3)]])
H120 = qmat(wedge(UP, SV))
VEV = dict(v_d=qi(1, -1), w_d=qi(-1, F(1, 3)), c_d=qi(0, 4), c_e=qi(5, -1), v_R=qi(11))


def check_residual_s2_fixes_120_family_form():
    premise("standard-model.imported-spinor-bilinears")
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("neutrino.invariant-symmetric-matrices")
    premise("neutrino.breaking-relation")
    # the breaking direction e3 e3^T is fixed by S2 and by no other element of S3
    D3 = outer(E3, E3)
    assert [conj(P, D3) == D3 for P in S3].count(True) == 2
    # (i) no S3-invariant antisymmetric matrix; (ii) S2-invariant antisymmetric ones form a line
    assert invariant_dim(basis_antisym(), S3) == 0
    assert invariant_dim(basis_antisym(), S2) == 1
    hS2 = wedge([F(1), F(1), F(0)], E3)                    # (e1 + e2) ^ e3
    assert all(conj(P, hS2) == hS2 for P in S2)
    assert wedge(UP, SV) == lin(hS2, hS2, F(-3), F(0))     # = -3 (e1+e2)^e3: heavy with S2-even
    assert mv(hS2, AV) == [F(0)] * 3                       # the S2-odd light state decouples
    assert mv(hS2, UP) != [F(0)] * 3 and mv(hS2, SV) != [F(0)] * 3
    # any breaking along e3 e3^T leaves a = (1,-1,0) massless and mixes s with u': a is the
    # first family at this stage, s the second, u' the third
    for eps in (F(1, 7), F(-2, 3)):
        Mb = lin(outer(UP, UP), D3, F(1), eps)
        assert mv(Mb, AV) == [F(0)] * 3
        assert mv(Mb, SV) != [F(0)] * 3
    # symmetric invariants: S3 gives the two-dimensional span of Pi and J, S2 four dimensions
    assert invariant_dim(basis_sym(), S3) == 2 and invariant_dim(basis_sym(), S2) == 4
    for X in (outer(UP, UP), outer(SV, SV), outer(AV, AV), lin(outer(UP, SV), outer(SV, UP), F(1), F(1))):
        assert all(conj(P, X) == X for P in S2)
    # (iii) the 126 under an S3-invariant Majorana matrix alpha Pi + M3 J/3, through M_R = v_R f
    alpha, M3 = qi(F(1, 500)), qi(1)
    J = qmat(outer(UP, UP))
    PI = madd(qmat([[F(1) if i == j else F(0) for j in N3] for i in N3]), msc(qi(F(-1, 3)), J))
    v_R, w_d = VEV["v_R"], VEV["w_d"]
    f = msc(qi(1) / v_R, madd(msc(alpha, PI), msc(M3 * qi(F(1, 3)), J)))
    Md = madd(msc(VEV["v_d"], TEN), msc(w_d, f), msc(VEV["c_d"], H120))
    Me = madd(msc(VEV["v_d"], TEN), msc(w_d * qi(-3), f), msc(VEV["c_e"], H120))
    Dsym = sym(madd(Md, msc(qi(-1), Me)))
    assert Dsym == msc(w_d * qi(4), f)                     # the 10 and the 120 drop out
    assert all(conj(qmat(P), Dsym) == Dsym for P in S3)
    light = w_d * qi(4) * alpha / v_R
    for y in (AV, SV):
        assert mv(Dsym, [qi(t) for t in y]) == [light * qi(t) for t in y]
    assert mv(Dsym, [qi(1)] * 3) == [w_d * qi(4) * M3 / v_R] * 3
    # a 126 entry on the S2-even light state alone is not S3-invariant, so not of this form
    Ess = qmat(outer(SV, SV))
    assert any(conj(qmat(P), Ess) != Ess for P in S3)
    return True
