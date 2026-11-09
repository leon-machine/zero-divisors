"""synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content: exact checks.

The light-ray central charge c of a content is the number of complex fermion arrays plus real boson arrays on a
generator; the one-window test is 24 | c (the window evolution exp(2 pi I_4 c/24) P equal to the grading P), the
two-window test 12 | c (the evolution over two windows equal to 1).
(1) Scalar null data, in Cl(1,3) with k = g0 + g3, m = g0 - g3: for polynomial fields the divergence of
    omega = f1 grad f2 - f2 grad f1 is f1 box f2 - f2 box f1 identically, so a symmetric potential term cancels;
    the flux through N_k is k.omega = f1 (k.grad) f2 - f2 (k.grad) f1, with no transverse derivative and no
    potential; box = (k.grad)(m.grad) - d1^2 - d2^2.
(2) The count c = 16 n_g + 2 n_V + n_s + 2 eps, and the gauge vectors of the twelve-dimensional algebra drop out.
(3) The verdict on generations: one-window iff eps = 0 and n_h = 2 n_g (mod 6); two-window iff eps = 0 and
    n_g + n_h = 0 (mod 3); complete over one period of (n_g mod 3, n_h mod 6, eps).
(4) Fifteen components per generation; the general count f per generation.
(5) Boson-fermion balance b = 2 f gives c = 48 n_g; the Sakharov content N_S = 72 at three generations.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = GA.sig(1, 3)                     # g0^2 = 1, g1^2 = g2^2 = g3^2 = -1
ETA = (1, -1, -1, -1)
PERIOD_G = range(3)                   # c mod 24 depends on n_g mod 3 (16 * 3 = 48)
PERIOD_H = range(6)                   # and on n_h mod 6 (4 * 6 = 24)
WIDE = range(40)
FERMION_TEST_RANGE = range(1, 97)
PER_GEN_RANGE = range(1, 49)


# ---------------------------------------------------------------- polynomial fields in (t, x, y, z)
def padd(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def pscale(a, p):
    return {e: a * c for e, c in p.items() if a * c != 0}


def pmul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            out[e] = out.get(e, F(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def pd(p, mu):
    out = {}
    for e, c in p.items():
        if e[mu] > 0:
            ne = tuple(x - (1 if i == mu else 0) for i, x in enumerate(e))
            out[ne] = out.get(ne, F(0)) + c * e[mu]
    return {e: c for e, c in out.items() if c != 0}


def box(p):
    return padd(*[pscale(F(ETA[mu]), pd(pd(p, mu), mu)) for mu in range(len(ETA))])


def mono(c, t, x, y, z):
    return {(t, x, y, z): F(c)}


PHI1 = padd(mono(3, 2, 1, 0, 0), mono(1, 0, 0, 1, 1), mono(-5, 0, 0, 0, 3), mono(1, 1, 0, 0, 0), mono(2, 1, 1, 1, 0))
PHI2 = padd(mono(1, 1, 1, 1, 0), mono(2, 0, 0, 0, 2), mono(-1, 3, 0, 0, 0), mono(7, 0, 1, 0, 0), mono(1, 0, 0, 2, 1))
WPOT = padd(mono(1, 0, 0, 0, 0), mono(2, 1, 1, 0, 0), mono(-1, 0, 0, 0, 2))     # V'' along a background


def vec(*cs):
    return GA.add(*[GA.scal(c, GA.gen(i)) for i, c in enumerate(cs)])


def components(v):
    """contravariant components v^mu of a vector v = v^mu g_mu"""
    return [v.get((mu,), F(0)) for mu in range(len(ETA))]


def directional(v, p):
    return padd(*[pscale(c, pd(p, mu)) for mu, c in enumerate(components(v))])


def current(f1, f2):
    """omega^mu = eta^{mu mu}(f1 d_mu f2 - f2 d_mu f1): omega = f1 grad f2 - f2 grad f1"""
    return [pscale(F(ETA[mu]), padd(pmul(f1, pd(f2, mu)), pscale(F(-1), pmul(f2, pd(f1, mu)))))
            for mu in range(len(ETA))]


def check_scalar_null_data_carries_no_potential():
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    k, m = vec(1, 0, 0, 1), vec(1, 0, 0, -1)
    GA.check("k is null", GA.mul(k, k, SQ) == {})
    GA.check("m is null", GA.mul(m, m, SQ) == {})
    GA.check("<k, m> = 2", GA.dot(k, m, SQ) == 2)
    om = current(PHI1, PHI2)
    div = padd(*[pd(om[mu], mu) for mu in range(len(ETA))])
    rhs = padd(pmul(PHI1, box(PHI2)), pscale(F(-1), pmul(PHI2, box(PHI1))))
    GA.check("div omega = f1 box f2 - f2 box f1 identically", div == rhs)
    # on linearised solutions box f = -W f (W = V'' symmetric): the divergence is f1(-W f2) - f2(-W f1) = 0
    lin = padd(pmul(PHI1, pscale(F(-1), pmul(WPOT, PHI2))), pscale(F(-1), pmul(PHI2, pscale(F(-1), pmul(WPOT, PHI1)))))
    GA.check("the potential term cancels from the divergence", lin == {})
    # flux through N_k: k . omega with omega = omega^mu g_mu, k . g_mu from the algebra
    kdot = [GA.dot(vec(1, 0, 0, 0), GA.gen(mu), SQ) for mu in range(len(ETA))]
    flux = padd(*[pscale(kdot[mu], om[mu]) for mu in range(len(ETA))])
    want = padd(pmul(PHI1, directional(k, PHI2)), pscale(F(-1), pmul(PHI2, directional(k, PHI1))))
    GA.check("flux k.omega = f1 (k.grad) f2 - f2 (k.grad) f1", flux == want)
    # no transverse derivative and no potential enter: k.grad = d_t + d_z
    GA.check("k.grad = d_t + d_z", directional(k, PHI2) == padd(pd(PHI2, 0), pd(PHI2, 3)))
    GA.check("m.grad = d_t - d_z", directional(m, PHI2) == padd(pd(PHI2, 0), pscale(F(-1), pd(PHI2, 3))))
    for p in (PHI1, PHI2, pmul(PHI1, PHI2)):
        fact = padd(directional(k, directional(m, p)), pscale(F(-1), pd(pd(p, 1), 1)), pscale(F(-1), pd(pd(p, 2), 2)))
        GA.check("box = (k.grad)(m.grad) - d_1^2 - d_2^2", fact == box(p))
    # control: through a constant-time surface (normal g0) the flux f1 d_t f2 - f2 d_t f1 differs
    e0 = vec(1, 0, 0, 0)
    t_flux = padd(pmul(PHI1, directional(e0, PHI2)), pscale(F(-1), pmul(PHI2, directional(e0, PHI1))))
    GA.check("control: the timelike flux differs from the null flux", t_flux != flux)
    return True


# ---------------------------------------------------------------- the light-ray central charge of a content
def charge(n_g, n_V, n_s, eps, per_gen=16):
    return per_gen * n_g + 2 * n_V + n_s + 2 * eps


def one_window(c):
    return F(c, 24).denominator == 1


def two_window(c):
    return F(c, 12).denominator == 1


def check_content_count_and_gauge_vectors_drop_out():
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    premise("standard-model.connection-forced")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    GA.check("the recorded content: c = 78 at three generations, one doublet, a graviton", charge(3, 12, 4, 1) == 78)
    GA.check("spin-1/2 content alone at three generations: 48", charge(3, 0, 0, 0) == 48)
    GA.check("with the vectors: 72", charge(3, 12, 0, 0) == 72)
    GA.check("with the linear rung field's eight components: 80", charge(3, 12, 8, 0) == 80)
    GA.check("the twelve vectors carry 24", charge(0, 12, 0, 0) == 24)
    GA.check("the twelve vectors pass both tests", one_window(24) and two_window(24))
    for d in WIDE:
        GA.check("a d-dimensional gauge algebra drops out of the one-window test iff 12 | d",
                 one_window(charge(0, d, 0, 0)) == (d % 12 == 0))
        GA.check("and out of the two-window test iff 6 | d", two_window(charge(0, d, 0, 0)) == (d % 6 == 0))
    GA.check("contrast: 45 vectors (so(10)) give 90, which fails", not two_window(charge(0, 45, 0, 0)))
    # the window phase as a rotor where it is a quarter turn: I4 = g0123, exp(2 pi I4 c/24) = I4^(c/6)
    I4 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), SQ), GA.mul(GA.gen(2), GA.gen(3), SQ), SQ)
    GA.check("I4^2 = -1", GA.mul(I4, I4, SQ) == GA.sc(-1))
    GA.check("the vectors' one-window phase I4^4 = 1", GA.mul(GA.mul(I4, I4, SQ), GA.mul(I4, I4, SQ), SQ) == GA.sc(1))
    return True


def check_verdict_on_generations():
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")
    premise("standard-model.connection-forced")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    # complete over one period: c mod 24 depends on (n_g mod 3, n_h mod 6, eps)
    for n_g, n_h, eps in product(PERIOD_G, PERIOD_H, (0, 1)):
        for lift_g, lift_h in ((0, 0), (3, 6), (6, 12)):
            c = charge(n_g + lift_g, 12, 4 * (n_h + lift_h), eps)
            GA.check("one-window iff eps = 0 and n_h = 2 n_g mod 6",
                     one_window(c) == (eps == 0 and (n_h - 2 * n_g) % 6 == 0))
            GA.check("two-window iff eps = 0 and n_g + n_h = 0 mod 3",
                     two_window(c) == (eps == 0 and (n_g + n_h) % 3 == 0))
    for n_g, n_h in product(WIDE, WIDE):
        c = charge(n_g, 12, 4 * n_h, 0)
        GA.check("one-window rule on a wide range", one_window(c) == ((n_h - 2 * n_g) % 6 == 0))
        GA.check("a graviton fails both tests: c = 2 mod 4", (c + 2) % 4 == 2 and not two_window(c + 2))
    passes = lambda test, n_h: [g for g in range(1, 10) if test(charge(g, 12, 4 * n_h, 0))]
    GA.check("no scalars: both tests pass at n_g = 3, 6, 9", passes(one_window, 0) == [3, 6, 9] == passes(two_window, 0))
    GA.check("one doublet: the one-window test never passes", passes(one_window, 1) == [])
    GA.check("one doublet: the two-window test passes at n_g = 2, 5, 8", passes(two_window, 1) == [2, 5, 8])
    GA.check("two doublets: both pass at n_g = 1, 4, 7", passes(one_window, 2) == [1, 4, 7] == passes(two_window, 2))
    GA.check("two generations with one doublet: c = 60", charge(2, 12, 4, 0) == 60)
    I4 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), SQ), GA.mul(GA.gen(2), GA.gen(3), SQ), SQ)
    I4p = lambda n: GA.sc(1) if n == 0 else GA.mul(I4, I4p(n - 1), SQ)
    GA.check("c = 60: the one-window phase I4^10 = -1 (U = -P)", I4p(60 // 6) == GA.sc(-1))
    GA.check("c = 60: the two-window phase I4^20 = 1", I4p(2 * 60 // 6) == GA.sc(1))
    return True


def check_neutral_singlet_and_the_per_generation_count():
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    for n_g in FERMION_TEST_RANGE:
        c15 = charge(n_g, 0, 0, 0, per_gen=15)
        GA.check("fifteen per generation: one-window iff 8 | n_g", one_window(c15) == (n_g % 8 == 0))
        GA.check("fifteen per generation: two-window iff 4 | n_g", two_window(c15) == (n_g % 4 == 0))
    for f in PER_GEN_RANGE:
        q = (F(24) / _gcd(24, f)).numerator
        for n_g in FERMION_TEST_RANGE:
            GA.check("f per generation: one-window iff 24/gcd(24, f) | n_g",
                     one_window(charge(n_g, 0, 0, 0, per_gen=f)) == (n_g % q == 0))
        q2 = (F(12) / _gcd(12, f)).numerator
        for n_g in FERMION_TEST_RANGE:
            GA.check("f per generation: two-window iff 12/gcd(12, f) | n_g",
                     two_window(charge(n_g, 0, 0, 0, per_gen=f)) == (n_g % q2 == 0))
        GA.check("the modulus is 3 exactly when f = 8 or 16 mod 24", (q == 3) == (f % 24 in (8, 16)))
    GA.check("sixteen and eight (Majorana-Weyl count) give the same modulus 3",
             (F(24) / _gcd(24, 16)) == (F(24) / _gcd(24, 8)) == 3)
    return True


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def check_boson_fermion_balance_passes_every_generation_number():
    premise("synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations")
    for n_g in WIDE:
        f = 16 * n_g
        b = 2 * f
        GA.check("balance b = 2f gives c = 48 n_g", f + b == 48 * n_g)
        GA.check("and both tests pass", one_window(f + b) and two_window(f + b))
    # the stored quartic coefficient 2 N_V + N_S - 2 N_W vanishes at N_g = 3, N_V = 12 only for N_S = 72
    N_W = 16 * 3
    N_S = 2 * N_W - 2 * 12
    GA.check("N_S = 72", N_S == 72)
    GA.check("the Sakharov-balanced content has c = 144", charge(3, 12, N_S, 0) == 144)
    GA.check("144 = 6 * 24", one_window(charge(3, 12, N_S, 0)) and F(144, 24) == 6)
    GA.check("control: removing one scalar breaks it", not one_window(charge(3, 12, N_S - 1, 0)))
    return True
