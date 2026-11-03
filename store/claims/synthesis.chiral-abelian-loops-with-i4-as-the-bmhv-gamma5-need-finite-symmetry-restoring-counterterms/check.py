"""BMHV symmetry-restoring counterterms of a chiral abelian gauge field in the spacetime algebra: exact checks.

Cl(1, D-1), signature (+, -, ..., -), generators g0..g_{D-1} (GA.gen). The four-dimensional I4 = g0 g1 g2 g3
inside Cl(1, D-1) is the BMHV gamma5 of the stored unit result (clause (iv)): with the unit of the Feynman
rules a coefficient outside the product (Gaussian rationals), gamma5 = i I4 squares to 1, anticommutes with
g0..g3 and commutes with the evanescent generators g4.. . Barred = components along g0..g3, hatted = the rest.
Traces are 4 <X>_0 (Tr 1 = 4 in every D); the checks work with the normalised trace <X>_0.

Massless right-handed field of charge Y, vertex gbar^mu P_R, propagator numerator the full D-dimensional
momentum k = kbar + khat; external momenta four-dimensional.
Part 1: the projectors delete the evanescent loop momentum: gbar^mu P_R k gbar^nu P_R = gbar^mu kbar gbar^nu P_R,
        and the same around the four-vertex loop; khat survives only in a trace with zero scalar part.
Part 2: the l l part of the bubble numerator after symmetric integration (l^a l^b -> g^ab l^2/D): chiral
        (barred contraction) -g^{mu nu}; vector-like half-Dirac (2-D)/2 g^{mu nu}, checked at D = 4..8;
        difference (D-4)/2 g^{mu nu}.
Part 3: the l^4 part of the four-point numerator summed over the six orderings (l^4 -> S l^4/(D(D+2))): chiral
        zero, vector-like (D-4)(D-2) S^{mu nu rho sigma} (normalised, half-Dirac), checked at D = 4..7; the
        gamma5 part of the chiral sum zero.
Part 4: the pole times the evanescent factor: (D-4) Gamma(1-D/2) -> 2, (D-4) Gamma(2-D/2) -> -2, as exact
        rational functions of D times Gamma(3-D/2).
Part 5: assembly: Pi_break = -(e^2 Y^2/(48 pi^2)) qbar^2 gbar^{mu nu} (not transverse), four-point
        -(e^4 Y^4/(24 pi^2)) S; counterterms (1/(16 pi^2)) [-(e^2 Y^2/6) Abar.dbar^2 Abar + (e^4 Y^4/12)(Abar^2)^2].
Part 6: one generation's left-handed content: sum Y^2 = 10/3, sum Y^4 = 95/54; both positive, no cancellation.
Exact arithmetic only (Fractions, Gaussian rationals).
"""
from fractions import Fraction as Fr
from itertools import permutations

import GA
from GA import QI
from tp_premise import premise

IU = QI(0, 1)


def sig(D):
    return tuple([1] + [-1] * (D - 1))


def gens(D):
    return [GA.gen(i) for i in range(D)]


def up(D, i):
    return GA.scal(Fr(1, sig(D)[i]), GA.gen(i))


def mul(D, *xs):
    S = sig(D)
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, S)
    return out


def add(*xs):
    out = {}
    for x in xs:
        for b, c in x.items():
            out[b] = out.get(b, Fr(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def cscal(c, x):
    return {b: c * v for b, v in x.items() if c * v != 0}


def sc(x):
    return x.get((), Fr(0))


def vec(c):
    return {(i,): Fr(c[i]) for i in range(len(c)) if c[i] != 0}


def bar(v):
    return {b: c for b, c in v.items() if b[0] < 4}


def gamma5():
    return {(0, 1, 2, 3): IU}


def proj(sign):
    return cscal(Fr(1, 2), add({(): Fr(1)}, cscal(Fr(sign), gamma5())))


def check_projectors_remove_the_evanescent_momentum():
    premise("synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four")
    premise("synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5")
    ok = True
    D = 6
    g5 = gamma5()
    ok &= mul(D, g5, g5) == {(): QI(1)} or mul(D, g5, g5) == {(): Fr(1)}
    k = vec([Fr(1, 2), 1, Fr(-1, 3), 2, Fr(3, 4), Fr(-2, 5)])
    k2 = vec([2, Fr(1, 3), 0, -1, Fr(-1, 2), Fr(5, 3)])
    k3 = vec([Fr(1, 7), 0, 1, Fr(1, 2), 2, -1])
    k4 = vec([-1, Fr(2, 3), Fr(1, 2), 0, Fr(1, 3), Fr(1, 4)])
    for s in (1, -1):
        P = proj(s)
        for mu, nu in [(0, 1), (2, 2), (3, 0), (1, 3)]:
            lhs = mul(D, up(D, mu), P, k, up(D, nu), P)
            rhs = mul(D, up(D, mu), bar(k), up(D, nu), P)
            ok &= add(lhs, cscal(Fr(-1), rhs)) == {}
            hat = add(k2, cscal(Fr(-1), bar(k2)))
            ok &= sc(mul(D, up(D, mu), bar(k), up(D, nu), P, hat)) == 0
        # four vertices around the loop: every momentum becomes barred
        ms = [0, 1, 2, 3]
        full = mul(D, up(D, ms[0]), P, k, up(D, ms[1]), P, k2, up(D, ms[2]), P, k3, up(D, ms[3]), P, k4)
        red = mul(D, up(D, ms[0]), bar(k), up(D, ms[1]), bar(k2), up(D, ms[2]), bar(k3), up(D, ms[3]), P, bar(k4))
        ok &= sc(full) == sc(red)
        ok &= sc(full) == QI(Fr(-43, 48), Fr(935 * s, 378))
        # without the projectors the evanescent parts do contribute
        plain = mul(D, up(D, 0), k, up(D, 0), k2)
        plainbar = mul(D, up(D, 0), bar(k), up(D, 0), bar(k2))
        ok &= sc(plain) == Fr(-41, 24) and sc(plainbar) == Fr(-2, 3)
    ok &= D == len(sig(D)) == max(b[0] for b in k) + 1
    GA.check("check_projectors_remove_the_evanescent_momentum", ok)
    return ok


def bubble_ll(D, chiral, mu, nu):
    rng = range(4) if chiral else range(D)
    tot = Fr(0)
    for a in rng:
        tot += Fr(1, 2) * sc(mul(D, up(D, mu), GA.gen(a), up(D, nu), up(D, a)))
    return tot


def check_bubble_contraction_is_a_polynomial_in_the_dimension():
    premise("synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four")
    ok = True
    for D in (4, 5, 6, 7, 8):
        for mu in range(4):
            for nu in range(4):
                g = Fr(sig(D)[mu]) if mu == nu else Fr(0)
                ch, vl = bubble_ll(D, True, mu, nu), bubble_ll(D, False, mu, nu)
                ok &= ch == -g
                ok &= vl == Fr(2 - D, 2) * g
                ok &= ch - vl == Fr(D - 4, 2) * g
    GA.check("check_bubble_contraction_is_a_polynomial_in_the_dimension", ok)
    return ok


PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def box_l4(D, chiral, ext):
    rng = range(4) if chiral else range(D)
    re, imp = Fr(0), Fr(0)
    I4 = {(0, 1, 2, 3): Fr(1)}
    for perm in permutations(ext[1:]):
        legs = (ext[0],) + perm
        for (p, q), (r, s) in PAIRINGS:
            for a in rng:
                for b in rng:
                    slots = [None] * 4
                    slots[p], slots[q], slots[r], slots[s] = GA.gen(a), up(D, a), GA.gen(b), up(D, b)
                    X = mul(D, up(D, legs[0]), slots[0], up(D, legs[1]), slots[1],
                            up(D, legs[2]), slots[2], up(D, legs[3]), slots[3])
                    re += Fr(1, 2) * sc(X)
                    if chiral:
                        imp += Fr(1, 2) * sc(mul(D, X, I4))
    return re, imp


def sym_g(D, ext):
    g = lambda i, j: Fr(sig(D)[i]) if i == j else Fr(0)
    a, b, c, d = ext
    return g(a, b) * g(c, d) + g(a, c) * g(b, d) + g(a, d) * g(b, c)


EXTS = [(0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 1, 1), (1, 2, 1, 2), (0, 1, 2, 3), (0, 0, 0, 1), (0, 1, 1, 2)]


def check_four_point_contraction_is_a_polynomial_in_the_dimension():
    premise("synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four")
    ok = True
    seen = {}
    for D in (4, 5, 6, 7):
        for e in (EXTS if D < 7 else EXTS[:3]):
            ch_re, ch_im = box_l4(D, True, e)
            vl_re, _ = box_l4(D, False, e)
            ok &= ch_re == 0 and ch_im == 0
            ok &= vl_re == (D - 4) * (D - 2) * sym_g(D, e)
            seen[(D, e)] = vl_re
    pinned = {(4, (0, 0, 0, 0)): 0, (5, (0, 0, 0, 0)): 9, (6, (0, 0, 0, 0)): 24, (7, (0, 0, 0, 0)): 45,
              (5, (0, 0, 1, 1)): -3, (6, (0, 0, 1, 1)): -8, (7, (0, 0, 1, 1)): -15, (6, (0, 1, 2, 3)): 0}
    ok &= all(seen.get(key) == val for key, val in pinned.items())
    GA.check("check_four_point_contraction_is_a_polynomial_in_the_dimension", ok)
    return ok


def check_pole_times_evanescent_factor():
    premise("synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5")
    ok = True
    # Gamma(1 - D/2) = Gamma(3 - D/2)/((1 - D/2)(2 - D/2)), Gamma(2 - D/2) = Gamma(3 - D/2)/(2 - D/2)
    # so (D - 4) Gamma(1 - D/2) = r1(D) Gamma(3 - D/2), (D - 4) Gamma(2 - D/2) = r2(D) Gamma(3 - D/2)
    r1 = lambda D: (D - 4) / ((1 - D / 2) * (2 - D / 2))
    r2 = lambda D: (D - 4) / (2 - D / 2)
    for D in (Fr(7, 2), Fr(9, 2), Fr(39, 10), Fr(401, 100), Fr(5)):
        ok &= r1(D) == -2 / (1 - D / 2)
        ok &= r2(D) == Fr(-2)
    # limits at D = 4, Gamma(1) = 1
    ok &= -2 / (1 - Fr(4) / 2) == 2
    # master integrals (Wick-rotated, Gamma form): prefactors at D = 4
    # l^2/(l^2-Delta)^2: (-1)^1 i (D/2)/Gamma(2) ; l^4/(l^2-Delta)^4: (-1)^4 i D(D+2)/4/Gamma(4)
    ok &= Fr(4, 2) / 1 == 2 and Fr(4 * 6, 4) / 6 == 1
    GA.check("check_pole_times_evanescent_factor", ok)
    return ok


def check_counterterm_coefficients():
    premise("synthesis.imported-one-loop-integrals-and-pauli-villars-regulators")
    premise("synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5")
    ok = True
    # two-point: i Pi = (-1)(i e Y)^2 (i)^2 int Tr[...]/(k^2 k'^2) = -e^2 Y^2 int ...
    pref2 = QI(-1) * (IU * IU) * (IU * IU)           # (-1) (i)^2 from the vertices, (i)^2 from the propagators
    ok &= pref2 == QI(-1)
    # breaking numerator from the computed contraction: chiral - vector = s2 (D - 4) g, s2 read off at D = 5, 6
    s2 = [(bubble_ll(D, True, 0, 0) - bubble_ll(D, False, 0, 0)) / (D - 4) for D in (5, 6)]
    ok &= s2[0] == s2[1]
    # trace 4 s2 (D-4)/D gbar l^2 against -i/(4pi)^{D/2} (D/2) Gamma(1-D/2) Delta^{D/2-1}:
    # 4 s2 (D-4)/D (D/2) Gamma(1-D/2) = 2 s2 (D-4) Gamma(1-D/2) -> 2 s2 * 2
    lim1 = -2 / (1 - Fr(4) / 2)                      # (D-4) Gamma(1-D/2) at D = 4
    per_x = QI(0, -1) * QI(2 * s2[0] * lim1)         # coefficient of Delta gbar /(16 pi^2)
    ok &= per_x == QI(0, -2)
    xint = Fr(1, 2) - Fr(1, 3)
    ok &= xint == Fr(1, 6)
    iPi = pref2 * per_x * QI(-xint)                  # coefficient of e^2 Y^2 qbar^2 gbar /(16 pi^2)
    Pi = iPi / QI(0, 1)
    ok &= Pi == QI(Fr(-1, 3))                        # -(1/3)/(16 pi^2) = -1/(48 pi^2)
    # effective action 1/2 A Pi A with qbar^2 -> -dbar^2 ; counterterm is its negative
    ct2 = -(Fr(1, 2) * Pi.re * Fr(-1))
    ok &= ct2 == Fr(-1, 6)                           # -(e^2 Y^2/6) Abar.dbar^2 Abar /(16 pi^2)
    # not transverse: q_mu qbar^2 gbar^{mu nu} = qbar^2 q^nu, nonzero for q^2 != 0
    q = [Fr(1), Fr(1, 2), 0, Fr(1, 3)]
    gdiag = [1, -1, -1, -1]
    q2 = sum(gdiag[i] * q[i] * q[i] for i in range(4))
    ok &= q2 != 0 and all((q2 * q[n] == 0) == (q[n] == 0) for n in range(4))
    # four-point: i Gamma4 = (-1)(i e Y)^4 (i)^4 sum_perm int Tr = -e^4 Y^4 sum ...
    pref4 = QI(-1) * (IU * IU * IU * IU) * (IU * IU * IU * IU)   # (-1) (i)^4 vertices, (i)^4 propagators
    ok &= pref4 == QI(-1)
    # chiral - half-vector = -(D-4) h(D) S (normalised), h read off the computed contraction at D = 5, 6, 7
    e = (0, 0, 1, 1)
    h = {D: box_l4(D, False, e)[0] / ((D - 4) * sym_g(D, e)) - box_l4(D, True, e)[0] for D in (5, 6, 7)}
    ok &= h[6] - h[5] == h[7] - h[6]                 # linear in D
    h4 = h[5] - (h[6] - h[5])
    lim2 = Fr(-2)                                    # (D-4) Gamma(2-D/2) at D = 4
    # trace 4, 1/(D(D+2)) against i D(D+2)/4 Gamma(2-D/2)/Gamma(4): -4 h(4) (1/4) lim2 / 6
    val = Fr(-4) * h4 * Fr(1, 4) * lim2 / 6
    ok &= val == Fr(2, 3)
    iG4 = pref4 * QI(0, 1) * QI(val)                 # coefficient of e^4 Y^4 S /(16 pi^2); simplex 3! * 1/6 = 1
    G4 = iG4 / QI(0, 1)
    ok &= G4 == QI(Fr(-2, 3))                        # -(2/3)/(16 pi^2) = -1/(24 pi^2)
    # c (Abar^2)^2 has four-point vertex 8 c S; counterterm cancels: 8 c = 2/3
    ct4 = -G4.re / 8
    ok &= ct4 == Fr(1, 12)                           # +(e^4 Y^4/12) (Abar^2)^2 /(16 pi^2)
    # published values (Belusca-Maito et al. 2021, eq. (6.5)): -1/6 and 1/12
    ok &= (ct2, ct4) == (Fr(-1, 6), Fr(1, 12))
    GA.check("check_counterterm_coefficients", ok)
    return ok


def check_one_generation_sums():
    premise("synthesis.anomaly-freedom-forces-slot-content")
    content = [(1, 1, Fr(0)), (3, 1, Fr(-2, 3)), (3, 2, Fr(1, 6)), (1, 2, Fr(-1, 2)), (1, 1, Fr(1)), (3, 1, Fr(1, 3))]
    s2 = sum(c * w * Y ** 2 for c, w, Y in content)
    s4 = sum(c * w * Y ** 4 for c, w, Y in content)
    ok = s2 == Fr(10, 3) and s4 == Fr(95, 54)
    ok &= sum(c * w * Y ** 3 for c, w, Y in content) == 0       # the triangle sum, for contrast
    ok &= Fr(-1, 6) * s2 == Fr(-5, 9) and Fr(1, 12) * s4 == Fr(95, 648)
    GA.check("check_one_generation_sums", ok)
    return ok


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("check_") and callable(fn):
            GA.check(name, fn())
