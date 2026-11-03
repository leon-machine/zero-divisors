"""standard-model.invariant-pairing-five-modes: exact checks.

The five-mode module Lambda(W + R_2) as 32 x 32 rational matrices (Jordan-Wigner, occupation basis
e_S = v_{m1} ... v_{mk}|0> with m1 < ... < mk). B is built from its defining formula: B(e_S, e_T) is
(-1)^(|S|(|S|-1)/2) eps(S, S^c) when T = S^c and 0 otherwise, eps(S, S^c) the sign of the permutation
(S, S^c) of (1, ..., 5).
(1) B is nondegenerate (a signed permutation matrix of rank 32), pairs each state only with its complement,
    the 16 only with the 16bar, and vanishes on all 16 x 16 pairs of even states.
(2) The 45 bilinears v_i w_j (i != j), v_i v_j, w_i w_j (i < j), n_i - 1/2 are independent and span the
    same space as the Majorana bilinears g_p g_q (so(10)); each X satisfies X^T B + B X = 0, which is
    B(X psi, phi) + B(psi, X phi) = 0 for all psi, phi (all 46080 basis identities at once).
    Control: dropping the reversal sign (-1)^(|S|(|S|-1)/2) breaks invariance under pair creation.
The claim has no premises; no premise() call. EXPORTS["pairing"] builds B for the checks that use it.
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
restrict = fock.restrict
tr = fock.transpose   # the transpose (fock.trace is the trace)


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


def complement(s):
    return (DIM - 1) ^ s


def eps_sign(s):
    S = [m for m in range(NM) if s >> m & 1]
    Sc = [m for m in range(NM) if not s >> m & 1]
    seq = S + Sc
    inv = sum(1 for i in range(NM) for j in range(i + 1, NM) if seq[i] > seq[j])
    return (-1) ** inv


def pairing(with_reversal=True):
    B = {}
    for s in range(DIM):
        k = bin(s).count("1")
        rev = (-1) ** (k * (k - 1) // 2) if with_reversal else 1
        B[(s, complement(s))] = F(rev * eps_sign(s))
    return B


def generators():
    gens = []
    for i in range(NM):
        for j in range(NM):
            if i != j:
                gens.append(mm(V[i], W[j]))
    for i in range(NM):
        for j in range(i + 1, NM):
            gens.append(mm(V[i], V[j]))
            gens.append(mm(W[i], W[j]))
    for i in range(NM):
        gens.append(msub(NUM[i], msc(F(1, 2), ONE)))
    return gens


def invariant(B, X):
    return not madd(mm(tr(X), B), mm(B, X))


def check_pairing_complement_nondegenerate():
    B = pairing()
    dense = [[B.get((r, c), F(0)) for c in range(DIM)] for r in range(DIM)]
    ok = GA.field_rank(dense) == 32
    # each row and each column carries exactly one entry, +-1, at the complement
    ok = ok and len(B) == 32 and all(abs(x) == 1 for x in B.values())
    ok = ok and all(c == complement(r) for (r, c) in B)
    ok = ok and len({c for (r, c) in B}) == 32
    even = [s for s in range(DIM) if bin(s).count("1") % 2 == 0]
    odd = [s for s in range(DIM) if bin(s).count("1") % 2 == 1]
    ok = ok and len(even) == 16 and len(odd) == 16
    # even pairs only with odd: the 16 with the 16bar, and the bare pairing of two sixteens vanishes
    ok = ok and sum(1 for (r, c) in B if r in even and c in odd) == 16
    ok = ok and sum(1 for (r, c) in B if r in even and c in even) == 0
    ok = ok and all(B.get((a, b), 0) == 0 for a in even for b in even)
    # two hand values: B(e_0, e_12345) = +1 and B(e_{12}, e_{345}) = (-1)^1 * (+1) = -1
    ok = ok and B[(0, 31)] == 1 and B[(3, 28)] == -1
    GA.check("B pairs each state with its complement only; nondegenerate; zero on two sixteens", ok)
    return ok


def check_so10_invariance():
    B = pairing()
    gens = generators()
    ok = len(gens) == 45 and rank(gens) == 45
    # the same span as the Majorana bilinears plus the identity: so(10) together with 1
    majo = list(bilinears().values())
    ok = ok and rank(majo + [ONE]) == 46 and rank(gens + majo + [ONE]) == 46
    ok = ok and all(invariant(B, X) for X in gens)
    ok = ok and all(invariant(B, X) for X in majo)
    # control: without the reversal sign, pair creation v_1 v_2 is not skew for the form
    Bbad = pairing(with_reversal=False)
    bad = [X for X in gens if not invariant(Bbad, X)]
    ok = ok and len(bad) > 0 and not invariant(Bbad, mm(V[0], V[1]))
    GA.check("B(X psi, phi) + B(psi, X phi) = 0 for all 45 generators of so(10)", ok)
    return ok


EXPORTS = {"pairing": pairing}
