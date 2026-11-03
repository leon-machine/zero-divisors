"""singularity.plane-rate: exact checks in Gauge Theory Gravity (GA, Cl(1,3), signature (+,-,-,-)).

Local background frame at a point of the radial plane: e_t = gen 0, e_r = gen 1, e_theta = gen 2,
e_phi = gen 3. Stored Schwarzschild field in Painleve-Gullstrand gauge: hb(a) = a - beta (a . e_t) e_r,
beta = sqrt(2M/r) (rational sample points: beta and M rational, r = 2M/beta^2); its rotation-gauge field on
the radial plane, in the GTG sign (DICTIONARY C10), Omega(e_t) = -beta beta' sigma_r = (M/r^2) sigma_r and
Omega(e_r) = -beta' sigma_r, beta' = -beta/(2r), sigma_r = e_r e_t; store-sign curvature
R(B) = -(M/r^3) S(B), S(B) = -(B + 3 sigma_r B sigma_r)/2.
(1) The pair is selected invariantly: on the six frame bivectors S has eigenvalue -2 exactly on
    span(sigma_r, I sigma_r) (kernel of S + 2 computed) and 1 on a 4-dimensional complement, S^2 + S = 2,
    and R(sigma_r) = +2M/r^3 sigma_r at several radii; sigma_r^2 = +1 and (I sigma_r)^2 = -1, so the boost
    member is sigma_r.
(2) The rate: K = hb^{-1}(e_t) has hb(K) = e_t and Q(K) = 1 - beta^2 = f; (K . D)K = D_{e_t} K
    = Omega(e_t) x K (K is t-independent) equals kappa K at the horizon beta = 1 (r = 2M) with
    kappa = 1/(4M) = f'(2M)/2 (f' from the rational function f = 1 - 2M/r), for four masses; at r > 2M it is
    not proportional to K. The Killing bivector there is in the radial plane: A . (D K) = A . F_K for
    A = K and A = hb^{-1}(e_r), with F_K = -(M/r^2) sigma_r, at the horizon and off it.
(3) The conversion: the boost rapidity per unit Killing time at the horizon is the sigma_r coefficient of
    Omega(e_t), equal to kappa; 2 pi of rapidity is 2 pi/kappa = 8 pi M of Killing time (kappa 8M = 2).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
ET, ER = GA.gen(0), GA.gen(1)
SIG = GA.mul(ER, ET, S13)
I4 = {(0, 1, 2, 3): F(1)}
BIV = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
SAMPLES = [(F(1), F(1)), (F(3, 2), F(1)), (F(1, 2), F(1)), (F(5), F(1)), (F(1), F(1, 2)), (F(2), F(2, 3))]


def dot(a, b):
    return GA.dot(a, b, S13)


def hb(a, beta):
    return GA.sub(a, GA.scal(beta * dot(a, ET), ER))


def hbinv(a, beta):
    return GA.add(a, GA.scal(beta * dot(a, ET), ER))


def comm(A, B):
    return GA.scal(F(1, 2), GA.sub(GA.mul(A, B, S13), GA.mul(B, A, S13)))


def omega(a, M, beta):
    """Rotation-gauge field on the radial plane, GTG sign."""
    r = 2 * M / (beta * beta)
    bp = -beta / (2 * r)
    return GA.add(GA.scal(-beta * bp * dot(a, ET), SIG), GA.scal(-bp * (-dot(a, ER)), SIG))


def shape(B):
    return GA.scal(F(-1, 2), GA.add(B, GA.scal(3, GA.mul(GA.mul(SIG, B, S13), SIG, S13))))


def coords(B):
    return [B.get(b, F(0)) for b in BIV]


def check_pair_selected_invariantly():
    premise("singularity.curvature-gauge-field-exact-shape-decoupling")
    Smat = [coords(shape({b: F(1)})) for b in BIV]          # rows = images of basis bivectors
    T = [list(c) for c in zip(*Smat)]                        # matrix acting on coordinate columns
    ker2 = GA.field_kernel([[T[i][j] + (2 if i == j else 0) for j in range(6)] for i in range(6)])
    ker1 = GA.field_kernel([[T[i][j] - (1 if i == j else 0) for j in range(6)] for i in range(6)])
    Isig = GA.mul(I4, SIG, S13)
    pair = [coords(SIG), coords(Isig)]
    ok = len(ker2) == 2 and len(ker1) == 4
    ok = ok and GA.rank_of_vectors(ker2 + pair) == 2
    for b in BIV:
        B = {b: F(1)}
        ok = ok and GA.eq(GA.add(shape(shape(B)), shape(B)), GA.scal(2, B))
    ok = ok and GA.eq(GA.mul(SIG, SIG, S13), GA.sc(1)) and GA.eq(GA.mul(Isig, Isig, S13), GA.sc(-1))
    for M, beta in SAMPLES:
        r = 2 * M / (beta * beta)
        R = GA.scal(-M / r ** 3, shape(SIG))
        ok = ok and GA.eq(R, GA.scal(2 * M / r ** 3, SIG))
    _tp_rv = (ok); assert _tp_rv is not False, "check_pair_selected_invariantly"; return _tp_rv


def check_surface_gravity_from_the_connection():
    premise("singularity.computed")
    ok = True
    horizon_masses = []
    for M, beta in SAMPLES:
        r = 2 * M / (beta * beta)
        K = hbinv(ET, beta)
        ok = ok and GA.eq(hb(K, beta), ET) and dot(K, K) == 1 - beta * beta
        KDK = comm(omega(hb(K, beta), M, beta), K)
        # D_{e_r} K = d_r K + Omega(e_r) x K, with d_r K = beta' e_r
        bp = -beta / (2 * r)
        ErK = GA.add(GA.scal(bp, ER), comm(omega(ER, M, beta), K))
        FK = GA.scal(-M / (r * r), SIG)
        # A . F = (A F - F A)/2 for a vector A and bivector F
        ok = ok and GA.eq(KDK, comm(K, FK)) and GA.eq(ErK, comm(hbinv(ER, beta), FK))
        if beta == 1:
            horizon_masses.append(M)
            kappa = F(1) / (4 * M)
            ok = ok and GA.eq(KDK, GA.scal(kappa, K))
            # f = 1 - 2M/r = (r - 2M)/r; f'(r) = 2M/r^2; at r = 2M: 1/(2M)
            f = GA.RF([-2 * M, F(1)], [F(0), F(1)])
            ok = ok and f.eval(2 * M) == 0 and f.deriv().eval(2 * M) / 2 == kappa
        else:
            # off the horizon (K . D)K is not a multiple of K
            c = KDK.get((0,), F(0))
            ok = ok and not GA.eq(KDK, GA.scal(c, K))
    _tp_rv = (ok and horizon_masses == [F(1), F(3, 2), F(1, 2), F(5)]); assert _tp_rv is not False, "check_surface_gravity_from_the_connection"; return _tp_rv


def check_two_pi_rapidity_is_eight_pi_m():
    premise("singularity.computed")
    premise("singularity.curvature-gauge-field-exact-shape-decoupling")
    ok = True
    for M in (F(1), F(3, 2), F(1, 2), F(5)):
        rate = omega(ET, M, F(1)).get((0, 1), F(0)) * (-1)       # sigma_r = e_r e_t = -e_0 e_1
        kappa = F(1) / (4 * M)
        ok = ok and rate == kappa and rate * 8 * M == 2 and 1 / rate == 4 * M
    _tp_rv = (ok); assert _tp_rv is not False, "check_two_pi_rapidity_is_eight_pi_m"; return _tp_rv
