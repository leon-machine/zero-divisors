"""R1: Koide middle-mass bound and class thresholds, recomputed with certified rational square-root bounds.

Route different from the proposal: (a) the bound from the trigonometric parametrisation
sqrt(b_k) = mu (1 + sqrt2 cos(theta + 2 pi k / 3)) is reproduced symbolically at the degenerate point theta = 0,
where sqrt(b_2)/sqrt(b_3) = (1 - 1/sqrt2)/(1 + sqrt2) = 3/sqrt2 - 2 (checked in Q(sqrt2) exactly);
(b) every threshold is bracketed by interval arithmetic on Q with isqrt bounds, by bisection to 1e-6, then
the stated decimal brackets are tested.
"""
from fractions import Fraction as F
from math import isqrt

SCALE = 10 ** 30


def sqrt_bounds(x):
    """rational lo <= sqrt(x) <= hi for a positive Fraction x"""
    n = x.numerator * SCALE * SCALE // x.denominator
    r = isqrt(n)
    return F(r, SCALE), F(r + 1, SCALE)


def Q_bounds(m):
    S2 = sum(m)
    lo = sum(sqrt_bounds(x)[0] for x in m)
    hi = sum(sqrt_bounds(x)[1] for x in m)
    return S2 / hi ** 2, S2 / lo ** 2


def sign_vs_two_thirds(m):
    lo, hi = Q_bounds(m)
    if lo > F(2, 3):
        return 1
    if hi < F(2, 3):
        return -1
    return 0


def crossing(f, a, b, tol=F(1, 10 ** 6)):
    """f decreasing through 2/3 on [a, b]: return a bracket [lo, hi] of the crossing"""
    assert sign_vs_two_thirds(f(a)) == 1 and sign_vs_two_thirds(f(b)) == -1
    while b - a > tol:
        c = (a + b) / 2
        s = sign_vs_two_thirds(f(c))
        if s == 1:
            a = c
        elif s == -1:
            b = c
        else:
            break
    return float(a), float(b)


SETS = {
    "down own": (F("0.00470"), F("0.0935"), F("4.18")),
    "down MZ": (F("0.00290"), F("0.055"), F("2.89")),
    "up own": (F("0.00216"), F("1.2730"), F("172.57")),
    "up MZ": (F("0.00127"), F("0.619"), F("171.7")),
}


def q2_check():
    # elements a + b sqrt2 as pairs; (1 - 1/sqrt2) = 1 - sqrt2/2 ; (1 + sqrt2); target 3/sqrt2 - 2 = -2 + (3/2) sqrt2
    def mul(x, y):
        return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
    t = (F(-2), F(3, 2))
    lhs = mul(t, (F(1), F(1)))            # t (1 + sqrt2)
    assert lhs == (F(1), F(-1, 2))        # = 1 - sqrt2/2
    t2 = mul(t, t)
    assert t2 == (F(17, 2), F(-6))        # 17/2 - 6 sqrt2
    # degenerate Koide triple (t^2, t^2, 1): Q = (2 t^2 + 1)/(2 t + 1)^2 = 2/3 <=> 2 t^2 + 8 t - 1 = 0
    val = (2 * t2[0] + 8 * t[0] - 1, 2 * t2[1] + 8 * t[1])
    assert val == (0, 0)
    return t2


def main():
    t2 = q2_check()
    print("t*^2 =", t2[0], "+", t2[1], "sqrt2; 2t^2 + 8t - 1 = 0 exactly in Q(sqrt2)")
    # rational test r < 17/2 - 6 sqrt2  <=>  r < 17/2 and (17/2 - r)^2 > 72
    lt = lambda r: r < F(17, 2) and (F(17, 2) - r) ** 2 > 72
    for name, (m1, m2, m3) in SETS.items():
        r = m2 / m3
        print(f"{name}: m2/m3 = {float(r):.6f}  below t*^2: {lt(r)}")
    for name in ("up own", "up MZ"):
        m1, m2, m3 = SETS[name]
        f = lambda rho: (rho * m2, rho * m2, m3)
        print(f"  {name}: order-kept threshold D_t/D_c crossing in", crossing(f, F(1), F(9)))
    for name, (m1, m2, m3) in SETS.items():
        R1 = crossing(lambda R: (R * m1, m2, m3), F(1), m3 / (9 * m1))
        R2 = crossing(lambda R: (m1, R * m2, m3), F(1), m3 / (9 * m2))
        Rs = crossing(lambda R: (R * m1, R * m2, m3), F(1), m3 / (9 * m2))
        print(f"{name}: R1 in {R1}, R2 in {R2}, R* in {Rs}")
        if name.startswith("up"):
            print(f"   R1 m_u = {R1[0] * float(m1):.4f} GeV vs m_c = {float(m2)}")


if __name__ == "__main__":
    main()
