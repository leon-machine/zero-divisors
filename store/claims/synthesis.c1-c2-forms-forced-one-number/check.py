"""synthesis.c1-c2-forms-forced-one-number: exact checks.

Schwarzschild interior in synchronous form ds^2 = dtau^2 - A dt^2 - r^2 dOmega^2, A = 2M/r - 1
(interior.kasner-form-interior). With b = r and a = sqrt(A), d/dtau = sqrt(A) d/dr, so
(db/dtau)^2 = A and every frame sectional curvature is a rational function of r computed below
with exact rational functions (GA.RF) at several rational masses.

(1) The six frame sectional curvatures (t-tau, theta-tau, phi-tau, t-theta, t-phi, theta-phi)
    are (2, -1, -1, -1, -1, 2) times M/r^3 exactly; Ricci vanishes; Kretschmann is
    48 M^2/r^6 = 12 (2M/r^3)^2. So every algebraic curvature criterion at an M-independent value
    selects a slice 2M/r^3 = lambda.
(2) The forced weights (Kasner exponents -1/3, 2/3, 2/3) reproduce the same six numbers as
    p_i(p_i - 1)/tau^2, p_i p_j/tau^2, with 4/(9 tau^2) = 2M/r^3 on the leading proper time
    tau = (2/3) r^(3/2) (2M)^(-1/2): level sets of the Weyl eigenvalue are level sets of the weighted
    blow-up's proper time.
(3) The count: slice volume per unit Killing time squared, (4 pi r_c^2)^2 (2M/r_c - 1), equals
    (8 pi M)^2 lambda^(-1) (1 - r_c/2M) exactly on the locus 2M = lambda r_c^3, and
    r_c/2M = lambda^(-1/3) (2M)^(-2/3); power-law slices r_c = c M^alpha give exponent
    (1 + 3 alpha)/2, linear iff alpha = 1/3.
(4) The slice's isometry group R x SO(3) is transitive: rotors carry e3 to any rational unit vector.
"""
from fractions import Fraction as F
from GA import RF, mul, add, scal, sc, gen, reverse, eq
from tp_premise import premise

MASSES = [F(1, 2), F(1), F(3), F(7, 5), F(40)]


def frame_curvatures(M):
    r = RF.var()
    A = RF.const(2 * M) / r - RF.const(1)          # (db/dtau)^2 = (da/dtau... ) a^2 = A
    # b = r, bdot^2 = A, bddot = (1/2) dA/dr
    bdd = RF.const(F(1, 2)) * A.deriv()
    # a = bdot, so adot = bddot and addot / a = d(bddot)/dr
    K_t_tau = bdd.deriv()                          # addot / a
    K_th_tau = bdd / r                             # bddot / b
    K_t_th = bdd / r                               # adot bdot / (a b) = bddot / b
    K_th_ph = (RF.const(1) + A) / (r * r)          # (1 + bdot^2) / b^2
    return [K_t_tau, K_th_tau, K_th_tau, K_t_th, K_t_th, K_th_ph]


def check_frame_curvature_multiples():
    premise("interior.kasner-form-interior")
    for M in MASSES:
        r = RF.var()
        unit = RF.const(M) / (r * r * r)           # M / r^3
        Ks = frame_curvatures(M)
        coeffs = [F(2), F(-1), F(-1), F(-1), F(-1), F(2)]
        for K, c in zip(Ks, coeffs):
            assert K.eqrf(RF.const(c) * unit)
        # vacuum: the three Ricci combinations vanish identically
        Ktt, Kth, _, Ktth, _, Kthph = Ks
        assert (Ktt + Kth + Kth).is_zero()
        assert (Ktt + Ktth + Ktth).is_zero()
        assert (Kth + Ktth + Kthph).is_zero()
        # Kretschmann = 4 * sum over the six planes of K^2 = 48 M^2 / r^6
        kre = RF.const(0)
        for K in Ks:
            kre = kre + RF.const(4) * K * K
        assert kre.eqrf(RF.const(48 * M * M) / (r * r * r * r * r * r))
        w = RF.const(2 * M) / (r * r * r)
        assert kre.eqrf(RF.const(12) * w * w)
        # the level set of the Kretschmann scalar at an M-independent value K0 is the level set
        # of the eigenvalue at lambda with 12 lambda^2 = K0: same slice family
        for lam in (F(1), F(4), F(1, 9)):
            rc3 = 2 * M / lam
            assert 12 * (2 * M / rc3) ** 2 == 12 * lam * lam
    return True


def check_forced_weights_reproduce_curvature():
    premise("sheaf.weights-are-forced-are-kasner-exponents")
    premise("sheaf.kasner-data-interior")
    p = [F(-1, 3), F(2, 3), F(2, 3)]
    assert sum(p) == 1 and sum(x * x for x in p) == 1
    diag = [x * (x - 1) for x in p]                # addot/a type, times tau^2
    off = [p[0] * p[1], p[0] * p[2], p[1] * p[2]]  # adot bdot / (a b) type, times tau^2
    # in units of 2/(9 tau^2) the six numbers are (2, -1, -1, -1, -1, 2)
    u = F(2, 9)
    assert [d / u for d in diag] == [F(2), F(-1), F(-1)]
    assert [o / u for o in off] == [F(-1), F(-1), F(2)]
    # 4/(9 tau^2) = 2M/r^3 on tau^2 = (4/9) r^3/(2M): check at rational (r, M)
    for M in MASSES:
        for rr in (F(1, 3), F(1, 2), F(1, 10)):
            tau2 = F(4, 9) * rr ** 3 / (2 * M)
            assert F(4, 9) / tau2 == 2 * M / rr ** 3
            assert u / tau2 == M / rr ** 3
    return True


def check_count_one_number():
    premise("scrambling.slice-volume-exactly-per-unit-killing")
    premise("singularity.imported-induced-geometry-interior-slice")
    # locus 2M = lambda r_c^3, lambda = mu^2 so lambda^(-1/2) = 1/mu is rational
    for mu in (F(1), F(2), F(1, 3), F(5, 2)):
        lam = mu * mu
        for rc in (F(1, 2), F(2), F(7, 3), F(11)):
            twoM = lam * rc ** 3
            if 2 * twoM / rc - 2 <= 0:
                continue
            lhs = (rc * rc) ** 2 * 16 * (twoM / rc - 1)              # (4 r_c^2)^2 A, pi^2 dropped
            rhs = (4 * twoM) ** 2 / lam * (1 - rc / twoM)            # (8M)^2 lambda^-1 (1 - r_c/2M)
            assert lhs == rhs
            # leading term: 8 pi M lambda^(-1/2) = 8 pi M / mu, so (nu, lambda) enter as nu/mu
            # the subleading ratio: (r_c/2M)^3 = lambda^-1 (2M)^-2
            assert (rc / twoM) ** 3 == 1 / (lam * twoM ** 2)
            # a different threshold gives a different leading rate unless nu compensates:
            # rate^2 / (8 pi M)^2 at leading order is nu^2 / lambda, so (nu, mu) -> (3 nu, 3 mu) is a
            # symmetry of the leading count and (nu, mu) -> (nu, 3 mu) is not
            lead = lambda nu_, mu_: nu_ * nu_ / (mu_ * mu_)
            assert lead(F(2), mu) == lead(F(6), 3 * mu) != lead(F(2), 3 * mu)
    # power-law slices r_c = c M^alpha: volume ~ sqrt(2M) r_c^(3/2) ~ M^((1 + 3 alpha)/2)
    for k in range(-12, 13):
        alpha = F(k, 12)
        expo = (1 + 3 * alpha) / 2
        assert (expo == 1) == (alpha == F(1, 3))
    return True


def check_slice_isometries_transitive():
    premise("singularity.imported-induced-geometry-interior-slice")
    SQ = (1, 1, 1)
    e = [gen(i) for i in range(3)]
    # rational unit vectors from Pythagorean quadruples
    targets = [(F(1, 3), F(2, 3), F(2, 3)), (F(2, 7), F(3, 7), F(6, 7)), (F(4, 9), F(-4, 9), F(7, 9)),
               (F(0), F(0), F(1)), (F(-12, 13), F(0), F(5, 13))]
    for t in targets:
        assert sum(x * x for x in t) == 1
        v = add(*[scal(t[i], e[i]) for i in range(3)])
        u = e[2]
        if eq(v, scal(F(-1), u)):
            R = mul(e[0], u, SQ)                    # half-turn about e0 (bivector), sends u to -u
        else:
            R = add(sc(F(1)), mul(v, u, SQ))        # rotor taking u to v, up to scale
        RR = mul(R, reverse(R), SQ)
        n = RR.get((), F(0))
        assert n != 0 and eq(RR, sc(n))
        img = scal(1 / n, mul(mul(R, u, SQ), reverse(R), SQ))
        assert eq(img, v)
    return True
