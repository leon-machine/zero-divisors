"""transport.centre: exact checks.

(1) Full linear algebra, every nondegenerate (p,q) with 1 <= n = p + q <= 6: the solution space of
x e_i = e_i x for all generators (2^n unknown coefficients) is computed as a kernel; it has dimension
1 (spanned by 1) for n even and 2 (spanned by 1 and omega = e_1 ... e_n) for n odd.
(2) Blade-wise, every (p,q) with n <= 9: conjugation by an invertible generator sends a blade to +- itself,
so the centre is spanned by the central blades; these are exactly {1} for n even and {1, omega} for
n odd (a blade e_I commutes with e_i iff |I| - [i in I] is even, so for 0 < |I| < n some generator
anticommutes with it).
"""
from fractions import Fraction as F
import GA


def centre_kernel(sq):
    n = len(sq)
    bl = GA.all_blades(n)
    cols = []
    for b in bl:
        x = {b: F(1)}
        col = []
        for i in range(n):
            d = GA.sub(GA.mul(x, GA.gen(i), sq), GA.mul(GA.gen(i), x, sq))
            col.extend(d.get(c, F(0)) for c in bl)
        cols.append(col)
    rows = [list(r) for r in zip(*cols)]
    return bl, GA.field_kernel(rows)


def check_centre_by_kernel():
    ok = True
    for n in range(1, 7):
        for p in range(n + 1):
            sq = GA.sig(p, n - p)
            bl, ker = centre_kernel(sq)
            supp = sorted({bl[j] for v in ker for j in range(len(bl)) if v[j] != 0})
            if n % 2 == 0:
                ok = ok and len(ker) == 1 and supp == [()]
            else:
                ok = ok and len(ker) == 2 and supp == [(), tuple(range(n))]
    GA.check("centre = R (n even), R + R omega (n odd), by kernel computation, all (p,q), n <= 6", ok)
    return ok


# Sample signatures (p, q): every signature with 1 <= n = p + q <= 9.
SIGNATURES = [(p, n - p) for n in range(1, 10) for p in range(n + 1)]


def unit_blade(b):
    return {b: F(1)}


def check_centre_blade_wise():
    ok = True
    for p, q in SIGNATURES:
        n = p + q
        sq = GA.sig(p, q)
        central = [b for b in GA.all_blades(n)
                   if all(GA.commutes(unit_blade(b), GA.gen(i), sq) for i in range(n))]
        want = [()] if n % 2 == 0 else [(), tuple(range(n))]
        ok = ok and central == want
    GA.check("central blades are 1 (n even) and 1, omega (n odd), all (p,q), n <= 9", ok)
    return ok
