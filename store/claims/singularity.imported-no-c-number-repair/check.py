"""singularity.imported-no-c-number-repair: exact checks.

In Cl(p,q) (generators 0..p-1 square +1, p..n-1 square -1) take the hyperbolic pair
v = (e_0 + e_p)/2, w = (e_0 - e_p)/2 (v^2 = w^2 = 0, vw + wv = 1) and U the span of the remaining
generators, orthogonal to both.
  (1) Partners. Q(a v + b w + x) = ab + Q(x) (x in U), checked on a grid, so the vectors y with
      vy + yv = 1 and Q(y) = 0 are exactly w(x) = w + x - Q(x) v, x in U: an affine space over U;
      sample partners are verified null with vw(x) + w(x)v = 1.
  (2) Null rotations. For u in U the rotor R_u = 1 + v u / 2 satisfies R_u R_u~ = 1, fixes v (so lies
      in the stabiliser of [v]), composes as R_u R_u' = R_(u + u') (N_v = U), and acts on partners by
      the translation w(x) -> w(x - u/2). The tautological homomorphism theta(R_u) = -u/2 is nonzero
      for u != 0, so no partner is fixed by N_v and no equivariant assignment exists. Tested on all
      mixed signatures with 3 <= n <= 6, and again inside the ascent Cl(p+1, q+1) with partners using
      the adjoined directions: the translation is unchanged (enlargement independence).
  (3) Dimension two: in Cl(1,1) the orthogonal complement of v is the line of v, U = 0, the only null
      rotation is 1 and the partner w is unique (Q(a v + w) = a), so the class vanishes.
  (4) The wall: for a covector k on R^4 and lambda in ker k, T_lambda = id - lambda (x) k is invertible,
      preserves k, composes additively, and moves every candidate u' (k(u') = 1) by -lambda: a free
      translation action with no fixed candidate.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def setup(p, q, extra=()):
    n = p + q
    sq = GA.sig(p, q) + tuple(extra)
    v = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(p)))
    w = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(p)))
    U = [GA.gen(i) for i in range(n + len(extra)) if i not in (0, p)]
    return sq, v, w, U


def Q(x, sq):
    s = GA.mul(x, x, sq)
    return s.get((), F(0)), s


def lincomb(cs, U):
    out = {}
    for c, u in zip(cs, U):
        out = GA.add(out, GA.scal(c, u))
    return out


def partner(w, v, x, sq):
    return GA.sub(GA.add(w, x), GA.scal(Q(x, sq)[0], v))


def rotor(v, u, sq):
    return GA.add(GA.sc(1), GA.scal(F(1, 2), GA.mul(v, u, sq)))


def vec(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c != 0}


# sample data (generic points; the expected values asserted in the checks are hand-derived)
GRID_A = (F(0), F(1), F(-3, 2))
GRID_B = (F(1), F(2), F(-1, 3))
X0 = [F(2), F(-1), F(1, 3), F(1)]
XS = ([0], [1], [F(-2, 3), 1], [1, 1, -1], [0, 2, 0, F(1, 2)])
US = ([1], [2, 1], [3, F(-1, 2)], [-1, 0, 0, 1])
K = [F(1), F(-2), F(0), F(3)]
LAMS = ([2, 1, 0, 0], [0, 0, 5, 0], [3, 0, 1, -1])
CANDS = ([1, 0, 0, 0], [0, 1, 7, 1], [F(1, 2), F(-1, 4), -2, 0])
PTS = ([1, 2, 3, 4], [0, -1, 0, 2])


def kv(x):
    return sum(a * b for a, b in zip(K, x))


def T(lam, x):
    return [xi - li * kv(x) for xi, li in zip(x, lam)]


def partner_family_ok(sq, v, w, U):
    ok = True
    x0 = lincomb(X0, U)
    for a in GRID_A:
        for b in GRID_B:
            y = GA.add(GA.scal(a, v), GA.scal(b, w), x0)
            ok = ok and Q(y, sq)[0] == a * b + Q(x0, sq)[0]
            ok = ok and GA.add(GA.mul(v, y, sq), GA.mul(y, v, sq)) == {(): b}
    for xc in XS:
        wx = partner(w, v, lincomb(xc, U), sq)
        ok = ok and GA.is_zero(GA.mul(wx, wx, sq))
        ok = ok and GA.eq(GA.add(GA.mul(v, wx, sq), GA.mul(wx, v, sq)), GA.sc(1))
    return ok


def acts_by_translation(sq, v, w, U, xs, us):
    ok = True
    for uc in us:
        u = lincomb(uc, U)
        R = rotor(v, u, sq)
        Rr = GA.reverse(R)
        ok = ok and GA.eq(GA.mul(R, Rr, sq), GA.sc(1))
        ok = ok and GA.eq(GA.mul(GA.mul(R, v, sq), Rr, sq), v)
        for xc in xs:
            x = lincomb(xc, U)
            wx = partner(w, v, x, sq)
            img = GA.mul(GA.mul(R, wx, sq), Rr, sq)
            shifted = partner(w, v, GA.sub(x, GA.scal(F(1, 2), u)), sq)
            ok = ok and GA.eq(img, shifted) and not GA.eq(img, wx)
    return ok


def check_partners_form_affine_space_over_u():
    premise("transport.no-go-level-elements")
    ok = True
    count = 0
    for n in range(3, 7):
        for p in range(1, n):
            sq, v, w, U = setup(p, n - p)
            ok = ok and len(U) == n - 2
            ok = ok and GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(w, w, sq))
            ok = ok and GA.eq(GA.add(GA.mul(v, w, sq), GA.mul(w, v, sq)), GA.sc(1))
            ok = ok and partner_family_ok(sq, v, w, U)
            count += 1
    ok = ok and count == 14
    # explicit partners, by hand: Cl(1,3), x = e2 + 2 e3, Q(x) = -5: w + x + 5 v = 3e0 + 2e1 + e2 + 2e3
    sq, v, w, U = setup(1, 3)
    ok = ok and GA.eq(partner(w, v, lincomb([1, 2], U), sq), vec([3, 2, 1, 2]))
    # Cl(2,1), x = 3 e1, Q(x) = 9: w + x - 9 v = -4 e0 + 3 e1 - 5 e2
    sq, v, w, U = setup(2, 1)
    ok = ok and GA.eq(partner(w, v, lincomb([3], U), sq), vec([-4, 3, -5]))
    GA.check("partners of v form the affine space w + x - Q(x) v over U", ok)
    return ok


def check_null_rotations_translate_partners():
    premise("transport.no-go-level-elements")
    premise("transport.cohomological-form-no-go")
    ok = True
    count = 0
    for n in range(3, 7):
        for p in range(1, n):
            sq, v, w, U = setup(p, n - p)
            ok = ok and acts_by_translation(sq, v, w, U, XS, US)
            # N_v is abelian and isomorphic to U: R_u R_u' = R_(u + u')
            u1, u2 = lincomb(US[0], U), lincomb(US[2], U)
            ok = ok and GA.eq(GA.mul(rotor(v, u1, sq), rotor(v, u2, sq), sq),
                              rotor(v, GA.add(u1, u2), sq))
            # inside the ascent Cl(p+1, q+1): partners may use the adjoined directions
            sqA, vA, wA, UA = setup(p, n - p, extra=(1, -1))
            ok = ok and len(UA) == n
            xsA = ([0] * (n - 2) + [1, 2], [1] * n)
            ok = ok and acts_by_translation(sqA, vA, wA, UA, xsA, US)
            count += 1
    ok = ok and count == 14
    # by hand in Cl(2,2), v = (e0 + e2)/2, u = e1: R_u = 1 + e0e1/4 - e1e2/4 and
    # R_u w R_u~ = w - u/2 - Q(u) v/4 = (3/8) e0 - (1/2) e1 - (5/8) e2
    sq, v, w, U = setup(2, 2)
    R = rotor(v, U[0], sq)
    ok = ok and GA.eq(R, {(): F(1), (0, 1): F(1, 4), (1, 2): F(-1, 4)})
    img = GA.mul(GA.mul(R, w, sq), GA.reverse(R), sq)
    ok = ok and GA.eq(img, {(0,): F(3, 8), (1,): F(-1, 2), (2,): F(-5, 8)})
    # u = e3 (Q(u) = -1): (5/8) e0 - (3/8) e2 - (1/2) e3
    R = rotor(v, U[1], sq)
    img = GA.mul(GA.mul(R, w, sq), GA.reverse(R), sq)
    ok = ok and GA.eq(img, {(0,): F(5, 8), (2,): F(-3, 8), (3,): F(-1, 2)})
    GA.check("null rotations translate the partners by theta(R_u) = -u/2, also in the ascent", ok)
    return ok


def check_dimension_two_exception():
    premise("transport.cohomological-form-no-go")
    sq, v, w, U = setup(1, 1)
    ok = len(U) == 0
    # v^perp: kernel of x -> v.x on R^{1,1}; v.e0 = 1/2, v.e1 = -1/2, so the kernel is the line (1, 1) of v
    row = [GA.dot(v, GA.gen(i), sq) for i in range(2)]
    ok = ok and row == [F(1, 2), F(-1, 2)]
    ker = GA.field_kernel([row])
    ok = ok and ker == [[F(1), F(1)]]
    perp = GA.add(GA.scal(ker[0][0], GA.gen(0)), GA.scal(ker[0][1], GA.gen(1)))
    ok = ok and GA.eq(perp, GA.scal(2, v))
    # the only null rotation: 1 + v (c v)/2 = 1
    ok = ok and GA.eq(rotor(v, perp, sq), GA.sc(1))
    # Q(a v + b w) = ab and vy + yv = b: a partner has b = 1, then a = 0, so it is w
    for a in GRID_A:
        for b in GRID_B:
            y = GA.add(GA.scal(a, v), GA.scal(b, w))
            ok = ok and Q(y, sq)[0] == a * b
            ok = ok and GA.add(GA.mul(v, y, sq), GA.mul(y, v, sq)) == {(): b}
    ok = ok and GA.eq(partner(w, v, {}, sq), w)
    GA.check("Cl(1,1): U = 0, null rotations trivial, the partner w unique", ok)
    return ok


def check_wall_translation_action():
    premise("sheaf.no-equivariant-value-wall")
    ok = True
    for lam in LAMS:
        lam = [F(c) for c in lam]
        ok = ok and kv(lam) == 0
        for cand in CANDS:
            cand = [F(c) for c in cand]
            ok = ok and kv(cand) == 1
            img = T(lam, cand)
            ok = ok and img == [c - l for c, l in zip(cand, lam)] and img != cand and kv(img) == 1
        # invertible with inverse id + lambda k, and additive: T_lam T_mu = T_(lam + mu)
        for x in PTS:
            x = [F(c) for c in x]
            back = [a + b * kv(T(lam, x)) for a, b in zip(T(lam, x), lam)]
            ok = ok and back == x
            mu = [F(c) for c in LAMS[0]]
            ok = ok and T(lam, T(mu, x)) == T([a + b for a, b in zip(lam, mu)], x)
    # by hand: k = (1, -2, 0, 3), lambda = (2, 1, 0, 0), candidate (0, 1, 7, 1) -> (-2, 0, 7, 1)
    ok = ok and T([2, 1, 0, 0], [0, 1, 7, 1]) == [-2, 0, 7, 1]
    ok = ok and T([3, 0, 1, -1], [1, 2, 3, 4]) == [-26, 2, -6, 13]
    GA.check("at the wall id - lambda k translates every candidate by -lambda (free action)", ok)
    return ok
