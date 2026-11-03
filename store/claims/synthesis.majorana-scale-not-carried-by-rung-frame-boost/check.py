"""synthesis.frame-tied-majorana-scale-forces-light-neutrinos-below-hubble: exact checks.

The Clifford algebra of the ten as Cl(5,5) in GA.py: generators 0..4 are e+_a (square +1), 5..9 are e-_a
(square -1), a = 0..4; the text's slots 1..5 are a = 0..4, the pair slots a = 0, 1, 2 and the rung slots
a = 3, 4 (the text's 4 and 5). v_a = (e-_a + e+_a)/2, w_a = (e+_a - e-_a)/2, so v_a w_b + w_b v_a = delta_ab,
n_a = v_a w_a. The tower's * is reverse composed with theta (theta fixes e+ and negates e-), so v_a* = w_a;
the *-norm of X is the scalar part of X* X. The frame boost B_s maps v_a -> s v_a, w_a -> w_a / s on the rung
slots and fixes the pair slots; it is extended to the algebra as the automorphism induced on generators.
N_R = n_3 + n_4, T_3R = (n_3 + n_4 - 1)/2, B - L = -(2/3) sum_{pair} (n_a - 1/2), Y = T_3R + (B - L)/2.
Units in (1)-(3): H = 1, so Lambda/3 = 1 and the balanced rung component is c = -w_3 + v_3.
Everything is exact (Fractions).
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise, quantity

NS = 5
SQ = GA.sig(NS, NS)
PAIR = (0, 1, 2)
RUNG = (3, 4)
HALF = F(1, 2)


def ep(a):
    return GA.gen(a)


def em(a):
    return GA.gen(NS + a)


def v(a):
    return GA.scal(HALF, GA.add(em(a), ep(a)))


def w(a):
    return GA.scal(HALF, GA.sub(ep(a), em(a)))


def mul(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def comm(a, b):
    return GA.sub(mul(a, b), mul(b, a))


def theta(x):
    return {b: (-c if sum(1 for i in b if i >= NS) % 2 else c) for b, c in x.items()}


def star(x):
    return GA.reverse(theta(x))


def scalar(x):
    return x.get((), F(0))


def snorm(x):
    return scalar(mul(star(x), x))


def num(a):
    return mul(v(a), w(a))


def boost_images(s):
    """Images of the ten generators under B_s."""
    s = F(s)
    img = {}
    for a in range(NS):
        if a in RUNG:
            img[a] = GA.add(GA.scal(s, v(a)), GA.scal(1 / s, w(a)))
            img[NS + a] = GA.sub(GA.scal(s, v(a)), GA.scal(1 / s, w(a)))
        else:
            img[a] = ep(a)
            img[NS + a] = em(a)
    return img


def boost(x, s):
    img = boost_images(s)
    out = {}
    for blade, c in x.items():
        out = GA.add(out, GA.scal(c, mul(*[img[i] for i in blade])))
    return out


def weight(op, x):
    """The eigenvalue q with [op, x] = q x, or None if x is not an eigenvector of ad(op)."""
    y = comm(op, x)
    if not y:
        return F(0)
    blade = next(iter(x))
    q = y.get(blade, F(0)) / x[blade]
    return q if GA.eq(y, GA.scal(q, x)) else None


N_R = GA.add(num(3), num(4))
T3R = GA.scal(HALF, GA.sub(N_R, GA.sc(1)))
BL = GA.scal(F(-2, 3), GA.add(*[GA.sub(num(a), GA.sc(HALF)) for a in PAIR]))
YH = GA.add(T3R, GA.scal(HALF, BL))
T = mul(v(0), v(1), v(2), v(3), v(4))
TS = star(T)
C_BAL = GA.add(GA.neg(w(3)), v(3))


def check_frame_boost_is_twice_right_isospin():
    """(1) B_s is an isometry of the ten (images obey the Clifford relations), it reproduces the stored lift
    family (B_{1/lam} c_1 = c_lam), and on every sampled monomial it acts as s^q with q the ad N_R weight,
    which is twice the ad T_3R weight."""
    premise("synthesis.rung-unit-is-frame-boost")
    premise("synthesis.rung-unit-transverse-to-norm")
    for s in (F(2), F(3, 2)):
        img = boost_images(s)
        for i in range(2 * NS):
            for j in range(i, 2 * NS):
                ac = GA.add(mul(img[i], img[j]), mul(img[j], img[i]))
                want = GA.sc(2 * SQ[i]) if i == j else {}
                GA.check("boost images obey the Clifford relations", GA.eq(ac, want))
        h = F(1, 3)
        c1 = GA.add(GA.neg(w(3)), GA.scal(h, v(3)))
        clam = GA.add(GA.scal(-s, w(3)), GA.scal(h / s, v(3)))
        GA.check("B_{1/lam} c_1 = c_lam (stored lift family)", GA.eq(boost(c1, 1 / s), clam))
        monos = [v(3), w(4), mul(v(3), w(4)), mul(w(3), w(4)), v(0), mul(w(1), v(3), v(4)),
                 mul(v(0), v(1), v(2), w(3), w(4)), T, TS]
        for x in monos:
            q = weight(N_R, x)
            GA.check("monomial is an ad N_R eigenvector", q is not None and q.denominator == 1)
            GA.check("ad N_R = 2 ad T_3R", weight(T3R, x) * 2 == q)
            GA.check("B_s x = s^q x", GA.eq(boost(x, s), GA.scal(s ** int(q), x)))
    return True


def check_majorana_directions_have_frame_weight_two():
    """(2) [B-L, T] = -2T, [T_3R, T] = T, [Y, T] = 0, [N_R, T] = 2T, and the opposite weights for T*.
    Over all 3^5 slot-type monomials (each slot v, w or absent) the weights are additive; the
    hypercharge-neutral ones with B - L = -2 or +2 are exactly the T-type and T*-type classes, of frame weight
    +2 and -2; every hypercharge-neutral class has N_R weight -(B - L); rung vectors have Y = +-1/2 and
    frame weight +-1."""
    premise("standard-model.majorana-element")
    premise("synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square")
    GA.check("[B-L, T] = -2T", weight(BL, T) == -2)
    GA.check("[T_3R, T] = T", weight(T3R, T) == 1)
    GA.check("[Y, T] = 0", weight(YH, T) == 0)
    GA.check("[N_R, T] = 2T", weight(N_R, T) == 2)
    GA.check("T* has B-L +2, N_R -2, Y 0",
             weight(BL, TS) == 2 and weight(N_R, TS) == -2 and weight(YH, TS) == 0)
    majorana = []
    neutral_ok = True
    for types in product((0, 1, -1), repeat=NS):
        factors = [v(a) if t == 1 else w(a) for a, t in enumerate(types) if t]
        x = mul(*factors)
        nr, bl, yy = weight(N_R, x), weight(BL, x), weight(YH, x)
        p = sum(types[a] for a in PAIR)
        r = sum(types[a] for a in RUNG)
        GA.check("weights additive", nr == r and bl == F(-2, 3) * p and yy == F(r, 2) - F(p, 3))
        if yy == 0:
            neutral_ok = neutral_ok and nr == -bl
            if abs(bl) == 2:
                majorana.append((types, nr))
        if p == 0 and abs(r) == 1 and sum(abs(t) for t in types) == 1:
            GA.check("rung vector: Y = +-1/2, frame weight +-1", abs(yy) == HALF and abs(nr) == 1)
    GA.check("Y = 0 implies N_R weight = -(B - L)", neutral_ok)
    GA.check("Y = 0 and |B-L| = 2: only the T and T* classes, frame weights +-2",
             sorted(majorana) == [((-1, -1, -1, -1, -1), -2), ((1, 1, 1, 1, 1), 2)])
    return True


def check_star_norm_is_chebyshev_in_the_frame():
    """(3) In H = 1 units: the balanced rung component has *-norm 1 and pairing Q = -1; the balanced
    Majorana element D = T + T* has frame-invariant pairing <rev(D) D> != 0. Under B_s,
    x = |B_s c|_* = (s^2 + s^-2)/2 and |B_s D|_* / |D|_* = (s^4 + s^-4)/2 = 2x^2 - 1 (Chebyshev T_2), the cross
    terms vanish, and the pairings are frame-invariant; a null element (T alone) has pairing 0 and its *-norm
    is rescaled by s^4 with nothing fixed."""
    premise("synthesis.rung-unit-is-frame-boost")
    premise("standard-model.majorana-element")
    D = GA.add(T, TS)
    tn = snorm(T)
    GA.check("|c_bal|_* = 1 and Q(c_bal) = -1", snorm(C_BAL) == 1 and scalar(mul(C_BAL, C_BAL)) == -1)
    GA.check("|T|_* = |T*|_* = 1/32", tn == F(1, 32) and snorm(TS) == tn)
    p0 = scalar(mul(GA.reverse(D), D))
    GA.check("balanced Majorana pairing nonzero", p0 != 0)
    GA.check("T is null for the pairing", scalar(mul(GA.reverse(T), T)) == 0)
    for s in (F(2), F(3), F(3, 2)):
        x = snorm(boost(C_BAL, s))
        GA.check("|B_s c|_* = (s^2 + s^-2)/2", x == (s ** 2 + s ** -2) / 2)
        GA.check("Q(B_s c) = -1", scalar(mul(boost(C_BAL, s), boost(C_BAL, s))) == -1)
        bd = boost(D, s)
        y = snorm(bd) / snorm(D)
        GA.check("|B_s D|_*/|D|_* = (s^4 + s^-4)/2", y == (s ** 4 + s ** -4) / 2)
        GA.check("Chebyshev: = 2 x^2 - 1", y == 2 * x ** 2 - 1)
        u = 2 * x
        GA.check("with v^2 = 2N (u = v^2/H^2): M^2/H^2 = u^2/2 - 1", y == u ** 2 / 2 - 1)
        GA.check("no cross term", snorm(bd) == snorm(boost(T, s)) + snorm(boost(TS, s)))
        GA.check("pairing frame-invariant", scalar(mul(GA.reverse(bd), bd)) == p0)
        GA.check("null element: |B_s T|_* = s^4 |T|_*", snorm(boost(T, s)) == s ** 4 * tn)
    return True


def arctan_partial(x, terms):
    return sum((F(-1) ** k * x ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), F(0))


def pi_upper():
    """Machin: pi = 16 atan(1/5) - 4 atan(1/239); alternating partial sums ending on a + term bound atan
    above, ending on a - term bound it below."""
    return 16 * arctan_partial(F(1, 5), 5) - 4 * arctan_partial(F(1, 239), 2)


def pi_lower():
    """Machin with the partial sums the other way round: a lower bound for pi."""
    return 16 * arctan_partial(F(1, 5), 4) - 4 * arctan_partial(F(1, 239), 3)


def check_frame_tied_majorana_scale_against_record():
    """(4) With v^2 = 2N, M^2 = 2 v^4/(4H^2) - H^2 = v^4/(2H^2) - H^2 >= (v^2/2H)^2 for v^2 >= 2H^2, so M >= v^2/2H, and
    H <= H_0: from stored quantities, v^2 = M_W^2 sin^2(theta_W) alpha^-1/pi > 6.08e4 GeV^2 (pi < 22/7, Machin),
    1/H_0 > 6.95e41 /GeV, so M > 2.1e46 GeV, more than 1.7e27 M_P and 4.05e34 times the perturbative cap 4 pi v_R
    (v_R = 4.15e10 GeV); and the seesaw light masses, below 4 pi v^2/(sigma M) <= 8 pi H/sigma for Majorana family
    couplings of smallest singular value sigma, reach the stored m_3 only if sigma < 1/1.38e30."""
    premise("synthesis.rung-unit-is-frame-boost")
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("standard-model.what-angle-asks-neutrino-sector")
    premise("synthesis.majorana-scale-free-on-pati-salam-route")
    premise("standard-model.imported-clebsch-structure-seesaw")
    hbar = quantity("quantity.reduced-planck-constant")
    mpc_m = quantity("quantity.megaparsec")
    h0 = quantity("quantity.hubble-constant")
    mw = quantity("quantity.w-boson-mass")
    s2w = quantity("quantity.weak-mixing-angle-mz")
    ainv = quantity("quantity.inverse-fine-structure-mz")
    mp = quantity("quantity.planck-mass")
    m3_ev = quantity("quantity.heaviest-neutrino-mass")
    GA.check("stored m_3 = 0.050 eV", m3_ev * 20 == 1)
    pi_hi = F(22, 7)
    GA.check("pi < 22/7 (Machin partial sums)", pi_upper() < pi_hi)
    h0_gev = hbar * h0 * 1000 / mpc_m
    GA.check("1/H_0 > 6.95e41 GeV^-1", h0_gev * 695 * 10 ** 39 < 1)
    v2_lo = mw ** 2 * s2w * ainv / pi_hi
    GA.check("v^2 > 6.08e4 GeV^2", v2_lo > 608 * 10 ** 2)
    xx = v2_lo / (2 * h0_gev ** 2)
    GA.check("x = v^2/2H^2 >= 1, so 2x^2 - 1 >= x^2", xx > 1 and 2 * xx ** 2 - 1 >= xx ** 2)
    m_lo = v2_lo / (2 * h0_gev)
    GA.check("M > 2.1e46 GeV", m_lo > 21 * 10 ** 45)
    GA.check("M > 1.7e27 M_P", m_lo > 17 * 10 ** 26 * mp)
    vr = F(415, 100) * 10 ** 10
    GA.check("M > 4.05e34 x 4 pi v_R", m_lo > 405 * 10 ** 32 * 4 * pi_hi * vr)
    h0_ev = h0_gev * 10 ** 9
    GA.check("seesaw light mass <= 8 pi H_0 < m_3 / 1.38e30", 8 * pi_hi * h0_ev * 138 * 10 ** 28 < m3_ev)
    return True


def check_other_extensions_tie_to_v_or_h():
    """(5) Boosting rung slot 4 alone: an isometry, T has weight 1 (n_4), like the rung vector v_4. Extending as the
    complexified hypercharge: T, T* and every Y = 0 monomial have weight 0. Against the record (pi > 3 by Machin,
    v^2 < 6.37e4 GeV^2): v_R^2 > 2.7e16 v^2 and v_R > 2.8e52 H_0."""
    premise("standard-model.majorana-element")
    premise("standard-model.what-angle-asks-neutrino-sector")
    for s in (F(2), F(5, 3)):
        img = {i: GA.gen(i) for i in range(2 * NS)}
        img[3] = GA.add(GA.scal(s, v(3)), GA.scal(1 / s, w(3)))
        img[NS + 3] = GA.sub(GA.scal(s, v(3)), GA.scal(1 / s, w(3)))
        ok = all(GA.eq(GA.add(mul(img[i], img[j]), mul(img[j], img[i])), GA.sc(2 * SQ[i]) if i == j else {})
                 for i in range(2 * NS) for j in range(i, 2 * NS))
        GA.check("slot-4 boost is an isometry", ok)
        bt = {}
        for blade, c in T.items():
            bt = GA.add(bt, GA.scal(c, mul(*[img[i] for i in blade])))
        GA.check("slot-4 boost: B T = s T (weight 1)", GA.eq(bt, GA.scal(s, T)))
        GA.check("slot-4 weight of T equals that of v_4", weight(num(3), T) == weight(num(3), v(3)) == 1)
    GA.check("hypercharge weight of T and T* is 0", weight(YH, T) == 0 and weight(YH, TS) == 0)
    GA.check("hypercharge weight of the rung vector is 1/2", weight(YH, v(3)) == HALF)
    hbar = quantity("quantity.reduced-planck-constant")
    mpc_m = quantity("quantity.megaparsec")
    h0 = quantity("quantity.hubble-constant")
    mw = quantity("quantity.w-boson-mass")
    s2w = quantity("quantity.weak-mixing-angle-mz")
    ainv = quantity("quantity.inverse-fine-structure-mz")
    pi_lo = 3
    GA.check("pi > 3 (Machin partial sums)", pi_lower() > pi_lo)
    v2_hi = mw ** 2 * s2w * ainv / pi_lo
    GA.check("v^2 < 6.37e4 GeV^2", v2_hi * 100 < 637 * 10 ** 4)
    vr = F(415, 100) * 10 ** 10
    GA.check("v_R^2 > 2.7e16 v^2", vr ** 2 > 27 * 10 ** 15 * v2_hi)
    h0_gev = hbar * h0 * 1000 / mpc_m
    GA.check("v_R > 2.8e52 H_0", vr > 28 * 10 ** 51 * h0_gev)
    return True


EXPORTS = {"frame_boost": boost, "majorana_element": T}
