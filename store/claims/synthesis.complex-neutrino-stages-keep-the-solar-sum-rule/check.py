"""synthesis.complex-neutrino-stages-keep-the-solar-sum-rule: exact checks.

(1) Over Q(i): for B = [[k, x], [y, 0]] with |x| = |y|, N = B B^T is carried to the symmetric block's
    N_s = [[k^2 + x^2, k x], [k x, x^2]] by D N D, D = diag(1, x/y) unitary, and D N N^dag D^dag =
    N_s N_s^dag, so the moduli of the Takagi vectors and the singular values agree.
(2) Over Q(i): for N_s, with s = |x|^2/k^2 and u = (Re x)^2/|x|^2,
    |a conj(b) + b conj(c)|^2 = k^8 s (1 + 4su + 4s^2 u), |a|^2 - |c|^2 = k^4 (1 + 2s(2u - 1)),
    tr N N^dag = k^4 (1 + 4su + 2s^2), |det N|^2 = k^8 s^4.
(3) Over Q: on the level set (1 + 4su + 2s^2)/s^2 = A + 2, f = tan^2(2 theta) equals
    4(A s^2 + A s - 1)/(A s - 2)^2, whose s-derivative has numerator -A s (A + 4); its value at u = 0,
    s = 1/y (A = y^2) is 4y/(y - 2)^2, decreasing for y > 2; with p = sqrt(m1/m2), y = (1 - p^2)/p
    and tan^2 theta = p(1 + p)/(1 - p); at p = 1/10: 3960/6241 and 11/90, attained at s = 10/99, u = 0.
(4) Over Q: under (H) cos^2 Delta > 0.8441 > 0.711 for every complex one-type neutrino stage.
(5) Over Q(i): 10 couplings on c and c* (with a P12-even 126) give y = x in each sector's
    compression; adding an antisymmetric 120 gives |y| != |x|.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

QI = GA.QI


def absq(z):
    return z.re * z.re + z.im * z.im


def m2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]


def t2(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def dag2(A):
    return [[A[j][i].conj() for j in range(2)] for i in range(2)]


def eq2(A, B):
    return all(A[i][j] == B[i][j] for i in range(2) for j in range(2))


SAMPLES = [
    (F(2, 3), QI(F(1, 5), F(2, 7)), QI(F(3, 5), F(4, 5))),
    (F(2, 3), QI(F(-1, 3), F(1, 4)), QI(0, 1)),
    (F(1), QI(F(3, 10), 0), QI(-1)),
    (F(5, 4), QI(F(1, 9), F(-2, 9)), QI(F(-5, 13), F(12, 13))),
]


def check_equal_modulus_stages_reduce_to_the_symmetric_block():
    premise("neutrino.breaking-relation")
    premise("synthesis.one-type-second-stages-are-twins")
    premise("synthesis.solar-angle-light-plane-sum-rule")
    premise("synthesis.series-family-structures-give-no-lopsided-second-stage")
    ok = True
    for k, x, w in SAMPLES:
        y = x * w                               # |w| = 1, so |y| = |x|
        ok = ok and absq(w) == 1 and absq(y) == absq(x)
        B = [[QI(k), x], [y, QI(0)]]
        N = m2(B, t2(B))
        Ns = [[QI(k * k) + x * x, x * k], [x * k, x * x]]
        d = x / y
        ok = ok and absq(d) == 1
        D = [[QI(1), QI(0)], [QI(0), d]]
        ok = ok and eq2(m2(m2(D, N), D), Ns)
        # the Takagi vectors of N are those of Ns up to the diagonal unitary D
        ok = ok and eq2(m2(m2(D, m2(N, dag2(N))), dag2(D)), m2(Ns, dag2(Ns)))
        # symmetric under transposition: B B^T is complex symmetric
        ok = ok and eq2(N, t2(N))
    GA.check("|x| = |y|: B B^T is D-conjugate to the symmetric block's, so Takagi moduli and masses agree", ok)
    return ok


def check_tilt_and_ratio_in_s_and_u():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    ok = True
    for k, x, _ in SAMPLES + [(F(2, 3), QI(F(1, 10), F(1, 10)), None), (F(3), QI(0, F(1, 2)), None)]:
        a = QI(k * k) + x * x
        b = x * k
        c = x * x
        q = a * b.conj() + b * c.conj()
        s = absq(x) / (k * k)
        u = x.re * x.re / absq(x)
        k4, k8 = k ** 4, k ** 8
        ok = ok and absq(q) == k8 * s * (1 + 4 * s * u + 4 * s * s * u)
        ok = ok and absq(a) - absq(c) == k4 * (1 + 2 * s * (2 * u - 1))
        ok = ok and absq(a) + 2 * absq(b) + absq(c) == k4 * (1 + 4 * s * u + 2 * s * s)
        ok = ok and absq(a * c - b * b) == k8 * s ** 4
        ok = ok and (1 + 2 * s * (2 * u - 1) > 0)
    GA.check("tan^2 2theta = 4s(1+4su+4s^2u)/(1+2s(2u-1))^2 and (s1^2+s2^2)/(s1 s2) = (1+4su+2s^2)/s^2", ok)
    return ok


def f_su(s, u):
    return 4 * s * (1 + 4 * s * u + 4 * s * s * u) / (1 + 2 * s * (2 * u - 1)) ** 2


def check_tilt_maximum_on_the_level_set():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    ok = True
    # (a) on the level set 4su = A s^2 - 1 the tilt is 4(A s^2 + A s - 1)/(A s - 2)^2
    for A in (F(9801, 100), F(400), F(50), F(7)):
        for s in (F(1, 9), F(1, 5), F(3, 7), F(2, 3)):
            u = (A * s * s - 1) / (4 * s)
            ok = ok and f_su(s, u) == 4 * (A * s * s + A * s - 1) / (A * s - 2) ** 2
            ok = ok and (1 + 4 * s * u + 2 * s * s) / (s * s) == A + 2
    # (b) its s-derivative numerator (2As + A)(As - 2) - 2A(As^2 + As - 1) = -A s (A + 4), as a
    # polynomial in s; coefficients have degree <= 2 in A, so four values of A prove it for all A
    for A in (F(1), F(2), F(-3), F(9801, 100)):
        lhs = GA.padd(GA.pmul([A, 2 * A], [F(-2), A]), GA.pmul([F(-2) * A], [F(-1), A, A]))
        ok = ok and GA.ptrim(GA.padd(lhs, [F(0), A * (A + 4)])) == []
    # (c) the u = 0 endpoint s = 1/y, A = y^2, gives 4y/(y - 2)^2; d/dy numerator -4(y - 2)(y + 2)
    for y in (F(99, 10), F(3), F(25, 2)):
        ok = ok and f_su(1 / y, F(0)) == 4 * y / (y - 2) ** 2
    lhs = GA.padd(GA.pmul([F(4)], GA.pmul([F(-2), F(1)], [F(-2), F(1)])),
                  GA.pmul([F(0), F(-8)], [F(-2), F(1)]))
    ok = ok and GA.ptrim(GA.padd(lhs, GA.pmul([F(4)], GA.pmul([F(-2), F(1)], [F(2), F(1)])))) == []
    # (d) closed form: p = sqrt(m1/m2), y = (1 - p^2)/p, tan^2 theta = p(1 + p)/(1 - p)
    for p in (F(1, 10), F(1, 20), F(1, 7)):
        y = (1 - p * p) / p
        t = p * (1 + p) / (1 - p)
        ok = ok and 4 * t / (1 - t) ** 2 == 4 * y / (y - 2) ** 2
    p = F(1, 10)
    y = (1 - p * p) / p
    ok = ok and y == F(99, 10) and 4 * y / (y - 2) ** 2 == F(3960, 6241)
    ok = ok and p * (1 + p) / (1 - p) == F(11, 90) and F(11, 90) > p   # above the real-coefficient sqrt(rho)
    # attained: s = 10/99, u = 0 has m1/m2 exactly 1/100 (rho + 1/rho = 100 + 1/100)
    s0 = F(10, 99)
    ok = ok and (1 + 2 * s0 * s0) / (s0 * s0) == 100 + F(1, 100) and f_su(s0, F(0)) == F(3960, 6241)
    # (e) sampled sweep: rational (s, u) with m1/m2 <= 1/100 have tan^2 2theta <= 3960/6241; the grid is
    # refined near the maximiser (s = 10/99, u = 0), which it contains, so the bound is attained on it
    R = 100 + F(1, 100)
    bound = F(3960, 6241)
    pts = [(F(i, 300), F(j, 10)) for i in range(1, 41) for j in range(0, 11)]
    pts += [(F(10, 99) - F(i, 10 ** 4), F(j, 10 ** 3)) for i in range(0, 21) for j in range(0, 21)]
    n_in, best = 0, F(0)
    for s, u in pts:
        if (1 + 4 * s * u + 2 * s * s) / (s * s) >= R:
            n_in += 1
            v = f_su(s, u)
            ok = ok and v <= bound
            best = max(best, v)
    ok = ok and n_in > 300 and best == bound
    # a step of 1e-4 inside the boundary along u = 0 lowers the tilt by between 9e-4 and 1e-3
    gap = bound - f_su(F(10, 99) - F(1, 10 ** 4), F(0))
    ok = ok and F(9, 10 ** 4) < gap < F(1, 10 ** 3)
    GA.check("max over phases of tan^2 2theta_nu at m1/m2 <= 1/100 is 3960/6241 (tan^2 theta = 11/90), at u = 0", ok)
    return ok


def check_bound_against_data_for_complex_neutrino_stages():
    premise("synthesis.solar-angle-light-plane-sum-rule")
    premise("synthesis.series-family-structures-give-no-lopsided-second-stage")
    ok = True
    me, mmu = F(51099895, 10 ** 8), F(1056583755, 10 ** 7)       # PDG masses, MeV (as the sum rule)
    r = me / mmu
    ok = ok and F(4836331692, 10 ** 12) < r < F(4836331693, 10 ** 12)
    a, c = F(6955, 10 ** 5), F(34961, 10 ** 5)
    step = F(1, 10 ** 5)
    ok = ok and (a - step) ** 2 < r <= a * a            # a: least 5-digit upper bound on sqrt(m_e/m_mu)
    ok = ok and (c - step) ** 2 < F(11, 90) <= c * c    # c: least 5-digit upper bound on sqrt(11/90)
    T = (a + c) / (1 - a * c)                           # tan(theta_e + theta_nu) upper bound
    ok = ok and F(4296060319, 10 ** 10) < T < F(4296060320, 10 ** 10)   # tan 23.25 deg
    cos2 = 1 / (1 + T * T)
    ok = ok and F(8441943561, 10 ** 10) < cos2 < F(8441943562, 10 ** 10)
    Ue1_max = (1 - F(275, 1000)) * (1 - F(2023, 100000))     # NuFIT 6.0 three-sigma union edges
    ok = ok and Ue1_max == F(71033325, 10 ** 8) and Ue1_max < F(711, 1000) < cos2
    # the overlap of two complex unit vectors at tilts te, tn is at least cos(theta_e + theta_nu):
    # |1 + w t|^2 - (1 - t)^2 = 2 t (1 + Re w) >= 0 for |w| = 1, t = te tn
    t = a * c
    for w in (QI(1), QI(F(3, 5), F(4, 5)), QI(-1), QI(F(-5, 13), F(-12, 13))):
        z = QI(1) + w * t
        ok = ok and absq(w) == 1 and absq(z) - (1 - t) ** 2 == 2 * t * (1 + w.re)
    GA.check("under (H): cos^2 Delta > 0.8441 > 0.711 for every complex one-type neutrino stage", ok)
    return ok


BE = [1, 1, -2]
BO = [1, -1, 0]
P12 = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]


def m3(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(3)), QI(0)) for j in range(3)] for i in range(3)]


def odd_compress(M):
    P = [[QI(v) for v in row] for row in P12]
    PMP = m3(m3(P, M), P)
    X = [[(M[i][j] - PMP[i][j]) * F(1, 2) for j in range(3)] for i in range(3)]
    x = sum((QI(BE[i]) * X[i][j] * QI(BO[j]) for i in range(3) for j in range(3)), QI(0))
    y = sum((QI(BO[i]) * X[i][j] * QI(BE[j]) for i in range(3) for j in range(3)), QI(0))
    return x, y


def sym3(e):
    return [[e[0], e[1], e[2]], [e[1], e[3], e[4]], [e[2], e[4], e[5]]]


def check_symmetric_couplings_give_one_type_stages():
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("standard-model.imported-clebsch-structure-seesaw")
    ok = True
    Y = sym3([QI(1, 2), QI(F(1, 3), -1), QI(0, F(1, 2)), QI(-2), QI(F(3, 4), F(1, 5)), QI(1, 1)])
    Yt = sym3([QI(0, 1), QI(2, F(-1, 7)), QI(-1, 3), QI(F(1, 2)), QI(0, -2), QI(F(5, 3))])
    f = sym3([QI(F(1, 4)), QI(0, 1), QI(1), QI(F(1, 4)), QI(1), QI(0)])      # P12-even: f11 = f22, f13 = f23
    al, be, wd, wu = QI(F(3, 5), F(4, 5)), QI(F(1, 7), 2), QI(-1, F(1, 3)), QI(F(2, 9), -1)
    # covariant completion plus the 126 with its lepton Clebsch -3 (charged leptons, Dirac neutrino)
    Me = [[be * Y[i][j] + al.conj() * Yt[i][j] - 3 * wd * f[i][j] for j in range(3)] for i in range(3)]
    MD = [[al * Y[i][j] + be.conj() * Yt[i][j] - 3 * wu * f[i][j] for j in range(3)] for i in range(3)]
    # a P12-even 126 coupling adds nothing to the odd stage (an odd f would also change M_R = v_R f)
    xf, yf = odd_compress(f)
    ok = ok and xf == 0 and yf == 0
    # each sector's odd stage compresses to y = x (values pinned for this sample)
    for M, pin in ((Me, QI(F(-296, 35), F(13, 5))), (MD, QI(F(-2836, 175), F(27, 175)))):
        x, y = odd_compress(M)
        ok = ok and x == y and x == pin
    # control: an antisymmetric 120 added in one sector makes |y| != |x|
    h = [[QI(0), QI(1, 1), QI(2)], [QI(-1, -1), QI(0), QI(0, 3)], [QI(-2), QI(0, -3), QI(0)]]
    MDh = [[MD[i][j] + QI(F(1, 2), 1) * h[i][j] for j in range(3)] for i in range(3)]
    x, y = odd_compress(MDh)
    ok = ok and absq(x) - absq(y) == F(-14616, 25)
    # the 120's own odd stage is antisymmetric: y = -x, so it shifts x and y oppositely
    xh, yh = odd_compress(h)
    ok = ok and yh == -xh and x == QI(F(-2836, 175), F(27, 175)) + QI(F(1, 2), 1) * xh
    GA.check("10s on c and c* (126 P12-even) give y = x in each sector; an added 120 gives |y| != |x|", ok)
    return ok
