"""primer.splitting-along-hyperbolic-plane: exact checks.

V' = H0 perp U' with H0 the hyperbolic plane of a hyperbolic pair (v, w0) and U' any diagonal form,
degenerate included (generators of square +1, -1 and 0).
(1) v and w0 are null with v w0 + w0 v = 1, for the standard pair (e0 + e1)/2, (e0 - e1)/2 in the
(1,1) plane and for a rescaled pair (e0 + e1), (e0 - e1)/4; {1, v, w0, v w0} spans Cl(H0) (rank 4).
(2) The 4 * 2^k products {1, v, w0, v w0} x (blades of U') are linearly independent and span
Cl(V') (rank 2^(k+2) = dim Cl(V')), so the expansion sigma = alpha + v beta + w0 gamma + v w0 delta
with alpha, ..., delta in Cl(U') exists and is unique; a sample element is decomposed and
reassembled.
(3) Left multiplication by v is injective on Cl(U'): the images v b of the 2^k blades of U' have
rank 2^k, for every U' in the list.
"""
from fractions import Fraction as F
from itertools import combinations
import GA

# U' signatures (squares of the generators after the plane): definite, indefinite, degenerate
U_FORMS = [(), (1,), (-1,), (0,), (1, -1), (0, 0), (1, 0, -1), (-1, -1, 0), (1, 1, 0, 0)]
PAIRS = [(F(1, 2), F(1, 2)), (F(1), F(1, 4))]   # (scale of e0 + e1, scale of e0 - e1)


def blades_of(idx):
    out = []
    for k in range(len(idx) + 1):
        out.extend(combinations(idx, k))
    return out


def coords(x, n):
    return [x.get(b, F(0)) for b in GA.all_blades(n)]


def rank(xs, n):
    return GA.rank_of_vectors([coords(x, n) for x in xs])


def setup(uform, pair):
    sq = (1, -1) + tuple(uform)
    a, b = pair
    v = GA.scal(a, GA.add(GA.gen(0), GA.gen(1)))
    w0 = GA.scal(b, GA.sub(GA.gen(0), GA.gen(1)))
    return sq, v, w0


def check_hyperbolic_pair_and_plane_basis():
    ok = True
    for pair in PAIRS:
        sq, v, w0 = setup((), pair)
        ok = ok and GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(w0, w0, sq))
        ok = ok and GA.eq(GA.add(GA.mul(v, w0, sq), GA.mul(w0, v, sq)), GA.sc(1))
        hb = [GA.sc(1), v, w0, GA.mul(v, w0, sq)]
        ok = ok and rank(hb, 2) == 4
    GA.check("hyperbolic pair: null, v w0 + w0 v = 1, {1, v, w0, v w0} a basis of Cl(H0)", ok)
    return ok


def check_unique_split_expansion():
    ok = True
    for uform in U_FORMS:
        k = len(uform)
        n = k + 2
        for pair in PAIRS:
            sq, v, w0 = setup(uform, pair)
            hb = [GA.sc(1), v, w0, GA.mul(v, w0, sq)]
            ub = [{b: F(1)} for b in blades_of(range(2, n))]
            prods = [GA.mul(h, u, sq) for h in hb for u in ub]
            ok = ok and len(prods) == 2 ** n and rank(prods, n) == 2 ** n
        # decompose and reassemble a sample element (standard pair)
        sq, v, w0 = setup(uform, PAIRS[0])
        hb = [GA.sc(1), v, w0, GA.mul(v, w0, sq)]
        ub = [{b: F(1)} for b in blades_of(range(2, n))]
        prods = [GA.mul(h, u, sq) for h in hb for u in ub]
        sigma = {b: F(len(b) + 1, 3 + i) for i, b in enumerate(GA.all_blades(n))}
        M = [[coords(p, n)[r] for p in prods] for r in range(2 ** n)]
        sol = GA.field_solve(M, coords(sigma, n))
        back = GA.add(*[GA.scal(c, p) for c, p in zip(sol, prods)])
        ok = ok and GA.eq(back, sigma)
    GA.check("{1, v, w0, v w0} x Cl(U') is a basis of Cl(V') for every U', degenerate included", ok)
    return ok


def check_left_mult_by_v_injective():
    ok = True
    for uform in U_FORMS:
        k = len(uform)
        n = k + 2
        for pair in PAIRS:
            sq, v, w0 = setup(uform, pair)
            imgs = [GA.mul(v, {b: F(1)}, sq) for b in blades_of(range(2, n))]
            ok = ok and rank(imgs, n) == 2 ** k
        # but v is a zero divisor on Cl(V'): v kills v Cl(U'), so injectivity is special to Cl(U')
        sq, v, w0 = setup(uform, PAIRS[0])
        full = [GA.mul(v, {b: F(1)}, sq) for b in GA.all_blades(n)]
        ok = ok and rank(full, n) == 2 ** (n - 1)
    GA.check("left multiplication by v is injective on Cl(U') (rank 2^k), half rank on Cl(V')", ok)
    return ok
