"""standard-model.quarks-leptons-two-level-fermion-content: exact checks.

The hypercharge generator is y = (3i I_2, -2i I_3), the centre of s(u(2) + u(3)) (it commutes with every generator
and has total trace 0 on C^5); its weight q on a representation is read off as the scalar by which it acts, and
Y = q/6. Weights are computed from the generator (diagonal entries summed over occupied modes), not typed in.
(1) On the cells C^2 (x) C^3 (tensor action X (x) 1 + 1 (x) Y) y acts as the scalar i: q = 1, Y = 1/6; the
    representation is irreducible (commutant of su(2) + su(3) of real dimension 2, span{1, i}): (2, 3)_{1/6}.
(2) Under (S): C^2 (x) Lambda^0 W and C^2 (x) Lambda^3 W have weights 3 and -3 (Y = +1/2, -1/2), total mode
    numbers 1 (odd) and 4 (even); su(3) acts on Lambda^3 W by its trace, 0, so both are (2, 1). Without (S), in
    Lambda^3(C^2 (x) C^3) the SU(2)-orbit of a filled row spans rank 4 (five unipotent images), and the raising
    operator e satisfies e^3(row) = 6 e_01^e_02^e_03, e^4 = 0: one Jordan block, the quadruplet (4, 1), weight +3.
(3) Single-spinor sector Lambda^k C^3: weights 0, -2, -4, -6 (Y = 0, -1/3, -2/3, -1); the sl(3) weights
    (mod (1,1,1)) of Lambda^1 are those of 3, of Lambda^2 those of 3bar (the negatives), Lambda^0 and Lambda^3 are
    trivial: 1, 3, 3bar, 1. The composite content is (2,3)_{1/6} + (2,1)_{-1/2}.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

QI = GA.QI
XY = [QI(0, 3), QI(0, 3)]           # diagonal of the C^2 part of y
YY = [QI(0, -2), QI(0, -2), QI(0, -2)]   # diagonal of the C^3 part of y
UNIP = [F(0), F(1), F(2), F(3), F(5)]


def _basis_su(n):
    out = []
    for k in range(n - 1):
        out.append({(k, k): QI(0, 1), (k + 1, k + 1): QI(0, -1)})
    for j in range(n):
        for k in range(j + 1, n):
            out.append({(j, k): QI(1), (k, j): QI(-1)})
            out.append({(j, k): QI(0, 1), (k, j): QI(0, 1)})
    return out


def _tensor(X, Y, m, k):
    M = {}
    for (a, c), z in X.items():
        for b in range(k):
            M[(a * k + b, c * k + b)] = M.get((a * k + b, c * k + b), QI(0)) + z
    for (b, d), z in Y.items():
        for a in range(m):
            M[(a * k + b, a * k + d)] = M.get((a * k + b, a * k + d), QI(0)) + z
    return {kk: v for kk, v in M.items() if v}


def _diag(vals):
    return {(i, i): v for i, v in enumerate(vals) if v}


def _scalar(M, N):
    c = M.get((0, 0), QI(0))
    return c if all(M.get((i, j), QI(0)) == (c if i == j else QI(0)) for i in range(N) for j in range(N)) else None


def _wedge_weight(diag, S):
    return sum((diag[i] for i in S), QI(0))


def _commutant_real_dim(gens, N):
    """Real dimension of {Z in M_N(C) : [Z, g] = 0 for all g}."""
    cols = []
    for r in range(N):
        for c in range(N):
            for part in (QI(1), QI(0, 1)):
                Z = {(r, c): part}
                row = []
                for g in gens:
                    C = {}
                    for (a, b), z in Z.items():
                        for (b2, d), w in g.items():
                            if b == b2:
                                C[(a, d)] = C.get((a, d), QI(0)) + z * w
                    for (a, b), w in g.items():
                        for (b2, d), z in Z.items():
                            if b == b2:
                                C[(a, d)] = C.get((a, d), QI(0)) - w * z
                    for i in range(N):
                        for j in range(N):
                            v = C.get((i, j), QI(0))
                            row.extend([v.re, v.im])
                cols.append(row)
    return 2 * N * N - GA.rank_of_vectors(cols)


def _wedge3(vecs):
    out = {}
    for I in combinations(range(6), 3):
        m = [[vecs[r][c] for c in I] for r in range(3)]
        d = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
             + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
        if d:
            out[I] = d
    return out


def _row_state(s):
    vecs = []
    for a in range(3):
        v = [F(0)] * 6
        v[a] = s
        v[3 + a] = F(1)
        vecs.append(v)
    return _wedge3(vecs)


def _apply_e(state):
    out = {}
    for I, c in state.items():
        for pos, cell in enumerate(I):
            if cell >= 3:
                new = list(I)
                new[pos] = cell - 3
                if len(set(new)) < 3:
                    continue
                sign, arr = 1, new[:]
                for x in range(3):
                    for y in range(2 - x):
                        if arr[y] > arr[y + 1]:
                            arr[y], arr[y + 1] = arr[y + 1], arr[y]
                            sign = -sign
                out[tuple(arr)] = out.get(tuple(arr), F(0)) + sign * c
    return {k: v for k, v in out.items() if v != 0}


def _sl3(w):
    s = F(sum(w), 3)
    return tuple(F(x) - s for x in w)


def check_cells_are_quark_doublet():
    premise("standard-model.global-form-quotient-determined")
    y2, y3 = _diag(XY), _diag(YY)
    # y is central in s(u(2) + u(3)) and traceless on C^5
    gens = [_tensor(X, {}, 2, 3) for X in _basis_su(2)] + [_tensor({}, Y, 2, 3) for Y in _basis_su(3)]
    ycell = _tensor(y2, y3, 2, 3)
    ok = sum(XY + YY, QI(0)) == QI(0)
    w = _scalar(ycell, 6)
    ok = ok and w == QI(0, 1) and F(w.im, 6) == F(1, 6)
    ok = ok and _commutant_real_dim(gens, 6) == 2
    GA.check("cells C^2 x C^3: y acts as i (q = 1, Y = 1/6), irreducible: (2,3)_{1/6}", ok)
    return ok


def check_doublets_under_s():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    ok = True
    w0 = _scalar(_diag(XY), 2)                                  # C^2 x Lambda^0 W
    w3 = _scalar(_diag([x + _wedge_weight(YY, (0, 1, 2)) for x in XY]), 2)   # C^2 x Lambda^3 W
    ok = ok and w0 == QI(0, 3) and w3 == QI(0, -3)
    ok = ok and (F(w0.im, 6), F(w3.im, 6)) == (F(1, 2), F(-1, 2))
    # su(3) on Lambda^3 C^3 acts by its trace: zero for every generator, so an SU(3) singlet
    ok = ok and all(sum((Y.get((i, i), QI(0)) for i in range(3)), QI(0)) == QI(0) for Y in _basis_su(3))
    modes = [1 + 0, 1 + 3]
    ok = ok and [m % 2 for m in modes] == [1, 0]
    GA.check("under (S): C^2 x Lambda^0 W weight 3 (odd), C^2 x Lambda^3 W weight -3 (even), both (2,1)", ok)
    return ok


def check_no_doublet_without_s():
    premise("standard-model.raw-representation-content-state-space")
    premise("standard-model.imported-cauchy-decomposition-exterior-power")
    states = [_row_state(s) for s in UNIP]
    keys = sorted(set(k for st in states for k in st))
    rk = GA.mat_rank([[st.get(k, F(0)) for k in keys] for st in states])
    filled = _row_state(F(0))
    e1 = _apply_e(filled)
    e2 = _apply_e(e1)
    e3 = _apply_e(e2)
    e4 = _apply_e(e3)
    cell_w = _scalar(_tensor(_diag(XY), _diag(YY), 2, 3), 6)
    ok = rk == 4 and len(keys) == 8 and e3 == {(0, 1, 2): F(6)} and e4 == {} and len(e1) == 3 and len(e2) == 3
    ok = ok and (cell_w * QI(3)) == QI(0, 3)
    GA.check("without (S) the filled rows form the quadruplet (4,1) of weight +3 (rank 4, one Jordan block)", ok)
    return ok


def check_single_spinor_sector():
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    ok = True
    weights = []
    for k in range(4):
        ws = [_wedge_weight(YY, S) for S in combinations(range(3), k)]
        ok = ok and all(x == ws[0] for x in ws)
        weights.append(ws[0].im)
    ok = ok and weights == [0, -2, -4, -6] and [F(x, 6) for x in weights] == [0, F(-1, 3), F(-2, 3), -1]
    sl = [sorted(_sl3(tuple(int(i in S) for i in range(3))) for S in combinations(range(3), k)) for k in range(4)]
    three = sorted(_sl3(tuple(int(i == j) for i in range(3))) for j in range(3))
    three_bar = sorted(tuple(-x for x in w) for w in three)
    ok = ok and sl[0] == sl[3] == [(0, 0, 0)] and sl[1] == three and sl[2] == three_bar and three != three_bar
    GA.check("Lambda^k C^3: weights 0, -2, -4, -6 and content 1, 3, 3bar, 1", ok)
    return ok
