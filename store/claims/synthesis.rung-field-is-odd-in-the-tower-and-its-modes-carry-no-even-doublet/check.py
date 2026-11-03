"""synthesis.rung-field-is-odd-in-the-tower-and-its-modes-carry-no-even-doublet: exact checks.

The two rung planes H_4, H_5 as Cl(2,2) with generators e_4, f_4, e_5, f_5 (squares +1, -1, +1, -1) and null pairs
v_a = (e_a + f_a)/2, w_a = (e_a - f_a)/2 (the tower's CAR, {v_a, w_b} = delta_ab); a fifth generator g, g^2 = 1,
stands for a generator outside the rung planes (as in synthesis.even-slots-need-a-spectator-generator (iv)).
The slot-mixing su(2) acts by commutators with the number-conserving bilinears t_j = sum v_a (sigma_j/2)_ab w_b
(the real elements t_1, t_3 and t_2' = [t_3, t_1] = i t_2), so the isospin Casimir on an element x is
C(x) = [t_1,[t_1,x]] + [t_3,[t_3,x]] - [t_2',[t_2',x]]. Exact arithmetic (GA engine over Fractions).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = (F(1), F(-1), F(1), F(-1), F(1))


def mul(x, y):
    return GA.mul(x, y, SQ)


def comm(a, b):
    return GA.sub(mul(a, b), mul(b, a))


V = {4: GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(1))), 5: GA.scal(F(1, 2), GA.add(GA.gen(2), GA.gen(3)))}
W = {4: GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(1))), 5: GA.scal(F(1, 2), GA.sub(GA.gen(2), GA.gen(3)))}
T1 = GA.scal(F(1, 2), GA.add(mul(V[4], W[5]), mul(V[5], W[4])))
T3 = GA.scal(F(1, 2), GA.sub(mul(V[4], W[4]), mul(V[5], W[5])))
T2P = comm(T3, T1)
NUM = GA.add(mul(V[4], W[4]), mul(V[5], W[5]))      # total rung mode number


def casimir(x):
    return GA.add(comm(T1, comm(T1, x)), comm(T3, comm(T3, x)), GA.neg(comm(T2P, comm(T2P, x))))


def span_blades(grades, gens):
    return [b for k in grades for b in combinations(gens, k)]


def nullity(op, blades, r):
    cols = [op({b: F(1)}) for b in blades]
    M = [[cols[j].get(b, F(0)) - (r if i == j else 0) for j, _ in enumerate(blades)] for i, b in enumerate(blades)]
    return len(blades) - GA.mat_rank(M)


def check_rung_modes_are_a_doublet_pair_of_the_slot_mixing():
    """Setting: the t_j close on su(2) ([t_3, t_1] = i t_2 with [t_3, t_2'] = t_1, read with i^2 = -1), the v_a are
    an isospin-1/2 doublet (Casimir 3/4, t_3 eigenvalues +-1/2) and the w_a the conjugate doublet; the mode number
    commutes with the t_j."""
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    premise("field-theory.imported-tower-limit")
    for a in (4, 5):
        GA.check("v_a, w_a null", GA.is_zero(mul(V[a], V[a])) and GA.is_zero(mul(W[a], W[a])))
        for b in (4, 5):
            GA.check("CAR {v_a, w_b} = delta_ab", GA.eq(GA.add(mul(V[a], W[b]), mul(W[b], V[a])), GA.sc(1 if a == b else 0)))
        GA.check("v_a doublet, w_a doublet", GA.eq(casimir(V[a]), GA.scal(F(3, 4), V[a]))
                 and GA.eq(casimir(W[a]), GA.scal(F(3, 4), W[a])))
    GA.check("t_3 v_4 = +1/2 v_4, t_3 v_5 = -1/2 v_5", GA.eq(comm(T3, V[4]), GA.scal(F(1, 2), V[4]))
             and GA.eq(comm(T3, V[5]), GA.scal(F(-1, 2), V[5])))
    GA.check("[t_3, t_2'] = t_1 (su(2): [t_3, t_2] = -i t_1 with t_2' = i t_2)", GA.eq(comm(T3, T2P), T1))
    GA.check("mode number is invariant", all(GA.is_zero(comm(t, NUM)) for t in (T1, T2P, T3)))
    return True


def check_even_rung_algebra_has_no_doublet():
    """(2): on the sixteen-dimensional algebra of the two rung planes the isospin Casimir has spectrum
    0 (multiplicity 5) and 2 (multiplicity 3) on the even part, 3/4 (multiplicity 8) on the odd part, and nothing else:
    an element is a doublet only if it is odd."""
    premise("standard-model.ten-transported-ambient-space-doublets-are")
    even = span_blades((0, 2, 4), range(4))
    odd = span_blades((1, 3), range(4))
    GA.check("eight even, eight odd blades", len(even) == 8 and len(odd) == 8)

    def cas_even(x):
        return casimir(x)
    GA.check("even part: Casimir 0 five times, 2 three times",
             nullity(cas_even, even, F(0)) == 5 and nullity(cas_even, even, F(2)) == 3)
    GA.check("even part: no isospin 1/2", nullity(cas_even, even, F(3, 4)) == 0)
    GA.check("odd part: all isospin 1/2", nullity(cas_even, odd, F(3, 4)) == 8)
    GA.check("Casimir preserves parity",
             all(all(len(bb) % 2 == len(b) % 2 for bb in casimir({b: F(1)})) for b in even + odd))
    return True


def fock_vacuum(x):
    """omega(x) for the Fock state annihilated by w_4, w_5: projector P = w_4 v_4 w_5 v_5, omega(x) = <P x P>_0/<P>_0."""
    P = mul(mul(W[4], V[4]), mul(W[5], V[5]))
    return mul(mul(P, x), P).get((), F(0)) / P.get((), F(0))


def check_rung_field_is_odd_and_its_invariants_are_even_expectations():
    """(1): for c = sum (alpha_a v_a + beta_a w_a) (real samples; the I4-complex case is the same computation over
    span{1, I4}, which commutes with the rung vectors) c is odd, the grading-invariant Fock vacuum gives omega(c) = 0
    and omega(odd blade) = 0, c^2 = Q(c) = alpha . beta, {c*, c} = 2N with c* = beta . v + alpha . w (real
    coefficients), and omega(c* c) = |alpha|^2, omega(c c*) = |beta|^2, so N and m = (|alpha|^2 - |beta|^2)/2 are
    vacuum expectations of even bilinears while the doublet c has none."""
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("field-theory.imported-tower-limit")
    for al, be in (((F(1, 2), F(-3)), (F(2), F(1, 3))), ((F(-1), F(5, 4)), (F(3, 7), F(2)))):
        c = GA.add(GA.scal(al[0], V[4]), GA.scal(al[1], V[5]), GA.scal(be[0], W[4]), GA.scal(be[1], W[5]))
        cs = GA.add(GA.scal(be[0], V[4]), GA.scal(be[1], V[5]), GA.scal(al[0], W[4]), GA.scal(al[1], W[5]))
        A = al[0] ** 2 + al[1] ** 2
        B = be[0] ** 2 + be[1] ** 2
        GA.check("c is odd", all(len(b) % 2 == 1 for b in c))
        GA.check("c^2 = Q(c)", GA.eq(mul(c, c), GA.sc(al[0] * be[0] + al[1] * be[1])))
        GA.check("{c*, c} = 2N", GA.eq(GA.add(mul(cs, c), mul(c, cs)), GA.sc(A + B)))
        GA.check("omega(c) = 0", fock_vacuum(c) == 0)
        GA.check("omega(c* c) = |alpha|^2, omega(c c*) = |beta|^2", fock_vacuum(mul(cs, c)) == A and fock_vacuum(mul(c, cs)) == B)
        GA.check("m = (omega(c* c) - omega(c c*))/2", (fock_vacuum(mul(cs, c)) - fock_vacuum(mul(c, cs))) / 2 == (A - B) / 2)
    GA.check("the vacuum vanishes on every odd blade", all(fock_vacuum({b: F(1)}) == 0 for b in span_blades((1, 3), range(4))))
    GA.check("the vacuum is normalised and even", fock_vacuum(GA.sc(1)) == 1)
    return True


def check_spectator_doublet_is_even_and_two_level():
    """(3): with g (g^2 = 1) anticommuting with the rung vectors and commuting with the t_j, x_a = v_a g is even, an
    isospin doublet, x_a* = g w_a, and {x_a, x_b*} = delta_ab, {x_a, x_b} = 0, x_a^2 = 0, [x_a, x_a*] = 2 n_a - 1: the canonical anticommutation
    relations, not the CCR."""
    premise("synthesis.even-slots-need-a-spectator-generator")
    g = GA.gen(4)
    GA.check("g anticommutes with the rung vectors, commutes with the t_j",
             all(GA.anticommutes(g, X[a], SQ) for X in (V, W) for a in (4, 5))
             and all(GA.commutes(g, t, SQ) for t in (T1, T2P, T3)))
    x = {a: mul(V[a], g) for a in (4, 5)}
    xs = {a: mul(g, W[a]) for a in (4, 5)}
    GA.check("x_a even", all(all(len(b) % 2 == 0 for b in x[a]) for a in (4, 5)))
    GA.check("x_a doublet", all(GA.eq(casimir(x[a]), GA.scal(F(3, 4), x[a])) for a in (4, 5)))
    for a in (4, 5):
        GA.check("x_a^2 = 0", GA.is_zero(mul(x[a], x[a])))
        for b in (4, 5):
            GA.check("{x_a, x_b*} = delta_ab", GA.eq(GA.add(mul(x[a], xs[b]), mul(xs[b], x[a])), GA.sc(1 if a == b else 0)))
            GA.check("{x_a, x_b} = 0", GA.is_zero(GA.add(mul(x[a], x[b]), mul(x[b], x[a]))))
    GA.check("not the CCR: [x_4, x_4*] = 2 n_4 - 1, not 1",
             GA.eq(comm(x[4], xs[4]), GA.sub(GA.scal(2, mul(V[4], W[4])), GA.sc(1))) and not GA.eq(comm(x[4], xs[4]), GA.sc(1)))
    return True


def check_time_direction_gives_a_doublet_that_is_not_a_lorentz_scalar():
    """(3), the requirement on g: in Cl(3,5) (gamma_0 .. gamma_3, then e_a, f_a for a = 4, 5) the time direction
    gamma_0 squares to 1 and anticommutes with the rung vectors, so x_a = v_a gamma_0 is even and obeys
    {x_a, x_b*} = delta_ab with x_b* = gamma_0 w_b; but the boost bivector gamma_0 gamma_1 does not commute with x_a
    ([gamma_0 gamma_1, x_a] = 2 gamma_0 gamma_1 x_a), so x_a is not a Lorentz scalar."""
    premise("synthesis.even-slots-need-a-spectator-generator")
    sq = tuple(F(x) for x in (1, -1, -1, -1, 1, -1, 1, -1))

    def m8(x, y):
        return GA.mul(x, y, sq)
    v = {a: GA.scal(F(1, 2), GA.add(GA.gen(e), GA.gen(e + 1))) for a, e in ((4, 4), (5, 6))}
    w = {a: GA.scal(F(1, 2), GA.sub(GA.gen(e), GA.gen(e + 1))) for a, e in ((4, 4), (5, 6))}
    g0 = GA.gen(0)
    GA.check("gamma_0^2 = 1", GA.eq(m8(g0, g0), GA.sc(1)))
    GA.check("gamma_0 anticommutes with the rung vectors",
             all(GA.anticommutes(g0, X[a], sq) for X in (v, w) for a in (4, 5)))
    x = {a: m8(v[a], g0) for a in (4, 5)}
    xs = {a: m8(g0, w[a]) for a in (4, 5)}
    GA.check("x_a even", all(all(len(bl) % 2 == 0 for bl in x[a]) for a in (4, 5)))
    for a in (4, 5):
        for b in (4, 5):
            GA.check("{x_a, x_b*} = delta_ab", GA.eq(GA.add(m8(x[a], xs[b]), m8(xs[b], x[a])), GA.sc(1 if a == b else 0)))
    B01 = m8(GA.gen(0), GA.gen(1))
    for a in (4, 5):
        cm = GA.sub(m8(B01, x[a]), m8(x[a], B01))
        GA.check("[gamma_01, x_a] = 2 gamma_01 x_a, nonzero: not a Lorentz scalar",
                 GA.eq(cm, GA.scal(2, m8(B01, x[a]))) and not GA.is_zero(cm))
    return True
