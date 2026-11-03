"""rule2.imported-rule-2-matrix-units-forgotten: exact checks.

Built on the constructions exported by the check of transport.rule-2-ideal-fusion-sharp-form
(fusion(p, q, gamma): nu, omega, eps_+-, and E11 = eps_+, E22 = eps_-, E12 = eps_+ nu,
E21 = gamma eps_- nu as stated). Signatures p - q = 1 mod 4 with n <= 7 (ten signatures; the four
with n = 7 have 256-dimensional ascents), both signs of gamma.
(1) Matrix units, simplicity and Ad_nu: the 16 products of the stated E_ij, E11 + E22 = 1; the
    centre of B_gamma is R (central blades); Ad_nu = grade involution on every blade of A and
    exchanges eps_+-, which are non-central.
(2) a -> eps_+ a is an isomorphism Cl^0(p,q) -> eps_+ A: injective (rank 2^(n-1)), onto
    (eps_+ A has dimension 2^(n-1)) and multiplicative on all pairs of even blades (n <= 5).
(3) The two ascents are isomorphic, non-isometric: nu_+ -> omega nu_- satisfies the relations of
    Cl(p+1, q) in Cl(p, q+1) and fixes A; the signatures (p+1, q) and (p, q+1) differ.
(4) The null generator never fuses: for gamma = 0, J = A nu is a two-sided ideal (stable under
    left and right multiplication by every generator), J^2 = 0 on all blade pairs, dim B_0 / J =
    2^n, and the trace form of B_0 is degenerate exactly on J, so B_0 is not semisimple.
(5) One generator is minimal and fusion fires at most once: A itself is not simple (eps_+ is a
    nontrivial central idempotent); over all transport histories of length <= 4 from the 15
    signatures with n <= 4 (Rule 1 always, Rule 2 when the algebra has type C, type C computed
    from the blades: omega central with omega^2 = +1), Rule 2 occurs at most once, moves the
    residue by +-1 into {0, 2, 4, 6}, and Rule 1 keeps it.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SMALL = [(1, 0), (2, 1), (0, 3), (3, 2), (1, 4), (5, 0)]
LARGE = [(4, 3), (2, 5), (6, 1), (0, 7)]


def check_matrix_units_simplicity_and_ad_nu():
    ex = premise("transport.rule-2-ideal-fusion-sharp-form")
    premise("transport.matrix-units-peirce-isomorphism")
    premise("transport.ascent-renders-grade-involution-inner")
    fusion, central_blades = ex["fusion"], ex["central_blades"]
    ok = True
    for (p, q) in SMALL + LARGE:
        for g in (1, -1):
            D = fusion(p, q, g)
            n, sq, nu, E = D["n"], D["sq"], D["nu"], D["E"]
            ok = ok and GA.eq(E[(2, 1)], GA.scal(g, GA.mul(D["em"], nu, sq)))
            for (i, j), Eij in E.items():
                for (k, l), Ekl in E.items():
                    ok = ok and GA.eq(GA.mul(Eij, Ekl, sq), E[(i, l)] if j == k else {})
            ok = ok and GA.eq(GA.add(E[(1, 1)], E[(2, 2)]), GA.sc(1))
            ok = ok and central_blades(sq, n + 1) == [()]
            nu_inv = GA.scal(g, nu)
            ok = ok and GA.eq(GA.mul(GA.mul(nu, D["ep"], sq), nu_inv, sq), D["em"])
            ok = ok and not GA.commutes(D["ep"], nu, sq)
            for b in GA.all_blades(n):
                a = {b: F(1)}
                ok = ok and GA.eq(GA.mul(GA.mul(nu, a, sq), nu_inv, sq), GA.grade_inv(a))
    GA.check("stated matrix units, centre R, Ad_nu = grade involution exchanging eps_+-, n <= 7", ok)
    return ok


def check_corner_map_isomorphism():
    ex = premise("transport.rule-2-ideal-fusion-sharp-form")
    premise("transport.corner-even-subalgebra")
    fusion, span_rank = ex["fusion"], ex["span_rank"]
    ok = True
    for (p, q) in SMALL:
        D = fusion(p, q, 1)
        n, sq, ep = D["n"], D["sq"], D["ep"]
        ev = [b for b in GA.all_blades(n) if len(b) % 2 == 0]
        img = [GA.mul(ep, {b: F(1)}, sq) for b in ev]
        epsA = [GA.mul(ep, {b: F(1)}, sq) for b in GA.all_blades(n)]
        ok = ok and len(ev) == 2 ** (n - 1)
        ok = ok and span_rank(img, n + 1) == 2 ** (n - 1) and span_rank(epsA, n + 1) == 2 ** (n - 1)
        for a in ev:
            for b in ev:
                lhs = GA.mul(GA.mul(ep, {a: F(1)}, sq), GA.mul(ep, {b: F(1)}, sq), sq)
                ok = ok and GA.eq(lhs, GA.mul(ep, GA.mul({a: F(1)}, {b: F(1)}, sq), sq))
    GA.check("a -> eps_+ a is an algebra isomorphism Cl^0(p,q) -> eps_+ A", ok)
    return ok


def check_ascents_isomorphic_not_isometric():
    ex = premise("transport.rule-2-ideal-fusion-sharp-form")
    premise("transport.one-generator-minimal-minimal-completions-classified")
    fusion = ex["fusion"]
    ok = True
    for (p, q) in SMALL + LARGE:
        n = p + q
        Dm = fusion(p, q, -1)
        sqm = Dm["sq"]
        images = [GA.gen(i) for i in range(n)] + [GA.mul(Dm["omega"], Dm["nu"], sqm)]
        target = GA.sig(p, q) + (1,)
        for i in range(n + 1):
            ok = ok and GA.eq(GA.mul(images[i], images[i], sqm), GA.sc(target[i]))
            for j in range(i + 1, n + 1):
                ok = ok and GA.anticommutes(images[i], images[j], sqm)
        gp = [[F(target[i]) if i == j else F(0) for j in range(n + 1)] for i in range(n + 1)]
        gm = [[F(sqm[i]) if i == j else F(0) for j in range(n + 1)] for i in range(n + 1)]
        ok = ok and GA.congruence_signature(gp) == (p + 1, q, 0)
        ok = ok and GA.congruence_signature(gm) == (p, q + 1, 0)
    GA.check("Cl(p+1,q) and Cl(p,q+1) isomorphic through nu -> omega nu; quadratic data differ", ok)
    return ok


def check_null_generator_never_fuses():
    ex = premise("transport.rule-2-ideal-fusion-sharp-form")
    premise("transport.one-generator-minimal-minimal-completions-classified")
    span_rank = ex["span_rank"]
    ok = True
    for (p, q) in SMALL:
        n = p + q
        sq = GA.sig(p, q) + (0,)
        nu = GA.gen(n)
        J = [GA.mul({b: F(1)}, nu, sq) for b in GA.all_blades(n)]
        ok = ok and span_rank(J, n + 1) == 2 ** n
        # J is exactly the span of the blades containing nu, so membership is read blade-wise
        ok = ok and all(n in b for x in J for b in x)
        for x in J:
            for i in range(n + 1):
                for y in (GA.mul(GA.gen(i), x, sq), GA.mul(x, GA.gen(i), sq)):
                    ok = ok and all(n in b for b in y)                  # stays in J
            for y in J:
                ok = ok and GA.is_zero(GA.mul(x, y, sq))                 # J^2 = 0
        ok = ok and 2 ** (n + 1) - span_rank(J, n + 1) == 2 ** n          # dim B_0 / J = dim A
        degenerate = [b for b in GA.all_blades(n + 1) if GA.mul({b: F(1)}, {b: F(1)}, sq) == {}]
        ok = ok and len(degenerate) == 2 ** n and all(n in b for b in degenerate)
    GA.check("gamma = 0: J = A nu is a square-zero two-sided ideal, B_0 not semisimple", ok)
    return ok


def _type_c(p, q):
    n = p + q
    if n % 2 == 0:
        return False
    sq = GA.sig(p, q)
    om = {tuple(range(n)): F(1)}
    central = all(GA.commutes(GA.gen(i), om, sq) for i in range(n))
    return central and GA.eq(GA.mul(om, om, sq), GA.sc(1))


def check_fusion_fires_at_most_once():
    premise("transport.fusion-occurs-most-once")
    ok = True
    # A itself (dim V' = n) is not simple: eps_+ is a nontrivial central idempotent
    for (p, q) in SMALL:
        n = p + q
        sq = GA.sig(p, q)
        ep = GA.scal(F(1, 2), GA.add(GA.sc(1), {tuple(range(n)): F(1)}))
        ok = ok and GA.eq(GA.mul(ep, ep, sq), ep) and all(GA.commutes(ep, GA.gen(i), sq) for i in range(n))
        ok = ok and not GA.eq(ep, GA.sc(1)) and not GA.is_zero(ep)
    tc = {}

    def is_c(s):
        if s not in tc:
            tc[s] = _type_c(*s)
        return tc[s]

    starts = [(p, n - p) for n in range(0, 5) for p in range(n + 1)]
    histories = 0
    with_rule2 = 0
    max_rule2 = 0
    frontier = [((p, q), 0) for (p, q) in starts]
    for _ in range(4):
        nxt = []
        for (p, q), k in frontier:
            d = (p - q) % 8
            nxt.append(((p + 1, q + 1), k))
            ok = ok and (p + 1 - (q + 1)) % 8 == d
            if is_c((p, q)):
                ok = ok and d in (1, 5)
                for s in ((p + 1, q), (p, q + 1)):
                    d2 = (s[0] - s[1]) % 8
                    ok = ok and d2 in (0, 2, 4, 6) and (d2 - d) % 8 in (1, 7)
                    nxt.append((s, k + 1))
        frontier = nxt
        for _, k in frontier:
            histories += 1
            with_rule2 += 1 if k > 0 else 0
            max_rule2 = max(max_rule2, k)
    ok = ok and max_rule2 == 1
    # type C at n <= 4: (1,0), (2,1), (0,3); each start branches once (two ascents) at most
    ok = ok and sorted(s for s in starts if is_c(s)) == [(0, 3), (1, 0), (2, 1)]
    ok = ok and with_rule2 > 0 and histories > len(starts)
    GA.check("Rule 2 fires at most once in every transport history of length <= 4 (n <= 4 starts)", ok)
    return ok
