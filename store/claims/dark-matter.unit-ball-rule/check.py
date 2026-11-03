"""dark-matter.unit-ball-rule: exact checks.

Numbers of Q(pi) are held as Laurent polynomials in pi with rational coefficients, {k: c} for
sum c pi^k; pi is transcendental, so equal polynomials are equal reals and unequal ones are not.
Decimal comparisons use the rational bounds PI_LO < pi < PI_HI. The unit-ball volumes come from
the recursion V_0 = 1, V_1 = 2, V_D = (2 pi / D) V_(D-2), not from typed values.

Checked:
(1) Under R1 and R2 the density of a tower of space dimension D is m/V_D per unit D-volume; under
    R3 it is read per unit of our three-volume through one unit cell of each unshared direction
    (factor 1^(D-3)), so the share is f = V_3/V_D, with m cancelling (two sample masses): the
    shares are 4/3 at D = 2, 1 at D = 3 and 8/(3 pi) at D = 4.
(2) The dark towers are the five populated residues other than this world's 6, with the census'
    representatives (2,1), (1,2), (4,1), (1,4) and (3,1): residues 1, 7, 3, 5, 2, all causal, of
    space dimensions D = p + q - 1 equal to 2, 2, 4, 4, 3.
(3) The sum V_3 * sum_r 1/V_(D_r) = 1 + 8/3 + 16/(3 pi) = (11 pi + 16)/(3 pi), as an identity in
    pi, lies in (5.36431, 5.36433) and within one sigma (0.065) of 0.1200/0.02237.
Not checked: the sentence that the agreement is a fit is a statement about how the relation was
found, with no computable content.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)
OBS = F(1200, 10000) / F(2237, 100000)        # Planck 2018 Omega_c h^2 / Omega_b h^2
SIG = F(65, 1000)
MASSES = [F(1), F(938, 7)]                    # two sample quantum masses (R1: m cancels)
# the census' representatives of the dark residues (Proposition (ii) of the residue census)
DARK_REPS = [(2, 1), (1, 2), (4, 1), (1, 4), (3, 1)]


def lp(c, k=0):
    return {k: F(c)} if c != 0 else {}


def ladd(*xs):
    out = {}
    for x in xs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def lmul(a, b):
    out = {}
    for k1, c1 in a.items():
        for k2, c2 in b.items():
            out[k1 + k2] = out.get(k1 + k2, F(0)) + c1 * c2
    return {k: c for k, c in out.items() if c != 0}


def linv(a):
    """inverse of a monomial c pi^k"""
    assert len(a) == 1
    (k, c), = a.items()
    return {-k: 1 / c}


def bounds(x):
    lo = hi = F(0)
    for k, c in x.items():
        u, v = c * PI_LO ** k, c * PI_HI ** k
        lo += min(u, v)
        hi += max(u, v)
    return lo, hi


def ball(D):
    V = {0: lp(1), 1: lp(2)}
    for n in range(2, D + 1):
        V[n] = lmul(lp(F(2, n), 1), V[n - 2])
    return V[D]


def share(D, m):
    """our-three-volume density of a tower of space dimension D over ours"""
    rho = lmul(lp(m), linv(ball(D)))            # R1, R2: m per unit ball
    rho = lmul(rho, lp(F(1) ** (D - 3)))         # R3: one unit cell per unshared direction
    rho_us = lmul(lp(m), linv(ball(3)))
    return lmul(rho, linv(rho_us))


def check_shares():
    premise("dark-matter.r1-equal-mass-per-quantum")
    premise("dark-matter.r2-one-quantum-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    assert ball(2) == {1: F(1)} and ball(3) == {1: F(4, 3)} and ball(4) == {2: F(1, 2)}
    for m in MASSES:
        assert share(2, m) == {0: F(4, 3)}
        assert share(3, m) == {0: F(1)}
        assert share(4, m) == {-1: F(8, 3)}
    return True


def check_dark_towers_and_dimensions():
    premise("dark-matter.towers-are-residues-single-clock-filter")
    residues = sorted((p - q) % 8 for p, q in DARK_REPS)
    assert residues == [1, 2, 3, 5, 7]
    assert 6 not in residues and 0 not in residues and 4 not in residues
    assert all(min(p, q) == 1 for p, q in DARK_REPS)
    dims = [p + q - 1 for p, q in DARK_REPS]
    assert dims.count(2) == 2 and dims.count(4) == 2 and dims.count(3) == 1
    return True


def check_total():
    premise("dark-matter.r1-equal-mass-per-quantum")
    premise("dark-matter.r2-one-quantum-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    premise("dark-matter.towers-are-residues-single-clock-filter")
    total = ladd(*[share(p + q - 1, MASSES[1]) for p, q in DARK_REPS])
    # (11 pi + 16)/(3 pi) = 11/3 + (16/3) pi^-1
    assert total == {0: F(11, 3), -1: F(16, 3)}
    assert total == ladd(lp(1), lp(F(8, 3)), lp(F(16, 3), -1))
    lo, hi = bounds(total)
    assert F(536431, 100000) < lo and hi < F(536433, 100000)
    assert max(abs(lo - OBS), abs(hi - OBS)) < SIG
    return True
