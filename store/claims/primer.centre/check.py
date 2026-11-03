"""primer.centre: exact checks.

For every signature (p, q) with 1 <= n = p + q <= 6 the centre of Cl(p, q) is computed by exact
linear algebra over the rationals, as the kernel of x -> ([e_1, x], ..., [e_n, x]) on the full
2^n-dimensional algebra (the generators generate, so this is the centre), without assuming the
blade basis diagonalises the map. The kernel is compared with R 1 (n even) and R 1 + R omega
(n odd). A second check confirms, for 6 <= n <= 9 (p = 0, 3, 6, 9), the blade-level form of the same statement:
the only blades commuting with every generator are 1, and omega when n is odd.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (self-contained lemma: no premises)


def centre_basis(p, q):
    n = p + q
    sq = GA.sig(p, q)
    blades = GA.all_blades(n)
    N = len(blades)
    rows = []
    for i in range(n):
        cols = []
        for b in blades:
            c = GA.sub(GA.mul(GA.gen(i), {b: F(1)}, sq), GA.mul({b: F(1)}, GA.gen(i), sq))
            cols.append([c.get(bb, F(0)) for bb in blades])
        for r in range(N):
            rows.append([cols[j][r] for j in range(N)])
    ker = GA.field_kernel(rows)
    return blades, ker


def check_centre_by_linear_algebra():
    ok = True
    count = 0
    for n in range(1, 7):
        for p in range(n + 1):
            q = n - p
            blades, ker = centre_basis(p, q)
            want = [()] if n % 2 == 0 else [(), tuple(range(n))]
            ok = ok and len(ker) == len(want)
            # the kernel is spanned by the wanted blades: stacking them on it leaves the rank unchanged
            wv = [[F(1) if b == w else F(0) for b in blades] for w in want]
            ok = ok and GA.field_rank(ker + wv) == len(want)
            count += 1
    ok = ok and count == 27
    GA.check("centre of Cl(p,q) is R (n even) or R + R omega (n odd), 1 <= n <= 6", ok)
    return ok


def check_central_blades_higher_n():
    ok = True
    count = 0
    for n in range(6, 10):
        for p in range(0, n + 1, 3):
            q = n - p
            sq = GA.sig(p, q)
            cb = [b for b in GA.all_blades(n)
                  if all(GA.commutes(GA.gen(i), {b: F(1)}, sq) for i in range(n))]
            want = [()] if n % 2 == 0 else [(), tuple(range(n))]
            ok = ok and cb == want
            count += 1
    ok = ok and count == 13
    GA.check("central blades of Cl(p,q) for 6 <= n <= 9 are 1 and, for n odd, omega", ok)
    return ok
