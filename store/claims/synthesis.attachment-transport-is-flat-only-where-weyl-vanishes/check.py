"""Conformal spinor transport on a gravitational field: exact checks in Cl(2,4).

Generators as in the stored tractor result: e0 (square +1), e1, e2, e3 (square -1), e+ (square +1),
e- (square -1); n0 = (e+ + e-)/2, ninf = e+ - e-; Theta(A) = -ninf ^ A + n0 ^ P(A) with P the Schouten
map; the derivative-free field strength of the tractor gauge field on the plane A ^ B is
F(A ^ B) = -R(A ^ B) + Theta(A) x Theta(B) (x the commutator product).
Weyl maps: I4-linear maps on spacetime bivectors given by a complex symmetric traceless 3 x 3 matrix M
in the basis sigma_k = e_k e0 (the complex unit read as I4 = e0 e1 e2 e3), Petrov type from the minimal
polynomial of M (I0: the type I normal form with a zero eigenvalue, unique up to a Lorentz rotor
and a complex scale). The curvature is R(A ^ B) = W(A ^ B) + P(A) ^ B + A ^ P(B) with an arbitrary
symmetric P (the Weyl plus Schouten split of the store's dictionary).
Conformal spinors: the even subalgebra Cl+(2,4) (32 real dimensions, centre spanned by 1 and I6,
I6^2 = -1, so a complex algebra of dimension 16, M(4, C)) acts on itself from the left as four copies
of the conformal spinor space CS (8 real dimensions); a bivector acts on spinors by left
multiplication (spin action of the rotor flow), so the subspace of CS annihilated by a set of
bivectors has complex dimension (real kernel dimension on Cl+(2,4)) / 8.
  (1) Each sample W is a Weyl map (pair-symmetric, Ricci-traceless, first Bianchi identity) of the
      stated Petrov type (O, N, III, D, II, I by the minimal polynomial of M).
  (2) For every sample and two non-Einstein Schouten maps, F(A ^ B) = -W(A ^ B) on all six coordinate
      planes: the Schouten map drops out (the attachment's transport is blind to the Ricci curvature).
  (3) The common kernel on CS of the F(A ^ B) has complex dimension 4 (O), 2 (N), 0 (III, D, II, I);
      for type N it is the kernel of left multiplication by the repeated principal null vector
      k = e0 + e3 (and not of the other null vector m = e0 - e3).
  (4) A Cotton block n0 ^ c added to the type N curvature keeps the kernel for c along k and cuts it
      to complex dimension 1 for c = e1, e0, m (samples).
  (5) Commutant: the bivectors of Cl(2,4) commuting with every F(A ^ B) span 15 (O), 5 (N), 1 (III, D,
      II, I, I0) dimensions, the last spanned by E = e+ e-; every one of them annihilates the null vector k under the commutator product,
      whereas Z = e0 e+ annihilates only the negative-definite 4-plane spanned by e1, e2, e3, e-; so no
      element conjugate to a nonzero multiple of Z (a conformal-energy generator) commutes with a
      nonzero Weyl curvature, while Z commutes with the type O curvature.
Exact arithmetic only (Fractions and Gaussian rationals).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import QI
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
I4 = GA.mul(GA.mul(E[0], E[1], S), GA.mul(E[2], E[3], S), S)
I6 = GA.mul(I4, GA.mul(E[4], E[5], S), S)
SIG = [GA.mul(E[k], E[0], S) for k in (1, 2, 3)]
EVEN = [b for b in GA.all_blades(6) if len(b) % 2 == 0]
ODD = [b for b in GA.all_blades(6) if len(b) % 2 == 1]
BIV = [b for b in GA.all_blades(6) if len(b) == 2]
K_NULL = GA.add(E[0], E[3])
M_NULL = GA.sub(E[0], E[3])
ZB = GA.mul(E[0], E[4], S)


def _premises():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("synthesis.imported-gtg-dictionary")
    premise("field-theory.twistor-attachment")
    premise("synthesis.attachment-conformal-energy-is-generated-by-z")
    premise("field-theory.where-each-lives")


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def scalar(x):
    return x.get((), F(0))


def smap(M):
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), ER[n])
                              for n in range(4)])


def theta(A, P):
    return GA.add(GA.neg(comm(NI, A)), comm(N0, P(A)))


def cbiv(z, k):
    return GA.add(GA.scal(z.re, SIG[k]), GA.scal(z.im, GA.mul(I4, SIG[k], S)))


def weyl(M):
    """W(sigma_j) = sum_k M[k][j] sigma_k, extended I4-linearly."""
    cols = [GA.add(*[cbiv(M[k][j], k) for k in range(3)]) for j in range(3)]

    def W(B):
        out = {}
        for j in range(3):
            x = scalar(GA.mul(B, SIG[j], S))
            y = -scalar(GA.mul(B, GA.mul(I4, SIG[j], S), S))
            out = GA.add(out, GA.scal(x, cols[j]), GA.scal(y, GA.mul(I4, cols[j], S)))
        return out
    return W


def curvature(W, P):
    return lambda A, B: GA.add(W(comm(A, B)), comm(P(A), B), comm(A, P(B)))


def field_strengths(W, P):
    R = curvature(W, P)
    out = []
    for m, n in combinations(range(4), 2):
        A, B = E[m], E[n]
        out.append(GA.add(GA.neg(R(A, B)), comm(theta(A, P), theta(B, P))))
    return out


def left_rows(X, src, dst):
    cols = [GA.mul(X, {b: F(1)}, S) for b in src]
    return [[c.get(d, F(0)) for c in cols] for d in dst]


def kernel_real_dim(Xs):
    rows = []
    for X in Xs:
        if X:
            rows.extend(left_rows(X, EVEN, EVEN))
    return len(EVEN) - (GA.mat_rank(rows) if rows else 0)


def commutant_basis(Xs):
    rows = []
    for X in Xs:
        if not X:
            continue
        cols = [comm(X, {b: F(1)}) for b in BIV]
        keys = sorted(set().union(*[set(c) for c in cols]))
        rows.extend([[c.get(k, F(0)) for c in cols] for k in keys])
    n = len(BIV)
    if not rows:
        return [{b: F(1)} for b in BIV]
    A = [r[:] for r in rows]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    basis = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fc]
        basis.append({b: x for b, x in zip(BIV, v) if x != 0})
    return basis


def cm_mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), QI(0)) for j in range(3)] for i in range(3)]


def cm_add(A, B, b=1):
    return [[A[i][j] + B[i][j] * b for j in range(3)] for i in range(3)]


def cm_zero(A):
    return all(not A[i][j] for i in range(3) for j in range(3))


def cm_id(c):
    return [[QI(c) if i == j else QI(0) for j in range(3)] for i in range(3)]


Z0, O1, II = QI(0), QI(1), QI(0, 1)
V_NULL = [O1, II, Z0]
W_AX = [Z0, Z0, O1]
M_N = [[V_NULL[i] * V_NULL[j] for j in range(3)] for i in range(3)]
M_III = [[V_NULL[i] * W_AX[j] + W_AX[i] * V_NULL[j] for j in range(3)] for i in range(3)]
M_D = [[QI(2), Z0, Z0], [Z0, QI(2), Z0], [Z0, Z0, QI(-4)]]
M_II = cm_add(M_D, M_N)
M_I = [[QI(1), Z0, Z0], [Z0, QI(2, 1), Z0], [Z0, Z0, QI(-3, -1)]]
M_I0 = [[QI(1), Z0, Z0], [Z0, QI(-1), Z0], [Z0, Z0, Z0]]
M_O = [[Z0] * 3 for _ in range(3)]
TYPES = [("O", M_O), ("N", M_N), ("III", M_III), ("D", M_D), ("II", M_II), ("I", M_I), ("I0", M_I0)]
EXPECTED_CS_DIM = {"O": 4, "N": 2, "III": 0, "D": 0, "II": 0, "I": 0, "I0": 0}
EXPECTED_COMMUTANT = {"O": 15, "N": 5, "III": 1, "D": 1, "II": 1, "I": 1, "I0": 1}
SCH1 = [[2, 1, 0, -3], [1, -1, 4, 0], [0, 4, 5, 2], [-3, 0, 2, 7]]
SCH2 = [[F(1, 3), 0, 1, 0], [0, F(-5, 2), 0, 1], [1, 0, 2, 0], [0, 1, 0, F(1, 4)]]


def petrov_type(M):
    """Type from the minimal polynomial of a traceless complex symmetric 3 x 3 matrix: O (M = 0),
    N (M^2 = 0), III (M^3 = 0), else a repeated eigenvalue iff tr(M^2)^3 = 6 tr(M^3)^2, with
    lambda = -tr(M^3)/tr(M^2); D if (M - lambda)(M + 2 lambda) = 0, II otherwise, I if no repeat."""
    if cm_zero(M):
        return "O"
    M2 = cm_mul(M, M)
    if cm_zero(M2):
        return "N"
    if cm_zero(cm_mul(M2, M)):
        return "III"
    M3 = cm_mul(M2, M)
    t2 = M2[0][0] + M2[1][1] + M2[2][2]
    t3 = M3[0][0] + M3[1][1] + M3[2][2]
    if t2 * t2 * t2 != t3 * t3 * 6:
        return "I"
    lam = -(t3 / t2)
    if cm_zero(cm_mul(cm_add(M, cm_id(lam), -1), cm_add(M, cm_id(lam * -2), -1))):
        return "D"
    return "II"


def check_samples_are_weyl_maps_of_each_petrov_type():
    _premises()
    for name, M in TYPES:
        GA.check("M symmetric and traceless (%s)" % name,
                 all(M[i][j] == M[j][i] for i in range(3) for j in range(3))
                 and not (M[0][0] + M[1][1] + M[2][2]))
        GA.check("Petrov type %s from the minimal polynomial" % name, petrov_type(M) == name.rstrip("0"))
        W = weyl(M)
        planes = [comm(E[m], E[n]) for m, n in combinations(range(4), 2)]
        GA.check("pair symmetry <W(B1) B2> = <B1 W(B2)> (%s)" % name,
                 all(scalar(GA.mul(W(B1), B2, S)) == scalar(GA.mul(B1, W(B2), S))
                     for B1 in planes for B2 in planes))
        for b in range(4):
            ric = GA.add(*[comm(ER[m], W(comm(E[m], E[b]))) for m in range(4)])
            ric1 = {k: c for k, c in ric.items() if len(k) == 1}
            bianchi = GA.add(*[GA.mul(ER[m], W(comm(E[m], E[b])), S) for m in range(4)])
            bianchi3 = {k: c for k, c in bianchi.items() if len(k) == 3}
            GA.check("Ricci trace of W vanishes (%s, e%d)" % (name, b), GA.is_zero(ric1))
            GA.check("first Bianchi identity (%s, e%d)" % (name, b), GA.is_zero(bianchi3))
        GA.check("W is I4-linear (%s)" % name,
                 all(GA.eq(W(GA.mul(I4, B, S)), GA.mul(I4, W(B), S)) for B in planes))
    GA.check("type N sample is nonzero", not GA.is_zero(weyl(M_N)(SIG[0])))


def check_schouten_drops_out_of_the_field_strength():
    _premises()
    for name, M in TYPES:
        W = weyl(M)
        for sch in (SCH1, SCH2):
            Fs = field_strengths(W, smap(sch))
            planes = [comm(E[m], E[n]) for m, n in combinations(range(4), 2)]
            GA.check("F(A ^ B) = -W(A ^ B) for every plane (%s)" % name,
                     all(GA.eq(Fx, GA.neg(W(Bp))) for Fx, Bp in zip(Fs, planes)))
    ric1 = GA.add(comm(smap(SCH1)(E[0]), E[1]), comm(E[0], smap(SCH1)(E[1])))
    ric2 = GA.add(comm(smap(SCH2)(E[0]), E[1]), comm(E[0], smap(SCH2)(E[1])))
    GA.check("tabulated: the Schouten part of R(e0 ^ e1) is nonzero and not a multiple of e0 ^ e1 (SCH1)",
             ric1 == {(0, 1): F(3), (1, 3): F(-3), (0, 2): F(-4)})
    GA.check("tabulated: the Schouten part of R(e0 ^ e1) (SCH2)",
             ric2 == {(0, 1): F(17, 6), (1, 2): F(1), (0, 3): F(-1)})
    table = {"O": {}, "N": {(0, 1): F(-1), (1, 3): F(1)}, "III": {(0, 3): F(-1)}, "D": {(0, 1): F(-2)},
             "II": {(0, 1): F(-3), (1, 3): F(1)}, "I": {(0, 1): F(-1)}, "I0": {(0, 1): F(-1)}}
    for name, M in TYPES:
        GA.check("tabulated: F(e0 ^ e1) (%s)" % name, field_strengths(weyl(M), smap(SCH2))[0] == table[name])


def check_parallel_conformal_spinors_by_petrov_type():
    _premises()
    GA.check("I6 squares to -1", GA.eq(GA.mul(I6, I6, S), GA.sc(-1)))
    GA.check("I6 is central in the even subalgebra",
             all(GA.commutes(I6, {b: F(1)}, S) for b in EVEN))
    for name, M in TYPES:
        Fs = field_strengths(weyl(M), smap(SCH1))
        d = kernel_real_dim(Fs)
        GA.check("kernel real dimension is a multiple of 8 (%s)" % name, d % 8 == 0)
        GA.check("parallel conformal spinors: complex dimension %d (%s)" % (EXPECTED_CS_DIM[name], name),
                 d // 8 == EXPECTED_CS_DIM[name])
    FN = field_strengths(weyl(M_N), smap(SCH1))
    kn = GA.mat_rank(left_rows(K_NULL, EVEN, ODD))
    joint = GA.mat_rank(left_rows(K_NULL, EVEN, ODD) + sum([left_rows(X, EVEN, EVEN) for X in FN], []))
    GA.check("type N: k annihilates half of Cl+(2,4)", 32 - kn == 16)
    GA.check("type N: the kernel is exactly the kernel of k (repeated principal null vector)",
             32 - joint == 16 and kernel_real_dim(FN) == 16)
    jm = GA.mat_rank(left_rows(M_NULL, EVEN, ODD) + sum([left_rows(X, EVEN, EVEN) for X in FN], []))
    GA.check("type N: the other null vector m meets the kernel only in zero", 32 - jm == 0)
    GA.check("k is the repeated principal null vector: the type N curvature bivectors annihilate it",
             all(GA.is_zero(comm(X, K_NULL)) for X in FN))


def check_cotton_block_only_cuts_the_type_n_kernel():
    _premises()
    FN = field_strengths(weyl(M_N), smap(SCH2))
    cases = [(K_NULL, 2), (E[1], 1), (E[0], 1), (M_NULL, 1)]
    for c, dim in cases:
        cot = comm(N0, c)
        d = kernel_real_dim(FN + [cot])
        GA.check("type N with Cotton block n0 ^ c: complex dimension %d" % dim, d == 8 * dim)
    GA.check("a Cotton block alone keeps half: n0 ^ e1", kernel_real_dim([comm(N0, E[1])]) == 16)


def check_no_conformal_energy_generator_commutes_with_weyl():
    _premises()
    zrows = []
    for i in range(6):
        c = comm(ZB, E[i])
        zrows.append([c.get((j,), F(0)) for j in range(6)])
    kernel = [i for i in range(6) if all(zrows[i][j] == 0 for j in range(6))]
    GA.check("Z annihilates exactly e1, e2, e3, e- (rank 2 on vectors)",
             kernel == [1, 2, 3, 5] and GA.mat_rank(zrows) == 2)
    GA.check("that 4-plane is negative definite", all(S[i] == -1 for i in kernel))
    GA.check("Z^2 = -1 (elliptic)", GA.eq(GA.mul(ZB, ZB, S), GA.sc(-1)))
    for name, M in TYPES:
        Fs = field_strengths(weyl(M), smap(SCH1))
        basis = commutant_basis(Fs)
        GA.check("commutant dimension %d (%s)" % (EXPECTED_COMMUTANT[name], name),
                 len(basis) == EXPECTED_COMMUTANT[name])
        if EXPECTED_COMMUTANT[name] == 1:
            GA.check("the commutant is spanned by E = e+ e- (%s)" % name,
                     basis[0] == {(4, 5): F(1)})
        zc = all(GA.is_zero(comm(X, ZB)) for X in Fs)
        if name == "O":
            GA.check("Z commutes with the flat curvature", zc)
        else:
            GA.check("Z does not commute with the %s curvature" % name, not zc)
            GA.check("every commutant element annihilates the null vector k (%s)" % name,
                     all(GA.is_zero(comm(X, K_NULL)) for X in basis))
    GA.check("k is null", dot(K_NULL, K_NULL) == 0)
