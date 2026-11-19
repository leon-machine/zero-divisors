#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T14.py: exact-arithmetic verification of the computational identities of
"Dark Matter and the Arrow of Time: The Dark Towers" (Transport Papers, T14),
v1.2 (rescope: the 1.091 even-split record retired with the withdrawn stance).

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rationals and integer arithmetic; irrational
physics constants ((4/11)^(4/3), cube roots) enter only through rational
brackets proved by integer inequalities, except Part H and the nucleosynthesis
block of Part J, whose logarithms, exponentials and fixed-point iterations are
evaluated in forty-digit decimal arithmetic (the T13 precedent), with Part H's
inequality chain checked as exact rational algebra on a rational grid.  Statement tags refer to the compiled
paper.  Imported theorems (Witt, Polyakov, the wall-march, the acoustic no-go)
are not re-proved here; this script covers the residue census and its window
sensitivity, the Witt witnesses, the counting arithmetic, the degree bookkeeping
of the theta no-go, the Fock-model conjugation, the projection exponents, the
N_eff arithmetic and thresholds, the ceiling range, the type table from
primitive idempotents, the even-subalgebra relations of the mirror theorem,
the Fock ideal and its chiralities in GA.py (null blades, the top state, the
pseudoscalar, the exchanging versors: Proposition prop:families and Theorem
thm:paritybit), the mirror's cosmology at its stated inputs, and the seeding
by gravity of Appendix A (Part K).

Checks that record rather than compute (the homotopy table, the degrees of
the characteristic classes, the parity identity, the one-loop coefficient
formula, and the script's own coupling-departure illustration: five) are
labelled RECORD in their own messages.

v1.17 (2026-09-07): Part L added, the infall computation (prem:ledgercharge,
prop:infall): exact rational brackets for the mass at which T_H = m_p, the
burst-to-swallowed baryon ratio, the S_star/S_BH ratio and T_H at one solar
mass, plus RECORD lines (floating point, not checked) for the Schwinger
discharge scales of fact:discharge.  94 checks (89 prior + 5).
v1.19 (2026-09-08): Part L's fifth check (the return fraction at 10^-8 solar
masses), implied by its second, replaced by an exact check of fact:discharge
(Q_c and Q_c/Q_extremal at one solar mass, the ratio proportional to M); a
sixth check added, the crossover mass at which Q_c = Q_extremal, in
(1.3, 1.4) x 10^5 solar masses, above which discharge does not limit the
charge; the RECORD lines now printed from the exact rationals in decimal, so
no machine floating point remains.  95 checks (94 prior - 1 + 2).
v2.0 (2026-09-26): Part M added, the unit-ball rule of Section 7 (the
remainder of the survey ratio): exact measures of unit balls and spheres,
the nesting relations in GA.py, the closed form (11 pi + 16)/(3 pi) against
the record, the equivalent forms and the hat-box identity, the thickness
curve T(c) with its symmetry, floor, roots, windows and fractions, the de
Sitter reductions, the clock reflection, the mass bound in one normalisation
(Gaussian rationals), the look-elsewhere count over 3136 closed forms, and
the consistency numbers (the baryon spacing, the three-dimensional fraction,
the sin^2 theta source factor).  173 checks (94 prior + 79).
v2.1 (2026-09-27): Part M.K added, the contact mechanism of Section 7.3
(lem:fifth, prop:thickness, tab:excludes, rem:Sfork, rem:scope, rem:twoc):
the identities of the four nestings in GA.py (omega central and its square,
the added or lacking direction as P^{-1} omega or omega^{-1} P, its reversal
under the neighbour's orientation, the central idempotents of Cl(1,4), the
action of e4 on them, and the reflection through our world exchanging them),
then the arithmetic of the stated counts: the one-sided slab as an exact
Riemann sum, the downward count, O solved for the sheet spacing, the total,
the alternatives of tab:excludes (both sides; the section weight as a
bracketed real integral and as the Wallis identity; one side and both sides
by section), the c_3 window with c_5 = 1, the module-indifference of S, and
the non-composition of the mechanism across the double nesting.  The clauses
C, I, S, O are postulated and are not checked.  195 checks (173 prior + 22).
v2.2 (2026-09-27): Part M.J gains J9-J11 for prop:sheetsmove (the stress
identity sigma = (1-g) psi, the metric feedback solved for psi, and the
orientation average 2/3 of the source factor, all exact).  The Boltzmann
computation of rem:isotropy (CLASS) is a deposited record, not a check
here.  198 checks (195 prior + 3).
v2.3 (2026-11-19): Part M.L added for Premise E, equal mass per unit ball,
which with R3 replaces R1 and R2 as the premise of the unit-ball rule
(prop:rule (ii) to (iv), prop:thickness (iv), rem:coexpand): the shares with
the length d written out, fillings that keep E and break R1 and R2, the
equivalence of E with R3 and the closed form's shares on all six towers in
both directions (with the mirror and split-pair counterexamples), the one
length, the two own-cell readings and the total, and the two scalings of
rem:coexpand.  All exact.  213 checks (200 prior, the 198 above and the two
floating-point checks of Section 7.7, + 13).
"""

from fractions import Fraction as F
import GA as g

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def res(p, q):
    return (p - q) % 8


def causal(p, q):
    """exactly one direction of the minority sign: convention-free"""
    return min(p, q) == 1


BRACKET_OK = []
INTERNAL_OK = []


def icbrt_bracket(x, denom=10 ** 6):
    """rational bracket (lo, hi) with lo^3 < x < hi^3, lo, hi multiples of 1/denom"""
    # integer cube root of floor(x * denom^3)
    n = (x * denom ** 3)
    n_floor = n.numerator // n.denominator
    lo_k, hi_k = 0, 1
    while hi_k ** 3 <= n_floor:          # integer binary search, no floats
        hi_k *= 2
    while hi_k - lo_k > 1:
        mid = (lo_k + hi_k) // 2
        if mid ** 3 <= n_floor:
            lo_k = mid
        else:
            hi_k = mid
    k = lo_k
    lo, hi = F(k, denom), F(k + 1, denom)
    BRACKET_OK.append(lo ** 3 <= x < hi ** 3)
    return lo, hi


def rank(rows):
    return g.rank_of_vectors([[F(x) for x in r] for r in rows])


# ---------------------------------------------------------------------------
# Part A: residues, the census, the window (prop:residues)
# ---------------------------------------------------------------------------

NMAX = 10
SIGS = [(p, q) for p in range(NMAX + 1) for q in range(NMAX + 1)
        if 1 <= p + q <= NMAX]

lowest_causal = {}
for r in range(8):
    cands = sorted([s for s in SIGS if res(*s) == r and causal(*s)],
                   key=lambda s: (s[0] + s[1], s))
    lowest_causal[r] = cands[0] if cands else None

g.check("prop:residues(i): every residue admits a causal signature "
      "(min(p,q) = 1) within dimension <= 10",
      all(lowest_causal[r] is not None for r in range(8)))

g.check("prop:residues(i): the lowest-dimensional causal signature per residue "
      "is (1,1), (2,1), (3,1), (4,1), (1,5)/(5,1), (1,4), (1,3), (1,2): in "
      "particular r = 0 is causal at dimension two and r = 4 at dimension six",
      lowest_causal[0] == (1, 1) and lowest_causal[1] == (2, 1)
      and lowest_causal[2] == (3, 1) and lowest_causal[3] == (4, 1)
      and lowest_causal[4] in ((1, 5), (5, 1)) and lowest_causal[5] == (1, 4)
      and lowest_causal[6] == (1, 3) and lowest_causal[7] == (1, 2)
      and sum(lowest_causal[4]) == 6)

g.check("prop:residues(i): the rule (t = 1, s = 1..8) gives one signature per "
      "residue, every one of them causal (min(p,q) = 1): the residue alone "
      "sorts nothing",
      sorted(res(1, s) for s in range(1, 9)) == list(range(8))
      and all(causal(1, s) for s in range(1, 9)))

# the sign-convention split for the two Minkowski residues
g.check("prop:residues: the signature reversal (p,q) -> (q,p) sends residue r "
      "to -r mod 8 on the whole grid to dimension ten, so the two Minkowski "
      "residues 6 and 2 swap with the convention while the causal criterion "
      "min(p,q) = 1 is reversal-invariant: the labels swap and the count does not",
      all(res(q, p) == (-res(p, q)) % 8 for p in range(11) for q in range(11))
      and all(causal(q, p) == causal(p, q) for p in range(11) for q in range(11))
      and res(1, 3) == 6 and res(3, 1) == 2)


def nearest_dimension_representative(r):
    """Premise P3: dimension nearest four; for odd residues the lower of 3, 5
    if it can tell time, else the higher.  Returns the list of representatives."""
    if r % 2 == 0:
        return [s for s in SIGS if sum(s) == 4 and res(*s) == r]
    three = [s for s in SIGS if sum(s) == 3 and res(*s) == r]
    if any(causal(*s) for s in three):
        return three
    return [s for s in SIGS if sum(s) == 5 and res(*s) == r]


P3 = {r: nearest_dimension_representative(r) for r in range(8)}
sterile_P3 = sorted(r for r in range(8) if not any(causal(*s) for s in P3[r]))

g.check("prop:residues(ii): under P3 the representatives are (1,3) at 6, (3,1) at 2, "
      "(2,2) at 0, (4,0)/(0,4) at 4, (2,1) at 1, (1,2) at 7, (4,1) at 3, "
      "(1,4) at 5 (up to the definite companions the census also lists)",
      (1, 3) in P3[6] and (3, 1) in P3[2] and P3[0] == [(2, 2)]
      and sorted(P3[4]) == [(0, 4), (4, 0)] and (2, 1) in P3[1]
      and (1, 2) in P3[7] and (4, 1) in P3[3] and (1, 4) in P3[5])

g.check("prop:residues(ii): under P3 exactly {0, 4} are sterile, and these are "
      "the fixed points of r -> -r mod 8",
      sterile_P3 == [0, 4]
      and sorted(r for r in range(8) if (-r) % 8 == r) == [0, 4])

g.check("prop:residues: the count: eight towers, two sterile under P3, six "
      "populated", 8 - len(sterile_P3) == 6)


def sterile_in_window(lo, hi):
    return sorted(r for r in range(8)
                  if not any(causal(*s) for s in SIGS
                             if lo <= sum(s) <= hi and res(*s) == r))


g.check("prop:residues(iii): sensitivity: dims <= 5 -> sterile {4}; dims 3..6 "
      "-> sterile {0}; dims 3..10 -> nothing sterile; dims 3..5 -> {0, 4}",
      sterile_in_window(1, 5) == [4] and sterile_in_window(3, 6) == [0]
      and sterile_in_window(3, 10) == [] and sterile_in_window(3, 5) == [0, 4])

lowest_any = {r: min((s for s in SIGS if res(*s) == r),
                     key=lambda s: (sum(s), s)) for r in range(8)}
g.check("prop:residues(iii): with no lower bound the literal lowest "
      "representative of r = 6 is (0,2) and of r = 2 is (2,0), both definite: "
      "that criterion would sterilise this world",
      lowest_any[6] == (0, 2) and lowest_any[2] == (2, 0))

# ---------------------------------------------------------------------------
# Part B: the flag is blind to the residue (prop:flaggable)
# ---------------------------------------------------------------------------

# (1,3): rotation fixing e0 carries span(e0,e1) to span(e0,e2) and the null
# line R(e0+e1) to R(e0+e2)
G13 = [F(1), F(-1), F(-1), F(-1)]


def ip13(u, v):
    return sum(G13[i] * u[i] * v[i] for i in range(4))


E = [[F(int(i == j)) for j in range(4)] for i in range(4)]


def rot13(v):  # e1 -> e2, e2 -> -e1, fixes e0 and e3
    return [v[0], -v[2], v[1], v[3]]


g.check("prop:flaggable: in (1,3) the rotation e1 -> e2 is an isometry fixing "
      "the timelike direction e0 (and its orientation) and carrying "
      "span(e0,e1) onto span(e0,e2): the time orientation distinguishes no "
      "hyperbolic plane",
      all(ip13(rot13(a), rot13(b)) == ip13(a, b) for a in E for b in E)
      and rot13(E[0]) == E[0] and rot13(E[1]) == E[2]
      and rank([E[0], E[1]]) == 2
      and rank([rot13(E[0]), rot13(E[1]), E[0], E[2]]) == 2)

n1 = [F(1), F(1), F(0), F(0)]
n2 = rot13(n1)
g.check("prop:flaggable: the null lines e0+e1 and e0+e2 of (1,3) are isotropic "
      "and exchanged by the same rotation: no distinguished half of a "
      "hyperbolic pair either",
      ip13(n1, n1) == 0 and ip13(n2, n2) == 0 and n2 == [F(1), F(0), F(1), F(0)])

# (2,2): two totally isotropic planes exchanged by an isometry; and the
# isotropic family is one-parameter per component (Jacobian rank 3 in 4)
G22 = [F(1), F(1), F(-1), F(-1)]


def ip22(u, v):
    return sum(G22[i] * u[i] * v[i] for i in range(4))


P1 = ([F(1), 0, F(1), 0], [0, F(1), 0, F(1)])
P2 = ([F(1), 0, 0, F(1)], [0, F(1), F(1), 0])


def isotropic22(plane):
    a, b = plane
    return ip22(a, a) == 0 and ip22(b, b) == 0 and ip22(a, b) == 0


def swap34(v):
    return [v[0], v[1], v[3], v[2]]


g.check("prop:flaggable: in (2,2) two totally isotropic planes are exchanged "
      "by the isometry e3 <-> e4: no distinguished member there either",
      isotropic22(P1) and isotropic22(P2)
      and rank([swap34(P1[0]), swap34(P1[1]), list(P2[0]), list(P2[1])]) == 2)

# Jacobian of the three isotropy equations at P1 in the graph chart
# a = (1,0,1+m11,m12), b = (0,1,m21,1+m22); the three functions are quadratic
# in (m11, m12, m21, m22), so exact central differences with a rational step
# give the derivative exactly; nothing is typed by hand
def plane_chart(m):
    m11, m12, m21, m22 = m
    return ([F(1), F(0), 1 + m11, m12], [F(0), F(1), m21, 1 + m22])
def iso_eqs(m):
    a, b = plane_chart(m)
    return [ip22(a, a), ip22(b, b), ip22(a, b)]
def jacobian(fun, m0, h=F(1, 3)):
    cols = []
    for j in range(4):
        mp = list(m0); mm = list(m0); mp[j] += h; mm[j] -= h
        cols.append([(fp - fm) / (2 * h) for fp, fm in zip(fun(mp), fun(mm))])
    return [[cols[j][i] for j in range(4)] for i in range(len(cols[0]))]
JAC = jacobian(iso_eqs, [F(0)] * 4)
def gram_det(plane):
    a, b = plane
    return ip22(a, a) * ip22(b, b) - ip22(a, b) ** 2
HYP = [F(1), F(0), F(0), F(-1)]      # a = (1,0,2,0), b = (0,1,0,0): <a,a> = -3, <b,b> = 1, <a,b> = 0: hyperbolic
perturbed_hyperbolic = all(
    gram_det(plane_chart([HYP[k] + F(1, 5) * F(int(k == j)) * sgn for k in range(4)])) < 0
    for j in range(4) for sgn in (1, -1))
g.check("prop:flaggable: the totally isotropic planes of (2,2) form a "
      "one-parameter family per component (the Jacobian of the three isotropy "
      "equations, computed by exact central differences in the graph chart, "
      "has rank 3 in 4 unknowns), while a hyperbolic plane (Gram determinant "
      "negative) stays hyperbolic under a step of 1/5 in each of the four chart "
      "directions: the hyperbolic planes are open in the chart, a four-parameter "
      "family",
      len(JAC) == 3 and 4 - rank(JAC) == 1 and iso_eqs([F(0)] * 4) == [0, 0, 0]
      and gram_det(plane_chart(HYP)) < 0 and perturbed_hyperbolic)

# ---------------------------------------------------------------------------
# Part C: the count (prop:count)
# ---------------------------------------------------------------------------

# Planck 2018: Omega_c h^2 = 0.1200 +- 0.0012, Omega_b h^2 = 0.02237 +- 0.00015
OC, DOC = F(1200, 10 ** 4), F(12, 10 ** 4)
OB, DOB = F(2237, 10 ** 5), F(15, 10 ** 5)
OBS = F(5364, 1000)
g.check("prop:count: the survey ratio 0.1200/0.02237 lies in (5.36, 5.37) and "
      "rounds to the 5.364 used; its quadrature relative uncertainty is in "
      "(0.0119, 0.0122)",
      F(536, 100) < OC / OB < F(537, 100) and abs(OC / OB - OBS) < F(1, 1000)
      and F(119, 10 ** 4) ** 2 < (DOC / OC) ** 2 + (DOB / OB) ** 2 < F(122, 10 ** 4) ** 2)
g.check("prop:count(ii): the remainder's absolute uncertainty, 0.0976 times the "
      "quadrature relative uncertainty, lies in (0.00115, 0.0012): quoted as 0.0012",
      (F(115, 10 ** 5)) ** 2 < ((OBS - 1) * OB) ** 2 * ((DOC / OC) ** 2 + (DOB / OB) ** 2) < (F(12, 10 ** 4)) ** 2)
g.check("prop:count: the symmetric remainder (5.364 - 1) Omega_b h^2 equals the "
      "survey's own difference Omega_c h^2 - Omega_b h^2 to the rounding of "
      "5.364: 4.364 x 0.02237 = 0.09762268 against 0.1200 - 0.02237 = 0.09763",
      abs((OBS - 1) * OB - (OC - OB)) < F(1, 10 ** 5))

# ---------------------------------------------------------------------------
# Part D: the arrow (prop:arrow, prop:orientation)
# ---------------------------------------------------------------------------

# characteristic classes of gauge bundles have even degree (Chern classes in
# degree 2k, Pontryagin in 4k); a theta-term integrates a degree-d class over
# a d-dimensional tower
CHAR_DEGREES = sorted({2 * k for k in range(1, 6)} | {4 * k for k in range(1, 3)})
g.check("prop:arrow (RECORD, not a computation): the characteristic classes of "
      "gauge bundles have even degree, so no odd-dimensional tower (3 or 5) "
      "carries a continuous theta, while the four-dimensional towers do",
      all(d % 2 == 0 for d in CHAR_DEGREES)
      and 3 not in CHAR_DEGREES and 5 not in CHAR_DEGREES and 4 in CHAR_DEGREES)

# homotopy bookkeeping: bundles on S^d are classified by pi_{d-1}(G)
PI = {("SU2", 2): 0, ("SU2", 3): "Z", ("SU2", 4): "Z2",
      ("SU3", 2): 0, ("SU3", 3): "Z", ("SU3", 4): 0}
g.check("prop:arrow (RECORD, not a computation): pi_2(G) = 0 (no instanton sectors in three dimensions); "
      "pi_3 = Z in four; pi_4(SU(2)) = Z_2 and pi_4(SU(3)) = 0 in five: at most "
      "a discrete angle, never a continuous theta, in odd dimension",
      PI[("SU2", 2)] == 0 and PI[("SU3", 2)] == 0
      and PI[("SU2", 3)] == "Z" and PI[("SU3", 3)] == "Z"
      and PI[("SU2", 4)] == "Z2" and PI[("SU3", 4)] == 0)


def grade(s):
    return bin(s).count("1")


# the flag conjugate on the Fock ideal is checked in Part J, where the ideal
# is built in GA.py (the three-bit model it replaces was a property of the
# encoding, not of the claim)

# the fibre metric (symmetric part of the Clifford product) is fixed by the
# exchange of a null pair: on Cl(1,1) with null pair v = e+ + e-, w = e+ - e-
squares = g.sig(1, 1)
ep, em = g.gen(0), g.gen(1)
v = g.add(ep, em)
w = g.sub(ep, em)


def sym(x, y):
    return g.scal(F(1, 2), g.add(g.mul(x, y, squares), g.mul(y, x, squares)))


def refl_em(x):      # the reflection negating e-: x -> -e- x e-^{-1}; with e-^2 = -1, e-^{-1} = -e-, so x -> e- x e-
    return g.mul(g.mul(em, x, squares), em, squares)
g.check("prop:orientation: on Cl(1,1) the null pair v = e+ + e-, w = e+ - e- "
      "is null (v^2 = w^2 = 0); the reflection negating e- (the versor e-) "
      "fixes e+, negates e-, exchanges v and w, and preserves the quadratic "
      "form on all four (v^2, w^2 and the symmetric product v.w = 2 carried "
      "to themselves): the flag conjugate is an isometry of the rung",
      g.is_zero(g.mul(v, v, squares)) and g.is_zero(g.mul(w, w, squares))
      and g.eq(refl_em(ep), ep) and g.eq(refl_em(em), g.neg(em))
      and g.eq(refl_em(v), w) and g.eq(refl_em(w), v)
      and g.eq(sym(refl_em(v), refl_em(w)), sym(v, w))
      and g.eq(sym(v, w), {(): F(2)}))

# ---------------------------------------------------------------------------
# Part E: projection, the audit, the open channel (lem:projection,
# prop:audit, prop:openchannel)
# ---------------------------------------------------------------------------


def projected_exponents(D, coexpand, sheets=True):
    """(matter, radiation) powers of a for a tower with D spatial dims,
    projected onto the shared three-volume, computed from the sourcing rule
    rather than typed: the shared directions (min(D,3)) expand with a; the
    extra directions (D - 3 if positive) expand with a or are static; a
    missing shared direction (3 - D if positive) is filled by a comoving
    family of sheets (sheets=True, the lemma's hypothesis) or by a single
    sheet of fixed thickness (sheets=False, the reading the lemma excludes)."""
    shared = min(D, 3)
    extra = max(D - 3, 0)
    missing = max(3 - D, 0)
    n_exp = shared + (extra if coexpand else 0)   # expanding directions in the tower
    matter = -n_exp                               # number density per tower volume
    radiation = -n_exp - 1                        # one redshift factor for a massless quantum
    # integrate over the extra directions: co-expanding ones contribute a^extra
    proj = extra if coexpand else 0
    # a missing direction: a comoving sheet family has a^-missing sheets per
    # unit proper length; a single fixed sheet contributes no power
    fill = -missing if sheets else 0
    return (matter + proj + fill, radiation + proj + fill)


g.check("lem:projection: computed from the sourcing rule for D = 2, 3, 4, "
      "co-expanding and static, the projected exponents are (-3, -4) in every "
      "case under the comoving-sheet hypothesis, and the single-sheet reading "
      "of the missing direction gives (-2, -3) for D = 2, which the lemma excludes",
      all(projected_exponents(D, c) == (-3, -4)
          for D in (2, 3, 4) for c in (True, False))
      and projected_exponents(2, True, sheets=False) == (-2, -3)
      and projected_exponents(2, False, sheets=False) == (-2, -3))

# N_eff arithmetic: rho_nu / rho_gamma = (7/8) (4/11)^(4/3) per species
lo3, hi3 = icbrt_bracket(F(4, 11))          # brackets (4/11)^(1/3)
r_lo = F(7, 8) * F(4, 11) * lo3
r_hi = F(7, 8) * F(4, 11) * hi3
dN_lo, dN_hi = 1 / r_hi, 1 / r_lo          # Delta N_eff of a 2-dof boson at T_gamma
g.check("prop:audit: one neutrino species carries between 0.2270 and 0.2272 "
      "of the photon energy density, so a two-polarisation boson at T_gamma "
      "is Delta N_eff between 4.40 and 4.41, and five such are between 22 "
      "and 22.1 ('of order twenty')",
      F(2270, 10 ** 4) < r_lo and r_hi < F(2272, 10 ** 4)
      and F(440, 100) < dN_lo and dN_hi < F(441, 100)
      and 22 < 5 * dN_lo and 5 * dN_hi < F(221, 10))

g.check("prop:audit: even one surviving photon-like species at T_gamma exceeds "
      "the Planck cap 0.3 by more than a factor of ten",
      dN_lo > 10 * F(3, 10))

g.check("prop:charge: the thermal reading's cap is the cube of the typed threshold "
      "0.448..: 0.448^3 = 0.0899 lies in (0.0899, 0.0900), 'at most 0.090'",
      F(899, 10 ** 4) < F(448, 1000) ** 3 < F(900, 10 ** 4))

g.check("prop:openchannel: with only the heaviest mirror neutrino non-relativistic the "
      "coefficient is 4.403 + 2 in (6.40, 6.41) and the threshold (0.3/6.41)^(1/4) in "
      "(0.464, 0.466), quoted as 0.47",
      F(640, 100) < dN_lo + 2 and dN_hi + 2 < F(641, 100)
      and F(464, 1000) ** 4 < F(3, 10) / (dN_hi + 2) and F(3, 10) / (dN_lo + 2) < F(466, 1000) ** 4)

# thresholds: (T3/Tgamma)^4 < 0.3 / (2.2 g3)  <=>  T3/Tgamma < (0.3/(2.2 g3))^(1/4)
cap = F(3, 10)
per_dof_lo, per_dof_hi = dN_lo / 2, dN_hi / 2   # bound here, not inside the loop below
for g3, lo_t, hi_t, lab in ((2, F(51, 100), F(52, 100), "0.51"), (3, F(46, 100), F(47, 100), "0.46")):
    x = cap / (per_dof_hi * g3)   # lower bound on the allowed (T3/Tg)^4
    y = cap / (per_dof_lo * g3)   # upper bound
    g.check("prop:openchannel: with g3 = %d light polarisations the cap is met "
          "iff T3/Tgamma < about %s (the fourth root of the allowed ratio is "
          "bracketed exactly)" % (g3, lab),
          lo_t ** 4 < x and y < hi_t ** 4)

# entropy-release factor (g*(GeV)/g*(now))^(1/3) ~ 2.51 and the resulting
# Delta N_eff ~ 0.11 for g3 = 2
gs_gev, gs_now = F(6175, 100), F(391, 100)
lo_c, hi_c = icbrt_bracket(gs_gev / gs_now)
g.check("prop:openchannel(a): (61.75/3.91)^(1/3) lies in (2.50, 2.52), and a "
      "two-polarisation species colder by that factor gives Delta N_eff in "
      "(0.10, 0.12), under the cap",
      F(250, 100) < lo_c and hi_c < F(252, 100)
      and F(10, 100) < dN_lo / hi_c ** 4 and dN_hi / lo_c ** 4 < F(12, 100))

g.check("prop:openchannel: route (a) alone puts one two-polarisation species at "
      "4.40/2.51^4 in (0.10, 0.12), so two five-dimensional towers sit at (0.21, "
      "0.23) with two polarisations each, under the cap, and at (0.32, 0.34) with "
      "three each, over it",
      F(10, 100) < dN_lo / hi_c ** 4 and dN_hi / lo_c ** 4 < F(12, 100)
      and F(21, 100) < 2 * dN_lo / hi_c ** 4 and 2 * dN_hi / lo_c ** 4 < F(23, 100)
      and F(32, 100) < 3 * dN_lo / hi_c ** 4 and 3 * dN_hi / lo_c ** 4 < F(34, 100)
      and 3 * dN_lo / hi_c ** 4 > cap)


# ---------------------------------------------------------------------------
# Part F: the ceiling range (prop:ceiling)
# ---------------------------------------------------------------------------

mt_lo, mt_hi = F(172), F(174)
mb_lo, mb_hi = F(415, 100), F(421, 100)
m3_lo, m3_hi = F(45, 10 ** 12), F(55, 10 ** 12)     # GeV
g.check("prop:ceiling: m_t^2/m_3 lies in (5e14, 7e14) GeV and m_b^2/m_3 in "
      "(3e11, 4e11) GeV for the stated input brackets, exact rational division",
      5 * 10 ** 14 < mt_lo ** 2 / m3_hi and mt_hi ** 2 / m3_lo < 7 * 10 ** 14
      and 3 * 10 ** 11 < mb_lo ** 2 / m3_hi and mb_hi ** 2 / m3_lo < 4 * 10 ** 11)
g.check("prop:ceiling: the ends of the range differ by (m_t/m_b)^2 in "
      "(1600, 1800)", 1600 < (mt_lo / mb_hi) ** 2 and (mt_hi / mb_lo) ** 2 < 1800)


# ---------------------------------------------------------------------------
# Part G: spinor type, the soldered invariant, and the mode counts
# (thm:types, thm:soldered, thm:modes)
# ---------------------------------------------------------------------------

from itertools import combinations

def centre_dim(n, sq):
    blades = g.all_blades(n)
    # x commutes with every generator e_i  <=>  linear conditions on coeffs
    rows = []
    for i in range(n):
        ei = g.gen(i)
        cols = []
        for b in blades:
            x = {b: F(1)}
            c = g.sub(g.mul(ei, x, sq), g.mul(x, ei, sq))
            cols.append(g.basis_vector_of(c, blades))
        # equations: for each output blade, sum_b coeff_b * cols[b][out] = 0
        for out in range(len(blades)):
            rows.append([cols[b][out] for b in range(len(blades))])
    return len(blades) - g.rank_of_vectors(rows)


def blade_square(b, sq):
    x = {b: F(1)}
    return g.mul(x, x, sq).get((), F(0))


def commute_blades(b1, b2, sq):
    x, y = {b1: F(1)}, {b2: F(1)}
    return g.eq(g.mul(x, y, sq), g.mul(y, x, sq))


def primitive_idempotent(n, sq):
    """largest set of pairwise commuting basis blades squaring to +1 whose
    generated group does not contain -1 (Lounesto); f = prod (1+e_T)/2"""
    blades = [b for b in g.all_blades(n) if b != () and blade_square(b, sq) == 1]
    best = []
    for k in range(len(blades), 0, -1):
        for S in combinations(blades, k):
            if all(commute_blades(a, b, sq) for a, b in combinations(S, 2)):
                # group generated must have order 2^k: check products of
                # subsets are distinct blades (never -1 or a repeat)
                seen = set()
                ok = True
                for m in range(1, k + 1):
                    for T in combinations(S, m):
                        prod = {(): F(1)}
                        for t in T:
                            prod = g.mul(prod, {t: F(1)}, sq)
                        (bl, co), = prod.items()
                        if bl == () or bl in seen or co != 1:
                            ok = False
                            break
                        seen.add(bl)
                    if not ok:
                        break
                if ok:
                    best = list(S)
                    break
        if best:
            break
    f = {(): F(1)}
    for t in best:
        f = g.mul(f, g.scal(F(1, 2), g.add({(): F(1)}, {t: F(1)})), sq)
    return best, f


def dim_fAf(n, sq, f):
    blades = g.all_blades(n)
    vecs = []
    for b in blades:
        y = g.mul(g.mul(f, {b: F(1)}, sq), f, sq)
        vecs.append(g.basis_vector_of(y, blades))
    return g.rank_of_vectors(vecs)


def analyse(p, q):
    n = p + q
    sq = g.sig(p, q)
    c = centre_dim(n, sq)
    omega = tuple(range(n))
    w2 = blade_square(omega, sq)
    S, f = primitive_idempotent(n, sq)
    INTERNAL_OK.append(g.eq(g.mul(f, f, sq), f))
    d = dim_fAf(n, sq, f)
    dimA = 2 ** n
    comps = 2 if (c == 2 and w2 == 1) else 1
    # simple component dim = m^2 d  ->  m = sqrt(dimA/comps/d); irreducible
    # module real dim = m d
    from math import isqrt
    m2 = dimA // comps // d
    m = isqrt(m2)
    INTERNAL_OK.append(m * m == m2)
    return dict(sig=(p, q), r=(p - q) % 8, centre=c, omega2=w2, k=len(S),
                D={1: "R", 2: "C", 4: "H"}[d], comps=comps, m=m, dimS=m * d)




P3_REPS = {6: (1, 3), 2: (3, 1), 0: (2, 2), 4: (4, 0), 1: (2, 1),
              7: (1, 2), 3: (4, 1), 5: (1, 4)}
TYPE = {r: analyse(*s) for r, s in P3_REPS.items()}
EXPECTED_D = {0: "R", 1: "R", 2: "R", 3: "C", 4: "H", 5: "H", 6: "H", 7: "C"}
EXPECTED_COMPS = {r: (2 if r in (1, 5) else 1) for r in range(8)}

g.check("thm:types: the representative table this part runs on is the census function's, "
      "reconciled residue by residue with Part A's P3 rather than typed independently; "
      "and for every P3 representative the division algebra fAf of a "
      "primitive idempotent (Lounesto construction, computed exactly) is R "
      "for r = 0, 1, 2, C for r = 3, 7 and H for r = 4, 5, 6",
      all(P3_REPS[r] in P3[r] for r in range(8))
      and all(TYPE[r]["D"] == EXPECTED_D[r] for r in range(8)))
g.check("thm:types: the centre is two-dimensional exactly for the odd residues, "
      "with omega^2 = +1 (two simple components) at r = 1, 5 and omega^2 = -1 "
      "(a complex centre, one component) at r = 3, 7",
      all((TYPE[r]["centre"] == 2) == (r % 2 == 1) for r in range(8))
      and all(TYPE[r]["comps"] == EXPECTED_COMPS[r] for r in range(8))
      and TYPE[3]["omega2"] == -1 and TYPE[7]["omega2"] == -1
      and TYPE[1]["omega2"] == 1 and TYPE[5]["omega2"] == 1)
g.check("thm:types: the type is a residue invariant on the full census to "
      "dimension five (every signature of each residue has the same D and "
      "component count)",
      all(analyse(p, n - p)["D"] == EXPECTED_D[(2 * p - n) % 8]
          and analyse(p, n - p)["comps"] == EXPECTED_COMPS[(2 * p - n) % 8]
          for n in range(1, 6) for p in range(n + 1)))

# the soldered invariant: Cl(1,3) and Cl(0,4) agree in every abstract
# invariant computed here (dimension, centre, D, component count, module
# dimension) yet differ in signature; and no vector of Cl(0,4) squares to a
# positive scalar, so no isomorphism preserving the generating subspace exists
A6, A4 = TYPE[6], TYPE[4]
g.check("thm:soldered: Cl(1,3) (r = 6) and Cl(0,4) (r = 4) have the same "
      "dimension 16, centre 1, D = H, one component and module dimension 8: "
      "abstract algebra does not see the residue",
      (A6["centre"], A6["D"], A6["comps"], A6["dimS"])
      == (A4["centre"], A4["D"], A4["comps"], A4["dimS"]) == (1, "H", 1, 8))
g.check("thm:soldered: likewise Cl(1,1) and Cl(2,0) (r = 0, 2) and Cl(1,2) and "
      "Cl(3,0) (r = 7, 3) are abstractly alike",
      (analyse(1, 1)["D"], analyse(1, 1)["comps"]) == (analyse(2, 0)["D"], analyse(2, 0)["comps"])
      and (analyse(1, 2)["D"], analyse(1, 2)["comps"]) == (analyse(3, 0)["D"], analyse(3, 0)["comps"]))

sq04, sq13 = g.sig(0, 4), g.sig(1, 3)
def vec(coeffs):
    return {(i,): F(c) for i, c in enumerate(coeffs) if c != 0}
def vsq(v, sq):
    return g.mul(v, v, sq).get((), F(0))
SAMPLE = [(1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0), (2, -1, 3, 1), (1, 2, 2, -3), (0, 0, 1, 1)]
g.check("thm:soldered: every sampled vector of Cl(0,4) squares to a "
      "non-positive scalar while e0 of Cl(1,3) squares to +1: the signature "
      "is read off the generating subspace, so a vector-preserving "
      "isomorphism between residues 6 and 4 cannot exist",
      all(vsq(vec(c), sq04) <= 0 for c in SAMPLE)
      and vsq(vec((1, 0, 0, 0)), sq13) == 1
      and all(vsq(vec(c), sq04) == -sum(x * x for x in c) for c in SAMPLE))
g.check("thm:soldered: on Cl(1,3) the quadratic form v -> v^2 on sampled "
      "vectors is c0^2 - c1^2 - c2^2 - c3^2: signature (1,3) recovered",
      all(vsq(vec(c), sq13) == c[0] ** 2 - c[1] ** 2 - c[2] ** 2 - c[3] ** 2
          for c in SAMPLE))

# mode counts: ground-module real dimensions of the populated P3 representatives,
# with both simple components at r = 1, 5 (the P2 reading) and the Witt index
POP = [6, 2, 1, 7, 3, 5]
dimS_total = {r: TYPE[r]["dimS"] * TYPE[r]["comps"] for r in POP}
dimS_single = {r: TYPE[r]["dimS"] for r in POP}
g.check("thm:modes: ground-module real dimensions (both components where the "
      "centre splits): r = 6: 8, r = 2: 4, r = 1: 4, r = 7: 4, r = 3: 8, "
      "r = 5: 16; single components: r = 1: 2, r = 5: 8",
      dimS_total == {6: 8, 2: 4, 1: 4, 7: 4, 3: 8, 5: 16}
      and dimS_single[1] == 2 and dimS_single[5] == 8)
g.check("thm:modes: every populated P3 representative has Witt index min(p,q) = 1, so "
      "the rung capacity 1 + k is residue-independent (T3 Thm 4.3)",
      all(min(*P3_REPS[r]) == 1 for r in POP))
sum_both = sum(F(dimS_total[r], dimS_total[6]) for r in POP if r != 6)
sum_single = sum(F(dimS_single[r], dimS_single[6]) for r in POP if r != 6)
sum_both_other = sum(F(dimS_total[r], dimS_total[2]) for r in POP if r != 2)
sum_single_other = sum(F(dimS_single[r], dimS_single[2]) for r in POP if r != 2)
g.check("thm:modes(iii): the ground-module weighting of the five dark towers is "
      "9/2 (both components) or 13/4 (one component) in the paper's convention, "
      "where this world is r = 6 with an 8-dimensional module, and 10 or 15/2 "
      "in the opposite convention, where this world is the 4-dimensional real "
      "module at r = 2: the weighting is convention-dependent",
      sum_both == F(9, 2) and sum_single == F(13, 4)
      and sum_both_other == 10 and sum_single_other == F(15, 2))


# ---------------------------------------------------------------------------
# Part H: the fragility bound (prop:massbound(ii)).  Logarithms and exponentials in
# forty-digit decimal arithmetic (the T13 precedent); the inequality chain
# itself as exact rational algebra.
# ---------------------------------------------------------------------------

from decimal import Decimal as Dec, getcontext
getcontext().prec = 40

def b_coeff(nf):
    return 11 - F(2, 3) * nf

g.check("prop:massbound (RECORD: the one-loop formula and its values, typed): "
      "b = 11 - 2 n_f / 3 gives b_6 = 7 at n_f = 6, b_2 = 9 at n_f = 3; one "
      "Dirac flavour is Delta b = 2/3, and Delta b = 1 is one and a half flavours",
      b_coeff(6) == 7 and b_coeff(3) == 9
      and b_coeff(5) - b_coeff(6) == F(2, 3) and b_coeff(F(9, 2)) - b_coeff(6) == 1)

# inequality chain: b6max * L >= Db * (L0 - L)  =>  L >= Db L0 / (b6max + Db)
# checked on a grid of exact rationals: for every L satisfying the premise
# the conclusion holds, and the bound is attained at equality
def chain_ok(b6max, Db, L0):
    Lstar = Db * L0 / (b6max + Db)
    # premise at L = Lstar holds with equality
    if b6max * Lstar != Db * (L0 - Lstar):
        return False
    # any L with b6max L >= Db (L0 - L) has L >= Lstar (monotone in L)
    for k in range(0, 41):
        L = L0 * k / 40
        premise = b6max * L >= Db * (L0 - L)
        if premise and not (L >= Lstar):
            return False
    return True

g.check("prop:massbound(ii): the inequality chain b6 L >= Db (L0 - L) => "
      "L >= Db L0 / (b6 + Db) holds as exact rational algebra on a 41-point grid "
      "for (b6, Db) = (11, 1), (9, 1), (7, 2), (9, 2), (11, 2/3), (7, 2/3), and the "
      "bound equals the proposition's typed values L0/12 (Delta b = 1, b6 = 11), "
      "2 L0/35 (2/3, 11) and 2 L0/23 (2/3, 7)",
      all(chain_ok(F(b6), F(Db), F(35)) for b6, Db in ((11, 1), (9, 1), (7, 2), (9, 2), (11, F(2, 3)), (7, F(2, 3))))
      and F(1) * F(35) / (11 + 1) == F(35) / 12
      and F(2, 3) * F(35) / (11 + F(2, 3)) == 2 * F(35) / 35
      and F(2, 3) * F(35) / (7 + F(2, 3)) == 2 * F(35) / 23)

L0 = (Dec(6) * Dec(10) ** 14 / Dec("0.3")).ln()
L0_low = (Dec("3.5") * Dec(10) ** 11 / Dec("0.3")).ln()
g.check("prop:massbound(ii): L0 = ln(2 x 10^15) lies in (35.2, 35.3) at the top of "
      "the ceiling range and ln(3.5e11/0.3) in (27.7, 27.9) at the bottom",
      Dec("35.2") < L0 < Dec("35.3") and Dec("27.7") < L0_low < Dec("27.9"))
def frag(L, b6, Db):
    return (Db * L / (b6 + Db)).exp()
r_cons = frag(L0, Dec(11), Dec(1))
g.check("prop:massbound(ii): one Dirac flavour (Delta b = 2/3) moves Lambda_2/Lambda_6 "
      "by e^(2 L0/35) in (7.4, 7.6) at b_6 = 11 and e^(2 L0/23) in (21, 22) at "
      "b_6 = 7 at the top of the ceiling range, and by (4.8, 5.0) and (11, 11.5) "
      "at the bottom: above 5.364 everywhere except the bottom of the range on "
      "the b_6 = 11 branch; Delta b = 1 gives e^(L0/12) in (18.8, 18.9)",
      Dec("7.4") < frag(L0, Dec(11), Dec(2) / 3) < Dec("7.6")
      and Dec(21) < frag(L0, Dec(7), Dec(2) / 3) < Dec(22)
      and Dec("4.8") < frag(L0_low, Dec(11), Dec(2) / 3) < Dec("5.0")
      and Dec(11) < frag(L0_low, Dec(7), Dec(2) / 3) < Dec("11.5")
      and frag(L0_low, Dec(11), Dec(2) / 3) < Dec("5.364") < frag(L0, Dec(11), Dec(2) / 3)
      and Dec("18.8") < r_cons < Dec("18.9"))

PI = Dec("3.14159265358979323846264338327950288")
def departure(x):
    M, Lam6 = Dec(6) * Dec(10) ** 14, Dec("0.3")
    return Dec(9) / (2 * PI) * (M / (x * Lam6)).ln() - Dec(7) / (2 * PI) * (M / Lam6).ln()

g.check("prop:massbound(ii): e^(2 pi / 7), the factor per unit of 1/alpha at b = 7, "
      "lies in (2.45, 2.46)", Dec("2.45") < (2 * PI / 7).exp() < Dec("2.46"))
g.check("prop:massbound(ii) (RECORD of the script's own illustration, not the "
      "proposition's): the coupling departure 1/alpha_2(M) - 1/alpha_6(M) "
      "that would accompany Lambda_2 = x Lambda_6 with b_2 = 9, b_6 = 7 is in "
      "(11.2, 11.3) at x = 1 and (10.2, 10.3) at x = 2",
      Dec("11.2") < departure(Dec(1)) < Dec("11.3")
      and Dec("10.2") < departure(Dec(2)) < Dec("10.3"))

g.check("prop:massbound(ii): with identical content a coupling departure of 0.1 "
      "units at the ceiling moves Lambda by e^(2 pi 0.1 / 7) in (1.09, 1.10) and one of "
      "0.106 by (1.099, 1.101): the ten-percent window is |delta| < 0.106",
      Dec("1.09") < (2 * PI * Dec("0.1") / 7).exp() < Dec("1.10")
      and Dec("1.099") < (2 * PI * Dec("0.106") / 7).exp() < Dec("1.101"))


# ---------------------------------------------------------------------------
# Part I: the mirror copy (thm:mirror, prop:count, prop:openchannel)
# ---------------------------------------------------------------------------

def even_subalgebra_relations(p, q):
    """e_i e_n (i < n) pairwise anticommute and square to -e_i^2 e_n^2 = e_i^2
    when e_n^2 = -1: the standard Cl^0(p,q) = Cl(p, q-1) identification."""
    n = p + q
    sq = g.sig(p, q)
    en = g.gen(n - 1)
    fs = [g.mul(g.gen(i), en, sq) for i in range(n - 1)]
    ok = sq[n - 1] == -1
    for i, fi in enumerate(fs):
        ok = ok and g.eq(g.mul(fi, fi, sq), {(): F(sq[i])})
        for j in range(i + 1, n - 1):
            ok = ok and g.is_zero(g.add(g.mul(fi, fs[j], sq), g.mul(fs[j], fi, sq)))
    return ok

g.check("thm:mirror: Cl^0(p,q) = Cl(p, q-1) by the generators e_i e_n, "
      "verified exactly for (2,4), (4,2), (1,3), (3,1)",
      all(even_subalgebra_relations(p, q) for p, q in ((2, 4), (4, 2), (1, 3), (3, 1))))

T23, T41 = analyse(2, 3), analyse(4, 1)
T12_, T30 = analyse(1, 2), analyse(3, 0)
g.check("thm:mirror: Cl(2,3) and Cl(4,1) have the same type (C, one component, "
      "module dimension 8): both M(4,C), so Spin(2,4) = Spin(4,2) = SU(2,2)",
      (T23["D"], T23["comps"], T23["dimS"]) == (T41["D"], T41["comps"], T41["dimS"]) == ("C", 1, 8))
g.check("thm:mirror: Cl(1,2) and Cl(3,0) have the same type (C, one component, "
      "module dimension 4): both M(2,C), so Spin(1,3) = Spin(3,1) = SL(2,C)",
      (T12_["D"], T12_["comps"], T12_["dimS"]) == (T30["D"], T30["comps"], T30["dimS"]) == ("C", 1, 4))

def isotropic_capacity(m, extra):
    """On the split form with m plus and m minus generators (and `extra`
    further generators squaring to +1), exhibit m mutually orthogonal null
    vectors u_i = e_i + e_{m+i}, verify isotropy and orthogonality exactly, and
    compute dim U^perp by exact rank so that dim U <= dim V / 2 is forced by
    U subset U^perp; returns (m, dim V, dim U^perp)."""
    sq = tuple([1] * m + [-1] * m + [1] * extra)
    n = len(sq)
    us = [[F(int(k == i)) + F(int(k == m + i)) for k in range(n)] for i in range(m)]
    ip = lambda a, b: sum(F(sq[k]) * a[k] * b[k] for k in range(n))
    INTERNAL_OK.append(all(ip(u, v) == 0 for u in us for v in us))
    # U^perp: kernel of the m x n Gram map v -> (ip(u_i, v))_i
    gram_rows = [[F(sq[k]) * u[k] for k in range(n)] for u in us]
    dim_perp = n - g.rank_of_vectors(gram_rows)
    return m, n, dim_perp

caps = {n_sp: isotropic_capacity((n_sp + 2) // 2, (n_sp + 2) % 2) for n_sp in (3, 4, 5)}
g.check("thm:modes(iv): on the split forms of dimensions five, six and seven "
      "m = 2, 3, 3 mutually orthogonal null vectors exist (isotropy and "
      "orthogonality exact) and their span U has dim U^perp = dim V - m, so "
      "U subset U^perp forces m <= dim V / 2: the pair counts 2, 3, 3 are "
      "exhibited and bounded in GA.py (m itself is the formula's value; what "
      "is computed is the exact null vectors and dim U^perp)",
      all(caps[n_sp][2] == caps[n_sp][1] - caps[n_sp][0] for n_sp in (3, 4, 5))
      and all(caps[n_sp][0] <= caps[n_sp][1] // 2 for n_sp in (3, 4, 5))
      and (caps[3][0], caps[4][0], caps[5][0]) == (2, 3, 3))

# mirror N_eff: photons (4.40) plus three neutrinos (3.044) in neutrino units
NNU = F(3044, 1000)
mir_lo, mir_hi = dN_lo + NNU, dN_hi + NNU
g.check("prop:openchannel: the mirror sector's relativistic content in neutrino "
      "units is 7.447 (photon 4.403 plus 3.044), so Delta N_eff = 7.447 (T'/T)^4",
      F(744, 100) < mir_lo and mir_hi < F(745, 100))
x_lo, x_hi = cap / mir_hi, cap / mir_lo        # allowed (T'/T)^4
g.check("prop:openchannel: the cap 0.3 requires T'/T_gamma < 0.448 (the fourth "
      "root of the allowed ratio lies in (0.4480, 0.4481)), exact fourth-power "
      "inequalities; and the cube of the threshold, the thermal reading's cap, "
      "lies in (0.0899, 0.0900)",
      F(4480, 10 ** 4) ** 4 < x_lo and x_hi < F(4481, 10 ** 4) ** 4
      and F(899, 10 ** 4) < F(4480, 10 ** 4) ** 3 and F(4481, 10 ** 4) ** 3 < F(900, 10 ** 4))
g.check("prop:openchannel: a silent decoupled copy at 1/2.51 of our temperature "
      "would give 7.447/2.51^4 in (0.18, 0.19), under the cap; recorded, the "
      "copy is not silent",
      F(18, 100) < mir_lo / hi_c ** 4 and mir_hi / lo_c ** 4 < F(19, 100))


# ---------------------------------------------------------------------------
# Part J: the flag bit exists exactly in the even residues (thm:paritybit,
# cor:whocarries), the charge reading (rem:chempot), and the count's
# arithmetic (prop:count)
# ---------------------------------------------------------------------------

def diag_isometry(n, signs):
    return [[F(signs[i]) if i == j else F(0) for j in range(n)] for i in range(n)]

def det(Mx):
    Mx = [row[:] for row in Mx]; n = len(Mx); d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if Mx[r][c] != 0), None)
        if p is None: return F(0)
        if p != c: Mx[c], Mx[p] = Mx[p], Mx[c]; d = -d
        d *= Mx[c][c]
        for r in range(c + 1, n):
            f = Mx[r][c] / Mx[c][c]; Mx[r] = [a - f * b for a, b in zip(Mx[r], Mx[c])]
    return d

def preserves(Mx, sq):
    n = len(sq)
    return all(sum(Mx[k][i] * F(sq[k]) * Mx[k][j] for k in range(n)) == (F(sq[i]) if i == j else F(0))
               for i in range(n) for j in range(n))

def carries_W_to_Wprime(Mx, m):
    n = len(Mx)
    for i in range(m):
        w = [F(0)] * n; w[i] = F(1); w[m + i] = F(1)
        img = [sum(Mx[r][c] * w[c] for c in range(n)) for r in range(n)]
        if not (img[i] == -img[m + i] and all(img[k] == 0 for k in range(n) if k not in (i, m + i))):
            return False
    return True

# Definition def:fock and Proposition prop:families in GA.py: on the split form
# with generators e_0..e_{m-1} (square +1) and e_m..e_{2m-1} (square -1), plus an
# extra generator ell (square +1) in odd dimension, the null pairs
# w_i = (e_i + e_{m+i})/2, v_i = (e_i - e_{m+i})/2 satisfy v_i w_j + w_j v_i =
# delta_ij; f = w_1...w_m is the null blade; top = v_1...v_m f; I = product of
# all generators (I^2 = +1 on these forms).  Everything below is exact.
def fock_data(m, extra):
    sq = tuple([1] * m + [-1] * m + [1] * extra)
    n = len(sq)
    w = [g.scal(F(1, 2), g.add(g.gen(i), g.gen(m + i))) for i in range(m)]
    v = [g.scal(F(1, 2), g.sub(g.gen(i), g.gen(m + i))) for i in range(m)]
    f = w[0]
    for x in w[1:]: f = g.mul(f, x, sq)
    top = f
    for x in reversed(v): top = g.mul(x, top, sq)
    I = g.gen(0)
    for i in range(1, n): I = g.mul(I, g.gen(i), sq)
    return sq, n, w, v, f, top, I
def eigen(I, psi, sq):
    """eigenvalue lambda with I psi = lambda psi, or None"""
    for lam in (F(1), F(-1)):
        if g.eq(g.mul(I, psi, sq), g.scal(lam, psi)): return lam
    return None
def anticomm(a, b, sq): return g.is_zero(g.add(g.mul(a, b, sq), g.mul(b, a, sq)))
def comm(a, b, sq): return g.is_zero(g.sub(g.mul(a, b, sq), g.mul(b, a, sq)))
fam_ok = True; chir = {}
for m in (2, 3, 4):
    sq, n, w, v, f, top, I = fock_data(m, 0)
    one = g.scal(F(1), g.gen(0)); one = g.mul(g.gen(0), g.gen(0), sq)     # the scalar 1
    ccr = all(g.eq(g.add(g.mul(v[i], w[j], sq), g.mul(w[j], v[i], sq)),
                   g.scal(F(int(i == j)), one)) for i in range(m) for j in range(m))
    annih_f = all(g.is_zero(g.mul(x, f, sq)) for x in w) and not g.is_zero(f)
    annih_top = all(g.is_zero(g.mul(x, top, sq)) for x in v) and not g.is_zero(top)
    I2 = g.eq(g.mul(I, I, sq), one)
    anti = all(anticomm(I, g.gen(i), sq) for i in range(n))
    lf, lt = eigen(I, f, sq), eigen(I, top, sq)
    chir[m] = (lf, lt)
    fam_ok = fam_ok and ccr and annih_f and annih_top and I2 and anti and lf is not None and lt is not None
g.check("prop:families (GA.py, dimensions four, six, eight): the null pairs satisfy "
      "v_i w_j + w_j v_i = delta_ij exactly; the null blade f is killed by W and the "
      "top state v_1...v_m f by W'; I^2 = 1 and I anticommutes with every "
      "generator; f and the top state are chirality eigenstates",
      fam_ok)
g.check("prop:families(iii)/thm:paritybit: the chiralities of f and of the top state "
      "agree at m = 2 and m = 4 (tower dimensions two and six: no bit) and differ "
      "at m = 3 (this tower and the mirror: the bit), i.e. their ratio is (-1)^m",
      all(chir[m][0] == chir[m][1] * F((-1) ** m) for m in (2, 3, 4)))
# the exchanging versor R = e_m ... e_{2m-1} (the reflections negating the partners),
# of parity m: R f is annihilated by W', so it is the pure spinor of W', and I R f =
# (-1)^m R I f, which is the whole theorem
versor_ok = True
for m in (2, 3, 4):
    sq, n, w, v, f, top, I = fock_data(m, 0)
    R = g.gen(m)
    for i in range(m + 1, 2 * m): R = g.mul(R, g.gen(i), sq)
    Rf = g.mul(R, f, sq)
    pure_of_Wprime = all(g.is_zero(g.mul(x, Rf, sq)) for x in v) and not g.is_zero(Rf)
    lam = eigen(I, Rf, sq)
    versor_ok = versor_ok and pure_of_Wprime and lam is not None and lam == chir[m][0] * F((-1) ** m)
g.check("prop:families(ii): the versor R = e_m ... e_{2m-1} of parity m carries the "
      "pure spinor f of W to a pure spinor R f of W' (killed by every v_i), and "
      "the chirality of R f is (-1)^m times that of f: odd versors reverse "
      "chirality, even ones preserve it",
      versor_ok)
odd_ok = True
for m, extra in ((2, 1), (3, 1)):
    sq, n, w, v, f, top, I = fock_data(m, extra)
    odd_ok = odd_ok and all(comm(I, g.gen(i), sq) for i in range(n))
g.check("prop:families (odd dimension, five and seven): the pseudoscalar commutes "
      "with every generator, so it is central and there is no chirality grading "
      "for a versor to preserve",
      odd_ok)

# def:fock in odd dimension: the left ideal Cl f has dimension 2^(m+1); its
# chirality-projected halves S+- = (1 +- I)/2 Cl f have dimension 2^m, and on
# each the extra generator ell acts as the Fock grade parity up to a fixed sign
def span_dim(vecs):
    """dimension of the span of a list of GA elements, by exact rank on blade coordinates"""
    blades = sorted({b for x in vecs for b in x})
    rows = [[x.get(b, F(0)) for b in blades] for x in vecs]
    return g.rank_of_vectors(rows) if rows else 0
odd_fock_ok = True
for m, extra in ((1, 1), (2, 1), (3, 1)):
    sq, n, w, v, f, top, I = fock_data(m, extra)
    ell = g.gen(n - 1)
    one = g.mul(g.gen(0), g.gen(0), sq)
    # Fock states v_S f for all subsets S
    states = []
    for k in range(m + 1):
        for S in combinations(range(m), k):
            st = f
            for i in reversed(S): st = g.mul(v[i], st, sq)
            states.append((k, st))
    # the full ideal Cl f: spanned by the states and their products with ell
    full = [st for _, st in states] + [g.mul(ell, st, sq) for _, st in states]
    Pp = g.scal(F(1, 2), g.add(one, I))
    proj = [(k, g.mul(Pp, st, sq)) for k, st in states]
    # dimension counts
    dim_full = span_dim(full); dim_proj = span_dim([st for _, st in proj])
    # ell on the projected states: a fixed sign times (-1)^k
    signs = set()
    good = True
    for k, st in proj:
        lp = None
        for lam in (F(1), F(-1)):
            if g.eq(g.mul(ell, st, sq), g.scal(lam, st)): lp = lam
        if lp is None: good = False; break
        signs.add(lp * F((-1) ** k))
    odd_fock_ok = odd_fock_ok and dim_full == 2 ** (m + 1) and dim_proj == 2 ** m and good and len(signs) == 1
g.check("def:fock (odd dimension, m = 1, 2, 3): the left ideal Cl f has dimension "
      "2^(m+1) (both irreducible modules), the chirality-projected half (1 + I)/2 "
      "Cl f has dimension 2^m, and on it the extra generator ell multiplies every "
      "Fock grade-k state by a fixed sign times (-1)^k: ell is the Fock grade "
      "parity on each irreducible module",
      odd_fock_ok)
# prop:orientation: the flag conjugate on the Fock ideal (m = 3) is the versor
# negating the pair partners; it carries the state with index set S to the
# state with the complementary index set, exchanging Fock grades k and 3 - k
sq, n, w, v, f, top, I = fock_data(3, 0)
R = g.mul(g.mul(g.gen(3), g.gen(4), sq), g.gen(5), sq)
def index_set(psi):
    return frozenset(i for i in range(3) if g.is_zero(g.mul(v[i], psi, sq)))
conj_ok = True
for k in range(4):
    for S in combinations(range(3), k):
        st = f
        for i in reversed(S): st = g.mul(v[i], st, sq)
        Rst = g.mul(R, st, sq)
        conj_ok = (conj_ok and index_set(st) == frozenset(S)
                   and index_set(Rst) == frozenset(range(3)) - frozenset(S)
                   and not g.is_zero(Rst)
                   and (g.eq(g.mul(R, Rst, sq), g.scal(F(-1), st)) or g.eq(g.mul(R, Rst, sq), st)))
g.check("prop:orientation: on the three-pair Fock ideal built in GA.py the flag "
      "conjugate (the versor e_4 e_5 e_6 negating the pair partners) carries the "
      "state with creation index set S, characterised as the state killed by "
      "exactly the v_i with i in S, to the state with the complementary index set, "
      "exchanging Fock grades k and 3 - k and the two singlet grades 0 and 3 "
      "wholesale, and it squares to plus or minus the identity on every state: the "
      "nu_R identification is flag-covariant",
      conj_ok)
# fact:sminputs / thm:mirror: the reversion product vanishes identically on the
# null-blade Fock ideal (f a pure blade, f~ x f a multiple of f), while on the
# minimal left ideal generated by a self-reverse primitive idempotent it does not
def reverse(x):
    out = {}
    for b, c in x.items():
        k = len(b); sgn = -1 if (k * (k - 1) // 2) % 2 else 1
        out[b] = c * sgn
    return out
rev_ok = True
for m in (1, 2, 3):
    sq, n, w, v, f, top, I = fock_data(m, 0)
    # every pair of basis states: scalar part of psi~ phi
    states = []
    for k in range(m + 1):
        for S in combinations(range(m), k):
            st = f
            for i in reversed(S): st = g.mul(v[i], st, sq)
            states.append(st)
    rev_ok = rev_ok and all(g.mul(reverse(a), b, sq).get((), F(0)) == 0 for a in states for b in states)
sq24 = g.sig(2, 4)
one24 = g.mul(g.gen(0), g.gen(0), sq24)
def blade(*idx):
    x = g.gen(idx[0])
    for i in idx[1:]: x = g.mul(x, g.gen(i), sq24)
    return x
B1 = blade(0, 1, 2, 3)          # e_0 e_1 e_2 e_3: 4-blade, square +1, self-reverse, even
B2 = blade(0, 1, 4, 5)          # e_0 e_1 e_4 e_5: 4-blade, square +1, self-reverse, even, commutes with B1
f24 = g.scal(F(1, 4), g.mul(g.add(one24, B1), g.add(one24, B2), sq24))   # self-reverse primitive idempotent of Cl^0(2,4)
even24 = [b for b in g.all_blades(6) if len(b) % 2 == 0]
ideal = [g.mul({b: F(1)}, f24, sq24) for b in even24]                   # spans Cl^0 f
def coords(vecs):
    blades = sorted({b for x in vecs for b in x})
    return [[x.get(b, F(0)) for b in blades] for x in vecs], blades
rows, bl = coords(ideal); dim_ideal = g.rank_of_vectors(rows)
# a basis of the ideal: greedy selection of independent elements
basis = []
for x in ideal:
    if g.rank_of_vectors(coords(basis + [x])[0]) > len(basis): basis.append(x)
comm = [g.mul(g.mul(f24, {b: F(1)}, sq24), f24, sq24) for b in even24]   # spans f Cl^0 f
dim_comm = g.rank_of_vectors(coords(comm)[0])
def form(psi, phi): return g.mul(reverse(psi), phi, sq24)                # psi-bar phi in f Cl^0 f
# Gram matrix of the form over the basis, as elements of f Cl^0 f (2-dimensional, complex)
gram = [[form(a, b) for b in basis] for a in basis]
hermitian = all(g.eq(reverse(gram[i][j]), gram[j][i]) for i in range(len(basis)) for j in range(len(basis)))
nonzero = any(not g.is_zero(x) for row in gram for x in row)
# nondegeneracy: the real linear map psi -> (psi-bar phi_j)_j has trivial kernel on the ideal;
# encode each form value by its coordinates in the commutant's blade basis and compute the rank
cblades = sorted({b for row in gram for x in row for b in x})
big = [[x.get(b, F(0)) for x in row for b in cblades] for row in gram]
nondeg = g.rank_of_vectors(big) == len(basis)
# invariance under exact spin elements R with R R~ = 1: a rotation in the (e_0, e_1) plane
# (both square +1) and a boost in the (e_0, e_2) plane (e_2^2 = -1)
R1 = g.add(g.scal(F(3, 5), one24), g.scal(F(4, 5), blade(0, 1)))      # (3/5) + (4/5) e_0 e_1, (e_0 e_1)^2 = -1
R2 = g.add(g.scal(F(5, 3), one24), g.scal(F(4, 3), blade(0, 2)))      # (5/3) + (4/3) e_0 e_2, (e_0 e_2)^2 = +1
unit = all(g.eq(g.mul(R, reverse(R), sq24), one24) for R in (R1, R2))
invariant = all(g.eq(form(g.mul(R, a, sq24), g.mul(R, b, sq24)), form(a, b))
                for R in (R1, R2) for a in basis for b in basis)
rev_ok = rev_ok and g.eq(g.mul(f24, f24, sq24), f24) and g.eq(g.mul(B1, B2, sq24), g.mul(B2, B1, sq24)) \
         and g.eq(reverse(f24), f24) and all(len(b) % 2 == 0 for b in f24) \
         and dim_ideal == 8 and dim_comm == 2 and nonzero and hermitian and nondeg and unit and invariant
g.check("fact:sminputs: on the null-blade Fock ideal of dimensions two, four and six "
      "the scalar part of psi~ phi vanishes for every pair of basis states, while on "
      "the minimal left ideal Cl^0(2,4) f of the self-reverse EVEN primitive "
      "idempotent f = (1 + e_0 e_1 e_2 e_3)(1 + e_0 e_1 e_4 e_5)/4 (real dimension "
      "8, commutant f Cl^0 f of real dimension 2: the twistor module over C) the "
      "form psi-bar phi is nonzero, Hermitian (reverse of the Gram matrix is its "
      "transpose), nondegenerate (the Gram map has full rank 8), and invariant "
      "under two exact unit even versors, a rotation and a boost: the helicity form "
      "lives there, not on the null-blade model",
      rev_ok)

g.check("thm:paritybit (RECORD: an identity of integers, kept as the statement "
      "the theorem's odd half rests on): (p - q) and (p + q) have the same "
      "parity on the grid to dimension ten",
      all(((p - q) % 2) == ((p + q) % 2) for p in range(11) for q in range(11)))
M6 = diag_isometry(6, (1, 1, 1, -1, -1, -1)); sq6 = (1, 1, 1, -1, -1, -1)
g.check("thm:paritybit: in ambient dimension six (this tower, the mirror) the "
      "isometry negating the three pair partners carries W to W' and has "
      "determinant -1: the halves are in opposite families, the choice is a bit",
      preserves(M6, sq6) and carries_W_to_Wprime(M6, 3) and det(M6) == -1)
M7 = diag_isometry(7, (1, 1, 1, -1, -1, -1, -1)); sq7 = (1, 1, 1, -1, -1, -1, 1)
M5 = diag_isometry(5, (1, 1, -1, -1, 1)); sq5 = (1, 1, -1, -1, 1)
g.check("thm:paritybit: in ambient dimensions seven and five a proper isometry "
      "(determinant +1) carries W to W': no bit in the odd residues",
      preserves(M7, sq7) and carries_W_to_Wprime(M7, 3) and det(M7) == 1
      and preserves(M5, sq5) and carries_W_to_Wprime(M5, 2) and det(M5) == 1)
sqL = (1, 1, 1, 1, -1, -1, -1)
ellv = g.gen(3); biv = g.mul(g.gen(0), ellv, sqL); pairg = g.add(g.gen(1), g.gen(5))
g.check("thm:paritybit: on the split form of dimension seven the bivector e1 ell "
      "is even, commutes with a pair generator not involving e1, and "
      "anticommutes with ell (the Fock parity up to scalar): spin(V) mixes the "
      "halves in odd dimension",
      all(len(b) % 2 == 0 for b in biv)
      and g.eq(g.mul(biv, pairg, sqL), g.mul(pairg, biv, sqL))
      and g.is_zero(g.add(g.mul(biv, ellv, sqL), g.mul(ellv, biv, sqL))))
g.check("cor:whocarries: the P3 representatives of the even residues, taken from the "
      "census function rather than typed here, all have dimension 0 mod 4 "
      "(so carry the bit), and among them only residues 6 and 2 are causal",
      sorted(r for r in (0, 2, 4, 6) if any(causal(*s_) for s_ in P3[r])) == [2, 6]
      and all(len(set(p + q for p, q in P3[r])) == 1 and (list(P3[r])[0][0] + list(P3[r])[0][1]) % 4 == 0
              for r in (0, 2, 4, 6)))
# A1 of the v2 review: the bit exists iff the ambient dimension is 2m with m
# odd; in ambient dimensions four and eight (representatives (1,1) and (1,5)) the
# exchanging isometry is proper
M4 = diag_isometry(4, (1, 1, -1, -1)); sq4 = (1, 1, -1, -1)
M8 = diag_isometry(8, (1, 1, 1, 1, -1, -1, -1, -1)); sq8 = (1, 1, 1, 1, -1, -1, -1, -1)
g.check("thm:paritybit: in ambient dimensions four and eight (m = 2, 4: the "
      "representatives (1,1) and (1,5)) the isometry negating the pair partners "
      "carries W to W' with determinant +1: no bit at tower dimension 2 mod 4, "
      "so the bit exists exactly when the tower dimension is 0 mod 4",
      preserves(M4, sq4) and carries_W_to_Wprime(M4, 2) and det(M4) == 1
      and preserves(M8, sq8) and carries_W_to_Wprime(M8, 4) and det(M8) == 1
      and det(M6) == -1)

def det2(mm): return mm[0][0] * mm[1][1] - mm[0][1] * mm[1][0]
ok22 = True
for p_, pt, r_, rt in (((F(1), F(2)), (F(3), F(-1)), (F(2), F(5)), (F(-4), F(1))),
                       ((F(2), F(0)), (F(1), F(1)), (F(0), F(3)), (F(2), F(-2))),
                       ((F(1), F(1)), (F(1), F(-1)), (F(2), F(2)), (F(3), F(-3)))):
    P1 = [[p_[i] * pt[j] for j in range(2)] for i in range(2)]
    P = [[p_[i] * pt[j] + r_[i] * rt[j] for j in range(2)] for i in range(2)]
    br = (p_[0] * r_[1] - p_[1] * r_[0]) * (pt[0] * rt[1] - pt[1] * rt[0])
    ok22 = ok22 and det2(P1) == 0 and det2(P) == br
g.check("cor:whocarries: in (2,2) a single constituent is null and the two-"
      "constituent determinant is <pi1 pi2><pit1 pit2>: mass begins at two on "
      "the fork", ok22)
# prop:charge: the baryon-to-photon ratio and the charge-versus-number window
eta = F(274, 10 ** 10) * OB          # eta = 2.74e-8 Omega_b h^2
eta_lo, eta_hi = icbrt_bracket(eta, denom=10 ** 7)
g.check("prop:charge: eta = 2.74e-8 x 0.02237 lies in (6.1, 6.2) x 10^-10 and its "
      "cube root, the charge-domination crossover, in (8.4, 8.6) x 10^-4 (eta' at "
      "the paper's own floor is bracketed in the cosmology block below)",
      F(61, 10 ** 11) < eta < F(62, 10 ** 11)
      and F(84, 10 ** 5) < eta_lo and eta_hi < F(86, 10 ** 5))

# the mirror's cosmology (prop:charge, Appendix A): the seeding floor from the
# species count with the mirror's own g_d, the yield against the baryon number,
# the hot-deposit ceiling, the weak-rate ratio and its crossing, the bottleneck,
# the entropy evolution of the ratio, the completion-limit reheating on the
# plasma budget, recombination, the mean mass per baryon and the atomic
# cross-section.  Decimal arithmetic for the powers, logarithms and fixed
# points; the burning network itself is not modelled.
getcontext().prec = 40
ETA_D = Dec(eta.numerator) / Dec(eta.denominator)
A_S, A_F, A_V = Dec("1.9e-4"), Dec("1.1e-3"), Dec("2.3e-3")     # Bernal et al. 2018, Table I, per produced species
C_LO = 4 * A_S + Dec("22.5") * A_F + 12 * A_V                     # 45 Weyl as 22.5 Dirac
C_HI = 4 * A_S + 45 * A_F + 12 * A_V                              # 45 Weyl counted singly
GD_MIRROR = 4 + 45 * Dec("1.75") + 24                             # 106.75
GD_GLUE = 18                                                      # nine vectors, two polarisations
MPRED = Dec("2.435e18"); M_CEIL = Dec(6) * Dec(10) ** 14; GSTAR100 = Dec(100)
FRIED_RED = (PI ** 2 * GSTAR100 / 90).sqrt()                      # H = sqrt(pi^2 g*/90) T^2 / M_P, reduced-mass convention
KAPPA_S = FRIED_RED * (2 * PI ** 2 / 45) * GSTAR100
g.check("prop:gravseed (convention): the reduced-mass Friedmann coefficient "
      "sqrt(pi^2 g*/90) equals 1.66 sqrt(g*)/sqrt(8 pi) to three figures (1.66 "
      "sqrt(g*) T^2/M_Pl with M_Pl = sqrt(8 pi) M_P is the same rate), and kappa_s "
      "= sqrt(pi^2 g*/90) (2 pi^2/45) g_s is in (145, 146) at g* = g_s = 100",
      abs(FRIED_RED - Dec("1.66") * GSTAR100.sqrt() / (8 * PI).sqrt()) < Dec("0.0001") * GSTAR100.sqrt()
      and Dec(145) < KAPPA_S < Dec(146))
def yield_grav(c, T): return c * (T / MPRED) ** 3 / (3 * KAPPA_S)
def xi_floor(c, gd, T=M_CEIL): return (4 * yield_grav(c, T) * GSTAR100 / Dec(gd)) ** (Dec(1) / 4)
XI_LO, XI_HI = xi_floor(C_LO, GD_MIRROR), xi_floor(C_HI, GD_MIRROR)
ETAP_HI, ETAP_LO = ETA_D / XI_LO ** 3, ETA_D / XI_HI ** 3
g.check("prop:coefficients(ii): the mirror's species count gives c in (0.053, 0.054) "
      "(Dirac counting) to (0.077, 0.078) (Weyl counting), g_d = 106.75, hence the "
      "floor xi in (2.8, 3.2) x 10^-4 and eta' in (19, 26) at the floor; the "
      "pure-glue value with g_d = 18 is in (3.5, 3.6) x 10^-4; and at the mirror's "
      "g_d the floor at c = 10 is in (1.0, 1.1) x 10^-3 and eta' falls below one "
      "only for c above 4 (xi above eta^(1/3) = 8.5e-4)",
      Dec("0.053") < C_LO < Dec("0.054") and Dec("0.077") < C_HI < Dec("0.078")
      and GD_MIRROR == Dec("106.75")
      and Dec("2.8e-4") < XI_LO < XI_HI < Dec("3.2e-4")
      and Dec(19) < ETAP_LO < ETAP_HI < Dec(26)
      and Dec("3.5e-4") < xi_floor(9 * A_V, GD_GLUE) < Dec("3.6e-4")
      and Dec("1.0e-3") < xi_floor(Dec(10), GD_MIRROR) < Dec("1.1e-3")
      and ETA_D / xi_floor(Dec("4.1"), GD_MIRROR) ** 3 < 1 < ETA_D / xi_floor(Dec(4), GD_MIRROR) ** 3)
NB_PER_S = ETA_D * Dec("0.1413")                                  # baryons per unit entropy
Y_LO, Y_HI = yield_grav(C_LO, M_CEIL), yield_grav(C_HI, M_CEIL)
T_RESCUE = M_CEIL * (NB_PER_S / Y_LO) ** (Dec(1) / 3)
T_RESCUE_LO = M_CEIL * (NB_PER_S / Y_HI) ** (Dec(1) / 3)
g.check("prop:coefficients(iii)/prop:charge: the gravitational yield at the ceiling is "
      "in (1.8, 2.7) x 10^-15 per unit entropy against 8.66e-11 baryons per unit "
      "entropy (eta times n_gamma/s = 0.1413): short by a factor in (3e4, 5e4); "
      "closing it needs T_desc in (1.9, 2.3) x 10^16 GeV at the two countings, above "
      "30 times the ceiling, where the floor itself, scaling as T^(3/4), is in "
      "(4.0, 4.5) x 10^-3, above 8.5e-4 (its equality with the hot-deposit value is "
      "an identity of the two expressions, stated in the proof, not a check)",
      Dec("1.8e-15") < Y_LO < Y_HI < Dec("2.7e-15")
      and Dec("8.6e-11") < NB_PER_S < Dec("8.7e-11")
      and Dec("3e4") < NB_PER_S / Y_HI < NB_PER_S / Y_LO < Dec("5e4")
      and Dec("1.9e16") < T_RESCUE_LO < T_RESCUE < Dec("2.2e16") and T_RESCUE_LO > 30 * M_CEIL
      and Dec("4.0e-3") < xi_floor(C_LO, GD_MIRROR, T_RESCUE) < Dec("4.5e-3"))
XI_HOT = (3 * NB_PER_S / Dec("0.75") * GSTAR100 / GD_MIRROR) ** (Dec(1) / 4)   # deposit energy 3 T_desc per baryon-number unit
ETAP_HOT = ETA_D / XI_HOT ** 3
g.check("prop:charge (hot deposit): if each deposited unit of baryon number carries "
      "energy 3 T_desc the mirror's energy fraction is 3 (n_B/s) T/(3T/4) in (3, 4) x "
      "10^-10, giving xi in (4.0, 4.5) x 10^-3 and eta' in (0.007, 0.009): the "
      "interval from the floor to the hot deposit straddles the crossover 8.5e-4, "
      "and eta'/eta is above 1e7 everywhere in it",
      Dec("3e-10") < 3 * NB_PER_S / Dec("0.75") < Dec("4e-10")
      and Dec("4.0e-3") < XI_HOT < Dec("4.5e-3") and Dec("0.007") < ETAP_HOT < Dec("0.009")
      and XI_LO < Dec("8.5e-4") < XI_HOT and Dec("1e7") < ETAP_HOT / ETA_D
      and Dec("3e10") < ETAP_HI / ETA_D < Dec("5e10"))
GF = Dec("1.166e-5"); MPL_ = Dec("1.22e19"); GSTAR = Dec(60)
def weak_over_H(Tp, xi):    # G_F^2 T'^5 against 1.66 sqrt(g*) (T'/xi)^2 / M_Pl, T' in GeV
    return GF ** 2 * Tp ** 5 / (Dec("1.66") * GSTAR.sqrt() * (Tp / xi) ** 2 / MPL_)
def crossing(xi):           # T' at which the ratio is one: ratio scales as T'^3
    return (1 / weak_over_H(Dec(1), xi)) ** (Dec(1) / 3)
g.check("prop:charge (weak equilibrium): Gamma/H scales as T'^3 at fixed xi; at the "
      "floor it is below 2e-5 at T' = 10 MeV, in (0.03, 0.05) at the QCD crossover "
      "155 MeV, and crosses one at T' in (0.42, 0.46) GeV (g* and xi both held at "
      "their seeded values, 60 being the value at the bottleneck epoch; taking g* = "
      "106.75 at the visible TeV scale and the evolved ratio together moves the "
      "crossing by under ten percent, the two corrections partly offsetting, checked "
      "below); at the hot deposit the crossing is below 0.1 GeV, where n/p = "
      "e^(-1.293 MeV/T') is still above 0.98",
      weak_over_H(Dec("0.01"), XI_HI) < Dec("2e-5")
      and Dec("0.03") < weak_over_H(Dec("0.155"), XI_LO) < weak_over_H(Dec("0.155"), XI_HI) < Dec("0.05")
      and Dec("0.42") < crossing(XI_HI) < crossing(XI_LO) < Dec("0.46")
      and crossing(XI_HOT) < Dec("0.1")
      and (-Dec("1.293e-3") / crossing(XI_HOT)).exp() > Dec("0.98")
      and all(abs(weak_over_H(Dec(2) * T, XI_LO) / weak_over_H(T, XI_LO) - 8) < Dec("1e-30") for T in (Dec("0.01"), Dec("0.1"))))
def crossing_full(xi):     # g* = 106.75 at the visible TeV scale and the ratio evolved by the crossover factor
    gstar_hi = Dec("106.75"); xi_eff = xi * (gstar_hi / Dec(100)) ** (Dec(1) / 3)   # mirror g unchanged at that epoch
    ratio1 = GF ** 2 / (Dec("1.66") * gstar_hi.sqrt() * (1 / xi_eff) ** 2 / MPL_)
    return (1 / ratio1) ** (Dec(1) / 3)
g.check("prop:charge (weak equilibrium, both corrections): with g* = 106.75 and the "
      "ratio evolved by (g_vis(T)/g_vis(seed))^(1/3) at the crossing epoch, the "
      "crossing moves by under ten percent from the seeded-value figure and stays "
      "above the crossover",
      all(abs(crossing_full(x) / crossing(x) - 1) < Dec("0.10") for x in (XI_LO, XI_HI))
      and crossing_full(XI_LO) > Dec("0.155"))
B_D, M_P = Dec("2.22e-3"), Dec("0.9383")            # GeV
def T_bottleneck(etap):
    T = Dec("1e-4")
    for _ in range(200):
        T = B_D / ((1 / etap).ln() + Dec("1.5") * (M_P / T).ln())
    return T
TD_LO, TD_HI = T_bottleneck(ETAP_LO), T_bottleneck(ETAP_HI)
g.check("prop:charge (bottleneck): B_D/T' = ln(1/eta') + 1.5 ln(m_p/T') iterated to a "
      "fixed point gives the deuterium bottleneck at T' in (0.23, 0.25) MeV for "
      "eta' at the floor, against (0.061, 0.063) MeV at our eta",
      Dec("0.23e-3") < TD_LO < TD_HI < Dec("0.25e-3")
      and Dec("0.061e-3") < T_bottleneck(ETA_D) < Dec("0.063e-3"))
EVOL = (GD_MIRROR / Dec("3.75")) ** (Dec(1) / 3) * (Dec("61.75") / GSTAR100) ** (Dec(1) / 3)
g.check("prop:charge (entropy evolution): between seeding (g_mir = 106.75, g_vis = 100) "
      "and the bottleneck (g_mir = 3.75, g_vis = 61.75) the ratio T'/T rises by "
      "(106.75/3.75)^(1/3) (61.75/100)^(1/3) in (2.5, 2.7), and eta' normalised to "
      "today's entropy is unchanged (it depends on n_B/s and the seeded xi only)",
      Dec("2.5") < EVOL < Dec("2.7"))
release = Dec("7.07e-3")                              # GeV per nucleon to helium-4
PLASMA = Dec("2.75")                                  # photons (2) plus pairs (3.5) over photons
def burn(etap):
    T = T_bottleneck(etap)
    E = Dec("2.701") * T / etap
    f = (1 + release / (PLASMA * E)) ** (Dec(1) / 4)
    return T, E, f, etap / f ** 3, T * f
T1, E1, f1, e1, Tp1 = burn(ETAP_LO)
T2, E2, f2, e2, Tp2 = burn(ETAP_HI)
g.check("prop:charge (completion limit at the floor): the photon energy per baryon "
      "2.701 T'/eta' lies in (25, 33) keV, the plasma budget is 2.75 times it (thermal "
      "pairs at zero chemical potential, a lower bound on the budget), the "
      "reheating factor (1 + 7.07 MeV/E_plasma)^(1/4) in (2.98, 3.19), the "
      "post-burning eta' in (0.72, 0.81), below one, and T' in (0.69, 0.78) MeV, "
      "where photodisintegration is active; at the hot deposit the photon energy per "
      "baryon exceeds 10 MeV and the reheating factor is below 1.1",
      Dec("25e-6") < min(E1, E2) and max(E1, E2) < Dec("33e-6")
      and Dec("2.98") < min(f1, f2) and max(f1, f2) < Dec("3.19")
      and Dec("0.72") < min(e1, e2) and max(e1, e2) < Dec("0.81")
      and Dec("0.69e-3") < min(Tp1, Tp2) and max(Tp1, Tp2) < Dec("0.78e-3")
      and Dec("2.701") * T_bottleneck(ETAP_HOT) / ETAP_HOT > Dec("10e-3")
      and burn(ETAP_HOT)[2] < Dec("1.1"))
GEV3_TO_CM3 = Dec("5.07e13") ** 3
def n_b_at(etap, T): return etap * Dec("0.2436") * T ** 3 * GEV3_TO_CM3
def t_H_at(T, xi): return Dec("2.42") / GSTAR.sqrt() * (Dec("1e-3") / (T / xi)) ** 2    # seconds at the visible T'/xi
g.check("prop:charge (bottleneck epoch at the floor): the mirror baryon density there "
      "is in (0.7, 1.3) x 10^31 cm^-3, the cosmic time in (1e-6, 1e-5) s with the "
      "evolved ratio (neutrons cannot decay first: eight orders below their "
      "lifetime), and n_b t exceeds the standard case's 1e19 cm^-3 x 300 s by a "
      "factor above 1000",
      Dec("0.7e31") < n_b_at(ETAP_LO, TD_LO) < n_b_at(ETAP_HI, TD_HI) < Dec("1.3e31")
      and Dec("1e-6") < t_H_at(TD_LO, XI_LO * EVOL) < Dec("1e-5")
      and n_b_at(ETAP_LO, TD_LO) * t_H_at(TD_LO, XI_LO * EVOL) / (Dec("1e19") * 300) > 1000
      and t_H_at(TD_LO, XI_LO * EVOL) < Dec(880) / Dec("1e8"))
m_p, m_He4 = Dec("938.272"), Dec("3727.379")
ours = Dec("0.75") * m_p + Dec("0.25") * m_He4 / 4
g.check("prop:massbound(i) / thm:share(ii): mean mass per baryon, ours (75 percent H, 25 percent "
      "He-4 by baryon number) in (936.5, 937.0) MeV against a helium mirror's "
      "931.8, ratio in (0.994, 0.996): f_2 = 0.995 (a deficit in (0.514, 0.516) "
      "percent) in the completion limit",
      Dec("936.5") < ours < Dec("937.0") and Dec("0.994") < (m_He4 / 4) / ours < Dec("0.996")
      and Dec("0.00514") < 1 - (m_He4 / 4) / ours < Dec("0.00516"))
def T_recomb(etap):         # Saha at half ionisation, hydrogen-like: 2 = eta' 3.84 (T/m_e)^(3/2) e^(13.6 eV/T)
    T = Dec("0.3")
    for _ in range(200):
        T = Dec("13.6") / ((2 / (etap * Dec("3.84"))).ln() - Dec("1.5") * (T / Dec("0.511e6")).ln())
    return T                # eV
a0 = Dec("0.529e-8"); sig_atom = PI * (2 * a0) ** 2
g.check("prop:audit (mirror self-interaction): the Saha condition puts our recombination "
      "in (0.30, 0.35) eV and the mirror's in (0.54, 0.86) eV between the hot end "
      "(eta' = 0.008) and the floor before burning, and at (0.65, 0.72) eV at the "
      "floor after it (eta' = 0.72-0.81) (hydrogen-like; helium's binding raises "
      "it), a visible temperature in (0.1, 0.8) keV across the interval at the "
      "epoch's own ratio (the hot end unreheated, the floor reheated by 3.0-3.2 "
      "and the copy's ratio otherwise restored by recombination); the atomic elastic "
      "cross-section pi (2 a_0)^2 in (3, 4) x 10^-16 cm^2 gives sigma/m in (5e7, "
      "1e8) cm^2/g for helium and (2e8, 3e8) for hydrogen",
      Dec("0.30") < T_recomb(ETA_D) < Dec("0.35")
      and Dec("0.54") < T_recomb(ETAP_HOT) < T_recomb(ETAP_HI) < Dec("0.86")
      and Dec("0.65") < min(T_recomb(e1), T_recomb(e2)) and max(T_recomb(e1), T_recomb(e2)) < Dec("0.72")
      and Dec("0.1e3") < T_recomb(ETAP_HOT) / XI_HOT and max(T_recomb(e1), T_recomb(e2)) / (XI_LO * min(f1, f2)) < Dec("0.8e3")
      and Dec("3e-16") < sig_atom < Dec("4e-16")
      and Dec("5e7") < sig_atom / Dec("6.64e-24") < Dec("1e8")
      and Dec("2e8") < sig_atom / Dec("1.67e-24") < Dec("3e8"))
def t_cool_gyr(T, Lam, n): return Dec("1.5") * Dec("1.38e-16") * T / (n * Lam) / Dec("3.15e16")
RHO_CRIT = Dec("9.5e-30")
mfp_pc = 1 / (Dec("1e8") * 200 * RHO_CRIT * Dec("0.186")) / Dec("3.086e18")
g.check("refutation item 6: primordial cooling at 1e6 K (Lambda = 1e-23 erg cm^3/s) gives "
      "t_cool in (5, 15) Gyr at n = 1e-4 cm^-3 and in (0.5, 1.5) Gyr at 1e-3, "
      "and at the Lyman-alpha peak (1e-22 at 1e5 K, 1e-3) below 0.01 Gyr: within a "
      "Hubble time inside the cooling radius, not at the virial radius; the mean "
      "free path at sigma/m = 1e8 and 200 rho_crit times the mirror fraction is "
      "in (5, 15) pc (the thin-disk factor of ten is literal arithmetic, not billed)",
      Dec(5) < t_cool_gyr(Dec("1e6"), Dec("1e-23"), Dec("1e-4")) < Dec(15)
      and Dec("0.5") < t_cool_gyr(Dec("1e6"), Dec("1e-23"), Dec("1e-3")) < Dec("1.5")
      and t_cool_gyr(Dec("1e5"), Dec("1e-22"), Dec("1e-3")) < Dec("0.01")
      and Dec(5) < mfp_pc < Dec(15))
g.check("prop:count(i): the survey ratio's uncertainty, 5.364 times the quadrature "
      "relative uncertainty, lies in (0.064, 0.066): quoted as 0.065",
      F(64, 1000) ** 2 < OBS ** 2 * ((DOC / OC) ** 2 + (DOB / OB) ** 2) < F(66, 1000) ** 2)

# ---------------------------------------------------------------------------
# Part K: Appendix A, seeding by gravity (prop:gravseed, prop:coefficients).
# Forty-digit decimal arithmetic; the graviton rate is the imported input.
# ---------------------------------------------------------------------------

g.check("prop:gravseed: the floor prefactor is xi = 9.6e-4 c^(1/4) (16/g_d)^(1/4) at "
      "the ceiling reheating: with g_d = 16, xi in (9.6, 9.7) x 10^-4 at c = 1, "
      "(1.7, 1.75) x 10^-3 at c = 10, (3.0, 3.1) x 10^-4 at c = 0.01; xi scales as "
      "T_desc^(3/4) (halving T_desc gives a factor in (0.59, 0.60), and the bottom "
      "of the ceiling range, 3.5e11 GeV, a factor in (3.5, 4.5) x 10^-3); and the "
      "non-reduced Planck mass would lower it by (2.435/12.2)^(3/4) in (0.29, 0.31)",
      Dec("9.6e-4") < xi_floor(Dec(1), 16) < Dec("9.7e-4")
      and Dec("1.7e-3") < xi_floor(Dec(10), 16) < Dec("1.75e-3")
      and Dec("3.0e-4") < xi_floor(Dec("0.01"), 16) < Dec("3.1e-4")
      and Dec("0.59") < xi_floor(Dec(1), 16, M_CEIL / 2) / xi_floor(Dec(1), 16) < Dec("0.60")
      and Dec("3.5e-3") < xi_floor(Dec(1), 16, Dec("3.5e11")) / xi_floor(Dec(1), 16) < Dec("4.5e-3")
      and Dec("0.29") < (Dec("2.435") / Dec("12.2")) ** (Dec(3) / 4) < Dec("0.31"))
def riemann(c, T, N, upper):
    """sum of c T^2/(kappa_s M_P^3) dT over [0, T] with N steps, right (upper) or left (lower) endpoints"""
    h = T / N
    tot = Dec(0)
    for k in range(N):
        Tk = (k + 1) * h if upper else k * h
        tot += c * Tk ** 2 / (KAPPA_S * MPRED ** 3) * h
    return tot
g.check("prop:gravseed: the Boltzmann integral at the paper's coefficients: the yield "
      "c T_desc^3/(3 kappa_s M_P^3) lies between the lower and upper Riemann sums "
      "of the integrand c T^2/(kappa_s M_P^3) over [0, T_desc] with 200 steps, for "
      "c = 0.053 and 0.078, and the sums bracket it to within two percent",
      all(riemann(c, M_CEIL, 200, False) < yield_grav(c, M_CEIL) < riemann(c, M_CEIL, 200, True)
          and riemann(c, M_CEIL, 200, True) / riemann(c, M_CEIL, 200, False) < Dec("1.02")
          for c in (C_LO, C_HI)))
g.check("prop:coefficients(i)/(iv): the nine-vector content gives c = 0.0207 and, with "
      "g_d = 18, xi in (3.5, 3.6) x 10^-4; the mirror's N_eff share 7.447 xi^4 is "
      "below 1e-13 at the floor and below 1e-8 at the hot deposit, and a nine-vector "
      "tower's (dN_eff per polarisation, derived in Part E and bracketed here in "
      "(2.201, 2.203), so that the printed 2.202 cannot be a typed substitute) x 18 xi^4 "
      "is in (5e-13, 1e-12) at its floor",
      9 * A_V == Dec("0.0207") and Dec("3.5e-4") < xi_floor(9 * A_V, GD_GLUE) < Dec("3.6e-4")
      and Dec("7.447") * XI_HI ** 4 < Dec("1e-13") and Dec("7.447") * XI_HOT ** 4 < Dec("1e-8")
      and F(2201, 1000) < per_dof_lo and per_dof_hi < F(2203, 1000)
      and Dec("5e-13") < Dec(per_dof_lo.numerator) / Dec(per_dof_lo.denominator) * 18 * xi_floor(9 * A_V, GD_GLUE) ** 4
      and Dec(per_dof_hi.numerator) / Dec(per_dof_hi.denominator) * 18 * xi_floor(9 * A_V, GD_GLUE) ** 4 < Dec("1e-12"))
g.check("refutation item 6: the mirror share 1/5.364 lies in (18.6, 18.7) percent (the "
      "fifth-below and quarter-above of the 0.8 Omega_b bound are literal arithmetic "
      "and are not billed here)",
      F(186, 1000) < 1 / OBS < F(187, 1000))

g.check("internal witnesses (formerly bare asserts): every cube-root bracket "
      "satisfies lo^3 <= x < hi^3 (%d brackets); every primitive idempotent "
      "exhibited by analyse() is idempotent and every component dimension is a "
      "perfect square; the null vectors of isotropic_capacity() are isotropic "
      "and orthogonal (%d witnesses)" % (len(BRACKET_OK), len(INTERNAL_OK)),
      BRACKET_OK and INTERNAL_OK and all(BRACKET_OK) and all(INTERNAL_OK))


# ---------------------------------------------------------------------------
# Part L: the infall computation (prem:ledgercharge, prop:infall, fact:discharge):
# the arithmetic behind "information is cheap, charge is expensive", as exact
# rational brackets; the Schwinger discharge ratio, its proportionality to M and
# the crossover mass at which it reaches extremality, exactly; the discharge
# scales printed as RECORD lines from the same rationals (no floating point).
# ---------------------------------------------------------------------------

_MPl = F(1220890, 10 ** 6) * 10 ** 19          # 1.220890e19 GeV (non-reduced Planck mass)
_mp = F(938272, 10 ** 6)                        # 0.938272 GeV
_Msun = F(1116, 1000) * 10 ** 57                # 1.116e57 GeV
_pi_lo, _pi_hi = F(314159, 10 ** 5), F(314160, 10 ** 5)
_GeV_per_g = F(56096, 10 ** 4) * 10 ** 23        # 1 g = 5.6096e23 GeV
_K_per_GeV = F(116045, 10 ** 5) * 10 ** 13       # 1 GeV = 1.16045e13 K
# the mass at which T_H = M_Pl^2/(8 pi M) equals m_p
_Mstar_lo = _MPl ** 2 / (8 * _pi_hi * _mp)
_Mstar_hi = _MPl ** 2 / (8 * _pi_lo * _mp)
g.check("prem:ledgercharge: the mass at which T_H = m_p, M_Pl^2/(8 pi m_p), lies in (6.2, 6.4) x 10^36 GeV "
        "and in (1.1, 1.2) x 10^13 g, bracketed with pi in (3.14159, 3.14160)",
        F(62, 10) * 10 ** 36 < _Mstar_lo and _Mstar_hi < F(64, 10) * 10 ** 36
        and F(11, 10) * 10 ** 13 < _Mstar_lo / _GeV_per_g and _Mstar_hi / _GeV_per_g < F(12, 10) * 10 ** 13)
# the most baryons a hole can ever emit is M*/m_p; a solar-mass progenitor swallowed M_sun/m_p
_Nmax_hi = _Mstar_hi / _mp
_Nswallowed = _Msun / _mp
g.check("prem:ledgercharge / prop:infall(iv): the maximal burst baryon number M*/m_p is below 7 x 10^36 while a "
        "solar-mass progenitor carried above 10^57 baryons: the return fraction is below 6 x 10^-21 < 10^-20 "
        "even for a pure-baryon final burst",
        _Nmax_hi < 7 * 10 ** 36 and _Nswallowed > 10 ** 57 and _Nmax_hi / _Nswallowed < 6 * F(1, 10 ** 21)
        and _Nmax_hi / _Nswallowed < F(1, 10 ** 20))
# information is cheap: S_BH = 4 pi (M/M_Pl)^2 at one solar mass against a few nats per baryon
_SBH_lo = 4 * _pi_lo * (_Msun / _MPl) ** 2
_SBH_hi = 4 * _pi_hi * (_Msun / _MPl) ** 2
_Sstar_hi = 10 * _Nswallowed                    # ten nats per baryon, a generous ceiling
g.check("prop:infall(ii): S_BH(solar) = 4 pi (M/M_Pl)^2 lies in (1.0, 1.1) x 10^77, and even at ten nats per "
        "baryon the progenitor's entropy is below 1.2 x 10^58: the ratio S_star/S_BH is below 1.2 x 10^-19, "
        "nineteen orders (information is cheap)",
        10 ** 77 < _SBH_lo and _SBH_hi < F(11, 10) * 10 ** 77 and _Sstar_hi < F(12, 10) * 10 ** 58
        and _Sstar_hi / _SBH_lo < F(12, 10) * F(1, 10 ** 19))
# charge is expensive: T_H at one solar mass, in kelvin, against the proton mass
_TH_lo = _MPl ** 2 / (8 * _pi_hi * _Msun)
_TH_hi = _MPl ** 2 / (8 * _pi_lo * _Msun)
g.check("prop:infall(iv): T_H(solar) = M_Pl^2/(8 pi M_sun) lies in (6.0, 6.5) x 10^-8 K, and m_p/T_H exceeds "
        "10^20: a GeV carrier against a nanokelvin temperature (charge is expensive)",
        6 * F(1, 10 ** 8) < _TH_lo * _K_per_GeV and _TH_hi * _K_per_GeV < F(65, 10) * F(1, 10 ** 8)
        and _mp / _TH_hi > 10 ** 20)
# the Schwinger discharge of fact:discharge, exactly: SI constants of the record as
# rationals, pi bracketed; Q_c = 4 pi eps0 E_c r_+^2 with r_+ = 2 G M/c^2, Q_ext =
# sqrt(4 pi eps0 G) M, so (Q_c/Q_ext)^2 = 16 (4 pi eps0) G^3 E_c^2 M^2 / c^8, a
# rational whose square root is never taken: every bracket is on the square.
_m_e = F(91093837, 10 ** 8) * F(1, 10 ** 30)     # 9.1093837e-31 kg
_e_ = F(1602176634, 10 ** 9) * F(1, 10 ** 19)    # 1.602176634e-19 C
_hbar = F(1054571817, 10 ** 9) * F(1, 10 ** 34)  # 1.054571817e-34 J s
_c_ = F(299792458)                               # m/s
_eps0 = F(88541878128, 10 ** 10) * F(1, 10 ** 12)  # 8.8541878128e-12 F/m
_G_ = F(667430, 10 ** 5) * F(1, 10 ** 11)        # 6.67430e-11 SI
_Msun_kg = F(198847, 10 ** 5) * 10 ** 30         # 1.98847e30 kg
_E_c = _m_e ** 2 * _c_ ** 3 / (_e_ * _hbar)      # Schwinger field, V/m, exact
def _Qc(M_solar, pi_):
    """the Schwinger bound 4 pi eps0 E_c r_+^2 at M solar masses, r_+ = 2 G M/c^2, coulombs"""
    r_plus = 2 * _G_ * (M_solar * _Msun_kg) / _c_ ** 2
    return 4 * pi_ * _eps0 * _E_c * r_plus ** 2
def _Qext2(M_solar, pi_):
    """the square of the extremal charge, (4 pi eps0 G) M^2"""
    return 4 * pi_ * _eps0 * _G_ * (M_solar * _Msun_kg) ** 2
def _ratio2(M_solar, pi_):
    """(Q_c/Q_ext)^2 at M solar masses, exact rational, built from the two charges"""
    return _Qc(M_solar, pi_) ** 2 / _Qext2(M_solar, pi_)
_Qc_lo, _Qc_hi = _Qc(1, _pi_lo), _Qc(1, _pi_hi)
g.check("fact:discharge: at one solar mass the Schwinger bound Q_c = 4 pi eps0 E_c r_+^2 lies in (1.28, 1.29) x 10^15 C "
        "and Q_c/Q_extremal in (7.4, 7.6) x 10^-6, brackets on the square with pi in (3.14159, 3.14160); and "
        "(Q_c/Q_extremal)^2 at 10 and at 10^-8 solar masses equals 10^2 and 10^-16 times its solar value exactly, "
        "so the ratio is proportional to M",
        F(128, 100) * 10 ** 15 < _Qc_lo and _Qc_hi < F(129, 100) * 10 ** 15
        and (F(74, 10 ** 7)) ** 2 < _ratio2(1, _pi_lo) and _ratio2(1, _pi_hi) < (F(76, 10 ** 7)) ** 2
        and _ratio2(10, _pi_lo) / _ratio2(1, _pi_lo) == 100
        and _ratio2(F(1, 10 ** 8), _pi_lo) / _ratio2(1, _pi_lo) == F(1, 10 ** 16))
# the crossover: Q_c = Q_ext at M_x^2 = c^8 / (16 (4 pi eps0) G^3 E_c^2), in solar masses
# obtained from the computed ratio at one solar mass by the proportionality just checked
_Mx2_lo = 1 / _ratio2(1, _pi_hi)
_Mx2_hi = 1 / _ratio2(1, _pi_lo)
g.check("fact:discharge / prop:infall(iii): the mass at which Q_c = Q_extremal lies in (1.3, 1.4) x 10^5 solar masses "
        "(bracket on its square); below it the Schwinger bound is sub-extremal, and at 4 x 10^6 solar masses "
        "(Q_c/Q_extremal)^2 exceeds 29^2, so discharge does not limit the charge of a supermassive hole",
        (F(13, 10) * 10 ** 5) ** 2 < _Mx2_lo and _Mx2_hi < (F(14, 10) * 10 ** 5) ** 2
        and _ratio2(4 * 10 ** 6, _pi_lo) > 29 ** 2)

# RECORD lines: the discharge scales, printed from the exact rationals above in
# forty-digit decimal (no machine floating point); the field E_c is not checked.
def _dec(x):
    return Dec(x.numerator) / Dec(x.denominator)
print("RECORD  fact:discharge: Schwinger critical field E_c = m_e^2 c^3/(e hbar) = %.4E V/m (from the record's constants)" % _dec(_E_c))
print("RECORD  fact:discharge: M = 1 M_sun: Q_c in (%.4E, %.4E) C, (Q_c/Q_extremal)^2 in (%.4E, %.4E)"
      % (_dec(_Qc_lo), _dec(_Qc_hi), _dec(_ratio2(1, _pi_lo)), _dec(_ratio2(1, _pi_hi))))
print("RECORD  fact:discharge: crossover Q_c = Q_extremal at M^2 in (%.4E, %.4E) M_sun^2, i.e. M = 1.33 x 10^5 M_sun"
      % (_dec(_Mx2_lo), _dec(_Mx2_hi)))


# ---------------------------------------------------------------------------
# Part M: the unit-ball rule (Section 7: prop:nesting, prop:rule, rem:forms,
# prop:Tc, prop:pole, rem:twoc, prop:democracy, prop:reduction, rem:massR1,
# prop:sourcing, cor:cavendish, rem:isotropy, obs:status).  Measures are exact
# monomials c * pi^k (c rational); numerical comparisons use rational bounds on
# pi and on square roots; the slice algebra uses GA.py; the mass-normalisation
# block uses Gaussian rationals.  No floating point.  Sub-parts M.A to M.J
# follow the section's order: measures, nesting, the rule against the record,
# the equivalent forms, the free length, the de Sitter reductions, the clock
# reflection, the mass bound, the look-elsewhere count, the consistency numbers;
# M.K, the contact mechanism (lem:fifth, prop:thickness, tab:excludes, rem:scope).
# ---------------------------------------------------------------------------
from itertools import product
from GA import mul, add, gen, sc, eq, sig
# ---------------------------------------------------------------- monomials in pi
def m(c, k=0):
    return (F(c), k)

def mmul(a, b):
    return (a[0] * b[0], a[1] + b[1])

def mdiv(a, b):
    return (a[0] / b[0], a[1] - b[1])

# unit balls by the two-step recursion V_n = (2 pi / n) V_{n-2}, V_0 = 1, V_1 = 2
V = {0: m(1), 1: m(2)}
for n in range(2, 9):
    V[n] = mmul(m(F(2, n), 1), V[n - 2])
# unit sphere areas: |S^(n-1)| = n V_n
S = {n - 1: mmul(m(n), V[n]) for n in range(1, 9)}
# Wallis integrals W_n = int_{-pi/2}^{pi/2} cos^n: W_0 = pi, W_1 = 2, W_n = (n-1)/n W_{n-2}
W = {0: m(1, 1), 1: m(2)}
for n in range(2, 9):
    W[n] = mmul(m(F(n - 1, n)), W[n - 2])

PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)

def bounds(terms):
    """terms: list of monomials to be summed; returns (lo, hi) with pi bounds."""
    lo = hi = F(0)
    for c, k in terms:
        a, b = c * PI_LO ** k, c * PI_HI ** k
        lo += min(a, b)
        hi += max(a, b)
    return lo, hi

def between(terms, lo_q, hi_q):
    lo, hi = bounds(terms)
    return lo_q < lo and hi < hi_q

OBS = F(1200, 10000) / F(2237, 100000)     # Planck 2018 with lensing
SIG = F(65, 1000)

def sigmas_away(terms):
    """(lo, hi) of |T - OBS| / SIG"""
    lo, hi = bounds(terms)
    d1, d2 = abs(lo - OBS), abs(hi - OBS)
    return min(d1, d2) / SIG, max(d1, d2) / SIG

# the family T(c) = 1 + 8/(3c) + 16 c/(3 pi), c rational, as monomials
def T(c):
    c = F(c)
    return [m(1), m(F(8, 3) / c), m(F(16, 3) * c, -1)]

# ........ Part M.A
print("Part M.A: the measures")
g.check("Section 7, A1  V_2 = pi, V_3 = 4pi/3, V_4 = pi^2/2, V_5 = 8pi^2/15",
      V[2] == m(1, 1) and V[3] == m(F(4, 3), 1) and V[4] == m(F(1, 2), 2)
      and V[5] == m(F(8, 15), 2))
g.check("Section 7, A2  |S^2| = 4pi, |S^3| = 2pi^2, |S^4| = 8pi^2/3, |S^5| = pi^3",
      S[2] == m(4, 1) and S[3] == m(2, 2) and S[4] == m(F(8, 3), 2) and S[5] == m(1, 3))
g.check("Section 7, A3  hat-box identity |S^(n+1)| = 2 pi V_n for n = 0..6",
      all(S[n + 1] == mmul(m(2, 1), V[n]) for n in range(0, 7)))

# the closed form |S^n| = 2 pi^((n+1)/2) / Gamma((n+1)/2), with Gamma(2) = 1, Gamma(5/2) = 3 sqrt(pi)/4, Gamma(3) = 2
g.check("Section 7, A4  closed form: |S^3| = 2 pi^2 / Gamma(2), |S^4| = 2 pi^(5/2) / (3 sqrt(pi)/4) = 8 pi^2/3, |S^5| = 2 pi^3 / Gamma(3)",
      S[3] == m(2, 2) and S[4] == m(F(2) / F(3, 4), 2) and S[5] == m(F(2, 2), 3))
g.check("Section 7, A5  the unit sphere's area peaks at n = 6: |S^5| < |S^6| and |S^6| > |S^7|",
      bounds([S[5]])[1] < bounds([S[6]])[0] and bounds([S[7]])[1] < bounds([S[6]])[0])
g.check("Section 7, A6  the unit ball's volume peaks at D = 5: V_4 < V_5 and V_5 > V_6, with V_2 = 3.14, V_3 = 4.19, V_4 = 4.93",
      bounds([V[4]])[1] < bounds([V[5]])[0] and bounds([V[6]])[1] < bounds([V[5]])[0]
      and between([V[2]], F(314, 100), F(315, 100)) and between([V[3]], F(418, 100), F(419, 100)) and between([V[4]], F(493, 100), F(494, 100)))
g.check("Section 7, A7  latitudes: |S^(n+1)| = |S^n| * int cos^n for n = 1..6 (Wallis, exact recursion)",
      all(S[n + 1] == mmul(S[n], W[n]) for n in range(1, 7)))
g.check("Section 7, A8  int cos^3 = 4/3 = |S^4|/|S^3| and int cos^4 = 3pi/8 = V_4/V_3, int cos^2 = pi/2",
      W[3] == m(F(4, 3)) == mdiv(S[4], S[3]) and W[4] == m(F(3, 8), 1) == mdiv(V[4], V[3])
      and W[2] == m(F(1, 2), 1))

# ........ Part M.B
print("Part M.B: the nesting, algebraically")
sq14, sq13 = sig(1, 4), sig(1, 3)

def relations_ok(gens, squares, target):
    ok = all(eq(mul(g, g, squares), sc(t)) for g, t in zip(gens, target))
    for i in range(len(gens)):
        for j in range(i + 1, len(gens)):
            ok = ok and add(mul(gens[i], gens[j], squares),
                            mul(gens[j], gens[i], squares)) == {}
    return ok

g.check("Section 7, B1  in Cl(1,4), e_0..e_3 satisfy the relations of Cl(1,3): this world is the slice x_5 = 0",
      relations_ok([gen(i) for i in range(4)], sq14, [1, -1, -1, -1]))
g.check("Section 7, B2  in Cl(1,3), e_0..e_2 satisfy the relations of Cl(1,2): the r = 7 tower's algebra is the slice x_4 = 0",
      relations_ok([gen(i) for i in range(3)], sq13, [1, -1, -1]))
sq41, sq31 = sig(4, 1), sig(3, 1)
g.check("Section 7, B4  mirror chain: in Cl(4,1) the slice e_0, e_1, e_2, e_4 is a Cl(3,1) (the mirror's algebra)",
      relations_ok([gen(0), gen(1), gen(2), gen(4)], sq41, [1, 1, 1, -1]))
g.check("Section 7, B5  mirror chain: in Cl(3,1) the slice e_0, e_1, e_3 is a Cl(2,1) (the r = 1 tower's algebra)",
      relations_ok([gen(0), gen(1), gen(3)], sq31, [1, 1, -1]))

# ........ Part M.C
print("Part M.C: the unit-ball rule and the observed ratio")
f3 = mdiv(V[3], V[2])          # 3D tower: V_3/V_2 (our ball over their disc)
f5 = mdiv(V[3], V[4])          # 5D tower: V_3/V_4 (our ball over their four-ball)
g.check("Section 7, C1  f_3D = V_3/V_2 = 4/3", f3 == m(F(4, 3)))
g.check("Section 7, C2  f_5D = V_3/V_4 = 8/(3 pi)", f5 == m(F(8, 3), -1))
rule = [m(1), mmul(m(2), f3), mmul(m(2), f5)]
g.check("Section 7, C3  V_3 (1/V_3 + 2/V_2 + 2/V_4) = 11/3 + 16/(3 pi), in (5.36431, 5.36433)",
      between(rule, F(536431, 100000), F(536433, 100000)))
g.check("Section 7, C4  the closed form equals T(1) of the family", rule == T(1))
g.check("Section 7, C6  the relation lies within one sigma (0.065) of the observed ratio",
      sigmas_away(rule)[1] < 1)
other = {"no lensing 0.1202/0.02236": F(1202, 10000) / F(2236, 100000),
         "with BAO 0.11933/0.02242": F(11933, 100000) / F(2242, 100000),
         "ACT DR6 + Planck + lensing + DESI 0.118/0.0226": F(118, 1000) / F(226, 10000)}
g.check("Section 7, C7  dataset dependence: the other columns give 5.376, 5.322 and about 5.22",
      F(5375, 1000) < other["no lensing 0.1202/0.02236"] < F(5377, 1000)
      and F(5321, 1000) < other["with BAO 0.11933/0.02242"] < F(5323, 1000)
      and F(521, 100) < other["ACT DR6 + Planck + lensing + DESI 0.118/0.0226"] < F(523, 100))

# ........ Part M.D
print("Part M.D: the sphere form, the volume/surface form, and the exchanged assignment")
g3, g5 = mdiv(S[4], S[3]), mdiv(S[4], S[5])       # one quantum per unit spacetime sphere
g.check("Section 7, D1  one quantum per unit spacetime sphere gives the same shares: |S^4|/|S^3| = V_3/V_2, |S^4|/|S^5| = V_3/V_4",
      g3 == f3 and g5 == f5)
g.check("Section 7, D2  because |S^n| = 2 pi V_(n-1) for n = 3, 4, 5",
      all(S[n] == mmul(m(2, 1), V[n - 1]) for n in (3, 4, 5)))
h3, h5 = mdiv(V[3], V[4]), mdiv(S[4], S[3])       # volume down, surface up
g.check("Section 7, D3  the volume/surface assignment is the same pair on the opposite towers",
      (h3, h5) == (f5, f3))
g.check("Section 7, D4  and the same total, T(pi/2) in the family: 1 + 2 h3 + 2 h5 = 1 + 16/(3pi) + 8/3",
      sorted([m(1), mmul(m(2), h3), mmul(m(2), h5)]) == sorted(rule))
num3 = {"V3": V[3], "S2": S[2]}
num5 = {"V5": V[5], "S4": S[4]}
divs = {"V4": V[4], "S3": S[3]}
g.check("Section 7, D5  no fixed divisor with unit regions reproduces the pair (8/(3pi), 4/3) in that order",
      not any(mdiv(N3, D) == h3 and mdiv(N5, D) == h5
              for D in divs.values() for N3 in num3.values() for N5 in num5.values()))

rev = [m(1), mmul(m(2), mdiv(V[2], V[3])), mmul(m(2), mdiv(V[4], V[3]))]
g.check("Section 7, D6  share proportional to the cell instead (3/4 and 3pi/8) gives 4.856, more than 7 sigma low",
      mdiv(V[2], V[3]) == m(F(3, 4)) and mdiv(V[4], V[3]) == m(F(3, 8), 1)
      and between(rev, F(4855, 1000), F(4857, 1000)) and sigmas_away(rev)[0] > 7)

# ........ Part M.E
print("Part M.E: the thickness as a parameter")

def T_reflected(c):
    # T(pi/(2c)) = 1 + 8/(3 pi/(2c)) + 16 (pi/(2c))/(3 pi) = 1 + 16c/(3 pi) + 8/(3c)
    c = F(c)
    return [m(1), m(F(16, 3) * c, -1), m(F(8, 3) / c)]
g.check("Section 7, E1  T(c) = T(pi/(2c)) as an identity in pi, for c = 1, 2, 1/2, 3/7, 5",
      all(sorted(T(c)) == sorted(T_reflected(c)) for c in (1, 2, F(1, 2), F(3, 7), 5)))
g.check("Section 7, E2  the two roots c = 1 and c = pi/2 have product pi/2 = A/B with A = 8/3, B = 16/(3 pi)",
      mdiv(m(F(8, 3)), m(F(16, 3), -1)) == m(F(1, 2), 1))
# the floor: T* = 1 + 2 sqrt(AB) = 1 + 2 sqrt(128/(9 pi)); bracket sqrt by rationals
AB_lo, AB_hi = F(128, 9) / PI_HI, F(128, 9) / PI_LO

def sqrt_bounds(x, digits=8):
    """rational (lo, hi) bracketing sqrt(x) to 10^-digits"""
    from math import isqrt
    scale = 10 ** digits
    n = isqrt(int(x * scale * scale))
    lo = F(n, scale)
    while lo * lo > x:
        lo -= F(1, scale)
    hi = lo + F(2, scale)
    return lo, hi
s_lo, _ = sqrt_bounds(AB_lo)
_, s_hi = sqrt_bounds(AB_hi)
g.check("Section 7, E3  the floor T* = 1 + 2 sqrt(128/(9 pi)) lies in (5.2553, 5.2555)",
      F(52553, 10000) < 1 + 2 * s_lo and 1 + 2 * s_hi < F(52555, 10000))
g.check("Section 7, E4  the floor is between 1.6 and 1.8 sigma below the observed value",
      F(16, 10) < (OBS - (1 + 2 * s_hi)) / SIG and (OBS - (1 + 2 * s_lo)) / SIG < F(18, 10))
g.check("Section 7, E5  T(c) >= T* on a rational grid c = 0.5 .. 3.0 (step 0.01), with equality nowhere on the grid",
      all(bounds(T(F(k, 100)))[0] > 1 + 2 * s_lo for k in range(50, 301)))
# windows: inside at the quoted endpoints (rounded inward), outside just beyond
def within(c, k):
    return sigmas_away(T(c))[1] < k
def outside(c, k):
    return sigmas_away(T(c))[0] > k
g.check("Section 7, E6  1-sigma windows: T within 1 sigma at c = 0.944, 1.085, 1.448, 1.666; outside at 0.942, 1.087, 1.446, 1.668",
      all(within(F(x, 1000), 1) for x in (944, 1085, 1448, 1666))
      and all(outside(F(x, 1000), 1) for x in (942, 1087, 1446, 1668)))
g.check("Section 7, E7  between the windows (c = 1.25) T is more than 1 sigma below the observation",
      outside(F(125, 100), 1) and bounds(T(F(125, 100)))[1] < OBS)
g.check("Section 7, E8  2-sigma window: within at c = 0.899 and 1.749; outside at 0.897 and 1.751",
      within(F(899, 1000), 2) and within(F(1749, 1000), 2)
      and outside(F(897, 1000), 2) and outside(F(1751, 1000), 2))
# sensitivities dT/dc = -8/(3c^2) + 16/(3 pi)
def dT(c):
    c = F(c)
    return [m(-F(8, 3) / (c * c)), m(F(16, 3), -1)]
g.check("Section 7, E9  dT/dc at c = 1 in (-0.970, -0.968); at c = pi/2 it is 16/(3pi) - 32/(3 pi^2) in (0.616, 0.618)",
      between(dT(1), F(-970, 1000), F(-968, 1000))
      and between([m(F(16, 3), -1), m(-F(32, 3), -2)], F(616, 1000), F(618, 1000)))
# composition: self-interacting fraction 2 (4/(3c)) / T(c)
def selfint_bounds(c):
    lo, hi = bounds(T(c))
    num = F(8, 3) / F(c)
    return num / hi, num / lo
g.check("Section 7, E10 self-interacting fraction at c = 1 in (0.4970, 0.4972)",
      F(4970, 10000) < selfint_bounds(1)[0] and selfint_bounds(1)[1] < F(4972, 10000))
# at c = pi/2 the 3D share is 8/(3 pi): fraction = (16/(3pi)) / T
lo, hi = bounds(rule)
g.check("Section 7, E11 self-interacting fraction at c = pi/2 in (0.3164, 0.3167)",
      F(3164, 10000) < bounds([m(F(16, 3), -1)])[0] / hi
      and bounds([m(F(16, 3), -1)])[1] / lo < F(3167, 10000))
# at the floor: with x = sqrt(2/pi), 2 f_3D = 8x/3 and T* = 1 + 16x/3, so the fraction is 8x/(3 + 16x)
_x_lo, _ = sqrt_bounds(2 / PI_HI)
_, _x_hi = sqrt_bounds(2 / PI_LO)
g.check("Section 7, E11b self-interacting fraction at the floor c* = sqrt(pi/2) is 8x/(3 + 16x) with x = sqrt(2/pi), in (0.4048, 0.4050)",
      F(4048, 10000) < 8 * _x_lo / (3 + 16 * _x_lo) and 8 * _x_hi / (3 + 16 * _x_hi) < F(4050, 10000))
g.check("Section 7, E12 mirror fraction 1/T in (0.1864, 0.1865)",
      F(1864, 10000) < 1 / hi and 1 / lo < F(1865, 10000))
# the chord and the arc: both poles
g.check("Section 7, E13 both poles by chord, c = 2: T(2) in (5.728, 5.730), more than 4 sigma high",
      between(T(2), F(5728, 1000), F(5730, 1000)) and outside(2, 4))
T_pi = [m(1), m(F(8, 3), -1), m(F(16, 3))]     # c = pi: 1 + 8/(3 pi) + 16/3
g.check("Section 7, E14 both poles by arc, c = pi: T(pi) in (7.181, 7.183), more than 4 sigma high",
      between(T_pi, F(7181, 1000), F(7183, 1000)) and sigmas_away(T_pi)[0] > 4)
# two thicknesses: the observed curve 8/(3 c3) + 16 c5/(3 pi) = OBS - 1
def c5_of_c3(c3):
    c3 = F(c3)
    val = OBS - 1 - F(8, 3) / c3           # = 16 c5 / (3 pi)
    return [m(val * F(3, 16), 1)]          # c5 as a monomial in pi
g.check("Section 7, E15 off the diagonal: c3 = 4/3 needs c5 in (1.39, 1.40); c3 = 2 needs c5 in (1.78, 1.79); c3 = 1 gives c5 in (0.9999, 1.0001)",
      between(c5_of_c3(F(4, 3)), F(139, 100), F(140, 100))
      and between(c5_of_c3(2), F(178, 100), F(179, 100))
      and between(c5_of_c3(1), F(9999, 10000), F(10001, 10000)))

# ........ Part M.F
print("Part M.F: the de Sitter reductions")
g.check("Section 7, F1  zero mode: the Einstein-Hilbert factor int cos^2 = pi/2 and the dust factor int cos^4 = 3pi/8",
      W[2] == m(F(1, 2), 1) and W[4] == m(F(3, 8), 1))
g.check("Section 7, F2  the effective thickness 3pi/8 is V_4/V_3, the mean chord of the cell",
      W[4] == mdiv(V[4], V[3]))
g.check("Section 7, F3  under democracy rho_5 l / rho_us = |S^4|/|S^5| = 8/(3pi), so the zero-mode share is (3pi/8)(8/(3pi)) = 1",
      mmul(W[4], f5) == m(1))
sms = F(2, 3) * (1 - F(1, 4))
g.check("Section 7, F4  local projection: (2/3)(rho - rho/4) = rho/2, so the bulk term is kappa_5^2 rho_5 / 2",
      sms == F(1, 2))
local = mmul(m(sms), W[2])                    # (1/2) * (pi/2) = pi/4
g.check("Section 7, F5  with G_4 = G_5 / (l pi/2) the local thickness is (1/2)(pi/2) l = (pi/4) l",
      local == m(F(1, 4), 1))
g.check("Section 7, F6  the local share is (pi/4)(8/(3pi)) = 2/3", mmul(local, f5) == m(F(2, 3)))
g.check("Section 7, F7  sheets carrying total mass M over S^4 have spacing (|S^4|/|S^3|) l = (4/3) l = l int cos^3, so the sheet share is 1",
      mdiv(S[4], S[3]) == W[3] == m(F(4, 3)) and mdiv(f3, W[3]) == m(1))
tot_dem = [m(1), m(2), m(2)]                                   # 1, 1
tot_zm = [m(1), mmul(m(2), f3), m(2)]                         # 4/3, 1
tot_loc = [m(1), mmul(m(2), f3), mmul(m(2), m(F(2, 3)))]     # 4/3, 2/3
g.check("Section 7, F8  democracy + zero mode: total 5.000, more than 5 sigma low",
      bounds(tot_dem) == (F(5), F(5)) and sigmas_away(tot_dem)[0] > 5)
g.check("Section 7, F9  sheets one radius apart + zero mode: total 5.6667, more than 4 sigma high",
      between(tot_zm, F(56666, 10000), F(56667, 10000)) and sigmas_away(tot_zm)[0] > 4)
g.check("Section 7, F10 sheets one radius apart + local projection: total 5.000, more than 5 sigma low",
      bounds(tot_loc) == (F(5), F(5)) and sigmas_away(tot_loc)[0] > 5)
tot_loc_M = [m(1), m(2), mmul(m(2), m(F(2, 3)))]   # local projection + sheets carrying total mass: 1 + 2 + 4/3
g.check("Section 7, F10b sheets carrying total mass + local projection: total 4.333, more than 15 sigma low",
      bounds(tot_loc_M) == (F(13, 3), F(13, 3)) and sigmas_away(tot_loc_M)[0] > 15)
g.check("Section 7, F11 the thicknesses 3pi/8 and pi/4 in the family: T(3pi/8) in (5.263, 5.265), T(pi/4) in (5.728, 5.730)",
      between([m(1), m(F(8, 3) * F(8, 3), -1), m(F(16, 3) * F(3, 8))], F(5263, 1000), F(5265, 1000))
      and between([m(1), m(F(8, 3) * 4, -1), m(F(16, 3) * F(1, 4))], F(5728, 1000), F(5730, 1000)))
g.check("Section 7, F12 neither reduction gives thickness l: 3pi/8 and pi/4 are not 1",
      W[4] != m(1) and local != m(1))

# ........ Part M.G
print("Part M.G: the clock reflection as bookkeeping")
rho = lambda r: (4 - r) % 8
res = lambda p, q: (p - q) % 8
g.check("Section 7, G1  rho is an involution fixing 6 and 2 and swapping 1<->3, 7<->5 (each 3D tower with a 5D one)",
      all(rho(rho(r)) == r for r in range(8)) and rho(6) == 6 and rho(2) == 2
      and rho(1) == 3 and rho(7) == 5)
g.check("Section 7, G2  the census residues: (1,2)=7, (1,4)=5, (2,1)=1, (4,1)=3, (1,3)=6, (3,1)=2",
      [res(1, 2), res(1, 4), res(2, 1), res(4, 1), res(1, 3), res(3, 1)] == [7, 5, 1, 3, 6, 2])
g.check("Section 7, G3  exchanging the odd shares is the exchange c <-> pi/(2c) of the family: (f3, f5) -> (h3, h5) = (f5, f3)",
      (h3, h5) == (f5, f3))

# ........ Part M.H
print("Part M.H: the mass bound in one normalisation (Gaussian rationals)")
def c(re, im=0):
    return (F(re), F(im))
def cadd(a, b): return (a[0] + b[0], a[1] + b[1])
def cmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def cconj(a): return (a[0], -a[1])
Z, O, I = c(0), c(1), c(0, 1)
def mat(rows): return [[c(*x) if isinstance(x, tuple) else c(x) for x in r] for r in rows]
def mm(A, B):
    n, k, p_ = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(p_):
            acc = Z
            for t in range(k):
                acc = cadd(acc, cmul(A[i][t], B[t][j]))
            row.append(acc)
        out.append(row)
    return out
def msc(s_, A): return [[cmul(s_, x) for x in r] for r in A]
def madd(A, B): return [[cadd(x, y) for x, y in zip(r, t)] for r, t in zip(A, B)]
def dag(A): return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def ident(n): return [[O if i == j else Z for j in range(n)] for i in range(n)]
def zero(n): return [[Z] * n for _ in range(n)]
def block(a, b, c_, d):
    n = len(a)
    return [a[i] + b[i] for i in range(n)] + [c_[i] + d[i] for i in range(n)]
sx = mat([[0, 1], [1, 0]]); sy = mat([[0, (0, -1)], [(0, 1), 0]]); sz = mat([[1, 0], [0, -1]])
I2, Z2 = ident(2), zero(2)
g0 = block(Z2, I2, I2, Z2)
gk = [block(Z2, s_, msc(c(-1), s_), Z2) for s_ in (sx, sy, sz)]
G4 = [g0] + gk
g5c = msc(I, mm(mm(g0, gk[0]), mm(gk[1], gk[2])))
G5 = G4 + [msc(I, g5c)]
G3 = [sz, msc(I, sx), msc(I, sy)]
def clifford_ok(G, n):
    for a in range(len(G)):
        for b in range(len(G)):
            anti = madd(mm(G[a], G[b]), mm(G[b], G[a]))
            want = msc(c(2 * (1 if a == 0 else -1)), ident(n)) if a == b else zero(n)
            if anti != want:
                return False
    return True
def herm_ok(G):
    return dag(G[0]) == G[0] and all(dag(g) == msc(c(-1), g) for g in G[1:])
for lab, G, n in (("3D (1,2)", G3, 2), ("4D (1,3)", G4, 4), ("5D (1,4)", G5, 4)):
    g.check("Section 7, H %s gammas satisfy the Clifford relations, gamma^0 Hermitian, spatial anti-Hermitian" % lab,
          clifford_ok(G, n) and herm_ok(G))
def current(psi, G):
    out = []
    for g in G:
        v = mm(mm([[cconj(x) for x in psi]], mm(G[0], g)), [[x] for x in psi])[0][0]
        out.append(v)
    return out
def norm2(psi):
    acc = Z
    for x in psi:
        acc = cadd(acc, cmul(cconj(x), x))
    return acc[0]
def msq(j):
    return j[0][0] ** 2 - sum(x[0] ** 2 for x in j[1:])
samples2 = [[c(1, 2), c(-3, 1)], [c(2), c(0, 5)], [c(1, 1), c(1, -1)]]
samples4 = [[c(1, 2), c(-3, 1), c(0, 1), c(2, -2)], [c(5), c(0, 1), c(-1, 1), c(3)],
            [c(1), c(0), c(1), c(0)]]
for lab, G, smp in (("3D", G3, samples2), ("4D", G4, samples4), ("5D", G5, samples4)):
    ok_real = all(all(x[1] == 0 for x in current(psi, G)) for psi in smp)
    ok_j0 = all(current(psi, G)[0][0] == norm2(psi) for psi in smp)
    ok_bound = all(msq(current(psi, G)) <= norm2(psi) ** 2 for psi in smp)
    g.check("Section 7, H %s: current real, j^0 = psi^dag psi, m^2 <= (psi^dag psi)^2 on samples" % lab,
          ok_real and ok_j0 and ok_bound)
e3 = [c(1), c(0)]
e4v = [c(1), c(0), c(1), c(0)]
g.check("Section 7, H the +1 eigenvectors of gamma^0 are eigenvectors",
      mm(G3[0], [[x] for x in e3]) == [[x] for x in e3] and mm(g0, [[x] for x in e4v]) == [[x] for x in e4v])
for lab, G, e in (("3D", G3, e3), ("4D", G4, e4v), ("5D", G5, e4v)):
    j = current(e, G)
    g.check("Section 7, H %s: spatial current vanishes and m^2 = (psi^dag psi)^2 on the eigenvector" % lab,
          all(x == Z for x in j[1:]) and msq(j) == norm2(e) ** 2)
g.check("Section 7, H slice: the first four components of the 5D current are the 4D current",
      all(current(psi, G5)[:4] == current(psi, G4) for psi in samples4))

# ........ Part M.I
print("Part M.I: the look-elsewhere count")
meas = {"V2": V[2], "V3": V[3], "V4": V[4], "V5": V[5], "S1": S[1], "S2": S[2], "S3": S[3], "S4": S[4]}
names = list(meas)
ratios = [mdiv(meas[a], meas[b]) for a in names for b in names if a != b]
g.check("Section 7, I1  eight measures give 56 ordered ratios and 3136 expressions 1 + 2a + 2b", len(ratios) == 56 and len(ratios) ** 2 == 3136)
def count_within(target, k):
    hits, vals = 0, set()
    for a, b in product(ratios, repeat=2):
        t = [m(1), mmul(m(2), a), mmul(m(2), b)]
        lo, hi = bounds(t)
        if hi < target + k * SIG and lo > target - k * SIG:
            hits += 1
            vals.add((a[0] * 2 + b[0] * 2 if a[1] == b[1] == 0 else None, a, b))
    return hits
n1 = count_within(F(5364, 1000), 1)
n2 = count_within(F(5364, 1000), 2)
g.check("Section 7, I2  54 expressions lie within 1 sigma of 5.364 and 85 within 2 sigma", n1 == 54 and n2 == 85)
# distinct values within 1 sigma: compare as (rational, power) monomial sums, canonicalised
def canon(t):
    d = {}
    for co, k in t:
        d[k] = d.get(k, F(0)) + co
    return tuple(sorted((k, v) for k, v in d.items() if v != 0))
distinct = set()
for a, b in product(ratios, repeat=2):
    t = [m(1), mmul(m(2), a), mmul(m(2), b)]
    lo, hi = bounds(t)
    if hi < F(5364, 1000) + SIG and lo > F(5364, 1000) - SIG:
        distinct.add(canon(t))
g.check("Section 7, I3  they take 14 distinct values, one of which is the unit-ball rule's", len(distinct) == 14 and canon(rule) in distinct)
g.check("Section 7, I4  about as many lie within 1 sigma of 5.322 (43) and of 5.24 (33): the density is not special at 5.364",
      count_within(F(5322, 1000), 1) == 43 and count_within(F(524, 100), 1) == 33)

# ........ Part M.J
print("Part M.J: consistency numbers")
# baryon spacing from Omega_b h^2 = 0.02237: rho_b = 0.02237 * rho_crit/h^2, rho_crit/h^2 = 1.8785e-26 kg/m^3,
# m_p = 1.67262e-27 kg; d_b^3 = 3/(4 pi n_b); all in exact rationals with pi bounds, cube root by bracketing
rho_crit_h2 = F(18785, 10 ** 30)          # 1.8785e-26
m_p = F(167262, 10 ** 32)                 # 1.67262e-27
n_b = F(2237, 100000) * rho_crit_h2 / m_p
rs3_lo, rs3_hi = F(3, 4) / (PI_HI * n_b), F(3, 4) / (PI_LO * n_b)
g.check("Section 7, J1  the baryon number density is between 0.24 and 0.26 per cubic metre", F(24, 100) < n_b < F(26, 100))
g.check("Section 7, J2  the baryon spacing d_b = (3/(4 pi n_b))^(1/3) lies in (0.95, 1.02) m: d_b^3 in (0.857, 1.061)",
      F(857, 1000) < rs3_lo and rs3_hi < F(1061, 1000))
g.check("Section 7, J3  d_b and the de Sitter radius (~1e26 m) both exceed the 40 micrometre bound by more than 10^4",
      rs3_lo > (F(4, 100000) * 10 ** 4) ** 3 and F(10) ** 26 > F(4, 100000) * 10 ** 4)
lo, hi = bounds(rule)
g.check("Section 7, J4  under the unit-ball rule the 3D towers are 2 f_3D / (1 + T) of all matter, in (0.418, 0.420)",
      F(418, 1000) < F(8, 3) / (1 + hi) and F(8, 3) / (1 + lo) < F(420, 1000))
g.check("Section 7, J5  with velocity confined to the plane the source factor is k_perp^2/k^2 = sin^2 theta: zero along the missing direction, one across it",
      all(F(kx * kx + ky * ky, kx * kx + ky * ky + kz * kz) == (F(0) if (kx, ky) == (0, 0) else F(1) if kz == 0 else F(kx * kx + ky * ky, kx * kx + ky * ky + kz * kz))
          for kx, ky, kz in ((0, 0, 3), (2, 1, 0), (1, 2, 2))))
# prop:sheetsmove: a reduced response g needs the anisotropic stress sigma = (1-g) psi; the metric feedback; the
# orientation average of k_perp^2/k^2 is 2/3 (exact integral of (1 - mu^2)/2 over mu in [-1, 1])
def _euler_full(theta, aH, k2, psi, sigma):        # theta' = -aH theta + k^2 psi - k^2 sigma
    return -aH * theta + k2 * psi - k2 * sigma
def _euler_reduced(theta, aH, k2, psi, gg):        # theta' = -aH theta + g k^2 psi
    return -aH * theta + gg * k2 * psi
g.check("Section 7, J9  a component with theta' = -aH theta + g k^2 psi carries sigma = (1 - g) psi and no other value (rational samples)",
      all(_euler_full(th, aH, k2, ps, (1 - gg) * ps) == _euler_reduced(th, aH, k2, ps, gg)
          and (_euler_full(th, aH, k2, ps, (1 - gg) * ps + F(1, 7)) != _euler_reduced(th, aH, k2, ps, gg))
          for th, aH, k2, ps, gg in ((F(3), F(1, 2), F(4), F(1, 5), F(2, 3)), (F(-1, 3), F(2), F(9, 4), F(-2), F(19, 20)), (F(0), F(1), F(1), F(1), F(1)))))
def _psi(phi, Sigma, rho, gg, a2_over_k2, C=F(3, 2)):   # 12 pi G a^2 = (3/2) a^2 in units 8 pi G = 1; C carries that factor
    return (phi - C * a2_over_k2 * Sigma) / (1 + C * a2_over_k2 * rho * (1 - gg))
g.check("Section 7, J10 with sigma = (1 - g) psi the traceless equation k^2 (phi - psi) = 12 pi G a^2 [Sigma + rho (1 - g) psi] solves to the displayed psi (rational samples)",
      all(k2 * (phi - _psi(phi, Sg, rho, gg, a2 / k2)) == F(3, 2) * a2 * (Sg + rho * (1 - gg) * _psi(phi, Sg, rho, gg, a2 / k2))
          for phi, Sg, rho, gg, a2, k2 in ((F(1), F(1, 10), F(3), F(2, 3), F(1, 4), F(5)), (F(-2, 3), F(0), F(7, 2), F(1), F(9), F(1, 3)), (F(1, 2), F(-1, 5), F(1), F(19, 20), F(1), F(100)))))
# average of sin^2 theta = 1 - mu^2 over the sphere: (1/2) int_{-1}^{1} (1 - mu^2) dmu = (1/2)(2 - 2/3) = 2/3, exactly
avg = F(1, 2) * ((F(1) - F(-1)) - (F(1) ** 3 - F(-1) ** 3) / 3)
g.check("Section 7, J11 the orientation average of the source factor k_perp^2/k^2 = sin^2 theta over the sphere is exactly 2/3", avg == F(2, 3))
# prop:sourcing (ii): the three standard tests as exponent arithmetic and identities
def _proj_exponent(b_exp):
    # rho_5 ~ a^-3 b^-1 with b = a^{b_exp}; L ~ b; rho_5 L ~ a^{-3 - b_exp + b_exp}
    return -3 - b_exp + b_exp
g.check("Section 7, J6  continuity in a product metric: rho_5 L dilutes as a^-3 for a co-expanding (b = a) and a static (b = 1) fifth direction alike",
      _proj_exponent(1) == -3 and _proj_exponent(0) == -3)
g.check("Section 7, J7  Kaluza-Klein: with G_4 = G_5 / L and rho_4 = rho_5 L the product G_4 rho_4 = G_5 rho_5 for every rational L",
      all((F(7, 3) / L) * (F(5, 11) * L) == F(7, 3) * F(5, 11) for L in (F(1, 2), F(1), F(98, 100), F(10 ** 26))))
g.check("Section 7, J8  five-momentum: p^A p_A = m^2 gives p^mu p_mu = m^2 + p_5^2 on rational samples (signature +----)",
      all((E * E - px * px - py * py - pz * pz) == (E * E - px * px - py * py - pz * pz - p5 * p5) + p5 * p5
          for (E, px, py, pz, p5) in ((F(5), F(1), F(2), F(1), F(3)), (F(13, 2), F(0), F(0), F(0), F(5, 2)))))

# ........ Part M.K
print("Part M.K: the contact mechanism (lem:fifth, prop:thickness, tab:excludes, rem:Sfork, rem:scope, rem:twoc)")
# What this part checks: the algebraic identities of lem:fifth in GA.py, and the arithmetic of the
# counts the mechanism states (slab, downward, alternatives, non-composition).  It does not, and
# cannot, check the clauses C, I, S, O themselves, which are postulated.
from GA import commutes, scal, sub

def _prod(gens, squares):
    x = sc(1)
    for i in gens:
        x = mul(x, gen(i), squares)
    return x

def _sinv(x, squares):
    """inverse of an element with x^2 = +-1"""
    return x if eq(mul(x, x, squares), sc(1)) else scal(-1, x)

# (i) residue 5: Cl(1,4) over Cl(1,3)
P14, w14 = _prod([0, 1, 2, 3], sq14), _prod([0, 1, 2, 3, 4], sq14)
g.check("Section 7, K1  Cl(1,4): omega = e0 e1 e2 e3 e4 is central and omega^2 = +1 (split centre, two modules)",
      all(commutes(w14, gen(i), sq14) for i in range(5)) and eq(mul(w14, w14, sq14), sc(1)))
g.check("Section 7, K2  Cl(1,4): P = e0 e1 e2 e3 has P^2 = -1 and e4 = P^{-1} omega exactly",
      eq(mul(P14, P14, sq14), sc(-1)) and eq(mul(_sinv(P14, sq14), w14, sq14), gen(4)))
g.check("Section 7, K3  Cl(1,4): P -> -P with omega fixed sends e4 -> -e4",
      eq(mul(_sinv(scal(-1, P14), sq14), w14, sq14), scal(-1, gen(4))))
ep, em = scal(F(1, 2), add(sc(1), w14)), scal(F(1, 2), sub(sc(1), w14))
g.check("Section 7, K4  Cl(1,4): (1 +- omega)/2 are central orthogonal idempotents summing to 1: they cut out the two simple components",
      eq(mul(ep, ep, sq14), ep) and eq(mul(em, em, sq14), em) and eq(mul(ep, em, sq14), {}) and eq(add(ep, em), sc(1))
      and all(commutes(ep, gen(i), sq14) for i in range(5)))
Pinv14 = _sinv(P14, sq14)
g.check("Section 7, K5  Cl(1,4): e4 acts as +P^{-1} on the omega = +1 component and as -P^{-1} on the omega = -1 component",
      eq(mul(gen(4), ep, sq14), mul(Pinv14, ep, sq14)) and eq(mul(gen(4), em, sq14), mul(scal(-1, Pinv14), em, sq14)))
# the reflection through our world: v -> -e4 v e4^{-1}
e4inv = _sinv(gen(4), sq14)
def _refl(v):
    return scal(-1, mul(mul(gen(4), v, sq14), e4inv, sq14))
def _refl_prod(gens):
    x = sc(1)
    for i in gens:
        x = mul(x, _refl(gen(i)), sq14)
    return x
g.check("Section 7, K6  the reflection x4 -> -x4 fixes e0..e3 and P, negates e4, and sends omega -> -omega: it exchanges the two components",
      all(eq(_refl(gen(i)), gen(i)) for i in range(4)) and eq(_refl(gen(4)), scal(-1, gen(4)))
      and eq(_refl_prod([0, 1, 2, 3]), P14) and eq(_refl_prod([0, 1, 2, 3, 4]), scal(-1, w14)))
# (ii) residue 3: Cl(4,1) over the mirror's slice {e0, e1, e2, e4}
Pm41, w41 = _prod([0, 1, 2, 4], sq41), _prod([0, 1, 2, 3, 4], sq41)
g.check("Section 7, K7  Cl(4,1): omega central with omega^2 = -1 (one module); the mirror's P = e0 e1 e2 e4 has P^2 = -1; the added direction is e3 = -P^{-1} omega, reversed by P -> -P",
      all(commutes(w41, gen(i), sq41) for i in range(5)) and eq(mul(w41, w41, sq41), sc(-1)) and eq(mul(Pm41, Pm41, sq41), sc(-1))
      and eq(mul(_sinv(Pm41, sq41), w41, sq41), scal(-1, gen(3))) and eq(mul(_sinv(scal(-1, Pm41), sq41), w41, sq41), gen(3)))
# (iii) residue 7: Cl(1,2) inside our Cl(1,3)
w13, P13 = _prod([0, 1, 2], sq13), _prod([0, 1, 2, 3], sq13)
g.check("Section 7, K8  Cl(1,2) in Cl(1,3): omega = e0 e1 e2 central in the slice, omega^2 = -1, and the lacking direction is e3 = omega^{-1} P",
      all(commutes(w13, gen(i), sq13) for i in range(3)) and eq(mul(w13, w13, sq13), sc(-1))
      and eq(mul(_sinv(w13, sq13), P13, sq13), gen(3)))
# (iv) residue 1: Cl(2,1) inside the mirror's Cl(3,1), slice {e0, e1, e3}
w31, P31 = _prod([0, 1, 3], sq31), _prod([0, 1, 2, 3], sq31)
g.check("Section 7, K9  Cl(2,1) in Cl(3,1): omega = e0 e1 e3 central in the slice, omega^2 = +1 (two modules), and the lacking direction is e2 = -omega^{-1} P",
      all(commutes(w31, gen(i), sq31) for i in (0, 1, 3)) and eq(mul(w31, w31, sq31), sc(1))
      and eq(mul(_sinv(w31, sq31), P31, sq31), scal(-1, gen(2))))
g.check("Section 7, K10 the pattern: omega^2 = +1 (a label per quantum) at residues 5 and 1, -1 (a convention per tower) at residues 3 and 7",
      eq(mul(w14, w14, sq14), sc(1)) and eq(mul(w31, w31, sq31), sc(1)) and eq(mul(w41, w41, sq41), sc(-1)) and eq(mul(w13, w13, sq13), sc(-1)))
# prop:thickness: the stated counts.  The slab count as an integral: constant density 1/V_4 over 0 <= h <= 1,
# done as an exact Riemann sum (N steps of width 1/N, the integrand constant so lower = upper = 1/V_4).
N = 64
slab = [mdiv(m(F(1, N)), V[4]) for _ in range(N)]
slab_sum = (sum(t[0] for t in slab), slab[0][1])
f5_stated = mdiv(V[3], V[4])
g.check("Section 7, K11 the one-sided slab integral int_0^1 dh / V_4 = 1/V_4 (exact Riemann sum), so the stated f_5D = (1/V_4)/(1/V_3) = V_3/V_4 = 8/(3 pi)",
      slab_sum == mdiv(m(1), V[4]) and mdiv(slab_sum, mdiv(m(1), V[3])) == f5_stated == m(F(8, 3), -1))
# the downward count on the 3D tower's plane: our quanta with |x3| <= 1 on one side, 1/V_3 per unit area, against 1/V_2
down = mdiv(mdiv(m(1), V[3]), mdiv(m(1), V[2]))
g.check("Section 7, K12 the downward count gives rho_us/rho_3D = (1/V_3)/(1/V_2) = V_2/V_3 = 3/4 on the sheet", down == m(F(3, 4)))
# O as the equal-thickness clause: sheets s apart read on our space give rho_3D/rho_us = V_3/(s V_2); equal to the
# inverse of the downward ratio iff s = 1 (solve for s exactly)
inv_down = mdiv(m(1), down)                        # V_3/V_2
s_solved = mdiv(mdiv(V[3], V[2]), inv_down)         # s = (V_3/V_2) / (rho_3D/rho_us)
g.check("Section 7, K13 O equates V_3/(s V_2) with the inverse of the downward ratio, which solves to s = 1 exactly: O is the equal-thickness clause",
      s_solved == m(1))
T_stated = [m(1), mmul(m(2), mdiv(V[3], V[2])), mmul(m(2), f5_stated)]
g.check("Section 7, K14 the mechanism's total is the unit-ball rule's (11 pi + 16)/(3 pi), in (5.36431, 5.36433), within one sigma",
      sorted(T_stated) == sorted(rule) and between(T_stated, F(536431, 100000), F(536433, 100000)) and sigmas_away(T_stated)[1] < 1)
# tab:excludes: the alternatives
T_both = [m(1), mmul(m(2), mdiv(V[3], mmul(m(2), V[2]))), mmul(m(2), mmul(m(2), f5_stated))]
g.check("Section 7, K15 S withdrawn (both sides): f_5D = 2 V_3/V_4, f_3D = V_3/(2 V_2) = 2/3, total = T(2) in (5.728, 5.729), more than 5.5 sigma high",
      sorted(T_both) == sorted(T(2)) and between(T_both, F(5728, 1000), F(5729, 1000)) and sigmas_away(T_both)[0] > F(55, 10))
# the section weight, as a real integral: int_0^1 (1 - h^2)^{3/2} dh bracketed by exact Riemann sums (the integrand
# is decreasing on [0, 1]); compare with half the Wallis value 3 pi / 16
def _w(h):     # (1 - h^2)^{3/2} bracketed rationally: the square root by sqrt_bounds
    x = 1 - h * h
    lo, hi = sqrt_bounds(x) if x > 0 else (F(0), F(0))
    return x * lo, x * hi
Nq = 400
low = sum(_w(F(k + 1, Nq))[0] for k in range(Nq)) / Nq
high = sum(_w(F(k, Nq))[1] for k in range(Nq)) / Nq
w_lo, w_hi = bounds([m(F(3, 16), 1)])
g.check("Section 7, K16 the one-sided section weight int_0^1 (1-h^2)^{3/2} dh brackets 3 pi/16 = 0.589 (Riemann sums, 400 steps, rational square roots)",
      low < w_hi and high > w_lo and high - low < F(1, 100))
g.check("Section 7, K17 section weights integrate over both sides to V_D/V_{D-1} = W_D (Wallis) for D = 2..8, as identities in pi; for D = 4 that is 3 pi/8, the zero-mode factor",
      all(mdiv(V[D], V[D - 1]) == W[D] for D in range(2, 9)) and W[4] == m(F(3, 8), 1))
g.check("Section 7, K18 I withdrawn, S kept (one side by section): f_5D = 1/2, f_3D = 2, total 6.000, more than 9.5 sigma high",
      mmul(mmul(m(F(1, 2)), mdiv(V[4], V[3])), f5_stated) == m(F(1, 2))
      and mdiv(mdiv(m(1), V[2]), mmul(mmul(m(F(1, 2)), mdiv(V[3], V[2])), mdiv(m(1), V[3]))) == m(2)
      and sigmas_away([m(6)])[0] > F(95, 10))
g.check("Section 7, K19 I and S withdrawn (by section, both sides): f_5D = 1, f_3D = 1, total 5.000, more than 5.5 sigma low",
      mmul(mdiv(V[4], V[3]), f5_stated) == m(1) and mdiv(mmul(mdiv(V[3], V[2]), mdiv(m(1), V[3])), mdiv(m(1), V[2])) == m(1)
      and sigmas_away([m(5)])[0] > F(55, 10))
# rem:twoc with c_5 = 1: c_3 window at one sigma
rem_lo, rem_hi = bounds([m(OBS - 1), m(F(-16, 3), -1)])
c3_lo = F(8, 3) / (rem_hi + SIG)
c3_hi = F(8, 3) / (rem_lo - SIG)
g.check("Section 7, K20 O withdrawn with c_5 = 1: the observation confines c_3 to [0.976, 1.025] at one sigma (brackets in (0.975, 0.977) and (1.024, 1.026))",
      F(975, 1000) < c3_lo < F(977, 1000) and F(1024, 1000) < c3_hi < F(1026, 1000))
# rem:Sfork: S selects no module: two components at half density each sourcing one side, or one at full density
half = mdiv(m(F(1, 2)), V[4])
both_modules = (half[0] + half[0], half[1])
g.check("Section 7, K21 two components at density 1/(2 V_4) each sourcing one side sum to the one-component slab 1/V_4: S selects no module",
      both_modules == mdiv(m(1), V[4]))
# rem:scope: the mechanism does not compose across the double nesting (1,2) in (1,3) in (1,4)
chained = mmul(mdiv(V[3], V[4]), mdiv(V[2], V[3]))            # R3: one cell radius per unshared direction, = V_2/V_4
direct_full = mdiv(mdiv(V[2], V[4]), mdiv(m(1), V[2]))         # 4-ball cells meeting the plane: transverse unit disc, area V_2
direct_half = mmul(m(F(1, 2)), direct_full)
direct_quarter = mmul(m(F(1, 4)), direct_full)
g.check("Section 7, K22 double nesting: R3 composes to rho_5D/rho_3D = V_2/V_4 = 2/pi, while the direct contact count gives V_2^2/V_4 = 2, 1 (half-disc) or 1/2 (quadrant): none agrees, the mechanism does not compose",
      chained == m(F(2, 1), -1) and direct_full == m(2) and direct_half == m(1) and direct_quarter == m(F(1, 2))
      and chained not in (direct_full, direct_half, direct_quarter))


# ........ Part M.L
print("Part M.L: Premise E (prop:rule (ii) to (iv), prop:thickness (iv), rem:coexpand)")
# Premise E with its length written out: every populated tower holds the mass mu
# per ball of radius d of its own space, rho_D V_D d^D = mu.  Densities are
# monomials q pi^k; lengths and masses are rationals.
def e_dens(D, mu, d):
    """Premise E: the mass per unit D-volume, mu/(V_D d^D)"""
    return mdiv(m(F(mu) / F(d) ** D), V[D])

def e_ball(rho, D, d):
    """the mass in a ball of radius d of a D-dimensional space at density rho"""
    return mmul(mmul(rho, V[D]), m(F(d) ** D))

def e_share(rho, rho3, D, length):
    """the sourcing rule on given densities: rho * length^(D-3) / rho3"""
    return mdiv(mmul(rho, m(F(length) ** (D - 3))), rho3)

E_MU = [F(1), F(938, 7), F(5, 11)]
E_D = [F(1), F(49, 50), F(7, 3)]
g.check("Section 7, L1  prop:rule(i) with d written out: under E and R3 the shares are 4/3 and 8/(3 pi) for every sample mu and d (both cancel)",
        all(e_share(e_dens(2, mu, d), e_dens(3, mu, d), 2, d) == f3
            and e_share(e_dens(4, mu, d), e_dens(3, mu, d), 4, d) == f5
            for mu in E_MU for d in E_D))

def _filling(k2, k4, mq, d):
    """quanta of mass k mq, one per k balls of radius d: (density, mass of a quantum, quanta per ball)"""
    out = {}
    for D, k in ((2, k2), (3, F(1)), (4, k4)):
        number = mdiv(m(1 / (k * d ** D)), V[D])
        out[D] = (mmul(m(k * mq), number), k * mq, mmul(mmul(number, V[D]), m(d ** D)))
    return out
_fills = [_filling(k2, k4, F(938, 7), F(49, 50)) for k2, k4 in ((F(5), F(16)), (F(1, 3), F(7, 2)))]
g.check("Section 7, L2  prop:rule(ii): fillings whose quanta are heavier and rarer by factors 5 and 16, or 1/3 and 7/2, keep E, break R1 and R2, and have the shares 4/3 and 8/(3 pi)",
        all(all(e_ball(fl[D][0], D, F(49, 50)) == m(F(938, 7)) for D in (2, 3, 4))
            and all(fl[D][1] != F(938, 7) and fl[D][2] != m(1) for D in (2, 4))
            and e_share(fl[2][0], fl[3][0], 2, F(49, 50)) == f3
            and e_share(fl[4][0], fl[3][0], 4, F(49, 50)) == f5
            for fl in _fills))
_pm = _filling(F(1), F(1), F(938, 7), F(49, 50))
g.check("Section 7, L3  prop:rule(ii): R1 with R2 in the length d is E with mu = m",
        all(_pm[D][1] == F(938, 7) and _pm[D][2] == m(1) and e_ball(_pm[D][0], D, F(49, 50)) == m(F(938, 7))
            for D in (2, 3, 4)))

_DIM = {1: 2, 7: 2, 2: 3, 3: 4, 5: 4}                  # the dark residues and their space dimensions
_TARGET = {1: f3, 7: f3, 2: m(1), 3: f5, 5: f5}

def _dens_from(shares, s, rho6):
    """the sourcing rule solved for the densities: f_r = rho_r s^(D_r - 3) / rho_6"""
    return {r: mmul(mmul(shares[r], rho6), m(F(s) ** (3 - _DIM[r]))) for r in _DIM}

def _e_holds(rho, rho6, d):
    return all(e_ball(rho[r], _DIM[r], d) == e_ball(rho6, 3, d) for r in _DIM)

_conv, _mirror, _split = [], [], []
for s_, rho6_ in [(F(1), m(F(3, 7), -1)), (F(49, 50), m(F(11, 2), -1)), (F(5, 3), m(F(2), -1))]:
    rho_ = _dens_from(_TARGET, s_, rho6_)
    _conv.append(_e_holds(rho_, rho6_, s_) and all(e_share(rho_[r], rho6_, _DIM[r], s_) == _TARGET[r] for r in _DIM))
    bad_ = dict(_TARGET); bad_[2] = m(2)                # the mirror at twice our density
    rb_ = _dens_from(bad_, s_, rho6_)
    _mirror.append(all(e_ball(rb_[2], 3, L_) == mmul(m(2), e_ball(rho6_, 3, L_)) and not _e_holds(rb_, rho6_, L_)
                       for L_ in (s_, s_ / 2, 2 * s_, s_ + 1, F(7, 3))))
    sp_ = dict(_TARGET); sp_[1] = mmul(f3, m(F(3, 2))); sp_[7] = mmul(f3, m(F(1, 2)))   # the pair's sum kept at 8/3
    rs_ = _dens_from(sp_, s_, rho6_)
    _split.append(sp_[1][0] + sp_[7][0] == 2 * f3[0] and sp_[1][1] == sp_[7][1] == f3[1]
                  and all(not _e_holds(rs_, rho6_, L_) for L_ in (s_, s_ / 2, 2 * s_, F(3, 2) * s_)))
g.check("Section 7, L4  prop:rule(iii): on all six towers, s = t with the five shares (4/3, 4/3, 1, 8/(3 pi), 8/(3 pi)) is E at d = s, and E at d with s = t = d gives each share; with the mirror at twice our density, or the sheet pair split 3/2 and 1/2 with its sum kept, E fails at every sample length",
        all(_conv) and all(_mirror) and all(_split))

_part, _five = [], []
for rho2_, rho3_ in [(F(1), F(1)), (F(7, 5), F(2, 9)), (F(1, 100), F(31))]:
    d_ = F(3) * rho2_ / (F(4) * rho3_)                # rho_2 V_2/(rho_3 V_3) with V_2 = pi, V_3 = 4 pi/3
    _part.append(e_ball(m(rho2_), 2, d_) == e_ball(m(rho3_), 3, d_)
                 and all(e_ball(m(rho2_), 2, o) != e_ball(m(rho3_), 3, o) for o in (d_ / 2, 2 * d_, d_ + 1))
                 and e_share(m(rho2_), m(rho3_), 2, d_) == f3)
    on = mdiv(mmul(m(rho3_), V[3]), mmul(V[4], m(d_)))
    off = mmul(on, m(F(9, 10)))
    _five.append(e_ball(on, 4, d_) == e_ball(m(rho3_), 3, d_) and e_share(on, m(rho3_), 4, d_) == f5
                 and e_ball(off, 4, d_) != e_ball(m(rho3_), 3, d_)
                 and e_share(off, m(rho3_), 4, d_) == mmul(f5, m(F(9, 10))))
g.check("Section 7, L5  prop:rule(iii): d = rho_2 V_2/(rho_3 V_3) equalises the mass per ball of a 3D tower and ours (d/2, 2d, d + 1 do not), and with sheets that far apart f_3D = 4/3 for three unrelated pairs of densities",
        all(_part))
g.check("Section 7, L6  prop:rule(iii): at that d, E for the 5D towers holds exactly when f_5D = 8/(3 pi); a 5D density nine tenths of it breaks E and gives nine tenths of the share",
        all(_five))
_r3 = m(F(1), -1)
_r2, _r4 = mmul(mmul(f3, m(1)), _r3), mmul(mmul(f5, _r3), m(F(1, 2)))     # s = 1, t = 2
g.check("Section 7, L7  prop:rule(iii): with s = 1 and t = 2 the sheets ask for the length 1 and the 5D towers for the length 2, so E holds at no d",
        mdiv(mmul(_r2, V[2]), mmul(_r3, V[3])) == m(1) and mdiv(mmul(_r3, V[3]), mmul(_r4, V[4])) == m(2))
g.check("Section 7, L8  prop:rule(iv): in a ball of radius k d the mass is k^2, k^3, k^4 times mu at D = 2, 3, 4, three different numbers for k = 2, 3, 1/2: E holds in one length only",
        all([mdiv(e_ball(e_dens(D, mu, d), D, k * d), m(mu)) for D in (2, 3, 4)] == [m(k ** 2), m(k ** 3), m(k ** 4)]
            and len({k ** 2, k ** 3, k ** 4}) == 3
            for mu in E_MU for d in E_D for k in (F(2), F(3), F(1, 2))))

_mu, _d = F(938, 7), F(49, 50)
_slab = mmul(e_dens(4, _mu, _d), m(_d))                 # int_0^d mu dh/(V_4 d^4)
g.check("Section 7, L9  prop:thickness(i), (ii) with d written out: the one-sided slab holds mu/(V_4 d^3) per unit three-volume, a share 8/(3 pi); sheets s apart give V_3 d/(s V_2), equal to V_3/V_2 only at s = d",
        mdiv(_slab, e_dens(3, _mu, _d)) == f5
        and all((mdiv(mmul(e_dens(2, _mu, _d), m(1 / s_)), e_dens(3, _mu, _d)) == f3) == (s_ == _d)
                for s_ in (_d, _d / 2, 2 * _d, F(1))))
_k, _a = 16, 2 * _d
_own5 = mdiv(mmul(e_dens(4, _mu, _d), m(_a)), e_dens(3, _mu, _d))
_own3 = mdiv(mmul(e_dens(2, _mu, _d), m(1 / _a)), e_dens(3, _mu, _d))
_own_total = [m(1), mmul(m(2), f3), mmul(m(2), _own5)]
g.check("Section 7, L10 prop:thickness(iv): quanta sixteen times heavier and rarer have own cell radius a = 2d (a^4 = 16 d^4); read on that cell the 5D share is 2 V_3/V_4 = 16/(3 pi) and a 3D tower's would be (V_3/V_2)(d/a) = 2/3",
        _a ** 4 == _k * _d ** 4 and _own5 == mmul(m(2), f5) == m(F(16, 3), -1) and _own3 == m(F(2, 3)))
g.check("Section 7, L11 prop:thickness(iv): with the 5D share doubled and the others unchanged the total is 11/3 + 32/(3 pi), in (7.06, 7.07), more than twenty standard deviations from the record",
        between(_own_total, F(706, 100), F(707, 100)) and sigmas_away(_own_total)[1] > 20)

_sheet_ok = []
for a6_ in (_d, 2 * _d, _d / 3):                         # this world's own cell radius
    for ar_ in (_d, 2 * _d, 5 * _d):                     # the sheet tower's own cell radius: it does not enter
        on_plane_ = mdiv(mmul(e_dens(3, _mu, _d), m(a6_)), e_dens(2, _mu, _d))     # rho_us/rho_3D on the plane
        share_ = mdiv(mmul(e_dens(2, _mu, _d), m(1 / a6_)), e_dens(3, _mu, _d))
        _sheet_ok.append(on_plane_ == mmul(mdiv(V[2], V[3]), m(a6_ / _d))
                         and all((mmul(mdiv(mmul(e_dens(2, _mu, _d), m(1 / s_)), e_dens(3, _mu, _d)), on_plane_) == m(1)) == (s_ == a6_)
                                 for s_ in (a6_, _d, ar_, 2 * a6_))
                         and share_ == mmul(f3, m(_d / a6_))
                         and (share_ == mmul(f3, m(_d / ar_))) == (ar_ == a6_))
g.check("Section 7, L13 prop:thickness(iv): for a sheet tower the count on own cells is made on this world's cells: the sheets come out a_6 apart and the share is (V_3/V_2)(d/a_6), whatever the tower's own cell radius (a_6 = d, 2d, d/3; a_r = d, 2d, 5d)",
        all(_sheet_ok))

def _lengths(a, b):
    """the two lengths of rem:coexpand at scale factors a, b: densities go as a^-2, a^-3, (a^3 b)^-1"""
    r2, r3, r4 = m(F(7, 5) / a ** 2), m(F(2, 9) / a ** 3), m(F(3, 4) / (a ** 3 * b), -1)
    return mdiv(mmul(r2, V[2]), mmul(r3, V[3])), mdiv(mmul(r3, V[3]), mmul(r4, V[4]))
_s0, _f0 = _lengths(F(1), F(1))
g.check("Section 7, L12 rem:coexpand: the length equalising a 3D tower with us scales as a and the length equalising a 5D tower with us scales as b; their ratio is constant exactly when b follows a (samples a = 2, 5, 1/3; b = a and b fixed)",
        all(_lengths(a, b)[0] == mmul(_s0, m(a)) and _lengths(a, b)[1] == mmul(_f0, m(b))
            and ((mdiv(_lengths(a, b)[0], _lengths(a, b)[1]) == mdiv(_s0, _f0)) == (a == b))
            for a in (F(2), F(5), F(1, 3)) for b in (a, F(1))))


# ---------------------------------------------------------------------------
# Section 7.7: R2's density excludes composite-strength annihilation
# (floating point, order of magnitude)
# ---------------------------------------------------------------------------
import math
hbarc = 1.97327e-16            # GeV m
m_q = 0.938272                 # GeV, R1's common mass (the nucleon's)
d_b = 0.98                     # m, R2's common spacing
T_cmb = 2.3487e-13             # GeV
M_Pl = 2.435e18                # GeV, reduced
H_0, Om_m, Om_L = 1.436e-42, 0.315, 0.685
def gstar(T):
    for Tc, gg in ((173, 106.75), (80, 96.25), (4, 86.25), (1.2, 75.75), (0.2, 61.75), (0.15, 17.25), (5e-4, 10.75)):
        if T > Tc:
            return gg
    return 3.36
def a_of(T):
    return (3.909 / gstar(T)) ** (1.0 / 3.0) * T_cmb / T
def H_of(T):
    a = a_of(T)
    return math.sqrt((math.pi ** 2 * gstar(T) / 90.0) * T ** 4 / M_Pl ** 2 + H_0 ** 2 * (Om_m / a ** 3 + Om_L))
n2_R2 = hbarc ** 2 / (math.pi * d_b ** 2)          # R2 per sheet today, GeV^2 (comoving, a = 1)
def depleted(P, T_start):
    """comoving per-sheet number left by 2D s-wave annihilation, sigma_1 v = 2P/m, once far above equilibrium"""
    sv = 2.0 * P / m_q
    N = 4000
    w_end = math.log(T_start / T_cmb)
    integral = 0.0
    for k in range(N):
        w0, w1 = w_end * k / N, w_end * (k + 1) / N
        A0 = sv / (a_of(T_start * math.exp(-w0)) ** 2 * H_of(T_start * math.exp(-w0)))
        A1 = sv / (a_of(T_start * math.exp(-w1)) ** 2 * H_of(T_start * math.exp(-w1)))
        integral += 0.5 * (A0 + A1) * (w1 - w0)
    return 1.0 / integral
ratio = depleted(1.0, m_q / 25.0) / n2_R2
G_ratio = (lambda T1, T2: (a_of(T1) ** 2 * math.sqrt(math.pi ** 2 * gstar(T1) / 90) * T1 ** 2) / (a_of(T2) ** 2 * math.sqrt(math.pi ** 2 * gstar(T2) / 90) * T2 ** 2))(0.02, 0.01)
g.check("Section 7.7 (floating point): on a sheet n ~ a^-2 and H ~ a^-2 in radiation domination, so a^2 H is constant (20 against 10 MeV, same g*): the annihilation-to-expansion ratio does not fall",
        abs(G_ratio - 1.0) < 1e-12)
g.check("Section 7.7 (floating point): a symmetric relic annihilating at full strength (P = 1) on its sheets is left at about 3e-14 of R2's density (between 1e-14 and 1e-13): composite strength cannot hold the density the rule assigns",
        1e-14 < ratio < 1e-13)


# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------

print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    raise SystemExit(1)
print("All checks pass.")
