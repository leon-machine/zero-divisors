"""Geometric modular conjugations on a generator: exact checks.

Conventions of the store: on one generator, affine parameter u, P = i d/du, a gauge-invariant
quasi-free state with symbol T = theta(P) (translation-invariant case), omega(psi*(v) psi(u)) = T(u, v);
the null vacuum has theta = chi(p < 0) and kernel (i/2 pi)(u - v + i0)^-1. The reflection about a cut a
is rho_a f(u) = f(2a - u); B(f) = psi(f) + psi*(f). For x supported in (0, inf) the natural-cone
form of the hypothesis is -i eta omega(B(x) B(rho_0 x)) = -2 eta r(x), r(x) = Im <x, T rho_0 x>, and in
momentum space r(x_a, x_b) = (1/2 pi) int_0^inf (1 - 2 theta(p)) kappa_p(a, b) dp for x_a = e^{-a u}.
Complex numbers are Gaussian rationals (GA.QI).

(1) kappa_p(a, b) = Im 1/((a - ip)(b - ip)) = p(a + b)/((a^2 + p^2)(b^2 + p^2)) is the double Laplace
    transform of sin(p(u + w)), and equals (g_p(a) - g_p(b))/(b - a) with g_p(a) = p/(a^2 + p^2): the
    Gram kernel of the form is a Loewner kernel (H(a) - H(b))/(a - b).
(2) The vacuum's form on x_m = u^m e^{-u} is (1/2 pi) m! n!/(m + n + 1) (Beta integral times (m + n)!),
    a positive matrix (exact signature); positivity of -2 eta r fixes eta = -1; the time-reversed state
    (theta = chi(p > 0)) has the negative matrix and needs eta = +1.
(3) The charge-symmetry condition theta(-p) = 1 - theta(p) (from J fixing Omega and acting as the
    charge-conjugating reflection): the vacuum, its reverse, the swapped-band state S = (-inf, -2) u (0, 2)
    and the translation-KMS states pass; the Fermi-level state chi(p < k), k != 0, fails. KMS symbols are
    not projections (excluded only by purity) and have 1 - 2 theta(p) >= 0 for p > 0.
(4) The swapped-band state: diagonal entries of the form on e^{-lambda u}, -1/lambda + 2 lambda/(lambda^2 + 4),
    are -3/5 at lambda = 1 and 3/20 at lambda = 4, so the form is indefinite for either eta (fails CGMA),
    while its kernel differs from the vacuum's by -(i/pi)(1 - cos 2s)/s, entire (Hadamard, locally normal).
(5) Two cuts do not suffice: a unimodular local gauge function g symmetric about the cuts 0 and 1 (period 2)
    keeps the hypothesis at both cuts, and the gauged vacuum kernel g(u) conj(g(v))/(u - v) is invariant under
    translation by 2 but not by 1/2.
Exact arithmetic only.
"""
from fractions import Fraction as F
import GA
from GA import QI
from tp_premise import premise


def _kappa(p, a, b):
    z = QI(1) / (QI(a, -p) * QI(b, -p))
    return z.im


def _g(p, a):
    return p / (a * a + p * p)


def _fact(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def _binom(n, k):
    return _fact(n) // (_fact(k) * _fact(n - k))


def _beta(m, n):
    # int_0^1 t^m (1 - t)^n dt by binomial expansion, exactly
    return sum(F((-1) ** k * _binom(n, k), m + k + 1) for k in range(n + 1))


def _vacuum_gram(size):
    # <x_m, (2 pi r) x_n> for the vacuum: int int u^m w^n e^{-(u+w)} / (u + w)
    #   = B(m+1, n+1) * int_0^inf s^{m+n} e^{-s} ds = B(m+1, n+1) (m+n)!
    return [[_beta(m, n) * _fact(m + n) for n in range(size)] for m in range(size)]


LOEWNER_SAMPLES = [(F(1, 3), F(2), F(5, 7)), (F(4), F(1, 2), F(3)), (F(2, 9), F(7, 4), F(11, 5))]
DIAG_LAMBDA = F(3, 2)
DIAG_P = (F(1, 5), F(2), F(9, 4))


def check_the_form_is_a_loewner_kernel():
    premise("synthesis.positive-null-energy-gives-r-premises")
    for p, a, b in LOEWNER_SAMPLES:
        k = _kappa(p, a, b)
        GA.check("kappa_p(a,b) = p(a+b)/((a^2+p^2)(b^2+p^2))",
                 k == p * (a + b) / ((a * a + p * p) * (b * b + p * p)))
        GA.check("kappa_p(a,b) = (g_p(a) - g_p(b))/(b - a)", k == (_g(p, a) - _g(p, b)) / (b - a))
        GA.check("kappa symmetric", k == _kappa(p, b, a))
    GA.check("kappa_1(1, 2) = 3/10", _kappa(F(1), F(1), F(2)) == F(3, 10))
    GA.check("kappa_2(3/2, 3/2) = 96/625", _kappa(F(2), F(3, 2), F(3, 2)) == F(96, 625))
    # diagonal: kappa_p(l, l) = 2 l p/(l^2 + p^2)^2, the p-derivative of -l/(l^2 + p^2)
    lam = DIAG_LAMBDA
    q = [lam * lam, F(0), F(1)]                # l^2 + p^2 as a polynomial in p
    dq = GA.pderiv(q)
    for p in DIAG_P:
        qv, dqv = GA.peval(q, p), GA.peval(dq, p)
        GA.check("d/dp(-l/q) = l q'/q^2 = kappa_p(l, l)", lam * dqv / (qv * qv) == _kappa(p, lam, lam))


def check_the_vacuum_form_is_positive_and_fixes_the_sign():
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state")
    G = _vacuum_gram(5)
    for m in range(5):
        for n in range(5):
            GA.check("Beta integral times (m+n)! = m! n!/(m+n+1)",
                     G[m][n] == F(_fact(m) * _fact(n), m + n + 1))
    GA.check("corner entries 1, 1/2, 4!4!/9 = 64", (G[0][0], G[0][1], G[4][4]) == (1, F(1, 2), 64))
    # the natural-cone form is -2 eta r with r = G/(2 pi): positive for eta = -1 only
    for eta, want in ((-1, (5, 0)), (1, (0, 5))):
        M = [[-eta * G[m][n] for n in range(5)] for m in range(5)]
        GA.check("vacuum: signature of -eta G", GA.congruence_signature(M)[:2] == want)
    # the time-reversed state chi(p > 0): 1 - 2 theta = -1 for p > 0, form -G, positive for eta = +1
    Mrev = [[-1 * (-G[m][n]) for n in range(5)] for m in range(5)]
    GA.check("reverse: positive for eta = +1", GA.congruence_signature(Mrev)[:2] == (5, 0))
    # Stieltjes form of the vacuum Gram: m! n! int_0^inf (1 + l)^{-(m+n+2)} dl = m! n!/(m+n+1)
    for m, n in ((0, 0), (1, 2), (3, 1)):
        GA.check("Laplace measure of 1/s is Lebesgue",
                 _fact(m) * _fact(n) * F(1, m + n + 1) == G[m][n])


def check_charge_symmetry_and_the_states_it_admits():
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("synthesis.imported-powers-stormer-takesaki-disjointness")
    vac = lambda p: 1 if p < 0 else 0
    rev = lambda p: 1 if p > 0 else 0
    band = lambda p: 1 if (p < -2 or 0 < p < 2) else 0
    ps = [F(1, 3), F(3, 2), F(5, 2), F(7)]
    for th, name in ((vac, "vacuum"), (rev, "reverse"), (band, "band")):
        for p in ps:
            GA.check(name + ": theta(-p) = 1 - theta(p)", th(-p) == 1 - th(p))
    GA.check("band: 1 - 2 theta changes sign on p > 0",
             (1 - 2 * band(F(1)), 1 - 2 * band(F(3))) == (-1, 1))
    # Fermi level k = 1: theta = chi(p < 1) fails at p = 1/2
    fermi = lambda p: 1 if p < 1 else 0
    GA.check("Fermi level fails charge symmetry", fermi(F(-1, 2)) + fermi(F(1, 2)) == 2)
    # translation-KMS symbol 1/(1 + x), x = e^{beta p} > 1 for p > 0, at rational x
    for x in (F(2), F(7, 3), F(10)):
        th_p, th_m = F(1) / (1 + x), F(1) / (1 + F(1) / x)
        GA.check("KMS: theta(-p) = 1 - theta(p)", th_p + th_m == 1)
        GA.check("KMS: 1 - 2 theta(p) = (x-1)/(x+1) >= 0", 1 - 2 * th_p == (x - 1) / (x + 1) and x > 1)
        GA.check("KMS: not a projection (only purity excludes it)", th_p * (1 - th_p) == x / (1 + x) ** 2)


def check_the_swapped_band_state_breaks_the_positivity():
    premise("synthesis.positive-null-energy-gives-r-premises")
    # w(p) = 1 - 2 theta(p) = -1 on (0, 2), +1 on (2, inf); antiderivative of kappa_p(l, l) is A(p) = -l/(l^2+p^2)
    def diag(lam):
        A = lambda p: -lam / (lam * lam + p * p)
        return -(A(2) - A(0)) + (0 - A(2))
    for lam in (F(1), F(4), F(3, 2)):
        GA.check("diag = -1/l + 2l/(l^2+4)", diag(lam) == F(-1) / lam + 2 * lam / (lam * lam + 4))
    GA.check("negative at e^{-u}", diag(F(1)) == F(-3, 5))
    GA.check("positive at e^{-4u}", diag(F(4)) == F(3, 20))
    GA.check("so indefinite for both signs of eta", diag(F(1)) * diag(F(4)) < 0)
    # the kernel difference from the vacuum is -(i/pi)(1 - cos 2s)/s; its series is entire:
    # (1 - cos 2s)/s = sum_{k>=1} (-1)^{k+1} 2^{2k} s^{2k-1}/(2k)!
    coeffs = [F((-1) ** (k + 1) * 2 ** (2 * k), _fact(2 * k)) for k in range(1, 5)]
    GA.check("series 2s - (2/3)s^3 + (4/45)s^5 - (2/315)s^7",
             coeffs == [F(2), F(-2, 3), F(4, 45), F(-2, 315)])
    # independent route: int_0^2 sin(p s) dp, expanded in s, integrating p^{2k+1} over [0, 2] exactly
    q_coeffs = []
    for k in range(4):
        prim = [F(0)] * (2 * k + 3)
        prim[2 * k + 2] = F(1, 2 * k + 2)                 # antiderivative of p^{2k+1}
        q_coeffs.append(F((-1) ** k, _fact(2 * k + 1)) * GA.peval(prim, F(2)))
    GA.check("int_0^2 sin(ps) dp has the same series as (1 - cos 2s)/s", q_coeffs == coeffs)


def check_two_cuts_do_not_give_stationarity():
    premise("synthesis.positive-null-energy-gives-r-premises")

    def tri(u):
        # distance from u to the nearest even integer: even about 0 and about 1, period 2
        r = u - 2 * (u // 2)
        return r if r <= 1 else 2 - r
    phase = QI(F(3, 5), F(4, 5))

    def g(u):
        return phase if tri(u) < F(1, 2) else QI(1)
    GA.check("g unimodular", phase * phase.conj() == 1)
    us = [F(k, 8) for k in range(-20, 21, 3)]
    for a in (0, 1):
        for u in us:
            GA.check("g symmetric about the cut", g(2 * a - u) == g(u))
    GA.check("not symmetric about the cut 1/4", any(g(F(1, 2) - u) != g(u) for u in us))

    def K(u, v):
        return g(u) * g(v).conj() / (u - v)
    u0, v0 = F(0), F(3, 4)
    GA.check("invariant under translation by 2", K(u0 + 2, v0 + 2) == K(u0, v0))
    GA.check("not under translation by 1/2", K(u0 + F(1, 2), v0 + F(1, 2)) != K(u0, v0))
    GA.check("the gauged values", (K(u0, v0), K(u0 + F(1, 2), v0 + F(1, 2))) == (QI(F(-4, 5), F(-16, 15)), QI(F(-4, 3))))
