"""sheaf.characterisation-forced-within-rain-bounded-class: exact checks on the Schwarzschild data (2M = m^2,
u = sqrt(r), rational-function identities in u; equator).

(1) Rain-bounded means inside W (the premise sheaf.rain-duality (3)): the W-frame has bounded rain components,
while adjoining any of dr, dtheta, du/u to W produces an unbounded component, so W is the maximal rain-bounded
extension.
(2) Within the rain-bounded class, tameness forces W (the premise sheaf.uniqueness-weighted-module): for five
rain-bounded transitions A, the extension is boundary tame (corank one at E and det G_M / r -> nonzero) exactly
when A(0) is invertible, i.e. exactly when M = W near E; the expected verdicts are written out.
(3) Some anchoring class must be named (Example ex:nullmix): the null-mixing frame alpha = du + C dtheta,
beta = dt + D dtheta, gamma = u^4 dtheta, delta = u^2 dphi, C = sqrt(m^2 - u^2)/2, D = -m u^2/(2C), at the
rational points (m, u) = (5, 3), (5, 4) (C = 2, 3/2): G(alpha, alpha) = G(alpha, beta) = 0, det = -r/4 exactly;
at u = 0 (C = m/2) the boundary Gram (the limit of the frame Gram written as rational functions of C, with
r = m^2 - 4C^2) has corank one with a nonzero 3 x 3 minor m^2/4, so (T2d) and (T3d) hold;
yet alpha(e_theta)^2 = C^2/r^2 = (m^2 - u^2)/(4u^4) has a pole at u = 0 (r^2 times it tends to m^2/4), so it is
not rain-bounded and is not W.
(4) The completion built on W is attached with it (the premise sheaf.one-sided-completion-singularity): with the
normalised transversal dt/m and mu nu = -m^2/2, det h = m^2 at every radius and the signature is (2,4) at E.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

U = GA.RF.var()
R = U * U
MASSES = (F(1), F(3))


def C(x):
    return GA.RF.const(F(x))


def rain_frame(m):
    beta = C(m) / U
    Z, O = GA.RF0, GA.RF1
    return [[O, -beta, Z, Z], [Z, O, Z, Z], [Z, Z, O / R, Z], [Z, Z, Z, O / R]]


def pair(a, X):
    acc = GA.RF0
    for i in range(4):
        acc = acc + a[i] * X[i]
    return acc


def bounded(f):
    try:
        f.eval(F(0))
        return True
    except ZeroDivisionError:
        return False


# coordinate covectors on (dt, dr, dtheta, dphi) at the equator
Z4 = [GA.RF0] * 4
W_FRAME = [[GA.RF0, U, GA.RF0, GA.RF0], [GA.RF1, GA.RF0, GA.RF0, GA.RF0],
           [GA.RF0, GA.RF0, R, GA.RF0], [GA.RF0, GA.RF0, GA.RF0, R]]
OUTSIDE = [[GA.RF0, GA.RF1, GA.RF0, GA.RF0], [GA.RF0, GA.RF0, GA.RF1, GA.RF0],
           [GA.RF0, GA.RF1 / (C(2) * R), GA.RF0, GA.RF0]]          # dr, dtheta, du/u = dr/(2r)


def check_rain_bounded_is_inclusion_in_w():
    premise("sheaf.rain-duality")
    ok = True
    for m in MASSES:
        fr = rain_frame(m)
        ok = ok and all(bounded(pair(a, X)) for a in W_FRAME for X in fr)
        unb = [sum(1 for X in fr if not bounded(pair(a, X))) for a in OUTSIDE]
        # dr: V-component -m/u; dtheta: e_theta-component 1/r; du/u: both e_r and V components diverge
        ok = ok and unb == [1, 1, 2]
    GA.check("W is rain-bounded and adjoining dr, dtheta or du/u breaks rain-boundedness: W is maximal", ok)
    return ok


def check_tame_rain_bounded_extensions_are_w():
    ex = premise("sheaf.uniqueness-weighted-module")
    ok = True
    for m in MASSES:
        W = ex["weighted_gram"](m)
        cases = transitions(m)
        verdicts = []
        for A in cases:
            GM = ex["congruence"](A, W)
            corank_one = GA.mat_rank([[e.eval(F(0)) for e in row] for row in GM]) == 3
            order, lead = ex["dying_order"](GA.rf_mat_det(GM))
            tame = corank_one and order == 1
            equal_w = GA.rf_mat_det(A).eval(F(0)) != 0
            ok = ok and tame == equal_w
            verdicts.append(tame)
        ok = ok and verdicts == [True, True, False, False, False]
    GA.check("among rain-bounded extensions exactly those equal to W near E are boundary tame", ok)
    return ok


def transitions(m):
    """Five rain-bounded transitions (rows: an M-frame in the W-frame)."""
    Z, O = GA.RF0, GA.RF1
    return [
        [[O, Z, Z, Z], [Z, O, Z, Z], [Z, Z, O, Z], [Z, Z, Z, O]],
        [[O, U, Z, Z], [Z, O, Z, Z], [R, Z, O, Z], [Z, Z, Z, C(2)]],
        [[U, Z, Z, Z], [O, C(m), Z, Z], [Z, Z, O, Z], [Z, Z, Z, O]],
        [[O, Z, Z, Z], [Z, O, Z, Z], [Z, Z, U, Z], [Z, Z, Z, O]],
        [[O, Z, Z, Z], [Z, U, Z, Z], [Z, Z, O, Z], [Z, Z, Z, O]],
    ]


def nullmix_gram(m, u, Cv):
    r = u * u
    D = -m * r / (2 * Cv)
    Gdd, Gdt, Gtt, Gang = (m * m - r) / (4 * r * r), -m / (2 * r), F(1), -1 / (r * r)
    fr = [{"du": F(1), "th": Cv}, {"dt": F(1), "th": D}, {"th": r * r}, {"ph": r}]

    def g(x, y):
        return (x.get("du", 0) * y.get("du", 0) * Gdd
                + (x.get("du", 0) * y.get("dt", 0) + x.get("dt", 0) * y.get("du", 0)) * Gdt
                + x.get("dt", 0) * y.get("dt", 0) * Gtt
                + (x.get("th", 0) * y.get("th", 0) + x.get("ph", 0) * y.get("ph", 0)) * Gang)
    return [[g(fr[i], fr[j]) for j in range(4)] for i in range(4)]


def det4(M):
    """Determinant of a rational square matrix (any size), through GA.rf_mat_det."""
    return GA.rf_mat_det([[C(x) for x in row] for row in M]).eval(F(0))


# row indices of alpha and beta in the null-mixing frame (alpha, beta, gamma, delta)
ALPHA, BETA = 0, 1
# the boundary (u = 0) rows kept by the 3 x 3 minor: alpha, gamma, delta
MINOR_ROWS = (0, 2, 3)


def nullmix_gram_c(m):
    """The null-mixing frame Gram as rational functions of c = C, using r = m^2 - 4 c^2 (so that
    C = sqrt(m^2 - r)/2 holds exactly); c = m/2 is the boundary u = 0."""
    c = GA.RF.var()
    mm = C(m * m)
    r = mm - C(4) * c * c
    D = -(C(m) * r) / (C(2) * c)
    Gdd, Gdt, Gang = (mm - r) / (C(4) * r * r), -C(m) / (C(2) * r), -GA.RF1 / (r * r)
    Z, O = GA.RF0, GA.RF1
    fr = [[O, Z, c, Z], [Z, O, D, Z], [Z, Z, r * r, Z], [Z, Z, Z, r]]      # on (du, dt, dtheta, dphi)

    def g(x, y):
        return (x[0] * y[0] * Gdd + (x[0] * y[1] + x[1] * y[0]) * Gdt + x[1] * y[1] * O
                + (x[2] * y[2] + x[3] * y[3]) * Gang)
    return [[g(fr[i], fr[j]) for j in range(4)] for i in range(4)]


def check_anchoring_class_must_be_named():
    ok = True
    m = F(5)
    for u, Cv in ((F(3), F(2)), (F(4), F(3, 2))):
        ok = ok and 4 * Cv * Cv == m * m - u * u
        M = nullmix_gram(m, u, Cv)
        ok = ok and M[ALPHA][ALPHA] == 0 and M[ALPHA][BETA] == 0
        ok = ok and det4(M) == -(u * u) / 4
    # boundary data (C = m/2): rows alpha, beta, gamma, delta
    B0 = [[F(0), F(0), -m / 2, F(0)], [F(0), F(0), F(0), F(0)],
          [-m / 2, F(0), F(0), F(0)], [F(0), F(0), F(0), F(-1)]]
    # B0 is the limit of the frame Gram as C -> m/2 (u -> 0), with the frame written as functions of C
    ok = ok and [[e.eval(m / 2) for e in row] for row in nullmix_gram_c(m)] == B0
    ok = ok and GA.mat_rank(B0) == 3 and GA.congruence_signature(B0) == (1, 2, 1)
    minor = [[B0[i][j] for j in MINOR_ROWS] for i in MINOR_ROWS]
    ok = ok and det4(minor) == m * m / 4
    # not rain-bounded: alpha(e_theta) = C / r, so alpha(e_theta)^2 = (m^2 - u^2)/(4 u^4), sqrt-free: a pole at
    # u = 0, with r^2 alpha(e_theta)^2 -> m^2/4
    sq = (C(m * m) - R) / (C(4) * R * R)
    ok = ok and not bounded(sq) and (sq * R * R).eval(F(0)) == m * m / 4
    GA.check("ex:nullmix: a non-rain-bounded extension satisfies (T2d) and (T3d) but is not W", ok)
    return ok


def check_completion_is_attached_to_w():
    premise("sheaf.one-sided-completion-singularity")
    ex = premise("sheaf.uniqueness-weighted-module")
    ok = True
    for m in MASSES:
        W = ex["weighted_gram"](m)
        nu, mu = F(1), -m * m / 2
        Z = GA.RF0
        cn, cm = C(nu / m), C(mu / m)                   # coupling column nu e, mu e with e = (0, 1/m, 0, 0)
        h = [[W[0][0], W[0][1], Z, Z, Z, Z],
             [W[1][0], W[1][1], Z, Z, cn, cm],
             [Z, Z, C(-1), Z, Z, Z],
             [Z, Z, Z, C(-1), Z, Z],
             [Z, cn, Z, Z, Z, C(-1)],
             [Z, cm, Z, Z, C(-1), Z]]
        ok = ok and GA.rf_mat_det(h).eqrf(C(m * m))
        h0 = [[e.eval(F(0)) for e in row] for row in h]
        ok = ok and GA.congruence_signature(h0) == (2, 4, 0)
    GA.check("the completion on W: det h = m^2 at every radius, signature (2,4) on E", ok)
    return ok
