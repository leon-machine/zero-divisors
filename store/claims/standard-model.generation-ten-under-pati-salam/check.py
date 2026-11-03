"""standard-model.generation-ten-under-pati-salam: exact checks.

The five-mode module as 32 x 32 rational matrices (pair modes 0, 1, 2; slot modes 3, 4, the text's 4
and 5), the sixteen being the states of even total mode number. su(2)_L = {v_4 w_5, v_5 w_4, (N_4 - N_5)/2},
su(2)_R = {v_4 v_5, w_5 w_4, (N_4 + N_5 - 1)/2} as in the premise; Casimir C = T_3^2 + (T_+ T_- + T_- T_+)/2.
B - L = 1 - (2/3) N_W. Species by (pairs, slots) occupied: nu^c (0,0), u^c (2,0), Q (1,1), L (3,1),
e^c (0,2), d^c (2,2).
(1) C_L and C_R are diagonal on the sixteen, (3/4, 0) on Q and L and (0, 3/4) on the four singlets;
    B - L is 1/3, -1, -1/3, -1/3, 1, 1 on Q, L, u^c, d^c, e^c, nu^c.
(2) The sixteen is (2,1,4) + (1,2,4bar): the slot-doublet half carries B - L weights {1/3 x 3, -1},
    the slot-singlet half {-1/3 x 3, 1} (conjugate 4s), and the commutant of the 15 pair bivectors
    (su(4)) on each half of eight is four-dimensional (two copies of one irreducible 4).
(3) Under the 21 (adjoint action X -> [B, X]) the span of the orbit of a slot Majorana is the four
    slot Majoranas and that of a pair Majorana the six pair Majoranas; on the four, C_L = C_R = 3/4
    (the bidoublet (2,2,1)); on the six su(2)_L and su(2)_R act trivially (the (1,1,6)).
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
comm, meq, restrict = fock.comm, fock.meq, fock.restrict


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

PAIR_G = tuple(range(6))
SLOT_G = (6, 7, 8, 9)
SPECIES = {(0, 0): "nuc", (2, 0): "uc", (1, 1): "Q", (3, 1): "L", (0, 2): "ec", (2, 2): "dc"}


def species(s):
    return SPECIES[(nw(s), nr(s))]


def su2(left):
    if left:
        return [mm(V[3], W[4]), mm(V[4], W[3]), msc(F(1, 2), msub(NUM[3], NUM[4]))]
    return [mm(V[3], V[4]), mm(W[4], W[3]), msc(F(1, 2), madd(NUM[3], NUM[4], msc(-1, ONE)))]


def casimir(left):
    tp, tm, t3 = su2(left)
    return madd(mm(t3, t3), msc(F(1, 2), madd(mm(tp, tm), mm(tm, tp))))


def ad_casimir(left, X):
    tp, tm, t3 = su2(left)
    a3 = comm(t3, comm(t3, X))
    apm = madd(comm(tp, comm(tm, X)), comm(tm, comm(tp, X)))
    return madd(a3, msc(F(1, 2), apm))


def orbit_span(start, gens):
    sp = Span()
    sp.add(start)
    span, frontier = [start], [start]
    while frontier:
        new = []
        for X in frontier:
            for g in gens:
                Y = comm(g, X)
                if sp.add(Y):
                    span.append(Y)
                    new.append(Y)
        frontier = new
    return span


def check_casimirs_and_b_minus_l():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("standard-model.hyp-s-slot-statistics")
    sixteen = [s for s in range(DIM) if ntot(s) % 2 == 0]
    CL, CR = casimir(True), casimir(False)
    ok = len(sixteen) == 16
    ok = ok and all(r == c for (r, c) in restrict(CL, sixteen)) and all(r == c for (r, c) in restrict(CR, sixteen))
    want = {"Q": (F(3, 4), 0), "L": (F(3, 4), 0), "uc": (0, F(3, 4)), "dc": (0, F(3, 4)),
            "ec": (0, F(3, 4)), "nuc": (0, F(3, 4))}
    bl = {"Q": F(1, 3), "L": F(-1), "uc": F(-1, 3), "dc": F(-1, 3), "ec": F(1), "nuc": F(1)}
    for s in sixteen:
        sp = species(s)
        ok = ok and (CL.get((s, s), 0), CR.get((s, s), 0)) == want[sp]
        ok = ok and 1 - F(2, 3) * nw(s) == bl[sp]
    GA.check("Casimirs (3/4, 0) on Q, L and (0, 3/4) on the singlets; B - L values", ok)
    return ok


def check_sixteen_is_2_1_4_plus_1_2_4bar():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("standard-model.hyp-s-slot-statistics")
    sixteen = [s for s in range(DIM) if ntot(s) % 2 == 0]
    doublet = [s for s in sixteen if nr(s) == 1]
    singlet = [s for s in sixteen if nr(s) != 1]
    ok = len(doublet) == 8 and len(singlet) == 8
    # B - L weights of one su(2) component of each half (fix the slot state)
    w_d = sorted(1 - F(2, 3) * nw(s) for s in doublet if s >> 3 & 1)
    w_s = sorted(1 - F(2, 3) * nw(s) for s in singlet if nr(s) == 0)
    ok = ok and w_d == [F(-1), F(1, 3), F(1, 3), F(1, 3)]
    ok = ok and w_s == [F(-1, 3), F(-1, 3), F(-1, 3), F(1)]
    ok = ok and w_s == sorted(-x for x in w_d)
    pair_b = [X for (p, q), X in bilinears().items() if p in PAIR_G and q in PAIR_G]
    ok = ok and commutant_dim(pair_b, doublet) == 4 and commutant_dim(pair_b, singlet) == 4
    GA.check("the sixteen is (2,1,4) + (1,2,4bar)", ok)
    return ok


def check_majoranas_span_bidoublet_and_six():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    Bl = bilinears()
    gens = [X for (p, q), X in Bl.items() if (p in SLOT_G) == (q in SLOT_G)]
    slot_m = [gam(p) for p in SLOT_G]
    pair_m = [gam(p) for p in PAIR_G]
    o_slot = orbit_span(gam(6), gens)
    o_pair = orbit_span(gam(0), gens)
    ok = len(o_slot) == 4 and len(o_pair) == 6
    ok = ok and rank(o_slot + slot_m) == 4 and rank(o_pair + pair_m) == 6
    ok = ok and all(meq(ad_casimir(True, X), msc(F(3, 4), X)) for X in slot_m)
    ok = ok and all(meq(ad_casimir(False, X), msc(F(3, 4), X)) for X in slot_m)
    ok = ok and all(not comm(t, X) for X in pair_m for t in su2(True) + su2(False))
    GA.check("slot Majoranas span the (2,2,1), pair Majoranas the (1,1,6)", ok)
    return ok
