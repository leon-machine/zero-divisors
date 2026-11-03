"""tower.rigidity-clock-frozen: exact checks.

GA.py blade engine, floor T_k = Cl(p+k, q+k) in the tower layout (ground first, then plane j as
e_j (+1), f_j (-1)), v_j = (e_j+f_j)/2, w_j = (e_j-f_j)/2, P_k = prod_j v_j w_j, Omega_k the plane
volume, twisted generators x Omega_k. Grounds: every (p,q) with n <= 4; floors k <= 2 (n + 2k <= 8).
(1) Clock and centre: the residue (p+k) - (q+k) mod 8 is p - q mod 8; the centre of each floor,
    computed blade-wise (exhaustive for diagonal forms), is span{1} when n is even and span{1, omega}
    when n is odd, with omega^2 of the floor equal to omega^2 of the ground. Hence a nontrivial
    central idempotent ((1 +- omega)/2, omega^2 = +1) exists on a floor exactly when it exists on the
    ground, exactly when p - q = 1 mod 4: never, at any height, over a simple ground.
(2) Morita: P_k is a full idempotent (1 = sum_I X_I P_k Y_I with X_I, Y_I products of plane matrix
    units, computed), and the corner P_k T_k P_k has dimension 2^n and is the twisted ground copy:
    the elements x Omega_k P_k satisfy the ground relations with unit P_k. So every floor is Morita
    equivalent to the ground, with the same division-ring type, simplicity class and centre.
(3) The physical tower: for Cl(1,3) and its floors k <= 2, e = (1 + e_0 e_1)/2 and P = e P_k give a
    corner P T P of dimension 4 spanned by P, I P, J P, IJ P with I = e_2 e_3, J = e_2 Omega_k,
    I^2 = J^2 = -1 on the corner and IJ = -JI: the quaternions; T P has dimension 4 * 2^(k+1), so
    Cl(1+k, 3+k) = Mat_{2^(k+1)}(H), at clock position 6 for every k.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

GROUNDS = [(p, n - p) for n in range(5) for p in range(n + 1)]


def floor(p, q, k):
    return tuple([1] * p + [-1] * q + [1, -1] * k)


def span_rank(elems, m):
    blades = GA.all_blades(m)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in elems])


def mulall(S, *xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, S)
    return out


def plane_data(n, k, S):
    E, Om = [], GA.sc(1)
    for j in range(k):
        e, f = GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1)
        v, w = GA.scal(F(1, 2), GA.add(e, f)), GA.scal(F(1, 2), GA.sub(e, f))
        E.append({(1, 1): GA.mul(v, w, S), (1, 2): v, (2, 1): w, (2, 2): GA.mul(w, v, S)})
        Om = GA.mul(Om, GA.mul(e, f, S), S)
    P = mulall(S, *[Ej[(1, 1)] for Ej in E])
    return E, Om, P


def centre(S):
    m = len(S)
    return [b for b in GA.all_blades(m) if all(GA.commutes({b: F(1)}, GA.gen(i), S) for i in range(m))]


def check_clock_and_centre_frozen():
    premise("tower.matrix-amplification-structural-properties")
    premise("transport.existence-classification-type-c")
    for p, q in GROUNDS:
        n = p + q
        S0 = GA.sig(p, q)
        z0 = centre(S0)
        om0 = {tuple(range(n)): F(1)}
        sq0 = GA.mul(om0, om0, S0)
        ground_c = n % 2 == 1 and GA.eq(sq0, GA.sc(1))
        assert ground_c == (n >= 1 and (p - q) % 4 == 1)
        for k in range(3):
            if n + 2 * k > 8:
                continue
            S = floor(p, q, k)
            m = n + 2 * k
            assert ((p + k) - (q + k)) % 8 == (p - q) % 8
            z = centre(S)
            assert len(z) == len(z0) == (2 if n % 2 == 1 else 1)
            assert z == ([(), tuple(range(m))] if n % 2 == 1 else [()])
            om = {tuple(range(m)): F(1)}
            sq = GA.mul(om, om, S)
            assert GA.eq(sq, sq0)
            has_c = n % 2 == 1 and GA.eq(sq, GA.sc(1))
            assert has_c == ground_c
            if has_c:
                eps = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
                assert GA.eq(GA.mul(eps, eps, S), eps)
    return True


# numbers of planes k for the full-corner check, and the largest floor (generators) it is run on (time)
CORNER_RUNGS = (1, 2)
MAX_GENERATORS = 8


def unit_blade(b):
    """The basis blade e_b as a multivector."""
    return {b: F(1)}


def check_full_corner_is_ground():
    premise("tower.commuting-copies")
    premise("tower.morita-equivalence-algebra-amplification")
    for p, q in GROUNDS:
        n = p + q
        for k in CORNER_RUNGS:
            S = floor(p, q, k)
            if len(S) > MAX_GENERATORS:
                continue
            m = n + 2 * k
            E, Om, P = plane_data(n, k, S)
            assert GA.eq(GA.mul(P, P, S), P)
            one = {}
            for I in product((1, 2), repeat=k):
                X = mulall(S, *[E[j][(I[j], 1)] for j in range(k)])
                Y = mulall(S, *[E[j][(1, I[j])] for j in reversed(range(k))])
                one = GA.add(one, mulall(S, X, P, Y))
            assert GA.eq(one, GA.sc(1))
            corner = [mulall(S, P, unit_blade(b), P) for b in GA.all_blades(m)]
            assert span_rank(corner, m) == 2 ** n
            tw = [mulall(S, GA.gen(i), Om, P) for i in range(n)]
            for i in range(n):
                assert GA.eq(GA.mul(tw[i], tw[i], S), GA.scal(S[i], P))
                for j in (j for j in range(n) if j != i):
                    assert GA.is_zero(GA.add(GA.mul(tw[i], tw[j], S), GA.mul(tw[j], tw[i], S)))
                assert GA.eq(GA.mul(P, tw[i], S), tw[i]) and GA.eq(GA.mul(tw[i], P, S), tw[i])
    return True


def check_physical_tower_is_quaternionic():
    for k in range(3):
        S = floor(1, 3, k)
        m = 4 + 2 * k
        E, Om, Pk = plane_data(4, k, S)
        e = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(GA.gen(0), GA.gen(1), S)))
        P = GA.mul(e, Pk, S)
        assert GA.eq(GA.mul(P, P, S), P)
        corner = [mulall(S, P, {b: F(1)}, P) for b in GA.all_blades(m)]
        assert span_rank(corner, m) == 4
        I = GA.mul(GA.gen(2), GA.gen(3), S)
        J = GA.mul(GA.gen(2), Om, S)
        IP, JP = GA.mul(I, P, S), GA.mul(J, P, S)
        for X in (IP, JP):
            assert GA.eq(GA.mul(P, X, S), X) and GA.eq(GA.mul(X, P, S), X)
            assert GA.eq(GA.mul(X, X, S), GA.neg(P))
        assert GA.eq(GA.mul(IP, JP, S), GA.neg(GA.mul(JP, IP, S)))
        assert span_rank([P, IP, JP, GA.mul(IP, JP, S)], m) == 4
        left = [GA.mul({b: F(1)}, P, S) for b in GA.all_blades(m)]
        assert span_rank(left, m) == 4 * 2 ** (k + 1)
        assert 2 ** m == 4 * (2 ** (k + 1)) ** 2
        assert ((1 + k) - (3 + k)) % 8 == 6
    return True
