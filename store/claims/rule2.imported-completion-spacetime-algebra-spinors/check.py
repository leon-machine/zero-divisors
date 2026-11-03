"""rule2.imported-completion-spacetime-algebra-spinors: exact checks.

(1) The forced completion Cl(1,3) -> Cl(2,4): the conformal model exported by the
    transport.minimality check has signature (2,4) and the lifts are null; the transvection obstruction
    (a null rotation fixing v = e0 + e1 moves the pseudo-inverse w0 = (e0 - e1)/4) holds in Cl(2,4).
(2) The complexified Cl(2,4) on the Fock space of three ladder pairs: with Jordan-Wigner
    a_j, a_j^dagger on C^8 (exact Gaussian rationals), the six matrices a_0 + a_0^+, a_1 + a_1^+,
    i(a_2 + a_2^+), a_j - a_j^+ (j = 0, 1, 2) satisfy the relations of signature (2,4); the 64
    products are linearly independent over C, so the image is all of Mat_8(C) and the module is
    irreducible.
(3) Chirality halves: I_6 (product of the six) squares to -1 and equals c (-1)^N with c = +-i, so
    its eigenspaces are the even and odd Fock halves Lambda^even W, Lambda^odd W (dimension 4 each);
    the 32 even products preserve them and restrict to all of Mat_4(C) on each half (rank 16):
    each half is an irreducible Cl^0(2,4)_C-module.
(4) The real minimal left ideal: P = (1 + e0 e2)(1 + e1 e3)/4 in Cl^0(2,4) (e0, e1 positive) is an
    idempotent with Cl^0(2,4) P of real dimension 8 and P Cl^0 P = span(P, I6 P), I6 P squaring to -P:
    the left ideal is C^4 with complex unit I_6, which commutes with every even element.
The identification of the odd half with the conjugate dual of CS is not tested.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI


def _fock():
    states = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    idx = {s: i for i, s in enumerate(states)}
    ann = []
    for j in range(3):
        M = [[QI(0) for _ in range(8)] for _ in range(8)]
        for s in states:
            if s[j] == 1:
                t = list(s)
                t[j] = 0
                sign = -1 if sum(s[:j]) % 2 else 1
                M[idx[tuple(t)]][idx[s]] = QI(sign)
        ann.append(M)
    return states, ann


def _T(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M))]


def _add(A, B, s=1):
    return [[A[i][j] + B[i][j] * s for j in range(len(A))] for i in range(len(A))]


def _scal(c, A):
    return [[c * x for x in r] for r in A]


def _mul(A, B):
    return GA.field_mat_mul(A, B)


def _eye(c=1):
    return [[QI(c) if i == j else QI(0) for j in range(8)] for i in range(8)]


def _gammas():
    states, ann = _fock()
    cre = [_T(a) for a in ann]
    gp = [_add(ann[j], cre[j]) for j in range(3)]
    gm = [_add(ann[j], cre[j], -1) for j in range(3)]
    return states, [gp[0], gp[1], _scal(GA.QI_I, gp[2]), gm[0], gm[1], gm[2]]


def check_forced_completion_of_spacetime_algebra():
    ex = premise("transport.minimality")
    premise("transport.no-go-level-elements")
    M = ex["conformal"](1, 3)
    sq = M["sq"]
    ok = True
    G = [[GA.dot(GA.gen(i), GA.gen(j), sq) for j in range(6)] for i in range(6)]
    ok = ok and GA.congruence_signature(G) == (2, 4, 0)
    for cs in ([1, 2, -1, 3], [5, 3, 4, 0], [0, 1, 0, 0]):
        Xx = M["X"](M["vec"](cs))
        ok = ok and GA.is_zero(GA.mul(Xx, Xx, sq))
    v = GA.add(GA.gen(0), GA.gen(1))
    w0 = GA.scal(F(1, 4), GA.sub(GA.gen(0), GA.gen(1)))
    u = GA.gen(2)
    R = GA.add(GA.sc(1), GA.mul(v, u, sq))
    Rinv = GA.sub(GA.sc(1), GA.mul(v, u, sq))
    ok = ok and GA.eq(GA.mul(GA.mul(v, w0, sq), v, sq), v)
    ok = ok and GA.eq(GA.mul(GA.mul(R, v, sq), Rinv, sq), v)
    moved = GA.mul(GA.mul(R, w0, sq), Rinv, sq)
    ok = ok and GA.eq(moved, GA.sub(GA.sub(w0, u), GA.scal(-1, v)))    # w0 - u - Q(u) v, Q(u) = -1
    GA.check("Cl(1,3) -> Cl(2,4): signature (2,4), null lifts, transvection obstruction", ok)
    return ok


def check_fock_module_irreducible():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    states, g = _gammas()
    sqs = [1, 1, -1, -1, -1, -1]
    ok = True
    for i in range(6):
        ok = ok and _mul(g[i], g[i]) == _eye(sqs[i])
        for j in range(i + 1, 6):
            ok = ok and _add(_mul(g[i], g[j]), _mul(g[j], g[i])) == _eye(0)
    prods = []
    for b in GA.all_blades(6):
        P = _eye()
        for i in b:
            P = _mul(P, g[i])
        prods.append([x for r in P for x in r])
    ok = ok and len(prods) == 64 and GA.field_rank(prods) == 64
    GA.check("Cl(2,4)_C acts on the 8-dimensional Fock space of three pairs with image Mat_8(C)", ok)
    return ok


def check_chirality_halves():
    premise("correspondence.fock-model-complexified-ascended-algebra")
    premise("correspondence.spinor-identification")
    states, g = _gammas()
    ok = True
    I6 = _eye()
    for x in g:
        I6 = _mul(I6, x)
    ok = ok and _mul(I6, I6) == _eye(-1)
    parity = [[QI(-1 if sum(s) % 2 else 1) if i == j else QI(0) for j in range(8)] for i, s in enumerate(states)]
    c = I6[0][0]
    ok = ok and c in (GA.QI_I, -GA.QI_I) and I6 == _scal(c, parity)
    even = [i for i, s in enumerate(states) if sum(s) % 2 == 0]
    odd = [i for i, s in enumerate(states) if sum(s) % 2 == 1]
    ok = ok and len(even) == 4 and len(odd) == 4
    for half, other in ((even, odd), (odd, even)):
        rows = []
        for b in GA.all_blades(6):
            if len(b) % 2:
                continue
            P = _eye()
            for i in b:
                P = _mul(P, g[i])
            ok = ok and all(P[i][j] == 0 for i in other for j in half)          # preserves the half
            rows.append([P[i][j] for i in half for j in half])
        ok = ok and len(rows) == 32 and GA.field_rank(rows) == 16
    GA.check("I_6 = +-i (-1)^N: the chirality halves are Lambda^even W and Lambda^odd W, each irreducible", ok)
    return ok


def check_real_minimal_left_ideal_with_unit_i6():
    premise("correspondence.spinor-identification")
    sq = GA.sig(2, 4)
    ok = True
    I6 = {tuple(range(6)): F(1)}
    ok = ok and GA.eq(GA.mul(I6, I6, sq), GA.sc(-1))
    evens = [b for b in GA.all_blades(6) if len(b) % 2 == 0]
    ok = ok and all(GA.commutes(I6, {b: F(1)}, sq) for b in evens)
    b1 = GA.mul(GA.gen(0), GA.gen(2), sq)
    b2 = GA.mul(GA.gen(1), GA.gen(3), sq)
    P = GA.mul(GA.scal(F(1, 2), GA.add(GA.sc(1), b1)), GA.scal(F(1, 2), GA.add(GA.sc(1), b2)), sq)
    ok = ok and GA.eq(GA.mul(P, P, sq), P)
    blades = GA.all_blades(6)
    left = [GA.basis_vector_of(GA.mul({b: F(1)}, P, sq), blades) for b in evens]
    ok = ok and GA.rank_of_vectors(left) == 8
    corner = [GA.basis_vector_of(GA.mul(GA.mul(P, {b: F(1)}, sq), P, sq), blades) for b in evens]
    ok = ok and GA.rank_of_vectors(corner) == 2
    J = GA.mul(I6, P, sq)
    ok = ok and GA.eq(GA.mul(J, J, sq), GA.scal(-1, P))
    ok = ok and GA.rank_of_vectors(corner + [GA.basis_vector_of(P, blades), GA.basis_vector_of(J, blades)]) == 2
    GA.check("Cl^0(2,4) P is C^4 (real dimension 8) with complex unit I_6", ok)
    return ok
