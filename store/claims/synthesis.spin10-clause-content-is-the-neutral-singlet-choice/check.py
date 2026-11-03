"""synthesis.spin10-clause-content-is-the-neutral-singlet-choice: exact checks.

Five fermionic modes on Lambda(C^5) (fock.py, LSB bitmask basis): modes 0, 1 the slot modes (C^2), modes
2, 3, 4 the pair modes (W). n = slot number, k = pair number, Y = (3n - 2k)/6. Gauge algebra of
S(U(2) x U(3)): su(2) on the slots, su(3) on the pairs, Y. Number-conserving bilinears a_i* a_j span u(5);
all bilinears (a_i* a_j, a_i a_j, a_i* a_j*) span so(10) acting through Spin(10); the ten Majoranas
generate Cl(10). Commutants are computed exactly as the solution spaces of [X, g] = 0 for all generators g,
with X supported on pairs of states of equal weight under the diagonal generators of the set.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

M = 5
DIM = 2 ** M
QI = GA.QI
I = GA.QI_I
ONE = fock.eye(DIM)


def cre(k):
    return fock.cre(k, M)


def ann(k):
    return fock.ann(k, M)


def bil(i, j):
    return fock.mm(cre(i), ann(j))


def nslot(s):
    return fock.popcount(s & 3)


def npair(s):
    return fock.popcount(s >> 2)


def deg(s):
    return fock.popcount(s)


def diag(fn):
    return {(s, s): F(fn(s)) for s in range(DIM) if fn(s) != 0}


# gauge algebra generators (complex coefficients allowed; commutant over C)
SU2 = [fock.madd(bil(0, 1), bil(1, 0)),
       fock.madd(fock.msc(-I, bil(0, 1)), fock.msc(I, bil(1, 0))),
       fock.msub(bil(0, 0), bil(1, 1))]
SU3 = []
for a, b in ((2, 3), (3, 4), (2, 4)):
    SU3.append(fock.madd(bil(a, b), bil(b, a)))
    SU3.append(fock.madd(fock.msc(-I, bil(a, b)), fock.msc(I, bil(b, a))))
SU3.append(fock.msub(bil(2, 2), bil(3, 3)))
SU3.append(fock.msub(bil(3, 3), bil(4, 4)))
YOP = diag(lambda s: F(3 * nslot(s) - 2 * npair(s), 6))
GAUGE = SU2 + SU3 + [YOP]
U5 = [bil(i, j) for i in range(M) for j in range(M)]
SO10 = U5 + [fock.mm(ann(i), ann(j)) for i in range(M) for j in range(i + 1, M)] \
    + [fock.mm(cre(i), cre(j)) for i in range(M) for j in range(i + 1, M)]
GAM = [fock.majorana(p, M, kind="real") for p in range(2 * M)]
PARITY = fock.parity(M)


def weights(gens):
    """Weight vector of each basis state under the diagonal generators of the set."""
    diags = [g for g in gens if all(r == c for (r, c) in g)]
    return [tuple(g.get((s, s), F(0)) for g in diags) for s in range(DIM)]


def commutant_dim(gens):
    w = weights(gens)
    unknowns = [(s, t) for s in range(DIM) for t in range(DIM) if w[s] == w[t]]
    idx = {u: n for n, u in enumerate(unknowns)}
    rows = []
    for g in gens:
        # [X, g]_{(r, c)} = sum_t X_{r t} g_{t c} - g_{r t} X_{t c}
        eqs = {}
        for (s, t), n in idx.items():
            # X_{s t} contributes to [X, g]_{(s, c)} with +g_{t c}, and to [X, g]_{(r, t)} with -g_{r s}
            for (a, b), v in g.items():
                if a == t:
                    eqs.setdefault((s, b), {})
                    eqs[(s, b)][n] = eqs[(s, b)].get(n, 0) + v
                if b == s:
                    eqs.setdefault((a, t), {})
                    eqs[(a, t)][n] = eqs[(a, t)].get(n, 0) - v
        rows.extend(r for r in eqs.values() if any(x != 0 for x in r.values()))
    # rank over QI by elimination on sparse rows
    rank = 0
    pivots = {}
    for r in rows:
        r = {k: (v if isinstance(v, QI) else QI(v)) for k, v in r.items() if v != 0}
        while r:
            k = min(r)
            if k in pivots:
                pr = pivots[k]
                f = r[k] / pr[k]
                for kk, vv in pr.items():
                    nv = r.get(kk, QI(0)) - f * vv
                    if nv == 0:
                        r.pop(kk, None)
                    else:
                        r[kk] = nv
            else:
                pivots[k] = r
                rank += 1
                break
    return len(unknowns) - rank


def components(gens):
    """Connected components of the basis under the off-diagonal entries of the generators (the cyclic
    submodules generated from the weight vectors), as sorted tuples of states."""
    adj = {s: set() for s in range(DIM)}
    for g in gens:
        for (r, cc) in g:
            if r != cc:
                adj[r].add(cc)
                adj[cc].add(r)
    seen = set()
    comps = []
    for s in range(DIM):
        if s in seen:
            continue
        stack, comp = [s], set()
        while stack:
            t = stack.pop()
            if t in comp:
                continue
            comp.add(t)
            stack.extend(adj[t] - comp)
        seen |= comp
        comps.append(tuple(sorted(comp)))
    return comps


def weight_multiset(comp, w):
    return tuple(sorted(w[s] for s in comp))


def conjugate_pairs(comps, w):
    """Pairs (C, C') with the weights of C' the negatives of those of C, and the self-conjugate components."""
    neg = {}
    for C in comps:
        neg[C] = tuple(sorted(tuple(-x for x in w[s]) for s in C))
    selfc = [C for C in comps if weight_multiset(C, w) == neg[C]]
    pairs = []
    used = set()
    for C in comps:
        if C in selfc or C in used:
            continue
        partners = [D for D in comps if D not in selfc and weight_multiset(D, w) == neg[C]]
        if len(partners) != 1:
            return None, selfc
        used.add(C)
        used.add(partners[0])
        pairs.append((C, partners[0]))
    return pairs, selfc


def constant_on(sign_of_state, comps):
    return all(len({sign_of_state[s] for s in C if s in sign_of_state}) <= 1 for C in comps)


def check_commutants_of_the_three_symmetries():
    """The commutant of the gauge algebra on Lambda(C^5) is 14-dimensional (ten multiplicity-one components
    and the full 2 x 2 algebra of the twice-occurring neutral singlet), that of u(5) is 6-dimensional (one per degree), that of so(10)
    is 2-dimensional (the two parities), and that of the ten Majoranas is the scalars; the product of the
    Majoranas is minus the parity."""
    premise("standard-model.hyp-s-slot-statistics")
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    GA.check("gauge commutant 14 = 10 + 2^2", commutant_dim(GAUGE) == 14)
    GA.check("u(5) commutant 6", commutant_dim(U5) == 6)
    GA.check("so(10) commutant 2", commutant_dim(SO10) == 2)
    GA.check("Cl(10) commutant 1", commutant_dim(GAM) == 1)
    prod = ONE
    for g in GAM:
        prod = fock.mm(prod, g)
    GA.check("volume element = - parity", fock.meq(prod, fock.msc(-1, PARITY)))
    # the neutral singlets: exactly two states with zero weight under all gauge generators
    w = weights(GAUGE)
    zero = [s for s in range(DIM) if all(x == 0 for x in w[s])]
    GA.check("neutral singlet block = vacuum and top", zero == [0, DIM - 1])
    return True


def check_halvings_fixed_by_each_symmetry():
    """Computed from the operators: the gauge components (cyclic submodules), their conjugate pairing by
    weights, and the u(5) and so(10) components. CPT halvings commuting with the gauge algebra: a sign per
    conjugate pair of charged components (2^5 = 32) times a pair of complementary lines in the two-dimensional
    self-conjugate (neutral) block; commuting with u(5): signs constant on the u(5) components and the
    neutral line one of the two neutral states, 8 in all; with the stored chirality (-1)^(n+k) on the charged
    components: 4; constant on the so(10) components: exactly +-(-1)^N; and +-(-1)^N are exactly the
    involutions for which all ten Majoranas are odd. The two u(5) survivors are conjugate by the gauge-commuting
    swap of the neutral states."""
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    premise("standard-model.hyp-s-slot-statistics")
    import itertools
    w = weights(GAUGE)
    comps = components(GAUGE)
    GA.check("twelve gauge components", len(comps) == 12)
    pairs, selfc = conjugate_pairs(comps, w)
    GA.check("five conjugate pairs of charged components, computed from the weights", pairs is not None and len(pairs) == 5)
    pairs = pairs or []
    GA.check("two self-conjugate components, each one state (the neutral block)",
             len(selfc) == 2 and all(len(C) == 1 for C in selfc) and sorted(C[0] for C in selfc) == [0, DIM - 1])
    charged_states = [s for C in comps if C not in selfc for s in C]
    GA.check("charged components exhaust the other thirty states", len(charged_states) == DIM - 2)
    # CPT sign patterns on the charged components
    patterns = []
    for signs in itertools.product((1, -1), repeat=len(pairs)):
        sg = {}
        for (C, D), x in zip(pairs, signs):
            for s in C:
                sg[s] = x
            for s in D:
                sg[s] = -x
        patterns.append(sg)
    GA.check("32 gauge-commuting CPT sign patterns", len(patterns) == 32)
    u5c = components(U5)
    GA.check("six u(5) components (the degrees)", len(u5c) == 6
             and sorted(len(C) for C in u5c) == [1, 1, 5, 5, 10, 10])
    u5_patterns = [sg for sg in patterns if constant_on(sg, u5c)]
    GA.check("u(5)-commuting charged patterns: 4", len(u5_patterns) == 4)
    neutral_in_different_u5 = all(not (0 in C and DIM - 1 in C) for C in u5c)
    GA.check("the two neutral states lie in different u(5) components, so the neutral line is one of them",
             neutral_in_different_u5)
    GA.check("u(5)-commuting CPT halvings: 8", len(u5_patterns) * 2 == 8)
    # the stored chirality on the charged components: +-(-1)^(n+k) = +-(-1)^deg
    anomaly_free = [sg for sg in u5_patterns if all(sg[s] == sg[charged_states[0]] * (-1) ** (deg(s) - deg(charged_states[0]))
                                                    for s in charged_states)]
    GA.check("anomaly-free u(5)-commuting charged patterns: 2", len(anomaly_free) == 2)
    # the four candidates: anomaly-free charged pattern x neutral choice; so(10) components decide
    so10c = components(SO10)
    GA.check("two so(10) components of sixteen states", sorted(len(C) for C in so10c) == [16, 16])
    survivors = []
    for sg in anomaly_free:
        for vac_sign in (1, -1):
            full = dict(sg)
            full[0] = vac_sign
            full[DIM - 1] = -vac_sign
            if constant_on(full, so10c):
                survivors.append(full)
    GA.check("Spin(10) leaves exactly two halvings", len(survivors) == 2)
    GA.check("they are +-(-1)^N", all(all(full[s] == full[0] * (-1) ** deg(s) for s in range(DIM)) for full in survivors))
    # as operators: involutions commuting with so(10) are al Pe + be Po; CPT excludes al = be
    Pe = diag(lambda s: 1 if deg(s) % 2 == 0 else 0)
    Po = fock.msub(ONE, Pe)
    cands = []
    for al in (1, -1):
        for be in (1, -1):
            G = fock.madd(fock.msc(al, Pe), fock.msc(be, Po))
            tr = sum(G.get((s, s), 0) for s in range(DIM))
            if fock.meq(fock.mm(G, G), ONE) and tr == 0:
                cands.append(G)
    GA.check("Spin(10)-commuting CPT halvings as operators: exactly +-(-1)^N", len(cands) == 2
             and all(fock.meq(G, PARITY) or fock.meq(G, fock.msc(-1, PARITY)) for G in cands))
    for G in cands:
        GA.check("all ten Majoranas odd", all(fock.is_zero(fock.acomm(G, g)) for g in GAM))
    # the vacuum-swapped halving: commutes with u(5), anomaly-free, fails Spin(10) and the grading
    Pvac = diag(lambda s: 1 if s == 0 else 0)
    Ptop = diag(lambda s: 1 if s == DIM - 1 else 0)
    bad = fock.madd(fock.msub(PARITY, fock.msc(2, Pvac)), fock.msc(2, Ptop))
    GA.check("vacuum-swapped halving is an involution of trace zero",
             fock.meq(fock.mm(bad, bad), ONE) and sum(bad.get((s, s), 0) for s in range(DIM)) == 0)
    GA.check("it commutes with u(5)", all(fock.is_zero(fock.comm(bad, g)) for g in U5))
    GA.check("it commutes with the gauge algebra", all(fock.is_zero(fock.comm(bad, g)) for g in GAUGE))
    GA.check("it fails Spin(10) on a creation bracket", not fock.is_zero(fock.comm(bad, fock.mm(cre(0), cre(1)))))
    GA.check("a Majorana is not odd for it", not fock.is_zero(fock.acomm(bad, GAM[0])))
    # unitary equivalence: S swaps the two neutral states and fixes the rest; S commutes with the gauge
    # algebra, S^2 = 1, and bad = S (-1)^N S
    S = fock.madd(fock.msub(fock.msub(ONE, Pvac), Ptop), {(0, DIM - 1): F(1), (DIM - 1, 0): F(1)})
    GA.check("S is an involution commuting with the gauge algebra",
             fock.meq(fock.mm(S, S), ONE) and all(fock.is_zero(fock.comm(S, g)) for g in GAUGE))
    GA.check("vacuum-swapped halving = S (-1)^N S", fock.meq(fock.mm(S, fock.mm(PARITY, S)), bad))
    GA.check("S does not commute with so(10)", not all(fock.is_zero(fock.comm(S, g)) for g in SO10))
    return True


def check_controls():
    """Controls: the same count for the three-mode pair system alone (Lambda(W), Cl(6)): so(6) commutant 2,
    u(3) commutant 4, and the parity is the volume element up to sign; the gauge commutant of Lambda(C^5)
    drops to 10 when the neutral block is removed (no coincidence among charged components)."""
    premise("standard-model.hyp-s-slot-statistics")
    m3 = 3
    d3 = 2 ** m3
    U3 = [fock.mm(fock.cre(i, m3), fock.ann(j, m3)) for i in range(m3) for j in range(m3)]
    SO6 = U3 + [fock.mm(fock.ann(i, m3), fock.ann(j, m3)) for i in range(m3) for j in range(i + 1, m3)] \
        + [fock.mm(fock.cre(i, m3), fock.cre(j, m3)) for i in range(m3) for j in range(i + 1, m3)]
    # reuse commutant_dim with a temporary DIM
    global DIM
    saved = DIM
    DIM = d3
    try:
        GA.check("u(3) commutant 4", commutant_dim(U3) == 4)
        GA.check("so(6) commutant 2", commutant_dim(SO6) == 2)
    finally:
        DIM = saved
    g6 = [fock.majorana(p, m3, kind="real") for p in range(2 * m3)]
    prod = fock.eye(d3)
    for g in g6:
        prod = fock.mm(prod, g)
    GA.check("Cl(6) volume element = - parity", fock.meq(prod, fock.msc(-1, fock.parity(m3))))
    # charged components of Lambda(C^5) are multiplicity-free: restrict the gauge commutant to states other
    # than vacuum and top
    w = weights(GAUGE)
    keep = [s for s in range(1, DIM - 1)]
    unknowns = sum(1 for s in keep for t in keep if w[s] == w[t])
    GA.check("charged weight spaces are one-dimensional", unknowns == len(keep))
    return True
