"""singularity.bundle-maps-quantise-without-hopping: exact matrix identities on a finite truncation.

Model: three points x1, x2, x3 of E, one mode per point (the mode line bundle), Fock space by
Jordan-Wigner (8 x 8 rational matrices), psi_j the annihilators, N_j = psi_j^dag psi_j, joint number
basis |n1 n2 n3>. dGamma(a) = sum_ij a_ij psi_i^dag psi_j.
(1) For a bundle map a = diag(a_1, a_2, a_3) (all eight 0/1 diagonals and two generic ones),
    dGamma(a) = sum_j a_j N_j, it is diagonal in the joint number basis with entry sum_j a_j n_j on
    |n1 n2 n3> (computed independently from the occupations), and commutes with every N_j.
(2) The controlled-Z generator sigma_x sigma_y (sigma = psi^dag psi - psi psi^dag = 2N - 1) is
    diagonal and conserves every occupation: cross-point diagonal products are not hopping.
(3) A cross component: for each ordered pair x != y, dGamma(E_xy) = psi_x^dag psi_y carries
    |(N_x, N_y) = (0, 1)> to |(1, 0)> (the only nonzero entry of that column, value 1) and fails to
    commute with N_x.
EXPORTS the model (PSI, PSID, NOCC, dgamma, basis_state, helpers) for the class-relative no-go.
"""
from fractions import Fraction as F
from itertools import product

import GA
import fock

NPTS = 3
DIM = 2 ** NPTS
GENERIC = ((F(2), F(-7, 2), F(3)), (F(1, 3), F(5), F(-1)))


mm = GA.mat_mul


def madd(A, B, c=1):
    return [[A[i][j] + c * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def zero(n):
    return [[F(0)] * n for _ in range(n)]


def is_zero(A):
    return all(x == 0 for row in A for x in row)


def comm(A, B):
    return madd(mm(A, B), mm(B, A), -1)


def psi(j):
    """psi_j on (C^2)^(x NPTS): Jordan-Wigner annihilator, point 0 the most significant factor."""
    return fock.to_dense(fock.ann(j, NPTS, fock.MSB), DIM)


PSI = [psi(j) for j in range(NPTS)]
PSID = [[list(r) for r in zip(*p)] for p in PSI]
NOCC = [mm(PSID[j], PSI[j]) for j in range(NPTS)]
SIGMA = [madd(mm(PSID[j], PSI[j]), mm(PSI[j], PSID[j]), -1) for j in range(NPTS)]


def dgamma(a):
    out = zero(DIM)
    for i in range(NPTS):
        for j in range(NPTS):
            if a[i][j] != 0:
                out = madd(out, mm(PSID[i], PSI[j]), a[i][j])
    return out


def basis_state(occ):
    return fock.idx(occ, fock.MSB)


def diag3(vals):
    return [[F(vals[i]) if i == j else F(0) for j in range(NPTS)] for i in range(NPTS)]


DIAGS = [diag3(d) for d in product((0, 1), repeat=NPTS)] + [diag3(g) for g in GENERIC]


def check_bundle_map_quantises_to_multiplication_operator():
    ok = True
    ok = ok and len(DIAGS) == 10
    for a in DIAGS:
        G = dgamma(a)
        want = zero(DIM)
        for j in range(NPTS):
            want = madd(want, NOCC[j], a[j][j])
        ok = ok and G == want
        for occ in product((0, 1), repeat=NPTS):
            s = basis_state(occ)
            val = sum((a[j][j] * occ[j] for j in range(NPTS)), F(0))
            ok = ok and G[s][s] == val and all(G[t][s] == 0 for t in range(DIM) if t != s)
        ok = ok and all(is_zero(comm(G, N)) for N in NOCC)
    ok = ok and all(NOCC[j][basis_state(o)][basis_state(o)] == o[j]
                    for o in product((0, 1), repeat=NPTS) for j in range(NPTS))
    GA.check("dGamma(diag a) = sum a_j N_j, diagonal with entries sum a_j n_j, commuting with every N_j", ok)
    return ok


def check_controlled_z_conserves_occupations():
    ok = True
    for j in range(NPTS):
        ok = ok and SIGMA[j] == madd(madd(zero(DIM), NOCC[j], 2), eye(DIM), -1)
    for x in range(NPTS):
        for y in range(x + 1, NPTS):
            P = mm(SIGMA[x], SIGMA[y])
            ok = ok and all(is_zero(comm(P, N)) for N in NOCC)
            for occ in product((0, 1), repeat=NPTS):
                s = basis_state(occ)
                ok = ok and P[s][s] == (2 * occ[x] - 1) * (2 * occ[y] - 1)
    GA.check("sigma_x sigma_y is diagonal (entries (2n_x - 1)(2n_y - 1)) and conserves every occupation", ok)
    return ok


def check_cross_component_hops():
    ok = True
    for x in range(NPTS):
        for y in range(NPTS):
            if x == y:
                continue
            E = [[F(1) if (r, c) == (x, y) else F(0) for c in range(NPTS)] for r in range(NPTS)]
            G = dgamma(E)
            occ = [0] * NPTS
            occ[y] = 1
            occ2 = [0] * NPTS
            occ2[x] = 1
            col = [G[i][basis_state(occ)] for i in range(DIM)]
            ok = ok and col[basis_state(occ2)] == 1 and sum(1 for c in col if c != 0) == 1
            ok = ok and not is_zero(comm(G, NOCC[x])) and not is_zero(comm(G, NOCC[y]))
    GA.check("psi_x^dag psi_y carries (N_x, N_y) = (0,1) onto (1,0) and does not commute with N_x", ok)
    return ok


EXPORTS = {"NPTS": NPTS, "DIM": DIM, "PSI": PSI, "PSID": PSID, "NOCC": NOCC, "SIGMA": SIGMA,
           "dgamma": dgamma, "basis_state": basis_state, "mm": mm, "madd": madd, "comm": comm,
           "is_zero": is_zero, "eye": eye, "zero": zero}
