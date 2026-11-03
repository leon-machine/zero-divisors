"""tower.structure-tower-c-norms: exact checks of the algebraic part.

Complexified floors T_k^C are GA.py multivectors with Gaussian-rational (GA.QI) coefficients, in the
tower layout (ground (p,q) first, then plane j as e_j (+1), f_j (-1)). The * of the statement is
    (c e_I)* = conj(c) (-1)^(|I|(|I|-1)/2) (-1)^(#{i in I : e_i^2 = -1}) e_I .
(1) Existence and uniqueness: on every floor with m = n + 2k <= 6 (all grounds n <= 4, k <= 1, and
    n <= 2, k = 2) this formula equals the reversed product of the generator values x* = +-x (so it is
    the antiautomorphism those values determine), it is antimultiplicative on every pair of basis
    blades, conjugate-linear and antimultiplicative on complex samples, and involutive.
(2) Unitarity and adjoints: every frame blade z (all of them, m <= 8) has z* z = 1, in particular the
    ground volume u_A, the plane volumes omega_j and Omega_k; v_j* = w_j and w_j* = v_j.
(3) Compatibility of the maps: iota_k (inclusion) commutes with * (same values on the blades of
    T_k inside T_{k+1}); phi_k is a *-map: phi_k^{-1}(M)* = phi_k^{-1}(M^dagger) for every basis matrix
    a (x) E_{I,J} (M^dagger = transpose with entrywise *), using the identification exported by
    tower.compatibility-connecting-maps-transported; theta_k commutes with dagger; the correctors V_k
    and W_k (W_0 = 1, W_{k+1} = theta_k(W_k) V_k^{-1}) are unitary for k <= 2.
(4) Even p - q: the tensor-Pauli assignment (over Q(i)) of the generators (x -> Y_i if x^2 = 1,
    x -> -i Y_i if x^2 = -1) satisfies the floor's relations, carries * to the conjugate transpose on
    every blade, and the 2^m blade images are orthogonal for the trace form (Tr(M_S^dagger M_T) =
    N delta_ST, computed), hence independent, and 2^m = N^2 with N = 2^(m/2): a *-isomorphism onto
    Mat_N(C), for every even floor with m <= 6.
Not computable here: the uniqueness of the C*-norm on a full matrix algebra and the isometry of
*-monomorphisms (spectral-radius arguments of analysis); they rest on (4).
"""
from fractions import Fraction as F
from itertools import product

import GA
import fock
from tp_premise import premise

QI = GA.QI
FLOORS = [((p, n - p), k) for n in range(5) for p in range(n + 1) for k in (0, 1)
          if n + 2 * k <= 6] + [((p, n - p), 2) for n in range(3) for p in range(n + 1)]
CS1 = {(): QI(2, 1), (0,): QI(0, 3), (0, 1): QI(1, -1), (1, 2): QI(F(1, 2), 0)}
CS2 = {(1,): QI(-1, 2), (0, 2): QI(3, 0), (): QI(0, F(1, 3)), (0, 1, 2): QI(1, 1)}


def floor(p, q, k):
    return tuple([1] * p + [-1] * q + [1, -1] * k)


def star(x, S):
    out = {}
    for b, c in x.items():
        g = len(b)
        sgn = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if S[i] == -1)
        cc = c.conj() if isinstance(c, QI) else c
        out[b] = cc * sgn
    return {b: c for b, c in out.items() if c != 0}


def restrict(x, m):
    return {b: c for b, c in x.items() if all(i < m for i in b)}


def check_star_exists_unique_antimultiplicative():
    for (p, q), k in FLOORS:
        S = floor(p, q, k)
        m = len(S)
        gstar = [GA.scal(S[i], GA.gen(i)) for i in range(m)]
        for b in GA.all_blades(m):
            prod_ = GA.sc(1)
            for i in reversed(b):
                prod_ = GA.mul(prod_, gstar[i], S)
            assert GA.eq(star({b: F(1)}, S), prod_)
        for b1 in GA.all_blades(m):
            for b2 in GA.all_blades(m):
                x, y = {b1: F(1)}, {b2: F(1)}
                assert GA.eq(star(GA.mul(x, y, S), S), GA.mul(star(y, S), star(x, S), S))
        a, c = restrict(CS1, m), restrict(CS2, m)
        assert GA.eq(star(GA.mul(a, c, S), S), GA.mul(star(c, S), star(a, S), S))
        assert GA.eq(star(star(a, S), S), a)
        ia = {b: x * QI(0, 1) for b, x in a.items()}
        assert GA.eq(star(ia, S), {b: x * QI(0, -1) for b, x in star(a, S).items()})
    return True


def check_frame_unitary_and_ladder_adjoint():
    for p, q in [(p, n - p) for n in range(5) for p in range(n + 1)]:
        for k in range(3):
            S = floor(p, q, k)
            m = len(S)
            if m > 8:
                continue
            n = p + q
            for b in GA.all_blades(m):
                z = {b: F(1)}
                assert GA.eq(GA.mul(star(z, S), z, S), GA.sc(1))
            vols = [{tuple(range(n)): F(1)}]
            Om = GA.sc(1)
            for j in range(k):
                e, f = GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1)
                om = GA.mul(e, f, S)
                Om = GA.mul(Om, om, S)
                vols.append(om)
                v, w = GA.scal(F(1, 2), GA.add(e, f)), GA.scal(F(1, 2), GA.sub(e, f))
                assert GA.eq(star(v, S), w) and GA.eq(star(w, S), v)
                assert GA.eq(star(om, S), om)
            vols.append(Om)
            for z in vols:
                assert GA.eq(GA.mul(star(z, S), z, S), GA.sc(1))
    return True


# (ground (p, q), number of floors kk + 1) for the compatibility check
COMPAT_CASES = [((1, 1), 3), ((2, 0), 2), ((0, 2), 2), ((1, 3), 2)]
# generators added by one plane (e_j, f_j): T_k is T_(k+1) without its last two generators
PLANE_GENS = 2
# matrix-unit level at which theta is checked to commute with the dagger
THETA_LEVEL = 1


def check_maps_and_correctors_compatible():
    ex = premise("tower.compatibility-connecting-maps-transported")
    premise("tower.commuting-copies")
    premise("tower.algebraic-limit-even-charge")
    premise("transport.rule-1-morita-trivial")
    Tower, idx, theta, corrector = ex["Tower"], ex["idx"], ex["theta"], ex["corrector"]
    for (p, q), floors in COMPAT_CASES:
        T = Tower(p, q, floors)
        S = T.S
        m = len(S)
        # iota: the * of T_k is the restriction of the * of T_{k+1}
        for b in GA.all_blades(m - PLANE_GENS):
            assert GA.eq(star({b: F(1)}, S[:m - PLANE_GENS]), star({b: F(1)}, S))
        for k in range(floors):
            for a in GA.all_blades(T.n):
                for I in idx(k):
                    for J in idx(k):
                        x = T.phi_inv({(I, J): {a: F(1)}}, k)
                        dag = T.phi_inv({(J, I): star({a: F(1)}, S)}, k)
                        assert GA.eq(star(x, S), dag)
        # theta commutes with dagger, on matrix units
        for I in idx(THETA_LEVEL):
            for J in idx(THETA_LEVEL):
                M = {(I, J): GA.sc(1)}
                th = theta(M)
                thd = {(L, K): star(a, S) for (K, L), a in th.items()}
                assert thd == theta({(J, I): GA.sc(1)})
        # correctors: diagonal with entries u_A or +-1; V^dagger V = 1; W recursion stays unitary
        W = {((), ()): GA.sc(1)}
        for k in range(floors):
            V, Vi = corrector(T, k, True)
            for K, x in V.items():
                assert GA.eq(GA.mul(star(x, S), x, S), GA.sc(1))
                assert GA.eq(star(x, S), Vi[K])
            th = theta(W)
            W = {(K, L): GA.mul(a, Vi[L], S) for (K, L), a in th.items()}
            for (K, L), a in W.items():
                assert K == L and GA.eq(GA.mul(star(a, S), a, S), GA.sc(1))
        assert len(W) == 2 ** floors
    return True


def pauli_rep(m):
    """Tensor-Pauli Y_1..Y_m on (C^2)^(m/2) as monomial matrices: row i -> (column, QI entry). These are
    the Hermitian Jordan-Wigner Majoranas (sz on earlier factors; sx, sy on the mode's own factor)."""
    return [[(j, QI(c)) for (i, j), c in sorted(fock.majorana(p, m // 2, fock.MSB, kind="herm").items())]
            for p in range(2 * (m // 2))]


def mm(A, B):
    """Product of monomial matrices: (AB)[i] = B applied after A's column."""
    return [(B[A[i][0]][0], A[i][1] * B[A[i][0]][1]) for i in range(len(A))]


def dagger(A):
    out = [None] * len(A)
    for i, (j, c) in enumerate(A):
        out[j] = (i, c.conj())
    return out


def trace(A):
    return sum((c for i, (j, c) in enumerate(A) if i == j), QI(0))


def check_even_floors_are_full_matrix_star_algebras():
    for (p, q), k in FLOORS:
        if (p - q) % 2:
            continue
        S = floor(p, q, k)
        m = len(S)
        if m == 0:
            continue
        N = 2 ** (m // 2)
        Y = pauli_rep(m)
        X = [Y[i] if S[i] == 1 else [(j, c * QI(0, -1)) for j, c in Y[i]] for i in range(m)]
        ident = [(i, QI(1)) for i in range(N)]
        for i in range(m):
            assert mm(X[i], X[i]) == [(j, c * S[i]) for j, c in ident]
            for j in range(i + 1, m):
                assert mm(X[i], X[j]) == [(a, -c) for a, c in mm(X[j], X[i])]
        imgs = []
        for b in GA.all_blades(m):
            M = ident
            for i in b:
                M = mm(M, X[i])
            (bb, sgn), = star({b: F(1)}, S).items()
            assert bb == b and dagger(M) == [(j, c * sgn) for j, c in M]
            imgs.append(M)
        # trace form: Tr(M_S^dagger M_T) = N delta_ST, so the 2^m images are independent
        for a, A in enumerate(imgs):
            Ad = dagger(A)
            for bi, B in enumerate(imgs):
                assert trace(mm(Ad, B)) == (QI(N) if a == bi else QI(0))
        assert len(imgs) == 2 ** m == N * N
    return True
