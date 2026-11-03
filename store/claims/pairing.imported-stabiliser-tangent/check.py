"""pairing.imported-stabiliser-tangent: exact checks on the real Fock space of nu = 2, 3, 4 modes.

Jordan-Wigner annihilators a_j on the 2^nu basis states (exact Fraction matrices), the Majorana
generators e_{2j} = a_j + a_j^dag, e_{2j+1} = a_j - a_j^dag (squares +1 and -1: a real form of the
Clifford algebra of rank 2 nu), and the bivectors e_a e_b, a < b.
  (1) The quadratic operators split the bivector algebra: hops a_i^dag a_j (i != j), Cartan elements
      a_i^dag a_i - 1/2, pair annihilations a_i a_j and pair creations a_i^dag a_j^dag (i < j) are
      nu(2nu - 1) operators spanning exactly the span of the bivectors (equal ranks, also jointly).
  (2) On the vacuum: hops with i != j and annihilations give 0, Cartan elements give -1/2 |0>, and
      the creations give nu(nu - 1)/2 independent states orthogonal to |0>.
  (3) The stabiliser of the vacuum ray, {B : B|0> in R|0>} inside the bivector span, has dimension
      nu^2 + nu(nu - 1)/2 (hops, Cartan, annihilations), so the tangent of the orbit has dimension
      nu(2nu - 1) minus that, nu(nu - 1)/2.
  (4) Rotations: the hop generator K_h = a_1^dag a_2 - a_2^dag a_1 kills |0>, and its rotation
      1 + s K_h + (1 - c) K_h^2 (K_h^3 = -K_h) is orthogonal and fixes |0>; the pairing generator
      K = a_1^dag a_2^dag + a_1 a_2 satisfies K^3 = -K, and at (c, s) = (3/5, 4/5) the rotation
      1 + s K + (1 - c) K^2 is orthogonal and sends |0> to 3/5 |0> + 4/5 |12>, |12> = a_1^dag a_2^dag |0>.
The claim restates the singularity paper's results; the functions testing them call premise() for
singularity.l-stabiliser-tangent (stabiliser and tangent) and
singularity.envelope-endpoint-why-boundary-mode-locality (the witness rotation). The literature entity
pairing.imported-stabiliser-tangent-external and the Thouless form are not used.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock
from tp_premise import premise

NUS = (2, 3, 4)


def ann(j, nu):
    """a_j on nu Jordan-Wigner modes, dense (LSB bitmask basis)."""
    return fock.to_dense(fock.ann(j, nu), 2 ** nu)


def T(M):
    return [list(r) for r in zip(*M)]


mm = GA.mat_mul


def madd(A, B, c=1):
    return [[a + c * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def eye(d, c=1):
    return [[F(c) if i == j else F(0) for j in range(d)] for i in range(d)]


def flat(M):
    return [x for r in M for x in r]


def col0(M):
    return [r[0] for r in M]


def ops(nu):
    a = [ann(j, nu) for j in range(nu)]
    ad = [T(x) for x in a]
    d = 2 ** nu
    maj = []
    for j in range(nu):
        maj += [madd(a[j], ad[j]), madd(a[j], ad[j], -1)]
    biv = [mm(maj[x], maj[y]) for x, y in combinations(range(2 * nu), 2)]
    hops = [mm(ad[i], a[j]) for i in range(nu) for j in range(nu) if i != j]
    cart = [madd(mm(ad[i], a[i]), eye(d, F(1, 2)), -1) for i in range(nu)]
    anns = [mm(a[i], a[j]) for i, j in combinations(range(nu), 2)]
    cres = [mm(ad[i], ad[j]) for i, j in combinations(range(nu), 2)]
    return a, ad, biv, hops, cart, anns, cres


def check_quadratic_operators_span_the_bivectors():
    ok = True
    for nu in NUS:
        a, ad, biv, hops, cart, anns, cres = ops(nu)
        quad = hops + cart + anns + cres
        dim = nu * (2 * nu - 1)
        ok = ok and len(quad) == dim and len(biv) == dim
        rb = GA.field_rank([flat(x) for x in biv])
        rq = GA.field_rank([flat(x) for x in quad])
        rj = GA.field_rank([flat(x) for x in biv + quad])
        ok = ok and rb == dim and rq == dim and rj == dim
    GA.check("hops, Cartan elements, pair annihilations and creations span so(2 nu) (nu = 2, 3, 4)", ok)
    return ok


def check_action_on_the_vacuum():
    premise("singularity.l-stabiliser-tangent")
    ok = True
    for nu in NUS:
        a, ad, biv, hops, cart, anns, cres = ops(nu)
        d = 2 ** nu
        vac = [F(1)] + [F(0)] * (d - 1)
        ok = ok and all(col0(h) == [F(0)] * d for h in hops + anns)
        ok = ok and all(col0(c) == [F(-1, 2)] + [F(0)] * (d - 1) for c in cart)
        imgs = [col0(c) for c in cres]
        ok = ok and all(v[0] == 0 for v in imgs)
        ok = ok and GA.field_rank(imgs) == nu * (nu - 1) // 2
        ok = ok and GA.field_rank(imgs + [vac]) == nu * (nu - 1) // 2 + 1
    GA.check("on |0>: hops and annihilations vanish, Cartan = -1/2, creations give nu(nu-1)/2 new directions", ok)
    return ok


def check_stabiliser_and_tangent_dimensions():
    premise("singularity.l-stabiliser-tangent")
    ok = True
    for nu in NUS:
        a, ad, biv, hops, cart, anns, cres = ops(nu)
        d = 2 ** nu
        # B = sum c_k biv_k; condition: components 1..d-1 of B|0> vanish
        cols = [col0(b)[1:] for b in biv]
        M = [[cols[k][i] for k in range(len(biv))] for i in range(d - 1)]
        stab = len(biv) - GA.field_rank(M)
        ok = ok and stab == nu * nu + nu * (nu - 1) // 2
        ok = ok and len(biv) - stab == nu * (nu - 1) // 2
    GA.check("the stabiliser of the vacuum ray has dimension nu^2 + nu(nu-1)/2; the tangent nu(nu-1)/2", ok)
    return ok


def check_hop_rotation_fixes_and_pairing_rotation_moves_the_vacuum():
    premise("singularity.envelope-endpoint-why-boundary-mode-locality")
    ok = True
    for nu in NUS:
        a, ad, biv, hops, cart, anns, cres = ops(nu)
        d = 2 ** nu
        vac = [F(1)] + [F(0)] * (d - 1)
        Kh = madd(mm(ad[0], a[1]), mm(ad[1], a[0]), -1)
        K = madd(mm(ad[0], ad[1]), mm(a[0], a[1]))
        c, s = F(3, 5), F(4, 5)
        for G, fixes in ((Kh, True), (K, False)):
            G2 = mm(G, G)
            ok = ok and mm(G2, G) == [[-x for x in r] for r in G]
            ok = ok and T(G) == [[-x for x in r] for r in G]
            U = madd(madd(eye(d), G, s), G2, 1 - c)
            ok = ok and mm(T(U), U) == eye(d)
            if fixes:
                ok = ok and col0(U) == vac
            else:
                pair = col0(mm(ad[0], ad[1]))
                want = [c * v + s * p for v, p in zip(vac, pair)]
                ok = ok and col0(U) == want and pair[3] != 0
    GA.check("a hop rotation fixes |0>; the pairing rotation at (3/5, 4/5) sends |0> to 3/5|0> + 4/5|12>", ok)
    return ok
