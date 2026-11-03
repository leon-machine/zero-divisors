"""transport.rule-2-ideal-fusion-sharp-form: exact checks.

For every signature with p - q = 1 mod 4 and n = p + q <= 5 ((1,0), (2,1), (0,3), (3,2), (1,4),
(5,0)) and both gamma = +1, -1: A = Cl(p,q) on e_0..e_{n-1}, nu = e_n with nu^2 = gamma,
omega = e_0...e_{n-1} (central, omega^2 = +1), eps_+- = (1 +- omega)/2,
E11 = eps_+, E22 = eps_-, E12 = eps_+ nu, E21 = gamma eps_- nu.
(main) The E_ij are a full system of 2 x 2 matrix units (all 16 products and E11 + E22 = 1); the
    corner E11 B E11 equals eps_+ A, of dimension 2^(n-1); a -> eps_+ a is injective on Cl^0(p,q)
    and multiplicative on all pairs of even blades; the 4 * 2^(n-1) elements E_i1 c E_1j (c in the
    corner basis) span B: B = Mat_2(Cl^0(p,q)).
(1) The central blades of B are the scalars only (A, as control, has the central omega); the
    trace form is diagonal with entries +-1 in the blade basis, so B is semisimple with
    one-dimensional centre: simple, centre R, no central idempotent (no type C).
(2) eps_+- are non-central in B, Ad_nu exchanges them, and Ad_nu restricts on every blade of A to
    the grade involution.
(3) phi: e_i -> e_i, nu_+ -> omega nu_- satisfies the relations of Cl(p+1, q) inside Cl(p, q+1),
    its images span (rank 2^(n+1)), so phi is an isomorphism; it fixes A (hence the corner) and
    sends each matrix unit E_ij^+ to E_ij^-. The quadratic data differ: the signatures of
    V + <+1> and V + <-1> are (p+1, q) and (p, q+1).
EXPORTS: fusion(p, q, gamma), central_blades(sq, m), span_rank(elems, m), for dependent checks.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(1, 0), (2, 1), (0, 3), (3, 2), (1, 4), (5, 0)]


def fusion(p, q, g):
    n = p + q
    sq = GA.sig(p, q) + (g,)
    nu = GA.gen(n)
    omega = {tuple(range(n)): F(1)}
    ep = GA.scal(F(1, 2), GA.add(GA.sc(1), omega))
    em = GA.scal(F(1, 2), GA.sub(GA.sc(1), omega))
    E = {(1, 1): ep, (2, 2): em, (1, 2): GA.mul(ep, nu, sq),
         (2, 1): GA.scal(g, GA.mul(em, nu, sq))}
    return {"n": n, "sq": sq, "nu": nu, "omega": omega, "ep": ep, "em": em, "E": E}


def central_blades(sq, m):
    out = []
    for b in GA.all_blades(m):
        e = {b: F(1)}
        if all(GA.commutes(GA.gen(i), e, sq) for i in range(m)):
            out.append(b)
    return out


def span_rank(elems, m):
    blades = GA.all_blades(m)
    rows = [GA.basis_vector_of(x, blades) for x in elems if x]
    return GA.rank_of_vectors(rows) if rows else 0


EXPORTS = {"fusion": fusion, "central_blades": central_blades, "span_rank": span_rank}


def _even_blades(n):
    return [b for b in GA.all_blades(n) if len(b) % 2 == 0]


def check_matrix_units_and_corner():
    premise("transport.matrix-units-peirce-isomorphism")
    premise("transport.corner-even-subalgebra")
    ok = True
    cases = 0
    for (p, q) in SIGS:
        for g in (1, -1):
            D = fusion(p, q, g)
            n, sq, E = D["n"], D["sq"], D["E"]
            for (i, j), Eij in E.items():
                for (k, l), Ekl in E.items():
                    prod = GA.mul(Eij, Ekl, sq)
                    ok = ok and GA.eq(prod, E[(i, l)] if j == k else {})
            ok = ok and GA.eq(GA.add(E[(1, 1)], E[(2, 2)]), GA.sc(1))
            # corner E11 B E11 = eps_+ A, dimension 2^(n-1)
            corner_B = [GA.mul(GA.mul(D["ep"], {b: F(1)}, sq), D["ep"], sq) for b in GA.all_blades(n + 1)]
            epsA = [GA.mul(D["ep"], {b: F(1)}, sq) for b in GA.all_blades(n)]
            r_corner = span_rank(corner_B, n + 1)
            ok = ok and r_corner == 2 ** (n - 1) and span_rank(corner_B + epsA, n + 1) == r_corner
            # a -> eps_+ a injective on Cl^0 and multiplicative on even blades
            ev = _even_blades(n)
            img = [GA.mul(D["ep"], {b: F(1)}, sq) for b in ev]
            ok = ok and span_rank(img, n + 1) == 2 ** (n - 1)
            for a in ev:
                for b in ev:
                    lhs = GA.mul(GA.mul(D["ep"], {a: F(1)}, sq), GA.mul(D["ep"], {b: F(1)}, sq), sq)
                    rhs = GA.mul(D["ep"], GA.mul({a: F(1)}, {b: F(1)}, sq), sq)
                    ok = ok and GA.eq(lhs, rhs)
            # B is spanned by E_i1 c E_1j: B = Mat_2(corner)
            span = []
            for i in (1, 2):
                for j in (1, 2):
                    for c in img:
                        span.append(GA.mul(GA.mul(E[(i, 1)], c, sq), E[(1, j)], sq))
            ok = ok and len(span) == 2 ** (n + 1) and span_rank(span, n + 1) == 2 ** (n + 1)
            cases += 1
    ok = ok and cases == 12
    GA.check("matrix units, corner eps_+ A = Cl^0, B = Mat_2(Cl^0): 6 signatures x 2 signs", ok)
    return ok


def check_fused_algebra_simple_centre_r():
    premise("transport.centre")
    premise("transport.classification-real-clifford-algebras")
    ok = True
    for (p, q) in SIGS:
        n = p + q
        sqA = GA.sig(p, q)
        ok = ok and central_blades(sqA, n) == [(), tuple(range(n))]        # A: centre R + R omega
        ok = ok and GA.eq(GA.mul({tuple(range(n)): F(1)}, {tuple(range(n)): F(1)}, sqA), GA.sc(1))
        for g in (1, -1):
            sq = fusion(p, q, g)["sq"]
            ok = ok and central_blades(sq, n + 1) == [()]
            # trace form: tau(e_I e_J) = 0 for I != J and e_I^2 = +-1, so nondegenerate
            ok = ok and all(GA.mul({b: F(1)}, {b: F(1)}, sq).get((), F(0)) in (1, -1)
                            for b in GA.all_blades(n + 1))
    GA.check("B_gamma semisimple with centre R (simple); A has centre R + R omega", ok)
    return ok


def check_eps_exchanged_by_ad_nu():
    premise("transport.ascent-renders-grade-involution-inner")
    ok = True
    for (p, q) in SIGS:
        for g in (1, -1):
            D = fusion(p, q, g)
            n, sq, nu = D["n"], D["sq"], D["nu"]
            nu_inv = GA.scal(g, nu)
            ok = ok and GA.eq(GA.mul(GA.mul(nu, D["ep"], sq), nu_inv, sq), D["em"])
            ok = ok and GA.eq(GA.mul(GA.mul(nu, D["em"], sq), nu_inv, sq), D["ep"])
            ok = ok and not GA.commutes(D["ep"], nu, sq) and not GA.commutes(D["em"], nu, sq)
            for b in GA.all_blades(n):
                a = {b: F(1)}
                ok = ok and GA.eq(GA.mul(GA.mul(nu, a, sq), nu_inv, sq), GA.grade_inv(a))
    GA.check("eps_+- non-central, exchanged by Ad_nu; Ad_nu = grade involution on A", ok)
    return ok


def check_two_ascents_isomorphic_fixing_corner():
    ok = True
    for (p, q) in SIGS:
        n = p + q
        Dp, Dm = fusion(p, q, 1), fusion(p, q, -1)
        sqm = Dm["sq"]
        images = [GA.gen(i) for i in range(n)] + [GA.mul(Dm["omega"], Dm["nu"], sqm)]
        target = GA.sig(p, q) + (1,)
        for i in range(n + 1):
            ok = ok and GA.eq(GA.mul(images[i], images[i], sqm), GA.sc(target[i]))
            for j in range(i + 1, n + 1):
                ok = ok and GA.anticommutes(images[i], images[j], sqm)

        def phi(x):
            out = {}
            for b, c in x.items():
                term = GA.sc(c)
                for i in b:
                    term = GA.mul(term, images[i], sqm)
                out = GA.add(out, term)
            return out

        ok = ok and span_rank([phi({b: F(1)}) for b in GA.all_blades(n + 1)], n + 1) == 2 ** (n + 1)
        for key in Dp["E"]:
            ok = ok and GA.eq(phi(Dp["E"][key]), Dm["E"][key])
        for b in GA.all_blades(n):
            ok = ok and GA.eq(phi({b: F(1)}), {b: F(1)})
        sig_p = GA.congruence_signature([[F(target[i]) if i == j else 0 for j in range(n + 1)] for i in range(n + 1)])
        sig_m = GA.congruence_signature([[F(sqm[i]) if i == j else 0 for j in range(n + 1)] for i in range(n + 1)])
        ok = ok and sig_p == (p + 1, q, 0) and sig_m == (p, q + 1, 0)
    GA.check("Cl(p+1,q) = Cl(p,q+1) by nu -> omega nu, fixing A and the matrix units; data non-isometric", ok)
    return ok
