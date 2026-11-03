"""standard-model.automorphisms-preserve-slot-pair-split-are: exact checks.

Two exact models. (GA) Cl(10,0) with generators e_0..e_9, e_0..e_5 the six pair Majoranas and e_6..e_9
the four slot Majoranas. (Fock) The five-mode module as 32 x 32 rational matrices, pair modes 0, 1, 2
and slot modes 3, 4 (the text's 4 and 5); real-form Majoranas g_{2m} = v_m + w_m, g_{2m+1} = w_m - v_m
(the text's gamma_{2m+1} = I g_{2m+1}, I central with I^2 = -1, so complex spans agree).
(1) GA: of the 45 bivectors e_p e_q, 6 + 15 = 21 have both indices in one block and 24 mix; the 21 close
    under the commutator (every commutator is a combination of block bivectors), the 24 do not (a mixed
    commutator of two mixed bivectors leaves the 24). Fock: the Clifford relations of the ten.
(2) Fock: su(2)_L = {v_4 w_5, v_5 w_4, (N_4 - N_5)/2} and su(2)_R = {v_4 v_5, w_5 w_4, (N_4 + N_5 - 1)/2}
    satisfy the su(2) relations, commute with each other and lie in (and with 1 span) the slot
    bilinears plus 1; su(3) (traceless pair mixings) and B - L = 1 - (2/3) N_W lie in the pair
    bilinears plus 1, which have dimension 15; Y = (3 N_R - 2 N_W)/6 equals T_3R + (B - L)/2 as matrices.
(3) Fock: on the sixteen (even total mode number) the commutant of the 21 is two-dimensional, spanned
    by 1 and chi = -(-1)^(N_R), which is +1 on the 8 slot-doublet states and -1 on the 8 others.
The group-level sentence (Spin(4) x Spin(6), and U(2) x U(3) when the mode number is kept) is the
Lie-algebra statement above integrated; it is not tested beyond the algebra.
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


ONE = fock.eye(DIM)
V = [fock.cre(m, NM) for m in range(NM)]    # v_m, creation
W = [fock.ann(m, NM) for m in range(NM)]    # w_m, annihilation
NUM = [mm(V[m], W[m]) for m in range(NM)]   # n_m


def gam(p):
    """Majorana p = 0..9 of mode p // 2 in the real form: gamma_{2m} = v_m + w_m (square +1),
    g_{2m+1} = w_m - v_m (square -1). The text's gamma_{2m+1} = I g_{2m+1}, I^2 = -1 central."""
    return fock.majorana(p, NM)


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

S10 = GA.sig(10, 0)
PAIR_G = tuple(range(6))
SLOT_G = (6, 7, 8, 9)


def gbiv(p, q):
    return GA.mul(GA.gen(p), GA.gen(q), S10)


def same_block(p, q):
    return (p in SLOT_G) == (q in SLOT_G)


def blade_ok(blade, allowed):
    return len(blade) == 2 and allowed(blade[0], blade[1])


def T3R():
    return msc(F(1, 2), madd(NUM[3], NUM[4], msc(-1, ONE)))


def T3L():
    return msc(F(1, 2), msub(NUM[3], NUM[4]))


def BL():
    return diag(lambda s: 1 - F(2, 3) * nw(s))


def HYP():
    return diag(lambda s: F(3 * nr(s) - 2 * nw(s), 6))


def check_split_bivectors_close():
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    pairs = [(p, q) for p in range(10) for q in range(p + 1, 10)]
    split = [pq for pq in pairs if same_block(*pq)]
    mixed = [pq for pq in pairs if not same_block(*pq)]
    ok = len(pairs) == 45 and len(split) == 21 and len(mixed) == 24
    ok = ok and sum(1 for p, q in split if p in SLOT_G) == 6 and sum(1 for p, q in split if p in PAIR_G) == 15
    closed = True
    for a in split:
        for b in split:
            c = GA.sub(GA.mul(gbiv(*a), gbiv(*b), S10), GA.mul(gbiv(*b), gbiv(*a), S10))
            closed = closed and all(blade_ok(bl, same_block) for bl in c)
    ok = ok and closed
    # the mixed ones do not close: [e0 e6, e1 e6] = -2 e0 e1 is a block bivector
    c = GA.sub(GA.mul(gbiv(0, 6), gbiv(1, 6), S10), GA.mul(gbiv(1, 6), gbiv(0, 6), S10))
    ok = ok and GA.eq(c, GA.scal(F(-2), gbiv(0, 1)))
    # Fock: the ten Majoranas satisfy the Clifford relations (signature (5,5) in the real form)
    G = [gam(p) for p in range(10)]
    for p in range(10):
        for q in range(10):
            want = {} if p != q else msc(2 * (-1) ** p, ONE)
            ok = ok and meq(acomm(G[p], G[q]), want)
    ok = ok and rank(list(bilinears().values())) == 45
    GA.check("the 21 split-preserving bivectors (6 + 15) close; the 45 are independent", ok)
    return ok


def check_left_right_and_pati_salam_generators():
    premise("standard-model.imported-pati-salam-representation-theory-survival")
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.hyp-s-slot-statistics")
    Bl = bilinears()
    slot_b = [X for (p, q), X in Bl.items() if p in SLOT_G and q in SLOT_G]
    pair_b = [X for (p, q), X in Bl.items() if p in PAIR_G and q in PAIR_G]
    ok = len(slot_b) == 6 and len(pair_b) == 15 and rank(slot_b) == 6 and rank(pair_b) == 15
    L = [mm(V[3], W[4]), mm(V[4], W[3]), T3L()]
    R = [mm(V[3], V[4]), mm(W[4], W[3]), T3R()]
    for (tp, tm, t3) in (L, R):
        ok = ok and meq(comm(tp, tm), msc(2, t3))
        ok = ok and meq(comm(t3, tp), tp) and meq(comm(t3, tm), msc(-1, tm))
    ok = ok and all(not comm(x, y) for x in L for y in R)
    # inside slot bilinears + 1, and together with 1 they span it
    ok = ok and rank(slot_b + [ONE]) == 7 and rank(slot_b + [ONE] + L + R) == 7 and rank(L + R + [ONE]) == 7
    su3 = [mm(V[a], W[b]) for a in PAIRS for b in PAIRS if a != b]
    su3 += [msub(NUM[0], NUM[1]), msub(NUM[1], NUM[2])]
    ok = ok and len(su3) == 8 and rank(su3) == 8
    ok = ok and rank(pair_b + [ONE]) == 16 and rank(pair_b + [ONE] + su3 + [BL()]) == 16
    ok = ok and rank(su3 + [BL(), ONE]) == 10
    # Y = T_3R + (B - L)/2 exactly
    ok = ok and meq(HYP(), madd(T3R(), msc(F(1, 2), BL())))
    # the 24 mixed bilinears all move an excitation between a slot and a pair mode
    mixed = [X for (p, q), X in Bl.items() if (p in SLOT_G) != (q in SLOT_G)]
    NR = madd(NUM[3], NUM[4])
    ok = ok and len(mixed) == 24 and all(comm(NR, X) for X in mixed)
    GA.check("su(2)_L + su(2)_R in the slot bivectors, su(3) and B - L in the pair ones, Y = T3R + (B-L)/2", ok)
    return ok


def check_commutant_on_sixteen():
    premise("standard-model.hyp-s-slot-statistics")
    Bl = bilinears()
    gens = [X for (p, q), X in Bl.items() if same_block(p, q)]
    sixteen = [s for s in range(DIM) if ntot(s) % 2 == 0]
    ok = len(gens) == 21 and len(sixteen) == 16
    ok = ok and commutant_dim(gens, sixteen) == 2
    chi = diag(lambda s: -(-1) ** nr(s))
    chi16 = restrict(chi, sixteen)
    ok = ok and all(not comm(restrict(X, sixteen), chi16) for X in gens)
    ok = ok and sum(1 for s in sixteen if nr(s) == 1) == 8
    ok = ok and all(chi[(s, s)] == (1 if nr(s) == 1 else -1) for s in sixteen)
    GA.check("on the sixteen the commutant of the 21 is spanned by 1 and chi", ok)
    return ok
