"""correspondence.imported-stabilisers-flat-model: exact checks in Cl(2,4) (GA blade engine).

V = R^(2,4): e0 (square +1), e1, e2, e3 (square -1) span W_(1,3); e+ = 4 (square +1), e- = 5 (square -1);
nInf = e- + e+, nO = (e- - e+)/2. A bivector B acts on vectors by v -> [B, v]/2.
(1) The stabiliser {B in Lambda^2 V : [B, nInf] = 0} is computed as an exact kernel: dimension 10; the six
    bivectors of W and the four nInf e_i (i in W) lie in it and span it. Lambda^2 W is closed under the
    commutator (so(1,3)); [Lambda^2 W, nInf W] lies in nInf W and [nInf W, nInf W] = 0 (the semidirect
    product with the abelian R^4): the Poincare algebra.
(2) The stabiliser of the ray, {B : [B, nInf] in R nInf}, has dimension 11 and contains nInf ^ nO, which acts
    on the nilradical nInf W with one nonzero weight (the grading element) and is not in the stabiliser of
    nInf.
(3) The nilradical acts as translations: T_a = 1 + nInf a / 2 is a rotor with T_a X(x) reverse(T_a) = X(x + a)
    for X(x) = nO + x + Q(x) nInf / 2, at sample x, a; and ad(nInf a) on vectors is two-step nilpotent:
    its cube vanishes on every basis vector, its square does not (it sends nO to 4 Q(a) nInf: ad nO = 2a, ad a = 2 Q(a) nInf).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
BIV = [b for b in GA.all_blades(6) if len(b) == 2]
NI = GA.add(GA.gen(5), GA.gen(4))
NO = GA.scal(F(1, 2), GA.sub(GA.gen(5), GA.gen(4)))
LW = [{(i, j): F(1)} for i in range(4) for j in range(i + 1, 4)]
NW = [GA.mul(NI, GA.gen(i), SQ) for i in range(4)]
PTS = [{(0,): F(1), (2,): F(-2)}, {(1,): F(3, 2), (3,): F(1, 3), (0,): F(2)}, {}]
SHIFTS = [{(0,): F(1, 2), (1,): F(-1)}, {(2,): F(4), (3,): F(-3, 5)}]


def com(x, y):
    return GA.sub(GA.mul(x, y, SQ), GA.mul(y, x, SQ))


def rank(elems):
    rows = [GA.basis_vector_of(x, GA.all_blades(6)) for x in elems if x]
    return GA.rank_of_vectors(rows) if rows else 0


def kernel_dim(cond_rows_of):
    """Dimension of {B = sum c_k BIV_k : linear conditions} from a function giving each BIV_k's image vector."""
    cols = [cond_rows_of({b: F(1)}) for b in BIV]
    M = [[cols[k][r] for k in range(len(BIV))] for r in range(len(cols[0]))]
    return len(BIV) - GA.field_rank(M)


def vec_coords(x):
    return [x.get((i,), F(0)) for i in range(6)]


def check_stabiliser_is_poincare():
    premise("interior.stabilisers-flat-model")
    ok = True
    ok = ok and len(BIV) == 15
    ok = ok and kernel_dim(lambda B: vec_coords(com(B, NI))) == 10
    gens = LW + NW
    ok = ok and all(com(B, NI) == {} for B in gens) and rank(gens) == 10
    ok = ok and rank(LW + [com(x, y) for x in LW for y in LW]) == 6
    ok = ok and rank(NW + [com(x, y) for x in LW for y in NW]) == 4
    ok = ok and all(com(x, y) == {} for x in NW for y in NW)
    GA.check("stabiliser of nInf: dimension 10 = Lambda^2 W + nInf W, so(1,3) |x R^4", ok)
    return ok


def check_ray_stabiliser_is_parabolic():
    premise("interior.stabilisers-flat-model")
    ok = True

    def cond(B):
        c = vec_coords(com(B, NI))
        # [B, nInf] in R nInf: components orthogonal to nInf's direction vanish and the e+, e- parts agree
        return c[:4] + [c[4] - c[5]]
    ok = ok and kernel_dim(cond) == 11
    G = GA.scal(F(1, 2), com(NI, NO))
    ok = ok and com(G, NI) != {} and cond(G) == [0] * 5
    ws = []
    for x in NW:
        y = com(G, x)
        lam = [y.get(b, F(0)) / x[b] for b in x][0]
        ok = ok and y == GA.scal(lam, x)
        ws.append(lam)
    ok = ok and len(set(ws)) == 1 and ws[0] != 0
    ok = ok and rank(LW + NW + [G]) == 11
    GA.check("ray stabiliser: dimension 11, adds the grading element nInf ^ nO", ok)
    return ok


def X(x):
    Q = GA.mul(x, x, SQ).get((), F(0))
    return GA.add(NO, x, GA.scal(Q * F(1, 2), NI))


def check_nilradical_translations_and_two_step():
    premise("interior.stabilisers-flat-model")
    premise("transport.no-go-level-elements")
    ok = True
    for a in SHIFTS:
        T = GA.add(GA.sc(1), GA.scal(F(1, 2), GA.mul(NI, a, SQ)))
        ok = ok and GA.mul(T, GA.reverse(T), SQ) == GA.sc(1)
        for x in PTS:
            ok = ok and GA.mul(GA.mul(T, X(x), SQ), GA.reverse(T), SQ) == X(GA.add(x, a))
        N = GA.mul(NI, a, SQ)
        ad = lambda v: com(N, v)
        ok = ok and all(ad(ad(ad(GA.gen(i)))) == {} for i in range(6))
        sq2 = ad(ad(NO))
        Qa = GA.mul(a, a, SQ).get((), F(0))
        ok = ok and sq2 != {} and sq2 == GA.scal(4 * Qa, NI)
    GA.check("nilradical: T_a X(x) T_a~ = X(x + a); ad(nInf a) two-step nilpotent on vectors", ok)
    return ok
