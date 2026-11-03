"""odd-extensions.volume-element-odd-dimension: exact checks.

For every signature (p, q) with n = p + q odd and n <= 11 (42 signatures) the volume element
omega = e_1 ... e_n is shown central (it commutes with every generator, hence with the algebra
they generate) and its square is computed with the exact blade engine and compared with
(-1)^(n(n-1)/2 + q). For n = 5 the six signatures are checked against the special form
omega^2 = (-1)^q with the values written out. As a control, for n even omega anticommutes with
every generator, so the parity hypothesis is not idle.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (self-contained lemma: no premises)


def omega_of(n):
    return {tuple(range(n)): F(1)}


def check_odd_volume_element_central_with_square():
    ok = True
    count = 0
    for n in range(1, 12, 2):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p, q)
            w = omega_of(n)
            ok = ok and all(GA.commutes(GA.gen(i), w, sq) for i in range(n))
            ok = ok and GA.mul(w, w, sq) == {(): F((-1) ** (n * (n - 1) // 2 + q))}
            count += 1
    ok = ok and count == 42
    GA.check("omega central in Cl(p,q), n odd, with omega^2 = (-1)^(n(n-1)/2 + q), n <= 11", ok)
    return ok


def check_n5_square_is_minus_one_to_q():
    # (p, q) -> omega^2 for n = 5, written out from (-1)^q
    stated = {(5, 0): 1, (4, 1): -1, (3, 2): 1, (2, 3): -1, (1, 4): 1, (0, 5): -1}
    ok = True
    for (p, q), s in stated.items():
        sq = GA.sig(p, q)
        w = omega_of(p + q)
        ok = ok and p + q == 5 and GA.eq(GA.mul(w, w, sq), GA.sc(s))
        ok = ok and all(GA.commutes(GA.gen(i), w, sq) for i in range(5))
    GA.check("n = 5: omega central with omega^2 = (-1)^q", ok)
    return ok


def check_even_control_not_central():
    ok = True
    count = 0
    for n in range(2, 11, 2):
        for p in range(n + 1):
            sq = GA.sig(p, n - p)
            w = omega_of(n)
            ok = ok and all(GA.anticommutes(GA.gen(i), w, sq) for i in range(n))
            count += 1
    ok = ok and count == 35
    GA.check("control: for n even omega anticommutes with every generator", ok)
    return ok
