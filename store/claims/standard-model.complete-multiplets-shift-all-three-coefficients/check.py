"""standard-model.complete-multiplets-shift-all-three-coefficients: exact checks.

The Cartan elements X_2 = T_3 = diag(0, 0, 0, 1/2, -1/2), X_3 = diag(1/2, -1/2, 0, 0, 0) and Y = diag(-1/3, -1/3,
-1/3, 1/2, 1/2) of su(5), the fundamental restricting to (1,3)_{-1/3} + (2,1)_{1/2}; T_i(rho) = sum over the
weights w of rho of X_i(w)^2, with T_1 = (3/5) sum Y(w)^2 (the normalisation of the trace-ratio Fact).
(1) General argument, finite core: the quadratic forms on the traceless diagonal of su(5) invariant under
    the Weyl group S_5 form a one-dimensional space (exact kernel of the invariance equations on the
    4 x 4 symmetric matrices), and X_1 = sqrt(3/5) Y, X_2, X_3 have equal norm 1/2 in the 5; the weight
    multisets of the representations below are S_5-invariant. Hence tr_rho(X_i^2) is one number.
(2) Representations, by their weights: SU(5) 5, 5bar, 10 = Lambda^2 5, 10bar, 15 = S^2 5, 24 = adjoint, and
    Spin(10) 16 (Lambda^even 5 twisted by det^-1/2, the twist invisible to traceless X_i), 10 = 5 + 5bar,
    45 = 24 + 10 + 10bar + 1: T_1 = T_2 = T_3 = 1/2, 1/2, 3/2, 3/2, 7/2, 5, 2, 1, 8.
(3) Shifts by the coefficient-sum Fact (2/3 T per Weyl fermion, 1/3 T per complex scalar): Weyl 10 gives
    (1,1,1), scalar 5bar (1/6)(1,1,1), Weyl 24 (10/3)(1,1,1), a Weyl 16 (4/3)(1,1,1), three scalar 16s
    2(1,1,1); control: the gauginos alone (adjoints of each factor) give (0, 4/3, 2), not a multiple of (1,1,1).
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations

import GA
from tp_premise import premise

X2 = (F(0), F(0), F(0), F(1, 2), F(-1, 2))
X3 = (F(1, 2), F(-1, 2), F(0), F(0), F(0))
YD = (F(-1, 3), F(-1, 3), F(-1, 3), F(1, 2), F(1, 2))


def e(i):
    return tuple(1 if j == i else 0 for j in range(5))


def addw(*ws):
    return tuple(sum(c) for c in zip(*ws))


def neg(w):
    return tuple(-x for x in w)


def reps():
    five = Counter(e(i) for i in range(5))
    fiveb = Counter(neg(e(i)) for i in range(5))
    ten = Counter(addw(e(i), e(j)) for i, j in combinations(range(5), 2))
    tenb = Counter(neg(w) for w in ten.elements())
    fifteen = Counter(addw(e(i), e(j)) for i in range(5) for j in range(i, 5))
    adj = Counter(addw(e(i), neg(e(j))) for i in range(5) for j in range(5) if i != j)
    adj[(0, 0, 0, 0, 0)] += 4
    sixteen = Counter(tuple(1 if i in S else 0 for i in range(5))
                      for k in (0, 2, 4) for S in combinations(range(5), k))
    so10_vec = five + fiveb
    so10_adj = adj + ten + tenb + Counter({(0, 0, 0, 0, 0): 1})
    return {"5": five, "5b": fiveb, "10": ten, "10b": tenb, "15": fifteen, "24": adj,
            "16": sixteen, "10v": so10_vec, "45": so10_adj}


def pair(X, w):
    return sum((a * b for a, b in zip(X, w)), F(0))


def indices(ch):
    t1 = F(3, 5) * sum((m * pair(YD, w) ** 2 for w, m in ch.items()), F(0))
    t2 = sum((m * pair(X2, w) ** 2 for w, m in ch.items()), F(0))
    t3 = sum((m * pair(X3, w) ** 2 for w, m in ch.items()), F(0))
    return (t1, t2, t3)


def check_invariant_form_is_unique():
    premise("standard-model.imported-invariant-forms-simple-lie-algebra")
    premise("standard-model.imported-one-loop-running-trace-ratio")
    # traceless basis h_a = e_a - e_5 (a = 0..3); a quadratic form is a symmetric 4 x 4 matrix S (10 unknowns)
    idx = [(a, b) for a in range(4) for b in range(a, 4)]

    def coords(v):                       # traceless v = sum c_a h_a: c_a = v_a for a < 4
        return v[:4]

    rows = []
    for (p, q) in [(0, 1), (1, 2), (2, 3), (3, 4)]:        # adjacent transpositions generate S_5
        for (a, b) in idx:
            ha = [F(1) if i == a else F(0) for i in range(5)]
            hb = [F(1) if i == b else F(0) for i in range(5)]
            ha[4] -= 1
            hb[4] -= 1
            sa, sb = list(ha), list(hb)
            sa[p], sa[q] = sa[q], sa[p]
            sb[p], sb[q] = sb[q], sb[p]
            ca, cb = coords(sa), coords(sb)
            row = [F(0)] * len(idx)
            # S(sigma h_a, sigma h_b) - S(h_a, h_b) = 0, bilinear in the coordinates
            for k, (i, j) in enumerate(idx):
                w = ca[i] * cb[j] + (ca[j] * cb[i] if i != j else 0)
                row[k] += w
            row[idx.index((a, b))] -= 1
            rows.append(row)
    ok = len(GA.field_kernel(rows)) == 1
    norms = [sum(x * x for x in X) for X in (X2, X3)] + [F(3, 5) * sum(x * x for x in YD)]
    ok = ok and norms == [F(1, 2)] * 3
    ok = ok and all(sum(X) == 0 for X in (X2, X3, YD))
    R = reps()
    for ch in R.values():
        for perm in permutations(range(5)):
            if Counter(tuple(w[perm[i]] for i in range(5)) for w in ch.elements()) != ch:
                ok = False
                break
    GA.check("one Weyl-invariant quadratic form on the Cartan of su(5); X_1, X_2, X_3 of equal norm", ok)
    return ok


def check_indices_equal_on_complete_multiplets():
    premise("standard-model.imported-one-loop-running-trace-ratio")
    R = reps()
    want = {"5": F(1, 2), "5b": F(1, 2), "10": F(3, 2), "10b": F(3, 2), "15": F(7, 2), "24": F(5),
            "16": F(2), "10v": F(1), "45": F(8)}
    dims = {"5": 5, "5b": 5, "10": 10, "10b": 10, "15": 15, "24": 24, "16": 16, "10v": 10, "45": 45}
    ok = True
    for name, ch in R.items():
        ok = ok and sum(ch.values()) == dims[name] and indices(ch) == (want[name],) * 3
    GA.check("T_1 = T_2 = T_3 on representations of SU(5) and Spin(10)", ok)
    return ok


def check_shifts_are_multiples_of_one_one_one():
    premise("standard-model.imported-coefficient-sum-indices")
    R = reps()

    def shift(ch, weyl, copies=1):
        w = F(2, 3) if weyl else F(1, 3)
        return tuple(copies * w * t for t in indices(ch))

    ok = shift(R["10"], True) == (F(1),) * 3
    ok = ok and shift(R["5b"], False) == (F(1, 6),) * 3
    ok = ok and shift(R["24"], True) == (F(10, 3),) * 3
    ok = ok and shift(R["16"], True) == (F(4, 3),) * 3
    ok = ok and shift(R["16"], False, 3) == (F(2),) * 3
    # control: the gauginos alone, the adjoints of SU(3), SU(2) and U(1) inside the 24 (by weights)
    gl = Counter(addw(e(i), neg(e(j))) for i in range(3) for j in range(3) if i != j)
    gl[(0, 0, 0, 0, 0)] += 2
    wino = Counter([addw(e(3), neg(e(4))), addw(e(4), neg(e(3))), (0, 0, 0, 0, 0)])
    bino = Counter({(0, 0, 0, 0, 0): 1})
    gauginos = shift(gl + wino + bino, True)
    ok = ok and gauginos == (F(0), F(4, 3), F(2)) and len(set(gauginos)) == 3
    GA.check("complete multiplets shift (b_1, b_2, b_3) by c(1,1,1), c = (2/3) T or (1/3) T", ok)
    return ok
