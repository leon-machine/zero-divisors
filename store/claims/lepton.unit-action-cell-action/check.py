"""lepton.unit-action-cell-action: exact checks.

Cells c_(i,a) = e_i (x) f_a (index 3 i + a) span C^2 (x) C^3; the tensor ledger Lambda^k(C^2 (x) C^3) carries
the cell action, the derivation of X (x) 1 + 1 (x) Y on the cells. The constituent space C_k = C^2 (x)
Lambda^k W carries the unit action (X on the slot once, Lambda^k(Y) on the pairs). R_k is spanned by the
single-row states c_(i,a1) ^ ... ^ c_(i,ak), identified with e_i (x) f_S.
(1) k = 1: for every elementary matrix of gl(2) and of gl(3) the cell action on R_1 stays in R_1 and equals
    the unit action under the identification: an isomorphism of representations.
(2) k = 2, 3: the cell action does not preserve R_k; the gl(2) + gl(3)-span of R_k (closure under the
    elementary matrices, computed by exact rank) has dimension (k + 1) C(3, k) = 9, 4, against
    dim C_k = 2 C(3, k) = 6, 2; the SU(2)-span of one single-row state has dimension k + 1 = 2, 3, 4 for
    k = 1, 2, 3 (unit action: 2); the y-weight is k under the cell action and 3 - 2k under the unit action;
    the su(2) Casimir EF + FE + H^2/2 on the cell span is k(k + 2)/2 (spin k/2: S^k C^2), not the doublet's
    3/2, at k = 2, 3.
(3) So the constituent space is not a subrepresentation of the ledger (R_2, R_3 are not invariant), and at
    k = 3 the filled-row states span (4, 1), not a (2, 1).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

Y_GEN = ([[3, 0], [0, 3]], [[-2, 0, 0], [0, -2, 0], [0, 0, -2]])


def _wedge(seq):
    """Normalise a wedge word f_s1 ^ ... ^ f_sk: (sign, sorted tuple), or (0, None) if a factor repeats."""
    if len(set(seq)) < len(seq):
        return 0, None
    seq = list(seq)
    sign = 1
    for i in range(len(seq)):
        for j in range(len(seq) - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                sign = -sign
    return sign, tuple(seq)


def derive(Y, S):
    """The derivation action of the matrix Y on the wedge basis vector f_S: a dict {T: coeff}."""
    out = {}
    for t, s in enumerate(S):
        for r in range(len(Y)):
            if Y[r][s]:
                sg, T = _wedge(S[:t] + (r,) + S[t + 1:])
                if sg:
                    out[T] = out.get(T, 0) + sg * Y[r][s]
    return {T: c for T, c in out.items() if c}


def unit_action(X, Y, state):
    """(X, Y) in gl(2) + gl(3) on C^2 (x) Lambda W, basis (i, S): X on the slot once, Y as a derivation."""
    out = {}
    for (i, S), c in state.items():
        for j in range(2):
            if X[j][i]:
                out[(j, S)] = out.get((j, S), 0) + X[j][i] * c
        for T, d in derive(Y, S).items():
            out[(i, T)] = out.get((i, T), 0) + d * c
    return {b: c for b, c in out.items() if c}


def unit(n, i, j):
    return [[1 if (a, b) == (i, j) else 0 for b in range(n)] for a in range(n)]


ZERO2 = [[0] * 2 for _ in range(2)]
ZERO3 = [[0] * 3 for _ in range(3)]


def con_basis(k):
    return [(i, S) for i in range(2) for S in combinations(range(3), k)]


def torus_weights(k):
    """Weights (a1, a2, b1, b2, b3) of U(2) x U(3) on C_k, read off the action of the diagonal units;
    returns None if some basis vector is not an eigenvector."""
    out = []
    for b in con_basis(k):
        w = []
        for t in range(5):
            X = unit(2, t, t) if t < 2 else ZERO2
            Y = unit(3, t - 2, t - 2) if t >= 2 else ZERO3
            img = unit_action(X, Y, {b: 1})
            if set(img) - {b}:
                return None
            w.append(img.get(b, 0))
        out.append(tuple(w))
    return sorted(out)


def sl3_class(w):
    """The sl(3) weight of a U(3) weight (b1, b2, b3): subtract the mean."""
    m = F(sum(w), 3)
    return tuple(F(x) - m for x in w)


FUND3 = sorted(sl3_class(tuple(1 if i == j else 0 for i in range(3))) for j in range(3))
ANTI3 = sorted(sl3_class(tuple(-1 if i == j else 0 for i in range(3))) for j in range(3))
TRIV = [sl3_class((0, 0, 0))]


def su3_content(ws):
    """'1', '3' or '3b' from the multiset of sl(3) weights of the U(3) part of one SU(2) weight space."""
    cls = sorted(sl3_class(w[2:]) for w in ws if w[:2] == ws[0][:2])
    return {tuple(TRIV): "1", tuple(FUND3): "3", tuple(ANTI3): "3b"}.get(tuple(cls))


def su2_dim(ws):
    """Number of distinct SU(2) weights a1 - a2 at fixed U(3) weight (the SU(2) dimension)."""
    return len({w[0] - w[1] for w in ws if w[2:] == ws[0][2:]})


def cell_matrix(X, Y):
    """X (x) 1 + 1 (x) Y on the six cells: entry [3j + b][3i + a]."""
    M = [[0] * 6 for _ in range(6)]
    for i in range(2):
        for a in range(3):
            for j in range(2):
                if X[j][i]:
                    M[3 * j + a][3 * i + a] += X[j][i]
            for b in range(3):
                if Y[b][a]:
                    M[3 * i + b][3 * i + a] += Y[b][a]
    return M


def cell_action(X, Y, state):
    M = cell_matrix(X, Y)
    out = {}
    for S, c in state.items():
        for T, d in derive(M, S).items():
            out[T] = out.get(T, 0) + c * d
    return {T: c for T, c in out.items() if c}


def row_state(i, S):
    return {tuple(3 * i + a for a in S): 1}


def generators():
    out = [(unit(2, i, j), ZERO3) for i in range(2) for j in range(2)]
    out += [(ZERO2, unit(3, a, b)) for a in range(3) for b in range(3)]
    return out


def _rank(states):
    keys = sorted({K for st in states for K in st})
    return GA.rank_of_vectors([[F(st.get(K, 0)) for K in keys] for st in states]) if states else 0


def closure(states, gens):
    span = list(states)
    r = _rank(span)
    while True:
        new = [act(X, Y, st) for st in span for (X, Y) in gens for act in (cell_action,)]
        cand = span + [s for s in new if s]
        r2 = _rank(cand)
        if r2 == r:
            return span, r
        basis = []
        for s in cand:
            if _rank(basis + [s]) > len(basis):
                basis.append(s)
        span, r = basis, r2


def check_one_pair_identification_is_isomorphism():
    premise("lepton.content-constituent-space")
    ok = True
    for (X, Y) in generators():
        for i in range(2):
            for a in range(3):
                cell = cell_action(X, Y, row_state(i, (a,)))
                unit_img = unit_action(X, Y, {(i, (a,)): 1})
                ok = ok and cell == {(3 * j + b[0],): c for (j, b), c in unit_img.items()}
    _tp_rv = (ok); assert _tp_rv is not False, "check_one_pair_identification_is_isomorphism"; return _tp_rv


def check_cell_span_exceeds_constituents():
    premise("lepton.content-constituent-space")
    premise("lepton.imported-tensor-ledger-contains-no-lepton")
    ok = True
    gens = generators()
    dims, orbit, preserved = [], [], []
    for k in (1, 2, 3):
        Rk = [row_state(i, S) for i in range(2) for S in combinations(range(3), k)]
        span, r = closure(Rk, gens)
        dims.append(r)
        orb, r1 = closure([row_state(0, tuple(range(k)))], gens[:4])
        orbit.append(r1)
        stays = all(_rank(Rk + [cell_action(X, Y, st)]) == len(Rk) for st in Rk for (X, Y) in gens)
        preserved.append(stays)
        ok = ok and len(con_basis(k)) == 2 * len(list(combinations(range(3), k)))
    ok = ok and dims == [6, 9, 4] and orbit == [2, 3, 4] and preserved == [True, False, False]
    _tp_rv = (ok); assert _tp_rv is not False, "check_cell_span_exceeds_constituents"; return _tp_rv


def check_weights_and_spin_of_the_two_actions():
    premise("lepton.content-constituent-space")
    premise("lepton.imported-tensor-ledger-contains-no-lepton")
    ok = True
    E, Fm, H = unit(2, 0, 1), unit(2, 1, 0), [[1, 0], [0, -1]]
    for k in (1, 2, 3):
        Rk = [row_state(i, S) for i in range(2) for S in combinations(range(3), k)]
        ycell = {cell_action(Y_GEN[0], Y_GEN[1], st).get(next(iter(st))) for st in Rk}
        yunit = {unit_action(Y_GEN[0], Y_GEN[1], {b: 1}).get(b) for b in con_basis(k)}
        ok = ok and ycell == {k} and yunit == {3 - 2 * k}
        span, _ = closure(Rk, generators())
        for st in span:
            ef = cell_action(E, ZERO3, cell_action(Fm, ZERO3, st))
            fe = cell_action(Fm, ZERO3, cell_action(E, ZERO3, st))
            hh = cell_action(H, ZERO3, cell_action(H, ZERO3, st))
            cas = {K: F(ef.get(K, 0) + fe.get(K, 0)) + F(hh.get(K, 0), 2) for K in set(ef) | set(fe) | set(hh)}
            cas = {K: c for K, c in cas.items() if c}
            ok = ok and cas == {K: F(k * (k + 2), 2) * c for K, c in st.items()}
    _tp_rv = (ok); assert _tp_rv is not False, "check_weights_and_spin_of_the_two_actions"; return _tp_rv
