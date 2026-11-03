#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T09.py: exact-arithmetic verification of the computational identities of
"The Twistor Correspondence: Ascended Spinors, Incidence, and the Palatial
Bridge" (Transport Papers, T9).

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rational and Gaussian-rational arithmetic
throughout, no floating point anywhere.

Conventions.  The paper's Clifford action is c(v) = sqrt(2) C(v) where C(v) is
the wedge-plus-contraction operator implemented here; irrational scalars never
appear because every checked identity is stated for C (the paper's identities
follow by scaling: c(u)c(v) = 2 C(u)C(v), and {c(u),c(v)} = 2<u,v> is
equivalent to {C(u),C(v)} = <u,v>, checked below).  The isotropic basis is
w1, w2, w3 (creation modes, indices 0..2) and w1', w2', w3' (annihilation,
indices 3..5), with <w_i, w_j'> = delta_ij.  Fock states are subsets of
{0,1,2} encoded as bitmasks 0..7; T = even masks, T' = odd masks.
The T-basis is t0 = 1, t1 = w2^w3, t2 = w3^w1 = -(w1^w3), t3 = w1^w2;
the T'-basis is s1 = w1, s2 = w2, s3 = w3, s0 = w1^w2^w3.
Psi denotes the C-normalised spinor identification; the paper's
sqrt(2)-normalised Psi gives the constant -2, corresponding to the
constant -1 checked here (tagged thm:spinorid).
Part H (v1.1, 2026-09-01) adds the reality checks of prop:reality: the real
orthonormal basis a1, a2, b1..b4 with w1 = a1 + b1, w2 = a2 + b2,
w3 = b3 + i b4 (and duals halved), the conjugation, kappa = Gamma C(b4) J
(kappa^2 = -1/2 in the C-normalisation, i.e. -1 for c), the twistor form
Sigma and its signature, the real-chart criterion, the summand composite of
prop:localtwistor(3), and the chiral-plane assignment of lem:homone.
"""

from fractions import Fraction
import GA as g
from itertools import permutations

I = g.QI_I
ZERO, ONE = g.QI(0), g.QI(1)


def qi_str(z):
    """Print a Gaussian rational as a number, e.g. 1, -7/25 + 24i/25."""
    if z.im == 0:
        return str(z.re)
    sgn = "+" if z.im > 0 else "-"
    return "%s %s %si" % (z.re, sgn, abs(z.im)) if z.re != 0 else "%s%si" % ("" if z.im > 0 else "-", abs(z.im))


def frac(x):
    return g.QI(x) if not isinstance(x, g.QI) else x


# ---------------------------------------------------------------------------
# 8x8 operator machinery on the Fock space (masks 0..7 over modes 0..2)
# ---------------------------------------------------------------------------

def zeros(n, m):
    return [[g.QI(0) for _ in range(m)] for _ in range(n)]


def mident(n):
    M = zeros(n, n)
    for i in range(n):
        M[i][i] = g.QI(1)
    return M


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscal(c, A):
    c = frac(c)
    return [[c * x for x in row] for row in A]


mmul = g.field_mat_mul


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mzero(A):
    return all(not A[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mtrace(A):
    return sum((A[i][i] for i in range(len(A))), g.QI(0))


def anti(A, B):
    return madd(mmul(A, B), mmul(B, A))


def comm(A, B):
    return msub(mmul(A, B), mmul(B, A))


def popcount(m):
    return bin(m).count("1")


def sign_below(mask, i):
    """(-1)^{number of set bits below i}."""
    return g.QI(-1) if popcount(mask & ((1 << i) - 1)) % 2 else g.QI(1)


def wedge_op(i):
    """a_i = w_i wedge (creation on mode i), as an 8x8 matrix."""
    M = zeros(8, 8)
    for m in range(8):
        if not (m >> i) & 1:
            M[m | (1 << i)][m] = sign_below(m, i)
    return M


def contract_op(i):
    """b_i = contraction with w_i' (annihilation on mode i)."""
    M = zeros(8, 8)
    for m in range(8):
        if (m >> i) & 1:
            M[m & ~(1 << i)][m] = sign_below(m, i)
    return M


A_OPS = [wedge_op(i) for i in range(3)]
B_OPS = [contract_op(i) for i in range(3)]


def C_of(v):
    """C(v) for v a 6-list [a1,a2,a3,b1,b2,b3] (w-basis then w'-basis)."""
    M = zeros(8, 8)
    for i in range(3):
        if frac(v[i]):
            M = madd(M, mscal(v[i], A_OPS[i]))
        if frac(v[3 + i]):
            M = madd(M, mscal(v[3 + i], B_OPS[i]))
    return M


def basis6(k):
    v = [g.QI(0)] * 6
    v[k] = g.QI(1)
    return v


def ip6(u, v):
    """The C-bilinear form: <w_i, w_j'> = delta."""
    return sum((frac(u[i]) * frac(v[3 + i]) + frac(u[3 + i]) * frac(v[i])
                for i in range(3)), g.QI(0))


def vadd(u, v):
    return [frac(a) + frac(b) for a, b in zip(u, v)]


def vscal(c, u):
    return [frac(c) * frac(a) for a in u]


BASIS_NAMES = ["w1", "w2", "w3", "w1'", "w2'", "w3'"]

# ---------------------------------------------------------------------------
# Part A: the Fock model (thm:purespinor)
# ---------------------------------------------------------------------------

ok = all(meq(anti(A_OPS[i], B_OPS[j]),
             mscal(1 if i == j else 0, mident(8)))
         for i in range(3) for j in range(3))
g.check("thm:purespinor: {w_i^, iota_j'} = delta_ij for the three wedge and "
      "contraction pairs (A_1, B_1 of prop:rent) on all states", ok)

ok = all(mzero(anti(A_OPS[i], A_OPS[j])) for i in range(3) for j in range(3)) and \
     all(mzero(anti(B_OPS[i], B_OPS[j])) for i in range(3) for j in range(3))
g.check("thm:purespinor: creation (and annihilation) operators anticommute", ok)

ok = True
for a in range(6):
    for b in range(6):
        lhs = anti(C_of(basis6(a)), C_of(basis6(b)))
        rhs = mscal(ip6(basis6(a), basis6(b)), mident(8))
        ok = ok and meq(lhs, rhs)
g.check("thm:purespinor: {C(u),C(v)} = <u,v> id on all 36 basis pairs "
      "(equivalently {c,c} = 2<,> for c = sqrt2 C)", ok)

# non-null and mixed instances: C(u)^2 = <u,u>/2, i.e. c(u)^2 = <u,u>
for u, lbl in [([1, 0, 0, 1, 0, 0], "w1+w1' (norm 2)"),
               ([1, g.QI_I, 0, 1, -g.QI_I, 0], "complex combination"),
               ([0, 1, 0, 0, 0, -1], "w2-w3' (null)")]:
    M2 = mmul(C_of(u), C_of(u))
    g.check("thm:purespinor: c(u)^2 = <u,u> id (as C(u)^2 = <u,u>/2) for u = " + lbl,
          meq(M2, mscal(ip6(u, u) / g.QI(2), mident(8))))

# 64 ordered products linearly independent -> simplicity, surjectivity,
# irreducibility at once
prods = []
for S in range(64):
    M = mident(8)
    for k in range(6):
        if (S >> k) & 1:
            M = mmul(M, C_of(basis6(k)))
    prods.append([M[i][j] for i in range(8) for j in range(8)])
g.check("thm:purespinor: the 64 ordered generator products are linearly "
      "independent in End(Fock) (rank 64)", g.field_rank(prods) == 64)

# parity: vectors are odd; even products block-diagonal
EVEN = [m for m in range(8) if popcount(m) % 2 == 0]
ODD = [m for m in range(8) if popcount(m) % 2 == 1]
ok = True
for k in range(6):
    M = C_of(basis6(k))
    for r in EVEN:
        for c in EVEN:
            ok = ok and not M[r][c]
    for r in ODD:
        for c in ODD:
            ok = ok and not M[r][c]
g.check("thm:purespinor: every vector acts oddly (swaps the chirality halves)", ok)

even_prods = [prods[S] for S in range(64) if popcount(S) % 2 == 0]
g.check("thm:purespinor: the even subalgebra has dimension exactly 32 = 16 + 16",
      g.field_rank(even_prods) == 32)


# ---------------------------------------------------------------------------
# Part B: the Chevalley pairing (lem:chevalley)
# ---------------------------------------------------------------------------

EPSK = {0: 1, 1: 1, 2: -1, 3: -1}  # (-1)^{k(k-1)/2}


def wedge_sign(S, T):
    """Sign of w_S ^ w_T as a multiple of w_{S union T}; 0 if not disjoint."""
    if S & T:
        return g.QI(0)
    seq = sorted([(x, 0) for x in range(3) if (S >> x) & 1]) + \
          sorted([(x, 1) for x in range(3) if (T >> x) & 1])
    vals = [x for x, _ in seq]
    inv = sum(1 for i in range(len(vals)) for j in range(i + 1, len(vals))
              if vals[i] > vals[j])
    return g.QI(-1) if inv % 2 else g.QI(1)


def B_mono(S, T):
    """Chevalley pairing of monomials: top coefficient of alpha(w_S) ^ w_T."""
    if (S | T) != 7 or (S & T):
        return g.QI(0)
    return frac(EPSK[popcount(S)]) * wedge_sign(S, T)


def B_pair(x, y):
    """B on 8-vectors."""
    out = g.QI(0)
    for S in range(8):
        if not x[S]:
            continue
        for T in range(8):
            if y[T]:
                out = out + x[S] * y[T] * B_mono(S, T)
    return out


def e8(mask):
    v = [g.QI(0)] * 8
    v[mask] = g.QI(1)
    return v


def apply_op(M, x):
    return [sum((M[i][j] * x[j] for j in range(8)), g.QI(0)) for i in range(8)]


ok = all(not B_mono(S, T)
         for S in EVEN for T in EVEN) and \
     all(not B_mono(S, T) for S in ODD for T in ODD)
g.check("lem:chevalley(1): B vanishes on T x T and on T' x T'", ok)

TP_MASKS = [1, 2, 4, 7]        # s1, s2, s3, s0
T_VECS = []                     # t0, t1, t2, t3 as 8-vectors
T_VECS.append(e8(0))
T_VECS.append(e8(6))
t2 = [g.QI(0)] * 8
t2[5] = g.QI(-1)                  # t2 = w3^w1 = -(w1^w3)
T_VECS.append(t2)
T_VECS.append(e8(3))

Bst = [[B_pair(e8(TP_MASKS[i]), T_VECS[j]) for j in range(4)] for i in range(4)]
g.check("lem:chevalley(1): B restricts to a perfect pairing T' x T (rank 4)",
      g.field_rank([row[:] for row in Bst]) == 4)

ok = all(B_pair(e8(S), e8(T)) == -B_pair(e8(T), e8(S))
         for S in range(8) for T in range(8))
g.check("lem:chevalley(2): B is antisymmetric on the full basis", ok)

ok = True
for k in range(6):
    Ck = C_of(basis6(k))
    for S in range(8):
        for T in range(8):
            lhs = B_pair(apply_op(Ck, e8(S)), e8(T))
            rhs = B_pair(e8(S), apply_op(Ck, e8(T)))
            ok = ok and lhs == rhs
g.check("lem:chevalley(3): B(C(v)x, y) = B(x, C(v)y) for all 6 basis vectors "
      "on all 64 pairs", ok)

ok = True
for a in range(6):
    for b in range(a + 1, 6):
        beta = mscal(Fraction(1, 2), comm(C_of(basis6(a)), C_of(basis6(b))))
        for S in range(8):
            for T in range(8):
                lhs = B_pair(apply_op(beta, e8(S)), e8(T))
                rhs = B_pair(e8(S), apply_op(beta, e8(T)))
                ok = ok and lhs == -rhs
g.check("lem:chevalley(4): B(beta x, y) + B(x, beta y) = 0 for all 15 "
      "antisymmetrised bivectors", ok)

# ---------------------------------------------------------------------------
# Part C: the spinor identification (thm:spinorid, ex:psi)
# ---------------------------------------------------------------------------

Binv = [g.field_solve([row[:] for row in Bst],
                    [g.QI(1) if r == j else g.QI(0) for r in range(4)])
        for j in range(4)]
Binv = [[Binv[j][i] for j in range(4)] for i in range(4)]  # Binv[i][j] = (Bst^-1)_ij


def G_of(v):
    """G_v(s_i, s_j) = B(s_i, C(v) s_j), 4x4 over the T'-basis."""
    Cv = C_of(v)
    return [[B_pair(e8(TP_MASKS[i]), apply_op(Cv, e8(TP_MASKS[j])))
             for j in range(4)] for i in range(4)]


def Psi(v):
    """Psi_C(v) as an antisymmetric 4x4 coefficient matrix in the t-basis:
    P = Bst^{-1} G (Bst^{-1})^T."""
    G = G_of(v)
    Mi = Binv
    P = zeros(4, 4)
    for k in range(4):
        for l in range(4):
            P[k][l] = sum((Mi[k][i] * G[i][j] * Mi[l][j]
                           for i in range(4) for j in range(4)), g.QI(0))
    return P


ok = all(all(G_of(basis6(k))[i][j] == -G_of(basis6(k))[j][i]
             for i in range(4) for j in range(4)) for k in range(6))
g.check("thm:spinorid: G_v is antisymmetric for all basis v", ok)

PSI_BASIS = [Psi(basis6(k)) for k in range(6)]
flat = []
for k in range(6):
    P = PSI_BASIS[k]
    flat.append([P[0][1], P[0][2], P[0][3], P[1][2], P[1][3], P[2][3]])
g.check("thm:spinorid: Psi is injective, hence an isomorphism (rank 6)",
      g.field_rank(flat) == 6)


def eps0(P, Q):
    """eps0(P ^ Q) for antisymmetric coefficient matrices in the t-basis."""
    out = g.QI(0)
    for perm in permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4)
                  if perm[i] > perm[j])
        s = g.QI(-1) if inv % 2 else g.QI(1)
        out = out + s * P[perm[0]][perm[1]] * Q[perm[2]][perm[3]]
    return out / g.QI(4)


ok = True
for a in range(6):
    for b in range(a, 6):
        val = eps0(PSI_BASIS[a], PSI_BASIS[b])
        ok = ok and val == -ip6(basis6(a), basis6(b))
g.check("thm:spinorid: eps0(Psi_C(v)^Psi_C(v')) = -<v,v'> on all 21 pairs "
      "(the C-normalised constant -1; -2 for the paper's Psi, whence "
      "eps := -eps0/2)", ok)

# ex:psi: explicit values and planes
P1 = Psi(basis6(0))   # Psi(w1)
exp1 = zeros(4, 4)
exp1[2][3], exp1[3][2] = g.QI(-1), g.QI(1)   # -t2^t3
g.check("ex:psi: Psi_C(w1) = -t2^t3 exactly", meq(P1, exp1))
P1p = Psi(basis6(3))  # Psi(w1')
exp2 = zeros(4, 4)
exp2[0][1], exp2[1][0] = g.QI(1), g.QI(-1)   # t0^t1
g.check("ex:psi: Psi_C(w1') = t0^t1 exactly", meq(P1p, exp2))
g.check("ex:psi: the planes are span(t2,t3) and span(t0,t1) "
      "(matrix ranks 2, supported on the stated blocks)",
      g.field_rank([r[:] for r in P1]) == 2 and g.field_rank([r[:] for r in P1p]) == 2
      and all(not P1[i][j] for i in range(2) for j in range(4))
      and all(not P1p[i][j] for i in range(2, 4) for j in range(4)))


def pfaffian(P):
    return P[0][1] * P[2][3] - P[0][2] * P[1][3] + P[0][3] * P[1][2]


ok = all(not pfaffian(PSI_BASIS[k]) for k in range(6))
g.check("thm:spinorid(2): all six null basis vectors give simple (Pf = 0) "
      "bivectors", ok)
vnn = vadd(basis6(0), basis6(3))   # w1 + w1', norm 2
Pnn = Psi(vnn)
g.check("thm:spinorid(2): the non-null w1+w1' gives Pf != 0 and rank 4",
      bool(pfaffian(Pnn)) and g.field_rank([r[:] for r in Pnn]) == 4)

# ---------------------------------------------------------------------------
# Part D: incidence (prop:skewwitt, thm:incidence), stabilisers, summands
# ---------------------------------------------------------------------------

# effective form on Lambda^2 T matching ip6 through Psi: <P,Q> := -eps0(P^Q)
N0 = P1        # Psi(w1): the origin line bivector, = pi1 ^ pi2
NINF = P1p     # Psi(w1'): the infinity line bivector, = e1 ^ e2

g.check("prop:skewwitt: <N0,NINF> = 1, <N0,N0> = <NINF,NINF> = 0 "
      "(hyperbolic pair)",
      -eps0(N0, NINF) == ONE and not eps0(N0, N0) and not eps0(NINF, NINF))

# bases with pi1^pi2 = N0 and e1^e2 = NINF:
PI1 = [g.QI(0), g.QI(0), g.QI(-1), g.QI(0)]   # -t2
PI2 = [g.QI(0), g.QI(0), g.QI(0), g.QI(1)]    # t3
E1 = [g.QI(1), g.QI(0), g.QI(0), g.QI(0)]     # t0
E2 = [g.QI(0), g.QI(1), g.QI(0), g.QI(0)]     # t1


def wedge4(u, v):
    P = zeros(4, 4)
    for k in range(4):
        for l in range(4):
            P[k][l] = u[k] * v[l] - u[l] * v[k]
    return P


g.check("thm:incidence: the chosen bases satisfy pi1^pi2 = N0, e1^e2 = NINF",
      meq(wedge4(PI1, PI2), N0) and meq(wedge4(E1, E2), NINF))


def P_of(A):
    """Pluecker bivector of the graph line of A: S_pi -> S_omega."""
    u = vadd4(PI1, [A[0][0] * E1[k] + A[1][0] * E2[k] for k in range(4)])
    v = vadd4(PI2, [A[0][1] * E1[k] + A[1][1] * E2[k] for k in range(4)])
    return wedge4(u, v)


def vadd4(u, v):
    return [u[k] + v[k] for k in range(4)]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


SAMPLES = [
    ("identity", [[g.QI(1), g.QI(0)], [g.QI(0), g.QI(1)]]),
    ("gaussian", [[g.QI(1, 1), g.QI(0, 2)], [g.QI(2), g.QI(1, -1)]]),
    ("singular", [[g.QI(1), g.QI(2)], [g.QI(3), g.QI(6)]]),
    ("i*hermitian", [[g.QI(0, 3), g.QI(0, 1) * g.QI(1, -1)], [g.QI(0, 1) * g.QI(1, 1), g.QI(0, 1)]]),
]

psimat = [[PSI_BASIS[k][0][1], PSI_BASIS[k][0][2], PSI_BASIS[k][0][3],
           PSI_BASIS[k][1][2], PSI_BASIS[k][1][3], PSI_BASIS[k][2][3]]
          for k in range(6)]
psimat_T = [[psimat[k][c] for k in range(6)] for c in range(6)]


def psi_inv(P):
    rhs = [P[0][1], P[0][2], P[0][3], P[1][2], P[1][3], P[2][3]]
    return g.field_solve([row[:] for row in psimat_T], rhs)


for name, A in SAMPLES:
    PA = P_of(A)
    dA = det2(A)
    phi = msub(msub(PA, N0), mscal(dA, NINF))
    # (a) expansion: phi lies in the mixed slot S_omega ^ S_pi
    okmix = all(not phi[i][j] for i in (0, 1) for j in (0, 1)) and \
            all(not phi[i][j] for i in (2, 3) for j in (2, 3))
    # (b) norm identity <phi,phi> = -2 det A (effective form)
    oknorm = -eps0(phi, phi) == g.QI(-2) * dA
    # (c) P(A) = X(m(A)): m orthogonal to the Witt pair, det A = -ip(m,m)/2
    m = psi_inv(phi)
    okm = (ip6(m, basis6(0)) == ZERO and ip6(m, basis6(3)) == ZERO
           and g.QI(-1) * ip6(m, m) / g.QI(2) == dA)
    # (d) simplicity of P(A)
    okpf = not pfaffian(PA)
    g.check("thm:incidence: expansion/norm/chart/simplicity for A = " + name,
          okmix and oknorm and okm and okpf)

# the sign flip of thm:incidence(2) on the i*xhat sample (xhat Hermitian, det xhat = 1):
# <m,m> = -2 det(i xhat) = +2 det xhat.  (Whether m is real is settled in Part H.)
name, A = SAMPLES[3]
m = psi_inv(msub(msub(P_of(A), N0), mscal(det2(A), NINF)))
g.check("thm:incidence(2): for A = i xhat with det xhat = 1 the chart point "
      "has ip(m,m) = -2 det(i xhat) = +2 det xhat (the sign flip of the i)",
      ip6(m, m) == g.QI(2))

ok = all(-eps0(P_of(A), NINF) == ONE for _, A in SAMPLES)
Pmeet = wedge4(E1, vadd4(PI1, E2))
g.check("thm:incidence(3): <P(A), n_inf> = 1 on the chart; a line meeting "
      "L_inf pairs to 0", ok and not eps0(Pmeet, NINF))

# --- bivector machinery: vector action and spinor action -------------------

PAIRS = [(a, b) for a in range(6) for b in range(a + 1, 6)]


def vec_action(a, b):
    """(w_a ^ w_b) acting on V: 6x6 matrix, (a^b)(w) = <b,w>a - <a,w>b."""
    M = zeros(6, 6)
    for k in range(6):
        w = basis6(k)
        cb, ca = ip6(basis6(b), w), ip6(basis6(a), w)
        for r in range(6):
            M[r][k] = M[r][k] + cb * frac(basis6(a)[r]) - ca * frac(basis6(b)[r])
    return M


def spin_element(a, b):
    """The Clifford element with commutator action = the bivector w_a ^ w_b:
    C(a)C(b) - <a,b>/2 (equals (1/2)c(a)c(b) - <a,b>/2)."""
    el = mmul(C_of(basis6(a)), C_of(basis6(b)))
    ip = ip6(basis6(a), basis6(b))
    return msub(el, mscal(ip / g.QI(2), mident(8)))


ok = True
for (a, b) in PAIRS:
    el = spin_element(a, b)
    V = vec_action(a, b)
    for k in range(6):
        lhs = comm(el, C_of(basis6(k)))
        img = [V[r][k] for r in range(6)]
        rhs = C_of(img)
        ok = ok and meq(lhs, rhs)
g.check("prop:spiniso: [beta, C(w)] = C(beta w) for all 15 basis bivectors "
      "on all 6 vectors", ok)

# T-block of each spin element (4x4 in the t-basis)
T_MAT = [[T_VECS[j][m] for j in range(4)] for m in range(8)]  # 8x4


def t_block(el):
    cols = []
    for j in range(4):
        img = apply_op(el, T_VECS[j])
        # solve T_MAT x = img restricted to even rows
        rows = [m for m in range(8) if popcount(m) % 2 == 0]
        Msys = [[T_MAT[m][k] for k in range(4)] for m in rows]
        rhs = [img[m] for m in rows]
        cols.append(g.field_solve(Msys, rhs))
    return [[cols[j][i] for j in range(4)] for i in range(4)]


RHO = {}
for (a, b) in PAIRS:
    RHO[(a, b)] = t_block(spin_element(a, b))

ok = all(mtrace(RHO[p]) == ZERO for p in PAIRS)
g.check("prop:spiniso: all 15 spinor actions are trace-free (land in sl(T))", ok)

g.check("prop:spiniso: the 15 spinor actions are linearly independent "
      "(faithful; iso onto sl(T) by dimension)",
      g.field_rank([[RHO[p][i][j] for i in range(4) for j in range(4)]
                  for p in PAIRS]) == 15)

# equivariance of Psi: Psi(beta v) = rho(beta) Psi(v) + Psi(v) rho(beta)^T
ok = True
for (a, b) in PAIRS:
    V = vec_action(a, b)
    rho = RHO[(a, b)]
    for k in range(6):
        lhs = Psi([sum((V[r][c] * frac(basis6(k)[c]) for c in range(6)), g.QI(0))
                   for r in range(6)])
        Pv = PSI_BASIS[k]
        rhs = madd(mmul(rho, Pv), mmul(Pv, [[rho[j][i] for j in range(4)]
                                            for i in range(4)]))
        ok = ok and meq(lhs, rhs)
g.check("thm:spinorid: equivariance Psi(beta v) = beta . Psi(v) for all 15 "
      "bivectors and 6 vectors (90 identities)", ok)

# Poincare: stabiliser census of n_inf = w1'
stab_vec = ray_only = non_stab = 0
twistor_match = True
for (a, b) in PAIRS:
    V = vec_action(a, b)
    img = [V[r][3] for r in range(6)]     # action on w1'
    if all(not x for x in img):
        stab_vec += 1
        in_parab = True
    elif all(not img[r] for r in range(6) if r != 3):
        ray_only += 1
        in_parab = True
    else:
        non_stab += 1
        in_parab = False
    rho = RHO[(a, b)]
    preserves_Somega = all(not rho[i][j] for i in (2, 3) for j in (0, 1))
    twistor_match = twistor_match and (in_parab == preserves_Somega)
g.check("thm:incidence(4)/fact:parabolic: stabiliser census of n_inf is "
      "10 (vector) + 1 (ray) + 4 (moved): the Poincare parabolic has dim 11",
      (stab_vec, ray_only, non_stab) == (10, 1, 4))
g.check("thm:incidence(4): a bivector stabilises the ray of n_inf exactly "
      "when its spinor action preserves the infinity plane S_omega",
      twistor_match)

# summands and grading (prop:localtwistor, prop:rent), X_p = w1, u_p = w1'
ok = True
for w in (1, 2, 4, 5):     # mixed directions w2, w3, w2', w3'
    rho = RHO[(min(3, w), max(3, w))]   # +- (u_p ^ w) with u_p = w1' (index 3)
    kills_omega = all(not rho[i][j] for i in range(4) for j in (0, 1))
    maps_pi_to_omega = all(not rho[i][j] for i in (2, 3) for j in (2, 3))
    nonzero = not all(not rho[i][j] for i in range(4) for j in range(4))
    ok = ok and kills_omega and maps_pi_to_omega and nonzero
g.check("prop:localtwistor: the soldering summand u_p^w maps S_pi to S_omega "
      "and annihilates S_omega, for all four mixed directions", ok)

ok = True
for w in (1, 2, 4, 5):
    rho = RHO[(min(0, w), max(0, w))]   # +- (X_p ^ w) with X_p = w1 (index 0)
    kills_pi = all(not rho[i][j] for i in range(4) for j in (2, 3))
    maps_omega_to_pi = all(not rho[i][j] for i in (0, 1) for j in (0, 1))
    nonzero = not all(not rho[i][j] for i in range(4) for j in range(4))
    ok = ok and kills_pi and maps_omega_to_pi and nonzero
g.check("prop:localtwistor: the Schouten summand X_p^w maps S_omega to S_pi "
      "and annihilates S_pi, for all four mixed directions", ok)

Eel = spin_element(0, 3)    # w1 ^ w1' = v ^ v*
expected = {m: (Fraction(1, 2) if (m & 1) else Fraction(-1, 2)) for m in range(8)}
ok = True
for m in range(8):
    img = apply_op(Eel, e8(m))
    ok = ok and all((img[r] == (frac(expected[m]) if r == m else ZERO))
                    for r in range(8))
g.check("prop:rent: rho(v^v*) = N - 1/2 on all eight states (eigenvalues "
      "+1/2 with the mode, -1/2 without)", ok)

# ---------------------------------------------------------------------------
# Part E: twistors as states (thm:states)
# ---------------------------------------------------------------------------


def annihilator(x):
    """The space {v in V_C : C(v)x = 0} for an 8-vector x, as a basis list."""
    rows = []
    for k in range(6):
        rows.append(apply_op(C_of(basis6(k)), x))
    # solve sum_k v_k C(w_k) x = 0: unknowns v in C^6
    Msys = [[rows[k][m] for k in range(6)] for m in range(8)]
    # kernel of the 8x6 system
    return kernel(Msys)


kernel = g.field_kernel   # promoted to GA.py (T9 v1.2)


# vacuum: W_1 = W'
W1 = annihilator(e8(0))
ok = len(W1) == 3 and all(all(not v[k] for k in range(3)) for v in W1)
g.check("thm:states(1): the annihilator of the vacuum is exactly W' "
      "(dimension 3, annihilation span)", ok)

# a generic twistor: u = t0 + 2 t1 + i t2 + (1-i) t3
u_gen = [g.QI(0)] * 8
u_gen[0] = g.QI(1)
u_gen[6] = g.QI(2)
u_gen[5] = g.QI(0, -1)      # i * t2 = i * (-(w1^w3)) -> coefficient -i on mask 5
u_gen[3] = g.QI(1, -1)
Wu = annihilator(u_gen)
ok = len(Wu) == 3
iso = all(ip6(v1, v2) == ZERO for v1 in Wu for v2 in Wu)
g.check("thm:states(1): a generic twistor is pure: annihilator dimension 3 "
      "and totally isotropic", ok and iso)

odd_gen = [g.QI(0)] * 8
odd_gen[1] = g.QI(1)
odd_gen[2] = g.QI(0, 1)
odd_gen[7] = g.QI(3)
Wo = annihilator(odd_gen)
g.check("thm:states(1)/(3): an odd (dual) twistor is likewise pure; its "
      "annihilator (a beta-plane) has dimension 3 and is isotropic",
      len(Wo) == 3 and all(ip6(v1, v2) == ZERO for v1 in Wo for v2 in Wo))

# thm:states(2): the generic twistor's own pair system.  Dual complement to
# W_u by the construction in the proof: v_j with <w_i, v_j> = delta_ij, then
# u_j = v_j - (1/2) sum_k <v_j, v_k> w_k.
Wmat = [[ip6(Wu[i], basis6(c)) for c in range(6)] for i in range(3)]   # 3x6
Vs = []
for j in range(3):
    # solve for v in the span of the six basis vectors: <w_i, v> = delta_ij
    # (use field_kernel on the augmented system to find one solution)
    aug = [Wmat[i] + [g.QI(-1 if i == j else 0)] for i in range(3)]
    ker = g.field_kernel(aug)
    sol = next(v for v in ker if v[6])
    Vs.append([x / sol[6] for x in sol[:6]])
Us = []
for j in range(3):
    u = Vs[j][:]
    for k in range(3):
        u = vadd(u, vscal(g.QI(0) - ip6(Vs[j], Vs[k]) / g.QI(2), Wu[k]))
    Us.append(u)
okd = all(ip6(Wu[i], Us[j]) == frac(1 if i == j else 0) for i in range(3) for j in range(3))
oki = all(ip6(Us[i], Us[j]) == ZERO for i in range(3) for j in range(3))
Fs = [C_of(Us[j]) for j in range(3)]      # creation for u_gen
Fd = [C_of(Wu[i]) for i in range(3)]      # annihilation for u_gen
okcar = all(meq(anti(Fd[i], Fs[j]), mscal(1 if i == j else 0, mident(8)))
            for i in range(3) for j in range(3)) \
    and all(mzero(anti(Fs[i], Fs[j])) and mzero(anti(Fd[i], Fd[j]))
            for i in range(3) for j in range(3)) \
    and all(all(not x for x in apply_op(Fd[i], u_gen)) for i in range(3))
g.check("thm:states(2): the generic twistor's own pair system (annihilator W_u, "
      "dual isotropic complement U' built as in the proof) satisfies the CAR "
      "relations {C(w_i), C(u_j)} = delta_ij, squares zero, and annihilates u", okd and oki and okcar)

# joint kernel of C(W') on the whole module is the vacuum line
Msys = []
for k in (3, 4, 5):
    Ck = C_of(basis6(k))
    for r in range(8):
        Msys.append([Ck[r][c] for c in range(8)])
K = kernel(Msys)
g.check("thm:states(1): the joint kernel of the annihilation operators is "
      "exactly the vacuum line (dimension 1)",
      len(K) == 1 and K[0][0] and all(not K[0][m] for m in range(1, 8)))

# Fock generation: c(Lambda^bullet W') applied to the top state w123 spans all
top = e8(7)
gen_vecs = []
for S in range(8):
    M = mident(8)
    for k in (3, 4, 5):
        if (S >> (k - 3)) & 1:
            M = mmul(M, C_of(basis6(k)))
    gen_vecs.append(apply_op(M, top))
g.check("thm:states(2): the dual system generates the whole module from the "
      "top state (rank 8): every twistor is the vacuum of its own pair system",
      g.field_rank(gen_vecs) == 8)

# ---------------------------------------------------------------------------
# Part F: the palatial algebra (lem:weyl, thm:core, lem:quartic)
# ---------------------------------------------------------------------------
# polynomial realisation Z^a = z_a, Zbar_b = -hbar d/dz_b with hbar = 1;
# monomials over 4 variables as exponent tuples.


def p_zero():
    return {}


def p_add(f, q):
    out = dict(f)
    for k, v in q.items():
        out[k] = out.get(k, g.QI(0)) + v
    return {k: v for k, v in out.items() if v}


def p_scal(c, f):
    c = frac(c)
    return {k: c * v for k, v in f.items() if c * v}


def op_Z(a, f):
    out = {}
    for k, v in f.items():
        kk = list(k)
        kk[a] += 1
        out[tuple(kk)] = out.get(tuple(kk), g.QI(0)) + v
    return out


def op_Zbar(b, f):
    """Zbar_b = -hbar d/dz_b with hbar = 1: this is the realisation with
    [Z^a, Zbar_b] = +hbar delta (the palatial sign); the derivative
    realisation with the opposite sign flips the homogeneity to +2s+2."""
    out = {}
    for k, v in f.items():
        if k[b] == 0:
            continue
        kk = list(k)
        kk[b] -= 1
        out[tuple(kk)] = out.get(tuple(kk), g.QI(0)) - frac(k[b]) * v
    return {k: v for k, v in out.items() if v}


def op_q(M, f):
    """q(M) = (1/2) sum M^b_a (Z^a Zbar_b + Zbar_b Z^a), hbar = 1."""
    out = {}
    for a in range(4):
        for b in range(4):
            if not M[b][a]:
                continue
            t1 = op_Z(a, op_Zbar(b, f))
            t2 = op_Zbar(b, op_Z(a, f))
            for k, v in p_add(t1, t2).items():
                out[k] = out.get(k, g.QI(0)) + M[b][a] * v / g.QI(2)
    return {k: v for k, v in out.items() if v}


def monos(maxdeg):
    out = []
    for d in range(maxdeg + 1):
        def rec(pos, left, cur):
            if pos == 3:
                out.append(tuple(cur + [left]))
                return
            for e in range(left + 1):
                rec(pos + 1, left - e, cur + [e])
        rec(0, d, [])
    return out


ok = True
for a in range(4):
    for b in range(4):
        for k in monos(2):
            f = {k: g.QI(1)}
            lhs = p_add(op_Z(a, op_Zbar(b, f)), p_scal(-1, op_Zbar(b, op_Z(a, f))))
            rhs = p_scal(1 if a == b else 0, f)
            ok = ok and p_add(lhs, p_scal(-1, rhs)) == {}
g.check("palatial relations: [Z^a, Zbar_b] = hbar delta_ab holds in the "
      "realisation Zbar = -hbar d/dz", ok)

ok = True
for k in monos(3):
    f = {k: g.QI(1)}
    h = sum(k)
    sid = op_q(mident(4), f)          # q(id); helicity s = q(id)/2
    expect = p_scal(g.QI(-1) * frac(Fraction(h + 2, 1)), f)   # 2s = -(h+2)... times 2
    ok = ok and p_add(sid, p_scal(-1, expect)) == {}
g.check("thm:core(4) point of contact: q(id) = -(h+2) hbar on homogeneity-h "
      "functions, i.e. helicity s has h = -2s-2: the ordering shift is the "
      "-2 in Penrose's homogeneity", ok)

MM = [[g.QI(1), g.QI(0, 2), g.QI(0), g.QI(-1)],
      [g.QI(2), g.QI(1, 1), g.QI(0, -1), g.QI(0)],
      [g.QI(0), g.QI(3), g.QI(1), g.QI(1, 2)],
      [g.QI(1, -1), g.QI(0), g.QI(2), g.QI(0, 1)]]
NN = [[g.QI(0), g.QI(1), g.QI(1, 1), g.QI(0)],
      [g.QI(0, 1), g.QI(2), g.QI(0), g.QI(3)],
      [g.QI(1), g.QI(0, -2), g.QI(1, -1), g.QI(0)],
      [g.QI(0), g.QI(1), g.QI(0), g.QI(2, 1)]]


def mat_comm4(A, B):
    C1 = [[sum((A[i][k] * B[k][j] for k in range(4)), g.QI(0)) for j in range(4)]
          for i in range(4)]
    C2 = [[sum((B[i][k] * A[k][j] for k in range(4)), g.QI(0)) for j in range(4)]
          for i in range(4)]
    return [[C1[i][j] - C2[i][j] for j in range(4)] for i in range(4)]


ok = True
for k in monos(2):
    f = {k: g.QI(1)}
    lhs = p_add(op_q(MM, op_q(NN, f)), p_scal(-1, op_q(NN, op_q(MM, f))))
    rhs = op_q(mat_comm4(MM, NN), f)
    ok = ok and p_add(lhs, p_scal(-1, rhs)) == {}
g.check("lem:weyl(2)/lem:quartic: [q(M), q(N)] = hbar q([M,N]) as operators "
      "(checked on all monomials of degree <= 2, which determine both sides)",
      ok)

ok = True
for k in monos(2):
    f = {k: g.QI(1)}
    # normal ordering: sum M^b_a Z^a Zbar_b
    nrm = {}
    for a in range(4):
        for b in range(4):
            if MM[b][a]:
                for kk, v in op_Z(a, op_Zbar(b, f)).items():
                    nrm[kk] = nrm.get(kk, g.QI(0)) + MM[b][a] * v
    nrm = {kk: v for kk, v in nrm.items() if v}
    trM = sum((MM[i][i] for i in range(4)), g.QI(0))
    rhs = p_add(nrm, p_scal(g.QI(-1) * trM / g.QI(2), f))
    ok = ok and p_add(op_q(MM, f), p_scal(-1, rhs)) == {}
g.check("lem:weyl(3): q(M) = normal ordering - (hbar/2) tr M on a sample M "
      "(the M = id shift 2 hbar follows by linearity and is covered by the "
      "q(id) = -(h+2) hbar check)", ok)

ok = True
for gi in range(4):
    for k in monos(2):
        f = {k: g.QI(1)}
        lhs = p_add(op_q(MM, op_Z(gi, f)), p_scal(-1, op_Z(gi, op_q(MM, f))))
        rhs = {}
        for a in range(4):
            if MM[gi][a]:
                for kk, v in op_Z(a, f).items():
                    rhs[kk] = rhs.get(kk, g.QI(0)) + g.QI(-1) * MM[gi][a] * v
        rhs = {kk: v for kk, v in rhs.items() if v}
        ok = ok and p_add(lhs, p_scal(-1, rhs)) == {}
g.check("lem:weyl(1): [q(M), Z^g] = -hbar (M Z)^g on all generators", ok)

# ---------------------------------------------------------------------------
# Part G: the chirality split and ordering blindness (lem:star, prop:blind)
# ---------------------------------------------------------------------------

ETA = [1, -1, -1, -1]


def lorentz_action(a, b):
    """(e_a ^ e_b) acting on R^{1,3}: M w = eta(b,w) e_a - eta(a,w) e_b."""
    M = [[g.QI(0)] * 4 for _ in range(4)]
    for k in range(4):
        M[a][k] = M[a][k] + frac(ETA[b] if k == b else 0)
        M[b][k] = M[b][k] - frac(ETA[a] if k == a else 0)
    return M


BB = [lorentz_action(0, i) for i in (1, 2, 3)]
RR = [lorentz_action(2, 3), lorentz_action(3, 1), lorentz_action(1, 2)]

EPS3 = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
        (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


def m4eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))


def m4comm(A, B):
    return mat_comm4(A, B)


def m4lin(*terms):
    out = [[g.QI(0)] * 4 for _ in range(4)]
    for c, M in terms:
        c = frac(c)
        for i in range(4):
            for j in range(4):
                out[i][j] = out[i][j] + c * M[i][j]
    return out


ok = True
ZERO4 = [[g.QI(0)] * 4 for _ in range(4)]
for i in range(3):
    for j in range(3):
        if i == j:
            ok = ok and m4eq(m4comm(RR[i], BB[i]), ZERO4)   # [R_i, B_i] = 0
            continue
        k = 3 - i - j
        e = frac(EPS3[(i, j, k)])
        ok = ok and m4eq(m4comm(RR[i], RR[j]), m4lin((e, RR[k])))
        ok = ok and m4eq(m4comm(RR[i], BB[j]), m4lin((e, BB[k])))
        ok = ok and m4eq(m4comm(BB[i], BB[j]), m4lin((g.QI(-1) * e, RR[k])))
g.check("prop:blind(1): the so(1,3) bracket table [R,R]=eR, [R,B]=eB, "
      "[B,B]=-eR holds exactly, all fifteen brackets including [R_i,B_i] = 0", ok)

AP = [m4lin((Fraction(1, 2), RR[i]), (g.QI(0, Fraction(1, 2)), BB[i])) for i in range(3)]
AM = [m4lin((Fraction(1, 2), RR[i]), (g.QI(0, Fraction(-1, 2)), BB[i])) for i in range(3)]

ok = True
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        k = 3 - i - j
        e = frac(EPS3[(i, j, k)])
        ok = ok and m4eq(m4comm(AP[i], AP[j]), m4lin((e, AP[k])))
        ok = ok and m4eq(m4comm(AM[i], AM[j]), m4lin((e, AM[k])))
for i in range(3):
    for j in range(3):
        ok = ok and all(not m4comm(AP[i], AM[j])[r][c]
                        for r in range(4) for c in range(4))
g.check("prop:blind(1): the chirality factors close ([A1,A1] = eA1, "
      "[A2,A2] = eA2) and commute ([A1,A2] = 0), for A1 = (R + iB)/2 and "
      "A2 = (R - iB)/2 (the paper's A^(1), A^(2)): sl2 + sl2", ok)

# Hodge star on 2-forms: (*F)_{ab} = (1/2) eps_{abcd} F^{cd}, indices by eta


def eps4(a, b, c, d):
    perm = (a, b, c, d)
    if len(set(perm)) < 4:
        return 0
    inv = sum(1 for x in range(4) for y in range(x + 1, 4)
              if perm[x] > perm[y])
    return -1 if inv % 2 else 1


def star_form(F):
    """F an antisymmetric 4x4 (lower indices); returns *F."""
    out = [[g.QI(0)] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            s = g.QI(0)
            for c in range(4):
                for d in range(4):
                    e = eps4(a, b, c, d)
                    if e:
                        s = s + frac(e) * frac(ETA[c]) * frac(ETA[d]) * F[c][d]
            out[a][b] = s / g.QI(2)
    return out


def form_of(a, b):
    F = [[g.QI(0)] * 4 for _ in range(4)]
    F[a][b], F[b][a] = g.QI(1), g.QI(-1)
    return F


ok = True
for (a, b) in [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]:
    F = form_of(a, b)
    ok = ok and m4eq(star_form(star_form(F)), m4lin((g.QI(-1), F)))
g.check("lem:star: the Lorentzian Hodge star satisfies *^2 = -1 on all six "
      "basis 2-forms", ok)

B_FORMS = [form_of(0, i) for i in (1, 2, 3)]
R_FORMS = [form_of(2, 3), form_of(3, 1), form_of(1, 2)]
ok = True
sgn = None
for i in range(3):
    sB = star_form(B_FORMS[i])
    # expect *B_i = s * R_i with one global sign s, and *R_i = -s * B_i
    matched = False
    for s in (g.QI(1), g.QI(-1)):
        if m4eq(sB, m4lin((s, R_FORMS[i]))):
            matched = True
            if sgn is None:
                sgn = s
            ok = ok and (s == sgn)
            break
    ok = ok and matched
    if sgn is not None:
        ok = ok and m4eq(star_form(R_FORMS[i]),
                         m4lin((g.QI(-1) * sgn, B_FORMS[i])))
# eigenvector check on the A± combinations at the form level
okpm = True
for i in range(3):
    Fp = m4lin((Fraction(1, 2), R_FORMS[i]), (g.QI(0, Fraction(1, 2)), B_FORMS[i]))
    Fm = m4lin((Fraction(1, 2), R_FORMS[i]), (g.QI(0, Fraction(-1, 2)), B_FORMS[i]))
    sFp, sFm = star_form(Fp), star_form(Fm)
    lp = None
    for lam in (g.QI_I, g.QI(0, -1)):
        if m4eq(sFp, m4lin((lam, Fp))):
            lp = lam
    lm = None
    for lam in (g.QI_I, g.QI(0, -1)):
        if m4eq(sFm, m4lin((lam, Fm))):
            lm = lam
    okpm = okpm and lp is not None and lm is not None and lp == g.QI(0) - lm
g.check("lem:star/prop:blind: *B_i is proportional to R_i with one global "
      "sign, and A1 = (R + iB)/2, A2 = (R - iB)/2 (the paper's A^(1), A^(2)) "
      "are *-eigenvectors with "
      "conjugate eigenvalues -i, +i (A1 spans g^-, A2 spans g^+; conjugation "
      "swaps the halves)", ok and okpm)

# ---------------------------------------------------------------------------
# Part H: reality (prop:reality), the summand composite (prop:localtwistor(3)),
# and the chiral planes (lem:homone)
# ---------------------------------------------------------------------------
# Real orthonormal basis of V = R^{2,4} in w-coordinates (w1,w2,w3,w1',w2',w3'):
# a1 = w1/2 + w1', b1 = w1/2 - w1' (and a2, b2 likewise), b3 = w3/2 - w3',
# b4 = -i (w3/2 + w3'); equivalently w1 = a1 + b1, w1' = (a1 - b1)/2,
# w3 = b3 + i b4, w3' = -(b3 - i b4)/2.  The real Witt pair is (w1, w1').

HALF = g.QI(Fraction(1, 2))
REAL_NAMES = ["a1", "a2", "b1", "b2", "b3", "b4"]
REAL = [[HALF, 0, 0, 1, 0, 0],
        [0, HALF, 0, 0, 1, 0],
        [HALF, 0, 0, -1, 0, 0],
        [0, HALF, 0, 0, -1, 0],
        [0, 0, HALF, 0, 0, -1],
        [0, 0, g.QI(0, Fraction(-1, 2)), 0, 0, g.QI(0, -1)]]
REAL = [[frac(x) for x in v] for v in REAL]
ETA6 = [1, 1, -1, -1, -1, -1]
ok = all(ip6(REAL[i], REAL[j]) == frac(ETA6[i] if i == j else 0)
         for i in range(6) for j in range(6))
ok = ok and vadd(REAL[0], REAL[2]) == basis6(0) \
    and vadd(REAL[4], vscal(I, REAL[5])) == basis6(2)
g.check("thm:purespinor/prop:reality: a1,a2,b1,..,b4 is an orthonormal basis of "
      "signature (2,4) with w1 = a1 + b1 and w3 = b3 + i b4", ok)

RMAT = [[REAL[k][r] for k in range(6)] for r in range(6)]   # columns = real vectors


def real_coords(v):
    return g.field_solve([row[:] for row in RMAT], [frac(x) for x in v])


def tau(v):
    """The real structure of V: conjugate the coordinates in the real basis."""
    c = [x.conj() for x in real_coords(v)]
    return [sum((RMAT[r][k] * c[k] for k in range(6)), g.QI(0)) for r in range(6)]


def is_real6(v):
    return all(x.im == 0 for x in real_coords(v))


ok = (tau(basis6(0)) == basis6(0) and tau(basis6(3)) == basis6(3)
      and tau(basis6(2)) == vscal(-2, basis6(5))
      and tau(basis6(5)) == vscal(Fraction(-1, 2), basis6(2)))
g.check("prop:reality: the conjugation fixes the Witt pair w1, w1' and sends "
      "w3 -> -2 w3', w3' -> -w3/2 (the reflection in b4 composed with "
      "coordinate conjugation)", ok)

# kappa := Gamma C(b4) J with Gamma the parity operator and J coordinate
# conjugation in the monomial basis; kappa(x) = KMAT . conj(x).
GAMMA = zeros(8, 8)
for m in range(8):
    GAMMA[m][m] = g.QI(-1) if popcount(m) % 2 else g.QI(1)
KMAT = mmul(GAMMA, C_of(REAL[5]))


def conj8(x):
    return [xi.conj() for xi in x]


def kappa(x):
    return apply_op(KMAT, conj8(x))


ok = True
for k in range(6):
    for v in (basis6(k), vscal(I, basis6(k))):
        for S in range(8):
            lhs = kappa(apply_op(C_of(v), e8(S)))
            rhs = apply_op(C_of(tau(v)), kappa(e8(S)))
            ok = ok and lhs == rhs
g.check("prop:reality(1): kappa C(v) = C(vbar) kappa on every basis state, for "
      "the six basis vectors and their i-multiples (antilinear intertwiner)", ok)

ok = all(kappa(kappa(e8(S))) == [x * g.QI(Fraction(-1, 2)) for x in e8(S)]
         for S in range(8))
okp = all(all(not kappa(e8(S))[T] for T in range(8)
              if popcount(T) % 2 == popcount(S) % 2) for S in range(8))
g.check("prop:reality(1): kappa^2 = -1/2 (the C-normalised -1 of the paper; "
      "negative: a quaternionic structure) and kappa swaps the chirality halves",
      ok and okp)

# B(kappa x, kappa y) = conj(lambda) conj(B(x,y)) ... determine lambda from
# conj B(kappa x, kappa y) = lambda B(x, y)
lam = None
ok = True
for S in range(8):
    for T in range(8):
        lhs = B_pair(kappa(e8(S)), kappa(e8(T))).conj()
        b = B_mono(S, T)
        if b:
            l0 = lhs / b
            if lam is None:
                lam = l0
            ok = ok and l0 == lam
        else:
            ok = ok and not lhs
TWOLAM = lam * g.QI(2)
g.check("prop:reality(2): conj B(kappa x, kappa y) = lambda_0 B(x, y) on the full "
      "basis, with |2 lambda_0| = 1 (here 2 lambda_0 = %s; the paper's lambda is "
      "conj(2 lambda_0) in the C-normalisation)" % qi_str(TWOLAM),
      ok and TWOLAM * TWOLAM.conj() == ONE)

# Sigma(Z1, Z2) := B(kappa Z1, Z2) on T, in the t-basis
SIG = [[B_pair(kappa(T_VECS[i]), T_VECS[j]) for j in range(4)] for i in range(4)]
LAM = TWOLAM.conj()     # the paper's lambda = conj(lambda_0), scaled by kappa^2 = -1/2
ok = all(SIG[j][i] == LAM * SIG[i][j].conj() for i in range(4) for j in range(4))
g.check("prop:reality(2): Sigma(Z2, Z1) = lambda conj Sigma(Z1, Z2) with lambda = "
      "conj(2 lambda_0): Sigma is Hermitian up to the phase lambda", ok)
MU = g.QI(0, 1) if LAM == g.QI(-1) else ONE + LAM.conj()   # mu = e^{-i theta/2}, lambda = e^{i theta}
HH = [[MU * SIG[i][j] for j in range(4)] for i in range(4)]
ok = all(HH[j][i] == HH[i][j].conj() for i in range(4) for j in range(4))
ok = ok and g.field_rank([r[:] for r in HH]) == 4
g.check("prop:reality(2): mu Sigma is Hermitian and nondegenerate for the phase "
      "mu (rescaling kappa)", ok)

ok = all(not HH[i][j] for i in (0, 1) for j in (0, 1)) and \
     all(not HH[i][j] for i in (2, 3) for j in (2, 3))
g.check("prop:reality(3): the infinity plane S_omega = span(t0,t1) and the origin "
      "plane S_pi = span(t2,t3) are both Sigma-null", ok)

# signature of the Hermitian form via its real form [[Re, -Im],[Im, Re]]
RE = [[HH[i][j].re for j in range(4)] for i in range(4)]
IM = [[HH[i][j].im for j in range(4)] for i in range(4)]
REAL8 = [[RE[i][j] for j in range(4)] + [-IM[i][j] for j in range(4)] for i in range(4)] + \
        [[IM[i][j] for j in range(4)] + [RE[i][j] for j in range(4)] for i in range(4)]
sig = g.congruence_signature(REAL8)
g.check("prop:reality(4): Sigma itself has signature (2,2) (real form (4,4,0))",
      sig[:2] == (4, 4) and sig[2] == 0)

# the general clause of prop:reality(2), tested where the two candidate relations
# differ: rescale kappa by the Gaussian-rational phase (3+4i)/5.
PH = g.QI(Fraction(3, 5), Fraction(4, 5))


def kappa2(x):
    return [PH * y for y in kappa(x)]


lam0 = None
okl = True
for S in range(8):
    for T in range(8):
        lhs = B_pair(kappa2(e8(S)), kappa2(e8(T))).conj()
        b = B_mono(S, T)
        if b:
            l0 = lhs / b
            lam0 = l0 if lam0 is None else lam0
            okl = okl and l0 == lam0
        else:
            okl = okl and not lhs
LAM2 = (lam0 * g.QI(2)).conj()
SIG2 = [[B_pair(kappa2(T_VECS[i]), T_VECS[j]) for j in range(4)] for i in range(4)]
ok_paper = all(SIG2[j][i] == LAM2 * SIG2[i][j].conj() for i in range(4) for j in range(4))
ok_old = all(SIG2[j][i] == LAM2.conj() * SIG2[i][j].conj() for i in range(4) for j in range(4))
MU2 = g.QI(0, 1) if LAM2 == g.QI(-1) else ONE + LAM2.conj()   # same guard as MU above
MU2bad = ONE + LAM2                # the conjugate prescription
H2 = [[MU2 * SIG2[i][j] for j in range(4)] for i in range(4)]
H2bad = [[MU2bad * SIG2[i][j] for j in range(4)] for i in range(4)]
herm2 = all(H2[j][i] == H2[i][j].conj() for i in range(4) for j in range(4))
herm2bad = all(H2bad[j][i] == H2bad[i][j].conj() for i in range(4) for j in range(4))
g.check("prop:reality(2), general clause: with kappa rescaled by (3+4i)/5 "
      "(lambda = %s, not 1) the paper's relation Sigma(Z2,Z1) = lambda conj "
      "Sigma(Z1,Z2) holds and the conjugate relation fails; mu = e^{-i theta/2} "
      "makes Sigma Hermitian and the conjugate phase does not" % qi_str(LAM2),
      okl and LAM2 != ONE and ok_paper and (not ok_old) and herm2 and (not herm2bad))

# invariance under the real bivectors: rho^* H + H rho = 0 on T
ok = True
for i in range(6):
    for j in range(i + 1, 6):
        el = msub(mmul(C_of(REAL[i]), C_of(REAL[j])),
                  mscal(ip6(REAL[i], REAL[j]) / g.QI(2), mident(8)))
        rho = t_block(el)
        rhostar = [[rho[j2][i2].conj() for j2 in range(4)] for i2 in range(4)]
        ok = ok and mzero(madd(mmul(rhostar, HH), mmul(HH, rho)))
g.check("prop:reality(2)/thm:core(1): all 15 real bivectors act Sigma-anti-"
      "Hermitianly on T (so(2,4) lands in su(2,2))", ok)

# real points = Sigma-null graph lines = A anti-Hermitian for the pairing
# sigma(e_i, pi_k) = Sigma(e_i, pi_k) =: S_ik


def herm_form(Z1, Z2):
    return sum((Z1[a].conj() * HH[a][b] * Z2[b] for a in range(4) for b in range(4)),
               g.QI(0))


SPAIR = [[herm_form(E, P) for P in (PI1, PI2)] for E in (E1, E2)]
SPINV = [g.field_solve([r[:] for r in SPAIR], [ONE if r == j else ZERO for r in range(2)])
         for j in range(2)]
SPINV = [[SPINV[j][i] for j in range(2)] for i in range(2)]   # S^{-1}


def A_from_form(hm):
    """A with A^* S = hm, i.e. the graph line has sesquilinear form hm on S_pi."""
    M = [[sum((hm[i][k] * SPINV[k][j] for k in range(2)), g.QI(0)) for j in range(2)]
         for i in range(2)]
    return [[M[j][i].conj() for j in range(2)] for i in range(2)]   # (hm S^-1)^*


PAULI = [[[ONE, ZERO], [ZERO, ONE]], [[ZERO, ONE], [ONE, ZERO]],
         [[ZERO, g.QI(0, -1)], [g.QI(0, 1), ZERO]], [[ONE, ZERO], [ZERO, -ONE]]]


def graph_is_null(A):
    U1 = vadd4(PI1, [A[0][0] * E1[k] + A[1][0] * E2[k] for k in range(4)])
    U2 = vadd4(PI2, [A[0][1] * E1[k] + A[1][1] * E2[k] for k in range(4)])
    return all(not herm_form(x, y) for x in (U1, U2) for y in (U1, U2))


def m_of(A):
    return psi_inv(msub(msub(P_of(A), N0), mscal(det2(A), NINF)))


ok_anti = True
ok_herm = True
mreal = []
for hm in PAULI:
    A_anti = A_from_form([[g.QI(0, 1) * hm[i][j] for j in range(2)] for i in range(2)])
    A_herm = A_from_form(hm)
    ok_anti = ok_anti and graph_is_null(A_anti) and is_real6(m_of(A_anti))
    ok_herm = ok_herm and (not graph_is_null(A_herm)) and (not is_real6(m_of(A_herm)))
    mreal.append([x.re for x in real_coords(m_of(A_anti))])
g.check("prop:reality(5): for A = i xhat with xhat sigma-Hermitian (four Pauli "
      "samples) the graph line is Sigma-null and m(A) is a REAL vector; for "
      "A = xhat Hermitian it is neither", ok_anti and ok_herm)
g.check("prop:reality(5): the four real vectors m(i xhat_k), xhat_k the Pauli "
      "samples, span the real "
      "Minkowski complement (rank 4): the real chart is exactly the "
      "anti-Hermitian A", g.field_rank([[frac(x) for x in row] for row in mreal]) == 4
      and all(row[0] == 0 and row[2] == 0 for row in mreal))

# the summand composite (prop:localtwistor(3)): on S_omega,
# sigma_a tau_c = -(1/4) c(u)c(e)c(X)c(p) = -C(u)C(e)C(X)C(p) equals (1/2)c(e)c(p) = C(e)C(p)
Cu, CX = C_of(basis6(3)), C_of(basis6(0))
ok = True
for e in (1, 2, 4, 5):
    for p in (1, 2, 4, 5):
        lhs = mscal(-1, mmul(mmul(Cu, C_of(basis6(e))), mmul(CX, C_of(basis6(p)))))
        rhs = mmul(C_of(basis6(e)), C_of(basis6(p)))
        for x in (e8(0), e8(6)):
            ok = ok and apply_op(lhs, x) == apply_op(rhs, x)
g.check("prop:localtwistor(3): the summand composite (soldering after Schouten) "
      "equals (1/2) c(e_a) c(P e_c) on S_omega for all 16 pairs of mixed "
      "directions (the invariant product of the two summand constants)", ok)

# lem:homone: the chiral planes.  Minkowski complement of the Witt pair:
# e0 = a2, e1 = b2, e2 = b3, e3 = b4 (signature (1,3)).
MINK = [REAL[1], REAL[3], REAL[4], REAL[5]]


def spin_vec(a, b):
    el = mmul(C_of(a), C_of(b))
    return msub(el, mscal(ip6(a, b) / g.QI(2), mident(8)))


BOOST = [t_block(spin_vec(MINK[0], MINK[i])) for i in (1, 2, 3)]
ROT = [t_block(spin_vec(MINK[j], MINK[k])) for (j, k) in ((2, 3), (3, 1), (1, 2))]
APLUS = [madd(mscal(HALF, ROT[i]), mscal(g.QI(0, Fraction(1, 2)), BOOST[i])) for i in range(3)]
AMINUS = [madd(mscal(HALF, ROT[i]), mscal(g.QI(0, Fraction(-1, 2)), BOOST[i])) for i in range(3)]


def kills(rho, cols):
    return all(not rho[r][c] for r in range(4) for c in cols)


OMEGA, PI = (0, 1), (2, 3)
plus_kills_pi = all(kills(A, PI) for A in APLUS)
plus_kills_om = all(kills(A, OMEGA) for A in APLUS)
minus_kills_pi = all(kills(A, PI) for A in AMINUS)
minus_kills_om = all(kills(A, OMEGA) for A in AMINUS)
one_each = (plus_kills_pi != plus_kills_om) and (minus_kills_pi != minus_kills_om) \
    and (plus_kills_pi != minus_kills_pi)
faithful = g.field_rank([[A[i][j] for i in range(4) for j in range(4)] for A in APLUS]) == 3 \
    and g.field_rank([[A[i][j] for i in range(4) for j in range(4)] for A in AMINUS]) == 3
g.check("lem:homone(1): each chirality factor annihilates exactly one of S_omega, S_pi "
      "and acts faithfully (rank 3) on the other, the two factors on different "
      "planes: the chiral halves", one_each and faithful)

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
