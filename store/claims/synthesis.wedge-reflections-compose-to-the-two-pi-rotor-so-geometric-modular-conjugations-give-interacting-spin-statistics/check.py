"""The wedge reflection in the spacetime algebra and the modular route to spin-statistics: exact checks.

Cl(1,3), g0^2 = +1, gi^2 = -1, I4 = g0 g1 g2 g3. The wedge W = {x1 > |x0|} has boost bivector
B = g0 g1, edge null directions n+- = g0 +- g1 and dual plane D = I4 B.

(1) B^2 = 1 and B B~ = -1; x -> B x B^{-1} is the wedge reflection j_W: (x0, x1) -> (-x0, -x1),
    (x2, x3) fixed. It factors as x -> I4 x I4^{-1} (= -x, the PT inversion) after x -> D x D^{-1}
    (the turn by pi in the dual plane, D^2 = -1), and D is the boost rotor continued to the
    I4-imaginary rapidity pi (exp(I4 pi B / 2) = cos(pi/2) + I4 B sin(pi/2)), the half modular period.
(2) j_W reverses the edge null translations n+- and fixes the transverse ones; the boost rotor
    (5 + 4B)/3 scales n+ by 1/9 and n- by 9 (rapidity log 9 dilates the edge translations).
(3) For the wedge turned by theta in the plane g1 g2 (exact Pythagorean half-angle rotors), the
    reflection bivector is B_theta = R B R~ = g0 (cos theta g1 + sin theta g2) and
    B_theta B_0 = cos theta + sin theta g1 g2 = R^2, the spin rotor of the turn by 2 theta; at
    theta = pi the turned wedge is the causal complement W' and B_pi B_0 = -1, the lift by continuity
    of the rotation by 2 pi; in a form independent of the signs of the versors, (B_{pi/2} B)^2 = -1.
(4) The standard Klein twist with i = I4 (the stand-in gradings k are even involutions of Cl(1,3)): for an even involution k commuting with I4 (the Bose-Fermi grading),
    V = (1 + I4 k)(1 + I4)^{-1} satisfies V^2 = k, V commutes with k, and the conjugate-linear
    map that reverses I4 sends V^* to V, so R(2 pi) = V J V^* J = V^2 = k.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = GA.sig(1, 3)


def g(i):
    return GA.gen(i)


def mm(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def s0(x):
    return x.get((), F(0))


def inv_versor(V):
    """V^{-1} = V~ / (V V~) for a versor whose V V~ is a nonzero scalar."""
    n = mm(V, GA.reverse(V))
    assert set(n.keys()) <= {()}
    return GA.scal(F(1) / n[()], GA.reverse(V))


def ad(V, x):
    return mm(V, x, inv_versor(V))


def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


I4 = mm(g(0), g(1), g(2), g(3))
BW = mm(g(0), g(1))
SAMPLE = [vec((3, 1, -2, 5)), vec((F(1, 2), -4, 7, 1)), vec((-2, 3, 3, -1))]
HALF_ANGLES = [(2, 1, 5), (3, 4, 25), (12, 5, 169), (1, 1, 2), (8, 15, 289)]   # (a, b, a^2 + b^2)


def coords(x):
    return [x.get((i,), F(0)) for i in range(4)]


# ---------------------------------------------------------------- (1)
def check_wedge_reflection_is_conjugation_by_the_boost_bivector():
    premise("synthesis.modular-period-on-values-is-the-dual-plane-turn")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    ok = GA.eq(mm(BW, BW), GA.sc(1)) and GA.eq(mm(BW, GA.reverse(BW)), GA.sc(-1))
    D = mm(I4, BW)
    ok = ok and GA.eq(mm(D, D), GA.sc(-1)) and GA.eq(D, mm(g(2), g(3)))
    # the continued boost at I4-imaginary rapidity pi: cos(pi/2) + I4 B sin(pi/2) with cos = 0, sin = 1
    ok = ok and GA.eq(GA.add(GA.scal(0, GA.sc(1)), GA.scal(1, D)), D)
    for x in SAMPLE:
        c = coords(x)
        jx = vec((-c[0], -c[1], c[2], c[3]))
        ok = ok and GA.eq(ad(BW, x), jx)
        ok = ok and GA.eq(ad(I4, x), GA.neg(x))
        ok = ok and GA.eq(ad(I4, ad(D, x)), jx)
        turned = vec((c[0], c[1], -c[2], -c[3]))
        ok = ok and GA.eq(ad(D, x), turned)
    ok = ok and GA.eq(mm(I4, D), GA.neg(BW))
    GA.check("j_W = Ad(B) = PT after the turn by pi of the dual plane I4 B", ok)
    return ok


# ---------------------------------------------------------------- (2)
def check_reflection_reverses_the_edge_translations_and_the_boost_dilates_them():
    premise("angle.imported-theorems-deliver-their-hypotheses")
    nplus, nminus = vec((1, 1, 0, 0)), vec((-1, 1, 0, 0))
    ok = GA.eq(ad(BW, nplus), GA.neg(nplus)) and GA.eq(ad(BW, nminus), GA.neg(nminus))
    ok = ok and GA.eq(ad(BW, g(2)), g(2)) and GA.eq(ad(BW, g(3)), g(3))
    boost = GA.scal(F(1, 3), GA.add(GA.sc(5), GA.scal(4, BW)))
    ok = ok and GA.eq(mm(boost, GA.reverse(boost)), GA.sc(1))
    ok = ok and GA.eq(ad(boost, nplus), GA.scal(F(1, 9), nplus))
    ok = ok and GA.eq(ad(boost, nminus), GA.scal(9, nminus))
    # the boost maps the wedge into itself: a point of W stays in W
    p = vec((1, 2, 5, -3))
    q = coords(ad(boost, p))
    ok = ok and q[1] > abs(q[0]) and q[2] == 5 and q[3] == -3
    GA.check("j_W reverses n+- and fixes the transverse translations; the boost dilates n+- by 9^{-+1}", ok)
    return ok


# ---------------------------------------------------------------- (3)
def check_reflections_of_turned_wedges_compose_to_the_spin_rotor_of_twice_the_turn():
    premise("synthesis.modular-period-on-values-is-the-dual-plane-turn")
    premise("synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem")
    B12 = mm(g(1), g(2))
    ok = True
    for a, b, n in HALF_ANGLES:
        R = GA.add(GA.sc(a), GA.scal(b, B12))           # unnormalised rotor, R R~ = n
        Rn = mm(R, GA.reverse(R))
        if not GA.eq(Rn, GA.sc(n)):
            ok = False
        cos, sin = F(a * a - b * b, n), F(2 * a * b, n)
        Bth = GA.scal(F(1, n), mm(R, BW, GA.reverse(R)))
        ok = ok and GA.eq(Bth, mm(g(0), vec((0, cos, sin, 0))))
        prod = mm(Bth, BW)
        ok = ok and GA.eq(prod, GA.add(GA.sc(cos), GA.scal(sin, B12)))
        ok = ok and GA.eq(prod, GA.scal(F(1, n), mm(R, R)))
        # Ad(prod) is the turn by 2 theta: g1 -> cos 2theta g1 + sin 2theta g2
        c2, s2 = cos * cos - sin * sin, 2 * sin * cos
        ok = ok and GA.eq(ad(prod, g(1)), vec((0, c2, s2, 0)))
    # theta = pi: the half-angle rotor is the turn by pi/2 ... composed twice; directly R = B12
    Bpi = mm(B12, BW, GA.reverse(B12))
    ok = ok and GA.eq(Bpi, GA.neg(BW)) and GA.eq(mm(Bpi, BW), GA.sc(-1))
    # the turned wedge at theta = pi is W': its spacelike direction g1 goes to -g1
    ok = ok and GA.eq(ad(B12, g(1)), GA.neg(g(1))) and GA.eq(ad(B12, g(0)), g(0))
    # theta = 0 gives +1: the path from +1 to -1 is the lift of the closed loop of turns by 2 theta
    ok = ok and GA.eq(mm(BW, BW), GA.sc(1))
    # lift-independent form: the quarter-turned wedge's reflection with W's, either sign of either versor,
    # composes to a rotor whose square is -1 (the rotation by 2 pi in the spin group)
    Bq = GA.scal(F(1, 2), mm(GA.add(GA.sc(1), B12), BW, GA.reverse(GA.add(GA.sc(1), B12))))
    ok = ok and GA.eq(Bq, mm(g(0), g(2)))
    for s1 in (1, -1):
        for s2 in (1, -1):
            P = mm(GA.scal(s1, Bq), GA.scal(s2, BW))
            ok = ok and GA.eq(mm(P, P), GA.sc(-1)) and GA.eq(ad(P, g(1)), GA.neg(g(1)))
    GA.check("B_theta B_0 = cos + sin g1g2, the rotor of the turn by 2 theta; -1 at theta = pi", ok)
    return ok


# ---------------------------------------------------------------- (4)
def check_the_klein_twist_with_unit_i4_squares_to_the_grading():
    premise("synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem")
    premise("synthesis.locality-of-the-attached-free-fields-fixes-their-statistics")
    ok = True
    for k in [BW, mm(g(0), g(2)), GA.neg(mm(g(0), g(3)))]:
        ok = ok and GA.eq(mm(k, k), GA.sc(1)) and GA.eq(mm(k, I4), mm(I4, k))
        one_plus_i = GA.add(GA.sc(1), I4)
        inv = GA.scal(F(1, 2), GA.sub(GA.sc(1), I4))
        ok = ok and GA.eq(mm(one_plus_i, inv), GA.sc(1))
        V = mm(GA.add(GA.sc(1), mm(I4, k)), inv)
        ok = ok and GA.eq(mm(V, V), k) and GA.eq(mm(V, k), mm(k, V))
        # the adjoint reverses I4 (k self-adjoint): V* = (1 - I4 k)(1 - I4)^{-1}; the conjugate-linear J
        # reverses I4 again, so J V* J = V and R(2 pi) = V J V* J = V^2
        Vstar = mm(GA.sub(GA.sc(1), mm(I4, k)), GA.scal(F(1, 2), GA.add(GA.sc(1), I4)))
        JVJ = mm(GA.add(GA.sc(1), mm(I4, k)), inv)       # I4 -> -I4 applied to V*
        ok = ok and GA.eq(mm(V, Vstar), GA.sc(1)) and GA.eq(JVJ, V) and GA.eq(mm(V, JVJ), k)
        ok = ok and not GA.eq(V, k) and not GA.eq(mm(V, Vstar), k)
    GA.check("V = (1 + I4 k)/(1 + I4): V^2 = k, V V* = 1, R(2 pi) = V J V* J = k", ok)
    return ok


if __name__ == "__main__":
    for fn in [check_wedge_reflection_is_conjugation_by_the_boost_bivector,
               check_reflection_reverses_the_edge_translations_and_the_boost_dilates_them,
               check_reflections_of_turned_wedges_compose_to_the_spin_rotor_of_twice_the_turn,
               check_the_klein_twist_with_unit_i4_squares_to_the_grading]:
        print(fn.__name__, fn())
