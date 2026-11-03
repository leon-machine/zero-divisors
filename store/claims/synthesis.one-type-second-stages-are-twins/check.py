"""synthesis.one-type-second-stages-are-twins: exact checks (Fractions).

Textures of the breaking lemma at the S3 -> S2 direction E = e3 e3^T: a sector matrix
M(X) = J + delta (E + X) with X real and odd under the exchange P12 of the first two families, and the
S3-invariant Majorana matrix M_R = alpha Pi + M3 J/3.  The twin of X is X P12.
"""
from fractions import Fraction as F
from tp_premise import premise
from GA import mat_mul, mat_rank


def mat(rows):
    return [[F(x) for x in r] for r in rows]


def T(A):
    return [list(r) for r in zip(*A)]


def add(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


def sc(c, A):
    return [[c * a for a in r] for r in A]


I3 = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
J = mat([[1, 1, 1]] * 3)
Pi = add(I3, sc(F(-1, 3), J))
E = mat([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
P12 = mat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])


def Xsym(s, b):
    return mat([[s, 0, b], [0, -s, -b], [b, -b, 0]])


def Xanti(c, e):
    return mat([[0, c, e], [-c, 0, -e], [-e, e, 0]])


def sector(delta, X):
    return add(J, sc(delta, add(E, X)))


def light(delta, X, alpha, M3):
    """m_nu = m_D M_R^{-1} m_D^T at d = 1, with M_R^{-1} = Pi/alpha + (J/3)/M3, since Pi and J/3
    are complementary projectors."""
    MRinv = add(sc(1 / alpha, Pi), sc(1 / (3 * M3), J))
    mD = sector(delta, X)
    return mat_mul(mat_mul(mD, MRinv), T(mD))


SAMPLES = [(F(1, 3), F(-2, 7)), (F(-5, 4), F(1, 9)), (F(2), F(3, 2)), (F(0), F(1, 5))]
DELTAS = [F(-286, 1000), F(286, 1000), F(-1), F(7, 3)]
SEESAW = [(F(1), F(5307, 10)), (F(1), F(66)), (F(3, 2), F(-17, 5))]


def check_twin_map():
    """X -> X P12 maps the P12-odd symmetric matrices bijectively onto the P12-odd antisymmetric
    ones (both two-dimensional), and in the basis (odd line | even plane) it keeps the (odd, even)
    entries x and reverses the (even, odd) entries y."""
    premise("synthesis.solar-angle-light-plane-sum-rule")
    o = [F(1), F(-1), F(0)]
    evens = ([F(1), F(1), F(0)], [F(0), F(0), F(1)])
    vAw = lambda v, A, w: sum(v[i] * A[i][j] * w[j] for i in range(3) for j in range(3))
    imgs = []
    for s, b in SAMPLES:
        X = Xsym(s, b)
        assert mat_mul(P12, mat_mul(X, P12)) == sc(F(-1), X) and T(X) == X
        Y = mat_mul(X, P12)
        assert mat_mul(P12, mat_mul(Y, P12)) == sc(F(-1), Y) and T(Y) == sc(F(-1), Y)
        for e in evens:
            assert vAw(o, Y, e) == vAw(o, X, e)          # x kept
            assert vAw(e, Y, o) == -vAw(e, X, o)         # y reversed
        imgs.append([Y[0][1], Y[0][2]])
    # the image spans the two-dimensional antisymmetric P12-odd space (parameters c = Y01, e = Y02)
    assert mat_rank(imgs) == 2
    # explicit: Xsym(s, b) P12 = Xanti(s, b) and Xanti(c, e) P12 = Xsym(c, e)
    for s, b in SAMPLES:
        assert mat_mul(Xsym(s, b), P12) == Xanti(s, b)
        assert mat_mul(Xanti(s, b), P12) == Xsym(s, b)


def check_observables_invariant():
    """For every delta, every P12-odd X and every S3-invariant M_R: M(X P12) = M(X) P12, so
    M M^T is unchanged (charged-lepton masses and left states), and the light neutrino matrix
    m_D M_R^{-1} m_D^T is unchanged exactly (P12 commutes with M_R): every lepton mass and the whole
    PMNS matrix are the same for X and its twin, at all orders."""
    premise("neutrino.breaking-relation")
    premise("synthesis.theta23-at-s3-s2-direction")
    for d in DELTAS:
        for s, b in SAMPLES:
            for c, e in SAMPLES:
                X = add(Xsym(s, b), Xanti(c, e))
                Xt = mat_mul(X, P12)
                assert sector(d, Xt) == mat_mul(sector(d, X), P12)
                M, Mt = sector(d, X), sector(d, Xt)
                assert mat_mul(Mt, T(Mt)) == mat_mul(M, T(M))
                for alpha, M3 in SEESAW:
                    assert light(d, Xt, alpha, M3) == light(d, X, alpha, M3)
    # M_R commutes with P12, and the twin of a mixed stage exchanges its two parts' types
    for alpha, M3 in SEESAW:
        MR = add(sc(alpha, Pi), sc(M3 / 3, J))
        assert mat_mul(P12, MR) == mat_mul(MR, P12)
    X = add(Xsym(F(1), F(2)), Xanti(F(3), F(-1)))
    Xt = mat_mul(X, P12)
    assert Xt == add(Xanti(F(1), F(2)), Xsym(F(3), F(-1)))
    # a nonzero stage is never its own twin
    assert Xt != X


EXPORTS = {}
