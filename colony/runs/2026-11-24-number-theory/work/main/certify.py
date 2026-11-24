import sys, time
from fractions import Fraction as F
from ivjet import *

K = 8


def thermal_jet(x):
    """Jet in delta of T = -r^2/24 + sum_a a/(exp(lam a) + 1) over an interval x of delta in (0, 1/2]."""
    d = jvar(x)
    u = jsub(d, jconst(F(1, 2)))
    r2 = jsub(jconst(1), jscale(12, jmul(u, u)))
    r = jsqrt(r2)
    lam = jmul(jscale(2, (PI, (0, 0), (0, 0))), jrecip(r))
    tot = jscale(F(-1, 24), r2)
    one = jconst(1)
    for k in range(K):
        for a in (jadd(jconst(k), d), jsub(jconst(k + 1), d)):
            tot = jadd(tot, jmul(a, jfermi(jmul(lam, a))))
    # tail: every term with a >= K and each of its first two derivatives is at most 11 M^2 a^3 exp(-lam a)
    M = max(P, lam[0][1], abs(lam[1][0]), abs(lam[1][1]), abs(lam[2][0]), abs(lam[2][1]))
    Mi = (M, M)
    rho = irecip(iexp((lam[0][0] * K, lam[0][0] * K)))       # upper bound of exp(-lam_lo K)
    bound = imul(imul(iv(F(223, 10) * (K + 1) ** 3), imul(Mi, Mi)), (0, rho[1]))[1]
    tail = (-bound, bound)
    return tuple(iadd(c, tail) for c in tot)


def sign_on(lo, hi, want, depth=0, stats=None):
    """Certify the sign of T on [lo, hi] (want = -1 or +1) by the mean-value form, bisecting when undecided."""
    stats[0] += 1
    mid = (lo + hi) / 2
    h = (hi - lo) / 2
    jm = thermal_jet(iv(mid))
    jx = thermal_jet(iv(lo, hi))
    spread = imul(jx[1], iv(-h, h))
    enc = iadd(jm[0], spread)
    if want < 0 and enc[1] < 0:
        return True
    if want > 0 and enc[0] > 0:
        return True
    if depth > 30:
        return False
    return sign_on(lo, mid, want, depth + 1, stats) and sign_on(mid, hi, want, depth + 1, stats)


def deriv_sign_on(lo, hi, order, want, pieces):
    ok = True
    for i in range(pieces):
        a = lo + (hi - lo) * i / pieces
        b = lo + (hi - lo) * (i + 1) / pieces
        j = thermal_jet(iv(a, b))[order]
        ok = ok and (j[1] < 0 if want < 0 else j[0] > 0)
    return ok


if __name__ == "__main__":
    print("pi in", to_float(PI))
    for d in (F(1, 4), F(1, 3), F(1, 2), F(3, 10)):
        j = thermal_jet(iv(d))
        print(d, [to_float(c) for c in j])
    t0 = time.time()
    regions = [("A", F(429, 2000), F(246, 1000), -1), ("C", F(254, 1000), F(3233, 10000), 1),
               ("E", F(3433, 10000), F(46, 100), -1)]
    for name, lo, hi, want in regions:
        st = [0]
        t = time.time()
        print(name, sign_on(lo, hi, want, 0, st), "intervals", st[0], "%.1fs" % (time.time() - t))
    t = time.time()
    print("B: T' > 0 near 1/4", deriv_sign_on(F(246, 1000), F(254, 1000), 1, 1, 16), "%.1fs" % (time.time() - t))
    print("D: T' < 0 near 1/3", deriv_sign_on(F(3233, 10000), F(3433, 10000), 1, -1, 20))
    print("F: T'' < 0 near 1/2", deriv_sign_on(F(46, 100), F(1, 2), 2, -1, 40))
    print("total %.1fs" % (time.time() - t0))
