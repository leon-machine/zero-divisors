"""sheaf.edge-wall: exact checks, as rational-function identities on the Kasner parametrisation
p(u) = (-u, 1+u, u(1+u))/(1+u+u^2) and the witness curve q(v) = (-v, v(1+v), 1+v)/(1+v+v^2).

(1) p(1/u) = (p1, p3, p2)(u) identically; p2 - p3 = (1 + u)(1 - u)/(1 + u + u^2), so for u > 0 the positive pair
collides only at the fixed point u = 1, the Schwarzschild triple (-1/3, 2/3, 2/3), on the census list.
(2) q satisfies both constraints identically; q(0) = (0,0,1) (Taub); axis 1 is negative for v in {1/4, 1/2, 3/4}
and axis 2 for v in {-1/8, -1/4, -2/5}; q1 q2 (1+v+v^2)^2 = -v^2 (1+v); q(1/2) = p(2) and q(-1/4) = p(3) with axes
1, 2 exchanged. The census premise: a vanishing exponent forces the Taub triple.
(3) The dying order d = -2 p1 = 2u/(1+u+u^2) obeys d(1) - d(u) = 2(u-1)^2/(3(1+u+u^2)), maximum 2/3 at u = 1,
d(1/w) -> 0 at w = 0 and -2 q1 -> 0 at v = 0 (zero at the edge); Schwarzschild consistency: with
tau = int_0^x 2 y^2 (1 - y^2)^(-1/2) dy (x = sqrt r, m = 1), tau^2 = (4/9) x^6 + (4/15) x^8 + ..., so
rho^3 = tau^2 is exactly third order in r, i.e. rho is first order in r.
(4) On Z the weighted Gram diag(1, -c1, -c2, -c3) (two unit choices) has signature (1,3), corank 0, while each
chamber's boundary Gram has corank 1: the radical line has rank 1 on chambers and 0 on Z; the Clifford sheaf keeps
rank 16 at all three (blade symbols of rank 16, the local-freeness premise).
(5) The v < 0 chamber at q(-1/4) = (4/13, -3/13, 12/13): weights (0, q1, 0, q3), Gram diag(1, -1, -rho', -1),
rho' = tau^(-2 q2), corank one with radical on axis 2; mu nu = -1/2 on axis 2 gives det h = 1 + rho' and signature
(2,4) at E and samples; the weight-forcing solves give (0, q1, 0, q3) and (0, q1, q2, q3) (the variable-weight
premise, relabelled).
(6) Both chamber weight assignments are (0,0,0,1) at the Taub point; the transition diag(tau^q1, tau^(-q2)) has
both exponents negative at v = 1/4, 1/2, 3/4 and both positive at v = -1/8, -1/4, -2/5 (so its inverse has both
negative there), and as rational
functions: q1 (-q2) (1+v+v^2)^2 = v^2 (1+v) and q1 - q2 = -v(2+v)/(1+v+v^2); a unit over A on neither side.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

V = GA.RF.var()
DV = GA.RF1 + V + V * V
Q = (-V / DV, V * (GA.RF1 + V) / DV, (GA.RF1 + V) / DV)


V_POS = (F(1, 4), F(1, 2), F(3, 4))          # samples on the v > 0 chamber
V_NEG = (F(-1, 8), F(-1, 4), F(-2, 5))        # samples on the -1 < v < 0 chamber
W_SAMPLES = (F(0), F(1, 3), F(1, 2), F(1))


def C(x):
    return GA.RF.const(F(x))


def kasner(u):
    u = F(u)
    D = 1 + u + u * u
    return (-u / D, (1 + u) / D, u * (1 + u) / D)


def qpt(v):
    return tuple(c.eval(F(v)) for c in Q)


def check_positive_pair_collision_is_exchange_fixed_point():
    premise("sheaf.collision-census")
    ok = True
    u = GA.RF.var()
    D = GA.RF1 + u + u * u
    p = (-u / D, (GA.RF1 + u) / D, u * (GA.RF1 + u) / D)
    iu = GA.RF1 / u
    Di = GA.RF1 + iu + iu * iu
    pi = (-iu / Di, (GA.RF1 + iu) / Di, iu * (GA.RF1 + iu) / Di)
    ok = ok and pi[0].eqrf(p[0]) and pi[1].eqrf(p[2]) and pi[2].eqrf(p[1])
    ok = ok and (p[1] - p[2]).eqrf((GA.RF1 + u) * (GA.RF1 - u) / D)
    zeros = [x for x in (F(1, 3), F(1, 2), F(1), F(2), F(5)) if (p[1] - p[2]).eval(x) == 0]
    ok = ok and zeros == [F(1)] and kasner(1) == (F(-1, 3), F(2, 3), F(2, 3))
    GA.check("p(1/u) = (p1, p3, p2)(u): the positive pair collides only at the fixed point u = 1 (Schwarzschild)", ok)
    return ok


def check_ordering_change_forces_taub_edge():
    premise("sheaf.collision-census")
    ok = True
    ok = ok and (Q[0] + Q[1] + Q[2]).eqrf(GA.RF1)
    ok = ok and (Q[0] * Q[0] + Q[1] * Q[1] + Q[2] * Q[2]).eqrf(GA.RF1)
    ok = ok and qpt(0) == (0, 0, 1)
    for v in V_POS:
        q = qpt(v)
        ok = ok and q[0] < 0 < q[1]
    for v in V_NEG:
        q = qpt(v)
        ok = ok and q[1] < 0 < q[0]
    ok = ok and (Q[0] * Q[1] * DV * DV).eqrf(-(V * V * (GA.RF1 + V)))
    ok = ok and qpt(F(1, 2)) == kasner(2) == (F(-2, 7), F(3, 7), F(6, 7))
    p3 = kasner(3)
    ok = ok and qpt(F(-1, 4)) == (p3[1], p3[0], p3[2]) == (F(4, 13), F(-3, 13), F(12, 13))
    GA.check("the witness curve lies on the variety, changes dying axis at v = 0 through the Taub point", ok)
    return ok


def check_dying_order_maximal_at_schwarzschild():
    ok = True
    u = GA.RF.var()
    Du = GA.RF1 + u + u * u
    d = C(2) * u / Du
    ok = ok and (C(F(2, 3)) - d).eqrf(C(2) * (u - GA.RF1) * (u - GA.RF1) / (C(3) * Du))
    ok = ok and d.eval(F(1)) == F(2, 3)
    wv = GA.RF.var()
    ok = ok and (C(2) * wv / (wv * wv + wv + GA.RF1)).eval(F(0)) == 0
    ok = ok and (C(-2) * Q[0]).eqrf(C(2) * V / DV) and (C(-2) * Q[0]).eval(F(0)) == 0
    N = 8
    inv_sqrt = GA.ps_pow_rat([F(1), F(0), F(-1)] + [F(0)] * (N - 2), F(-1, 2), N)
    integrand = [F(0)] * (N + 1)
    for k, c in enumerate(inv_sqrt):
        if k + 2 <= N:
            integrand[k + 2] += 2 * c
    tau = GA.ps_int(integrand)
    tau2 = GA.ps_mul(tau, tau, N + 3)
    ok = ok and all(tau2[k] == 0 for k in range(6)) and tau2[6] == F(4, 9) and tau2[7] == 0
    ok = ok and tau2[8] == F(4, 15)
    GA.check("d(1) - d(u) = 2(u-1)^2/(3(1+u+u^2)): maximal 2/3 at Schwarzschild, zero at the edge", ok)
    return ok


def check_edge_gram_nondegenerate_and_sheaf_rank():
    premise("sheaf.local-freeness-constant-rank")
    ok = True
    grams = []
    for c in ((1, 1, 1), (2, F(1, 3), 5)):
        M = [[F(0)] * 4 for _ in range(4)]
        M[0][0] = F(1)
        for i, ci in enumerate(c):
            M[i + 1][i + 1] = -F(ci)
        ok = ok and GA.congruence_signature(M) == (1, 3, 0)
        grams.append(M)
    for zero_slot in (1, 2):                         # the chambers' boundary Grams
        M = [[F(0)] * 4 for _ in range(4)]
        for i, dv in enumerate((1, -1, -1, -1)):
            M[i][i] = F(0) if i == zero_slot else F(dv)
        ok = ok and GA.congruence_signature(M) == (1, 2, 1) and len(GA.field_kernel(M)) == 1
        grams.append(M)
    ok = ok and [len(GA.field_kernel(M)) for M in grams] == [0, 0, 1, 1]
    blades = GA.all_blades(4)
    for M in grams:
        rows = []
        for I in blades:
            st = GA.ext_sigma_blade(I, M, 4)
            rows.append([st.get(frozenset(J), F(0)) for J in blades])
        ok = ok and GA.rank_of_vectors(rows) == 16
    GA.check("on Z the Gram is Lorentzian (corank 0), on chambers corank 1; the Clifford sheaf keeps rank 16", ok)
    return ok


def check_chamber_package_across_the_edge():
    premise("sheaf.variable-weight-boundary-tameness-completion-forced")
    ok = True
    qv = qpt(F(-1, 4))
    Dq = 13
    w = GA.RF.var()

    def tau_pow(e):
        e = F(e) * Dq
        assert e.denominator == 1
        out = GA.RF1
        for _ in range(abs(e.numerator)):
            out = out * w
        return out if e >= 0 else GA.RF1 / out

    raw = [GA.RF1, -tau_pow(-2 * qv[0]), -tau_pow(-2 * qv[1]), -tau_pow(-2 * qv[2])]
    wts = [F(0), qv[0], F(0), qv[2]]
    Wd = [raw[i] * tau_pow(2 * wts[i]) for i in range(4)]
    rho2 = tau_pow(-2 * qv[1])
    ok = ok and Wd[0].eqrf(GA.RF1) and Wd[1].eqrf(C(-1)) and Wd[2].eqrf(-rho2) and Wd[3].eqrf(C(-1))
    G0 = [x.eval(F(0)) for x in Wd]
    M0 = [[G0[i] if i == j else F(0) for j in range(4)] for i in range(4)]
    ok = ok and GA.congruence_signature(M0) == (1, 2, 1) and G0[2] == 0 and G0[1] == -1
    z = GA.RF0
    h = [[Wd[0], z, z, z, z, z], [z, Wd[1], z, z, z, z], [z, z, Wd[2], z, GA.RF1, C(F(-1, 2))],
         [z, z, z, Wd[3], z, z], [z, z, GA.RF1, z, z, C(-1)], [z, z, C(F(-1, 2)), z, C(-1), z]]
    ok = ok and GA.rf_mat_det(h).eqrf(GA.RF1 + rho2)
    for w0 in W_SAMPLES:
        ok = ok and GA.congruence_signature([[e.eval(w0) for e in row] for row in h]) == (2, 4, 0)
    o = [F(0)] + [-2 * t for t in qv]
    deg = [(t - oo) / 2 for oo, t in zip(o, [F(0), F(0), -2 * qv[1], F(0)])]
    exc = [(F(0) - oo) / 2 for oo in o]
    ok = ok and deg == [F(0), F(4, 13), F(0), F(12, 13)] and exc == [F(0), F(4, 13), F(-3, 13), F(12, 13)]
    GA.check("the v < 0 chamber carries the full package with dying axis 2: (2,4), det h = 1 + rho', forced weights", ok)
    return ok


def check_no_module_crosses_the_edge():
    ok = True
    taub = (F(0), F(0), F(1))
    w1 = [F(0), F(0), taub[1], taub[2]]
    w2 = [F(0), taub[0], F(0), taub[2]]
    ok = ok and w1 == w2 == [0, 0, 0, 1]
    ok = ok and (Q[0] * (-Q[1]) * DV * DV).eqrf(V * V * (GA.RF1 + V))
    ok = ok and (Q[0] - Q[1]).eqrf(-(V * (C(2) + V)) / DV)
    for v in V_POS:
        q = qpt(v)
        ok = ok and q[0] < 0 and -q[1] < 0
    for v in V_NEG:
        q = qpt(v)
        ok = ok and q[0] > 0 and -q[1] > 0
    ok = ok and qpt(F(1, 2))[0] == F(-2, 7) and -qpt(F(1, 2))[1] == F(-3, 7)
    GA.check("the chamber modules meet on Z, but the transition (tau^q1, tau^-q2) is a unit on neither side", ok)
    return ok
