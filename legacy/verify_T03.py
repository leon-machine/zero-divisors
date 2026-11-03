#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T03.py: exact-arithmetic verification of the computational identities of

    "The Tower and the CAR Limit: Iterated Transport, the Frozen Clock, and
     Second Quantisation"  (Transport Papers T3)

in the style of verify_T01.py / verify_T04.py: the shared library's (GA.py)
basis-blade Clifford product over exact rationals, plus small exact
models (the Fock module on an exterior algebra; 2x2 matrices with Clifford
entries).  Every check is reported PASS/FAIL and the script exits nonzero on
any failure.  No floating point is used anywhere.
Shared machinery (the blade engine, exact linear algebra, rational functions,
the exterior model and the check harness) lives in GA.py, deposited alongside.

Generator layout for a floor T_k over base Cl(p,q): indices 0..n-1 are the
ground generators (squares +1 x p, -1 x q); then plane j occupies indices
n+2(j-1), n+2j-1 with squares (+1, -1).

Coverage (labels refer to the paper):
  [Lem 3.1]  volume elements: omega_j^2 = 1, anticommutation with own plane,
             commutation with ground and other planes; Omega_k properties
  [Thm 3.2]  commuting copies at k = 2 over Cl(1,3) (T_2 = Cl(3,5), dim 256):
             twisted generators satisfy the ground relations; A_2 commutes
             with B_2 elementwise (all generator pairs); the 256 products of
             A-blades with B-blades are 256 distinct basis blades (exact
             generation and dimension count)
  [Thm 3.6]  frozen clock: centre = span{1} on floors k = 0, 1, 2 of the
             physical tower (blade-wise commutant, valid for diagonal forms);
             hence no nontrivial central idempotent on any checked floor
  [Prop 4.1] CAR as vectors: all pairwise relations for 3 planes in Cl(3,3)
  [Thm 4.2]  Fock module on Lambda W_3 (dim 8): CAR of the operators, the
             Clifford square c(alpha)^2 = <alpha,alpha> id, vacuum killed by
             contractions, and irreducibility: the 64 blade images span the
             full 64-dimensional End(Lambda W_3)
  [Thm 4.3]  capacity instances: min(p,q) CAR pairs constructed in Cl(2,4)
             and Cl(3,5); isotropy and independence of the creation span
  [Lem 5.1]  grade twist inner for even charge: Ad_u = grade involution on
             all blades of Cl(1,3) (16) and Cl(2,4) (64); the 2x2 diagonal
             conjugation U diag(a,a) U^{-1} = diag(a, ahat); outerness for
             odd charge: Cl(1,0) is commutative yet grade involution moves
             its central idempotents
  [Lem 5.2]  compatibility at one full stage over ground Cl(1,1): the
             transported connecting map psi_1 = phi_2 o iota o phi_1^{-1}
             equals Ad(V_1) o theta_1 with the SPLIT corrector
             V_1 = diag(u_A x 1, 1 x Omega_1), checked generator by
             generator inside Cl(3,3); the naive transported single-step
             corrector diag(1, u_{T_1}) is checked to FAIL
  [Lem 5.4]  the *-structure on Cl(2,2): conjugate-linear antiautomorphism
             on the rational subalgebra (antimultiplicative on samples,
             involutive, all generators and volume elements unitary,
             v* = w for the ladder pair)
  [Lem 5.1]  one step of the corrector: Ad(U^{-1}) o psi = theta on a
             sample element (the corrector recursion's commuting square)
"""

from fractions import Fraction
from itertools import combinations
import sys

import GA as g


def floor_squares(p, q, k):
    """Squares list for T_k over Cl(p,q) in the paper's generator layout."""
    return tuple([1] * p + [-1] * q + [1, -1] * k)


# ---------------------------------------------------------------------------
# [Lem 3.1] volume elements
# ---------------------------------------------------------------------------

def volume_checks():
    p, q, k = 1, 3, 2
    n = p + q
    squares = floor_squares(p, q, k)
    omegas = []
    for j in range(k):
        e, f = g.gen(n + 2 * j), g.gen(n + 2 * j + 1)
        omegas.append(g.mul(e, f, squares))
    ok = all(g.eq(g.mul(w, w, squares), g.sc(1)) for w in omegas)
    g.check("[Lem 3.1] omega_j^2 = 1 for both planes", ok)
    ok = True
    for j in range(k):
        for idx in (n + 2 * j, n + 2 * j + 1):
            ok = ok and g.anticommutes(omegas[j], g.gen(idx), squares)
    g.check("[Lem 3.1] omega_j anticommutes with its own plane generators", ok)
    ok = True
    for j in range(k):
        others = list(range(n)) + [n + 2 * i + t for i in range(k) if i != j for t in (0, 1)]
        for idx in others:
            ok = ok and g.commutes(omegas[j], g.gen(idx), squares)
    g.check("[Lem 3.1] omega_j commutes with ground and other-plane generators", ok)
    Omega = g.mul(omegas[0], omegas[1], squares)
    ok = g.eq(g.mul(Omega, Omega, squares), g.sc(1))
    ok = ok and all(g.commutes(Omega, g.gen(i), squares) for i in range(n))
    ok = ok and all(g.anticommutes(Omega, g.gen(n + i), squares) for i in range(2 * k))
    g.check("[Lem 3.1] Omega_2: squares to 1, commutes with ground, anticommutes with plane generators", ok)
    return squares, Omega


# ---------------------------------------------------------------------------
# [Thm 3.2] commuting copies at k = 2 over Cl(1,3)
# ---------------------------------------------------------------------------

def commuting_copies_checks(squares, Omega):
    p, q, k = 1, 3, 2
    n = p + q
    twisted = [g.mul(g.gen(i), Omega, squares) for i in range(n)]
    base_sq = [1, -1, -1, -1]
    ok = True
    for i in range(n):
        ok = ok and g.eq(g.mul(twisted[i], twisted[i], squares), g.sc(base_sq[i]))
        for j in range(i + 1, n):
            ok = ok and g.anticommutes(twisted[i], twisted[j], squares)
    g.check("[Thm 3.2] twisted generators x Omega satisfy the ground Cl(1,3) relations", ok)
    ok = True
    for i in range(n):
        for idx in range(n, n + 2 * k):
            ok = ok and g.commutes(twisted[i], g.gen(idx), squares)
    g.check("[Thm 3.2] A_2 and B_2 commute (all 16 generator pairs)", ok)
    # generation: A-blades x_I Omega^{|I| mod 2} times B-blades are 256 distinct blades
    ground_blades = g.all_blades(n)
    plane_letters = list(range(n, n + 2 * k))
    plane_blades = []
    for r in range(2 * k + 1):
        plane_blades.extend(combinations(plane_letters, r))
    seen = set()
    ok = True
    for I in ground_blades:
        aI = {I: Fraction(1)}
        if len(I) % 2 == 1:
            aI = g.mul(aI, Omega, squares)
        for J in plane_blades:
            prod = g.mul(aI, {J: Fraction(1)}, squares)
            if len(prod) != 1:
                ok = False
                break
            (bl, co), = prod.items()
            if co == 0 or bl in seen:
                ok = False
                break
            seen.add(bl)
    ok = ok and len(seen) == 256
    g.check("[Thm 3.2] A-blade times B-blade: 256 distinct basis blades (exact generation of T_2)", ok)


# ---------------------------------------------------------------------------
# [Thm 3.6] frozen clock: centre = span{1} on floors 0, 1, 2
# (blade-wise commutant: for a diagonal form, [blade, generator] is a single
#  blade multiple with support determined by the blade, so an element is
#  central iff every blade in its support is; the check below is therefore
#  exhaustive, not a sample.)
# ---------------------------------------------------------------------------

def centre_checks():
    no_typeC = True
    for k in (0, 1, 2):
        squares = floor_squares(1, 3, k)
        n_tot = 4 + 2 * k
        central = []
        for b in g.all_blades(n_tot):
            x = {b: Fraction(1)}
            if all(g.commutes(x, g.gen(i), squares) for i in range(n_tot)):
                central.append(b)
        g.check("[Thm 3.6] floor %d of the physical tower: centre = span{1} (blade-wise, exhaustive)" % k,
              central == [()])
        # Type C criterion: a nontrivial central idempotent would be (1 +- omega)/2 with omega
        # the floor volume element, central and squaring to +1.  Compute omega from the
        # generators and test that it anticommutes with every generator (so it is not central),
        # and that the central span found above contains no idempotent other than 0 and 1.
        omega = g.gen(0)
        for i in range(1, n_tot):
            omega = g.mul(omega, g.gen(i), squares)
        half = Fraction(1, 2)
        eps_plus = g.add(g.sc(half), g.scal(half, omega))
        eps_minus = g.sub(g.sc(half), g.scal(half, omega))
        omega_not_central = all(g.anticommutes(omega, g.gen(i), squares) for i in range(n_tot))
        eps_not_central = not all(g.commutes(e, g.gen(i), squares) for e in (eps_plus, eps_minus)
                                  for i in range(n_tot))
        # idempotents in span(central): with central == [()] these are c with c^2 = c, c rational
        central_idempotents_trivial = (central == [()])
        no_typeC = no_typeC and omega_not_central and eps_not_central and central_idempotents_trivial
    g.check("[Thm 3.6] no floor checked has a nontrivial central idempotent: the floor volume element "
            "anticommutes with every generator, (1 +- omega)/2 is not central, centre = span{1} (no type C)",
            no_typeC)


# ---------------------------------------------------------------------------
# [Prop 4.1] CAR as vectors: 3 planes in Cl(3,3)
# ---------------------------------------------------------------------------

def pairs_in(squares, n_ground, k):
    vs, ws = [], []
    for j in range(k):
        e, f = g.gen(n_ground + 2 * j), g.gen(n_ground + 2 * j + 1)
        vs.append(g.scal(Fraction(1, 2), g.add(e, f)))
        ws.append(g.scal(Fraction(1, 2), g.sub(e, f)))
    return vs, ws


def car_checks():
    k = 3
    squares = floor_squares(0, 0, k)  # Cl(3,3), no ground
    vs, ws = pairs_in(squares, 0, k)
    ok = True
    for i in range(k):
        for j in range(k):
            ok = ok and g.is_zero(g.add(g.mul(vs[i], vs[j], squares), g.mul(vs[j], vs[i], squares)))
            ok = ok and g.is_zero(g.add(g.mul(ws[i], ws[j], squares), g.mul(ws[j], ws[i], squares)))
            anti = g.add(g.mul(vs[i], ws[j], squares), g.mul(ws[j], vs[i], squares))
            want = g.sc(1) if i == j else {}
            ok = ok and g.eq(anti, want)
    g.check("[Prop 4.1] three ladder pairs in Cl(3,3): all 27 CAR relations hold as vector identities", ok)


# ---------------------------------------------------------------------------
# [Thm 4.2] the Fock module on Lambda W_3
# states: dict {frozenset subset of {0,1,2}: Fraction}
# ---------------------------------------------------------------------------

def fock_wedge(j, st):
    out = {}
    for S, c in st.items():
        if j in S:
            continue
        sign = Fraction(-1) ** len([i for i in S if i < j])
        T = frozenset(S | {j})
        out[T] = out.get(T, Fraction(0)) + sign * c
    return {S: c for S, c in out.items() if c != 0}


def fock_contract(j, st):
    out = {}
    for S, c in st.items():
        if j not in S:
            continue
        sign = Fraction(-1) ** len([i for i in sorted(S) if i < j])
        T = frozenset(S - {j})
        out[T] = out.get(T, Fraction(0)) + sign * c
    return {S: c for S, c in out.items() if c != 0}


def fock_c(coeffs, st):
    """Action of the vector sum_j (a_j v_j + b_j w_j); coeffs = [(a_j, b_j)]."""
    out = {}
    for j, (a, b) in enumerate(coeffs):
        if a:
            for S, c in fock_wedge(j, st).items():
                out[S] = out.get(S, Fraction(0)) + a * c
        if b:
            for S, c in fock_contract(j, st).items():
                out[S] = out.get(S, Fraction(0)) + b * c
    return {S: c for S, c in out.items() if c != 0}


def fock_checks():
    k = 3
    states = [frozenset(s) for s in g.all_blades(k)]
    unit = lambda S: {S: Fraction(1)}

    def vvec(j):
        return [(Fraction(1) if i == j else Fraction(0), Fraction(0)) for i in range(k)]

    def wvec(j):
        return [(Fraction(0), Fraction(1) if i == j else Fraction(0)) for i in range(k)]

    ok = True
    for i in range(k):
        for j in range(k):
            for S in states:
                st = unit(S)
                lhs = fock_c(vvec(i), fock_c(wvec(j), dict(st)))
                rhs = fock_c(wvec(j), fock_c(vvec(i), dict(st)))
                tot = {}
                for d in (lhs, rhs):
                    for T, c in d.items():
                        tot[T] = tot.get(T, Fraction(0)) + c
                tot = {T: c for T, c in tot.items() if c != 0}
                want = st if i == j else {}
                ok = ok and tot == want
    g.check("[Thm 4.2] Fock operators: {c(v_i), c(w_j)} = delta_ij id on all 8 states", ok)
    alpha = [(Fraction(2), Fraction(3)), (Fraction(-1), Fraction(1, 2)), (Fraction(0), Fraction(5))]
    qa = sum(a * b for a, b in alpha)  # <alpha,alpha> = sum a_j b_j
    ok = True
    for S in states:
        st = unit(S)
        got = fock_c(alpha, fock_c(alpha, dict(st)))
        want = {S: qa} if qa != 0 else {}
        ok = ok and got == want
    g.check("[Thm 4.2] c(alpha)^2 = <alpha,alpha> id for a general vector, all states", ok)
    ok = all(fock_c(wvec(j), unit(frozenset())) == {} for j in range(k))
    g.check("[Thm 4.2] the vacuum is annihilated by every contraction", ok)
    # irreducibility: images of the 64 blades of Cl(3,3) span End(Lambda W_3)
    squares = floor_squares(0, 0, k)
    vs, ws = pairs_in(squares, 0, k)

    def act_vector(vec_elem, st):
        """Translate a Clifford VECTOR (linear in generators) to Fock coeffs."""
        coeffs = [[Fraction(0), Fraction(0)] for _ in range(k)]
        for b, c in vec_elem.items():
            (idx,) = b
            j, t = divmod(idx, 2)
            # e_j = v_j + w_j, f_j = v_j - w_j
            if t == 0:
                coeffs[j][0] += c
                coeffs[j][1] += c
            else:
                coeffs[j][0] += c
                coeffs[j][1] -= c
        return fock_c([tuple(cc) for cc in coeffs], st)

    def act_blade(blade, st):
        for idx in reversed(blade):
            st = act_vector(g.gen(idx), st)
        return st

    mats = []
    for blade in g.all_blades(2 * k):
        cols = []
        for S in states:
            img = act_blade(blade, unit(S))
            cols.extend([img.get(T, Fraction(0)) for T in states])
        mats.append(cols)
    g.check("[Thm 4.2] irreducibility: the 64 blade actions span the full End(Lambda W_3) (rank 64)",
          g.rank_of_vectors(mats) == 64)


# ---------------------------------------------------------------------------
# [Thm 4.3] capacity instances
# ---------------------------------------------------------------------------

def capacity_checks():
    # Cl(2,4): Witt index 2; build 2 pairs from (e0,e2) and (e1,e3)
    squares = tuple([1, 1, -1, -1, -1, -1])
    pairs = [(0, 2), (1, 3)]
    vs = [g.scal(Fraction(1, 2), g.add(g.gen(i), g.gen(j))) for (i, j) in pairs]
    ws = [g.scal(Fraction(1, 2), g.sub(g.gen(i), g.gen(j))) for (i, j) in pairs]
    ok = True
    for i in range(2):
        for j in range(2):
            ok = ok and g.is_zero(g.add(g.mul(vs[i], vs[j], squares), g.mul(vs[j], vs[i], squares)))
            anti = g.add(g.mul(vs[i], ws[j], squares), g.mul(ws[j], vs[i], squares))
            ok = ok and g.eq(anti, g.sc(1) if i == j else {})
    g.check("[Thm 4.3] Cl(2,4): min(p,q) = 2 CAR pairs constructed from a Witt decomposition", ok)
    vecs = [[v.get((i,), Fraction(0)) for i in range(6)] for v in vs]
    iso = all(g.is_zero(g.add(g.mul(vs[i], vs[j], squares), g.mul(vs[j], vs[i], squares))) for i in range(2) for j in range(2))
    g.check("[Thm 4.3] creation span is totally isotropic and independent (rank 2)",
          iso and g.rank_of_vectors(vecs) == 2)
    # tower floor Cl(3,5): three pairs
    squares = floor_squares(1, 3, 2)
    vs, ws = pairs_in(squares, 4, 2)
    v0 = g.scal(Fraction(1, 2), g.add(g.gen(0), g.gen(1)))
    w0 = g.scal(Fraction(1, 2), g.sub(g.gen(0), g.gen(1)))
    vs, ws = [v0] + vs, [w0] + ws
    ok = True
    for i in range(3):
        for j in range(3):
            ok = ok and g.is_zero(g.add(g.mul(vs[i], vs[j], squares), g.mul(vs[j], vs[i], squares)))
            anti = g.add(g.mul(vs[i], ws[j], squares), g.mul(ws[j], vs[i], squares))
            ok = ok and g.eq(anti, g.sc(1) if i == j else {})
    # isotropy of the creation span is the vv-anticommutator clause above;
    # independence by exact rank of the three creation vectors in R^8
    vecs = [[v.get((i,), Fraction(0)) for i in range(len(squares))] for v in vs]
    ok = ok and g.rank_of_vectors(vecs) == 3
    g.check("[Thm 4.3] tower floor Cl(3,5): min(1,3) + 2 = 3 CAR pairs (capacity climbs one per rung); "
          "creation span isotropic and independent (rank 3)", ok)


# ---------------------------------------------------------------------------
# [Lem 5.1] the grade twist
# ---------------------------------------------------------------------------

def clifford_inverse_of_pm1_square(u, squares):
    u2 = g.mul(u, u, squares)
    if g.eq(u2, g.sc(1)):
        return u
    if g.eq(u2, g.sc(-1)):
        return g.neg(u)
    raise ValueError("volume element does not square to +-1")


def twist_checks():
    for (p, q, name) in [(1, 3, "Cl(1,3)"), (2, 4, "Cl(2,4)")]:
        n = p + q
        squares = tuple([1] * p + [-1] * q)
        u = {tuple(range(n)): Fraction(1)}
        uinv = clifford_inverse_of_pm1_square(u, squares)
        ok = True
        for b in g.all_blades(n):
            x = {b: Fraction(1)}
            conj = g.mul(g.mul(u, x, squares), uinv, squares)
            ok = ok and g.eq(conj, g.grade_inv(x))
        g.check("[Lem 5.1] %s: Ad_u = grade involution on all %d blades" % (name, 2 ** n), ok)
    # 2x2 diagonal conjugation over Cl(1,3)
    squares = tuple([1, -1, -1, -1])
    u = {(0, 1, 2, 3): Fraction(1)}
    uinv = clifford_inverse_of_pm1_square(u, squares)
    a = g.add(g.sc(2), g.gen(0), g.scal(3, g.mul(g.gen(1), g.gen(2), squares)), g.scal(Fraction(1, 5), g.gen(3)))

    def m22_mul(A, B):
        return [[g.add(g.mul(A[i][0], B[0][j], squares), g.mul(A[i][1], B[1][j], squares))
                 for j in range(2)] for i in range(2)]

    U = [[g.sc(1), {}], [{}, u]]
    Uinv = [[g.sc(1), {}], [{}, uinv]]
    D = [[a, {}], [{}, a]]
    conj = m22_mul(m22_mul(U, D), Uinv)
    want = [[a, {}], [{}, g.grade_inv(a)]]
    ok = all(g.eq(conj[i][j], want[i][j]) for i in range(2) for j in range(2))
    g.check("[Lem 5.1] U diag(a,a) U^{-1} = diag(a, ahat) in M_2(Cl(1,3)) (sample element)", ok)
    # odd charge: Cl(1,0) commutative, grade involution swaps central idempotents
    squares = (1,)
    # commutativity: every pair of basis blades commutes, and so do two
    # general rational elements a = 2 + 3 e0, b = -1 + 5 e0
    blades10 = [{b: Fraction(1)} for b in g.all_blades(1)]
    ok = all(g.commutes(x, y, squares) for x in blades10 for y in blades10)
    a10 = g.add(g.sc(2), g.scal(Fraction(3), g.gen(0)))
    b10 = g.add(g.sc(-1), g.scal(Fraction(5), g.gen(0)))
    ok = ok and g.eq(g.mul(a10, b10, squares), g.mul(b10, a10, squares))
    e_plus = g.scal(Fraction(1, 2), g.add(g.sc(1), g.gen(0)))
    e_minus = g.scal(Fraction(1, 2), g.sub(g.sc(1), g.gen(0)))
    ok = ok and g.eq(g.grade_inv(e_plus), e_minus) and g.eq(g.grade_inv(e_minus), e_plus)
    ok = ok and g.eq(g.mul(e_plus, e_plus, squares), e_plus) and g.eq(g.mul(e_minus, e_minus, squares), e_minus)
    g.check("[Lem 5.1] Cl(1,0): commutative (all inner automorphisms trivial) yet the grade involution "
          "swaps the central idempotents: the twist is outer for odd charge", ok)
    return squares


def intertwining_checks():
    # One commuting square: Ad(U^{-1}) o psi = theta, psi(a) = diag(a, ahat), theta(a) = diag(a,a)
    squares = tuple([1, -1, -1, -1])
    u = {(0, 1, 2, 3): Fraction(1)}
    uinv = clifford_inverse_of_pm1_square(u, squares)
    a = g.add(g.sc(-1), g.scal(2, g.gen(1)), g.mul(g.gen(0), g.gen(3), squares),
            g.scal(Fraction(3, 7), g.mul(g.mul(g.gen(0), g.gen(1), squares), g.gen(2), squares)))

    def m22_mul(A, B):
        return [[g.add(g.mul(A[i][0], B[0][j], squares), g.mul(A[i][1], B[1][j], squares))
                 for j in range(2)] for i in range(2)]

    U = [[g.sc(1), {}], [{}, u]]
    Uinv = [[g.sc(1), {}], [{}, uinv]]
    psi = [[a, {}], [{}, g.grade_inv(a)]]
    got = m22_mul(m22_mul(Uinv, psi), U)
    want = [[a, {}], [{}, a]]
    ok = all(g.eq(got[i][j], want[i][j]) for i in range(2) for j in range(2))
    g.check("[Lem 5.1] single-step corrector: Ad(U^{-1}) o (a -> diag(a, ahat)) = block doubling (sample element)", ok)


# ---------------------------------------------------------------------------
# [Lem 5.2] compatibility: the transported connecting map and its split corrector
# ---------------------------------------------------------------------------

def compat_checks():
    # Ground Cl(1,1), floors T_1 = Cl(2,2) inside T_2 = Cl(3,3).
    # Generator ordering: 0 = x1 (+1), 1 = x2 (-1), 2 = e1 (+1), 3 = f1 (-1),
    #                     4 = e2 (+1), 5 = f2 (-1).
    S = (1, -1, 1, -1, 1, -1)
    x1, x2 = g.gen(0), g.gen(1)
    e1, f1, e2, f2 = g.gen(2), g.gen(3), g.gen(4), g.gen(5)
    v1 = g.scal(Fraction(1, 2), g.add(e1, f1)); w1 = g.scal(Fraction(1, 2), g.sub(e1, f1))
    v2 = g.scal(Fraction(1, 2), g.add(e2, f2)); w2 = g.scal(Fraction(1, 2), g.sub(e2, f2))
    om1 = g.mul(e1, f1, S); om2 = g.mul(e2, f2, S)
    Om2 = g.mul(om1, om2, S)
    uA = g.mul(x1, x2, S)                       # ground volume, uA^2 = 1 here
    # plane matrix units, labelled per Fact 2.1: E11 = vw, E12 = v, E21 = w, E22 = wv
    E1 = {  # plane 1 (inner index)
        (1, 1): g.mul(v1, w1, S), (1, 2): v1, (2, 1): w1, (2, 2): g.mul(w1, v1, S)}
    E2 = {  # plane 2 (outer index)
        (1, 1): g.mul(v2, w2, S), (1, 2): v2, (2, 1): w2, (2, 2): g.mul(w2, v2, S)}

    def alpha(a, Om):
        # the twisted ground embedding on an element of span{1, x1, x2, x1x2}
        out = {}
        for b, c in a.items():
            piece = {b: c} if len(b) % 2 == 0 else g.mul({b: c}, Om, S)
            for bb, cc in piece.items():
                out[bb] = out.get(bb, Fraction(0)) + cc
        return {b: c for b, c in out.items() if c != 0}

    idx = [(1, 1), (1, 2), (2, 1), (2, 2)]      # (outer, inner)

    def phi2_inv(M):
        # M: dict ((i2,i1),(j2,j1)) -> ground element; returns element of Cl(3,3).
        # Nested Peirce dictionary: the outer (plane-2) units do not commute with
        # odd inner (plane-1) units, so the outer entry (i2, j2) with inner content
        # b is E2_{i2 1} b E2_{1 j2}, per Fact 2.1 iterated.
        out = {}
        for i2 in (1, 2):
            for j2 in (1, 2):
                inner = {}
                for i1 in (1, 2):
                    for j1 in (1, 2):
                        a = M.get(((i2, i1), (j2, j1)))
                        if not a:
                            continue
                        term = g.mul(alpha(a, Om2), E1[(i1, j1)], S)
                        for bb, cc in term.items():
                            inner[bb] = inner.get(bb, Fraction(0)) + cc
                inner = {b: c for b, c in inner.items() if c != 0}
                if not inner:
                    continue
                term = g.mul(g.mul(E2[(i2, 1)], inner, S), E2[(1, j2)], S)
                for bb, cc in term.items():
                    out[bb] = out.get(bb, Fraction(0)) + cc
        return {b: c for b, c in out.items() if c != 0}

    def mat_mul(Ma, Mb):
        out = {}
        for i in idx:
            for j in idx:
                acc = {}
                for l in idx:
                    a, b = Ma.get((i, l)), Mb.get((l, j))
                    if a and b:
                        t = g.mul(a, b, S)
                        for bb, cc in t.items():
                            acc[bb] = acc.get(bb, Fraction(0)) + cc
                acc = {b: c for b, c in acc.items() if c != 0}
                if acc:
                    out[(i, j)] = acc
        return out

    def diag_corrector(entries):
        # entries: list of 4 ground elements in idx order
        return {(i, i): entries[k] for k, i in enumerate(idx) if entries[k]}

    V = diag_corrector([uA, uA, g.sc(-1), g.sc(1)])       # the split corrector (self-inverse)
    naive = diag_corrector([g.sc(1), g.sc(1), g.scal(-1, uA), uA])  # diag(1, u_{T_1}) transported

    def theta(G):
        # block doubling in the outer index of a 2x2 (inner) ground-valued matrix
        return {((o, i[0]), (o, j[0])): a for ((i0, j0), a) in [] } if False else None

    # generators of A x Mat_2 as inner 2x2 matrices; theta doubles into the outer index
    def theta_of_inner(Minner):
        out = {}
        for (i1, j1), a in Minner.items():
            for o in (1, 2):
                out[((o, i1), (o, j1))] = a
        return out

    gens = []
    # ground generators x (x) 1_2
    for x, nm in [(x1, "x1"), (x2, "x2")]:
        Minner = {(1, 1): x, (2, 2): x}
        lhs = g.mul(x, om1, S)                            # phi_1^{-1}(x (x) 1) = x Omega_1
        gens.append((nm + " (x) 1", Minner, lhs))
    # plane-1 matrix units 1 (x) E
    for (i1, j1), elem, nm in [((1, 1), E1[(1, 1)], "E11"), ((1, 2), v1, "E12"),
                               ((2, 1), w1, "E21"), ((2, 2), E1[(2, 2)], "E22")]:
        Minner = {(i1, j1): g.sc(1)}
        gens.append(("1 (x) " + nm, Minner, elem))

    ok_split, ok_naive_fails = True, False
    for nm, Minner, lhs in gens:
        M4 = theta_of_inner(Minner)
        rhs = phi2_inv(mat_mul(mat_mul(V, M4), V))        # V is self-inverse
        ok_split = ok_split and g.eq(lhs, rhs)
        rhs_naive = phi2_inv(mat_mul(mat_mul(naive, M4), naive))
        if not g.eq(lhs, rhs_naive):
            ok_naive_fails = True
    g.check("[Lem 5.2] psi_1 = Ad(V_1) o theta_1 with the split corrector, on all six generators "
          "(ground Cl(1,1), inside Cl(3,3))", ok_split)
    g.check("[Lem 5.2] sanity: V_1 is invertible (self-inverse) and unitary-compatible: V_1 V_1 = 1",
          all(g.eq(mat_mul(V, V).get((i, i), {}), g.sc(1)) for i in idx))
    g.check("[Lem 5.2] the naive transported single-step corrector diag(1, u_T1) FAILS on some generator "
          "(the split is necessary)", ok_naive_fails)


# ---------------------------------------------------------------------------
# [Lem 5.4] the *-structure, on the rational subalgebra of Cl(2,2)
# ---------------------------------------------------------------------------

def star_checks():
    # Generator ordering: 0 = e1 (+1), 1 = f1 (-1), 2 = e2 (+1), 3 = f2 (-1).
    S = (1, -1, 1, -1)
    neg = {1, 3}

    def star(x):
        out = {}
        for b, c in x.items():
            k = len(b)
            sign = (-1) ** (k * (k - 1) // 2) * (-1) ** sum(1 for i in b if i in neg)
            out[b] = c * sign
        return {b: c for b, c in out.items() if c != 0}

    e1, f1, e2, f2 = g.gen(0), g.gen(1), g.gen(2), g.gen(3)
    v1 = g.scal(Fraction(1, 2), g.add(e1, f1)); w1 = g.scal(Fraction(1, 2), g.sub(e1, f1))
    a = g.add(g.sc(2), e1, g.scal(3, g.mul(f1, e2, S)), g.scal(Fraction(1, 7), g.mul(g.mul(e1, e2, S), f2, S)))
    b = g.add(g.scal(-1, f2), g.mul(e1, f1, S), g.scal(Fraction(2, 5), g.mul(g.mul(f1, e2, S), f2, S)))
    g.check("[Lem 5.4] * is antimultiplicative on sampled elements: (ab)* = b* a*",
          g.eq(star(g.mul(a, b, S)), g.mul(star(b), star(a), S)))
    g.check("[Lem 5.4] * is an involution on sampled elements: a** = a",
          g.eq(star(star(a)), a) and g.eq(star(star(b)), b))
    om1 = g.mul(e1, f1, S); om2 = g.mul(e2, f2, S); Om2 = g.mul(om1, om2, S)
    units = [e1, f1, e2, f2, om1, om2, Om2]
    g.check("[Lem 5.4] generators and volume elements are unitary: z* z = 1",
          all(g.eq(g.mul(star(z), z, S), g.sc(1)) for z in units))
    g.check("[Lem 5.4] the ladder pair is mutually adjoint: v* = w",
          g.eq(star(v1), w1) and g.eq(star(w1), v1))


def main():
    print("verify_T03.py: exact-arithmetic checks for Transport Papers T3\n")
    squares, Omega = volume_checks()
    commuting_copies_checks(squares, Omega)
    centre_checks()
    car_checks()
    fock_checks()
    capacity_checks()
    twist_checks()
    compat_checks()
    star_checks()
    intertwining_checks()
    print()
    if g.FAILURES:
        print("FAILURES (%d):" % len(g.FAILURES))
        for f in g.FAILURES:
            print("  " + f)
        sys.exit(1)
    print("ALL CHECKS PASSED.")


if __name__ == "__main__":
    main()
