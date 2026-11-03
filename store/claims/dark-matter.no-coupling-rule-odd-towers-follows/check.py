"""dark-matter.no-coupling-rule-odd-towers-follows: exact checks of the computable reasons.

(a) Under g -> lambda^2 g the Yang-Mills density sqrt|det g| g^(mu alpha) g^(nu beta) F_(mu nu)
    F_(alpha beta) is computed exactly for a sample field strength in d = 3, 4, 5, 6 (diagonal
    metric of one time and d - 1 space directions, sqrt taken of a perfect rational square) and two
    values of lambda: it scales as lambda^(d-4), so 1/g^2 must carry length^(4-d), [g^2] =
    mass^(4-d): dimensionless exactly at d = 4, so comparing an odd tower's coupling with ours
    needs a length.
(c) The reversal orbit of this world's (1,3) is {(1,3), (3,1)}, residues {6, 2}; the odd towers'
    representatives (2,1), (1,2), (4,1), (1,4) have residues 1, 7, 3, 5, none on that orbit, and
    their generating subspaces (dimension 3 or 5, signatures by congruence of the Gram matrix)
    are not isometric to this world's (dimension 4, signature (1,3)), so no soldered isomorphism
    joins them.
(b) is a statement about the record and the series (no coupling value derived) and is not computed.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

LAMBDAS = [F(2), F(3, 2)]
# a sample antisymmetric field strength (upper-left block used in each dimension)
F_SAMPLE = [[0, 1, -2, 3, 1, 2],
            [-1, 0, 4, -1, 2, 1],
            [2, -4, 0, 5, -3, 1],
            [-3, 1, -5, 0, 2, -2],
            [-1, -2, 3, -2, 0, 7],
            [-2, -1, -1, 2, -7, 0]]
ODD_REPS = [(2, 1), (1, 2), (4, 1), (1, 4)]
THIS_WORLD = (1, 3)


def isqrt(n):
    if n < 2:
        return n
    x, y = n, (n + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def qsqrt(q):
    """exact square root of a rational perfect square"""
    a, b = isqrt(q.numerator), isqrt(q.denominator)
    assert a * a == q.numerator and b * b == q.denominator
    return F(a, b)


def density(d, lam):
    g = [F(lam * lam) * (1 if i == 0 else -1) for i in range(d)]      # diagonal metric
    ginv = [1 / x for x in g]
    det = F(1)
    for x in g:
        det *= x
    vol = qsqrt(abs(det))
    s = F(0)
    for m in range(d):
        for n in range(d):
            s += ginv[m] * ginv[n] * F_SAMPLE[m][n] * F_SAMPLE[m][n]
    return vol * s


def check_coupling_is_dimensionful_off_four():
    for d in (3, 4, 5, 6):
        base = density(d, F(1))
        assert base != 0
        for lam in LAMBDAS:
            assert density(d, lam) == base * lam ** (d - 4)
    dims = {d: 4 - d for d in (3, 4, 5, 6)}
    assert [d for d in dims if dims[d] == 0] == [4]
    assert dims[3] == 1 and dims[5] == -1
    return True


def gram_signature(p, q):
    sq = GA.sig(p, q)
    n = p + q
    G = [[GA.dot(GA.gen(i), GA.gen(j), sq) for j in range(n)] for i in range(n)]
    return GA.congruence_signature(G)


def check_odd_towers_off_the_reversal_orbit():
    premise("dark-matter.p2-indifference")
    premise("dark-matter.mirror-tower-copy-one")
    premise("dark-matter.residue-soldered-invariant-not-algebraic-one")
    p, q = THIS_WORLD
    orbit = {(p, q), (q, p)}
    orbit_res = sorted((a - b) % 8 for a, b in orbit)
    assert orbit_res == [2, 6]
    odd_res = sorted((a - b) % 8 for a, b in ODD_REPS)
    assert odd_res == [1, 3, 5, 7]
    assert not set(odd_res) & set(orbit_res)
    ours = gram_signature(p, q)
    assert ours == (1, 3, 0)
    for a, b in ODD_REPS:
        s = gram_signature(a, b)
        assert s[2] == 0 and s[0] + s[1] in (3, 5) and s != ours
    return True
