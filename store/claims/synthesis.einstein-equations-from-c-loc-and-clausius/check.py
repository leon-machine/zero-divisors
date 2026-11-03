"""synthesis.einstein-equations-from-c-loc-and-clausius: exact checks.

Signature (1,3), eta = diag(1,-1,-1,-1). Ric0 is the Ricci tensor of the convention in which the round
sphere has positive Ricci curvature (the one in the Raychaudhuri equation); the store's Ric is -Ric0
(synthesis.einstein-condition-is-infinity-vacuum-incidence, clause (7)). pi never enters an exact
quantity: e := eta_S/(2 pi) (eta_S the entropy per unit area) and kap := 2 pi/eta_S = 1/e = 8 pi G_cl are
used as rational stand-ins, and where pi does appear its power is tracked by hand in the comments.

Focusing step, on one generator with affine parameter lam (lam = 0 at p, patch lam in [lam0, 0]):
    dtheta/dlam = -theta^2/2 - S(lam) - Ric0(k,k)(lam),   S = |shear|^2,  theta(0) = theta0,
    A(lam)/A(0) = exp(int_0^lam theta),  chi = -kappa (lam + e2 lam^2) k  (e2: Killing-field error),
    dQ = int_{lam0}^0 T(chi,k) A dlam,  T_chi dS = (kappa/2pi) eta_S dA = kappa e dA.
All series are exact truncated power series (GA.ps_*).

  check_focusing_leading_order: theta = -r0 lam + O(lam^2); the Clausius defect dQ - kappa e dA has no
      lam0^0, lam0^1 terms and lam0^2 coefficient kappa (t0 - e r0)/2 for every value of the curvature
      and matter slopes, the shear (zero at p) and the Killing error; the slopes and the Killing error
      enter at lam0^3 (control), the shear at lam0^4 (it leaves lam0^3 unchanged and moves lam0^4);
      the zero set t0 = e r0 does not depend on kappa.
  check_equilibrium_hypotheses: shear s0 != 0 at p shifts the lam0^2 coefficient by -kappa e s0/2;
      expansion theta0 != 0 at p gives a lam0^1 defect kappa e theta0, so Clausius at leading order
      forces theta0 = 0.
  check_unruh_to_killing_temperature: on the Rindler orbit x^2 - t^2 = rho^2 (rational
      parametrisation) the acceleration is 1/rho and |chi| = kappa rho for chi = kappa(x d_t + t d_x),
      so T_local |chi| = (a/2pi)(kappa/a) = kappa/2pi; on the past horizon x = -t, chi = -kappa lam k.
  check_null_null_to_store_einstein: S(l,l) = 0 on eleven rational null l has rank 9 with kernel eta;
      Ric0(l,l) = kap T(l,l) on the cone gives Ric0 = kap T - h g; then Ric0 - R0 g/2 - Lambda g = kap T
      with Lambda = h - kap tau/2, and the store form Ric + kap T = (Lambda + kap tau/2) g; the
      leading Clausius defect equals kappa e (kap T(l,l)/2 - omega_l(I_g,l)) with the own-ray class
      omega_l(I_g,l) = -P(l,l) of clause (7), on every listed l.
  check_universality_at_bianchi: differences reading dS = eta_S(p) dA. With Ric = h g - kap T
      (kap = gamma = 2 pi/eta_S a function), div T = 0 and the contracted Bianchi identity at a point,
      d(h - kap tau/2) = -T(grad kap, .): zero for constant kap (Lambda an integration constant),
      nonzero for dust with grad kap along u.
  check_integrated_entropy_reading: the other reading, S = int eta_S dA with eta_S/2pi = e0 + e1 lam
      along the generator: the Clausius defect has a lam0^1 term kappa e1 = (kappa/2pi)(k.grad eta_S),
      so Clausius forces k.grad eta_S = 0 at the focusing step; under the differences reading the
      lam0^1 term is absent.
  check_dimension_enters_only_at_trace: polarisation also holds in dimension three (rank 5 of 6 on
      rational null vectors of signature (1,2), kernel g); in dimension n the Bianchi step makes
      h - kap tau/(n - 2) constant, which is h - 4 pi G tau only for n = 4.
  check_newton_constant: 2 pi/eta_S = 8 pi G_cl gives G_cl = 1/(4 eta_S); with eta_S = 4 pi nu <s>/G
      (clause (i)) G_cl/G = 1/(16 pi nu <s>), equal to 1 at the registered nu and at no other value.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

N = 5
ETA = [1, -1, -1, -1]
EXP = [F(1), F(1), F(1, 2), F(1, 6), F(1, 24), F(1, 120)]
NULLS = [
    [F(1), F(1), F(0), F(0)], [F(1), F(-1), F(0), F(0)], [F(1), F(0), F(1), F(0)],
    [F(1), F(0), F(-1), F(0)], [F(1), F(0), F(0), F(1)], [F(1), F(0), F(0), F(-1)],
    [F(1), F(3, 5), F(4, 5), F(0)], [F(1), F(0), F(3, 5), F(4, 5)], [F(1), F(4, 5), F(0), F(3, 5)],
    [F(1), F(2, 3), F(2, 3), F(1, 3)], [F(1), F(2, 7), F(-3, 7), F(6, 7)],
]
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]


# ---------------------------------------------------------------- helpers

def theta_series(theta0, r, S):
    """Raychaudhuri with theta(0) = theta0, solved by Picard iteration in exact series."""
    th = [F(0)] * (N + 1)
    th[0] = F(theta0)
    for _ in range(N + 2):
        sq = GA.ps_mul(th, th, N)
        rhs = [-sq[i] / 2 - (S[i] if i < len(S) else 0) - (r[i] if i < len(r) else 0)
               for i in range(N + 1)]
        new = GA.ps_trunc(GA.ps_int(rhs), N)
        new[0] = F(theta0)
        th = new
    return th


def defect(kappa, e, theta0, r, S, t, e2):
    """coefficients in lam0 of dQ - kappa e dA (per unit area of the pencil at p)."""
    th = theta_series(theta0, r, S)
    a = GA.ps_compose(EXP, GA.ps_trunc(GA.ps_int(th), N), N)
    dA = [F(0)] + [-a[k] for k in range(1, N + 1)]
    chi = [F(0), -kappa, -kappa * e2]
    f = GA.ps_mul(GA.ps_mul(chi, GA.ps_trunc(list(t), N), N), a, N)
    Fq = GA.ps_trunc(GA.ps_int(f), N)
    dQ = [-Fq[k] for k in range(N + 1)]
    return [dQ[k] - kappa * e * dA[k] for k in range(N + 1)], th


def form(S, u, v):
    return sum((S[a][b] * u[a] * v[b] for a in range(4) for b in range(4)), F(0))


def gmat():
    return [[F(ETA[a]) if a == b else F(0) for b in range(4)] for a in range(4)]


def trace(S):
    return sum((F(ETA[a]) * S[a][a] for a in range(4)), F(0))


def lin(c1, A, c2, B):
    return [[c1 * A[a][b] + c2 * B[a][b] for b in range(4)] for a in range(4)]


def raise_first(T, v_lower):
    """(T(grad f, .))_b = T_ab g^{ac} d_c f."""
    return [sum((T[a][b] * F(ETA[a]) * v_lower[a] for a in range(4)), F(0)) for b in range(4)]


RIC0 = [[F(2), F(1, 3), F(-1), F(0)], [F(1, 3), F(5), F(2, 7), F(1)],
        [F(-1), F(2, 7), F(-3), F(1, 2)], [F(0), F(1), F(1, 2), F(4, 9)]]
TMAT = [[F(3), F(1), F(0), F(-2, 5)], [F(1), F(1, 2), F(1, 4), F(0)],
        [F(0), F(1, 4), F(2), F(3)], [F(-2, 5), F(0), F(3), F(7, 3)]]
# Focusing samples: the leading slopes r0 = Ric0(k,k)(p), t0 = T(k,k)(p); surface gravities; entropy
# densities e = eta_S/2pi; nuisance tuples (r1, t1, s2, e2) = (curvature slope, matter slope, shear
# lam^2 coefficient, Killing error), the last all zero; a second shear value for the lam0^4 control;
# slopes e1 of eta_S/2pi along the generator for the integrated reading.
R0, T0 = F(2, 3), F(11, 13)
KAPPAS = [F(3, 2), F(7)]
ES = [F(5, 7), F(1, 4)]
NUISANCE = [(F(1), F(2), F(3), F(4)), (F(-5, 2), F(1, 3), F(7), F(-1)), (F(0), F(0), F(0), F(0))]
SHEAR_ALT = F(8)
BASE_KAPPA, BASE_E = KAPPAS[0], ES[0]        # the pair used for the lam0^3 and shear controls
BASE_NUISANCE = NUISANCE[0]                  # nuisance tuple for the zero set, shear and integrated checks
E1S = [F(0), F(2), F(-1, 3)]


# ---------------------------------------------------------------- checks

def check_focusing_leading_order():
    premise("synthesis.imported-raychaudhuri-null-congruence")
    premise("synthesis.imported-jacobson-clausius-1995")
    premise("synthesis.c-loc-local-horizon-premise")
    r0, t0 = R0, T0
    third = set()
    for kappa in KAPPAS:
        for e in ES:
            for (r1, t1, s2, e2) in NUISANCE:
                d, th = defect(kappa, e, 0, [r0, r1], [0, 0, s2], [t0, t1], e2)
                assert th[0] == 0 and th[1] == -r0          # theta = -r0 lam + O(lam^2)
                assert d[0] == 0 and d[1] == 0
                assert d[2] == kappa * (t0 - e * r0) / 2
                # by hand: theta = -r0 lam - r1 lam^2/2 + O(lam^3), A = 1 - r0 lam^2/2 - r1 lam^3/6 + O(lam^4),
                # dQ = kappa (t0 lam0^2/2 + (t1 + e2 t0) lam0^3/3) + ...: the lam0^3 coefficient carries the
                # slopes and the Killing error, and no shear
                assert d[3] == kappa * ((t1 + e2 * t0) / 3 - e * r1 / 6)
                if kappa == BASE_KAPPA and e == BASE_E:
                    third.add(d[3])
            # the zero set of the leading coefficient: t0 = e r0, whatever kappa
            r1, t1, s2, e2 = BASE_NUISANCE
            d, _ = defect(kappa, e, 0, [r0, r1], [0, 0, s2], [e * r0, t1], e2)
            # (the lam0^3 coefficient here is kappa((2 + 4 e r0)/3 - e/6) > 0: the zero set does not reach lam0^3)
            assert d[2] == 0 and d[3] == kappa * ((t1 + e2 * e * r0) / 3 - e * r1 / 6)
    assert len(third) == 3                                  # control: nuisance terms enter at lam0^3
    # the shear alone: lam0^3 unchanged, lam0^4 moved. By hand: S = s2 lam^2 adds -s2 lam^3/3 to theta,
    # -s2 lam^4/12 to A, so -kappa e s2/12 to the lam0^4 defect.
    r1, t1, s2, e2 = BASE_NUISANCE
    kappa, e = BASE_KAPPA, BASE_E
    d1, _ = defect(kappa, e, 0, [r0, r1], [0, 0, s2], [t0, t1], e2)
    d2, _ = defect(kappa, e, 0, [r0, r1], [0, 0, SHEAR_ALT], [t0, t1], e2)
    assert d1[2] == d2[2] and d1[3] == d2[3] and d1[4] - d2[4] == -kappa * e * (s2 - SHEAR_ALT) / 12
    return True


def check_equilibrium_hypotheses():
    premise("synthesis.imported-raychaudhuri-null-congruence")
    premise("synthesis.imported-jacobson-clausius-1995")
    kappa, e, r0, t0 = F(3, 2), F(5, 7), F(2, 3), F(11, 13)
    s0 = F(1, 5)
    d, _ = defect(kappa, e, 0, [r0], [s0], [t0], 0)
    assert d[2] == kappa * (t0 - e * (r0 + s0)) / 2
    assert d[2] - kappa * (t0 - e * r0) / 2 == -kappa * e * s0 / 2
    th0 = F(1, 9)
    d, _ = defect(kappa, e, th0, [r0], [0], [t0], 0)
    assert d[1] == kappa * e * th0 and d[1] != 0
    d, _ = defect(kappa, e, 0, [r0], [0], [t0], 0)
    assert d[1] == 0
    return True


def check_unruh_to_killing_temperature():
    premise("synthesis.c-loc-local-horizon-premise")
    premise("synthesis.imported-jacobson-clausius-1995")
    u = GA.RF.var()
    one = GA.RF.const(1)
    for rho in (F(1, 2), F(3), F(5, 4)):
        for kappa in (F(1), F(2, 3)):
            R = GA.RF.const(rho)
            t = R * (u - one / u) / GA.RF.const(2)
            x = R * (u + one / u) / GA.RF.const(2)
            # x^2 - t^2 = rho^2 on the whole orbit
            assert (x * x - t * t).eqrf(R * R)
            # proper time: d tau/du = rho/u; unit velocity U = (u/rho) dX/du
            dt, dx = t.deriv(), x.deriv()
            n2 = dt * dt - dx * dx
            assert n2.eqrf(R * R / (u * u))
            s = u / R
            Ut, Ux = s * dt, s * dx
            assert (Ut * Ut - Ux * Ux).eqrf(one)
            At, Ax = s * Ut.deriv(), s * Ux.deriv()
            acc2 = At * At - Ax * Ax                         # = -a^2 (spacelike)
            assert acc2.eqrf(GA.RF.const(-1) / (R * R))
            a = 1 / rho
            # boost field chi = kappa (x d_t + t d_x): |chi|^2 = kappa^2 (x^2 - t^2)
            chi_t, chi_x = GA.RF.const(kappa) * x, GA.RF.const(kappa) * t
            assert (chi_t * chi_t - chi_x * chi_x).eqrf(GA.RF.const(kappa * kappa * rho * rho))
            norm_chi = kappa * rho
            # T_local = a/2pi, Killing-normalised T_chi = T_local |chi|: coefficient of 1/(2 pi)
            assert a * norm_chi == kappa
    # on the past horizon x = -t of the right wedge, lam = t < 0, k = d_t - d_x:
    lam = GA.RF.var()
    for kappa in (F(1), F(2, 3)):
        chi_t = GA.RF.const(kappa) * (GA.RF.const(-1) * lam)   # kappa x with x = -lam
        chi_x = GA.RF.const(kappa) * lam                        # kappa t
        # chi = c k with k = (1, -1): c = chi_t = -chi_x
        assert chi_t.eqrf(GA.RF.const(-1) * chi_x)
        assert chi_t.eqrf(GA.RF.const(-kappa) * lam)
    return True


def check_null_null_to_store_einstein():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    premise("synthesis.imported-jacobson-clausius-1995")
    g = gmat()
    for l in NULLS:
        assert form(g, l, l) == 0
    rows = [[(l[a] * l[b] if a == b else 2 * l[a] * l[b]) for (a, b) in PAIRS] for l in NULLS]
    assert GA.mat_rank(rows) == 9
    gv = [g[a][b] for (a, b) in PAIRS]
    assert all(sum((r[i] * gv[i] for i in range(10)), F(0)) == 0 for r in rows)
    for kap in (F(3), F(5, 2)):
        for h in (F(1, 3), F(-2)):
            ric0 = lin(kap, TMAT, -h, g)                       # Ric0 = kap T - h g
            for l in NULLS:
                assert form(ric0, l, l) == kap * form(TMAT, l, l)
            # control: adding c l1 l1 breaks the cone condition on some listed l
            l1 = NULLS[6]
            bad = [[ric0[a][b] + l1[a] * l1[b] for b in range(4)] for a in range(4)]
            assert any(form(bad, l, l) != kap * form(TMAT, l, l) for l in NULLS)
            tau = trace(TMAT)
            R0 = trace(ric0)
            assert R0 == kap * tau - 4 * h
            Lam = h - kap * tau / 2
            lhs = lin(F(1), lin(F(1), ric0, -R0 / 2, g), -Lam, g)
            assert lhs == lin(kap, TMAT, F(0), g)            # Ric0 - R0 g/2 - Lambda g = kap T
            ric = lin(F(-1), ric0, F(0), g)                  # store convention
            assert lin(F(1), ric, kap, TMAT) == lin(Lam + kap * tau / 2, g, F(0), g)
    # the leading Clausius defect is the gap between the matter class and the vacuum class
    kappa = F(3, 2)
    for e in (F(5, 7), F(1, 4)):
        kap = 1 / e
        ric = lin(F(-1), RIC0, F(0), g)
        Rs = trace(ric)
        P = lin(F(1, 2), ric, -Rs / 12, g)                    # Ric = 2P + (R/6) g
        for l in NULLS:
            r0, t0 = form(RIC0, l, l), form(TMAT, l, l)
            omega = -form(P, l, l)                            # own-ray class of clause (7)
            assert omega == r0 / 2
            d, _ = defect(kappa, e, 0, [r0, F(1)], [0, 0, F(2)], [t0, F(3)], F(1))
            assert d[2] == kappa * e * (kap * t0 / 2 - omega)
    return True


def check_universality_at_bianchi():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    g = gmat()
    tau = trace(TMAT)
    # pointwise data: d tau, d kap (lower index); div T = 0
    dtau = [F(1), F(-2), F(1, 3), F(4)]
    for dkap in ([F(0)] * 4, [F(2), F(0), F(0), F(0)], [F(1, 2), F(-1), F(3), F(0)]):
        for kap in (F(3), F(7, 2)):
            TdK = raise_first(TMAT, dkap)
            # unknown dh: div Ric = dh - T(grad kap) (with div T = 0), Bianchi: div Ric = dR/2,
            # trace: R = 4h - kap tau, so dR = 4 dh - kap dtau - tau dkap; solve componentwise
            dh = []
            for b in range(4):
                M = [[F(1), F(-1, 2)], [F(-4), F(1)]]           # [dh, dR]
                rhs = [TdK[b], -kap * dtau[b] - tau * dkap[b]]
                det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
                x0 = (rhs[0] * M[1][1] - M[0][1] * rhs[1]) / det
                dh.append(x0)
            dLam = [dh[b] - kap * dtau[b] / 2 - tau * dkap[b] / 2 for b in range(4)]
            assert dLam == [-TdK[b] for b in range(4)]
            if dkap == [F(0)] * 4:
                assert dLam == [F(0)] * 4
    # dust T = rho u u with u = (1,0,0,0) (lower index): grad kap along u moves Lambda
    rho = F(5)
    dust = [[rho if a == b == 0 else F(0) for b in range(4)] for a in range(4)]
    assert raise_first(dust, [F(2), F(0), F(0), F(0)]) == [F(10), F(0), F(0), F(0)]
    assert raise_first(dust, [F(0), F(1), F(0), F(0)]) == [F(0)] * 4
    assert g[0][0] == 1
    return True


def check_integrated_entropy_reading():
    premise("synthesis.imported-jacobson-clausius-1995")
    premise("synthesis.c-loc-local-horizon-premise")
    kappa, r0, t0 = BASE_KAPPA, R0, T0
    r1, t1, s2, e2 = BASE_NUISANCE
    agree = 0
    for e0 in ES:
        for e1 in E1S:
            th = theta_series(0, [r0, r1], [0, 0, s2])
            a = GA.ps_compose(EXP, GA.ps_trunc(GA.ps_int(th), N), N)
            ea = GA.ps_mul([e0, e1], a, N)                   # (eta_S/2pi) A along the generator
            dS = [e0 - ea[0]] + [-ea[k] for k in range(1, N + 1)]   # e(0)A(0) - e(lam0)A(lam0)
            d_diff, _ = defect(kappa, e0, 0, [r0, r1], [0, 0, s2], [t0, t1], e2)
            dQ = [d_diff[k] + kappa * e0 * (
                [F(0)] + [-a[j] for j in range(1, N + 1)])[k] for k in range(N + 1)]
            d_int = [dQ[k] - kappa * dS[k] for k in range(N + 1)]
            # closed form: dS = -e1 lam0 + e0 r0/2 lam0^2 + (e0 r1/6 + e1 r0/2) lam0^3
            assert dS[1] == -e1 and dS[2] == e0 * r0 / 2
            assert dS[3] == e0 * r1 / 6 + e1 * r0 / 2
            assert d_int[0] == 0
            assert d_int[1] == kappa * e1                    # (kappa/2pi)(k.grad eta_S) lam0
            assert d_diff[1] == 0                            # differences reading: no first-order term
            # and its next terms are those of check_focusing_leading_order (shear and expansion zero at p)
            assert d_diff[2] == kappa * (t0 - e0 * r0) / 2
            assert d_diff[3] == kappa * ((t1 + e2 * t0) / 3 - e0 * r1 / 6)
            if e1 == 0:
                assert d_int == d_diff
                agree += 1
    assert agree == len(ES)                                  # the e1 = 0 control ran for every e0
    return True


def check_dimension_enters_only_at_trace():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    eta3 = [1, -1, -1]
    nulls3 = [[F(1), F(1), F(0)], [F(1), F(-1), F(0)], [F(1), F(0), F(1)], [F(1), F(0), F(-1)],
              [F(1), F(3, 5), F(4, 5)], [F(1), F(4, 5), F(-3, 5)], [F(1), F(-5, 13), F(12, 13)]]
    pairs3 = [(a, b) for a in range(3) for b in range(a, 3)]
    for l in nulls3:
        assert sum((eta3[a] * l[a] * l[a] for a in range(3)), F(0)) == 0
    rows = [[(l[a] * l[b] if a == b else 2 * l[a] * l[b]) for (a, b) in pairs3] for l in nulls3]
    assert GA.mat_rank(rows) == 5
    gv = [F(eta3[a]) if a == b else F(0) for (a, b) in pairs3]
    assert all(sum((r[i] * gv[i] for i in range(6)), F(0)) == 0 for r in rows)
    # Bianchi in dimension n: dh - dR/2 = 0, dR - n dh = -kap dtau  =>  dh = kap dtau/(n - 2)
    kap, dtau = F(3), F(7, 5)
    for n in (3, 4, 5, 6):
        M = [[F(1), F(-1, 2)], [F(-n), F(1)]]
        rhs = [F(0), -kap * dtau]
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        dh = (rhs[0] * M[1][1] - M[0][1] * rhs[1]) / det
        assert dh == kap * dtau / (n - 2)
        assert (dh - kap * dtau / 2 == 0) == (n == 4)        # 4 pi G tau = kap tau/2 only in 4D
    return True


def check_newton_constant():
    premise("synthesis.c-loc-local-horizon-premise")
    premise("synthesis.imported-jacobson-clausius-1995")
    # 2 pi/eta_S = 8 pi G_cl: the pi's cancel, G_cl = 2/(8 eta_S) = 1/(4 eta_S)
    for eta_S in (F(1, 4), F(3), F(2, 9)):
        G_cl = F(2) / (8 * eta_S)
        assert G_cl == 1 / (4 * eta_S)
    # clause (i): eta_S G = 4 pi nu <s>. With nu = c/(pi L), <s> = b L: eta_S G = 4 c b (pi^0 L^0)
    for c in (F(1, 16), F(1, 8), F(3, 7)):
        for b in (F(1), F(1, 2)):
            etaG = 4 * c * b
            ratio = 1 / (4 * etaG)                            # G_cl/G = 1/(16 pi nu <s>) = 1/(16 c b)
            assert ratio == 1 / (16 * c * b)
            assert (ratio == 1) == (c * b == F(1, 16))
    # the registered value at zero weight, nu = 1/(16 pi ln 2), <s> = ln 2: c = 1/16, b = 1
    assert 1 / (16 * F(1, 16) * F(1)) == 1
    return True
