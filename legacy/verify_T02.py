#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T02.py: exact-arithmetic verification of the computational identities of

    "Projective Completes to Conformal"  (Transport Papers T2)

in the style of the series' verification scripts: the shared library's
basis-blade Clifford product over exact rationals, with degenerate
generators.  Every check is reported PASS/FAIL and the script exits nonzero on
any failure.  No floating point is used anywhere.
Shared machinery (the blade engine, exact linear algebra, rational functions,
the exterior model and the check harness) lives in GA.py, deposited alongside.

Coverage (labels refer to the note):
  [Prop 2.5] the radical ideal of Cl(3,0,1): dim J = 8, all 64 ideal
             products vanish (the corank-one, square-zero case)
  [Prop 2.5] the nilpotency profile at r = 2 in Cl(2,1,2): dim J = 24,
             J^2 != 0 with dim J^2 = 8, and J^3 = 0
  [Thm 2.3]  the model completion of PGA: Gram nondegenerate (rank 5) with
             signature (4,1); an r = 2 instance Cl(2,1,2) -> signature (4,3)
  [Thm 2.3]  the embedding e_i -> f_i, e_0 -> n_inf: isometry of the
             degenerate form (all pairs) and algebra map on all 256 blade
             products
  [Prop 2.5] the unit ideal in the completion: n_inf phi + phi n_inf = 1 for the
             normalised partner phi = -n_0/2
  [Ex 3.2]   translators: T_s T_t = T_{s+t} in PGA; the image of T_t equals
             CGA's 1 - (1/2) t n_inf; phi respects composition and the
             sandwich action on a sample vector, which the translator is
             checked to move (the check is not vacuous)
  [Thm 2.3]  the radical pairing: Q(n_inf, W) = 0 yet Q(n_inf, n_0) != 0
             (the minimality argument's injectivity, instantiated)
"""

from fractions import Fraction
from itertools import combinations
import sys

import GA as g


# ---------------------------------------------------------------------------
# PGA and CGA setups
# ---------------------------------------------------------------------------

PGA = g.sig(3, 0, 1)     # e1,e2,e3 at indices 0,1,2 (square +1); e0 at index 3 (square 0)
CGA = g.sig(4, 1)        # f1..f4 at 0..3 (square +1); f5 at 4 (square -1)

N_INF = g.add(g.gen(3), g.gen(4))                       # f4 + f5, null
N_0 = g.scal(Fraction(1, 2), g.sub(g.gen(4), g.gen(3)))   # (f5 - f4)/2, null, n_inf . n_0 = -1


def phi(x):
    """The embedding Cl(3,0,1) -> Cl(4,1): e_i -> f_i, e_0 -> n_inf, extended bladewise."""
    images = [g.gen(0), g.gen(1), g.gen(2), N_INF]
    out = {}
    for b, c in x.items():
        img = g.sc(1)
        for idx in b:
            img = g.mul(img, images[idx], CGA)
        for bb, cc in g.scal(c, img).items():
            out[bb] = out.get(bb, Fraction(0)) + cc
    return {b: c for b, c in out.items() if c != 0}


def ideal_checks():
    e0 = g.gen(3)
    Jbasis = [g.mul({I: Fraction(1)}, e0, PGA) for I in g.all_blades(3)]
    vecs = [[x.get(b, Fraction(0)) for b in g.all_blades(4)] for x in Jbasis]
    g.check("[Prop 2.5] Cl(3,0,1): ideal J = Cl e0 has dimension exactly 8",
          g.rank_of_vectors(vecs) == 8)
    ok = all(g.is_zero(g.mul(x, y, PGA)) for x in Jbasis for y in Jbasis)
    g.check("[Prop 2.5] r = 1: J^2 = 0 (all 64 ideal products vanish)", ok)


def nilpotency_checks():
    # r = 2 instance Cl(2,1,2): generators 0,1 square +1, 2 squares -1,
    # 3 and 4 are the radical letters rho_1, rho_2
    S = g.sig(2, 1, 2)
    rhos = [g.gen(3), g.gen(4)]
    Jbasis = []
    for I in g.all_blades(5):
        for r in rhos:
            x = g.mul({I: Fraction(1)}, r, S)
            if not g.is_zero(x):
                Jbasis.append(x)
    allb = g.all_blades(5)
    vecs = [[x.get(b, Fraction(0)) for b in allb] for x in Jbasis]
    g.check("[Prop 2.5] r = 2: dim J = 24 = 2^5 - 2^3", g.rank_of_vectors(vecs) == 24)
    g.check("[Prop 2.5] r = 2: rho_1 rho_2 != 0, so J^2 != 0 (the ideal is not square-zero)",
          not g.is_zero(g.mul(rhos[0], rhos[1], S)))
    J2 = [g.mul(x, y, S) for x in Jbasis for y in Jbasis]
    J2 = [z for z in J2 if not g.is_zero(z)]
    vecs2 = [[z.get(b, Fraction(0)) for b in allb] for z in J2]
    g.check("[Prop 2.5] r = 2: dim J^2 = 8 (blades carrying both radical letters)",
          g.rank_of_vectors(vecs2) == 8)
    ok = all(g.is_zero(g.mul(z, x, S)) for z in J2 for x in Jbasis)
    g.check("[Prop 2.5] r = 2: J^3 = 0 (every J^2 times J product vanishes)", ok)


def completion_gram_checks():
    # model completion of PGA: basis (e1,e2,e3, rho, phi) with rho the radical, phi its dual
    G = [[Fraction(0)] * 5 for _ in range(5)]
    for i in range(3):
        G[i][i] = Fraction(1)
    G[3][4] = G[4][3] = Fraction(1)   # the hyperbolic pairing rho.phi = 1 (any nonzero scale)
    g.check("[Thm 2.3] model completion of PGA: Gram rank 5 (nondegenerate)", g.rank_of_vectors(G) == 5)
    g.check("[Thm 2.3] model completion of PGA: signature (4,1)", g.congruence_signature(G) == (4, 1, 0))
    # r = 2 instance: Cl(2,1,2) -> signature (4,3)
    G2 = [[Fraction(0)] * 7 for _ in range(7)]
    G2[0][0] = G2[1][1] = Fraction(1)
    G2[2][2] = Fraction(-1)
    G2[3][5] = G2[5][3] = Fraction(1)
    G2[4][6] = G2[6][4] = Fraction(1)
    g.check("[Thm 2.3] r = 2 instance Cl(2,1,2): completion signature (4,3), rank 7",
          g.congruence_signature(G2) == (4, 3, 0) and g.rank_of_vectors(G2) == 7)


def embedding_checks():
    gens_pga = [g.gen(0), g.gen(1), g.gen(2), g.gen(3)]
    imgs = [g.gen(0), g.gen(1), g.gen(2), N_INF]
    ok = True
    for i in range(4):
        for j in range(4):
            ok = ok and g.dot(gens_pga[i], gens_pga[j], PGA) == g.dot(imgs[i], imgs[j], CGA)
    g.check("[Thm 2.3] e_i -> f_i, e_0 -> n_inf is an isometry of the degenerate form (all 10 pairs)", ok)
    blades = g.all_blades(4)
    ok = True
    for I in blades:
        for J in blades:
            lhs = phi(g.mul({I: Fraction(1)}, {J: Fraction(1)}, PGA))
            rhs = g.mul(phi({I: Fraction(1)}), phi({J: Fraction(1)}), CGA)
            ok = ok and g.eq(lhs, rhs)
    g.check("[Thm 2.3] phi is an algebra map on all 256 blade products", ok)
    imgs_blades = [phi({I: Fraction(1)}) for I in blades]
    vecs = [[x.get(b, Fraction(0)) for b in g.all_blades(5)] for x in imgs_blades]
    g.check("[Thm 2.3] phi is injective (the 16 blade images have rank 16)", g.rank_of_vectors(vecs) == 16)


def unit_ideal_checks():
    partner = g.scal(Fraction(-1, 2), N_0)
    anti = g.add(g.mul(N_INF, partner, CGA), g.mul(partner, N_INF, CGA))
    g.check("[Prop 2.5] in the completion: n_inf phi + phi n_inf = 1 with phi = -n_0/2 (unit ideal)", g.eq(anti, g.sc(1)))
    g.check("[Prop 2.5] the partner is null: (n_0)^2 = 0 and (n_inf)^2 = 0",
          g.is_zero(g.mul(N_0, N_0, CGA)) and g.is_zero(g.mul(N_INF, N_INF, CGA)))


def translator(tvec, squares, e0_elem):
    """T_t = 1 + (1/2) e0 t, t a Euclidean vector element."""
    return g.add(g.sc(1), g.scal(Fraction(1, 2), g.mul(e0_elem, tvec, squares)))


def translator_checks():
    e0 = g.gen(3)
    s = g.add(g.scal(2, g.gen(0)), g.scal(Fraction(-1, 3), g.gen(1)))
    t = g.add(g.gen(1), g.scal(Fraction(5, 2), g.gen(2)))
    Ts, Tt = translator(s, PGA, e0), translator(t, PGA, e0)
    Tst = translator(g.add(s, t), PGA, e0)
    g.check("[Ex 3.2] PGA: T_s T_t = T_{s+t} (exact composition)", g.eq(g.mul(Ts, Tt, PGA), Tst))
    img = phi(Tt)
    cga_translator = g.sub(g.sc(1), g.scal(Fraction(1, 2), g.mul(phi(t), N_INF, CGA)))
    g.check("[Ex 3.2] phi(T_t) = 1 - (1/2) t n_inf, the CGA translator, verbatim", g.eq(img, cga_translator))
    g.check("[Ex 3.2] phi respects the composition: phi(T_s T_t) = phi(T_s) phi(T_t)",
          g.eq(phi(g.mul(Ts, Tt, PGA)), g.mul(phi(Ts), phi(Tt), CGA)))
    x = g.add(g.gen(0), g.scal(2, g.gen(1)))  # a sample Euclidean vector e1 + 2 e2, moved by T_t
    sand = g.mul(g.mul(Tt, x, PGA), g.reverse(Tt), PGA)
    g.check("[Ex 3.2] the sandwich moves the sample vector (the check is not vacuous)",
          not g.eq(sand, x))
    lhs = phi(sand)
    rhs = g.mul(g.mul(phi(Tt), phi(x), CGA), g.reverse(phi(Tt)), CGA)
    g.check("[Ex 3.2] phi carries the sandwich action verbatim (sample vector)", g.eq(lhs, rhs))


def pairing_checks():
    ok = all(g.dot(N_INF, w, CGA) == 0 for w in [g.gen(0), g.gen(1), g.gen(2), N_INF])
    ok = ok and g.dot(N_INF, N_0, CGA) == Fraction(-1)
    g.check("[Thm 2.3] radical pairing: Q(n_inf, W) = 0 yet Q(n_inf, n_0) = -1 != 0 "
          "(the minimality map lambda is injective here)", ok)


def main():
    print("verify_T02.py: exact-arithmetic checks for Transport Papers T2\n")
    ideal_checks()
    nilpotency_checks()
    completion_gram_checks()
    embedding_checks()
    unit_ideal_checks()
    translator_checks()
    pairing_checks()
    print()
    if g.FAILURES:
        print("FAILURES (%d):" % len(g.FAILURES))
        for f in g.FAILURES:
            print("  " + f)
        sys.exit(1)
    print("ALL CHECKS PASSED.")


if __name__ == "__main__":
    main()
