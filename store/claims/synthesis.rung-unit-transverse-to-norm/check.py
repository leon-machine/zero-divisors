"""synthesis.rung-unit-transverse-to-norm: exact checks in the Clifford algebra of GA.py.

Generators (squares): 0 f+ (+1), 1 f- (-1)  the first rung, holding I = n_inf - (Lambda/6) n_O;
                      2 e+ (+1), 3 e- (-1)  the second rung, v = (e- + e+)/2, w = (e+ - e-)/2;
                      4 x1 (+1), 5 x2 (-1)  two further ground directions for generic lifts.
The lift with unit mu is X_mu(x) = mu n_O' + x + Q(x)/(2 mu) n_inf' with n_O' = -w, n_inf' = 2 v
(mu = 1 is transport.totality's X); the rung boost B_s is v -> s v, w -> w/s, the rest fixed;
* fixes e+ and negates e- (so v* = w).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = (1, -1, 1, -1, 1, -1)


def vec(cs):
    return GA.add(*[GA.scal(c, GA.gen(i)) for i, c in enumerate(cs) if c != 0]) if any(cs) else {}


def dot(x, y):
    return GA.dot(x, y, SQ)


def mul(x, y):
    return GA.mul(x, y, SQ)


H = F(1, 2)
V = vec([0, 0, H, H, 0, 0])            # v = (e- + e+)/2
Wm = vec([0, 0, H, -H, 0, 0])          # w = (e+ - e-)/2
NO1 = vec([-H, H, 0, 0, 0, 0])         # n_O of the first rung = (f- - f+)/2
NI1 = vec([1, 1, 0, 0, 0, 0])          # n_inf of the first rung = f- + f+


def I_of(Lam):
    return GA.add(NI1, GA.scal(-Lam / 6, NO1))


def Q(x):
    return dot(x, x)


def X(x, mu):
    """X_mu(x) = mu n_O' + x + Q(x)/(2 mu) n_inf' = -mu w + x + (Q(x)/mu) v."""
    return GA.add(GA.scal(-mu, Wm), x, GA.scal(Q(x) / mu, V))


def coords(x):
    return [x.get((i,), F(0)) for i in range(6)]


def boost(x, s):
    """B_s: v -> s v, w -> w/s on the second rung, identity on generators 0, 1, 4, 5."""
    c = coords(x)
    a, b = c[2], c[3]                  # x has a e+ + b e- = (a + b) v + (a - b) w
    pv, pw = a + b, a - b
    pv, pw = pv * s, pw / s
    # back to e+, e-: p v + q w = (p + q)/2 e+ + (p - q)/2 e-
    c[2], c[3] = (pv + pw) / 2, (pv - pw) / 2
    return vec(c)


def star(x):
    c = coords(x)
    c[3] = -c[3]
    return vec(c)


def rung(x):
    c = coords(x)
    return vec([0, 0, c[2], c[3], 0, 0])


def herm(x):
    return dot(star(x), x)


def proportional(a, b):
    """a = t b for some nonzero rational t (vectors)."""
    ca, cb = coords(a), coords(b)
    k = next(i for i in range(6) if cb[i] != 0)
    t = ca[k] / cb[k]
    return t != 0 and all(ca[i] == t * cb[i] for i in range(6))


def _generic_part():
    lams = (F(3, 5), F(4, 3), F(3), F(-6, 7))
    mus = (F(1), F(2), F(1, 3), F(7, 5))
    gens = [vec([1 if j == i else 0 for j in range(6)]) for i in range(6)]
    for s in mus:
        # the boost is a Klein isometry and keeps the CAR pair
        for a in gens:
            for b in gens:
                assert dot(boost(a, s), boost(b, s)) == dot(a, b)
        bv, bw = boost(V, s), boost(Wm, s)
        assert mul(bv, bv) == {} and mul(bw, bw) == {}
        assert GA.add(mul(bv, bw), mul(bw, bv)) == GA.sc(1)
        # * does not commute with the boost unless s = 1
        assert (star(boost(V, s)) == boost(star(V), s)) == (s == 1)
    xs = [vec([1, 2, 0, 0, 3, 1]), vec([F(1, 2), 0, 0, 0, -1, 2]), vec([0, 1, 0, 0, 1, 1])]
    for mu in mus:
        ep = boost(vec([0, 0, 1, 0, 0, 0]), 1 / mu)        # the boosted e+
        for x in xs:
            Xm = X(x, mu)
            assert Q(Xm) == 0 and Xm == boost(X(x, F(1)), 1 / mu)
            if Q(x) != 0:
                # totality (2) in the boosted frame: e+ X_mu(x) e+ is proportional to X_mu(x/Q(x))
                r = mul(mul(ep, Xm), ep)
                assert proportional(r, X(GA.scal(1 / Q(x), x), mu))
        for Lam in lams:
            I = I_of(Lam)
            assert Q(I) == Lam / 3
            c = rung(X(I, mu))
            assert Q(c) == -Lam / 3                         # Klein norm: Lambda only
            hn = herm(c)
            assert hn == (mu * mu + (Lam / (3 * mu)) ** 2) / 2
            if Lam > 0:
                assert hn - Lam / 3 == (mu - Lam / (3 * mu)) ** 2 / 2
                # mu <-> (Lambda/3)/mu leaves the Hermitian norm unchanged
                assert herm(rung(X(I, Lam / (3 * mu)))) == hn
            # rapidity tangent dc/dmu = -w - Lambda/(3 mu^2) v is Klein-orthogonal to c
            dc = GA.add(GA.scal(-1, Wm), GA.scal(-Lam / (3 * mu * mu), V))
            assert dot(dc, c) == 0 and (Q(c) != 0) == (Lam != 0)
    return True


def check_rung_unit_transverse_to_norm():
    premise("transport.totality")
    premise("standard-model.transported-frozen-point")
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    premise("odd-extensions.transport-constrains-frozen-point-only-through")
    # worked numbers at Lambda = 4/3 (Lambda/3 = 4/9, H = 2/3 in the lift's unit)
    Lam = F(4, 3)
    I = I_of(Lam)
    c1 = rung(X(I, F(1)))
    assert c1 == GA.add(GA.scal(-1, Wm), GA.scal(F(4, 9), V))          # transported-frozen-point (i)
    assert Q(c1) == F(-4, 9) and herm(c1) == F(97, 162)
    c2 = rung(X(I, F(2)))
    assert Q(c2) == F(-4, 9) and herm(c2) == F(328, 162)
    cb = rung(X(I, F(2, 3)))                                            # the balanced frame mu = H
    assert herm(cb) == F(4, 9) == -Q(cb)
    # the reciprocal's lift (transported-frozen-point (ii)) is the frame mu = Lambda/3
    recip = rung(GA.add(GA.scal(Lam / 3, vec([0, 0, -H, H, 0, 0])), GA.scal(H, GA.scal(2, V)), I))
    assert recip == rung(X(I, Lam / 3)) and herm(recip) == herm(c1)
    # a change of Lambda at fixed unit moves c off its level set: (d c/d Lambda) . c = -1/6
    for mu in (F(1), F(5, 2)):
        c = rung(X(I, mu))
        assert dot(GA.scal(1 / (3 * mu), V), c) == F(-1, 6)
        dc = GA.add(GA.scal(-1, Wm), GA.scal(-Lam / (3 * mu * mu), V))
        assert dot(dc, c) == 0
    # the boost by 3 moves the CAR pair but * sees it
    assert herm(boost(V, F(3))) == F(9, 2) and herm(V) == F(1, 2)
    return _generic_part()
