"""descent-lift.imported-taxonomy-type-p-rule-algorithm: exact checks.

The Fact restates the taxonomy and the transport algorithm; its finite content is tested at
exact sample points in nondegenerate Clifford algebras (blade engine, rational linear algebra).
  (1) Zero divisors and idempotents. For sample zero divisors x (a null vector in Cl(1,3), a nilpotent
      non-vector in Cl(2,0), 1 + omega in Cl(0,3), 1 + e0 in Cl(1,2), a null vector in Cl(1,1)) the
      right annihilator {y : xy = 0} and left annihilator {y : yx = 0} are computed; an element e of
      the right annihilator with e r = r on it (and e' of the left one with r e' = r) is found by
      solving a linear system, so e is idempotent with x e = 0, e' x = 0, e, e' not 0 or 1. The
      annihilator dimensions are compared with the values read off the Wedderburn type, and e is
      non-central exactly in the simple algebras. Control: 2 + e0 has trivial annihilators.
  (2) Type N: for the hyperbolic pair v = (e0 + e_p)/2, w = (e0 - e_p)/2, wv is an idempotent with
      (wv) v = 0, written out by hand; Cl(2,0) has no nonzero null vector, so its zero divisors,
      nilpotent ones included, are never of this form.
  (3) Step 2 in order (null vector: N; central idempotent: C; otherwise P), with the caution that the
      nilpotent e0 + e0e1 of Cl(2,0) is diagnosed P.
  (4) Step 3. Type C: adjoining one generator of either sign to Cl(0,3) makes eps_+ non-central and the
      grade involution inner (conjugation by the new volume element). Type P: the identity satisfies
      both von Neumann identities on idempotents, and the general zero divisors above have
      pseudo-inverses y (xyx = x, yxy = y), the solution sets of xyx = x having the affine dimension
      dim A - dim(x A x) predicted by the Wedderburn type.
  (5) Self-adjoint generators of a right ideal: with the reversion of a definite form (Cl(2,0)) the
      self-adjoint idempotent with a given image exists and is unique; in Cl(1,1) and Cl(1,3) the
      null right ideal v A has none for the reversion, and in Cl(1,3) the positive involutions
      x -> u x~ u built from two different unit timelike u (auxiliary definite forms) give two
      different ones, so the choice is not canonical without a definite form.
  (6) The (1,1) ascent of Cl(1,3) to Cl(2,4): f = (e_a + e_b)/2, f* = (e_a - e_b)/2 and the
      projectors ff*, f*f are a full system of 2 x 2 matrix units; f and f* are null; the reflection
      in e_b, X -> e_b X^ e_b^-1, is multiplicative on every pair of blades, fixes the base and e_a,
      negates e_b and exchanges f and f*.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def el(*terms):
    out = {}
    for c, b in terms:
        out = GA.add(out, {tuple(b): F(c)})
    return out


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def from_coords(c, blades):
    return {b: x for b, x in zip(blades, c) if x != 0}


def lin_map_matrix(fn, blades):
    cols = [coords(fn({b: F(1)}), blades) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


def kernel_elems(M, blades):
    return [from_coords(v, blades) for v in GA.field_kernel(M)]


def solve_affine(rows, rhs):
    """A particular solution of rows . c = rhs (None if inconsistent) and the kernel dimension."""
    if not rows:
        return [], 0
    aug = [r + [-b] for r, b in zip(rows, rhs)]
    ker = GA.field_kernel(aug)
    nvar = len(rows[0])
    part = None
    for k in ker:
        if k[-1] != 0:
            part = [x / k[-1] for x in k[:-1]]
            break
    kdim = len([k for k in GA.field_kernel(rows)])
    return part, kdim


def annihilator_idempotent(x, sq, blades, side):
    """side 'right': e with x e = 0, e r = r on {y: xy = 0}. 'left': e' with e' x = 0, r e' = r."""
    if side == "right":
        ann = kernel_elems(lin_map_matrix(lambda y: GA.mul(x, y, sq), blades), blades)
    else:
        ann = kernel_elems(lin_map_matrix(lambda y: GA.mul(y, x, sq), blades), blades)
    if not ann:
        return ann, None
    rows, rhs = [], []
    for r in ann:
        prods = [GA.mul(a, r, sq) if side == "right" else GA.mul(r, a, sq) for a in ann]
        pc = [coords(pr, blades) for pr in prods]
        rc = coords(r, blades)
        for i in range(len(blades)):
            rows.append([pc[j][i] for j in range(len(ann))])
            rhs.append(rc[i])
    part, _ = solve_affine(rows, rhs)
    if part is None:
        return ann, None
    e = {}
    for c, a in zip(part, ann):
        e = GA.add(e, GA.scal(c, a))
    return ann, e


def is_central(x, n, sq):
    return all(GA.commutes(GA.gen(i), x, sq) for i in range(n))


# sample zero divisors: (p, q, x)
ZD = [
    (1, 3, el((1, [0]), (1, [1]))),
    (2, 0, el((1, [0]), (1, [0, 1]))),
    (0, 3, el((1, []), (1, [0, 1, 2]))),
    (1, 2, el((1, []), (1, [0]))),
    (1, 1, el((1, [0]), (1, [1]))),
]


def check_zero_divisors_annihilated_by_idempotents():
    premise("transport.exhaustiveness-every-zero-divisor-annihilated-idempotent")
    # annihilator dimension (right = left) and whether the annihilating idempotent is central:
    # Mat_2(H): rank-one x, 8; Mat_2(R): 2; H + H: the other ideal, 4; Mat_2(C): 4; Mat_2(R): 2
    expect = [(8, False), (2, False), (4, True), (4, False), (2, False)]
    ok = True
    for (p, q, x), (dim, central) in zip(ZD, expect):
        n = p + q
        sq = GA.sig(p, q)
        blades = GA.all_blades(n)
        for side in ("right", "left"):
            ann, e = annihilator_idempotent(x, sq, blades, side)
            ok = ok and e is not None and len(ann) == dim
            if e is None:
                continue
            ok = ok and GA.eq(GA.mul(e, e, sq), e) and not GA.is_zero(e) and not GA.eq(e, GA.sc(1))
            prod = GA.mul(x, e, sq) if side == "right" else GA.mul(e, x, sq)
            ok = ok and GA.is_zero(prod)
            ok = ok and is_central(e, n, sq) == central
            ok = ok and central == ((p - q) % 4 == 1)
    # control: 2 + e0 in Cl(1,3) is invertible ((2 + e0)(2 - e0) = 3), annihilators trivial
    sq = GA.sig(1, 3)
    blades = GA.all_blades(4)
    ann, e = annihilator_idempotent(el((2, []), (1, [0])), sq, blades, "right")
    ok = ok and len(ann) == 0 and e is None
    GA.check("zero divisors are annihilated on each side by nontrivial idempotents", ok)
    return ok


HYP_SIGS = ((1, 3), (2, 2), (1, 1), (3, 1))
GRID_AB = [(a, b) for a in (1, -2, 3) for b in (0, 1, -1)]


def check_type_n_hyperbolic_idempotent():
    premise("transport.exhaustiveness-every-zero-divisor-annihilated-idempotent")
    ok = True
    for p, q in HYP_SIGS:
        sq = GA.sig(p, q)
        n = p + q
        v = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(p)))
        w = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(p)))
        ok = ok and GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(w, w, sq))
        ok = ok and GA.eq(GA.add(GA.mul(v, w, sq), GA.mul(w, v, sq)), GA.sc(1))
        e = GA.mul(w, v, sq)
        ok = ok and GA.eq(GA.mul(e, e, sq), e) and GA.is_zero(GA.mul(e, v, sq))
        ok = ok and GA.is_zero(GA.mul(v, GA.mul(v, w, sq), sq)) and not is_central(e, n, sq)
        # by hand: wv = (1 + e0 e_p)/2
        ok = ok and GA.eq(e, el((F(1, 2), []), (F(1, 2), [0, p])))
    # Cl(2,0): Q(a e0 + b e1) = a^2 + b^2, so no nonzero null vector and no hyperbolic pair
    sq = GA.sig(2, 0)
    for a, b in GRID_AB:
        x = el((a, [0]), (b, [1]))
        ok = ok and GA.mul(x, x, sq) == {(): F(a * a + b * b)}
    GA.check("type N: the annihilating idempotent wv of a hyperbolic pair", ok)
    return ok


def diagnose(x, n, sq):
    grades = {len(b) for b in x}
    if grades == {1} and GA.is_zero(GA.mul(x, x, sq)):
        return "N"
    if GA.eq(GA.mul(x, x, sq), x) and is_central(x, n, sq):
        return "C"
    return "P"


DIAG_CASES = [
    ((1, 3), el((1, [0]), (1, [1]))),
    ((2, 2), el((1, [0]), (1, [2]), (1, [1]), (1, [3]))),
    ((0, 3), el((F(1, 2), []), (F(1, 2), [0, 1, 2]))),
    ((1, 0), el((F(1, 2), []), (F(-1, 2), [0]))),
    ((2, 0), el((F(1, 2), []), (F(1, 2), [0]))),
    ((2, 0), el((1, [0]), (1, [0, 1]))),
    ((1, 1), el((F(1, 2), []), (F(1, 2), [0, 1]))),
]


def check_step_two_diagnosis():
    premise("transport.transport-algorithm")
    got = [diagnose(x, p + q, GA.sig(p, q)) for (p, q), x in DIAG_CASES]
    ok = got == ["N", "N", "C", "C", "P", "P", "P"]
    # the caution: e0 + e0e1 in Cl(2,0) is nilpotent and not a vector, yet Cl(2,0) has no null
    # vector (Q(a e0 + b e1) = a^2 + b^2), so it is not of type N
    sq = GA.sig(2, 0)
    x = el((1, [0]), (1, [0, 1]))
    ok = ok and GA.is_zero(GA.mul(x, x, sq)) and sorted({len(b) for b in x}) == [1, 2]
    # by hand: x = e0 (1 + e1), and (1 + e1)/2 is an idempotent annihilating it from the left
    ok = ok and GA.eq(x, GA.mul(GA.gen(0), el((1, []), (1, [1])), sq))
    ok = ok and GA.is_zero(GA.mul(el((F(1, 2), []), (F(1, 2), [1])), x, sq))
    ok = ok and diagnose(x, len(sq), sq) == "P"
    GA.check("Step 2 diagnoses N, C, P in order; nilpotence alone does not give N", ok)
    return ok


def pseudo_inverse_space(x, sq, blades):
    """Solve x y x = x: particular solution and kernel dimension."""
    M = lin_map_matrix(lambda y: GA.mul(GA.mul(x, y, sq), x, sq), blades)
    return solve_affine(M, coords(x, blades))


def check_step_three_rules():
    premise("transport.transport-algorithm")
    premise("transport.type-p-self-repairing")
    ok = True
    # type C: Cl(0,3) + one generator of either sign
    for extra, w2 in ((1, -1), (-1, 1)):
        sq = GA.sig(0, 3) + (extra,)
        eps = el((F(1, 2), []), (F(1, 2), [0, 1, 2]))
        ok = ok and is_central(eps, 3, GA.sig(0, 3)) and not is_central(eps, 4, sq)
        Om = {(0, 1, 2, 3): F(1)}
        ok = ok and GA.mul(Om, Om, sq) == {(): F(w2)}
        Oi = GA.scal(F(w2), Om)
        for b in GA.all_blades(4):
            x = {b: F(1)}
            ok = ok and GA.eq(GA.mul(GA.mul(Om, x, sq), Oi, sq), GA.grade_inv(x))
    # type P: the identity is a von Neumann repair of an idempotent
    sq = GA.sig(2, 0)
    e = el((F(1, 2), []), (F(3, 10), [0]), (F(2, 5), [1]))
    ok = ok and GA.eq(GA.mul(e, e, sq), e) and GA.eq(GA.mul(GA.mul(e, e, sq), e, sq), e)
    # pseudo-inverses of the sample zero divisors; affine dimension dim A - dim(x A x):
    # rank one in Mat_2(H): 16 - 4; Mat_2(R): 4 - 1; H + H: 8 - 4; Mat_2(C): 8 - 2; Mat_2(R): 4 - 1
    kd = [12, 3, 4, 6, 3]
    for (p, q, x), want in zip(ZD, kd):
        sq = GA.sig(p, q)
        blades = GA.all_blades(p + q)
        part, kdim = pseudo_inverse_space(x, sq, blades)
        ok = ok and part is not None and kdim == want
        if part is None:
            continue
        y = from_coords(part, blades)
        y2 = GA.mul(GA.mul(y, x, sq), y, sq)
        ok = ok and GA.eq(GA.mul(GA.mul(x, y, sq), x, sq), x)
        ok = ok and GA.eq(GA.mul(GA.mul(x, y2, sq), x, sq), x) and GA.eq(GA.mul(GA.mul(y2, x, sq), y2, sq), y2)
    GA.check("Step 3: type C fused by one generator, type P repaired by itself, pseudo-inverses exist", ok)
    return ok


def selfadjoint_generators(g, sq, blades, inv):
    """p in g A with p r = r on g A and inv(p) = p: (particular solution or None, kernel dim)."""
    ideal = [GA.mul(g, {b: F(1)}, sq) for b in blades]
    rk = GA.field_rank([coords(r, blades) for r in ideal])
    basis = []
    for r in ideal:
        if r and GA.field_rank([coords(s, blades) for s in basis + [r]]) > len(basis):
            basis.append(r)
    rows, rhs = [], []
    for r in basis:
        pc = [coords(GA.mul(a, r, sq), blades) for a in basis]
        rc = coords(r, blades)
        for i in range(len(blades)):
            rows.append([pc[j][i] for j in range(len(basis))])
            rhs.append(rc[i])
    ic = [coords(GA.sub(inv(a), a), blades) for a in basis]
    for i in range(len(blades)):
        rows.append([ic[j][i] for j in range(len(basis))])
        rhs.append(F(0))
    part, kdim = solve_affine(rows, rhs)
    if part is None:
        return None, kdim, rk
    p = {}
    for c, a in zip(part, basis):
        p = GA.add(p, GA.scal(c, a))
    return p, kdim, rk


def check_self_adjoint_idempotent_needs_definite_form():
    ok = True
    # definite Cl(2,0) with reversion: R = g A for a non-self-adjoint idempotent g with g A = e A
    sq = GA.sig(2, 0)
    blades = GA.all_blades(2)
    e = el((F(1, 2), []), (F(3, 10), [0]), (F(2, 5), [1]))
    one_minus_e = GA.sub(GA.sc(1), e)
    g = GA.add(e, GA.mul(GA.mul(e, el((1, [0, 1])), sq), one_minus_e, sq))
    ok = ok and GA.eq(GA.mul(g, g, sq), g) and not GA.eq(GA.reverse(g), g)
    p, kdim, rk = selfadjoint_generators(g, sq, blades, GA.reverse)
    ok = ok and rk == 2 and p is not None and kdim == 0 and GA.eq(p, e)
    # indefinite Cl(1,1): the null right ideal v A, v = (e0 + e1)/2, has no reversion-self-adjoint generator
    sq = GA.sig(1, 1)
    v = el((F(1, 2), [0]), (F(1, 2), [1]))
    p, kdim, rk = selfadjoint_generators(v, sq, blades, GA.reverse)
    ok = ok and rk == 2 and p is None
    # Cl(1,3): the same for the null right ideal v A (dimension 8, rank one in Mat_2(H)) ...
    sq = GA.sig(1, 3)
    blades = GA.all_blades(4)
    v = el((F(1, 2), [0]), (F(1, 2), [1]))
    p, kdim, rk = selfadjoint_generators(v, sq, blades, GA.reverse)
    ok = ok and rk == 8 and p is None
    # ... while the positive involutions x -> u x~ u of auxiliary definite forms (u unit timelike)
    # each give exactly one, depending on u
    found = []
    for u in (el((1, [0])), el((F(5, 4), [0]), (F(3, 4), [3]))):
        ok = ok and GA.eq(GA.mul(u, u, sq), GA.sc(1))
        p, kdim, rk = selfadjoint_generators(v, sq, blades,
                                             lambda x, u=u: GA.mul(GA.mul(u, GA.reverse(x), sq), u, sq))
        ok = ok and p is not None and kdim == 0
        found.append(p)
    # by hand, for u = e0: v w = (1 - e0e1)/2; the boosted u gives a different projector
    ok = ok and len(found) == 2 and GA.eq(found[0], el((F(1, 2), []), (F(-1, 2), [0, 1])))
    ok = ok and not GA.eq(found[0], found[1])
    GA.check("self-adjoint idempotent with given image: canonical only with a definite form", ok)
    return ok


def check_one_one_ascent():
    premise("transport.rule-1-morita-trivial")
    premise("transport.no-transport-terminates")
    p, q = 1, 3
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    a, b = n, n + 1
    blades = GA.all_blades(n + 2)
    f = GA.scal(F(1, 2), GA.add(GA.gen(a), GA.gen(b)))
    fs = GA.scal(F(1, 2), GA.sub(GA.gen(a), GA.gen(b)))
    ok = GA.is_zero(GA.mul(f, f, sq)) and GA.is_zero(GA.mul(fs, fs, sq))
    E = {(1, 1): GA.mul(f, fs, sq), (2, 2): GA.mul(fs, f, sq), (1, 2): f, (2, 1): fs}
    ok = ok and GA.eq(GA.add(E[(1, 1)], E[(2, 2)]), GA.sc(1))
    ok = ok and GA.eq(E[(1, 1)], el((F(1, 2), []), (F(-1, 2), [a, b])))
    for (i, j), X in E.items():
        for (k, l), Y in E.items():
            want = E[(i, l)] if j == k else {}
            ok = ok and GA.eq(GA.mul(X, Y, sq), want)
    # reflection in e_b: X -> e_b X^ e_b^-1, e_b^-1 = -e_b
    eb, ebi = GA.gen(b), GA.neg(GA.gen(b))

    def rho(X):
        return GA.mul(GA.mul(eb, GA.grade_inv(X), sq), ebi, sq)

    for I in blades:
        for J in blades:
            x, y = {I: F(1)}, {J: F(1)}
            ok = ok and GA.eq(rho(GA.mul(x, y, sq)), GA.mul(rho(x), rho(y), sq))
    ok = ok and all(GA.eq(rho(GA.gen(i)), GA.gen(i)) for i in range(n + 1))
    ok = ok and GA.eq(rho(GA.gen(b)), GA.neg(GA.gen(b)))
    ok = ok and GA.eq(rho(f), fs) and GA.eq(rho(fs), f)
    # Rule 1 keeps the clock residue
    ok = ok and ((p + 1) - (q + 1)) % 8 == (p - q) % 8 == 6
    GA.check("(1,1) ascent: f, f*, ff*, f*f are matrix units, f null, reflection an automorphism", ok)
    return ok
