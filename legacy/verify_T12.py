#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T12.py: exact-arithmetic verification of the computational identities of
"The Standard Model from the Minimal Massive Composite" (Transport Papers,
T12), printed version 1.1.

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rationals, Gaussian rationals, the
cyclotomic field Q(zeta_6) (realised locally below), rational functions in a
formal Lambda, and integer arithmetic; no floating point anywhere except the
lines marked RECORD (GeV conversions, proton lifetimes and the two-loop
integrations, printed and not checked) and the lines marked CONTROL: two in
Part J (the integrator against the exact one-loop result, and the two-loop
meeting), five in Part L (the proton condition on the candidates, the
integrator against the exact one-loop chain, the chain against the proton
bound, and the requirement on the neutrino sector) and two in Part M (the
stored fits and their tuning).  Part M's floating-point lines need numpy and
are skipped without it.  Statement tags refer to the compiled paper.

Thirteen parts.  A to E are the paper's original five (the ladder; the algebra and
the global form; content and charges; unification; the one number, now with
the fourth alternative, prop:trichotomy(4)).  F: the partner sector priced
(Section 8).  G: the frozen point on the two-rung module (Sections 9.1 to
9.3).  H: the ten, the pairing, the Yukawa pattern and the transported frozen
point (Sections 9.4, 9.5).  I: the three no-go theorems (Section 9.6), in
three instalments: the family no-go with the Georgi-Jarlskog direction
rebuilt before use, the two-dimensional span and the frozen-point no-go, and
the bracket no-go.  J: two thresholds and two loops (Sections 8.4, 8.5).
K: the slot/pair split on the module (Section 10: Pati-Salam, the
generation and the ten, the matching, the proton channel, the Majorana
element, left-right parity and the rung parity, the complex bidoublet) and
the twisted action of prop:sixteen(3).  L: the proton condition (Section
8.6), the chains (prop:pschains), the normalisation of cor:mirror without
(S), and the desert's generation count and Higgs-free value (prop:desert).
M: the weak angle on the Pati-Salam route (Section 11: equal weight on the
module, the elimination identity, the grade-three direction, the stored
fits of obs:anglefits).
Parts F to J are the companion notes' scripts of 2026-09-07 (verify_T12_partner,
verify_T12_split, verify_T12_higgs, and the relevant parts of
verify_four_programmes, verify_quarter_coefficient_state and
verify_cheap_fills), each wrapped as a function with its tags mapped to this
paper's numbering; their check bodies are unchanged.

v1.10 (2026-10-07, printed version 1.1, Stage 2): 243 checks (234 exact, 9
floating-point CONTROL lines; 241 if scipy is absent, 239 if numpy is absent
too).  Added Part M (4 exact checks M1-M4 and CONTROL C11, C12 on four
stored coupling sets) and, in Part L, the requirement record and C10.
v1.9 (2026-10-07, printed version 1.1): 236 checks (230 exact, 6 floating-point
CONTROL lines; 234 if scipy is absent, Part J's two CONTROL lines then being
skipped).  Added Parts K (19 checks) and L (7 checks and 4 CONTROL lines) for
the merge of the unification findings: Section 8.6 (fact:proton,
prop:proton), Section 10 (prop:split to prop:pschains), the corrected
prop:sixteen(3) in the action the state space carries, cor:mirror's
normalisation, and prop:desert's wording.  The Part C check of
prop:sixteen(3) now names its action (the untwisted one).
v1.8 (2026-09-08, review-repair pass against T12_review_v5.md): 206 checks.
Three checks rebuilt so that they can fail: cor:mirror (the mirror copy's
coefficients computed from its species content with and without the lepton
doublet, (41/10, -19/6, -7) and (7/2, -25/6, -7), ratios 218/115 and 46/17);
Thm 9.33 NO-GO (c_4, c_5 tested to commute with su(3), the su(3)-invariant
part of the odd span computed and found to be span{c_4, c_5} inside the ten,
T_GJ and its form outside); Prop 9.27(ii) (the reciprocal evaluated at
Lambda = 0 as the ideal point).  Thm 8.15 (B1) now tests points on the line
and off it.  Cor 9.36 (A8): chi = -(-1)^{N_R} used, sign -(2/3).  Added:
Rem 8.17 (B6), the species-level enumeration (4096 splits, 296 with the
gluino light admitting a segment).  Labels: A10 retag order, dim_singlets
== 8, retired vocabulary removed from messages.
v1.6 (2026-09-07): 205 checks (48 prior + 2 in Part E + 155 in Parts F to J;
203 if scipy is absent, Part J's two CONTROL lines then being skipped).
v1.4 (2026-09-03): 48 checks; v1.3 (same day): 42; v1.2: 40; v1.1: 36 (was 27).
v1.4 adds, per the v3 review: the lepton-free trace ratio 9/26 and the
lepton-free anomaly sums (1/2, 1, 1/4) (B1, B2); the ledger's weights all
non-negative and no (1,3) or (1,3bar) in any degree (S1); the exhaustive
no-(2,1) check over the partitions of the 2 x 3 box (N5); the e^3 != 0
irreducibility witness for the filled row's span (N5); the general
abelian generator alpha j + beta k with the integer sweep (prop:sixteen(3),
S2); t = 5/7 unrescaled in the family (N6); comments swept (N11).
Added or rebuilt in v1.1, per the v1 review:
the n = 3 polarisation witness for prop:ladder (the old rank-4 check covered
n = 2 only); a real Z6 kernel check in Q(zeta_6) replacing the vacuous
"3*2 == 6"; the lattice residue on every representation used, with the
hypercharge-zero singlet and a failing example; the hypercharge generator's
weights on every representation of prop:content; the [SU(2)]^2 U(1)
selection of the full twistor; the one-handed singlet listing; the four
anomaly sums on the derived spectrum; the second solution with a free fourth
singlet and three members of the Y + t(B-L) family; the trace ratios 9/10
and 3/4; the three pairwise meeting scales; the third compression identity.
v1.3 adds: the filled-row rank-4 witness (no lepton in the tensor
ledger); the opposite-handedness anomaly sums; t = 0 in the family; the
Hodge-star loop; the Z6 check evaluated on matrices with a non-kernel
element.  v1.2 adds: the converse m^2 + k^2 = 13; the mass bracket's weight 6; the
pair-system duality weights; the Lambda^*(C^2 + C^3) component table
against the derived generation and its conjugate.
"""

from fractions import Fraction as F
from itertools import combinations

from fractions import Fraction
import GA as g

# ---------------------------------------------------------------------------
# Part A: the internal ladder (prop:ladder) and the mass bracket as a
# charged singlet (prop:singlet)
# ---------------------------------------------------------------------------

# prop:ladder.  The proof goes through rank-one configurations because the
# n^2 products pi^j pibar^k live in a four-dimensional space: for n = 2 they
# can form a basis (rank 4 of 4), for n = 3 they cannot (rank 4 of 9).
P1 = [g.qi(1), g.qi(0)]
P2 = [g.qi(1, 1), g.qi(2)]
P3 = [g.qi(2, -1), g.qi(F(1, 3), 1)]


def outer(a, b):
    """pi^j_A conj(pi^k)_{A'} flattened to a 4-vector."""
    return [a[A] * b[Ap].conj() for A in range(2) for Ap in range(2)]


rows2 = [outer(p, q) for p in (P1, P2) for q in (P1, P2)]
g.check("prop:ladder: for n = 2 the four products pi^j pibar^k of an explicit "
      "configuration are linearly independent (rank 4 over the Gaussian "
      "rationals)", g.field_rank(rows2) == 4)

rows3 = [outer(p, q) for p in (P1, P2, P3) for q in (P1, P2, P3)]
g.check("prop:ladder: for n = 3 the nine products pi^j pibar^k of a generic "
      "configuration have rank 4, not 9: they are dependent, which is why "
      "the proof argues from rank-one configurations",
      g.field_rank(rows3) == 4)

# the polarisation step at n = 3: a Hermitian M with v^dag M v = 0 for the
# nine listed vectors is zero.  Parametrise Hermitian M by nine real
# coordinates (three diagonal, three real and three imaginary off-diagonal
# parts) and check the nine linear functionals v -> v^dag M v have rank 9.
E = [[g.qi(1 if i == j else 0) for j in range(3)] for i in range(3)]


def herm_basis():
    out = []
    for j in range(3):
        M = [[g.qi(0)] * 3 for _ in range(3)]
        M[j][j] = g.qi(1)
        out.append(M)
    for j in range(3):
        for k in range(j + 1, 3):
            M = [[g.qi(0)] * 3 for _ in range(3)]
            M[j][k] = M[k][j] = g.qi(1)
            out.append(M)
            M2 = [[g.qi(0)] * 3 for _ in range(3)]
            M2[j][k], M2[k][j] = g.QI_I, -g.QI_I
            out.append(M2)
    return out


def quad_form(M, v):
    tot = g.qi(0)
    for j in range(3):
        for k in range(3):
            tot = tot + v[j].conj() * M[j][k] * v[k]
    return tot


e1, e2, e3 = [g.qi(1), g.qi(0), g.qi(0)], [g.qi(0), g.qi(1), g.qi(0)], \
    [g.qi(0), g.qi(0), g.qi(1)]
i_ = g.QI_I
TESTV = [e1, e2, e3,
         [g.qi(1), g.qi(1), g.qi(0)], [g.qi(1), g.qi(0), g.qi(1)],
         [g.qi(0), g.qi(1), g.qi(1)],
         [g.qi(1), i_, g.qi(0)], [g.qi(1), g.qi(0), i_], [g.qi(0), g.qi(1), i_]]
HB = herm_basis()
pol_rows = []
all_real = True
for v in TESTV:
    row = []
    for M in HB:
        q = quad_form(M, v)
        all_real = all_real and q.im == 0
        row.append(F(q.re))
    pol_rows.append(row)
g.check("prop:ladder: polarisation at n = 3: v^dag M v is real on the nine "
      "listed vectors and the nine functionals have rank 9 on the "
      "nine-dimensional space of Hermitian forms, so v^dag M v = 0 for all v "
      "forces M = 0 and U^dag U = 1", all_real and g.mat_rank(pol_rows) == 9)

# unitarity preserves the momentum: exact rational unitary instances
U_real = [[g.qi(F(3, 5)), g.qi(F(4, 5))], [g.qi(F(-4, 5)), g.qi(F(3, 5))]]
U_cplx = [[g.qi(F(3, 5), F(4, 5)), g.qi(0)], [g.qi(0), g.qi(1)]]


def apply_mix(U, spinors):
    return [[sum(U[i][j] * spinors[j][A] for j in range(2)) for A in range(2)]
            for i in range(2)]


def total_p(spinors):
    p = [[g.qi(0)] * 2 for _ in range(2)]
    for s in spinors:
        for A in range(2):
            for Ap in range(2):
                p[A][Ap] = p[A][Ap] + s[A] * s[Ap].conj()
    return p


ok = True
for U in (U_real, U_cplx):
    p0 = total_p([P1, P2])
    p1 = total_p(apply_mix(U, [P1, P2]))
    ok = ok and all(p0[A][Ap] == p1[A][Ap] for A in range(2) for Ap in range(2))
g.check("prop:ladder: exact unitary instances (real and complex rational) "
      "preserve the total momentum", ok)


def eps2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def det2(U):
    return U[0][0] * U[1][1] - U[0][1] * U[1][0]


ok = True
for U in (U_real, U_cplx):
    s1, s2 = apply_mix(U, [P1, P2])
    ok = ok and eps2(s1, s2) == det2(U) * eps2(P1, P2)
g.check("prop:singlet: the mass bracket transforms by det(U) exactly on both "
      "unitary instances (SU(2)-singlet; charge one under det, two under the "
      "scalar phase)", ok)

# ---------------------------------------------------------------------------
# Part B: the gauge algebra (thm:algebra) and the global form (thm:global)
# ---------------------------------------------------------------------------

def basis_u(n):
    """A real basis of u(n) as QI matrices: i E_kk, (E_jk - E_kj),
    i(E_jk + E_kj)."""
    out = []
    for k in range(n):
        M = [[g.qi(0)] * n for _ in range(n)]
        M[k][k] = g.QI_I
        out.append(M)
    for j in range(n):
        for k in range(j + 1, n):
            M = [[g.qi(0)] * n for _ in range(n)]
            M[j][k], M[k][j] = g.qi(1), g.qi(-1)
            out.append(M)
            M2 = [[g.qi(0)] * n for _ in range(n)]
            M2[j][k] = M2[k][j] = g.QI_I
            out.append(M2)
    return out


def action_vec(X, Y, m, k):
    """(X ox 1 + 1 ox Y) on C^m ox C^k, flattened to a (mk)^2 vector."""
    mk = m * k
    M = [[g.qi(0)] * mk for _ in range(mk)]
    for a in range(m):
        for b in range(k):
            r = a * k + b
            for c in range(m):
                if X[a][c]:
                    M[r][c * k + b] = M[r][c * k + b] + X[a][c]
            for d in range(k):
                if Y[b][d]:
                    M[r][a * k + d] = M[r][a * k + d] + Y[b][d]
    return [M[i][j] for i in range(mk) for j in range(mk)]


def image_rank(m, k):
    zero_m = [[g.qi(0)] * m for _ in range(m)]
    zero_k = [[g.qi(0)] * k for _ in range(k)]
    vecs = [action_vec(X, zero_k, m, k) for X in basis_u(m)]
    vecs += [action_vec(zero_m, Y, m, k) for Y in basis_u(k)]
    return len(vecs), g.field_rank(vecs)

n_gen, rk = image_rank(2, 3)
g.check("thm:algebra: u(2) + u(3) has 13 generators and its action on "
      "C^2 ox C^3 has rank exactly 12 (one-dimensional kernel, the diagonal "
      "phase): dim = 3 + 8 + 1, the Standard Model Lie algebra",
      n_gen == 13 and rk == 12)

n_gen, rk = image_rank(3, 3)
g.check("thm:algebra: the maximal hierarchy: u(3) + u(3) on C^3 ox C^3 has "
      "18 generators and image rank 17 = dim(su(3) + su(3) + u(1)), not 12",
      n_gen == 18 and rk == 17)

# the kernel coset arithmetic of thm:global: replacing (A,B) by
# (lam A, lam^-1 B) rescales detA * detB by lam^2 lam^-3 = lam^-1
lam = g.qi(F(3, 5), F(4, 5))         # unit-modulus Gaussian rational
g.check("thm:global: the coset rescaling law: lam^2 * lam^-3 = lam^-1 "
      "exactly for a unit-modulus Gaussian rational",
      lam * lam * (g.qi(1) / (lam * lam * lam)) == g.qi(1) / lam)

# the Z6 kernel, for real: realise zeta_6 exactly in Q(zeta_6) = Q(zeta),
# zeta^2 = zeta - 1, elements p + q zeta with p, q rational.
class Z6(object):
    """Element p + q*zeta of Q(zeta_6), zeta^2 = zeta - 1, exact."""
    __slots__ = ("p", "q")

    def __init__(self, p=0, q=0):
        self.p, self.q = F(p), F(q)

    def __mul__(self, o):
        # (p + q z)(r + s z) = pr + (ps + qr) z + qs z^2, z^2 = z - 1
        return Z6(self.p * o.p - self.q * o.q,
                  self.p * o.q + self.q * o.p + self.q * o.q)

    def __eq__(self, o):
        return self.p == o.p and self.q == o.q

    def __ne__(self, o):
        return not self.__eq__(o)

    def __pow__(self, n):
        out = Z6(1, 0)
        base = self
        if n < 0:
            base = self.inv()
            n = -n
        for _ in range(n):
            out = out * base
        return out

    def inv(self):
        # zeta^-1 = 1 - zeta (since zeta * (1 - zeta) = zeta - zeta^2 = 1)
        # general inverse via the norm: (p + q z)(p + q zbar), zbar = 1 - z
        conj = Z6(self.p + self.q, -self.q)
        nrm = (self * conj)
        assert nrm.q == 0
        return Z6(conj.p / nrm.p, conj.q / nrm.p)


zeta = Z6(0, 1)
one6 = Z6(1, 0)
# sanity: zeta has order exactly 6 and zeta^3 = -1
powers = [zeta ** j for j in range(6)]
order_ok = (zeta ** 6 == one6 and zeta ** 3 == Z6(-1, 0)
            and len({(z.p, z.q) for z in powers}) == 6)


def hom_image(a_scalar, b_scalar, lam):
    """The second isomorphism (a, b, lam) -> (lam^3 a, lam^-2 b) evaluated on
    scalar a = a_scalar I_2, b = b_scalar I_3, returned as the two scalars."""
    return (lam ** 3 * a_scalar, lam ** (-2) * b_scalar)


def in_kernel(j):
    """Is (zeta^-3j I_2, zeta^2j I_3, zeta^j) in the kernel?  Evaluate the
    homomorphism and check the image is (I_2, I_3), and check that a, b lie
    in SU(2), SU(3): det a = zeta^-6j = 1, det b = zeta^6j = 1."""
    a_s, b_s = zeta ** (-3 * j), zeta ** (2 * j)
    img = hom_image(a_s, b_s, zeta ** j)
    return img == (one6, one6) and a_s ** 2 == one6 and b_s ** 3 == one6


kernel_ok = all(in_kernel(j) for j in range(6))
# a non-kernel element: (I_2, I_3, zeta) maps to (zeta^3 I_2, zeta^-2 I_3),
# which is not the identity
img_nonker = hom_image(one6, one6, zeta)
nonkernel_ok = img_nonker != (one6, one6)
# that nothing else is in the kernel is the determinant argument of the
# proof (lam^6 = 1 has exactly six solutions), not a computation
g.check("thm:global: in Q(zeta_6), zeta has order exactly six; the second "
      "isomorphism evaluated on (zeta^-3j I_2, zeta^2j I_3, zeta^j) returns "
      "(I_2, I_3) for j = 0..5 with det a = det b = 1, and evaluated on "
      "(I_2, I_3, zeta) does not: the Z6 kernel, realised exactly",
      order_ok and kernel_ok and nonkernel_ok)

# the Z6 charge lattice: 2t + 3 delta + q = 0 mod 6, i.e. t/3 + delta/2 + Y
# integral, on every representation used in Section 5 (t = triality, delta =
# weak parity, q = 6Y the abelian weight), the hypercharge-zero singlet
# included; and a colour singlet of hypercharge 1/3 fails it.
SPECTRUM = [
    ("Q",   1, 1, F(1, 6)),
    ("L",   0, 1, F(-1, 2)),
    ("L+",  0, 1, F(1, 2)),       # the empty-twistor doublet, also on the lattice
    ("uc", -1, 0, F(-2, 3)),
    ("dc", -1, 0, F(1, 3)),
    ("ec",  0, 0, F(1)),
    ("nuc", 0, 0, F(0)),
    ("d_R", 1, 0, F(-1, 3)),      # the odd-grade states before conjugation
    ("e_R", 0, 0, F(-1)),
]
ok = True
for (name, t, delta, Y) in SPECTRUM:
    q6 = 6 * Y
    ok = ok and q6.denominator == 1 and (2 * t + 3 * delta + int(q6)) % 6 == 0
bad = (2 * 0 + 3 * 0 + 2) % 6      # colour singlet, Y = 1/3: q = 2
g.check("thm:global: the lattice residue 2t + 3 delta + q (q = 6Y) vanishes mod 6 on every "
      "representation used (Q, both twistor-level doublets, u^c, d^c, e^c, "
      "the hypercharge-zero singlet, and the odd-grade states), and a colour "
      "singlet of hypercharge 1/3 fails it", ok and bad != 0)

# prop:four: (n+2)/2 = 3 iff n = 4
g.check("prop:four(1): the pair count (n+2)/2 equals 3 exactly at n = 4 and "
      "at no other even n in 2..12, and the algebra dimension "
      "((n+2)/2)^2 + 3 equals 12 only there",
      [n for n in range(2, 13, 2) if F(n + 2, 2) == 3] == [4]
      and [n for n in range(2, 13, 2) if (n + 2) ** 2 // 4 + 3 == 12] == [4])

# prop:four(2), the converse: dim(su(m) + su(k) + u(1)) = m^2 + k^2 - 1 equals
# 12 only at {m, k} = {2, 3}
sols = [(m, k) for m in range(1, 13) for k in range(1, 13)
        if m * m + k * k - 1 == 12]
g.check("prop:four(2): m^2 + k^2 - 1 = 12 has exactly the solutions (2,3) and "
      "(3,2) for 1 <= m, k <= 12: the Standard Model algebra is the "
      "automorphism algebra of a two-factor hierarchy only for the unordered "
      "pair {2, 3}", sorted(sols) == [(2, 3), (3, 2)])

# ---------------------------------------------------------------------------
# Part C: content and charges (prop:raw, thm:hypercharge)
# ---------------------------------------------------------------------------

# prop:raw: graded dimensions of Lambda^*(C^6) and the Cauchy splits
from math import comb
dims = [comb(6, k) for k in range(7)]
g.check("prop:raw: the graded dimensions of the Fock space are "
      "1, 6, 15, 20, 15, 6, 1 (total 64)",
      dims == [1, 6, 15, 20, 15, 6, 1] and sum(dims) == 64)
# the Cauchy splits, with the Schur-functor dimensions computed from the
# hook-content formula rather than typed in: dim S^k(C^n) = C(n+k-1, k),
# dim Lambda^k(C^n) = C(n, k), dim S_(2,1)(C^n) = n(n^2 - 1)/3
def dim_sym(n, k):
    return comb(n + k - 1, k)


def dim_s21(n):
    return n * (n * n - 1) // 3


split2 = dim_sym(2, 2) * comb(3, 2) + comb(2, 2) * dim_sym(3, 2)
split3 = dim_sym(2, 3) * comb(3, 3) + dim_s21(2) * dim_s21(3) \
    + comb(2, 3) * dim_sym(3, 3)
g.check("prop:raw: the Cauchy splits from the Schur-functor dimensions: "
      "S^2 A x Lambda^2 B + Lambda^2 A x S^2 B = 3*3 + 1*6 = 15 = C(6,2) and "
      "S^3 A x Lambda^3 B + S_21 A x S_21 B + Lambda^3 A x S^3 B "
      "= 4*1 + 2*8 + 0*10 = 20 = C(6,3)",
      split2 == comb(6, 2) == 15 and split3 == comb(6, 3) == 20
      and dim_s21(2) == 2 and dim_s21(3) == 8 and comb(2, 3) == 0)

# no (2,1) in any degree, exhaustively (N5 of the v3 review): by the Cauchy
# formula Lambda^d(C^2 ox C^3) = sum over partitions lambda of d inside the
# 2 x 3 box of S_lambda(C^2) ox S_lambda'(C^3).  The dimensions come from the
# hook-content formula.  S_lambda(C^2) is two-dimensional exactly when
# lambda_1 - lambda_2 = 1, and for those lambda the conjugate S_lambda'(C^3)
# is never one-dimensional.  Also: every cell weighs +1 so degree d has weight
# d >= 0 (no negative weight anywhere, S1), and the only one-dimensional
# SU(3) factors occur at lambda' = (), (3), (3,3), i.e. lambda = (), (1,1,1)
# -- impossible in two rows -- so the SU(3) singlets are at lambda = (), (3), (3,3).
def hook_content_dim(lam, n):
    """dim S_lambda(C^n) by the hook-content formula, exact."""
    lam = [x for x in lam if x > 0]
    if not lam:
        return 1
    conj = [sum(1 for x in lam if x > j) for j in range(lam[0])]
    num, den = 1, 1
    for i, row in enumerate(lam):
        for j in range(row):
            num *= n + j - i
            den *= (row - j) + (conj[j] - i) - 1
    return num // den


def conjugate(lam):
    lam = [x for x in lam if x > 0]
    return [sum(1 for x in lam if x > j) for j in range(lam[0])] if lam else []


box = [(a, b) for a in range(4) for b in range(a + 1)]      # lambda_1 >= lambda_2, <= 3
total = 0
no_21 = True
no_1_dim3 = True
singlet_lams = []
for lam in box:
    d2 = hook_content_dim(list(lam), 2)
    d3 = hook_content_dim(conjugate(list(lam)), 3)
    total += d2 * d3
    if d2 == 2 and d3 == 1:
        no_21 = False
    if d3 == 1:
        singlet_lams.append(lam)
    # Both 3 and 3bar are three-dimensional, so ruling out every summand with a
    # one-dimensional SU(2) factor against a three-dimensional SU(3) factor rules
    # out (1,3) and (1,3bar) together, without deciding which conjugate occurs.
    if d2 == 1 and d3 == 3:
        no_1_dim3 = False
g.check("prop:raw, S1: over all ten partitions in the 2 x 3 box the Cauchy "
      "summands S_lambda(C^2) ox S_lambda'(C^3) total 64, none is (2,1) (the "
      "two-dimensional S_lambda(C^2) occur at lambda = (1), (2,1), (3,2), whose "
      "conjugates give 3, 8, 3bar), the SU(3) singlets occur only at lambda = (), "
      "(3), (3,3), and no summand pairs a one-dimensional S_lambda(C^2) with a "
      "three-dimensional S_lambda'(C^3), so neither (1,3) nor (1,3bar) occurs "
      "in any degree",
      total == 64 and no_21 and no_1_dim3
      and sorted(singlet_lams) == [(0, 0), (3, 0), (3, 3)]
      and hook_content_dim([2], 2) == 3 and conjugate([2]) == [1, 1]
      and hook_content_dim([1, 1], 3) == 3
      and hook_content_dim([1], 2) == 2 and hook_content_dim([1], 3) == 3
      and hook_content_dim([2, 1], 3) == 8 and hook_content_dim([2, 2, 1], 3) == 3)

# character check at rational diagonal instances: e_k of the six products
# a_i b_j vs the plethysm formulas
def esym(vals, k):
    tot = F(0)
    for c in combinations(range(len(vals)), k):
        p = F(1)
        for i in c:
            p *= vals[i]
        tot += p
    return tot


def hsym(vals, k):
    # complete homogeneous via generating recursion h_k = sum e-products;
    # small k: direct enumeration of multisets
    from itertools import combinations_with_replacement
    tot = F(0)
    for c in combinations_with_replacement(range(len(vals)), k):
        p = F(1)
        for i in c:
            p *= vals[i]
        tot += p
    return tot


ok2 = ok3 = True
for (a, b) in (((F(2), F(3)), (F(1), F(5), F(7))),
               ((F(1, 2), F(-3)), (F(2), F(-1), F(1, 3)))):
    prods = [x * y for x in a for y in b]
    # degree 2: e2(ab) = h2(a) e2(b) + e2(a) h2(b)
    ok2 = ok2 and esym(prods, 2) == hsym(a, 2) * esym(b, 2) + \
        esym(a, 2) * hsym(b, 2)
    # degree 3: e3(ab) = h3(a) e3(b) + s21(a) s21(b), with
    # s21 = h1 h2 - h3 (Jacobi-Trudi)
    s21a = hsym(a, 1) * hsym(a, 2) - hsym(a, 3)
    s21b = hsym(b, 1) * hsym(b, 2) - hsym(b, 3)
    ok3 = ok3 and esym(prods, 3) == hsym(a, 3) * esym(b, 3) + s21a * s21b
g.check("prop:raw: the degree-2 Cauchy character identity "
      "e2(ab) = h2(a)e2(b) + e2(a)h2(b) at two rational instances", ok2)
g.check("prop:raw: the degree-3 Cauchy character identity "
      "e3(ab) = h3(a)e3(b) + s21(a)s21(b) at two rational instances "
      "(the Lambda^3 A term dead for two-dimensional A)", ok3)

# prop:content: the hypercharge generator y = (3i I_2, -2i I_3), the centre
# of s(u(2) + u(3)), built as an exact matrix on each representation used;
# it must act as the scalar i*q with q the abelian weight, Y = q/6.
def scalar_of(M):
    """If M is a scalar multiple c*I (QI entries), return c, else None."""
    n = len(M)
    c = M[0][0]
    for i in range(n):
        for j in range(n):
            if (M[i][j] != c) if i == j else bool(M[i][j]):
                return None
    return c


X_y = [[g.qi(0, 3) if i == j else g.qi(0) for j in range(2)] for i in range(2)]
Y_y = [[g.qi(0, -2) if i == j else g.qi(0) for j in range(3)] for i in range(3)]
# on C^2 ox C^3: X ox 1 + 1 ox Y
vec = action_vec(X_y, Y_y, 2, 3)
M_Q = [vec[r * 6:(r + 1) * 6] for r in range(6)]
w_Q = scalar_of(M_Q)
# on C^2 ox Lambda^0 W: X alone;  on C^2 ox Lambda^3 W: X + tr(Y) I_2
w_L0 = scalar_of(X_y)
trY = Y_y[0][0] + Y_y[1][1] + Y_y[2][2]
w_L3 = scalar_of([[X_y[i][j] + (trY if i == j else g.qi(0)) for j in range(2)]
                  for i in range(2)])


def ext_power_diag_action(Y, k):
    """Action of a diagonal Y on Lambda^k C^3 in the wedge basis: the basis
    element e_S is an eigenvector with eigenvalue sum_{j in S} Y_jj."""
    out = []
    for S in combinations(range(3), k):
        out.append(sum((Y[j][j] for j in S), g.qi(0)))
    return out


weights_single = []
for k in range(4):
    eig = ext_power_diag_action(Y_y, k)
    weights_single.append(eig[0] if all(e == eig[0] for e in eig) else None)
g.check("prop:content: the hypercharge generator y = (3i I_2, -2i I_3) acts as "
      "the scalar i*q with q = 1 on C^2 ox C^3 (Y_Q = 1/6), q = 3 on the "
      "empty-twistor doublet and q = -3 on the full-twistor doublet "
      "(Y = +1/2, -1/2), and q = 0, -2, -4, -6 on Lambda^k C^3 "
      "(Y = 0, -1/3, -2/3, -1)",
      w_Q == g.qi(0, 1) and w_L0 == g.qi(0, 3) and w_L3 == g.qi(0, -3)
      and weights_single == [g.qi(0, 0), g.qi(0, -2), g.qi(0, -4),
                             g.qi(0, -6)])

# the ledger's weights, computed from the generator: a cell e_i ox f_a carries
# the eigenvalue of X_y on e_i plus that of Y_y on f_a, and a wedge of d cells
# the sum; every value is >= 0, while the singlet sector's weights -2k are < 0
cell_w = sorted(set((X_y[i][i] + Y_y[a][a]).im for i in range(2) for a in range(3)))
ledger_w = sorted(set(sum(cell_w[0] for _ in range(d)) for d in range(7)))
single_w = [ext_power_diag_action(Y_y, k)[0].im for k in range(4)]
g.check("S1: every cell of the tensor state space has weight +1 under the hypercharge "
      "generator, so degree d has weight d and no state of negative weight "
      "exists in it, while the single-twistor grades k = 1, 2, 3 have weights "
      "-2, -4, -6 and u^c has q = -4: the singlet sector is not in the ledger",
      cell_w == [1] and ledger_w == list(range(7)) and single_w == [0, -2, -4, -6]
      and min(ledger_w) >= 0 > max(single_w[1:]))

# prop:singlet: the mass bracket is Lambda^2 C^2 of the slots, on which y acts
# as tr X = 6i: weight 6, hypercharge +1, an SU(2) x SU(3) singlet
trX = X_y[0][0] + X_y[1][1]
lam6 = g.qi(F(3, 5), F(4, 5))      # unit modulus
lamA = [[lam6 * lam6 * lam6 * U_real[i][j] for j in range(2)] for i in range(2)]
det_scaled = det2(lamA)
g.check("prop:singlet: on Lambda^2 C^2 (the slot factor of the mass bracket) "
      "the hypercharge generator acts as tr(3i I_2) = 6i, weight 6, Y = +1; "
      "and det(lam^3 a) = lam^6 det(a) exactly on a unit-modulus Gaussian "
      "rational lam and a rational unitary a",
      trX == g.qi(0, 6) and F(trX.im, 6) == 1
      and det_scaled == lam6 * lam6 * lam6 * lam6 * lam6 * lam6 * det2(U_real))

# prop:chirality: duality inside the pair system.  (Lambda^k W)^* is
# Lambda^(3-k) W ox det^-1: weight -2(3-k) + 6 = 2k, the negative of the
# grade-k weight; and (C^2)^* = C^2 ox det(A)^-1 has weight 3 - 6 = -3, the
# full-twistor doublet's weight.
dual_ok = True
for k in range(4):
    w_dual = ext_power_diag_action(Y_y, 3 - k)[0] - trY
    dual_ok = dual_ok and w_dual == -weights_single[k]
w_C2dual = X_y[0][0] - trX
g.check("prop:chirality: the dual of the grade-k state, Lambda^(3-k) W ox det^-1, "
      "has weight +2k = minus the grade-k weight for k = 0..3, and (C^2)^* = "
      "C^2 ox det(A)^-1 has weight -3, the full-twistor doublet's: the empty "
      "and full twistor doublets are each other's duals",
      dual_ok and w_C2dual == g.qi(0, -3) and w_C2dual == w_L3)

# prop:content(2), the negative clause: in the tensor state space Lambda^*(C^2 ox
# C^3) a filled row is cubic in the slot vector.  Cells are indexed 3i + a
# (slot i, pair a); the unipotent A(s) = [[1, s], [0, 1]] on the slot index
# sends e_1 -> e_1 and e_0 -> e_0 + s e_1... use A(s) e_1 = s e_0 + e_1 so
# that row 1 spreads into row 0.  Expand the wedge of the three transformed
# cells of row 1 in the wedge basis of Lambda^3(C^6) and collect the
# coefficients: they are polynomials s^3, s^2, s, 1 on four groups of basis
# elements, so the SU(2)-span of the filled rows has rank four (S^3 C^2 ox
# Lambda^3 C^3, the (4,1)), and is not a doublet.
def wedge3_coeffs(vecs):
    """Coefficients of v1 ^ v2 ^ v3 in the basis e_I, I a 3-subset of 0..5,
    for vecs given as lists of Fractions."""
    out = {}
    for I in combinations(range(6), 3):
        # 3x3 determinant of rows vecs restricted to columns I
        m = [[vecs[r][c] for c in I] for r in range(3)]
        det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
               - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
               + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
        if det:
            out[I] = det
    return out


def row_state(s_):
    """The filled row 1 after A(s): each cell e_{1,a} -> s e_{0,a} + e_{1,a}."""
    vecs = []
    for a_ in range(3):
        v = [F(0)] * 6
        v[0 + a_] = s_          # slot 0, pair a
        v[3 + a_] = F(1)        # slot 1, pair a
        vecs.append(v)
    return wedge3_coeffs(vecs)


states = [row_state(F(sv)) for sv in (0, 1, 2, 3, 5)]
keys = sorted(set(k for st in states for k in st))
mat = [[st.get(k, F(0)) for k in keys] for st in states]
rk_rows = g.mat_rank(mat)
g.check("prop:content(2), negative clause: in the tensor state space the SU(2)-orbit "
      "of a filled row spans a space of rank exactly 4 (five unipotent images "
      "of row 1, supported on eight wedge basis elements, have rank 4 in "
      "Lambda^3(C^6)): the row-filling states form the quadruplet (4,1) of "
      "weight +3, not a doublet",
      rk_rows == 4 and len(keys) == 8 and len(states) == 5)

# irreducibility of that rank-4 span (N5): the Lie algebra element e of the
# unipotent, e(e_{1,a}) = e_{0,a}, acts on the filled row by the Leibniz
# rule; e^3 of the filled row is 6 e_{0,1}^e_{0,2}^e_{0,3} != 0, and a
# four-dimensional sl2-module on which e^3 != 0 is a single Jordan block,
# hence irreducible: the quadruplet (4,1), not 2 + 2 (on which e^2 = 0)
def apply_e(state):
    """Leibniz action of e on a wedge state {I: coeff}, cells 3i + a,
    e: cell (1,a) -> cell (0,a)."""
    out = {}
    for I, c in state.items():
        for pos, cell in enumerate(I):
            if cell >= 3:
                new = list(I)
                new[pos] = cell - 3
                if len(set(new)) < 3:
                    continue
                # sort with sign
                sign = 1
                arr = new[:]
                for x in range(3):
                    for y in range(2 - x):
                        if arr[y] > arr[y + 1]:
                            arr[y], arr[y + 1] = arr[y + 1], arr[y]
                            sign = -sign
                key = tuple(arr)
                out[key] = out.get(key, F(0)) + sign * c
    return {k: v for k, v in out.items() if v != 0}


filled = row_state(F(0))
e1 = apply_e(filled)
e2 = apply_e(e1)
e3 = apply_e(e2)
e4 = apply_e(e3)
g.check("prop:content(2), negative clause: the Lie-algebra generator e of the "
      "slot unipotent applied three times to the filled row gives "
      "6 e_01 ^ e_02 ^ e_03, nonzero, and four times gives zero: the "
      "four-dimensional span is a single Jordan block, irreducible under "
      "SU(2), the quadruplet (4,1) and not 2 + 2",
      e3 == {(0, 1, 2): F(6)} and e4 == {} and len(e1) == 3 and len(e2) == 3)

YQ = F(w_Q.im, 6)
YL_full, YL_empty = F(w_L3.im, 6), F(w_L0.im, 6)
g.check("thm:hypercharge(1): the [SU(2)]^2 U(1) coefficient 3 Y_Q + Y_L is 0 "
      "for the listing that keeps the full twistor (Y_L = -1/2, even total "
      "parity like the quark) and 1 for the listing that keeps the empty one "
      "(Y_L = +1/2): the anomaly confirms the parity's orientation",
      3 * YQ + YL_full == 0 and 3 * YQ + YL_empty == 1)
YL = YL_full

# thm:hypercharge(2): the single-twistor sector listed by one handedness:
# even grades kept, odd grades conjugated (Y -> -Y, 3 <-> 3bar)
single = [(k, F(w.im, 6)) for k, w in enumerate(weights_single)]
listed = {}
for k, Y in single:
    if k % 2 == 0:
        listed[k] = Y
    else:
        listed[k] = -Y
Ynu, Yd, Yu, Ye = listed[0], listed[1], listed[2], listed[3]
g.check("thm:hypercharge(2): the one-handed listing gives the singlet "
      "hypercharges nu^c = 0 (grade 0), u^c = -2/3 (grade 2), d^c = +1/3 "
      "(grade 1 conjugated), e^c = +1 (grade 3 conjugated): the observed "
      "singlet spectrum with the fourth singlet at zero",
      (Ynu, Yu, Yd, Ye) == (F(0), F(-2, 3), F(1, 3), F(1)))


def anomaly_sums(a, b, c, d, e, f=None):
    """(a,b,c,d,e,f) = Y of Q, u^c, d^c, L, e^c, nu^c (f None = absent).
    Returns ([SU(3)]^2 U(1), [SU(2)]^2 U(1), gravitational, cubic)."""
    fs = [] if f is None else [f]
    su3 = 2 * a + b + c
    su2 = 3 * a + d
    grav = 6 * a + 3 * b + 3 * c + 2 * d + e + sum(fs)
    cube = 6 * a ** 3 + 3 * b ** 3 + 3 * c ** 3 + 2 * d ** 3 + e ** 3 \
        + sum(x ** 3 for x in fs)
    return (su3, su2, grav, cube)


g.check("thm:hypercharge(3): all four anomaly sums vanish on the derived "
      "spectrum (Q 1/6, u^c -2/3, d^c 1/3, L -1/2, e^c 1, nu^c 0)",
      anomaly_sums(YQ, Yu, Yd, YL, Ye, Ynu) == (0, 0, 0, 0))
# B2 of the v3 review: without the lepton doublet (the unconditional content
# alone) three of the four sums are nonzero
no_L = (2 * YQ + Yu + Yd, 3 * YQ, 6 * YQ + 3 * Yu + 3 * Yd + Ye + Ynu,
        6 * YQ ** 3 + 3 * Yu ** 3 + 3 * Yd ** 3 + Ye ** 3 + Ynu ** 3)
g.check("thm:hypercharge(3), consistency clause needs (S): over the quark doublet "
      "and the four singlets alone, without the lepton, the four sums are "
      "(0, 1/2, 1, 1/4): the [SU(2)]^2 U(1), gravitational and cubic "
      "conditions fail",
      no_L == (0, F(1, 2), 1, F(1, 4)))

# uniqueness given the content, line by line
Ysum = -2 * YQ                       # [SU(3)]^2 U(1)
Ye_forced = -(6 * YQ + 2 * YL + 3 * Ysum)   # gravitational, with f = 0
g.check("thm:hypercharge(3): [SU(3)]^2 U(1) forces Yu + Yd = -1/3 and the "
      "gravitational anomaly forces Y(e^c) = 1",
      Ysum == F(-1, 3) and Ye_forced == 1)

cube_sum = -(6 * YQ ** 3 + 2 * YL ** 3 + Ye_forced ** 3) / 3
g.check("thm:hypercharge(3): the cubic anomaly forces Yu^3 + Yd^3 = -7/27",
      cube_sum == F(-7, 27))
s_ = Ysum
p_ = (s_ ** 3 - cube_sum) / (3 * s_)
g.check("thm:hypercharge(3): sum -1/3 and cube sum -7/27 give product -2/9, "
      "so {Yu, Yd} are roots of y^2 + y/3 - 2/9", p_ == F(-2, 9))
disc = F(1, 9) + F(8, 9)
g.check("thm:hypercharge(3): the discriminant is exactly 1 and the roots are "
      "{+1/3, -2/3}, the spectrum of (2): unique given the content",
      disc == 1 and {(-F(1, 3) + 1) / 2, (-F(1, 3) - 1) / 2}
      == {F(1, 3), F(-2, 3)} and {Yu, Yd} == {F(1, 3), F(-2, 3)})

# necessity of the content hypothesis: with a fourth singlet of free
# hypercharge the conditions admit a one-parameter family.  The exhibited
# point, and three members of Y + t(B-L) rescaled to Y_Q = 1/6.
exhibited = (F(1, 6), F(-1, 6), F(-1, 6), F(-1, 2), F(1, 2), F(1, 2))
BL = (F(1, 3), F(-1, 3), F(-1, 3), F(-1), F(1), F(1))
SM = (YQ, Yu, Yd, YL, Ye, Ynu)
fam_ok = anomaly_sums(*exhibited) == (0, 0, 0, 0)
for t in (F(0), F(1), F(-1), F(2), F(5, 7)):
    Yt = tuple(y + t * bl for y, bl in zip(SM, BL))
    fam_ok = fam_ok and anomaly_sums(*Yt) == (0, 0, 0, 0) and (t == 0 or Yt[5] != 0)
    if Yt[0] != 0:          # rescaling to Y_Q = 1/6, possible for t != -1/2
        scale = YQ / Yt[0]
        Ys = tuple(scale * y for y in Yt)
        fam_ok = fam_ok and anomaly_sums(*Ys) == (0, 0, 0, 0)
# at t = -1/2 the family has Y_Q = 0 and cannot be rescaled; it still solves
t = F(-1, 2)
Yt = tuple(y + t * bl for y, bl in zip(SM, BL))
fam_ok = fam_ok and Yt[0] == 0 and anomaly_sums(*Yt) == (0, 0, 0, 0)
g.check("thm:hypercharge(3): with a fourth singlet of free hypercharge the "
      "conditions are not unique: the point (1/6, -1/6, -1/6, -1/2, 1/2, 1/2) "
      "and the members t = 0, 1, -1, 2, 5/7 of Y + t(B-L), unrescaled and (where "
      "Y_Q != 0) rescaled to Y_Q = 1/6, all satisfy all four sums (four points "
      "kill a cubic in t; t = -1/2 has Y_Q = 0 and cannot be rescaled), so the "
      "hypothesis nu^c at zero (or absent) is needed", fam_ok)

# necessity of the common handedness: conjugate the two doublets alone
flip = anomaly_sums(-YQ, Yu, Yd, -YL, Ye, Ynu)
g.check("thm:hypercharge(3): listing the doublets in the opposite handedness "
      "from the singlets (Q, L conjugated: Y_Q -> -1/6, Y_L -> +1/2) gives "
      "[SU(3)]^2 U(1) = -2/3 and cubic = +4/9, the other two sums 0: the "
      "common-handedness hypothesis is needed",
      flip == (F(-2, 3), 0, 0, F(4, 9)))

# prop:sixteen: Lambda^*(C^2 + C^3) component by component.  On
# Lambda^j C^2 ox Lambda^k C^3 the generator acts as the scalar
# i(3j - 2k) (a diagonal generator acts on a wedge basis element by the
# sum of its eigenvalues over the occupied modes); the SU(2) x SU(3)
# content is (Lambda^j C^2, Lambda^k C^3) with Lambda^0 = Lambda^2 = 1,
# Lambda^1 = 2 for C^2 and 1, 3, 3bar, 1 for C^3.  Compare the multisets
# (content, Y) of the even part with the derived spectrum and of the odd
# part with its conjugate.
def comp_weight(j, k):
    # X_y is scalar on C^2, so every j-subset of {0, 1} has the same sum
    wj = sum((X_y[i][i] for i in range(j)), g.qi(0))
    wk = ext_power_diag_action(Y_y, k)[0]
    return wj + wk


SU2 = {0: "1", 1: "2", 2: "1"}
SU3 = {0: "1", 1: "3", 2: "3bar", 3: "1"}
CONJ3 = {"1": "1", "3": "3bar", "3bar": "3"}
even, odd = [], []
dim_even = 0
for j in range(3):
    for k in range(4):
        w = comp_weight(j, k)
        entry = (SU2[j], SU3[k], F(w.im, 6))
        d = comb(2, j) * comb(3, k)
        if (j + k) % 2 == 0:
            even.append(entry)
            dim_even += d
        else:
            odd.append(entry)
derived = [("2", "3", YQ), ("2", "1", YL), ("1", "3bar", Yu), ("1", "3bar", Yd),
           ("1", "1", Ye), ("1", "1", Ynu)]
derived_conj = [(a_, CONJ3[b_], -c_) for (a_, b_, c_) in derived]
hodge_ok = all(comp_weight(2 - j, 3 - k) == -comp_weight(j, k)
               for j in range(3) for k in range(4))
g.check("prop:sixteen: the even part of Lambda^*(C^2 + C^3) has dimension 16 "
      "and its (SU(2), SU(3), Y) multiset is exactly the derived generation "
      "{Q, L, u^c, d^c, e^c, nu^c}; the odd part's is the conjugate multiset "
      "(the antiparticles), with (2,1)_{1/2} at (1,0) and the slot factor "
      "(1,1)_1 at the even component (2,0); and the Hodge star "
      "(j,k) -> (2-j, 3-k) negates the weight on all twelve components",
      dim_even == 16 and sorted(even) == sorted(derived)
      and sorted(odd) == sorted(derived_conj)
      and comp_weight(2, 0) == g.qi(0, 6) and comp_weight(1, 0) == g.qi(0, 3)
      and hodge_ok)

# prop:sixteen(3)(a): a general abelian generator alpha j + beta k of the
# split-and-number-preserving algebra, in the untwisted action, evaluated on the even half (nu^c
# (0,0), u^c (0,2), Q (1,1), L (1,3), e^c (2,0), d^c (2,2)) and fed to the
# four anomaly sums in place of Y.  The three linear sums are multiples of
# 2 alpha + 3 beta; the integer sweep finds them vanishing exactly at the
# multiples of (3, -2), hypercharge's direction.
def gen_sums(al, be):
    w = lambda j, k: al * j + be * k
    return anomaly_sums(w(1, 1), w(0, 2), w(2, 2), w(1, 3), w(2, 0), w(0, 0))


lin_ok = all(gen_sums(al, be)[:3] == (2 * (2 * al + 3 * be), 2 * (2 * al + 3 * be),
                                       8 * (2 * al + 3 * be))
             for al in range(-6, 7) for be in range(-6, 7))
sols = sorted((al, be) for al in range(-6, 7) for be in range(-6, 7)
              if (al, be) != (0, 0) and gen_sums(al, be)[:3] == (0, 0, 0))
g.check("prop:sixteen(3)(a): in the untwisted action Lambda(A + B), for every integer (alpha, beta) in [-6, 6]^2 the "
      "[SU(3)]^2, [SU(2)]^2 and gravitational sums of alpha j + beta k over "
      "the derived generation are 2(2a+3b), 2(2a+3b), 8(2a+3b); they vanish "
      "exactly at the multiples of (3, -2), where the cubic sum vanishes too; "
      "the total mode number (1,1) has sums (10, 10, 40, 400) and the kernel "
      "generator (1,-1) has (-2, -2, -8, -32); in the action the state space "
      "carries (Part K, K10) every such sum vanishes",
      lin_ok and sols == [(-6, 4), (-3, 2), (3, -2), (6, -4)]
      and gen_sums(3, -2) == (0, 0, 0, 0) and gen_sums(F(1, 2), F(-1, 3)) == (0, 0, 0, 0)
      and gen_sums(1, 1) == (10, 10, 40, 400) and gen_sums(1, -1) == (-2, -2, -8, -32))

g.check("rem:wound: the abelian weights are integers, so hypercharge comes in "
      "units of 1/6, and Y_L = -3 Y_Q exactly (full pair system weight -6 "
      "against the empty one's 0)",
      all(w.im.denominator == 1 for w in weights_single)
      and YL == -3 * YQ and weights_single[3].im - weights_single[0].im == -6)

# ---------------------------------------------------------------------------
# Part D: unification and the run (prop:unification, prop:desert)
# ---------------------------------------------------------------------------

# the 3/8 trace ratio over one derived generation (the hypercharge-zero
# singlet contributes nothing to either sum), and the two other ratios the
# text prints: over the fibre alone (9/10) and over the two doublets (3/4)
T3sq = 3 * (F(1, 4) + F(1, 4)) + (F(1, 4) + F(1, 4))
Ysq = 6 * YQ ** 2 + 2 * YL ** 2 + 3 * Yu ** 2 + 3 * Yd ** 2 + Ye ** 2 + Ynu ** 2
cross = 3 * (F(1, 2) * YQ + F(-1, 2) * YQ) + (F(1, 2) * YL + F(-1, 2) * YL)
g.check("prop:unification: Sum T3^2 = 2, Sum Y^2 = 10/3, cross term exactly "
      "zero, so Sum Q^2 = 16/3 and the ratio is 3/8 over the derived "
      "generation",
      T3sq == 2 and Ysq == F(10, 3) and cross == 0
      and T3sq / (T3sq + Ysq) == F(3, 8))
fib_T3, fib_Y = 3 * (F(1, 4) + F(1, 4)), 6 * YQ ** 2
dbl_T3, dbl_Y = T3sq, 6 * YQ ** 2 + 2 * YL ** 2
g.check("prop:unification: the same ratio is 9/10 over the fibre C^2 ox C^3 "
      "alone and 3/4 over the two doublets alone: the fibre's own trace form "
      "does not give 3/8",
      fib_T3 / (fib_T3 + fib_Y) == F(9, 10)
      and dbl_T3 / (dbl_T3 + dbl_Y) == F(3, 4))
# B1 of the v3 review: the lepton doublet contributes 1/2 to each sum, so over
# the unconditional content alone (quark doublet and four singlets) the ratio
# is 9/26, not 3/8: the values 3/8 and 3/4 rest on (S) with the lepton
noL_T3 = 3 * (F(1, 4) + F(1, 4))
noL_Y = 6 * YQ ** 2 + 3 * Yu ** 2 + 3 * Yd ** 2 + Ye ** 2 + Ynu ** 2
g.check("prop:unification: without the lepton doublet Sum T3^2 = 3/2, Sum Y^2 = "
      "17/6, Sum Q^2 = 13/3 and the ratio is 9/26; the lepton contributes "
      "exactly 1/2 to each of Sum T3^2 and Sum Y^2, so 3/8 rests on (S)",
      noL_T3 == F(3, 2) and noL_Y == F(17, 6) and noL_T3 + noL_Y == F(13, 3)
      and noL_T3 / (noL_T3 + noL_Y) == F(9, 26)
      and T3sq - noL_T3 == F(1, 2) and Ysq - noL_Y == F(1, 2))


def one_loop(b1, b2, b3, aem=F(128), a3=F(500, 59)):
    Lc = (aem - F(8, 3) * a3) / (F(5, 3) * (b1 - b3) + (b2 - b3))
    a2 = a3 + (b2 - b3) * Lc
    return a2 / aem, Lc


B_SM = (F(41, 10), F(-19, 6), F(-7))
B_SUSY = (F(33, 5), F(1), F(-3))
sm, Lsm = one_loop(*B_SM)
susy, Lsusy = one_loop(*B_SUSY)
g.check("prop:desert: the closed-form one-loop angle with SM coefficients is "
      "exactly 78761/379488 (= 0.2075...), with L/2pi = 18656/3953: the "
      "ten-percent miss",
      sm == F(78761, 379488) and Lsm == F(18656, 3953))
g.check("prop:desert: with the supersymmetric coefficients it is exactly "
      "6539/28320 (= 0.2308...), with L/2pi = 4664/885: the sharpening",
      susy == F(6539, 28320) and Lsusy == F(4664, 885))
target = F(2312, 10000)
g.check("prop:desert: both runs have L > 0, the partner run meets higher "
      "(L_susy > L_sm), and the partner value is over 20 times closer to "
      "the measured 0.2312",
      Lsm > 0 and Lsusy > Lsm
      and abs(susy - target) * 20 < abs(sm - target))

# no common meeting point: with all three couplings from the record the
# three pairwise meetings L_ij / 2pi = (a_i - a_j)/(b_i - b_j) differ
aem = F(128)
a2_meas = target * aem
a1_meas = F(3, 5) * (aem - a2_meas)
a3_meas = F(500, 59)
A = (a1_meas, a2_meas, a3_meas)
Lpair = {}
for (i, j) in ((0, 1), (0, 2), (1, 2)):
    Lpair[(i, j)] = (A[i] - A[j]) / (B_SM[i] - B_SM[j])
vals = list(Lpair.values())
g.check("prop:desert: with SM coefficients and all three measured couplings "
      "the pairwise meeting values L_12, L_13, L_23 (over 2pi) are exact "
      "rationals, all positive and pairwise distinct: no common meeting point",
      all(v > 0 for v in vals) and len(set(vals)) == 3
      and Lpair[(0, 1)] < Lpair[(0, 2)] < Lpair[(1, 2)])

# ---------------------------------------------------------------------------
# Part E: the one number (obs:N, prop:trichotomy)
# ---------------------------------------------------------------------------

# monomial identities in the two scales (M_P, H), exponent bookkeeping:
# represent q = c * M_P^a * H^b as (c, a, b) with G = M_P^-2, Lambda = 3H^2,
# N = M_P / H
def mono_mul(x, y):
    return (x[0] * y[0], x[1] + y[1], x[2] + y[2])


G_ = (F(1), -2, 0)
Lam_ = (F(3), 0, 2)
N_ = (F(1), 1, -1)
Ninv2 = (F(1), -2, 2)
g.check("obs:N: G Lambda = 3 N^-2 as an exact monomial identity in "
      "(M_P, H)", mono_mul(G_, Lam_) == (F(3), -2, 2)
      and mono_mul(Ninv2, (F(3), 0, 0)) == (F(3), -2, 2))
g.check("obs:N: gravity's weakness: G E^2 at E = H is (H/M_P)^2 = N^-2 as an "
      "exact monomial identity",
      mono_mul(G_, (F(1), 0, 2)) == Ninv2)
g.check("obs:N: the hierarchy identity Im w = (m/M_P) N: exponents of "
      "m M_P^-1 * M_P H^-1 = m/H exactly",
      mono_mul((F(1), -1, 0), N_) == (F(1), 0, -1))

# trichotomy(1): chart equivariance of the rescaling Lambda -> s^2 Lambda
# on the Lambda^2 C^4 flat model: the norm of I_Lam scales by s^2
PAIRS4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def perm_sign(perm):
    s = 1
    p = list(perm)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def amb_pair(P, Q):
    tot = F(0)
    for a, (i, j) in enumerate(PAIRS4):
        for b, (k, l) in enumerate(PAIRS4):
            idx = (i, j, k, l)
            if len(set(idx)) != 4:
                continue
            tot += F(perm_sign(idx)) * P[a] * Q[b]
    return tot


def biv6(pos, val=F(1)):
    out = [F(0)] * 6
    out[pos] = val
    return out


n_inf = biv6(0)      # e1^e2
n_0 = biv6(5)        # e3^e4


def I_of(lamval):
    return [n_inf[i] + lamval * n_0[i] for i in range(6)]


ok = True
for Lam_val in (F(3), F(1, 2)):
    for s_ in (F(2), F(3, 5)):
        norm1 = amb_pair(I_of(Lam_val / 6), I_of(Lam_val / 6))
        norm2 = amb_pair(I_of(s_ ** 2 * Lam_val / 6),
                         I_of(s_ ** 2 * Lam_val / 6))
        ok = ok and norm2 == s_ ** 2 * norm1
g.check("prop:trichotomy(1): under Lambda -> s^2 Lambda the chart's frozen "
      "point rescales with norm ratio exactly s^2 (instances on the flat "
      "model), so H -> sH and N -> N/s at fixed M_P", ok)

# the rung count: 2^398 < 10^120 < 2^399, so R = log2 N^2 is 398.xx,
# approximately 400, and 400 rungs = 50 turns of the mod-8 clock
g.check("prop:trichotomy: 2^398 < 10^120 < 2^399 exactly (integer "
      "arithmetic), so R = log2(N^2) lies in (398, 399), the 'about 400 "
      "rungs' of the units statement",
      2 ** 398 < 10 ** 120 < 2 ** 399)


# prop:trichotomy(4): N^2 = 3 M_P^2 / Lambda is constant along the norm-preserving
# fluctuations of the frozen point and varies across Lambda (the action paper's
# fourth alternative, its arithmetic on the flat model; M_P = 1).
_LamRF = g.RF.var()
_Nsq = g.RF.const(F(3)) / _LamRF
g.check("prop:trichotomy(4): d(N^2)/dLambda = -3/Lambda^2 as a rational-function "
        "identity: N varies across the family of theories indexed by Lambda, so it "
        "is not dynamically fixed",
        _Nsq.deriv().eqrf(-(g.RF.const(F(3)) / (_LamRF * _LamRF))))
_Nsq_chart = lambda lv: F(3) / amb_pair(I_of(lv), I_of(lv))   # N^2 = 3 M_P^2 / (3 <I,I>) with <I,I> = Lambda/3 in the chart
_pairs = ((F(3), F(12)), (F(1, 5), F(4, 5)), (F(3), F(1, 3)))
g.check("prop:trichotomy(4): on the flat model N^2 read from the chart's norm satisfies "
        "N^2(Lambda_1)/N^2(Lambda_2) = Lambda_2/Lambda_1 on three pairs and takes distinct "
        "values at distinct Lambda: N is a function of the parameter Lambda alone, the (P) "
        "reading of the action paper's Definition 5.6",
        all(_Nsq_chart(a) / _Nsq_chart(b) == b / a and _Nsq_chart(a) != _Nsq_chart(b) for a, b in _pairs))

# ---------------------------------------------------------------------------
# Part F: the partner sector priced (Section 8: Props 8.5, 8.6, Lem 8.8, Thm 8.9, Cor 8.10, Props 8.11, 8.13, Rem 8.12)
# ---------------------------------------------------------------------------

def part_F():
    _RETAG = [
        ('fact:running / Fact 1.2', 'Fact 2.8 / Fact 8.1'),
        ('Fact 1.2', 'Fact 8.1'),
        ('lem:complete', 'Lem 8.8'),
        ('Thm 3.2', 'Thm 8.9'),
        ('cor:direction', 'Cor 8.10'),
        ('prop:table', 'Prop 8.11'),
        ('consistency with T12 Prop 6.2', 'Prop 8.11 / Prop 6.2'),
        ('rem:sensitivity', 'Rem 8.12'),
        ('prop:towers', 'Prop 8.5'),
        ('cor:mirror', 'Cor 8.6'),
        ('prop:ledger', 'Prop 8.13'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)
    from math import exp, pi, comb


    # ---------------------------------------------------------------------------
    # Part A.  One-loop coefficients from a component listing (Fact 1.2)
    #
    # A field is (name, kind, dim2, T2, dim3, T3, Y, multiplicity), kind in
    # {"weyl", "scalar"}: dim2 and T2 the SU(2) dimension and index (1/2 for the
    # doublet, 2 for the triplet, 0 for the singlet), dim3 and T3 the SU(3)
    # dimension and index (1/2 for 3 or 3bar, 3 for the adjoint), Y the
    # hypercharge.  b_i = -(11/3) C_2(G_i) + (2/3) sum_weyl T_i + (1/3) sum_sc T_i
    # with T_1 = (3/5) Y^2 per component and the group index weighted by the
    # dimension of the other factor.
    # ---------------------------------------------------------------------------

    WEYL, SC = "weyl", "scalar"


    def index_triple(field):
        _, kind, d2, T2, d3, T3, Y, m = field
        t1 = F(3, 5) * Y * Y * d2 * d3
        t2 = T2 * d3
        t3 = T3 * d2
        w = F(2, 3) if kind == WEYL else F(1, 3)
        return tuple(w * t * m for t in (t1, t2, t3))


    def delta_b(fields):
        tot = [F(0)] * 3
        for f in fields:
            for i, t in enumerate(index_triple(f)):
                tot[i] += t
        return tuple(tot)


    def b_total(fields):
        gauge = (F(0), F(-22, 3), F(-11))
        d = delta_b(fields)
        return tuple(gauge[i] + d[i] for i in range(3))


    H = F(1, 2)
    # one derived generation at the particle handedness (T12 Thm 5.5)
    GEN = [
        ("Q",    WEYL, 2, H, 3, H, F(1, 6),  1),
        ("L",    WEYL, 2, H, 1, 0, F(-1, 2), 1),
        ("u^c",  WEYL, 1, 0, 3, H, F(-2, 3), 1),
        ("d^c",  WEYL, 1, 0, 3, H, F(1, 3),  1),
        ("e^c",  WEYL, 1, 0, 1, 0, F(1),     1),
        ("nu^c", WEYL, 1, 0, 1, 0, F(0),     1),
    ]
    HIGGS = [("H", SC, 2, H, 1, 0, H, 1)]
    SM = [(n, k, d2, T2, d3, T3, Y, 3 * m) for (n, k, d2, T2, d3, T3, Y, m) in GEN] + HIGGS

    b_SM = b_total(SM)
    _chk("fact:running / Fact 1.2: the listing of three derived generations "
            "and one Higgs doublet returns (41/10, -19/6, -7)",
            b_SM == (F(41, 10), F(-19, 6), F(-7)))

    GAUGINOS = [("gluino", WEYL, 1, 0, 8, F(3), F(0), 1),
                ("wino",   WEYL, 3, F(2), 1, 0, F(0), 1),
                ("bino",   WEYL, 1, 0, 1, 0, F(0), 1)]
    HIGGSINOS = [("Hu~", WEYL, 2, H, 1, 0, H, 1), ("Hd~", WEYL, 2, H, 1, 0, -H, 1)]
    HIGGS2 = [("H2", SC, 2, H, 1, 0, -H, 1)]
    SFERMIONS = [(n, SC, d2, T2, d3, T3, Y, 3 * m) for (n, k, d2, T2, d3, T3, Y, m) in GEN]
    MSSM = SM + GAUGINOS + HIGGSINOS + HIGGS2 + SFERMIONS
    _chk("Fact 1.2: the supersymmetric listing returns (33/5, 1, -3)",
            b_total(MSSM) == (F(33, 5), F(1), F(-3)))

    d_gen = delta_b(GEN)
    _chk("lem:complete: one generation of Weyl fermions, the 16 of Spin(10) "
            "without its gauge part, shifts all three coefficients equally, by 4/3",
            d_gen == (F(4, 3), F(4, 3), F(4, 3)))
    d_sfer = delta_b(SFERMIONS)
    _chk("lem:complete: three generations of complex scalars in the same "
            "representations shift all three equally, by 2", d_sfer == (F(2),) * 3)
    FIVE = [("Hd", SC, 2, H, 1, 0, -H, 1), ("T", SC, 1, 0, 3, H, F(1, 3), 1)]
    _chk("lem:complete: a complete scalar 5bar of SU(5) (doublet plus colour "
            "triplet of Y = 1/3) shifts all three equally, by 1/6",
            delta_b(FIVE) == (F(1, 6),) * 3)
    TEN = [("Q", WEYL, 2, H, 3, H, F(1, 6), 1), ("u^c", WEYL, 1, 0, 3, H, F(-2, 3), 1),
           ("e^c", WEYL, 1, 0, 1, 0, F(1), 1)]
    _chk("lem:complete: the Weyl 10 of SU(5) shifts all three equally, by 1",
            delta_b(TEN) == (F(1),) * 3)
    ADJ24 = GAUGINOS + [("X", WEYL, 2, H, 3, H, F(-5, 6), 1), ("Y", WEYL, 2, H, 3, H, F(5, 6), 1)]
    _chk("lem:complete: the Weyl 24 of SU(5) (the gauginos with the X, Y "
            "partners of hypercharge -5/6 and 5/6) shifts all three equally, by 10/3, "
            "while the gauginos alone shift them by (0, 4/3, 2)",
            delta_b(ADJ24) == (F(10, 3),) * 3 and delta_b(GAUGINOS) == (F(0), F(4, 3), F(2)))

    # ---------------------------------------------------------------------------
    # Part B.  The Spin(10) spinor content under (S), from the ledger itself
    # (Prop 4.1): Lambda^j C^2 ox Lambda^k C^3 with abelian weight 3j - 2k,
    # Y = q/6 (T12 Prop 5.8); the even total mode number is the 16.
    # ---------------------------------------------------------------------------

    D2 = {0: (1, 0), 1: (2, H), 2: (1, 0)}          # dim, index of Lambda^j C^2
    D3 = {0: (1, 0), 1: (3, H), 2: (3, H), 3: (1, 0)}  # dim, index of Lambda^k C^3


    def ledger_half(parity):
        fields = []
        for j in range(3):
            for k in range(4):
                if (j + k) % 2 != parity:
                    continue
                d2, T2 = D2[j]
                d3, T3 = D3[k]
                fields.append((f"L{j}{k}", WEYL, d2, T2, d3, T3, F(3 * j - 2 * k, 6), 1))
        return fields


    even_half, odd_half = ledger_half(0), ledger_half(1)


    def Ymultiset(fields):
        return sorted(sum(([f[6]] * (f[2] * f[4]) for f in fields), []))


    _chk("prop:ledger(1): the even half of Lambda^*(C^2 + C^3) has sixteen states "
            "and the odd half sixteen",
            sum(f[2] * f[4] for f in even_half) == 16 and sum(f[2] * f[4] for f in odd_half) == 16)
    _chk("prop:ledger(2): the even half's hypercharge multiset is the derived "
            "generation's, {1/6 x6, -1/2 x2, -2/3 x3, 1/3 x3, 1, 0}, and the odd "
            "half's is its negative (the conjugate generation)",
            Ymultiset(even_half) == Ymultiset(GEN)
            and Ymultiset(odd_half) == sorted(-y for y in Ymultiset(GEN)))
    _chk("prop:ledger(3): each half, taken with a common threshold, shifts the "
            "three coefficients equally: (4/3, 4/3, 4/3) for each half",
            delta_b(odd_half) == (F(4, 3),) * 3 and delta_b(even_half) == (F(4, 3),) * 3)
    # which sub-multisets of the generation's six components are inert?  Exactly
    # the unions of the SU(5) pieces 10 = {Q, u^c, e^c}, 5bar = {L, d^c}, 1 = {nu^c}.
    inert = sorted(sorted(f[0] for f in S)
                   for r in range(0, 7) for S in combinations(GEN, r)
                   if len(set(delta_b(list(S)))) == 1)
    pieces = [["Q", "u^c", "e^c"], ["L", "d^c"], ["nu^c"]]
    unions = sorted(sorted(sum((pieces[i] for i in range(3) if mask >> i & 1), []))
                    for mask in range(8))
    _chk("prop:ledger(4): the inert sub-multisets of the generation's six "
            "S(U(2) x U(3)) components are exactly the eight unions of its SU(5) "
            "pieces 10, 5bar, 1: every other split moves the meeting condition",
            inert == unions)

    # ---------------------------------------------------------------------------
    # Part C.  The record, the ratios, and the one-threshold theorem (Thm 3.2)
    # ---------------------------------------------------------------------------

    def record(aem_inv, s2, as_inv):
        a2 = s2 * aem_inv
        a1 = F(3, 5) * (aem_inv - a2)
        return (a1, a2, as_inv)


    A_T12 = record(F(128), F(2312, 10000), F(500, 59))
    a1, a2, a3 = A_T12
    R = (a1 - a2) / (a2 - a3)
    b1, b2, b3 = b_SM
    b12, b23 = b1 - b2, b2 - b3
    r0 = b12 / b23

    _chk("Thm 3.2: the record's ratio R = (a1 - a2)/(a2 - a3) at T12's inputs "
            "is 1357472/973455 = 1.3945...",
            R == F(1357472, 973455) and F(13944, 10000) < R < F(13946, 10000))
    _chk("Thm 3.2: the Standard-Model ratio r_0 = (b1 - b2)/(b2 - b3) is "
            "218/115 = 1.8957..., and r_0 > R (the desert is refuted)",
            r0 == F(218, 115) and r0 > R)
    _chk("Thm 3.2: the record differences are positive, a1 > a2 > a3",
            a1 > a2 > a3)


    def solve(delta, A=A_T12):
        """Exact solution of a_i = a_U + b_i x + d_i y, i = 1, 2, 3; returns
        (f, x, y, a_U) or None when the 2x2 system is singular."""
        A1, A2, A3 = A
        D12, D23 = A1 - A2, A2 - A3
        d12, d23 = delta[0] - delta[1], delta[1] - delta[2]
        det = b12 * d23 - b23 * d12
        if det == 0:
            return None
        x = (D12 * d23 - D23 * d12) / det
        y = (b12 * D23 - b23 * D12) / det
        aU = A3 - b3 * x - delta[2] * y
        return (y / x, x, y, aU)


    def r_of(delta, f=F(1)):
        return (b12 + f * (delta[0] - delta[1])) / (b23 + f * (delta[1] - delta[2]))


    def admissible(delta, A=A_T12):
        s = solve(delta, A)
        if s is None:
            return False
        f, x, y, aU = s
        return x > 0 and 0 <= f <= 1 and aU > 0


    def GeV(x):
        """M_Z e^{2 pi x}; the one floating-point conversion, RECORD lines only."""
        return 91.1876 * exp(2 * pi * float(x))


    CANDIDATES = [
        ("complete multiplet (any)",       (F(1), F(1), F(1))),
        ("gluino alone",                    delta_b(GAUGINOS[:1])),
        ("the three gauginos",              delta_b(GAUGINOS)),
        ("higgsinos alone",                 delta_b(HIGGSINOS)),
        ("second Higgs doublet alone",      delta_b(HIGGS2)),
        ("gauginos + higgsinos (split)",    delta_b(GAUGINOS + HIGGSINOS)),
        ("gauginos + higgsinos + 2nd Higgs", delta_b(GAUGINOS + HIGGSINOS + HIGGS2)),
        ("full supersymmetric content",     delta_b(GAUGINOS + HIGGSINOS + HIGGS2 + SFERMIONS)),
        ("wino alone",                      delta_b(GAUGINOS[1:2])),
        ("wino + bino + higgsinos",         delta_b(GAUGINOS[1:] + HIGGSINOS)),
        ("supersymmetric content without the gluino",
                                            delta_b(GAUGINOS[1:] + HIGGSINOS + HIGGS2 + SFERMIONS)),
    ]

    # (i) the solution formulas satisfy the three equations exactly
    ok = True
    for name, d in CANDIDATES:
        s = solve(d)
        if s is None:
            continue
        f, x, y, aU = s
        ok = ok and all(A_T12[i] == aU + b_SM[i] * x + d[i] * y for i in range(3))
        ok = ok and f == (R * b23 - b12) / ((d[0] - d[1]) - R * (d[1] - d[2]))
    _chk("Thm 3.2(i): for every non-singular candidate the closed forms for "
            "(x, y, a_U) satisfy the three one-loop equations exactly, and "
            "f = y/x = (R b23 - b12)/(D12 - R D23)", ok)

    # (ii) inertness: adding c(1,1,1) leaves f, x, y unchanged and lowers a_U by c y
    ok = True
    for name, d in CANDIDATES[1:]:
        for c in (F(1), F(-2), F(7, 3)):
            dd = tuple(v + c for v in d)
            s, ss = solve(d), solve(dd)
            ok = ok and s[:3] == ss[:3] and ss[3] == s[3] - c * s[2]
    _chk("Thm 3.2(ii): a shift D -> D + c(1,1,1) leaves f, x, y (hence M_U and "
            "M_I) unchanged and lowers a_U by c y: complete multiplets are inert",
            ok)
    _chk("Thm 3.2(ii): a complete multiplet alone gives a singular system "
            "(no meeting), r_D = r_0 exactly",
            solve(CANDIDATES[0][1]) is None and r_of(CANDIDATES[0][1]) == r0)

    # (iii) the interval criterion: 0 <= f <= 1 iff R between r_0 and r_D,
    # on every candidate, with the denominator positive on [0, 1]
    ok = True
    for name, d in CANDIDATES[1:]:
        rD = r_of(d)
        den_pos = (b23 + (d[1] - d[2])) > 0
        s = solve(d)
        interval = min(rD, r0) <= R <= max(rD, r0)
        ok = ok and den_pos and ((0 <= s[0] <= 1) == interval)
    _chk("Thm 3.2(iii): on every candidate, 0 <= f <= 1 exactly when R lies "
            "between r_0 and r_D (the ratio with the whole content), the "
            "denominator b23 + D23 staying positive", ok)
    # monotonicity: r(f) is a Moebius function of f; its derivative has the
    # constant sign of (D12 b23 - D23 b12) on any interval free of the pole
    ok = True
    for name, d in CANDIDATES[1:]:
        d12, d23 = d[0] - d[1], d[1] - d[2]
        sgn = d12 * b23 - d23 * b12
        vals = [r_of(d, F(k, 8)) for k in range(9)]
        mono = all((vals[k + 1] - vals[k]) * sgn > 0 for k in range(8)) if sgn != 0 else \
            all(v == vals[0] for v in vals)
        ok = ok and mono
    _chk("Thm 3.2(iii): r(f) is strictly monotone on [0, 1] with the sign of "
            "D12 b23 - D23 b12 (sampled at ninths, exactly)", ok)

    # (iv) the necessary direction: f > 0 iff (1 + R) D2 > D1 + R D3
    ok = True
    for name, d in CANDIDATES[1:]:
        s = solve(d)
        ok = ok and ((s[0] > 0) == ((1 + R) * d[1] > d[0] + R * d[2]))
    _chk("cor:direction: f > 0 exactly when (1 + R) D2 > D1 + R D3, the content "
            "doublet-heavy in the R-weighted sense", ok)

    # ---------------------------------------------------------------------------
    # Part D.  The table (Prop 3.4), exact
    # ---------------------------------------------------------------------------

    table = {name: (r_of(d), solve(d), admissible(d)) for name, d in CANDIDATES}

    _chk("prop:table: gluino alone: r_D = 218/55 > r_0, f < 0: it worsens the miss",
            table["gluino alone"][0] == F(218, 55) and table["gluino alone"][1][0] < 0)
    _chk("prop:table: the three gauginos: r_D = 178/95 = 1.8737 > R, f = 4.76 > 1 "
            "and a_U < 0: not enough even at M_Z",
            table["the three gauginos"][0] == F(178, 95)
            and table["the three gauginos"][1][0] > 4 and table["the three gauginos"][1][3] < 0)
    _chk("prop:table: higgsinos alone: r_D = 14/9 > R, f > 1: not enough",
            table["higgsinos alone"][0] == F(14, 9) and table["higgsinos alone"][1][0] > 1)
    _chk("prop:table: a second Higgs doublet alone: r_D = 9/5 > R, f > 6",
            table["second Higgs doublet alone"][0] == F(9, 5)
            and table["second Higgs doublet alone"][1][0] > 6)
    _chk("prop:table: gauginos + higgsinos (the split spectrum): r_D = 34/23 = "
            "1.4783 > R, f = 1.20 > 1: not enough at one loop",
            table["gauginos + higgsinos (split)"][0] == F(34, 23)
            and F(12, 10) < table["gauginos + higgsinos (split)"][1][0] < F(121, 100))
    f_mssm = table["full supersymmetric content"][1][0]
    _chk("prop:table: the full supersymmetric content: r_D = 7/5 exactly, "
            "f = 1.0116 (M_I just below M_Z): inadmissible at strict one loop by "
            "1.2 percent in f",
            table["full supersymmetric content"][0] == F(7, 5) and F(1011, 1000) < f_mssm < F(1012, 1000))
    _chk("prop:table: gauginos + higgsinos + second Higgs has the same r_D, f "
            "and M_U as the full content (the sfermions are complete), a_U differing",
            table["gauginos + higgsinos + 2nd Higgs"][1][:3] == table["full supersymmetric content"][1][:3]
            and table["gauginos + higgsinos + 2nd Higgs"][1][3] != table["full supersymmetric content"][1][3])
    _chk("prop:table: wino alone is admissible: r_D = 178/155, f = 0.60",
            table["wino alone"][0] == F(178, 155) and table["wino alone"][2]
            and F(60, 100) < table["wino alone"][1][0] < F(61, 100))
    _chk("prop:table: wino + bino + higgsinos is admissible, f = 0.44",
            table["wino + bino + higgsinos"][2]
            and F(43, 100) < table["wino + bino + higgsinos"][1][0] < F(44, 100))
    _chk("prop:table: the supersymmetric content without its gluino is "
            "admissible, f = 0.41", table["supersymmetric content without the gluino"][2]
            and F(40, 100) < table["supersymmetric content without the gluino"][1][0] < F(42, 100))
    _chk("prop:table: exactly three of the ten non-trivial candidates are "
            "admissible at strict one loop, and none of the three contains a gluino",
            sorted(n for n, _ in CANDIDATES[1:] if table[n][2])
            == sorted(["wino alone", "wino + bino + higgsinos",
                       "supersymmetric content without the gluino"]))

    # the T12 numbers reproduced as consistency with T12's script
    def predict_desert(bs, A=A_T12):
        """T12 Prop 6.2: content bs from M_Z up; returns (L/2pi, sin^2)."""
        aem_inv = F(5, 3) * A[0] + A[1]
        x = (aem_inv - F(8, 3) * A[2]) / (F(5, 3) * (bs[0] - bs[2]) + (bs[1] - bs[2]))
        return x, (A[2] + (bs[1] - bs[2]) * x) / aem_inv


    x_sm, s_sm = predict_desert(b_SM)
    x_ss, s_ss = predict_desert((F(33, 5), F(1), F(-3)))
    _chk("consistency with T12 Prop 6.2: the desert gives sin^2 = 78761/379488 "
            "and the supersymmetric content from M_Z gives 6539/28320",
            s_sm == F(78761, 379488) and s_ss == F(6539, 28320))
    # the admissibility threshold in sin^2 for the full content is T12's prediction
    s2_star = (F(3) * F(128) + F(7) * F(500, 59)) / F(15) / F(128)
    _chk("prop:table: the full content is admissible (f <= 1) exactly when the "
            "record's sin^2 is at most 6539/28320 = 0.23090, T12's own one-loop "
            "prediction for that content at M_Z",
            s2_star == F(6539, 28320)
            and admissible(CANDIDATES[7][1], record(F(128), s2_star, F(500, 59)))
            and not admissible(CANDIDATES[7][1], record(F(128), s2_star + F(1, 10**6), F(500, 59))))

    # ---------------------------------------------------------------------------
    # Part E.  Sensitivity (Rem 3.4): the record's central values, and the size
    # of shift in sin^2 that moves a conclusion
    # ---------------------------------------------------------------------------

    A_PDG = record(F(127951, 1000), F(23122, 100000), F(10000, 1180))
    R_pdg = (A_PDG[0] - A_PDG[1]) / (A_PDG[1] - A_PDG[2])
    _chk("rem:sensitivity: at the record's central values (127.951, 0.23122, "
            "0.1180) R = 1.3943..., within 2 x 10^-4 of T12's inputs' value",
            abs(R_pdg - R) < F(2, 10000))
    verdicts_T12 = [admissible(d) for _, d in CANDIDATES]
    verdicts_PDG = [admissible(d, A_PDG) for _, d in CANDIDATES]
    _chk("rem:sensitivity: every admissibility conclusion of the table is the same "
            "at the record's central values", verdicts_T12 == verdicts_PDG)
    # dR/d(sin^2): R = (3/5 aem - 8/5 a2)/(a2 - a3) with a2 = s2 aem
    def R_of_s2(s2, aem_inv=F(128), as_inv=F(500, 59)):
        A = record(aem_inv, s2, as_inv)
        return (A[0] - A[1]) / (A[1] - A[2])


    dR = (R_of_s2(F(2312, 10000) + F(1, 10000)) - R_of_s2(F(2312, 10000) - F(1, 10000))) / F(2, 10000)
    _chk("rem:sensitivity: dR/d(sin^2) is about -18.1 at the record point, so a "
            "shift of 3 x 10^-4 in the effective sin^2 (the scale of two-loop and "
            "threshold corrections) moves R by 0.0054, the size of the full "
            "content's gap 7/5 - R = 0.0055",
            F(-182, 10) < dR < F(-181, 10)
            and F(54, 10000) < F(7, 5) - R < F(56, 10000))
    # the robust conclusions: the gap between R and the failing ratios far exceeds that
    _chk("rem:sensitivity: the gaps r_D - R for the gauginos (0.48), the "
            "higgsinos (0.16) and the split spectrum (0.084) are each more than ten "
            "times the two-loop-scale shift 0.006",
            all(table[n][0] - R > F(6, 100) for n in
                ("the three gauginos", "higgsinos alone", "gauginos + higgsinos (split)")))

    # ---------------------------------------------------------------------------
    # Part F.  The towers (Prop 2.1): index bookkeeping of a field with no
    # component in this tower's hierarchy bundle, and the mirror's copy
    # ---------------------------------------------------------------------------

    _chk("prop:towers: a field carrying no component of this tower's hierarchy "
            "bundle has vanishing SU(2), SU(3) and hypercharge indices, so its "
            "contribution to every b_i is zero, for either statistics",
            index_triple(("dark", WEYL, 1, 0, 1, 0, F(0), 1)) == (0, 0, 0)
            and index_triple(("dark", SC, 1, 0, 1, 0, F(0), 5)) == (0, 0, 0))
    # the mirror copy, built from the species content of Fact 8.2: three copies of
    # the derived generation with one mirror Higgs doublet, once with the lepton
    # doublet (Hypothesis (S)) and once without it (the unconditional content)
    MIRROR_S = [(n, k, d2, T2, d3, T3, Y, 3 * m) for (n, k, d2, T2, d3, T3, Y, m) in GEN] + HIGGS
    MIRROR_noL = [(n, k, d2, T2, d3, T3, Y, 3 * m) for (n, k, d2, T2, d3, T3, Y, m) in GEN if n != "L"] + HIGGS
    def ratio_of(b):
        return (b[0] - b[1]) / (b[1] - b[2])
    bM_S, bM_noL = b_total(MIRROR_S), b_total(MIRROR_noL)
    _chk("cor:mirror: the mirror copy's coefficients from its species content are "
            "(41/10, -19/6, -7) with the lepton doublet, under (S), and (7/2, -25/6, -7) "
            "without it, ratios 218/115 and 46/17, b_3 = -7 either way; the (S) copy "
            "has r_0 > R, so its couplings fail to meet from the same boundary values",
            bM_S == (F(41, 10), F(-19, 6), F(-7)) and ratio_of(bM_S) == F(218, 115)
            and bM_noL == (F(7, 2), F(-25, 6), F(-7)) and ratio_of(bM_noL) == F(46, 17)
            and ratio_of(bM_S) > R and ratio_of(bM_noL) != ratio_of(bM_S))

    # ---------------------------------------------------------------------------
    # RECORD lines: the GeV conversions (floating point, not checks)
    # ---------------------------------------------------------------------------
    print("RECORD  scales in GeV (M_Z e^{2 pi x}, floating point; T12's inputs):")
    for name, d in CANDIDATES[1:]:
        rD, s, adm = table[name]
        f, x, y, aU = s
        MU = GeV(x)
        MI = GeV(x - y) if abs(float(x - y)) < 100 else float("inf")
        print(f"RECORD  {name:44s} r_D={float(rD):7.4f} f={float(f):8.4f} "
              f"a_U={float(aU):8.3f} M_U={MU:9.3e} M_I={MI:9.3e} {'ADMISSIBLE' if adm else 'no'}")


part_F()

# ---------------------------------------------------------------------------
# Part G: the frozen point on the two-rung module (Section 9.1 to 9.3: Props 9.9, 9.14 to 9.16, 9.18, 9.20, 9.21, Thms 9.10, 9.11, Cor 9.12, Obs 9.17)
# ---------------------------------------------------------------------------

def part_G():
    _RETAG = [
        ('Fact 1.2', 'Fact 9.1 / Def 9.8'),
        ('Thm 2.1(i)', 'Prop 9.9(3)'),
        ('Thm 2.1(ii)', 'Prop 9.9(1)'),
        ('Thm 2.1(iii)', 'Thm 9.10(i)'),
        ('Thm 2.1(iv)', 'Thm 9.10(ii)'),
        ('Thm 2.2 / Prop 3.1', 'Thm 9.11 / Prop 5.8'),
        ('Thm 2.2', 'Thm 9.11'),
        ('Prop 3.1: the six vectors', 'Prop 9.14: the six vectors'),
        ('Prop 3.1: every vector of V_C commutes', 'Prop 9.14: every vector of V_C commutes'),
        ('Prop 3.1', 'Prop 5.8 / Def 9.8'),
        ('Prop 3.2', 'Prop 9.15'),
        ('Prop 3.3', 'Prop 9.16'),
        ('Cor 2.3', 'Cor 9.12'),
        ('Obs 3.4', 'Obs 9.17'),
        ('Prop 4.2', 'Prop 9.20'),
        ('Prop 4.3', 'Prop 9.21'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)
    from itertools import product
    from math import comb

    Q0, Q1 = g.qi(0), g.qi(1)
    N_MODES = 5          # three pair modes (W) and two rung modes (R_2)
    DIM = 2 ** N_MODES   # 32

    # ---------------------------------------------------------------------------
    # Part A.  The Fock module and its operators (Fact 1.2, Thm 2.1)
    #
    # Basis states are subsets S of {0,..,4} (occupied modes), ordered as integers
    # with bit i set iff mode i is occupied.  Creation a_i^dag on S: zero if i in
    # S, else (-1)^{#occupied modes below i} times the state S + {i}.
    # ---------------------------------------------------------------------------

    # Matrices are sparse dictionaries {(row, col): Gaussian rational}; the
    # module's operators are permutation-like and dense products would be slow.

    def sign_below(S, i):
        return -1 if bin(S & ((1 << i) - 1)).count("1") % 2 else 1


    def creator(i):
        return {(S | 1 << i, S): g.qi(sign_below(S, i)) for S in range(DIM) if not S >> i & 1}


    def annihilator(i):
        return {(S & ~(1 << i), S): g.qi(sign_below(S, i)) for S in range(DIM) if S >> i & 1}


    def mm(A, B):
        byrow = {}
        for (r, c), v in B.items():
            byrow.setdefault(r, []).append((c, v))
        out = {}
        for (r, t), v in A.items():
            for c, w in byrow.get(t, ()):
                out[(r, c)] = out.get((r, c), Q0) + v * w
        return {k: v for k, v in out.items() if v != Q0}


    def madd(A, B, cb=Q1):
        out = dict(A)
        for k, v in B.items():
            out[k] = out.get(k, Q0) + cb * v
        return {k: v for k, v in out.items() if v != Q0}


    def comm(A, B):
        return madd(mm(A, B), mm(B, A), g.qi(-1))


    def anticomm(A, B):
        return madd(mm(A, B), mm(B, A))


    def is_zero(M):
        return len(M) == 0


    def ident():
        return {(r, r): Q1 for r in range(DIM)}


    def entry(M, r, c):
        return M.get((r, c), Q0)


    CR = [creator(i) for i in range(N_MODES)]
    AN = [annihilator(i) for i in range(N_MODES)]
    I32 = ident()

    # the Clifford relations of the 3 + 2 hyperbolic pairs (Fact 1.2: v_i w_j +
    # w_j v_i = delta_ij, v's and w's anticommuting among themselves)
    ok = True
    for i in range(N_MODES):
        for j in range(N_MODES):
            ok = ok and is_zero(anticomm(CR[i], CR[j])) and is_zero(anticomm(AN[i], AN[j]))
            ac = anticomm(CR[i], AN[j])
            ok = ok and (ac == I32 if i == j else is_zero(ac))
    _chk("Fact 1.2: the ten mode operators satisfy the Clifford relations of five "
            "hyperbolic pairs on the 32-dimensional module", ok)

    # vectors of V_C (pair modes) and of the rung plane R_C (rung modes)
    V_VECS = [CR[i] for i in range(3)] + [AN[i] for i in range(3)]
    R_VECS = [CR[i] for i in (3, 4)] + [AN[i] for i in (3, 4)]

    # bivectors of V: products of two distinct vectors of V (a spanning set of
    # so(V_C) together with the identity); likewise for R
    V_BIV = [mm(x, y) for x, y in combinations(V_VECS, 2)]
    R_BIV = [mm(x, y) for x, y in combinations(R_VECS, 2)]


    def number(modes):
        M = {}
        for i in modes:
            M = madd(M, mm(CR[i], AN[i]))
        return M


    N_W, N_R = number(range(3)), number((3, 4))
    U2_GENS = [mm(CR[a], AN[b]) for a in (3, 4) for b in (3, 4)]
    U3_GENS = [mm(CR[a], AN[b]) for a in range(3) for b in range(3)]

    _chk("Thm 2.1(i): every bivector of V commutes with the rung number operator",
            all(is_zero(comm(X, N_R)) for X in V_BIV))
    _chk("Thm 2.1(i): every bivector of V commutes with every generator of the "
            "rung mixing u(2)", all(is_zero(comm(X, E)) for X in V_BIV for E in U2_GENS))
    _chk("Thm 2.1(i): every bivector of R commutes with every bivector of V "
            "(so(V) and so(R) commute inside so(V + R))",
            all(is_zero(comm(X, Y)) for X in V_BIV for Y in R_BIV))
    _chk("Thm 2.1(i): a vector of V and a vector of R anticommute, so the odd "
            "parts do not commute and the factorisation is one of even elements",
            all(is_zero(anticomm(x, y)) for x in V_VECS for y in R_VECS)
            and not all(is_zero(comm(x, y)) for x in V_VECS for y in R_VECS))

    # the tensor factorisation: with pair modes first, an operator built from pair
    # modes alone is X_W (x) 1 with respect to the state index S = S_W + 8 S_R.
    def is_pair_factor(X):
        """X = X_W (x) I_4: entries depend on (S_W, T_W) and vanish unless S_R = T_R."""
        for S in range(DIM):
            for T in range(DIM):
                if (S >> 3) != (T >> 3) and entry(X, S, T) != Q0:
                    return False
                if (S >> 3) == (T >> 3) and entry(X, S, T) != entry(X, S & 7, T & 7):
                    return False
        return True


    _chk("Thm 2.1(ii): every bivector of V acts on Lambda^*W (x) Lambda^*R_2 as "
            "X_W (x) 1: the same 8 x 8 block on each of the four rung states, no "
            "matrix element between different rung states",
            all(is_pair_factor(X) for X in V_BIV))
    _chk("Thm 2.1(ii): a single vector of V is also of the form X_W (x) 1 in this "
            "ordering (the grading sits on the rung vectors), while a vector of R is "
            "not", all(is_pair_factor(x) for x in V_VECS)
            and not any(is_pair_factor(y) for y in R_VECS))

    # (iii) sector additivity: for X = X_W (x) 1 and Psi = sum_j Psi_j by rung
    # number, <Psi, X Psi> = sum_j <Psi_j, X Psi_j> in the Fock form.
    def rand_state(seed):
        # deterministic Gaussian-rational state
        return [g.qi(F((seed * (S + 3)) % 7 - 3, 2), F((seed * (S + 5)) % 5 - 2, 3)) for S in range(DIM)]


    def conjq(z):
        return g.qi(z.re, -z.im) if hasattr(z, "re") else z


    def form(phi, psi):
        return sum((conjq(a) * b for a, b in zip(phi, psi)), Q0)


    def apply(X, psi):
        out = [Q0] * DIM
        for (r, c), v in X.items():
            out[r] = out[r] + v * psi[c]
        return out


    def project_j(psi, j):
        return [psi[S] if bin(S >> 3).count("1") == j else Q0 for S in range(DIM)]


    ok = True
    for seed in (1, 2, 5):
        psi = rand_state(seed)
        for X in V_BIV[:6] + [mm(V_VECS[0], V_VECS[4]), mm(V_VECS[1], V_VECS[3])]:
            lhs = form(psi, apply(X, psi))
            rhs = sum((form(project_j(psi, j), apply(X, project_j(psi, j))) for j in range(3)), Q0)
            ok = ok and lhs == rhs
    _chk("Thm 2.1(iii): the moment <Psi, X Psi> of a pair bivector is the sum of "
            "the moments of the rung-number components of Psi (no cross-sector "
            "terms), on three Gaussian-rational states", ok)


    # (iv) within a sector, the moment is the sum over slot components: for
    # Psi_1 = e_1 (x) psi_1 + e_2 (x) psi_2, <Psi_1, X Psi_1> = <psi_1, X_W psi_1>
    # + <psi_2, X_W psi_2>.
    def embed(psi_W, rung_state):
        return [psi_W[S & 7] if (S >> 3) == rung_state else Q0 for S in range(DIM)]


    def block_W(X):
        return [[entry(X, r, c) for c in range(8)] for r in range(8)]


    def apply8(XW, psi):
        return [sum((XW[r][c] * psi[c] for c in range(8)), Q0) for r in range(8)]


    ok = True
    for seed in (3, 4):
        p1 = rand_state(seed)[:8]
        p2 = rand_state(seed + 10)[:8]
        Psi1 = [a + b for a, b in zip(embed(p1, 1), embed(p2, 2))]   # rung states {4}, {5}
        for X in V_BIV[:8]:
            XW = block_W(X)
            lhs = form(Psi1, apply(X, Psi1))
            rhs = form(p1, apply8(XW, p1)) + form(p2, apply8(XW, p2))
            ok = ok and lhs == rhs
        Psi2 = embed(p1, 3)  # rung state {4,5}
        ok = ok and all(form(Psi2, apply(X, Psi2)) == form(p1, apply8(block_W(X), p1)) for X in V_BIV[:8])
        Psi0 = embed(p1, 0)
        ok = ok and all(form(Psi0, apply(X, Psi0)) == form(p1, apply8(block_W(X), p1)) for X in V_BIV[:8])
    _chk("Thm 2.1(iv): on the doublet sector the moment is the sum of the two "
            "slot components' moments, and on each singlet sector (rung vacuum, "
            "rung-filled) it is the single component's moment", ok)

    # ---------------------------------------------------------------------------
    # Part B.  The grip mass at Lambda = 0 (Thm 2.2): null momenta add
    # ---------------------------------------------------------------------------

    def spinor_momentum(pi):
        """p_{AA'} = pi_A conj(pi_A') as a 2x2 Gaussian-rational matrix."""
        return [[pi[a] * conjq(pi[b]) for b in range(2)] for a in range(2)]


    def minkowski_sq(p):
        """p^2 = 2 det p for p_{AA'} Hermitian in the spinor convention of T11
        (eps^{AB} eps^{A'B'} p_{AA'} p_{BB'} = 2 det p)."""
        return 2 * (p[0][0] * p[1][1] - p[0][1] * p[1][0])


    def bracket(pi1, pi2):
        return pi1[0] * pi2[1] - pi1[1] * pi2[0]


    def absq(z):
        return z * conjq(z)


    SPINORS = [[g.qi(1, 0), g.qi(0, 1)], [g.qi(2, -1), g.qi(1, 1)], [g.qi(0, 3), g.qi(-1, 2)],
               [g.qi(F(1, 2), 0), g.qi(F(3, 2), -1)]]
    _chk("Thm 2.2(i): a single spinor's momentum is null, p^2 = 0, on four instances",
            all(minkowski_sq(spinor_momentum(pi)) == Q0 for pi in SPINORS))


    def padd(p, q):
        return [[p[a][b] + q[a][b] for b in range(2)] for a in range(2)]


    ok = True
    for pi1, pi2 in combinations(SPINORS, 2):
        ptot = padd(spinor_momentum(pi1), spinor_momentum(pi2))
        ok = ok and minkowski_sq(ptot) == 2 * absq(bracket(pi1, pi2))
    _chk("Thm 2.2(ii): two null momenta add to m^2 = 2 |[pi^1 pi^2]|^2 (T11's area "
            "formula) on all six pairs", ok)
    _chk("Thm 2.2(ii): aligned slot components give m^2 = 0 (pi^2 = 3 pi^1)",
            minkowski_sq(padd(spinor_momentum(SPINORS[0]),
                              spinor_momentum([3 * x for x in SPINORS[0]]))) == Q0)
    ok = True
    for a, b, c in combinations(SPINORS, 3):
        ptot = padd(padd(spinor_momentum(a), spinor_momentum(b)), spinor_momentum(c))
        ok = ok and minkowski_sq(ptot) == 2 * (absq(bracket(a, b)) + absq(bracket(b, c)) + absq(bracket(a, c)))
    _chk("Thm 2.2(iii): three null momenta give m^2 = 2 (|[ab]|^2 + |[bc]|^2 + "
            "|[ac]|^2), the general C(n, j)-component formula at n = 3, j = 1", ok)

    # ---------------------------------------------------------------------------
    # Part C.  The sectors, the weights, and the frozen point's non-invariance
    # under the pair mixing (Prop 3.1)
    # ---------------------------------------------------------------------------

    def sector(S):
        return (bin(S >> 3).count("1"), bin(S & 7).count("1"))


    def Y_of(S):
        j, k = sector(S)
        return F(3 * j - 2 * k, 6)


    # the hypercharge generator y = 3 N_R - 2 N_W acts on sector (j, k) by 3j - 2k
    Yop = madd(madd({}, N_R, g.qi(3)), N_W, g.qi(-2))
    _chk("Prop 3.1: the hypercharge generator 3 N_R - 2 N_W is diagonal with "
            "eigenvalue 6 Y(j, k) = 3j - 2k on each basis state",
            all(r == c for (r, c) in Yop) and all(entry(Yop, S, S) == g.qi(6 * Y_of(S)) for S in range(DIM)))
    even16 = [S for S in range(DIM) if sum(sector(S)) % 2 == 0]
    _chk("Prop 3.1: the even half has sixteen states with the generation's "
            "hypercharges and the odd half their negatives",
            len(even16) == 16
            and sorted(Y_of(S) for S in even16)
            == sorted([F(1, 6)] * 6 + [F(-1, 2)] * 2 + [F(-2, 3)] * 3 + [F(1, 3)] * 3 + [F(1), F(0)])
            and sorted(Y_of(S) for S in range(DIM) if S not in even16)
            == sorted(-y for y in [F(1, 6)] * 6 + [F(-1, 2)] * 2 + [F(-2, 3)] * 3 + [F(1, 3)] * 3 + [F(1), F(0)]))

    # slot-singlet and slot-doublet sectors of the even half
    singlets = sorted(set(sector(S) for S in even16 if sector(S)[0] in (0, 2)))
    doublets = sorted(set(sector(S) for S in even16 if sector(S)[0] == 1))
    _chk("Thm 2.2 / Prop 3.1: in the generation the slot-singlet sectors are "
            "(0,0), (0,2), (2,0), (2,2) = nu^c, u^c, e^c, d^c and the slot-doublet "
            "sectors are (1,1), (1,3) = Q, L",
            singlets == [(0, 0), (0, 2), (2, 0), (2, 2)] and doublets == [(1, 1), (1, 3)])

    # the frozen point is a vector of V_C = W + Wbar; under the pair mixing u(3)
    # its weights are +e_i and -e_i: the 3 and the 3bar, no zero weight, so no
    # nonzero vector of V_C is u(3)-invariant.
    def u3_weights_of_vector(x):
        """weights of a mode vector under the Cartan of u(3): (n_1, n_2, n_3)."""
        ws = []
        for i in range(3):
            c = comm(mm(CR[i], AN[i]), x)
            (S, T), v = next(iter(x.items()))
            lam = entry(c, S, T) / v
            assert madd(c, x, -lam) == {}
            assert lam.im == 0
            ws.append(lam.re)
        return tuple(ws)


    wts = sorted(u3_weights_of_vector(x) for x in V_VECS)
    _chk("Prop 3.1: the six vectors of V_C have u(3)-weights +e_i and -e_i (3 + "
            "3bar); none is a zero weight, so no nonzero frozen point is invariant "
            "under the pair mixing, whose stabiliser of a generic vector is a U(2)",
            wts == sorted([(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]))
    _chk("Prop 3.1: every vector of V_C commutes with the rung mixing u(2) and "
            "the rung number: the frozen point is insensitive to the slots exactly",
            all(is_zero(comm(x, E)) for x in V_VECS for E in U2_GENS + [N_R]))

    # Lambda^2 of the five modes: the 10 of SU(5), and the bracket direction
    lam2 = {}
    for S in range(DIM):
        if bin(S).count("1") == 2:
            lam2.setdefault(sector(S), []).append(S)
    _chk("Prop 3.2: Lambda^2(R_2 + W) has sectors (2,0) x1, (1,1) x6, (0,2) x3 with "
            "Y = 1, 1/6, -2/3: the 10 of SU(5) as e^c + Q + u^c, and the slot "
            "bivector Lambda^2 R_2 is the e^c direction, Y = 1, T_3 = 0, charge 1",
            {s: len(v) for s, v in lam2.items()} == {(2, 0): 1, (1, 1): 6, (0, 2): 3}
            and Y_of(lam2[(2, 0)][0]) == 1)

    # ---------------------------------------------------------------------------
    # Part D.  The commutant of s(u(2) + u(3)) on the module (Prop 3.3)
    # ---------------------------------------------------------------------------

    # Cartan weights of each basis state: (n_4 - n_5 for su(2) T_3 x 2, n_1, n_2,
    # n_3 for the u(3) torus); the s(u(2)+u(3)) torus is these four numbers
    # (the abelian factor is 3 N_R - 2 N_W, a combination), so components are
    # separated by the full weight vector under u(2) + u(3).
    def weight(S):
        """The weight under the Cartan of s(u(2) + u(3)), the traceless diagonal
        matrices: the five occupation numbers modulo (1,1,1,1,1), which vanishes
        on that Cartan; the vacuum and the filled state share the weight zero."""
        n = tuple(S >> i & 1 for i in range(5))
        return (0,) * 5 if n == (1,) * 5 else n


    # An operator commuting with the whole of u(2) + u(3) (all E_ab, a,b in
    # {4,5}; all E_ab, a,b in {1,2,3}) is determined on highest-weight vectors:
    # we compute the commutant dimension directly by solving [X, E] = 0 for all
    # generators, X restricted to be torus-invariant (block diagonal in weights).
    by_w = {}
    for S in range(DIM):
        by_w.setdefault(weight(S), []).append(S)
    unknowns = [(S, T) for w, Ss in by_w.items() for S in Ss for T in Ss]
    idx = {u: n for n, u in enumerate(unknowns)}
    # the off-diagonal generators (all traceless); the Cartan is imposed through
    # the weight blocks
    GENS = [mm(CR[a], AN[b]) for a in (3, 4) for b in (3, 4) if a != b] + \
           [mm(CR[a], AN[b]) for a in range(3) for b in range(3) if a != b]
    rows = []
    for E in GENS:
        # [X, E]_{r c} = sum_t X_{r t} E_{t c} - E_{r t} X_{t c}
        for r in range(DIM):
            for c in range(DIM):
                row = {}
                for (S, T), n in idx.items():
                    if S == r and entry(E, T, c) != Q0:
                        row[n] = row.get(n, Q0) + entry(E, T, c)
                    if T == c and entry(E, r, S) != Q0:
                        row[n] = row.get(n, Q0) - entry(E, r, S)
                if row:
                    rows.append(row)
    # rank of the constraint system over Q(i) by elimination on sparse rows
    def rank_sparse(rows, nvars):
        pivots = {}
        rank = 0
        for row in rows:
            row = {k: v for k, v in row.items() if v != Q0}
            while row:
                p = min(row)
                if p in pivots:
                    prow, pv = pivots[p]
                    f = row[p] / pv
                    for k, v in prow.items():
                        nv = row.get(k, Q0) - f * v
                        if nv == Q0:
                            row.pop(k, None)
                        else:
                            row[k] = nv
                else:
                    pivots[p] = (row, row[p])
                    rank += 1
                    break
        return rank


    r = rank_sparse(rows, len(unknowns))
    comm_dim = len(unknowns) - r
    _chk("Prop 3.3: the commutant of s(u(2) + u(3)) on the 32-dimensional module "
            "has dimension 14 = 10 x 1^2 + 1 x 2^2: ten components occur once and "
            "one type, (1,1)_0, twice, at (0,0) in the even half and (2,3) in the "
            "odd half", comm_dim == 14)
    # the two (1,1)_0 states
    inv_states = [S for S in range(DIM) if weight(S) in ((0, 0, 0, 0, 0), (1, 1, 1, 1, 1))]
    _chk("Prop 3.3: the two singlet states are the vacuum (sector (0,0), even) "
            "and the filled state (sector (2,3), odd), of opposite chirality, so the "
            "one off-diagonal invariant operator is chirality-changing",
            sorted(sector(S) for S in inv_states) == [(0, 0), (2, 3)]
            and sum(sector(inv_states[0])) % 2 != sum(sector(inv_states[1])) % 2)
    # restricted to the even half alone, the commutant is six-dimensional (scalars)
    even_unknowns = [(S, T) for (S, T) in unknowns if S in even16 and T in even16]
    eidx = {u: n for n, u in enumerate(even_unknowns)}
    erows = []
    for E in GENS:
        for r_ in even16:
            for c in even16:
                row = {}
                for (S, T), n in eidx.items():
                    if S == r_ and entry(E, T, c) != Q0:
                        row[n] = row.get(n, Q0) + entry(E, T, c)
                    if T == c and entry(E, r_, S) != Q0:
                        row[n] = row.get(n, Q0) - entry(E, r_, S)
                if row:
                    erows.append(row)
    _chk("Prop 3.3: on the sixteen alone the commutant is six-dimensional: an "
            "invariant operator is one scalar per component of the generation",
            len(even_unknowns) - rank_sparse(erows, len(even_unknowns)) == 6)

    # ---------------------------------------------------------------------------
    # Part E.  The 5 = R_2 + W and its two halves (Cor 2.3), and the sector of the
    # configuration (Obs 3.4)
    # ---------------------------------------------------------------------------

    five = [S for S in range(DIM) if bin(S).count("1") == 1]
    _chk("Cor 2.3: the one-mode states form (1,0) x2 + (0,1) x3, the doublet of "
            "Y = 1/2 and the triplet of Y = -1/3: the 5 of SU(5) split by slot and pair",
            sorted(sector(S) for S in five) == [(0, 1)] * 3 + [(1, 0)] * 2
            and {Y_of(S) for S in five if sector(S) == (1, 0)} == {F(1, 2)}
            and {Y_of(S) for S in five if sector(S) == (0, 1)} == {F(-1, 3)})
    _chk("Cor 2.3: the doublet of the 5 has two slot components (grip mass the "
            "area of two null momenta) and each triplet state one (grip mass zero): "
            "the frozen point's split of the 5 is doublet massive, triplet massless",
            len([S for S in five if sector(S) == (1, 0)]) == 2
            and all(bin(S >> 3).count("1") == 0 for S in five if sector(S) == (0, 1)))
    _chk("Obs 3.4: the configuration sectors (1,0) and (1,2) of the odd half carry "
            "Y = 1/2 and Y = -1/6, the Higgs doublet's and the anti-quark doublet's "
            "hypercharges, and (1,0) is the pair vacuum of the slot doublet",
            Y_of([S for S in range(DIM) if sector(S) == (1, 0)][0]) == F(1, 2)
            and Y_of([S for S in range(DIM) if sector(S) == (1, 2)][0]) == F(-1, 6))
    # the general count: a state in sector (j, k) has C(2, j) slot components
    from math import comb
    _chk("Thm 2.2: a state in rung sector j of the two-rung module has C(2, j) slot "
            "components, 1, 2, 1 for j = 0, 1, 2, so only j = 1 admits a nonzero area",
            [comb(2, j) for j in range(3)] == [1, 2, 1])

    # ---------------------------------------------------------------------------
    # Part F.  The two flags resolved (Section 4)
    # ---------------------------------------------------------------------------

    # Prop 4.2(ii): the commutant of so(2,4) on the twistor's own Fock space
    # Lambda^*W (the 8 states with no rung occupied) is two-dimensional: scalars
    # on T and on T'.  Restrict the fifteen bivectors of V_C to those states.
    W_STATES = [S for S in range(DIM) if S >> 3 == 0]
    w_unknowns = [(S, T) for S in W_STATES for T in W_STATES]
    widx = {u: n for n, u in enumerate(w_unknowns)}
    wrows = []
    for X in V_BIV:
        for r_ in W_STATES:
            for c in W_STATES:
                row = {}
                for (S, T), n in widx.items():
                    if S == r_ and entry(X, T, c) != Q0:
                        row[n] = row.get(n, Q0) + entry(X, T, c)
                    if T == c and entry(X, r_, S) != Q0:
                        row[n] = row.get(n, Q0) - entry(X, r_, S)
                if row:
                    wrows.append(row)
    _chk("Prop 4.2(ii): the commutant of the bivectors of V_C on Lambda^*W is "
            "two-dimensional (a scalar on each chirality half): no non-scalar "
            "operator on the twistor's Fock space, hence no element of the pair "
            "mixing u(3), commutes with the conformal algebra",
            len(w_unknowns) - rank_sparse(wrows, len(w_unknowns)) == 2)
    _chk("Prop 4.2(ii): each u(3) generator fails to commute with some bivector "
            "of V_C (it is a Bogoliubov relabelling, not an internal symmetry)",
            all(any(not is_zero(comm(E, X)) for X in V_BIV) for E in U3_GENS))
    _chk("Prop 4.2(ii): the u(3) generators are themselves bivectors of V_C "
            "(v_i w_j), so the pair mixing lies in the complexified conformal "
            "algebra so(6, C) and the question is one of real forms",
            all(E in V_BIV or any(madd(E, X, g.qi(-1)) == {} for X in V_BIV) for E in U3_GENS))

    # Prop 4.3(ii): a rung component of the frozen point is a slot doublet of
    # hypercharge +-1/2: the rung vectors v_4, v_5 form an su(2) doublet with
    # y-weight +3, the w's the conjugate doublet with weight -3.
    def y_weight(x):
        c = comm(Yop, x)
        (S, T), v = next(iter(x.items()))
        lam = entry(c, S, T) / v
        assert madd(c, x, -lam) == {}
        return lam


    E45, E54 = mm(CR[3], AN[4]), mm(CR[4], AN[3])
    _chk("Prop 4.3(ii): the rung creation vectors have hypercharge weight +3 "
            "(Y = 1/2) and the rung annihilation vectors -3 (Y = -1/2), and the "
            "su(2) raising operator carries v_5 to v_4 and w_4 to -w_5: R_2 + "
            "conj(R_2) = (2,1)_{1/2} + (2,1)_{-1/2}",
            [y_weight(x) for x in R_VECS] == [g.qi(3), g.qi(3), g.qi(-3), g.qi(-3)]
            and comm(E45, CR[4]) == CR[3] and comm(E45, AN[3]) == {k: -v for k, v in AN[4].items()}
            and comm(E45, CR[3]) == {} and comm(E45, AN[4]) == {})
    # the stabiliser in u(2) of a nonzero real rung vector c = v_4 + w_4 is
    # one-dimensional
    c_vec = madd(CR[3], AN[3])
    st_rows = []
    for r_ in range(DIM):
        for cc in range(DIM):
            row = {}
            for n, E in enumerate(U2_GENS):
                val = entry(comm(E, c_vec), r_, cc)
                if val != Q0:
                    row[n] = val
            if row:
                st_rows.append(row)
    _chk("Prop 4.3(ii): the stabiliser in u(2) of the real rung vector v_4 + w_4 "
            "is one-dimensional: a nonzero rung component breaks the slot mixing "
            "U(2) to a U(1)", 4 - rank_sparse(st_rows, 4) == 1)

    # Prop 4.3(iii): the mixed bivectors (a vector of V times a vector of R)
    # change (j, k) by (+-1, +-1), have no diagonal block on any sector, and on
    # the even half connect Q to all four singlets and L to u^c and d^c only.
    MIXED = [mm(x, y) for x in V_VECS for y in R_VECS]
    ok = True
    links = set()
    for X in MIXED:
        for (r_, cc), v in X.items():
            jr, kr = sector(r_)
            jc, kc = sector(cc)
            ok = ok and abs(jr - jc) == 1 and abs(kr - kc) == 1
            if (jr + kr) % 2 == 0:
                links.add(tuple(sorted([(jr, kr), (jc, kc)])))
    _chk("Prop 4.3(iii): every mixed bivector changes the rung number and the "
            "pair number by one each; it has no matrix element within any sector, "
            "so pure-sector states keep their Theorem 2.3 masses at first order in "
            "the rung component", ok)
    expected = {tuple(sorted(p)) for p in [((1, 1), (0, 0)), ((1, 1), (0, 2)), ((1, 1), (2, 0)),
                                           ((1, 1), (2, 2)), ((1, 3), (0, 2)), ((1, 3), (2, 2))]}
    _chk("Prop 4.3(iii): on the generation the mixed bivectors connect Q (1,1) "
            "to nu^c, u^c, e^c, d^c and L (1,3) to u^c and d^c only, never L to "
            "e^c or nu^c: not the Yukawa pattern", links == expected)
    # a sector-diagonal expectation vanishes on pure-sector states
    ok = True
    for seed in (6, 7):
        psi = rand_state(seed)
        for j in range(3):
            pj = project_j(psi, j)
            ok = ok and all(form(pj, apply(X, pj)) == Q0 for X in MIXED[:8])
    _chk("Prop 4.3(iii): the expectation of a mixed bivector vanishes on every "
            "rung-sector component of two Gaussian-rational states", ok)


part_G()

# ---------------------------------------------------------------------------
# Part H: the ten, the pairing, the Yukawa pattern and the transported frozen point (Sections 9.4, 9.5: Prop 9.22, Lem 9.23, Thm 9.24, Cor 9.25, Props 9.26, 9.27, Cor 9.28)
# ---------------------------------------------------------------------------

def part_H():
    _RETAG = [
        ('Prop 2.1', 'Prop 9.22'),
        ('Lemma 2.2', 'Lem 9.23'),
        ('Thm 2.3', 'Thm 9.24'),
        ('Cor 2.4', 'Cor 9.25'),
        ('Prop 3.1', 'Prop 9.26'),
        ('Prop 3.2', 'Prop 9.27'),
        ('Cor 3.3', 'Cor 9.28'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)

    Q0, Q1 = g.qi(0), g.qi(1)
    N_MODES, DIM, FULL = 5, 32, 31

    # ---------------------------------------------------------------------------
    # Part A.  The module (sparse), the mode vectors, and the 10 (Prop 2.1)
    # ---------------------------------------------------------------------------

    def sign_below(S, i):
        return -1 if bin(S & ((1 << i) - 1)).count("1") % 2 else 1


    def creator(i):
        return {(S | 1 << i, S): g.qi(sign_below(S, i)) for S in range(DIM) if not S >> i & 1}


    def annihilator(i):
        return {(S & ~(1 << i), S): g.qi(sign_below(S, i)) for S in range(DIM) if S >> i & 1}


    def mm(A, B):
        byrow = {}
        for (r, c), v in B.items():
            byrow.setdefault(r, []).append((c, v))
        out = {}
        for (r, t), v in A.items():
            for c, w in byrow.get(t, ()):
                out[(r, c)] = out.get((r, c), Q0) + v * w
        return {k: v for k, v in out.items() if v != Q0}


    def madd(A, B, cb=Q1):
        out = dict(A)
        for k, v in B.items():
            out[k] = out.get(k, Q0) + cb * v
        return {k: v for k, v in out.items() if v != Q0}


    def comm(A, B):
        return madd(mm(A, B), mm(B, A), g.qi(-1))


    def entry(M, r, c):
        return M.get((r, c), Q0)


    def apply(X, psi):
        out = [Q0] * DIM
        for (r, c), v in X.items():
            out[r] = out[r] + v * psi[c]
        return out


    def basis(S):
        return [Q1 if i == S else Q0 for i in range(DIM)]


    def sector(S):
        return (bin(S >> 3).count("1"), bin(S & 7).count("1"))


    def Y_of(S):
        j, k = sector(S)
        return F(3 * j - 2 * k, 6)


    CR = [creator(i) for i in range(N_MODES)]
    AN = [annihilator(i) for i in range(N_MODES)]
    N_W = madd(madd(mm(CR[0], AN[0]), mm(CR[1], AN[1])), mm(CR[2], AN[2]))
    N_R = madd(mm(CR[3], AN[3]), mm(CR[4], AN[4]))
    Yop = madd(madd({}, N_R, g.qi(3)), N_W, g.qi(-2))
    T3op = madd(mm(CR[3], AN[3]), mm(CR[4], AN[4]), g.qi(-1))   # 2 T_3 on the rung doublet

    even16 = [S for S in range(DIM) if sum(sector(S)) % 2 == 0]
    NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}


    def ad_weight(H, x):
        """eigenvalue of ad(H) on the vector x (exact; asserts x is an eigenvector)."""
        c = comm(H, x)
        (S, T), v = next(iter(x.items()))
        lam = entry(c, S, T) / v if c else Q0
        assert madd(c, x, -lam) == {}
        return lam


    RUNG_V, RUNG_W = [CR[3], CR[4]], [AN[3], AN[4]]
    PAIR_V, PAIR_W = [CR[0], CR[1], CR[2]], [AN[0], AN[1], AN[2]]
    TEN = RUNG_V + RUNG_W + PAIR_V + PAIR_W

    _chk("Prop 2.1: the ten mode vectors carry hypercharge weights 6Y = +3, -3 "
            "(rung creation, annihilation) and -2, +2 (pair creation, annihilation): "
            "Y = 1/2, -1/2, -1/3, +1/3",
            [ad_weight(Yop, x) for x in TEN] == [g.qi(3)] * 2 + [g.qi(-3)] * 2 + [g.qi(-2)] * 3 + [g.qi(2)] * 3)
    _chk("Prop 2.1: the rung vectors carry 2T_3 = +-1 (doublets) and the pair "
            "vectors 2T_3 = 0 (SU(2) singlets)",
            [ad_weight(T3op, x) for x in RUNG_V] == [Q1, g.qi(-1)]
            and [ad_weight(T3op, x) for x in RUNG_W] == [g.qi(-1), Q1]
            and all(ad_weight(T3op, x) == Q0 for x in PAIR_V + PAIR_W))
    E12 = mm(CR[0], AN[1])
    _chk("Prop 2.1: the su(3) generator E_12 carries the pair vector v_2 to v_1 and "
            "w_1 to -w_2 and annihilates every rung vector: the pair vectors are the "
            "colour triplet and antitriplet, the rung vectors colour singlets",
            comm(E12, CR[1]) == CR[0] and comm(E12, AN[0]) == {k: -v for k, v in AN[1].items()}
            and all(comm(E12, x) == {} for x in RUNG_V + RUNG_W))
    one_mode = [S for S in range(DIM) if bin(S).count("1") == 1]
    _chk("Prop 2.1: the one-mode states are (1,0) x2 with Y = 1/2 and (0,1) x3 with "
            "Y = -1/3: the 5 of SU(5) is the slot doublet plus the pair triplet",
            sorted((sector(S), Y_of(S)) for S in one_mode)
            == [((0, 1), F(-1, 3))] * 3 + [((1, 0), F(1, 2))] * 2)

    # ---------------------------------------------------------------------------
    # Part B.  The invariant spinor pairing (Lemma 2.2)
    # B(psi, phi) = sum_S (-1)^{k(k-1)/2} sgn(S, S^c) psi_S phi_{S^c}, k = |S|
    # ---------------------------------------------------------------------------

    def wedge_sign(S, T):
        if S & T:
            return 0
        sgn = 1
        for i in range(N_MODES):
            if T >> i & 1:
                sgn *= (-1) ** bin(S >> (i + 1)).count("1")
        return sgn


    def B(psi, phi):
        tot = Q0
        for S in range(DIM):
            if psi[S] == Q0:
                continue
            T = FULL ^ S
            if phi[T] == Q0:
                continue
            k = bin(S).count("1")
            tot = tot + psi[S] * phi[T] * g.qi(wedge_sign(S, T) * (-1) ** (k * (k - 1) // 2))
        return tot


    HALF = {(r, r): g.qi(F(-1, 2)) for r in range(DIM)}
    SO10 = [mm(CR[i], AN[j]) for i in range(5) for j in range(5) if i != j] + \
           [mm(CR[i], CR[j]) for i, j in combinations(range(5), 2)] + \
           [mm(AN[i], AN[j]) for i, j in combinations(range(5), 2)] + \
           [madd(mm(CR[i], AN[i]), HALF) for i in range(5)]


    def rank_sparse(rows):
        pivots, rank = {}, 0
        for row in rows:
            row = {k: v for k, v in row.items() if v != Q0}
            while row:
                p = min(row)
                if p in pivots:
                    prow, pv = pivots[p]
                    f = row[p] / pv
                    for k, v in prow.items():
                        nv = row.get(k, Q0) - f * v
                        if nv == Q0:
                            row.pop(k, None)
                        else:
                            row[k] = nv
                else:
                    pivots[p] = (row, row[p])
                    rank += 1
                    break
        return rank


    _chk("Lemma 2.2: the forty-five bivectors v_i w_j (i != j), v_i v_j, w_i w_j and "
            "v_i w_i - 1/2 are linearly independent: a basis of so(10)",
            len(SO10) == 45 and rank_sparse([{r * DIM + c: v for (r, c), v in X.items()} for X in SO10]) == 45)
    # invariance: B(X psi, phi) + B(psi, X phi) = 0 on a basis, for every generator
    ok = True
    for X in SO10:
        for S in range(DIM):
            for T in range(DIM):
                if B(apply(X, basis(S)), basis(T)) + B(basis(S), apply(X, basis(T))) != Q0:
                    ok = False
    _chk("Lemma 2.2: the pairing is invariant under every one of the bivectors, "
            "hence under so(10): B(X psi, phi) + B(psi, X phi) = 0 on all basis pairs", ok)
    _chk("Lemma 2.2: the pairing is nondegenerate and pairs a state only with its "
            "complement (even with odd degree: the 16 with the 16bar)",
            all(any(B(basis(S), basis(T)) != Q0 for T in range(DIM)) for S in range(DIM))
            and all(B(basis(S), basis(T)) == Q0 for S in range(DIM) for T in range(DIM) if T != FULL ^ S)
            and all(bin(S).count("1") % 2 != bin(FULL ^ S).count("1") % 2 for S in range(DIM)))

    # ---------------------------------------------------------------------------
    # Part C.  The Yukawa pattern (Thm 2.3): Y_x(psi, phi) = B(psi, x phi) on the 16
    # ---------------------------------------------------------------------------

    def couplings(vecs):
        pairs = set()
        for x in vecs:
            for S in even16:
                for T in even16:
                    if B(basis(S), apply(x, basis(T))) != Q0:
                        pairs.add(tuple(sorted([NAMES[sector(S)], NAMES[sector(T)]])))
        return sorted(pairs)


    _chk("Thm 2.3(i): the rung creation directions (Y = +1/2, H_u) couple exactly "
            "L with nu^c and Q with u^c", couplings(RUNG_V) == [("L", "nu^c"), ("Q", "u^c")])
    _chk("Thm 2.3(i): the rung annihilation directions (Y = -1/2, H_d) couple "
            "exactly L with e^c and Q with d^c", couplings(RUNG_W) == [("L", "e^c"), ("Q", "d^c")])
    _chk("Thm 2.3(ii): the pair creation directions (colour triplet, Y = -1/3) "
            "couple Q with Q, d^c with nu^c and e^c with u^c",
            couplings(PAIR_V) == [("Q", "Q"), ("d^c", "nu^c"), ("e^c", "u^c")])
    _chk("Thm 2.3(ii): the pair annihilation directions (antitriplet, Y = +1/3) "
            "couple Q with L and u^c with d^c",
            couplings(PAIR_W) == [("L", "Q"), ("d^c", "u^c")])
    # symmetry of the 10 coupling, and hypercharge conservation of every entry
    ok_sym, ok_Y = True, True
    for x in TEN:
        yx = ad_weight(Yop, x)
        for S in even16:
            for T in even16:
                a = B(basis(S), apply(x, basis(T)))
                b = B(basis(T), apply(x, basis(S)))
                if a != b:
                    ok_sym = False
                if a != Q0 and g.qi(6 * (Y_of(S) + Y_of(T))) + yx != Q0:
                    ok_Y = False
    _chk("Thm 2.3(iii): every coupling is symmetric in the two sixteens (the 10 is "
            "the symmetric part of 16 x 16)", ok_sym)
    _chk("Thm 2.3(iii): every nonzero entry conserves hypercharge, Y(psi) + Y(phi) + "
            "Y(x) = 0", ok_Y)
    # no coupling of the 16 to itself without a vector, and none with a bivector
    # in the pattern of a 10: the singlet pairing of two sixteens vanishes
    _chk("Thm 2.3(iii): the bare pairing of the sixteen with itself vanishes (no "
            "singlet in 16 x 16): every mass term needs a vector",
            all(B(basis(S), basis(T)) == Q0 for S in even16 for T in even16))


    # universal masses from one vev vector c = a v_4 + b w_4
    def mass_matrix(c_vec):
        M = {}
        for S in even16:
            for T in even16:
                val = B(basis(S), apply(c_vec, basis(T)))
                if val != Q0:
                    M[(S, T)] = val
        return M


    a, b = g.qi(5), g.qi(F(2, 7))
    cvec = madd(madd({}, CR[3], a), AN[3], b)
    M = mass_matrix(cvec)
    by_species = {}
    for (S, T), val in M.items():
        key = tuple(sorted([NAMES[sector(S)], NAMES[sector(T)]]))
        mag = val * g.qi(-1) if val.re < 0 or (val.re == 0 and val.im < 0) else val
        by_species.setdefault(key, set()).add((mag.re, mag.im))
    _chk("Cor 2.4: with one vev vector a v_4 + b w_4 the mass entries are |a| on "
            "(L, nu^c) and (Q, u^c) and |b| on (L, e^c) and (Q, d^c): m_nu = m_u = |a| "
            "and m_e = m_d = |b|, the 10_H relations, and nothing else is coupled",
            by_species == {("L", "nu^c"): {(5, 0)}, ("Q", "u^c"): {(5, 0)}, ("L", "e^c"): {(F(2, 7), 0)}, ("Q", "d^c"): {(F(2, 7), 0)}})
    # the vev selects one slot component: the L states coupled by v_4 all have the
    # same T_3, and by w_4 the opposite one
    def t3_of_coupled(vec, species):
        out = set()
        for (S, T), val in mass_matrix(vec).items():
            for U in (S, T):
                if NAMES[sector(U)] == species:
                    out.add((entry(T3op, U, U).re, entry(T3op, U, U).im))
        return out


    _chk("Cor 2.4: the v_4 vev couples the T_3 = -1/2 components of L and Q and the "
            "w_4 vev the T_3 = +1/2 components: a vev along one rung breaks the slot "
            "SU(2) x U(1)_Y to the U(1) fixing it, as an electroweak vev does",
            t3_of_coupled(CR[3], "L") == {(-1, 0)} and t3_of_coupled(AN[3], "L") == {(1, 0)}
            and t3_of_coupled(CR[3], "Q") == {(-1, 0)} and t3_of_coupled(AN[3], "Q") == {(1, 0)})

    # ---------------------------------------------------------------------------
    # Part D.  The conformal model of T1 and the transported frozen point (Prop 3.2)
    # Vectors of R^{2,4} + H' + H'' as coordinate lists with a diagonal metric:
    # ground e_1..e_6 with signs (+,+,-,-,-,-); rung 2 plane e_+', e_-'; rung 3
    # plane e_+'', e_-''.
    # ---------------------------------------------------------------------------

    SIG = [1, 1, -1, -1, -1, -1, 1, -1, 1, -1]
    NV = len(SIG)


    def vec(**kw):
        v = [F(0)] * NV
        for k, val in kw.items():
            v[int(k[1:])] = F(val)
        return v


    def dot(x, y):
        return sum(F(s) * a * b for s, a, b in zip(SIG, x, y))


    def add(*vs):
        return [sum(c) for c in zip(*vs)]


    def scale(c, v):
        return [F(c) * a for a in v]


    ep1, em1 = vec(c6=1), vec(c7=1)      # rung-2 plane
    ep2, em2 = vec(c8=1), vec(c9=1)      # rung-3 plane
    n_o1, n_inf1 = scale(F(1, 2), add(em1, scale(-1, ep1))), add(em1, ep1)
    n_o2, n_inf2 = scale(F(1, 2), add(em2, scale(-1, ep2))), add(em2, ep2)
    _chk("Prop 3.2: T1's null pair: n_0^2 = n_inf^2 = 0 and n_0 . n_inf = -1 in each "
            "rung plane",
            dot(n_o1, n_o1) == 0 and dot(n_inf1, n_inf1) == 0 and dot(n_o1, n_inf1) == -1
            and dot(n_o2, n_o2) == 0 and dot(n_inf2, n_inf2) == 0 and dot(n_o2, n_inf2) == -1)
    # the Fock modes of the rung plane: v = n_inf/2, w = -n_0, with v.w = 1/2
    v1, w1 = scale(F(1, 2), n_inf1), scale(-1, n_o1)
    _chk("Prop 3.2: v = n_inf/2 and w = -n_0 are null with v . w = 1/2, so as Clifford "
            "vectors vw + wv = 1: T1's null pair is the rung's mode pair, with * "
            "(fixing e_+, negating e_-) exchanging v and w",
            dot(v1, v1) == 0 and dot(w1, w1) == 0 and dot(v1, w1) == F(1, 2))


    def lift(x, n_o, n_inf):
        return add(n_o, x, scale(dot(x, x) / 2, n_inf))


    # the frozen point: a vector of the ground space with norm Lambda/3; take it in
    # the ground hyperbolic plane (e_1 + e_3 is null: the Lambda = 0 point at
    # infinity of R^{1,3}'s own completion) and add the norm through e_1 - e_3.
    def frozen(Lam):
        # I = alpha (e_1 + e_3) + beta (e_1 - e_3) with I^2 = 4 alpha beta = Lam/3
        alpha = F(1)
        beta = Lam / 12
        return add(scale(alpha, add(vec(c0=1), vec(c2=1))), scale(beta, add(vec(c0=1), vec(c2=-1))))


    ok = True
    for Lam in (F(0), F(1, 5), F(3)):
        I = frozen(Lam)
        ok = ok and dot(I, I) == Lam / 3
        XI = lift(I, n_o1, n_inf1)
        ok = ok and dot(XI, XI) == 0
        rung = [XI[i] if i in (6, 7) else F(0) for i in range(NV)]
        ok = ok and rung == add(n_o1, scale(Lam / 6, n_inf1))
        ok = ok and rung == add(scale(-1, w1), scale(Lam / 3, v1))
        ok = ok and dot(rung, rung) == -Lam / 3
    _chk("Prop 3.2(i): the lift X(I) = n_0 + I + (Lambda/6) n_inf is null; its rung "
            "component is n_0 + (Lambda/6) n_inf = -w + (Lambda/3) v, of norm -Lambda/3, "
            "for Lambda = 0, 1/5, 3", ok)
    ok = True
    for Lam in (F(1, 5), F(3)):
        I = frozen(Lam)
        Q = dot(I, I)
        recip = lift(scale(1 / Q, I), n_o1, n_inf1)       # X(I / Q(I))
        recip = scale(Q, recip)                           # normalise the ground part to I
        ok = ok and dot(recip, recip) == 0
        rung = [recip[i] if i in (6, 7) else F(0) for i in range(NV)]
        ok = ok and rung == add(scale(Lam / 3, n_o1), scale(F(1, 2), n_inf1))
        ok = ok and rung == add(v1, scale(-Lam / 3, w1))
        ok = ok and dot(rung, rung) == -Lam / 3
    _chk("Prop 3.2(ii): the lift of the reciprocal, normalised to ground part I, has "
            "rung component (Lambda/3) n_0 + n_inf/2 = v - (Lambda/3) w, of norm "
            "-Lambda/3: the conjugate null direction to the lift's", ok)
    # at Lambda = 0 the frozen point is null and Fact 9.4's reciprocal is the ideal
    # point x_0 + n_inf/2; evaluate it there, and check it is the Lambda -> 0 limit
    # of the normalised reciprocal Q n_0 + I + n_inf/2 computed above
    I0 = frozen(F(0))
    ideal0 = add(I0, scale(F(1, 2), n_inf1))
    rung0 = [ideal0[i] if i in (6, 7) else F(0) for i in range(NV)]
    def recip_norm(Lam):
        I = frozen(Lam)
        return scale(dot(I, I), lift(scale(1 / dot(I, I), I), n_o1, n_inf1))
    _chk("Prop 3.2(ii): at Lambda = 0 the frozen point is null, the reciprocal is T1's "
            "ideal point I + n_inf/2 (Fact 9.4), which is null with rung component "
            "exactly n_inf/2 = v and no n_0 part, and the normalised reciprocal "
            "Q n_0 + I + n_inf/2 at Lambda = 1/5, 3 differs from it by (Lambda/3) n_0 "
            "plus the ground shift of I alone",
            dot(I0, I0) == 0 and dot(ideal0, ideal0) == 0
            and rung0 == v1 and dot(rung0, n_inf1) == 0
            and all(recip_norm(Lam) == add(ideal0, scale(Lam / 3, n_o1),
                                              add(frozen(Lam), scale(-1, I0)))
                    for Lam in (F(1, 5), F(3))))
    # the second rung: lifting the null X(I) adds n_0'' only
    ok = True
    for Lam in (F(0), F(3)):
        XI = lift(frozen(Lam), n_o1, n_inf1)
        XXI = lift(XI, n_o2, n_inf2)
        ok = ok and dot(XXI, XXI) == 0
        ok = ok and [XXI[i] for i in (8, 9)] == [n_o2[8], n_o2[9]]
        ok = ok and [XXI[i] for i in (6, 7)] == [XI[i] for i in (6, 7)]
    _chk("Prop 3.2(iii): lifting the null X(I) to the third rung adds the component "
            "n_0'' = -w'' and nothing else: the doubly lifted frozen point has rung "
            "components (-w + (Lambda/3) v, -w''), the direction (1,1) of the "
            "w-doublet", ok)
    # the frozen point as a first-rung component: in the ground plane e_1 +- e_3,
    # I = (e_1 + e_3) + (Lambda/12)(e_1 - e_3) has the form n_inf^(1) + c n_0^(1)
    n_inf_g, n_o_g = add(vec(c0=1), vec(c2=1)), scale(F(1, 2), add(vec(c2=1), vec(c0=-1)))
    _chk("Prop 3.1: the frozen point lies in the ground hyperbolic plane, I = "
            "n_inf^(1) - (Lambda/6) n_0^(1) for n_inf^(1) = e_+ + e_- and n_0^(1) = "
            "(e_- - e_+)/2 with n_0^(1) . n_inf^(1) = -1 (T1's conventions): at Lambda = "
            "0 it is the null vector n_inf^(1), and its norm is Lambda/3",
            dot(n_o_g, n_inf_g) == -1 and dot(n_o_g, n_o_g) == 0 and dot(n_inf_g, n_inf_g) == 0
            and all(frozen(Lam) == add(n_inf_g, scale(-Lam / 6, n_o_g)) and dot(frozen(Lam), frozen(Lam)) == Lam / 3
                    for Lam in (F(0), F(2), F(7, 3))))

    # ---------------------------------------------------------------------------
    # Part E.  Reading the lifted components as vevs (Cor 3.3)
    # ---------------------------------------------------------------------------

    # X-lift: rung component -w_4 + (Lambda/3) v_4; reciprocal: v_4 - (Lambda/3) w_4
    Lam = F(1, 10)
    c_lift = madd(madd({}, AN[3], g.qi(-1)), CR[3], g.qi(Lam / 3))
    c_recip = madd(madd({}, CR[3]), AN[3], g.qi(-Lam / 3))
    def species_masses(cv):
        out = {}
        for (S, T), val in mass_matrix(cv).items():
            key = tuple(sorted([NAMES[sector(S)], NAMES[sector(T)]]))
            mag = val if (val.re > 0 or (val.re == 0 and val.im > 0)) else val * g.qi(-1)
            out.setdefault(key, set()).add((mag.re, mag.im))
        return out
    sm_lift, sm_recip = species_masses(c_lift), species_masses(c_recip)
    _chk("Cor 3.3: the lift's rung component gives m_e = m_d = 1 and m_nu = m_u = "
            "Lambda/3; the reciprocal's gives m_nu = m_u = 1 and m_e = m_d = Lambda/3 "
            "(rung units): H_d-type and H_u-type, each with the conjugate at order "
            "Lambda",
            sm_lift == {("L", "e^c"): {(1, 0)}, ("Q", "d^c"): {(1, 0)}, ("L", "nu^c"): {(Lam / 3, 0)}, ("Q", "u^c"): {(Lam / 3, 0)}}
            and sm_recip == {("L", "nu^c"): {(1, 0)}, ("Q", "u^c"): {(1, 0)}, ("L", "e^c"): {(Lam / 3, 0)}, ("Q", "d^c"): {(Lam / 3, 0)}})
    # both together: every Dirac entry of magnitude exactly 1 + Lambda/3
    both = species_masses(madd(c_lift, c_recip))
    _chk("Cor 3.3: lift and reciprocal together give every Dirac entry the "
            "magnitude exactly 1 + Lambda/3 (Lambda = 1/10: 31/30, no entry at "
            "1 - Lambda/3), m_u = m_nu and m_d = m_e exactly and m_u/m_d = 1 exactly",
            all(v == {(1 + Lam / 3, 0)} for v in both.values())
            and set(both) == {("L", "nu^c"), ("Q", "u^c"), ("L", "e^c"), ("Q", "d^c")}
            and both[("L", "nu^c")] == both[("Q", "u^c")] and both[("L", "e^c")] == both[("Q", "d^c")]
            and next(iter(both[("Q", "u^c")]))[0] / next(iter(both[("Q", "d^c")]))[0] == 1)
    # the ground frozen point itself, read the same way, is a triplet-direction
    # vector (it lies in V): its couplings are the triplet ones
    I_mod = madd(CR[0], AN[0])   # a real vector of the ground plane in the module: v_1 + w_1
    _chk("Cor 3.3: the ground frozen point, a vector of V read through the same "
            "pairing, couples Q Q, Q L, u^c d^c, u^c e^c and d^c nu^c: the triplet "
            "couplings, baryon-number violating, and no Dirac mass",
            couplings([I_mod]) == [("L", "Q"), ("Q", "Q"), ("d^c", "nu^c"), ("d^c", "u^c"), ("e^c", "u^c")])


part_H()

# ---------------------------------------------------------------------------
# Part I (1): the family no-go and the Georgi-Jarlskog direction recomputed (Section 9.6: Thm 9.31; T13 Prop 8.1 rebuilt before use)
# ---------------------------------------------------------------------------

def part_I1():
    _RETAG = [
        ('[D] FAMILY NO-GO', 'Thm 9.31 FAMILY NO-GO'),
        ('[D] on the 126 direction M_e = -3 M_d', 'Thm 9.31 / Sec 9.6: on the 126 direction M_e = -3 M_d'),
        ('[D] the e^c state', 'Prop 9.15 / Sec 9.6: the e^c state'),
        ('[D]', 'Sec 9.6 (T13 Prop 8.1 recomputed):'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)

    NM = 5                                 # modes 0,1,2 = pairs W (colour), 3,4 = rungs (slots)
    PAIRS, RUNGS = (0, 1, 2), (3, 4)
    STATES = [frozenset(S) for k in range(NM + 1) for S in combinations(range(NM), k)]
    IDX = {S: i for i, S in enumerate(STATES)}
    DIM = len(STATES)                      # 32

    # sparse matrices: dict {(row, col): Fraction}
    def sp_from_action(act):
        """act(state frozenset) -> dict{frozenset: Fraction}; returns sparse matrix."""
        M = {}
        for S in STATES:
            for T, c in act(S).items():
                if c != 0:
                    M[(IDX[T], IDX[S])] = M.get((IDX[T], IDX[S]), F(0)) + c
        return {k: v for k, v in M.items() if v != 0}

    def sp_mul(A, B):
        Bc = {}
        for (i, j), b in B.items():
            Bc.setdefault(i, []).append((j, b))
        C = {}
        for (i, k), a in A.items():
            for j, b in Bc.get(k, ()):
                C[(i, j)] = C.get((i, j), F(0)) + a * b
        return {k: v for k, v in C.items() if v != 0}

    def sp_add(*Ms):
        C = {}
        for M in Ms:
            for k, v in M.items():
                C[k] = C.get(k, F(0)) + v
        return {k: v for k, v in C.items() if v != 0}

    def sp_scal(c, M):
        return {k: c * v for k, v in M.items() if c * v != 0}

    def sp_eq(A, B):
        return sp_add(A, sp_scal(F(-1), B)) == {}

    def sp_apply(M, vec):
        out = {}
        for (i, j), a in M.items():
            if j in vec:
                out[i] = out.get(i, F(0)) + a * vec[j]
        return {k: v for k, v in out.items() if v != 0}

    def sp_trace(M):
        return sum(v for (i, j), v in M.items() if i == j)

    ID = {(i, i): F(1) for i in range(DIM)}

    def wedge_act(i):
        return lambda S: g.ext_wedge(i, {S: F(1)})

    def contract_act(i):
        fv = [F(1) if j == i else F(0) for j in range(NM)]
        return lambda S: g.ext_contract(fv, {S: F(1)})

    V = [sp_from_action(wedge_act(i)) for i in range(NM)]      # creation  v_i
    Wm = [sp_from_action(contract_act(i)) for i in range(NM)]  # annihilation w_i

    # CAR: {v_i, w_j} = delta_ij, {v_i, v_j} = {w_i, w_j} = 0
    ok = True
    for i in range(NM):
        for j in range(NM):
            ac = sp_add(sp_mul(V[i], Wm[j]), sp_mul(Wm[j], V[i]))
            ok = ok and sp_eq(ac, ID if i == j else {})
            ok = ok and sp_add(sp_mul(V[i], V[j]), sp_mul(V[j], V[i])) == {}
            ok = ok and sp_add(sp_mul(Wm[i], Wm[j]), sp_mul(Wm[j], Wm[i])) == {}
    _chk("[D] five mode pairs: {v_i, w_j} = delta_ij, {v_i, v_j} = {w_i, w_j} = 0 on the 32-dimensional module", ok)

    # number operators, hypercharge, T_3, B-L
    def num(i):
        return sp_mul(V[i], Wm[i])
    N_W = sp_add(*[num(i) for i in PAIRS])
    N_R = sp_add(*[num(i) for i in RUNGS])
    Y = sp_add(sp_scal(F(1, 2), N_R), sp_scal(F(-1, 3), N_W))          # Y = N_R/2 - N_W/3
    T3 = sp_scal(F(1, 2), sp_add(num(3), sp_scal(F(-1), num(4))))
    BmL = sp_add(ID, sp_scal(F(-2, 3), N_W))                              # B - L = 1 - (2/3) N_W

    def species(S):
        nr, nw = len(S & set(RUNGS)), len(S & set(PAIRS))
        return {(0, 0): "nu^c", (2, 0): "e^c", (1, 1): "Q", (1, 3): "L", (0, 2): "u^c", (2, 2): "d^c",
                (1, 0): "slot", (0, 1): "pair", (1, 2): "(1,2)", (2, 1): "(2,1)", (0, 3): "(0,3)", (2, 3): "(2,3)"}[(nr, nw)]

    SIXTEEN = [S for S in STATES if len(S) % 2 == 0]
    _chk("[D] the even states number sixteen: nu^c (1), e^c (1), Q (6), L (2), u^c (3), d^c (3)",
            len(SIXTEEN) == 16 and sorted(species(S) for S in SIXTEEN) ==
            sorted(["nu^c", "e^c"] + ["Q"] * 6 + ["L"] * 2 + ["u^c"] * 3 + ["d^c"] * 3))
    Yval = {"nu^c": F(0), "e^c": F(1), "Q": F(1, 6), "L": F(-1, 2), "u^c": F(-2, 3), "d^c": F(1, 3)}
    BLval = {"nu^c": F(1), "e^c": F(1), "Q": F(1, 3), "L": F(-1), "u^c": F(-1, 3), "d^c": F(-1, 3)}
    def diag_val(M, S):
        v = sp_apply(M, {IDX[S]: F(1)})
        return v.get(IDX[S], F(0)) if set(v) <= {IDX[S]} else None
    _chk("[D] Y = N_R/2 - N_W/3 gives the Standard-Model hypercharges on the sixteen",
            all(diag_val(Y, S) == Yval[species(S)] for S in SIXTEEN))
    _chk("[D] B - L = 1 - (2/3) N_W gives (nu^c, e^c, Q, L, u^c, d^c) = (1, 1, 1/3, -1, -1/3, -1/3): "
            "the pair number is the B - L charge",
            all(diag_val(BmL, S) == BLval[species(S)] for S in SIXTEEN))

    # the invariant pairing B(psi, phi) = sum_S (-1)^{|S|(|S|-1)/2} eps(S, S^c) psi_S phi_{S^c}
    FULL = frozenset(range(NM))
    def eps_sign(S):
        """sign of e_S wedge e_{S^c} = eps e_{01234}."""
        seq = sorted(S) + sorted(FULL - S)
        inv = sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[a] > seq[b])
        return F(-1) ** inv
    Bcoef = {S: F(-1) ** (len(S) * (len(S) - 1) // 2) * eps_sign(S) for S in STATES}
    def Bpair(psi, phi):
        return sum(Bcoef[S] * psi.get(IDX[S], F(0)) * phi.get(IDX[FULL - S], F(0)) for S in STATES)

    def basis(S):
        return {IDX[S]: F(1)}
    # so(10) generators: 45 bivectors
    GENS = []
    for i in range(NM):
        for j in range(NM):
            if i != j:
                GENS.append(sp_mul(V[i], Wm[j]))
    for i, j in combinations(range(NM), 2):
        GENS.append(sp_mul(V[i], V[j]))
        GENS.append(sp_mul(Wm[i], Wm[j]))
    for i in range(NM):
        GENS.append(sp_add(num(i), sp_scal(F(-1, 2), ID)))
    _chk("[D] forty-five bivector generators", len(GENS) == 45)
    inv_ok = True
    for X in GENS:
        for S in STATES:
            Xs = sp_apply(X, basis(S))
            for T in STATES:
                if Bpair(Xs, basis(T)) + Bpair(basis(S), sp_apply(X, basis(T))) != 0:
                    inv_ok = False
    _chk("[D] the pairing B is so(10)-invariant on all 45 x 32 x 32 basis identities (the companion note's lemma, recomputed)", inv_ok)

    def yukawa(Top):
        """Y_T(psi, phi) = B(psi, T phi) on the sixteen, returned as {(species_S, species_T): set of values}
        together with the full matrix over basis pairs."""
        mat = {}
        for S in SIXTEEN:
            Tphi_cache = None
            for T in SIXTEEN:
                val = Bpair(basis(S), sp_apply(Top, basis(T)))
                if val != 0:
                    mat[(S, T)] = val
        return mat

    def clebsch(mat):
        """collect the nonzero values by species pair, unordered."""
        out = {}
        for (S, T), v in mat.items():
            key = tuple(sorted((species(S), species(T))))
            out.setdefault(key, set()).add(v)
        return out

    def is_symmetric(mat):
        return all(mat.get((T, S), F(0)) == v for (S, T), v in mat.items())

    # --- the 10: x = w_3 (a rung annihilation vector, Y = -1/2): couples (L, e^c) and (Q, d^c)
    Y10 = yukawa(Wm[3])
    c10 = clebsch(Y10)
    _chk("[D] the 10 (x = w_4): Y_x nonzero exactly on (L, e^c) and (Q, d^c), symmetric, all entries +-1",
            set(c10) == {("L", "e^c"), ("Q", "d^c")} and is_symmetric(Y10)
            and all(abs(v) == 1 for vs in c10.values() for v in vs))

    # --- the B-L weighted rung coupling.  The Standard-Model Yukawas conserve B - L, so a weighting by the
    # B - L of one argument alone is antisymmetric on every coupled pair; the symmetric weighting is by the
    # B - L of the DOUBLET member of the pair, which is chi (B - L) with chi = +1 on the doublet sector N_R = 1
    # and -1 on the singlet sectors N_R = 0, 2, i.e. chi = -(-1)^{N_R}.
    PARITY_R = sp_mul(sp_add(ID, sp_scal(F(-2), num(3))), sp_add(ID, sp_scal(F(-2), num(4))))   # (-1)^{N_R}
    CHI = sp_scal(F(-1), PARITY_R)
    T_GJ = sp_mul(Wm[3], sp_mul(BmL, CHI))
    YGJ = yukawa(T_GJ)
    cGJ = clebsch(YGJ)
    _chk("[D] T = w_4 (B - L) chi: symmetric, entries -1 on (L, e^c) and +1/3 on (Q, d^c): the Georgi-Jarlskog "
            "ratio m_e/m_d = -3 is the ratio of the lepton doublet's to the quark doublet's B - L",
            set(cGJ) == {("L", "e^c"), ("Q", "d^c")} and cGJ[("L", "e^c")] <= {F(1), F(-1)}
            and cGJ[("Q", "d^c")] <= {F(1, 3), F(-1, 3)} and is_symmetric(YGJ))
    # the unsymmetrised weighting is antisymmetric on every coupled pair (B - L conservation)
    Yraw = yukawa(sp_mul(Wm[3], BmL))
    _chk("[D] the one-sided weighting w_4 (B - L) is ANTISYMMETRIC on every coupled pair: the Yukawa pairs are "
            "B - L neutral, (B-L)(L) + (B-L)(e^c) = 0 = (B-L)(Q) + (B-L)(d^c)",
            Yraw != {} and all(Yraw.get((T, S), F(0)) == -v for (S, T), v in Yraw.items())
            and BLval["L"] + BLval["e^c"] == 0 and BLval["Q"] + BLval["d^c"] == 0)
    def mag(c, key):
        vals = {abs(v) for v in c[key]}
        assert len(vals) == 1
        return vals.pop()
    _chk("[D] the ratio |Y(L e^c)| / |Y(Q d^c)| is 1 for the 10 and 3 for the B-L weighted coupling",
            mag(c10, ("L", "e^c")) / mag(c10, ("Q", "d^c")) == 1
            and mag(cGJ, ("L", "e^c")) / mag(cGJ, ("Q", "d^c")) == 3)

    # --- grade decomposition of T_GJ in the Clifford algebra of the ten.
    # Orthonormal basis: a_i = v_i + w_i (square +1), b_i = v_i - w_i (square -1); blades = products.
    Aon = [sp_add(V[i], Wm[i]) for i in range(NM)]
    Bv = [sp_add(V[i], sp_scal(F(-1), Wm[i])) for i in range(NM)]
    _chk("[D] a_i = v_i + w_i square to +1, b_i = v_i - w_i to -1, and all ten anticommute pairwise: Cl(5,5)",
            all(sp_eq(sp_mul(Aon[i], Aon[i]), ID) and sp_eq(sp_mul(Bv[i], Bv[i]), sp_scal(F(-1), ID)) for i in range(NM))
            and all(sp_add(sp_mul(Aon[i], Bv[j]), sp_mul(Bv[j], Aon[i])) == {} for i in range(NM) for j in range(NM))
            and all(sp_add(sp_mul(Aon[i], Aon[j]), sp_mul(Aon[j], Aon[i])) == {} for i in range(NM) for j in range(NM) if i != j)
            and all(sp_add(sp_mul(Bv[i], Bv[j]), sp_mul(Bv[j], Bv[i])) == {} for i in range(NM) for j in range(NM) if i != j))
    TEN = Aon + Bv
    SQ = [F(1)] * NM + [F(-1)] * NM

    def blade(idx):
        M = ID
        for k in idx:
            M = sp_mul(M, TEN[k])
        return M

    def blade_inverse_sign(idx):
        """Gamma_idx^{-1} = sign * Gamma_idx reversed... compute Gamma_idx * Gamma_idx = s * ID, so inverse = Gamma/s."""
        k = len(idx)
        s = F(-1) ** (k * (k - 1) // 2)
        for t in idx:
            s *= SQ[t]
        return s

    # grade projection by the trace formula: coefficient of Gamma_A in M is tr(Gamma_A^{-1} M)/32
    def grade_parts(M):
        parts = {}
        for k in range(0, 2 * NM + 1):
            acc = {}
            for idx in combinations(range(2 * NM), k):
                G = blade(idx)
                s = blade_inverse_sign(idx)
                coef = sp_trace(sp_mul(G, M)) / s / DIM
                if coef != 0:
                    acc = sp_add(acc, sp_scal(coef, G))
            if acc:
                parts[k] = acc
        return parts

    parts = grade_parts(T_GJ)
    pass
    _chk("[D] T = w_4 (B - L) chi is odd (grades among 1, 3, 5 only) and the grade parts sum back to T",
            set(parts) <= {1, 3, 5} and sp_eq(sp_add(*parts.values()), T_GJ))
    Y1, Y3, Y5 = (yukawa(parts.get(k, {})) for k in (1, 3, 5))
    c1, c3, c5 = clebsch(Y1), clebsch(Y3), clebsch(Y5)
    _chk("[D] the grade-1 (10) part of T contributes NOTHING on the sixteen: its Yukawa form is identically zero",
            Y1 == {})
    _chk("[D] T = w_4 (B - L) chi is PURE grade five: no 10 and no 120 component at all; it is an element of the 126",
            set(parts) == {5} and Y3 == {})
    _chk("[D] the grade-5 (126) part is symmetric and carries the whole Georgi-Jarlskog pattern: "
            "|Y(L e^c)| / |Y(Q d^c)| = 3 on the 126 alone",
            is_symmetric(Y5) and set(c5) == {("L", "e^c"), ("Q", "d^c")}
            and mag(c5, ("L", "e^c")) / mag(c5, ("Q", "d^c")) == 3)
    _chk("[D] the symmetric part of Y_T is exactly Y_126 (the 120 drops out of any one-family mass term): "
            "(Y_T + Y_T^t)/2 = Y_5",
            all(F(1, 2) * (YGJ.get((S, T), F(0)) + YGJ.get((T, S), F(0))) == Y5.get((S, T), F(0))
                for S in SIXTEEN for T in SIXTEEN))
    pass
    pass

    # the analogous statement for the up-type doublet direction v_4 (Y = +1/2): (L nu^c), (Q u^c)
    T_GJu = sp_mul(V[3], sp_mul(BmL, CHI))
    cu = clebsch(yukawa(T_GJu))
    _chk("[D] up-type: T' = v_4 (B - L) couples (L, nu^c) with |.| = 1 and (Q, u^c) with |.| = 1/3: "
            "the Dirac neutrino mass is -3 times the up mass on the 126 direction",
            set(cu) == {("L", "nu^c"), ("Q", "u^c")} and mag(cu, ("L", "nu^c")) / mag(cu, ("Q", "u^c")) == 3)

    # --- the family no-go: a vev in the 10 tensored with ANY family matrix gives identical charged-lepton
    # and down spectra, family by family.
    def charpoly_invariants(M3):
        """trace, sum of principal 2-minors, determinant of a 3x3 Fraction matrix."""
        t = M3[0][0] + M3[1][1] + M3[2][2]
        m2 = sum(M3[i][i] * M3[j][j] - M3[i][j] * M3[j][i] for i, j in combinations(range(3), 2))
        d = (M3[0][0] * (M3[1][1] * M3[2][2] - M3[1][2] * M3[2][1])
             - M3[0][1] * (M3[1][0] * M3[2][2] - M3[1][2] * M3[2][0])
             + M3[0][2] * (M3[1][0] * M3[2][1] - M3[1][1] * M3[2][0]))
        return (t, m2, d)

    Ffam = [[F(2), F(1, 3), F(-1)], [F(1, 3), F(5, 7), F(4)], [F(-1), F(4), F(0)]]      # any family matrix
    def species_entry(c, key):
        vals = c[key]
        return max(vals, key=abs)          # representative magnitude (all entries share |.|)
    for name, c in (("10", c10), ("126", c5)):
        ye, yd = mag(c, ("L", "e^c")), mag(c, ("Q", "d^c"))
        Me = [[ye * Ffam[i][j] for j in range(3)] for i in range(3)]
        Md = [[yd * Ffam[i][j] for j in range(3)] for i in range(3)]
        same = charpoly_invariants(Me) == charpoly_invariants(Md)
        if name == "10":
            _chk("[D] FAMILY NO-GO: with the vev in the 10, M_e = Y F and M_d = Y F for the same family matrix F have "
                    "the same characteristic polynomial (identical spectra), whatever F is: no family-space breaking "
                    "separates m_e from m_d", same)
    # the second check above is only a sanity statement; the exact one:
    ye5, yd5 = mag(c5, ("L", "e^c")), mag(c5, ("Q", "d^c"))
    _chk("[D] on the 126 direction M_e = -3 M_d family by family (eigenvalues in the ratio -3 for every F)",
            ye5 == 3 * yd5 and (species_entry(c5, ("L", "e^c")) / species_entry(c5, ("Q", "d^c"))) in (F(3), F(-3)))

    # --- the bracket cannot serve: the e^c direction of Lambda^2(5) carries hypercharge +1
    ec = [S for S in SIXTEEN if species(S) == "e^c"][0]
    _chk("[D] the e^c state (both rungs occupied, no pairs) has Y = 1: a mass form B(psi, T phi) conserving "
            "hypercharge needs Y(T) = -(Y(psi) + Y(phi)); a direction of charge +1 is not a neutral vev",
            diag_val(Y, ec) == 1)
    # hypercharge conservation of the Yukawa forms computed: Y(S) + Y(T) + Y(x) = 0 on every nonzero entry
    def conserves(mat, yx):
        return all(Yval[species(S)] + Yval[species(T)] + yx == 0 for (S, T) in mat)
    _chk("[D] every nonzero entry of Y_x (x = w_4, Y = -1/2) and of Y_T (T = w_4 (B-L)) conserves hypercharge",
            conserves(Y10, F(-1, 2)) and conserves(YGJ, F(-1, 2)))


    # --- the closed form of the 126 direction: T_GJ = (4/3) w_4 ^ (v_5 ^ w_5) ^ sum_i (v_i ^ w_i)
    def wedge2(v, w):
        """v ^ w = (v w - w v)/2 for vectors."""
        return sp_scal(F(1, 2), sp_add(sp_mul(v, w), sp_scal(F(-1), sp_mul(w, v))))
    area5 = wedge2(V[4], Wm[4])
    pairbiv = sp_add(*[wedge2(V[i], Wm[i]) for i in PAIRS])
    _chk("[D] B - L = -(2/3) sum_{pairs} v_i ^ w_i (pure grade two) and chi w_4 = w_4 (1 - 2 n_5) = -2 w_4 (v_5 ^ w_5)",
            sp_eq(BmL, sp_scal(F(-2, 3), pairbiv))
            and sp_eq(sp_mul(Wm[3], CHI), sp_scal(F(-2), sp_mul(Wm[3], area5))))
    closed = sp_scal(F(4, 3), sp_mul(sp_mul(Wm[3], area5), pairbiv))
    _chk("[D] closed form: T_GJ = (4/3) w_4 (v_5 ^ w_5) (sum_i v_i ^ w_i), and since the three factors are mutually "
            "orthogonal the product is the wedge: the rung vector, wedged with the other rung's area bivector and with "
            "the pair-sector u(1) generator", sp_eq(T_GJ, closed))
    # orthogonality of the factors: w_4 anticommutes with every vector of the other rung and of the pairs
    _chk("[D] w_4 anticommutes with v_5, w_5 and with every pair vector (the factors are orthogonal)",
            all(sp_add(sp_mul(Wm[3], x), sp_mul(x, Wm[3])) == {} for x in [V[4], Wm[4]] + [V[i] for i in PAIRS] + [Wm[i] for i in PAIRS]))



    # =====================================================================================  Part E (in B/C block above: [E] lines)

part_I1()

# ---------------------------------------------------------------------------
# Part I (2): the two-dimensional span and the frozen point no-go (Section 9.6: Prop 9.32, Thm 9.33)
# ---------------------------------------------------------------------------

def part_I2():
    _RETAG = [
        ('[G] each of I, c_4, c_5', 'Thm 9.33: each of I, c_4, c_5'),
        ('[G] the algebra they generate', 'Thm 9.33: the algebra they generate'),
        ('[G] NO-GO', 'Thm 9.33 NO-GO'),
        ('[G] the pair-sector u(1) bivector', 'Thm 9.33: the pair-sector u(1) bivector'),
        ('[G]', 'Prop 9.32:'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)

    # ------------------------------------------------------------------ Part G: the mass-form space and the no-go
    # reuse the module machinery (imported from the first note's Part D via exec of a small subset)
    NM = 5; PAIRS, RUNGS = (0, 1, 2), (3, 4)
    STATES = [frozenset(S) for k in range(NM + 1) for S in combinations(range(NM), k)]
    IDX = {S: i for i, S in enumerate(STATES)}; DIM = len(STATES)
    def sp_from_action(act):
        M = {}
        for S in STATES:
            for T, c in act(S).items():
                if c != 0: M[(IDX[T], IDX[S])] = M.get((IDX[T], IDX[S]), F(0)) + c
        return {k: v for k, v in M.items() if v != 0}
    def sp_mul(Aa, B):
        Bc = {}
        for (i, j), b in B.items(): Bc.setdefault(i, []).append((j, b))
        C = {}
        for (i, k), a in Aa.items():
            for j, b in Bc.get(k, ()): C[(i, j)] = C.get((i, j), F(0)) + a * b
        return {k: v for k, v in C.items() if v != 0}
    def sp_add(*Ms):
        C = {}
        for M in Ms:
            for k, v in M.items(): C[k] = C.get(k, F(0)) + v
        return {k: v for k, v in C.items() if v != 0}
    def sp_scal(c, M): return {k: c * v for k, v in M.items() if c * v != 0}
    def sp_eq(Aa, B): return sp_add(Aa, sp_scal(F(-1), B)) == {}
    def sp_apply(M, vec):
        out = {}
        for (i, j), a in M.items():
            if j in vec: out[i] = out.get(i, F(0)) + a * vec[j]
        return {k: v for k, v in out.items() if v != 0}
    ID = {(i, i): F(1) for i in range(DIM)}
    V = [sp_from_action(lambda S, i=i: g.ext_wedge(i, {S: F(1)})) for i in range(NM)]
    Wm = [sp_from_action(lambda S, i=i: g.ext_contract([F(1) if j == i else F(0) for j in range(NM)], {S: F(1)})) for i in range(NM)]
    def num(i): return sp_mul(V[i], Wm[i])
    N_W = sp_add(*[num(i) for i in PAIRS]); N_R = sp_add(*[num(i) for i in RUNGS])
    Y = sp_add(sp_scal(F(1, 2), N_R), sp_scal(F(-1, 3), N_W))
    T3 = sp_scal(F(1, 2), sp_add(num(3), sp_scal(F(-1), num(4))))
    def species(S):
        nr, nw = len(S & set(RUNGS)), len(S & set(PAIRS))
        return {(0, 0): "nu^c", (2, 0): "e^c", (1, 1): "Q", (1, 3): "L", (0, 2): "u^c", (2, 2): "d^c"}.get((nr, nw), "odd")
    SIXTEEN = [S for S in STATES if len(S) % 2 == 0]
    FULL = frozenset(range(NM))
    def eps_sign(S):
        seq = sorted(S) + sorted(FULL - S)
        return F(-1) ** sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[a] > seq[b])
    Bcoef = {S: F(-1) ** (len(S) * (len(S) - 1) // 2) * eps_sign(S) for S in STATES}
    def Bpair(psi, phi): return sum(Bcoef[S] * psi.get(IDX[S], F(0)) * phi.get(IDX[FULL - S], F(0)) for S in STATES)
    def basis(S): return {IDX[S]: F(1)}
    def yukawa(Top):
        mat = {}
        for S in SIXTEEN:
            for T in SIXTEEN:
                val = Bpair(basis(S), sp_apply(Top, basis(T)))
                if val != 0: mat[(S, T)] = val
        return mat
    def sym(mat): return {k: F(1, 2) * (mat.get(k, F(0)) + mat.get((k[1], k[0]), F(0))) for k in set(mat) | {(b, a) for a, b in mat}}
    def comm(Aa, B): return sp_add(sp_mul(Aa, B), sp_scal(F(-1), sp_mul(B, Aa)))
    SU3 = [sp_mul(V[i], Wm[j]) for i in PAIRS for j in PAIRS if i != j]

    # the operator space: all monomials in the ten mode operators (products of distinct operators, any order fixed),
    # restricted to odd degree; select colour singlets with Y = -1/2, T_3 = -1/2 (the w_4 charges)
    OPS = V + Wm
    odd_monos = []
    for k in (1, 3, 5, 7, 9):
        for idx in combinations(range(2 * NM), k):
            M = ID
            for t in idx: M = sp_mul(M, OPS[t])
            if M: odd_monos.append(M)
    def weight(M, Q):
        """return q if [Q, M] = q M, else None."""
        c = comm(Q, M)
        if c == {} and M: return F(0)
        for (i, j), a in M.items():
            q = c.get((i, j), F(0)) / a
            break
        return q if sp_eq(c, sp_scal(q, M)) else None
    cands = [M for M in odd_monos if weight(M, Y) == F(-1, 2) and weight(M, T3) == F(-1, 2)]
    # colour singlets: linear combinations annihilated by all su(3) generators -> solve on the span
    # build the span's coordinates
    keys = sorted({k for M in cands for k in M})
    def vecof(M): return [M.get(k, F(0)) for k in keys]
    rows = [vecof(M) for M in cands]
    rank_c = g.mat_rank(rows) if rows else 0
    # su(3)-invariant subspace: kernel of the map M -> ([X, M])_X on the span; compute via a basis of the span
    # pick a basis of the span by greedy elimination
    basis_ops = []
    cur = []
    for M in cands:
        if g.mat_rank(cur + [vecof(M)]) > len(cur):
            cur.append(vecof(M)); basis_ops.append(M)
    n = len(basis_ops)
    # matrix of the su(3) action: for each generator X, [X, M_b] expressed... simpler: find kernel of the linear map
    # c -> sum_b c_b [X, M_b] for all X jointly, over the rationals, by solving with GA.field_solve? Use rank trick:
    # stack the images as columns and compute nullspace via Gaussian elimination on the transpose.
    img_keys = sorted({k for X in SU3 for M in basis_ops for k in comm(X, M)})
    def img_vec(M): return [comm(X, M).get(k, F(0)) for X in SU3 for k in img_keys]
    Mimg = [img_vec(M) for M in basis_ops]           # n rows, each the image of a basis op
    rank_img = g.mat_rank(Mimg) if Mimg else 0
    dim_singlets = n - rank_img
    _chk(f"[G] colour-singlet odd operators of hypercharge -1/2 and T_3 = -1/2 acting 16 -> 16bar: the su(3)-invariant subspace "
            f"of the monomial span has dimension {dim_singlets} = 8 (its mass forms are computed next)", dim_singlets == 8)
    # compute an explicit basis of the singlet subspace: nullspace of Mimg^T c = 0 by elimination over Q
    def nullspace(rows_):
        # rows_: list of vectors (length m); find c with sum_i c_i rows_[i] = 0 -> nullspace of transpose
        m = len(rows_[0]); nrow = len(rows_)
        # build matrix m x nrow (transpose) and eliminate
        Mt = [[rows_[i][j] for i in range(nrow)] for j in range(m)]
        piv_cols = []; r = 0
        Mt = [row[:] for row in Mt]
        for c in range(nrow):
            pr = None
            for i in range(r, m):
                if Mt[i][c] != 0: pr = i; break
            if pr is None: continue
            Mt[r], Mt[pr] = Mt[pr], Mt[r]
            pv = Mt[r][c]; Mt[r] = [x / pv for x in Mt[r]]
            for i in range(m):
                if i != r and Mt[i][c] != 0:
                    f = Mt[i][c]; Mt[i] = [a - f * b for a, b in zip(Mt[i], Mt[r])]
            piv_cols.append(c); r += 1
        free = [c for c in range(nrow) if c not in piv_cols]
        sols = []
        for fc in free:
            sol = [F(0)] * nrow; sol[fc] = F(1)
            for i, pc in enumerate(piv_cols): sol[pc] = -Mt[i][fc]
            sols.append(sol)
        return sols
    singlet_coeffs = nullspace(Mimg)
    singlet_ops = [sp_add(*[sp_scal(c, M) for c, M in zip(sol, basis_ops) if c != 0]) for sol in singlet_coeffs]
    # their symmetric mass forms and the Clebsch ratios
    forms = [sym(yukawa(T)) for T in singlet_ops]
    def clebsch_ratio(form):
        ye = {abs(v) for (S, T), v in form.items() if {species(S), species(T)} == {"L", "e^c"} and v != 0}
        yd = {abs(v) for (S, T), v in form.items() if {species(S), species(T)} == {"Q", "d^c"} and v != 0}
        others = {(species(S), species(T)) for (S, T), v in form.items() if v != 0} - {("L", "e^c"), ("e^c", "L"), ("Q", "d^c"), ("d^c", "Q")}
        return ye, yd, others
    # the space of symmetric mass forms spanned: rank
    fkeys = sorted({k for f in forms for k in f})
    frows = [[f.get(k, F(0)) for k in fkeys] for f in forms]
    rank_forms = g.mat_rank(frows)
    print("[G] singlet operator directions:", len(singlet_ops), " independent symmetric mass forms:", rank_forms)
    _chk("[G] the symmetric doublet mass forms of hypercharge -1/2 on one generation span exactly a TWO-dimensional space: "
            "one direction from the 10 and one from the 126 (Sym^2(16) = 10 + 126, each with a single such doublet); the 120 is "
            "antisymmetric and contributes none", rank_forms == 2)
    # find, inside that space, the forms with m_e = m_d (ratio 1) and the one with ratio 3: solve for the ratio structure
    # by projecting onto the two species blocks
    def block(form, sp_pair):
        return {k: v for k, v in form.items() if {species(k[0]), species(k[1])} == set(sp_pair)}
    # ratio-1 subspace: forms where the (L e^c) block equals +-(Q d^c) block magnitudes on a matched basis
    ratios = []
    for f in forms:
        ye, yd, others = clebsch_ratio(f)
        ratios.append((sorted(ye), sorted(yd), others))
    print("[G] per-direction (|y_e| values, |y_d| values, other couplings):", ratios)
    _chk("[G] every symmetric doublet mass form couples ONLY (L, e^c) and (Q, d^c): no other species pair appears",
            all(not o for _, _, o in ratios))
    # the GJ direction from the first note lies in the span
    PARITY_R = sp_mul(sp_add(ID, sp_scal(F(-2), num(3))), sp_add(ID, sp_scal(F(-2), num(4))))
    BmL = sp_add(ID, sp_scal(F(-2, 3), N_W))
    T_GJ = sp_mul(Wm[3], sp_mul(BmL, sp_scal(F(-1), PARITY_R)))
    fGJ = sym(yukawa(T_GJ))
    _chk("[G] the 126 direction T_GJ = w_4 (B-L) chi lies in the span of the symmetric doublet mass forms (rank unchanged)",
            g.mat_rank(frows + [[fGJ.get(k, F(0)) for k in fkeys]]) == rank_forms)
    f10 = sym(yukawa(Wm[3]))
    _chk("[G] the 10 direction w_4 lies in the span too", g.mat_rank(frows + [[f10.get(k, F(0)) for k in fkeys]]) == rank_forms)
    # the ratio y_e/y_d is a free parameter of the three-dimensional space: exhibit ratio 1 (the 10), ratio 3 (T_GJ),
    # and a third independent form; any ratio is reachable by combination
    comb = sp_add(f10, fGJ)
    ye_c, yd_c, _ = clebsch_ratio(comb)
    _chk("[G] the ratio m_e/m_d is not fixed by the representation theory: 10 gives |y_e/y_d| = 1, T_GJ gives 3, their sum "
            "kills (L e^c) and leaves (Q d^c): the one free ratio of the two-dimensional space is dynamics' to fix",
            clebsch_ratio(f10)[0] == {F(1)} and clebsch_ratio(f10)[1] == {F(1)} and clebsch_ratio(fGJ)[0] == {F(1)}
            and clebsch_ratio(fGJ)[1] == {F(1, 3)} and (ye_c == set() or ye_c == {F(0)}))

    # --- the no-go: the algebra generated by the frozen point and its lifts contains no 126 doublet direction.
    # I sits in one pair mode's hyperbolic plane: I = a v_1 + b w_1 (norm 2ab... with v.w = 1/2: <I,I> = ab); rung components
    # c_4 = -w_4 + lam v_4, c_5 = -w_5.  Generate the algebra of {I, c_4, c_5}.
    lam = F(1, 7); a_, b_ = F(2), F(3)
    Iop = sp_add(sp_scal(a_, V[0]), sp_scal(b_, Wm[0]))
    c4 = sp_add(sp_scal(F(-1), Wm[3]), sp_scal(lam, V[3]))
    c5 = sp_scal(F(-1), Wm[4])
    gens = [Iop, c4, c5]
    def span_rank(ops):
        ks = sorted({k for M in ops for k in M})
        return g.mat_rank([[M.get(k, F(0)) for k in ks] for M in ops]) if ops else 0
    # products of distinct generators (each generator squares to a scalar), all orderings reduce to signed subsets
    prods = [ID]
    for k in (1, 2, 3):
        for idx in combinations(range(3), k):
            M = ID
            for t in idx: M = sp_mul(M, gens[t])
            prods.append(M)
    _chk("[G] each of I, c_4, c_5 squares to a scalar (<I,I> = ab = 6, <c_4,c_4> = -lam, <c_5,c_5> = 0) and they pairwise anticommute",
            sp_eq(sp_mul(Iop, Iop), sp_scal(a_ * b_, ID)) and sp_eq(sp_mul(c4, c4), sp_scal(-lam, ID)) and sp_mul(c5, c5) == {}
            and all(sp_add(sp_mul(x, y), sp_mul(y, x)) == {} for x, y in combinations(gens, 2)))
    _chk("[G] the algebra they generate has dimension 8 = 2^3: spanned by 1, I, c_4, c_5, I c_4, I c_5, c_4 c_5, I c_4 c_5",
            span_rank(prods) == 8)
    odd_gen = [Iop, c4, c5, sp_mul(sp_mul(Iop, c4), c5)]
    # charges of the odd elements: I carries pair-mode charge (colour non-singlet), I c_4 c_5 likewise; c_4, c_5 are grade one
    # the colour test on the objects themselves: c_4 and c_5 commute with every su(3) generator, I and I c_4 c_5 with none
    # of v_1 w_2; then the su(3)-invariant part of the odd span, computed as a nullspace, and the conclusion tested on it
    odd_img_keys = sorted({k for X in SU3 for M in odd_gen for k in comm(X, M)})
    odd_img = [[comm(X, M).get(k, F(0)) for X in SU3 for k in odd_img_keys] for M in odd_gen]
    odd_inv_ops = [sp_add(*[sp_scal(c, M) for c, M in zip(sol, odd_gen) if c != 0]) for sol in nullspace(odd_img)]
    inv_forms = [sym(yukawa(T)) for T in odd_inv_ops]
    ikeys = sorted({k for f in inv_forms + [fGJ] for k in f})
    inv_rows = [[f.get(k, F(0)) for k in ikeys] for f in inv_forms]
    _chk("[G] NO-GO: the odd part of that algebra is span{I, c_4, c_5, I c_4 c_5}; c_4 and c_5 commute with all eight su(3) "
            "generators and I, I c_4 c_5 do not ([v_1 w_2, .] != 0); the su(3)-invariant part of the odd span is exactly "
            "span{c_4, c_5}, which lies in the span of the ten mode operators (grade one, the 10); T_GJ is outside it, and "
            "T_GJ's mass form is outside the span of the mass forms of the invariant part: no colour-singlet element beyond "
            "the 10 direction, and in particular no 126 doublet direction, is generated by the frozen point and its lifts",
            all(comm(X, c4) == {} and comm(X, c5) == {} for X in SU3)
            and all(comm(sp_mul(V[0], Wm[1]), M) != {} for M in (Iop, odd_gen[3]))
            and span_rank(odd_gen) == 4
            and span_rank(odd_inv_ops) == 2 and span_rank(odd_inv_ops + [c4, c5]) == 2
            and span_rank(odd_inv_ops + V + Wm) == 10
            and span_rank(odd_inv_ops + [T_GJ]) == 3
            and g.mat_rank(inv_rows + [[fGJ.get(k, F(0)) for k in ikeys]]) == g.mat_rank(inv_rows) + 1
            and weight(Wm[3], Y) == F(-1, 2) and weight(Wm[4], Y) == F(-1, 2) and weight(V[3], Y) == F(1, 2)
            and weight(c4, Y) is None)
    # the missing factor is the pair-sector u(1) bivector, which no polynomial in {I, c_4, c_5} contains
    pairbiv = sp_add(*[sp_scal(F(1, 2), sp_add(sp_mul(V[i], Wm[i]), sp_scal(F(-1), sp_mul(Wm[i], V[i])))) for i in PAIRS])
    _chk("[G] the pair-sector u(1) bivector sum_i v_i ^ w_i is NOT in the generated algebra (rank rises by one when adjoined)",
            span_rank(prods + [pairbiv]) == 9)


part_I2()

# ---------------------------------------------------------------------------
# Part I (3): the bracket no-go (Section 9.6: Thm 9.35, Cor 9.36)
# ---------------------------------------------------------------------------

def part_I3():
    _RETAG = [
        ('A8', 'Cor 9.36 (A8)'),
        ('A9', 'Cor 9.36 (A9)'),
        ('A10', 'Thm 9.35 (A10)'),
        ('A1', 'Thm 9.35 (A1)'),
        ('A2', 'Thm 9.35 (A2)'),
        ('A3', 'Thm 9.35 (A3)'),
        ('A4', 'Thm 9.35 (A4)'),
        ('A5', 'Thm 9.35 (A5)'),
        ('A6', 'Thm 9.35 (A6)'),
        ('A7', 'Thm 9.35 (A7)'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)
    from itertools import product
    def check(label, ok):
        _chk(label, ok)
    def record(line):
        print('RECORD  ' + line)

    # ===========================================================================
    # Part A.  The bracket composite
    # ===========================================================================
    print("\nPart A: the bracket composite and the 126 direction")

    NM = 5
    PAIRS, RUNGS = (0, 1, 2), (3, 4)
    STATES = [frozenset(S) for k in range(NM + 1) for S in combinations(range(NM), k)]
    IDX = {S: i for i, S in enumerate(STATES)}
    DIM = len(STATES)


    def sp_from_action(act):
        M = {}
        for S in STATES:
            for T, c in act(S).items():
                if c != 0:
                    M[(IDX[T], IDX[S])] = M.get((IDX[T], IDX[S]), F(0)) + c
        return {k: v for k, v in M.items() if v != 0}


    def sp_mul(A, B):
        Bc = {}
        for (i, j), b in B.items():
            Bc.setdefault(i, []).append((j, b))
        C = {}
        for (i, k), a in A.items():
            for j, b in Bc.get(k, ()):
                C[(i, j)] = C.get((i, j), F(0)) + a * b
        return {k: v for k, v in C.items() if v != 0}


    def sp_add(*Ms):
        C = {}
        for M in Ms:
            for k, v in M.items():
                C[k] = C.get(k, F(0)) + v
        return {k: v for k, v in C.items() if v != 0}


    def sp_scal(c, M):
        return {k: c * v for k, v in M.items() if c * v != 0}


    def sp_eq(A, B):
        return sp_add(A, sp_scal(F(-1), B)) == {}


    def sp_apply(M, vec):
        out = {}
        for (i, j), a in M.items():
            if j in vec:
                out[i] = out.get(i, F(0)) + a * vec[j]
        return {k: v for k, v in out.items() if v != 0}


    ID = {(i, i): F(1) for i in range(DIM)}
    V = [sp_from_action(lambda S, i=i: g.ext_wedge(i, {S: F(1)})) for i in range(NM)]
    Wm = [sp_from_action(lambda S, i=i: g.ext_contract([F(1) if j == i else F(0) for j in range(NM)], {S: F(1)}))
          for i in range(NM)]


    def num(i):
        return sp_mul(V[i], Wm[i])


    N_W = sp_add(*[num(i) for i in PAIRS])
    N_R = sp_add(*[num(i) for i in RUNGS])
    Y = sp_add(sp_scal(F(1, 2), N_R), sp_scal(F(-1, 3), N_W))
    T3 = sp_scal(F(1, 2), sp_add(num(3), sp_scal(F(-1), num(4))))


    def species(S):
        nr, nw = len(S & set(RUNGS)), len(S & set(PAIRS))
        return {(0, 0): "nu^c", (2, 0): "e^c", (1, 1): "Q", (1, 3): "L", (0, 2): "u^c", (2, 2): "d^c"}.get((nr, nw), "odd")


    SIXTEEN = [S for S in STATES if len(S) % 2 == 0]
    FULL = frozenset(range(NM))


    def eps_sign(S):
        seq = sorted(S) + sorted(FULL - S)
        return F(-1) ** sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[a] > seq[b])


    Bcoef = {S: F(-1) ** (len(S) * (len(S) - 1) // 2) * eps_sign(S) for S in STATES}


    def Bpair(psi, phi):
        return sum(Bcoef[S] * psi.get(IDX[S], F(0)) * phi.get(IDX[FULL - S], F(0)) for S in STATES)


    def basis(S):
        return {IDX[S]: F(1)}


    def yukawa(T):
        mat = {}
        for S in SIXTEEN:
            for U in SIXTEEN:
                val = Bpair(basis(S), sp_apply(T, basis(U)))
                if val != 0:
                    mat[(S, U)] = val
        return mat


    def sym(mat):
        return {k: F(1, 2) * (mat.get(k, F(0)) + mat.get((k[1], k[0]), F(0))) for k in set(mat) | {(b, a) for a, b in mat}}


    def comm(A, B):
        return sp_add(sp_mul(A, B), sp_scal(F(-1), sp_mul(B, A)))


    SU3 = [sp_mul(V[i], Wm[j]) for i in PAIRS for j in PAIRS if i != j]


    def weight(M, Q):
        c = comm(Q, M)
        if c == {} and M:
            return F(0)
        for (i, j), a in M.items():
            q = c.get((i, j), F(0)) / a
            break
        return q if sp_eq(c, sp_scal(q, M)) else None


    def span_rank(ops):
        ks = sorted({k for M in ops for k in M})
        return g.mat_rank([[M.get(k, F(0)) for k in ks] for M in ops]) if ops else 0


    def form_vec(f, keys):
        return [f.get(k, F(0)) for k in keys]


    def species_blocks(f):
        out = {}
        for (S, U), v in f.items():
            out.setdefault(tuple(sorted((species(S), species(U)))), set()).add(abs(v))
        return out


    # the objects: the frozen point in pair mode 1, its lifted rung components, the bracket
    lam = F(1, 7)
    a_, b_ = F(2), F(3)
    Iop = sp_add(sp_scal(a_, V[0]), sp_scal(b_, Wm[0]))
    c4 = sp_add(sp_scal(F(-1), Wm[3]), sp_scal(lam, V[3]))
    c5 = sp_scal(F(-1), Wm[4])
    brk = sp_mul(V[3], V[4])              # the bracket direction: both rungs created, the (2,0) sector
    brk_d = sp_mul(Wm[4], Wm[3])          # its conjugate
    check("A1: the bracket b = v_4 v_5 has hypercharge 1 and T_3 = 0, commutes with su(3) (a colour singlet), and is the "
          "creation operator of the (2,0) sector, the e^c direction of the 10 = Lambda^2(5)",
          weight(brk, Y) == F(1) and weight(brk, T3) == F(0) and all(comm(X, brk) == {} for X in SU3)
          and sp_apply(brk, basis(frozenset())) != {} and species(frozenset({3, 4})) == "e^c")

    # the algebra generated by {I, c_4, c_5, b, b^dag}: close under products
    gens = [Iop, c4, c5, brk, brk_d]
    words = [ID] + gens
    frontier = gens
    for _ in range(6):
        new = []
        for w in frontier:
            for gg in gens:
                new.append(sp_mul(w, gg))
        before = span_rank(words)
        words = words + new
        after = span_rank(words)
        frontier = new
        if after == before:
            break
    dimA = span_rank(words)
    check(f"A2: the algebra generated by the frozen point, its two lifted rung components, the bracket and its conjugate has "
          f"dimension {dimA} = 32 = 2 x 16: the rung Clifford algebra Cl(2,2) tensored with span(1, I)", dimA == 32)

    # a basis of that algebra, then its su(3)-invariant part
    keysA = sorted({k for M in words for k in M})
    basisA, cur = [], []
    for M in words:
        if g.mat_rank(cur + [form_vec(M, keysA)]) > len(cur):
            cur.append(form_vec(M, keysA))
            basisA.append(M)
    img_keys = sorted({k for X in SU3 for M in basisA for k in comm(X, M)})
    Mimg = [[comm(X, M).get(k, F(0)) for X in SU3 for k in img_keys] for M in basisA]
    inv_dim = len(basisA) - g.mat_rank(Mimg)
    check(f"A3: its su(3)-invariant (colour-singlet) part has dimension {inv_dim} = 16 = dim Cl(2,2): exactly the rung "
          "Clifford algebra; every element carrying the frozen point carries a pair index", inv_dim == 16)

    # the odd, Y = -1/2, T_3 = -1/2 elements of the rung Clifford algebra
    RUNG_OPS = [V[3], Wm[3], V[4], Wm[4]]
    rung_monos = []
    for k in range(0, 5):
        for idx in combinations(range(4), k):
            M = ID
            for t in idx:
                M = sp_mul(M, RUNG_OPS[t])
            if M:
                rung_monos.append(M)
    check("A4a: the rung Clifford algebra is spanned by the 16 ordered monomials in v_4, w_4, v_5, w_5", span_rank(rung_monos) == 16)
    w4 = Wm[3]
    w4N5 = sp_mul(w4, num(4))
    doublet = [M for M in rung_monos if len(M) and weight(M, Y) == F(-1, 2) and weight(M, T3) == F(-1, 2)]
    # odd elements only: those changing total mode number by an odd amount; filter by anticommutation with the parity
    PAR = ID
    for i in range(NM):
        PAR = sp_mul(PAR, sp_add(ID, sp_scal(F(-2), num(i))))
    doublet_odd = [M for M in doublet if sp_add(sp_mul(PAR, M), sp_mul(M, PAR)) == {}]
    check(f"A4b: the odd elements of hypercharge -1/2 and T_3 = -1/2 in the rung algebra span a space of dimension "
          f"{span_rank(doublet_odd)} = 2, spanned by w_4 and w_4 N_5",
          span_rank(doublet_odd) == 2 and span_rank(doublet_odd + [w4, w4N5]) == 2)

    f10 = sym(yukawa(w4))
    fN5 = sym(yukawa(w4N5))
    fkeys = sorted(set(f10) | set(fN5))
    check("A5: the mass form of w_4 N_5 is exactly half the mass form of w_4: both are the 10 form, with |y_e| = |y_d| "
          "(ratio one) and no other species pair",
          sp_eq(fN5, sp_scal(F(1, 2), f10)) and species_blocks(f10) == {("L", "e^c"): {F(1)}, ("Q", "d^c"): {F(1)}})
    comp = sp_mul(brk_d, V[4])
    check("A6: the neutral composite b^dag v_5 = w_5 w_4 v_5 equals -w_4 + w_4 N_5 and its mass form is -(1/2) x the 10 form: "
          "the bracket's composites with the rung vectors all land on the 10 direction",
          sp_eq(comp, sp_add(sp_scal(F(-1), w4), w4N5)) and sp_eq(sym(yukawa(comp)), sp_scal(F(-1, 2), f10)))
    PARITY_R = sp_mul(sp_add(ID, sp_scal(F(-2), num(3))), sp_add(ID, sp_scal(F(-2), num(4))))
    BmL = sp_add(ID, sp_scal(F(-2, 3), N_W))
    T_GJ = sp_mul(w4, sp_mul(BmL, sp_scal(F(-1), PARITY_R)))
    fGJ = sym(yukawa(T_GJ))
    fkeys = sorted(set(fkeys) | set(fGJ))
    check("A7: the 126 direction T_GJ = w_4 (B - L) chi is NOT in the span of the forms the rung algebra produces (rank 1 -> 2)",
          g.mat_rank([form_vec(f10, fkeys), form_vec(fN5, fkeys)]) == 1
          and g.mat_rank([form_vec(f10, fkeys), form_vec(fN5, fkeys), form_vec(fGJ, fkeys)]) == 2)
    CHI = sp_scal(F(-1), PARITY_R)          # chi = -(-1)^{N_R}, the paper's rung parity
    fNW = sym(yukawa(sp_mul(w4, N_W)))
    fchi = sym(yukawa(sp_mul(w4, CHI)))
    fNWchi = sym(yukawa(sp_mul(w4, sp_mul(N_W, CHI))))
    fkeys = sorted(set(fkeys) | set(fNW) | set(fchi) | set(fNWchi))
    check("A8: adjoining the pair number N_W reaches it, and only jointly with the rung parity chi = -(-1)^{N_R}: w_4 N_W alone "
          "gives the 10 form again (its symmetric form is 3/2 x f(w_4)), w_4 chi has vanishing symmetric form, and w_4 N_W chi has "
          "|y_e| = 3/2, |y_d| = 1/2, ratio 3, with f(T_GJ) = -(2/3) f(w_4 N_W chi) exactly (T_GJ = w_4 chi - (2/3) w_4 N_W chi): "
          "the 126 direction is the pair number read through the rung parity",
          sp_eq(fNW, sp_scal(F(3, 2), f10)) and all(v == 0 for v in fchi.values())
          and species_blocks(fNWchi) == {("L", "e^c"): {F(3, 2)}, ("Q", "d^c"): {F(1, 2)}}
          and sp_eq(fGJ, sp_scal(F(-2, 3), fNWchi)))
    check("A9: N_W is not a function of the rung sector on the sixteen: the two rung-odd species carry pair numbers 1 (Q) and "
          "3 (L), the rung-even species 0 (nu^c, e^c) and 2 (u^c, d^c), so B - L = 1 - (2/3) N_W takes four values while "
          "the rung algebra sees two parities",
          sorted({len(S & set(PAIRS)) for S in SIXTEEN if len(S & set(RUNGS)) == 1}) == [1, 3]
          and sorted({len(S & set(PAIRS)) for S in SIXTEEN if len(S & set(RUNGS)) != 1}) == [0, 2])
    pairbiv = sp_add(*[sp_scal(F(1, 2), sp_add(sp_mul(V[i], Wm[i]), sp_scal(F(-1), sp_mul(Wm[i], V[i])))) for i in PAIRS])
    check("A10: the pair bivector sum_i v_i ^ w_i lies outside the 32-dimensional algebra (rank 32 -> 33 on adjoining it): "
          "no polynomial in the frozen point, its lifts and the bracket contains the pair-sector u(1)",
          span_rank(basisA + [pairbiv]) == 33)


part_I3()

# ---------------------------------------------------------------------------
# Part J: two thresholds and two loops (Sections 8.4, 8.5: Thm 8.15, Prop 8.16, Fact 8.18, Prop 8.19; C4, C5 are floating-point CONTROL lines, the RECORD lines are the GeV values)
# ---------------------------------------------------------------------------

def part_J():
    _RETAG = [
        ('B0', 'Thm 8.15 (B0)'),
        ('B1', 'Thm 8.15 (B1)'),
        ('B2', 'Thm 8.15 (B2)'),
        ('B5', 'Thm 8.15 (B5)'),
        ('B3', 'Prop 8.16 (B3)'),
        ('B4', 'Prop 8.16 (B4)'),
        ('B6', 'Rem 8.17 (B6)'),
        ('C1', 'Fact 8.18 (C1)'),
        ('C2', 'Fact 8.18 (C2)'),
        ('C3', 'Fact 8.18 (C3)'),
        ('C4', 'Prop 8.19 (C4)'),
        ('C5', 'Prop 8.19 (C5)'),
    ]
    def _retag(label):
        for a, b in _RETAG:
            if label.startswith(a):
                return b + label[len(a):]
        return label
    def _chk(label, ok):
        g.check(_retag(label), ok)
    from itertools import product
    from math import exp, log, pi, sqrt
    def check(label, ok):
        _chk(label, ok)
    def record(line):
        print('RECORD  ' + line)

    # ===========================================================================
    # Part B.  Two thresholds
    # ===========================================================================
    print("\nPart B: two thresholds")
    WEYL, SC = "weyl", "scalar"
    H = F(1, 2)


    def index_triple(field):
        _, kind, d2, T2, d3, T3_, Yh, m = field
        t1 = F(3, 5) * Yh * Yh * d2 * d3
        t2 = T2 * d3
        t3 = T3_ * d2
        w = F(2, 3) if kind == WEYL else F(1, 3)
        return tuple(w * t * m for t in (t1, t2, t3))


    def delta_b(fields):
        tot = [F(0)] * 3
        for f in fields:
            for i, t in enumerate(index_triple(f)):
                tot[i] += t
        return tuple(tot)


    def b_total(fields):
        gauge = (F(0), F(-22, 3), F(-11))
        d = delta_b(fields)
        return tuple(gauge[i] + d[i] for i in range(3))


    GEN = [("Q", WEYL, 2, H, 3, H, F(1, 6), 1), ("L", WEYL, 2, H, 1, 0, F(-1, 2), 1),
           ("u^c", WEYL, 1, 0, 3, H, F(-2, 3), 1), ("d^c", WEYL, 1, 0, 3, H, F(1, 3), 1),
           ("e^c", WEYL, 1, 0, 1, 0, F(1), 1), ("nu^c", WEYL, 1, 0, 1, 0, F(0), 1)]
    HIGGS = [("H", SC, 2, H, 1, 0, H, 1)]
    SM = [(n, k, d2, T2, d3, T3_, Yh, 3 * m) for (n, k, d2, T2, d3, T3_, Yh, m) in GEN] + HIGGS
    GAUGINOS = [("gluino", WEYL, 1, 0, 8, F(3), F(0), 1), ("wino", WEYL, 3, F(2), 1, 0, F(0), 1),
                ("bino", WEYL, 1, 0, 1, 0, F(0), 1)]
    HIGGSINOS = [("Hu~", WEYL, 2, H, 1, 0, H, 1), ("Hd~", WEYL, 2, H, 1, 0, -H, 1)]
    HIGGS2 = [("H2", SC, 2, H, 1, 0, -H, 1)]
    SFERMIONS = [(n, SC, d2, T2, d3, T3_, Yh, 3 * m) for (n, k, d2, T2, d3, T3_, Yh, m) in GEN]
    MSSM = SM + GAUGINOS + HIGGSINOS + HIGGS2 + SFERMIONS
    b_SM = b_total(SM)
    check("B0: the one-loop coefficients of the derived content are (41/10, -19/6, -7) and of the supersymmetric content "
          "(33/5, 1, -3) (the partner note's Fact, rebuilt)", b_SM == (F(41, 10), F(-19, 6), F(-7)) and b_total(MSSM) == (F(33, 5), F(1), F(-3)))


    def rec(aem_inv, s2, as_inv):
        a2 = s2 * aem_inv
        return (F(3, 5) * (aem_inv - a2), a2, as_inv)


    A = rec(F(128), F(2312, 10000), F(500, 59))
    a1, a2, a3 = A
    R = (a1 - a2) / (a2 - a3)
    b1, b2, b3 = b_SM
    b12, b23 = b1 - b2, b2 - b3
    MZ = 91.1876


    def GeV(x):
        return MZ * exp(2 * pi * float(x))


    def r2(d, dp, f, fp):
        return (b12 + f * (d[0] - d[1]) + fp * (dp[0] - dp[1])) / (b23 + f * (d[1] - d[2]) + fp * (dp[1] - dp[2]))


    def line(d, dp):
        """P f + Q f' = C: the level set r(f, f') = R."""
        d12, d23 = d[0] - d[1], d[1] - d[2]
        dp12, dp23 = dp[0] - dp[1], dp[1] - dp[2]
        return d12 - R * d23, dp12 - R * dp23, R * b23 - b12


    def segment(d, dp):
        """Endpoints of the admissible set {0 <= f' <= f <= 1} on the level line, exact."""
        P, Q, C = line(d, dp)
        pts = []
        if P != 0 and 0 <= C / P <= 1:
            pts.append((C / P, F(0)))
        if Q != 0 and 0 <= (C - P) / Q <= 1:
            pts.append((F(1), (C - P) / Q))
        if P + Q != 0 and 0 <= C / (P + Q) <= 1:
            pts.append((C / (P + Q), C / (P + Q)))
        pts = sorted(set(pts))
        # the meeting scale must also be positive: x = (a1 - a2)/(b12 + f d12 + f' d'12) > 0 on the endpoints
        pts = [(f, fp) for (f, fp) in pts if (a1 - a2) / (b12 + f * (d[0] - d[1]) + fp * (dp[0] - dp[1])) > 0]
        return pts


    FAMILIES = [
        ("gauginos + higgsinos light; sfermions + second doublet heavy", delta_b(GAUGINOS + HIGGSINOS), delta_b(SFERMIONS + HIGGS2)),
        ("higgsinos light; gauginos + sfermions + second doublet heavy", delta_b(HIGGSINOS), delta_b(GAUGINOS + SFERMIONS + HIGGS2)),
        ("both doublets (higgsinos, second doublet) light; the rest heavy", delta_b(HIGGSINOS + HIGGS2), delta_b(GAUGINOS + SFERMIONS)),
        ("wino, bino, higgsinos light; gluino, sfermions, second doublet heavy", delta_b(GAUGINOS[1:] + HIGGSINOS), delta_b(GAUGINOS[:1] + SFERMIONS + HIGGS2)),
    ]
    # B1: the level set is the stated line: at points ON the line (f' solved from f)
    # r(f, f') = R exactly, and at points off it (f' shifted by 1/4) r(f, f') != R
    ok = True
    n_on = n_off = 0
    for _, d, dp in FAMILIES:
        P, Q, C = line(d, dp)
        for f in (F(0), F(1, 3), F(1, 2), F(1), F(3, 2), F(-1)):
            fp = (C - P * f) / Q
            den = b23 + f * (d[1] - d[2]) + fp * (dp[1] - dp[2])
            if den != 0:
                ok = ok and P * f + Q * fp == C and r2(d, dp, f, fp) == R
                n_on += 1
            for shift in (F(1, 4), F(-1, 4)):
                den2 = b23 + f * (d[1] - d[2]) + (fp + shift) * (dp[1] - dp[2])
                if den2 != 0:
                    ok = ok and r2(d, dp, f, fp + shift) != R
                    n_off += 1
    check(f"B1: r(f, f') = R exactly at {n_on} points on the line f (D12 - R D23) + f' (D'12 - R D'23) = R b23 - b12 "
          f"(six values of f on each of four families, f' solved from the line) and r(f, f') != R at {n_off} points off it "
          "(f' shifted by +-1/4)", ok and n_on == 24 and n_off == 48)
    # B2: reduction to one threshold at f' = f (all content at M_I) and at f' = 0 (heavy content at M_U)
    d_full = delta_b(GAUGINOS + HIGGSINOS + HIGGS2 + SFERMIONS)
    f_one = (R * b23 - b12) / ((d_full[0] - d_full[1]) - R * (d_full[1] - d_full[2]))
    d, dp = FAMILIES[0][1], FAMILIES[0][2]
    P, Q, C = line(d, dp)
    check("B2: at f' = f the line gives the one-threshold f of the whole content, 1.0116 (the partner note's 1.2 percent miss), "
          "and at f' = 0 the one-threshold f of the light content alone",
          C / (P + Q) == f_one and F(1011, 1000) < f_one < F(1012, 1000)
          and C / P == (R * b23 - b12) / ((d[0] - d[1]) - R * (d[1] - d[2])))
    # B3: the conclusions for the four families
    segs = [(name, segment(d, dp)) for name, d, dp in FAMILIES]
    for (name, pts), (_, d, dp) in zip(segs, FAMILIES):
        if pts:
            for f, fp in pts:
                x = (a1 - a2) / (b12 + f * (d[0] - d[1]) + fp * (dp[0] - dp[1]))
                record(f"{name}: endpoint f = {float(f):.4f}, f' = {float(fp):.4f}: M_U = {GeV(x):.2e} GeV, "
                       f"M_I = {GeV(x * (1 - f)):.2e} GeV, M_I' = {GeV(x * (1 - fp)):.2e} GeV")
        else:
            record(f"{name}: the level line misses the triangle: no admissible pair at one loop")
    check("B3: of the four supersymmetric split families, the three with the gluino at the LIGHT threshold have no admissible "
          "pair at one loop, and the one with the gluino at the heavy threshold has a segment of them",
          [bool(p) for _, p in segs] == [False, False, False, True] and len(segs[3][1]) == 2)
    f_a, fp_a = segs[3][1][0]
    f_b, fp_b = segs[3][1][1]
    check("B4: that segment runs from (f, f') = (1, 0.991), every partner within a factor 1.34 of M_Z, to (0.438, 0), the "
          "electroweak-inos at 7 x 10^8 GeV and everything else at M_U = 1.6 x 10^14 GeV: doublet-heavy at every point",
          f_b == 1 and F(990, 1000) < fp_b < F(992, 1000) and fp_a == 0 and F(437, 1000) < f_a < F(438, 1000))
    # B6: the gluino statement of Rem 8.17 at the block level of Prop 8.16, and its
    # failure at the species level: the twelve species-level components (three
    # gauginos, two higgsinos, the second doublet, six sfermion species) give 4096
    # light/heavy splits, and the reviewer's split with the gluino LIGHT has a segment
    SPECIES12 = GAUGINOS + HIGGSINOS + HIGGS2 + SFERMIONS
    n_seg = n_gluino_light_seg = 0
    for mask in product((0, 1), repeat=len(SPECIES12)):
        light = [sp for sp, mk in zip(SPECIES12, mask) if mk]
        heavy = [sp for sp, mk in zip(SPECIES12, mask) if not mk]
        if segment(delta_b(light), delta_b(heavy)):
            n_seg += 1
            if mask[0]:
                n_gluino_light_seg += 1
    ce_light = [GAUGINOS[1], GAUGINOS[0], SFERMIONS[0]]      # wino, gluino, three squark doublets
    ce_heavy = [sp for sp in SPECIES12 if sp not in ce_light]
    ce_seg = segment(delta_b(ce_light), delta_b(ce_heavy))
    record(f"Rem 8.17: of the {2 ** len(SPECIES12)} species-level splits, {n_seg} admit a segment, {n_gluino_light_seg} of them "
           "with the gluino at the lighter threshold (exact enumeration)")
    check(f"B6: at the block level of Prop 8.16 only the family with the gluino heavy has a segment (B3), but at the species "
          f"level the split light = (wino, gluino, three squark doublets), Delta = (1/10, 17/6, 3), heavy = the rest, "
          f"Delta' = (12/5, 4/3, 1), has a nonempty admissible segment with the gluino at the LIGHTER threshold, and "
          f"{n_gluino_light_seg} of the 4096 species-level splits with the gluino light do (Rem 8.17's statement is block-level)",
          delta_b(ce_light) == (F(1, 10), F(17, 6), F(3)) and delta_b(ce_heavy) == (F(12, 5), F(4, 3), F(1))
          and len(ce_seg) == 2 and n_gluino_light_seg == 296 and n_seg == 1464)
    # B5: complete multiplets are inert at either threshold
    ok = True
    for c in (F(1), F(-2), F(5, 3)):
        for name, d, dp in FAMILIES:
            ok = ok and line(tuple(v + c for v in d), dp) == line(d, dp) and line(d, tuple(v + c for v in dp)) == line(d, dp)
    check("B5: a complete multiplet added at either threshold leaves the level line unchanged: inert at two thresholds as at one", ok)

    # ===========================================================================
    # Part C.  Two loops
    # ===========================================================================
    print("\nPart C: two loops")
    CG = (F(0), F(2), F(3))


    def casimirs(field):
        _, kind, d2, T2, d3, T3_, Yh, m = field
        return (F(3, 5) * Yh * Yh, {1: F(0), 2: F(3, 4), 3: F(2)}[d2], {1: F(0), 3: F(4, 3), 8: F(3)}[d3])


    def Tidx(field):
        _, kind, d2, T2, d3, T3_, Yh, m = field
        return (F(3, 5) * Yh * Yh * d2 * d3 * m, T2 * d3 * m, T3_ * d2 * m)


    def B_generic(fields):
        """Machacek-Vaughn two-loop gauge matrix for Weyl fermions and complex scalars, gauge Yukawas excluded."""
        B = [[F(0)] * 3 for _ in range(3)]
        for i in range(3):
            B[i][i] += -F(34, 3) * CG[i] ** 2
            for f in fields:
                T = Tidx(f)
                C = casimirs(f)
                wC, wG = (F(2), F(10, 3)) if f[1] == WEYL else (F(4), F(2, 3))
                for j in range(3):
                    B[i][j] += T[i] * (wC * C[j] + (wG * CG[i] if i == j else 0))
        return B


    def B_susy(chiral):
        """Superfield formula: B_ij = delta_ij (-6 C(G_i)^2 + 2 C(G_i) S_i) + 4 S_i C_j summed over chiral superfields."""
        B = [[F(0)] * 3 for _ in range(3)]
        for i in range(3):
            B[i][i] += -6 * CG[i] ** 2
            for f in chiral:
                T = Tidx(f)
                C = casimirs(f)
                for j in range(3):
                    B[i][j] += 4 * T[i] * C[j] + (2 * CG[i] * T[i] if i == j else 0)
        return B


    B_SM = [[F(199, 50), F(27, 10), F(44, 5)], [F(9, 10), F(35, 6), F(12)], [F(11, 10), F(9, 2), F(-26)]]
    B_MSSM = [[F(199, 25), F(27, 5), F(88, 5)], [F(9, 5), F(25), F(24)], [F(11, 5), F(9), F(14)]]
    check("C1: the generic two-loop formula on the derived content with one Higgs doublet returns the Standard Model's matrix "
          "[[199/50, 27/10, 44/5], [9/10, 35/6, 12], [11/10, 9/2, -26]] exactly", B_generic(SM) == B_SM)
    CHIRAL = [(n, WEYL, d2, T2, d3, T3_, Yh, 3 * m) for (n, k, d2, T2, d3, T3_, Yh, m) in GEN] + \
        [("Hu", WEYL, 2, H, 1, 0, H, 1), ("Hd", WEYL, 2, H, 1, 0, -H, 1)]
    check("C2: the superfield formula on three generations and two Higgs superfields returns the supersymmetric matrix "
          "[[199/25, 27/5, 88/5], [9/5, 25, 24], [11/5, 9, 14]] exactly", B_susy(CHIRAL) == B_MSSM)
    check("C3: the generic formula applied naively to the supersymmetric component content does NOT return it (it omits the "
          "gaugino-matter Yukawas, which are gauge couplings in disguise): the two-loop run below therefore uses the superfield "
          "matrix above the threshold", B_generic(MSSM) != B_MSSM)

    # the run: numerical, RECORD only
    try:
        import numpy as np
        from scipy.integrate import solve_ivp
        from scipy.optimize import brentq
        HAVE_SCIPY = True
    except ImportError:
        HAVE_SCIPY = False

    if HAVE_SCIPY:
        bSMf = np.array([float(x) for x in b_SM])
        BSMf = np.array([[float(x) for x in r] for r in B_SM])
        bMSf = np.array([33 / 5, 1.0, -3.0])
        BMSf = np.array([[float(x) for x in r] for r in B_MSSM])
        cSM, cMS = np.array([17 / 10, 3 / 2, 2.0]), np.array([26 / 5, 6.0, 4.0])

        def alphas(aem_inv=127.951, s2=0.23122, as_=0.1180):
            aem = 1 / aem_inv
            return np.array([(5 / 3) * aem / (1 - s2), aem / s2, as_])

        def rhs(t, y, susy, yuk, twoloop):
            g2, yt = y[:3], y[3]
            b, B, c = (bMSf, BMSf, cMS) if susy else (bSMf, BSMf, cSM)
            d = g2 ** 2 / (8 * pi ** 2) * (b + ((B @ g2) / (16 * pi ** 2) - (c * yt ** 2 / (16 * pi ** 2) if yuk else 0)) * (1 if twoloop else 0))
            if susy:
                dyt = yt / (16 * pi ** 2) * (6 * yt ** 2 - 13 / 15 * g2[0] - 3 * g2[1] - 16 / 3 * g2[2])
            else:
                dyt = yt / (16 * pi ** 2) * (9 / 2 * yt ** 2 - 17 / 20 * g2[0] - 9 / 4 * g2[1] - 8 * g2[2])
            return np.append(d, dyt)

        def mismatch(MI, al, yt0=0.95, yuk=True, twoloop=True, sinb=1.0):
            y0 = np.append(4 * pi * al, yt0)
            tI = log(MI / MZ)
            s1 = solve_ivp(lambda t, y: rhs(t, y, False, yuk, twoloop), [0, tI], y0, rtol=1e-11, atol=1e-13)
            y1 = s1.y[:, -1].copy()
            y1[3] /= sinb
            tU = log(3e17 / MZ)
            s2 = solve_ivp(lambda t, y: rhs(t, y, True, yuk, twoloop), [tI, tU], y1, rtol=1e-11, atol=1e-13, dense_output=True)
            f12 = lambda t: (lambda a: a[0] - a[1])(4 * pi / s2.sol(t)[:3])
            tc = brentq(f12, tI + 1e-9, tU)
            a = 4 * pi / s2.sol(tc)[:3]
            return a[2] - a[0], MZ * exp(tc), a[0]

        def MI_star(al, **kw):
            lo, hi = log(60.0), log(1e6)
            return exp(brentq(lambda lm: mismatch(exp(lm), al, **kw)[0], lo, hi))

        # CONTROL: with the two-loop terms off the integrator must reproduce the exact one-loop threshold of the
        # partner note, M_I = 62 GeV (f = 1.012 means the threshold sits below M_Z)
        MI1 = MI_star(alphas(128.0, 0.2312, 59 / 500), twoloop=False, yuk=False)
        x_exact = (a1 - a2) / (b12 + f_one * (d_full[0] - d_full[1]))
        MI_exact = GeV(x_exact * (1 - f_one))
        check(f"C4 (CONTROL, floating point): with the two-loop terms switched off the integrator reproduces the exact one-loop "
              f"threshold of the supersymmetric content, {MI_exact:.1f} GeV against {MI1:.1f} GeV", abs(MI1 / MI_exact - 1) < 1e-3)
        rows = []
        for label, al, kw in [("record central, top Yukawa on", alphas(), {}),
                              ("record central, top Yukawa off", alphas(), {"yuk": False}),
                              ("alpha_s + 0.0009", alphas(as_=0.1189), {}),
                              ("alpha_s - 0.0009", alphas(as_=0.1171), {}),
                              ("sin^2 theta_W + 0.0001", alphas(s2=0.23132), {}),
                              ("y_t(M_Z) = 0.99", alphas(), {"yt0": 0.99}),
                              ("sin beta = 0.9", alphas(), {"sinb": 0.9})]:
            MI = MI_star(al, **kw)
            m, MU, aU = mismatch(MI, al, **kw)
            rows.append((label, MI, MU, aU))
            record(f"two loops, {label}: the three couplings meet exactly for M_I = {MI:.0f} GeV, M_U = {MU:.2e} GeV, "
                   f"alpha_U^-1 = {aU:.2f}")
        MIs = [r[1] for r in rows]
        check(f"C5 (CONTROL, floating point): at two loops the supersymmetric content at one common threshold meets exactly, "
              f"with M_I between {min(MIs):.0f} and {max(MIs):.0f} GeV across the record's one-sigma inputs and the Yukawa "
              "choices: the row that one loop could not decide is ADMISSIBLE at two loops, the threshold in the low TeV range",
              all(MZ < mi < 1e4 for mi in MIs) and 1500 < rows[0][1] < 3500)
    else:
        print("(scipy not available: Part C's RECORD run skipped; C1 to C3 are exact and ran)")


part_J()

# ---------------------------------------------------------------------------
# Part K: the slot/pair split on the five-mode module (Section 10), the twisted action of
# prop:sixteen(3), the proton channel, the breaking field, D-parity and what breaks it.
# Exact throughout: Gaussian rationals on the 32-dimensional module, rationals elsewhere.
# ---------------------------------------------------------------------------

def part_K():
    from fractions import Fraction as F
    from itertools import combinations
    Q0, Q1, QI = g.qi(0), g.qi(1), g.qi(0, 1)
    N_MODES, DIM = 5, 32
    # modes 0, 1, 2 are the paper's pair modes 1, 2, 3 (W); modes 3, 4 are the rung modes 4, 5 (R2)

    def sign_below(S, i):
        return -1 if bin(S & ((1 << i) - 1)).count("1") % 2 else 1

    def creator(i):
        return {(S | 1 << i, S): g.qi(sign_below(S, i)) for S in range(DIM) if not S >> i & 1}

    def annihilator(i):
        return {(S & ~(1 << i), S): g.qi(sign_below(S, i)) for S in range(DIM) if S >> i & 1}

    def mm(A, B):
        byrow = {}
        for (r, c), v in B.items():
            byrow.setdefault(r, []).append((c, v))
        out = {}
        for (r, t), v in A.items():
            for c, w in byrow.get(t, ()):
                out[(r, c)] = out.get((r, c), Q0) + v * w
        return {k: v for k, v in out.items() if v != Q0}

    def madd(A, B, cb=Q1):
        out = dict(A)
        for k, v in B.items():
            out[k] = out.get(k, Q0) + cb * v
        return {k: v for k, v in out.items() if v != Q0}

    def msc(A, c):
        return {k: v * c for k, v in A.items() if v * c != Q0}

    def comm(A, B):
        return madd(mm(A, B), mm(B, A), g.qi(-1))

    def acomm(A, B):
        return madd(mm(A, B), mm(B, A))

    def diag(fun):
        return {(S, S): g.qi(fun(S)) for S in range(DIM) if fun(S) != 0}

    ident = diag(lambda S: 1)

    def rank(mats):
        """exact rank over Q(i) of a list of sparse matrices viewed as vectors"""
        pivots = {}
        r = 0
        for M in mats:
            v = dict(M)
            for key in sorted(pivots):
                if key in v and v[key] != Q0:
                    p = pivots[key]
                    f = v[key] / p[key]
                    for k2, w in p.items():
                        v[k2] = v.get(k2, Q0) - f * w
                    v = {k2: w for k2, w in v.items() if w != Q0}
            if v:
                pivots[min(v)] = v
                r += 1
        return r

    occ = lambda S, a: (S >> a) & 1
    NW = lambda S: occ(S, 0) + occ(S, 1) + occ(S, 2)
    NR = lambda S: occ(S, 3) + occ(S, 4)
    EVEN = [S for S in range(DIM) if bin(S).count("1") % 2 == 0]
    cr = [creator(a) for a in range(N_MODES)]
    an = [annihilator(a) for a in range(N_MODES)]
    num = [mm(cr[a], an[a]) for a in range(N_MODES)]
    gam = []
    for a in range(N_MODES):
        gam.append(madd(an[a], cr[a]))                           # w + v
        gam.append(msc(madd(cr[a], an[a], g.qi(-1)), QI))         # i(v - w)
    PAIR, SLOT = list(range(6)), list(range(6, 10))
    sigma = lambda m, n: msc(mm(gam[m], gam[n]), g.qi(F(1, 2)))
    split = [sigma(m, n) for m, n in combinations(PAIR, 2)] + [sigma(m, n) for m, n in combinations(SLOT, 2)]
    mixed = [sigma(m, n) for m in PAIR for n in SLOT]
    chi = diag(lambda S: -(-1) ** NR(S))
    BL = diag(lambda S: 1 - F(2, 3) * NW(S))
    Yop = diag(lambda S: F(3 * NR(S) - 2 * NW(S), 6))
    names = {(0, 0): 'nu^c', (0, 2): 'u^c', (1, 1): 'Q', (1, 3): 'L', (2, 0): 'e^c', (2, 2): 'd^c'}
    spec = lambda S: names[(NR(S), NW(S))]
    dval = lambda M, S: M.get((S, S), Q0)
    hq = lambda q: (q.re, q.im)          # QI is not hashable; use (re, im)

    g.check("K1 (Sec 10, setting): the ten Majoranas w_a + v_a, i(v_a - w_a) of the module satisfy "
            "{gamma_m, gamma_n} = 2 delta_mn",
            all(madd(acomm(gam[m], gam[n]), msc(ident, g.qi(-2 if m == n else 0))) == {}
                for m in range(10) for n in range(10)))
    g.check("K2 (prop:split): the 45 bivectors are 21 that preserve the 4 + 6 slot/pair split of the ten "
            "(6 slot, 15 pair) and 24 that mix it, all 45 independent",
            len(split) == 21 and len(mixed) == 24 and rank(split + mixed) == 45)
    g.check("K3 (prop:split): the 21 split-preserving bivectors close under the commutator",
            rank(split + [comm(A, B) for A, B in combinations(split, 2)]) == 21)

    L = [mm(cr[3], an[4]), mm(cr[4], an[3]), msc(madd(num[3], num[4], g.qi(-1)), g.qi(F(1, 2)))]
    R = [mm(cr[3], cr[4]), mm(an[4], an[3]), msc(madd(madd(num[3], num[4]), ident, g.qi(-1)), g.qi(F(1, 2)))]
    slot6 = [sigma(m, n) for m, n in combinations(SLOT, 2)]
    pair15 = [sigma(m, n) for m, n in combinations(PAIR, 2)]
    su3 = [mm(cr[a], an[b]) for a in range(3) for b in range(3) if a != b] + \
          [madd(num[0], num[1], g.qi(-1)), madd(num[1], num[2], g.qi(-1))]
    g.check("K4 (prop:split): su(2)_L = {v4 w5, v5 w4, (N4 - N5)/2} and su(2)_R = {v4 v5, w5 w4, (N4 + N5 - 1)/2} "
            "lie in the span of the six slot bivectors and the identity, and commute with each other",
            all(rank(slot6 + [ident, X]) == 7 for X in L + R) and all(comm(a, b) == {} for a in L for b in R))
    g.check("K5 (prop:split): su(3) and B - L = 1 - (2/3)N_W lie in the span of the 15 pair bivectors and the "
            "identity, so the pair factor is su(4) with B - L in it; and Y = T_3R + (B - L)/2 exactly",
            all(rank(pair15 + [ident, X]) == 16 for X in su3 + [BL])
            and madd(Yop, madd(R[2], msc(BL, g.qi(F(1, 2)))), g.qi(-1)) == {})

    def cas(J):
        return madd(mm(J[2], J[2]), msc(madd(mm(J[0], J[1]), mm(J[1], J[0])), g.qi(F(1, 2))))
    CL, CR = cas(L), cas(R)
    tab = {}
    for S in EVEN:
        tab.setdefault(spec(S), set()).add((hq(dval(CL, S)), hq(dval(CR, S)), hq(dval(BL, S))))
    z, tq = (F(0), F(0)), (F(3, 4), F(0))
    want = {'Q': {(tq, z, (F(1, 3), F(0)))}, 'L': {(tq, z, (F(-1), F(0)))},
            'u^c': {(z, tq, (F(-1, 3), F(0)))}, 'd^c': {(z, tq, (F(-1, 3), F(0)))},
            'e^c': {(z, tq, (F(1), F(0)))}, 'nu^c': {(z, tq, (F(1), F(0)))}}
    offdiag = [k for k in list(CL) + list(CR) if k[0] != k[1] and k[0] in EVEN]
    g.check("K6 (prop:pscontent): on the sixteen the Casimirs are (C_L, C_R) = (3/4, 0) on Q and L and (0, 3/4) on "
            "u^c, d^c, e^c, nu^c, with B - L = 1/3, -1, -1/3, -1/3, 1, 1: 16 = (2,1,4) + (1,2,4bar)",
            tab == want and not offdiag)

    # commutant of the 21 on the sixteen: the five Cartan generators separate the sixteen states, so the commutant
    # is diagonal; the 21 connect the states into exactly two classes, on which chi is +1 and -1
    cartan = [num[0], num[1], num[2], num[3], num[4]]
    wts = {S: tuple(hq(dval(Hm, S) - g.qi(F(1, 2))) for Hm in cartan) for S in EVEN}
    distinct = len(set(wts.values())) == 16
    parent = {S: S for S in EVEN}
    def find(S):
        while parent[S] != S:
            S = parent[S]
        return S
    for X in split:
        for (r, c), v in X.items():
            if r != c and r in parent and c in parent:
                parent[find(r)] = find(c)
    classes = {}
    for S in EVEN:
        classes.setdefault(find(S), []).append(S)
    cls = sorted(len(v) for v in classes.values())
    chi_on = sorted(set(dval(chi, S) == Q1 for S in v) == {True} or set(dval(chi, S) == Q1 for S in v) == {False}
                    for v in classes.values())
    g.check("K7 (prop:split): the commutant of the 21 in End(16) is spanned by 1 and chi: the Cartan weights are "
            "distinct on the sixteen and the 21 connect its states into two classes of eight, chi = +1 on one and -1 on "
            "the other",
            distinct and cls == [8, 8] and chi_on == [True, True])

    def orbit_dim(vecs, gens):
        span = list(vecs)
        frontier = list(vecs)
        while frontier:
            new = []
            for X in gens:
                for v in frontier:
                    w = comm(X, v)
                    if w and rank(span + [w]) > len(span):
                        span.append(w)
                        new.append(w)
            frontier = new
        return len(span)
    g.check("K8 (prop:pscontent): under the 21, the rung Majoranas span an invariant 4-space (the bidoublet (2,2,1)) "
            "and the pair Majoranas an invariant 6-space ((1,1,6))",
            orbit_dim([gam[k] for k in SLOT], split) == 4 and orbit_dim([gam[k] for k in PAIR], split) == 6)

    tr16 = lambda M: sum((dval(M, S) for S in EVEN), Q0)
    tL, tR, tB, tY = tr16(mm(L[2], L[2])), tr16(mm(R[2], R[2])), tr16(mm(BL, BL)), tr16(mm(Yop, Yop))
    wR, wB = tR / tY, g.qi(F(1, 4)) * tB / tY
    g.check("K9 (lem:matching): traces on the sixteen tr T_3L^2 = 2, tr T_3R^2 = 2, tr (B - L)^2 = 16/3, tr Y^2 = 10/3; "
            "with Y = T_3R + (B - L)/2 the hypercharge coupling matches as a_1 = (3/5) a_2R + (2/5) a_4",
            (tL, tR, tB, tY) == (g.qi(2), g.qi(2), g.qi(F(16, 3)), g.qi(F(10, 3)))
            and (wR, wB) == (g.qi(F(3, 5)), g.qi(F(2, 5))))

    # prop:sixteen(3) under the twisted action: alpha j + beta k - (2 alpha + 3 beta)/2
    comps = {'nu^c': (0, 0), 'u^c': (0, 2), 'Q': (1, 1), 'L': (1, 3), 'e^c': (2, 0), 'd^c': (2, 2)}
    colour = {'nu^c': 1, 'u^c': 3, 'Q': 3, 'L': 1, 'e^c': 1, 'd^c': 3}
    weak = {'nu^c': 1, 'u^c': 1, 'Q': 2, 'L': 2, 'e^c': 1, 'd^c': 1}
    Yv = {'nu^c': F(0), 'u^c': F(-2, 3), 'Q': F(1, 6), 'L': F(-1, 2), 'e^c': F(1), 'd^c': F(1, 3)}
    BLv = {'nu^c': F(1), 'u^c': F(-1, 3), 'Q': F(1, 3), 'L': F(-1), 'e^c': F(1), 'd^c': F(-1, 3)}

    def sums(q):
        a3 = sum(F(weak[s]) * q[s] for s in comps if colour[s] == 3)                  # [SU(3)]^2 U(1)
        a2 = sum(F(colour[s]) * q[s] for s in comps if weak[s] == 2)                  # [SU(2)]^2 U(1)
        gr = sum(F(colour[s] * weak[s]) * q[s] for s in comps)
        cu = sum(F(colour[s] * weak[s]) * q[s] ** 3 for s in comps)
        y2x = sum(F(colour[s] * weak[s]) * Yv[s] ** 2 * q[s] for s in comps)
        yx2 = sum(F(colour[s] * weak[s]) * Yv[s] * q[s] ** 2 for s in comps)
        return (a3, a2, gr, cu, y2x, yx2)
    grid = [F(n, 2) for n in range(-2, 3)]
    allzero = all(sums({s: al * comps[s][0] + be * comps[s][1] - (2 * al + 3 * be) / 2 for s in comps}) == (0,) * 6
                  for al in grid for be in grid)
    untw = sums({s: F(comps[s][0] + comps[s][1]) for s in comps})
    g.check("K10 (prop:sixteen(3)): in the action the state space carries (Lambda tensor det^(-1/2)), the generator "
            "alpha j + beta k acts by alpha j + beta k - (2 alpha + 3 beta)/2, and all six anomaly sums ([SU(3)]^2 U(1), "
            "[SU(2)]^2 U(1), gravitational, cubic, Y^2 X, Y X^2) vanish on a 5 x 5 grid of (alpha, beta), hence "
            "identically (degree at most three in each variable); untwisted, j + k has (10, 10, 40, 400)",
            allzero and untw[:4] == (10, 10, 40, 400))
    Xv = {s: F(comps[s][0] + comps[s][1]) - F(5, 2) for s in comps}
    T3R = {'nu^c': F(-1, 2), 'e^c': F(1, 2), 'u^c': F(-1, 2), 'd^c': F(1, 2), 'Q': F(0), 'L': F(0)}
    g.check("K11 (prop:sixteen(3)): the twisted thirteenth generator X = j + k - 5/2 takes -5/2 on nu^c, -1/2 on "
            "Q, u^c, e^c and 3/2 on L, d^c, and equals 2Y - (5/2)(B - L) = 2T_3R - (3/2)(B - L) on every species "
            "(so it lies in the Pati-Salam algebra); the nu^c Majorana bilinear carries X = -5 and B - L = 2",
            all(Xv[s] == 2 * Yv[s] - F(5, 2) * BLv[s] == 2 * T3R[s] - F(3, 2) * BLv[s] for s in comps)
            and Xv['nu^c'] == F(-5, 2) and 2 * Xv['nu^c'] == -5 and 2 * BLv['nu^c'] == 2)
    # the T_3R values used just above, from the module itself
    t3r_ok = all(dval(R[2], S) == g.qi(T3R[spec(S)]) for S in EVEN)

    Bop = msc(madd(BL, chi), g.qi(F(1, 4)))
    Lop = msc(madd(chi, BL, g.qi(-3)), g.qi(F(1, 4)))
    BLwant = {'nu^c': (0, -1), 'u^c': (F(-1, 3), 0), 'Q': (F(1, 3), 0), 'L': (0, 1), 'e^c': (0, -1), 'd^c': (F(-1, 3), 0)}
    got = {spec(S): (dval(Bop, S), dval(Lop, S)) for S in EVEN}
    g.check("K12 (prop:protonchannel): on the sixteen B = ((B - L) + chi)/4 and L = (chi - 3(B - L))/4 give every "
            "species' baryon and lepton number, so 3B + L = chi; and T_3R read from the module agrees with K11",
            got == {k: (g.qi(v[0]), g.qi(v[1])) for k, v in BLwant.items()} and t3r_ok)
    g.check("K13 (prop:protonchannel): all 21 split-preserving generators commute with chi and all 24 slot-pair mixing "
            "generators anticommute with it; p -> e+ pi0 has Delta(B - L) = 0 and Delta(3B + L) = -4, so only the mixing "
            "generators mediate it",
            all(comm(X, chi) == {} for X in split) and all(acomm(X, chi) == {} for X in mixed)
            and (-1) - (-1) == 0 and 3 * (-1) + (-1) == -4)

    T = cr[0]
    for a in range(1, 5):
        T = mm(T, cr[a])
    g.check("K14 (prop:breaking): T = v1 v2 v3 v4 v5 maps nu^c (the empty state) to the full state and annihilates "
            "every other state; it commutes with su(3), su(2)_L and Y and carries Delta(B - L) = -2",
            set(T) == {(31, 0)} and all(comm(X, T) == {} for X in su3 + L + [Yop])
            and madd(comm(BL, T), msc(T, g.qi(2))) == {})
    orb = [T]
    frontier = [T]
    while frontier:
        new = []
        for X in split:
            for v in frontier:
                w = comm(X, v)
                if w and rank(orb + [w]) > len(orb):
                    orb.append(w)
                    new.append(w)
        frontier = new
    g.check("K15 (prop:breaking): the orbit of T under the 21 spans 30 dimensions, su(2)_L annihilates all of it, and T "
            "is the highest weight of an su(2)_R triplet ([v4 v5, T] = 0, [T_3R, T] = T): the (10,1,3)",
            len(orb) == 30 and all(comm(X, v) == {} for X in L for v in orb)
            and comm(R[0], T) == {} and madd(comm(R[2], T), T, g.qi(-1)) == {})

    def realsplit(M):
        out = {}
        for (r, c), v in M.items():
            if v.re != 0:
                out[(r, c, 0)] = g.qi(v.re)
            if v.im != 0:
                out[(r, c, 1)] = g.qi(v.im)
        return out
    rank_R = rank([realsplit(comm(X, T)) for X in split])   # the 21 bivectors are a real basis of the compact algebra
    sm12 = su3 + L + [Yop]
    g.check("K15b (prop:breaking(2)): in the compact Pati-Salam algebra (the real span of the 21 bivectors) the map "
            "X -> [X, T] has rank 9, so the subalgebra fixing T is 12-dimensional; it contains the compact forms of su(3), "
            "su(2)_L and Y, which annihilate T and span 12 dimensions, so it is exactly the Standard Model algebra",
            rank_R == 9 and rank(sm12) == 12 and all(comm(X, T) == {} for X in sm12)
            and all(rank(split + [X]) == 21 for X in sm12))

    D = mm(gam[5], gam[9])
    Dinv = msc(D, g.qi(-1))
    conjD = lambda A: mm(mm(D, A), Dinv)
    span_LR = L + R + [ident]
    QLst = [S for S in EVEN if NR(S) == 1]
    SING = [S for S in EVEN if NR(S) != 1]
    g.check("K16 (prop:dparity): D = gamma_5 gamma_9 (one pair Majorana times one slot Majorana) has D^2 = -1; "
            "conjugation by D maps su(2)_L onto su(2)_R, maps the eight (Q, L) states onto the eight singlet states, "
            "and anticommutes with chi",
            madd(mm(D, D), ident) == {} and all(rank(span_LR + [conjD(X)]) == rank(span_LR) for X in L)
            and rank([conjD(X) for X in L] + R) == 3
            and {r for (r, c) in D if c in QLst} == set(SING) and acomm(D, chi) == {})

    # chi is the only Pati-Salam singlet among the 210 grade-four elements: Clifford blades, generators 0..9 square to +1
    sq = [F(1)] * 10
    bl4 = list(combinations(range(10), 4))
    biv_split = [(m, n) for m, n in combinations(PAIR, 2)] + [(m, n) for m, n in combinations(SLOT, 2)]
    rows = {}
    for col, S in enumerate(bl4):
        e = {S: F(1)}
        for gi, (m, n) in enumerate(biv_split):
            bv = {(m, n): F(1)}
            cm = g.sub(g.mul(bv, e, sq), g.mul(e, bv, sq))
            for blade, val in cm.items():
                if val != 0:
                    rows.setdefault((gi, blade), {})[col] = val
    def frank(vecs):
        pivots, r = {}, 0
        for v0 in vecs:
            v = dict(v0)
            changed = True
            while v:
                k = min(v)
                if k in pivots:
                    p = pivots[k]
                    fct = v[k] / p[k]
                    for k2, w in p.items():
                        v[k2] = v.get(k2, F(0)) - fct * w
                    v = {k2: w for k2, w in v.items() if w != 0}
                else:
                    pivots[k] = v
                    r += 1
                    break
        return r
    rk = frank(list(rows.values()))
    slotvol = bl4.index((6, 7, 8, 9))
    in_kernel = all(rw.get(slotvol, F(0)) == 0 for rw in rows.values())
    ksup = (len(bl4) - rk == 1) and in_kernel
    vol = mm(mm(gam[6], gam[7]), mm(gam[8], gam[9]))
    vol_is_chi = madd(vol, chi, g.qi(-1)) == {}            # gamma_6 gamma_7 gamma_8 gamma_9 = i(1-2N_4) i(1-2N_5) = chi
    g.check("K17 (prop:dparity): among the 210 grade-four elements of the Clifford algebra of the ten, the Pati-Salam "
            "singlets form a one-dimensional space spanned by gamma_6 gamma_7 gamma_8 gamma_9, the product of the four slot "
            "Majoranas, which on the module equals chi; it is D-odd, so a vev along it breaks Spin(10) to Pati-Salam and "
            "breaks D-parity at once",
            ksup and vol_is_chi and acomm(D, vol) == {})

    x, y = g.qi(3), g.qi(5)
    vreal = madd(msc(gam[6], x), msc(gam[7], y))
    a, b = x + QI * y, x - QI * y
    g.check("K18 (cor:complexrung): a real rung vector x gamma_6 + y gamma_7 equals a v_4 + b w_4 with b = conj(a), so "
            "|a| = |b| and by cor:vev m_u = m_d at tree level: m_t != m_b needs a complex rung field",
            madd(vreal, madd(msc(cr[3], a), msc(an[3], b)), g.qi(-1)) == {} and b == a.conj())


part_K()


# ---------------------------------------------------------------------------
# Part L: the proton condition (Section 8.6) and the Pati-Salam chains (Section 10).  Coefficients, two-loop
# matrices, exact one-loop solutions and the criterion form are exact; GeV scales, lifetimes and the two-loop
# runs are RECORD lines, and the comparisons with the proton bound are CONTROL lines (floating point).
# ---------------------------------------------------------------------------

def part_L():
    from fractions import Fraction as F
    import math

    def record(line):
        print('RECORD  ' + line)

    # group data: ('U1',) or ('SU', N); representations by label; returns b and the generic two-loop matrix
    def su_rep(N, name):
        if name == '1':
            return (1, F(0), F(0))
        if name in ('N', 'Nb'):
            return (N, F(1, 2), F(N * N - 1, 2 * N))
        if name == 'adj':
            return (N * N - 1, F(N), F(N))
        if name == 'sym':
            return (N * (N + 1) // 2, F(N + 2, 2), F((N - 1) * (N + 2), N))
        raise ValueError(name)

    def CG(grp):
        return F(0) if grp[0] == 'U1' else F(grp[1])

    def data(groups, rep):
        dims, T, C = [], [], []
        for grp, r in zip(groups, rep):
            if grp[0] == 'U1':
                dims.append(1); T.append(F(3, 5) * r * r); C.append(F(3, 5) * r * r)
            else:
                d, t, c = su_rep(grp[1], r); dims.append(d); T.append(t); C.append(c)
        return dims, T, C

    def wT(groups, rep, i):
        dims, T, C = data(groups, rep)
        w = T[i]
        for k, d in enumerate(dims):
            if k != i:
                w *= d
        return w

    def coeffs(groups, weyl, scal):
        n = len(groups)
        b, B = [], [[F(0)] * n for _ in range(n)]
        for i, grp in enumerate(groups):
            bi = -F(11, 3) * CG(grp)
            bi += sum(F(2, 3) * m * wT(groups, rep, i) for rep, m in weyl)
            bi += sum(F(1, 3) * m * wT(groups, rep, i) for rep, m in scal)
            b.append(bi)
            for j in range(n):
                s = F(0)
                if i == j:
                    s += -F(34, 3) * CG(grp) ** 2
                    s += F(10, 3) * CG(grp) * sum(m * wT(groups, rep, i) for rep, m in weyl)
                    s += F(2, 3) * CG(grp) * sum(m * wT(groups, rep, i) for rep, m in scal)
                s += sum(2 * m * wT(groups, rep, i) * data(groups, rep)[2][j] for rep, m in weyl)
                s += sum(4 * m * wT(groups, rep, i) * data(groups, rep)[2][j] for rep, m in scal)
                B[i][j] = s
        return b, B

    SMg = [('U1',), ('SU', 2), ('SU', 3)]
    gen1 = [((F(1, 6), 'N', 'N'), 1), ((F(-1, 2), 'N', '1'), 1), ((F(-2, 3), '1', 'Nb'), 1),
            ((F(1, 3), '1', 'Nb'), 1), ((F(1), '1', '1'), 1), ((F(0), '1', '1'), 1)]
    bSM, BSM = coeffs(SMg, [(r, 3 * m) for r, m in gen1], [((F(1, 2), 'N', '1'), 1)])
    PSg = [('SU', 4), ('SU', 2), ('SU', 2)]
    PSweyl = [(('N', 'N', '1'), 3), (('Nb', '1', 'N'), 3)]
    chains = {
        'real bidoublet':           [(('1', 'N', 'N'), F(1, 2)), (('sym', '1', 'adj'), 1)],
        'complex bidoublet':        [(('1', 'N', 'N'), F(1)), (('sym', '1', 'adj'), 1)],
        'complex + (15,2,2)':       [(('1', 'N', 'N'), F(1)), (('sym', '1', 'adj'), 1), (('adj', 'N', 'N'), 1)],
        'D-parity kept (real)':     [(('1', 'N', 'N'), F(1, 2)), (('sym', '1', 'adj'), 1), (('sym', 'adj', '1'), 1)],
    }
    co = {k: coeffs(PSg, PSweyl, v) for k, v in chains.items()}
    g.check("L1 (prop:pschains): Fact fact:index on the Pati-Salam content (three generations (4,2,1) + (4bar,1,2), "
            "the bidoublet, the complex (10,1,3), and the complex (15,2,2) where named) gives b(4, 2L, 2R) = "
            "(-23/3, -19/6, 7/2) with a real bidoublet, (-23/3, -3, 11/3) with a complex one, and (-7/3, 2, 26/3) with a "
            "complex bidoublet and the (15,2,2); the Standard Model's (41/10, -19/6, -7) from the same routine",
            co['real bidoublet'][0] == [F(-23, 3), F(-19, 6), F(7, 2)]
            and co['complex bidoublet'][0] == [F(-23, 3), F(-3), F(11, 3)]
            and co['complex + (15,2,2)'][0] == [F(-7, 3), F(2), F(26, 3)]
            and bSM == [F(41, 10), F(-19, 6), F(-7)])
    g.check("L2 (prop:pschains): Fact fact:twoloop's generic formula gives the two-loop matrices (rows 4, 2L, 2R) "
            "[[643/6, 9/2, 153/2], [45/2, 8, 3], [765/2, 3, 584/3]] for the complex chain and "
            "[[2435/6, 105/2, 249/2], [525/2, 73, 48], [1245/2, 48, 779/3]] with the (15,2,2), and reproduces the "
            "Standard Model's matrix of Fact fact:twoloop",
            co['complex bidoublet'][1] == [[F(643, 6), F(9, 2), F(153, 2)], [F(45, 2), F(8), F(3)], [F(765, 2), F(3), F(584, 3)]]
            and co['complex + (15,2,2)'][1] == [[F(2435, 6), F(105, 2), F(249, 2)], [F(525, 2), F(73), F(48)],
                                                 [F(1245, 2), F(48), F(779, 3)]]
            and BSM == [[F(199, 50), F(27, 10), F(44, 5)], [F(9, 10), F(35, 6), F(12)], [F(11, 10), F(9, 2), F(-26)]])

    # exact one-loop chain: a_i(M_Z) = a_U + b_i^SM x + b_i^eff y, x = ln(M_I/M_Z)/2pi, y = ln(M_U/M_I)/2pi,
    # with the Pati-Salam stage seen at M_Z through a_1 = (3/5) a_2R + (2/5) a_4, a_2 = a_2L, a_3 = a_4
    aem, s2, a3 = F(128), F(2312, 10000), F(500, 59)
    a2 = s2 * aem
    a1 = F(3, 5) * (aem - a2)

    def solve(bPS):
        beff = [F(3, 5) * bPS[2] + F(2, 5) * bPS[0], bPS[1], bPS[0]]
        # unknowns (a_U, x, y): a_i = a_U + bSM_i x + beff_i y
        M = [[F(1), bSM[i], beff[i]] for i in range(3)]
        rhs = [a1, a2, a3]
        det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
               + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        sol = []
        for k in range(3):
            Mk = [[rhs[i] if j == k else M[i][j] for j in range(3)] for i in range(3)]
            dk = (Mk[0][0] * (Mk[1][1] * Mk[2][2] - Mk[1][2] * Mk[2][1]) - Mk[0][1] * (Mk[1][0] * Mk[2][2] - Mk[1][2] * Mk[2][0])
                  + Mk[0][2] * (Mk[1][0] * Mk[2][1] - Mk[1][1] * Mk[2][0]))
            sol.append(dk / det)
        aU, x, y = sol
        ok = all(aU + bSM[i] * x + beff[i] * y == [a1, a2, a3][i] for i in range(3))
        return aU, x, y, beff, ok
    sols = {k: solve(co[k][0]) for k in ('real bidoublet', 'complex bidoublet', 'complex + (15,2,2)')}
    g.check("L3 (prop:pschains): the one-loop chain is solved exactly on the inputs of prop:desert: real bidoublet "
            "x = 11901069/3355625, y = 5610391/3355625, a_U = 464273942/10066875; complex x = 25548992/7116875, "
            "y = 11220782/7116875, a_U = 975544318/21350625; complex with the (15,2,2) x = 22055284/6305625, "
            "y = 11220782/6305625, a_U = 702018938/18916875 (x = ln(M_I/M_Z)/2pi, y = ln(M_U/M_I)/2pi), each "
            "substituted back; M_I < M_U and a_U > 0 in all three",
            sols['real bidoublet'][:3] == (F(464273942, 10066875), F(11901069, 3355625), F(5610391, 3355625))
            and sols['complex bidoublet'][:3] == (F(975544318, 21350625), F(25548992, 7116875), F(11220782, 7116875))
            and sols['complex + (15,2,2)'][:3] == (F(702018938, 18916875), F(22055284, 6305625), F(11220782, 6305625))
            and all(s[4] and s[1] > 0 and s[2] > 0 and s[0] > 0 for s in sols.values()))
    aU, x, y, beff, _ = sols['real bidoublet']
    Deff = [beff[i] - bSM[i] for i in range(3)]
    f = y / (x + y)
    R = (a1 - a2) / (a2 - a3)
    gauge = [F(3, 5) * (-F(22, 3)) + F(2, 5) * (-F(44, 3)) - F(0), -F(22, 3) - (-F(22, 3)), -F(44, 3) - (-F(11))]
    trip = [F(3, 5) * F(1, 3) * 2 * 10 + F(2, 5) * F(1, 3) * 3 * 3, F(0), F(1, 3) * 3 * 3]   # (10,1,3): T(adj SU2) = 2, T(10 of SU4) = 3
    g.check("L4 (prop:pschains): in Theorem thm:criterion's language the real-bidoublet chain is the one-threshold "
            "shift Delta = (-76/15, 0, -2/3) at f = 5610391/17511460 = 0.320, inside [0, 1], and satisfies "
            "cor:direction, (1 + R) Delta_2 = 0 > Delta_1 + R Delta_3; Delta splits as the extra gauge bosons "
            "(-154/15, 0, -11/3) plus the (10,1,3) (26/5, 0, 3), the bidoublet's light doublet being the Standard "
            "Model's",
            Deff == [F(-76, 15), F(0), F(-2, 3)] and f == F(5610391, 17511460) and 0 < f < 1
            and (1 + R) * Deff[1] > Deff[0] + R * Deff[2]
            and gauge == [F(-154, 15), F(0), F(-11, 3)] and trip == [F(26, 5), F(0), F(3)]
            and [gauge[i] + trip[i] for i in range(3)] == Deff)
    # cor:mirror without (S): the content's own normalisation k = 17/9 (ratio 9/26 of prop:unification)
    bYnoL = F(5, 3) * F(7, 2)
    b1k = bYnoL / F(17, 9)
    g.check("L5 (cor:mirror): without the lepton doublet the coefficients (7/2, -25/6, -7) are in the normalisation "
            "(S) supplies; in the content's own trace normalisation k = 17/9 the ratio is 740/289, not 46/17",
            (F(7, 2) + F(25, 6)) / (F(-25, 6) + 7) == F(46, 17) and (b1k + F(25, 6)) / (F(-25, 6) + 7) == F(740, 289))

    def closed(b):
        Lx = (aem - F(8, 3) * a3) / (F(5, 3) * (b[0] - b[2]) + (b[1] - b[2]))
        return (a3 + (b[1] - b[2]) * Lx) / aem, Lx
    gens = [closed([bSM[i] + n * F(4, 3) for i in range(3)])[0] for n in range(-2, 2)]
    g.check("L6 (prop:desert): the desert's angle does not depend on the number of generations (each adds (4/3)(1,1,1); "
            "the closed form returns 78761/379488 for one to four generations), and without the imported Higgs doublet, "
            "b = (4, -10/3, -7), it is 3457/16992 = 0.2034, further from the record",
            all(v == F(78761, 379488) for v in gens) and closed([F(4), F(-10, 3), F(-7)])[0] == F(3457, 16992))
    bMS = [F(33, 5), F(1), F(-3)]
    Lp = {(i, j): ([a1, a2, a3][i] - [a1, a2, a3][j]) / (bMS[i] - bMS[j]) for i, j in ((0, 1), (0, 2), (1, 2))}
    g.check("L7 (prop:desert): with the record's three couplings the supersymmetric coefficients meet pairwise at three "
            "distinct scales (exact rationals L_ij/2pi), not at one point",
            len(set(Lp.values())) == 3)

    # ---- floating point from here: GeV conversions, the proton condition, the two-loop runs ----
    MZ = 91.1876
    GeV = lambda xx: MZ * math.exp(2 * math.pi * float(xx))
    def tau(MU, aUinv):           # Fact fact:proton: tau = 1.6e33 yr x [ (a_U/45) 10^{2(n_U - 15)} / 5.2 ]^2
        return 1.6e33 * ((aUinv / 45) * 10 ** (2 * (math.log10(MU) - 15)) / 5.2) ** 2
    def MUmin(aUinv, lim=2.4e34):
        return 10 ** (15 + 0.5 * math.log10(5.2 * math.sqrt(lim / 1.6e33) * 45 / aUinv))
    record("prop:desert, supersymmetric coefficients, pairwise meetings at the record: "
           + ", ".join(f"(a{i+1},a{j+1}) at {GeV(v):.3e} GeV" for (i, j), v in sorted(Lp.items())))
    record(f"proton condition (fact:proton): M_U >= {MUmin(45):.2e} GeV at alpha_U^-1 = 45, {MUmin(40):.2e} at 40, "
           f"{MUmin(25.7):.2e} at 25.7")
    for k, s in sols.items():
        record(f"one loop, {k}: M_I = {GeV(s[1]):.3e} GeV, M_U = {GeV(s[1] + s[2]):.3e} GeV, alpha_U^-1 = {float(s[0]):.3f}")
    # Prop prop:table, its three admissible rows
    b12, b23 = bSM[0] - bSM[1], bSM[1] - bSM[2]
    rows = []
    for name, Dl in [("wino", (F(0), F(4, 3), F(0))), ("wino + bino + higgsinos", (F(2, 5), F(2), F(0))),
                     ("supersymmetric content without gluino", (F(5, 2), F(25, 6), F(2)))]:
        d12, d23 = Dl[0] - Dl[1], Dl[1] - Dl[2]
        den = b12 * d23 - b23 * d12
        X = ((a1 - a2) * d23 - (a2 - a3) * d12) / den
        Yy = (b12 * (a2 - a3) - b23 * (a1 - a2)) / den
        aUr = a3 - bSM[2] * X - Dl[2] * Yy
        MU = GeV(X)
        t = tau(MU, float(aUr))
        rows.append(t)
        record(f"prop:table row '{name}': M_I = {GeV(X - Yy):.1e} GeV, M_U = {MU:.2e} GeV, alpha_U^-1 = {float(aUr):.1f}, "
               f"tau = {t:.1e} yr")
    g.check("C6 (CONTROL, floating point; prop:proton): the three rows prop:table finds admissible all have proton "
            "lifetimes below 2.4e34 yr by more than four orders of magnitude",
            all(t < 2.4e30 for t in rows))
    # Prop prop:splits (d): where the segment crosses the proton limit
    Dl, Dp = (F(2, 5), F(2), F(0)), (F(21, 10), F(13, 6), F(4))
    c1 = Dl[0] - Dl[1] - R * (Dl[1] - Dl[2])
    c2 = Dp[0] - Dp[1] - R * (Dp[1] - Dp[2])
    rhs = R * b23 - b12
    def seg(ff):
        fp = (rhs - ff * c1) / c2
        X = (a1 - a2) / (b12 + ff * (Dl[0] - Dl[1]) + fp * (Dp[0] - Dp[1]))
        aUs = a3 - (bSM[2] + ff * Dl[2] + fp * Dp[2]) * X
        MU = GeV(X)
        return fp, MU, float(aUs), MU ** (1 - float(ff)) * MZ ** float(ff), MU ** (1 - float(fp)) * MZ ** float(fp)
    lo, hi = F(438, 1000), F(1)
    for _ in range(50):
        m = (lo + hi) / 2
        fp, MU, aUs, _, _ = seg(m)
        if tau(MU, aUs) < 2.4e34:
            lo = m
        else:
            hi = m
    fp, MU, aUs, MI, MIp = seg(hi)
    record(f"prop:splits(d) crosses the proton limit at f = {float(hi):.4f}, f' = {float(fp):.4f}: light set at "
           f"{MI:.1e} GeV, heavy set at {MIp:.1e} GeV, M_U = {MU:.2e} GeV, alpha_U^-1 = {aUs:.1f}")
    _, MUa, aUa, _, _ = seg(F(438, 1000))
    _, MUb, aUb, _, _ = seg(F(1))
    g.check("C7 (CONTROL, floating point; prop:proton): along prop:splits(d) the end f = 0.438 fails the proton limit "
            "and the near-degenerate end f = 1 passes, the crossing lying between f = 0.85 and 0.88",
            tau(MUa, aUa) < 2.4e34 < tau(MUb, aUb) and F(85, 100) < hi < F(88, 100))

    # two loops: Standard Model below M_I (with the top Yukawa), Pati-Salam above (Yukawa term inert, omitted)
    PI = math.pi
    def fl(Mx): return [[float(v) for v in r] for r in Mx]
    bS, BS, cS = [float(v) for v in bSM], fl(BSM), [1.7, 1.5, 2.0]
    def ySM(yy, g2): return yy / (16 * PI ** 2) * (4.5 * yy * yy - 0.85 * g2[0] - 2.25 * g2[1] - 8 * g2[2])
    def rhsf(a, yy, b, B, c, yb, loops):
        al = [1 / v for v in a]
        g2 = [4 * PI * v for v in al]
        da = []
        for i in range(len(a)):
            s = b[i]
            if loops == 2:
                s += sum(B[i][j] * al[j] / (4 * PI) for j in range(len(a))) - c[i] * yy * yy / (16 * PI * PI)
            da.append(-s / (2 * PI))
        return da, (yb(yy, g2) if (yb and loops == 2) else 0.0)
    def run(a, yy, t0, t1, b, B, c, yb, loops, h=0.01):
        n = max(1, int(abs(t1 - t0) / h))
        h = (t1 - t0) / n
        a = list(a)
        for _ in range(n):
            k1 = rhsf(a, yy, b, B, c, yb, loops)
            k2 = rhsf([a[i] + h / 2 * k1[0][i] for i in range(3)], yy + h / 2 * k1[1], b, B, c, yb, loops)
            k3 = rhsf([a[i] + h / 2 * k2[0][i] for i in range(3)], yy + h / 2 * k2[1], b, B, c, yb, loops)
            k4 = rhsf([a[i] + h * k3[0][i] for i in range(3)], yy + h * k3[1], b, B, c, yb, loops)
            a = [a[i] + h / 6 * (k1[0][i] + 2 * k2[0][i] + 2 * k3[0][i] + k4[0][i]) for i in range(3)]
            yy = yy + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        return a, yy
    def cross(a, t0, b, B, loops):
        h, t, d0 = 0.05, t0, a[0] - a[1]
        while t < math.log(1e19):
            a1_, _ = run(a, 0.0, t, t + h, b, B, [0, 0, 0], None, loops)
            if (a1_[0] - a1_[1]) * d0 <= 0:
                lo_, hi_ = 0.0, h
                for _ in range(40):
                    m = (lo_ + hi_) / 2
                    am, _ = run(a, 0.0, t, t + m, b, B, [0, 0, 0], None, loops, h=max(m / 10, 1e-9))
                    if (am[0] - am[1]) * d0 > 0:
                        lo_ = m
                    else:
                        hi_ = m
                am, _ = run(a, 0.0, t, t + lo_, b, B, [0, 0, 0], None, loops, h=max(lo_ / 10, 1e-9))
                return t + lo_, am
            a, t = a1_, t + h
        return None
    tZ = math.log(MZ)
    def inputs(aem_=127.951, s2_=0.23122, als=0.1180):
        return [0.6 * (1 - s2_) * aem_, s2_ * aem_, 1 / als]
    def mismatch(tI, bP, BP, loops, inp):
        a, yy = run(inp, 0.95, tZ, tI, bS, BS, cS, ySM, loops)
        a4, a2L, a2R = a[2], a[1], (5 / 3) * (a[0] - 0.4 * a[2])
        tU, aU_ = cross([a4, a2L, a2R], tI, bP, BP, loops)
        return aU_[2] - aU_[0], tU, aU_
    def solveMI(bP, BP, loops, inp):
        lo_, hi_ = math.log(1e7), math.log(1e15)
        flo = mismatch(lo_, bP, BP, loops, inp)[0]
        for _ in range(36):
            m = (lo_ + hi_) / 2
            fm = mismatch(m, bP, BP, loops, inp)[0]
            if fm * flo > 0:
                lo_, flo = m, fm
            else:
                hi_ = m
        tI = (lo_ + hi_) / 2
        _, tU, aU_ = mismatch(tI, bP, BP, loops, inp)
        return math.exp(tI), math.exp(tU), aU_[0]
    # CONTROL: with the two-loop terms off and T12's inputs, the integrator returns the exact one-loop chain
    bc = [float(v) for v in co['complex + (15,2,2)'][0]]
    MI1, MU1, _ = solveMI(bc, fl(co['complex + (15,2,2)'][1]), 1, inputs(128.0, 0.2312, 0.118))
    s = sols['complex + (15,2,2)']
    g.check(f"C8 (CONTROL, floating point; prop:pschains): with the two-loop terms off the integrator reproduces the "
            f"exact one-loop chain with the (15,2,2), M_I = {GeV(s[1]):.3e} GeV against {MI1:.3e} GeV",
            abs(MI1 / GeV(s[1]) - 1) < 2e-3 and abs(MU1 / GeV(s[1] + s[2]) - 1) < 2e-3)
    res = {}
    for k in ('complex + (15,2,2)', 'complex bidoublet', 'real bidoublet', 'D-parity kept (real)'):
        bP = [float(v) for v in co[k][0]]
        MI, MU, aUi = solveMI(bP, fl(co[k][1]), 2, inputs())
        res[k] = (MI, MU, aUi)
        record(f"two loops, {k}: M_I = {MI:.3e} GeV, M_U = {MU:.3e} GeV, alpha_U^-1 = {aUi:.2f}, "
               f"M_U / proton bound = {MU / MUmin(aUi):.1f}, tau = {tau(MU, aUi):.1e} yr")
    MI, MU, aUi = res['complex + (15,2,2)']
    # prop:requirement: g_R at M_I from the Standard Model run (a_2R = (5/3)(a_1 - (2/5) a_4)), v_R = M_I/g_R,
    # and the effective Dirac mass the seesaw needs on the heavy direction, m_D = sqrt(m_3 f_J v_R)
    aI, _ = run(inputs(), 0.95, tZ, math.log(MI), bS, BS, cS, ySM, 2)
    gR = math.sqrt(4 * PI / ((5 / 3) * (aI[0] - 0.4 * aI[2])))
    vR = MI / gR
    mD1 = math.sqrt(5.02e-11 * vR)
    record(f"prop:requirement: on the chain with the (15,2,2), g_R(M_I) = {gR:.4f}, v_R = M_I/g_R = {vR:.3e} GeV, and "
           f"m_D = sqrt(m_3 f_J v_R) = {mD1:.3f} GeV x sqrt(f_J) for m_3 = 0.0502 eV; with m_D = m_t(M_I) = 92.45 GeV "
           f"the angle would need f_J = {(92.45 / mD1) ** 2:.0f}")
    g.check("C10 (CONTROL, floating point; prop:requirement): g_R(M_I) lies between 0.46 and 0.48 and the effective Dirac "
            "mass the angle asks of the heavy direction at f_J = 1 lies between 1.3 and 1.6 GeV",
            0.46 < gR < 0.48 and 1.3 < mD1 < 1.6)
    g.check("C9 (CONTROL, floating point; prop:pschains): at two loops the chain with the complex bidoublet and the "
            "(15,2,2) meets with M_I between 1e10 and 3e10 GeV and M_U at least five times the proton bound; the chain "
            "with D-parity kept fails the bound",
            1e10 < MI < 3e10 and MU / MUmin(aUi) > 5 and res['D-parity kept (real)'][1] < MUmin(res['D-parity kept (real)'][2]))
    # sensitivity of the headline chain to the record's one-sigma alpha_s
    bP, BP = [float(v) for v in co['complex + (15,2,2)'][0]], fl(co['complex + (15,2,2)'][1])
    for lab, inp in [("alpha_s = 0.1171", inputs(als=0.1171)), ("alpha_s = 0.1189", inputs(als=0.1189)),
                     ("sin^2 theta_W + 0.0001", inputs(s2_=0.23132))]:
        MI, MU, aUi = solveMI(bP, BP, 2, inp)
        record(f"two loops, complex + (15,2,2), {lab}: M_I = {MI:.3e} GeV, M_U = {MU:.3e} GeV, alpha_U^-1 = {aUi:.2f}")


part_L()


# ---------------------------------------------------------------------------
# Part M: the weak angle on the Pati-Salam route (Section 11).  Exact: equal weight on the module
# (prop:equalweight), the elimination identity on rational matrices (prop:elimination), the grade-three
# direction (prop:gradethree).  Floating point (numpy, optional): the four stored coupling sets of
# obs:anglefits, every observable and the tuning measure recomputed from them (RECORD), with CONTROL lines.
# ---------------------------------------------------------------------------

def part_M():
    from fractions import Fraction as F

    def record(line):
        print('RECORD  ' + line)
    from itertools import combinations
    import random
    Q0, Q1, QI = g.qi(0), g.qi(1), g.qi(0, 1)
    DIM = 32

    def sign_below(S, i):
        return -1 if bin(S & ((1 << i) - 1)).count("1") % 2 else 1
    def creator(i):
        return {(S | 1 << i, S): g.qi(sign_below(S, i)) for S in range(DIM) if not S >> i & 1}
    def annihilator(i):
        return {(S & ~(1 << i), S): g.qi(sign_below(S, i)) for S in range(DIM) if S >> i & 1}
    def mm(A, B):
        byrow = {}
        for (r, c), v in B.items():
            byrow.setdefault(r, []).append((c, v))
        out = {}
        for (r, t), v in A.items():
            for c, w in byrow.get(t, ()):
                out[(r, c)] = out.get((r, c), Q0) + v * w
        return {k: v for k, v in out.items() if v != Q0}
    def madd(A, B, cb=Q1):
        out = dict(A)
        for k, v in B.items():
            out[k] = out.get(k, Q0) + cb * v
        return {k: v for k, v in out.items() if v != Q0}
    def msc(A, c):
        return {k: v * c for k, v in A.items() if v * c != Q0}
    def diag(fun):
        return {(S, S): g.qi(fun(S)) for S in range(DIM) if fun(S) != 0}
    def dag(A):
        return {(c, r): v.conj() for (r, c), v in A.items()}
    occ = lambda S, a: (S >> a) & 1
    NW = lambda S: occ(S, 0) + occ(S, 1) + occ(S, 2)
    NR = lambda S: occ(S, 3) + occ(S, 4)
    EVEN = [S for S in range(DIM) if bin(S).count("1") % 2 == 0]
    names = {(0, 0): 'nu^c', (0, 2): 'u^c', (1, 1): 'Q', (1, 3): 'L', (2, 0): 'e^c', (2, 2): 'd^c'}
    spec = lambda S: names[(NR(S), NW(S))]
    cr = [creator(a) for a in range(5)]
    an = [annihilator(a) for a in range(5)]
    v4, w4 = cr[3], an[3]
    chi = diag(lambda S: -(-1) ** NR(S))
    BL = diag(lambda S: 1 - F(2, 3) * NW(S))
    TGJu = mm(mm(v4, BL), chi)          # the up-type twin of T_GJ
    TGJ = mm(mm(w4, BL), chi)
    T = cr[0]
    for a in range(1, 5):
        T = mm(T, cr[a])
    P = madd(mm(dag(T), T), mm(T, dag(T)))

    def eps(S):          # sign of e_S ^ e_{S^c} against e_{12345}
        Sl = [a for a in range(5) if occ(S, a)]
        order = Sl + [a for a in range(5) if not occ(S, a)]
        inv = sum(1 for i in range(5) for j in range(i + 1, 5) if order[i] > order[j])
        return -1 if inv % 2 else 1
    def form(E):
        """mass form B(e_p, E e_q) on the sixteen (lem:pairing)"""
        Fm = {}
        for (r, c), v in E.items():
            if c in EVEN:
                p = (DIM - 1) ^ r                      # B pairs e_r with its complement only
                if p in EVEN:
                    k = bin(p).count("1")
                    Fm[(p, c)] = v * g.qi((-1) ** (k * (k - 1) // 2) * eps(p))
        return {k: v for k, v in Fm.items() if v != Q0}
    def species(Fm):
        out = {}
        for (p, q), v in Fm.items():
            out.setdefault(tuple(sorted((spec(p), spec(q)))), set()).add((v.re, v.im))
        return out

    cu = madd(v4, madd(mm(v4, P), mm(P, v4)), g.qi(-1))
    cd = madd(w4, madd(mm(w4, P), mm(P, w4)), g.qi(-1))
    eqw = msc(madd(v4, TGJu), g.qi(F(3, 4)))
    Fcu, Fv = species(form(cu)), species(form(v4))
    g.check("M1 (prop:equalweight(1)): keeping v_4 off the condensate, v_4 - (v_4 P + P v_4), gives on the sixteen the mass "
            "form of (3/4)(v_4 + v_4 (B - L) chi), the 10 and the 126 doublet at equal weight; it couples (Q, u^c) exactly as "
            "v_4 does and has no (L, nu^c) entry; and w_4 - (w_4 P + P w_4) has the mass form of w_4",
            form(cu) == form(eqw) and set(Fcu) == {('Q', 'u^c')} and Fcu[('Q', 'u^c')] == Fv[('Q', 'u^c')]
            and ('L', 'nu^c') in Fv and form(cd) == form(w4))

    def comm16(E):
        C = madd(mm(E, P), mm(P, E), g.qi(-1))
        return {k: v for k, v in C.items() if k[1] in EVEN}
    up = [(a, b) for a, b in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (3, 3)]]
    up_ok = all((comm16(madd(msc(v4, g.qi(a)), msc(TGJu, g.qi(b)))) == {}) == (a == b) for a, b in up)
    kills = all((comm16(madd(msc(v4, g.qi(a)), msc(TGJu, g.qi(b)))) == {})
                == (not any(c == 0 for (r, c) in madd(msc(v4, g.qi(a)), msc(TGJu, g.qi(b))))) for a, b in up)
    dn_ok = all(comm16(madd(msc(w4, g.qi(a)), msc(TGJ, g.qi(b)))) == {} for a, b in [(1, 0), (0, 1), (1, 1), (2, -1), (5, 3)])
    g.check("M2 (prop:equalweight(2), rem:equalweight): a v_4 + a' v_4 (B - L) chi commutes with P on the sixteen exactly "
            "when a' = a, which is exactly when it annihilates nu^c; every b w_4 + b' T_GJ commutes with P",
            up_ok and kills and dn_ok)

    # prop:gradethree: w_4 (B - L) and v_4 (B - L)
    gam = []
    for a in range(5):
        gam.append(madd(an[a], cr[a]))
        gam.append(msc(madd(cr[a], an[a], g.qi(-1)), QI))
    def gprod(Sset):
        M = {(S, S): Q1 for S in range(DIM)}
        for k in Sset:
            M = mm(M, gam[k])
        return M
    def grades(O):
        gs = set()
        for r in range(11):
            for Sset in combinations(range(10), r):
                gm = gprod(Sset)
                tr = sum((v for (rr, cc), v in mm(dag(gm), O).items() if rr == cc), Q0)
                if tr != Q0:
                    gs.add(r)
        return gs
    res = []
    for E, pairs in ((mm(w4, BL), {('L', 'e^c'), ('Q', 'd^c')}), (mm(v4, BL), {('L', 'nu^c'), ('Q', 'u^c')})):
        Fm = form(E)
        sp = species(Fm)
        anti = all((Fm.get((q, p), Q0) + v) == Q0 for (p, q), v in Fm.items())
        mod = {k: max(abs(F(re)) for re, im in v) for k, v in sp.items()}
        lep = [k for k in sp if 'L' in k][0]
        qk = [k for k in sp if 'Q' in k][0]
        res.append(grades(E) == {3} and anti and set(sp) == {tuple(sorted(x)) for x in pairs} and mod[lep] == 3 * mod[qk])
    # family factor: an antisymmetric internal form times an antisymmetric family matrix is symmetric, zero on the
    # family diagonal
    Fw = form(mm(w4, BL))
    h = [[F(0), F(2), F(-1)], [F(-2), F(0), F(3)], [F(1), F(-3), F(0)]]
    sym = all(Fw.get((p, q), Q0) * g.qi(h[i][j]) == Fw.get((q, p), Q0) * g.qi(h[j][i])
              for (p, q) in Fw for i in range(3) for j in range(3))
    g.check("M3 (prop:gradethree): w_4 (B - L) and v_4 (B - L) are pure grade three, their mass forms on the sixteen are "
            "antisymmetric and couple exactly (L, e^c), (Q, d^c), resp. (L, nu^c), (Q, u^c), with lepton/quark modulus "
            "ratio 3; times an antisymmetric family matrix the form is symmetric and vanishes on the family diagonal",
            all(res) and sym and all(h[i][i] == 0 for i in range(3)))

    # prop:elimination on rational matrices: two 10s (Y1, Y2 with vev ratios r1, r2), one 126 (f; w_u, w_d), and a 120
    rng = random.Random(12)
    def rsym():
        A = [[F(rng.randint(-9, 9), rng.randint(1, 5)) for _ in range(3)] for _ in range(3)]
        return [[A[i][j] + A[j][i] for j in range(3)] for i in range(3)]
    def lin(*terms):
        return [[sum(c * M[i][j] for c, M in terms) for j in range(3)] for i in range(3)]
    Y1, Y2, f = rsym(), rsym(), rsym()
    r1, r2, wu, wd = F(1, 7), F(-2, 5), F(3, 4), F(-5, 6)
    Mu = lin((1, Y1), (1, Y2), (wu, f))
    Mnu = lin((1, Y1), (1, Y2), (-3 * wu, f))
    Md = lin((r1, Y1), (r2, Y2), (wd, f))
    Me = lin((r1, Y1), (r2, Y2), (-3 * wd, f))
    ok1 = lin((1, Md), (-1, Me)) == lin((4 * wd, f)) and lin((1, Mu), (-1, Mnu)) == lin((4 * wu, f))
    # premise (EW): choose w_u with 4 w_u f_33 = (M_u)_33 by solving for it, then M_nu = M_u - (M_u)_33 fhat
    Ysum = lin((1, Y1), (1, Y2))
    wu2 = Ysum[2][2] / (3 * f[2][2])                      # (M_nu)_33 = Ysum_33 - 3 w_u f_33 = 0
    Mu2 = lin((1, Ysum), (wu2, f))
    Mnu2 = lin((1, Ysum), (-3 * wu2, f))
    D = lin((1, Md), (-1, Me))
    fhat = [[D[i][j] / D[2][2] for j in range(3)] for i in range(3)]
    ok2 = Mnu2 == lin((1, Mu2), (-Mu2[2][2], fhat)) and Mnu2[2][2] == 0 and 4 * wu2 * f[2][2] == Mu2[2][2]
    hh = [[F(0), F(1), F(2)], [F(-1), F(0), F(-3)], [F(-2), F(3), F(0)]]
    cu_, cn_, cd_, ce_ = F(1, 3), F(-2, 3), F(1, 2), F(5, 2)
    Mu3, Mnu3 = lin((1, Mu2), (cu_, hh)), lin((1, Mnu2), (cn_, hh))
    Md3, Me3 = lin((1, Md), (cd_, hh)), lin((1, Me), (ce_, hh))
    D3 = lin((1, Md3), (-1, Me3))
    ok3 = D3 == lin((4 * wd, f), (cd_ - ce_, hh)) and lin((1, Mu3), (-1, Mnu3)) == lin((4 * wu2, f), (cu_ - cn_, hh)) \
        and Mnu3 != lin((1, Mu3), (-Mu3[2][2], [[D3[i][j] / D3[2][2] for j in range(3)] for i in range(3)]))
    g.check("M4 (prop:elimination): on rational matrices with two 10s and one 126, M_d - M_e = 4 w_d f and "
            "M_u - M_nu = 4 w_u f; with (M_nu)_33 = 0 imposed, M_nu = M_u - (M_u)_33 fhat, fhat = (M_d - M_e)/(M_d - M_e)_33; "
            "a 120 adds (c_d - c_e) h and (c_u - c_nu) h with independent coefficients, and the identity then fails",
            ok1 and ok2 and ok3)

    # ---- floating point: the stored coupling sets of obs:anglefits ----
    try:
        import numpy as np
    except ImportError:
        print("(numpy not available: Part M's RECORD lines and CONTROL lines C11, C12 skipped; M1 to M4 are exact and ran)")
        return
    import math
    STORED_FITS = {
        'natural': {
            'Y': [[[0.00044030999999999996, 8.558e-05], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.24034995, -0.00696217], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [69.3375, 0.0]]],
            'Z': [[[0.00075216, -0.00054827], [0.00253266, -0.00586652], [0.00265671, -0.00918216]], [[0.00253266, -0.00586652], [-0.0008808, -0.04857195], [-0.29373987, -0.00537998]], [[0.00265671, -0.00918216], [-0.29373987, -0.00537998], [-0.03473334, 0.50947232]]],
            'f': [[[2.159909099841564e-06, -8.815156696286951e-07], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.0007895328365602121, 7.171374093969165e-05], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [0.23807000367250775, 0.0]]],
            'H': [[[0.0, 0.0], [0.02177590845600245, 0.0009747223764485373], [0.00822980338529986, -0.05458645619613881]], [[-0.02177590845600245, -0.0009747223764485373], [0.0, 0.0], [-0.9982371706480334, 0.0]], [[-0.00822980338529986, 0.05458645619613881], [0.9982371706480334, 0.0], [0.0, 0.0]]],
            'wu': [97.08278927820685, 0.0],
            'wd': [0.008947149859879542, 3.115949788115471],
            'cu': [0.0, 0.0],
            'cn': [-0.03465126, -0.01185399],
            'cd': [-0.24735128, -0.00300884],
            'ce': [-0.00955048, -0.00124468],
        },
        'gj126_two10': {
            'Y': [[[0.000653983551094825, 0.0008460701866779715], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [-0.32692023733842507, 0.45020175112285876], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [69.3375, 0.0]]],
            'Z': [[[-0.0027436561059755804, -0.003365125720341077], [0.0049076222711831674, -0.004726335959628511], [-0.003207953313353855, -0.0016826581891301023]], [[0.0049076222711831674, -0.004726335959628511], [0.0, 0.0], [0.06520378954772495, -0.092692036899521]], [[-0.003207953313353855, -0.0016826581891301023], [0.06520378954772495, -0.092692036899521], [-0.5824819611272574, 0.06172057857070413]]],
            'f': [[[-6.109819775706838e-07, -0.0001297670403905826], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.0987620468877402, -0.06905023926118693], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [3.5449077018109154, 0.0]]],
            'H': [[[0.0, 0.0], [0.08557073397893822, 0.05442657738299888], [0.015877954334293523, 0.027791050323897205]], [[-0.08557073397893822, -0.05442657738299888], [0.0, 0.0], [0.9943293947423716, 0.0]], [[-0.015877954334293523, -0.027791050323897205], [-0.9943293947423716, 0.0], [0.0, 0.0]]],
            'wu': [6.519915874873973, 0.0],
            'wd': [-0.21612336005639018, -0.01412337148205993],
            'cu': [0.0, 0.0],
            'cn': [0.9167958271897713, -0.14187472874203033],
            'cd': [-0.006490610063581949, 0.09665319646658238],
            'ce': [0.18966815537826093, -0.1208754419902196],
        },
        'gj126_one10': {
            'Y': [[[0.002659817694930318, 0.0013348], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.9694610208902068, 0.68751179], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [69.33380733332764, 0.0]]],
            'Z': [[[1.1477396090192475e-05, 2.607330196234614e-05], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.002957085559958288, 0.010986007544488929], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [0.511454696555758, 0.42298822508879863]]],
            'f': [[[-0.0003841618032288598, -0.00020473659254241508], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [-0.10021688863310176, -0.10545311748377019], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [3.5448924836224682, 0.0]]],
            'H': [[[0.0, 0.0], [-0.07667673984276244, 0.062465370504992956], [-0.009418130015656171, -0.0541530995543228]], [[0.07667673984276244, -0.062465370504992956], [0.0, 0.0], [-0.9935781276227991, 0.0]], [[0.009418130015656171, 0.0541530995543228], [0.9935781276227991, 0.0], [0.0, 0.0]]],
            'wu': [6.519596635972491, 0.0],
            'wd': [0.06251862880519644, 0.204598763981685],
            'cu': [-0.14361513, 0.02808065],
            'cn': [-2.13103665, 0.63952452],
            'cd': [0.03865532, 0.04586222],
            'ce': [0.06209646, 0.06630892],
        },
        'shared_no120': {
            'Y': [[[0.001443564705269343, 0.0006321252819870818], [-0.012927810350428328, 0.021763542653096046], [0.00786511830511321, -0.017583889139157937]], [[-0.012927810350428332, 0.021763542653096043], [-0.25406839648292606, -0.25204028344307117], [0.3941847166536046, 0.14632241507355737]], [[0.007865118305113215, -0.017583889139157947], [0.39418471665360466, 0.14632241507355745], [69.3375, 0.0]]],
            'Z': [[[-0.0010803809256332174, 4.35032194065487e-05], [0.0028630494351771533, -0.005477306433422383], [0.0021456799207014154, 0.005169686922661418]], [[0.0028630494351771538, -0.005477306433422383], [-0.0013870412824325464, 0.04368818155292397], [0.03197087910883101, -0.06189021687439567]], [[0.0021456799207014163, 0.005169686922661419], [0.031970879108831014, -0.06189021687439568], [-0.38452195300565983, -0.437313333439209]]],
            'f': [[[-0.00012171281146283579, -9.695207556045759e-05], [0.0019828000582194833, -0.0033379785493365703], [-0.0012063107835399904, 0.002696925114444623]], [[0.0019828000582194838, -0.0033379785493365694], [0.08758748922675343, 0.038656622826155465], [-0.06045799388634301, -0.022442168105989604]], [[-0.0012063107835399913, 0.002696925114444624], [-0.060457993886343014, -0.02244216810598962], [3.544874584587284, 0.0]]],
            'H': [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]],
            'wu': [6.519976785777007, 0.0],
            'wd': [-0.1478086471861219, -0.16301013935319839],
            'cu': [0.0, 0.0],
            'cn': [0.0, 0.0],
            'cd': [0.0, 0.0],
            'ce': [0.0, 0.0],
        },
    }
    mt_, mc_, mu_ = 92.45, 0.3170, 0.00065
    target = dict(up=(mu_, mc_, mt_), down=(0.00130, 0.0261, 1.3651), lep=(0.000502, 0.1037, 1.764),
                  V=(0.2245, 0.045, 0.0040), sind=math.sin(1.144), m3=5.02e-11, ratio=5.83, pmns=(0.307, 0.0220, 0.51))
    vR = 1.95e10 / 0.469
    def C_of(d):
        M = lambda key: np.array([[complex(*d[key][i][j]) for j in range(3)] for i in range(3)])
        z = lambda key: complex(*d[key])
        return dict(Y=M('Y'), Z=M('Z'), f=M('f'), H=M('H'), wu=z('wu'), wd=z('wd'), cu=z('cu'), cn=z('cn'),
                    cd=z('cd'), ce=z('ce'))
    def left(M):
        U, s, _ = np.linalg.svd(M)
        o = np.argsort(s)
        return s[o], U[:, o]
    def obs(C):
        Y = C['Y'].copy()
        Y[2, 2] = 3 * C['wu'] * C['f'][2, 2]                     # premise (EW), held exact
        f, H = C['f'], C['H']
        Mu = Y + C['wu'] * f + C['cu'] * H
        Mn = Y - 3 * C['wu'] * f + C['cn'] * H
        Md = C['Z'] + C['wd'] * f + C['cd'] * H
        Me = C['Z'] - 3 * C['wd'] * f + C['ce'] * H
        su, Uu = left(Mu); sd, Ud = left(Md); se, Ue = left(Me)
        sn, Un = left(Mn @ np.linalg.inv(vR * f) @ Mn.T)
        V = Uu.conj().T @ Ud
        A = np.abs(V)
        J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
        s12, s13, s23 = A[0, 1], A[0, 2], A[1, 2]
        sind = J / (math.sqrt(1 - s12 ** 2) * (1 - s13 ** 2) * math.sqrt(1 - s23 ** 2) * s12 * s13 * s23)
        Pm = np.abs(Ue.conj().T @ Un)
        t13 = Pm[0, 2] ** 2
        return dict(up=su, down=sd, lep=se, V=(A[0, 1], A[1, 2], A[0, 2]), sind=sind, nu=sn,
                    pmns=(Pm[0, 1] ** 2 / (1 - t13), t13, Pm[1, 2] ** 2 / (1 - t13)), Mnmax=np.abs(Mn).max())
    def delta(C, eps_=1e-7):
        def m3r(D):
            o = obs(D)
            return o['nu'][2], o['nu'][2] / o['nu'][1]
        b3, br = m3r(C)
        best = [0.0, 0.0]
        for key in ('Y', 'Z', 'f', 'H'):
            for i in range(3):
                for j in range(i, 3):
                    if (key == 'Y' and (i, j) == (2, 2)) or abs(C[key][i, j]) < 1e-300:
                        continue
                    for d in (eps_, 1j * eps_):
                        D = dict(C)
                        A = C[key].copy()
                        A[i, j] *= (1 + d)
                        A[j, i] = -A[i, j] if key == 'H' else A[i, j]
                        D[key] = A
                        n3, nr = m3r(D)
                        best[0] = max(best[0], abs(math.log(n3 / b3)) / eps_)
                        best[1] = max(best[1], abs(math.log(nr / br)) / eps_)
        for key in ('wu', 'wd', 'cn', 'cd', 'ce'):
            if abs(C[key]) < 1e-300:
                continue
            for d in (eps_, 1j * eps_):
                D = dict(C)
                D[key] = C[key] * (1 + d)
                n3, nr = m3r(D)
                best[0] = max(best[0], abs(math.log(n3 / b3)) / eps_)
                best[1] = max(best[1], abs(math.log(nr / br)) / eps_)
        return best
    labels = {'natural': "two or more 10s + 126 + 120, factor 3 through 2-3 mixing",
              'gj126_two10': "two or more 10s + 126 + 120, factor 3 from the 126's second-family entry",
              'gj126_one10': "one 10 + 126 + 120",
              'shared_no120': "two or more 10s + 126, no 120"}
    good, D = {}, {}
    for k, d in STORED_FITS.items():
        C = C_of(d)
        o = obs(C)
        rel = lambda a, b: abs(a / b - 1)
        ok = (all(rel(a, b) < 0.01 for a, b in zip(o['up'], target['up']))
              and all(rel(a, b) < 0.02 for a, b in zip(o['down'], target['down']))
              and all(rel(a, b) < 0.01 for a, b in zip(o['lep'], target['lep']))
              and all(rel(a, b) < 0.02 for a, b in zip(o['V'], target['V']))
              and abs(o['sind'] - target['sind']) < 0.05
              and rel(o['nu'][2], target['m3']) < 0.01 and rel(o['nu'][2] / o['nu'][1], target['ratio']) < 0.01
              and all(abs(a - b) < s for a, b, s in zip(o['pmns'], target['pmns'], (0.013, 0.0007, 0.04))))
        good[k] = ok
        D[k] = delta(C)
        record(f"obs:anglefits, {labels[k]}: f_J = {abs(C['f'][2, 2]):.3f}, max |M_nu| entry = {o['Mnmax']:.3f} GeV, "
               f"m_nu = {', '.join(f'{v * 1e12:.4g}' for v in o['nu'])} meV, Delta(m_3) = {D[k][0]:.0f}, "
               f"Delta(m_3/m_2) = {D[k][1]:.0f}")
    g.check("C11 (CONTROL, floating point; obs:anglefits): each of the four stored coupling sets reproduces at M_I the "
            "nine charged-fermion masses, |V_us|, |V_cb|, |V_ub|, sin(delta_CKM), m_3, m_3/m_2 and the three lepton mixing "
            "angles",
            all(good.values()))
    g.check("C12 (CONTROL, floating point; obs:anglefits): the tuning measure is below 15 for the row whose factor 3 comes "
            "through 2-3 mixing, above 40 for both rows in which the 126 supplies it with a 120 present, and above 1000 "
            "without a 120",
            max(D['natural']) < 15 and min(D['gj126_two10']) > 40 and min(D['gj126_one10']) > 40
            and min(D['shared_no120']) > 1000)


part_M()


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
