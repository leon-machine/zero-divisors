"""standard-model.imported-frozen-point-dictionary: exact checks.

Cl(2,4) conventions: e0 (+1), e1..e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-; tractors
sigma ninf + mu + rho n0; Theta(A) = -ninf ^ A + n0 ^ P(A).
  (1) Frozen point: on an Einstein field (P = (Lambda/6) id) I = ninf + (Lambda/6) n0 is parallel with
      Q(I) = Lambda/3 = H^2 (null ninf at Lambda = 0). In the flat chart (hb = 1, Omega = 0, P = 0) the
      scale tractor V(x) = sigma ninf - (Lambda/6) x + (Lambda/6) n0, sigma = 1 - Lambda Q(x)/12, is parallel
      (central difference, exact on quadratics), Q(V) = Lambda/3, V(0) = I_Lambda; the null lifts
      X(x) = n0 + x - Q(x) ninf/2 give X.(ninf + l n0) = 1 - l Q(x)/2, which is sigma only for l = Lambda/6.
  (2) The dictionary as a differential identity in the de Sitter chart g = sigma^-2 eta: for a density f
      of weight w (flat representative, a polynomial in x) and the tractor D-operator
      Df = (w(2w+2) f, (2w+2) grad f, -box f) in the flat scale (n = 4),
      (box_g + m^2)(sigma^-w f) = -sigma^(1-w) (I.Df),  m^2 = -w(w+3) Lambda/3,
      exactly, for w = 0, -1, -2, -3 and two polynomials f: the coupling I.Df = 0 is the Klein-Gordon
      equation with that mass; a shifted mass breaks the identity.
  (3) The weight polynomial: -w(w+3) = Delta(3 - Delta) = 9/4 - (w + 3/2)^2; m^2 >= 0 exactly on
      [-3, 0] (grid), maximum 9/4 H^2 at w = -3/2, so m <= 3H/2; w = -3/2 +- i nu gives 9/4 + nu^2 (Gaussian
      rationals) with m/H = M on the exact rational points of M^2 - nu^2 = 9/4, m/H - nu = (9/4)/(m/H + nu),
      and nu = m/H - (9/8) H/m up to less than 2 (H/m)^3.
  (4) The number: N = M_P/H with H^2 = Lambda/3 = H_0^2 Omega_Lambda (PDG 2024 values, exact rationals):
      N^2 lies in [1.025^2, 1.035^2] 10^122, so N is 1.03e61, about 1.0e61, and Im w(M_P) differs from
      N by less than 10^-60.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
ETA = (1, -1, -1, -1)


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def theta(A, P):
    return GA.add(GA.neg(comm(NI, A)), comm(N0, P(A)))


def lift(x):
    X = vec(x)
    return GA.add(N0, X, GA.scal(-dot(X, X) / 2, NI))


# ---------------------------------------------------------------- polynomials in x0..x3
def padd(*ps):
    o = {}
    for p in ps:
        for k, v in p.items():
            o[k] = o.get(k, F(0)) + v
    return {k: v for k, v in o.items() if v != 0}


def pscal(c, p):
    return {k: F(c) * v for k, v in p.items()} if c else {}


def pmul(p, q):
    o = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            o[k] = o.get(k, F(0)) + v1 * v2
    return {k: v for k, v in o.items() if v != 0}


def pd(p, i):
    o = {}
    for k, v in p.items():
        if k[i]:
            kk = list(k)
            kk[i] -= 1
            o[tuple(kk)] = o.get(tuple(kk), F(0)) + v * k[i]
    return {k: v for k, v in o.items() if v != 0}


def box(p):
    return padd(*[pscal(ETA[i], pd(pd(p, i), i)) for i in range(4)])


def ip(p, q):
    return padd(*[pscal(ETA[i], pmul(pd(p, i), pd(q, i))) for i in range(4)])


def X_(i):
    k = [0] * 4
    k[i] = 1
    return {tuple(k): F(1)}


ONE = {(0, 0, 0, 0): F(1)}


def ppow(p, n):
    r = ONE
    for _ in range(n):
        r = pmul(r, p)
    return r


QX = padd(*[pscal(ETA[i], pmul(X_(i), X_(i))) for i in range(4)])
F1 = padd(pmul(X_(0), X_(1)), pscal(3, pmul(X_(2), pmul(X_(2), X_(3)))), pscal(F(1, 2), X_(1)), ONE,
          pmul(X_(0), pmul(X_(0), X_(0))))
F2 = padd(pscal(2, X_(3)), pmul(X_(1), X_(2)), pscal(-1, pmul(X_(0), pmul(X_(1), X_(1)))))
LAMS = (F(3, 5), F(-2, 7))
POINTS = ([1, 2, 0, -1], [F(1, 2), 0, 3, 1], [0, -2, 1, 4])
QS = (F(4), F(10), F(50))
DIRS = ([1, 0, 0, 0], [0, 1, 0, 0], [3, 1, -2, 5])
# PDG 2024 inputs
M_P = F("1.220890e19")            # GeV, G = M_P^-2
HBAR = F("6.582119569e-25")       # GeV s
H0 = F("67.4")                    # km/s/Mpc
MPC_KM = F("3.08567758149e19")    # km
OMEGA_L = F("0.685")


def check_frozen_point_and_flat_chart():
    premise("interior.scale-tractor-leaves-cone")
    premise("interior.covariant-form-vacuum-equations")
    premise("mass.de-sitter-scale-frozen-point")
    ok = dot(NI, NI) == 0
    for lam in LAMS:
        I = GA.add(NI, GA.scal(lam / 6, N0))
        pe = lambda A: GA.scal(lam / 6, A)
        ok = ok and all(GA.is_zero(comm(theta(vec(a), pe), I)) for a in DIRS) and dot(I, I) == lam / 3

        def V(x):
            X = vec(x)
            sig = 1 - lam * dot(X, X) / 12
            return GA.add(GA.scal(sig, NI), GA.scal(-lam / 6, X), GA.scal(lam / 6, N0))
        zero = lambda A: {}
        for x in POINTS:
            ok = ok and dot(V(x), V(x)) == lam / 3
            X = vec(x)
            sig = 1 - lam * dot(X, X) / 12
            ok = ok and dot(lift(x), I) == sig and dot(lift(x), lift(x)) == 0
            for a in DIRS:
                xp = [x[i] + a[i] for i in range(4)]
                xm = [x[i] - a[i] for i in range(4)]
                dV = GA.scal(F(1, 2), GA.sub(V(xp), V(xm)))
                ok = ok and GA.is_zero(GA.add(dV, comm(theta(vec(a), zero), V(x))))
        ok = ok and GA.eq(V([0, 0, 0, 0]), I)
    # uniqueness and the inverted chart, by hand at x = (1,2,0,-1): Q(x) = 1 - 4 - 1 = -4
    x = POINTS[0]
    for l in (F(1, 10), F(1, 3)):
        ok = ok and dot(lift(x), GA.add(NI, GA.scal(l, N0))) == 1 + 2 * l
        ok = ok and dot(lift(x), GA.add(N0, GA.scal(l, NI))) == l + 2
    ok = ok and (1 + 2 * F(1, 10) == 1 - F(3, 5) * (-4) / 12)       # l = Lambda/6 at Lambda = 3/5
    GA.check("frozen point: parallel, Q(I) = Lambda/3 = H^2, flat chart I_Lambda = ninf + (Lambda/6) n0", ok)
    assert ok


def check_dictionary_is_klein_gordon_in_de_sitter_chart():
    premise("mass.mass-weight-dictionary")
    premise("mass.de-sitter-scale-frozen-point")
    ok = True
    lam = F(3, 5)
    sig = padd(ONE, pscal(-lam / 12, QX))
    xgrad = lambda f: padd(*[pmul(X_(i), pd(f, i)) for i in range(4)])
    boxg = lambda u: padd(pmul(pmul(sig, sig), box(u)), pscal(-2, pmul(sig, ip(sig, u))))
    for w in (0, -1, -2, -3):
        m2 = -w * (w + 3) * lam / 3
        for f in (F1, F2):
            u = pmul(ppow(sig, -w), f)
            # I = (sigma, grad sigma, Lambda/6) = (sigma, -(Lambda/6) x, Lambda/6); Df as above
            IDf = padd(pscal(-1, pmul(sig, box(f))), pscal(lam / 6 * w * (2 * w + 2), f),
                       pscal(-(2 * w + 2) * lam / 6, xgrad(f)))
            lhs = padd(boxg(u), pscal(m2, u))
            ok = ok and lhs == pscal(-1, pmul(ppow(sig, 1 - w), IDf))
            if w == -1:
                ok = ok and padd(lhs, pscal(lam / 3, u)) != pscal(-1, pmul(ppow(sig, 1 - w), IDf))
    # by hand: w = -1 gives m^2 = 2 Lambda/3 = 2/5, the conformally coupled mass 2 H^2
    ok = ok and -(-1) * (-1 + 3) * lam / 3 == F(2, 5)
    GA.check("I.Df = 0 is (box_g + m^2) sigma^-w f = 0 with m^2 = -w(w+3) Lambda/3", ok)
    assert ok


def check_weight_polynomial_and_complex_weights():
    premise("mass.mass-weight-dictionary")
    premise("mass.weight-polynomial-two-series")
    ok = True
    poly = lambda w: -w * (w + 3)
    for k in range(-40, 41):
        w = F(k, 8)
        ok = ok and poly(w) == (-w) * (3 + w) == F(9, 4) - (w + F(3, 2)) ** 2
        ok = ok and ((poly(w) >= 0) == (-3 <= w <= 0)) and poly(w) <= F(9, 4)
    ok = ok and poly(F(-3, 2)) == F(9, 4) and poly(F(0)) == 0 and poly(F(-3)) == 0
    for q in QS:
        M, nu = (q + F(9, 4) / q) / 2, (q - F(9, 4) / q) / 2       # exact points of M^2 - nu^2 = 9/4
        for s in (1, -1):
            w = GA.qi(F(-3, 2), s * nu)
            ok = ok and -(w * (w + 3)) == GA.qi(M * M)             # m/H = M for w = -3/2 +- i nu
        ok = ok and M - nu == F(9, 4) / (M + nu)
        d = (M - F(9, 8) / M) - nu                                 # nu = m/H - (9/8) H/m + O(H^3/m^3)
        ok = ok and 0 < d < 2 / M ** 3
    GA.check("m^2/H^2 = -w(w+3) = Delta(3 - Delta): real weights in [-3,0], complex w = -3/2 +- i nu", ok)
    assert ok


def check_number_n_is_planck_over_hubble():
    premise("standard-model.imported-frozen-point-dictionary-external")
    H0_GeV = HBAR * H0 / MPC_KM                               # hbar H_0 in GeV
    H2 = H0_GeV ** 2 * OMEGA_L                                # H^2 = Lambda/3 = H_0^2 Omega_Lambda
    N2 = M_P ** 2 / H2
    ok = F(1025, 1000) ** 2 * 10 ** 122 <= N2 < F(1035, 1000) ** 2 * 10 ** 122     # N = 1.03e61
    ok = ok and F(95, 100) ** 2 * 10 ** 122 <= N2 < F(105, 100) ** 2 * 10 ** 122   # about 1.0e61
    ok = ok and N2 > (F(9, 4) * 10 ** 60) ** 2                # so N - nu < 9/(4N) < 10^-60
    # the measured Hubble rate itself: hbar H_0 is 1.44e-42 GeV
    ok = ok and F(1435, 1000) * F(1, 10 ** 42) < H0_GeV < F(1445, 1000) * F(1, 10 ** 42)
    GA.check("N = M_P/H is 1.03e61 (about 1.0e61) at the PDG 2024 values", ok)
    assert ok
