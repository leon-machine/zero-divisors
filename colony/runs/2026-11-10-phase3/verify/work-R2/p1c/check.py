"""synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball: exact checks.

Numbers of Q(pi) are rational functions GA.RF in one variable standing for pi (pi is transcendental, so two such
functions are equal as reals exactly when they are equal as rational functions). Decimal comparisons use the
rational bounds PI_LO < pi < PI_HI. Ball volumes V_D come from V_0 = 1, V_1 = 2, V_D = (2 pi / D) V_(D-2); sphere
measures |S^n| from |S^0| = 2, |S^1| = 2 pi, |S^n| = (2 pi / (n-1)) |S^(n-2)|: two separate recursions.

A filling is, per populated tower, a quantum mass and a number of quanta per unit volume of the tower's own space
(space dimension D = 2, 3 or 4), in one unit of length d. The stored sourcing reads a tower's mass density per unit
of this world's three-volume through a length lam * d of each extra direction (D = 4) or with sheets mu * d apart
(D = 2); the stored premise R3 is lam = mu = 1.

(1) Shares and total from an arbitrary filling; R1 and R2 give V_3/V_D and (11 pi + 16)/(3 pi). Rescaling the mass
    of each tower by its own factor and the number density by the inverse factor breaks R1 and R2 and keeps every
    share; rescaling the mass alone moves the total.
(2) The sphere law (equal mass per unit sphere of the tower's Euclidean spacetime, dimension D + 1) gives the same
    shares, by |S^(D+1)| = 2 pi V_D from the two recursions (D = 0 to 8). The total mass of a tower on its sphere of
    radius ell, filled at one quantum per ball of radius d, is proportional to (ell/d)^(D+1): equal across the three
    dimensions only at ell = d.
(3) The mirror term: 1 from the density law at D = 3; 199/200 on the burning branch of the stored mirror share; the
    two totals differ by 1/200 and both lie within one standard deviation of the record's ratio.
(4) Each remaining premise moves the total: thickness (2, 1) and (1, 2); cubic cells of side two units give exactly
    5, more than five standard deviations below the record; a tower moved from D = 2 to D = 4 changes it.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI = GA.RF.var()
C = GA.RF.const
PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)
OBS = F(1200, 10000) / F(2237, 100000)        # Omega_c h^2 / Omega_b h^2 of the stored comparison
SIG = F(65, 1000)
ODD_DIMS = [2, 2, 4, 4]                        # residues 1, 7, 3, 5 under the stored representatives
MIRROR_DIM = 3
OUR_DIM = 3


def ball(D):
    V = {0: C(1), 1: C(2)}
    for n in range(2, D + 1):
        V[n] = C(F(2, n)) * PI * V[n - 2]
    return V[D]


def sphere(n):
    S = {0: C(2), 1: C(2) * PI}
    for k in range(2, n + 1):
        S[k] = C(F(2, k)) * PI * S[k - 2]
    return S[n]


def between(x):
    """rational lower and upper bounds of a rational function of pi that is monotone data: evaluate at both ends"""
    a, b = x.eval(PI_LO), x.eval(PI_HI)
    return min(a, b), max(a, b)


def share(D, mass, number, our_mass, our_number, lam=F(1), mu=F(1)):
    """mass density per unit of our three-volume over ours, for a tower of space dimension D"""
    rho = C(mass) * number
    if D == 4:
        rho = rho * C(lam)
    elif D == 2:
        rho = rho / C(mu)
    return rho / (C(our_mass) * our_number)


def total(filling, lam=F(1), mu=F(1)):
    """filling: dict tower -> (D, mass, number density); tower 'us' is this world"""
    _, m0, n0 = filling["us"]
    t = C(0)
    for name, (D, m, n) in filling.items():
        if name != "us":
            t = t + share(D, m, n, m0, n0, lam, mu)
    return t


def unit_ball_filling(scale=None, mass=F(1)):
    """R1 and R2: mass m, one quantum per unit ball; optional per-tower factor s: mass s m, number 1/(s V_D)"""
    towers = {"us": OUR_DIM, "mirror": MIRROR_DIM, "r1": 2, "r7": 2, "r3": 4, "r5": 4}
    out = {}
    for name, D in towers.items():
        s = F(1) if scale is None else scale[name]
        out[name] = (D, mass * s, C(1) / (C(s) * ball(D)))
    return out


CLOSED = (C(11) * PI + C(16)) / (C(3) * PI)


def check_total_depends_on_mass_times_number_only():
    premise("dark-matter.unit-ball-rule")
    premise("dark-matter.projection-every-towers-content-dilutes-ones")
    base = unit_ball_filling()
    GA.check("R1 and R2 give the stored closed form", total(base).eqrf(CLOSED))
    _, m0, n0 = base["us"]
    GA.check("share 4/3 at D = 2", share(2, *base["r1"][1:], m0, n0).eqrf(C(F(4, 3))))
    GA.check("share 8/(3 pi) at D = 4", share(4, *base["r3"][1:], m0, n0).eqrf(C(F(8, 3)) / PI))
    scales = [
        ({"us": F(1), "mirror": F(1), "r1": F(3), "r7": F(1, 5), "r3": F(7, 2), "r5": F(11)},
         C(1) + C(F(64, 15)) + C(F(116, 3)) / PI),
        ({"us": F(2), "mirror": F(5, 3), "r1": F(1, 9), "r7": F(4), "r3": F(1), "r5": F(13, 7)},
         C(F(5, 6)) + C(F(74, 27)) + C(F(80, 21)) / PI),
    ]
    for sc, mass_only in scales:
        f = unit_ball_filling(scale=sc)
        masses = {v[1] for v in f.values()}
        GA.check("the rescaled filling breaks R1", len(masses) >= 5)
        GA.check("the rescaled filling breaks R2",
                 sum(1 for k in f if not (f[k][2] * ball(f[k][0])).eqrf(C(1))) >= 4)
        GA.check("mass per unit ball is common", all((C(f[k][1]) * f[k][2] * ball(f[k][0])).eqrf(C(1)) for k in f))
        GA.check("every share is kept", total(f).eqrf(CLOSED))
        # mass rescaled without the compensating number density: the total moves, to the value computed by hand
        g = {k: (f[k][0], f[k][1], base[k][2]) for k in f}
        GA.check("mass alone moves the total", total(g).eqrf(mass_only) and not mass_only.eqrf(CLOSED))
    return True


def check_sphere_law_is_the_ball_law_and_fixes_the_unit():
    premise("dark-matter.democracy-de-sitter-radius-unit-ball")
    for D in range(0, 9):
        GA.check("hat-box at D = %d" % D, sphere(D + 1).eqrf(C(2) * PI * ball(D)))
    for D in (2, 3, 4):
        GA.check("sphere share equals ball share at D = %d" % D,
                 (sphere(4) / sphere(D + 1)).eqrf(ball(3) / ball(D)))
    GA.check("sphere measures 2 pi^2, 8 pi^2/3, pi^3",
             sphere(3).eqrf(C(2) * PI * PI) and sphere(4).eqrf(C(F(8, 3)) * PI * PI)
             and sphere(5).eqrf(PI * PI * PI))

    def sphere_mass(D, ell, d):
        # one quantum of unit mass per ball of radius d, read per unit (D+1)-measure with the factor 1/(2 pi d),
        # integrated over the sphere of radius ell
        dens = C(1) / (ball(D) * C(d ** D)) / (C(2) * PI * C(d))
        return dens * sphere(D + 1) * C(ell ** (D + 1))

    for ell, d in [(F(1), F(1)), (F(7, 3), F(7, 3))]:
        ms = [sphere_mass(D, ell, d) for D in (2, 3, 4)]
        GA.check("equal total masses at ell = d", ms[0].eqrf(ms[1]) and ms[1].eqrf(ms[2]))
    for ell, d in [(F(2), F(1)), (F(1), F(3)), (F(5, 4), F(1))]:
        ms = [sphere_mass(D, ell, d) for D in (2, 3, 4)]
        r = ell / d
        GA.check("total masses in ratio (ell/d)^(D+1)",
                 ms[0].eqrf(C(r ** 3)) and ms[1].eqrf(C(r ** 4)) and ms[2].eqrf(C(r ** 5)))
        GA.check("democracy of the total mass fails at ell != d", not ms[0].eqrf(ms[1]))
        # the shares do not see the unit: the filling at radius d has the same total
    return True


def check_mirror_term_is_obtained_twice():
    premise("dark-matter.population-count-one-share-half-percent")
    premise("dark-matter.mirror-share-one-how-fragile")
    premise("dark-matter.unit-ball-rule")
    base = unit_ball_filling()
    _, m0, n0 = base["us"]
    GA.check("the density law gives the mirror share one", share(3, *base["mirror"][1:], m0, n0).eqrf(C(1)))
    burning = F(199, 200)                       # stored mean mass per baryon ratio on the burning branch
    f = dict(base)
    f["mirror"] = (3, base["mirror"][1] * burning, base["mirror"][2])
    t_burn = total(f)
    GA.check("the two totals differ by 1/200", (CLOSED - t_burn).eqrf(C(F(1, 200))))
    for t in (CLOSED, t_burn):
        lo, hi = between(t)
        GA.check("within one standard deviation of the record", OBS - SIG < lo and hi < OBS + SIG)
    lo, hi = between(CLOSED)
    GA.check("closed form in (5.36431, 5.36433)", F(536431, 100000) < lo and hi < F(536433, 100000))
    return True


def check_each_remaining_premise_moves_the_total():
    premise("dark-matter.total-function-thickness")
    base = unit_ball_filling()
    t21 = total(base, lam=F(2), mu=F(1))
    t12 = total(base, lam=F(1), mu=F(2))
    GA.check("thickness (2, 1)", t21.eqrf(C(F(11, 3)) + C(F(32, 3)) / PI))
    GA.check("thickness (1, 2)", t12.eqrf(C(F(7, 3)) + C(F(16, 3)) / PI))
    GA.check("both differ from the closed form", not t21.eqrf(CLOSED) and not t12.eqrf(CLOSED))
    lo, hi = between(t21)
    GA.check("thickness (2, 1) is far above the record", lo > OBS + 5 * SIG)
    lo, hi = between(t12)
    GA.check("thickness (1, 2) is far below the record", hi < OBS - 5 * SIG)
    # cubic cells of side 2 (the cube circumscribing the unit ball), thickness one cell side
    towers = {"us": 3, "mirror": 3, "r1": 2, "r7": 2, "r3": 4, "r5": 4}
    cubes = {k: (D, F(1), C(F(1, 2 ** D))) for k, D in towers.items()}
    t_cube = total(cubes, lam=F(2), mu=F(2))
    GA.check("cubic cells give exactly 5", t_cube.eqrf(C(5)))
    GA.check("5 is more than five standard deviations below", F(5) < OBS - 5 * SIG)
    # one three-dimensional tower read at space dimension 4 instead of 2 (a change of representative)
    moved = dict(base)
    moved["r1"] = (4, base["r3"][1], base["r3"][2])
    t_moved = total(moved)
    GA.check("a changed representative moves the total",
             t_moved.eqrf(C(F(7, 3)) + C(8) / PI) and not t_moved.eqrf(CLOSED))
    return True
