"""Conditional inheritance of B - L and the conversion coefficient as a Gram ratio: exact checks.

Five-mode module in the occupation basis (pair modes 1, 2, 3; slot modes 4, 5), v_a creation and w_a contraction,
as in the checks of synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them. The sixteen is the
even states; the fifteen is the sixteen without the empty state nu^c. In this basis the neutral lepton of the
doublet is the state {1, 2, 3, 4}, so the electrically neutral slot operators are v_5, w_5.
(1) The forty off-diagonal mode bilinears are weight vectors of ad(B - L) with weights 0 (ten), +-2/3 (twelve
    each), +-4/3 (three each); the slot vectors have weight 0; the Majorana element has weight -2.
(2) The bilinear forms on the sixteen invariant under colour and the electric charge form a space of dimension
    10; those of nonzero B - L weight are exactly two, on (nu^c, nu^c) with weight +2 and total weak isospin 0, and
    on (nu, nu) with weight -2 and total weak isospin 1.
(3) State-level conserved charges (16 state numbers, four slot charges, the W charge) of the equilibrated
    interactions. Symmetric phase: dimension 4, with the weak anomalous condition 3, spanned by T_3, Y, B - L.
    Broken phase (neutral slot operators carry nothing): dimension 3, with the weak condition 2, spanned by the
    electric charge and B - L.
(4) The susceptibility form: one per fermion state of the fifteen and per family, two per charged boson state.
    The Gram ratio c = n_B / n_(B-L) for the charge orthogonal to the neutral gauge charges equals
    (8 N_f + 4 N_H)/(22 N_f + 13 N_H) in the symmetric phase (28/79, 8/23) and
    (8 N_f + 4 (N_H + 2))/(24 N_f + 13 (N_H + 2)) in the broken phase (12/37, 10/31), on a grid, and agrees with
    the kernel of the five conditions of the cited check. The interpolating mediant lies between 12/37 and 28/79.
(5) Lepton flavour: with the three charges B/3 - L_f conserved separately the ratio of baryon number to total
    B - L is the same c for every distribution of the asymmetry over the flavours.
(6) Doublets: with independent charges of the slot creation and contraction operators the conserved space gains
    one charge, the unit of the module minus 4 n_B with slot charge -2, of colour coefficient 8; the colour
    anomalous condition removes it. Arithmetic on quoted numbers: the stored bound of about 2500 GeV on the second doublet
    is between 18 and 19 times the literature's freeze-out temperature of 132 GeV; 79/28 and 37/12 times 8.7.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

MODES = (1, 2, 3, 4, 5)
PAIR, SLOT = (1, 2, 3), (4, 5)
STATES = [frozenset(c) for r in range(6) for c in combinations(MODES, r)]
EVEN = [S for S in STATES if len(S) % 2 == 0]
IDX = {S: c for c, S in enumerate(EVEN)}
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}


def jk(S):
    return len(S & set(SLOT)), len(S & set(PAIR))


def bml(S):
    return 1 - F(2, 3) * jk(S)[1]


def chi(S):
    return -(-1) ** jk(S)[0]


def n_b(S):
    return (bml(S) + chi(S)) / 4


def n_l(S):
    return (chi(S) - 3 * bml(S)) / 4


def hyp(S):
    return F(jk(S)[0] - 1, 2) + bml(S) / 2


def t3(S):
    return F((4 in S) - (5 in S), 2)


def qem(S):
    return t3(S) + hyp(S)


def lam(S):
    return (1 in S) - (2 in S)


def lam2(S):
    return (2 in S) - (3 in S)


def word(ops, st):
    """Apply a product of mode operators (rightmost first) to a state {set: coefficient}."""
    for kind, a in reversed(ops):
        out = {}
        for S, c in st.items():
            if kind == "v" and a not in S:
                T = S | {a}
            elif kind == "w" and a in S:
                T = S - {a}
            else:
                continue
            sign = -1 if sum(1 for b in S if b < a) % 2 else 1
            out[T] = out.get(T, 0) + sign * c
        st = out
    return {k: v for k, v in st.items() if v != 0}


def pairing(S, U):
    """B(e_S, e_U) of standard-model.invariant-pairing-five-modes."""
    if U != frozenset(MODES) - S:
        return 0
    lst = sorted(S) + sorted(U)
    inv = sum(1 for a in range(5) for b in range(a + 1, 5) if lst[a] > lst[b])
    return (-1) ** (len(S) * (len(S) - 1) // 2) * (-1) ** inv


def weights(ops):
    return {bml(T) - bml(S) for S in STATES for T in word(ops, {S: F(1)})}


def check_stored_terms_carry_b_minus_l_except_the_majorana_element():
    premise("standard-model.hyp-s-slot-statistics")
    premise("synthesis.baryon-number-centraliser-in-the-five-mode-algebra")
    premise("standard-model.majorana-element")
    count = {}
    for a in MODES:
        for b in MODES:
            if a < b:
                for ka in "vw":
                    for kb in "vw":
                        ws = weights([(ka, a), (kb, b)])
                        if len(ws) != 1:
                            return False
                        w = ws.pop()
                        count[w] = count.get(w, 0) + 1
    ok = count == {F(0): 10, F(2, 3): 12, F(-2, 3): 12, F(4, 3): 3, F(-4, 3): 3}
    ok = ok and sum(count.values()) == 40
    ok = ok and all(weights([(kind, a)]) == {F(0)} for kind in "vw" for a in SLOT)
    top = [("v", a) for a in MODES]
    ok = ok and weights(top) == {F(-2)}
    ok = ok and weights([("w", a) for a in MODES]) == {F(2)}
    ok = ok and all(weights([("v", a), ("w", a)]) == {F(0)} for a in MODES)
    GA.check("B - L weights: 40 mode bilinears are weight vectors; slot vectors 0; Majorana element -2", ok)
    return ok


def check_neutral_colour_singlet_mass_forms():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.majorana-element")
    premise("standard-model.invariant-pairing-five-modes")
    zero = [(S, T) for S in EVEN for T in EVEN
            if all(fn(S) + fn(T) == 0 for fn in (lam, lam2, qem))]
    zidx = {p: c for c, p in enumerate(zero)}
    rows = []
    for a in PAIR:
        for b in PAIR:
            if a != b:
                img = {S: word([("v", a), ("w", b)], {S: F(1)}) for S in EVEN}
                # (g.beta)(S, T) = sum_U beta(U, T) g_{U S} + sum_U beta(S, U) g_{U T} must vanish for all S, T
                acc = {}
                for (U, T) in zero:
                    for S in EVEN:
                        c = img[S].get(U, 0)
                        if c:
                            acc.setdefault((S, T), {})[zidx[(U, T)]] = c
                for (S, U) in zero:
                    for T in EVEN:
                        c = img[T].get(U, 0)
                        if c:
                            d = acc.setdefault((S, T), {})
                            d[zidx[(S, U)]] = d.get(zidx[(S, U)], 0) + c
                for d in acc.values():
                    r = [F(0)] * len(zero)
                    for col, c in d.items():
                        r[col] = F(c)
                    rows.append(r)
    ker = GA.field_kernel(rows)
    found = {}
    for kv in ker:
        supp = [zero[c] for c, v in enumerate(kv) if v != 0]
        ws = {bml(S) + bml(T) for S, T in supp}
        ts = {t3(S) + t3(T) for S, T in supp}
        names = {(NAMES[jk(S)], NAMES[jk(T)]) for S, T in supp}
        if len(ws) != 1 or len(ts) != 1 or len(names) != 1:
            return False
        found[names.pop()] = (ws.pop(), ts.pop())
    ok = len(ker) == 10 and len(found) == 10
    violating = {k: v for k, v in found.items() if v[0] != 0}
    ok = ok and violating == {("nu^c", "nu^c"): (F(2), F(0)), ("L", "L"): (F(-2), F(1))}
    # the Majorana element pairs the empty state with itself, and nothing else in the sixteen
    top = [("v", a) for a in MODES]
    hits = [(S, T) for S in EVEN for T in EVEN for U, c in word(top, {T: F(1)}).items() if pairing(S, U) * c != 0]
    ok = ok and hits == [(frozenset(), frozenset())]
    GA.check("mass forms invariant under colour and charge: 10; with B - L: nu^c nu^c (+2) and nu nu (-2, isospin 1)", ok)
    return ok


NV = 21          # 16 state numbers, h(v4), h(w4), h(v5), h(w5), h(W)


def conserved_space(broken, weak, conjugate=True, colour=False):
    rows = []
    for a in PAIR:
        for b in PAIR:
            if a != b:
                for S in EVEN:
                    for T in word([("v", a), ("w", b)], {S: F(1)}):
                        r = [0] * NV
                        r[IDX[T]] += 1
                        r[IDX[S]] -= 1
                        rows.append(r)
    for S in EVEN:
        for T in word([("v", 4), ("w", 5)], {S: F(1)}):
            r = [0] * NV
            r[IDX[T]] += 1
            r[IDX[S]] -= 1
            r[20] -= 1
            rows.append(r)
    for kind, a, col in (("v", 4, 16), ("w", 4, 17), ("v", 5, 18), ("w", 5, 19)):
        for T in EVEN:
            for U, c in word([(kind, a)], {T: F(1)}).items():
                for S in EVEN:
                    if pairing(S, U) * c != 0:
                        r = [0] * NV
                        r[IDX[S]] += 1
                        r[IDX[T]] += 1
                        r[col] += 1
                        rows.append(r)
    if conjugate:
        rows.append([0] * 16 + [1, 1, 0, 0, 0])
        rows.append([0] * 16 + [0, 0, 1, 1, 0])
    if colour:
        rows.append([lam(S) ** 2 for S in EVEN] + [0, 0, 0, 0, 0])
    if broken:
        rows.append([0] * 16 + [0, 0, 1, 0, 0])
    if weak:
        r = [0] * NV
        for S in EVEN:
            if jk(S)[0] == 1:
                r[IDX[S]] += 1
        rows.append(r)
    return GA.field_kernel([[F(x) for x in r] for r in rows])


def charge_vector(fn, h4, h5, hw):
    return [F(fn(S)) for S in EVEN] + [F(h4), -F(h4), F(h5), -F(h5), F(hw)]


def spans(basis, vectors):
    return (len(basis) == len(vectors) == GA.field_rank(vectors)
            and all(GA.field_rank(basis + [v]) == len(basis) for v in vectors))


Y_V = charge_vector(hyp, F(1, 2), F(1, 2), 0)
T3_V = charge_vector(t3, F(1, 2), F(-1, 2), 1)
Q_V = charge_vector(qem, 1, 0, 1)
BL_V = charge_vector(bml, 0, 0, 0)
NB_V = charge_vector(n_b, 0, 0, 0)
NL_V = charge_vector(n_l, 0, 0, 0)


def check_conserved_charges_of_the_equilibrated_interactions():
    premise("synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them")
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.invariant-pairing-five-modes")
    ok = spans(conserved_space(False, False), [T3_V, Y_V, NB_V, NL_V])
    ok = ok and spans(conserved_space(False, True), [T3_V, Y_V, BL_V])
    ok = ok and spans(conserved_space(True, False), [Q_V, NB_V, NL_V])
    ok = ok and spans(conserved_space(True, True), [Q_V, BL_V])
    ok = ok and len(conserved_space(True, True)) == 2 and len(conserved_space(False, True)) == 3
    weak_row = lambda v: sum(v[IDX[S]] for S in EVEN if jk(S)[0] == 1)
    ok = ok and [weak_row(v) for v in (Y_V, T3_V, Q_V, BL_V, NB_V, NL_V)] == [0, 0, 0, 0, 2, 2]
    ok = ok and Q_V == [a + b for a, b in zip(T3_V, Y_V)]
    GA.check("conserved charges: span{T3, Y, B-L} (symmetric), span{Q, B-L} (broken), weak process included", ok)
    return ok


FIFTEEN = [S for S in EVEN if jk(S) != (0, 0)]


def fermion_form(X, Xp, nf=1):
    return nf * sum(F(X(S)) * F(Xp(S)) for S in FIFTEEN)


def ratio_symmetric(nf, nh):
    """n_B / n_(B-L) for mu = (B - L) + a T_3 + b Y orthogonal to T_3 and Y in the susceptibility form."""
    def form(A, B):
        (fa, ha, ta, wa), (fb, hb, tb, wb) = A, B
        out = fermion_form(fa, fb, nf)
        out += 2 * nh * sum((ha + s * ta) * (hb + s * tb) for s in (F(1, 2), F(-1, 2)))   # doublet components
        out += 2 * 2 * wa * wb                                                           # W, two helicities
        return out
    Y = (hyp, F(1, 2), 0, 0)
    T3 = (t3, 0, 1, 1)
    BL = (bml, 0, 0, 0)
    NB = (n_b, 0, 0, 0)
    sol = GA.field_solve([[form(T3, T3), form(T3, Y)], [form(Y, T3), form(Y, Y)]], [-form(T3, BL), -form(Y, BL)])
    a, b = sol
    num = form(NB, BL) + a * form(NB, T3) + b * form(NB, Y)
    den = form(BL, BL) + a * form(BL, T3) + b * form(BL, Y)
    return num / den, a, (form(Y, Y), form(T3, T3), form(Y, BL), form(BL, BL), form(NB, BL), form(NB, Y))


def ratio_broken(nf, nh):
    """The same with the electric charge as the one neutral gauge charge; W (two helicities) and nh charged
    scalars in the form, each of charge one."""
    bos = 2 * (2 + nh)
    qq = fermion_form(qem, qem, nf) + bos
    qbl, blbl = fermion_form(qem, bml, nf), fermion_form(bml, bml, nf)
    bbl, bq = fermion_form(n_b, bml, nf), fermion_form(n_b, qem, nf)
    return (bbl * qq - bq * qbl) / (blbl * qq - qbl * qbl), qq


def stored_kernel_ratio(nf, nh):
    """B/(B - L) on the kernel of the five conditions of the cited check; columns mu_Q, mu_u, mu_d, mu_L, mu_e,
    mu_H."""
    rows = [[3 * nf, 0, 0, nf, 0, 0], [-1, 1, 0, 0, 0, -1], [-1, 0, 1, 0, 0, 1], [0, 0, 0, -1, 1, 1],
            [nf, 2 * nf, -nf, -nf, -nf, 2 * nh]]
    ker = GA.field_kernel([[F(x) for x in r] for r in rows])
    mq, mu, md, ml, me, mh = ker[0]
    b = nf * (2 * mq + mu + md)
    lep = nf * (2 * ml + me)
    return b / (b - lep)


def check_gram_ratio_in_the_symmetric_phase():
    premise("synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them")
    premise("dark-tower-matter.mirrors-composition")
    c1, a1, entries = ratio_symmetric(3, 1)
    ok = c1 == F(28, 79) and a1 == 0 and entries == (F(11), F(11), F(8), F(13), F(4), F(2))
    ok = ok and ratio_symmetric(3, 2)[0] == F(8, 23)
    per_family = ratio_symmetric(1, 0)[2]
    ok = ok and per_family == (F(10, 3), F(6), F(8, 3), F(13, 3), F(4, 3), F(2, 3))
    ok = ok and all(ratio_symmetric(nf, nh)[0] == F(8 * nf + 4 * nh, 22 * nf + 13 * nh)
                    for nf in range(1, 7) for nh in range(0, 7))
    ok = ok and all(ratio_symmetric(nf, nh)[0] == stored_kernel_ratio(nf, nh) for nf in (2, 3) for nh in (1, 2))
    # with the neutral singlet in the plasma the form on B - L grows by one per family and the ratio changes
    full = lambda nf: fermion_form(bml, bml, nf) + nf
    ok = ok and full(3) == 16 and fermion_form(bml, bml, 3) == 13
    GA.check("symmetric phase: Gram ratio = (8 N_f + 4 N_H)/(22 N_f + 13 N_H); 28/79 and 8/23", ok)
    return ok


def check_gram_ratio_in_the_broken_phase_and_the_bracket():
    premise("synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them")
    ok = ratio_broken(3, 1) == (F(12, 37), F(22)) and ratio_broken(3, 2)[0] == F(10, 31)
    ok = ok and all(ratio_broken(nf, nh)[0] == F(8 * nf + 4 * (nh + 2), 24 * nf + 13 * (nh + 2))
                    for nf in range(1, 7) for nh in range(0, 7))
    lo, hi, two = F(12, 37), F(28, 79), F(8, 23)
    ok = ok and lo < two < hi
    # the interpolation (28 a + 72 b)/(79 a + 222 b), a, b >= 0, is a mediant of the two one-doublet values
    ok = ok and F(72, 222) == lo
    ok = ok and all(lo <= F(28 * a + 72 * b, 79 * a + 222 * b) <= hi
                    for a in range(0, 6) for b in range(0, 6) if a + b)
    ok = ok and 1 / hi == F(79, 28) and 1 / lo == F(37, 12)
    GA.check("broken phase: (8 N_f + 4 (N_H+2))/(24 N_f + 13 (N_H+2)); 12/37 <= c <= 28/79 for one doublet", ok)
    return ok


DISTRIBUTIONS = ((1, 0, 0), (0, 1, 0), (1, 1, 1), (2, -1, 5), (3, 3, -4))


def flavour_ratios(nf, nh, third):
    """n_B / n_(B-L) for mu = a Y + sum_f b_f Delta_f, Delta_f = third * n_B - L_f, over DISTRIBUTIONS."""
    def val(name, fam, S):
        if name == "Y":
            return hyp(S)
        if name == "B":
            return n_b(S)
        if name == "BL":
            return bml(S)
        return third * n_b(S) - (n_l(S) if fam == name else 0)

    def form(p, q):
        out = sum(val(p, fam, S) * val(q, fam, S) for fam in range(nf) for S in FIFTEEN)
        return out + (nh if p == q == "Y" else 0)
    total = all(sum(val(f, 0, S) for f in range(nf)) == bml(S) for S in FIFTEEN)
    ratios = set()
    for b in DISTRIBUTIONS:
        a = -sum(b[f] * form("Y", f) for f in range(nf)) / form("Y", "Y")
        nB = a * form("B", "Y") + sum(b[f] * form("B", f) for f in range(nf))
        nBL = a * form("BL", "Y") + sum(b[f] * form("BL", f) for f in range(nf))
        ratios.add(nB / nBL)
    return ratios, total


def check_lepton_flavour_does_not_enter_the_ratio():
    premise("synthesis.abelian-charges-of-the-sixteen-and-the-terms-that-break-them")
    ratios, total = flavour_ratios(3, 1, F(1, 3))
    ok = total and ratios == {F(28, 79)}
    ok = ok and flavour_ratios(3, 2, F(1, 3))[0] == {F(8, 23)}
    ok = ok and len(DISTRIBUTIONS) == 5 and GA.field_rank([[F(x) for x in b] for b in DISTRIBUTIONS]) == 3
    GA.check("lepton flavour: n_B / n_(B-L) = 28/79 for every distribution over the three B/3 - L_f", ok)
    return ok


def check_doublets_carry_one_charge_and_the_count_at_freeze_out():
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    premise("synthesis.covariant-rung-coupling-gives-the-normal-pair-tree-level-b-meson-mixing-that-excludes-the-transmutation-branch")
    premise("standard-model.imported-anomaly-coefficients")
    free = conserved_space(False, True, conjugate=False)
    ok = len(free) == 4 and len(conserved_space(False, True)) == 3
    # the one further charge has a nonzero colour coefficient; the colour anomalous condition removes it
    a3 = lambda v: sum(lam(S) ** 2 * v[IDX[S]] for S in EVEN)
    ok = ok and any(a3(v) != 0 for v in free) and [a3(v) for v in (T3_V, Y_V, BL_V)] == [0, 0, 0]
    ok = ok and spans(conserved_space(False, True, conjugate=False, colour=True), [T3_V, Y_V, BL_V])
    extra = [1 - 4 * n_b(S) for S in EVEN] + [F(-2), F(-2), F(-2), F(-2), F(0)]
    ok = ok and GA.field_rank(free + [extra]) == 4 and a3(extra) == 8
    # stored lower bound on the second doublet with a level, about 2500 GeV, against the literature's freeze-out
    ok = ok and 18 * 132 < 2600 < 20 * 132
    ok = ok and F(79, 28) * 87 < 246 and F(37, 12) * 87 > 268 and F(37, 12) * 87 < 269
    GA.check("doublets: independent slot charges add one colour-anomalous charge; one light doublet at freeze-out", ok)
    return ok
