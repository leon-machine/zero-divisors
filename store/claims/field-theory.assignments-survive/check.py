"""field-theory.assignments-survive: exact checks.

One generation in T12's listing (a): Q (2, 3, 1/6), L (2, 1, -1/2), u^c (1, 3bar, -2/3), d^c (1, 3bar, 1/3),
e^c (1, 1, 1), nu^c (1, 1, 0). Conjugating a multiplet sends Y -> -Y and 3 <-> 3bar (the SU(2) doublet is
self-conjugate). Anomaly conditions: [SU(3)]^2 U(1), [SU(2)]^2 U(1), gravitational, cubic U(1), and [SU(3)]^3
(A(3) = 1, A(3bar) = -1).
(1) Listing (a) and its conjugate (b) satisfy all five; the mixed listing (doublets conjugated, singlets not) gives
    [SU(3)]^2 U(1) = -2/3, cubic 4/9, [SU(3)]^3 = -4. Read as right-handed (contributions counted with -1), the
    conjugate of (a) is anomaly-free as well.
(2) Of the 64 conjugation patterns exactly four are anomaly-free: (a) and (b), each with nu^c either way (the only
    multiplet that is its own conjugate).
(3) With span{1, I4} as the numbers: the conjugate of the SU(2) doublet is equivalent to it (intertwiner space of
    real dimension 2 = complex dimension 1, solved exactly: M Xbar = X M for the three i sigma/2), while the
    conjugate of the SU(3) triplet admits no nonzero intertwiner (the 18 real unknowns are forced to zero): an
    I4-antilinear reading is the outer automorphism Y -> -Y, 3 <-> 3bar.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
LIST_A = [("Q", 2, "3", F(1, 6)), ("L", 2, "1", F(-1, 2)), ("uc", 1, "3b", F(-2, 3)), ("dc", 1, "3b", F(1, 3)),
          ("ec", 1, "1", F(1)), ("nuc", 1, "1", F(0))]
DIM3 = {"1": 1, "3": 3, "3b": 3}
FLIP3 = {"3": "3b", "3b": "3", "1": "1"}


def _conj(lst):
    return [(n + "~", d, FLIP3[c], -Y) for (n, d, c, Y) in lst]


def _anoms(lst, sign=None):
    sg = sign or [1] * len(lst)
    su3 = sum((s * d * Y for s, (n, d, c, Y) in zip(sg, lst) if c != "1"), F(0))
    su2 = sum((s * DIM3[c] * Y for s, (n, d, c, Y) in zip(sg, lst) if d == 2), F(0))
    grav = sum((s * d * DIM3[c] * Y for s, (n, d, c, Y) in zip(sg, lst)), F(0))
    cub = sum((s * d * DIM3[c] * Y ** 3 for s, (n, d, c, Y) in zip(sg, lst)), F(0))
    su3c = sum(s * d * {"3": 1, "3b": -1, "1": 0}[c] for s, (n, d, c, Y) in zip(sg, lst))
    return (su3, su2, grav, cub, su3c)


def _intertwiners(gens):
    """Real dimension of {M : M conj(X) = X M for all X}, M an n x n matrix over Q(i)."""
    n = len(gens[0])
    unk = [(i, j, p) for i in range(n) for j in range(n) for p in (0, 1)]
    pos = {u: t for t, u in enumerate(unk)}
    rows = []
    for X in gens:
        Xc = [[z.conj() for z in r] for r in X]
        for i in range(n):
            for j in range(n):
                re_row, im_row = [F(0)] * len(unk), [F(0)] * len(unk)
                for kk in range(n):
                    for (src, coef) in (((i, kk), Xc[kk][j]), ((kk, j), QI(0) - X[i][kk])):
                        ir, ii = pos[(src[0], src[1], 0)], pos[(src[0], src[1], 1)]
                        re_row[ir] += coef.re
                        re_row[ii] -= coef.im
                        im_row[ir] += coef.im
                        im_row[ii] += coef.re
                rows.extend([re_row, im_row])
    return len(unk) - GA.rank_of_vectors(rows)


def _su2():
    Z, O, I = QI(0), QI(1), QI(0, 1)
    sig = [[[Z, O], [O, Z]], [[Z, QI(0, -1)], [I, Z]], [[O, Z], [Z, QI(-1)]]]
    return [[[QI(0, F(1, 2)) * z for z in r] for r in s] for s in sig]


def _su3():
    def M3(entries):
        m = [[QI(0)] * 3 for _ in range(3)]
        for (i, j, z) in entries:
            m[i][j] = z
        return m
    O, I, mI = QI(1), QI(0, 1), QI(0, -1)
    lam = [M3([(0, 1, O), (1, 0, O)]), M3([(0, 1, mI), (1, 0, I)]), M3([(0, 0, O), (1, 1, QI(-1))]),
           M3([(0, 2, O), (2, 0, O)]), M3([(0, 2, mI), (2, 0, I)]), M3([(1, 2, O), (2, 1, O)]),
           M3([(1, 2, mI), (2, 1, I)]), M3([(0, 0, O), (1, 1, O), (2, 2, QI(-2))])]
    return [[[QI(0, F(1, 2)) * z for z in r] for r in l] for l in lam]


def check_listing_and_conjugate_anomaly_free():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    premise("standard-model.imported-anomaly-coefficients")
    ok = _anoms(LIST_A) == (0, 0, 0, 0, 0) and _anoms(_conj(LIST_A)) == (0, 0, 0, 0, 0)
    mixed = _anoms(_conj(LIST_A[:2]) + LIST_A[2:])
    ok = ok and (mixed[0], mixed[3], mixed[4]) == (F(-2, 3), F(4, 9), -4)
    ok = ok and _anoms(_conj(LIST_A), sign=[-1] * 6) == (0, 0, 0, 0, 0)
    GA.check("listing (a) and its conjugate are anomaly-free; the mixed listing is not (-2/3, 4/9, -4)", ok)
    return ok


def check_exactly_four_patterns():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    premise("standard-model.imported-anomaly-coefficients")
    free = []
    for mask in range(64):
        lst = [_conj([f])[0] if (mask >> i) & 1 else f for i, f in enumerate(LIST_A)]
        if _anoms(lst) == (0, 0, 0, 0, 0):
            free.append(mask)
    ok = free == [0, 31, 32, 63]
    ok = ok and len(free) == 4 and all((m & 31) in (0, 31) for m in free)
    GA.check("exactly four of 64 conjugation patterns are anomaly-free: (a), (b), nu^c either way", ok)
    return ok


def check_conjugate_representations_with_i4():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    d2 = _intertwiners(_su2())
    d3 = _intertwiners(_su3())
    eps = [[QI(0), QI(1)], [QI(-1), QI(0)]]
    epsinv = [[QI(0), QI(-1)], [QI(1), QI(0)]]
    mm = lambda A, B: [[sum((A[i][k] * B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))]
                       for i in range(len(A))]
    ok = d2 == 2 and d3 == 0
    ok = ok and all(mm(mm(eps, [[z.conj() for z in r] for r in X]), epsinv) == X for X in _su2())
    GA.check("conj(2) = 2 through epsilon (complex dimension 1); conj(3) has no intertwiner with 3", ok)
    return ok
