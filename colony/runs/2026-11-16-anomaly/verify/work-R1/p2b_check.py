"""The phase of the quark mass determinant on the covariant completion: exact checks.

Family matrices are 3 x 3 with entries in span{1, I_4}, represented as Gaussian rationals (GA.QI; its unit stands
for I_4, and conj is I_4 -> -I_4). The stored completion: M_u = alpha Y + conj(beta) Yt, M_d = beta Y +
conj(alpha) Yt. Theta = det(M_u) det(M_d); H_q = M_q M_q^dagger; D = det[H_u, H_d].
(1) Off the balanced frame, |alpha| != |beta|, the map (Y, Yt) -> (M_u, M_d) is inverted by
    Y = (conj(alpha) M_u - conj(beta) M_d)/(|alpha|^2 - |beta|^2), Yt = (alpha M_d - beta M_u)/(|alpha|^2 - |beta|^2)
    and keeps symmetric pairs; turning M_u by a unit z keeps H_u, H_d and D and multiplies Theta by z^3. The
    hypercharge phase of the rung field leaves Theta, the common phase does not. On the balanced frame
    M_d = (beta/alpha) M_u and D = 0.
(2) Readings with a real Theta: real matrices (D = 0); the self-conjugate coupling Yt = conj(Y) in any frame
    (M_d = conj(M_u), Theta >= 0, D != 0, the two H have the same characteristic polynomial); Hermitian matrices
    in a real frame (Theta real, D != 0, different characteristic polynomials), which are real when symmetric.
(3) Stages: for X odd under the exchange of the first two families, with entries p, q, r, s,
    det(J + d (E + X)) = -3 d^2 x y + d^3 (q^2 - p^2), x y = (p - q - 2s)(p + q - 2r)/3 the product of the
    off-diagonal entries of the stored light-plane block; for a symmetric one-type stage X = t S it is
    -d^2 t^2 ((p - 2r)^2 + d p^2).
(4) One-type symmetric stages with real first stages: Theta = (c_u c_d)^3 (d_u d_d)^2 (t_u t_d)^2 R, R > 0. With
    the down coefficient real and the up coefficient at a quarter turn, Theta is real, of sign -sign(c_u c_d),
    with D != 0 and different spectra; the up matrix is fixed by conjugation composed with the family exchange and
    the down matrix by conjugation; at an eighth turn Theta is not real; a common conjugation of both gives D = 0.
"""
from fractions import Fraction as F

import GA
from GA import QI
from tp_premise import premise

UNIT = QI(0, 1)


def mat(rows):
    return [[QI(x) for x in r] for r in rows]


def mm(A, B):
    return [[sum((A[r][m] * B[m][c] for m in range(len(B))), QI(0)) for c in range(len(B[0]))] for r in range(len(A))]


def madd(A, B, s=1):
    return [[a + QI(s) * b for a, b in zip(r, t)] for r, t in zip(A, B)]


def msc(c, A):
    return [[QI(c) * a for a in r] for r in A]


def conj(A):
    return [[a.conj() for a in r] for r in A]


def tr(A):
    return [list(r) for r in zip(*A)]


def dag(A):
    return tr(conj(A))


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def herm_square(M):
    return mm(M, dag(M))


def big_d(Mu, Md):
    Hu, Hd = herm_square(Mu), herm_square(Md)
    return det3(madd(mm(Hu, Hd), mm(Hd, Hu), -1))


def charpoly(H):
    t1 = H[0][0] + H[1][1] + H[2][2]
    H2 = mm(H, H)
    t2 = H2[0][0] + H2[1][1] + H2[2][2]
    return (t1, (t1 * t1 - t2) / QI(2), det3(H))


def masses(al, be, Y, Yt):
    al, be = QI(al), QI(be)
    return madd(msc(al, Y), msc(be.conj(), Yt)), madd(msc(be, Y), msc(al.conj(), Yt))


def theta(Mu, Md):
    return det3(Mu) * det3(Md)


def is_real(z):
    return QI(z).im == 0


Y_S = mat([[QI(1, 2), QI(0, 1), 2], [QI(0, 1), 3, QI(1, -1)], [2, QI(1, -1), QI(5, 1)]])
YT_S = mat([[2, QI(1, 1), QI(0, 3)], [QI(1, 1), QI(-1, 2), 1], [QI(0, 3), 1, QI(4, -1)]])
JJ = mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
EE = mat([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
P12 = mat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])


def odd_stage(p, q, r, s):
    """The general matrix X with P12 X P12 = -X."""
    return mat([[p, q, r], [-QI(q), -QI(p), -QI(r)], [s, -QI(s), 0]])


def stage_matrix(c, d, X):
    return msc(c, madd(JJ, msc(d, madd(EE, X))))


def check_completion_is_a_bijection_off_the_balanced_frame():
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.imported-left-right-bidoublet-two-yukawa-couplings")
    ok = True
    for al, be in ((QI(F(1, 3)), QI(-3)), (QI(2, 1), QI(-1, 3))):
        Mu, Md = masses(al, be, Y_S, YT_S)
        m2 = al * al.conj() - be * be.conj()
        ok = ok and m2 != 0
        Yrec = msc(1 / m2, madd(msc(al.conj(), Mu), msc(be.conj(), Md), -1))
        Ytrec = msc(1 / m2, madd(msc(al, Md), msc(be, Mu), -1))
        ok = ok and Yrec == Y_S and Ytrec == YT_S
        # turn M_u by the unit z = (3 + 4 I_4)/5 and pull back
        z = QI(F(3, 5), F(4, 5))
        ok = ok and z * z.conj() == 1
        Yz = msc(1 / m2, madd(msc(al.conj(), msc(z, Mu)), msc(be.conj(), Md), -1))
        Ytz = msc(1 / m2, madd(msc(al, Md), msc(be, msc(z, Mu)), -1))
        Mu2, Md2 = masses(al, be, Yz, Ytz)
        ok = ok and Yz == tr(Yz) and Ytz == tr(Ytz) and Mu2 == msc(z, Mu) and Md2 == Md
        ok = ok and herm_square(Mu2) == herm_square(Mu) and big_d(Mu2, Md2) == big_d(Mu, Md)
        ok = ok and big_d(Mu, Md) != 0 and theta(Mu2, Md2) == z * z * z * theta(Mu, Md)
        ok = ok and z * z * z == QI(F(-117, 125), F(44, 125))
        # hypercharge phase and common phase of the rung field
        ok = ok and theta(*masses(z * al, z.conj() * be, Y_S, YT_S)) == theta(Mu, Md)
        ok = ok and theta(*masses(z * al, z * be, Y_S, YT_S)) != theta(Mu, Md)
    # balanced frame |alpha| = |beta|: 3^2 + 4^2 = 5^2
    al, be = QI(3, 4), QI(0, 5)
    Mu, Md = masses(al, be, Y_S, YT_S)
    ok = ok and al * al.conj() == be * be.conj() and Md == msc(be / al, Mu) and big_d(Mu, Md) == 0
    ok = ok and theta(Mu, Md) == (be / al) * (be / al) * (be / al) * det3(Mu) * det3(Mu)
    GA.check("completion: (Y, Yt) -> (M_u, M_d) invertible off the balanced frame; unit turn of M_u moves only det", ok)
    return ok


def check_readings_with_a_real_determinant():
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog")
    premise("synthesis.imported-jarlskog-commutator-identity")
    al, be = QI(F(1, 3)), QI(-3)
    # (a) real matrices, real frame: real determinant of either sign, D = 0
    Yr, Ytr = mat([[1, 2, 0], [2, -3, 1], [0, 1, 5]]), mat([[2, 1, 3], [1, 0, -1], [3, -1, 4]])
    Mu, Md = masses(al, be, Yr, Ytr)
    ok = is_real(theta(Mu, Md)) and big_d(Mu, Md) == 0 and theta(Mu, Md) == QI(F(5936125, 27))
    Mu, Md = masses(al, be, Yr, msc(-1, Ytr))
    ok = ok and is_real(theta(Mu, Md)) and theta(Mu, Md).re < 0
    # (b) self-conjugate coupling, complex frame
    Mu, Md = masses(QI(2, 1), QI(-1, 3), Y_S, conj(Y_S))
    ok = ok and Md == conj(Mu) and theta(Mu, Md) == QI(546500) and big_d(Mu, Md) == QI(0, 10909000000)
    ok = ok and charpoly(herm_square(Mu)) == charpoly(herm_square(Md))
    # (c) Hermitian matrices, real frame
    Yh = mat([[1, QI(2, 1), QI(0, -1)], [QI(2, -1), 3, QI(1, 1)], [QI(0, 1), QI(1, -1), -2]])
    Yth = mat([[2, QI(0, 3), 1], [QI(0, -3), 1, QI(2, -1)], [1, QI(2, 1), 5]])
    Mu, Md = masses(al, be, Yh, Yth)
    ok = ok and Yh == dag(Yh) and Mu == dag(Mu) and Md == dag(Md) and is_real(theta(Mu, Md))
    ok = ok and big_d(Mu, Md) != 0 and big_d(Mu, Md).re == 0
    ok = ok and charpoly(herm_square(Mu)) != charpoly(herm_square(Md))
    ok = ok and not is_real(theta(*masses(QI(2, 1), QI(-1, 3), Yh, Yth)))
    # Hermitian and symmetric is real: the Hermitian sample is not symmetric, its symmetric part is real
    sym = madd(Yh, tr(Yh))
    ok = ok and Yh != tr(Yh) and sym == conj(sym)
    GA.check("real determinant: real (D = 0); self-conjugate (equal spectra); Hermitian with a real frame", ok)
    return ok


def check_stage_determinant_formula():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    premise("synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase")
    ok = True
    samples = [(QI(2), QI(-1), QI(3), QI(5), QI(F(1, 7))), (QI(1, 2), QI(0, 1), QI(-2, 1), QI(3, -1), QI(F(2, 5))),
               (QI(0, 3), QI(4), QI(1, 1), QI(-2), QI(F(1, 3), 1))]
    for p, q, r, s, d in samples:
        X = odd_stage(p, q, r, s)
        ok = ok and mm(mm(P12, X), P12) == msc(-1, X)
        xy = (p - q - 2 * s) * (p + q - 2 * r) / 3
        # the light-plane block in the basis (1, 1, -2)/sqrt 6, (1, -1, 0)/sqrt 2: product of off-diagonal entries
        be_, bo_ = [QI(1), QI(1), QI(-2)], [QI(1), QI(-1), QI(0)]
        form = lambda u, w: sum((u[a] * X[a][b] * w[b] for a in range(3) for b in range(3)), QI(0))
        ok = ok and form(be_, bo_) * form(bo_, be_) / 12 == xy and form(be_, be_) == 0 and form(bo_, bo_) == 0
        ok = ok and sum((be_[a] * EE[a][b] * be_[b] for a in range(3) for b in range(3)), QI(0)) / 6 == QI(F(2, 3))
        lhs = det3(madd(JJ, msc(d, madd(EE, X))))
        ok = ok and lhs == -3 * d * d * xy + d * d * d * (q * q - p * p)
    # symmetric one-type stage X = t S, S real symmetric with entries p, r
    for p, r, t, d in ((QI(2), QI(-1), QI(1, 1), QI(F(1, 5))), (QI(3), QI(5), QI(0, 2), QI(F(2, 3)))):
        X = msc(t, odd_stage(p, 0, r, r))
        ok = ok and X == tr(X)
        ok = ok and det3(madd(JJ, msc(d, madd(EE, X)))) == -d * d * t * t * ((p - 2 * r) * (p - 2 * r) + d * p * p)
    GA.check("stages: det(J + d(E + X)) = -3 d^2 x y + d^3 (q^2 - p^2); one-type symmetric: -d^2 t^2 (positive)", ok)
    return ok


S_UP, S_DOWN = odd_stage(2, 0, -1, -1), odd_stage(1, 0, 3, 3)
D_UP, D_DOWN = F(-5), F(1, 3)
C_UP, C_DOWN = 7, 2
T_QUARTER, T_REAL, T_EIGHTH, T_EIGHTH_BAR = QI(0, 2), QI(3), QI(1, 1), QI(3, -3)
GENERIC = ((QI(1, 2), QI(3, -1)), (QI(-2, 5), QI(1, 4)))


def stage_pair(cu, cd, tu, td):
    return stage_matrix(cu, D_UP, msc(tu, S_UP)), stage_matrix(cd, D_DOWN, msc(td, S_DOWN))


def check_quarter_turn_stage_gives_a_real_determinant():
    premise("synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase")
    premise("synthesis.flag-conjugate-antilinear-on-one-chirality-and-conjugation-reverses-jarlskog")
    premise("synthesis.one-type-second-stages-are-twins")
    # down coefficient real, up coefficient a quarter turn: pinned values of the two determinants and of D
    Mu, Md = stage_pair(C_UP, C_DOWN, T_QUARTER, T_REAL)
    ok = Mu == tr(Mu) and Md == tr(Md)
    ok = ok and det3(Mu) == QI(F(115248, 125)) and det3(Md) == QI(F(-608, 3))
    ok = ok and theta(Mu, Md) == QI(F(-23356928, 125))
    ok = ok and big_d(Mu, Md) == QI(0, F(-149375920805085184, 1265625))
    ok = ok and charpoly(herm_square(Mu)) != charpoly(herm_square(Md))
    ok = ok and mm(mm(P12, conj(Mu)), P12) == Mu and conj(Md) == Md and mm(mm(P12, conj(Md)), P12) != Md
    # the Hermitian twin: M_u P12 is Hermitian, of opposite determinant
    tw = mm(Mu, P12)
    ok = ok and tw == dag(tw) and det3(tw) + det3(Mu) == 0
    # opposite sign of c_u c_d: the determinant is the opposite real number
    ok = ok and theta(*stage_pair(C_UP, -C_DOWN, T_QUARTER, T_REAL)) == QI(F(23356928, 125))
    # an eighth turn against a real coefficient: a quarter-turn determinant; opposite eighth turns: positive
    ok = ok and theta(*stage_pair(C_UP, C_DOWN, T_EIGHTH, T_REAL)) == QI(0, F(11678464, 125))
    ok = ok and theta(*stage_pair(C_UP, C_DOWN, T_EIGHTH, T_EIGHTH_BAR)) == QI(F(23356928, 125))
    ok = ok and big_d(*stage_pair(C_UP, C_DOWN, T_EIGHTH, T_EIGHTH_BAR)) != 0
    # general law: Theta / (t_u t_d)^2 is real, with the sign of c_u c_d
    for tu, td in GENERIC:
        ratio = theta(*stage_pair(C_UP, C_DOWN, tu, td)) / (tu * tu * td * td)
        ok = ok and is_real(ratio) and ratio.re > 0
        ratio = theta(*stage_pair(-C_UP, C_DOWN, tu, td)) / (tu * tu * td * td)
        ok = ok and is_real(ratio) and ratio.re < 0
    # a common conjugation of both sectors (both coefficients real, or both quarter turns) gives D = 0
    ok = ok and big_d(*stage_pair(C_UP, C_DOWN, T_REAL, T_REAL)) == 0
    ok = ok and big_d(*stage_pair(C_UP, C_DOWN, T_QUARTER, UNIT * T_REAL)) == 0
    # cos(2 phi) = 2 cos^2 phi - 1 equals -1/2 at cos^2 phi = 1/4 and -1 at the quarter turn
    ok = ok and 2 * F(1, 4) - 1 == F(-1, 2) and 2 * F(0, 4) - 1 == -1
    GA.check("quarter turn in one sector, real vacuum: det real with D != 0 and different spectra; sign -sign(c_u c_d)", ok)
    return ok
