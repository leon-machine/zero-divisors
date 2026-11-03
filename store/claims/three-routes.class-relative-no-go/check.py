"""three-routes.class-relative-no-go: exact checks in a finite model.

Base: three points x1, x2, x3 of Sigma, one ladder mode per point; functions act on one-particle sections by
diagonal multiplication; Fock space of the three modes by Jordan-Wigner (8 x 8 matrices), occupations N_j.
(1) Function-linearity forces support preservation (the premise lemma): a one-particle map commutes with
multiplication by every function (the three point indicators) exactly when it is diagonal; checked on all nine
matrix units and on two composite maps.
(2) Bundle maps quantise without hopping (the premise proposition): for every diagonal a (all eight 0/1 diagonals
and a generic one), dGamma(a) = sum a_ij psi_i^dag psi_j commutes with N_1, N_2, N_3; the products sigma_x sigma_y
(sigma = psi^dag psi - psi psi^dag) conserve every occupation.
(3) Hence no supplied (function-linear) generator moves occupation, while every off-diagonal unit E_xy quantises to
a generator that carries the sector (N_x, N_y) = (0, 1) into (1, 0); the same holds for a nearest-neighbour
difference operator, the discrete stand-in for a differential operator outside the supplied class.
"""
from fractions import Fraction as F
from itertools import product
import GA
import fock
from tp_premise import premise

NPTS = 3
# two composite one-particle maps: a generic diagonal one and one with a single hop x1 -> x2
COMPOSITE_DIAG = [[F(2), F(0), F(0)], [F(0), F(-1, 3), F(0)], [F(0), F(0), F(5)]]
COMPOSITE_HOP = [[F(1), F(0), F(0)], [F(4), F(1), F(0)], [F(0), F(0), F(1)]]
# the nearest-neighbour difference operator (path Laplacian on x1 - x2 - x3)
DIFF_OP = [[F(1), F(-1), F(0)], [F(-1), F(2), F(-1)], [F(0), F(-1), F(1)]]
# every occupation pattern of the three modes
OCC_PATTERNS = list(product((0, 1), repeat=NPTS))


def mm(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B)) if A[i][t] != 0) for j in range(len(B[0]))]
            for i in range(len(A))]


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


PSI = [fock.to_dense(fock.ann(j, NPTS, fock.MSB), 2 ** NPTS) for j in range(NPTS)]   # Jordan-Wigner
PSID = [[list(r) for r in zip(*p)] for p in PSI]
NOCC = [mm(PSID[j], PSI[j]) for j in range(NPTS)]


def dgamma(a):
    out = zero(2 ** NPTS)
    for i in range(NPTS):
        for j in range(NPTS):
            if a[i][j] != 0:
                out = madd(out, mm(PSID[i], PSI[j]), a[i][j])
    return out


def unit(i, j):
    return [[F(1) if (r, c) == (i, j) else F(0) for c in range(NPTS)] for r in range(NPTS)]


def check_function_linear_maps_are_diagonal():
    premise("three-routes.function-linear-maps-preserve-supports")
    ok = True
    indicators = [unit(p, p) for p in range(NPTS)]
    verdicts = []
    for i in range(NPTS):
        for j in range(NPTS):
            E = unit(i, j)
            verdicts.append(all(is_zero(comm(E, chi)) for chi in indicators))
    ok = ok and verdicts == [True, False, False, False, True, False, False, False, True]
    diag, hop = COMPOSITE_DIAG, COMPOSITE_HOP
    ok = ok and all(is_zero(comm(diag, chi)) for chi in indicators)
    ok = ok and [is_zero(comm(hop, chi)) for chi in indicators] == [False, False, True]
    # exactly the three diagonal units preserve supports; and by hand [hop, chi_1] = hop E_11 - E_11 hop
    # = 4 E_21, the hop entry itself: the obstruction is the off-diagonal part
    ok = ok and verdicts.count(True) == 3
    ok = ok and comm(hop, indicators[0]) == [[0, 0, 0], [4, 0, 0], [0, 0, 0]]
    GA.check("a map commutes with all function multiplications exactly when it is diagonal (support preserving)", ok)
    return ok


# generic one-particle bundle maps: all 0/1 diagonals and one generic diagonal
DIAGS = [[[F(d[i]) if i == j else F(0) for j in range(NPTS)] for i in range(NPTS)]
         for d in product((0, 1), repeat=NPTS)]
VALS = (F(2), F(-7, 2), F(3))
DIAGS.append([[VALS[i] if i == j else F(0) for j in range(NPTS)] for i in range(NPTS)])


def check_bundle_maps_quantise_without_hopping():
    premise("three-routes.support-preserving-families-quantise-without-hopping")
    ok = True
    ok = ok and len(DIAGS) == 9
    for a in DIAGS:
        G = dgamma(a)
        # dGamma of a bundle map is the sum of single-point bilinears a_jj N_j
        want = zero(2 ** NPTS)
        for j in range(NPTS):
            want = madd(want, NOCC[j], a[j][j])
        ok = ok and G == want
        ok = ok and all(is_zero(comm(G, N)) for N in NOCC)
    sig = [madd(mm(PSID[j], PSI[j]), mm(PSI[j], PSID[j]), -1) for j in range(NPTS)]
    # sigma_j = 2 N_j - 1, diagonal in occupation
    ok = ok and all(sig[j] == madd(madd(zero(2 ** NPTS), NOCC[j], 2), eye(2 ** NPTS), -1) for j in range(NPTS))
    for x in range(NPTS):
        for y in range(x + 1, NPTS):
            ok = ok and all(is_zero(comm(mm(sig[x], sig[y]), N)) for N in NOCC)
    GA.check("dGamma of every bundle map, and every sigma_x sigma_y, conserves all three occupations", ok)
    return ok


def basis_state(occ):
    idx = 0
    for o in occ:
        idx = 2 * idx + o
    return idx


def check_off_diagonal_generators_hop():
    premise("three-routes.support-preserving-families-quantise-without-hopping")
    ok = True
    for x in range(NPTS):
        for y in range(NPTS):
            if x == y:
                continue
            G = dgamma(unit(x, y))
            occ = [0] * NPTS
            occ[y] = 1
            src = basis_state(occ)
            occ2 = [0] * NPTS
            occ2[x] = 1
            dst = basis_state(occ2)
            col = [G[i][src] for i in range(2 ** NPTS)]
            ok = ok and col[dst] != 0 and sum(1 for c in col if c != 0) == 1
            ok = ok and not is_zero(comm(G, NOCC[x]))
    # occupation numbers are diagonal with the expected eigenvalues (the state labelling is right)
    ok = ok and len(set(OCC_PATTERNS)) == 2 ** NPTS
    ok = ok and all(NOCC[j][basis_state(o)][basis_state(o)] == o[j] for o in OCC_PATTERNS for j in range(NPTS))
    # the difference operator hops between neighbours, so it moves every occupation
    ok = ok and all(not is_zero(comm(dgamma(DIFF_OP), NOCC[j])) for j in range(NPTS))
    GA.check("off-diagonal units and a difference operator quantise to hopping: (0,1) -> (1,0)", ok)
    return ok
