"""lepton.content-constituent-space: exact checks.

The constituent space C_k = C^2 (x) Lambda^k W with the unit action of Hypothesis (C): (X, Y) in
gl(2) + gl(3) acts as X on the slot vector once and as the derivation Lambda^k(Y) on the pairs, built on
the wedge basis (signs from reordering). Everything below is read off this action.
(1) The hypercharge generator y = (3 I_2, -2 I_3) (times i) acts on C_k as the scalar 3 - 2k (checked to be
    diagonal and constant), so Y = q/6 = 1/2, 1/6, -1/6, -1/2; the torus weights give SU(2) content 2 and
    SU(3) content 1, 3, 3b, 1 (sl(3) weight multisets), i.e. C_0 = (2,1)_{1/2}, C_1 = (2,3)_{1/6},
    C_2 = (2,3b)_{-1/6}, C_3 = (2,1)_{-1/2}.
(2) Odd half C_1 + C_3 = (2,3)_{1/6} + (2,1)_{-1/2} = Q + L (both of odd grade, one chirality half for
    either epsilon); even half C_0 + C_2 = L* + Q*, of even grade.
(3) Duality on the section: the negated U(2) x U(3) torus weights of C_k equal the weights of C_(3-k) shifted
    by -(1,1,1,1,1) (the det(A) det(B) twist), which is trivial on S(U(2) x U(3)) (the trace-zero torus);
    so C_k* = C_(3-k) there, with the y-weights -(3 - 2k) = 3 - 2(3 - k); C_0 (the vacuum slot) is L*.
(4) The lattice condition 2t + 3 delta + q = 0 mod 6 on every C_k, with t the triality (sum of the U(3)
    weight mod 3, represented in {-1, 0, 1}), delta = 1 the SU(2) duality (sum of the U(2) weight mod 2)
    and q the y-weight, all read off the weights.
"""
from fractions import Fraction as F
from itertools import combinations

import GA  # noqa: F401
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


def y_weight(k):
    vals = set()
    for b in con_basis(k):
        img = unit_action(Y_GEN[0], Y_GEN[1], {b: 1})
        if set(img) - {b}:
            return None
        vals.add(img.get(b, 0))
    return vals.pop() if len(vals) == 1 else None


def content(k):
    ws = torus_weights(k)
    return su2_dim(ws), su3_content(ws), F(y_weight(k), 6)


def check_constituent_content_and_weights():
    premise("lepton.hyp-c-constituent")
    premise("lepton.imported-automorphism-group-section-hypercharge-generator")
    ok = [y_weight(k) for k in range(4)] == [3, 1, -1, -3]
    ok = ok and [content(k) for k in range(4)] == [(2, "1", F(1, 2)), (2, "3", F(1, 6)),
                                                   (2, "3b", F(-1, 6)), (2, "1", F(-1, 2))]
    ok = ok and [len(con_basis(k)) for k in range(4)] == [2, 6, 6, 2]
    _tp_rv = (ok); assert _tp_rv is not False, "check_constituent_content_and_weights"; return _tp_rv


def _conj(c):
    return (c[0], {"1": "1", "3": "3b", "3b": "3"}[c[1]], -c[2])


def check_odd_and_even_halves():
    premise("lepton.hyp-c-constituent")
    premise("lepton.imported-duality-pair-system")
    Q, L = (2, "3", F(1, 6)), (2, "1", F(-1, 2))
    odd = sorted(content(k) for k in range(4) if k % 2 == 1)
    even = sorted(content(k) for k in range(4) if k % 2 == 0)
    ok = odd == sorted([Q, L])
    ok = ok and even == sorted([_conj(L), _conj(Q)])
    ok = ok and content(0) == _conj(L) and content(2) == _conj(Q)
    ok = ok and sum(len(con_basis(k)) for k in (1, 3)) == 8 == sum(len(con_basis(k)) for k in (0, 2))
    _tp_rv = (ok); assert _tp_rv is not False, "check_odd_and_even_halves"; return _tp_rv


def check_duality_on_the_section():
    premise("lepton.imported-duality-pair-system")
    premise("lepton.imported-automorphism-group-section-hypercharge-generator")
    ok = True
    for k in range(4):
        neg = sorted(tuple(-x for x in w) for w in torus_weights(k))
        shifted = sorted(tuple(x - 1 for x in w) for w in torus_weights(3 - k))
        ok = ok and neg == shifted
        ok = ok and neg != torus_weights(3 - k)                  # not isomorphic before the section
        ok = ok and -y_weight(k) == y_weight(3 - k)
    # the twist det(A) det(B) has weight (1,1,1,1,1): zero on y = (3,3,-2,-2,-2) (the section) but not on
    # the K generator (1, 1, -1, -1, -1)
    twist = (1, 1, 1, 1, 1)
    ok = ok and sum(a * b for a, b in zip(twist, (3, 3, -2, -2, -2))) == 0
    ok = ok and sum(a * b for a, b in zip(twist, (1, 1, -1, -1, -1))) == -1
    _tp_rv = (ok); assert _tp_rv is not False, "check_duality_on_the_section"; return _tp_rv


def check_lattice_condition():
    premise("lepton.imported-automorphism-group-section-hypercharge-generator")
    ok = True
    triality = []
    for k in range(4):
        ws = torus_weights(k)
        t = {sum(w[2:]) % 3 for w in ws}
        d = {sum(w[:2]) % 2 for w in ws}
        ok = ok and len(t) == 1 and len(d) == 1
        t = t.pop()
        t = t - 3 if t == 2 else t
        delta = d.pop()
        triality.append(t)
        ok = ok and delta == 1 and (2 * t + 3 * delta + y_weight(k)) % 6 == 0
    _tp_rv = (ok and triality == [0, 1, -1, 0]); assert _tp_rv is not False, "check_lattice_condition"; return _tp_rv
