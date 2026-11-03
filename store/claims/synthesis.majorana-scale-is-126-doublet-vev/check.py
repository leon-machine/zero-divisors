"""synthesis.majorana-matrix-is-126-difference: exact checks.

Complex rational 3 x 3 matrices (GA.QI). Two 10 couplings Y1, Y2 (symmetric), one 126
coupling f (symmetric), one 120 coupling h (antisymmetric), all vevs complex rationals.
The Dirac matrices are those of the imported Clebsch structure:
M_u = sum v_u^a Y_a + w_u f + c_u h,   M_nu = sum v_u^a Y_a - 3 w_u f + c_nu h,
M_d = sum v_d^a Y_a + w_d f + c_d h,   M_e  = sum v_d^a Y_a - 3 w_d f + c_e h,   M_R = v_R f.
"""
import GA
from GA import QI, qi
from tp_premise import premise
from fractions import Fraction as F

N3 = range(3)
ZERO = qi(0)


def mat(rows):
    return [[x if isinstance(x, QI) else qi(x) for x in r] for r in rows]


def madd(*Ms):
    return [[sum((M[i][j] for M in Ms), ZERO) for j in N3] for i in N3]


def msc(c, A):
    c = c if isinstance(c, QI) else qi(c)
    return [[c * A[i][j] for j in N3] for i in N3]


def tr(A):
    return [[A[j][i] for j in N3] for i in N3]


def sym(A):
    return msc(F(1, 2), madd(A, tr(A)))


def asym(A):
    return msc(F(1, 2), madd(A, msc(-1, tr(A))))


def mv(A, x):
    return [sum((A[i][j] * x[j] for j in N3), ZERO) for i in N3]


def quad(A, x, y):
    return sum((x[i] * mv(A, y)[i] for i in N3), ZERO)


def clebsch(Y, f, h, v_u, v_d, w_u, w_d, c):
    ten_u = madd(*[msc(v_u[a], Y[a]) for a in range(len(Y))])
    ten_d = madd(*[msc(v_d[a], Y[a]) for a in range(len(Y))])
    Mu = madd(ten_u, msc(w_u, f), msc(c[0], h))
    Mn = madd(ten_u, msc(w_u * qi(-3), f), msc(c[1], h))
    Md = madd(ten_d, msc(w_d, f), msc(c[2], h))
    Me = madd(ten_d, msc(w_d * qi(-3), f), msc(c[3], h))
    return Mu, Mn, Md, Me


UP = [qi(1)] * 3


def _data():
    Y1 = mat([[qi(2, 1), qi(-1), qi(3, -2)], [qi(-1), qi(5), qi(0, 1)], [qi(3, -2), qi(0, 1), qi(-4, 3)]])
    Y2 = mat([[qi(1), qi(2, 2), qi(-1)], [qi(2, 2), qi(-3, 1), qi(7)], [qi(-1), qi(7), qi(1, -1)]])
    f = mat([[qi(3), qi(1, -1), qi(2)], [qi(1, -1), qi(-2, 5), qi(-1, 1)], [qi(2), qi(-1, 1), qi(6, 1)]])
    h = mat([[0, qi(1, 2), qi(-3)], [qi(-1, -2), 0, qi(2, -1)], [qi(3), qi(-2, 1), 0]])
    assert sym(Y1) == Y1 and sym(Y2) == Y2 and sym(f) == f and asym(h) == h
    v_u, v_d = [qi(3, 1), qi(-2)], [qi(1, -1), qi(5, 2)]
    w_u, w_d = qi(F(2, 7), 1), qi(-1, F(1, 3))
    c = [qi(1), qi(-2, 3), qi(0, 4), qi(5, -1)]
    v_R = qi(11, 0)
    return Y1, Y2, f, h, v_u, v_d, w_u, w_d, c, v_R


DATA = _data()
M_T = qi(91)


def check_majorana_matrix_is_126_difference():
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("standard-model.imported-spinor-bilinears")
    Y1, Y2, f, h, v_u, v_d, w_u, w_d, c, v_R = DATA
    Mu, Mn, Md, Me = clebsch([Y1, Y2], f, h, v_u, v_d, w_u, w_d, c)
    M_R = msc(v_R, f)
    # (i) the symmetric parts of the two differences are 4 w f; the 10s and the 120 drop out
    assert sym(madd(Mu, msc(-1, Mn))) == msc(w_u * qi(4), f)
    assert sym(madd(Md, msc(-1, Me))) == msc(w_d * qi(4), f)
    assert asym(madd(Md, msc(-1, Me))) == msc(c[2] - c[3], h)
    assert msc(v_R / (w_d * qi(4)), sym(madd(Md, msc(-1, Me)))) == M_R
    assert msc(v_R / (w_u * qi(4)), sym(madd(Mu, msc(-1, Mn)))) == M_R
    # kill-condition control: a symmetric 120 coupling would enter the symmetric part
    hs = sym(mat([[1, 2, 0], [0, 1, 3], [1, 0, 2]]))
    _, _, Md2, Me2 = clebsch([Y1, Y2], f, hs, v_u, v_d, w_u, w_d, c)
    assert sym(madd(Md2, msc(-1, Me2))) != msc(w_d * qi(4), f)
    # (ii) Premise (EW) along a heavy direction x: x^T M_nu x = 0 and x^T M_u x = m_t x.x give
    premise("standard-model.premise-ew-equal-weight")
    # x^T M_R x = v_R m_t x.x / (4 w_u). Impose it by solving for the 33-type freedom in Y1.
    x = UP
    xx = sum((a * a for a in x), ZERO)
    m_t = M_T
    # choose the 10 vev v_u^1 so that x^T M_nu x = 0, then rescale w_u so that x^T M_u x = m_t x.x
    base = madd(msc(v_u[1], Y2), msc(w_u * qi(-3), f), msc(c[1], h))
    v1 = -quad(base, x, x) / quad(Y1, x, x)
    vu = [v1, v_u[1]]
    Mu, Mn, Md, Me = clebsch([Y1, Y2], f, h, vu, v_d, w_u, w_d, c)
    assert quad(Mn, x, x) == ZERO
    scale = m_t * xx / quad(Mu, x, x)          # the overall normalisation of the up sector
    Mu_s, Mn_s = msc(scale, Mu), msc(scale, Mn)
    w_us = w_u * scale
    assert quad(Mn_s, x, x) == ZERO and quad(Mu_s, x, x) == m_t * xx
    assert quad(M_R, x, x) == v_R * m_t * xx / (w_us * qi(4))
    return True
