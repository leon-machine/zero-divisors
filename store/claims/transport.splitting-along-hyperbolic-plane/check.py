"""transport.splitting-along-hyperbolic-plane: exact checks.

V' = H0 + U' with H0 = span{e_0, e_1} (e_0^2 = +1, e_1^2 = -1) and U' spanned by further orthogonal
generators of square +1, -1 or 0 (degenerate forms included), k = dim U' from 0 to 3, nine forms.
Two hyperbolic pairs: v = (e_0 + e_1)/2, w0 = (e_0 - e_1)/2, and the rescaled v = e_0 + e_1,
w0 = (e_0 - e_1)/4; both have v^2 = w0^2 = 0 and v.w0 = 1/2.
  (1) {1, v, w0, v w0} x blades(U') has rank 2^(k+2) = dim Cl(V'), so it is a basis and every element
      has a unique expansion alpha + v beta + w0 gamma + v w0 delta, alpha..delta in Cl(U'); a sample
      element is expanded by exact solve and rebuilt.
  (2) Left multiplication by v is injective on Cl(U') (rank 2^k), while on all of Cl(V') it has rank
      2^(k+1), half: the injectivity is special to Cl(U').
The claim restates primer.splitting-along-hyperbolic-plane (equivalent_to), so no premise() call.
"""
from fractions import Fraction as F

import GA

FORMS = [(), (1,), (-1,), (0,), (1, -1), (0, 0), (1, 0, -1), (-1, -1, -1), (0, 1, 1)]
PAIRS = [(F(1, 2), F(1, 2)), (F(1), F(1, 4))]          # v = a(e0 + e1), w0 = b(e0 - e1)
SAMPLE = [((), 3), ((0,), -1), ((1,), 2), ((0, 1), 5), ((0, 2), 1), ((2, 3), -2), ((0, 1, 2), 7), ((1, 3, 4), 1)]


def setup(form, a, b):
    sq = (1, -1) + tuple(form)
    v = GA.scal(a, GA.add(GA.gen(0), GA.gen(1)))
    w0 = GA.scal(b, GA.sub(GA.gen(0), GA.gen(1)))
    ub = [tuple(i + 2 for i in bl) for bl in GA.all_blades(len(form))]
    return sq, v, w0, ub


def basis(sq, v, w0, ub):
    h = [GA.sc(1), v, w0, GA.mul(v, w0, sq)]
    return [GA.mul(x, {b: F(1)}, sq) for x in h for b in ub]


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def check_hyperbolic_pair_and_unique_expansion():
    ok = True
    for form in FORMS:
        k = len(form)
        blades = GA.all_blades(k + 2)
        for a, b in PAIRS:
            sq, v, w0, ub = setup(form, a, b)
            ok = ok and GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(w0, w0, sq))
            ok = ok and GA.dot(v, w0, sq) == F(1, 2)
            B = basis(sq, v, w0, ub)
            M = [[x.get(bl, F(0)) for x in B] for bl in blades]
            ok = ok and GA.field_rank(M) == 2 ** (k + 2)
            sigma = {bl: F(c) for bl, c in SAMPLE if all(i < k + 2 for i in bl)}
            co = GA.field_solve(M, coords(sigma, blades))
            n = 2 ** k
            parts = []
            for j in range(4):
                parts.append({bl: c for bl, c in zip(ub, co[j * n:(j + 1) * n]) if c != 0})
            al, be, ga, de = parts
            rebuilt = GA.add(al, GA.mul(v, be, sq), GA.mul(w0, ga, sq), GA.mul(GA.mul(v, w0, sq), de, sq))
            ok = ok and GA.eq(rebuilt, sigma)
            ok = ok and all(all(0 not in bl and 1 not in bl for bl in x) for x in parts)
    GA.check("{1, v, w0, v w0} x blades(U') is a basis of Cl(V') for nine forms U' (degenerate included)", ok)
    return ok


def check_left_multiplication_by_v_injective_on_cl_u():
    ok = True
    for form in FORMS:
        k = len(form)
        blades = GA.all_blades(k + 2)
        for a, b in PAIRS:
            sq, v, w0, ub = setup(form, a, b)
            imgs = [coords(GA.mul(v, {bl: F(1)}, sq), blades) for bl in ub]
            ok = ok and GA.field_rank(imgs) == 2 ** k
            allimgs = [coords(GA.mul(v, {bl: F(1)}, sq), blades) for bl in blades]
            ok = ok and GA.field_rank(allimgs) == 2 ** (k + 1)
    GA.check("v x is injective on Cl(U') (rank 2^k) and has half rank 2^(k+1) on Cl(V')", ok)
    return ok
