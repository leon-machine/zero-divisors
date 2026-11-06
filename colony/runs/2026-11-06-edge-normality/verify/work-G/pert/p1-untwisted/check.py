"""synthesis.blade-square-signs-f2-quadratic-form: exact checks.

Blades e_S of Cl(p,q) are indexed by subsets S of the n directions, stored as bitmasks.
q(S) = 1 iff e_S^2 = -1, read from GA products. Everything is exact (Fractions in GA.py).
(1) The sign from symmetry: a skew relation x y = c y x read both ways forces c^2 = 1, and the
    square x^2 commutes with y exactly when c^2 = 1 (normal-ordered model of the quantum plane
    for c = 2, 1/3, -1, 1); in Cl(p,q) the squares of generators are central.
(2) q is a quadratic form over F2 with polar form the anticommutation form, and the closed forms
    q(S) = C(|S|,2) + |S cap Neg| and b(S,T) = |S||T| + |S cap T| (mod 2), for every signature
    with n <= 5; e_S e_T = +/- e_{S xor T} (the vee group is a central extension by +/-1).
(3) Radical, Gauss sum and type, for all 44 signatures with 1 <= n <= 8: the radical is {0} for
    n even and {0, full} for n odd; sum_S (-1)^q(S) = <(1 - j)(1 + j)^p (1 - j)^q>_0 with j a unit
    bivector of a Euclidean plane; its value fixes the type of the classification table.
(4) The (1,1) ascent: the twisted ground blades and the plane blades give an isometry
    q_(p,q) + q_(1,1) -> q_(p+1,q+1); Arf(q_(1,1)) = 0, Arf(q_(0,2)) = 1.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise


def blade(mask, n):
    return {tuple(i for i in range(n) if mask >> i & 1): F(1)}


def qform(p, q):
    """q(S) in {0, 1} for every bitmask S, from the GA square of the blade."""
    n = p + q
    S = GA.sig(p, q)
    out = []
    for m in range(2 ** n):
        b = blade(m, n)
        sq = GA.mul(b, b, S)
        assert list(sq) == [()] and sq[()] in (1, -1)
        out.append(0 if sq[()] == 1 else 1)
    return out


def popcount(m):
    return bin(m).count("1")


def gauss(qv):
    return sum(1 - 2 * x for x in qv)


def arf_even(qv, n):
    """Arf invariant of a nondegenerate form on F2^n, n even: the value taken most often."""
    ones = sum(qv)
    if ones == 2 ** (n - 1) - 2 ** (n // 2 - 1):
        return 0
    assert ones == 2 ** (n - 1) + 2 ** (n // 2 - 1)
    return 1


# --- type table of the classification (p - q mod 8) -------------------------
TYPE = {0: "R", 2: "R", 4: "H", 6: "H", 1: "R+R", 5: "H+H", 3: "C", 7: "C"}


def check_symmetry_forces_the_sign():
    premise("std-algebra.orthogonal-anticommute")
    # normal-ordered model of k<x,y>/(y x = c^{-1} x y): monomial x^a y^b; y^b x^a = c^(-ab) x^a y^b
    def mono_mul(m1, m2, c):
        (a1, b1), (a2, b2) = m1, m2
        return (c ** (-(b1 * a2)), (a1 + a2, b1 + b2))
    results = {}
    for c in (F(2), F(1, 3), F(-1), F(1)):
        # x y = c y x  <=>  y x = c^{-1} x y ; read with i, j exchanged: y x = c x y, so c^{-1} = c
        symmetric = (c ** -1 == c)
        coef1, m1 = mono_mul((2, 0), (0, 1), c)      # x^2 . y
        coef2, m2 = mono_mul((0, 1), (2, 0), c)      # y . x^2
        assert m1 == m2 == (2, 1)
        central = (coef1 == coef2)
        assert coef1 == c ** 2 * coef2              # x^2 y = c^2 y x^2
        results[c] = (symmetric, central)
    assert all(s == z for s, z in results.values())
    assert [results[c] for c in (F(2), F(-1))] == [(False, False), (True, True)]
    # in Cl(p,q): distinct generators anticommute (c = -1) and every square is central
    for p, q in ((1, 3), (2, 2), (0, 3)):
        S = GA.sig(p, q)
        n = p + q
        for i in range(n):
            sq = GA.mul(GA.gen(i), GA.gen(i), S)
            for j in range(n):
                assert GA.commutes(sq, GA.gen(j), S)
                if i != j:
                    assert GA.anticommutes(GA.gen(i), GA.gen(j), S)
    return True


def check_blade_signs_are_a_quadratic_form():
    premise("std-algebra.orthogonal-anticommute")
    count = 0
    for n in range(1, 6):
        for p in range(n + 1):
            q = n - p
            S = GA.sig(p, q)
            qv = qform(p, q)
            neg = sum(1 << i for i in range(p, n))
            for s in range(2 ** n):
                k = popcount(s)
                assert qv[s] == (k * (k - 1) // 2 + popcount(s & neg)) % 2
            for s in range(2 ** n):
                bs = blade(s, n)
                for t in range(2 ** n):
                    bt = blade(t, n)
                    st = GA.mul(bs, bt, S)
                    ts = GA.mul(bt, bs, S)
                    # e_S e_T = +/- e_{S xor T}
                    assert list(st) == list(blade(s ^ t, n)) and abs(st[tuple(st)[0]]) == 1
                    anti = 1 if GA.eq(st, GA.neg(ts)) else 0
                    assert anti == (0 if GA.eq(st, ts) else 1)
                    polar = (qv[s ^ t] + qv[s] + qv[t]) % 2
                    assert polar == anti
                    assert anti == (popcount(s) * popcount(t) + popcount(s & t)) % 2
            count += 1
    assert count == 20
    return True


def check_radical_gauss_sum_and_type():
    premise("transport.classification-real-clifford-algebras")
    premise("primer.sign")
    E2 = GA.sig(2, 0)
    j = {(0, 1): F(1)}
    one = GA.sc(1)
    assert GA.eq(GA.mul(j, j, E2), GA.sc(-1))
    seen = {}
    for n in range(1, 9):
        full = 2 ** n - 1
        for p in range(n + 1):
            q = n - p
            qv = qform(p, q)
            pol = lambda s, t: (popcount(s) * popcount(t) + popcount(s & t)) % 2
            gens = [1 << i for i in range(n)]
            radical = [s for s in range(2 ** n) if all(pol(s, g) == 0 for g in gens)]
            g = gauss(qv)
            # the Gauss sum in the algebra: <(1 - j)(1 + j)^p (1 - j)^q>_0
            x = GA.sub(one, j)
            for _ in range(p):
                x = GA.mul(x, GA.add(one, j), E2)
            for _ in range(q):
                x = GA.mul(x, GA.sub(one, j), E2)
            assert x.get((), F(0)) == g
            t = TYPE[(p - q) % 8]
            if n % 2 == 0:
                assert radical == [0]
                assert g * g == 2 ** n
                arf = arf_even(qv, n)
                assert (arf == 0) == (t == "R") and (arf == 1) == (t == "H")
                assert g == (2 ** (n // 2)) * (1 - 2 * arf)
            else:
                assert radical == [0, full]
                omega_sq_neg = qv[full]
                assert (omega_sq_neg == 1) == (t == "C")
                if omega_sq_neg:
                    assert g == 0
                else:
                    assert g * g == 2 ** (n + 1)
                    split = 0 if g > 0 else 1
                    assert (split == 0) == (t == "R+R") and (split == 1) == (t == "H+H")
            seen[(p, q)] = t
    assert len(seen) == 44
    assert sum(1 for (p, q) in seen if (p + q) % 2 == 0) == 24
    return True


def check_ascent_adds_a_hyperbolic_plane():
    premise("tower.commuting-copies")
    premise("tower.rigidity-clock-frozen")
    qH = qform(1, 1)
    q02 = qform(0, 2)
    assert arf_even(qH, 2) == 0 and arf_even(q02, 2) == 1
    assert q02 == [0, 1, 1, 1]
    for p, q in ((1, 3), (0, 2), (2, 1), (1, 1), (0, 3)):
        n = p + q
        # Cl(p+1, q+1): ground generators 0..n-1 reordered to keep the signature layout:
        # positive ground 0..p-1, e = p, negative ground p+1..p+q, f = n+1
        S = GA.sig(p + 1, q + 1)
        ground = list(range(p)) + list(range(p + 1, p + 1 + q))
        e, f = p, n + 1
        omega = GA.mul(GA.gen(e), GA.gen(f), S)
        assert GA.eq(GA.mul(omega, omega, S), GA.sc(1))
        twisted = [GA.gen(g) for g in ground]
        plane = [GA.gen(e), GA.gen(f)]
        qg = qform(p, q)
        images = set()
        for A in range(2 ** n):
            xa = GA.sc(1)
            for i in range(n):
                if A >> i & 1:
                    xa = GA.mul(xa, twisted[i], S)
            for B in range(4):
                y = xa
                for i in range(2):
                    if B >> i & 1:
                        y = GA.mul(y, plane[i], S)
                assert len(y) == 1
                (bl, c), = y.items()
                images.add(bl)
                sq = GA.mul(y, y, S)
                assert sq == {(): F(1 - 2 * ((qg[A] + qH[B]) % 2))}
                for g in twisted:
                    for h in plane:
                        assert GA.commutes(g, h, S)
        assert len(images) == 2 ** (n + 2)
    return True
