"""synthesis.einstein-route-makes-n-initial-data: exact checks.

(1) For g = sigma^{-2} eta with sigma = 1 - Lambda Q(x)/12 on the flat chart (signature (1,3)), the Ricci
tensor in the positive-sphere convention, Ric_ab = 2 sigma^{-1} d_a d_b sigma + eta_ab (sigma^{-1} box sigma
- 3 sigma^{-2} |d sigma|^2), equals -Lambda g_ab at rational points, for two values of Lambda: both metrics
solve the vacuum equations of the Einstein route, Ric - (1/2) R g - Lambda g = 0 in signature (1,3), each
with its own constant. (2) N^2 = 3 M_P^2 / Lambda takes two values on that solution set, so N is not
constant on it. (3) For (ii), an instance only: on each de Sitter member the Lambda read off the metric is one
constant at the sample points; the promoted equations themselves, the set equality of the solution spaces, tau
and the Liouville density are not computed. (4) If N is not constant and v/H is constant, v/M_P = (v/H)/N is not
constant.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

ETA = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
R4 = range(4)


def Q(x):
    return sum((ETA[a][a] * x[a] * x[a] for a in R4), F(0))


def ricci_desitter(L, x):
    """Ric (positive-sphere convention) and g of sigma^{-2} eta, sigma = 1 - L Q/12, at the point x."""
    s = 1 - L * Q(x) / 12
    # d_a sigma = -(L/6) eta_ab x^b ; d_a d_b sigma = -(L/6) eta_ab ; box sigma = eta^{ab} d_a d_b sigma = -4 L/6
    ds = [-(L / 6) * ETA[a][a] * x[a] for a in R4]
    dds = [[-(L / 6) * ETA[a][b] for b in R4] for a in R4]
    box = sum((ETA[a][a] * dds[a][a] for a in R4), F(0))
    grad2 = sum((ETA[a][a] * ds[a] * ds[a] for a in R4), F(0))
    ric = [[2 * dds[a][b] / s + ETA[a][b] * (box / s - 3 * grad2 / (s * s)) for b in R4] for a in R4]
    g = [[ETA[a][b] / (s * s) for b in R4] for a in R4]
    return ric, g


POINTS = [[F(1, 3), F(1, 2), F(0), F(-1, 5)], [F(2, 7), F(-1, 4), F(1, 6), F(1, 9)], [F(0), F(0), F(0), F(0)]]


def check_de_sitter_family_solves_route_equations():
    premise("mass.de-sitter-scale-frozen-point")
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    # the sample points are pinned: Q and sigma at the first two points (Lambda = 3)
    GA.check("Q at the sample points", Q(POINTS[0]) == F(-161, 900) and Q(POINTS[1]) == F(-1333, 63504))
    GA.check("g_00 at the first point, Lambda = 3", ricci_desitter(F(3), POINTS[0])[1][0][0] == F(3600, 3761) ** 2)
    for L in (F(3), F(12)):
        for x in POINTS:
            ric, g = ricci_desitter(L, x)
            GA.check("Ric = -Lambda g at Lambda = %s" % L, all(ric[a][b] == -L * g[a][b] for a in R4 for b in R4))
            ginv = [[1 / g[a][b] if a == b else F(0) for b in R4] for a in R4]
            R = sum((ginv[a][a] * ric[a][a] for a in R4), F(0))
            GA.check("vacuum equation Ric - R g/2 - Lambda g = 0 (signature (1,3))",
                     all(ric[a][b] - R * g[a][b] / 2 - L * g[a][b] == 0 for a in R4 for b in R4))
            # control: the other member's constant does not solve this metric's equation
            L2 = F(15) - L
            GA.check("control: wrong constant fails",
                     any(ric[a][b] - R * g[a][b] / 2 - L2 * g[a][b] != 0 for a in R4 for b in R4))
    return True


def check_n_not_constant_on_route_solutions():
    premise("dark-energy.under-action-written-norm-parameter-laws")
    premise("synthesis.smallness-monomials-exact-hierarchy-casimir")
    MP2 = F(1)                       # units M_P = 1
    N2 = {L: 3 * MP2 / L for L in (F(3), F(12))}
    GA.check("N^2 = 3/Lambda takes two values: 1 and 1/4", N2[F(3)] == 1 and N2[F(12)] == F(1, 4))
    # along one solution Lambda is constant (the route's Bianchi step), so N is conserved; across the
    # solution set it is not constant: (I) in the Definition, read with the route's equations as the laws
    GA.check("not constant on the union", N2[F(3)] != N2[F(12)])
    # under the action as written the two metrics lie in different S_mu, mu = Lambda: N is constant on each
    # action as written: S_mu = {g_mu}, so N^2 = 3/mu on S_mu; the two members lie in different S_mu
    GA.check("action as written: N^2 on S_mu is 3/mu", all(N2[m] == 3 / m for m in N2) and N2[F(3)] * 4 == N2[F(12)] * 16)
    return True


def check_de_sitter_lambda_constant_instance():
    premise("synthesis.promoted-norm-one-global-pair")
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    # Instance for (ii) only: the promoted equations (Einstein with Lambda a field, d Lambda = 0) are not solved
    # here. On each of the two de Sitter members the Lambda read off the metric, -Ric_11 / g_11, is one constant
    # across the sample points, as d Lambda = 0 requires of a promoted solution's metric part.
    for L in (F(3), F(12)):
        vals = set()
        for x in POINTS:
            ric, g = ricci_desitter(L, x)
            vals.add(-ric[1][1] / g[1][1])
        GA.check("Lambda read off the de Sitter metric is one constant at the sample points", vals == {L})
    return True


def check_rung_ratio_register():
    premise("synthesis.smallness-monomials-exact-hierarchy-casimir")
    # if v/H is the same number c on every solution and N takes the values N1 != N2, then v/M_P = c/N takes
    # two values; and if v/M_P is the same on every solution, v/H = (v/M_P) N takes two values
    c = F(7, 2)
    N = [F(1), F(2)]
    vMP = [c / n for n in N]
    GA.check("v/H constant forces v/M_P to vary", vMP[0] != vMP[1])
    d = F(5, 3)
    vH = [d * n for n in N]
    GA.check("v/M_P constant forces v/H to vary", vH[0] != vH[1])
    # G v^2 N^2 = (v/H)^2 in units G = M_P^{-2}
    GA.check("G v^2 N^2 = (v/H)^2", all((vMP[i] ** 2) * N[i] ** 2 == c ** 2 for i in range(2)))
    return True
