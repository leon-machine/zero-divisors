"""standard-model.module-factorises-even-ground-elements-act: exact checks.

Lambda(W + R_2) as 32 x 32 rational matrices in the Jordan-Wigner form, pair modes 0, 1, 2 (W) ordered
before the rung modes 3, 4 (R_2). A state s factorises as (s & 7, s >> 3): the occupation basis of
Lambda W (x) Lambda R_2. V_C (x) C is spanned by the pair operators v_a, w_a; the rung plane by v_3, w_3,
v_4, w_4. An operator has the form X_W (x) 1 when all its entries keep the rung part and its 8 x 8 block is
the same on each of the four rung states; it has the form gamma (x) y_R with gamma = (-1)^(N_W) when all its
entries keep the pair part and equal (-1)^(N_W) times one 4 x 4 block y_R.
(0) The ten mode operators satisfy the CAR of five modes and their commutant is the scalars (exact
    elimination over all 1024 matrix entries): the module is irreducible, the generated algebra is
    M_32(C) (Burnside), 32 = 8 x 4.
(1) Every pair operator, every product of two, and every even product of distinct pair operators (the 32
    monomials spanning Cl^0(V_C), among them the 15 bivectors of so(2,4)) has the form X_W (x) 1; no rung
    operator has it.
(2) Every rung operator has the form gamma (x) y_R, anticommutes with every pair operator, and every
    product of two rung operators has the form 1 (x) Y_R.
(3) Every pair bivector commutes with N_R, with the four v_a w_b (a, b rungs) and with every product of
    two rung operators.
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


mm, madd, comm, acomm = fock.mm, fock.madd, fock.comm, fock.acomm
meq, restrict = fock.meq, fock.restrict


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

PAIR_OPS = [V[a] for a in PAIRS] + [W[a] for a in PAIRS]
RUNG_OPS = [V[a] for a in SLOTS] + [W[a] for a in SLOTS]


def block_W(X):
    """Return the 8 x 8 block if X = X_W (x) 1, else None."""
    blk = {}
    for (r, c), x in X.items():
        if r >> 3 != c >> 3:
            return None
        get_or_set(blk, (r & 7, c & 7), set()).add(x)
    if any(len(v) != 1 for v in blk.values()):
        return None
    full = {(w1 + 8 * rho, w2 + 8 * rho) for (w1, w2) in blk for rho in range(4)}
    return blk if full == set(X) else None


def block_R(X, twisted):
    """Return y_R if X = gamma (x) y_R (twisted, gamma = (-1)^N_W) or 1 (x) y_R, else None."""
    blk = {}
    for (r, c), x in X.items():
        if r & 7 != c & 7:
            return None
        g = (-1) ** bin(c & 7).count("1") if twisted else 1
        get_or_set(blk, (r >> 3, c >> 3), set()).add(x * g)
    if any(len(v) != 1 for v in blk.values()):
        return None
    full = {(8 * y1 + w, 8 * y2 + w) for (y1, y2) in blk for w in range(8)}
    return blk if full == set(X) else None


def check_module_irreducible_and_factorised():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    premise("standard-model.imported-cauchy-decomposition-exterior-power")
    ok = True
    for i in range(NM):
        for j in range(NM):
            ok = ok and not acomm(V[i], V[j]) and not acomm(W[i], W[j])
            ok = ok and meq(acomm(V[i], W[j]), ONE if i == j else {})
    ok = ok and commutant_dim(V + W, range(DIM)) == 1
    # the occupation basis is the product basis: 8 pair states times 4 rung states
    ok = ok and len({(s & 7, s >> 3) for s in range(DIM)}) == 32 and DIM == 8 * 4
    GA.check("five CAR pairs act irreducibly on Lambda W (x) Lambda R_2 = C^8 (x) C^4", ok)
    return ok


def check_even_ground_elements_act_on_pairs_only():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    ok = all(block_W(X) is not None for X in PAIR_OPS)
    ok = ok and all(block_W(X) is None for X in RUNG_OPS)
    ok = ok and all(block_W(mm(X, Y)) is not None for X in PAIR_OPS for Y in PAIR_OPS)
    biv = [mm(PAIR_OPS[i], PAIR_OPS[j]) for i, j in combinations(range(6), 2)]
    ok = ok and len(biv) == 15
    even = []
    for k in (0, 2, 4, 6):
        for idx in combinations(range(6), k):
            M = ONE
            for i in idx:
                M = mm(M, PAIR_OPS[i])
            even.append(M)
    ok = ok and len(even) == 32 and all(block_W(M) is not None for M in even)
    ok = ok and rank(even) == 32
    GA.check("every element of the even ground subalgebra acts as X_W (x) 1", ok)
    return ok


def check_rung_vectors_twisted_and_commuting():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    ok = all(block_R(X, True) is not None for X in RUNG_OPS)
    ok = ok and all(block_R(X, False) is None for X in RUNG_OPS)
    ok = ok and all(not acomm(X, Y) for X in PAIR_OPS for Y in RUNG_OPS)
    rbiv = [mm(X, Y) for X in RUNG_OPS for Y in RUNG_OPS]
    ok = ok and all(block_R(Z, False) is not None for Z in rbiv)
    NR = madd(NUM[3], NUM[4])
    mix = [mm(V[a], W[b]) for a in SLOTS for b in SLOTS]
    pbiv = [mm(PAIR_OPS[i], PAIR_OPS[j]) for i, j in combinations(range(6), 2)]
    ok = ok and len(mix) == 4 and len(rbiv) == 16
    ok = ok and all(not comm(X, Z) for X in pbiv for Z in [NR] + mix + rbiv)
    # control: a single pair operator does not commute with a rung operator
    ok = ok and bool(comm(V[0], V[3]))
    GA.check("rung vectors act as (-1)^N_W (x) y_R; so(V_C) commutes with the rung algebra", ok)
    return ok
