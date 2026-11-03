"""standard-model.ten-transported-ambient-space-doublets-are: exact checks.

The module Lambda(C^5) in the occupation basis e_S (pairs 1, 2, 3; rungs 4, 5); v_a creates mode a,
w_a contracts it. S(U(2) x U(3)) acts through its Lie algebra: hypercharge y acts on e_S by
3j - 2k (j occupied rungs, k occupied pairs, Y = y/6), 2T_3 = N_4 - N_5, su(2) = span(v_4 w_5,
v_5 w_4, N_4 - N_5), su(3) = span(v_a w_b (a != b <= 3), N_1 - N_2, N_2 - N_3). Commutators are
computed as operators on all 32 basis states.
(1) [y, v_a] = 3 v_a on rungs and -2 v_a on pairs, opposite on w_a: Y = +-1/2 on rung vectors,
-+1/3 on pair vectors; [2T_3, v_4] = v_4, [2T_3, v_5] = -v_5, 2T_3 kills pair vectors; v_1 w_2 sends
v_2 to v_1 and w_1 to -w_2 and kills rung vectors.
(2) The ten splits into the four invariant blocks span(v_4, v_5), span(w_4, w_5), span(v_1..v_3),
span(w_1..w_3): [v_a w_b, v_c] = delta_bc v_a and [v_a w_b, w_c] = -delta_ac w_b for all a, b, c, so
su(2) acts only on rung blocks, su(3) only on pair blocks, each irreducibly (raising maps reach every
basis vector); the su(3) Cartan weights are those of 3 on the v's and of 3bar on the w's.
(3) The one-mode states: (1,0) twice with Y = 1/2, (0,1) three times with Y = -1/3.
(4) In GA, Cl(5,5) with v_a = (e+_a + e-_a)/2, w_a = (e+_a - e-_a)/2 satisfies the null-pair relations,
the Fock operators satisfy the same relations, the rung pairs span hyperbolic planes and the pair
vectors span W + Wbar with W, Wbar maximal isotropic: the ten is the complexified ambient space.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

N = 5
STATES = [frozenset(c) for r in range(N + 1) for c in combinations(range(1, N + 1), r)]
RUNGS, PAIRS, MODES = (4, 5), (1, 2, 3), (1, 2, 3, 4, 5)


def act(op, st):
    out = {}
    for (kind, i), c in op.items():
        for S, a in st.items():
            if kind == "v" and i not in S:
                T = S | {i}
            elif kind == "w" and i in S:
                T = S - {i}
            else:
                continue
            sign = -1 if sum(1 for j in S if j < i) % 2 else 1
            out[T] = out.get(T, 0) + sign * c * a
    return {k: v for k, v in out.items() if v != 0}


def lin(*terms):
    out = {}
    for c, st in terms:
        for k, v in st.items():
            out[k] = out.get(k, 0) + c * v
    return {k: v for k, v in out.items() if v != 0}


def V(a):
    return lambda st: act({("v", a): F(1)}, st)


def W(a):
    return lambda st: act({("w", a): F(1)}, st)


def prod(A, B):
    return lambda st: A(B(st))


def comm(A, B):
    return lambda st: lin((1, A(B(st))), (-1, B(A(st))))


def acomm(A, B):
    return lambda st: lin((1, A(B(st))), (1, B(A(st))))


def scaled(c, A):
    return lambda st: lin((c, A(st)))


def diag_op(f):
    return lambda st: {S: f(S) * a for S, a in st.items() if f(S) != 0}


def same(A, B):
    return all(A({S: F(1)}) == B({S: F(1)}) for S in STATES)


def zero_op(st):
    return {}


def ident(st):
    return dict(st)


Y6 = diag_op(lambda S: 3 * len(S & set(RUNGS)) - 2 * len(S & set(PAIRS)))
T3x2 = diag_op(lambda S: (4 in S) - (5 in S))


def num(a):
    return diag_op(lambda S: 1 if a in S else 0)


def check_weights_by_commutators():
    ok = True
    for a in RUNGS:
        ok = ok and same(comm(Y6, V(a)), scaled(3, V(a))) and same(comm(Y6, W(a)), scaled(-3, W(a)))
    for a in PAIRS:
        ok = ok and same(comm(Y6, V(a)), scaled(-2, V(a))) and same(comm(Y6, W(a)), scaled(2, W(a)))
        ok = ok and same(comm(T3x2, V(a)), zero_op) and same(comm(T3x2, W(a)), zero_op)
    ok = ok and same(comm(T3x2, V(4)), V(4)) and same(comm(T3x2, V(5)), scaled(-1, V(5)))
    ok = ok and same(comm(T3x2, W(4)), scaled(-1, W(4))) and same(comm(T3x2, W(5)), W(5))
    g = prod(V(1), W(2))
    ok = ok and same(comm(g, V(2)), V(1)) and same(comm(g, W(1)), scaled(-1, W(2)))
    ok = ok and all(same(comm(g, X(a)), zero_op) for X in (V, W) for a in RUNGS)
    GA.check("ten: Y = +-1/2 on rung vectors, -+1/3 on pair vectors; 2T_3 and the su(3) generator v_1 w_2", ok)
    return ok


def check_four_multiplets():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    ok = True
    n = 0
    for a in MODES:
        for b in MODES:
            g = prod(V(a), W(b))
            for c in MODES:
                ok = ok and same(comm(g, V(c)), V(a) if b == c else zero_op)
                ok = ok and same(comm(g, W(c)), scaled(-1, W(b)) if a == c else zero_op)
                n += 2
    ok = ok and n == 250
    # irreducibility: raising and lowering connect every basis vector of each block
    ok = ok and same(comm(prod(V(4), W(5)), V(5)), V(4)) and same(comm(prod(V(5), W(4)), V(4)), V(5))
    ok = ok and same(comm(prod(V(4), W(5)), W(4)), scaled(-1, W(5)))
    ok = ok and all(same(comm(prod(V(a), W(b)), V(b)), V(a)) for a in PAIRS for b in PAIRS if a != b)
    # su(3) Cartan weights (H_1, H_2) = (N_1 - N_2, N_2 - N_3): 3 on v, 3bar on w
    H1 = lambda st: lin((1, num(1)(st)), (-1, num(2)(st)))
    H2 = lambda st: lin((1, num(2)(st)), (-1, num(3)(st)))
    wts = {1: (1, 0), 2: (-1, 1), 3: (0, -1)}
    for a, (p, q) in wts.items():
        ok = ok and same(comm(H1, V(a)), scaled(p, V(a))) and same(comm(H2, V(a)), scaled(q, V(a)))
        ok = ok and same(comm(H1, W(a)), scaled(-p, W(a))) and same(comm(H2, W(a)), scaled(-q, W(a)))
    GA.check("ten: (2,1)_{1/2} + (2,1)_{-1/2} + (1,3)_{-1/3} + (1,3bar)_{1/3}", ok)
    return ok


def check_one_mode_states_form_the_five():
    one = [S for S in STATES if len(S) == 1]
    data = sorted((len(S & set(RUNGS)), len(S & set(PAIRS)), F(3 * len(S & set(RUNGS)) - 2 * len(S & set(PAIRS)), 6))
                  for S in one)
    ok = data == [(0, 1, F(-1, 3))] * 3 + [(1, 0, F(1, 2))] * 2
    GA.check("ten: the one-mode states are (1,0) twice with Y = 1/2 and (0,1) three times with Y = -1/3", ok)
    return ok


def check_ten_is_the_complexified_ambient_space():
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    premise("standard-model.imported-fock-model-twistor-space")
    sq = [F(1)] * 5 + [F(-1)] * 5
    half = F(1, 2)
    gv = {a: GA.scal(half, GA.add(GA.gen(a - 1), GA.gen(a + 4))) for a in MODES}
    gw = {a: GA.scal(half, GA.sub(GA.gen(a - 1), GA.gen(a + 4))) for a in MODES}
    ok = True
    for a in MODES:
        for b in MODES:
            d = F(1) if a == b else F(0)
            ok = ok and GA.eq(GA.add(GA.mul(gv[a], gv[b], sq), GA.mul(gv[b], gv[a], sq)), {})
            ok = ok and GA.eq(GA.add(GA.mul(gw[a], gw[b], sq), GA.mul(gw[b], gw[a], sq)), {})
            ok = ok and GA.eq(GA.add(GA.mul(gv[a], gw[b], sq), GA.mul(gw[b], gv[a], sq)), GA.sc(d))
            # the same relations hold for the Fock operators
            ok = ok and same(acomm(V(a), V(b)), zero_op) and same(acomm(W(a), W(b)), zero_op)
            ok = ok and same(acomm(V(a), W(b)), ident if a == b else zero_op)
    ten = [gv[a] for a in MODES] + [gw[a] for a in MODES]
    G = [[GA.dot(x, y, sq) for y in ten] for x in ten]
    ok = ok and GA.mat_rank(G) == 10
    # rung pairs: hyperbolic planes; pair vectors: W and Wbar totally isotropic of dimension 3
    for a in RUNGS:
        ok = ok and [[GA.dot(x, y, sq) for y in (gv[a], gw[a])] for x in (gv[a], gw[a])] == [[0, half], [half, 0]]
    ok = ok and all(GA.dot(gv[a], gv[b], sq) == 0 and GA.dot(gw[a], gw[b], sq) == 0 for a in PAIRS for b in PAIRS)
    GA.check("ten: the mode vectors span the complexified ambient space, rung planes hyperbolic", ok)
    return ok
