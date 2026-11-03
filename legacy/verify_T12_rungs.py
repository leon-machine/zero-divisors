#!/usr/bin/env python3
"""
verify_T12_rungs.py: exact-arithmetic verification of the computational
identities of "Two Rungs Up: The Composite as a Spinor of the Transported
Algebra, and What That Would Decide" (companion note to Transport Papers T12).

Imports the series' shared library GA.py.  Exact rationals, Gaussian
rationals (as integer real and imaginary parts), and GA.py's basis-blade
Clifford engine; no floating point anywhere (numpy is used only as an
int64 container for exact integer matrix arithmetic; every entry that
arises is a small integer).  Statement tags refer to the compiled note.
v1.2 (2026-09-03): tags swept (prop:equiv, cor:onerung, prop:outside,
sec:fallback(iv)); 17 checks, unchanged.  v1.1 (2026-09-03): 17 checks.  v1.0 had 12, five of them tautological
(the same formula evaluated twice); those are replaced here by an explicit
Fock representation on which the note's claims are computed.  All ranks
are computed by GA.mat_rank on Fraction entries (exact).
"""

from fractions import Fraction as F
from itertools import combinations
from math import comb

import numpy as np

import GA as g

# ---------------------------------------------------------------------------
# 0. exact complex integer matrices: pairs (re, im) of int64 arrays
# ---------------------------------------------------------------------------

def cm(re, im=None):
    re = np.array(re, dtype=np.int64)
    im = np.zeros_like(re) if im is None else np.array(im, dtype=np.int64)
    return (re, im)


def cmul(A, B):
    return (A[0] @ B[0] - A[1] @ B[1], A[0] @ B[1] + A[1] @ B[0])


def cadd(A, B):
    return (A[0] + B[0], A[1] + B[1])


def csub(A, B):
    return (A[0] - B[0], A[1] - B[1])


def cscal(re, im, A):
    return (re * A[0] - im * A[1], re * A[1] + im * A[0])


def cdag(A):
    return (A[0].T.copy(), -A[1].T.copy())


def czero(A):
    return not A[0].any() and not A[1].any()


def ceq(A, B):
    return czero(csub(A, B))


def comm(A, B):
    return csub(cmul(A, B), cmul(B, A))


def anti(A, B):
    return cadd(cmul(A, B), cmul(B, A))


def flat(A):
    """Row of Fractions: real parts then imaginary parts (exact rank input)."""
    return [F(int(x)) for x in A[0].ravel()] + [F(int(x)) for x in A[1].ravel()]


def crank(mats):
    return g.mat_rank([flat(A) for A in mats])


# ---------------------------------------------------------------------------
# 1. the five-mode Fock representation (Jordan-Wigner), modes 0,1 = rungs
#    (slots), modes 2,3,4 = pairs of W.  Basis state index b has bit i set
#    when mode i is occupied.  a_i lowers bit i with the Jordan-Wigner sign.
# ---------------------------------------------------------------------------
NM = 5
DIM = 2 ** NM
ID = cm(np.eye(DIM, dtype=np.int64))
ZERO = cm(np.zeros((DIM, DIM), dtype=np.int64))


def annih(i):
    M = np.zeros((DIM, DIM), dtype=np.int64)
    for b in range(DIM):
        if b >> i & 1:
            sign = (-1) ** bin(b & ((1 << i) - 1)).count("1")
            M[b ^ (1 << i), b] = sign
    return cm(M)


a = [annih(i) for i in range(NM)]
ad = [cdag(a[i]) for i in range(NM)]


def occ(b):
    return [(b >> i) & 1 for i in range(NM)]


def jk(b):
    o = occ(b)
    return o[0] + o[1], o[2] + o[3] + o[4]


ok = all(ceq(anti(a[i], ad[j]), ID if i == j else ZERO) for i in range(NM) for j in range(NM))
ok = ok and all(czero(anti(a[i], a[j])) for i in range(NM) for j in range(NM))
# vacuum: the unique state killed by every a_i; the creation monomials give 32
vac = np.zeros((DIM, 1), dtype=np.int64)
vac[0, 0] = 1
stack = np.vstack([a[i][0] for i in range(NM)])
ker_dim = DIM - g.mat_rank([[F(int(x)) for x in r] for r in stack])
states = []
for k in range(NM + 1):
    for S in combinations(range(NM), k):
        v = cm(vac)
        for i in reversed(S):
            v = cmul(ad[i], v)
        states.append(v)
ok = ok and ker_dim == 1 and crank(states) == DIM
g.check("fact:fock, thm:rungs(1): the five-mode Fock representation on 32 states "
      "satisfies the canonical anticommutation relations exactly, its vacuum is "
      "the unique state annihilated by every a_i, and the creation monomials on "
      "the vacuum span all 32 dimensions (an irreducible module)", ok)

# chirality = parity of j + k: Gamma = prod (1 - 2 a_i^dag a_i) is diagonal
# with entry (-1)^(j+k), and anticommutes with every generator
Gamma = ID
for i in range(NM):
    Gamma = cmul(Gamma, csub(ID, cscal(2, 0, cmul(ad[i], a[i]))))
diag_ok = all(Gamma[0][b, b] == (-1) ** sum(jk(b)) for b in range(DIM)) \
    and not Gamma[1].any() and not (Gamma[0] - np.diag(np.diag(Gamma[0]))).any()
g.check("thm:rungs(1): the chirality operator (-1)^N is diagonal with entry "
      "(-1)^(j+k) on the state with j rung modes and k pair modes, and "
      "anticommutes with every a_i and a_i^dag",
      diag_ok and all(czero(anti(Gamma, X)) for X in a + ad))

# bigraded dimensions and the even half
dims = {(j, k): comb(2, j) * comb(3, k) for j in range(3) for k in range(4)}
counts = {}
for b in range(DIM):
    counts[jk(b)] = counts.get(jk(b), 0) + 1
g.check("thm:rungs(1): the bigraded pieces Lambda^j C^2 ox Lambda^k W, counted on "
      "the Fock basis, are C(2,j) C(3,k), total 32, even half 16, none above 6",
      counts == dims and sum(dims.values()) == 32
      and sum(d for (j, k), d in dims.items() if (j + k) % 2 == 0) == 16
      and max(dims.values()) == 6)

# ---------------------------------------------------------------------------
# 2. the Majorana generators and so(10): gamma_{2i} = a_i + a_i^dag,
#    gamma_{2i+1} = i (a_i - a_i^dag); the 45 bilinears gamma_a gamma_b, a < b
# ---------------------------------------------------------------------------
gam = []
for i in range(NM):
    gam.append(cadd(a[i], ad[i]))
    gam.append(cscal(0, 1, csub(a[i], ad[i])))
cliff_ok = all(ceq(anti(gam[p], gam[q]), cscal(2, 0, ID) if p == q else ZERO)
               for p in range(2 * NM) for q in range(2 * NM))
pairs = list(combinations(range(2 * NM), 2))
L = {(p, q): cmul(gam[p], gam[q]) for p, q in pairs}
g.check("thm:rungs(3): the ten Majorana generators of the five modes satisfy "
      "gamma_p gamma_q + gamma_q gamma_p = 2 delta_pq exactly, and the 45 "
      "bilinears gamma_p gamma_q (p < q) are linearly independent",
      cliff_ok and crank([L[pq] for pq in pairs]) == 45)


def Lg(p, q):
    if p == q:
        return ZERO
    return L[(p, q)] if p < q else cscal(-1, 0, L[(q, p)])


# closure: [g_a g_b, g_c g_d] = 2 (d_bc g_a g_d - d_ac g_b g_d - d_bd g_a g_c + d_ad g_b g_c)
def d(x, y):
    return 1 if x == y else 0


clos_ok = True
for (p, q) in pairs:
    for (r, s) in pairs:
        lhs = comm(L[(p, q)], L[(r, s)])
        rhs = cadd(cadd(cscal(2 * d(q, r), 0, Lg(p, s)), cscal(-2 * d(p, r), 0, Lg(q, s))),
                   cadd(cscal(-2 * d(q, s), 0, Lg(p, r)), cscal(2 * d(p, s), 0, Lg(q, r))))
        clos_ok = clos_ok and ceq(lhs, rhs)
g.check("thm:rungs(3): the 45 bilinears close under the commutator with the "
      "so(10) bracket [g_a g_b, g_c g_d] = 2(d_bc g_a g_d - d_ac g_b g_d - "
      "d_bd g_a g_c + d_ad g_b g_c), verified on all 45 x 45 pairs, and every "
      "one commutes with the chirality operator: Spin(10) preserves the halves",
      clos_ok and all(czero(comm(L[pq], Gamma)) for pq in pairs))

# ---------------------------------------------------------------------------
# 3. u(2) + u(3) inside so(10), and the counts 45 - 13 = 32 = 12 + 20
# ---------------------------------------------------------------------------
Nr = cadd(cmul(ad[0], a[0]), cmul(ad[1], a[1]))
Np = cadd(cadd(cmul(ad[2], a[2]), cmul(ad[3], a[3])), cmul(ad[4], a[4]))
N = cadd(Nr, Np)


def in_span(X, basis):
    return crank(basis + [X]) == len(basis)


allL = [L[pq] for pq in pairs]
# number-preserving elements a_i^dag a_j - a_j^dag a_i, i(a_i^dag a_j + a_j^dag a_i)
# for i < j, and a_i^dag a_i - 1/2 = -(i/2) gamma_{2i} gamma_{2i+1}
num_pres = []
for i in range(NM):
    X = cscal(0, 1, csub(cscal(2, 0, cmul(ad[i], a[i])), ID))   # i(2 a^dag a - 1) = g g
    num_pres.append(X)
for i, j in combinations(range(NM), 2):
    E, Ed = cmul(ad[i], a[j]), cmul(ad[j], a[i])
    num_pres.append(csub(E, Ed))
    num_pres.append(cscal(0, 1, cadd(E, Ed)))
split_pres = [X for X in num_pres if czero(comm(X, Nr)) and czero(comm(X, Np))]
# the subspace of span(L) commuting with N_r and N_p: kernel of X -> ([X,N_r],[X,N_p])
img_rows = [flat(comm(X, Nr)) + flat(comm(X, Np)) for X in allL]
kernel_dim_split = 45 - g.mat_rank(img_rows)
img_rows_N = [flat(comm(X, N)) for X in allL]
kernel_dim_num = 45 - g.mat_rank(img_rows_N)
ok = all(in_span(X, allL) for X in num_pres)
ok = ok and len(num_pres) == 25 and crank(num_pres) == 25 and kernel_dim_num == 25
ok = ok and len(split_pres) == 13 and crank(split_pres) == 13 and kernel_dim_split == 13
g.check("thm:rungs(2),(3) and sec:fallback(iv), prop:outside: inside the 45 the elements "
      "commuting with the total number operator form exactly u(5) (dimension "
      "25, spanned by the a_i^dag a_j bilinears), those commuting with the rung "
      "and pair numbers separately form exactly u(2) + u(3) (dimension 13); so "
      "45 - 13 = 32 generators lie outside, 25 - 13 = 12 of them in u(5) "
      "(rung-pair movers) and 20 changing the mode number by two",
      ok and 45 - 13 == 32 and 25 - 13 == 12 and 45 - 25 == 20)

# ---------------------------------------------------------------------------
# 4. the U(1) factor and the weight table, computed from the operator
# ---------------------------------------------------------------------------
# the centre of u(2)+u(3) is spanned by the two number operators; the
# trace-free element (trace on C^2 + C^3 = 2 x - 3 y ... = 0 for (x, y) = (3, 2))
# is 3 N_rung - 2 N_pair, T12's hypercharge generator, with eigenvalue 3j - 2k;
# the kernel generator N_rung - N_pair of the cell action has eigenvalue j - k,
# zero on the cell sector (1,1) and nonzero elsewhere: faithful on the module
centre_ok = all(czero(comm(Nr, X)) and czero(comm(Np, X)) for X in split_pres)
trace_free = [(x, y) for x in range(-3, 4) for y in range(-3, 4)
              if (x, y) != (0, 0) and 2 * x + 3 * y == 0]
Yop = csub(cscal(3, 0, Nr), cscal(2, 0, Np))
Kop = csub(Nr, Np)
weight_ok = not Yop[1].any() and not (Yop[0] - np.diag(np.diag(Yop[0]))).any() \
    and all(Yop[0][b, b] == 3 * jk(b)[0] - 2 * jk(b)[1] for b in range(DIM))
K_ok = all(Kop[0][b, b] == jk(b)[0] - jk(b)[1] for b in range(DIM)) \
    and all(Kop[0][b, b] == 0 for b in range(DIM) if jk(b) == (1, 1)) \
    and any(Kop[0][b, b] != 0 for b in range(DIM))
g.check("prop:equiv, thm:rungs(3): the number operators span the centre of "
      "u(2)+u(3) on the module; the trace-free combinations 2x + 3y = 0 in "
      "[-3, 3]^2 are exactly the multiples of (3, -2), so 3 N_rung - 2 N_pair "
      "is T12's hypercharge generator, with eigenvalue 3j - 2k on every state; "
      "and K's generator N_rung - N_pair has eigenvalue j - k, zero on the cell "
      "sector (1,1) and nonzero elsewhere: K acts faithfully on the module",
      centre_ok and trace_free == [(-3, 2), (3, -2)] and weight_ok and K_ok)

# ---------------------------------------------------------------------------
# 5. the su(2) and su(3) content of the sectors via the quadratic Casimir
#    C = sum_ij E_ij E_ji - N^2/n on the mode set, which on Lambda^k C^n
#    is the scalar k (n - k) (n + 1) / n
# ---------------------------------------------------------------------------

def casimir(modes):
    n = len(modes)
    C = ZERO
    for i in modes:
        for j in modes:
            C = cadd(C, cmul(cmul(ad[i], a[j]), cmul(ad[j], a[i])))
    Nm = ZERO
    for i in modes:
        Nm = cadd(Nm, cmul(ad[i], a[i]))
    # n C - N^2 to stay in integers
    return csub(cscal(n, 0, C), cmul(Nm, Nm))


C2 = casimir([0, 1])
C3 = casimir([2, 3, 4])
cas_ok = not C2[1].any() and not C3[1].any()
cas_ok = cas_ok and not (C2[0] - np.diag(np.diag(C2[0]))).any() \
    and not (C3[0] - np.diag(np.diag(C3[0]))).any()
for b in range(DIM):
    j, k = jk(b)
    cas_ok = cas_ok and C2[0][b, b] == j * (2 - j) * 3 and C3[0][b, b] == k * (3 - k) * 4
# weights of the pair torus on the (0,2) piece are e_i + e_j: the 3bar (x det)
w02 = sorted(tuple(occ(b)[2:]) for b in range(DIM) if jk(b) == (0, 2))
w01 = sorted(tuple(occ(b)[2:]) for b in range(DIM) if jk(b) == (0, 1))
g.check("prop:config, fact:sixteen: the su(2) and su(3) Casimirs computed on the "
      "Fock module are the scalars j(2-j)3/2 and k(3-k)4/3 on the (j,k) piece: "
      "the j = 1 row is a doublet, the k = 1, 2 columns are triplets, and the "
      "(0,2) weights are the pair sums e_i + e_j, the 3bar; so the sector (1,0) "
      "+ (1,2), which is C^2 ox T, is (2,1)_{1/2} + (2,3bar)_{-1/6}",
      cas_ok and w02 == [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
      and w01 == [(0, 0, 1), (0, 1, 0), (1, 0, 0)]
      and dims[(1, 0)] + dims[(1, 2)] == 8
      and F(3 * 1 - 2 * 0, 6) == F(1, 2) and F(3 * 1 - 2 * 2, 6) == F(-1, 6))

# ---------------------------------------------------------------------------
# 6. thm:rungs(3), n = 3: u(3)+u(3) on C^3 ox C^3 acts with rank 17, and the
#    trace-free subalgebra (dimension 17, containing the kernel) with rank 16;
#    contrast n = 2: s(u(2)+u(3)) acts with full rank 12
# ---------------------------------------------------------------------------

def u_basis(n):
    """Real basis of u(n) as (re, im) pairs of n x n integer matrices."""
    out = []
    for i in range(n):
        Z = np.zeros((n, n), dtype=np.int64)
        Z[i, i] = 1
        out.append((np.zeros((n, n), dtype=np.int64), Z))          # i E_ii
    for i, j in combinations(range(n), 2):
        R = np.zeros((n, n), dtype=np.int64)
        R[i, j], R[j, i] = 1, -1
        out.append((R, np.zeros((n, n), dtype=np.int64)))          # E_ij - E_ji
        I_ = np.zeros((n, n), dtype=np.int64)
        I_[i, j], I_[j, i] = 1, 1
        out.append((np.zeros((n, n), dtype=np.int64), I_))         # i(E_ij + E_ji)
    return out


def cell_action(X, Xp, m, n):
    """X ox 1 + 1 ox X' on C^m ox C^n as an (re, im) pair of mn x mn matrices."""
    Im, In = np.eye(m, dtype=np.int64), np.eye(n, dtype=np.int64)
    re = np.kron(X[0], In) + np.kron(Im, Xp[0])
    im = np.kron(X[1], In) + np.kron(Im, Xp[1])
    return (re, im)


def trace_im(X):
    return int(np.trace(X[1]))


def rank_of_action(m, n, trace_free):
    Zm = (np.zeros((m, m), dtype=np.int64),) * 2
    Zn = (np.zeros((n, n), dtype=np.int64),) * 2
    gens = [(X, Zn) for X in u_basis(m)] + [(Zm, Xp) for Xp in u_basis(n)]
    if trace_free:
        # replace the diagonal generators by trace-free combinations plus the
        # kernel generator (i I_m, -i I_n) when it is trace free
        diag = [(X, Xp) for X, Xp in gens if trace_im(X) + trace_im(Xp) != 0]
        offd = [(X, Xp) for X, Xp in gens if trace_im(X) + trace_im(Xp) == 0]
        new = []
        for k in range(1, len(diag)):
            X0, Xp0 = diag[0]
            Xk, Xpk = diag[k]
            t0, tk = trace_im(X0) + trace_im(Xp0), trace_im(Xk) + trace_im(Xpk)
            new.append(((tk * X0[0] - t0 * Xk[0], tk * X0[1] - t0 * Xk[1]),
                        (tk * Xp0[0] - t0 * Xpk[0], tk * Xp0[1] - t0 * Xpk[1])))
        gens = offd + new
    acts = [cell_action(X, Xp, m, n) for X, Xp in gens]
    return len(gens), crank(acts)


n18, r17 = rank_of_action(3, 3, False)
n17, r16 = rank_of_action(3, 3, True)
n13, r12 = rank_of_action(2, 3, False)
n12, r12b = rank_of_action(2, 3, True)
kern33 = cell_action((np.zeros((3, 3), dtype=np.int64), np.eye(3, dtype=np.int64)),
                     (np.zeros((3, 3), dtype=np.int64), -np.eye(3, dtype=np.int64)), 3, 3)
g.check("thm:rungs(3), n = 3: u(3)+u(3) (18 generators) acts on C^3 ox C^3 with "
      "rank 17, the quotient by K being the seventeen; the trace-free subalgebra "
      "(17 generators) contains K's generator (i I_3, -i I_3), which acts as zero, "
      "and so acts with rank 16 only; at n = 2, u(2)+u(3) (13) acts with rank 12 "
      "and the trace-free s(u(2)+u(3)) (12) with full rank 12",
      (n18, r17) == (18, 17) and (n17, r16) == (17, 16) and czero(kern33)
      and (n13, r12) == (13, 12) and (n12, r12b) == (12, 12))

# ---------------------------------------------------------------------------
# 7. lem:bracket: the volume identities and the slot trace
# ---------------------------------------------------------------------------

def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    tot = F(0)
    for c in range(n):
        minor = [row[:c] + row[c + 1:] for row in M[1:]]
        tot += (-1) ** c * M[0][c] * det(minor)
    return tot


def eps4(vs):
    """Coefficient of e1^e2^pi1^pi2 in v1^v2^v3^v4 (T = S_omega + S_pi with
    basis e1, e2, pi1, pi2 in that order)."""
    return det(vs)


e1 = [F(1), F(0), F(0), F(0)]
e2 = [F(0), F(1), F(0), F(0)]
p1 = [F(0), F(0), F(1), F(0)]
p2 = [F(0), F(0), F(0), F(1)]
ok = True
for Z1, Z2 in (([F(2), F(-1), F(3), F(5)], [F(1), F(4), F(-2), F(7)]),
               ([F(1, 2), F(3), F(-1), F(2, 3)], [F(5), F(-2), F(4), F(1)]),
               ([F(0), F(1), F(1), F(0)], [F(1), F(0), F(0), F(1)])):
    pipi = Z1[2] * Z2[3] - Z1[3] * Z2[2]
    ww = Z1[0] * Z2[1] - Z1[1] * Z2[0]
    ok = ok and eps4([e1, e2, Z1, Z2]) == pipi and eps4([p1, p2, Z1, Z2]) == ww
g.check("lem:bracket: eps(n_inf ^ Z1 ^ Z2) = <pi1 pi2> and eps(n_0 ^ Z1 ^ Z2) = "
      "<omega1 omega2> for n_inf = e1^e2, n_0 = pi1^pi2, on three rational "
      "instances", ok)

Z1c = [g.qi(1, 1), g.qi(2), g.qi(3, -1), g.qi(F(1, 2))]
Z2c = [g.qi(0, 2), g.qi(-1), g.qi(1, 1), g.qi(2, 3)]


def mom(Zs):
    p = [[g.qi(0)] * 2 for _ in range(2)]
    for Z in Zs:
        for A in range(2):
            for Ap in range(2):
                p[A][Ap] = p[A][Ap] + Z[2 + A] * Z[2 + Ap].conj()
    return p


Psi = {0: Z1c, 1: Z2c}
# Psi as a vector of C^2 ox T, index (i, c) -> 4 i + c; the 8 x 8 matrix
# Psi ox conj(Psi); the partial trace over the slot index i is a 4 x 4 matrix
# on T whose pi-block is the momentum
vec = [Psi[i][c] for i in (0, 1) for c in range(4)]
outer = [[vec[r] * vec[c].conj() for c in range(8)] for r in range(8)]
ptrace = [[sum((outer[4 * i + x][4 * i + y] for i in (0, 1)), g.qi(0))
           for y in range(4)] for x in range(4)]
# also the sum over slots of the diagonal blocks equals the trace of the
# 8 x 8 matrix on the omega-omega and pi-pi blocks together
g.check("lem:bracket: the partial trace over the slot index of the 8 x 8 "
      "matrix Psi ox conj(Psi) on C^2 ox T is a 4 x 4 matrix on T whose "
      "pi-block is the total momentum sum_i pi^i conj(pi^i), and whose trace "
      "is |Psi|^2, on a Gaussian-rational two-twistor instance",
      all(ptrace[2 + A][2 + Ap] == mom([Z1c, Z2c])[A][Ap]
          for A in range(2) for Ap in range(2))
      and sum((ptrace[x][x] for x in range(4)), g.qi(0))
      == sum((v * v.conj() for v in vec), g.qi(0)))

# ---------------------------------------------------------------------------
# 8. prop:ladderrung: the rung-mixing u(2) restricted to the (1, even) sector
#    is the ladder action.  Compute the Fock operator of X in u(2) on the
#    states v_i ox (vacuum or full pair) and compare with X acting on the
#    slot index of C^2 ox T.
# ---------------------------------------------------------------------------

def fock_op(X, modes):
    """sum_ij X_ij a_i^dag a_j over the listed modes."""
    Op = ZERO
    for r, i in enumerate(modes):
        for s, j in enumerate(modes):
            Op = cadd(Op, cscal(int(X[0][r, s]), int(X[1][r, s]), cmul(ad[i], a[j])))
    return Op


def basis_index(S):
    return sum(1 << i for i in S)


lr_ok = True
for X in u_basis(2):
    Op = fock_op(X, [0, 1])
    for pair_set in ((), (2, 3), (2, 4), (3, 4)):      # k even: 0 or 2 pairs
        for i in (0, 1):
            col = basis_index((i,) + pair_set)
            # expected: sum_j X_ji |v_j ox pairs>, sign from Jordan-Wigner is
            # trivial here because rung modes precede pair modes
            for j in (0, 1):
                row = basis_index((j,) + pair_set)
                lr_ok = lr_ok and Op[0][row, col] == X[0][j, i] and Op[1][row, col] == X[1][j, i]
            # and nothing leaves the sector
            colv = (Op[0][:, col], Op[1][:, col])
            for b in range(DIM):
                if jk(b) != (1, len(pair_set)):
                    lr_ok = lr_ok and colv[0][b] == 0 and colv[1][b] == 0
g.check("prop:ladderrung: for every basis element X of u(2) the Fock operator "
      "sum X_ij a_i^dag a_j, restricted to the states with one rung mode and an "
      "even number of pairs, is X acting on the slot index of C^2 ox T and "
      "nothing else: the rung mixing is the ladder action on that sector",
      lr_ok)

# ---------------------------------------------------------------------------
# 9. cor:onerung, fact:tower instance: in GA.py's blade engine, a null p of
#    R^{1,3} stays null in the completions Cl(2,4) and Cl(3,5) (the completion
#    does not invert it at element level), while the rungs supply 1, 2, 3
#    mutually anticommuting null pairs with v_i w_j + w_j v_i = delta_ij:
#    the Witt index rises by one per rung
# ---------------------------------------------------------------------------
ok = True
for (P_, Q_) in ((1, 3), (2, 4), (3, 5)):
    sq = g.sig(P_, Q_)
    G = [g.gen(i) for i in range(P_ + Q_)]
    # R^{1,3} = span(g0 (+), and the last three (-)); rungs use the pairs
    # (g_1, g_{P_}), (g_2, g_{P_+1}), ... of one + and one - generator each
    pos = list(range(P_))
    neg = list(range(P_, P_ + Q_))
    minus_base = neg[-3:]
    p = g.add(g.scal(F(5), G[0]), g.scal(F(3), G[minus_base[0]]), g.scal(F(4), G[minus_base[1]]))
    ok = ok and g.is_zero(g.mul(p, p, sq))
    vs, ws = [], []
    for r in range(P_ - 1):
        gp, gm = G[pos[1 + r]], G[neg[r]]
        vs.append(g.scal(F(1, 2), g.add(gp, gm)))
        ws.append(g.scal(F(1, 2), g.sub(gp, gm)))
    for i in range(P_ - 1):
        for j in range(P_ - 1):
            ok = ok and g.is_zero(g.add(g.mul(vs[i], vs[j], sq), g.mul(vs[j], vs[i], sq)))
            ok = ok and g.is_zero(g.add(g.mul(ws[i], ws[j], sq), g.mul(ws[j], ws[i], sq)))
            ok = ok and g.eq(g.add(g.mul(vs[i], ws[j], sq), g.mul(ws[j], vs[i], sq)),
                             g.sc(F(1 if i == j else 0)))
        # p is orthogonal to the rung pairs
        ok = ok and g.is_zero(g.add(g.mul(p, vs[i], sq), g.mul(vs[i], p, sq)))
g.check("cor:onerung and fact:tower (instance): in Cl(1,3), Cl(2,4) and Cl(3,5) "
      "the null momentum p = 5 g_0 + 3 g_a + 4 g_b stays null (p^2 = 0: the "
      "rung is an isometric extension and inverts nothing as an element), and "
      "the rungs supply 0, 1, 2 mutually anticommuting null pairs with "
      "v_i w_j + w_j v_i = delta_ij, orthogonal to p, one more per rung",
      ok)

# ---------------------------------------------------------------------------
# 10. prop:bivector: Z1 ^ Z2 is null under eps(P ^ P); all pairwise bivectors
#     of an n-tuple lie in one V_C; the one-rung module has a one-dimensional
#     rung-mode space
# ---------------------------------------------------------------------------

def wedge2(Z1, Z2):
    return {(x, y): Z1[x] * Z2[y] - Z1[y] * Z2[x] for x, y in combinations(range(4), 2)}


def eps_PP(P):
    return 2 * (P[(0, 1)] * P[(2, 3)] - P[(0, 2)] * P[(1, 3)] + P[(0, 3)] * P[(1, 2)])


Zs = [[F(2), F(-1), F(3), F(5)], [F(1), F(4), F(-2), F(7)],
      [F(1), F(0), F(0), F(1)], [F(0), F(1), F(1), F(0)]]
pair_null = all(eps_PP(wedge2(Zs[i], Zs[j])) == 0 for i, j in combinations(range(4), 2))
PQ = {k: wedge2(Zs[0], Zs[1])[k] + wedge2(Zs[2], Zs[3])[k] for k in wedge2(Zs[0], Zs[1])}
g.check("prop:bivector: every pairwise bivector Z^i ^ Z^j of a four-twistor "
      "instance is null under eps(P ^ P) (decomposable), all in the one "
      "six-dimensional V_C, while a sum of two of them is not null",
      pair_null and eps_PP(PQ) != 0)

# ---------------------------------------------------------------------------
# 10b. prop:bivector: one rung.  Four-mode Fock space (mode 0 the rung, modes
#      1, 2, 3 the pairs of W).  The twisted ground generators omega gamma_a
#      (a >= 2, omega = gamma_0 gamma_1 the rung's volume element) generate
#      M_8(C) (their 64 blades are independent), so their commutant in M_16(C)
#      is the M_2(C) of the rung, spanned by 1, gamma_0, gamma_1, omega: the
#      rung's unitary group is U(2), but gamma_0 and gamma_1 anticommute with
#      chirality, and the chirality-preserving part span{1, omega} is abelian
# ---------------------------------------------------------------------------
NM4, DIM4 = 4, 16
ID4 = cm(np.eye(DIM4, dtype=np.int64))


def annih4(i):
    M = np.zeros((DIM4, DIM4), dtype=np.int64)
    for b in range(DIM4):
        if b >> i & 1:
            M[b ^ (1 << i), b] = (-1) ** bin(b & ((1 << i) - 1)).count("1")
    return cm(M)


a4 = [annih4(i) for i in range(NM4)]
ad4 = [cdag(x) for x in a4]
gam4 = []
for i in range(NM4):
    gam4.append(cadd(a4[i], ad4[i]))
    gam4.append(cscal(0, 1, csub(a4[i], ad4[i])))
Gamma4 = ID4
for i in range(NM4):
    Gamma4 = cmul(Gamma4, csub(ID4, cscal(2, 0, cmul(ad4[i], a4[i]))))
omega = cmul(gam4[0], gam4[1])
twisted = [cmul(omega, gam4[k]) for k in range(2, 8)]
blades = []
for k in range(7):
    for S in combinations(range(6), k):
        Bl = ID4
        for t in S:
            Bl = cmul(Bl, twisted[t])
        blades.append(Bl)
rung_alg = [ID4, gam4[0], gam4[1], omega]
# complex-linear independence: the real span of X and iX over all X
one_rung_ok = crank(blades + [cscal(0, 1, B) for B in blades]) == 128     # M_8(C)
one_rung_ok = one_rung_ok and crank(rung_alg + [cscal(0, 1, X) for X in rung_alg]) == 8
one_rung_ok = one_rung_ok and all(czero(comm(X, t)) for X in rung_alg for t in twisted)
one_rung_ok = one_rung_ok and czero(anti(gam4[0], Gamma4)) and czero(anti(gam4[1], Gamma4))
one_rung_ok = one_rung_ok and czero(comm(omega, Gamma4)) and czero(comm(omega, ID4))
# twisted generators satisfy the Clifford relations of the ground signature
# up to the overall sign omega^2 = -1: (omega g_a)(omega g_b) + (b a) = -2 delta
tw_ok = all(ceq(anti(twisted[p], twisted[q]), cscal(-2, 0, ID4) if p == q else
            (np.zeros((DIM4, DIM4), dtype=np.int64),) * 2) for p in range(6) for q in range(6))
g.check("prop:bivector: on the four-mode Fock space of one rung above the three "
      "pairs, the six twisted ground generators omega gamma_a satisfy Clifford "
      "relations and their 64 blades are independent (they generate M_8(C)), so "
      "their commutant is the rung's M_2(C) = span{1, gamma_0, gamma_1, omega}, "
      "which commutes with them and has unitary group U(2); gamma_0 and "
      "gamma_1 anticommute with chirality and the chirality-preserving part "
      "span{1, omega} is abelian: the one-rung U(2) mixes chirality",
      one_rung_ok and tw_ok)

# ---------------------------------------------------------------------------
# 11. prop:config: T ox T contains the sl(3)-weight of S^2(Lambda^2 W), the
#     six-dimensional 6bar, which occurs in no sector of the two-rung module:
#     the module's SU(3) content is only 1, 3, 3bar.  Weights are compared
#     modulo (1,1,1), i.e. as sl(3) weights, so the statement is about SU(3)
#     representations and not about the U(1) charge.
# ---------------------------------------------------------------------------

def sl3(w):
    s = F(sum(w), 3)
    return tuple(F(x) - s for x in w)


T_weights = [(0, 0, 0)] + [tuple(int(i in S) for i in range(3)) for S in combinations(range(3), 2)]
TT_weights = [tuple(x + y for x, y in zip(u, v)) for u in T_weights for v in T_weights]
mod_sl3 = set(sl3(tuple(occ(b)[2:])) for b in range(DIM))
absent = sorted(set(w for w in TT_weights if sl3(w) not in mod_sl3))
S2L2 = sorted(set(tuple(x + y for x, y in zip(u, v)) for u, v in combinations(T_weights[1:], 2))
              | set(tuple(2 * x for x in u) for u in T_weights[1:]))
L2L2 = sorted(set(tuple(x + y for x, y in zip(u, v)) for u, v in combinations(T_weights[1:], 2)))
g.check("prop:config: of the 16 weights of T ox T the doubled ones 2(e_i + e_j), "
      "the highest weights of S^2(Lambda^2 W) = 6bar, are absent from the two-rung "
      "module even as sl(3) weights (its SU(3) content is 1, 3, 3bar only), while "
      "the weights of Lambda^2(Lambda^2 W), the 3, are present; and the "
      "both-rungs sector has dimension 8, one copy of S",
      len(TT_weights) == 16 and absent == [(0, 2, 2), (2, 0, 2), (2, 2, 0)]
      and len(S2L2) == 6 and all(sl3(w) in mod_sl3 for w in L2L2)
      and sum(dims[(2, k)] for k in range(4)) == 8)

# ---------------------------------------------------------------------------
# 12. thm:rungs(4): dimension counts
# ---------------------------------------------------------------------------
spin_dims = [2 ** (3 + n) for n in range(4)]
so_dims = [(6 + 2 * n) * (5 + 2 * n) // 2 for n in range(4)]
u_dims = [9 + n * n for n in range(4)]
g.check("thm:rungs(4): spinor dimensions 2^(3+n) = 8, 16, 32, 64; dim so(6+2n) = "
      "15, 28, 45, 66; dim u(3)+u(n) = 9, 10, 13, 18 for n = 0..3",
      spin_dims == [8, 16, 32, 64] and so_dims == [15, 28, 45, 66]
      and u_dims == [9, 10, 13, 18])

# ---------------------------------------------------------------------------
print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    raise SystemExit(1)
print("All checks pass.")
