"""synthesis.up-down-split-under-conjugate-reading-needs-su2r-odd-weighting: exact checks.

The five-mode module Lambda(W + R_2) as 32 x 32 rational matrices (fock.py, LSB order), modes 0, 1, 2 the
pairs, 3, 4 the rungs, v_i creating, w_i annihilating, as in the stored checks of the Majorana element's
square and moment map. T = v_1 ... v_5; T T^dag is expanded in the 1024 Majorana monomials a_I b_J
(a_i = v_i + w_i, b_i = v_i - w_i) by the trace form and split by support: pair-only, rung-only, mixed.
Mass forms are B(psi, X phi) on the sixteen (even states) with the stored pairing B. Under the c* reading the
down-type and charged-lepton entries of a composite c g come from w_4 g and the up-type and Dirac-neutrino
entries from v_4 g (c = a v_4 + b w_4, c* = conj(b) v_4 + conj(a) w_4); entries are compared with the 10 forms
of w_4 and v_4 on the same species pairs.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock
from tp_premise import premise

NM = 5
STATES = [s for k in range(NM + 1) for s in combinations(range(NM), k)]
IDX = {s: sum(1 << x for x in s) for s in STATES}
STATE_OF = {i: s for s, i in IDX.items()}
D = len(STATES)
mm, madd, msc, tr, comm = fock.mm, fock.madd, fock.msc, fock.transpose, fock.comm
PAIRS = (0, 1, 2)
RUNGS = (3, 4)


def nw(s):
    return sum(1 for x in s if x in PAIRS)


def nr(s):
    return sum(1 for x in s if x in RUNGS)


def diag(fn):
    return fock.diag(lambda i: fn(STATE_OF[i]), D)


V = [fock.cre(m, NM) for m in range(NM)]
W = [tr(v) for v in V]
ONE = fock.eye(D)
BETA = [madd(mm(V[i], W[i]), msc(F(-1, 2), ONE)) for i in range(NM)]   # n_i - 1/2
BL = diag(lambda s: 1 - F(2, 3) * nw(s))                               # B - L
CHI = diag(lambda s: -(-1) ** nr(s))                                    # rung parity chi
PPAR = diag(lambda s: (-1) ** nw(s))                                    # pair parity
MUP = msc(F(1, 8), madd(BETA[0], BETA[1], BETA[2]))
MUR = msc(F(1, 8), madd(BETA[3], BETA[4]))
T = mm(mm(mm(mm(V[0], V[1]), V[2]), V[3]), V[4])
SIXTEEN = [s for s in STATES if len(s) % 2 == 0]

BMAT = {}
for s in STATES:
    comp = tuple(x for x in range(NM) if x not in s)
    seq = list(s) + list(comp)
    inv = sum(1 for i in range(NM) for j in range(i + 1, NM) if seq[i] > seq[j])
    k = len(s)
    BMAT[(IDX[s], IDX[comp])] = F((-1) ** (k * (k - 1) // 2) * (-1) ** inv)


def gen_act(kind, i, st):
    sign = (-1) ** sum(1 for x in st if x < i)
    if i in st:
        return (sign if kind == 0 else -sign), tuple(x for x in st if x != i)
    return sign, tuple(sorted(st + (i,)))


def monomial_cols(I, J):
    cols = {}
    for st in STATES:
        sg, cur = 1, st
        for j in reversed(J):
            e, cur = gen_act(1, j, cur)
            sg *= e
        for i in reversed(I):
            e, cur = gen_act(0, i, cur)
            sg *= e
        cols[st] = (cur, sg)
    return cols


MONOS = [(I, J) for k in range(NM + 1) for I in combinations(range(NM), k)
         for l in range(NM + 1) for J in combinations(range(NM), l)]
COLS = {m: monomial_cols(*m) for m in MONOS}


def monomial(I, J):
    return {(IDX[img], IDX[st]): F(sg) for st, (img, sg) in COLS[(I, J)].items()}


def expand(X):
    out = {}
    for m in MONOS:
        c = sum((sg * X.get((IDX[img], IDX[st]), 0) for st, (img, sg) in COLS[m].items()), F(0)) / D
        if c:
            out[m] = c
    return out


def assemble(coeffs):
    M = {}
    for (I, J), c in coeffs.items():
        M = madd(M, msc(c, monomial(I, J)))
    return M


def forms(X):
    """symmetric and antisymmetric parts of B(psi, X phi) on the sixteen."""
    BX = mm(BMAT, X)
    sym, anti = {}, {}
    for a in SIXTEEN:
        for b in SIXTEEN:
            x, y = BX.get((IDX[a], IDX[b]), 0), BX.get((IDX[b], IDX[a]), 0)
            if x + y:
                sym[(a, b)] = (x + y) * F(1, 2)
            if x - y:
                anti[(a, b)] = (x - y) * F(1, 2)
    return sym, anti


def is_multiple(f, g):
    keys = set(f) | set(g)
    c = None
    for k in keys:
        a, b = f.get(k, F(0)), g.get(k, F(0))
        if b == 0:
            if a != 0:
                return None
            continue
        if c is None:
            c = a / b
        elif a != c * b:
            return None
    return c if c is not None else F(0)


def combo(f, g1, g2):
    """f = x g1 + y g2 for scalars (x, y), solved on two entries and verified on all; returns (x, y) or None."""
    keys = sorted(set(f) | set(g1) | set(g2))
    for k1 in keys:
        for k2 in keys:
            det = g1.get(k1, F(0)) * g2.get(k2, F(0)) - g2.get(k1, F(0)) * g1.get(k2, F(0))
            if det != 0:
                x = (f.get(k1, F(0)) * g2.get(k2, F(0)) - g2.get(k1, F(0)) * f.get(k2, F(0))) / det
                y = (g1.get(k1, F(0)) * f.get(k2, F(0)) - f.get(k1, F(0)) * g1.get(k2, F(0))) / det
                if all(f.get(k, F(0)) == x * g1.get(k, F(0)) + y * g2.get(k, F(0)) for k in keys):
                    return x, y
                return None
    return None


def restrict16(X):
    keep = {IDX[s] for s in SIXTEEN}
    return {(r, c): v for (r, c), v in X.items() if c in keep}


def split_square():
    ex = expand(mm(T, tr(T)))
    g4 = {m: c for m, c in ex.items() if len(m[0]) + len(m[1]) == 4}
    pp = assemble({m: c for m, c in g4.items() if all(i in PAIRS for i in m[0] + m[1])})
    rr = assemble({m: c for m, c in g4.items() if all(i in RUNGS for i in m[0] + m[1])})
    mx = assemble({m: c for m, c in g4.items() if any(i in PAIRS for i in m[0] + m[1])
                   and any(i in RUNGS for i in m[0] + m[1])})
    return ex, pp, rr, mx


EX, PP, RR, MX = split_square()
W4, V4 = W[3], V[3]
TGJ = mm(mm(W4, BL), CHI)
UGJ = mm(mm(V4, BL), CHI)
S10, _ = forms(W4)
SGJ, _ = forms(TGJ)
_, A3 = forms(mm(W4, BL))


T3R = diag(lambda s: F(nr(s) - 1, 2))
S10D, _ = forms(W4)
S10U, _ = forms(V4)
SUGJ, _ = forms(UGJ)


def sector_weights(X, S10):
    """symmetric form of X relative to the 10 form, as {sector: set of ratios}; None if X has symmetric
    entries where the 10 form has none."""
    s, _ = forms(X)
    out = {}
    for k, v in s.items():
        if k not in S10:
            return None
        sec = "lep" if nw(k[0]) in (0, 3) else "qrk"
        out[sec] = out.get(sec, set()) | {v / S10[k]}
    return out


def pair_weights(g):
    """(down, up) sector weights of the composite with weighting g under the c* reading."""
    return sector_weights(mm(W4, g), S10D), sector_weights(mm(V4, g), S10U)


def neg(w):
    return {k: {-x for x in v} for k, v in w.items()}


# weightings h(T3R, B - L): (c00, c20, c02, c22) for 1, T3R^2, (B-L)^2, T3R^2 (B-L)^2 (even in T3R) and
# (c10, c12) for T3R, T3R (B-L)^2 (odd), with the expected down weights (lep, qrk) tabulated by hand as the
# average of h over the two states of each coupled pair, with
# T3R(e^c) = T3R(d^c) = 1/2, T3R(L) = T3R(Q) = 0, |B - L| = 1 on leptons and 1/3 on quarks
EVEN_SAMPLES = (((F(1), F(0), F(0), F(0)), (F(1), F(1))),
                ((F(0), F(1), F(0), F(0)), (F(1, 8), F(1, 8))),
                ((F(0), F(0), F(1), F(0)), (F(1), F(1, 9))),
                ((F(2), F(-4), F(9), F(36)), (F(15), F(3))))
ODD_SAMPLES = (((F(1), F(0)), (F(1, 4), F(1, 4))),
               ((F(3), F(-9)), (F(-3, 2), F(1, 2))))


def check_t3r_even_weightings_never_split_up_from_down():
    """For every weighting h(T3R, B - L) the down and up entries are e + o and e - o, e and o the
    contributions of the even and odd parts in T3R; so T3R-even weightings, among them the 10 and every
    f(B - L) (the Georgi-Jarlskog composite w_4 P_4 included), give m_u = m_d and m_nu = m_e family by
    family, and T3R-odd ones give equal and opposite entries."""
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.invariant-pairing-five-modes")
    premise("standard-model.generation-ten-under-pati-salam")
    premise("standard-model.hyp-s-slot-statistics")
    GA.check("the sixteen is the even half and contains the empty state", () in SIXTEEN and all(len(s) % 2 == 0 for s in SIXTEEN))
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    GA.check("T3R = (N_R - 1)/2 is mu_R times 4", T3R == msc(F(4), MUR))
    BL2 = mm(BL, BL)
    T2 = mm(T3R, T3R)
    for (c00, c20, c02, c22), (wl, wq) in EVEN_SAMPLES:
        g = madd(msc(c00, ONE), msc(c20, T2), msc(c02, BL2), msc(c22, mm(T2, BL2)))
        d, u = pair_weights(g)
        GA.check("T3R-even weighting: down weights (%s, %s), up = down" % (wl, wq),
                 d == {"lep": {wl}, "qrk": {wq}} and u == d)
    for (c10, c12), (wl, wq) in ODD_SAMPLES:
        g = madd(msc(c10, T3R), msc(c12, mm(T3R, BL2)))
        d, u = pair_weights(g)
        GA.check("T3R-odd weighting: down weights (%s, %s), up = -down" % (wl, wq),
                 d == {"lep": {wl}, "qrk": {wq}} and u == neg(d))
    return True


def check_parts_of_the_square_under_the_conjugate_reading():
    """The 10 and P_4 = (3/32)(B - L)(-1)^{N_P} are T3R-even: up = down, weights (1, 1) and (3/32, -1/32);
    X_4 = 8 mu_R mu_P and mu_R are T3R-odd: X_4 down (-3/32, 1/32), up (3/32, -1/32); mu_R down (1/16, 1/16),
    up (-1/16, -1/16); R_4 and mu_P give no symmetric entries. Hence the whole degree-four part G_4 of T T^dag
    gives no down-type or charged-lepton entry and up-type entries -(3/16) times the up-type Georgi-Jarlskog
    form (|m_nu^D| = 3 |m_u|), and the square through degree four, 1/32 + mu/2 + G_4, gives the down sector the
    10 relation with weight 1/16 and the up sector that Georgi-Jarlskog form alone."""
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("synthesis.georgi-jarlskog-square-of-majorana-element")
    premise("synthesis.georgi-jarlskog-majorana-moment-map")
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    premise("standard-model.majorana-element")
    GA.check("P_4 is (3/32)(B - L) times the pair parity", PP == msc(F(3, 32), mm(BL, PPAR)))
    GA.check("P_4 = 4 mu_P^2 - 3/64 and R_4 = -chi/32 (the derived split)",
             PP == madd(msc(F(4), mm(MUP, MUP)), msc(F(-3, 64), ONE)) and RR == msc(F(-1, 32), CHI))
    GA.check("X_4 = 8 mu_R mu_P and mu_R = T3R / 4", MX == msc(F(8), mm(MUR, MUP)) and MUR == msc(F(1, 4), T3R))
    table = ((ONE, {"lep": {F(1)}, "qrk": {F(1)}}, F(1)),
             (PP, {"lep": {F(3, 32)}, "qrk": {F(-1, 32)}}, F(1)),
             (MX, {"lep": {F(-3, 32)}, "qrk": {F(1, 32)}}, F(-1)),
             (MUR, {"lep": {F(1, 16)}, "qrk": {F(1, 16)}}, F(-1)))
    for g, dw, sgn in table:
        d, u = pair_weights(g)
        GA.check("down weights %s, up = %s x down" % (sorted(dw.items()), sgn),
                 d == dw and u == {k: {sgn * x for x in v} for k, v in dw.items()})
    for g in (RR, MUP):
        GA.check("no symmetric entries", forms(mm(W4, g))[0] == {} and forms(mm(V4, g))[0] == {})
    G4 = madd(PP, MX, RR)
    GA.check("G_4: no down-type entry", forms(mm(W4, G4))[0] == {})
    su, au = forms(mm(V4, G4))
    GA.check("G_4: up-type entries -(3/16) up-type GJ", is_multiple(su, SUGJ) == F(-3, 16))
    up_abs = {sec: {abs(x) for x in v} for sec, v in sector_weights(mm(V4, G4), S10U).items()}
    GA.check("|m_nu^D| = 3 |m_u| from G_4", up_abs == {"lep": {F(3, 16)}, "qrk": {F(1, 16)}})
    MU = madd(MUP, MUR)
    TRUNC = madd(msc(F(1, 32), ONE), msc(F(1, 2), MU), G4)
    d, u = pair_weights(TRUNC)
    GA.check("square through degree four: down 10 relation with weight 1/16", d == {"lep": {F(1, 16)}, "qrk": {F(1, 16)}})
    GA.check("square through degree four: up sector -(3/16) up-type GJ", is_multiple(forms(mm(V4, TRUNC))[0], SUGJ) == F(-3, 16))
    GA.check("the whole square gives no entry at all", forms(mm(W4, mm(T, tr(T))))[0] == {}
             and forms(mm(V4, mm(T, tr(T))))[0] == {})
    return True
