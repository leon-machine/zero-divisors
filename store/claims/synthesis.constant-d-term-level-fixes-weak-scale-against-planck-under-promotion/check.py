"""Exact checks: under the promoted reading, the stored D-term action with a constant level fixes the weak scale
against the Planck mass, not against the Hubble scale.

Orbit-space form of the stored D-term potential on the locus L (synthesis.rung-field-d-term-action-and-tree-
masses-on-the-lift-locus (1), (2)): V_D = (1/2)[(g^2/4)(N^2 - h^2) + g'^2 (m/2 - zeta)^2], h = H^2, xi = 2 zeta,
boundary N^2 - m^2 = h^2. Rung coordinates (alpha, beta) in C^2 + C^2 as Gaussian rationals (GA.QI) for the
cross-check of that form on the lift family c_lambda: alpha = (h/lambda, 0), beta = (-lambda, 0).
Units hbar = c = 1, G = M_P^{-2}, N_grav = M_P/H (synthesis.smallness-monomials-exact-hierarchy-casimir).
Exact throughout.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
g, gp = F(2, 3), F(1, 2)
MSTAR = F(12)
TRIPLES = ((F(5), F(13)), (F(9), F(15)), (F(16), F(20)), (F(35), F(37)))   # (h, N*) with N*^2 = 12^2 + h^2


def q(re, im=0):
    return QI(F(re), F(im))


def VD(Nv, mv_, h, zeta):
    return (g * g * (Nv * Nv - h * h) / 4 + gp * gp * (mv_ / 2 - zeta) ** 2) / 2


def VD_rung(c, h, zeta):
    """The stored potential from rung coordinates: (1/2)[g^2 sum mu_j^2 + g'^2 (mu_Y - zeta)^2] with
    sum mu_j^2 = (N^2 - |Q|^2)/4 and mu_Y = m/2 (stored (1)); here evaluated from alpha, beta directly."""
    a, b = c
    al2 = sum((z.re * z.re + z.im * z.im for z in a), F(0))
    be2 = sum((z.re * z.re + z.im * z.im for z in b), F(0))
    Qc = a[0] * b[0] + a[1] * b[1]
    Nv, mv_ = (al2 + be2) / 2, (al2 - be2) / 2
    return (g * g * (Nv * Nv - (Qc.re ** 2 + Qc.im ** 2)) / 4 + gp * gp * (mv_ / 2 - zeta) ** 2) / 2, Nv, mv_, Qc


def check_level_vacuum_moment_map_independent_of_h():
    """On the boundary N^2 - m^2 = h^2 the stored V_D is (1/2)[(g^2/4) m^2 + g'^2 (m/2 - zeta)^2], with no h;
    its minimum m* = g'^2 xi/(g^2 + g'^2) is the same for every h, checked at four h with N* rational."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    xi = MSTAR * (g * g + gp * gp) / (gp * gp)
    zeta = xi / 2
    GA.check("m* = g'^2 xi/(g^2 + g'^2)", gp * gp * xi / (g * g + gp * gp) == MSTAR)
    for lam, h in ((F(1), F(5)), (F(3), F(15)), (F(2), F(7))):
        c = ([q(h / lam), q(0)], [q(-lam), q(0)])
        V, Nv, mv_, Qc = VD_rung(c, h, zeta)
        GA.check("family point on L", Qc == q(-h))
        GA.check("orbit-space form of V_D", V == VD(Nv, mv_, h, zeta))
        GA.check("boundary has no h", V == (g * g * mv_ * mv_ / 4 + gp * gp * (mv_ / 2 - zeta) ** 2) / 2)
    vals = []
    for h, Nst in TRIPLES:
        GA.check("boundary point", Nst * Nst - MSTAR * MSTAR == h * h)
        V0 = VD(Nst, MSTAR, h, zeta)
        vals.append(V0)
        for dm in (F(1, 7), F(-1, 7), F(3), F(-3)):
            m1 = MSTAR + dm
            # the boundary value at m1 needs only N^2 = m1^2 + h^2
            V1 = (g * g * (m1 * m1) / 4 + gp * gp * (m1 / 2 - zeta) ** 2) / 2
            GA.check("V_D larger away from m*", V1 > V0)
            GA.check("excess is (g^2 + g'^2) dm^2 / 8", V1 - V0 == (g * g + gp * gp) * dm * dm / 8)
    GA.check("same vacuum value for every h", all(v == vals[0] for v in vals))
    return True


def check_ratio_fixed_by_the_laws():
    """With xi constant, N*/h = sqrt(1 + m*^2/h^2) takes four distinct values at four h (decreasing in h),
    while 0 <= N* - |m*| <= h^2/(2|m*|); with xi proportional to h (level proportional to Lambda) N*/h is
    the same at every h; G v^2 N^2 = (v/H)^2 is an identity when G = M_P^{-2} and N = M_P/H. The (h, N*) pairs
    are verified against m* computed from the level."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.einstein-route-makes-n-initial-data")
    premise("synthesis.smallness-monomials-exact-hierarchy-casimir")
    xi = MSTAR * (g * g + gp * gp) / (gp * gp)
    mstar = gp * gp * xi / (g * g + gp * gp)
    for h, Nst in TRIPLES:
        GA.check("triple is the boundary vacuum: N*^2 = m*^2 + h^2", Nst > 0 and Nst * Nst == mstar * mstar + h * h)
    ratios = [Nst / h for h, Nst in TRIPLES]
    GA.check("N*/h strictly decreasing in h", all(ratios[i] > ratios[i + 1] for i in range(3)))
    GA.check("N*/h values", ratios == [F(13, 5), F(5, 3), F(5, 4), F(37, 35)])
    for h, Nst in TRIPLES:
        GA.check("N* - m* bounded by h^2/(2 m*)", F(0) < Nst - mstar <= h * h / (2 * mstar))
    k = F(12, 5)
    for h, Nst in ((F(5), F(13)), (F(10), F(26)), (F(15, 2), F(39, 2))):
        GA.check("level proportional to h: boundary", Nst * Nst == (k * h) ** 2 + h * h)
        GA.check("level proportional to h: N*/h constant", Nst / h == F(13, 5))
    for MP, H in ((F(7), F(1, 3)), (F(11, 2), F(2, 5))):
        G = 1 / (MP * MP)
        Ng = MP / H
        GA.check("G Lambda = 3 N^-2", G * 3 * H * H == 3 / (Ng * Ng))
        for v in (F(1, 9), F(5), F(41, 3)):
            GA.check("G v^2 N^2 = (v/H)^2 for every v", G * v * v * Ng * Ng == (v / H) ** 2)
    return True
