"""synthesis.collar-kms-extension-completion-locus: exact checks.

Units 2M = 1: A = 1/r - 1, horizon r = 1, kappa = 1/2. The ladder pair exists only over the
exceptional set E (completion Fact); the synchronous frame is parallel along d/dtau (collar Fact).
Hypothesis (E): the boundary-mode atom read on the slice r at (t, theta, phi) is the E-atom at
(t, theta, phi), carried along the tau-line through it.

check_killing_bivector_parallel_carry: for a diagonal metric -dtau^2 + a(tau)^2 dt^2 (a any
rational function, two samples) the Christoffel symbol from the metric gives nabla_tau (a^{-1} d_t) = 0
and the Killing bivector of d_t is a' e0 e1; with a^2 = A(r), dr/dtau = a it is (A'/2) e0 e1, of
magnitude rho(r) = 1/(2 r^2). Carried to E (parallel frame) the slice generators are rho(r) e0 e1/2,
pairwise proportional (checked in Cl(1,3)), so every slice acts on the same atom through one K.

check_one_atom_kms_every_slice: the atom of the completed pair in Cl(1,1) has sigma = e0 e1 = B1,
K = sigma/2. With z = e^{pi} kept as a formal variable (rational functions in z), the Gibbs state
of rapidity period 2 pi is KMS, on all matrix units, for the flow of generator c K at beta exactly
when beta c = 2 pi; this holds for the Killing parametrisation on the slices r = 1, 1/2, 1/4
(beta = 4 pi r^2) and for the Hubble parametrisation at E (rate 1/3, beta = 6 pi), and on two
E-points (4 x 4). Contrast: the slice-product reading (C) with two independent slice atoms at
r = 1, 1/2 (generator rho(1) K1 + rho(1/2) K2) admits no beta for which that product is KMS.
The local Hubble value 2 pi / rho_H(r) = 6 pi (1 - 4 r/5 + ...) is computed as a series.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

N = 6


def S_series(n):
    out, c = [], F(1)
    for k in range(n + 1):
        if k > 0:
            c = c * F(2 * k - 1, 2 * k)
        out.append(c * F(3, 2 * k + 3))
    return out


def check_killing_bivector_parallel_carry():
    premise("singularity.imported-interior-collar-kasner-form")
    premise("singularity.modular-flow-boundary-modes-holonomy-universal")
    vals = []
    for a in [GA.RF([F(1), F(2)], [F(3), F(-1)]), GA.RF([F(1), F(0), F(1)], [F(1)])]:
        gtt = a * a
        Gamma = GA.RF.const(F(1, 2)) * gtt.deriv() / gtt          # Gamma^t_{tau t} = (1/2) g^tt d_tau g_tt
        inv_a = GA.RF.const(F(1)) / a
        nabla = inv_a.deriv() + inv_a * Gamma                       # nabla_tau (a^{-1} d_t), t-component
        assert nabla.is_zero()
        # Killing bivector of xi = d_t: (1/2) d_tau(g_tt) in coordinates, divided by |d_tau||d_t| = a
        F01 = GA.RF.const(F(1, 2)) * gtt.deriv() / a
        assert F01.eqrf(a.deriv())
        assert not (Gamma * GA.RF.const(F(2))).eqrf(Gamma)          # nonzero connection: the identity has content
        vals.append((F01.eval(F(0)), F01.eval(F(1)), Gamma.eval(F(1))))
    # samples: a = (1 + 2s)/(3 - s) has a' = 7/(3 - s)^2; a = 1 + s^2 has a' = 2s, Gamma = 2s/(1 + s^2)
    assert vals == [(F(7, 9), F(7, 4), F(7, 6)), (F(0), F(2), F(1))]
    # a^2 = A(r), dr/dtau = a, so a' = (dA/dr)(dr/dtau)/(2a) = A'/2: the rate on the slice r
    A = GA.RF([F(1), F(-1)], [F(0), F(1)])
    rate = A.deriv() * GA.RF.const(F(-1, 2))
    assert rate.eqrf(GA.RF([F(1, 2)], [F(0), F(0), F(1)]))         # rho = 1/(2 r^2)
    assert rate.eval(F(1)) == F(1, 2)                               # kappa at the horizon
    assert [rate.eval(r) for r in [F(1, 2), F(1, 4), F(1, 8)]] == [F(2), F(8), F(32)]
    # carry to E in Cl(1,3): frame components constant along tau, so the slice-r generator is rho(r) e0e1/2
    sq = GA.sig(1, 3)
    B1 = GA.mul(GA.gen(0), GA.gen(1), sq)
    B2 = GA.mul(GA.gen(0), GA.gen(2), sq)
    gens = {r: GA.scal(rate.eval(r) / 2, B1) for r in [F(1), F(1, 2), F(1, 4), F(1, 8)]}
    for r1, g1 in gens.items():
        for r2, g2 in gens.items():
            assert GA.eq(GA.scal(rate.eval(r2), g1), GA.scal(rate.eval(r1), g2))   # proportional
            assert GA.commutes(g1, g2, sq)
    assert not GA.commutes(B1, B2, sq)                              # a sphere boost would not be
    assert gens[F(1, 2)] == GA.scal(4, gens[F(1)])
    return True


def mm(X, Y):
    n = len(X)
    return [[sum((X[i][l] * Y[l][j] for l in range(n)), GA.RF.const(F(0))) for j in range(n)]
            for i in range(n)]


def tr(X):
    return sum((X[i][i] for i in range(len(X))), GA.RF.const(F(0)))


def dg(xs):
    z0 = GA.RF.const(F(0))
    return [[xs[i] if i == j else z0 for j in range(len(xs))] for i in range(len(xs))]


def zpow(m):
    # z^m for integer m as a rational function of the formal variable z = e^{pi}
    z = GA.RF.var()
    out = GA.RF.const(F(1))
    for _ in range(abs(m)):
        out = out * z
    return out if m >= 0 else GA.RF.const(F(1)) / out


def kms_holds(rho_diag, flow_diag):
    """KMS on all matrix units: tr(rho A e^{-bH} B e^{bH}) = tr(rho B A); flow_diag = diag of e^{-bH}."""
    n = len(rho_diag)
    one, zero = GA.RF.const(F(1)), GA.RF.const(F(0))
    R, Ef = dg(rho_diag), dg(flow_diag)
    Ei = dg([one / x for x in flow_diag])
    units = [[[one if (i, j) == (a, b) else zero for j in range(n)] for i in range(n)]
             for a in range(n) for b in range(n)]
    for X in units:
        for Y in units:
            if not tr(mm(R, mm(X, mm(Ef, mm(Y, Ei))))).eqrf(tr(mm(R, mm(Y, X)))):
                return False
    return True


def check_one_atom_kms_every_slice():
    premise("singularity.imported-one-sided-completion-singularity")
    premise("singularity.modular-structure-completed-pair")
    premise("singularity.kms-uniqueness-factor")
    premise("singularity.rate-rigidity-temperature-not-algebra-intrinsic")
    premise("singularity.modular-flow-boundary-modes-holonomy-universal")
    sq = GA.sig(1, 1)
    e0, e1 = GA.gen(0), GA.gen(1)
    v = GA.scal(F(1, 2), GA.add(e0, e1))
    vs = GA.scal(F(1, 2), GA.sub(e0, e1))
    assert GA.mul(v, v, sq) == {} and GA.eq(GA.add(GA.mul(v, vs, sq), GA.mul(vs, v, sq)), GA.sc(1))
    sigma = GA.sub(GA.mul(vs, v, sq), GA.mul(v, vs, sq))
    assert GA.eq(sigma, GA.mul(e0, e1, sq))                         # sigma = B1: K = B1/2
    # one atom, basis |0>, |1>: K = diag(-1/2, 1/2); e^{-beta c K} = diag(z^m, z^-m), m = beta c/(2 pi)
    Z = zpow(1) + zpow(-1)
    state = [zpow(1) / Z, zpow(-1) / Z]                             # rapidity period 2 pi
    rate = {F(1): F(1, 2), F(1, 2): F(2), F(1, 4): F(8)}            # rho(r) = 1/(2 r^2)
    for r, c in rate.items():
        beta_over_pi = 2 / c                                        # Killing inverse temperature / pi
        assert beta_over_pi == 4 * r * r
        m = beta_over_pi * c / 2
        assert m == 1
        assert kms_holds(state, [zpow(1), zpow(-1)])
    # Hubble parametrisation at E: rate |p1| = 1/3, beta_H = 6 pi
    S = S_series(N)
    one_minus_r = [F(1), F(-1)] + [F(0)] * (N - 1)
    rhoH = [F(1, 3) * c for c in GA.ps_mul(S, GA.ps_pow_rat(one_minus_r, F(-1, 2), N), N)]
    assert rhoH[:2] == [F(1, 3), F(4, 15)]
    betaH_over_pi = [2 * c for c in GA.ps_inv(rhoH, N)]             # local Hubble value / pi on slice r
    assert betaH_over_pi[:2] == [F(6), F(-24, 5)]
    assert betaH_over_pi[0] * rhoH[0] / 2 == 1                      # m = 1 at E: KMS at 6 pi
    # wrong period fails: m = 2 is not KMS for this state
    assert not kms_holds(state, [zpow(2), zpow(-2)])
    # two E-points, generator c (K1 + K2): product state KMS for every slice parametrisation
    st2 = [state[a] * state[b] for a in (0, 1) for b in (0, 1)]
    flow2 = [zpow(1 - 2 * a) * zpow(1 - 2 * b) for a in (0, 1) for b in (0, 1)]
    assert kms_holds(st2, flow2)
    # slice-product reading (C): slices r = 1 and r = 1/2 as independent atoms, generator
    # rho(1) K1 + rho(1/2) K2 with rho(1/2)/rho(1) = 4; e^{-beta H} has exponents (m, 4m) and m = 1 or 1/4
    # would be needed on the two factors at once
    for m1, m2 in [(1, 4), (-1, -4), (2, 8)]:
        flowC = [zpow(m1 * (1 - 2 * a)) * zpow(m2 * (1 - 2 * b)) for a in (0, 1) for b in (0, 1)]
        assert not kms_holds(st2, flowC)
    assert rate[F(1, 2)] / rate[F(1)] == 4
    return True
