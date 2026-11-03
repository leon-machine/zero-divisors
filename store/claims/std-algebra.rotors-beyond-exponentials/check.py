"""std-algebra.rotors-beyond-exponentials: exact checks.

(ii) In every signature (p, q) with p, q >= 2 and n <= 6: R = -e1 e2 e3 e4 (5/4 + 3/4 e1 e3)
(e1, e2 positive, e3, e4 negative) is a product of six unit vectors, R R~ = 1, Ad_R maps V to V,
and the characteristic polynomial of Ad_R is (t + 4)(t + 1/4)(t + 1)^2 (t - 1)^(n - 4), with -4 a
simple root.
(iii) Exponential rotors e^{(pi/2) e_i e_j} = e_i e_j (Q(e_i) Q(e_j) = 1) and their commuting
products have the negative eigenvalue -1 with even multiplicity, in the same signatures.
(iv) n = 1 and Cl(1,1): -1 is a rotor; exp(l e1 e2) = c + s e1 e2 has c >= 1 at rational points of
the hyperbola; every sampled rotor a + b e1 e2 has a^2 - b^2 = 1 and |a| >= 1.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SPLIT = [(2, 2), (2, 3), (3, 2), (2, 4), (3, 3), (4, 2)]


def _vecpart(x, n):
    out = [F(0)] * n
    for b, c in x.items():
        if c != 0:
            assert len(b) == 1
            out[b[0]] = c
    return out


def _ad_matrix(R, sq, n):
    Rt = GA.reverse(R)
    cols = [_vecpart(GA.mul(GA.mul(R, GA.gen(j), sq), Rt, sq), n) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def _charpoly(M):
    """det(t I - M), coefficients low to high (Faddeev-LeVerrier, exact)."""
    n = len(M)
    c = [F(0)] * (n + 1)
    c[n] = F(1)
    A = [[F(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        A = [[sum(M[i][t] * (A[t][j] + (c[n - k + 1] if t == j else 0)) for t in range(n))
              for j in range(n)] for i in range(n)]
        c[n - k] = -sum(A[i][i] for i in range(n)) / F(k)
    return c


def _pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def _peval(c, t):
    return sum(ci * t ** i for i, ci in enumerate(c))


def _split_rotor(p, q):
    sq = GA.sig(p, q)
    e1, e2, e3, e4 = GA.gen(0), GA.gen(1), GA.gen(p), GA.gen(p + 1)
    u = GA.add(GA.scal(F(5, 4), e1), GA.scal(F(3, 4), e3))
    factors = [GA.neg(e1), e2, e3, e4, e1, u]
    R = GA.sc(1)
    for f in factors:
        R = GA.mul(R, f, sq)
    return R, factors, sq


def check_split_rotor_has_simple_negative_eigenvalue():
    premise("std-algebra.bivector-exponential")
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.bivector-lie-algebra")
    for p, q in SPLIT:
        n = p + q
        R, factors, sq = _split_rotor(p, q)
        # ad of the boost bivector e1 e3 maps V to V: e1 -> -2 e3, e3 -> -2 e1, the rest -> 0
        E = GA.mul(GA.gen(0), GA.gen(p), sq)
        for j in range(n):
            x = GA.gen(j)
            adx = GA.sub(GA.mul(E, x, sq), GA.mul(x, E, sq))
            want = {0: GA.scal(-2, GA.gen(p)), p: GA.scal(-2, GA.gen(0))}.get(j, {})
            assert GA.eq(adx, want)
        I4 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), sq), GA.mul(GA.gen(p), GA.gen(p + 1), sq), sq)
        R0 = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), GA.mul(GA.gen(0), GA.gen(p), sq)))
        assert GA.eq(R, GA.neg(GA.mul(I4, R0, sq)))
        Qs = [GA.mul(f, f, sq) for f in factors]
        assert [GA.eq(x, GA.sc(1)) or GA.eq(x, GA.sc(-1)) for x in Qs] == [True] * 6
        assert GA.eq(GA.mul(R, GA.reverse(R), sq), GA.sc(1))
        assert all(len(b) % 2 == 0 for b, c in R.items() if c != 0)
        M = _ad_matrix(R, sq, n)
        cp = _charpoly(M)
        want = _pmul(_pmul([F(4), F(1)], [F(1, 4), F(1)]), [F(1), F(2), F(1)])
        for _ in range(n - 4):
            want = _pmul(want, [F(-1), F(1)])
        assert cp == want
        dcp = [i * cp[i] for i in range(1, len(cp))]
        assert _peval(cp, F(-4)) == 0 and _peval(dcp, F(-4)) != 0
    return True


def check_exponential_rotors_have_even_negative_multiplicity():
    premise("std-algebra.bivector-exponential")
    for p, q in SPLIT:
        n = p + q
        sq = GA.sig(p, q)
        planes = [(i, j) for i, j in combinations(range(n), 2) if sq[i] * sq[j] == 1]
        assert planes
        for i, j in planes[:4]:
            E = GA.mul(GA.gen(i), GA.gen(j), sq)
            assert GA.eq(GA.mul(E, E, sq), GA.sc(-1))          # elliptic: e^{(pi/2)E} = E
            cp = _charpoly(_ad_matrix(E, sq, n))
            want = [F(1), F(2), F(1)]
            for _ in range(n - 2):
                want = _pmul(want, [F(-1), F(1)])
            assert cp == want                                   # -1 twice, +1 otherwise
        # a commuting product of two quarter-turn exponentials: -1 four times
        i, j = planes[0]
        rest = [(a, b) for a, b in planes if len({a, b, i, j}) == 4]
        if rest:
            a, b = rest[0]
            R = GA.mul(GA.mul(GA.gen(i), GA.gen(j), sq), GA.mul(GA.gen(a), GA.gen(b), sq), sq)
            cp = _charpoly(_ad_matrix(R, sq, n))
            assert _peval(cp, F(-1)) == 0
            mult = 0
            c = cp
            while _peval(c, F(-1)) == 0:
                mult += 1
                c = [sum(c[k + 1 + m] * (-1) ** m for m in range(len(c) - k - 1)) for k in range(len(c) - 1)]
            assert mult == 4
    return True


def check_low_dimensions():
    premise("std-algebra.bivector-exponential")
    for p, q in [(1, 0), (0, 1)]:
        sq = GA.sig(p, q)
        e = GA.gen(0)
        R = GA.mul(e, GA.scal(-sq[0], e), sq)
        assert GA.eq(R, GA.sc(-1))
        assert GA.eq(GA.mul(e, GA.neg(e), sq), GA.sc(-sq[0]))       # e(-e) = -Q(e): +1 in Cl(0,1)
        m1 = GA.sc(-1)
        assert GA.eq(GA.mul(m1, GA.reverse(m1), sq), GA.sc(1))
        assert [b for b in GA.all_blades(1) if len(b) == 2] == []
    sq = GA.sig(1, 1)
    E = GA.mul(GA.gen(0), GA.gen(1), sq)
    assert GA.eq(GA.mul(E, E, sq), GA.sc(1)) and GA.eq(GA.reverse(E), GA.neg(E))
    m1 = GA.mul(GA.gen(0), GA.neg(GA.gen(0)), sq)
    assert GA.eq(m1, GA.sc(-1)) and GA.eq(GA.mul(m1, GA.reverse(m1), sq), GA.sc(1))
    for c, s in [(F(5, 4), F(3, 4)), (F(5, 3), F(-4, 3)), (F(13, 12), F(5, 12)), (F(1), F(0))]:
        assert c * c - s * s == 1 and c >= 1
        R = GA.add(GA.sc(c), GA.scal(s, E))
        assert GA.eq(GA.mul(R, GA.reverse(R), sq), GA.sc(1)) and not GA.eq(R, m1)
        mR = GA.neg(R)
        assert GA.eq(GA.mul(mR, GA.reverse(mR), sq), GA.sc(1)) and mR.get((), F(0)) <= -1
    return True
