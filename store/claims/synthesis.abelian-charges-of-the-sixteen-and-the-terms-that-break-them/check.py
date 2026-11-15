"""Abelian charges of the sixteen and the stored terms: exact checks.

Five-mode module Lambda(C^5) in the occupation basis (pair modes 1, 2, 3; slot modes 4, 5), v_a creation and
w_a contraction, as in the check of standard-model.proton-decay-only-through-slot-pair. The sixteen is the
even states; species by (slot number, pair number).
(1) The commutant of su(3) + su(2)_L + u(1)_Y on the sixteen has dimension six and is diagonal in the
    occupation basis; the six blocks have dimensions 6, 3, 3, 2, 1, 1.
(2) A charge is a vector (x_Q, x_u, x_d, x_L, x_e, x_nu, h_v, h_w). The pairing terms B(psi, a phi), a a slot
    operator, give the Dirac conditions; with h_v + h_w = 0 their solution space has dimension three and is
    spanned by Y, n_B, n_L; without it dimension four, and the extra charge has a nonzero colour coefficient.
(3) The Majorana element T = v_1 ... v_5 gives 2 x_nu = 0: the space drops to span{Y, n_B}.
(4) The 24 slot-pair root vectors carry a definite charge only for span{Y, B - L}.
(5) Mixed coefficients A_2 (weak isospin) and A_3 (colour): A_2(n_B) = A_2(n_L) = 2, zero on Y and B - L;
    the conditions together leave span{Y}. The unit of the module is not a Dirac charge, and Y, n_B, n_L,
    B - L are traceless on the sixteen.
(6) The equilibrium conditions of the check of dark-tower-matter.mirrors-composition are recomputed here as an
    exact kernel: B/(B - L) = 28/79 at three families and one doublet, 8/23 with two doublets, and
    (8 N_f + 4 N_H)/(22 N_f + 13 N_H) in four cases; with one doublet (B, L) = (0, -79) ends with B = 28 and
    (79, 79) with B = 0. Dirac, Majorana and the 24 root vectors alone leave span{Y}.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

MODES = (1, 2, 3, 4, 5)
PAIR, SLOT = (1, 2, 3), (4, 5)
EVEN = [frozenset(c) for r in (0, 2, 4) for c in combinations(MODES, r)]
SPECIES = ["Q", "u^c", "d^c", "L", "e^c", "nu^c"]
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}


def jk(S):
    return len(S & set(SLOT)), len(S & set(PAIR))


def sp(S):
    return SPECIES.index(NAMES[jk(S)])


def word(ops, st):
    """Apply a product of mode operators (rightmost first) to a state {set: coefficient}."""
    for kind, i in reversed(ops):
        out = {}
        for S, a in st.items():
            if kind == "v" and i not in S:
                T = S | {i}
            elif kind == "w" and i in S:
                T = S - {i}
            else:
                continue
            sign = -1 if sum(1 for j in S if j < i) % 2 else 1
            out[T] = out.get(T, 0) + sign * a
        st = out
    return {k: v for k, v in st.items() if v != 0}


def chi(S):
    return -(-1) ** jk(S)[0]


def bml(S):
    return 1 - F(2, 3) * jk(S)[1]


def n_b(S):
    return (bml(S) + chi(S)) / 4


def n_l(S):
    return (chi(S) - 3 * bml(S)) / 4


def hyp(S):
    return F(jk(S)[0] - 1, 2) + bml(S) / 2


def t3(S):
    return F((4 in S) - (5 in S), 2)


def lam(S):
    return (1 in S) - (2 in S)


def pairing(S, U):
    """B(e_S, e_U) of standard-model.invariant-pairing-five-modes."""
    if U != frozenset(MODES) - S:
        return 0
    lst = sorted(S) + sorted(U)
    inv = sum(1 for a in range(5) for b in range(a + 1, 5) if lst[a] > lst[b])
    return (-1) ** (len(S) * (len(S) - 1) // 2) * (-1) ** inv


def vec(fn, h):
    d = {}
    for S in EVEN:
        d[sp(S)] = F(fn(S))
    return [d[s] for s in range(6)] + [F(h), -F(h)]


def dirac_rows():
    rows = set()
    for kind in ("v", "w"):
        for i in SLOT:
            for T in EVEN:
                for U, c in word([(kind, i)], {T: F(1)}).items():
                    for S in EVEN:
                        if pairing(S, U) * c != 0:
                            r = [0] * 8
                            r[sp(S)] += 1
                            r[sp(T)] += 1
                            r[6 if kind == "v" else 7] += 1
                            rows.add(tuple(r))
    return [list(r) for r in sorted(rows)]


def majorana_rows():
    rows = set()
    top = [("v", i) for i in MODES]
    for T in EVEN:
        for U, c in word(top, {T: F(1)}).items():
            for S in EVEN:
                if pairing(S, U) * c != 0:
                    r = [0] * 8
                    r[sp(S)] += 1
                    r[sp(T)] += 1
                    rows.add(tuple(r))
    return [list(r) for r in sorted(rows)]


def mixing_rows():
    rows = []
    for a in PAIR:
        for i in SLOT:
            for ka in ("v", "w"):
                for ki in ("v", "w"):
                    trans = []
                    for S in EVEN:
                        for T in word([(ka, a), (ki, i)], {S: F(1)}):
                            r = [0] * 8
                            r[sp(T)] += 1
                            r[sp(S)] -= 1
                            trans.append(r)
                    rows += [[x - y for x, y in zip(r, trans[0])] for r in trans[1:]]
    return rows


def coefficient_rows():
    a2, a3 = [F(0)] * 8, [F(0)] * 8
    for S in EVEN:
        a2[sp(S)] += 4 * t3(S) ** 2
        a3[sp(S)] += lam(S) ** 2
    return a2, a3


def kernel(rows):
    return GA.field_kernel([[F(x) for x in r] for r in rows])


def inside(v, basis):
    return GA.field_rank(basis + [v]) == GA.field_rank(basis)


def spans(basis, vectors):
    return len(basis) == len(vectors) == GA.field_rank(vectors) and all(inside(v, basis) for v in vectors)


Y, NB, NL, BML = vec(hyp, F(1, 2)), vec(n_b, 0), vec(n_l, 0), vec(bml, 0)
ONE = vec(lambda S: 1, 0)


def check_commutant_of_the_gauge_algebra_is_six_dimensional():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")

    def weight(S):
        return (lam(S), (2 in S) - (3 in S), t3(S), hyp(S))

    units = [(S, T) for S in EVEN for T in EVEN if weight(S) == weight(T)]
    roots = [[("v", a), ("w", b)] for a in PAIR for b in PAIR if a != b]
    roots += [[("v", 4), ("w", 5)], [("v", 5), ("w", 4)]]
    rows = []
    for E in roots:
        img = {S: word(E, {S: F(1)}) for S in EVEN}
        for A in EVEN:
            for B in EVEN:
                row = [F(0)] * len(units)
                for c, (S, T) in enumerate(units):
                    if S == A:
                        row[c] += img[B].get(T, 0)
                    if T == B:
                        row[c] -= img[S].get(A, 0)
                if any(row):
                    rows.append(row)
    ker = GA.field_kernel(rows)
    diagonal = all(v == 0 or units[c][0] == units[c][1] for k in ker for c, v in enumerate(k))
    dims = sorted(sum(1 for S in EVEN if sp(S) == s) for s in range(6))
    ok = len(EVEN) == 16 and len(units) == 16 and len(roots) == 8 and len(ker) == 6 and diagonal
    ok = ok and dims == [1, 1, 2, 3, 3, 6]
    ok = ok and [vec(hyp, 0)[s] for s in range(6)] == [F(1, 6), F(-2, 3), F(1, 3), F(-1, 2), F(1), F(0)]
    GA.check("sixteen: commutant of su(3)+su(2)_L+u(1)_Y has dimension 6, diagonal; blocks 6,3,3,2,1,1", ok)
    return ok


def check_dirac_majorana_and_mixing_conditions():
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.majorana-element")
    premise("standard-model.proton-decay-only-through-slot-pair")
    D = dirac_rows()
    one_doublet = D + [[0, 0, 0, 0, 0, 0, 1, 1]]
    M = majorana_rows()
    X = mixing_rows()
    ok = len(D) == 4 and M == [[0, 0, 0, 0, 0, 2, 0, 0]]
    ok = ok and spans(kernel(one_doublet), [Y, NB, NL])
    ok = ok and len(kernel(D)) == 4
    ok = ok and spans(kernel(one_doublet + M), [Y, NB])
    ok = ok and spans(kernel(one_doublet + X), [Y, BML])
    ok = ok and spans(kernel(one_doublet + M + X), [Y])
    unit = ONE[:6] + [F(-2), F(-2)]
    ok = ok and not inside(ONE, kernel(one_doublet)) and not inside(ONE, kernel(D))
    ok = ok and inside(unit, kernel(D)) and spans(kernel(D), [Y, NB, NL, unit])
    ok = ok and BML == [a - b for a, b in zip(NB, NL)]
    GA.check("sixteen: Dirac charges span{Y, n_B, n_L}; Majorana leaves {Y, n_B}; mixing leaves {Y, B-L}", ok)
    return ok


def check_mixed_coefficients_leave_hypercharge_only():
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.majorana-element")
    a2, a3 = coefficient_rows()
    dot = lambda r, v: sum(x * y for x, y in zip(r, v))
    D = dirac_rows()
    one_doublet = D + [[0, 0, 0, 0, 0, 0, 1, 1]]
    ok = a2[:6] == [6, 0, 0, 2, 0, 0] and a3[:6] == [4, 2, 2, 0, 0, 0]
    ok = ok and [dot(a2, v) for v in (Y, NB, NL, BML, ONE)] == [0, 2, 2, 0, 8]
    ok = ok and [dot(a3, v) for v in (Y, NB, NL, BML, ONE)] == [0, 0, 0, 0, 8]
    ok = ok and spans(kernel(one_doublet + [a2]), [Y, BML])
    ok = ok and spans(kernel(one_doublet + [a2] + majorana_rows()), [Y])
    ok = ok and len(kernel(D + [a3])) == 3 and len(kernel(D)) == 4
    ok = ok and all(sum(fn(S) for S in EVEN) == 0 for fn in (hyp, n_b, n_l, bml))
    GA.check("sixteen: A_2(n_B) = A_2(n_L) = 2, A_2 = 0 on Y and B-L; all conditions leave span{Y}", ok)
    return ok


def equilibrium_ratio(nf, nh):
    """B/(B - L) and L/B on the kernel of the five equilibrium conditions; columns mu_Q, mu_u, mu_d, mu_L, mu_e,
    mu_H."""
    rows = [
        [3 * nf, 0, 0, nf, 0, 0],
        [-1, 1, 0, 0, 0, -1],
        [-1, 0, 1, 0, 0, 1],
        [0, 0, 0, -1, 1, 1],
        [nf, 2 * nf, -nf, -nf, -nf, 2 * nh],
    ]
    ker = GA.field_kernel([[F(x) for x in r] for r in rows])
    if len(ker) != 1:
        return None
    mq, mu, md, ml, me, mh = ker[0]
    b = nf * (2 * mq + mu + md)
    lep = nf * (2 * ml + me)
    return b / (b - lep), lep / b


def check_equilibrium_generates_and_erases_baryon_number():
    premise("dark-tower-matter.mirrors-composition")
    premise("standard-model.bidoublet-complex")
    one, two = equilibrium_ratio(3, 1), equilibrium_ratio(3, 2)
    ok = one == (F(28, 79), F(-51, 28)) and two is not None and two[0] == F(8, 23)
    ok = ok and all(equilibrium_ratio(nf, nh)[0] == F(8 * nf + 4 * nh, 22 * nf + 13 * nh)
                    for nf in (2, 3) for nh in (1, 2))
    c = one[0]
    final = lambda B, L: c * (B - L)
    ok = ok and final(0, -79) == 28 and final(79, 79) == 0 and final(28, -51) == 28
    GA.check("equilibrium kernel: B/(B-L) = 28/79 (one doublet), 8/23 (two); (0,-79) -> 28, (79,79) -> 0", ok)
    return ok
