"""standard-model.majorana-element: exact checks.

The five-mode module as 32 x 32 rational matrices (pair modes 0, 1, 2; slot modes 3, 4, the text's 4 and
5), T = v_1 v_2 v_3 v_4 v_5. The 21 of the Pati-Salam algebra in a weight basis: slot v_4 w_5, v_5 w_4,
N_4 - N_5, v_4 v_5, w_5 w_4, N_4 + N_5 - 1 and pair v_a w_b (a != b), n_a - 1/2, v_a v_b, w_a w_b
(its span is that of the 21 split-preserving Majorana bilinears, checked). The compact real form (the
real span of the 21) is i times the Hermitian elements of that span; an element A + iB (A, B real
matrices) is stored as the pair (A, B), and real ranks of images are taken on realified vectors.
Orbit spans are complex spans (the complex span of the orbit is the same for the real form).
(1) T has one nonzero entry, from the empty state (nu^c) to the full state; the form B(psi, T phi) of
    the invariant pairing (built by that Lemma's EXPORTS) is nonzero on the sixteen only at (nu^c, nu^c).
(2) [T, su(3)] = [T, su(2)_L] = [T, Y] = 0 and [B - L, T] = -2T; on the compact real span of the 21,
    X -> [X, T] has real rank 9, so its kernel is 12-dimensional, and the compact su(3) + su(2)_L + u(1)_Y
    (12 real-independent elements of that span, all fixing T) is that kernel. Control: over C the
    stabiliser is larger (16: the pair creators v_a v_b also kill T), which is why the real form matters.
(3) The orbit of T under repeated brackets with the 21 spans 30 dimensions; su(2)_L kills all of it;
    [T_3R, T] = T, [T_+R, T] = 0, ad(T_-R)^2 T != 0, ad(T_-R)^3 T = 0 (highest weight of a triplet);
    the ad T_3R eigenspaces are 10 + 10 + 10, and on the top one ad(B - L) has the weights of the
    symmetric square of the 4 with B - L weights (1/3, 1/3, 1/3, -1): {2/3 x 6, -2/3 x 3, -2 x 1}.
    So the orbit is the (10,1,3).
(4) X = 2 T_3R - (3/2)(B - L) equals 2Y - (5/2)(B - L) and N - 5/2 on every species, and [X, T] = 5T,
    so the vev along T breaks it.
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
tr = fock.transpose   # the transpose (fock.trace is the trace)


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

PAIR_G = tuple(range(6))
SLOT_G = (6, 7, 8, 9)
SPECIES = {(0, 0): "nuc", (2, 0): "uc", (1, 1): "Q", (3, 1): "L", (0, 2): "ec", (2, 2): "dc"}


def T_el():
    return mm(V[0], V[1], V[2], V[3], V[4])


def HYP():
    return diag(lambda s: F(3 * nr(s) - 2 * nw(s), 6))


def BL():
    return diag(lambda s: 1 - F(2, 3) * nw(s))


def T3R():
    return msc(F(1, 2), madd(NUM[3], NUM[4], msc(-1, ONE)))


def su2L():
    return [mm(V[3], W[4]), mm(V[4], W[3]), msub(NUM[3], NUM[4])]


def su2R():
    return [mm(V[3], V[4]), mm(W[4], W[3]), T3R()]


def su3():
    out = [mm(V[a], W[b]) for a in PAIRS for b in PAIRS if a != b]
    return out + [msub(NUM[0], NUM[1]), msub(NUM[1], NUM[2])]


def ps21():
    out = su2L() + [mm(V[3], V[4]), mm(W[4], W[3]), madd(NUM[3], NUM[4], msc(-1, ONE))]
    out += [mm(V[a], W[b]) for a in PAIRS for b in PAIRS if a != b]
    out += [msub(NUM[a], msc(F(1, 2), ONE)) for a in PAIRS]
    out += [mm(V[a], V[b]) for a in PAIRS for b in PAIRS if a < b]
    out += [mm(W[a], W[b]) for a in PAIRS for b in PAIRS if a < b]
    return out


def eigen(H, X):
    """c with [H, X] = c X, or None."""
    Y = comm(H, X)
    k = next(iter(X))
    c = Y.get(k, 0) / X[k]
    return c if meq(Y, msc(c, X)) else None


def check_t_pairs_nu_c_with_itself():
    pairing = premise("standard-model.invariant-pairing-five-modes")["pairing"]
    premise("standard-model.hyp-s-slot-statistics")
    T = T_el()
    ok = len(T) == 1 and list(T)[0] == (31, 0)
    B = pairing()
    BT = mm(B, T)
    sixteen = [s for s in range(DIM) if ntot(s) % 2 == 0]
    ent = {(a, b): x for (a, b), x in BT.items() if a in sixteen and b in sixteen}
    ok = ok and list(ent) == [(0, 0)] and SPECIES[(nw(0), nr(0))] == "nuc"
    GA.check("T maps nu^c to the full state; B(psi, T phi) on the sixteen is the nu^c nu^c entry", ok)
    return ok


def compact21():
    """Real basis (A, B) of the compact real span, X = A + iB."""
    out = []
    for blk in (SLOTS, PAIRS):
        out += [({}, msub(NUM[a], msc(F(1, 2), ONE))) for a in blk]
        for a in blk:
            for b in blk:
                if a < b:
                    out.append(({}, madd(mm(V[a], W[b]), mm(V[b], W[a]))))
                    out.append((msub(mm(V[a], W[b]), mm(V[b], W[a])), {}))
                    out.append(({}, madd(mm(V[a], V[b]), mm(W[b], W[a]))))
                    out.append((msub(mm(V[a], V[b]), mm(W[b], W[a])), {}))
    return out


def compact_sm():
    out = [({}, msub(NUM[0], NUM[1])), ({}, msub(NUM[1], NUM[2]))]
    for a in PAIRS:
        for b in PAIRS:
            if a < b:
                out.append(({}, madd(mm(V[a], W[b]), mm(V[b], W[a]))))
                out.append((msub(mm(V[a], W[b]), mm(V[b], W[a])), {}))
    out += [({}, msub(NUM[3], NUM[4])), ({}, madd(mm(V[3], W[4]), mm(V[4], W[3]))),
            (msub(mm(V[3], W[4]), mm(V[4], W[3])), {}), ({}, HYP())]
    return out


def realify(A, B):
    v = {("re",) + k: x for k, x in A.items()}
    v.update({("im",) + k: x for k, x in B.items()})
    return v


def check_stabiliser_is_standard_model():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("standard-model.under-s-composites-state-space-spinor")
    T = T_el()
    gens = ps21()
    split = [X for (p, q), X in bilinears().items() if (p in SLOT_G) == (q in SLOT_G)]
    ok = len(gens) == 21 and rank(gens) == 21 and rank(gens + split) == 21
    ok = ok and all(not comm(X, T) for X in su3() + su2L()) and not comm(HYP(), T)
    ok = ok and meq(comm(BL(), T), msc(-2, T))
    K = compact21()
    ok = ok and len(K) == 21 and rank([realify(A, B) for A, B in K]) == 21
    # each compact element is anti-Hermitian: A antisymmetric, B symmetric, and lies in the complex span
    ok = ok and all(meq(tr(A), msc(-1, A)) and meq(tr(B), B) for A, B in K)
    ok = ok and all(in_span(gens, A) and in_span(gens, B) for A, B in K)
    ok = ok and rank([realify(comm(A, T), comm(B, T)) for A, B in K]) == 9
    sm = compact_sm()
    ok = ok and len(sm) == 12 and rank([realify(A, B) for A, B in sm]) == 12
    ok = ok and rank([realify(A, B) for A, B in K + sm]) == 21
    ok = ok and all(not comm(A, T) and not comm(B, T) for A, B in sm)
    # control: over C the stabiliser of T in the 21 is 16-dimensional
    ok = ok and 21 - rank([comm(X, T) for X in gens]) == 16
    GA.check("the subalgebra of the compact 21 fixing T is su(3) + su(2)_L + u(1)_Y, dimension 12", ok)
    return ok


def check_orbit_is_10_1_3():
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    premise("standard-model.under-s-composites-state-space-spinor")
    T = T_el()
    gens = ps21()
    sp = Span()
    sp.add(T)
    orbit, frontier = [T], [T]
    while frontier:
        new = []
        for X in frontier:
            for g in gens:
                Y = comm(g, X)
                if sp.add(Y):
                    orbit.append(Y)
                    new.append(Y)
        frontier = new
    ok = len(orbit) == 30
    ok = ok and all(not comm(l, X) for l in su2L() for X in orbit)
    tp, tm, t3 = su2R()
    ok = ok and meq(comm(t3, T), T) and not comm(tp, T)
    a2 = comm(tm, comm(tm, T))
    ok = ok and bool(a2) and not comm(tm, a2)
    by_t3, top_bl = Counter(), Counter()
    tops = {}
    for X in orbit:
        c3, cb = eigen(t3, X), eigen(BL(), X)
        ok = ok and c3 is not None and cb is not None
        by_t3[c3] += 1
        if c3 == 1:
            get_or_set(tops, cb, []).append(X)
    ok = ok and by_t3 == Counter({F(1): 10, F(0): 10, F(-1): 10})
    top_dims = {cb: rank(Xs) for cb, Xs in tops.items()}
    ok = ok and top_dims == {F(2, 3): 6, F(-2, 3): 3, F(-2): 1}
    GA.check("the orbit of T under the 21 is the (10,1,3), T the su(2)_R highest weight", ok)
    return ok


def check_thirteenth_generator_broken():
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.automorphisms-preserve-slot-pair-split-are")
    X1 = madd(msc(2, T3R()), msc(F(-3, 2), BL()))
    X2 = madd(msc(2, HYP()), msc(F(-5, 2), BL()))
    X3 = diag(lambda s: ntot(s) - F(5, 2))
    ok = meq(X1, X2) and meq(X1, X3)
    vals = {}
    for s in range(DIM):
        if ntot(s) % 2 == 0:
            get_or_set(vals, SPECIES[(nw(s), nr(s))], set()).add(X1.get((s, s), 0))
    ok = ok and vals == {"nuc": {F(-5, 2)}, "Q": {F(-1, 2)}, "uc": {F(-1, 2)}, "ec": {F(-1, 2)},
                         "L": {F(3, 2)}, "dc": {F(3, 2)}}
    ok = ok and meq(comm(X1, T_el()), msc(5, T_el()))
    GA.check("X = 2 T3R - (3/2)(B - L) = N - 5/2, and [X, T] = 5T", ok)
    return ok
