"""tower.grade-twist-when-it-inner: exact checks.

GA.py blade engine, ground Cl(p,q) at indices 0..n-1 and the new plane (e, f) after it, with the
ladder pair v = (e+f)/2, w = (e-f)/2 and the matrix units of Fact transport.rule-1-morita-trivial,
E11 = v w, E22 = w v, E12 = v, E21 = w (so E11 = (1 - e f)/2).
(1) The matrix form of the tower embedding: for every ground with n <= 4, every basis blade a of the
    base, read through the corner identification (entry c_ij defined by c_ij E11 = E1i a Ej1), has
    the matrix diag(a, a^) (a^ the grade involution): the twisted diagonal. In the twisted-copy
    coordinates of tower.commuting-copies with the same labelling (a ground generator x read as
    x omega = x^(1) times omega = 1 (x) diag(-1, 1)) the same embedding reads diag(a^, a); the order of
    the two corners is the labelling convention that tower.compatibility-connecting-maps-transported
    records (exchanging vw and wv exchanges them).
(2) Even n (every signature with n <= 6): the volume element u anticommutes with every generator,
    u^2 = +-1, and u a u^-1 = a^ on every basis blade; U diag(a, a) U^-1 = diag(a, a^) with
    U = diag(1, u) on sample elements (2 x 2 matrices with Clifford entries). For odd n <= 7, u
    commutes with every generator instead.
(3) Innerness exactly when n is even: the space of g with g x = -x g for every generator x (the
    elements implementing the grade involution, together with 0) is R u for even n <= 6 and {0}
    for odd n <= 5, computed as an exact kernel. For odd n <= 7 the centre is span{1, omega}
    (blade-wise), and the grade involution sends omega to -omega: it moves the centre, so it is outer.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(p, n - p) for n in range(1, 8) for p in range(n + 1)]
SAMPLE = {(): F(2), (0,): F(1), (0, 1): F(3), (1,): F(-1, 5), (0, 1, 2): F(4, 7)}


def sample_in(n):
    return {b: c for b, c in SAMPLE.items() if all(i < n for i in b)}


def vol(n):
    return {tuple(range(n)): F(1)}


def inv_pm1(u, S):
    u2 = GA.mul(u, u, S)
    return u if GA.eq(u2, GA.sc(1)) else GA.neg(u)


def m22(A, B, S):
    return [[GA.add(GA.mul(A[i][0], B[0][j], S), GA.mul(A[i][1], B[1][j], S)) for j in range(2)]
            for i in range(2)]


def check_embedding_is_twisted_diagonal():
    premise("transport.rule-1-morita-trivial")
    for p, q in [(p, n - p) for n in range(5) for p in range(n + 1)]:
        n = p + q
        S = GA.sig(p, q) + (1, -1)
        e, f = GA.gen(n), GA.gen(n + 1)
        v, w = GA.scal(F(1, 2), GA.add(e, f)), GA.scal(F(1, 2), GA.sub(e, f))
        E = {(1, 1): GA.mul(v, w, S), (2, 2): GA.mul(w, v, S), (1, 2): v, (2, 1): w}
        assert GA.eq(E[(1, 1)], GA.scal(F(1, 2), GA.sub(GA.sc(1), GA.mul(e, f, S))))
        for a_b in GA.all_blades(n):
            a = {a_b: F(1)}
            for i in (1, 2):
                for j in (1, 2):
                    m = GA.mul(GA.mul(E[(1, i)], a, S), E[(j, 1)], S)
                    # m = c E11 with c in the base: c is twice the part of m free of plane letters
                    c = {b: 2 * x for b, x in m.items() if n not in b and n + 1 not in b}
                    assert GA.eq(GA.mul(c, E[(1, 1)], S), m)
                    want = {} if i != j else (a if i == 1 else GA.grade_inv(a))
                    assert GA.eq(c, want), ((p, q), a_b, i, j)
            # twisted-copy coordinates: odd x = (x omega) omega, omega = E22 - E11 = diag(-1, 1)
            om = GA.mul(e, f, S)
            assert GA.eq(om, GA.sub(E[(2, 2)], E[(1, 1)]))
            if len(a_b) % 2 == 1:
                assert GA.eq(GA.mul(GA.mul(a, om, S), om, S), a)
    return True


def check_even_charge_volume_element_implements_twist():
    for p, q in SIGS:
        n = p + q
        S = GA.sig(p, q)
        u = vol(n)
        u2 = GA.mul(u, u, S)
        assert GA.eq(u2, GA.sc(1)) or GA.eq(u2, GA.sc(-1))
        uinv = inv_pm1(u, S)
        for i in range(n):
            x = GA.gen(i)
            if n % 2 == 0:
                assert GA.anticommutes(u, x, S)
            else:
                assert GA.commutes(u, x, S) and not GA.anticommutes(u, x, S)
        if n % 2 == 0 and n <= 6:
            for b in GA.all_blades(n):
                a = {b: F(1)}
                assert GA.eq(GA.mul(GA.mul(u, a, S), uinv, S), GA.grade_inv(a))
            a = sample_in(n)
            U = [[GA.sc(1), {}], [{}, u]]
            Ui = [[GA.sc(1), {}], [{}, uinv]]
            got = m22(m22(U, [[a, {}], [{}, a]], S), Ui, S)
            want = [[a, {}], [{}, GA.grade_inv(a)]]
            assert all(GA.eq(got[i][j], want[i][j]) for i in range(2) for j in range(2))
    return True


def check_inner_exactly_for_even_charge():
    for p, q in SIGS:
        n = p + q
        S = GA.sig(p, q)
        blades = GA.all_blades(n)
        if n <= 6:
            # unknown g = sum g_B B; equations: g x + x g = 0 for every generator x
            cols = []
            for B in blades:
                col = []
                for i in range(n):
                    x = GA.gen(i)
                    z = GA.add(GA.mul({B: F(1)}, x, S), GA.mul(x, {B: F(1)}, S))
                    col.extend(z.get(bb, F(0)) for bb in blades)
                cols.append(col)
            rows = [[cols[c][r] for c in range(len(blades))] for r in range(len(cols[0]))]
            ker = GA.field_kernel(rows)
            if n % 2 == 0:
                assert len(ker) == 1
                kv = ker[0]
                nz = [blades[i] for i in range(len(blades)) if kv[i] != 0]
                assert nz == [tuple(range(n))]
            elif n <= 5:
                assert len(ker) == 0
        if n % 2 == 1:
            central = [b for b in blades
                       if all(GA.commutes({b: F(1)}, GA.gen(i), S) for i in range(n))]
            assert central == [(), tuple(range(n))]
            om = vol(n)
            assert GA.eq(GA.grade_inv(om), GA.neg(om)) and not GA.eq(GA.grade_inv(om), om)
    return True
