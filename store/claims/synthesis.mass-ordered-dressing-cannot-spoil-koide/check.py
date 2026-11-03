"""synthesis.mass-ordered-dressing-cannot-spoil-koide: exact checks.

Q(m) = sum m_k / (sum sqrt m_k)^2. Square roots of data enter only through certified rational bounds
(integer square roots at scale 10^-12), and every inequality is decided with the bound that makes it
harder to pass.
(1) Homogeneity: Q(lam m) = Q(m), exactly, on rational square-coordinates s_k (m_k = s_k^2, lam = r^2).
(2) Monotonicity: with S1 = sum s_k, S2 = sum s_k^2, dQ/dm_j has the sign of S1 s_j - S2 ... exactly:
    m_j dQ/dm_j = (s_j / S1^3)(S1 s_j - S2); checked against the difference quotient of Q along s_j on
    rational samples, and the sufficient condition s_j <= s_max/3 => S1 s_j < S2 checked on samples.
    Then raising the lighter masses (factors >= 1, the heaviest fixed) lowers Q: checked on a rational grid.
(3) Data: Q > 2/3 for the down sector at the stored values (d, s at 2 GeV, b at m_b) and at the M_Z values,
    and for the up sector at the own-scale, the pole and the M_Z values (u, c and the M_Z set cited from
    memory: the 2008 running-mass table, flagged in the proof).
(4) The required ratio: Q(R m_1, R m_2, m_3) > 2/3 for R below R_lo and < 2/3 at R_hi, so the least ratio
    R* of heavy to light dressing that a Koide bracket needs lies in (R_lo, R_hi): down (stored) (1.88, 1.89),
    down (M_Z) (2.19, 2.20), up (own scale) (8.67, 8.68), up (M_Z) (17.5, 17.6).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

SCALE = 10 ** 12
TWO3 = F(2, 3)


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


def Q_exact_s(s):
    S1 = sum(s, F(0))
    return sum((x * x for x in s), F(0)) / (S1 * S1)


def Q_gt_two_thirds(m):
    """certified: 3 sum m > 2 (sum sqrt m)^2, using upper bounds on the roots."""
    hi = sum((sqrt_bounds(x)[1] for x in m), F(0))
    return 3 * sum(m, F(0)) > 2 * hi * hi


def Q_lt_two_thirds(m):
    lo = sum((sqrt_bounds(x)[0] for x in m), F(0))
    return 3 * sum(m, F(0)) < 2 * lo * lo


def corner(m, R):
    return [R * m[0], R * m[1], m[2]]


# data -------------------------------------------------------------------------------------------

def stored_down():
    md = F(1, 1000) * quantity("quantity.down-quark-mass")     # MeV -> GeV
    ms = F(1, 1000) * quantity("quantity.strange-quark-mass")
    mb = quantity("quantity.bottom-quark-mass")
    return [F(md), F(ms), F(mb)]


DOWN_MZ = [F(290, 100000), F(55, 1000), F(289, 100)]          # memory: running masses at M_Z (2008 table)
UP_MZ = [F(127, 100000), F(619, 1000), F(1717, 10)]           # memory: running masses at M_Z (2008 table)
UP_OWN_MEMORY = [F(216, 100000), F(1273, 1000)]               # memory: u at 2 GeV, c at m_c
C_POLE_MEMORY = F(167, 100)                                   # memory: charm pole mass


def up_own():
    return UP_OWN_MEMORY + [quantity("quantity.top-quark-mass")]


def up_pole():
    return [UP_OWN_MEMORY[0], C_POLE_MEMORY, quantity("quantity.top-quark-mass")]


# checks -----------------------------------------------------------------------------------------

def check_flavour_blind_dressing_keeps_q():
    premise("families.linear-conjecture-refuted-data")
    ok = True
    samples = [[F(1, 7), F(3, 5), F(11, 2)], [F(2, 9), F(1), F(13, 3)], [F(1, 100), F(9, 10), F(37, 3)]]
    want = [F(150089, 190969), F(803, 1250), F(13762909, 15784729)]
    ok = ok and [Q_exact_s(s) for s in samples] == want
    for s in samples:
        for r in (F(3, 2), F(7, 11), F(5)):
            ok = ok and Q_exact_s([r * x for x in s]) == Q_exact_s(s)
        ok = ok and Q_exact_s([F(2) * s[0], s[1], s[2]]) != Q_exact_s(s)
    GA.check("Q is unchanged by a common dressing factor and changed by a flavour-dependent one", ok)
    return ok


def check_raising_lighter_masses_lowers_q():
    premise("families.linear-conjecture-refuted-data")
    ok = True
    samples = [[F(1, 7), F(3, 5), F(11, 2)], [F(1, 20), F(1, 3), F(3)], [F(1, 100), F(9, 10), F(37, 3)]]
    corner_want = [F(155681, 239121), F(8509, 12769), F(3495409, 4507129)]
    ok = ok and [Q_exact_s([2 * x[0], 2 * x[1], x[2]]) for x in samples] == corner_want
    ok = ok and all(Q_exact_s([2 * x[0], 2 * x[1], x[2]]) < Q_exact_s(x) for x in samples)
    counted = 0
    for s in samples:
        S1 = sum(s, F(0))
        S2 = sum((x * x for x in s), F(0))
        for j in range(3):
            # derivative in m_j = s_j^2 through the s-derivative: dQ/ds_j = 2 (S1 s_j - S2)/S1^3
            h = F(1, 10 ** 9)
            sp = list(s)
            sp[j] += h
            dq = (Q_exact_s(sp) - Q_exact_s(s)) / h
            exact = 2 * (S1 * s[j] - S2) / S1 ** 3
            ok = ok and abs(dq - exact) < F(1, 10 ** 6)
        smax = max(s)
        for j in range(3):
            if 3 * s[j] <= smax:
                ok = ok and S1 * s[j] < S2
        ok = ok and S1 * smax > S2            # the heaviest always raises Q
        # grid: lighter two raised by factors r^2 in [1, 4] (r in [1, 2]), heaviest fixed, lights stay <= s_max/3
        base = Q_exact_s(s)
        for a in range(0, 5):
            for b in range(0, 5):
                ra, rb = 1 + F(a, 4), 1 + F(b, 4)
                t = [ra * s[0], rb * s[1], s[2]]
                if 3 * max(t[0], t[1]) <= s[2]:
                    counted += 1
                    q = Q_exact_s(t)
                    ok = ok and q <= base and (q < base or (a == 0 and b == 0))
    ok = ok and counted == 75
    GA.check("m_j dQ/dm_j has the sign of S1 s_j - S2; raising the lighter masses lowers Q", ok)
    return ok


def check_quark_quotients_exceed_two_thirds():
    premise("families.linear-conjecture-refuted-data")
    sets = {"down stored": stored_down(), "down MZ": DOWN_MZ, "up own": up_own(), "up pole": up_pole(),
            "up MZ": UP_MZ}
    ok = all(Q_gt_two_thirds(m) for m in sets.values())
    # and the stated values to three places
    want = {"down stored": (F(731, 1000), F(732, 1000)), "down MZ": (F(745, 1000), F(746, 1000)),
            "up own": (F(848, 1000), F(849, 1000)), "up pole": (F(831, 1000), F(832, 1000)),
            "up MZ": (F(888, 1000), F(889, 1000))}
    for k, (lo, hi) in want.items():
        m = sets[k]
        rlo = sum((sqrt_bounds(x)[0] for x in m), F(0))
        rhi = sum((sqrt_bounds(x)[1] for x in m), F(0))
        q_hi, q_lo = sum(m, F(0)) / (rlo * rlo), sum(m, F(0)) / (rhi * rhi)
        ok = ok and lo < q_lo and q_hi < hi
    GA.check("Q > 2/3 for both quark sectors at every mass definition used (0.731 to 0.889)", ok)
    return ok


def check_required_heavy_to_light_ratio():
    premise("families.linear-conjecture-refuted-data")
    cases = {"down stored": (stored_down(), F(188, 100), F(189, 100)),
             "down MZ": (DOWN_MZ, F(219, 100), F(220, 100)),
             "up own": (up_own(), F(867, 100), F(868, 100)),
             "up MZ": (UP_MZ, F(175, 10), F(176, 10))}
    ok = True
    for k, (m, rlo, rhi) in cases.items():
        ok = ok and Q_gt_two_thirds(corner(m, rlo)) and Q_lt_two_thirds(corner(m, rhi))
        # the lemma's sufficient condition holds at the corner: R m_2 <= m_3 / 9
        ok = ok and 9 * rhi * m[1] <= m[2]
    GA.check("a Koide bracket needs heavy-to-light dressing ratios in (1.88, 1.89), (2.19, 2.20), (8.67, 8.68), (17.5, 17.6)", ok)
    return ok


if __name__ == "__main__":
    import sys
    r = [check_flavour_blind_dressing_keeps_q(), check_raising_lighter_masses_lowers_q(),
         check_quark_quotients_exceed_two_thirds(), check_required_heavy_to_light_ratio()]
    sys.exit(0 if all(r) else 1)
