"""standard-model.frozen-point-pair-mixing: exact checks.

Model: the five-mode module (pair modes 0, 1, 2 spanning W; rung modes 3, 4), creation v_i, annihilation w_i;
V_C = W + Wbar is spanned by the six pair-mode operators v_i, w_i (i <= 3 in the text's labels).
(1) Weights: [N_j, v_i] = delta_ij v_i and [N_j, w_i] = -delta_ij w_i for the three pair number operators,
    so the weights of V_C are +-e_i, none zero; the joint kernel of x -> ([N_1, x], [N_2, x], [N_3, x]) on
    V_C is zero (no nonzero vector is invariant under the maximal torus, so none under U(3)); the frozen point
    I = a v_1 + b w_1 is moved by N_1 for every sample (a, b) != 0.
(2) Stabiliser: for five nonzero vectors of C^3 the real stabiliser in u(3) (nine real generators) has real
    dimension 4 = dim u(2).
(3) Every pair-mode operator commutes with the rung mixing u(2) = span{v_a w_b : a, b rungs} and with N_R.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
from tp_premise import premise

# ---------------------------------------------------------------------------
# The five-mode module Lambda(W + R_2) = Lambda(C^5), exact (sparse matrices {(row, col): Fraction}).
# Modes 0, 1, 2 are the pair modes (W), modes 3, 4 the two rung (slot) modes, the text's modes 4 and 5.
# v_i = creation (wedge), w_i = annihilation (contraction), v_i w_i + w_i v_i = 1.
# ---------------------------------------------------------------------------
NM = 5
PAIRS5, RUNGS5 = (0, 1, 2), (3, 4)
STATES = [frozenset(S) for k in range(NM + 1) for S in combinations(range(NM), k)]
SIDX = {S: i for i, S in enumerate(STATES)}
DIM5 = len(STATES)


def sp_from_action(act):
    M = {}
    for S in STATES:
        for T, c in act(S).items():
            if c != 0:
                M[(SIDX[T], SIDX[S])] = M.get((SIDX[T], SIDX[S]), F(0)) + c
    return {k: v for k, v in M.items() if v != 0}


def sp_mul(A, B):
    Bc = {}
    for (i, j), b in B.items():
        get_or_set(Bc, i, []).append((j, b))
    C = {}
    for (i, k), a in A.items():
        for j, b in Bc.get(k, ()):
            C[(i, j)] = C.get((i, j), F(0)) + a * b
    return {k: v for k, v in C.items() if v != 0}


def sp_add(*Ms):
    C = {}
    for M in Ms:
        for k, v in M.items():
            C[k] = C.get(k, F(0)) + v
    return {k: v for k, v in C.items() if v != 0}


def sp_scal(c, M):
    return {k: c * v for k, v in M.items() if c * v != 0}


def sp_eq(A, B):
    return sp_add(A, sp_scal(F(-1), B)) == {}


def sp_apply(M, vec):
    out = {}
    for (i, j), a in M.items():
        if j in vec:
            out[i] = out.get(i, F(0)) + a * vec[j]
    return {k: v for k, v in out.items() if v != 0}


ID5 = {(i, i): F(1) for i in range(DIM5)}
V5 = [sp_from_action(lambda S, i=i: GA.ext_wedge(i, {S: F(1)})) for i in range(NM)]
W5 = [sp_from_action(lambda S, i=i: GA.ext_contract([F(1) if j == i else F(0) for j in range(NM)], {S: F(1)}))
      for i in range(NM)]


def num(i):
    return sp_mul(V5[i], W5[i])


N_W = sp_add(*[num(i) for i in PAIRS5])
N_R = sp_add(*[num(i) for i in RUNGS5])
HYP = sp_add(sp_scal(F(1, 2), N_R), sp_scal(F(-1, 3), N_W))
T3 = sp_scal(F(1, 2), sp_add(num(3), sp_scal(F(-1), num(4))))
SU3 = [sp_mul(V5[i], W5[j]) for i in PAIRS5 for j in PAIRS5 if i != j]
SU2 = [sp_mul(V5[3], W5[4]), sp_mul(V5[4], W5[3]), T3]


def comm(A, B):
    return sp_add(sp_mul(A, B), sp_scal(F(-1), sp_mul(B, A)))


def weight(M, Q):
    """The eigenvalue of ad Q on M, or None if M is not an eigenvector."""
    c = comm(Q, M)
    if c == {}:
        return F(0)
    (i, j), a = next(iter(M.items()))
    q = c.get((i, j), F(0)) / a
    return q if sp_eq(c, sp_scal(q, M)) else None


def basis5(S):
    return {SIDX[frozenset(S)]: F(1)}

QI = GA.QI
AB_SAMPLES = [(F(1), F(0)), (F(0), F(1)), (F(2), F(1, 6)), (F(1), F(-1, 3)), (F(-3), F(5))]
C3_SAMPLES = [(1, 0, 0), (0, 1, 0), (1, QI(0, 1), 0), (QI(2, 1), -1, 3), (F(1, 2), QI(0, -2), QI(1, 1))]


def check_ambient_weights_are_nonzero():
    premise("standard-model.module-factorises-even-ground-elements-act")
    ok = True
    for i in PAIRS5:
        for j in PAIRS5:
            ok = ok and weight(V5[i], num(j)) == (F(1) if i == j else F(0))
            ok = ok and weight(W5[i], num(j)) == (F(-1) if i == j else F(0))
    ops = [V5[i] for i in PAIRS5] + [W5[i] for i in PAIRS5]
    keys = sorted({k for j in PAIRS5 for x in ops for k in comm(num(j), x)})
    M = [[comm(num(j), x).get(k, F(0)) for x in ops] for j in PAIRS5 for k in keys]
    ok = ok and len(GA.field_kernel(M)) == 0
    for a, b in AB_SAMPLES:
        I = sp_add(sp_scal(a, V5[0]), sp_scal(b, W5[0]))
        ok = ok and comm(num(0), I) != {}
    _tp_rv = (ok); assert _tp_rv is not False, "check_ambient_weights_are_nonzero"; return _tp_rv


def u3_basis():
    out = []
    for j in range(3):
        out.append([[QI(0, 1) if (r, c) == (j, j) else QI(0) for c in range(3)] for r in range(3)])
    for j, k in combinations(range(3), 2):
        out.append([[QI(1) if (r, c) == (j, k) else QI(-1) if (r, c) == (k, j) else QI(0) for c in range(3)]
                    for r in range(3)])
        out.append([[QI(0, 1) if (r, c) in ((j, k), (k, j)) else QI(0) for c in range(3)] for r in range(3)])
    return out


def check_generic_stabiliser_is_u2():
    ok = True
    basis = u3_basis()
    ok = ok and len(basis) == 9
    for v in C3_SAMPLES:
        v = [x if isinstance(x, QI) else QI(x) for x in v]
        imgs = [[sum((X[r][c] * v[c] for c in range(3)), QI(0)) for r in range(3)] for X in basis]
        real_rows = [[img[r].re for img in imgs] for r in range(3)] + [[img[r].im for img in imgs] for r in range(3)]
        ok = ok and len(GA.field_kernel(real_rows)) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_generic_stabiliser_is_u2"; return _tp_rv


def check_vectors_commute_with_rung_mixing():
    premise("standard-model.module-factorises-even-ground-elements-act")
    ok = True
    mixing = [sp_mul(V5[a], W5[b]) for a in RUNGS5 for b in RUNGS5]
    ok = ok and len(mixing) == 4
    checked = 0
    for i in PAIRS5:
        for x in (V5[i], W5[i]):
            ok = ok and all(comm(x, g) == {} for g in mixing) and comm(x, N_R) == {}
            checked += 1
    ok = ok and checked == 6
    # control: a rung operator is moved by the rung number, [v_4, N_R] = -v_4
    ok = ok and comm(V5[3], N_R) == sp_scal(F(-1), V5[3])
    _tp_rv = (ok); assert _tp_rv is not False, "check_vectors_commute_with_rung_mixing"; return _tp_rv
