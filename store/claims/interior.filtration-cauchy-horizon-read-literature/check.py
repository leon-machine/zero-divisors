"""interior.filtration-cauchy-horizon-read-literature: exact check of the algebraic core of finding (3).

Findings (1) and (2) are readings of the imported mass-inflation statements (literature regularity classes,
a C^0 extension, the Cauchy horizon beyond one flat chart) and have no finite computation. Finding (3) rests on
the boost-weight (parabolic) filtration attached to a null direction, which is computed here in GA.py on the
bivectors of Cl(1,3) ((+,-,-,-)), physical frame adapted to the generator l = e0 + e1, n = e0 - e1, boost
generator N = e0 e1:
(a) the boost rotor U = (1 + c) + s e0 e1 (c = cosh, s = sinh rational with c^2 - s^2 = 1) acts by
    x -> U x U~/(U U~) and scales l by q and n by 1/q (q = c - s); the bivectors split into boost weights
    +1, 0, -1 of dimension 2 each (l ^ e2, l ^ e3 | e0 e1, e2 e3 | n ^ e2, n ^ e3), checked as eigenvectors
    of B -> N x B and by the exact scaling under U;
(b) the parabolic algebra of the null direction, {B : B . l in R l}, has dimension 4 (weights 0 and +1),
    its nilradical {B : B . l = 0, B . l^perp in R l} is span{l ^ e2, l ^ e3} (dimension 2, abelian, squares zero), an ideal of
    the parabolic: the top of the filtration;
(c) on the algebraic Weyl maps (10-dimensional exact kernel), the boost acts with weights -2, ..., 2, each of
    real dimension 2; each basis map of extreme weight +2 has image exactly the nilpotent slot
    span{l ^ e2, l ^ e3} (image rank 2, inside the slot) and kills the weight 0 and +1 bivectors, and under the boost their components grow
    by q^2, the largest factor: divergence carried by extreme boost weight sits in the nilpotent slots.
The parabolic/nilradical pattern is that of the premise interior.stabilisers-flat-model, here in the Lorentz
algebra of the physical frame. That the mass-inflation divergence is of extreme weight is the imported
literature statement (interior.imported-mass-inflation-stability) and is not recomputed.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


# ---- algebraic Weyl maps on the bivectors of a four-dimensional signature (exact) ----
BLADES2 = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def wop(X, B, sq):
    """Apply the bivector map with matrix X (X[i][j] = blade_i coefficient of W(blade_j)) to bivector B."""
    out = {}
    for j, bl in enumerate(BLADES2):
        c = B.get(bl, F(0))
        if c:
            out = GA.add(out, {BLADES2[i]: c * X[i][j] for i in range(6) if X[i][j]})
    return out


def wedge_vb(a, B, sq):
    return {k: v for k, v in GA.scal(F(1, 2), GA.add(GA.mul(a, B, sq), GA.mul(B, a, sq))).items() if len(k) == 3}


def dot_vb(a, B, sq):
    return {k: v for k, v in GA.scal(F(1, 2), GA.sub(GA.mul(a, B, sq), GA.mul(B, a, sq))).items() if len(k) == 1}


def weyl_constraints(X, sq):
    """Linear constraints of an algebraic Weyl map: symmetry, Ricci trace-free, first Bianchi."""
    rows = []
    for i in range(6):
        for j in range(i + 1, 6):
            A, B = {BLADES2[i]: F(1)}, {BLADES2[j]: F(1)}
            rows.append(GA.mul(A, wop(X, B, sq), sq).get((), F(0)) - GA.mul(wop(X, A, sq), B, sq).get((), F(0)))
    for nu in range(4):
        tr, bi = {}, {}
        for mu in range(4):
            if mu == nu:
                continue
            Bmn = GA.mul(GA.gen(mu), GA.gen(nu), sq)
            WB = wop(X, Bmn, sq)
            recip = GA.scal(F(1) / sq[mu], GA.gen(mu))
            tr = GA.add(tr, dot_vb(recip, WB, sq))
            bi = GA.add(bi, wedge_vb(recip, WB, sq))
        rows.extend(tr.get((k,), F(0)) for k in range(4))
        rows.extend(bi.get(t, F(0)) for t in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)])
    return rows


def weyl_space(sq):
    """Basis of the algebraic Weyl maps (6 x 6 matrices) of the signature sq, by an exact kernel."""
    cols = []
    for i in range(6):
        for j in range(6):
            X = [[F(1) if (a, b) == (i, j) else F(0) for b in range(6)] for a in range(6)]
            cols.append(weyl_constraints(X, sq))
    mat = [list(r) for r in zip(*cols)]
    return [[[v[6 * i + j] for j in range(6)] for i in range(6)] for v in GA.field_kernel(mat)]


def op_matrix(fn):
    """6 x 6 matrix of a bivector map given as a function on Fraction bivectors."""
    cols = [fn({bl: F(1)}) for bl in BLADES2]
    return [[cols[j].get(BLADES2[i], F(0)) for j in range(6)] for i in range(6)]


S = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]
L = GA.add(E[0], E[1])
NN = GA.sub(E[0], E[1])
NB = GA.mul(E[0], E[1], S)
BOOSTS = [(F(5, 4), F(3, 4)), (F(5, 3), F(-4, 3)), (F(13, 12), F(5, 12))]       # (cosh, sinh)


def wedge(a, b):
    return GA.scal(F(1, 2), GA.sub(GA.mul(a, b, S), GA.mul(b, a, S)))


def comm(a, b):
    return GA.scal(F(1, 2), GA.sub(GA.mul(a, b, S), GA.mul(b, a, S)))


def vdot(B, v):
    return {k: c for k, c in comm(B, v).items() if len(k) == 1}


SLOTS = {1: [wedge(L, E[2]), wedge(L, E[3])], 0: [NB, GA.mul(E[2], E[3], S)], -1: [wedge(NN, E[2]), wedge(NN, E[3])]}


def rank(xs):
    return GA.field_rank([[x.get(bl, F(0)) for bl in BLADES2] for x in xs])


def check_boost_weights_of_bivectors():
    ok = rank(SLOTS[1] + SLOTS[0] + SLOTS[-1]) == 6
    for w, Bs in SLOTS.items():
        ok = ok and len(Bs) == 2 and all(GA.eq(comm(NB, B), GA.scal(-w, B)) or GA.eq(comm(NB, B), GA.scal(w, B)) for B in Bs)
    signs = {w: (1 if GA.eq(comm(NB, SLOTS[w][0]), GA.scal(w, SLOTS[w][0])) else -1) for w in (1, -1)}
    ok = ok and signs[1] == signs[-1]
    for c, s in BOOSTS:
        U = GA.add(GA.sc(1 + c), GA.scal(s, NB))
        nrm = GA.mul(U, GA.reverse(U), S)[()]

        def act(x):
            return GA.scal(1 / nrm, GA.mul(GA.mul(U, x, S), GA.reverse(U), S))
        q = c - s
        ok = ok and GA.eq(act(L), GA.scal(q, L)) and GA.eq(act(NN), GA.scal(1 / q, NN))
        for w, Bs in SLOTS.items():
            ok = ok and all(GA.eq(act(B), GA.scal(q ** w, B)) for B in Bs)
    _tp_rv = (ok); assert _tp_rv is not False, "check_boost_weights_of_bivectors"; return _tp_rv


def check_parabolic_and_its_nilradical():
    premise("interior.stabilisers-flat-model")
    rows_stab, rows_nil = [], []
    for bl in BLADES2:
        v = vdot({bl: F(1)}, L)
        comps = [v.get((i,), F(0)) for i in range(4)]
        rows_stab.append([comps[0] - comps[1], comps[2], comps[3]])        # B . l in R l: (x0 = x1, x2 = x3 = 0)
        row = list(comps)                                                   # B . l = 0
        for x in (E[2], E[3]):                                              # B . l^perp in R l
            w = vdot({bl: F(1)}, x)
            row += [w.get((0,), F(0)) - w.get((1,), F(0)), w.get((2,), F(0)), w.get((3,), F(0))]
        rows_nil.append(row)
    stab = GA.field_kernel([list(r) for r in zip(*rows_stab)])
    nil = GA.field_kernel([list(r) for r in zip(*rows_nil)])
    ok = len(stab) == 4 and len(nil) == 2
    nilv = [{bl: c for bl, c in zip(BLADES2, v) if c} for v in nil]
    stabv = [{bl: c for bl, c in zip(BLADES2, v) if c} for v in stab]
    ok = ok and rank(nilv + SLOTS[1]) == 2 and rank(stabv + SLOTS[0] + SLOTS[1]) == 4
    ok = ok and all(GA.mul(x, x, S) == {} for x in SLOTS[1]) and comm(SLOTS[1][0], SLOTS[1][1]) == {}
    ok = ok and all(rank(nilv + [comm(p, x)]) == 2 for p in stabv for x in nilv)
    _tp_rv = (ok); assert _tp_rv is not False, "check_parabolic_and_its_nilradical"; return _tp_rv


def check_extreme_weight_curvature_occupies_nilpotent_slots():
    Ws = weyl_space(S)
    ok = len(Ws) == 10
    adN = op_matrix(lambda B: comm(NB, B))
    sgn = 1 if GA.eq(comm(NB, SLOTS[1][0]), SLOTS[1][0]) else -1
    dims = {}
    for w in (-2, -1, 0, 1, 2):
        rows = []
        for X in Ws:
            Y = [[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(GA.mat_mul(adN, X), GA.mat_mul(X, adN))]
            rows.append([Y[i][j] - sgn * w * X[i][j] for i in range(6) for j in range(6)])
        ker = GA.field_kernel([list(r) for r in zip(*rows)])
        dims[w] = ker
    ok = ok and {w: len(k) for w, k in dims.items()} == {-2: 2, -1: 2, 0: 2, 1: 2, 2: 2}
    union = []
    for v in dims[2]:
        X = [[sum(c * W[i][j] for c, W in zip(v, Ws)) for j in range(6)] for i in range(6)]
        images = [wop(X, {bl: F(1)}, S) for bl in BLADES2]
        ok = ok and rank([im for im in images if im] + SLOTS[1]) == 2 and rank([im for im in images if im]) == 2
        union += [im for im in images if im]
        ok = ok and all(wop(X, B, S) == {} for B in SLOTS[0] + SLOTS[1])
        for c, s in BOOSTS:
            q = c - s
            U = GA.add(GA.sc(1 + c), GA.scal(s, NB))
            nrm = GA.mul(U, GA.reverse(U), S)[()]

            def act(x, U=U, nrm=nrm):
                return GA.scal(1 / nrm, GA.mul(GA.mul(U, x, S), GA.reverse(U), S))

            def act_inv(x, U=U, nrm=nrm):
                return GA.scal(1 / nrm, GA.mul(GA.mul(GA.reverse(U), x, S), U, S))
            for B in SLOTS[-1]:
                ok = ok and GA.eq(act(wop(X, act_inv(B), S)), GA.scal(q * q, wop(X, B, S)))
    ok = ok and rank(union) == 2 and rank(union + SLOTS[1]) == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_extreme_weight_curvature_occupies_nilpotent_slots"; return _tp_rv
