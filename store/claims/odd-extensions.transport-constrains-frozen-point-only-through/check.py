"""odd-extensions.transport-constrains-frozen-point-only-through: exact checks.

The rung as GA's Cl(2,4) (e_0 +1; e_1, e_2, e_3 -1; e_4 +1; e_5 -1); the null frozen point I = e_4 + e_5 and
W = I^perp = span{e_0..e_3, I}, signature (1,3;1).
(i) The conditions on x in R^{2,4}: <x, e_mu> = 0 (mu = 0..3) and <x, I> = 1 have rank 5; the solution set is the
    line phi + c I with phi = (e_4 - e_5)/2, and Q(phi + c I) = 2c (checked at sample c and as the affine identity),
    so the null solution is unique: phi. Gram of {e_0..e_3, I, phi} has signature (2,4): the completion is the rung.
(ii) a I + b phi is orthogonal to the frame with norm 2ab for sample (a, b) of both signs and zero.
(iii) Isometries of the plane in the null basis (Gram [[0,1],[1,0]]): M = [[p, q], [r, s]] preserves it iff
    pr = qs = 0 and ps + qr = 1; for sample M of both kinds (boost, swap times boost, with -1) and sample x,
    Q(Mx) = Q(x); for sample pairs with equal norm (nonzero of both signs, and null) an explicit isometry maps
    one to the other: the orbits are the level sets of the norm.
(iv) Cl(1,4) and Cl(2,3) (the two intermediate algebras) are not isomorphic: omega^2 = +1 and -1, so the centre
    span{1, omega} is R + R, respectively C (computed: omega central, its square).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
I0 = {(4,): F(1), (5,): F(1)}
CS = [F(0), F(3), F(-2, 5)]
AB = [(F(2), F(3)), (F(-1), F(4)), (F(5, 2), F(-2)), (F(0), F(7)), (F(1, 3), F(0))]
MATS = [[[F(3), F(0)], [F(0), F(1, 3)]], [[F(0), F(2)], [F(1, 2), F(0)]], [[F(-5), F(0)], [F(0), F(-1, 5)]],
        [[F(0), F(-1, 4)], [F(-4), F(0)]]]
PAIRS_EQ = [((F(2), F(3)), (F(-6), F(-1))), ((F(1), F(-2)), (F(4), F(-1, 2))), ((F(5), F(0)), (F(0), F(-3))),
            ((F(0), F(2)), (F(7), F(0)))]


def vec(cs):
    return {(i,): F(x) for i, x in enumerate(cs) if x}


def dot(a, b):
    return GA.dot(a, b, SQ)


def qnull(M, a, b):
    """Norm 2ab of (a, b) in the null basis after applying M (columns: images of I and phi)."""
    a2 = M[0][0] * a + M[0][1] * b
    b2 = M[1][0] * a + M[1][1] * b
    return 2 * a2 * b2


def check_unique_canonical_partner():
    premise("odd-extensions.imported-minimal-completion-degenerate-algebra-rule")
    frame = [GA.gen(i) for i in range(4)]
    rows = [[dot(f, GA.gen(i)) for i in range(6)] for f in frame] + [[dot(I0, GA.gen(i)) for i in range(6)]]
    ok = GA.rank_of_vectors(rows) == 5
    phi = vec([0, 0, 0, 0, F(1, 2), F(-1, 2)])
    ok = ok and all(dot(phi, f) == 0 for f in frame) and dot(phi, I0) == 1 and dot(phi, phi) == 0
    ker = GA.field_kernel(rows)
    ok = ok and len(ker) == 1 and GA.rank_of_vectors([ker[0], [I0.get((i,), F(0)) for i in range(6)]]) == 1
    for c in CS:
        x = GA.add(phi, GA.scal(c, I0))
        ok = ok and dot(x, x) == 2 * c and (dot(x, x) == 0) == (c == 0)
    G = [[dot(a, b) for b in frame + [I0, phi]] for a in frame + [I0, phi]]
    ok = ok and GA.congruence_signature(G) == (2, 4, 0)
    Gw = [[dot(a, b) for b in frame + [I0]] for a in frame + [I0]]
    ok = ok and GA.congruence_signature(Gw) == (1, 3, 1)
    GA.check("the completion of (1,3;1) is (2,4) with a unique null partner phi of I", ok)
    return ok


def check_norm_is_two_ab():
    premise("odd-extensions.imported-minimal-completion-degenerate-algebra-rule")
    phi = vec([0, 0, 0, 0, F(1, 2), F(-1, 2)])
    ok = True
    for a, b in AB:
        x = GA.add(GA.scal(a, I0), GA.scal(b, phi))
        ok = ok and all(dot(x, GA.gen(i)) == 0 for i in range(4))
        ok = ok and dot(x, x) == 2 * a * b
    signs = {(a * b > 0) - (a * b < 0) for a, b in AB}
    ok = ok and signs == {1, -1, 0}
    GA.check("a I + b phi has norm 2ab: the sign of Lambda is the sign of ab", ok)
    return ok


def check_orbits_are_level_sets():
    premise("odd-extensions.imported-minimal-completion-degenerate-algebra-rule")
    ok = True
    for M in MATS:
        p, q, r, s = M[0][0], M[0][1], M[1][0], M[1][1]
        ok = ok and p * r == 0 and q * s == 0 and p * s + q * r == 1
        ok = ok and all(qnull(M, a, b) == 2 * a * b for a, b in AB)
    # a non-isometry fails
    bad = [[F(2), F(0)], [F(0), F(1)]]
    ok = ok and any(qnull(bad, a, b) != 2 * a * b for a, b in AB)
    for (a, b), (a2, b2) in PAIRS_EQ:
        ok = ok and a * b == a2 * b2
        if a != 0 and a2 != 0:
            t = a2 / a
            M = [[t, F(0)], [F(0), 1 / t]]
        elif a != 0:          # (a, 0) -> (0, b2): boost then swap
            t = b2 / a
            M = [[F(0), 1 / t], [t, F(0)]]
        else:                 # (0, b) -> (a2, 0)
            t = a2 / b
            M = [[F(0), t], [1 / t, F(0)]]
        ok = ok and M[0][0] * M[1][0] == 0 and M[0][1] * M[1][1] == 0
        ok = ok and M[0][0] * M[1][1] + M[0][1] * M[1][0] == 1
        ok = ok and [M[0][0] * a + M[0][1] * b, M[1][0] * a + M[1][1] * b] == [a2, b2]
    GA.check("O(1,1) preserves 2ab and is transitive on each level set: the norm is the only invariant", ok)
    return ok


def check_two_signs_non_isomorphic():
    premise("odd-extensions.twistor-algebra")
    out = {}
    for p, q in ((1, 4), (2, 3)):
        sq = GA.sig(p, q)
        om = {tuple(range(5)): F(1)}
        central = all(GA.commutes(om, GA.gen(i), sq) for i in range(5))
        out[(p, q)] = (central, GA.mul(om, om, sq))
    ok = out[(1, 4)] == (True, GA.sc(1)) and out[(2, 3)] == (True, GA.sc(-1))
    GA.check("Cl(1,4) has centre R+R (omega^2 = 1), Cl(2,3) centre C (omega^2 = -1): not isomorphic", ok)
    return ok
