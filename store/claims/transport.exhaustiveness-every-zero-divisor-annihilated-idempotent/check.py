"""transport.exhaustiveness-every-zero-divisor-annihilated-idempotent: exact checks.

Fourteen sample nonzero zero divisors a in twelve nondegenerate signatures (simple and split), in GA.py:
  (1) The right annihilator {y : a y = 0} and the left annihilator {y : y a = 0} are computed as exact
      kernels; a linear solve finds g in the right annihilator with g r = r for all r in it (and g' in
      the left annihilator with r g' = r). Then g, g' are idempotents, e = 1 - g and f = 1 - g' are
      idempotents outside {0, 1}, and a(1 - e) = 0, (1 - f)a = 0. The annihilator dimensions are
      hand-tabulated per sample.
  (2) p - q != 1 mod 4: the centre (exact kernel of the commutators with the generators) is R or
      C = R[omega] with omega^2 = -1, whose only idempotents are 0 and 1 (the polynomial identity for
      (x + y omega)^2 = x + y omega), so every annihilating idempotent is non-central; e and f are
      checked non-central.
  (3) p - q = 1 mod 4: eps_+- = (1 +- omega)/2 are central idempotents. A zero divisor inside one
      ideal (eps_- a = 0) is annihilated by the central eps_-. For samples with both components
      nonzero, the computed e and f are non-central.
  (4) Isotropic origin in mixed signatures: for a null v with partner w (vw + wv = 1) the idempotent
      wv satisfies v(1 - wv) = 0 and is non-central.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def el(*terms):
    out = {}
    for c, b in terms:
        out = GA.add(out, {tuple(b): F(c)})
    return out


def prod(p, q, *xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, GA.sig(p, q))
    return out


def half_pm(n, sign):
    return el((F(1, 2), []), (F(sign, 2), list(range(n))))


# (p, q, a, dim right annihilator, dim left annihilator); a = (invertible) x (rank-deficient) and
# combinations across the two ideals in the split signatures
SAMPLES = [
    (2, 0, el((1, []), (1, [0])), 2, 2),
    (1, 1, el((1, [0]), (1, [1])), 2, 2),
    (1, 1, prod(1, 1, el((2, []), (1, [0]), (3, [0, 1])), el((1, []), (1, [0]))), 2, 2),
    (3, 0, prod(3, 0, el((1, []), (1, [0])), el((2, []), (1, [0, 1]), (1, [2]))), 4, 4),
    (1, 3, el((1, [0]), (1, [3])), 8, 8),
    (3, 1, prod(3, 1, el((2, []), (1, [2])), el((1, []), (1, [0])), el((1, []), (1, [1, 3]))), 12, 12),
    (2, 2, el((1, []), (1, [0, 2])), 8, 8),
    (0, 4, el((1, []), (1, [0, 1, 2, 3])), 8, 8),
    (2, 1, el((1, []), (1, [0, 1, 2])), 4, 4),
    (2, 1, GA.add(prod(2, 1, half_pm(3, 1), el((1, []), (1, [0]))),
                  prod(2, 1, half_pm(3, -1), el((2, []), (1, [1])))), 2, 2),
    (0, 3, el((1, []), (1, [0, 1, 2])), 4, 4),
    (1, 2, el((1, []), (1, [0])), 4, 4),
    (4, 1, prod(4, 1, el((1, []), (1, [0])), el((1, []), (1, [1, 4]))), 24, 24),
    (3, 2, prod(3, 2, el((1, []), (1, [0])), el((1, []), (1, [1, 3])), el((3, []), (1, [0, 1, 2, 3, 4]))), 24, 24),
]


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def from_coords(c, blades):
    return {b: v for b, v in zip(blades, c) if v != 0}


def kernel(fn, blades):
    cols = [coords(fn({b: F(1)}), blades) for b in blades]
    M = [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]
    return [from_coords(k, blades) for k in GA.field_kernel(M)]


def unit_of_ideal(ann, sq, blades, side):
    """g in span(ann) with g r = r (side 'right') or r g = r (side 'left') for every r in ann."""
    rows, rhs = [], []
    for r in ann:
        prods = [GA.mul(a, r, sq) if side == "right" else GA.mul(r, a, sq) for a in ann]
        pc = [coords(x, blades) for x in prods]
        rc = coords(r, blades)
        for i in range(len(blades)):
            rows.append([pc[j][i] for j in range(len(ann))])
            rhs.append(rc[i])
    m = len(ann)
    A = [row + [b] for row, b in zip(rows, rhs)]
    ker = GA.field_kernel([[x for x in row] for row in A])
    sol = None
    for k in ker:
        if k[-1] != 0:
            sol = [-x / k[-1] for x in k[:-1]]
            break
    if sol is None:
        return None
    g = {}
    for c, a in zip(sol[:m], ann):
        g = GA.add(g, GA.scal(c, a))
    return g


def central(x, n, sq):
    return all(GA.commutes(GA.gen(i), x, sq) for i in range(n))


def annihilating_idempotents(p, q, a):
    n = p + q
    sq = GA.sig(p, q)
    blades = GA.all_blades(n)
    ra = kernel(lambda y: GA.mul(a, y, sq), blades)
    la = kernel(lambda y: GA.mul(y, a, sq), blades)
    g = unit_of_ideal(ra, sq, blades, "right")
    g2 = unit_of_ideal(la, sq, blades, "left")
    return sq, ra, la, GA.sub(GA.sc(1), g), GA.sub(GA.sc(1), g2)


def check_every_zero_divisor_annihilated_both_sides():
    premise("transport.regularity-localises-zero-divisors-idempotents")
    ok = True
    for p, q, a, dr, dl in SAMPLES:
        sq, ra, la, e, f = annihilating_idempotents(p, q, a)
        ok = ok and len(ra) == dr and len(la) == dl
        one = GA.sc(1)
        for x in (e, f):
            ok = ok and GA.eq(GA.mul(x, x, sq), x) and not GA.is_zero(x) and not GA.eq(x, one)
        ok = ok and GA.is_zero(GA.mul(a, GA.sub(one, e), sq))
        ok = ok and GA.is_zero(GA.mul(GA.sub(one, f), a, sq))
    ok = ok and len(SAMPLES) == 14
    GA.check("14 zero divisors: idempotents e, f not in {0,1} with a(1-e) = 0 and (1-f)a = 0", ok)
    return ok


def centre(p, q):
    n = p + q
    sq = GA.sig(p, q)
    blades = GA.all_blades(n)
    cols = []
    for b in blades:
        x = {b: F(1)}
        col = []
        for i in range(n):
            col += coords(GA.sub(GA.mul(GA.gen(i), x, sq), GA.mul(x, GA.gen(i), sq)), blades)
        cols.append(col)
    M = [[cols[j][i] for j in range(len(blades))] for i in range(len(cols[0]))] if n else [[F(0)]]
    return [from_coords(k, blades) for k in GA.field_kernel(M)] if n else [GA.sc(1)]


def check_simple_signatures_only_noncentral_annihilators():
    premise("transport.existence-classification-type-c")
    premise("transport.classification-real-clifford-algebras")
    ok = True
    simple = 0
    for p, q, a, dr, dl in SAMPLES:
        if (p - q) % 4 == 1:
            continue
        n = p + q
        simple += 1
        z = centre(p, q)
        sqz = GA.sig(p, q)
        if len(z) == 1:
            ok = ok and GA.eq(z[0], GA.scal(z[0].get((), F(0)), GA.sc(1)))
        else:
            ok = ok and len(z) == 2
            w = {tuple(range(n)): F(1)}
            ok = ok and GA.eq(GA.mul(w, w, sqz), GA.sc(-1)) and central(w, n, sqz)
            # (x + y w)^2 = x^2 - y^2 + 2xy w; idempotent forces y(2x - 1) = 0 and x^2 - y^2 = x:
            # y = 0 gives x in {0, 1}; x = 1/2 gives y^2 = -1/4, no real y
            for x0, y0 in ((F(1, 2), F(1, 2)), (F(1, 2), F(-1, 3)), (F(1), F(1))):
                z2 = GA.mul(GA.add(GA.sc(x0), GA.scal(y0, w)), GA.add(GA.sc(x0), GA.scal(y0, w)), sqz)
                ok = ok and not GA.eq(z2, GA.add(GA.sc(x0), GA.scal(y0, w)))
            ok = ok and GA.eq(GA.mul(w, w, sqz), GA.sc(-1))
        sq, ra, la, e, f = annihilating_idempotents(p, q, a)
        ok = ok and not central(e, n, sq) and not central(f, n, sq)
    ok = ok and simple == 10
    GA.check("p - q != 1 mod 4: centre R or C, only trivial central idempotents, annihilators non-central", ok)
    return ok


def check_split_signatures_central_or_type_p():
    premise("transport.existence-classification-type-c")
    ok = True
    split = 0
    for p, q, a, dr, dl in SAMPLES:
        if (p - q) % 4 != 1:
            continue
        n = p + q
        sq = GA.sig(p, q)
        w = {tuple(range(n)): F(1)}
        ep = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
        em = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
        ok = ok and central(ep, n, sq) and GA.eq(GA.mul(ep, ep, sq), ep) and GA.is_zero(GA.mul(ep, em, sq))
        inside = GA.is_zero(GA.mul(em, a, sq)) or GA.is_zero(GA.mul(ep, a, sq))
        if inside:
            killer = em if GA.is_zero(GA.mul(em, a, sq)) else ep
            ok = ok and GA.is_zero(GA.mul(a, killer, sq)) and central(killer, n, sq)
        else:
            sq, ra, la, e, f = annihilating_idempotents(p, q, a)
            ok = ok and not central(e, n, sq) and not central(f, n, sq)
        split += 1
    # (2,1): 1 + e012 lies in one ideal, the eps-combination does not; (0,3) inside; (3,2) not inside
    kinds = []
    for p, q, a, dr, dl in SAMPLES:
        if (p - q) % 4 == 1:
            n = p + q
            w = {tuple(range(n)): F(1)}
            em = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
            ep = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
            sq = GA.sig(p, q)
            kinds.append(GA.is_zero(GA.mul(em, a, sq)) or GA.is_zero(GA.mul(ep, a, sq)))
    ok = ok and split == 4 and kinds == [True, False, True, False]
    GA.check("p - q = 1 mod 4: a in one ideal is killed by a central eps; otherwise the annihilators are non-central", ok)
    return ok


# Sample mixed signatures (p, q >= 1).
MIXED_SIGNATURES = ((1, 1), (1, 2), (2, 1), (1, 3), (2, 2), (3, 1))


def check_isotropic_origin_in_mixed_signatures():
    premise("transport.existence-locus-type-n")
    ok = True
    for p, q in MIXED_SIGNATURES:
        n = p + q
        sq = GA.sig(p, q)
        v = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(p)))
        w = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(p)))
        ok = ok and GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(w, w, sq))   # v, w null
        ok = ok and GA.eq(GA.add(GA.mul(v, w, sq), GA.mul(w, v, sq)), GA.sc(1))
        e = GA.mul(w, v, sq)
        ok = ok and GA.eq(GA.mul(e, e, sq), e) and not central(e, n, sq)
        ok = ok and GA.is_zero(GA.mul(v, GA.sub(GA.sc(1), e), sq))
    GA.check("a null v is annihilated by the hyperbolic idempotent wv: v(1 - wv) = 0", ok)
    return ok
