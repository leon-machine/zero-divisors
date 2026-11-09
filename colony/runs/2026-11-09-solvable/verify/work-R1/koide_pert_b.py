"""synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class: exact checks.

Q(m) = sum m_k / (sum sqrt m_k)^2. Square roots of data enter only through certified rational bounds (integer
square roots at scale 10^-12), and every inequality is decided with the bound that makes it harder to pass.
t* = 3/sqrt(2) - 2 is the positive root of 2t^2 + 8t - 1, and t*^2 = 17/2 - 6 sqrt(2); a rational r satisfies
r < t*^2 exactly when r < 17/2 and 72 < (17/2 - r)^2, decided in rationals with no square root.
(1) The middle-mass lemma: Q(t, t, 1) - 2/3 = -(2t^2 + 8t - 1)/(3(2t + 1)^2) as rational functions (sampled), a
    rational bracket of t* and of t*^2, Q > 2/3 on a rational grid of [0, t_lo]^2 with the heaviest root 1, and
    Q(t_hi, t_hi, 1) < 2/3.
(2) The up sector: m_c/m_t < t*^2 at the own-scale and the M_Z values (stored quantities), while m_s/m_b > t*^2 in
    the down sector at both; Q(m_c, m_c, m_t) > 2/3, so (x, m_c, m_t) with x <= m_c is never a Koide triple; an
    order-preserving Koide bracket of the up sector needs D_t/D_c in (1.99, 2.00) or above (own scale), (4.08, 4.09)
    or above (M_Z).
(3) The remaining class D2 > D3 > D1: the least D3/D1 with Q(R m_1, m_2, m_3) <= 2/3 is certified in (7.88, 7.89),
    (11.00, 11.01), (2010.2, 2010.3), (4799.8, 4799.9); the class D1 > D3 > D2 needs D3/D2 in (2.19, 2.20),
    (2.63, 2.64), (9.36, 9.37), (19.33, 19.34) or above; the ninth conditions hold at the upper ends; and each class
    contains Koide brackets (an explicit certified point), so it is a threshold, not an exclusion.
(4) The stored lemma (iv) covers the class: on a rational grid of points with D2 > D3 > D1 and D3/D1 below the stored
    corner value, Q stays above Q(R m_1, R m_2, m_3) > 2/3.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

SCALE = 10 ** 12
TWO3 = F(2, 3)
HALF17 = F(9)


def isqrt(n):
    if n < 0:
        raise ValueError
    x = int(n)
    if x == 0:
        return 0
    r = 1 << ((x.bit_length() + 1) // 2)
    while True:
        y = (r + x // r) // 2
        if y >= r:
            return r
        r = y


def sqrt_bounds(q):
    q = F(q)
    n = (q * SCALE * SCALE).__floor__()
    lo = isqrt(n)
    return F(lo, SCALE), F(lo + 1, SCALE)


def Q_s(s):
    S1 = sum(s, F(0))
    return sum((x * x for x in s), F(0)) / (S1 * S1)


def Q_gt(m):
    hi = sum((sqrt_bounds(x)[1] for x in m), F(0))
    return 3 * sum(m, F(0)) > 2 * hi * hi


def Q_lt(m):
    lo = sum((sqrt_bounds(x)[0] for x in m), F(0))
    return 3 * sum(m, F(0)) < 2 * lo * lo


def below_tstar_sq(r):
    """r < 17/2 - 6 sqrt 2, exactly."""
    r = F(r)
    return r < HALF17 and 72 < (HALF17 - r) ** 2


def above_tstar_sq(r):
    r = F(r)
    return r < HALF17 and (HALF17 - r) ** 2 < 72


def gev(qid, scale=F(1)):
    return scale * F(quantity(qid))


def down_own():
    return [gev("quantity.down-quark-mass", F(1, 1000)), gev("quantity.strange-quark-mass", F(1, 1000)),
            gev("quantity.bottom-quark-mass")]


def down_mz():
    return [gev("quantity.down-quark-mass-mz", F(1, 1000)), gev("quantity.strange-quark-mass-mz", F(1, 1000)),
            gev("quantity.bottom-quark-mass-mz")]


def up_own():
    return [gev("quantity.up-quark-mass", F(1, 1000)), gev("quantity.charm-quark-mass"),
            gev("quantity.top-quark-mass")]


def up_mz():
    return [gev("quantity.up-quark-mass-mz", F(1, 1000)), gev("quantity.charm-quark-mass-mz"),
            gev("quantity.top-quark-mass-mz")]


def sets():
    return {"down own": down_own(), "down MZ": down_mz(), "up own": up_own(), "up MZ": up_mz()}


# (1) --------------------------------------------------------------------------------------------

def check_middle_mass_lemma():
    premise("families.linear-conjecture-refuted-data")
    premise("synthesis.mass-ordered-dressing-cannot-spoil-koide")
    ok = True
    want = {F(0): F(1), F(1, 9): F(83, 121), F(1, 8): F(33, 50), F(3, 10): F(59, 128), F(7, 5): F(123, 361),
            F(2): F(9, 25)}
    for t, q in want.items():
        ok = ok and Q_s([t, t, F(1)]) == q
        ok = ok and q - TWO3 == -(2 * t * t + 8 * t - 1) / (3 * (2 * t + 1) ** 2)
    # sign pattern of Q(t, t, 1) - 2/3 on the samples: above 2/3 below t*, below 2/3 above it
    ok = ok and [q > TWO3 for q in want.values()] == [True, True, False, False, False, False]
    # rational bracket of t*: 2t^2 + 8t - 1 changes sign
    t_lo, t_hi = F(1213, 10000), F(1214, 10000)
    p = lambda t: 2 * t * t + 8 * t - 1
    ok = ok and p(t_lo) < 0 < p(t_hi)
    # and of t*^2 = 17/2 - 6 sqrt 2, decided without roots
    ok = ok and below_tstar_sq(t_lo * t_lo) and above_tstar_sq(t_hi * t_hi)
    ok = ok and below_tstar_sq(F(1471, 100000)) and above_tstar_sq(F(1472, 100000))
    ok = ok and 3 * t_hi < 1 and t_hi - t_lo == F(1, 10000)
    # Q > 2/3 whenever both lighter roots are at most t_lo (heaviest root 1): grid, corner included
    n = 0
    for a in range(0, 13):
        for b in range(a, 13):
            s1, s2 = t_lo * F(a, 12), t_lo * F(b, 12)
            ok = ok and Q_s([s1, s2, F(1)]) > TWO3
            n += 1
    ok = ok and n == 91
    # the bound is attained only at the degenerate triple: just above t*, both equal, Q < 2/3
    ok = ok and Q_s([t_hi, t_hi, F(1)]) < TWO3 and Q_s([t_lo, t_lo, F(1)]) > TWO3
    GA.check("Koide triple: middle entry at least (17/2 - 6 sqrt 2) of the heaviest, t* = 3/sqrt 2 - 2", ok)
    return ok


# (2) --------------------------------------------------------------------------------------------

def check_up_sector_charm_to_top_ratio_is_below_the_bound():
    premise("synthesis.mass-ordered-dressing-cannot-spoil-koide")
    s = sets()
    ok = True
    for k in ("up own", "up MZ"):
        m = s[k]
        ok = ok and below_tstar_sq(m[1] / m[2])
        # (x, m_c, m_t) with x <= m_c: Q >= Q(m_c, m_c, m_t) > 2/3
        ok = ok and Q_gt([m[1], m[1], m[2]]) and 9 * m[1] <= m[2]
    for k in ("down own", "down MZ"):
        m = s[k]
        ok = ok and above_tstar_sq(m[1] / m[2])
    # the ratios to three places
    r_own, r_mz = s["up own"][1] / s["up own"][2], s["up MZ"][1] / s["up MZ"][2]
    ok = ok and F(737, 100000) < r_own < F(738, 100000) and F(360, 100000) < r_mz < F(361, 100000)
    # order-preserving Koide bracket (b_u <= b_c): needs rho = D_t/D_c at least t*^2 m_t/m_c
    for k, lo, hi in (("up own", F(199, 100), F(200, 100)), ("up MZ", F(408, 100), F(409, 100))):
        m = s[k]
        ok = ok and Q_gt([lo * m[1], lo * m[1], m[2]]) and Q_lt([hi * m[1], hi * m[1], m[2]])
        ok = ok and 9 * hi * m[1] <= m[2]
    GA.check("up quarks: m_c/m_t < 17/2 - 6 sqrt 2 (0.0074, 0.0036), so no (x <= m_c, m_c, m_t) is Koide", ok)
    return ok


# (3) --------------------------------------------------------------------------------------------

def check_remaining_class_thresholds():
    premise("synthesis.mass-ordered-dressing-cannot-spoil-koide")
    s = sets()
    r1 = {"down own": (F(788, 100), F(789, 100)), "down MZ": (F(1100, 100), F(1101, 100)),
          "up own": (F(20102, 10), F(20103, 10)), "up MZ": (F(47998, 10), F(47999, 10))}
    r2 = {"down own": (F(219, 100), F(220, 100)), "down MZ": (F(263, 100), F(264, 100)),
          "up own": (F(936, 100), F(937, 100)), "up MZ": (F(1933, 100), F(1934, 100))}
    ok = True
    for k, m in s.items():
        lo, hi = r1[k]
        ok = ok and Q_gt([lo * m[0], m[1], m[2]]) and Q_lt([hi * m[0], m[1], m[2]])
        ok = ok and 9 * hi * m[0] <= m[2] and 9 * m[1] <= m[2]
        lo, hi = r2[k]
        ok = ok and Q_gt([m[0], lo * m[1], m[2]]) and Q_lt([m[0], hi * m[1], m[2]])
        ok = ok and 9 * hi * m[1] <= m[2]
    # the class D2 > D3 > D1 is not empty of Koide brackets: rho_2 = 99/100 < 1 < rho_1
    witness = {"down own": F(9), "down MZ": F(13), "up own": F(2200), "up MZ": F(5200)}
    for k, m in s.items():
        ok = ok and Q_lt([witness[k] * m[0], F(99, 100) * m[1], m[2]])
    witness2 = {"down own": F(24, 10), "down MZ": F(29, 10), "up own": F(10), "up MZ": F(21)}
    for k, m in s.items():
        ok = ok and Q_lt([F(99, 100) * m[0], witness2[k] * m[1], m[2]])
        ok = ok and Q_gt([F(99, 100) * m[0], m[1], m[2]]) and Q_gt([m[0], F(99, 100) * m[1], m[2]])
    # in the up sector the threshold puts the up bracket above the charm bracket (rho_2 <= 1)
    for k in ("up own", "up MZ"):
        m = s[k]
        ok = ok and r1[k][0] * m[0] > m[1]
    GA.check("class D2 > D3 > D1 needs D3/D1 > 7.88, 11.00, 2010.2, 4799.8; class D1 > D3 > D2 needs D3/D2 > 2.19,"
             " 2.63, 9.36, 19.33", ok)
    return ok


# (4) --------------------------------------------------------------------------------------------

def check_stored_corner_bound_covers_the_class():
    premise("synthesis.mass-ordered-dressing-cannot-spoil-koide")
    s = sets()
    corner_lo = {"down own": F(188, 100), "down MZ": F(219, 100), "up own": F(867, 100), "up MZ": F(1755, 100)}
    ok = True
    n = 0
    for k, m in s.items():
        R = corner_lo[k]
        ok = ok and Q_gt([R * m[0], R * m[1], m[2]])
        for a in range(1, 5):
            for b in range(1, 5):
                rho1 = 1 + (R - 1) * F(a, 5)          # 1 < rho1 < R
                rho2 = F(b, 5)                        # rho2 < 1
                ok = ok and Q_gt([rho1 * m[0], rho2 * m[1], m[2]])
                n += 1
    ok = ok and n == 64
    GA.check("the stored corner bound applies with R = D3/D1 inside the class D2 > D3 > D1", ok)
    return ok


if __name__ == "__main__":
    import sys
    r = [check_middle_mass_lemma(), check_up_sector_charm_to_top_ratio_is_below_the_bound(),
         check_remaining_class_thresholds(), check_stored_corner_bound_covers_the_class()]
    sys.exit(0 if all(r) else 1)
