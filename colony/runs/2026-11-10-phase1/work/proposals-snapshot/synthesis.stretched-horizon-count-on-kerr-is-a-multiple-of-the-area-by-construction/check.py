"""synthesis.stretched-horizon-count-on-kerr-is-a-multiple-of-the-area-by-construction: exact checks.

Kerr in the Kerr-Schild gauge, in oblate coordinates (t, r, u = cos theta, phi) of the flat background, in
components in the signature (-+++) of the stored Kerr results:
  eta = -dt^2 + Sigma/P dr^2 + Sigma/(1 - u^2) du^2 + P (1 - u^2) dphi^2,  P = r^2 + a^2,
  k   = -dt - (Sigma/P) dr + a (1 - u^2) dphi,  g = eta + 2 H k k,  H = M r / Sigma,  Sigma = r^2 + a^2 u^2.
Holes are rational with sqrt(M^2 - a^2) = s rational; pi is kept as a formal factor (nu = 1/(16 pi) enters as
NU_PI = nu * pi = 1/16).
  (1) the Gram determinant of (d_t + Omega d_phi, d_u, d_phi) on a surface r = const is -Delta Sigma for every
      Omega, and +Delta Sigma at one point computed in Cl(1,3) with the store's product from the gauge field
      hb^{-1}(b) = b - H (b.k) k (clause (i));
  (2) the squared rate per unit horizon area, divided by the squared proper distance, is a polynomial in the
      coordinate distance delta whose constant term is kappa_+^2 at every latitude, likewise kappa_-^2 at the
      inner locus, kappa_+ A_+ = kappa_- A_-, the generator d_t + Omega_H d_phi is null and orthogonal to d_phi
      on the locus at Omega_H = a/P_+ and not null at -a/P_+, and the cancellation (clauses (ii), (iii), (iv),
      (vi)); an independent second placement would double the density, and 12 pi M rho_0 = 3 kappa rho_0 A;
  (3) the two stored forms of the Schwarzschild rate and the area form give three different counts on Kerr;
      the rate in the area form is 8 pi nu (M - 2 Omega_H J); the near-extremal sequence (clauses (v), (vii));
  (4) on Schwarzschild the rate 8 pi M is reached on three slices r = const, bracketed exactly (clause (vi)).
The integral I(r) of sqrt(r^2 + a^2 u^2) over u and the limits are the proof's.
"""
from fractions import Fraction as F

import GA
from GA import padd, peval, pmul
from tp_premise import premise

NU_PI = F(1, 16)                      # nu * pi at nu = 1/(16 pi), the stored 1-nat density
# (M, a, s) with s^2 = M^2 - a^2
HOLES = [(F(5), F(3), F(4)), (F(13), F(5), F(12)), (F(5), F(4), F(3)), (F(25), F(24), F(7)),
         (F(41), F(40), F(9))]
# (M, a, r, u, Omega): between the horizons, outside, inside the inner locus
POINTS = [(F(5), F(3), F(7), F(1, 3), F(2, 7)), (F(5), F(3), F(4), F(-2, 5), F(0)),
          (F(13), F(5), F(30), F(3, 4), F(1, 9)), (F(5), F(4), F(1, 2), F(1, 7), F(3))]
LATITUDES = [F(0), F(1, 3), F(-3, 5), F(1)]
RHOS = [F(4), F(10)]                  # Schwarzschild cutoff radii rho, 2M = rho^3
SQ = (1, -1, -1, -1)                  # the store's product on flat spacetime, generators e_t, e_x, e_y, e_z
# one point with rational Cartesian frame data: sqrt(r^2 + a^2) = 5, sqrt(1 - u^2) = 4/5, at phi = 0
GA_POINT = (F(7), F(3), F(4), F(3, 5), F(5), F(4, 5), F(2, 7))


def vec(c):
    return GA.add(*[GA.scal(c[i], GA.gen(i)) for i in range(4)])


def store_gram_det(M, a, r, u, rootP, sinth, Om):
    """Gram determinant of hb^{-1}(d_t + Om d_phi), hb^{-1}(d_u), hb^{-1}(d_phi) in the store's product,
    with x = sqrt(P) sin(theta) cos(phi), y = sqrt(P) sin(theta) sin(phi), z = r u, at phi = 0."""
    assert rootP * rootP == r * r + a * a and sinth * sinth == 1 - u * u
    P, Sigma = r * r + a * a, r * r + a * a * u * u
    d_t = vec([F(1), F(0), F(0), F(0)])
    d_r = vec([F(0), r * sinth / rootP, F(0), u])
    d_u = vec([F(0), -rootP * u / sinth, F(0), r])
    d_phi = vec([F(0), F(0), rootP * sinth, F(0)])
    k = GA.add(d_t, GA.scal(F(-1), d_r), GA.scal(a / P, d_phi))     # ingoing principal null direction
    assert GA.dot(k, k, SQ) == 0                                    # Q(k) = 0
    H = M * r / Sigma

    def hbinv(b):
        return GA.sub(b, GA.scal(H * GA.dot(b, k, SQ), k))

    vs = [hbinv(GA.add(d_t, GA.scal(Om, d_phi))), hbinv(d_u), hbinv(d_phi)]
    m = [[GA.dot(v, w, SQ) for w in vs] for v in vs]
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def metric(M, a, r, u):
    S = r * r + a * a * u * u
    P = r * r + a * a
    eta = [[F(0)] * 4 for _ in range(4)]
    eta[0][0] = F(-1)
    eta[1][1] = S / P
    eta[2][2] = S / (1 - u * u)
    eta[3][3] = P * (1 - u * u)
    k = [F(-1), -S / P, F(0), a * (1 - u * u)]
    assert sum(k[i] * k[i] / eta[i][i] for i in range(4)) == 0          # k is null for eta
    H = M * r / S
    return [[eta[i][j] + 2 * H * k[i] * k[j] for j in range(4)] for i in range(4)]


def gram_det(g, vs):
    m = [[sum(v[i] * g[i][j] * w[j] for i in range(4) for j in range(4)) for w in vs] for v in vs]
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def horizon(M, a, s):
    assert s * s == M * M - a * a
    rp, rm = M + s, M - s
    return rp, rm, rp * rp + a * a, rm * rm + a * a


def check_volume_rate_of_constant_r_surfaces_is_flow_independent():
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    dets = []
    for (M, a, r, u, Om) in POINTS:
        g = metric(M, a, r, u)
        Delta = r * r - 2 * M * r + a * a
        Sigma = r * r + a * a * u * u
        d = gram_det(g, [[F(1), F(0), F(0), Om], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]])
        assert d == -Delta * Sigma
        # with Omega = a/P the generator has g(K, K) = -Delta Sigma / P^2 (Q(K) = +Delta Sigma / P^2 in the store)
        OmP = a / (r * r + a * a)
        assert g[0][0] + 2 * OmP * g[0][3] + OmP * OmP * g[3][3] == -Delta * Sigma / (r * r + a * a) ** 2
        # the same for the static flow and for a second angular velocity
        for Om2 in (F(0), Om + F(5, 3)):
            d2 = gram_det(g, [[F(1), F(0), F(0), Om2], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]])
            assert d2 == d
        dets.append(d)
    # pinned values: spacelike between the horizon loci (positive), timelike outside and inside r_-
    assert dets[0] == F(600) and dets[1] == F(1308, 5)
    assert dets[2] == F(-2120625, 16) and dets[3] == F(-5085, 784)
    # the store's product (+,-,-,-), through the gauge field in Cl(1,3): the sign is reversed, +Delta Sigma
    M, a, r, u, rootP, sinth, Om = GA_POINT
    dg = store_gram_det(M, a, r, u, rootP, sinth, Om)
    assert dg == (r * r - 2 * M * r + a * a) * (r * r + a * a * u * u) == F(-14911, 25)
    assert dg == -gram_det(metric(M, a, r, u), [[F(1), F(0), F(0), Om], [F(0), F(0), F(1), F(0)],
                                                [F(0), F(0), F(0), F(1)]])
    return True


def check_rate_per_area_over_proper_distance_is_the_surface_gravity_at_every_latitude():
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("synthesis.c-loc-is-a-second-placement-of-the-count")
    premise("synthesis.exceptional-boundary-measure-one-calibration")
    kappas = []
    for (M, a, s) in HOLES:
        rp, rm, Pp, Pm = horizon(M, a, s)
        kp = (rp - rm) / (2 * Pp)
        km = (rp - rm) / (2 * Pm)
        assert kp == s / (2 * M * rp) and Pp == 2 * M * rp and Pm == 2 * M * rm
        assert kp * Pp == s and km * Pm == s            # kappa_+ A_+ = kappa_- A_- = 4 pi s
        for u in LATITUDES[:3]:
            # the generator d_t + Omega_H d_phi on the outer locus: null and orthogonal to d_phi at
            # Omega_H = +a/P_+, not null at -a/P_+ (the sense of rotation of the entered k)
            g = metric(M, a, rp, u)
            OmH = a / Pp
            assert g[0][0] + 2 * OmH * g[0][3] + OmH * OmH * g[3][3] == 0
            assert g[0][3] + OmH * g[3][3] == 0
            assert g[0][0] - 2 * OmH * g[0][3] + OmH * OmH * g[3][3] != 0
            assert (g[2][2] * g[3][3]) == Pp * Pp                   # cross-section area element squared
        for u in LATITUDES:
            for (r0, sign, P0, k0) in ((rp, -1, Pp, kp), (rm, 1, Pm, km)):
                # r = r0 + sign * delta lies between the loci; |Delta| = delta (2 s - delta)
                rpoly = [r0, F(sign)]
                Sig = padd(pmul(rpoly, rpoly), [a * a * u * u])
                w2_over_delta = pmul([2 * s, F(-1)], Sig)       # |Delta| Sigma / delta
                Sig0 = peval(Sig, F(0))
                assert Sig0 == r0 * r0 + a * a * u * u
                ell2_over_delta = 4 * Sig0 / (2 * s)            # leading proper distance squared
                assert peval(w2_over_delta, F(0)) / (P0 * P0 * ell2_over_delta) == k0 * k0
                # exact check of |Delta| at a sample delta
                dl = s / 3
                rr = r0 + sign * dl
                assert -(rr * rr - 2 * M * rr + a * a) == dl * (2 * s - dl)
                assert peval(w2_over_delta, dl) * dl == -(rr * rr - 2 * M * rr + a * a) * peval(Sig, dl)
        kappas.append((kp, km, Pp, Pm))
    assert kappas[0] == (F(2, 45), F(2, 5), F(90), F(10))
    assert kappas[1] == (F(6, 325), F(6, 13), F(650), F(26))
    # count per unit horizon area over one period 2 pi / kappa at proper distance rho_0 = 2:
    # nu * kappa * rho_0 * 2 pi / kappa = 2 pi nu rho_0 = 1/4, with no kappa left
    for (kp, km, Pp, Pm) in kappas:
        assert NU_PI * kp * 2 * 2 / kp == F(1, 4)
    # an independent second placement of the same density would double it (G_cl = 2 G): 1/4 + 1/4 = 2 * 1/4
    eta = NU_PI * 2 * 2                                   # 2 pi nu rho_0 at rho_0 = 2
    assert eta + eta == F(1, 2) and 1 / (4 * (eta / 2)) == 2  # total 1/4 forces eta = 1/8, G_cl = 1/(4 eta) = 2
    # a -> 0 limit of the inner surface: mu_E rho_0 = 12 pi M rho_0 is three times kappa rho_0 A = 4 pi M rho_0
    M = HOLES[1][0]
    assert 12 * M * 2 == 3 * (F(1, 4) / M * 2 * 16 * M * M) == F(312)
    return True


def check_three_schwarzschild_forms_split_on_kerr_and_the_area_form_is_the_smarr_rate():
    premise("scrambling.epoch-modular-period-two-unknowns-become")
    premise("singularity.stretched-singularity-count")
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    rows = []
    for (M, a, s) in HOLES + [(F(7), F(0), F(7))]:
        rp, rm, Pp, Pm = horizon(M, a, s)
        kappa = s / (2 * M * rp)
        beta_over_pi = 2 / kappa                          # modular period 2 pi / kappa_+
        S_over_pi = Pp                                    # A_+/4 = pi (r_+^2 + a^2)
        # rates over pi at nu = 1/(16 pi):  area form 2 nu kappa A,  mass form 8 pi nu M,  temperature form nu beta
        rate_area = 2 * NU_PI * kappa * 4 * Pp            # (2 nu kappa A)/1, A = 4 pi P
        rate_mass = 8 * NU_PI * M
        rate_temp = NU_PI * beta_over_pi
        ratio = [rate * beta_over_pi / S_over_pi for rate in (rate_area, rate_mass, rate_temp)]
        assert ratio[0] == 1
        assert ratio[1] == M / s and ratio[2] == M * rp / (2 * s * s)
        # Smarr: M = 2 T S + 2 Omega_H J, so the area-form rate is 8 pi nu (M - 2 Omega_H J) = 16 pi nu T S
        OmH = a / Pp
        J = a * M
        TS = (kappa / 2) * Pp                             # (kappa / 2 pi)(pi P)
        assert M == 2 * TS + 2 * OmH * J and TS == s / 2
        assert rate_area == 8 * NU_PI * (M - 2 * OmH * J) == 16 * NU_PI * TS
        # slow rotation: ratio - 1 = e^2 c(sigma), e = a/M, sigma = s/M; c -> 1/2 and 3/4 at sigma = 1
        e2, sg = (a / M) ** 2, s / M
        assert ratio[1] - 1 == e2 / (sg * (1 + sg))
        assert ratio[2] - 1 == e2 * (1 + 2 * sg) / (2 * sg * sg * (1 + sg))
        rows.append((ratio[1], ratio[2], rate_area / rate_mass))
    one = F(1)
    assert one / (one * (1 + one)) == F(1, 2) and (1 + 2 * one) / (2 * one * one * (1 + one)) == F(3, 4)
    assert rows[0] == (F(5, 4), F(45, 32), F(4, 5))
    assert rows[2] == (F(5, 3), F(20, 9), F(3, 5))
    # near-extremal sequence: the rate falls as s/M while the count per period stays A_+/4
    assert rows[3][2] == F(7, 25) and rows[4][2] == F(9, 41)
    assert rows[5] == (F(1), F(1), F(1))                  # Schwarzschild: the three forms agree
    return True


def check_schwarzschild_rate_is_reached_on_three_slices():
    premise("singularity.stretched-singularity-count")
    vals = []
    for rho in RHOS:
        twoM = rho ** 3
        M = twoM / 2

        def g(r):
            # (V'/4 pi)^2 - (2M)^2 = r^3 |2M - r| - 4 M^2
            return r ** 3 * abs(twoM - r) - 4 * M * M

        assert g(rho) == -rho ** 4                        # the (C1) radius, short by the stored factor
        assert g(rho) < 0 < g(rho + 1 / rho)              # root just above the cutoff radius
        assert g(twoM - 1 / M) > 0 > g(twoM - 1 / twoM)   # inside, proper distance 2 at leading order
        assert g(twoM + 1 / (2 * twoM)) < 0 < g(twoM + 1 / twoM)   # outside
        assert g(F(3, 2) * M) == F(27, 16) * M ** 4 - 4 * M * M > 0     # the interior maximum
        # the stretched horizon at proper distance 2: kappa * 2 * A = 8 pi M (over pi)
        assert F(1, 4) / M * 2 * 16 * M * M == 8 * M
        vals.append((g(rho), g(twoM - 1 / twoM)))
    assert vals[0] == (F(-256), F(-50319361, 16777216))
    return True
