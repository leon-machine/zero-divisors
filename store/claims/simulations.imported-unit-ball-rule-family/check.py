"""simulations.imported-unit-ball-rule-family: exact checks in Q(pi).

pi is transcendental, so identities in pi are checked as identities of rational functions in an
indeterminate (GA.RF); numerical statements use rational bounds on pi from Machin's formula
(alternating arctan series with explicit remainder), all exact.
(1) Unit-ball volumes from V_0 = 1, V_1 = 2, V_D = (2 pi / D) V_{D-2}: V_2 = pi, V_3 = 4 pi/3,
    V_4 = pi^2/2. Under R1 (equal mass) and R2 (one quantum per unit ball, common radius) the share
    of a tower of space dimension D is V_3/V_D: 1, 4/3, 8/(3 pi); with this tower, two D = 2 towers
    and two D = 4 towers the total is 1 + 8/3 + 16/(3 pi) = (11 pi + 16)/(3 pi), in
    [5.3643, 5.3644) (so 5.364 to the stated figure).
(2) With thickness c d_b (R3 at c = 1) the D = 2 shares divide by c and the D = 4 shares multiply
    by c: T(c) = 1 + 8/(3c) + 16c/(3 pi) (as rational functions in pi at five rational c);
    T(1) = T(pi/2) = (11 pi + 16)/(3 pi); T(c) = T(pi/(2c)).
(3) The floor: with A = 8/3, B = 16/(3 pi), (A/c + Bc)^2 - 4AB = (A/c - Bc)^2 (identity at sample c),
    so T >= 1 + 2 sqrt(AB) with equality only at c^2 = A/B = pi/2; 4AB = 512/(9 pi) = 4 * 128/(9 pi),
    i.e. T* = 1 + 2 sqrt(128/(9 pi)); numerically c* = sqrt(pi/2) in [1.2533, 1.2534) and
    T* in [5.2553, 5.2555), the stated 1.2533 and 5.255.
Not tested: that the sheets move with the matter (a dynamical statement resting on
dark-matter.reduced-response-gravity-needs-supporting-stress, with no finite core here).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI = GA.RF.var()


def _c(x):
    return GA.RF.const(F(x))


def _arctan_bounds(x, terms):
    s = F(0)
    for k in range(terms):
        s += F((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
    err = x ** (2 * terms + 1) / (2 * terms + 1)
    return s - err, s + err


def _pi_bounds():
    a_lo, a_hi = _arctan_bounds(F(1, 5), 12)
    b_lo, b_hi = _arctan_bounds(F(1, 239), 4)
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo


def _volumes():
    V = {0: _c(1), 1: _c(2)}
    for D in range(2, 5):
        V[D] = _c(F(2, D)) * PI * V[D - 2]
    return V


def check_unit_ball_shares_and_total():
    premise("dark-matter.unit-ball-rule")
    premise("dark-matter.r1-equal-mass-per-quantum")
    premise("dark-matter.r2-one-quantum-per-unit-ball")
    ok = True
    V = _volumes()
    ok = ok and V[2].eqrf(PI) and V[3].eqrf(_c(F(4, 3)) * PI) and V[4].eqrf(_c(F(1, 2)) * PI * PI)
    share = {D: V[3] / V[D] for D in (2, 3, 4)}
    ok = ok and share[3].eqrf(_c(1)) and share[2].eqrf(_c(F(4, 3))) and share[4].eqrf(_c(F(8, 3)) / PI)
    total = share[3] + _c(2) * share[2] + _c(2) * share[4]
    closed = (_c(11) * PI + _c(16)) / (_c(3) * PI)
    ok = ok and total.eqrf(closed)
    lo, hi = _pi_bounds()
    ok = ok and lo < hi and hi - lo < F(1, 10 ** 12)
    # (11 pi + 16)/(3 pi) = 11/3 + 16/(3 pi) is decreasing in pi
    t_hi = F(11, 3) + 16 / (3 * lo)
    t_lo = F(11, 3) + 16 / (3 * hi)
    ok = ok and F(53643, 10000) <= t_lo and t_hi < F(53644, 10000)
    GA.check("shares V3/V_D = 1, 4/3, 8/(3 pi); total (11 pi + 16)/(3 pi) = 5.3643...", ok)
    return ok


def _T(c):
    return _c(1) + _c(F(8, 3)) / c + _c(F(16, 3)) * c / PI


def check_thickness_family():
    premise("dark-matter.total-function-thickness")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    ok = True
    V = _volumes()
    for c in (F(1), F(1, 2), F(3), F(7, 5), F(2, 9)):
        cc = _c(c)
        built = _c(1) + _c(2) * (V[3] / V[2]) / cc + _c(2) * (V[3] / V[4]) * cc
        ok = ok and built.eqrf(_T(cc))
        ok = ok and _T(cc).eqrf(_T(PI / (_c(2) * cc)))                # T(c) = T(pi/(2c))
    closed = (_c(11) * PI + _c(16)) / (_c(3) * PI)
    ok = ok and _T(_c(1)).eqrf(closed) and _T(PI / _c(2)).eqrf(closed)
    GA.check("T(c) = 1 + 8/(3c) + 16c/(3 pi) from the shares; T(1) = T(pi/2); T(c) = T(pi/(2c))", ok)
    return ok


def check_floor_of_the_family():
    premise("dark-matter.total-function-thickness")
    ok = True
    A, B = _c(F(8, 3)), _c(F(16, 3)) / PI
    for c in (F(1), F(1, 3), F(5, 4), F(9, 2)):
        cc = _c(c)
        lhs = (A / cc + B * cc) * (A / cc + B * cc) - _c(4) * A * B
        rhs = (A / cc - B * cc) * (A / cc - B * cc)
        ok = ok and lhs.eqrf(rhs)
    ok = ok and (A / B).eqrf(PI / _c(2))
    ok = ok and (_c(4) * A * B).eqrf(_c(F(512, 9)) / PI) and (_c(4) * A * B).eqrf(_c(4) * _c(F(128, 9)) / PI)
    lo, hi = _pi_bounds()
    # c* = sqrt(pi/2): 1.2533^2 <= pi/2 < 1.2534^2
    ok = ok and F(12533, 10000) ** 2 <= lo / 2 and hi / 2 < F(12534, 10000) ** 2
    # T* - 1 = sqrt(512/(9 pi)): bounds by squares
    ok = ok and F(42553, 10000) ** 2 <= F(512, 9) / hi and F(512, 9) / lo < F(42555, 10000) ** 2
    GA.check("floor at c^2 = pi/2 (1.2533), T* = 1 + 2 sqrt(128/(9 pi)) in [5.2553, 5.2555)", ok)
    return ok
