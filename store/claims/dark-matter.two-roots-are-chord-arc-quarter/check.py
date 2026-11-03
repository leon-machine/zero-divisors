"""dark-matter.two-roots-are-chord-arc-quarter: exact checks.

Numbers of Q(pi) are Laurent polynomials in pi, {k: c} for sum c pi^k (pi transcendental);
thicknesses are monomials, so c = pi/2 and c = pi are exact; decimals use rational bounds on pi.
T(c) = 1 + 8/(3c) + 16c/(3 pi) is the total of the premise.

(1) Chord and arc: on the sphere of radius R with our spacetime as its equator, the region between
    the equator and a pole has extent R along the polar axis (the pole (0, .., R) is at distance R
    from the equatorial hyperplane) and a quarter of a great circle along the surface, |S^1| R / 4
    with |S^1| = 2 V_2 = 2 pi: arc/chord = pi/2. With R = d_b the chord assignment is c = 1 and the
    arc assignment c = pi/2.
(2) The two totals agree, T(1) = T(pi/2) (identity in pi, the exchange symmetry of the premise),
    while the compositions differ: (f_3D, f_5D) = (4/3, 8/(3 pi)) at c = 1 and (8/(3 pi), 4/3) at
    c = pi/2.
(3) R2's cells: that a unit ball's extent along the added direction from its centre is its radius is the
    definition of the ball, so the selection of the chord (c = 1, against the arc's pi/2 of (1)) is
    definitional and has no separate check.
(4) Both poles: c = 2 and c = pi give T(2) = 7/3 + 32/(3 pi), which rounds to 5.729, and
    T(pi) = 19/3 + 8/(3 pi), which rounds to 7.182, each more than four sigma above 0.1200/0.02237
    (sigma 0.065): excluded.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)
OBS = F(1200, 10000) / F(2237, 100000)
SIG = F(65, 1000)
RADII = [F(1), F(49, 50), F(7, 3)]


def lp(c, k=0):
    return {k: F(c)} if c != 0 else {}


def ladd(*xs):
    out = {}
    for x in xs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def lmul(*xs):
    out = {0: F(1)}
    for b in xs:
        new = {}
        for k1, c1 in out.items():
            for k2, c2 in b.items():
                new[k1 + k2] = new.get(k1 + k2, F(0)) + c1 * c2
        out = {k: c for k, c in new.items() if c != 0}
    return out


def linv(a):
    assert len(a) == 1
    (k, c), = a.items()
    return {-k: 1 / c}


def bounds(x):
    lo = hi = F(0)
    for k, c in x.items():
        u, v = c * PI_LO ** k, c * PI_HI ** k
        lo += min(u, v)
        hi += max(u, v)
    return lo, hi


def ball(D):
    V = {0: lp(1), 1: lp(2)}
    for n in range(2, D + 1):
        V[n] = lmul(lp(F(2, n), 1), V[n - 2])
    return V[D]


def shares(c):
    return lmul(lp(F(4, 3)), linv(c)), lmul(lp(F(8, 3), -1), c)


def T(c):
    f3, f5 = shares(c)
    return ladd(lp(1), lmul(lp(2), f3), lmul(lp(2), f5))


def check_chord_and_arc():
    circle = lmul(lp(2), ball(2))                     # |S^1| = 2 V_2
    assert circle == {1: F(2)}
    for R in RADII:
        pole = [F(0), F(0), F(0), F(0), R]
        chord = pole[4]                               # distance to the hyperplane x_5 = 0
        arc = lmul(circle, lp(R / 4))
        assert lmul(arc, linv(lp(chord))) == {1: F(1, 2)}
    return True


def check_totals_agree_compositions_differ():
    premise("dark-matter.total-function-thickness")
    c_chord, c_arc = lp(1), lp(F(1, 2), 1)
    assert T(c_chord) == T(c_arc)
    assert T(c_chord) == {0: F(11, 3), -1: F(16, 3)}
    assert shares(c_chord) == ({0: F(4, 3)}, {-1: F(8, 3)})
    assert shares(c_arc) == ({-1: F(8, 3)}, {0: F(4, 3)})
    assert shares(c_chord) != shares(c_arc)
    return True


def check_both_poles_excluded():
    premise("dark-matter.total-function-thickness")
    t2, tpi = T(lp(2)), T(lp(1, 1))
    assert t2 == {0: F(7, 3), -1: F(32, 3)} and tpi == {0: F(19, 3), -1: F(8, 3)}
    lo, hi = bounds(t2)
    assert round(lo * 1000) == round(hi * 1000) == 5729 and (lo - OBS) / SIG > 4
    lo, hi = bounds(tpi)
    assert round(lo * 1000) == round(hi * 1000) == 7182 and (lo - OBS) / SIG > 4
    return True
