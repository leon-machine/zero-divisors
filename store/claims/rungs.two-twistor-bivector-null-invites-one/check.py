"""rungs.two-twistor-bivector-null-invites-one: exact checks.

(1) Lambda^2 of the conformal spinor space C^4 with the Klein form eps(P ^ P) (Fact
    rungs.imported-spinor-identification-witt-data-line): the form has rank 6 on the six-dimensional V_C, every
    pairwise bivector Z^i ^ Z^j of four Gaussian-rational conformal spinors is null, and a sum of two of them is not.
    With Z = (omega, pi), n_inf = e_1 ^ e_2: eps(n_inf ^ Z^1 ^ Z^2) = <pi^1 pi^2>, and the momentum
    p = sum pi^i pibar^i has p^2 = 2 det p = 2 |eps(n_inf ^ Z^1 ^ Z^2)|^2 (Lemma rungs.mass-bracket-frozen-points-
    grip-slot), zero for one spinor.
(2) Completion: R^(2,4) plus one hyperbolic pair v, w (v^2 = w^2 = 0, vw + wv = 1, orthogonal to R^(2,4)) has
    congruence signature (3, 5, 0); in GA Cl(3,5) the pair satisfies these relations and a null p of R^(2,4) stays
    null and anticommutes with v and w. The count of conformal spinors does not enter (the input is the quadratic
    space alone); uniqueness up to isometry and the totality of the reciprocal are the imported fact's content.
(3) One rung: on the four-mode Fock space (mode 0 the rung, 16 = 2 x 8 states, Jordan-Wigner, Gaussian-rational
    sparse matrices) the six twisted ground generators omega gamma_a (omega = gamma_0 gamma_1) satisfy Clifford
    relations with square -1 and their 64 blades have complex rank 64 (real rank 128 with their i-multiples), so
    they generate M_8(C) and the commutant is 4-dimensional: the rung algebra span{1, gamma_0, gamma_1, omega},
    which commutes with them. gamma_0 = v + w and gamma_1 anticommute with the chirality Gamma; inside the rung
    algebra the chirality-preserving part has complex dimension 2, span{1, omega}, and is commutative: a torus.
(4) Two rungs (five modes, rungs 0 and 1): the rung-mixing operators a_r^dag a_s span a complex 4-dimensional space,
    are non-abelian ([E_01, E_10] = n_0 - n_1), commute with Gamma and with the twisted ground generators
    Omega gamma_a (Omega = gamma_0 gamma_1 gamma_2 gamma_3): a U(2) within one chirality.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
from tp_premise import premise

QI = GA.QI
TWISTORS = [[QI(2), QI(-1), QI(3), QI(5)], [QI(1), QI(4), QI(-2), QI(7)], [QI(1), QI(0, 1), QI(0), QI(1)],
            [QI(0), QI(1), QI(1, 1), QI(0)]]


# ---- Lambda^2 C^4 and the Klein form --------------------------------------------------------------------
PAIRS = list(combinations(range(4), 2))


def _wedge2(Z1, Z2):
    return {(x, y): Z1[x] * Z2[y] - Z1[y] * Z2[x] for x, y in PAIRS}


def _sign4(arr):
    if len(set(arr)) < 4:
        return 0
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if arr[i] > arr[j]:
                s = -s
    return s


def _klein(P, Q):
    """eps(P ^ Q) for bivectors given on the basis e_x ^ e_y, x < y."""
    return sum((QI(_sign4([a, b, c, d])) * P[(a, b)] * Q[(c, d)] for (a, b) in PAIRS for (c, d) in PAIRS), QI(0))


def _eps3(n, Z1, Z2):
    """eps(n ^ Z1 ^ Z2) for a decomposable n = e_i ^ e_j given as (i, j)."""
    i, j = n
    return sum((QI(_sign4([i, j, c, d])) * (Z1[c] * Z2[d]) for c in range(4) for d in range(4)), QI(0))


# ---- sparse Gaussian-rational matrices on Fock spaces ----------------------------------------------------
def _annih(i, dim):
    M = {}
    for b in range(dim):
        if b >> i & 1:
            M[(b ^ (1 << i), b)] = QI(-1 if bin(b & ((1 << i) - 1)).count("1") % 2 else 1)
    return M


def _dag(M):
    return {(c, r): z.conj() for (r, c), z in M.items()}


def _mul(A, B):
    byrow = {}
    for (r, c), z in B.items():
        get_or_set(byrow, r, []).append((c, z))
    out = {}
    for (r, c), z in A.items():
        for (d, w) in byrow.get(c, []):
            out[(r, d)] = out.get((r, d), QI(0)) + z * w
    return {k: v for k, v in out.items() if v}


def _add(A, B, s=1):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, QI(0)) + (v if s == 1 else QI(0) - v)
    return {k: v for k, v in out.items() if v}


def _scal(c, A):
    return {k: c * v for k, v in A.items() if c * v}


def _comm(A, B):
    return _add(_mul(A, B), _mul(B, A), -1)


def _acomm(A, B):
    return _add(_mul(A, B), _mul(B, A))


def _fock(nm):
    dim = 2 ** nm
    a = [_annih(i, dim) for i in range(nm)]
    ad = [_dag(x) for x in a]
    gam = []
    for i in range(nm):
        gam.append(_add(a[i], ad[i]))
        gam.append(_scal(QI(0, 1), _add(a[i], ad[i], -1)))
    I = {(b, b): QI(1) for b in range(dim)}
    G = I
    for i in range(nm):
        G = _mul(G, _add(I, _scal(QI(2), _mul(ad[i], a[i])), -1))
    return dim, a, ad, gam, I, G


def _real_rank(mats):
    keys = sorted(set(k for M in mats for k in M))
    rows = [[x for k in keys for x in (M.get(k, QI(0)).re, M.get(k, QI(0)).im)] for M in mats]
    return GA.rank_of_vectors(rows)


def check_pairwise_bivectors_null():
    premise("rungs.imported-spinor-identification-witt-data-line")
    premise("rungs.mass-bracket-frozen-points-grip-slot")
    basis = [{p: (QI(1) if p == q else QI(0)) for p in PAIRS} for q in PAIRS]
    gram = [[_klein(P, Q) for Q in basis] for P in basis]
    ok = GA.field_rank(gram) == 6 == len(PAIRS)
    n = len(TWISTORS)
    for i in range(n):
        for j in range(i + 1, n):
            P = _wedge2(TWISTORS[i], TWISTORS[j])
            ok = ok and _klein(P, P) == QI(0) and any(v != QI(0) for v in P.values())
    S = {k: _wedge2(TWISTORS[0], TWISTORS[1])[k] + _wedge2(TWISTORS[2], TWISTORS[3])[k] for k in PAIRS}
    ok = ok and _klein(S, S) != QI(0)
    for i in range(n):
        for j in range(i + 1, n):
            Z1, Z2 = TWISTORS[i], TWISTORS[j]
            br = Z1[2] * Z2[3] - Z1[3] * Z2[2]
            e3 = _eps3((0, 1), Z1, Z2)
            p = [[sum((Z[A] * Z[B].conj() for Z in (Z1, Z2)), QI(0)) for B in (2, 3)] for A in (2, 3)]
            detp = p[0][0] * p[1][1] - p[0][1] * p[1][0]
            ok = ok and e3 == br and detp == e3 * e3.conj()
            p1 = [[Z1[A] * Z1[B].conj() for B in (2, 3)] for A in (2, 3)]
            ok = ok and p1[0][0] * p1[1][1] - p1[0][1] * p1[1][0] == QI(0)
    GA.check("pairwise bivectors are null in V_C (Klein form rank 6), a sum is not; m^2 = 2|eps(n_inf Z1 Z2)|^2", ok)
    return ok


def check_one_hyperbolic_plane_completion():
    premise("rungs.imported-totality-minimality-completion")
    premise("rungs.imported-tower-one-qubit-per-rung")
    S = GA.sig(3, 5)                       # e0, e1, e2 square +1; e3..e7 square -1; R^(2,4) on e0, e1, e3..e6
    v = GA.scal(F(1, 2), GA.add(GA.gen(2), GA.gen(7)))
    w = GA.scal(F(1, 2), GA.sub(GA.gen(2), GA.gen(7)))
    ok = GA.is_zero(GA.mul(v, v, S)) and GA.is_zero(GA.mul(w, w, S))
    ok = ok and GA.eq(GA.add(GA.mul(v, w, S), GA.mul(w, v, S)), GA.sc(1))
    old = [0, 1, 3, 4, 5, 6]
    ok = ok and all(GA.anticommutes(GA.gen(i), x, S) for i in old for x in (v, w))
    p = GA.add(GA.scal(F(5), GA.gen(0)), GA.scal(F(3), GA.gen(3)), GA.scal(F(4), GA.gen(4)))
    ok = ok and GA.is_zero(GA.mul(p, p, S)) and GA.anticommutes(p, v, S) and GA.anticommutes(p, w, S)
    gram = [[F(0)] * 8 for _ in range(8)]
    for i, s in enumerate((1, 1, -1, -1, -1, -1)):
        gram[i][i] = F(s)
    gram[6][7] = gram[7][6] = F(1, 2)
    ok = ok and GA.congruence_signature(gram) == (3, 5, 0)
    GA.check("R^(2,4) + one hyperbolic plane = R^(3,5); the rung pair is null, reciprocal, orthogonal; p stays null", ok)
    return ok


def check_one_rung_u2_mixes_chirality():
    premise("rungs.imported-tower-one-qubit-per-rung")
    premise("rungs.imported-spinor-identification-witt-data-line")
    dim, a, ad, gam, I, G = _fock(4)
    omega = _mul(gam[0], gam[1])
    tw = [_mul(omega, gam[k]) for k in range(2, 8)]
    ok = dim == 2 * 8
    ok = ok and all(_acomm(tw[p], tw[q]) == (_scal(QI(-2), I) if p == q else {}) for p in range(6) for q in range(6))
    blades = []
    for k in range(7):
        for Sb in combinations(range(6), k):
            B = I
            for t in Sb:
                B = _mul(B, tw[t])
            blades.append(B)
    ok = ok and len(blades) == 64 and _real_rank(blades + [_scal(QI(0, 1), B) for B in blades]) == 128
    rung = [I, gam[0], gam[1], omega]
    ok = ok and _real_rank(rung + [_scal(QI(0, 1), X) for X in rung]) == 8
    ok = ok and all(_comm(X, t) == {} for X in rung for t in tw)
    ok = ok and _acomm(gam[0], G) == {} and _acomm(gam[1], G) == {} and gam[0] == _add(a[0], ad[0])
    # chirality-preserving part of span{1, g0, g1, omega}: complex kernel of X -> [X, Gamma]
    rows = []
    cols = [_comm(X, G) for X in rung]
    keys = sorted(set(k for C in cols for k in C))
    rows = [[C.get(k, QI(0)) for C in cols] for k in keys]
    ker = GA.field_kernel(rows)
    ok = ok and len(ker) == 2 and all(v[1] == QI(0) and v[2] == QI(0) for v in ker)
    ok = ok and _comm(I, omega) == {} and _comm(gam[0], gam[1]) != {}
    GA.check("one rung: twisted ground generates M_8(C), commutant span{1, g0, g1, omega} = M_2(C); "
             "its chirality-preserving part span{1, omega} is abelian", ok)
    return ok


def check_two_rungs_give_chirality_preserving_u2():
    premise("rungs.rung-spinor-module-mixings")
    dim, a, ad, gam, I, G = _fock(5)
    E = {(r, s): _mul(ad[r], a[s]) for r in range(2) for s in range(2)}
    Om = _mul(_mul(gam[0], gam[1]), _mul(gam[2], gam[3]))
    tw = [_mul(Om, gam[k]) for k in range(4, 10)]
    ok = dim == 32 and _real_rank(list(E.values()) + [_scal(QI(0, 1), X) for X in E.values()]) == 8
    ok = ok and _comm(E[(0, 1)], E[(1, 0)]) == _add(_mul(ad[0], a[0]), _mul(ad[1], a[1]), -1)
    ok = ok and _comm(E[(0, 1)], E[(1, 0)]) != {}
    ok = ok and all(_comm(X, G) == {} for X in E.values()) and all(_comm(X, t) == {} for X in E.values() for t in tw)
    GA.check("two rungs: a_r^dag a_s span a non-abelian u(2) commuting with chirality and the twisted ground", ok)
    return ok
