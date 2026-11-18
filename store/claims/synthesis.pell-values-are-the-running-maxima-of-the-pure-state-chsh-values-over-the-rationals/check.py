"""synthesis.pell-values-are-the-running-maxima-of-the-pure-state-chsh-values-over-the-rationals: exact checks.

Pure-state values of the sector are the rationals P/Q with 8 Q^2 - P^2 = R^2 (the stored circle X^2 + Y^2 = 8).
Integer arithmetic only.  The Clifford part (the circle is the set of pure states of the corner of Cl(2,2)) is the
stored theorem's; one of its states is rebuilt here to tie the integers to the algebra.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QMAX = 1000           # all pure values with denominator up to this bound are enumerated
PELL_STEPS = 14       # Pell pairs (x_n, Q_n) checked for the growth bound
SQ22 = (1, -1, 1, -1)


def isqrt(n):
    if n < 0:
        return -1
    x = int(n)
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def igcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def pell(nsteps):
    out = [(1, 1)]
    for _ in range(nsteps):
        x, q = out[-1]
        out.append((3 * x + 4 * q, 2 * x + 3 * q))
    return out


def pure_values(qmax):
    """All (P, Q, R) with P > 0, Q >= 1, gcd(P, Q) = 1, 8 Q^2 - P^2 = R^2, R > 0, Q <= qmax."""
    out = []
    for q in range(1, qmax + 1):
        top = isqrt(8 * q * q)
        for p in range(1, top + 1):
            d = 8 * q * q - p * p
            r = isqrt(d)
            if r > 0 and r * r == d and igcd(p, q) == 1:
                out.append((p, q, r))
    return out


def check_deficit_of_a_pure_value_is_one_or_at_least_seven():
    premise("synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records")
    vals = pure_values(QMAX // 4)
    assert len(vals) == 79
    for p, q, r in vals:
        assert p % 2 == 0 and r % 2 == 0 and q % 2 == 1
        a, b = p // 2, r // 2
        assert a % 2 == 1 and b % 2 == 1 and a * a + b * b == 2 * q * q
        assert b == 1 or b >= 7
        m = b
        f = 3
        while m > 1:
            if m % f == 0:
                assert f % 8 in (1, 7)
                m //= f
            else:
                f += 2
        if b == 1:
            assert a * a - 2 * q * q == -1
    # 2 is not a square modulo 3 or 5, and is one modulo 7
    assert all((t * t - 2) % 3 != 0 for t in range(3)) and all((t * t - 2) % 5 != 0 for t in range(5))
    assert (3 * 3 - 2) % 7 == 0
    return True


def check_pell_denominators_grow_by_less_than_the_square_root_of_thirty_four():
    premise("synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records")
    pp = pell(PELL_STEPS)
    assert pp[:4] == [(1, 1), (7, 5), (41, 29), (239, 169)]
    for (x, q), (x1, q1) in zip(pp, pp[1:]):
        assert x * x - 2 * q * q == -1
        assert q1 * q1 < 34 * q * q and q1 > q
        assert x * x < 2 * q * q
    # 12 sqrt 2 < 17, so (3 + 2 sqrt 2)^2 = 17 + 12 sqrt 2 < 34; and 4 * 34 < 4 * 7^2
    assert 12 * 12 * 2 < 17 * 17 and 4 * 34 < 4 * 7 * 7
    return True


def check_running_maxima_of_pure_values_are_the_pell_values():
    premise("synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records")
    vals = pure_values(QMAX)
    pp = [(x, q) for x, q in pell(PELL_STEPS) if q <= QMAX]
    assert [q for x, q in pp] == [1, 5, 29, 169, 985]
    pellset = set((2 * x, q) for x, q in pp)
    # every value that is not a Pell value is exceeded by the Pell value of the largest smaller denominator
    for p, q, r in vals:
        if (p, q) in pellset:
            continue
        x, qn = [t for t in pp if t[1] < q][-1]
        assert F(2 * x, qn) > F(p, q)
        assert 4 * q * q < 34 * 4 * qn * qn and r * r >= 196
    # running maxima by increasing denominator
    best = None
    records = []
    for q in range(1, QMAX + 1):
        here = [F(p, q) for p, q_, r in vals if q_ == q]
        if not here:
            continue
        top = max(here)
        if best is None or top > best:
            best = top
            records.append((top.numerator, top.denominator))
    assert records == [(2, 1), (14, 5), (82, 29), (478, 169), (2786, 985)]
    return True


def check_first_pell_value_is_the_value_of_the_even_state():
    premise("synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records")
    e1, f1, e2, f2 = (GA.gen(i) for i in range(4))
    one = GA.sc(F(1))

    def prod(*xs):
        r = one
        for x in xs:
            r = GA.mul(r, x, SQ22)
        return {b: c for b, c in r.items() if c != 0}

    p1, p2 = prod(f1, e1), prod(f2, e2)
    a1, a2, b1, b2 = e1, p1, prod(e2, p1), p2
    c = GA.add(prod(a1, b1), prod(a1, b2), prod(a2, b1), GA.neg(prod(a2, b2)))
    rho0 = GA.scal(F(1, 4), prod(GA.add(one, prod(a1, b1)), GA.sub(one, prod(a2, b2))))
    rho0 = {b: v for b, v in rho0.items() if v != 0}
    assert prod(rho0, rho0) == rho0
    assert 4 * prod(rho0, c).get((), F(0)) == 2
    return True
