"""primer.sign: exact checks.

omega = e_1 ... e_n in Cl(p,q) is squared with the exact blade engine for every signature with
1 <= n = p + q <= 10 (65 signatures) and compared with both closed forms,
(-1)^(n(n-1)/2) (-1)^q and (-1)^((p-q)(p-q-1)/2); the "in particular" clause (omega^2 = +1 iff
p - q = 0 or 1 mod 4) is tested on the same range (32 of the 65 have omega^2 = +1, counted by hand
from p = n/2 mod 2 for n even and p = (n+1)/2 mod 2 for n odd). The equality of the two closed forms
rests on the polynomial identity n(n-1)/2 + q - (p-q)(p-q-1)/2 = 2pq, tested at every integer point
of a 21 x 21 grid (degree 2 in each variable, so the grid determines it).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (self-contained lemma: no premises)


def omega_sq(p, q):
    n = p + q
    w = {tuple(range(n)): F(1)}
    return GA.mul(w, w, GA.sig(p, q))


def check_omega_square():
    ok = True
    count = 0
    plus = 0
    for n in range(1, 11):
        for p in range(n + 1):
            q = n - p
            s = omega_sq(p, q)
            a = (-1) ** (n * (n - 1) // 2) * (-1) ** q
            b = (-1) ** ((p - q) * (p - q - 1) // 2)
            ok = ok and s == {(): F(a)} and a == b
            ok = ok and ((a == 1) == ((p - q) % 4 in (0, 1)))
            plus += a == 1
            count += 1
    ok = ok and count == 65 and plus == 32
    GA.check("omega^2 = (-1)^(n(n-1)/2)(-1)^q = (-1)^((p-q)(p-q-1)/2) for 1 <= n <= 10", ok)
    return ok


def check_exponent_parity_identity():
    # n(n-1)/2 + q - (p-q)(p-q-1)/2 = 2pq, an even integer, for all integers p, q
    ok = True
    pts = 0
    for p in range(-10, 11):
        for q in range(-10, 11):
            n = p + q
            e1 = n * (n - 1) // 2 + q
            e2 = (p - q) * (p - q - 1) // 2
            ok = ok and e1 - e2 == 2 * p * q and (e1 - e2) % 2 == 0
            pts += 1
    ok = ok and pts == 441
    GA.check("the two exponents of omega^2 agree mod 2 on a 21 x 21 integer grid", ok)
    return ok
