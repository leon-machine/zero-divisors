#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T16.py: exact-arithmetic verification of the computational identities of
"Quantum Mechanics and General Relativity from One Relation: The Two Shadows
and the Laboratory" (Transport Papers, T16).

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rationals and Gaussian rationals, the
Clifford blade engine for the frame computations, and exact linear algebra
over the Gaussian rationals for the kernel computations.  No floating point
anywhere.  Statement tags refer to the compiled paper.  The interpretive
clauses (where each theory is located; the hbar and G identifications; the
supervenience premise and its consequences; the freedom counts, which are
imported counts) are not computations and are not scripted; the paper says
so.  The placement of c (lem:speed) is computational at the level the paper
states and is scripted in the second part of Part B.

Parts:
  A  the two presentations: Witt bases and the CAR in Cl(1,1), Cl(1,3)_C,
     Cl(2,4)_C, with the real and complex capacities exhibited
  B  capacity increment (real and complex), and the overlap table
  C  the manifold of vacuum lines: nullity of the point embedding from the
     inner product; the Fock model of Cl(2,4)_C; the kernel of a point's
     null vector on twistor space is the two-dimensional incidence line, a
     projective line of Fock vacua and not one vacuum
  D  the laboratory: covariant first-order operators (uniqueness of the vector
     derivative up to a constant factor, by exact kernel computation); the
     time direction gamma_0, the boost and spin planes; the Pauli identity;
     the Klein-Gordon square of the Dirac-Hestenes equation
  E  the measure: the Dirac current's positivity and conservation, and its
     uniqueness among constant sesquilinear currents by exact kernel
     computation; the indifference step (invariant weights are uniform) and
     the fine-graining construction on rational instances
  Second parts (v1.6, 2026-09-07), each a companion script of the same day
  wrapped as one function with its tags mapped to the paper:
  B (2)  the third constant, lem:speed and fact:cone: component counts of
     {Q > 0} on the signature grid by union-find over rational sample points
     joined by exact piecewise-linear paths with certified Q-minima, the
     cone-determines-form kernel up to (3,3), the Witt rescaling as the
     boost rotor in Cl(1,1) with the sign convention fixed, the unit
     determinant -2 and the Planck monomials, the Galilean degeneration,
     and the conjugacy of three hyperbolic planes of (1,3) by Witt
     (45 checks)
  C (2)  the nu = 4 quadric, rem:quadric: the Cartan form against the M^2 = -1
     purity test on seeded random Gaussian-rational states, on and off the
     quadric, the Thouless-Pfaffian identity and its converse on the chart
     psi_0 != 0, the orbit ranks at nu = 2, 3, 4 (27 checks)
  D (2)  the Schrodinger sharpening, lem:square, lem:oddroots, lem:onedatum,
     cor:onebit: the square of the general first-order law, odd square
     roots of -1 and the chiral phase, the commutant of C and the J to
     gamma_0 bijection, the one bit, the ideal picture (34 checks)
  Total 146 checks (37 prior + 45 + 27 + 34 + 3); the three added 2026-09-11
  are Part A's checks for the paragraph "The relation in words" (the
  occupation projectors, the eigen-relations of sigma, the sign reversals).
  Count 143 unchanged from v1.6 to the terminology pass, where the
  component-count, I4, H4, H5 and Part F checks were made substantive.
"""

from fractions import Fraction as F
from itertools import combinations, permutations

import GA as g

ZERO, ONE = g.qi(0), g.qi(1)
I_ = g.qi(0, 1)


# ---------------------------------------------------------------------------
# helpers: blade-engine elements with Gaussian-rational coefficients
# ---------------------------------------------------------------------------

def vec(coeffs):
    """Vector sum_i coeffs[i] e_i as a blade-engine element (QI coefficients)."""
    return {(i,): g.qi(c) for i, c in enumerate(coeffs) if g.qi(c)}


def cscal(c, x):
    c = g.qi(c)
    return {b: c * v for b, v in x.items()} if c else {}


def anti(x, y, sq):
    return g.add(g.mul(x, y, sq), g.mul(y, x, sq))


def is_scalar(x, value):
    """x equals the scalar `value` exactly."""
    return g.eq(x, {(): g.qi(value)} if g.qi(value) else {})


def check_car(pairs, sq, label):
    """pairs: list of (w, wbar).  Checks the CAR of len(pairs) modes."""
    ok = True
    n = len(pairs)
    for i in range(n):
        for j in range(n):
            wi, wbi = pairs[i]
            wj, wbj = pairs[j]
            ok = ok and g.is_zero(anti(wi, wj, sq))
            ok = ok and g.is_zero(anti(wbi, wbj, sq))
            ok = ok and is_scalar(anti(wi, wbj, sq), 1 if i == j else 0)
    g.check(label, ok)
    return ok


# ---------------------------------------------------------------------------
# Part A: the two presentations (prop:twopresentations)
# ---------------------------------------------------------------------------

# A1. Cl(1,1), real: orthogonal reading and Witt reading from one pair of
#     generators.  e0^2 = +1, e1^2 = -1.
SQ11 = g.sig(1, 1)
e0, e1 = vec([1, 0]), vec([0, 1])
g.check("prop:twopresentations (A1): the orthogonal reading in Cl(1,1): "
        "{e0,e0} = 2, {e1,e1} = -2, {e0,e1} = 0 exactly",
        is_scalar(anti(e0, e0, SQ11), 2) and is_scalar(anti(e1, e1, SQ11), -2)
        and g.is_zero(anti(e0, e1, SQ11)))
w11 = cscal(F(1, 2), g.add(e0, e1))
wb11 = cscal(F(1, 2), g.sub(e0, e1))
check_car([(w11, wb11)], SQ11,
          "prop:twopresentations (A1): the Witt reading in Cl(1,1): the real "
          "null pair w = (e0+e1)/2, wbar = (e0-e1)/2 satisfies {w,w} = "
          "{wbar,wbar} = 0, {w,wbar} = 1: the CAR of one real mode")

# A1 (words). The paragraph "The relation in words" (Section 3): the two
#     occupation projectors are (1 +/- sigma)/2 for sigma = e0 e1, the pair
#     diagonalises sigma with opposite signs, and the sign of sigma (the
#     orientation of the plane) is what tells creation from annihilation:
#     reversing e0 alone or e1 alone swaps the projectors, both together
#     fixes them.  Here n_+ = w11, n_- = wb11.
sigma11 = g.mul(e0, e1, SQ11)
half = F(1, 2)
proj_occ = g.mul(wb11, w11, SQ11)     # n_- n_+
proj_emp = g.mul(w11, wb11, SQ11)     # n_+ n_-
g.check("Section 3 (words): in Cl(1,1) the occupation projectors are "
        "n_- n_+ = (1 + sigma)/2 and n_+ n_- = (1 - sigma)/2 for sigma = e0 e1, "
        "and they sum to 1",
        g.eq(proj_occ, g.add(g.sc(half), cscal(half, sigma11)))
        and g.eq(proj_emp, g.sub(g.sc(half), cscal(half, sigma11)))
        and is_scalar(g.add(proj_occ, proj_emp), 1))
g.check("Section 3 (words): sigma n_+ = -n_+ and sigma n_- = +n_-: the pair "
        "diagonalises the plane's bivector with opposite signs, so the sign "
        "of sigma labels which ray is which",
        g.eq(g.mul(sigma11, w11, SQ11), g.neg(w11))
        and g.eq(g.mul(sigma11, wb11, SQ11), wb11))
def _projs(a, b):
    """(n_- n_+, n_+ n_-) for n_+ = (a+b)/2, n_- = (a-b)/2."""
    np_, nm_ = cscal(half, g.add(a, b)), cscal(half, g.sub(a, b))
    return g.mul(nm_, np_, SQ11), g.mul(np_, nm_, SQ11)
p_t0 = _projs(g.neg(e0), e1)        # reverse the time direction alone
p_s0 = _projs(e0, g.neg(e1))        # reverse the space direction alone
p_b0 = _projs(g.neg(e0), g.neg(e1)) # reverse both
g.check("Section 3 (words): reversing e0 alone, or e1 alone, swaps the two "
        "projectors (sigma -> -sigma); reversing both leaves them fixed: the "
        "datum is the orientation of the plane, not a time orientation",
        p_t0 == (proj_emp, proj_occ) and p_s0 == (proj_emp, proj_occ)
        and p_b0 == (proj_occ, proj_emp))

# A2. Cl(1,3) complexified: signature (+,-,-,-).  One real hyperbolic plane
#     (e0, e1) and one complex pair from the anisotropic (e2, e3).
SQ13 = g.sig(1, 3)
E = [vec([1 if j == i else 0 for j in range(4)]) for i in range(4)]
w1 = cscal(F(1, 2), g.add(E[0], E[1]))
wb1 = cscal(F(1, 2), g.sub(E[0], E[1]))
w2 = cscal(F(1, 2), g.add(E[2], cscal(I_, E[3])))
wb2 = cscal(F(-1, 2), g.sub(E[2], cscal(I_, E[3])))
check_car([(w1, wb1), (w2, wb2)], SQ13,
          "prop:twopresentations (A2): Cl(1,3) complexified carries two "
          "modes: the real pair on the boost plane (e0,e1) and the complex "
          "pair (e2 + i e3)/2, -(e2 - i e3)/2 on the anisotropic kernel; all "
          "CAR relations exact over the Gaussian rationals")
# the change of basis (e0..e3) -> (w1, wb1, w2, wb2) is invertible over C
M13 = [[g.qi(F(1, 2)), g.qi(F(1, 2)), ZERO, ZERO],
       [g.qi(F(1, 2)), g.qi(F(-1, 2)), ZERO, ZERO],
       [ZERO, ZERO, g.qi(F(1, 2)), g.qi(0, F(1, 2))],
       [ZERO, ZERO, g.qi(F(-1, 2)), g.qi(0, F(1, 2))]]
g.check("prop:twopresentations (A2): the Witt basis of C^4 is a change of "
        "basis of the orthogonal one: the 4x4 coefficient matrix has rank 4 "
        "over the Gaussian rationals", g.field_rank(M13) == 4)
# the real pair is real and the second pair is not: a real isotropic vector
# in the (e2, e3) plane does not exist (definite form), so the real capacity
# of (1,3) is one and the complex capacity is two
g.check("prop:capacity (A2): the anisotropic kernel of (1,3) is definite: "
        "for rational (a,b) != 0 the vector a e2 + b e3 has square -(a^2+b^2) "
        "< 0, so no real null vector exists there and the real capacity of "
        "(1,3) is one while the complex capacity is two",
        all(g.mul(vec([0, 0, a, b]), vec([0, 0, a, b]), SQ13)
            == {(): g.qi(-(a * a + b * b))}
            for a in (F(0), F(1), F(-2), F(3, 7)) for b in (F(0), F(1), F(-5, 3))
            if (a, b) != (0, 0)))

# A3. Cl(2,4) complexified: signature (+,+,-,-,-,-).  Two real hyperbolic
#     planes (e0,e2), (e1,e3); one complex pair from (e4, e5).
SQ24 = g.sig(2, 4)
E6 = [vec([1 if j == i else 0 for j in range(6)]) for i in range(6)]
p1 = (cscal(F(1, 2), g.add(E6[0], E6[2])), cscal(F(1, 2), g.sub(E6[0], E6[2])))
p2 = (cscal(F(1, 2), g.add(E6[1], E6[3])), cscal(F(1, 2), g.sub(E6[1], E6[3])))
p3 = (cscal(F(1, 2), g.add(E6[4], cscal(I_, E6[5]))),
      cscal(F(-1, 2), g.sub(E6[4], cscal(I_, E6[5]))))
check_car([p1, p2, p3], SQ24,
          "prop:twopresentations (A3): Cl(2,4) complexified carries three "
          "modes: two real pairs on the hyperbolic planes (e0,e2), (e1,e3) "
          "and one complex pair on the anisotropic (e4,e5); all nine CAR "
          "relation sets exact")
g.check("prop:capacity (A3): the anisotropic kernel of (2,4) is definite, so "
        "the real capacity of (2,4) is two (T3, Thm. 4.3) and the complex "
        "capacity is three",
        all(g.mul(vec([0, 0, 0, 0, a, b]), vec([0, 0, 0, 0, a, b]), SQ24)
            == {(): g.qi(-(a * a + b * b))}
            for a in (F(1), F(-2)) for b in (F(1), F(-5, 3))))

# ---------------------------------------------------------------------------
# Part B: capacity increment and the overlap table (prop:capacity, prop:overlap)
# ---------------------------------------------------------------------------

def real_capacity(p, q):
    return min(p, q)


def complex_capacity(p, q):
    return (p + q) // 2


g.check("prop:capacity(2): a (1,1) ascent raises BOTH capacities by exactly "
        "one, on the exhaustive grid p, q <= 8: min(p+1,q+1) = min(p,q) + 1 "
        "and floor((p+q+2)/2) = floor((p+q)/2) + 1",
        all(real_capacity(p + 1, q + 1) == real_capacity(p, q) + 1
            and complex_capacity(p + 1, q + 1) == complex_capacity(p, q) + 1
            for p in range(9) for q in range(9)))

g.check("prop:capacity: the two capacity tables for the series' signatures: "
        "real (1,1),(1,3),(2,4),(3,5) -> 1,1,2,3; complex -> 1,2,3,4",
        [real_capacity(*s) for s in ((1, 1), (1, 3), (2, 4), (3, 5))]
        == [1, 1, 2, 3]
        and [complex_capacity(*s) for s in ((1, 1), (1, 3), (2, 4), (3, 5))]
        == [1, 2, 3, 4])
g.check("prop:capacity: on the grid p, q <= 8 the real and complex capacities "
        "agree exactly when |p - q| <= 1 (a biconditional: both directions "
        "tested on all 81 signatures, 25 agreeing and 56 not)",
        all((real_capacity(p, q) == complex_capacity(p, q)) == (abs(p - q) <= 1)
            for p in range(9) for q in range(9))
        and sum(1 for p in range(9) for q in range(9) if abs(p - q) <= 1) == 25)

# prop:overlap(i): the tower rung's dimension doubling against the index
# increment: Cl(p+1, q+1) = Mat(2, Cl(p,q)) has 2^2 = 4 times the dimension,
# i.e. the matrix dimension doubles once per rung, one mode per rung; the
# Witt increment is one per rung.  One count in two vocabularies: the
# dimension shadow of the periodicity isomorphism, and index arithmetic;
# both identities, recorded rather than tested (prop:overlap(i)).
def cl_dim(p, q):
    return 2 ** (p + q)


g.check("prop:overlap(i): per rung the algebra dimension multiplies by 4 = "
        "2^2 (one matrix doubling, one mode) and the real and complex "
        "capacities each rise by one, on the grid p, q <= 6",
        all(cl_dim(p + 1, q + 1) == 4 * cl_dim(p, q)
            and real_capacity(p + 1, q + 1) - real_capacity(p, q) == 1
            and complex_capacity(p + 1, q + 1) - complex_capacity(p, q) == 1
            for p in range(7) for q in range(7)))

# ---------------------------------------------------------------------------
# Part C: the manifold of vacuum lines (prop:vacuummanifold)
# ---------------------------------------------------------------------------

# C1. The conformal model of R^{1,3} inside R^{2,4}.  Basis of R^{2,4}:
#     index 0: e_plus (+1), 1: gamma_0 (+1), 2: e_minus (-1), 3,4,5: gamma_1..3
#     (-1).  n0 = (e_plus + e_minus)/2, ninf = e_plus - e_minus, so that
#     n0^2 = ninf^2 = 0 and <n0, ninf> = +1, the convention under which
#     X(x) = n0 + x - (1/2) Q(x) ninf is null (T9, Thm. 4.2).
SQC = (1, 1, -1, -1, -1, -1)
EP, G0, EM, G1, G2, G3 = [vec([1 if j == i else 0 for j in range(6)])
                          for i in range(6)]
N0 = cscal(F(1, 2), g.add(EP, EM))
NINF = g.sub(EP, EM)


def dotc(x, y):
    z = anti(x, y, SQC)
    return z.get((), ZERO) * g.qi(F(1, 2))


g.check("prop:vacuummanifold(1): the null basis: n0^2 = 0, ninf^2 = 0, "
        "<n0, ninf> = 1 exactly",
        g.is_zero(g.mul(N0, N0, SQC)) and g.is_zero(g.mul(NINF, NINF, SQC))
        and dotc(N0, NINF) == ONE)


def point(x):
    """X(x) = n0 + x - (1/2) Q(x) ninf for x = (t, x1, x2, x3) rational."""
    xv = g.add(cscal(x[0], G0), cscal(x[1], G1), cscal(x[2], G2), cscal(x[3], G3))
    Q = dotc(xv, xv)
    return g.add(N0, xv, cscal(g.qi(F(-1, 2)) * Q, NINF)), Q


POINTS = [(F(0), F(0), F(0), F(0)), (F(1), F(0), F(0), F(0)),
          (F(2), F(1), F(0), F(0)), (F(1), F(1), F(0), F(0)),
          (F(3, 2), F(-1), F(2), F(1, 3)), (F(-5), F(2), F(7, 4), F(-1))]
ok = True
Qs = []
for x in POINTS:
    X, Q = point(x)
    Qs.append(Q.re)
    ok = ok and dotc(X, X) == ZERO and g.is_zero(g.mul(X, X, SQC)) and not g.is_zero(X)
g.check("prop:vacuummanifold(1): on six rational points with Q(x) taking "
        "timelike, null and spacelike values, <X(x), X(x)> = 0 computed "
        "from the inner product, X(x)^2 = 0 in the algebra, and X(x) != 0: "
        "every point is a nonzero nilpotent, hence non-invertible",
        ok and any(q > 0 for q in Qs) and any(q < 0 for q in Qs) and 0 in Qs)
# the slot coefficient is forced: with coefficient c in place of -1/2 the
# square is Q(x)(1 + 2c), nonzero for Q != 0 unless c = -1/2
ok = True
for c in (F(0), F(1), F(-1), F(1, 2)):
    xv = G0
    Xc = g.add(N0, xv, cscal(c, NINF))          # Q(gamma_0) = 1
    ok = ok and dotc(Xc, Xc) == g.qi(1 + 2 * c) and dotc(Xc, Xc) != ZERO
g.check("prop:vacuummanifold(1): with any other slot coefficient c the "
        "square is Q(x)(1 + 2c) != 0: the nullity is a property of the "
        "embedding, not of the point", ok)

# C2. The Fock model of Cl(2,4)_C on the exterior algebra of W = span(w1,w2,w3)
#     (dimension 8), with c(w_i) = wedge and c(w'_i) = contraction, which is
#     the Clifford relation for <w_i, w'_j> = delta_ij / 2.  Basis of R^{2,4}
#     as in C1; Witt pairs: (e_plus, e_minus) -> w1, w1'; (gamma_0, gamma_1)
#     -> w2, w2'; (gamma_2, gamma_3) complexified -> w3, w3'.
SUBSETS = [frozenset(s) for k in range(4) for s in combinations(range(3), k)]
IDX = {S: i for i, S in enumerate(SUBSETS)}


def wedge_mat(i):
    M = [[ZERO] * 8 for _ in range(8)]
    for S in SUBSETS:
        if i in S:
            continue
        sign = (-1) ** len([j for j in S if j < i])
        M[IDX[frozenset(S | {i})]][IDX[S]] = g.qi(sign)
    return M


def contract_mat(i):
    M = [[ZERO] * 8 for _ in range(8)]
    for S in SUBSETS:
        if i not in S:
            continue
        pos = sorted(S).index(i)
        M[IDX[frozenset(S - {i})]][IDX[S]] = g.qi((-1) ** pos)
    return M


def madd(*Ms):
    return [[sum((M[r][c] for M in Ms), ZERO) for c in range(8)] for r in range(8)]


def mscal(c, M):
    c = g.qi(c)
    return [[c * v for v in row] for row in M]


def mmul(A, B):
    return g.field_mat_mul(A, B)


def mzero(M):
    return all(not v for row in M for v in row)


CW = [wedge_mat(i) for i in range(3)]        # c(w_i)
CWP = [contract_mat(i) for i in range(3)]    # c(w'_i)
# ambient basis vectors as operators:  e = w + w' for a real pair with
# w = (e_a + e_b)/2, w' = (e_a - e_b)/2  (e_a^2 = +1, e_b^2 = -1):
#   e_a = w + w',  e_b = w - w'
# complex pair on (gamma_2, gamma_3): w3 = (g2 + i g3)/2, w3' = -(g2 - i g3)/2:
#   g2 = w3 - w3',  g3 = -i (w3 + w3')
C_EP = madd(CW[0], CWP[0])
C_EM = madd(CW[0], mscal(-1, CWP[0]))
C_G0 = madd(CW[1], CWP[1])
C_G1 = madd(CW[1], mscal(-1, CWP[1]))
C_G2 = madd(CW[2], mscal(-1, CWP[2]))
C_G3 = mscal(g.qi(0, -1), madd(CW[2], CWP[2]))
CBASIS = [C_EP, C_G0, C_EM, C_G1, C_G2, C_G3]
ID8 = [[ONE if r == c else ZERO for c in range(8)] for r in range(8)]

ok = True
for a in range(6):
    for b in range(6):
        ac = madd(mmul(CBASIS[a], CBASIS[b]), mmul(CBASIS[b], CBASIS[a]))
        target = mscal(2 * SQC[a], ID8) if a == b else [[ZERO] * 8 for _ in range(8)]
        ok = ok and ac == target
g.check("prop:vacuummanifold(2): the Fock model: wedge and contraction on "
        "Lambda W (dim 8) realise the six ambient generators with "
        "{c(e_a), c(e_b)} = 2 g_ab exactly (36 products): Cl(2,4)_C acts "
        "on the three-mode Fock space, T9's Thm. 3.1 re-verified", ok)


def c_of(x):
    """Operator of a vector x (blade-engine element) in the Fock model."""
    M = [[ZERO] * 8 for _ in range(8)]
    for a in range(6):
        coef = x.get((a,), ZERO)
        if coef:
            M = madd(M, mscal(coef, CBASIS[a]))
    return M


def kernel_dim(M):
    return len(g.field_kernel(M))


EVEN = [IDX[S] for S in SUBSETS if len(S) % 2 == 0]
ODD = [IDX[S] for S in SUBSETS if len(S) % 2 == 1]


def restrict_cols(M, cols):
    return [[row[c] for c in cols] for row in M]


ok = True
lines = []
for x in POINTS:
    X, Q = point(x)
    CX = c_of(X)
    ok = ok and mzero(mmul(CX, CX))
    ok = ok and kernel_dim(CX) == 4
    # kernel on the twistor half T = Lambda^even W (columns EVEN)
    kT = g.field_kernel(restrict_cols(CX, EVEN))
    kTp = g.field_kernel(restrict_cols(CX, ODD))
    ok = ok and len(kT) == 2 and len(kTp) == 2
    lines.append(kT)
g.check("prop:vacuummanifold(2): for each of the six points, c(X(x)) is "
        "nilpotent (square zero) with kernel of dimension 4 on the Fock "
        "module and exactly 2 on the twistor half T: the point's null "
        "vector annihilates a LINE of twistors, the incidence line, not a "
        "single vacuum", ok)


def kernel_of_state(state_even):
    """Annihilator W_Z = {v in C^6 : c(v) Z = 0} of a twistor Z (as a list of
    8 coefficients); returns its dimension."""
    Z = [[v] for v in state_even]
    cols = []
    for a in range(6):
        cols.append([row[0] for row in mmul(CBASIS[a], Z)])
    # matrix with columns c(e_a) Z, unknowns v_a
    M = [[cols[a][r] for a in range(6)] for r in range(8)]
    return g.field_kernel(M)


def embed_even(vec4):
    out = [ZERO] * 8
    for k, col in enumerate(EVEN):
        out[col] = vec4[k]
    return out


ok = True
for kT in lines:
    Z1, Z2 = embed_even(kT[0]), embed_even(kT[1])
    W1, W2 = kernel_of_state(Z1), kernel_of_state(Z2)
    ok = ok and len(W1) == 3 and len(W2) == 3            # both pure: T9 Thm 5.3
    # the two annihilators are distinct 3-planes: their span has dimension > 3
    ok = ok and g.field_rank(W1 + W2) > 3
    # and a generic combination Z1 + Z2 is again pure with a third annihilator
    Z3 = [a + b for a, b in zip(Z1, Z2)]
    W3 = kernel_of_state(Z3)
    ok = ok and len(W3) == 3 and g.field_rank(W1 + W3) > 3
g.check("prop:vacuummanifold(2): on each incidence line, two independent "
        "twistors and their sum are each Fock vacua (annihilator of "
        "dimension 3, T9 Thm. 5.3) with pairwise DISTINCT annihilator "
        "3-planes: a point is a projective line of distinct vacua whose systems share "
        "its null vector, not one vacuum", ok)

# each point's null vector lies in every annihilator on its line
ok = True
for x, kT in zip(POINTS, lines):
    X, Q = point(x)
    xcoef = [X.get((a,), ZERO) for a in range(6)]
    for kv in kT:
        Wb = kernel_of_state(embed_even(kv))
        ok = ok and g.field_rank(Wb + [xcoef]) == 3
g.check("prop:vacuummanifold(2): X(x) lies in the annihilator 3-plane of "
        "every twistor on its incidence line (rank of W_Z + X(x) stays 3): "
        "incidence is membership of the point's null vector in the vacuum's "
        "isotropic system", ok)

# distinct points give distinct incidence lines
ok = True
met, missed = 0, 0
for i in range(len(POINTS)):
    for j in range(i + 1, len(POINTS)):
        rk = g.field_rank(lines[i] + lines[j])
        d = [a - b for a, b in zip(POINTS[i], POINTS[j])]
        Qd = d[0] ** 2 - d[1] ** 2 - d[2] ** 2 - d[3] ** 2
        ok = ok and rk >= 3                       # distinct lines
        ok = ok and (rk == 3) == (Qd == 0)        # meet iff null-separated
        if Qd == 0:
            met += 1
        else:
            missed += 1
ok_ip = True
for i in range(len(POINTS)):
    for j in range(i + 1, len(POINTS)):
        Xi, _ = point(POINTS[i])
        Xj, _ = point(POINTS[j])
        d = [a - b for a, b in zip(POINTS[i], POINTS[j])]
        Qd = d[0] ** 2 - d[1] ** 2 - d[2] ** 2 - d[3] ** 2
        ok_ip = ok_ip and dotc(Xi, Xj) == g.qi(F(-1, 2) * Qd)
g.check("prop:vacuummanifold(2): <X(x), X(y)> = -(1/2) Q(x - y) on all fifteen "
        "pairs, computed from the inner product: null separation is "
        "orthogonality of the null vectors (the shared-vacuum half is the "
        "neighbouring rank check)", ok_ip)
g.check("prop:vacuummanifold(2): the six points give pairwise distinct "
        "incidence lines (the point-to-line map is injective on the sample), "
        "and two lines MEET exactly when the two points are null-separated "
        "(%d meeting pairs, %d skew pairs): the incidence geometry of T9's "
        "chart theorem" % (met, missed), ok)

# ---------------------------------------------------------------------------
# Part D: the laboratory (prop:slowshadow)
# ---------------------------------------------------------------------------

# D1. Covariant first-order operators.  Unknown: A = (A^0..A^3), four elements
#     of Cl(1,3) (64 real unknowns), with the covariance condition
#     R^{-1} A^mu R = M(R)^mu_nu A^nu for rotors R, M(R) being the vector
#     matrix defined by R^{-1} gamma^mu R = M(R)^mu_nu gamma^nu.
#     Solutions contain gamma^mu (by definition of M) and gamma^mu I (I the
#     pseudoscalar, central in the even subalgebra).  The script computes the
#     kernel of the stacked conditions for six rational rotors: an UPPER bound
#     on the covariant space, which the two known solutions saturate.
SQ = g.sig(1, 3)
BL = g.all_blades(4)
GAM = [vec([1 if j == i else 0 for j in range(4)]) for i in range(4)]
PS = g.mul(g.mul(GAM[0], GAM[1], SQ), g.mul(GAM[2], GAM[3], SQ), SQ)   # I


def rotor(i, j, a, b):
    """R = a + b e_i e_j (a rational rotor when a^2 - (e_i e_j)^2 b^2 = 1)."""
    return g.add({(): g.qi(a)}, cscal(b, g.mul(GAM[i], GAM[j], SQ)))


def inverse_rotor(R):
    Rt = g.reverse(R)
    nrm = g.mul(R, Rt, SQ)
    assert is_scalar(nrm, 1), nrm
    return Rt


ROTORS = [rotor(0, 1, F(5, 4), F(3, 4)), rotor(0, 2, F(13, 12), F(5, 12)),
          rotor(0, 3, F(17, 15), F(8, 15)), rotor(1, 2, F(3, 5), F(4, 5)),
          rotor(1, 3, F(5, 13), F(12, 13)), rotor(2, 3, F(8, 17), F(15, 17))]


def coords(x):
    return [x.get(b, ZERO) for b in BL]


def vector_matrix(R):
    Ri = inverse_rotor(R)
    M = []
    for mu in range(4):
        y = g.mul(g.mul(Ri, GAM[mu], SQ), R, SQ)
        row = [y.get((nu,), ZERO) for nu in range(4)]
        assert all(len(b) == 1 for b in y)          # stays a vector
        M.append(row)
    return M


# build the linear map A -> (R^{-1} A^mu R - M^mu_nu A^nu) for each rotor;
# unknown vector: 64 coordinates (mu, blade)
def condition_rows(R):
    Ri = inverse_rotor(R)
    M = vector_matrix(R)
    rows = []
    # columns indexed by (mu, blade b): basis element A with A^mu = b
    for out_mu in range(4):
        for out_b in BL:
            row = []
            for mu in range(4):
                for b in BL:
                    Ab = {b: ONE}
                    # contribution of unit A^mu = b to the out_mu component
                    val = ZERO
                    if mu == out_mu:
                        conj = g.mul(g.mul(Ri, Ab, SQ), R, SQ)
                        val = val + conj.get(out_b, ZERO)
                    val = val - M[out_mu][mu] * (ONE if b == out_b else ZERO)
                    row.append(val)
            rows.append(row)
    return rows


ROWS = []
for R in ROTORS:
    ROWS.extend(condition_rows(R))
KER = g.field_kernel(ROWS)
# the two known solutions as 64-vectors
def sol_vec(mult):
    out = []
    for mu in range(4):
        y = g.mul(GAM[mu], mult, SQ)
        out.extend(coords(y))
    return out


S1 = sol_vec({(): ONE})
S2 = sol_vec(PS)
g.check("prop:slowshadow(1) / lem:vectorderivative: the space of "
        "constant-coefficient first-order operators A^mu d_mu covariant "
        "under six rational Spin(1,3) rotors (three boosts, three rotations) "
        "has dimension exactly 2 over the Gaussian rationals, spanned by "
        "gamma^mu and gamma^mu I: the vector derivative is unique up to the "
        "invertible constant factor a + bI",
        len(KER) == 2 and g.field_rank([S1, S2]) == 2
        and g.field_rank(KER + [S1, S2]) == 2)
g.check("lem:vectorderivative: the pseudoscalar I anticommutes with all four "
        "generators, so gamma^mu (a + bI) = (a - bI) gamma^mu, checked on "
        "three (a, b) instances for every mu",
        all(g.anticommutes(PS, GAM[m], SQ) for m in range(4))
        and all(g.eq(g.mul(GAM[m], g.add({(): g.qi(a)}, cscal(b, PS)), SQ),
                     g.mul(g.add({(): g.qi(a)}, cscal(-b, PS)), GAM[m], SQ))
                for m in range(4)
                for a, b in ((F(1), F(0)), (F(2), F(3)), (F(-1, 2), F(5)))))
g.check("lem:vectorderivative: a + bI is invertible for (a,b) != 0: "
        "(a + bI)(a - bI) = a^2 + b^2 since I^2 = -1 in Cl(1,3)",
        is_scalar(g.mul(PS, PS, SQ), -1)
        and all(is_scalar(g.mul(g.add({(): g.qi(a)}, cscal(b, PS)),
                                g.add({(): g.qi(a)}, cscal(-b, PS)), SQ), a * a + b * b)
                for a, b in ((F(1), F(0)), (F(2), F(3)), (F(-1, 2), F(5)))))

# D2. The time direction gamma_0, the boost plane, and the spin plane.
B01 = g.mul(GAM[0], GAM[1], SQ)          # boost plane bivector
ISIG3 = g.mul(GAM[2], GAM[1], SQ)        # Hestenes' i sigma_3 = gamma_2 gamma_1
g.check("prop:slowshadow(3): the boost plane gamma_0 gamma_1 squares to +1 "
        "(hyperbolic: NOT an imaginary unit), while the spin plane "
        "gamma_2 gamma_1 squares to -1, commutes with gamma_0 and "
        "anticommutes with gamma_1, gamma_2: the imaginary unit is a "
        "spacelike plane in the rest space of the time direction gamma_0, "
        "not the boost plane",
        is_scalar(g.mul(B01, B01, SQ), 1) and is_scalar(g.mul(ISIG3, ISIG3, SQ), -1)
        and g.commutes(ISIG3, GAM[0], SQ) and g.anticommutes(ISIG3, GAM[1], SQ)
        and g.anticommutes(ISIG3, GAM[2], SQ))
# the spin plane is not unique: every rotation of it in the rest space is
# another imaginary unit commuting with gamma_0 (the representation freedom)
R13 = rotor(1, 3, F(5, 13), F(12, 13))
ISIG_ROT = g.mul(g.mul(g.reverse(R13), ISIG3, SQ), R13, SQ)
g.check("prop:slowshadow(3): a rest-space rotation carries the spin plane to "
        "another bivector squaring to -1 and commuting with gamma_0, distinct "
        "from the first: the choice of plane within the rest space is "
        "representation freedom; neither the plane nor gamma_0 is fixed by "
        "the series, only an orientation bit",
        is_scalar(g.mul(ISIG_ROT, ISIG_ROT, SQ), -1)
        and g.commutes(ISIG_ROT, GAM[0], SQ) and not g.eq(ISIG_ROT, ISIG3))

# D3. The Klein-Gordon square of the Dirac-Hestenes equation
#     grad psi (I sigma_3) = m psi gamma_0:  the algebra needed is
#     (I sigma_3)^{-1} = -I sigma_3,  gamma_0 (I sigma_3) gamma_0 = I sigma_3,
#     so grad^2 psi = -m^2 psi, i.e. every component obeys (box + m^2) psi = 0.
g.check("prop:slowshadow(2): (I sigma_3)^{-1} = -I sigma_3 and gamma_0 "
        "(I sigma_3) gamma_0 = I sigma_3, so applying the vector derivative "
        "twice to the Dirac-Hestenes equation gives grad^2 psi = -m^2 psi: "
        "each component is a Klein-Gordon field of the same mass, the mass "
        "the dictionary of T11 prices",
        is_scalar(g.mul(ISIG3, cscal(-1, ISIG3), SQ), 1)
        and g.eq(g.mul(g.mul(GAM[0], ISIG3, SQ), GAM[0], SQ), ISIG3))
# grad^2 = box: the symmetric part of gamma^mu gamma^nu is the metric
g.check("prop:slowshadow(2): {gamma^mu, gamma^nu} = 2 eta^{mu nu} on all 16 "
        "pairs, so grad^2 = eta^{mu nu} d_mu d_nu = box",
        all(is_scalar(anti(GAM[m], GAM[n], SQ), 2 * SQ[m] if m == n else 0)
            for m in range(4) for n in range(4)))

# D4. The Pauli identity (sigma.a)(sigma.b) = a.b + i sigma.(a x b) in Cl(3,0),
#     the algebraic input of the g = 2 extraction: a b = a.b + a ^ b and
#     a ^ b = I3 (a x b) for the unit pseudoscalar I3 of the rest space.
SQ3 = g.sig(3, 0)
S = [vec([1 if j == i else 0 for j in range(3)]) for i in range(3)]
I3 = g.mul(g.mul(S[0], S[1], SQ3), S[2], SQ3)


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


ok = is_scalar(g.mul(I3, I3, SQ3), -1)
for a in ([F(1), F(2), F(3)], [F(0), F(-1), F(5, 2)], [F(7), F(0), F(0)]):
    for b in ([F(2), F(-1), F(1)], [F(1, 3), F(4), F(-2)], [F(0), F(0), F(1)]):
        av, bv = vec(a), vec(b)
        prod = g.mul(av, bv, SQ3)
        adotb = sum(x * y for x, y in zip(a, b))
        expect = g.add({(): g.qi(adotb)} if adotb else {}, g.mul(I3, vec(cross(a, b)), SQ3))
        ok = ok and g.eq(prod, expect)
g.check("prop:slowshadow(4): the Pauli identity a b = a.b + I3 (a x b) holds "
        "exactly on nine rational vector pairs in Cl(3,0), with I3^2 = -1: "
        "the algebraic input whose antisymmetric part doubles the spin "
        "coupling against the orbital one (g = 2) in the imported descent",
        ok)

# ---------------------------------------------------------------------------
# Part E: the measure (prop:born, lem:current)
# ---------------------------------------------------------------------------

# Dirac matrices (Dirac representation) over the Gaussian rationals.
def m4(rows):
    return [[g.qi(*v) if isinstance(v, tuple) else g.qi(v) for v in r] for r in rows]


G = [m4([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]),
     m4([[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]]),
     m4([[0, 0, 0, (0, -1)], [0, 0, (0, 1), 0], [0, (0, 1), 0, 0], [(0, -1), 0, 0, 0]]),
     m4([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])]
ETA = (1, -1, -1, -1)
ID4 = m4([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


def mm(A, B):
    return g.field_mat_mul(A, B)


def msum(*Ms):
    return [[sum((M[r][c] for M in Ms), ZERO) for c in range(len(Ms[0][0]))]
            for r in range(len(Ms[0]))]


def msc(c, M):
    c = g.qi(c)
    return [[c * v for v in row] for row in M]


def dagger(M):
    return [[M[c][r].conj() for c in range(len(M))] for r in range(len(M[0]))]


g.check("lem:current: the Dirac matrices satisfy {gamma^mu, gamma^nu} = "
        "2 eta^{mu nu} on all 16 pairs, gamma^0 is Hermitian and gamma^k "
        "anti-Hermitian (so gamma^0 gamma^mu gamma^0 = gamma^mu dagger)",
        all(msum(mm(G[a], G[b]), mm(G[b], G[a])) == msc(2 * ETA[a] if a == b else 0, ID4)
            for a in range(4) for b in range(4))
        and dagger(G[0]) == G[0]
        and all(dagger(G[k]) == msc(-1, G[k]) for k in (1, 2, 3)))


def slash(p):
    return msum(*[msc(ETA[mu] * p[mu], G[mu]) for mu in range(4)])


MASS = F(5)
# rational points of the mass shell p^2 = 25 (both energy signs), from the
# Pythagorean quadruples 13^2 = 5^2 + 12^2, 13^2 = 5^2 + 3^2 + 4^2 + ... etc.
SHELL = [(F(5), F(0), F(0), F(0)), (F(-5), F(0), F(0), F(0)),
         (F(13), F(12), F(0), F(0)), (F(13), F(0), F(-12), F(0)),
         (F(-13), F(0), F(0), F(12)), (F(13), F(36, 5), F(48, 5), F(0)),
         (F(7), F(2), F(4), F(2)), (F(-7), F(-2), F(4), F(2)),
         (F(9), F(4), F(6), F(2)), (F(11), F(4), F(4), F(-8)),
         (F(-9), F(-4), F(6), F(2)), (F(15), F(10), F(-10), F(0))]
g.check("lem:current: the twelve chosen momenta lie on the mass shell "
        "p^2 = m^2 = 25 exactly (both energy signs represented)",
        all(p[0] ** 2 - p[1] ** 2 - p[2] ** 2 - p[3] ** 2 == MASS ** 2 for p in SHELL)
        and any(p[0] < 0 for p in SHELL))


def shell_spinors(p):
    """Basis of ker(pslash - m): the plane-wave solutions with momentum p."""
    M = msum(slash(p), msc(-MASS, ID4))
    return g.field_kernel(M)


SPIN = {p: shell_spinors(p) for p in SHELL}
g.check("lem:current: ker(pslash - m) is two-dimensional at every chosen "
        "momentum (two spin states), so the sample of solutions is complete",
        all(len(v) == 2 for v in SPIN.values()))


def bar(u):
    """ubar = u^dagger gamma^0, as a row."""
    row = [v.conj() for v in u]
    return [sum((row[r] * G[0][r][c] for r in range(4)), ZERO) for c in range(4)]


# unknowns: Gamma^mu, four 4x4 complex matrices = 64 complex unknowns,
# indexed (mu, r, c).  Condition for conservation on all solutions:
#   (p - p')_mu ubar Gamma^mu v = 0   for all on-shell p, p', u in ker(pslash-m),
#   v in ker(p'slash - m)  (the cross terms of d_mu J^mu between plane waves;
#   the diagonal terms p = p' vanish identically).
def lower(p):
    return [ETA[mu] * p[mu] for mu in range(4)]


ROWS_J = []
for p in SHELL:
    for pp in SHELL:
        if p == pp:
            continue
        q = [a - b for a, b in zip(lower(p), lower(pp))]
        for u in SPIN[p]:
            ub = bar(u)
            for v in SPIN[pp]:
                row = []
                for mu in range(4):
                    for r in range(4):
                        for c in range(4):
                            row.append(g.qi(q[mu]) * ub[r] * v[c])
                ROWS_J.append(row)
KER_J = g.field_kernel(ROWS_J)
gamma_vec = []
for mu in range(4):
    for r in range(4):
        for c in range(4):
            gamma_vec.append(G[mu][r][c])
g.check("lem:current: the space of constant sesquilinear currents "
        "psibar Gamma^mu psi conserved on every solution (%d exact linear "
        "conditions from the %d-momentum sample) is ONE-dimensional over the "
        "Gaussian rationals and is spanned by Gamma^mu = gamma^mu: the "
        "Dirac current is the unique conserved constant sesquilinear current, "
        "up to scale" % (len(ROWS_J), len(SHELL)),
        len(KER_J) == 1 and g.field_rank(KER_J + [gamma_vec]) == 1)
# and it IS conserved: the same condition holds for gamma^mu on every sample
# pair (checked directly, not via the kernel), since ubar pslash = m ubar and
# p'slash v = m v
g.check("lem:current: on every sample pair, (p - p')_mu ubar gamma^mu v = "
        "ubar (pslash - p'slash) v = (m - m) ubar v = 0 exactly: the Dirac "
        "current is conserved",
        all(not sum((g.qi(q) * val for q, val in
                     zip([a - b for a, b in zip(lower(p), lower(pp))],
                         [sum((bar(u)[r] * G[mu][r][c] * v[c] for r in range(4)
                                for c in range(4)), ZERO) for mu in range(4)])), ZERO)
            for p in SHELL for pp in SHELL if p != pp
            for u in SPIN[p] for v in SPIN[pp]))
# positivity: J^0 = psi^dagger psi
ok = True
for psi in ([g.qi(1, 2), g.qi(0, -1), g.qi(3), g.qi(1, 1)],
            [g.qi(0), g.qi(2, 5), g.qi(-1), g.qi(0)],
            [g.qi(0), g.qi(0), g.qi(0), g.qi(0)]):
    ub = bar(psi)
    J0 = sum((ub[r] * G[0][r][c] * psi[c] for r in range(4) for c in range(4)), ZERO)
    J0s = sum((v * v.conj() for v in psi), ZERO)
    ok = ok and J0 == J0s and J0.im == 0 and J0.re >= 0 and (J0.re == 0) == all(not v for v in psi)
g.check("prop:born / lem:current: J^0 = psibar gamma^0 psi = psi^dagger psi "
        "is a sum of squared moduli, positive and zero only on the zero "
        "state, on exact instances", ok)

# E2. Indifference on an exact orbit: the weight vectors invariant under ALL
#     transpositions of n components form a ONE-dimensional space (the uniform
#     vector), while invariance under a proper subgroup (one transposition on
#     four components) leaves a THREE-dimensional space: the check
#     discriminates "invariant under the full exact orbit" from "invariant
#     under some symmetry", which is the distinction prop:born rests on.
def invariant_dim(n, transpositions):
    rows = []
    for (i, j) in transpositions:
        row = [F(0)] * n
        row[i], row[j] = F(1), F(-1)          # w_i = w_j
        rows.append([g.qi(v) for v in row])
    ker = g.field_kernel(rows)
    return len(ker), ker


ok = True
for n in (2, 3, 4, 5):
    dim, ker = invariant_dim(n, [(i, i + 1) for i in range(n - 1)])
    ok = ok and dim == 1 and all(v == ker[0][0] for v in ker[0])
g.check("prop:born: on n = 2, 3, 4, 5 equal-norm components the weight vectors "
        "invariant under all transpositions form a one-dimensional space, "
        "the uniform assignment: indifference on an exact orbit forces "
        "equality", ok)
dim_sub, _ = invariant_dim(4, [(0, 1)])
dim_two, _ = invariant_dim(4, [(0, 1), (2, 3)])
# a transitive proper subgroup whose relation set is NOT the one used above:
# the Klein four-group {e, (01)(23), (02)(13)}, whose orbit graph is the
# 4-cycle 0-1-3-2-0 rather than the path 0-1-2-3
dim_klein, _ = invariant_dim(4, [(0, 1), (2, 3), (0, 2), (1, 3)])
g.check("prop:born: under an INTRANSITIVE subgroup the conclusion fails: one "
        "transposition on four components leaves a three-dimensional "
        "invariant space and two disjoint transpositions a two-dimensional "
        "one (one dimension per orbit), while the transitive Klein four-group "
        "leaves one dimension: equality is forced by transitivity on the "
        "components, which is what an exact orbit supplies",
        dim_sub == 3 and dim_two == 2 and dim_klein == 1)

# E3. Fine-graining: a state with rational squared amplitudes 9/25, 16/25 is
#     rewritten as an equal-amplitude superposition of 25 constituents (9 in
#     branch A, 16 in branch B); uniform weight on the constituents returns
#     the squared norms on the branches.  This is the construction, exhibited;
#     the paper isolates its additivity presupposition.
ok = True
for (a, b) in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17))):
    N = (a * a + b * b)
    ok = ok and N == 1
    na, nb = (a * a).numerator, (b * b).numerator
    den = (a * a).denominator
    ok = ok and nb * 1 == (b * b) * den and na + nb == den
    weights = [F(1, den)] * den
    wA = sum(weights[:na])
    wB = sum(weights[na:])
    ok = ok and wA == a * a and wB == b * b
g.check("prop:born: fine-graining on three rational instances: equal weight "
        "on the constituents adds up to the squared norms on the branches "
        "(the step whose additivity presupposition the paper isolates)", ok)


# ---------------------------------------------------------------------------
# Part B (second part): the third constant (lem:speed, fact:cone). The c-placement script of 2026-09-07, wrapped; the component count made a union-find computation at v1.8.
# ---------------------------------------------------------------------------

def part_B2():
    _RETAG = [
        ('cone (', 'fact:cone ('),
        ('(', 'lem:speed(iv) ('),
        ('Cl(1,1)', 'lem:speed(iii): Cl(1,1)'),
        ('f+ =', 'lem:speed(iii): f+ ='),
        ('the boost bivector', 'lem:speed(iii): the boost bivector'),
        ('R R~', 'lem:speed(iii): R R~'),
        ('R f+', 'lem:speed(iii): R f+'),
        ('the same rotor', 'lem:speed(iii): the same rotor'),
        ('coordinate velocity', 'lem:speed(iii): coordinate velocity'),
        ('the null lines', 'lem:speed(iii): the null lines'),
        ('the opposite rotor', 'lem:speed(iii): the opposite rotor'),
        ('det of the', 'lem:speed (units): det of the'),
        ('no monomial', 'lem:speed (units): no monomial'),
        ('Planck', 'lem:speed (units): Planck'),
        ('Q_c / c^2', 'lem:speed(i): Q_c / c^2'),
        ('at c = infinity', 'lem:speed(i): at c = infinity'),
        ('null pair', 'lem:speed(ii): null pair'),
        ('the three planes', 'lem:speed(ii): the three planes'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)
    from itertools import product, combinations, permutations

    # ---------------------------------------------------------------------------
    # helpers: exact quadratic forms on coordinate vectors
    # ---------------------------------------------------------------------------

    def Qform(p, q):
        sq = g.sig(p, q)
        return lambda x: sum(F(s) * F(xi) * F(xi) for s, xi in zip(sq, x))


    def Bform(p, q):
        sq = g.sig(p, q)
        return lambda x, y: sum(F(s) * F(xi) * F(yi) for s, xi, yi in zip(sq, x, y))


    def segment_min_positive(u, v, B):
        """True iff Q((1-t)u + t v) > 0 for all t in [0, 1], decided exactly.
        Q along the segment is the quadratic a t^2 + b t + c with
        a = Q(v-u), b = 2 B(u, v-u), c = Q(u)."""
        d = [F(vi) - F(ui) for ui, vi in zip(u, v)]
        a, b, c = B(d, d), 2 * B(u, d), B(u, u)
        vals = [c, a + b + c]
        if a > 0:
            t = -b / (2 * a)
            if 0 < t < 1:
                vals.append(a * t * t + b * t + c)
        return min(vals) > 0


    def path_positive(points, B):
        return all(segment_min_positive(points[i], points[i + 1], B) for i in range(len(points) - 1))


    # ---------------------------------------------------------------------------
    # Part A: connectedness of {Q > 0} by signature
    # ---------------------------------------------------------------------------
    print("\nPart A: the sign-definite cones and the arrow")

    # A rational sample of timelike points in (p, q): positive part a, negative
    # part b with |a|^2 > |b|^2, drawn from a fixed small grid so the checks are
    # deterministic and exact.
    GRID = [F(-2), F(-1), F(0), F(1), F(2)]


    def timelike_points(p, q, Q, limit=40):
        out = []
        for coords in product(GRID, repeat=p + q):
            if Q(coords) > 0 and any(coords):
                out.append(list(coords))
                if len(out) >= limit:
                    break
        return out


    def components(p, q):
        """Number of classes of a union-find over rational sample points of
        {Q > 0}, two points joined when the straight segment between them is
        certified Q-positive.  The node set is the grid sample together with
        each point's projection onto the positive subspace and the unit
        vectors +-e_1, e_2 (when timelike), so the routes of the lemma's
        deformation retraction are available as chains of segments.  The
        count is computed, not read off p; the sign classes of x_1 are
        returned alongside so the p = 1 separation can be certified."""
        n = p + q
        Q, B = Qform(p, q), Bform(p, q)
        nodes = [tuple(pt) for pt in timelike_points(p, q, Q)]
        extra = [tuple(list(pt[:p]) + [F(0)] * q) for pt in nodes]
        for k in range(min(n, 2)):
            for sgn in (1, -1):
                e = [F(0)] * n
                e[k] = F(sgn)
                extra.append(tuple(e))
        for x in extra:
            if Q(list(x)) > 0 and x not in nodes:
                nodes.append(x)
        parent = list(range(len(nodes)))

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                if find(i) != find(j) and segment_min_positive(list(nodes[i]), list(nodes[j]), B):
                    parent[find(i)] = find(j)
        classes = {}
        for i, x in enumerate(nodes):
            classes.setdefault(find(i), set()).add((x[0] > 0) - (x[0] < 0))
        return len(classes), list(classes.values())


    # The lemma's counts, S^{p-1} components, entered as literals per signature
    # and not computed from p here; the script's count is the union-find above.
    EXPECTED = {(1, 0): 2, (1, 1): 2, (1, 2): 2, (1, 3): 2, (2, 0): 1, (2, 1): 1,
                (2, 2): 1, (3, 1): 1, (3, 2): 1, (0, 3): 0}


    def count_and_certify(p, q):
        """The union-find count, and, when two classes are found, the
        certificate that they are distinct: the sign of x_1 is constant on
        each class and differs between them (Q > 0 forces x_1 != 0 when p = 1,
        and the sign is continuous, so it separates components)."""
        c, signs = components(p, q)
        separated = (c != 2) or (all(len(sg) == 1 for sg in signs) and
                                 set.union(*signs) == {1, -1})
        return c, separated


    for p, q in [(1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 1), (3, 2)]:
        c, sep = count_and_certify(p, q)
        _chk(f"({p},{q}): union-find over {len(timelike_points(p, q, Qform(p, q)))} rational sample points of {{Q > 0}} "
              f"joined by certified segments finds {c} class(es), the lemma's S^{p-1} count being {EXPECTED[(p, q)]}"
              + (", the two classes separated by the sign of x_1" if c == 2 else ""),
              c == EXPECTED[(p, q)] and sep)

    _chk("(0,3): {Q > 0} is empty (no positive direction): Q <= 0 on the whole grid, no sample point, zero classes",
          all(Qform(0, 3)(c) <= 0 for c in product(GRID, repeat=3)) and components(0, 3)[0] == EXPECTED[(0, 3)])

    # T14's causal criterion: some sign-definite cone has two components iff
    # min(p, q) = 1.  {Q < 0} of (p, q) is {Q > 0} of (q, p).
    for p, q in [(1, 3), (3, 1), (2, 2), (1, 1), (2, 1), (1, 4), (2, 3)]:
        (cp, sp), (cm, sm) = count_and_certify(p, q), count_and_certify(q, p)
        splits = (cp == 2) or (cm == 2)
        _chk(f"({p},{q}): {{Q > 0}} has {cp}, {{Q < 0}} has {cm} class(es) by union-find; some cone splits <=> min(p,q) = 1 "
              f"[{splits} vs {min(p, q) == 1}]", sp and sm and splits == (min(p, q) == 1))


    # ---------------------------------------------------------------------------
    # Part B: the null cone determines the form up to scale
    # ---------------------------------------------------------------------------
    print("\nPart B: the cone determines the form")


    def rational_null_vectors(p, q):
        """A spanning family of rational null vectors of signature (p, q):
        e_i +- e_j (i positive, j negative) and the Pythagorean vectors
        3 e_i + 4 e_k +- 5 e_j, 3 e_i +- 4 e_j +- 5 e_l for distinct indices."""
        n = p + q
        pos, neg = range(p), range(p, n)
        out = []

        def vec(d):
            v = [F(0)] * n
            for i, c in d.items():
                v[i] += F(c)
            return v

        for i in pos:
            for j in neg:
                out.append(vec({i: 1, j: 1}))
                out.append(vec({i: 1, j: -1}))
        for i, k in permutations(pos, 2):
            for j in neg:
                out.append(vec({i: 3, k: 4, j: 5}))
                out.append(vec({i: 3, k: 4, j: -5}))
        for j, l in permutations(neg, 2):
            for i in pos:
                out.append(vec({i: 5, j: 3, l: 4}))
                out.append(vec({i: 5, j: 3, l: -4}))
        return out


    for p in range(1, 4):
        for q in range(1, 4):
            n = p + q
            Q = Qform(p, q)
            nulls = rational_null_vectors(p, q)
            assert all(Q(v) == 0 for v in nulls)
            idx = [(i, j) for i in range(n) for j in range(i, n)]
            rows = [[v[i] * v[j] * (1 if i == j else 2) for (i, j) in idx] for v in nulls]
            nullity = len(idx) - g.mat_rank(rows)
            _chk(f"cone ({p},{q}): symmetric forms vanishing on the null cone form a space of dimension {nullity} "
                  f"(Sym^2 has dimension {len(idx)}, {len(nulls)} rational null vectors): the cone determines Q up to scale",
                  nullity == 1)


    # ---------------------------------------------------------------------------
    # Part C: Witt rescaling is the boost (Cl(1,1), exact rapidity)
    # ---------------------------------------------------------------------------
    print("\nPart C: the Witt rescaling is the boost")

    SQ11 = g.sig(1, 1)
    e0, e1 = g.gen(0), g.gen(1)


    def m11(*xs):
        out = xs[0]
        for x in xs[1:]:
            out = g.mul(out, x, SQ11)
        return out


    ONE = g.sc(1)
    _chk("Cl(1,1): e0^2 = +1, e1^2 = -1, e0 e1 = -e1 e0",
          g.eq(m11(e0, e0), ONE) and g.eq(m11(e1, e1), g.sc(-1)) and g.anticommutes(e0, e1, SQ11))
    fp = g.scal(F(1, 2), g.add(e0, e1))
    fm = g.scal(F(1, 2), g.sub(e0, e1))
    _chk("f+ = (e0 + e1)/2 and f- = (e0 - e1)/2 are null with f+ . f- = 1/2 (a Witt pair)",
          g.is_zero(m11(fp, fp)) and g.is_zero(m11(fm, fm)) and g.dot(fp, fm, SQ11) == F(1, 2))

    # Exact hyperbolic functions: lam = mu^2, mu = 2.
    mu = F(2)
    lam = mu * mu
    ch_half, sh_half = (mu + 1 / mu) / 2, (mu - 1 / mu) / 2
    ch, sh = (lam + 1 / lam) / 2, (lam - 1 / lam) / 2
    assert ch * ch - sh * sh == 1 and ch_half ** 2 - sh_half ** 2 == 1
    Bv = m11(e0, e1)
    _chk("the boost bivector B = e0 e1 squares to +1", g.eq(m11(Bv, Bv), ONE))
    R = g.sub(g.scal(ch_half, ONE), g.scal(sh_half, Bv))      # cosh(eta/2) - sinh(eta/2) B
    Rt = g.add(g.scal(ch_half, ONE), g.scal(sh_half, Bv))     # its reverse
    _chk("R R~ = 1 for the rotor R = cosh(eta/2) - sinh(eta/2) B", g.eq(m11(R, Rt), ONE))
    _chk("R f+ R~ = lam f+ and R f- R~ = f-/lam: the rotor rescales the Witt pair (lam = e^eta = 4)",
          g.eq(m11(R, fp, Rt), g.scal(lam, fp)) and g.eq(m11(R, fm, Rt), g.scal(1 / lam, fm)))
    e0b, e1b = m11(R, e0, Rt), m11(R, e1, Rt)
    _chk("the same rotor boosts the frame: R e0 R~ = cosh(eta) e0 + sinh(eta) e1, norms preserved",
          g.eq(e0b, g.add(g.scal(ch, e0), g.scal(sh, e1))) and g.eq(m11(e0b, e0b), ONE) and g.eq(m11(e1b, e1b), g.sc(-1)))
    # Coordinate velocity of the boosted time axis: components (cosh eta, sinh eta)
    # along (e0, e1) = (c t, x), so x/t = c tanh(eta); with c = 1 in the algebra,
    # tanh(eta) = (lam^2 - 1)/(lam^2 + 1) exactly.
    _chk("coordinate velocity of the boosted time axis is tanh(eta) = (lam^2 - 1)/(lam^2 + 1) = 15/17",
          sh / ch == (lam * lam - 1) / (lam * lam + 1) == F(15, 17))
    _chk("the null lines are the fixed lines of every boost: f+ and f- are eigenvectors of Ad_R (the invariant speed)",
          all(g.eq(m11(R, f, Rt), g.scal(c, f)) for f, c in [(fp, lam), (fm, 1 / lam)]))
    Rop = g.add(g.scal(ch_half, ONE), g.scal(sh_half, Bv))
    Ropt = g.sub(g.scal(ch_half, ONE), g.scal(sh_half, Bv))
    _chk("the opposite rotor sign reverses the boost: cosh(eta/2) + sinh(eta/2) B sends f+ -> f+/lam",
          g.eq(m11(Rop, fp, Ropt), g.scal(1 / lam, fp)) and g.eq(m11(Rop, e0, Ropt), g.sub(g.scal(ch, e0), g.scal(sh, e1))))


    # ---------------------------------------------------------------------------
    # Part D: unit closure
    # ---------------------------------------------------------------------------
    print("\nPart D: the three placements close the unit system")


    def det3(M):
        (a, b, c), (d, e, f), (gg, h, i) = [[F(x) for x in r] for r in M]
        return a * (e * i - f * h) - b * (d * i - f * gg) + c * (d * h - e * gg)


    E = [[1, -1, 0],     # c    : L T^-1
         [2, -1, 1],     # hbar : L^2 T^-1 M
         [3, -2, -1]]    # G    : L^3 T^-2 M^-1
    _chk("det of the (c, hbar, G) exponent matrix over (L, T, M) is -2: the three constants fix the three base units",
          det3(E) == -2)
    E2 = E[1:]
    _chk("no monomial in hbar and G alone has the dimension of a length, a time or a mass (each unit row is independent of the hbar, G rows)",
          all(g.mat_rank(g.frac_matrix(E2 + [row])) == 3 for row in ([1, 0, 0], [0, 1, 0], [0, 0, 1])))


    def solve3(M, rhs):
        """Exact solution of M^T x = rhs by Cramer's rule (M 3x3 rational)."""
        MT = [[F(M[j][i]) for j in range(3)] for i in range(3)]
        D = det3(MT)
        sol = []
        for k in range(3):
            Mk = [row[:] for row in MT]
            for r in range(3):
                Mk[r][k] = F(rhs[r])
            sol.append(det3(Mk) / D)
        return sol


    _chk("Planck length: l_P = c^(-3/2) hbar^(1/2) G^(1/2) (exponents solve exactly)",
          solve3(E, [1, 0, 0]) == [F(-3, 2), F(1, 2), F(1, 2)])
    _chk("Planck time t_P = c^(-5/2) hbar^(1/2) G^(1/2) and Planck mass m_P = c^(1/2) hbar^(1/2) G^(-1/2)",
          solve3(E, [0, 1, 0]) == [F(-5, 2), F(1, 2), F(1, 2)] and solve3(E, [0, 0, 1]) == [F(1, 2), F(1, 2), F(-1, 2)])


    # ---------------------------------------------------------------------------
    # Part E: the Galilean limit as degeneration
    # ---------------------------------------------------------------------------
    print("\nPart E: finiteness of c is nondegeneracy")


    def diag(vals):
        n = len(vals)
        return [[F(vals[i]) if i == j else F(0) for j in range(n)] for i in range(n)]


    _chk("Q_c / c^2 = diag(1, -1/c^2, -1/c^2, -1/c^2) has signature (1,3) for c = 1, 10, 1000 (every finite c)",
          all(g.congruence_signature(diag([1, -F(1, c * c), -F(1, c * c), -F(1, c * c)])) == (1, 3, 0) for c in (1, 10, 1000)))
    _chk("at c = infinity the form is diag(1, 0, 0, 0): rank 1, radical the simultaneity hyperplane t = 0 (dimension 3)",
          g.congruence_signature(diag([1, 0, 0, 0])) == (1, 0, 3))


    # ---------------------------------------------------------------------------
    # Part F: Witt, all hyperbolic planes of (1,3) conjugate
    # ---------------------------------------------------------------------------
    print("\nPart F: one invariant ratio for the whole space (Witt)")

    B13 = Bform(1, 3)
    Q13 = Qform(1, 3)


    def complement_signature(n, mvec):
        """Exact signature of the orthogonal complement of span(n, m) in (1,3)."""
        # Solve B(x, n) = B(x, m) = 0 for x in Q^4: a 2x4 homogeneous system.
        sq = g.sig(1, 3)
        rows = [[F(s) * F(c) for s, c in zip(sq, v)] for v in (n, mvec)]
        kern = g.field_kernel(rows)
        assert len(kern) == 2
        G = [[B13(u, v) for v in kern] for u in kern]
        return g.congruence_signature(G)


    pairs = [
        ([F(1), F(1), F(0), F(0)], [F(-1, 2), F(1, 2), F(0), F(0)]),
        ([F(5), F(3), F(4), F(0)], [F(-1, 10), F(3, 50), F(4, 50), F(0)]),
        ([F(13), F(3), F(4), F(12)], [F(-1, 26), F(3, 338), F(4, 338), F(12, 338)]),
    ]
    sgns = []
    for n, mv in pairs:
        hyper = Q13(n) == 0 and Q13(mv) == 0 and B13(n, mv) == -1
        sgn = complement_signature(n, mv)
        sgns.append(sgn)
        _chk(f"null pair n = {[str(x) for x in n]}, m with n.m = -1: hyperbolic plane; complement has signature {sgn} = (0,2)",
              hyper and sgn == (0, 2, 0))
    def plane_rank(pair_a, pair_b):
        return g.mat_rank([list(v) for v in (pair_a[0], pair_a[1], pair_b[0], pair_b[1])])
    distinct = all(plane_rank(pairs[i], pairs[j]) >= 3 for i in range(len(pairs)) for j in range(i + 1, len(pairs)))
    _chk("the three planes are pairwise distinct (their spans differ) and their complements have one signature (0,2), "
         "so by Witt's extension theorem the hyperbolic planes are conjugate under O(1,3): one invariant ratio for the whole space",
          distinct and all(sgn == (0, 2, 0) for sgn in sgns) and len(sgns) == len(pairs) == 3)


part_B2()

# ---------------------------------------------------------------------------
# Part C (second part): the nu = 4 quadric and the orbit test (rem:quadric, fact:cartan). A companion script's Parts H, I, J, wrapped (seeded random Gaussian-rational states); H4, H5 and I4 made substantive at v1.8.
# ---------------------------------------------------------------------------

def part_C2():
    _RETAG = [
        ('H', 'rem:quadric H'),
        ('I', 'rem:quadric I'),
        ('J', 'rem:quadric J'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)
    from itertools import combinations
    import random
    import GA
    from GA import QI
    random.seed(20260907)

    # ---------------------------------------------------------------- Fock module
    def jw(i, S):  return (-1) ** len([j for j in S if j < i])
    def cre(i, st):
        o = {}
        for S, c in st.items():
            if i in S: continue
            T = frozenset(S | {i}); o[T] = o.get(T, QI(0)) + QI(jw(i, S)) * c
        return {S: c for S, c in o.items() if c}
    def ann(i, st):
        o = {}
        for S, c in st.items():
            if i not in S: continue
            T = frozenset(S - {i}); o[T] = o.get(T, QI(0)) + QI(jw(i, T)) * c
        return {S: c for S, c in o.items() if c}
    def sadd(*sts):
        o = {}
        for st in sts:
            for S, c in st.items(): o[S] = o.get(S, QI(0)) + c
        return {S: c for S, c in o.items() if c}
    def sscal(z, st):
        z = z if isinstance(z, QI) else QI(z)
        return {S: z * c for S, c in st.items() if z * c}
    def sneg(st): return sscal(QI(-1), st)
    def seq(x, y):
        ks = set(x) | set(y)
        return all(x.get(k, QI(0)) == y.get(k, QI(0)) for k in ks)
    def bas(nu, even=None):
        out = []
        for k in range(nu + 1):
            if even is not None and k % 2 != (0 if even else 1): continue
            for S in combinations(range(nu), k): out.append(frozenset(S))
        return out
    def ip(x, y):
        t = QI(0)
        for S, c in x.items():
            if S in y: t = t + c.conj() * y[S]
        return t
    def maj(k):
        i, r = divmod(k, 2)
        if r == 0: return lambda st: sadd(ann(i, st), cre(i, st))
        return lambda st: sscal(QI(0, -1), sadd(ann(i, st), sneg(cre(i, st))))
    def corr_raw(psi, nu):
        """M_kl = i <psi| c_k c_l |psi>, psi NOT necessarily normalised."""
        M = [[QI(0)] * (2 * nu) for _ in range(2 * nu)]
        for k in range(2 * nu):
            for l in range(2 * nu):
                if k == l: continue
                M[k][l] = QI(0, 1) * ip(psi, maj(k)(maj(l)(psi)))
        return M
    def msq(M):
        n = len(M)
        return [[sum((M[i][k] * M[k][j] for k in range(n)), QI(0)) for j in range(n)]
                for i in range(n)]
    def is_witt_vacuum(psi, nu):
        """M^2 = -N^4 I with N^2 = <psi|psi>, i.e. the normalised M squares to -I."""
        N2 = ip(psi, psi)
        M2 = msq(corr_raw(psi, nu))
        n = 2 * nu
        return all(M2[i][j] == (-(N2 * N2) if i == j else QI(0))
                   for i in range(n) for j in range(n))

    def rq(lo=-5, hi=5):
        return F(random.randint(lo, hi), random.randint(1, 4))
    def rqi():
        return QI(rq(), rq())
    def rand_even(nu, real=False):
        st = {}
        for S in bas(nu, even=True):
            st[S] = QI(rq()) if real else rqi()
        return {S: c for S, c in st.items() if c}

    # --------------------------------------------------- the Cartan quadric, nu = 4
    def fs(*xs): return frozenset(xs)
    def coef(psi, S): return psi.get(frozenset(S), QI(0))
    def pf4(A):
        """Pfaffian of a 4x4 antisymmetric matrix given as dict {(i,j): a_ij}, i<j."""
        g = lambda i, j: A.get((i, j), QI(0))
        return g(0, 1) * g(2, 3) - g(0, 2) * g(1, 3) + g(0, 3) * g(1, 2)
    def cartan_Q(psi):
        """Q(psi) = psi_0 psi_1234 - Pf(psi_ij) on the even sector of nu = 4."""
        A = {(i, j): coef(psi, (i, j)) for i in range(4) for j in range(i + 1, 4)}
        return coef(psi, ()) * coef(psi, (0, 1, 2, 3)) - pf4(A)


    cand = sadd(sscal(F(3, 5), {fs(): QI(1)}), sscal(F(4, 5), {fs(0, 1, 2, 3): QI(1)}))
    cand2 = sadd(sscal(F(1, 2), {fs(): QI(1)}), sscal(F(1, 2), {fs(0, 1): QI(1)}),
                 sscal(F(1, 2), {fs(2, 3): QI(1)}), sscal(F(1, 2), {fs(0, 2): QI(1)}))
    gauss4 = sadd(sscal(F(9, 25), {fs(): QI(1)}), sscal(F(12, 25), {fs(0, 1): QI(1)}),
                  sscal(F(12, 25), {fs(2, 3): QI(1)}), sscal(F(16, 25), {fs(0, 1, 2, 3): QI(1)}))
    _chk("H1      witness state 1 has Q = 12/25 != 0, so it is no vacuum",
          cartan_Q(cand) == QI(F(12, 25)) and not is_witt_vacuum(cand, 4))
    _chk("H2      witness state 2 has Q = -1/4 != 0, so it is no vacuum",
          cartan_Q(cand2) == QI(F(-1, 4)) and not is_witt_vacuum(cand2, 4))
    _chk("H3      the paired-block state has Q = 144/625 - 144/625 = 0 and IS a vacuum",
          cartan_Q(gauss4) == QI(0) and is_witt_vacuum(gauss4, 4))

    def thouless(A, nu):
        """exp(sum_{i<j} A_ij a_i+ a_j+)|0>, computed exactly (the series terminates)."""
        vac = {fs(): QI(1)}
        def pair_op(st):
            out = {}
            for (i, j), a in A.items():
                if a: out = sadd(out, sscal(a, cre(i, cre(j, st))))
            return out
        total, term, k = dict(vac), dict(vac), 0
        while term:
            k += 1
            term = sscal(QI(F(1, k)), pair_op(term))
            total = sadd(total, term)
        return total

    def on_quadric(psi):
        """The even state with the same psi_0 != 0 and psi_ij as psi and the
        quartic coefficient set to Pf(psi_ij)/psi_0, so that Q = 0 there by
        the defining formula; whether it is a vacuum is then the M^2 test."""
        A = {(i, j): coef(psi, (i, j)) for i in range(4) for j in range(i + 1, 4)}
        out = {S: c for S, c in psi.items() if len(S) < 4}
        q4 = pf4(A) / coef(psi, ())
        if q4: out[fs(0, 1, 2, 3)] = q4
        return out

    # H4: random rational even states, off the quadric (generic) and on it
    #     (scaled Thouless states, states with the quartic coefficient adjusted,
    #     and psi_0 = 0 Slater states): Q != 0  <=>  not a Witt vacuum, both
    #     directions exercised.
    sample = []
    for _ in range(40):
        psi = rand_even(4)
        sample.append(psi)
        if coef(psi, ()):
            sample.append(on_quadric(psi))
    for _ in range(10):
        A = {(i, j): rqi() for i in range(4) for j in range(i + 1, 4)}
        sample.append(sscal(rqi() or QI(1), thouless(A, 4)))
    sample.append(sadd({fs(0, 1): QI(1)}, {fs(0, 2): QI(1)}))     # psi_0 = 0, a Slater determinant
    n_zero = sum(1 for psi in sample if cartan_Q(psi) == QI(0))
    n_nonzero = len(sample) - n_zero
    ok_both = all((cartan_Q(psi) != QI(0)) == (not is_witt_vacuum(psi, 4)) for psi in sample)
    _chk("H4      %d complex-rational even states, %d with Q = 0 and %d with Q != 0: Q != 0 iff not a vacuum, both directions"
          % (len(sample), n_zero, n_nonzero), ok_both and n_zero >= 20 and n_nonzero >= 20)
    # H5: Q = 0 is one condition on the quartic coefficient: a random even state
    #     has Q != 0, and exactly one value of psi_1234 (Pf/psi_0) brings Q to 0.
    ok_h5 = True
    for _ in range(20):
        psi = rand_even(4)
        adj = on_quadric(psi)
        other = dict(adj)
        other[fs(0, 1, 2, 3)] = coef(adj, (0, 1, 2, 3)) + QI(1)
        ok_h5 = ok_h5 and cartan_Q(psi) != QI(0) and cartan_Q(adj) == QI(0) and cartan_Q(other) != QI(0)
    _chk("H5      generically Q != 0, and Q = 0 is one condition on the quartic coefficient: "
          "exactly the value Pf(psi_ij)/psi_0 brings a random even state onto the quadric (20 states)", ok_h5)

    # H6: states ON the quadric are all vacua.  Build them as Thouless states (I2)
    #     and also with psi_0 = 0 (the chart at infinity), where Q = 0 reads Pf = 0.
    inf_vac = sadd({fs(0, 1): QI(1)}, {fs(0, 2): QI(1)})          # a_0+ (a_1+ + a_2+)|0>, Pf = 0
    inf_not = sadd({fs(0, 1): QI(1)}, {fs(2, 3): QI(1)})          # Pf = 1
    _chk("H6      psi_0 = 0, Pf = 0: |12> + |13> is a vacuum (a Slater determinant)",
          cartan_Q(inf_vac) == QI(0) and is_witt_vacuum(inf_vac, 4))
    _chk("H7      psi_0 = 0, Pf = 1 so Q = -1: |12> + |34> is NOT a vacuum (Slater rank two)",
          cartan_Q(inf_not) == QI(-1) and not is_witt_vacuum(inf_not, 4))
    ghz = sadd({fs(): QI(1)}, {fs(0, 1, 2, 3): QI(1)})
    _chk("H8      |0> + |1234| has Q = 1: maximally non-Gaussian, |Q|/N^2 = 1/2",
          cartan_Q(ghz) == QI(1) and ip(ghz, ghz) == QI(2))


    for trial in range(10):
        A = {(i, j): rqi() for i in range(4) for j in range(i + 1, 4)}
        psi = thouless(A, 4)
        ok = (coef(psi, ()) == QI(1)
              and all(coef(psi, (i, j)) == A[(i, j)] for (i, j) in A)
              and coef(psi, (0, 1, 2, 3)) == pf4(A))
        if not ok: break
    _chk("I1      10 random A: exp(A)|0> = |0> + A_ij|ij> + Pf(A)|1234>, exactly", ok)
    _chk("I2      hence Q(exp(A)|0>) = Pf(A) - Pf(A) = 0 on every Thouless state",
          all(cartan_Q(thouless({(i, j): rqi() for i in range(4) for j in range(i + 1, 4)}, 4))
              == QI(0) for _ in range(10)))
    _chk("I3      and every Thouless state is a Witt vacuum by the M^2 test too",
          all(is_witt_vacuum(thouless({(i, j): rqi() for i in range(4)
                                       for j in range(i + 1, 4)}, 4), 4) for _ in range(4)))

    # converse on the affine chart: psi_0 != 0 and Q = 0  =>  psi = psi_0 exp(psi_ij/psi_0)|0>.
    # The states are built from random coefficients with the quartic coefficient
    # adjusted (not from thouless()), Q = 0 is verified by cartan_Q, and the
    # Thouless form is then compared; a control with the quartic coefficient
    # moved has Q != 0 and is not of Thouless form.
    ok = True
    for _ in range(10):
        psi = on_quadric(rand_even(4))
        B = {(i, j): coef(psi, (i, j)) / coef(psi, ()) for i in range(4) for j in range(i + 1, 4)}
        control = dict(psi)
        control[fs(0, 1, 2, 3)] = coef(psi, (0, 1, 2, 3)) + QI(1)
        ok = ok and cartan_Q(psi) == QI(0) and seq(psi, sscal(coef(psi, ()), thouless(B, 4)))
        ok = ok and cartan_Q(control) != QI(0) and not seq(control, sscal(coef(control, ()), thouless(B, 4)))
    _chk("I4      converse on the chart psi_0 != 0: Q = 0 (by cartan_Q) => psi = psi_0 exp(psi_ij/psi_0)|0>, "
          "10 states built on the quadric, with 10 controls off it failing both", ok)

    # nu = 3: the even sector is |0>, |12>, |13>, |23>: NO quartic exists, so every
    # even state with psi_0 != 0 is a Thouless state with nothing to check.
    ok = True
    for _ in range(20):
        psi = rand_even(3)
        if not coef(psi, ()): continue
        A = {(i, j): coef(psi, (i, j)) / coef(psi, ()) for i in range(3) for j in range(i + 1, 3)}
        if not seq(psi, sscal(coef(psi, ()), thouless(A, 3))): ok = False
        if not is_witt_vacuum(psi, 3): ok = False
    _chk("I5      nu = 3: every random even state with psi_0 != 0 is psi_0 exp(A)|0>, a vacuum", ok)
    _chk("I6      nu = 3 even sector has dimension 4 = 1 + C(3,2): no quartic term to constrain",
          len(bas(3, even=True)) == 4 and all(len(S) <= 2 for S in bas(3, even=True)))
    _chk("I7      nu = 4 even sector has dimension 8 = 1 + C(4,2) + 1: the quartic appears",
          len(bas(4, even=True)) == 8 and any(len(S) == 4 for S in bas(4, even=True)))


    def orbit_rank(psi, nu):
        """rank over C of span{psi, c_k c_l psi : k < l} on the even sector."""
        B = bas(nu, even=True)
        rows = [[psi.get(S, QI(0)) for S in B]]
        for k in range(2 * nu):
            for l in range(k + 1, 2 * nu):
                v = maj(k)(maj(l)(psi))
                rows.append([v.get(S, QI(0)) for S in B])
        return GA.field_rank(rows)

    for nu in (2, 3, 4):
        vac = {fs(): QI(1)}
        r = orbit_rank(vac, nu)
        _chk("J1.nu=%d  tangent rank of the vacuum orbit is 1 + nu(nu-1)/2 = %d"
              % (nu, 1 + nu * (nu - 1) // 2), r == 1 + nu * (nu - 1) // 2)
    _chk("J2      nu = 3: rank 4 = dim(even sector): the orbit is OPEN, so it is everything",
          orbit_rank({fs(): QI(1)}, 3) == len(bas(3, even=True)))
    _chk("J3      nu = 4: rank 7 < 8: the vacuum orbit is a hypersurface (the quadric)",
          orbit_rank({fs(): QI(1)}, 4) == 7 < len(bas(4, even=True)))
    _chk("J4      nu = 4: a NON-vacuum (Q != 0) has orbit rank 8: it lies in the open orbit",
          orbit_rank(cand, 4) == 8 and orbit_rank(ghz, 4) == 8)
    _chk("J5      the same rank 7 at a generic point of the quadric (a random Thouless state)",
          orbit_rank(thouless({(i, j): rqi() for i in range(4) for j in range(i + 1, 4)}, 4), 4) == 7)

    # Gaussian unitaries preserve Q.  Pairing rotation on modes (i,j) with (c,s):
    #   |S> -> c|S> + s a_i+ a_j+ |S>   (i,j not in S);   a_i+a_j+|T> -> -s|T> + c a_i+a_j+|T>
    def pair_rot(i, j, c, s, psi):
        out = {}
        for S, z in psi.items():
            if i in S and j in S:
                T = frozenset(S - {i, j})
                P = cre(i, cre(j, {T: QI(1)}))          # = sigma |S>
                sigma = P[S]
                out = sadd(out, sscal(z * sigma, sadd(sscal(-s, {T: QI(1)}), sscal(c, P))))
            elif i not in S and j not in S:
                out = sadd(out, sscal(z, sadd(sscal(c, {S: QI(1)}), sscal(s, cre(i, cre(j, {S: QI(1)}))))))
            else:
                out = sadd(out, {S: z})
        return out
    # hop rotation exp(theta (a_i+ a_j - a_j+ a_i)): rotates the one-occupied subspace
    def hop_rot(i, j, c, s, psi):
        out = {}
        for S, z in psi.items():
            if (i in S) != (j in S):
                src, dst = (j, i) if j in S else (i, j)
                moved = cre(dst, ann(src, {S: QI(1)}))
                sign = QI(1) if dst == i else QI(-1)
                out = sadd(out, sscal(z, sadd(sscal(c, {S: QI(1)}), sscal(sign * s, moved))))
            else:
                out = sadd(out, {S: z})
        return out

    c, s = QI(F(3, 5)), QI(F(4, 5))
    ok_u = True
    for rot in (pair_rot, hop_rot):
        for (i, j) in ((0, 1), (0, 2), (1, 3), (2, 3)):
            for _ in range(3):
                psi = rand_even(4)
                img = rot(i, j, c, s, psi)
                if ip(img, img) != ip(psi, psi): ok_u = False
    _chk("J6      the pairing and hop rotations are isometries on random even states", ok_u)
    ok_q = True
    for rot in (pair_rot, hop_rot):
        for (i, j) in ((0, 1), (0, 2), (1, 3), (2, 3)):
            for _ in range(4):
                psi = rand_even(4)
                if cartan_Q(rot(i, j, c, s, psi)) != cartan_Q(psi): ok_q = False
    _chk("J7      Q is INVARIANT under every pairing and hop rotation tried (Spin(8) invariance)",
          ok_q)
    vac4 = {fs(): QI(1)}
    _chk("J8      a pairing rotation MOVES the vacuum (to the Thouless state c|0> + s|ij>)",
          seq(pair_rot(0, 1, c, s, vac4), sadd(sscal(c, vac4), sscal(s, {fs(0, 1): QI(1)}))))
    _chk("J9      a hop rotation FIXES the vacuum",
          seq(hop_rot(0, 1, c, s, vac4), vac4))
    _chk("J10     the moved vacuum still has Q = 0: the pairing rotation runs along the quadric",
          cartan_Q(pair_rot(0, 1, c, s, vac4)) == QI(0))


part_C2()

# ---------------------------------------------------------------------------
# Part D (second part): the Schrodinger sharpening (lem:square, lem:oddroots, lem:onedatum, cor:onebit). A companion script's Parts A to E, wrapped; C6 made exact at v1.8.
# ---------------------------------------------------------------------------

def part_D2():
    _RETAG = [
        ('A', 'lem:square A'),
        ('B', 'lem:oddroots B'),
        ('C7b', 'cor:onebit C7b'),
        ('C', 'lem:onedatum C'),
        ('D', 'prop:slowshadow(3) D'),
        ('E', 'lem:onedatum (ideal picture) E'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)
    from itertools import product

    SQ = g.sig(1, 3)
    BL = g.all_blades(4)
    E = [g.gen(i) for i in range(4)]
    I = g.mul(g.mul(E[0], E[1], SQ), g.mul(E[2], E[3], SQ), SQ)
    ONE = g.sc(1)


    def m(*xs):
        out = xs[0]
        for x in xs[1:]:
            out = g.mul(out, x, SQ)
        return out


    def vec(c):
        return g.add(*[g.scal(c[i], E[i]) for i in range(4)]) if any(c) else {}


    def sq(x):
        return m(x, x)


    def is_scalar(x, val):
        return g.eq(x, g.sc(val))


    def grade(x, k):
        return {b: c for b, c in x.items() if len(b) == k}


    def even(x):
        return {b: c for b, c in x.items() if len(b) % 2 == 0}


    def coords(x):
        return [x.get(b, F(0)) for b in BL]


    def kernel_dim_of_maps(maps, domain_blades):
        """Dimension of {x in span(domain_blades): f(x) = 0 for all f in maps}."""
        rows = []
        for f in maps:
            cols = [coords(f(g.sc(0) if False else {b: F(1)})) for b in domain_blades]
            for r in range(len(BL)):
                rows.append([cols[j][r] for j in range(len(domain_blades))])
        rank = g.mat_rank(rows) if rows else 0
        return len(domain_blades) - rank


    def commutator(x, y):
        return g.sub(m(x, y), m(y, x))


    def anticomm(x, y):
        return g.add(m(x, y), m(y, x))


    # ---------------------------------------------------------------------------
    # A. The square of nabla psi = m psi C.  nabla acts on the left and C is
    #    constant, so nabla(nabla psi C^{-1}) C^{-1} = nabla^2 psi C^{-2}: the
    #    Klein-Gordon operator of mass m appears iff C^{-2} = -1 iff C^2 = -1.
    #    Checked at the level of the right factor: for the operator identity the
    #    only algebra is C^{-2}, and we check that on a sample of odd C.
    # ---------------------------------------------------------------------------
    EVEN_BL = [b for b in BL if len(b) % 2 == 0]
    ODD_BL = [b for b in BL if len(b) % 2 == 1]

    # an odd element with C^2 = -1 (Hestenes' C) and one with C^2 = +1 (I gamma_0)
    C_hest = m(E[0], g.neg(m(I, m(E[3], E[0]))))          # gamma_0 (I sigma_3)^{-1}
    Isig3 = m(I, m(E[3], E[0]))                             # I sigma_3 = gamma_2 gamma_1
    _chk("A1: I sigma_3 = gamma_2 gamma_1", g.eq(Isig3, m(E[2], E[1])))
    _chk("A2: (I sigma_3)^{-1} = -I sigma_3", is_scalar(m(Isig3, g.neg(Isig3)), 1))
    _chk("A3: Hestenes' right factor C = gamma_0 (I sigma_3)^{-1} has C^2 = -1",
            is_scalar(sq(C_hest), -1))
    C_tach = m(I, E[0])
    _chk("A4: C = I gamma_0 is odd with C^2 = +1 (a tachyonic right factor)",
            g.eq(C_tach, {b: c for b, c in C_tach.items() if len(b) % 2 == 1})
            and is_scalar(sq(C_tach), 1))
    # psi C^{-1} with C^{-1} = -C when C^2 = -1: the double application gives
    # psi C^{-2} = -psi, i.e. nabla^2 psi = -m^2 psi.  For C^2 = +1 it gives
    # +m^2 psi.  For a C whose square is not scalar there is no scalar KG
    # equation at all: exhibit one.
    C_mixed = g.add(E[3], m(I, E[2]))                       # v = e3, w = e2, v^w != 0
    _chk("A5: C = gamma_3 + I gamma_2 has a non-scalar square (no KG equation)",
            len(sq(C_mixed)) > 1)


    # ---------------------------------------------------------------------------
    # B. Odd square roots of -1: the identity C^2 = v^2 + w^2 - 2 I (v ^ w).
    # ---------------------------------------------------------------------------
    def wedge_vv(v, w):
        return g.scal(F(1, 2), g.sub(m(v, w), m(w, v)))


    samples = [([1, 2, -1, 3], [2, -1, 1, 1]), ([0, 1, 0, 0], [0, 0, 1, 0]),
               ([3, 1, 4, 1], [1, 0, -2, 5]), ([2, 2, 2, 2], [1, 1, 1, 1])]
    ok = True
    for vc, wc in samples:
        v, w = vec(vc), vec(wc)
        C = g.add(v, m(I, w))
        lhs = sq(C)
        rhs = g.add(g.sc(g.dot(v, v, SQ) + g.dot(w, w, SQ)),
                    g.scal(-2, m(I, wedge_vv(v, w))))
        ok = ok and g.eq(lhs, rhs)
    _chk("B1: (v + I w)^2 = v.v + w.w - 2 I (v ^ w) on four rational samples", ok)

    # consequence: C^2 = -1 forces v ^ w = 0 and v.v + w.w = -1, so C = (a + b I) u
    # with u.u = -1 and a^2 + b^2 = 1.  Instances: (3/5, 4/5), u = e3 and a boosted u.
    u = E[3]
    for a, b in [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13))]:
        C = m(g.add(g.sc(a), g.scal(b, I)), u)
        _chk("B2: C = (%s + %s I) gamma_3 squares to -1" % (a, b), is_scalar(sq(C), -1))
    # a boosted spacelike unit vector: R = 5/4 + 3/4 e0 e3 sends e3 to a unit
    # spacelike vector with a time component; C = I u' still squares to -1
    R = g.add(g.sc(F(5, 4)), g.scal(F(3, 4), m(E[0], E[3])))
    Rt = g.reverse(R)
    _chk("B3: R = 5/4 + 3/4 e0 e3 is a rotor", is_scalar(m(R, Rt), 1))
    u2 = m(Rt, u, R)
    _chk("B4: the boosted u' = R~ gamma_3 R is a unit spacelike vector with a time component",
            is_scalar(sq(u2), -1) and u2.get((0,), F(0)) != 0)
    _chk("B5: C' = I u' squares to -1 and equals R~ (I gamma_3) R (rotor covariance)",
            is_scalar(sq(m(I, u2)), -1) and g.eq(m(I, u2), m(Rt, m(I, u), R)))
    # the chiral phase: psi -> psi exp(t I) with exp(t I) = cos t + sin t I sends
    # the equation with C to the equation with exp(-t I) C exp(t I) = C exp(2 t I).
    ct, st = F(3, 5), F(4, 5)
    ph = g.add(g.sc(ct), g.scal(st, I))
    ph_inv = g.add(g.sc(ct), g.scal(-st, I))
    _chk("B6: exp(t I) exp(-t I) = 1 for cos t = 3/5, sin t = 4/5", is_scalar(m(ph, ph_inv), 1))
    C0 = m(I, u)
    c2, s2 = ct * ct - st * st, 2 * ct * st
    ph2 = g.add(g.sc(c2), g.scal(s2, I))
    _chk("B7: exp(-t I) C exp(t I) = C exp(2 t I) for odd C (I anticommutes with odd elements)",
            g.eq(m(ph_inv, C0, ph), m(C0, ph2)))
    _chk("B8: exp(t I) is NOT a rotor (its reverse is itself, not its inverse): the chiral "
            "phase is a field redefinition outside Spin+(1,3)",
            g.eq(g.reverse(ph), ph) and not is_scalar(m(ph, g.reverse(ph)), 1))
    # the chiral phase shifts the Takabayasi angle: psi psi~ -> exp(2 t I) psi psi~
    psi = g.add(g.sc(2), g.scal(F(1, 3), m(E[1], E[2])), g.scal(F(-1, 2), m(E[0], E[1])),
                g.scal(F(1, 5), I))
    lhs = m(psi, ph, g.reverse(m(psi, ph)))
    rhs = m(ph2, psi, g.reverse(psi))
    _chk("B9: (psi e^{tI})(psi e^{tI})~ = e^{2tI} psi psi~ (the chiral phase shifts beta by 2t)",
            g.eq(lhs, rhs))


    # ---------------------------------------------------------------------------
    # C. One datum, not two.  Given C = I u (u = gamma_3 after alignment), the
    #    complex structures J in Cl^+ with J^2 = -1 and [J, C] = 0.
    # ---------------------------------------------------------------------------
    Cu = m(I, u)
    # C1: the commutant of C in the even subalgebra has dimension 4
    maps = [lambda x: commutator(x, Cu)]
    rows = []
    for b in EVEN_BL:
        col = coords(commutator({b: F(1)}, Cu))
        rows.append(col)
    # rows are images of basis even elements; kernel dim = 8 - rank
    rank = g.mat_rank([[rows[j][r] for j in range(len(EVEN_BL))] for r in range(len(BL))])
    _chk("C1: the commutant of C = I gamma_3 in Cl^+(1,3) is 4-dimensional", 8 - rank == 4)
    comm_basis = [ONE, m(E[0], E[1]), m(E[0], E[2]), m(E[1], E[2])]
    _chk("C2: it is spanned by 1, e0e1, e0e2, e1e2 (the even algebra of the 3-space orthogonal to u)",
            all(g.is_zero(commutator(x, Cu)) for x in comm_basis))
    _chk("C3: the pseudoscalar I is even, squares to -1, but does NOT commute with C (it anticommutes)",
            is_scalar(sq(I), -1) and g.is_zero(anticomm(I, Cu)) and not g.is_zero(commutator(I, Cu)))
    # C4: J = a + b e0e1 + c e0e2 + d e1e2 has J^2 = a^2 + (b^2 + c^2 - d^2) + 2 a B;
    #     J^2 = -1 iff a = 0 and d^2 - b^2 - c^2 = 1: a two-sheeted hyperboloid.
    ok = True
    for a, b, c, d in [(F(0), F(0), F(0), F(1)), (F(0), F(3, 4), F(0), F(5, 4)),
                       (F(0), F(5, 12), F(0), F(-13, 12)), (F(0), F(1, 2), F(1, 2), F(0))]:
        J = g.add(g.sc(a), g.scal(b, m(E[0], E[1])), g.scal(c, m(E[0], E[2])), g.scal(d, m(E[1], E[2])))
        want = (a == 0 and d * d - b * b - c * c == 1)
        ok = ok and (is_scalar(sq(J), -1) == want)
    _chk("C4: J^2 = -1 on the commutant iff a = 0 and d^2 - b^2 - c^2 = 1 (four instances, one negative)", ok)
    # C5: the bijection J <-> gamma_0 := C J onto unit timelike vectors orthogonal to u
    ok = True
    for b, c, d in [(F(0), F(0), F(1)), (F(3, 4), F(0), F(5, 4)), (F(0), F(5, 12), F(13, 12)),
                    (F(3, 4), F(0), F(-5, 4))]:
        J = g.add(g.scal(b, m(E[0], E[1])), g.scal(c, m(E[0], E[2])), g.scal(d, m(E[1], E[2])))
        gam0 = m(Cu, J)
        is_vec = g.eq(gam0, grade(gam0, 1))
        ok = ok and is_vec and is_scalar(sq(gam0), 1) and g.dot(gam0, u, SQ) == 0
        # and back: J = C^{-1} gamma_0 = -C gamma_0
        ok = ok and g.eq(J, m(g.neg(Cu), gam0))
    _chk("C5: gamma_0 := C J is a unit timelike vector orthogonal to u, and J = C^{-1} gamma_0 recovers J "
            "(four instances, both sheets)", ok)
    J0 = m(E[1], E[2])
    _chk("C6: at J = e1e2 and C = I e3, C J = +gamma_0 exactly, and at J = -e1e2 it is -gamma_0: the sign is the choice of sheet",
            g.eq(m(Cu, J0), E[0]) and g.eq(m(Cu, g.neg(J0)), g.neg(E[0])))
    # C7: the stabiliser of (C, J) in Cl^+ is span{1, J}: the U(1) of the J-plane
    rows = []
    for bb in EVEN_BL:
        x = {bb: F(1)}
        rows.append(coords(commutator(x, Cu)) + coords(commutator(x, J0)))
    rank = g.mat_rank([[rows[j][r] for j in range(len(EVEN_BL))] for r in range(2 * len(BL))])
    _chk("C7: the joint commutant of C and J in Cl^+(1,3) is 2-dimensional, span{1, J}", 8 - rank == 2)
    # C7b: with C fixed, J -> -J forces gamma_0 -> -gamma_0: the frequency sign
    #      (particle/antiparticle) and the time direction are one bit, given the law.
    #      The rest rotation by pi about e1 (R = e2 e3) flips J and fixes gamma_0,
    #      but it also flips C, so it is not a symmetry of the law with C fixed.
    Rpi = m(E[2], E[3])
    _chk("C7b: given C, J -> -J is gamma_0 -> -gamma_0 (C(-J) = -(CJ)); the pi-rotation that flips J "
            "while fixing gamma_0 flips C, so it is not a symmetry of the fixed law",
            g.eq(m(Cu, g.neg(J0)), g.neg(m(Cu, J0)))
            and g.eq(m(g.reverse(Rpi), J0, Rpi), g.neg(J0))
            and g.eq(m(g.reverse(Rpi), E[0], Rpi), E[0])
            and g.eq(m(g.reverse(Rpi), Cu, Rpi), g.neg(Cu)))
    # C8: the frame need not start orthogonal to u: a rotor aligns it.  Take the
    #     lab frame gamma_0 and the datum C = I u' with u' boosted (B4); the
    #     rotor R~ of B3 realigns.  Equivalently: any lab frame f (unit timelike)
    #     and any C = I u admit a rotor S with S~ u S orthogonal to f.
    f = E[0]
    _chk("C8: the boosted datum u' is not orthogonal to the lab frame, and R (of B3) realigns it",
            g.dot(u2, f, SQ) != 0 and g.dot(m(R, u2, Rt), f, SQ) == 0)


    # ---------------------------------------------------------------------------
    # D. The Hestenes instance and the Klein-Gordon sign lemma in the form
    #    nabla psi J = m psi gamma_0: gamma_0 J gamma_0 = +J iff [J, gamma_0] = 0
    #    (KG at -m^2), = -J iff {J, gamma_0} = 0 (tachyonic), else non-scalar.
    # ---------------------------------------------------------------------------
    _chk("D1: J = I sigma_3 commutes with gamma_0: gamma_0 J gamma_0 = J, the square is -m^2",
            g.eq(m(E[0], Isig3, E[0]), Isig3))
    _chk("D2: J = I (pseudoscalar) anticommutes with gamma_0: gamma_0 I gamma_0 = -I, the square is +m^2",
            g.eq(m(E[0], I, E[0]), g.neg(I)))
    Rb = g.add(g.sc(F(5, 4)), g.scal(F(3, 4), m(E[0], E[1])))
    Jmix = m(g.reverse(Rb), Isig3, Rb)          # the spin plane boosted out of the rest space
    _chk("D3: a boosted spin plane J = R~ (I sigma_3) R squares to -1, neither commutes nor anticommutes "
            "with gamma_0, and gamma_0 J gamma_0 J^{-1} is not scalar: no scalar KG equation",
            is_scalar(sq(Jmix), -1) and not g.is_zero(commutator(Jmix, E[0]))
            and not g.is_zero(anticomm(Jmix, E[0])) and len(m(E[0], Jmix, E[0], g.neg(Jmix))) > 1)
    # the commutant of gamma_0 in Cl^+ is the quaternions of the rest space
    rows = []
    for bb in EVEN_BL:
        rows.append(coords(commutator({bb: F(1)}, E[0])))
    rank = g.mat_rank([[rows[j][r] for j in range(len(EVEN_BL))] for r in range(len(BL))])
    _chk("D4: the commutant of gamma_0 in Cl^+(1,3) is 4-dimensional (1 and the three rest bivectors)",
            8 - rank == 4)


    # ---------------------------------------------------------------------------
    # E. The ideal picture: P = (1 + gamma_0)/2, P Cl P has dimension 4.
    # ---------------------------------------------------------------------------
    P = g.scal(F(1, 2), g.add(ONE, E[0]))
    _chk("E1: P = (1 + gamma_0)/2 is idempotent", g.eq(m(P, P), P))
    imgs = [coords(m(P, {bb: F(1)}, P)) for bb in BL]
    rank = g.mat_rank([[imgs[j][r] for j in range(len(BL))] for r in range(len(BL))])
    _chk("E2: dim P Cl(1,3) P = 4 (the division ring H of the minimal left ideal)", rank == 4)
    quat = [P, m(P, m(E[1], E[2])), m(P, m(E[2], E[3])), m(P, m(E[3], E[1]))]
    _chk("E3: P, P e1e2, P e2e3, P e3e1 lie in P Cl P and the three bivector ones square to -P",
            all(g.eq(m(P, x, P), x) for x in quat) and all(g.eq(sq(x), g.neg(P)) for x in quat[1:]))
    # a right factor C preserves the ideal Cl P iff P C = P C P; Hestenes' J = I sigma_3 does,
    # the pseudoscalar I does not
    _chk("E4: right multiplication by I sigma_3 preserves the ideal Cl P (P J = P J P); by I it does not",
            g.eq(m(P, Isig3), m(P, Isig3, P)) and not g.eq(m(P, I), m(P, I, P)))


part_D2()

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
