"""dark-matter.unit-ball-rule: exact checks.

Numbers of Q(pi) are held as Laurent polynomials in pi with rational coefficients, {k: c} for
sum c pi^k; pi is transcendental, so equal polynomials are equal reals and unequal ones are not.
Decimal comparisons use the rational bounds PI_LO < pi < PI_HI. The unit-ball volumes come from
the recursion V_0 = 1, V_1 = 2, V_D = (2 pi / D) V_(D-2), not from typed values.

Checked:
(1) Under Premise E the mass density of a tower of space dimension D is mu/(V_D d^D) per unit
    D-volume; under R3 it is read per unit of our three-volume through one length d of each unshared
    direction (factor d^(D-3)), so the share is f = V_3/V_D, with mu and d cancelling (two sample
    masses, two sample lengths): the shares are 4/3 at D = 2, 1 at D = 3 and 8/(3 pi) at D = 4.
(2) The dark towers are the five populated residues other than this world's 6, with the census'
    representatives (2,1), (1,2), (4,1), (1,4) and (3,1): residues 1, 7, 3, 5, 2, all causal, of
    space dimensions D = p + q - 1 equal to 2, 2, 4, 4, 3.
(3) The sum V_3 * sum_r 1/V_(D_r) = 1 + 8/3 + 16/(3 pi) = (11 pi + 16)/(3 pi), as an identity in
    pi, lies in (5.36431, 5.36433) and within one sigma (0.065) of 0.1200/0.02237.
(4) (ii) Fillings whose quanta are heavier and rarer by a factor (different factors in the three-
    and five-dimensional towers) keep the mass per unit ball and have the same shares; R1 with R2
    in the length d gives mass per ball m on every tower.
(5) (iii) E at d with s = t = d gives the two shares; conversely s = t and the two shares give E at
    d = s; for any rho_2, rho_3 the length d = rho_2 V_2/(rho_3 V_3) = 3 rho_2/(4 rho_3) is the one
    solution and the three-dimensional share is then 4/3 identically; a five-dimensional density off
    the condition breaks E and moves the share; s different from t leaves no common length.
(6) (iv) at d' = 2d, 3d the ratio (d'/d)^D is different at D = 2, 3, 4.
Not checked: the sentence that the agreement is a fit is a statement about how the relation was
found, with no computable content.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)
OBS = F(1200, 10000) / F(2237, 100000)        # Planck 2018 Omega_c h^2 / Omega_b h^2
SIG = F(65, 1000)
MASSES = [F(1), F(938, 7)]                    # two sample masses per unit ball (E: mu cancels)
LENGTHS = [F(1), F(49, 50)]                   # two sample lengths d (it cancels)
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


def lmul(*xs):
    out = {0: F(1)}
    for b in xs:
        new = {}
        for k1, c1 in out.items():
            for k2, c2 in b.items():
                new[k1 + k2] = new.get(k1 + k2, F(0)) + c1 * c2
        out = {k: c for k, c in new.items() if c != 0}
    return out


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


def density(D, mu, d):
    """Premise E: mass per unit D-volume of a tower of space dimension D, mu/(V_D d^D)"""
    return lmul(lp(mu / d ** D), linv(ball(D)))


def share(D, mu, d=F(1), thick=None):
    """our-three-volume density of a tower of space dimension D over ours; thick is the counted
    length (R3: the length d of E), entering as thick^(D-3)"""
    thick = d if thick is None else thick
    rho = lmul(density(D, mu, d), lp(thick ** (D - 3)))
    return lmul(rho, linv(density(3, mu, d)))


def share_from(rho, rho3, D, length):
    """the sourcing rule on given densities: rho * length^(D-3) / rho3"""
    return lmul(rho, lp(length ** (D - 3)), linv(rho3))


def mass_per_ball(rho, D, d):
    return lmul(rho, ball(D), lp(d ** D))


def check_shares():
    premise("dark-matter.e-equal-mass-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    assert ball(2) == {1: F(1)} and ball(3) == {1: F(4, 3)} and ball(4) == {2: F(1, 2)}
    for mu in MASSES:
        for d in LENGTHS:
            assert share(2, mu, d) == {0: F(4, 3)}
            assert share(3, mu, d) == {0: F(1)}
            assert share(4, mu, d) == {-1: F(8, 3)}
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
    premise("dark-matter.e-equal-mass-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    premise("dark-matter.towers-are-residues-single-clock-filter")
    total = ladd(*[share(p + q - 1, MASSES[1], LENGTHS[1]) for p, q in DARK_REPS])
    # (11 pi + 16)/(3 pi) = 11/3 + (16/3) pi^-1
    assert total == {0: F(11, 3), -1: F(16, 3)}
    assert total == ladd(lp(1), lp(F(8, 3)), lp(F(16, 3), -1))
    lo, hi = bounds(total)
    assert F(536431, 100000) < lo and hi < F(536433, 100000)
    assert max(abs(lo - OBS), abs(hi - OBS)) < SIG
    return True


def check_quanta_do_not_enter():
    premise("dark-matter.e-equal-mass-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    m, d = F(938, 7), F(49, 50)
    # a filling: quanta of mass k m, number 1/(k V_D d^D) per unit volume; k = 1 is R1 with R2
    for k2, k4 in [(F(1), F(1)), (F(5), F(16)), (F(1, 3), F(7, 2))]:
        rho = {}
        for D, k in ((2, k2), (3, F(1)), (4, k4)):
            mass, number = k * m, lmul(lp(1 / (k * d ** D)), linv(ball(D)))
            rho[D] = lmul(lp(mass), number)
            assert mass_per_ball(rho[D], D, d) == {0: m}          # E holds, mu = m
            if k != 1:
                assert mass != m                                   # R1 fails
                assert lmul(number, ball(D), lp(d ** D)) != {0: F(1)}   # R2 fails
        assert share_from(rho[2], rho[3], 2, d) == {0: F(4, 3)}
        assert share_from(rho[4], rho[3], 4, d) == {-1: F(8, 3)}
    return True


def check_e_and_r3_are_the_closed_form():
    premise("dark-matter.e-equal-mass-per-unit-ball")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    f3, f5 = lmul(ball(3), linv(ball(2))), lmul(ball(3), linv(ball(4)))
    assert f3 == {0: F(4, 3)} and f5 == {-1: F(8, 3)}
    # E at d and s = t = d give the shares
    for mu in MASSES:
        for d in LENGTHS:
            r2, r3, r4 = density(2, mu, d), density(3, mu, d), density(4, mu, d)
            assert share_from(r2, r3, 2, d) == f3 and share_from(r4, r3, 4, d) == f5
    # conversely: s = t and the two shares give E at d = s
    for s, rho3 in [(F(1), lp(F(3, 7), -1)), (F(49, 50), lp(F(11, 2), -1)), (F(5, 3), lp(F(2), -1))]:
        r2 = lmul(f3, lp(s), rho3)
        r4 = lmul(f5, rho3, lp(1 / s))
        mu = mass_per_ball(rho3, 3, s)
        assert mass_per_ball(r2, 2, s) == mu and mass_per_ball(r4, 4, s) == mu
        # the three-dimensional share holds by the definition of the length
        dd = lmul(r2, ball(2), linv(lmul(rho3, ball(3))))
        assert dd == {0: s}
    for rho2, rho3q in [(F(1), F(1)), (F(7, 5), F(2, 9)), (F(1, 100), F(31))]:
        d = F(3) * rho2 / (F(4) * rho3q)                  # rho_2 V_2/(rho_3 V_3), V_2 = pi, V_3 = 4 pi/3
        assert lmul(lp(rho2), ball(2), lp(d ** 2)) == lmul(lp(rho3q), ball(3), lp(d ** 3))
        for other in (d / 2, 2 * d, d + 1):
            assert lmul(lp(rho2), ball(2), lp(other ** 2)) != lmul(lp(rho3q), ball(3), lp(other ** 3))
        assert share_from(lp(rho2), lp(rho3q), 2, d) == {0: F(4, 3)}
        # E for the five-dimensional towers is one condition, and it is the share
        r4_on = lmul(lp(rho3q), ball(3), linv(lmul(ball(4), lp(d))))
        assert mass_per_ball(r4_on, 4, d) == mass_per_ball(lp(rho3q), 3, d)
        assert share_from(r4_on, lp(rho3q), 4, d) == f5
        r4_off = lmul(r4_on, lp(F(9, 10)))
        assert mass_per_ball(r4_off, 4, d) != mass_per_ball(lp(rho3q), 3, d)
        assert share_from(r4_off, lp(rho3q), 4, d) == lmul(f5, lp(F(9, 10)))
    # s different from t: the sheets and the five-dimensional towers ask for different lengths
    s, t, rho3 = F(1), F(2), lp(F(1), -1)
    r2, r4 = lmul(f3, lp(s), rho3), lmul(f5, rho3, lp(1 / t))
    d_sheets = lmul(r2, ball(2), linv(lmul(rho3, ball(3))))
    d_five = lmul(rho3, ball(3), linv(lmul(r4, ball(4))))
    assert d_sheets == {0: s} and d_five == {0: t} and d_sheets != d_five
    return True


def check_one_length_only():
    premise("dark-matter.e-equal-mass-per-unit-ball")
    for mu in MASSES:
        for d in LENGTHS:
            for k in (F(2), F(3), F(1, 2)):
                ratios = [lmul(mass_per_ball(density(D, mu, d), D, k * d), linv(lp(mu))) for D in (2, 3, 4)]
                assert ratios == [{0: k ** 2}, {0: k ** 3}, {0: k ** 4}]
                assert len({tuple(sorted(r.items())) for r in ratios}) == 3
    return True
