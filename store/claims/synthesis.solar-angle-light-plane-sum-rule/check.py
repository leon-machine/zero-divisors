"""synthesis.solar-angle-light-plane-sum-rule: exact checks (Fractions).

Face basis (unnormalised, orthogonal): u' = (1,1,1), b_e = (1,1,-2), b_o = (1,-1,0).
S2 is the exchange of the first two families, fixing the S3 -> S2 direction E = e3 e3^T.
"""
from fractions import Fraction as F
from tp_premise import premise
from GA import mat_mul


def mat(rows): return [[F(x) for x in r] for r in rows]
def mm(A, B): return mat_mul(A, B)                 # exact rational product (GA)
def tr(A): return [list(r) for r in zip(*A)]
def add(A, B): return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]
def sc(c, A): return [[c * a for a in r] for r in A]
def vAw(v, A, w): return sum(v[i] * A[i][j] * w[j] for i in range(3) for j in range(3))


I3 = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
J = mat([[1, 1, 1]] * 3)
Pi = add(I3, sc(F(-1, 3), J))
E = mat([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
P12 = mat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
UP, BE, BO = [F(1)] * 3, [F(1), F(1), F(-2)], [F(1), F(-1), F(0)]
SAMPLES = [mat([[1, 2, 3], [4, 5, 6], [7, 8, 10]]), mat([[F(1, 3), -2, 0], [5, F(-7, 4), 1], [2, 2, F(9, 5)]]),
           mat([[0, 1, -1], [3, 0, 2], [-4, F(1, 2), 1]])]


def s2_odd(Y):          # the S2-odd part of Y
    return sc(F(1, 2), add(Y, sc(F(-1), mm(P12, mm(Y, P12)))))


def check_compression_shape():
    """For A = E + X with X S2-odd: the compression of A to u'^perp has zero (odd,odd) entry and
    (even,even) entry 2/3 (normalised), and Pi A Pi A^T Pi = (Pi A Pi)(Pi A Pi)^T."""
    premise("neutrino.breaking-relation")
    premise("synthesis.theta23-at-s3-s2-direction")
    for Y in SAMPLES:
        for kind in ("any", "sym", "anti"):
            X = s2_odd(Y)
            if kind == "sym":
                X = sc(F(1, 2), add(X, tr(X)))
            if kind == "anti":
                X = sc(F(1, 2), add(X, sc(F(-1), tr(X))))
            assert mm(P12, mm(X, P12)) == sc(F(-1), X)
            A = add(E, X)
            assert vAw(BO, A, BO) == 0                              # (odd,odd) = 0
            assert vAw(BE, A, BE) / 6 == F(2, 3)                    # (even,even) = 2/3
            assert vAw(UP, X, UP) == 0 and vAw(UP, X, BE) == 0 and vAw(BE, X, UP) == 0
            # one-type: x = (even,odd), y = (odd,even) entries, normalised by |b_e||b_o| (common
            # factor sqrt12 dropped): symmetric X gives y = x, antisymmetric X gives y = -x
            x, y = vAw(BE, A, BO), vAw(BO, A, BE)
            if kind == "sym":
                assert y == x
            if kind == "anti":
                assert y == -x
            PAP = mm(Pi, mm(A, Pi))
            assert mm(Pi, mm(A, mm(Pi, mm(tr(A), Pi)))) == mm(PAP, tr(PAP))


def rot(c, s): return [[c, -s], [s, c]]


def half(tau):          # rational point of the circle from a half-angle tangent
    d = 1 + tau * tau
    return (1 - tau * tau) / d, 2 * tau / d


def check_svd_identity():
    """B = R(thL) diag(s1, s2) R(thR)^T has B_22 = 0 iff s2 = -s1 tan thL tan thR; then the heavy
    left/right singular vectors are (cos, sin) of thL, thR, and for y = +-x the tilts agree."""
    taus = [F(1, 3), F(-2, 5), F(1, 7), F(3, 4), F(-1, 9), F(5, 2)]
    for tl in taus:
        for trr in taus:
            cl, sl = half(tl)
            cr, sr = half(trr)
            s1 = F(7, 2)
            s2 = -s1 * (sl / cl) * (sr / cr)
            B = mm(rot(cl, sl), mm([[s1, F(0)], [F(0), s2]], tr(rot(cr, sr))))
            assert B[1][1] == 0
            BBt, BtB = mm(B, tr(B)), mm(tr(B), B)
            # heavy left vector (cl, sl) with eigenvalue s1^2, heavy right (cr, sr)
            assert [BBt[0][0] * cl + BBt[0][1] * sl, BBt[1][0] * cl + BBt[1][1] * sl] == [s1 * s1 * cl, s1 * s1 * sl]
            assert [BtB[0][0] * cr + BtB[0][1] * sr, BtB[1][0] * cr + BtB[1][1] * sr] == [s1 * s1 * cr, s1 * s1 * sr]
            # the tilt quadratics: k y t^2 + (k^2 + x^2 - y^2) t - k y = 0 at t = tan thL, and the
            # mirror one at tan thR (k = B00, x = B01, y = B10)
            k, x, y = B[0][0], B[0][1], B[1][0]
            tL, tR = sl / cl, sr / cr
            assert k * y * tL * tL + (k * k + x * x - y * y) * tL - k * y == 0
            assert k * x * tR * tR + (k * k + y * y - x * x) * tR - k * x == 0
            if y == x and k != 0:            # k = 0 is the degenerate s1 = |s2| case
                assert tL == tR
            # ratio of singular values is |tan thL tan thR|
            assert abs(s2 / s1) == abs(tL * tR)
            # the texture ratio, exactly: y/x = tL (1 + tR^2) / (tR (1 + tL^2))
            if x != 0:
                assert y / x == tL * (1 + tR * tR) / (tR * (1 + tL * tL))
    # one-type: for y = +-x the two quadratics have the same roots up to t -> -t
    for k, x in [(F(2, 3), F(1, 10)), (F(2, 3), F(-3, 7)), (F(1), F(5))]:
        for sgn in (1, -1):
            y = sgn * x
            qL = (k * y, k * k + x * x - y * y, -k * y)
            qR = (k * x, k * k + y * y - x * x, -k * x)
            assert qL == (qR if sgn == 1 else (-qR[0], qR[1], -qR[2]))


def check_bound_against_data():
    """One-type in both sectors: Delta <= arctan sqrt(m_e/m_mu) + arctan (m1/m2)^(1/4); under (H)
    cos^2 Delta > 0.865, against |U_e1|^2 <= 0.711 at the 3-sigma edges of the global fit.
    Every rational bound is bracketed on both sides at its last digit, so each number is pinned."""
    me, mmu = F(51099895, 10 ** 8), F(1056583755, 10 ** 7)       # PDG masses, MeV
    r = me / mmu
    a, b = F(6955, 10 ** 5), F(31623, 10 ** 5)
    step = F(1, 10 ** 5)
    assert (a - step) ** 2 < r <= a * a           # a: least 5-digit upper bound on sqrt(m_e/m_mu)
    assert (b - step) ** 4 < F(1, 100) <= b ** 4  # b: least 5-digit upper bound on 0.01^(1/4)
    T = (a + b) / (1 - a * b)                     # tan of the sum of the two arctans, an upper bound
    assert F(3944, 10000) < T < F(3945, 10000)    # below tan 21.6 deg = 0.3959
    cos2 = 1 / (1 + T * T)
    assert F(8653, 10000) < cos2 < F(8654, 10000)
    Ue1_max = (1 - F(275, 1000)) * (1 - F(203, 10000))   # (1 - s12^2_min)(1 - s13^2_min)
    assert Ue1_max == F(7102825, 10 ** 7)
    assert Ue1_max < F(711, 1000) < cos2
    # the lopsidedness the data then need on the neutrino side (charged side one-type):
    # cos^2 Delta <= 0.711 gives tan Delta >= T0 = 0.6375; tan thL_nu >= (T0 - a)/(1 + a T0), and
    # tan thL tan thR = (m1/m2)^(1/2) <= 1/10, so |tan thL / tan thR| >= 10 tan^2 thL >= 2.95
    edge = (1 - F(711, 1000)) / F(711, 1000)      # tan^2 Delta at cos^2 Delta = 0.711
    T0 = F(6375, 10000)
    assert T0 * T0 <= edge < (T0 + F(1, 10 ** 4)) ** 2
    tl = (T0 - a) / (1 + a * T0)
    assert F(2957, 1000) < 10 * tl * tl < F(2958, 1000)
    # in texture entries: |y/x| = (tL^2 + rho^2)/(rho (1 + tL^2)), rho = |tL tR| <= 1/10, increasing in
    # tL^2 and decreasing in rho (rho^2 < tL^2); at the corner tL^2 = 0.295, rho = 1/10 it is 2.355
    t2, rho = F(295, 1000), F(1, 10)
    assert tl * tl > t2 and rho * rho < t2
    corner = (t2 + rho * rho) / (rho * (1 + t2))
    assert F(2355, 1000) < corner < F(2356, 1000)
    # the first-order guide |y/x| ~ |tan thL/tan thR| would wrongly give 2.95 here: the two differ
    assert corner < 10 * t2


EXPORTS = {}
