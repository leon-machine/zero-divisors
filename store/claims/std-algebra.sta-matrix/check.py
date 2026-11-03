from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def block(A, B, C, D):
    """4x4 complex matrix from 2x2 blocks [[A, B], [C, D]]."""
    top = [A[r] + B[r] for r in range(2)]
    bot = [C[r] + D[r] for r in range(2)]
    return top + bot


def quaternion_units():
    i = GA.QI(0, 1)
    z = GA.QI(0)
    return [[[i, z], [z, -i]], S.mat([[0, 1], [-1, 0]]), [[z, i], [i, z]]]


def check_quaternionic_and_dirac_readings():
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.blade-basis")
    premise("primer.classification-real-clifford-algebras")
    ok = True
    one, zero = S.mat_id(2), S.mat_scal(0, S.mat_id(2))
    mone = S.mat_scal(-1, one)
    qs = quaternion_units()
    ok = ok and S.mat_eq(S.mat_mul(qs[0], qs[1]), qs[2])
    gq = [block(one, zero, zero, mone)] + [block(zero, q, q, zero) for q in qs]
    ok = ok and S.check_matrix_rep(gq, GA.sig(1, 3), 16)
    # the images lie in M_2(H): its real span, E_ab tensor {1, q1, q2, q3}, has dimension 16
    # and adding the 16 products of the images does not raise it
    span = []
    for a in range(2):
        for b in range(2):
            for q in [one] + qs:
                blocks = [[zero, zero], [zero, zero]]
                blocks[a][b] = q
                span.append(block(blocks[0][0], blocks[0][1], blocks[1][0], blocks[1][1]))
    prods = []
    for k in range(5):
        for idx in combinations(range(4), k):
            P = S.mat_id(4)
            for t in idx:
                P = S.mat_mul(P, gq[t])
            prods.append(P)
    ok = ok and S.real_span_rank(span) == 16 and S.real_span_rank(span + prods) == 16
    # the Dirac reading: faithful on Cl(1,3), complex span M_4(C)
    i = GA.QI(0, 1)
    z = GA.QI(0)
    sig = [S.mat([[0, 1], [1, 0]]), [[z, -i], [i, z]], S.mat([[1, 0], [0, -1]])]
    gd = [block(one, zero, zero, mone)] + [block(zero, s, S.mat_scal(-1, s), zero) for s in sig]
    ok = ok and S.check_matrix_rep(gd, GA.sig(1, 3), 16)
    dprods = []
    for k in range(5):
        for idx in combinations(range(4), k):
            P = S.mat_id(4)
            for t in idx:
                P = S.mat_mul(P, gd[t])
            dprods.append([a for row in P for a in row])
    ok = ok and GA.field_rank(dprods) == 16
    GA.check("Cl(1,3) = M_2(H) by quaternion blocks; the Dirac matrices represent it with complex span M_4(C)", ok)
    return ok


def check_spacetime_split():
    premise("std-algebra.z2-grading")
    ok = True
    sq = GA.sig(1, 3)
    g = [GA.gen(a) for a in range(4)]
    s = [GA.mul(g[k], g[0], sq) for k in (1, 2, 3)]
    for j in range(3):
        for k in range(3):
            d = GA.sc(2) if j == k else {}
            ok = ok and GA.eq(GA.add(GA.mul(s[j], s[k], sq), GA.mul(s[k], s[j], sq)), d)
    I = S.pseudoscalar(4)
    ok = ok and GA.eq(GA.mul(GA.mul(s[0], s[1], sq), s[2], sq), I)
    prods = []
    for k in range(4):
        for idx in combinations(range(3), k):
            x = GA.sc(1)
            for t in idx:
                x = GA.mul(x, s[t], sq)
            prods.append(x)
            ok = ok and all(len(b) % 2 == 0 for b in x)
    ok = ok and S.span_rank(prods, 4) == 8
    ok = ok and len([b for b in GA.all_blades(4) if len(b) % 2 == 0]) == 8
    GA.check("sigma_k = gamma_k gamma_0 generate Cl+(1,3) = Cl(3,0), with sigma_1 sigma_2 sigma_3 = I", ok)
    return ok
