"""standard-model.matching-traces: exact checks.

The five-mode module as 32 x 32 rational matrices (pair modes 0, 1, 2; slot modes 3, 4), the sixteen being
the states of even total mode number; T_3L = (N_4 - N_5)/2, T_3R = (N_4 + N_5 - 1)/2, B - L = 1 - (2/3) N_W,
Y = (3 N_R - 2 N_W)/6.
(1) On the sixteen: tr T_3L^2 = tr T_3R^2 = 2, tr (B - L)^2 = 16/3, tr Y^2 = 10/3, and tr T_3R (B - L) = 0.
(2) The su(4) generator along B - L in the normalisation of T_3L is T_BL = c (B - L) with c^2 = 3/8
    (tr T_BL^2 = tr T_3L^2); Y = T_3R + (1/2)(B - L) = T_3R + k T_BL with k^2 = (1/4)/(3/8) = 2/3. Hence
    alpha_Y^-1 = alpha_2R^-1 + (2/3) alpha_4^-1 and, with a_1 = (3/5) alpha_Y^-1, a_1 = (3/5) a_2R + (2/5) a_4;
    the two weights equal tr T_3R^2 / tr Y^2 and (1/4) tr (B - L)^2 / tr Y^2 and sum to 1. The relation is
    checked as an identity at exact sample couplings.
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


mm, madd, msc, comm = fock.mm, fock.madd, fock.msc, fock.comm
meq, restrict = fock.meq, fock.restrict


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

SAMPLES = [(F(45), F(30)), (F(7, 2), F(-11, 3)), (F(46), F(46))]


def sixteen():
    return [s for s in range(DIM) if ntot(s) % 2 == 0]


def ops():
    return {"T3L": diag(lambda s: F((s >> 3 & 1) - (s >> 4 & 1), 2)),
            "T3R": diag(lambda s: F(nr(s) - 1, 2)),
            "BL": diag(lambda s: 1 - F(2, 3) * nw(s)),
            "Y": diag(lambda s: F(3 * nr(s) - 2 * nw(s), 6))}


def tr16(A):
    return sum((A.get((s, s), 0) for s in sixteen()), F(0))


def check_traces_on_sixteen():
    O = ops()
    ok = len(sixteen()) == 16
    ok = ok and tr16(mm(O["T3L"], O["T3L"])) == 2 and tr16(mm(O["T3R"], O["T3R"])) == 2
    ok = ok and tr16(mm(O["BL"], O["BL"])) == F(16, 3) and tr16(mm(O["Y"], O["Y"])) == F(10, 3)
    ok = ok and tr16(mm(O["T3R"], O["BL"])) == 0
    # T_3L is the slot mixing generator: it is half the commutator of v_4 w_5 and v_5 w_4
    ok = ok and meq(O["T3L"], msc(F(1, 2), comm(mm(V[3], W[4]), mm(V[4], W[3]))))
    GA.check("tr T3L^2 = tr T3R^2 = 2, tr (B-L)^2 = 16/3, tr Y^2 = 10/3 on the sixteen", ok)
    return ok


def check_matching_relations():
    premise("standard-model.imported-one-loop-running-trace-ratio")
    O = ops()
    t3 = tr16(mm(O["T3L"], O["T3L"]))
    c2 = t3 / tr16(mm(O["BL"], O["BL"]))          # T_BL = c (B - L): c^2 tr (B-L)^2 = tr T3L^2
    ok = c2 == F(3, 8)
    ok = ok and meq(O["Y"], madd(O["T3R"], msc(F(1, 2), O["BL"])))
    k2 = F(1, 4) / c2                              # Y = T3R + k T_BL with k c = 1/2
    ok = ok and k2 == F(2, 3)
    w1 = tr16(mm(O["T3R"], O["T3R"])) / tr16(mm(O["Y"], O["Y"]))
    w2 = F(1, 4) * tr16(mm(O["BL"], O["BL"])) / tr16(mm(O["Y"], O["Y"]))
    ok = ok and w1 == F(3, 5) and w2 == F(2, 5) and w1 + w2 == 1
    for a2R, a4 in SAMPLES:
        aY = a2R + k2 * a4                        # alpha_Y^-1 = alpha_2R^-1 + k^2 alpha_4^-1
        a1 = F(3, 5) * aY                         # Fact (a): a_1 = (3/5) alpha_Y^-1
        ok = ok and a1 == F(3, 5) * a2R + F(2, 5) * a4
    # at a point of Pati-Salam unification a_2R = a_4 the matched a_1 equals it
    ok = ok and F(3, 5) * (SAMPLES[2][0] + k2 * SAMPLES[2][1]) == SAMPLES[2][0]
    GA.check("a_1 = (3/5) a_2R + (2/5) a_4, a_2 = a_2L, a_3 = a_4 at the Pati-Salam breaking", ok)
    return ok
