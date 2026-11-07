"""A Fock slot module over b doublets is CPT-closed only for b = 1, as the exterior algebra: exact checks.

Notation of synthesis.cpt-closure-forces-slot-module-and-chirality, numbers read in span{1, I4}: D is the slot
doublet (weights e1, e2 of the slot U(2) torus), the one-slot space is F_1 = D (x) M with M of dimension b
(trivial U(2) action, weights f_1..f_b of a torus of GL(M) used only to separate copies), F_(l1,l2) the U(2)
irreducible of highest weight (l1, l2) (weak spin (l1 - l2)/2). CPT closure (clause (1) of that theorem):
F_0 = a F_(0,0), F_1 = b F_(1,0), F_2 = a F_(1,1), F_n = 0 for n >= 3.

(1) Characters: Lambda^2(V (x) W) = Sym^2 V (x) Lambda^2 W + Lambda^2 V (x) Sym^2 W as GL(V) x GL(W) torus
    characters for dim V, dim W in 1..3; for V = D, dim M = b in 1..4, the exterior Fock module has
    F_2 = b(b-1)/2 F_(2,0) + b(b+1)/2 F_(1,1), F_3 != 0 for b >= 2, and satisfies CPT closure exactly for b = 1
    (b = 0 fails too: F_2 = 0 while F_0 = F_(0,0)).
(2) Symmetric Fock module: Sym^n(D (x) M) has dimension C(2b + n - 1, n) > 0 for every n (checked n <= 6,
    b = 1..4), and Sym^2 contains b(b+1)/2 F_(2,0): never CPT-closed, never finite-dimensional.
(3) Geometric algebra: the 2b modes as null pairs v, w of Cl(2b, 2b) (v w + w v = 1 as vectors), vacuum the null
    blade of the w's; on the two-slot states v_i v_j f the weak Casimir T- T+ + T3^2 + T3 (T+ = sum_c v_{up,c}
    w_{dn,c}) has eigenvalue 2 (weak spin one) with multiplicity 3 b(b-1)/2 and 0 with multiplicity b(b+1)/2,
    for b = 1, 2.
Exact arithmetic only.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
import GA
from tp_premise import premise


def _ext_weights(dv, dw, n):
    """Multiset of torus weights (tuple over V-weights, tuple over W-weights) of Lambda^n(V (x) W)."""
    modes = [(i, c) for i in range(dv) for c in range(dw)]
    out = {}
    for S in combinations(modes, n):
        wv = tuple(sum(1 for (i, c) in S if i == k) for k in range(dv))
        ww = tuple(sum(1 for (i, c) in S if c == k) for k in range(dw))
        out[(wv, ww)] = out.get((wv, ww), 0) + 1
    return out


def _sym_weights(d, n):
    out = {}
    for S in combinations_with_replacement(range(d), n):
        w = tuple(sum(1 for x in S if x == k) for k in range(d))
        out[w] = out.get(w, 0) + 1
    return out


def _alt_weights(d, n):
    out = {}
    for S in combinations(range(d), n):
        w = tuple(sum(1 for x in S if x == k) for k in range(d))
        out[w] = out.get(w, 0) + 1
    return out


def _tensor(A, B):
    out = {}
    for a, ma in A.items():
        for b, mb in B.items():
            out[(a, b)] = out.get((a, b), 0) + ma * mb
    return out


def _add(A, B):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, 0) + v
    return out


def _u2_decompose(wts):
    """Decompose a U(2) character {(w1, w2): mult} into irreducibles {(l1, l2): mult}."""
    wts = {k: v for k, v in wts.items() if v}
    irr = {}
    while wts:
        top = max(wts, key=lambda w: (w[0] - w[1], w[0]))
        m = wts[top]
        irr[top] = irr.get(top, 0) + m
        l1, l2 = top
        for t in range(l1 - l2 + 1):
            key = (l1 - t, l2 + t)
            wts[key] = wts.get(key, 0) - m
            if wts[key] == 0:
                del wts[key]
    return irr


def _u2_of_fermi(b, n):
    wts = {}
    for (wv, ww), m in _ext_weights(2, b, n).items():
        wts[wv] = wts.get(wv, 0) + m
    return _u2_decompose(wts)


def _cpt_closed(graded):
    """Clause (1): F_0 = a(0,0), F_1 = b(1,0), F_2 = a(1,1), nothing above."""
    a = graded[0].get((0, 0), 0)
    ok = set(graded[0]) <= {(0, 0)} and set(graded[1]) <= {(1, 0)}
    ok = ok and set(graded[2]) <= {(1, 1)} and graded[2].get((1, 1), 0) == a
    return ok and all(not graded[n] for n in graded if n >= 3)


def check_exterior_fock_module_is_cpt_closed_only_for_one_doublet():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    ok_id = True
    for dv in (1, 2, 3):
        for dw in (1, 2, 3):
            lhs = _ext_weights(dv, dw, 2)
            rhs = _add(_tensor(_sym_weights(dv, 2), _alt_weights(dw, 2)),
                       _tensor(_alt_weights(dv, 2), _sym_weights(dw, 2)))
            ok_id = ok_id and lhs == rhs
    GA.check("(1) Lambda^2(V x W) = S^2V x L^2W + L^2V x S^2W (dims 1..3)", ok_id)
    closed = []
    ok_mult = ok_f3 = True
    for b in (1, 2, 3, 4):
        graded = {n: _u2_of_fermi(b, n) for n in range(2 * b + 1)}
        ok_mult = ok_mult and graded[2].get((2, 0), 0) == b * (b - 1) // 2
        ok_mult = ok_mult and graded[2].get((1, 1), 0) == b * (b + 1) // 2
        ok_f3 = ok_f3 and (bool(graded[3]) if b >= 2 else not graded.get(3))
        if _cpt_closed(graded):
            closed.append(b)
    GA.check("(1) F_2 = b(b-1)/2 F_(2,0) + b(b+1)/2 F_(1,1) for b = 1..4", ok_mult)
    GA.check("(1) F_3 != 0 exactly for b >= 2", ok_f3)
    GA.check("(1) CPT closure holds for b = 1 only", closed == [1])
    GA.check("(1) b = 0: F_0 = F_(0,0), F_2 = 0, not closed",
             not _cpt_closed({0: {(0, 0): 1}, 1: {}, 2: {}}))
    GA.check("(1) b = 1 module is Lambda^0 + Lambda^1 + Lambda^2 of the doublet",
             [_u2_of_fermi(1, n) for n in range(3)] == [{(0, 0): 1}, {(1, 0): 1}, {(1, 1): 1}])


def check_symmetric_fock_module_is_never_cpt_closed():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    ok_dim = ok_spin = True
    for b in (1, 2, 3, 4):
        for n in range(1, 7):
            d = sum(_sym_weights(2 * b, n).values())
            num, den = 1, 1
            for t in range(n):
                num *= 2 * b + t
                den *= t + 1
            ok_dim = ok_dim and d == num // den and d > 0
        wts = {}
        for w, m in _sym_weights(2 * b, 2).items():
            key = (sum(w[0::2]), sum(w[1::2]))
            wts[key] = wts.get(key, 0) + m
        ok_spin = ok_spin and _u2_decompose(wts).get((2, 0), 0) == b * (b + 1) // 2
    GA.check("(2) dim Sym^n(D x M) = C(2b + n - 1, n) > 0 for n = 1..6", ok_dim)
    GA.check("(2) Sym^2(D x M) contains b(b+1)/2 copies of weak spin one", ok_spin)


def _null_pairs(nm):
    sq = tuple([1] * nm + [-1] * nm)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(k), GA.gen(nm + k))) for k in range(nm)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(k), GA.gen(nm + k))) for k in range(nm)]
    return sq, v, w


def check_weak_triplet_in_the_two_slot_space_by_null_pairs():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    counts = {}
    for b in (1, 2):
        nm = 2 * b
        sq, v, w = _null_pairs(nm)
        ok_car = all(GA.eq(GA.add(GA.mul(v[i], w[j], sq), GA.mul(w[j], v[i], sq)),
                           GA.sc(1 if i == j else 0)) for i in range(nm) for j in range(nm))
        f = GA.sc(1)
        for k in range(nm):
            f = GA.mul(f, w[k], sq)
        up = list(range(0, nm, 2))
        dn = list(range(1, nm, 2))

        def op(terms, x):
            out = {}
            for c, a, bb in terms:
                out = GA.add(out, GA.scal(c, GA.mul(a, GA.mul(bb, x, sq), sq)))
            return out

        tp = [(F(1), v[u], w[d]) for u, d in zip(up, dn)]
        tm = [(F(1), v[d], w[u]) for u, d in zip(up, dn)]
        t3 = [(F(1, 2), v[u], w[u]) for u in up] + [(F(-1, 2), v[d], w[d]) for d in dn]
        states = [GA.mul(GA.mul(v[i], v[j], sq), f, sq) for i, j in combinations(range(nm), 2)]
        blades = sorted({bl for s in states for bl in s})

        def coords(x):
            return [x.get(bl, F(0)) for bl in blades]

        cas = [coords(GA.add(op(tm, op(tp, s)), op(t3, op(t3, s)), op(t3, s))) for s in states]
        basis = [coords(s) for s in states]
        n = len(states)
        GA.check("(3) CAR as vectors and nonzero two-slot states, b = %d" % b,
                 ok_car and GA.rank_of_vectors(basis) == n)
        # Casimir matrix in the state basis: solve cas[s] = sum_t C[t][s] basis[t]
        for lam in (2, 0):
            shifted = [[cas[s][i] - lam * basis[s][i] for i in range(len(blades))] for s in range(n)]
            counts[(b, lam)] = n - GA.rank_of_vectors(shifted)
    GA.check("(3) b = 1: the two-slot space is one weak singlet", counts[(1, 0)] == 1 and counts[(1, 2)] == 0)
    GA.check("(3) b = 2: weak spin one with multiplicity 3, singlets 3", counts[(2, 2)] == 3 and counts[(2, 0)] == 3)
