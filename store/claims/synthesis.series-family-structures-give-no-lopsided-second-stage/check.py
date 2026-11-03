"""synthesis.series-family-structures-give-no-lopsided-second-stage: exact checks.

(1) Over Q: the P12-odd part of the span of the series' family structures 1, J, E = e3 e3^T, u' ^ s and
    the cyclic shift S (with S^T) is the single line of A = [u']_x = S - S^T; A spans the sign
    representation of S3, which occurs once in M_3; S + S^T = J - 1.
(2) Over Q(sqrt3)(i): the circulant C = 1 + (lam/2)(e^{i d} S + e^{-i d} S^T) = (1 - (lam/2)cos d) 1 +
    (lam/2) cos d J + i (lam/2) sin d A has the Fourier vectors f_k = (1, z^k, z^{2k}) as eigenvectors
    with eigenvalues 1 + lam cos(d - 2 pi k/3) (z = e^{2 pi i/3}), at cos d = 3/5, sin d = 4/5, two lam.
(3) Over Q(i): light-plane compression of P12-odd X in the unnormalised basis b_e = (1,1,-2),
    b_o = (1,-1,0): symmetric X gives y = x, antisymmetric y = -x, Hermitian y = conj(x); the series'
    line gamma A gives y = -x for complex gamma; a lopsided control (e3 a^T) gives |y| != |x|.
(4) Over Q: for B = [[k, x], [y, 0]] with |x|^2 = |y|^2 = r2, the polynomial s (k^2 + r2 - s)^2 - k^2 r2^2
    is divisible by the characteristic polynomial s^2 - (k^2 + 2 r2) s + r2^2 of B B^dag, so the light
    left vector has tan^2 = sigma2/sigma1; the eigenvector (k conj(y), s - k^2 - |x|^2) solves
    (B B^dag - s) u = 0 modulo that polynomial; and |1 + t_e t_nu w|^2 >= (1 - t_e t_nu)^2 for |w| = 1.
"""
from fractions import Fraction as F
from itertools import permutations
import GA
from tp_premise import premise

QI = GA.QI


def mm(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(3)), 0 * A[0][0]) for j in range(3)] for i in range(3)]


def tr(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def qm(M):
    return [[F(x) for x in row] for row in M]


I3 = qm([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
J3 = qm([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
E3 = qm([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
UP = [1, 1, 1]
SV = [1, 1, -2]
W3 = qm([[UP[i] * SV[j] - SV[i] * UP[j] for j in range(3)] for i in range(3)])
S3 = qm([[1 if i == (j + 1) % 3 else 0 for j in range(3)] for i in range(3)])
A3 = qm([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
P12 = qm([[0, 1, 0], [1, 0, 0], [0, 0, 1]])


def perm_matrix(p):
    return qm([[1 if p[j] == i else 0 for j in range(3)] for i in range(3)])


def sgn(p):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    return s


def check_odd_part_of_series_structures_is_the_sign_line():
    premise("neutrino.breaking-relation")
    premise("synthesis.residual-s2-fixes-120-family-form")
    ok = True
    gens = [I3, J3, E3, W3, S3, tr(S3)]

    def odd(X):
        PXP = mm(mm(P12, X), P12)
        return [[(X[i][j] - PXP[i][j]) / 2 for j in range(3)] for i in range(3)]
    odds = [sum(odd(X), []) for X in gens]
    ok = ok and GA.rank_of_vectors(odds) == 1
    # without the circulant shift the odd part of the span is zero
    ok = ok and all(x == 0 for v in odds[:4] for x in v)
    ok = ok and odd(S3) == [[x / 2 for x in row] for row in A3]
    # the even structures are even
    for X in (I3, J3, E3, W3):
        ok = ok and mm(mm(P12, X), P12) == X
    ok = ok and [[S3[i][j] - S3[j][i] for j in range(3)] for i in range(3)] == A3
    ok = ok and [[S3[i][j] + S3[j][i] for j in range(3)] for i in range(3)] == [[J3[i][j] - I3[i][j] for j in range(3)] for i in range(3)]
    # A is the cross product with u'
    for v in ([1, 0, 0], [0, 1, 0], [3, -2, 5]):
        cross = [UP[1] * v[2] - UP[2] * v[1], UP[2] * v[0] - UP[0] * v[2], UP[0] * v[1] - UP[1] * v[0]]
        ok = ok and [sum(A3[i][j] * v[j] for j in range(3)) for i in range(3)] == [F(x) for x in cross]
    # sign representation: P A P^T = sgn(P) A for all P, and it occurs once in M_3
    rows = []
    for p in permutations(range(3)):
        M = perm_matrix(p)
        ok = ok and mm(mm(M, A3), tr(M)) == [[sgn(p) * x for x in row] for row in A3]
        for i in range(3):
            for j in range(3):
                row = [F(0)] * 9
                for a in range(3):
                    for b in range(3):
                        row[3 * a + b] += M[i][a] * M[j][b]
                row[3 * i + j] -= sgn(p)
                rows.append(row)
    ok = ok and 9 - GA.rank_of_vectors(rows) == 1
    GA.check("odd part of span{1, J, E, u'^s, S, S^T} is the line of A = [u']_x, the sign representation (once in M_3)", ok)
    return ok


# Q(sqrt3)(i): pairs (a, b) = a + b sqrt3 with a, b in Q(i)
def kadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def kmul(x, y):
    return (x[0] * y[0] + x[1] * y[1] * 3, x[0] * y[1] + x[1] * y[0])


def keq(x, y):
    return all(x[t].re == y[t].re and x[t].im == y[t].im for t in range(2))


def kq(q):
    return (QI(q), QI(0))


ZETA = (QI(F(-1, 2), F(0)), QI(0, F(1, 2)))     # -1/2 + i sqrt3/2


def check_koide_circulant_puts_the_channel_phase_on_the_sign_line():
    premise("synthesis.coherent-face-vector-real-slices")
    ok = True
    cd, sd = F(3, 5), F(4, 5)
    for lam in (F(1), F(3, 2)):
        C = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                re = (1 - lam * cd / 2) * I3[i][j] + lam * cd / 2 * J3[i][j]
                im = lam * sd / 2 * A3[i][j]
                C[i][j] = (QI(re, im), QI(0))
        # same matrix as 1 + (lam/2)(e^{id} S + e^{-id} S^T)
        for i in range(3):
            for j in range(3):
                alt = I3[i][j] + lam / 2 * (QI(cd, sd) * S3[i][j] + QI(cd, -sd) * S3[j][i])
                ok = ok and keq(C[i][j], (alt, QI(0)))
        cos23, sin23 = F(-1, 2), F(1, 2)        # cos(2pi/3); sin(2pi/3) = sin23 * sqrt3
        for k in range(3):
            zk = kq(1)
            for _ in range(k):
                zk = kmul(zk, ZETA)
            f = [kq(1), zk, kmul(zk, zk)]
            # cos(d - 2pi k/3) = cd cos(2pi k/3) + sd sin(2pi k/3)
            ck = F(1) if k == 0 else cos23
            sk = 0 if k == 0 else (1 if k == 1 else -1)
            eig = (QI(1 + lam * cd * ck), QI(lam * sd * sin23 * sk))
            Cf = [kadd(kadd(kmul(C[i][0], f[0]), kmul(C[i][1], f[1])), kmul(C[i][2], f[2])) for i in range(3)]
            ok = ok and all(keq(Cf[i], kmul(eig, f[i])) for i in range(3))
    GA.check("circulant reading: C = (1 - (lam/2)cos d) 1 + (lam/2) cos d J + i (lam/2) sin d A, eigenvalues 1 + lam cos(d - 2 pi k/3)", ok)
    return ok


BE = [1, 1, -2]
BO = [1, -1, 0]


def compress(X):
    x = sum((QI(BE[i]) * X[i][j] * QI(BO[j]) for i in range(3) for j in range(3)), QI(0))
    y = sum((QI(BO[i]) * X[i][j] * QI(BE[j]) for i in range(3) for j in range(3)), QI(0))
    return x, y


def qieq(a, b):
    return a.re == b.re and a.im == b.im


def absq(z):
    return z.re * z.re + z.im * z.im


def check_light_plane_compression_is_one_type_in_modulus():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    ok = True
    s1, b1 = QI(2, -1), QI(F(1, 3), 5)
    Xs = [[s1, QI(0), b1], [QI(0), -s1, -b1], [b1, -b1, QI(0)]]                 # symmetric, P12-odd
    c1, e1 = QI(-1, 2), QI(F(3, 4), F(-1, 2))
    Xa = [[QI(0), c1, e1], [-c1, QI(0), -e1], [-e1, e1, QI(0)]]                 # antisymmetric, P12-odd
    Xh = [[QI(2), QI(0, 7), QI(1, 3)], [QI(0, -7), QI(-2), QI(-1, -3)], [QI(1, -3), QI(-1, 3), QI(0)]]   # Hermitian
    P = [[QI(P12[i][j]) for j in range(3)] for i in range(3)]
    for X in (Xs, Xa, Xh):
        PXP = mm(mm(P, X), P)
        ok = ok and all(qieq(PXP[i][j], -X[i][j]) for i in range(3) for j in range(3))
    x, y = compress(Xs)
    ok = ok and qieq(y, x) and not qieq(x, QI(0))
    x, y = compress(Xa)
    ok = ok and qieq(y, -x)
    x, y = compress(Xh)
    ok = ok and qieq(y, x.conj()) and not qieq(x, x.conj())
    for g in (QI(1), QI(0, 1), QI(F(3, 5), F(4, 5)), QI(-2, 7)):
        Xg = [[g * A3[i][j] for j in range(3)] for i in range(3)]
        x, y = compress(Xg)
        ok = ok and qieq(x, g * 6) and qieq(y, -(g * 6))
    # control: the lopsided product A E = a e3^T is P12-odd with |y| != |x|
    AE = mm(A3, E3)
    ok = ok and AE == qm([[0, 0, 1], [0, 0, -1], [0, 0, 0]])
    x, y = compress([[QI(v) for v in row] for row in AE])
    ok = ok and absq(x) != absq(y)
    GA.check("light-plane compression: symmetric y = x, antisymmetric y = -x, Hermitian y = conj x, gamma A one-type; A E lopsided", ok)
    return ok


def check_complex_one_type_light_angle_and_overlap():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    ok = True
    for k, r2 in ((F(2, 3), F(1, 100)), (F(2, 3), F(3, 7)), (F(2, 3), F(4, 9)), (F(1), F(5))):
        q = [r2 * r2, -(k * k + 2 * r2), F(1)]
        a = k * k + r2
        P = GA.padd(GA.pmul([F(0), F(1)], GA.pmul([a, F(-1)], [a, F(-1)])), [-(k * k * r2 * r2)])
        _, rem = GA.pdivmod(P, q)
        ok = ok and GA.ptrim(rem) == []
    # eigenvector of B B^dag for the light root, with complex x, y of equal modulus (|x|^2 = |y|^2 = 1)
    k = F(2, 3)
    for x, y in ((QI(F(3, 5), F(4, 5)), QI(0, 1)), (QI(1), QI(F(-5, 13), F(12, 13)))):
        ok = ok and absq(x) == absq(y)
        # B B^dag = [[k^2 + |x|^2, k conj(y)], [k y, |y|^2]]; u = (k conj(y), s - k^2 - |x|^2)
        # second component of (B B^dag - s) u, as a polynomial in s, is minus the characteristic polynomial
        t0 = (k * y * (k * y.conj())).re            # k^2 |y|^2 (real)
        lin_c = -(k * k + absq(x)) - absq(y)
        poly = GA.padd(GA.pmul([absq(y), F(-1)], [-(k * k + absq(x)), F(1)]), [t0])
        charp = [absq(x) * absq(y), -(k * k + absq(x) + absq(y)), F(1)]
        ok = ok and GA.ptrim(GA.padd(poly, charp)) == [] and lin_c == charp[1]
    # overlap: |1 + t_e t_nu w|^2 - (1 - t_e t_nu)^2 >= 0 for |w| = 1
    for te, tn in ((F(7, 100), F(1, 3)), (F(1, 2), F(2, 5))):
        for w in (QI(1), QI(F(3, 5), F(4, 5)), QI(-1), QI(0, 1)):
            z = QI(1) + w * (te * tn)
            ok = ok and absq(z) - (1 - te * tn) ** 2 >= 0
    GA.check("complex one-type light angle: tan^2 = sigma2/sigma1 depends on moduli only; overlap bound cos(theta_e + theta_nu)", ok)
    return ok
