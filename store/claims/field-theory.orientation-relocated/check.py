"""field-theory.orientation-relocated: exact checks in the blade engine (Cl(2,4), Fraction).

The conformal spinor module of Cl(2,4) is taken from the premise's exported construction: P, the even
half T = Cl+(2,4) P and the odd half T' = Cl-(2,4) P (real dimension 8 each). I4 = gamma_0123,
I6 = gamma_0123 e_+ e_-, E = e_+ e_-, n_0 = (e_- - e_+)/2.
(1) Left multiplication by e_+ maps T onto T' (the images of a basis of T are a basis of T'), commutes
with I4 and with Lorentz rotors (boost, rotation, a product), and anticommutes with E, so it swaps the
E = +1 and E = -1 doublets (checked on the computed doublets).
(2) J = right multiplication by I6 commutes with left multiplication by every generator, preserves T
and T', and equals +left I6 on T and -left I6 on T'. The real-linear maps T -> T' commuting with all
15 bivectors and intertwining J with J form the zero space (inequivalent halves: conformal spinors and
their duals), while with left I6 on both sides they form a 2-dimensional space (equivalent). The
momentum doublet ker n_0 has real dimension 4 in each half and is the E = +1 doublet in both; on it
J = +I4 in T and J = -I4 in T'.
(3) The commutant fixes the unit only up to sign (premise: commutant span{1, I6}): with -J in place of
J the I4-linear momentum doublet is the one in T', and the I4-conjugate one is in T.
"""
from fractions import Fraction as F

import GA
from GA import mul, add, sub, neg, sc, gen, eq, commutes, anticommutes, all_blades
from tp_premise import premise

ROTORS = [((F(5, 4), F(3, 4), (0, 1)),), ((F(3, 5), F(4, 5), (1, 2)),),
          ((F(5, 4), F(3, 4), (0, 2)), (F(3, 5), F(4, 5), (2, 3)))]


def setup():
    d = premise("field-theory.where-each-lives")["twistor_data"]()
    return d


# Spinors of each half on which -J is tested (the first N_SAMPLE_SPINORS basis elements of T and T').
N_SAMPLE_SPINORS = 2


def momentum_n0(d):
    """n_0 = (e_- - e_+)/2 in the premise's labelling (e_+ = gen 4, e_- = gen 5)."""
    return d["scl"](F(1, 2), sub(gen(5), gen(4)))


def rotor(d, factors):
    R = sc(1)
    for c, s, b in factors:
        R = mul(R, add(sc(c), d["scl"](s, d["blade"](b))), d["S6"])
    return R


def doublet(d, basis, sign):
    S6 = d["S6"]
    return d["kernel_of_images"]([sub(mul(d["E"], z, S6), d["scl"](sign, z)) for z in basis], basis)


def intertwiner_dim(d, src, dst, unit_src, unit_dst):
    """dim of real-linear M: span(src) -> span(dst) with M b z = b M z for all bivectors b and
    M unit_src(z) = unit_dst(M z)."""
    S6, AB, co = d["S6"], d["ALLB6"], d["coords"]
    gens = [d["blade"](b) for b in all_blades(6) if len(b) == 2]
    ops = [(lambda z, g=g: mul(g, z, S6), lambda z, g=g: mul(g, z, S6)) for g in gens]
    ops.append((unit_src, unit_dst))
    n = len(src)
    rows = []
    for A_src, A_dst in ops:
        As = [co(A_src(z), src, AB) for z in src]
        Ad = [co(A_dst(z), dst, AB) for z in dst]
        for j in range(n):
            for r in range(n):
                row = [F(0)] * (n * n)
                for i in range(n):
                    row[r * n + i] += As[j][i]
                    row[i * n + j] -= Ad[i][r]
                rows.append(row)
    return len(GA.field_kernel(rows))


def check_e_plus_maps_halves_and_swaps_doublets():
    d = setup()
    S6, AB, T, Tp = d["S6"], d["ALLB6"], d["S"], d["Sodd"]
    ep = gen(4)
    imgs = [mul(ep, z, S6) for z in T]
    assert d["span_rank"](imgs, AB) == 8 and d["span_rank"](Tp + imgs, AB) == 8
    assert commutes(ep, d["I4"], S6) and anticommutes(ep, d["E"], S6)
    for fac in ROTORS:
        R = rotor(d, fac)
        assert commutes(ep, R, S6)
    for sign in (1, -1):
        L = doublet(d, T, sign)
        Lp_other = doublet(d, Tp, -sign)
        assert len(L) == 4 and len(Lp_other) == 4
        moved = [mul(ep, z, S6) for z in L]
        assert d["span_rank"](moved + Lp_other, AB) == 4


def check_unit_J_distinguishes_halves():
    d = setup()
    S6, AB, T, Tp, I4, I6 = d["S6"], d["ALLB6"], d["S"], d["Sodd"], d["I4"], d["I6"]
    rI6 = lambda z: mul(z, I6, S6)
    lI6 = lambda z: mul(I6, z, S6)
    for z in T:
        assert eq(rI6(z), lI6(z)) and d["span_rank"](T + [rI6(z)], AB) == 8
    for z in Tp:
        assert eq(rI6(z), neg(lI6(z))) and d["span_rank"](Tp + [rI6(z)], AB) == 8
    for i in range(6):
        for z in (T[0], T[3], Tp[1]):
            assert eq(mul(gen(i), rI6(z), S6), rI6(mul(gen(i), z, S6)))
    assert intertwiner_dim(d, T, Tp, rI6, rI6) == 0
    assert intertwiner_dim(d, T, Tp, lI6, lI6) == 2
    n0 = d["scl"](F(1, 2), sub(gen(5), gen(4)))
    K0T = d["kernel_of_images"]([mul(n0, z, S6) for z in T], T)
    K0Tp = d["kernel_of_images"]([mul(n0, z, S6) for z in Tp], Tp)
    assert len(K0T) == 4 and len(K0Tp) == 4
    assert all(eq(mul(d["E"], z, S6), z) for z in K0T + K0Tp)
    assert all(eq(rI6(z), mul(I4, z, S6)) for z in K0T)
    assert all(eq(rI6(z), neg(mul(I4, z, S6))) for z in K0Tp)


def check_sign_of_unit_relocates_orientation():
    d = setup()
    S6, T, Tp, I4, I6 = d["S6"], d["S"], d["Sodd"], d["I4"], d["I6"]
    n0 = momentum_n0(d)
    K0T = d["kernel_of_images"]([mul(n0, z, S6) for z in T], T)
    K0Tp = d["kernel_of_images"]([mul(n0, z, S6) for z in Tp], Tp)
    assert len(K0T) == 4 and len(K0Tp) == 4          # the momentum doublet: real dimension 4 in each half
    mJ = lambda z: neg(mul(z, I6, S6))
    assert all(eq(mJ(z), mul(I4, z, S6)) for z in K0Tp)
    assert all(eq(mJ(z), neg(mul(I4, z, S6))) for z in K0T)
    # -J squares to -1 and commutes with the Clifford action just as J does
    for z in T[:N_SAMPLE_SPINORS] + Tp[:N_SAMPLE_SPINORS]:
        assert eq(mJ(mJ(z)), neg(z))
        assert eq(mul(gen(2), mJ(z), S6), mJ(mul(gen(2), z, S6)))
