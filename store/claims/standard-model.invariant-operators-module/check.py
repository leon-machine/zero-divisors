"""standard-model.invariant-operators-module: exact checks.

The two-rung module Lambda(W + R_2) as 32 x 32 rational matrices (pair modes 0, 1, 2; rung/slot modes 3, 4);
s(u(2) + u(3)) acts through X -> sum X_ab v_a w_b, with the basis E_ab (a != b in one block: 2 + 6),
the traceless diagonals n_3 - n_4, n_0 - n_1, n_1 - n_2, and 3 N_R - 2 N_W (12 elements). The sector (j, k)
is the span of the states with j rungs and k pairs occupied.
(1) The commutant of the 12 on the module is 14-dimensional and on the even half (16 states) 6-dimensional
    (exact sparse elimination over all 32 x 32, respectively 16 x 16, matrix entries).
(2) Characters: the twelve sectors have pairwise distinct weight multisets (Cartan eigenvalues of
    n_0 - n_1, n_1 - n_2, n_3 - n_4, 3 N_R - 2 N_W) except (0,0) and (2,3), which agree; so
    14 = 10 x 1 + 2^2. The operator |filled><vacuum| commutes with the 12 and anticommutes with the
    chirality (-1)^(j+k), the two states having j + k = 0 and 5.
(3) On the even half the six sector projectors commute with the 12 and are independent, so an invariant
    operator there is one free number per species (nu^c, u^c, Q, L, e^c, d^c); nothing in the algebra relates them.
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
comm, acomm, restrict = fock.comm, fock.acomm, fock.restrict


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
from collections import Counter

SPECIES = {(0, 0): "nuc", (2, 0): "uc", (1, 1): "Q", (3, 1): "L", (0, 2): "ec", (2, 2): "dc"}


def gens12():
    out = [mm(V[a], W[b]) for a in SLOTS for b in SLOTS if a != b]
    out += [mm(V[a], W[b]) for a in PAIRS for b in PAIRS if a != b]
    out += [msub(NUM[3], NUM[4]), msub(NUM[0], NUM[1]), msub(NUM[1], NUM[2])]
    out += [madd(msc(3, madd(NUM[3], NUM[4])), msc(-2, madd(NUM[0], NUM[1], NUM[2])))]
    return out


def weight(s):
    n = [s >> m & 1 for m in range(NM)]
    return (n[0] - n[1], n[1] - n[2], n[3] - n[4], 3 * (n[3] + n[4]) - 2 * (n[0] + n[1] + n[2]))


def check_commutant_dimensions():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.hyp-s-slot-statistics")
    g = gens12()
    ok = len(g) == 12 and rank(g) == 12
    ok = ok and commutant_dim(g, range(DIM)) == 14
    even = [s for s in range(DIM) if ntot(s) % 2 == 0]
    ok = ok and len(even) == 16 and commutant_dim(g, even) == 6
    GA.check("the commutant of s(u(2) + u(3)) is 14-dimensional on the module and 6 on the even half", ok)
    return ok


def check_sectors_and_the_chirality_changing_operator():
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.hyp-s-slot-statistics")
    chars = {}
    for s in range(DIM):
        get_or_set(chars, (nr(s), nw(s)), Counter())[weight(s)] += 1
    ok = len(chars) == 12
    keys = sorted(chars)
    same = [(a, b) for i, a in enumerate(keys) for b in keys[i + 1:] if chars[a] == chars[b]]
    ok = ok and same == [((0, 0), (2, 3))]
    classes = Counter(tuple(sorted(c.items())) for c in chars.values())
    ok = ok and sum(m * m for m in classes.values()) == 14 and len(classes) == 11
    K = {(31, 0): F(1)}
    ok = ok and all(not comm(K, X) for X in gens12())
    chi = diag(lambda s: (-1) ** ntot(s))
    ok = ok and not acomm(K, chi) and ntot(0) == 0 and ntot(31) == 5
    GA.check("sectors inequivalent except vacuum and filled state; the off-diagonal invariant changes chirality", ok)
    return ok


def check_one_mass_per_species():
    premise("standard-model.hyp-s-slot-statistics")
    even = [s for s in range(DIM) if ntot(s) % 2 == 0]
    proj = {}
    for s in even:
        get_or_set(proj, SPECIES[(nw(s), nr(s))], {})[(s, s)] = F(1)
    ok = sorted(proj) == sorted(["nuc", "uc", "Q", "L", "ec", "dc"])
    ok = ok and sorted(len(P) for P in proj.values()) == [1, 1, 2, 3, 3, 6]
    ok = ok and all(not comm(restrict(X, even), P) for X in gens12() for P in proj.values())
    ok = ok and rank(list(proj.values())) == 6
    GA.check("on the even half an invariant operator is one number per species", ok)
    return ok
