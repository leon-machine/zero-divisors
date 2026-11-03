"""standard-model.left-right-parity-what-breaks-it: exact checks.

(GA) Cl(10,0), generators e_0..e_9: e_0..e_5 the pair Majoranas, e_6..e_9 the slot Majoranas, D = e_5 e_9.
(Fock) The five-mode module as 32 x 32 rational matrices (pair modes 0, 1, 2; slot modes 3, 4), real-form
Majoranas g_{2m} = v_m + w_m, g_{2m+1} = w_m - v_m; the text's gamma_{2m+1} = I g_{2m+1} with I central,
I^2 = -1, so gamma_5 gamma_9 = -g_5 g_9 and gamma_6 gamma_7 gamma_8 gamma_9 = -g_6 g_7 g_8 g_9.
(1) GA: D^2 = -1, D^3 = -D, D^4 = 1 (the polynomial identities that make exp(theta D) = cos theta + D sin theta,
    equal to D at theta = pi/2); D reverse(D) = 1 and D x D^-1 reverses e_5 and e_9 and fixes the other
    eight generators: a half-turn in a slot-pair mixing plane.
(2) Fock: D su(2)_L D^-1 lies in su(2)_R and spans it, and conversely; D maps the eight slot-doublet
    states of the sixteen (Q and L) onto the eight slot-singlet states; D anticommutes with chi = -(-1)^(N_R).
(3) GA: the grade-four elements commuting with the 21 split-preserving bivectors form a space of dimension
    210 - rank = 1, spanned by e_6 e_7 e_8 e_9; in the Fock model gamma_6 gamma_7 gamma_8 gamma_9 = chi.
The final sentence (a vev along the rung parity breaks Spin(10) to Pati-Salam and left-right parity at
the same scale) is the reading of (2) and (3) and is not a separate computation.
"""
from fractions import Fraction as F

import GA
from pyutil import get_or_set
import fock
from tp_premise import premise

# ---------------------------------------------------------------------------
# The five-mode module Lambda(W + R_2) = Lambda(C^5), exact.
# States are bitmasks s in 0..31; mode m is occupied when bit m is set.
# Modes 0, 1, 2 are the three pair modes (W), modes 3, 4 the two slot (rung)
# modes, the text's modes 4 and 5. Operators are sparse matrices
# {(row, col): Fraction}; Jordan-Wigner sign (-1)^(occupied modes below m).
# ---------------------------------------------------------------------------
NM = 5
DIM = 32
PAIRS = (0, 1, 2)
SLOTS = (3, 4)


def nw(s):
    return sum(1 for m in PAIRS if s >> m & 1)


def nr(s):
    return sum(1 for m in SLOTS if s >> m & 1)


def ntot(s):
    return nw(s) + nr(s)


mm, madd, msc, msub = fock.mm, fock.madd, fock.msc, fock.msub
comm, acomm, meq, restrict = fock.comm, fock.acomm, fock.meq, fock.restrict


def diag(fn):
    return fock.diag(fn, DIM)


def gam(p):
    """Majorana p = 0..9 of mode p // 2 in the real form: gamma_{2m} = v_m + w_m (square +1),
    g_{2m+1} = w_m - v_m (square -1). The text's gamma_{2m+1} = I g_{2m+1}, I^2 = -1 central."""
    return fock.majorana(p, NM)


ONE = fock.eye(DIM)
V = [fock.cre(m, NM) for m in range(NM)]  # v_m, creation
W = [fock.ann(m, NM) for m in range(NM)]  # w_m, annihilation
NUM = [fock.num(m, NM) for m in range(NM)]  # n_m


class Span:
    """Incremental exact span of sparse vectors (dicts with hashable keys), reduced row echelon."""

    def __init__(self):
        self.piv, self.where = {}, {}

    def reduce(self, v):
        v = {k: x for k, x in v.items() if x}
        for k in [k for k in v if k in self.piv]:
            c = v.pop(k)
            for kk, xx in self.piv[k].items():
                if kk != k:
                    y = v.get(kk, 0) - c * xx
                    if y:
                        v[kk] = y
                    else:
                        v.pop(kk, None)
        return v

    def add(self, v):
        v = self.reduce(v)
        if not v:
            return False
        k0 = next(iter(v))
        c0 = v[k0]
        v = {k: x / c0 for k, x in v.items()}
        for p in list(self.where.get(k0, ())):
            row = self.piv[p]
            c = row.pop(k0)
            for kk, xx in v.items():
                if kk != k0:
                    y = row.get(kk, 0) - c * xx
                    if y:
                        row[kk] = y
                        get_or_set(self.where, kk, set()).add(p)
                    else:
                        row.pop(kk, None)
                        self.where.get(kk, set()).discard(p)
        self.where.pop(k0, None)
        self.piv[k0] = v
        for kk in v:
            if kk != k0:
                get_or_set(self.where, kk, set()).add(k0)
        return True

    def __len__(self):
        return len(self.piv)


def rank(vecs):
    """Exact rank of sparse vectors (dicts with hashable keys)."""
    sp = Span()
    for v in vecs:
        sp.add(v)
    return len(sp)


def in_span(vecs, v):
    sp = Span()
    for u in vecs:
        sp.add(u)
    return not sp.reduce(v)


def bilinears():
    """The 45 products g_p g_q, p < q, of the real-form Majoranas (the bivectors of the ten,
    up to the central factors of I)."""
    G = [gam(p) for p in range(2 * NM)]
    return {(p, q): mm(G[p], G[q]) for p in range(2 * NM) for q in range(p + 1, 2 * NM)}


def commutant_dim(gens, states):
    """Dimension of {X on span(states) : [X, g] = 0 for all g}, by exact sparse elimination."""
    S = list(states)
    Sset = set(S)
    rows = []
    for g in gens:
        g = restrict(g, S)
        grow, gcol = {}, {}
        for (r, c), x in g.items():
            get_or_set(grow, r, []).append((c, x))
            get_or_set(gcol, c, []).append((r, x))
        for r in S:
            for c in S:
                eq = {}
                # (X g)_{rc} = sum_k X_{rk} g_{kc};  (g X)_{rc} = sum_k g_{rk} X_{kc}
                for k, x in gcol.get(c, ()):
                    eq[(r, k)] = eq.get((r, k), 0) + x
                for k, x in grow.get(r, ()):
                    eq[(k, c)] = eq.get((k, c), 0) - x
                eq = {k: x for k, x in eq.items() if x}
                if eq:
                    rows.append(eq)
    return len(S) * len(S) - rank(rows)
from itertools import combinations

S10 = GA.sig(10, 0)
SLOT_G = (6, 7, 8, 9)


def same_block(p, q):
    return (p in SLOT_G) == (q in SLOT_G)


def gprod(*idx):
    out = GA.sc(1)
    for i in idx:
        out = GA.mul(out, GA.gen(i), S10)
    return out


def su2(left):
    if left:
        return [mm(V[3], W[4]), mm(V[4], W[3]), msc(F(1, 2), msub(NUM[3], NUM[4]))]
    return [mm(V[3], V[4]), mm(W[4], W[3]), msc(F(1, 2), madd(NUM[3], NUM[4], msc(-1, ONE)))]


def check_d_is_a_half_turn():
    premise("standard-model.hyp-s-slot-statistics")
    D = gprod(5, 9)
    D2 = GA.mul(D, D, S10)
    ok = GA.eq(D2, GA.sc(-1))
    ok = ok and GA.eq(GA.mul(D2, D, S10), GA.neg(D)) and GA.eq(GA.mul(D2, D2, S10), GA.sc(1))
    ok = ok and GA.eq(GA.mul(D, GA.reverse(D), S10), GA.sc(1))
    Dinv = GA.reverse(D)
    for i in range(10):
        img = GA.mul(GA.mul(D, GA.gen(i), S10), Dinv, S10)
        want = GA.neg(GA.gen(i)) if i in (5, 9) else GA.gen(i)
        ok = ok and GA.eq(img, want)
    ok = ok and not same_block(5, 9)
    # the same in the Fock model: gamma_5 gamma_9 = -g_5 g_9 squares to -1
    Df = msc(-1, mm(gam(5), gam(9)))
    ok = ok and meq(mm(Df, Df), msc(-1, ONE))
    GA.check("D = gamma5 gamma9 squares to -1 and is the half-turn of a slot-pair plane", ok)
    return ok


def check_d_exchanges_left_and_right():
    premise("standard-model.hyp-s-slot-statistics")
    Df = msc(-1, mm(gam(5), gam(9)))
    Dinv = msc(-1, Df)
    ok = meq(mm(Df, Dinv), ONE)
    L, R = su2(True), su2(False)
    imgL = [mm(Df, X, Dinv) for X in L]
    imgR = [mm(Df, X, Dinv) for X in R]
    ok = ok and rank(imgL) == 3 and rank(R + imgL) == 3
    ok = ok and rank(imgR) == 3 and rank(L + imgR) == 3
    sixteen = [s for s in range(DIM) if ntot(s) % 2 == 0]
    doublet = [s for s in sixteen if nr(s) == 1]
    singlet = [s for s in sixteen if nr(s) != 1]
    targets = set()
    for (r, c) in Df:
        if c in doublet:
            ok = ok and r in singlet
            targets.add(r)
    ok = ok and len(doublet) == 8 and targets == set(singlet)
    chi = diag(lambda s: -(-1) ** nr(s))
    ok = ok and not acomm(Df, chi) and comm(Df, chi)
    GA.check("D exchanges su(2)_L and su(2)_R, maps Q and L onto the singlets, anticommutes with chi", ok)
    return ok


def check_grade_four_pati_salam_singlet():
    premise("standard-model.hyp-s-slot-statistics")
    split = [gprod(p, q) for p in range(10) for q in range(p + 1, 10) if same_block(p, q)]
    quads = list(combinations(range(10), 4))
    ok = len(split) == 21 and len(quads) == 210
    images = []
    for b in quads:
        bb = gprod(*b)
        vec = {}
        for i, B in enumerate(split):
            c = GA.sub(GA.mul(B, bb, S10), GA.mul(bb, B, S10))
            for bl, x in c.items():
                if x:
                    vec[(i, bl)] = x
        images.append(vec)
    ok = ok and 210 - rank(images) == 1
    slot4 = gprod(6, 7, 8, 9)
    ok = ok and all(GA.is_zero(GA.sub(GA.mul(B, slot4, S10), GA.mul(slot4, B, S10))) for B in split)
    # its Fock image: gamma6 gamma7 gamma8 gamma9 = (I^2) g6 g7 g8 g9 = chi
    chi = diag(lambda s: -(-1) ** nr(s))
    ok = ok and meq(msc(-1, mm(gam(6), gam(7), gam(8), gam(9))), chi)
    GA.check("the grade-four Pati-Salam singlets are the line of gamma6789, which acts as chi", ok)
    return ok
