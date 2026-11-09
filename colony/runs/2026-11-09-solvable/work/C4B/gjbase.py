"""synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square: exact checks.

The five-mode module Lambda(W + R_2) as 32 x 32 rational matrices (fock.py, LSB order), modes 0, 1, 2 the
pairs, 3, 4 the rungs, v_i creating, w_i annihilating, as in the stored checks of the Majorana element's
square and moment map. T = v_1 ... v_5; T T^dag is expanded in the 1024 Majorana monomials a_I b_J
(a_i = v_i + w_i, b_i = v_i - w_i) by the trace form and split by support: pair-only, rung-only, mixed.
Mass forms are B(psi, X phi) on the sixteen (even states) with the stored pairing B.
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


def check_pati_salam_split_of_the_square():
    """The degree-four part of T T^dag splits as PP + MX + RR with PP = 4 mu_P^2 - 3/64
    = (3/64)(3(B - L)^2 - 1) = (3/32)(B - L)(-1)^{N_P}, MX = 8 mu_R mu_P (stored) and RR = 4 mu_R^2 - 1/32 = -chi/32;
    PP commutes with su(2)_L, su(2)_R, su(3) and B - L but not with the pair bracket v_1 v_2, so it lies in the
    (15,1,1); MX commutes with su(2)_L but not with v_4 v_5 ((15,1,3)); RR is the Pati-Salam singlet chi."""
    premise("standard-model.majorana-element")
    premise("synthesis.georgi-jarlskog-square-of-majorana-element")
    premise("synthesis.georgi-jarlskog-majorana-moment-map")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    TT = mm(T, tr(T))
    GA.check("expansion reassembles T T^dag", assemble(EX) == TT)
    G4 = madd(PP, RR, MX)
    MU = madd(MUP, MUR)
    GA.check("G4 = 4 mu^2 - 5/64 (stored)", G4 == madd(msc(F(4), mm(MU, MU)), msc(F(-5, 64), ONE)))
    GA.check("PP has three monomials of coefficient -1/32",
             sorted(c for m, c in EX.items() if len(m[0]) + len(m[1]) == 4 and all(i in PAIRS for i in m[0])) == [F(-1, 32)] * 3)
    GA.check("PP = 4 mu_P^2 - 3/64", PP == madd(msc(F(4), mm(MUP, MUP)), msc(F(-3, 64), ONE)))
    GA.check("PP = (3/64)(3 (B-L)^2 - 1)", PP == msc(F(3, 64), madd(msc(F(3), mm(BL, BL)), msc(F(-1), ONE))))
    GA.check("PP = (3/32)(B-L) times the pair parity", PP == msc(F(3, 32), mm(BL, PPAR)))
    GA.check("MX = 8 mu_R mu_P (stored)", MX == msc(F(8), mm(MUR, MUP)))
    GA.check("RR = 4 mu_R^2 - 1/32 = -chi/32", RR == madd(msc(F(4), mm(MUR, MUR)), msc(F(-1, 32), ONE))
             and RR == msc(F(-1, 32), CHI))
    su2l = [mm(V[3], W[4]), mm(V[4], W[3])]
    su2r = [mm(V[3], V[4]), mm(W[4], W[3])]
    su3 = [mm(V[a], W[b]) for a in PAIRS for b in PAIRS if a != b]
    GA.check("PP commutes with su(2)_L, su(2)_R, su(3), B - L",
             all(comm(PP, g) == {} for g in su2l + su2r + su3 + [BL]))
    GA.check("PP is not an su(4) singlet", comm(PP, mm(V[0], V[1])) != {})
    GA.check("MX: su(2)_L singlet, not su(2)_R singlet", all(comm(MX, g) == {} for g in su2l)
             and comm(MX, su2r[0]) != {})
    return True


def check_rung_vector_times_pair_part_is_georgi_jarlskog():
    """On the sixteen the rung parity is minus the pair parity, so w_4 PP = -(3/32) T_GJ there as operators;
    its mass form is -(3/32) times the Georgi-Jarlskog form, symmetric, with no antisymmetric (120) part and
    no 10 component (ratio |y_e/y_d| = 3); v_4 PP gives -(3/32) times the up-type form (|m_nu^D| = 3|m_u|).
    MX gives +(3/32) GJ and -(3/32) the grade-three form (stored); RR gives no symmetric form; the symmetric
    forms of the three parts cancel, so w_4 G_4 has none; and the scalar part with PP, 1/32 + PP, gives the
    rung vector a lepton-only form (y_d = 0), not the factor 3."""
    premise("standard-model.invariant-pairing-five-modes")
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    premise("standard-model.grade-three-georgi-jarlskog-direction")
    premise("synthesis.georgi-jarlskog-square-of-majorana-element")
    premise("standard-model.hyp-s-slot-statistics")
    GA.check("the sixteen is the even half and contains the empty state", () in SIXTEEN and all(len(s) % 2 == 0 for s in SIXTEEN))
    GA.check("chi = - pair parity on the sixteen",
             all(CHI.get((IDX[s], IDX[s]), 0) == -PPAR.get((IDX[s], IDX[s]), 0) for s in SIXTEEN))
    GA.check("w_4 PP = -(3/32) T_GJ on the sixteen", restrict16(mm(W4, PP)) == restrict16(msc(F(-3, 32), TGJ)))
    s, a = forms(mm(W4, PP))
    GA.check("sym(w_4 PP) = -(3/32) GJ form", is_multiple(s, SGJ) == F(-3, 32))
    GA.check("no antisymmetric part", a == {})
    GA.check("no 10 component: GJ form is not a multiple of the 10 form", is_multiple(SGJ, S10) is None)
    lep = [(x, y) for (x, y) in SGJ if nw(x) in (0, 3)]
    qrk = [(x, y) for (x, y) in SGJ if nw(x) in (1, 2)]
    GA.check("GJ ratio 3", {abs(SGJ[k]) for k in lep} == {F(1)} and {abs(SGJ[k]) for k in qrk} == {F(1, 3)})
    su, au = forms(mm(V4, PP))
    sU, _ = forms(UGJ)
    GA.check("v_4 PP = -(3/32) up-type form, symmetric", is_multiple(su, sU) == F(-3, 32) and au == {})
    sm, am = forms(mm(W4, MX))
    GA.check("MX: +(3/32) GJ, -(3/32) grade three", is_multiple(sm, SGJ) == F(3, 32) and is_multiple(am, A3) == F(-3, 32))
    sr, ar = forms(mm(W4, RR))
    GA.check("RR: no symmetric form, nonzero antisymmetric", sr == {} and ar != {})
    s4, _ = forms(mm(W4, madd(PP, MX, RR)))
    GA.check("w_4 G_4 has no symmetric form", s4 == {})
    s0, _ = forms(mm(W4, madd(msc(F(1, 32), ONE), PP)))
    GA.check("1/32 + PP: quark entries vanish, lepton entries 1/8 of the 10's",
             all(nw(x) in (0, 3) for (x, y) in s0) and s0 != {}
             and is_multiple(s0, {k: v for k, v in S10.items() if nw(k[0]) in (0, 3)}) == F(1, 8))
    return True


EVEN_TABLE = ((F(1), F(0), F(1), F(0)), (F(0), F(1), F(1, 3), F(-2, 3)), (F(1), F(-3), F(0), F(2)),
              (F(2), F(5, 7), F(47, 21), F(-10, 21)))
ODD_TABLE = ((F(0), F(1)), (F(2), F(-9)))
TRACE_TABLE = ((2, ({F(0)}, {F(0)})), (4, ({F(0)}, {F(0)})), (6, ({F(-4)}, {F(4)})))


def check_even_and_odd_pair_weightings():
    """For a weighting f(B - L): f even gives a symmetric form x (10) + y (GJ) with x one quarter of the trace of
    f over a Pati-Salam quartet (B - L = 1/3, 1/3, 1/3, -1) and y = (3/4)(f(1/3) - f(1)), and no antisymmetric
    part; f odd gives a nonzero antisymmetric form and no symmetric part, the grade-three form for f = B - L. Pair-only Majorana monomials of
    degree two and four have zero trace on each pair-parity half (quartet) of Lambda(W); the degree-six one does
    not."""
    premise("standard-model.invariant-pairing-five-modes")
    premise("families.doublet-direction-module-georgi-jarlskog-clebsch")
    premise("standard-model.grade-three-georgi-jarlskog-direction")
    premise("standard-model.generation-ten-under-pati-salam")
    premise("standard-model.yukawa-pattern-two-rung-module")
    # (c0, c2, x, y): f = c0 + c2 (B - L)^2 gives x (10) + y (GJ); tabulated by hand from
    # x = (3 f(1/3) + f(1)) / 4, y = (3/4)(f(1/3) - f(1))
    for (c0, c2, xx, yy) in EVEN_TABLE:
        fx = madd(msc(c0, ONE), msc(c2, mm(BL, BL)))
        s, a = forms(mm(W4, fx))
        GA.check("even weighting (%s, %s): 10 weight %s, GJ weight %s" % (c0, c2, xx, yy),
                 combo(s, S10, SGJ) == (xx, yy) and a == {})
    for (c1, c3) in ODD_TABLE:
        fx = madd(msc(c1, BL), msc(c3, mm(BL, mm(BL, BL))))
        s, a = forms(mm(W4, fx))
        GA.check("odd weighting: antisymmetric form only (the 120 sector)", s == {} and a != {})
    s, a = forms(mm(W4, BL))
    GA.check("B - L itself: the grade-three form", s == {} and is_multiple(a, A3) == F(1))
    # quartet traces on Lambda(W), the three pair modes: degree -> (trace on even half, trace on odd half)
    vv = [fock.cre(i, 3) for i in PAIRS]
    gens = [madd(v, tr(v)) for v in vv] + [madd(v, msc(F(-1), tr(v))) for v in vv]
    for deg, expect in TRACE_TABLE:
        for half in (0, 1):
            sel = [s for s in range(8) if fock.popcount(s) % 2 == half]
            traces = set()
            for idxs in combinations(range(6), deg):
                M = fock.eye(8)
                for i in idxs:
                    M = mm(M, gens[i])
                traces.add(sum((M.get((s, s), 0) for s in sel), F(0)))
            GA.check("pair monomials of degree %d: quartet traces %s" % (deg, expect[half]), traces == expect[half])
    return True
