"""lepton.relative-handedness-slotted-free-sectors: exact checks.

Fields are read off actions, not typed: the slot sector C^2 (x) Lambda^k W with the unit action of (C)
(X on the slot once, Lambda^k(Y) on the pairs), the free sector Lambda^k W with the pair factor acting as
Lambda^k(lambda^-2 b) (y-weight -2 per pair); SU(2) dimension, SU(3) content (sl(3) weight multisets) and
hypercharge Y = q/6 come from the torus weights. Conjugation conjugates the content and negates Y. The four
anomaly sums of the imported Fact, for left-handed Weyl fields (colour c, SU(2) dimension d, Y):
[SU(3)]^2 U(1) = sum over coloured fields of d Y; [SU(2)]^2 U(1) = sum over doublets of dim(c) Y;
gravitational = sum of dim Y; cubic = sum of dim Y^3.
(1) Listing the free CS half (grades 0, 2) with the slot sector's CS-bar half (Q = C_1, L = C_3), and the free
    CS-bar half (grades 1, 3) conjugated: the list is Q, L, nu^c, u^c, d^c, e^c, i.e. (2,3)_{1/6},
    (2,1)_{-1/2}, (1,1)_0, (1,3b)_{-2/3}, (1,3b)_{1/3}, (1,1)_1, and all four sums vanish.
(2) The other listing gives Q, L, (3)_{-1/3}, (1)_{-1}, (1)_0, (3)_{2/3}: [SU(3)]^2 U(1) = 2/3, [SU(2)]^2 U(1)
    = 0, gravitational 0, cubic -4/9; its free part is the conjugate of the first list's free part.
(3) So exactly one of the two listings is anomaly-free, the one in which the free half of even grade sits
    with the slot fields of odd grade: a slot reverses the half (epsilon = -1); the bare free spinor (grade 0)
    is the neutrino singlet nu^c = (1,1)_0 and the bare slotted spinor C_0 is the antilepton (2,1)_{1/2}.
"""
from fractions import Fraction as F
from itertools import combinations

import GA  # noqa: F401
from tp_premise import premise

Y_GEN = ([[3, 0], [0, 3]], [[-2, 0, 0], [0, -2, 0], [0, 0, -2]])
DIM3 = {"1": 1, "3": 3, "3b": 3}


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


def slot_field(k):
    ws = torus_weights(k)
    q = {unit_action(Y_GEN[0], Y_GEN[1], {b: 1}).get(b) for b in con_basis(k)}
    return (su3_content(ws), su2_dim(ws), F(q.pop(), 6)) if len(q) == 1 else None


def free_field(k):
    S0 = list(combinations(range(3), k))
    ws, qs = [], set()
    for S in S0:
        w = []
        for t in range(3):
            img = derive(unit(3, t, t), S)
            w.append(img.get(S, 0))
        ws.append((0, 0) + tuple(w))
        qs.add(derive(Y_GEN[1], S).get(S, 0))
    return (su3_content(sorted(ws)), 1, F(qs.pop(), 6)) if len(qs) == 1 else None


def conj(f):
    return ({"1": "1", "3": "3b", "3b": "3"}[f[0]], f[1], -f[2])


def sums(fields):
    su3 = sum((d * Y for c, d, Y in fields if c != "1"), F(0))
    su2 = sum((DIM3[c] * Y for c, d, Y in fields if d == 2), F(0))
    grav = sum((DIM3[c] * d * Y for c, d, Y in fields), F(0))
    cube = sum((DIM3[c] * d * Y ** 3 for c, d, Y in fields), F(0))
    return (su3, su2, grav, cube)


def listing(free_with_slot):
    """Q, L, the free grades in free_with_slot unconjugated, the other free grades conjugated."""
    others = [k for k in range(4) if k not in free_with_slot]
    return [slot_field(1), slot_field(3)] + [free_field(k) for k in free_with_slot] + [conj(free_field(k)) for k in others]


def check_first_listing_is_one_generation_anomaly_free():
    premise("lepton.content-constituent-space")
    premise("lepton.imported-free-sector-anomaly-conditions")
    premise("lepton.hyp-c-constituent")
    ok = [free_field(k) for k in range(4)] == [("1", 1, F(0)), ("3", 1, F(-1, 3)), ("3b", 1, F(-2, 3)), ("1", 1, F(-1))]
    L1 = listing((0, 2))
    sm = [("3", 2, F(1, 6)), ("1", 2, F(-1, 2)), ("1", 1, F(0)), ("3b", 1, F(-2, 3)), ("3b", 1, F(1, 3)), ("1", 1, F(1))]
    ok = ok and L1 == sm and sums(L1) == (0, 0, 0, 0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_first_listing_is_one_generation_anomaly_free"; return _tp_rv


def check_second_listing_is_anomalous():
    premise("lepton.content-constituent-space")
    premise("lepton.imported-free-sector-anomaly-conditions")
    L1, L2 = listing((0, 2)), listing((1, 3))
    ok = L2[2:] == [("3", 1, F(-1, 3)), ("1", 1, F(-1)), ("1", 1, F(0)), ("3", 1, F(2, 3))]
    ok = ok and sums(L2) == (F(2, 3), 0, 0, F(-4, 9))
    ok = ok and sorted(L2[2:]) == sorted(conj(f) for f in L1[2:])
    _tp_rv = (ok); assert _tp_rv is not False, "check_second_listing_is_anomalous"; return _tp_rv


def check_consistency_fixes_relative_handedness():
    premise("lepton.hyp-c-constituent")
    premise("lepton.imported-free-sector-anomaly-conditions")
    free_ok = [w for w in ((0, 2), (1, 3)) if sums(listing(w)) == (0, 0, 0, 0)]
    ok = free_ok == [(0, 2)]
    slot_grades = (1, 3)
    # epsilon = -1: the anomaly-free listing pairs free grades of one parity with slot grades of the other
    ok = ok and all((a - b) % 2 == 1 for a in free_ok[0] for b in slot_grades)
    ok = ok and free_field(0) == ("1", 1, F(0)) and slot_field(0) == ("1", 2, F(1, 2))
    _tp_rv = (ok); assert _tp_rv is not False, "check_consistency_fixes_relative_handedness"; return _tp_rv
