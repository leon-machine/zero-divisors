"""neutrino.imported-indifference-faces-democratic-alignment-rank: exact checks of the computable core.

Computable part: the S_3 linear algebra on the three-dimensional face space. The statuses (the instrument a
structural premise, the face identification a conjecture, the three-spinor bound at observation level) and the
conversion of the CKM shape into CKM numbers are not computed.
(1) Indifference: the vectors of R^3 fixed by all six permutation matrices form the line spanned by
    u' = (1,1,1) (exact kernel); the symmetric 3 x 3 matrices commuting with S_3 form span{1, J}.
(2) Gram-square reading: Y_0 = u' u'^T = J, the all-ones matrix; rank 1, characteristic polynomial t^3 - 3t^2
    (spectrum (3, 0, 0)), J u' = 3 u', and J kills the plane orthogonal to u'.
(3) The two light families stay degenerate under every S_3-invariant perturbation a 1 + b J (its compression to
    the plane orthogonal to u' is a multiple of that plane's Gram matrix), and an S_2-invariant perturbation
    (sample) splits them: the second-order breaking is what lifts the degeneracy.
"""
from fractions import Fraction as F
from itertools import permutations

import GA
from tp_premise import premise

PERMS = list(permutations(range(3)))
S3_SAMPLES = [(F(1), F(2)), (F(-3), F(1, 2)), (F(5, 7), F(0))]
S2_PERT = [[F(1), F(2), F(-1)], [F(2), F(1), F(-1)], [F(-1), F(-1), F(4)]]   # invariant under swapping 0, 1
LIGHT = [[F(1), F(-1), F(0)], [F(1), F(1), F(-2)]]                            # basis of the plane orthogonal to u'


def pmat(p):
    return [[F(1) if p[j] == i else F(0) for j in range(3)] for i in range(3)]


mm = GA.mat_mul


def compress(A):
    return [[sum(x[i] * A[i][j] * y[j] for i in range(3) for j in range(3)) for y in LIGHT] for x in LIGHT]


def proportional(A, B):
    flat_a = [x for r in A for x in r]
    flat_b = [x for r in B for x in r]
    return GA.rank_of_vectors([flat_a, flat_b]) <= 1


def check_democratic_line_and_invariant_forms():
    premise("families.imported-indifference-instrument")
    premise("families.hyp-face-identification")
    rows = []
    for p in PERMS:
        P = pmat(p)
        rows += [[P[i][j] - (1 if i == j else 0) for j in range(3)] for i in range(3)]
    ker = GA.field_kernel(rows)
    ok = len(PERMS) == 6 and len(ker) == 1 and len(set(ker[0])) == 1 and ker[0][0] != 0
    # symmetric matrices S = sum s_k E_k (6 unknowns) with P S P^T = S for all P
    sym_basis = []
    for i in range(3):
        for j in range(i, 3):
            E = [[F(0)] * 3 for _ in range(3)]
            E[i][j] = E[j][i] = F(1)
            sym_basis.append(E)
    eqs = []
    for p in PERMS:
        P = pmat(p)
        Pt = [[P[j][i] for j in range(3)] for i in range(3)]
        imgs = [mm(mm(P, E), Pt) for E in sym_basis]
        for i in range(3):
            for j in range(3):
                eqs.append([imgs[k][i][j] - sym_basis[k][i][j] for k in range(6)])
    inv = GA.field_kernel(eqs)
    J = [[F(1)] * 3 for _ in range(3)]
    one = [[F(1) if i == j else F(0) for j in range(3)] for i in range(3)]
    mats = [[[sum(c[k] * sym_basis[k][i][j] for k in range(6)) for j in range(3)] for i in range(3)] for c in inv]
    flat = [[x for r in M for x in r] for M in mats]
    ok = ok and len(inv) == 2 and GA.rank_of_vectors(flat + [[x for r in J for x in r], [x for r in one for x in r]]) == 2
    GA.check("S_3-fixed vectors: the democratic line; S_3-invariant symmetric forms: span{1, J}", ok)
    return ok


def check_rank_one_spectrum():
    premise("families.alignment-computed-thirteenth-refutation-democracy-one")
    up = [F(1)] * 3
    J = [[up[i] * up[j] for j in range(3)] for i in range(3)]
    tr = sum(J[i][i] for i in range(3))
    m2 = sum(J[i][i] * J[j][j] - J[i][j] * J[j][i] for i, j in ((0, 1), (0, 2), (1, 2)))
    det = (J[0][0] * (J[1][1] * J[2][2] - J[1][2] * J[2][1]) - J[0][1] * (J[1][0] * J[2][2] - J[1][2] * J[2][0])
           + J[0][2] * (J[1][0] * J[2][1] - J[1][1] * J[2][0]))
    ok = (tr, m2, det) == (3, 0, 0) and GA.rank_of_vectors(J) == 1
    ok = ok and [sum(J[i][k] * up[k] for k in range(3)) for i in range(3)] == [3 * x for x in up]
    ok = ok and all(sum(J[i][k] * v[k] for k in range(3)) == 0 for v in LIGHT for i in range(3))
    GA.check("Y_0 = J: rank one, spectrum (3, 0, 0): one heavy family, two light", ok)
    return ok


def check_s3_protects_light_pair():
    premise("families.faces-ordered-what-identification-requires-first")
    G = compress([[F(1) if i == j else F(0) for j in range(3)] for i in range(3)])
    ok = G == [[2, 0], [0, 6]]
    for a, b in S3_SAMPLES:
        P = [[a * (1 if i == j else 0) + b for j in range(3)] for i in range(3)]
        ok = ok and proportional(compress(P), G)
    swap = pmat((1, 0, 2))
    ok = ok and mm(mm(swap, S2_PERT), swap) == S2_PERT
    ok = ok and not proportional(compress(S2_PERT), G)
    GA.check("S_3-invariant perturbations keep the two light families degenerate; an S_2 one splits them", ok)
    return ok
