"""dark-energy.variable-exponents-residue-pointwise-corrections-are: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3), labels (tau, x1, x2, x3); hb^{-1}(e_tau) = gamma0, hb^{-1}(e_i) = tau^{p_i(x)} gamma_i (the
coframe e^0 = d tau, e^i = tau^{p_i(x)} dx^i). At a point tau0 with tau0^{p_i} rational, the first-order jets of
the coframe are exact except for log(tau0), which (as in the proof's script) is replaced by independent rational
placeholders L, together with placeholder gradients d_j p_i: the identities checked are polynomial in them.
(1) The displayed connection, omega^{i0} = (p_i/tau) e^i and omega^{ij} = L[(d_i p_j) tau^{-p_i} e^j -
    (d_j p_i) tau^{-p_j} e^i], assembled into Omega(gamma_c) (omega^i_j = -omega^{ij}), satisfies the torsion
    equation of the GTG field exactly, and the torsion map has rank 24, so it is the rotation-gauge field; its
    boost entries are exactly -(p_i/tau) on gamma_0 ^ gamma_i whatever the gradients (the pointwise Kasner pole with
    no correction). With the opposite tangential sign the torsion equation fails (the sign is not a convention).
(2) Exponent arithmetic only: the relative orders tau^{1 - p_j} and tau^{2 - p_j - p_k} that the proof assigns to
    the curvature terms beyond the double pole are entered as that list (they are not computed from the field,
    and the log powers m <= 2 are not tested); at rational points of the Kasner circle the list's minimal exponent
    is 1 - p_max, positive on the open circle (p_max < 1) and zero exactly at the excluded points, the
    permutations of (0, 0, 1).
(3) The wall equations pointwise: the constant-exponent Kasner field (premise frozen-point datum) computed from its
    gauge fields is Ricci-flat (calR(a) = 0) at circle points, and not for (1/3, 1/3, 1/3) (sum p^2 != 1): at each x
    the leading equations are the Kasner relations of p(x). The counterterm density 8 p1 p2 p3 is the premise's
    value read pointwise and is not recomputed.
"""
from fractions import Fraction as F

import GA
import gtg
import series
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (jets, multivectors with jet coefficients, Field, torsion, curvature) ----
qpow = series.qpow
J, Field, omega_forms, m_val = gtg.J, gtg.Field, gtg.omega_forms, gtg.m_val


def ricci(Rc, b):
    """calR(gamma_b) = sum_a gamma^a . calR(gamma_a ^ gamma_b) (b an index)."""
    return gtg.ricci(Rc, GA.gen(b))

# (p, tau0) with tau0^{p_i} rational
POINTS = [((F(-1, 3), F(2, 3), F(2, 3)), F(1, 64)), ((F(-2, 7), F(3, 7), F(6, 7)), F(1, 128)),
          ((F(0), F(0), F(1)), F(1, 4)), ((F(-3, 13), F(12, 13), F(4, 13)), F(1, 2) ** 13)]
DP = [[F(0), F(7), F(-2)], [F(3), F(0), F(4)], [F(-5), F(6), F(1, 3)]]       # DP[j][i] = d_j p_i
LS = [F(-3), F(5, 2)]
KASNER_T = [F(1), F(2), F(1, 2), F(-3), F(5, 3), F(0)]


def varexp_field(p, tau0, L, sign):
    TH = [[J(0)] * 4 for _ in range(4)]
    TH[0][0] = J(1)
    a = [qpow(tau0, p[i]) for i in range(3)]
    for i in range(3):
        grad = [p[i] * a[i] / tau0] + [DP[j][i] * L * a[i] for j in range(3)]
        TH[i + 1][i + 1] = J(a[i], grad)
    spec = []
    for i in range(3):
        spec.append((i + 1, i + 1, 0, J(p[i] / tau0)))
        for j in range(i + 1, 3):
            # omega^i_j(gamma_c) = -omega^{ij}(gamma_c): c = j gives -L d_i p_j tau^{-p_i}, c = i gives L d_j p_i tau^{-p_j}
            spec.append((j + 1, i + 1, j + 1, J(-sign * L * DP[i][j] / a[i])))
            spec.append((i + 1, i + 1, j + 1, J(sign * L * DP[j][i] / a[j])))
    return Field(TH, omega_forms(spec))


def kasner_point(t):
    d = 1 + t + t * t
    return [-t / d, (1 + t) / d, t * (1 + t) / d]


def check_displayed_connection_is_torsion_free():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    ok = True
    for p, tau0 in POINTS:
        for L in LS:
            fld = varexp_field(p, tau0, L, 1)
            ok = ok and fld.torsion_free() and fld.torsion_rank() == 24
            for i in range(3):
                ok = ok and m_val(fld.om[i + 1]).get((0, i + 1), F(0)) == -p[i] / tau0
            bad = varexp_field(p, tau0, L, -1)
            ok = ok and not bad.torsion_free()
    _tp_rv = (ok); assert _tp_rv is not False, "check_displayed_connection_is_torsion_free"; return _tp_rv


def check_listed_correction_orders_positive_on_open_circle():
    ok = True
    for t in KASNER_T:
        p = kasner_point(t)
        ok = ok and sum(p) == 1 and sum(x * x for x in p) == 1
        exps = [1 - pj for pj in p] + [2 - p[j] - p[k] for j in range(3) for k in range(3)]
        ok = ok and min(exps) == 1 - max(p)
        ok = ok and (max(p) < 1) == (min(exps) > 0)
        ok = ok and (max(p) == 1) == (sorted(p) == [0, 0, 1])
    _tp_rv = (ok); assert _tp_rv is not False, "check_listed_correction_orders_positive_on_open_circle"; return _tp_rv


def check_kasner_relations_pointwise():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    ok = True
    for p, tau0, flat in [(POINTS[0][0], POINTS[0][1], True), (POINTS[1][0], POINTS[1][1], True),
                          ((F(1, 3), F(1, 3), F(1, 3)), F(1, 8), False)]:
        TH = [[J(0)] * 4 for _ in range(4)]
        TH[0][0] = J(1)
        om = [{}]
        for i in range(3):
            ai = qpow(tau0, p[i])
            TH[i + 1][i + 1] = J(ai, (p[i] * ai / tau0, 0, 0, 0))
            om.append({(0, i + 1): J(-p[i] / tau0, (p[i] / (tau0 * tau0), 0, 0, 0))})
        fld = Field(TH, om)
        ok = ok and fld.torsion_free()
        Rc = fld.curvature()
        ric_zero = all(ricci(Rc, b) == {} for b in range(4))
        ok = ok and ric_zero == flat and (sum(p) == 1 and sum(x * x for x in p) == 1) == flat
    _tp_rv = (ok); assert _tp_rv is not False, "check_kasner_relations_pointwise"; return _tp_rv
