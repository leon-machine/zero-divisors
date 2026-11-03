"""dark-energy.forcing-half-schwarzschild-wall-residue-sense: exact checks of the computable core of the three
steps, in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)). The Kasner model at the wall is the synchronous diagonal field
hb^{-1}(e_t) = gamma0, hb^{-1}(e_i) = t^{p_i} gamma_i on labels (t, x1, x2, x3), with the rotation-gauge field
Omega(e_i) = (p_i/t) e_i ^ e_0 fixed by the torsion equation (exact first-order jets at t = 8, 27, 64, 1/8
where every t^{p_i} with p_i in thirds is rational). The store's curvature operator calR(B) = -R(hb(B)) and
its contraction calR(a) are computed from Omega. Computed:
(1) the pole: t Omega(e_i) = p_i e_i ^ e_0 at every sample time (a simple pole with residue p_i B_i up to the
    Definition's boost sign, tangential legs only, Omega(e_0) = 0), not removable since the residue is
    nonzero; the Schwarzschild interior has the same residue as the limit of its Hubble-normalised rates
    (exact series: -1/3, 2/3, 2/3);
(2) the residues satisfy the field equations: on the 4^3 triples from {-1/3, 0, 2/3, 1}, the Kasner field
    is Ricci-flat (calR(a) = 0) exactly on the 6 triples with sum p = sum p^2 = 1 (the permutations of
    (-1/3, 2/3, 2/3) and of (1, 0, 0)) and on the trivial field p = 0; B_w = sum p_i e_0 ^ e_i then has B_w^2 = sum p_i^2 = 1 (unit boost);
(3) the residues are the completion's weights: the weights are computed from the Schwarzschild interior
    coframe (2M = 1, u = sqrt r) as the leading powers of its spatial legs, sqrt(1/r - 1) = u^{-1}(1 - u^2)^{1/2}
    (from the Laurent series of 1/r - 1) and sqrt(r^2) = u^2: in r they are (-1/2, 1, 1), the forced weights of
    the cited theorem, the unique rescalings r^{-w} with a finite nonzero limit; the proper time
    tau = (2/3) u^3 + ... (exact series) converts them to (-1/3, 2/3, 2/3), the residues of (1); and the static
    and rain frames coincide at the wall: the boost (sinh chi, cosh chi) = (-sqrt r, m)/sqrt(m^2 - r) is unit
    and equals (0, 1) at r = 0, at three sample (m, r). The sheaf completion itself is not rebuilt.
The discharge of the three qualifications is carried by the cited propositions and is not recomputed.
"""
from fractions import Fraction as F

import GA
import gtg
import series
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, multivectors with jet coefficients, Field, torsion, curvature) ----
S13 = gtg.S13
qpow = series.qpow
J, Field, m_val, gbiv = gtg.J, gtg.Field, gtg.m_val, gtg.biv


# ---- the synchronous diagonal (Kasner) field on flat spacetime ----
def kasner_field(p, t0):
    """hb^{-1}(e_t) = gamma0, hb^{-1}(e_i) = t^{p_i} gamma_i (labels (t, x1, x2, x3)), with the rotation-gauge
    field Omega(e_i) = (p_i/t) e_i ^ e_0 of the Definition's convention (checked by the torsion equation)."""
    t = J.var(0, t0)
    TH = [[J(0)] * 4 for _ in range(4)]
    TH[0][0] = J(1)
    for i in range(3):
        TH[i + 1][i + 1] = t.pw(p[i])
    om = [{}] + [{(0, i + 1): -F(p[i]) / t} for i in range(3)]
    return Field(TH, om)


def ricci(Rc, b):
    """calR(gamma_b) = sum_a gamma^a . calR(gamma_a ^ gamma_b) (b an index)."""
    return gtg.ricci(Rc, GA.gen(b))


# ---- exact series of the Schwarzschild interior (2M = 1) in u = sqrt(r) ----
NS = 8


def interior_series(N=NS):
    """tau(u) = int_0^r sqrt(s/(1-s)) ds = int 2 v^2 (1 - v^2)^{-1/2} dv; returns (tau, tau sigma_1,
    tau sigma_2, R/u^2, tau/r) as coefficient lists in u, with sigma_1 = -(1/2) r^{-3/2} (1 - r)^{-1/2},
    sigma_2 = r^{-3/2} (1 - r)^{1/2}, R = (3 tau/2)^{2/3}."""
    w = GA.ps_pow_rat([F(1), F(0), F(-1)], F(-1, 2), N)
    tau = GA.ps_int(GA.ps_mul([F(0), F(0), F(2)], w, N))
    t3 = GA.ps_trunc(tau[3:], N)
    ts1 = [-c / 2 for c in GA.ps_mul(w, t3, N)]
    ts2 = GA.ps_mul(GA.ps_pow_rat([F(1), F(0), F(-1)], F(1, 2), N), t3, N)
    Ru2 = GA.ps_pow_rat([F(3, 2) * c for c in t3], F(2, 3), N)
    tau_over_r = [F(0)] + t3[:N]
    return tau, ts1, ts2, Ru2, tau_over_r


TIMES = [F(8), F(1, 8), F(64)]
THIRDS = [F(-1, 3), F(0), F(2, 3), F(1)]
SCHW_P = (F(-1, 3), F(2, 3), F(2, 3))
MS = [(F(1), F(3, 5)), (F(5, 4), F(3, 4)), (F(13, 12), F(5, 12))]          # (m, sqrt r) with m^2 - r a square
FORCED = (F(-1, 2), F(1), F(1))                                           # the cited theorem's weights in r


def check_simple_pole_with_kasner_residue():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    premise("dark-energy.imported-weighted-limit-schwarzschild-singularity-matching")
    ok = True
    for t0 in TIMES:
        fld = kasner_field(SCHW_P, t0)
        ok = ok and fld.torsion_free() and m_val(fld.om[0]) == {}
        for i in range(3):
            res = GA.scal(t0, m_val(fld.om[i + 1]))
            ok = ok and GA.eq(res, GA.scal(-SCHW_P[i], gbiv(0, i + 1)))
            ok = ok and res != {}
    tau, ts1, ts2, Ru2, tor = interior_series()
    _tp_rv = (ok and (ts1[0], ts2[0], ts2[0]) == SCHW_P); assert _tp_rv is not False, "check_simple_pole_with_kasner_residue"; return _tp_rv


def check_residues_satisfy_the_field_equations():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    vac = []
    for a in THIRDS:
        for b in THIRDS:
            for c in THIRDS:
                fld = kasner_field((a, b, c), F(8))
                if all(ricci(fld.curvature(), j) == {} for j in range(4)):
                    vac.append((a, b, c))
    flat = [p for p in vac if p == (0, 0, 0)]
    ok = len(vac) == 7 and len(flat) == 1
    ok = ok and all(sum(p) == 1 and sum(x * x for x in p) == 1 for p in vac if p not in flat)
    ok = ok and SCHW_P in vac and (F(1), F(0), F(0)) in vac
    Bw = GA.add(*[GA.scal(SCHW_P[i], gbiv(0, i + 1)) for i in range(3)])
    _tp_rv = (ok and GA.eq(GA.mul(Bw, Bw, S13), GA.sc(1))); assert _tp_rv is not False, "check_residues_satisfy_the_field_equations"; return _tp_rv


def boost(m, s):
    root = qpow(m * m - s * s, F(1, 2))
    return -s / root, m / root


def check_residues_are_the_completion_weights():
    premise("sheaf.weights-are-forced-are-kasner-exponents")
    premise("sheaf.matching-fibre")
    premise("sheaf.matching-connection-level")
    tau = interior_series()[0]
    vt = series.ps_valuation(tau)
    ok = vt == 3 and tau[vt] == F(2, 3)                      # tau = (2/3) r^{3/2} + ...
    # spatial legs of the interior coframe: sqrt of 1/r - 1 = u^{-2}(1 - u^2) and of r^2 = u^4, as Laurent series
    metric = [series.laurent([F(1), F(0), F(-1)], -2), series.laurent([F(1)], 4), series.laurent([F(1)], 4)]
    legs = []
    for v, c in metric:
        ok = ok and v % 2 == 0 and c[0] == 1
        legs.append((v // 2, series.ps_pow_rat(c, F(1, 2), NS)))
    weights = tuple(F(v, 2) for v, _ in legs)               # leading power in r of each leg
    ok = ok and weights == FORCED and all(c[0] == 1 for _, c in legs)
    exps = tuple(F(v, vt) for v, _ in legs)                 # r^{v/2} = tau^{v/vt} at leading order
    ok = ok and exps == SCHW_P and sum(exps) == 1 and sum(e * e for e in exps) == 1
    for m, s in MS:
        sh, ch = boost(m, s)
        ok = ok and ch * ch - sh * sh == 1 and sh < 0 < ch
        ok = ok and boost(m, F(0)) == (0, 1)                 # at the wall the two frames coincide
    _tp_rv = (ok); assert _tp_rv is not False, "check_residues_are_the_completion_weights"; return _tp_rv

