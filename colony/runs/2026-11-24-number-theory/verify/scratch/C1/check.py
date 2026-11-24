"""synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-quarter-turn

Exact checks.  The ring of clause (6) of the stored cohomology theorem is A_n = Z[chi]/(chi^4 - 1, (chi - 1)^(n+1)).
With sigma = chi - 1 it is Z[sigma]/((1 + sigma)^4 - 1, sigma^(n+1)).  The ring of the quarter turn is Z[J],
J = e_1 e_2 in Cl(2,0), J^2 = -1.  Everything is integer or Fraction arithmetic.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ2 = (1, 1)
ONE = GA.sc(F(1))
J = GA.mul(GA.gen(0), GA.gen(1), SQ2)


def binom(n, k):
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


def reduce_mod_f(p, N):
    """Reduce an integer polynomial in sigma (list, low degree first) modulo f = (1 + sigma)^N - 1, monic."""
    f = [binom(N, k) for k in range(N + 1)]
    f[0] = 0
    p = p[:]
    while len(p) > N:
        c = p[-1]
        d = len(p) - 1 - N
        if c != 0:
            for k in range(N + 1):
                p[d + k] -= c * f[k]
        p.pop()
    return p + [0] * (N - len(p))


def times_sigma(p, N):
    return reduce_mod_f([0] + p, N)


def hermite(rows):
    """Row echelon form over Z of an integer matrix (list of rows); returns the nonzero rows."""
    rows = [r[:] for r in rows if any(r)]
    out = []
    ncol = len(rows[0]) if rows else 0
    col = 0
    while rows and col < ncol:
        rows = [r for r in rows if any(r)]
        piv = [r for r in rows if r[col] != 0]
        if not piv:
            col += 1
            continue
        while len(piv) > 1:
            piv.sort(key=lambda r: abs(r[col]))
            a = piv[0]
            for r in piv[1:]:
                q = r[col] // a[col]
                for k in range(ncol):
                    r[k] -= q * a[k]
            piv = [r for r in piv if r[col] != 0]
        a = piv[0]
        out.append(a[:])
        rows = [r for r in rows if r is not a and any(r)]
        col += 1
    return out


def in_lattice(ech, t):
    t = t[:]
    for r in ech:
        col = next(k for k in range(len(r)) if r[k] != 0)
        if t[col] % r[col] != 0:
            return False
        q = t[col] // r[col]
        for k in range(len(t)):
            t[k] -= q * r[k]
    return not any(t)


def order_of_sign_line(a, n, cap=80):
    """Least m with 2^m (1 - chi^(N/2)) = 0 in Z[chi]/(chi^N - 1, (chi - 1)^(n+1)), N = 2^a."""
    N = 2 ** a
    gen = reduce_mod_f([0] * n + [1], N)          # sigma^(n+1)
    rows = []
    g = gen
    for _ in range(N):
        rows.append(g)
        g = times_sigma(g, N)
    ech = hermite(rows)
    w = [binom(N // 2, k) for k in range(N // 2 + 1)]    # (1 + sigma)^(N/2) - 1
    w[0] = 0
    w = reduce_mod_f(w, N)
    for m in range(cap):
        if in_lattice(ech, [(2 ** m) * c for c in w]):
            return m
    return None


def ceil_div(n, d):
    return -((-n) // d)


def check_two_is_the_quarter_turn_times_the_square_of_j_minus_one():
    premise("std-algebra.complex-numbers")
    ok = True
    ok = ok and GA.eq(GA.mul(J, J, SQ2), GA.sc(F(-1)))
    Jm = GA.sub(J, ONE)
    sqr = GA.mul(Jm, Jm, SQ2)
    ok = ok and GA.eq(sqr, GA.scal(F(-2), J))
    ok = ok and GA.eq(GA.mul(J, sqr, SQ2), GA.sc(F(2)))
    # the norm (J - 1)(J - 1)~ is 2, so J - 1 is not invertible in Z[J]
    ok = ok and GA.eq(GA.mul(Jm, GA.reverse(Jm), SQ2), GA.sc(F(2)))
    # least m with (J - 1)^n dividing 2^m in Z[J] is ceil(n/2), n = 1..40
    inv = GA.scal(F(-1, 2), GA.add(J, ONE))               # (J - 1)^{-1} = -(J + 1)/2
    ok = ok and GA.eq(GA.mul(Jm, inv, SQ2), ONE)
    count = 0
    for n in range(1, 41):
        den = ONE
        for _ in range(n):
            den = GA.mul(den, inv, SQ2)
        m = 0
        while True:
            x = GA.scal(F(2) ** m, den)
            if all(c.denominator == 1 for c in x.values()):
                break
            m += 1
        ok = ok and m == ceil_div(n, 2)
        count += 1
    ok = ok and count == 40
    GA.check("2 = J (J - 1)^2, (J - 1)(J - 1)~ = 2, and 2^m is divisible by (J - 1)^n exactly from m = ceil(n/2)", ok)
    return ok


def check_order_of_one_minus_chi_squared_in_the_stored_k_ring_is_two_to_the_ceiling_of_n_over_two():
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    ok, count = True, 0
    for n in range(1, 41):
        m = order_of_sign_line(2, n)
        ok = ok and m == ceil_div(n, 2) and m == (n + 1) // 2
        count += 1
    ok = ok and count == 40
    # the relation used by the proof: in the ring, 2 (chi^2 - 1) = -4 sigma^2 at n = 2, and 4 sigma^2 = 0 there
    N = 4
    sig2 = reduce_mod_f([0, 0, 1], N)
    gen = reduce_mod_f([0, 0, 0, 1], N)
    rows, g = [], gen
    for _ in range(N):
        rows.append(g)
        g = times_sigma(g, N)
    ech = hermite(rows)
    ok = ok and in_lattice(ech, [4 * c for c in sig2]) and not in_lattice(ech, [2 * c for c in sig2])
    GA.check("in Z[chi]/(chi^4 - 1, (chi - 1)^(n+1)) the order of 1 - chi^2 is 2^ceil(n/2) for n = 1..40", ok)
    return ok


def check_order_of_the_sign_line_for_the_half_turn_and_the_eighth_turn():
    ok, count = True, 0
    for n in range(1, 25):
        ok = ok and order_of_sign_line(1, n) == n            # real projective spaces: 2^n
        ok = ok and order_of_sign_line(3, n) == ceil_div(n, 4)
        count += 2
    for n in range(1, 13):
        ok = ok and order_of_sign_line(4, n) == ceil_div(n, 8)
        count += 1
    ok = ok and count == 60
    GA.check("the same order for chi^2, chi^8 and chi^16 = 1: 2^n, 2^ceil(n/4), 2^ceil(n/8)", ok)
    return ok


def check_rung_bound_for_every_n_against_the_stored_bounds():
    premise("synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height")
    ok = True
    for n in range(1, 41):
        new = 1 + ceil_div(n, 2)
        old = 1 + n // 2
        ok = ok and new >= old and (new == old) == (n % 2 == 0)
    # the stored instances: L^7(4), L^11(4), L^15(4) need at least 3, 4, 5 rungs
    ok = ok and [1 + ceil_div(n, 2) for n in (3, 5, 7)] == [3, 4, 5]
    # n = 1: the bound 2, attained on the L(4,1) wall with an indefinite side (stored)
    ok = ok and 1 + ceil_div(1, 2) == 2
    GA.check("1 + ceil(n/2) improves the stored 1 + floor(n/2) exactly at odd n and reproduces 3, 4, 5", ok)
    return ok
