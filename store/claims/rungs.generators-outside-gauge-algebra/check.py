"""rungs.generators-outside-gauge-algebra: exact checks.

The composite's five modes (three pair modes, two rung/slot modes) as the 32-dimensional Fock module,
exact rational matrices (Jordan-Wigner). The ten Majoranas are g_{2m} = v_m + w_m, g_{2m+1} = w_m - v_m
(the text's gamma_{2m+1} is I g_{2m+1} with I central, so complex spans agree); the 45 bilinears
g_p g_q span so(10). The counts are kernel dimensions of linear maps on that span, computed as
45 - rank of the images (the bilinears are independent):
(1) ad N (N the total mode number) has a 25-dimensional kernel, spanned by v_i w_j (i != j) and
    n_i - 1/2: u(5); the other 20 bilinear directions v_i v_j, w_i w_j have [N, X] = +-2X.
(2) ad N_R and ad N_W jointly have a 13-dimensional kernel, spanned by the v_a w_b with a, b both rungs
    or both pairs (4 + 9): u(2) + u(3).
(3) The 12 = 25 - 13 directions v_a w_b with one rung and one pair index have [N_R, X] = +-X and
    [N_W, X] = -+X: one excitation moves between a rung and a pair. 45 - 13 = 32 lie outside.
The five-mode CAR is Hypothesis (S)'s clause (v) (or the rung reading (R), which gives the same module);
the span of the bilinears being so(10) is the imported Bogoliubov Fact.
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


def create(m):
    return fock.cre(m, NM)


# sparse exact operators from lib/fock.py (LSB order; comm and acomm are not halved); tr is the TRANSPOSE
tr = fock.transpose
mm, madd, msc, msub = fock.mm, fock.madd, fock.msc, fock.msub
comm, acomm, meq = fock.comm, fock.acomm, fock.meq
restrict = fock.restrict


ONE = fock.eye(DIM)
V = [create(m) for m in range(NM)]          # v_m, creation
W = [tr(v) for v in V]                      # w_m, annihilation
NUM = [fock.num(m, NM) for m in range(NM)]   # n_m


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


def nr_op():
    return madd(NUM[3], NUM[4])


def nw_op():
    return madd(NUM[0], NUM[1], NUM[2])


def check_mode_number_preserving_is_u5():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    premise("standard-model.hyp-s-slot-statistics")
    B = list(bilinears().values())
    N = madd(nr_op(), nw_op())
    ok = rank(B) == 45
    kernel = 45 - rank([comm(N, X) for X in B])
    ok = ok and kernel == 25
    u5 = [mm(V[i], W[j]) for i in range(NM) for j in range(NM) if i != j]
    u5 += [msub(NUM[i], msc(F(1, 2), ONE)) for i in range(NM)]
    ok = ok and len(u5) == 25 and rank(u5) == 25
    ok = ok and rank(B + u5) == 45                      # inside the span of the bilinears
    ok = ok and all(not comm(N, X) for X in u5)         # inside the kernel, so they span it
    changing = [mm(V[i], V[j]) for i in range(NM) for j in range(i + 1, NM)]
    changing += [mm(W[i], W[j]) for i in range(NM) for j in range(i + 1, NM)]
    ok = ok and len(changing) == 20 and rank(B + changing) == 45 and rank(u5 + changing) == 45
    ok = ok and all(meq(comm(N, X), msc(2, X)) for X in changing[:10])
    ok = ok and all(meq(comm(N, X), msc(-2, X)) for X in changing[10:])
    GA.check("25 of the 45 preserve the mode number (u(5)); 20 change it by two", ok)
    return ok


def check_split_preserving_is_u2_u3():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    premise("standard-model.hyp-s-slot-statistics")
    B = list(bilinears().values())
    NR, NW = nr_op(), nw_op()
    images = [madd({("R",) + k: x for k, x in comm(NR, X).items()},
                   {("W",) + k: x for k, x in comm(NW, X).items()}) for X in B]
    kernel = 45 - rank(images)
    ok = kernel == 13
    blocks = [(a, b) for a in SLOTS for b in SLOTS] + [(a, b) for a in PAIRS for b in PAIRS]
    u23 = [mm(V[a], W[b]) if a != b else msub(NUM[a], msc(F(1, 2), ONE)) for a, b in blocks]
    ok = ok and len(u23) == 13 and rank(u23) == 13 and rank(B + u23) == 45
    ok = ok and all(not comm(NR, X) and not comm(NW, X) for X in u23)
    cross = [mm(V[a], W[b]) for a in SLOTS for b in PAIRS] + [mm(V[b], W[a]) for a in SLOTS for b in PAIRS]
    ok = ok and len(cross) == 12 and rank(u23 + cross) == 25
    # v_rung w_pair raises N_R by one and lowers N_W by one, and conversely
    ok = ok and all(meq(comm(NR, X), X) and meq(comm(NW, X), msc(-1, X)) for X in cross[:6])
    ok = ok and all(meq(comm(NR, X), msc(-1, X)) and meq(comm(NW, X), X) for X in cross[6:])
    ok = ok and 45 - kernel == 32
    GA.check("13 preserve the slot-pair split and the mode number (u(2) + u(3)); 12 move one excitation", ok)
    return ok
