"""odd-extensions.two-towers-one-curved-universe: exact checks (Clifford algebra in GA.py).

(i) Tractor spaces: this world R^{2,4}, the mirror (metric -g) R^{4,2}. The scale tractor I has Q(I) = Lambda/3
    (premise Fact) in this world and -Q(I) in the mirror. For sample non-basis vectors I of either sign of
    norm, the orthogonal complement I^perp (computed as the kernel of x -> x . I) carries, by exact
    congruence, the signature (1,4) [this world, de Sitter], (2,3) [this world, anti-de Sitter], (4,1)
    [mirror, de Sitter], (3,2) [mirror, anti-de Sitter]. In each Cl(p,q) with p + q = 5 the volume element
    omega is central and omega^2 = +1 for Cl(1,4), Cl(3,2) and -1 for Cl(4,1), Cl(2,3); doubled exactly
    when omega^2 = +1 (central idempotents (1 +- omega)/2 exist), complexified when omega^2 = -1. The rule
    "doubled iff (de Sitter and this world) or (anti-de Sitter and mirror)" holds on all four cases.
(ii) In Cl(1,4) (e0^2 = +1, e1..e3 and e5 square -1) and Cl(4,1) (the reversed signs) the elements
    E_mu = e_mu e_5 anticommute pairwise with squares (+,-,-,-) in both; the map E_mu -> E'_mu extends to an
    algebra isomorphism Cl^0(1,4) -> Cl^0(4,1) (multiplicative on all 256 pairs of the 16 basis products,
    bijective), so the bivector algebras (spin algebras) coincide; both are Cl(1,3).
(iii) The fifth generator: in the doubled case e5^2 = -1 and P_+- e5 = -+ P_+- omega' on the two summands
    (P_+- = (1 +- omega)/2, omega' = e0 e1 e2 e3): e5 = +-omega' with opposite signs on the two summands; in
    the complexified case e5^2 = +1 and e5 = omega'^{-1} omega with omega central and omega^2 = -1.
The consequence (no derived quantity uses e5) rests on the cited propositions and is not recomputed.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

from itertools import combinations

CASES = {("this", "dS"): ((2, 4), 1), ("this", "AdS"): ((2, 4), -1), ("mirror", "dS"): ((4, 2), -1),
         ("mirror", "AdS"): ((4, 2), 1)}                     # (tractor signature, sign of Q(I))
ICANDS = [[F(2), F(1), F(1), F(0), F(0), F(0)], [F(1), F(0), F(2), F(1), F(0), F(0)], [F(1), F(0), F(0), F(0), F(2), F(1)]]


def vec_from(coef):
    return GA.add(*[GA.scal(c, GA.gen(i)) for i, c in enumerate(coef) if c])


def complement_signature(sq, I):
    """Signature of the form on I^perp (kernel of x -> x . I)."""
    n = len(sq)
    row = [GA.dot(GA.gen(i), I, sq) for i in range(n)]
    ker = GA.field_kernel([row])
    vs = [vec_from(v) for v in ker]
    gram = [[GA.dot(a, b, sq) for b in vs] for a in vs]
    return tuple(GA.congruence_signature(gram)[:2])


def volume_square(p, q):
    sq = GA.sig(p, q)
    om = {tuple(range(p + q)): F(1)}
    central = all(GA.commutes(om, GA.gen(i), sq) for i in range(p + q))
    return central, GA.mul(om, om, sq)


def norm_of(sq, coef):
    v = vec_from(coef)
    return GA.dot(v, v, sq)


def check_intermediate_algebras_and_the_rule():
    premise("odd-extensions.imported-frozen-point")
    premise("odd-extensions.doubling-or-complexification")
    premise("odd-extensions.four-extensions-oriented-pair")
    want = {("this", "dS"): ((1, 4), True), ("this", "AdS"): ((2, 3), False),
            ("mirror", "dS"): ((4, 1), False), ("mirror", "AdS"): ((3, 2), True)}
    ok = True
    for key, ((p, q), sgn) in CASES.items():
        sq = GA.sig(p, q)
        coef = next(c for c in ICANDS if norm_of(sq, c) * sgn > 0)
        I = vec_from(coef)
        ok = ok and GA.dot(I, I, sq) * sgn > 0
        sig = complement_signature(sq, I)
        central, om2 = volume_square(*sig)
        doubled = om2 == GA.sc(1)
        ok = ok and central and (om2 == GA.sc(1) or om2 == GA.sc(-1)) and (sig, doubled) == want[key]
        rule = (key == ("this", "dS")) or (key == ("mirror", "AdS"))
        ok = ok and doubled == rule
    _tp_rv = (ok); assert _tp_rv is not False, "check_intermediate_algebras_and_the_rule"; return _tp_rv


def even_basis(sq):
    E = [GA.mul(GA.gen(mu), GA.gen(4), sq) for mu in range(4)]
    words = []
    for k in range(5):
        for comb in combinations(range(4), k):
            w = GA.sc(1)
            for i in comb:
                w = GA.mul(w, E[i], sq)
            words.append(w)
    return E, words


def check_even_subalgebras_coincide():
    premise("odd-extensions.imported-copy-theorem-soldered-residue")
    sqA, sqB = (1, -1, -1, -1, -1), (-1, 1, 1, 1, 1)
    EA, WA = even_basis(sqA)
    EB, WB = even_basis(sqB)
    ok = True
    for E, sq in ((EA, sqA), (EB, sqB)):
        ok = ok and [GA.mul(x, x, sq) for x in E] == [GA.sc(1), GA.sc(-1), GA.sc(-1), GA.sc(-1)]
        ok = ok and all(GA.anticommutes(E[i], E[j], sq) for i in range(4) for j in range(i + 1, 4))
    blades = sorted({b for w in WA + WB for b in w})
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(w, blades) for w in WA]) == 16
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(w, blades) for w in WB]) == 16
    for i in range(16):
        for j in range(16):
            ca = solve_in(WA, GA.mul(WA[i], WA[j], sqA), blades)
            cb = solve_in(WB, GA.mul(WB[i], WB[j], sqB), blades)
            ok = ok and ca == cb
    _tp_rv = (ok); assert _tp_rv is not False, "check_even_subalgebras_coincide"; return _tp_rv


def solve_in(words, x, blades):
    """Coordinates of x in the span of the 16 words (exact, by elimination on the blade coordinates)."""
    rows = [[w.get(b, F(0)) for w in words] + [x.get(b, F(0))] for b in blades]
    ncol = len(words)
    piv_cols, r = [], 0
    for c in range(ncol):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        pv = rows[r][c]
        rows[r] = [v / pv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        piv_cols.append(c)
        r += 1
    sol = [F(0)] * ncol
    for i, c in enumerate(piv_cols):
        sol[c] = rows[i][-1]
    return sol


def check_fifth_generator_alone_differs():
    premise("odd-extensions.doubling-or-complexification")
    ok = True
    sqD = (1, -1, -1, -1, -1)                        # Cl(1,4), doubled
    om = {(0, 1, 2, 3, 4): F(1)}
    omp = {(0, 1, 2, 3): F(1)}
    e5 = GA.gen(4)
    ok = ok and GA.mul(e5, e5, sqD) == GA.sc(-1) and GA.mul(om, om, sqD) == GA.sc(1)
    for s in (1, -1):
        P = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(s, om)))
        ok = ok and GA.eq(GA.mul(P, e5, sqD), GA.scal(-s, GA.mul(P, omp, sqD)))
    sqC = (-1, 1, 1, 1, 1)                           # Cl(4,1), complexified
    ok = ok and GA.mul(e5, e5, sqC) == GA.sc(1) and GA.mul(om, om, sqC) == GA.sc(-1)
    ok = ok and all(GA.commutes(om, GA.gen(i), sqC) for i in range(5))
    omp_inv = GA.scal(1 / GA.mul(omp, GA.reverse(omp), sqC)[()], GA.reverse(omp))
    ok = ok and GA.eq(GA.mul(omp_inv, omp, sqC), GA.sc(1)) and GA.eq(GA.mul(omp_inv, om, sqC), e5)
    _tp_rv = (ok); assert _tp_rv is not False, "check_fifth_generator_alone_differs"; return _tp_rv
