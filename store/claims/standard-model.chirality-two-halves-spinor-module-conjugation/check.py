"""standard-model.chirality-two-halves-spinor-module-conjugation: exact checks.

Hypercharge generator y = (3i I_2, -2i I_3); on Lambda^k W = Lambda^k C^3 it acts by the sum of its C^3
eigenvalues over occupied modes, weight q = -2k, Y = q/6.
(1) Halves: S = Lambda^even W carries grades 0, 2, i.e. (1)_0 + (3bar)_{-2/3}; S' = Lambda^odd W carries grades
    1, 3, i.e. (3)_{-1/3} + (1)_{-1}; each half is four-dimensional and the two (content, Y) multisets differ (no
    common summand), so the halves are inequivalent; their direct sum is Lambda^* W (dimension 8). The colour
    content of the halves is 3bar + 3; listing by one handedness (odd grades conjugated, 3 <-> 3bar, Y -> -Y)
    gives 3bar + 3bar and the singlet hypercharges 0, -2/3, +1/3, +1.
(2) Duality: the wedge pairing Lambda^k x Lambda^(3-k) -> Lambda^3 is nondegenerate and, for rational g in
    GL(3), Lambda^k(g)^T J Lambda^(3-k)(g) = det(g) J, so (Lambda^k W)^* = Lambda^(3-k) W (x) (Lambda^3 W)^*; its
    weight -2(3-k) + 6 = 2k is minus the grade-k weight. For C^2: A^T eps A = det(A) eps, so (C^2)^* =
    C^2 (x) det^-1, and (C^2 (x) Lambda^0)^* has weight -3 = weight of C^2 (x) Lambda^3: the two doublets are
    duals; their total mode numbers 1 and 4 have opposite parity (the (S) reading).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

QI = GA.QI
YY = [QI(0, -2)] * 3
XY = [QI(0, 3)] * 2
G_SAMPLES = [[[F(2), F(1), F(0)], [F(-1), F(3), F(1)], [F(0), F(1, 2), F(1)]],
             [[F(1), F(2), F(3)], [F(0), F(1), F(4)], [F(5), F(6), F(0)]]]
A_SAMPLES = [[[F(2), F(5)], [F(-1), F(3)]], [[F(1, 2), F(1)], [F(4), F(-3)]]]
CONJ = {"1": "1", "3": "3b", "3b": "3"}


def _grade_weight(k):
    ws = [sum((YY[i] for i in S), QI(0)) for S in combinations(range(3), k)]
    return ws[0] if all(w == ws[0] for w in ws) else None


def _colour(k):
    return {0: "1", 1: "3", 2: "3b", 3: "1"}[k]


def _minor(g, rows, cols):
    if not rows:
        return F(1)
    if len(rows) == 1:
        return g[rows[0]][cols[0]]
    if len(rows) == 2:
        return g[rows[0]][cols[0]] * g[rows[1]][cols[1]] - g[rows[0]][cols[1]] * g[rows[1]][cols[0]]
    return sum(((-1) ** j * g[rows[0]][cols[j]] * _minor(g, rows[1:], cols[:j] + cols[j + 1:])
                for j in range(3)), F(0))


def _wedge_mat(g, k):
    idx = list(combinations(range(3), k))
    return [[_minor(g, list(I), list(J)) for J in idx] for I in idx], idx


def _sign_of(I, J):
    arr = list(I) + list(J)
    if len(set(arr)) < 3:
        return 0
    s = 1
    for x in range(len(arr)):
        for y in range(x + 1, len(arr)):
            if arr[x] > arr[y]:
                s = -s
    return s


def check_halves_inequivalent():
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    content = {k: (_colour(k), F(_grade_weight(k).im, 6)) for k in range(4)}
    even = sorted(content[k] for k in (0, 2))
    odd = sorted(content[k] for k in (1, 3))
    dims = [len(list(combinations(range(3), k))) for k in range(4)]
    ok = even == sorted([("1", F(0)), ("3b", F(-2, 3))]) and odd == sorted([("3", F(-1, 3)), ("1", F(-1))])
    ok = ok and dims[0] + dims[2] == 4 and dims[1] + dims[3] == 4 and sum(dims) == 8
    ok = ok and not set(even) & set(odd)
    listed = sorted((c, y) if k % 2 == 0 else (CONJ[c], -y) for k, (c, y) in content.items())
    ok = ok and sorted([content[1][0], content[2][0]]) == ["3", "3b"]
    ok = ok and [c for c, y in listed if c != "1"] == ["3b", "3b"]
    ok = ok and sorted(y for c, y in listed) == [F(-2, 3), F(0), F(1, 3), F(1)]
    GA.check("S = (1)_0 + (3b)_{-2/3}, S' = (3)_{-1/3} + (1)_{-1}: inequivalent; one-handed colour 3b + 3b", ok)
    return ok


def check_conjugation_is_duality():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    ok = True
    for k in range(4):
        idx_k = list(combinations(range(3), k))
        idx_c = list(combinations(range(3), 3 - k))
        J = [[F(_sign_of(I, Jc)) for Jc in idx_c] for I in idx_k]
        ok = ok and GA.mat_rank(J) == len(idx_k) == len(idx_c)
        for g in G_SAMPLES:
            Wk, _ = _wedge_mat(g, k)
            Wc, _ = _wedge_mat(g, 3 - k)
            det = _minor(g, [0, 1, 2], [0, 1, 2])
            WkT = [list(r) for r in zip(*Wk)] if Wk else Wk
            lhs = GA.mat_mul(GA.mat_mul(WkT, J), Wc)
            ok = ok and det != 0 and lhs == [[det * x for x in r] for r in J]
        w_dual = _grade_weight(3 - k) - _grade_weight(3)
        ok = ok and w_dual == QI(0) - _grade_weight(k) and w_dual.im == 2 * k
    eps = [[F(0), F(1)], [F(-1), F(0)]]
    for A in A_SAMPLES:
        AT = [list(r) for r in zip(*A)]
        dA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        ok = ok and GA.mat_mul(GA.mat_mul(AT, eps), A) == [[dA * x for x in r] for r in eps]
    w_empty = XY[0]
    w_full = XY[0] + _grade_weight(3)
    w_dual_doublet = XY[0] - (XY[0] + XY[1])
    ok = ok and w_dual_doublet == QI(0) - w_empty == w_full and w_full == QI(0, -3)
    ok = ok and (1 + 0) % 2 != (1 + 3) % 2
    GA.check("(Lambda^k W)^* = Lambda^(3-k) W x det^-1 of weight 2k; (C^2 x Lambda^0)^* = C^2 x Lambda^3", ok)
    return ok
