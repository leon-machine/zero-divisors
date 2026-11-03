"""sheaf.schwarzschild-degeneration-boundary-tame: exact checks in Gauge Theory Gravity.

The gauge field of the premise Fact sheaf.gauge-field-cometric, computed literally on Cl(1,3) (GA.py,
(+,-,-,-)): hb(a) = a - beta P(a), P(a) = (a . e_t) e_r, with adjoint hb^T(b) = b - beta (b . e_r) e_t
(checked: a . hb^T(b) = hb(a) . b on all basis pairs), beta = m/sqrt r, m^2 = 2M. Covectors are background
vectors through the reciprocal frame (dt -> e^t = e_t, dr -> e^r = -e_r, the unit angular covectors
e^2, e^3), the derived cometric is G(a, b) = hb^T(a) . hb^T(b), and the frame of W is rho = sqrt(r) dr, dt,
mu_1, mu_2. Everything is rational in (m, s = sqrt r) at rational sample points. Computed:
(0) the Gram matrix of G on (rho, dt, mu_1, mu_2) is [[m^2 - r, -m, 0, 0], [-m, 1, 0, 0], 0 + diag(-1, -1)]
    at every sample (entries polynomial of degree <= 1 in r, so the identity holds identically);
(1) det G = -r; congruence signature (1,3) at every r > 0 sampled, inside, on (r = m^2) and outside the horizon;
(2) at r = 0 the rank is 3, the radical is spanned by k = rho + m dt, and <rho, mu_1, mu_2> carries
    diag(m^2, -1, -1) of signature (1,2);
(3) G(k, k) = -r at every sample radius and mass;
(4) dt_S = dt + (m/(m^2 - r)) rho is G-orthogonal to rho (the frame (rho, dt_S, mu) diagonalises G), the
    change of frame has determinant 1, and k = m dt_S + (r/(r - m^2)) rho;
(5) k = d Phi with Phi = m t + (2/3) r^{3/2} (exact first-order jets of Phi on the labels (t, r)), and
    k(d_t - beta d_r) = 0; the rain velocity hb^{-1}(e_t - beta e_r) = e_t is D-parallel along itself in
    the Painleve-Gullstrand field (its rotation-gauge field along e_t vanishes; torsion equation checked).
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13
J = gtg.J
vec = gtg.vec


def field_cov(fld, A, V):
    """(A . D) V = D_{hb(A)} V for constant physical components A and a jet vector field V (value)."""
    return fld.cov_phys(A, V)
# ---- end of engine ----


MASSES = [F(1), F(5, 4), F(3, 7)]
SROOTS = [F(1, 3), F(2, 3), F(3, 2), F(5, 2)]
E = [GA.gen(i) for i in range(4)]
UP = [E[0], GA.neg(E[1]), GA.neg(E[2]), GA.neg(E[3])]          # reciprocal frame e^mu


def hbT(beta, b):
    return GA.sub(b, GA.scal(beta * GA.dot(b, E[1], S13), E[0]))


def hb(beta, a):
    return GA.sub(a, GA.scal(beta * GA.dot(a, E[0], S13), E[1]))


def frame(m, s):
    return [GA.scal(s, UP[1]), UP[0], UP[2], UP[3]]                 # rho, dt, mu_1, mu_2


def gram(m, s, vs=None):
    beta = m / s
    vs = vs or frame(m, s)
    return [[GA.dot(hbT(beta, a), hbT(beta, b), S13) for b in vs] for a in vs]


def components(x):
    """Coefficients of a vector x on the generators e_0..e_3."""
    return [x.get((i,), F(0)) for i in range(len(E))]


def transition(new, old):
    """The matrix T with new_a = sum_b T_ab old_b (old a basis), solved exactly."""
    M = [[components(o)[i] for o in old] for i in range(len(E))]
    return [GA.field_solve(M, components(x)) for x in new]


def det(Mx):
    n = len(Mx)
    if n == 1:
        return Mx[0][0]
    return sum((-1) ** j * Mx[0][j] * det([row[:j] + row[j + 1:] for row in Mx[1:]]) for j in range(n) if Mx[0][j])


def check_gram_matrix_of_the_cometric():
    premise("sheaf.gauge-field-cometric")
    ok = True
    for m in MASSES:
        for s in SROOTS:
            beta, r = m / s, s * s
            ok = ok and all(GA.dot(GA.gen(i), hbT(beta, GA.gen(j)), S13) == GA.dot(hb(beta, GA.gen(i)), GA.gen(j), S13)
                            for i in range(4) for j in range(4))
            want = [[m * m - r, -m, 0, 0], [-m, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
            ok = ok and gram(m, s) == want
    _tp_rv = (ok); assert _tp_rv is not False, "check_gram_matrix_of_the_cometric"; return _tp_rv


def check_nondegenerate_off_the_wall():
    premise("sheaf.gauge-field-cometric")
    ok = True
    for m in MASSES:
        for s in SROOTS + [m]:                                       # s = m is the horizon r = m^2
            G = gram(m, s)
            ok = ok and det(G) == -s * s and GA.congruence_signature([row[:] for row in G])[:2] == (1, 3)
    _tp_rv = (ok); assert _tp_rv is not False, "check_nondegenerate_off_the_wall"; return _tp_rv


def wall_gram(m):
    """The polynomial Gram at r = 0 (entries are polynomials in r, read off at r = 0)."""
    return [[m * m, -m, 0, 0], [-m, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]


def check_corank_one_on_the_wall():
    premise("sheaf.gauge-field-cometric")
    ok = True
    for m in MASSES:
        G0 = [[F(x) for x in row] for row in wall_gram(m)]
        # the wall Gram is the limit of the sampled Grams: G(s) - G0 = -s^2 E_11 at every sample
        ok = ok and all(GA.mat_eq([[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(gram(m, s), G0)],
                                  [[-s * s if (i, j) == (0, 0) else 0 for j in range(4)] for i in range(4)]) for s in SROOTS)
        ok = ok and GA.field_rank(G0) == 3
        ker = GA.field_kernel(G0)
        ok = ok and len(ker) == 1 and ker[0][1] == m * ker[0][0] and ker[0][2] == ker[0][3] == 0
        V1 = [[G0[i][j] for j in (0, 2, 3)] for i in (0, 2, 3)]
        ok = ok and V1 == [[m * m, 0, 0], [0, -1, 0], [0, 0, -1]] and GA.congruence_signature(V1)[:2] == (1, 2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_corank_one_on_the_wall"; return _tp_rv


def check_first_order_degeneration():
    premise("sheaf.gauge-field-cometric")
    ok = True
    for m in MASSES:
        for s in SROOTS + [m]:
            rho, dt = frame(m, s)[:2]
            k = GA.add(rho, GA.scal(m, dt))
            beta = m / s
            ok = ok and GA.dot(hbT(beta, k), hbT(beta, k), S13) == -s * s
    _tp_rv = (ok); assert _tp_rv is not False, "check_first_order_degeneration"; return _tp_rv


def check_schwarzschild_frame_transition():
    premise("sheaf.gauge-field-cometric")
    ok = True
    for m in MASSES:
        for s in SROOTS:
            r, beta = s * s, m / s
            if r == m * m:
                continue
            rho, dt, mu1, mu2 = frame(m, s)
            dtS = GA.add(dt, GA.scal(m / (m * m - r), rho))
            Gs = gram(m, s, [rho, dtS, mu1, mu2])
            ok = ok and all(Gs[i][j] == 0 for i in range(4) for j in range(4) if i != j)
            k = GA.add(rho, GA.scal(m, dt))
            ok = ok and GA.eq(k, GA.add(GA.scal(m, dtS), GA.scal(r / (r - m * m), rho)))
            # the transition (rho, dt, mu) -> (rho, dt_S, mu), computed from the frames, is the unitriangular
            # matrix written by hand, of determinant 1
            Tm = transition([rho, dtS, mu1, mu2], [rho, dt, mu1, mu2])
            ok = ok and Tm == [[1, 0, 0, 0], [m / (m * m - r), 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
            ok = ok and det(Tm) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_schwarzschild_frame_transition"; return _tp_rv


def check_rain_identity():
    premise("sheaf.gauge-field-cometric")
    ok = True
    for m in MASSES:
        for s in SROOTS:
            r0 = s * s
            t, r = J.var(0, F(2)), J.var(1, r0)
            Phi = m * t + F(2, 3) * r.pw(F(3, 2))
            k = GA.add(frame(m, s)[0], GA.scal(m, frame(m, s)[1]))
            kt, kr = GA.dot(k, E[0], S13), GA.dot(k, E[1], S13)        # components on dt, dr
            ok = ok and (Phi.g[0], Phi.g[1]) == (kt, kr) == (m, s)
            beta = m / s
            ok = ok and kt - beta * kr == 0
            rain = GA.sub(E[0], GA.scal(beta, E[1]))
            hbinv = GA.add(rain, GA.scal(beta * GA.dot(rain, E[0], S13), E[1]))      # hb^{-1} = 1 + beta P
            ok = ok and GA.eq(hbinv, E[0]) and GA.eq(hb(beta, hbinv), rain)
            fld = pg_field(beta, m * m / 2)
            ok = ok and fld.torsion_free() and field_cov(fld, [F(1), F(0), F(0), F(0)], vec([J(1), J(0), J(0), J(0)])) == {}
    _tp_rv = (ok); assert _tp_rv is not False, "check_rain_identity"; return _tp_rv


def pg_field(b0, M, s0=F(3, 5), c0=F(4, 5)):
    """Schwarzschild in the PG gauge with beta = b0 at the point."""
    return gtg.schwarzschild_pg(M, 2 * M / (b0 * b0), s0, c0)
