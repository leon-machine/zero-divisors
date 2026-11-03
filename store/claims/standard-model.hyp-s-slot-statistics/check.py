"""standard-model.hyp-s-slot-statistics: exact checks.

(iv), (ii) slot content: for F = Lambda C^2 (F_0 = C, F_1 = C^2, F_2 = Lambda^2 C^2, the module the CPT-closure
    theorem forces under the generation clause) the U(2)-equivariant maps C^2 (x) F_n -> F_{n+1} are computed as
    exact kernels of the gl(2) intertwining equations: one line for n = 0 and n = 1, zero for n = 2; the
    composite a+(u) a+(u') from F_0 to F_2 is an antisymmetric bilinear form in (u, u'), so
    a+(u) a+(u') = -a+(u') a+(u) and a+(u)^2 = 0. Control: for the bosonic module S^2 C^2 the same
    computation gives a symmetric composite.
(ii) content: on Lambda(C^2 + C^3), the 32-dimensional five-mode module, the sector (j, k) (j slots, k pairs)
    carries U(2) x U(3) weights; SU(2) dimension, colour (dimension and triality) and Y = q/6 with
    q = 3 (U(2) weight sum) - 2 (U(3) weight sum) are read off the weights; the even half is
    (1,1)_0 + (1,3b)_{-2/3} + (2,3)_{1/6} + (2,1)_{-1/2} + (1,1)_1 + (1,3b)_{1/3}.
(iii), (i): the operators commuting with the 21 split-preserving Majorana bilinears (the Pati-Salam algebra)
    form a 4-dimensional space, spanned by the (slot parity, pair parity) projectors; with (2,3)_{1/6} in V+
    the CPT halvings there are (-1)^(j+k) and the pair parity, and anomaly freedom keeps (-1)^(j+k). The
    neutral-block step is checked directly: a deviation on span{Omega, Omega^top} commuting with the two-slot
    creation x and its adjoint vanishes. The tower grading (-1)^(pi j + k) equals the chirality on every sector
    exactly for odd pi (pi = 0..3 tested).
(v): the five modes satisfy one CAR system; the ten Majoranas (gamma_{2m} = v_m + w_m, gamma_{2m+1} =
    I (w_m - v_m), I central with I^2 = -1) satisfy gamma_p gamma_q + gamma_q gamma_p = 2 delta_pq, act
    irreducibly (commutant the scalars), and their product is a multiple of the parity (-1)^(j+k).
Anomaly freedom of the particle half: the four sums of the imported Fact vanish on it.
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
from collections import Counter


def gl2_basis():
    out = []
    for i in range(2):
        for j in range(2):
            out.append([[F(1) if (r, c) == (i, j) else F(0) for c in range(2)] for r in range(2)])
    return out


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def madd_d(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def equivariant_maps(act_src, act_tgt, ds, dt):
    """Kernel of phi -> phi act_src(X) - act_tgt(X) phi over the gl(2) basis; phi is dt x ds."""
    rows = []
    for X in gl2_basis():
        S, T = act_src(X), act_tgt(X)
        for i in range(dt):
            for j in range(ds):
                row = [F(0)] * (dt * ds)
                for k in range(ds):
                    row[i * ds + k] += S[k][j]
                for k in range(dt):
                    row[k * ds + j] -= T[i][k]
                rows.append(row)
    if not rows or dt * ds == 0:
        return []
    return GA.field_kernel(rows)


def act_F(n):
    """gl(2) on F_n = Lambda^n C^2: 0 on F_0, X on F_1, trace on F_2."""
    if n == 0:
        return lambda X: [[F(0)]]
    if n == 1:
        return lambda X: X
    return lambda X: [[X[0][0] + X[1][1]]]


def act_S2(X):
    """gl(2) on S^2 C^2 in the basis e1^2, e1 e2, e2^2."""
    a, b, c, d = X[0][0], X[0][1], X[1][0], X[1][1]
    return [[2 * a, b, F(0)], [2 * c, a + d, 2 * b], [F(0), c, 2 * d]]


def tensor_act(act, d):
    return lambda X: madd_d(kron(X, eye(d)), kron(eye(2), act(X)))


def check_equivariant_slot_creation_is_exclusive():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("standard-model.slot-module-hypothesis")
    k0 = equivariant_maps(tensor_act(act_F(0), 1), act_F(1), 2, 2)
    k1 = equivariant_maps(tensor_act(act_F(1), 2), act_F(2), 4, 1)
    ok = len(k0) == 1 and len(k1) == 1
    # a nonzero intertwiner C^2 (x) C^2 -> C^2 (x) C^2 that is not in the span of 1 exists (the swap),
    # so the one-dimensionality of k1 is a statement about the target Lambda^2, not a triviality
    ok = ok and len(equivariant_maps(tensor_act(act_F(1), 2), tensor_act(act_F(1), 2), 4, 4)) == 2
    phi0 = [k0[0][0:2], k0[0][2:4]]           # 2 x 2: u (x) 1 -> phi0 u
    phi1 = k1[0]                             # 1 x 4: u (x) u' -> phi1 . (u (x) u')
    ok = ok and phi0[0][1] == 0 and phi0[1][0] == 0 and phi0[0][0] == phi0[1][1] != 0
    # composite a+(u) a+(u') 1 = phi1 (u (x) phi0 u'): the bilinear form M[i][j] = phi1[2 i + j'] phi0[j'][j]
    M = [[sum(phi1[2 * i + jj] * phi0[jj][j] for jj in range(2)) for j in range(2)] for i in range(2)]
    ok = ok and all(M[i][j] == -M[j][i] for i in range(2) for j in range(2)) and M[0][1] != 0
    # control: bosonic S^2 C^2 gives a symmetric composite
    kb = equivariant_maps(tensor_act(act_F(1), 2), act_S2, 4, 3)
    ok = ok and len(kb) == 1
    Mb = [[[sum(kb[0][r * 4 + 2 * i + jj] * phi0[jj][j] for jj in range(2)) for j in range(2)]
           for i in range(2)] for r in range(3)]
    ok = ok and all(Mb[r][i][j] == Mb[r][j][i] for r in range(3) for i in range(2) for j in range(2))
    GA.check("equivariant slot creation on Lambda C^2 is unique and anticommuting (exclusion)", ok)
    return ok


def content():
    """Species of the five-mode module from its weights: (j, k) -> (SU(2) dim, colour, Y)."""
    sectors = {}
    for s in range(DIM):
        j, k = nr(s), nw(s)
        u2 = (s >> 3 & 1, s >> 4 & 1)
        u3 = (s & 1, s >> 1 & 1, s >> 2 & 1)
        get_or_set(sectors, (j, k), []).append((u2, u3))
    out = {}
    for (j, k), ws in sectors.items():
        u2w = Counter(w[0] for w in ws)
        u3w = Counter(w[1] for w in ws)
        d2 = len(u2w)
        d3 = len(u3w)
        tri = sum(next(iter(u3w))) % 3
        col = "1" if d3 == 1 else ("3" if tri == 1 else "3b")
        q = {3 * sum(a) - 2 * sum(b) for a, b in ws}
        out[(j, k)] = (d2, col, F(q.pop(), 6)) if len(q) == 1 else None
    return out


def check_five_mode_content():
    premise("standard-model.global-form-quotient-determined")
    C = content()
    ok = len(C) == 12 and None not in C.values()
    even = sorted(v for (j, k), v in C.items() if (j + k) % 2 == 0)
    want = sorted([(1, "1", F(0)), (1, "3b", F(-2, 3)), (2, "3", F(1, 6)), (2, "1", F(-1, 2)),
                   (1, "1", F(1)), (1, "3b", F(1, 3))])
    ok = ok and even == want
    ok = ok and C[(1, 1)] == (2, "3", F(1, 6)) and C[(1, 3)] == (2, "1", F(-1, 2))
    ok = ok and sum(d * (1 if c == "1" else 3) for d, c, y in even) == 16
    GA.check("the five-mode module's particle half is one generation with its lepton doublet", ok)
    return ok


CONJ = {"1": "1", "3": "3b", "3b": "3"}


def anomaly_sums(species):
    """The four sums of the imported anomaly Fact over a list of species (SU(2) dim, colour, Y)."""
    ncol = {"1": 1, "3": 3, "3b": 3}
    su3 = sum((d * y for d, c, y in species if c != "1"), F(0))
    su2 = sum((ncol[c] * y for d, c, y in species if d == 2), F(0))
    grav = sum((d * ncol[c] * y for d, c, y in species), F(0))
    cub = sum((d * ncol[c] * y ** 3 for d, c, y in species), F(0))
    return (su3, su2, grav, cub)


def check_chirality_is_total_mode_parity():
    """(iii) through the Pati-Salam clause: the 21 split-preserving Majorana bilinears have a commutant of
    dimension 4, spanned by the four (slot parity, pair parity) projectors; among the involutions there with
    trace 0 and (2,3)_{1/6} in V+, exactly two are CPT halvings, (-1)^(j+k) and the pair parity, and anomaly
    freedom keeps only (-1)^(j+k). The written-out step: off the neutral block Gamma = (-1)^(j+k), and a
    deviation supported on the block {Omega, Omega^top} that commutes with the two-slot creation x and its
    adjoint is zero (x alone leaves one line). (i): the tower grading equals it exactly for odd pi."""
    premise("standard-model.slot-module-hypothesis")
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    B = bilinears()
    slot_gam = set(range(2 * SLOTS[0], 2 * NM))            # Majoranas 6..9 of the slot modes
    PS = [X for (p, q), X in B.items() if (p in slot_gam) == (q in slot_gam)]
    ok = len(PS) == 21
    ok = ok and commutant_dim(PS, range(DIM)) == 4
    P = {(a, b): diag(lambda s, a=a, b=b: 1 if (nr(s) % 2, nw(s) % 2) == (a, b) else 0)
         for a in (0, 1) for b in (0, 1)}
    ok = ok and all(not comm(X, Q) for X in PS for Q in P.values())
    C = content()
    q_state = (1 << 0) | (1 << 3)            # one pair, one slot: a state of (2,3)_{1/6}
    cpt, free = [], []
    for signs in [(e0, e1, e2, e3) for e0 in (1, -1) for e1 in (1, -1) for e2 in (1, -1) for e3 in (1, -1)]:
        eps = dict(zip(sorted(P), signs))
        if sum(signs) != 0 or eps[(1, 1)] != 1:
            continue
        plus = sorted(C[jk] for jk in C if eps[(jk[0] % 2, jk[1] % 2)] == 1)
        minus = sorted(C[jk] for jk in C if eps[(jk[0] % 2, jk[1] % 2)] == -1)
        if sorted((d, CONJ[c], -y) for d, c, y in plus) == minus:
            cpt.append(eps)
            if anomaly_sums(plus) == (0, 0, 0, 0):
                free.append(eps)
    ok = ok and len(cpt) == 2 and len(free) == 1
    G = madd(*[msc(free[0][k], P[k]) for k in P])
    ok = ok and G[(q_state, q_state)] == 1 and meq(G, diag(lambda s: (-1) ** ntot(s)))
    # the other CPT halving is the pair parity, anomalous (SU(3)^2 U(1) sum 2/3 on its plus half)
    other = [e for e in cpt if e is not free[0]][0]
    ok = ok and all(other[(a, b)] == (-1) ** (b + 1) for (a, b) in P)
    ok = ok and anomaly_sums(sorted(C[jk] for jk in C if jk[1] % 2 == 1))[0] == F(2, 3)
    # written-out neutral-block step: x = two-slot creation, in the Pati-Salam span; x^dag its adjoint
    x = mm(V[3], V[4])
    xd = mm(W[4], W[3])
    ok = ok and in_span(PS, x) and in_span(PS, xd) and not in_span(PS, mm(V[0], V[3]))
    om, top = 0, DIM - 1
    blk = [(om, om), (om, top), (top, om), (top, top)]

    def flat(*Ms):
        out = {}
        for i, M in enumerate(Ms):
            for k, v in M.items():
                out[(i,) + k] = v
        return out
    devs = [{e: F(1)} for e in blk]
    ok = ok and rank([flat(comm(D, x), comm(D, xd)) for D in devs]) == 4
    ok = ok and rank([flat(comm(D, x)) for D in devs]) == 3
    # a number-conserving bilinear leaves the block free; the vacuum-swapped halving fails x
    u5 = mm(V[3], W[4])
    ok = ok and rank([flat(comm(D, u5), comm(D, fock.transpose(u5))) for D in devs]) == 0
    swap = madd(G, msc(-2, {(om, om): F(1)}), msc(2, {(top, top): F(1)}))
    ok = ok and meq(mm(swap, swap), ONE) and bool(comm(swap, x))
    # (i): the tower grading (-1)^(pi j + k) is this chirality on every sector iff pi is odd
    good = [pi for pi in range(4)
            if all((-1) ** (pi * nr(s) + nw(s)) == (-1) ** ntot(s) for s in range(DIM))]
    ok = ok and good == [1, 3]
    GA.check("the anomaly-free CPT halving commuting with Pati-Salam is the total mode parity; slot parity odd", ok)
    return ok


def check_one_clifford_system():
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    ok = True
    for i in range(NM):
        for j in range(NM):
            ok = ok and not acomm(V[i], V[j]) and meq(acomm(V[i], W[j]), ONE if i == j else {})
    # physical gamma_p = I^(p mod 2) g_p: gamma_p gamma_q + gamma_q gamma_p = (I^2)^(p mod 2) {g_p, g_q}
    for p in range(10):
        for q in range(10):
            sign = (-1) ** (p % 2) if p == q else 1
            want = msc(2, ONE) if p == q else {}
            ok = ok and meq(msc(sign, acomm(gam(p), gam(q))), want)
    ok = ok and commutant_dim([gam(p) for p in range(10)], range(DIM)) == 1
    prod = ONE
    for p in range(10):
        prod = mm(prod, gam(p))
    ok = ok and meq(prod, diag(lambda s: -(-1) ** ntot(s)))
    GA.check("two slot and three pair modes form one CAR system; Cl(10) on Lambda C^5, parity its chirality", ok)
    return ok


def check_particle_half_anomaly_free():
    premise("standard-model.imported-anomaly-coefficients")
    C = content()
    half = [v for (j, k), v in C.items() if (j + k) % 2 == 0]
    ncol = {"1": 1, "3": 3, "3b": 3}
    su3 = sum((d * y for d, c, y in half if c != "1"), F(0))
    su2 = sum((ncol[c] * y for d, c, y in half if d == 2), F(0))
    grav = sum((d * ncol[c] * y for d, c, y in half), F(0))
    cub = sum((d * ncol[c] * y ** 3 for d, c, y in half), F(0))
    ok = (su3, su2, grav, cub) == (0, 0, 0, 0)
    # control: dropping e^c = (1,1)_1 from the half breaks the gravitational sum
    ok = ok and sum((d * ncol[c] * y for d, c, y in half if y != 1), F(0)) == -1
    GA.check("the particle half satisfies the four anomaly conditions", ok)
    return ok
