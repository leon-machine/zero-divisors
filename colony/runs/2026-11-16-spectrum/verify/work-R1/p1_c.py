"""synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit: exact checks.

Field (conformal time eta = label 0, momentum k along label 1, first order in eps, eps carried as jet label 4):
  hb^-1(e_0) = a (1 + eps phi cos kx) e_0,   hb^-1(e_1) = a (1 - eps psi cos kx) e_1 + eps a b sin kx e_0,
  hb^-1(e_j) = a (1 - eps psi cos kx) e_j  (j = 2, 3),
with a, phi, psi, b given by their Taylor coefficients at a rational point (generic rationals). The rotation-gauge
field is solved from the torsion equation and the field strength, Ricci and Einstein maps are contracted exactly
by lib/gtg.py (store sign: n.G(n) = -8 pi rho for the unit normal n). Nothing is assumed about the linearised
Einstein map: every coefficient below is read off the engine's output.

(1) Omega to first order; n.G(n), m_1.G(n); the expansion D.n of the slice normal; the scalar curvature of the
    slice's induced field (a field on Cl(0,3)); the Gauss relation; hence the energy constraint
    (k/a)^2 psi = H kappa - (3/2) H^2 delta and 3R = 6 H^2 (delta - 2 delta_H).
(2) Under a relabelling of time (phi, psi, b) -> (phi + xi' + Hc xi, psi - Hc xi, b - k xi) the combinations
    psi + u, -psi + delta/(3(1+w)), delta + 3(1+w) u and psi - Hc b/k are unchanged, on a generic background;
    k^2 (psi - Hc b/k) = -(3/2) Hc^2 (delta + 3(1+w) u) (the Poisson relation, every slice).
(3) Radiation field a = eta: in the zero-shear slicing with phi = psi = A the spatial and normal components give
    A'' + 4 A'/eta + k^2 A/3 = 0; exact series of the two solutions; the comoving curvature perturbation of the
    decaying solution is cos x/(2x); the projection zeta_inf = -[R (cos x + x sin x) + (delta_c/4) cos x].
(4) The three readings (uniform expansion, flat slice, flat slice with matter at rest) and their indices.
(5) The thermal deposit: fluctuation identities, the coefficient 135/(pi^4 g), the closed form
    (g^(2/3) g_s0^(1/3)/60)(T_d/M_P)^4 (a_0 T_0/k_*) at the pivot, and its values on the window.
"""
from fractions import Fraction as F

import GA
import gtg
from gtg import Jet
from GA import RF
from tp_premise import premise

NV = 5
ORD = 3
Z0 = (0, 0, 0, 0, 0)
E1 = (0, 0, 0, 0, 1)

# generic rational samples: Taylor coefficients (value, first derivative, half the second, ...) at the point
BACKGROUNDS = ([F(2), F(3), F(5, 7), F(1, 3)], [F(3, 2), F(-1, 4), F(2, 5), F(1, 6)])
PHI = [F(7, 3), F(1, 2), F(-2, 5), F(1, 7)]
PSI = [F(5, 2), F(-1, 3), F(3, 4), F(2, 7)]
BSH = [F(1, 4), F(2, 3), F(-3, 5), F(1, 9)]
XI = [F(2, 5), F(-3, 7), F(1, 3), F(5, 11), F(1, 13)]
WAVES = ((F(3, 2), F(3, 5), F(4, 5)), (F(2, 3), F(5, 13), F(12, 13)))     # (k, sin kx, cos kx) at the point


def tay(coeffs):
    j = Jet.from_taylor(0, list(coeffs)[:ORD + 1], NV)
    return Jet(c=dict(j.c), nv=NV, order=ORD)


def build(a_c, phi_c, psi_c, b_c, k, s0, c0):
    a, phi, psi, b = tay(a_c), tay(phi_c), tay(psi_c), tay(b_c)
    sn, cs = gtg.jsincos(Jet.var(1, F(0), NV, ORD) * k, s0, c0)
    eps = Jet.var(4, F(0), NV, ORD)
    one = Jet(1, None, NV, ORD)
    TH = [[F(0)] * 4 for _ in range(4)]
    TH[0][0] = a * (one + eps * phi * cs)
    TH[0][1] = eps * a * b * sn
    for i in range(1, 4):
        TH[i][i] = a * (one - eps * psi * cs)
    return gtg.Field(TH, sq=gtg.S13)


def split(j):
    """(zeroth, first) order in eps at the point"""
    if isinstance(j, Jet):
        return j.coeff(Z0), j.coeff(E1)
    return F(j), F(0)


def frame_vectors(bs):
    """unit normal n = e_0 + eps b sin e_1 of the slices eta = const and unit tangent m_1 = e_1 + eps b sin e_0"""
    eps = Jet.var(4, F(0), NV, 1)
    one = Jet(1, None, NV, 1)
    return {(0,): one, (1,): eps * bs}, {(1,): one, (0,): eps * bs}, {(2,): one}


def einstein_components(fld, bs):
    Rc = fld.curvature_jet()
    n, m1, e2 = frame_vectors(bs)
    Gn = gtg.einstein(Rc, n)
    return {"nn": split(gtg.vdot(n, Gn)), "n1": split(gtg.vdot(m1, Gn)),
            "11": split(gtg.vdot(m1, gtg.einstein(Rc, m1))), "22": split(gtg.vdot(e2, gtg.einstein(Rc, e2)))}


def expansion(fld):
    """theta = D.n for the unit normal n = hb^T(e^0)/|hb^T(e^0)| of the slices (jets), with the normal itself"""
    HJ = fld.hb_matrix_jet()
    g0 = {(c,): HJ[0][c] * fld.sq[c] for c in range(4) if HJ[0][c]}
    norm = gtg.vdot(g0, g0, fld.sq).pw(F(-1, 2))
    n = {bl: x * norm for bl, x in g0.items()}
    th = None
    for c in range(4):
        dn = gtg.comm(fld.om[c], n, fld.sq)
        for mu in range(4):
            if HJ[mu][c]:
                dn = gtg.m_add(dn, gtg.m_scal(HJ[mu][c], gtg.m_d(n, mu)))
        t = gtg.vdot(gtg.er(c, fld.sq), dn, fld.sq)
        th = t if th is None else th + t
    return n, split(th)


def slice_scalar_curvature(scale):
    """scalar curvature of the 3-field hb^-1(e_i) = scale(x) e_i on Cl(0,3); labels 0..2, eps = label 3;
    returned with the sign in which the round sphere is positive (see the control in check (1))"""
    sq3 = GA.sig(0, 3)
    TH = [[F(0)] * 3 for _ in range(3)]
    for i in range(3):
        TH[i][i] = scale
    fld = gtg.Field(TH, sq=sq3)
    return gtg.ricci_scalar(fld.curvature_jet(), sq3)


def slice_data(a_c, phi_c, psi_c, b_c, k, s0, c0):
    """slice data read off the engine: (delta, u, kappa*a, 1 + w, Hc) with rho, p from the background field
    equation, delta = first-order n.G(n) over its background value, v from m_1.G(n) = 8 pi (rho + p) v sin,
    u = (Hc/k) v"""
    fld = build(a_c, phi_c, psi_c, b_c, k, s0, c0)
    G = einstein_components(fld, b_c[0] * s0)
    _, th = expansion(fld)
    a0 = a_c[0]
    Hc = a_c[1] / a0
    rho8, p8 = -G["nn"][0], -G["11"][0]              # 8 pi rho, 8 pi p
    delta = G["nn"][1] / G["nn"][0] / c0
    v = G["n1"][1] / (rho8 + p8) / s0
    return {"delta": delta, "u": Hc * v / k, "kappa_a": th[1] * a0 / c0, "w1": (rho8 + p8) / rho8, "Hc": Hc,
            "G": G, "theta": th, "fld": fld}


def shifted(a_c, phi_c, psi_c, b_c, xi_c, k):
    """the same field in the time label eta + eps xi cos kx: (phi + xi' + Hc xi, psi - Hc xi, b - k xi) as jets"""
    a = Jet.from_taylor(0, a_c, 1)
    xi = Jet.from_taylor(0, xi_c, 1)
    Hc = a.d(0) / a.trunc(2)
    xi2 = xi.trunc(2)
    lst = lambda j: [j.coeff((n,)) for n in range(3)]
    phi = [x + y + z for x, y, z in zip(phi_c, lst(xi.d(0)), lst(Hc * xi2))]
    psi = [x - y for x, y in zip(psi_c, lst(Hc * xi2))]
    b = [x - k * y for x, y in zip(b_c, lst(xi2))]
    return phi, psi, b


# ----------------------------------------------------------------------------------------------- series in x
def fact(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def sadd(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def sshift(p, m, c=1):
    return {e + m: v * c for e, v in p.items()}


def sder(p):
    return {e - 1: c * e for e, c in p.items() if e}


def smul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            out[e1 + e2] = out.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in out.items() if c}


def below(p, top):
    return {e: c for e, c in p.items() if e <= top}


def trig_series(top):
    sin = {n: F((-1) ** ((n - 1) // 2), fact(n)) for n in range(1, top + 8, 2)}
    cos = {n: F((-1) ** (n // 2), fact(n)) for n in range(0, top + 8, 2)}
    return sin, cos


# ------------------------------------------------------------------------------------------------ the checks
def check_constraints_of_the_perturbed_field_from_the_field_equation():
    premise("synthesis.imported-gtg-dictionary")
    for a_c in BACKGROUNDS:
        for k, s0, c0 in WAVES:
            a0, Hc = a_c[0], a_c[1] / a_c[0]
            phi, dphi = PHI[0], PHI[1]
            psi, dpsi = PSI[0], PSI[1]
            b, db = BSH[0], BSH[1]
            d = slice_data(a_c, PHI, PSI, BSH, k, s0, c0)
            fld, G, th = d["fld"], d["G"], d["theta"]
            GA.check("the field is torsion free", fld.torsion_free())
            # rotation-gauge field to first order
            Om = [{bl: split(x) for bl, x in fld.Om[mu].items() if split(x) != (0, 0)} for mu in range(4)]
            boost = (-Hc, (Hc * (phi + psi) + dpsi) * c0)
            GA.check("Omega(e_0) = (k phi + b' + Hc b) sin e_0 e_1",
                     Om[0] == {(0, 1): (0, (k * phi + db + Hc * b) * s0)})
            GA.check("Omega(e_1) = -(Hc - (Hc phi + Hc psi + psi') cos) e_0 e_1", Om[1] == {(0, 1): boost})
            GA.check("Omega(e_j) = boost part + (k psi - Hc b) sin e_1 e_j",
                     Om[2] == {(0, 2): boost, (1, 2): (0, (k * psi - Hc * b) * s0)}
                     and Om[3] == {(0, 3): boost, (1, 3): (0, (k * psi - Hc * b) * s0)})
            # Einstein map on the slice normal (store sign: n.G(n) = -8 pi rho)
            GA.check("background n.G(n) = -3 Hc^2/a^2", G["nn"][0] == -3 * Hc ** 2 / a0 ** 2)
            GA.check("first-order n.G(n) = (2/a^2)(k^2 psi + 3 Hc (psi' + Hc phi) - Hc k b) cos",
                     G["nn"][1] == 2 * (k ** 2 * psi + 3 * Hc * (dpsi + Hc * phi) - Hc * k * b) * c0 / a0 ** 2)
            GA.check("first-order m_1.G(n) = (2/a^2) k (psi' + Hc phi) sin, background zero",
                     G["n1"] == (0, 2 * k * (dpsi + Hc * phi) * s0 / a0 ** 2))
            # expansion of the normal congruence
            GA.check("theta = 3 Hc/a + (-3 (psi' + Hc phi) + k b) cos / a",
                     th == (3 * Hc / a0, (-3 * (dpsi + Hc * phi) + k * b) * c0 / a0))
            # scalar curvature of the slice's induced field (function of the slice's own data psi only)
            nv = 4
            sn, cs = gtg.jsincos(Jet.var(0, F(0), nv, ORD) * k, s0, c0)
            scale = (Jet(1, None, nv, ORD) - Jet.var(3, F(0), nv, ORD) * cs * psi) * a0
            R3 = slice_scalar_curvature(scale)
            R3 = (R3.coeff((0, 0, 0, 0)), R3.coeff((0, 0, 0, 1)))
            GA.check("3R = -4 (k/a)^2 psi cos", R3 == (0, -4 * k ** 2 * psi * c0 / a0 ** 2))
            # Gauss relation at zeroth and first order: 3R + (2/3) theta^2 + 2 n.G(n) = 0
            GA.check("Gauss relation, zeroth order", R3[0] + F(2, 3) * th[0] ** 2 + 2 * G["nn"][0] == 0)
            GA.check("Gauss relation, first order", R3[1] + F(4, 3) * th[0] * th[1] + 2 * G["nn"][1] == 0)
            # energy constraint in slice data: (k/a)^2 psi = H kappa - (3/2) H^2 delta, 3R = 6 H^2 (delta - 2 delta_H)
            H = Hc / a0
            kappa = d["kappa_a"] / a0
            GA.check("energy constraint", (k / a0) ** 2 * psi == H * kappa - F(3, 2) * H ** 2 * d["delta"])
            GA.check("3R = 6 H^2 (delta - 2 delta_H)",
                     R3[1] / c0 == 6 * H ** 2 * (d["delta"] - 2 * kappa / (3 * H)))
            GA.check("control: the uniform-expansion relation does not hold for generic data",
                     (k / a0) ** 2 * psi != -F(3, 2) * H ** 2 * d["delta"])
    # sign control for the slice curvature: the unit 3-sphere in stereographic labels, scale 1/(1 + r^2/4)
    nv = 4
    r2 = sum((Jet.var(i, F(0), nv, ORD) ** 2 for i in range(3)), Jet(0, None, nv, ORD))
    sphere = slice_scalar_curvature((Jet(1, None, nv, ORD) + r2 * F(1, 4)).inv())
    GA.check("unit round sphere has scalar curvature +6 in the sign used", sphere.coeff((0, 0, 0, 0)) == 6)
    return True


def check_slice_independent_combinations_and_the_poisson_relation():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.imported-superhorizon-zeta-conservation")
    for a_c in BACKGROUNDS:
        for k, s0, c0 in WAVES:
            d0 = slice_data(a_c, PHI, PSI, BSH, k, s0, c0)
            phi2, psi2, b2 = shifted(a_c, PHI, PSI, BSH, XI, k)
            d1 = slice_data(a_c, phi2, psi2, b2, k, s0, c0)
            w1, Hc = d0["w1"], d0["Hc"]
            GA.check("background 1 + w is the same on both slicings and generic", d1["w1"] == w1 and w1 != F(4, 3))
            GA.check("the slicings differ", psi2[0] != PSI[0] and d1["delta"] != d0["delta"] and d1["u"] != d0["u"])
            GA.check("u shifts by Hc xi", d1["u"] - d0["u"] == Hc * XI[0])
            GA.check("delta shifts by -3 (1 + w) Hc xi", d1["delta"] - d0["delta"] == -3 * w1 * Hc * XI[0])
            GA.check("R = psi + u is slice independent", psi2[0] + d1["u"] == PSI[0] + d0["u"])
            GA.check("zeta = -psi + delta/(3(1+w)) is slice independent",
                     -psi2[0] + d1["delta"] / (3 * w1) == -PSI[0] + d0["delta"] / (3 * w1))
            GA.check("delta_c = delta + 3(1+w) u is slice independent",
                     d1["delta"] + 3 * w1 * d1["u"] == d0["delta"] + 3 * w1 * d0["u"])
            GA.check("Psi = psi - Hc b/k is slice independent",
                     psi2[0] - Hc * b2[0] / k == PSI[0] - Hc * BSH[0] / k)
            for dd, ps, bb in ((d0, PSI, BSH), (d1, psi2, b2)):
                GA.check("Poisson relation k^2 Psi = -(3/2) Hc^2 delta_c on every slice",
                         k ** 2 * (ps[0] - Hc * bb[0] / k) == -F(3, 2) * Hc ** 2 * (dd["delta"] + 3 * w1 * dd["u"]))
                GA.check("u = 2 (psi' + Hc phi)/(3 (1+w) Hc) is not zero on the samples", dd["u"] != 0)
    return True


def check_radiation_equation_and_the_growing_mode_projection():
    premise("synthesis.imported-large-scale-potential-and-sachs-wolfe-relations")
    premise("synthesis.imported-superhorizon-zeta-conservation")
    zero = [F(0)] * 4
    for eta0 in (F(2), F(5, 3)):
        for k, s0, c0 in WAVES:
            a_c = [eta0, F(1), F(0), F(0)]                 # a = eta: the radiation field in conformal time
            A, dA, ddA = PHI[0], PHI[1], 2 * PHI[2]
            G = einstein_components(build(a_c, PHI, PHI, zero, k, s0, c0), F(0))
            GA.check("radiation background: p = rho/3", G["11"][0] * 3 == G["nn"][0])
            GA.check("zero-shear slicing, phi = psi: isotropic stress", G["11"][1] == G["22"][1])
            GA.check("delta p = delta rho/3 is A'' + 4 A'/eta + k^2 A/3 = 0",
                     G["11"][1] - G["nn"][1] / 3 == -2 * (ddA + 4 * dA / eta0 + k ** 2 * A / 3) * c0 / eta0 ** 2)
            G2 = einstein_components(build(a_c, PSI, PHI, zero, k, s0, c0), F(0))
            GA.check("phi != psi gives anisotropic stress -k^2 (phi - psi) cos/a^2",
                     G2["11"][1] - G2["22"][1] == -k ** 2 * (PSI[0] - PHI[0]) * c0 / eta0 ** 2)
            d = slice_data(a_c, PHI, PHI, zero, k, s0, c0)
            GA.check("1 + w = 4/3 and u = (eta A' + A)/2 in this slicing",
                     d["w1"] == F(4, 3) and d["u"] == (eta0 * dA + A) / 2)
            GA.check("delta_c = -(2/3) (k eta)^2 A", d["delta"] + 4 * d["u"] == -F(2, 3) * (k * eta0) ** 2 * A)
    # the two solutions in x = k eta / sqrt 3: g = 3 (sin x - x cos x)/x^3, d = (cos x + x sin x)/x^3
    top = 24
    sin, cos = trig_series(top)
    g = below(sadd(sshift(sin, -3, 3), sshift(cos, -2, -3)), top)
    dd = below(sadd(sshift(cos, -3), sshift(sin, -2)), top)
    ode = lambda p: below(sadd(sder(sder(p)), sshift(sder(p), -1, 4), p), top - 4)
    GA.check("g and d solve Psi'' + 4 Psi'/x + Psi = 0", ode(g) == {} and ode(dd) == {})
    GA.check("leading terms: g = 1 - x^2/10 + x^4/280, d = x^-3 + x^-1/2 - x/8",
             (g[0], g[2], g[4]) == (1, F(-1, 10), F(1, 280)) and (dd[-3], dd[-1], dd[1]) == (1, F(1, 2), F(-1, 8)))
    wr = below(sadd(smul(sder(g), dd), sshift(smul(g, sder(dd)), 0, -1)), top - 8)
    GA.check("Wronskian g' d - g d' = 3/x^4", wr == {-4: 3})
    Rof = lambda p: sadd(sshift(p, 0, F(3, 2)), sshift(sder(p), 1, F(1, 2)))      # R = (3/2) Psi + (x/2) Psi'
    GA.check("R of the decaying solution is cos x/(2x): it carries no constant curvature perturbation",
             below(sadd(Rof(dd), sshift(cos, -1, F(-1, 2))), top - 4) == {})
    GA.check("R of the growing solution starts 3/2 - x^2/4", (Rof(g)[0], Rof(g)[2]) == (F(3, 2), F(-1, 4)))
    # projection: for Psi = A0 g + D d, with R and delta_c = -2 x^2 Psi,
    #   (3/2) A0 = R (cos x + x sin x) + (delta_c/4) cos x, so zeta_inf = -(3/2) A0 = -[R (cos + x sin) + (delta_c/4) cos]
    cxs = sadd(cos, sshift(sin, 1))
    for sol, want in ((g, {0: F(3, 2)}), (dd, {})):
        lhs = sadd(smul(Rof(sol), cxs), sshift(smul(sshift(sol, 2, -2), cos), 0, F(1, 4)))
        GA.check("projection identity on the two solutions", below(lhs, top - 6) == want)
    GA.check("control: without the delta_c term the decaying solution is not projected out",
             below(smul(Rof(dd), cxs), top - 6) != {})
    return True


def check_three_readings_and_the_index_ledger():
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    premise("synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise")
    top = 12
    sin, cos = trig_series(top)
    cxs = sadd(cos, sshift(sin, 1))
    # zeta_inf = -psi (cos + x sin) - (delta/4) cos - u (2 cos + x sin),  psi = -(delta - 2 delta_H)/(2 x^2)
    def zeta_inf(psi, delta, u):
        """coefficient series of zeta_inf for slice data given as series in x"""
        return below(sadd(sshift(smul(psi, cxs), 0, -1), sshift(smul(delta, cos), 0, F(-1, 4)),
                          sshift(smul(u, sadd(sshift(cos, 0, 2), sshift(sin, 1))), 0, -1)), top)
    one = {0: F(1)}
    # uniform expansion (delta_H = 0), unit delta, u = 0
    ue = zeta_inf({-2: F(-1, 2)}, one, {})
    GA.check("uniform expansion: zeta_inf/delta = 1/(2 x^2) + x^2/16 - x^4/144 + ...",
             (ue[-2], ue.get(0, 0), ue[2], ue[4]) == (F(1, 2), 0, F(1, 16), F(-1, 144)))
    # with 1/(2 x^2) = (3/2)(a_d H_d/k)^2 since x^2 = k^2/(3 a_d^2 H_d^2)
    GA.check("1/(2 x^2) = (3/2)(aH/k)^2", F(1, 2) * 3 == F(3, 2))
    # flat slice (psi = 0): unit delta, u = 0, and unit u, delta = 0
    fl_d, fl_u = zeta_inf({}, one, {}), zeta_inf({}, {}, one)
    GA.check("flat slice, matter at rest: zeta_inf/delta = -cos x/4", (fl_d[0], fl_d[2]) == (F(-1, 4), F(1, 8)))
    GA.check("flat slice: zeta_inf/u = -(2 cos x + x sin x) = -2 + 0 x^2 + x^4/12", (fl_u[0], fl_u.get(2, 0), fl_u[4]) == (-2, 0, F(1, 12)))
    # the time-shift (pure growing) datum on the flat slice: u = -delta/4 (1 + O(x^2)) gives zeta_inf = delta/4
    grow = zeta_inf({}, one, {0: F(-1, 4)})
    GA.check("pure growing datum on the flat slice: zeta_inf = +delta/4 at leading order", grow[0] == F(1, 4))
    # indices of Delta^2 = k^3 P/(2 pi^2): transfer (aH/k)^m on a source spectrum P ~ k^s gives n_s - 1 = 3 + s - 2m
    index = lambda s, m: 3 + s - 2 * m
    GA.check("white deposit: uniform expansion -1, flat slice with momentum noise +1, flat and at rest +3",
             (index(0, 2), index(0, 1), index(0, 0)) == (-1, 1, 3))
    GA.check("structure factor ~ k: uniform expansion gives index 0", index(1, 2) == 0)
    GA.check("the stored thermal reading: extensive capacity under the Poisson conversion is -1 too",
             2 - 3 - 2 * 0 == index(0, 2))
    # a slice between the readings, delta_H = (1 - lam) delta/2: psi = -lam delta/(2 x^2)
    for lam in (F(1, 3), F(-2, 7)):
        mix = zeta_inf({-2: -lam / 2}, one, {})
        GA.check("mixed slice: leading term lam/(2 x^2)", mix[-2] == lam / 2 and mix[0] == (lam - 1) / 4)
    # thermal deposit on the flat slice: P_v = (3/16) P_delta, so Delta^2 = (1 + 12 (aH/k)^2) Delta_delta^2/16
    GA.check("flat slice, thermal momentum noise: 4 (3/16) = 12/16", 4 * F(3, 16) == F(12, 16))
    return True


def check_thermal_deposit_under_uniform_expansion():
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.finite-range-descent-deposit-cannot-seed-cmb")
    premise("synthesis.imported-bbn-reheating-temperature-floor")
    premise("hawking.i-state")
    # fluctuation identities: with y = e^(omega/T), n = 1/(y + 1) (Fermi-Dirac) and 1/(y - 1) (Bose-Einstein),
    # n (1 - n) = y/(y + 1)^2 = -T dn/d omega and n (1 + n) = y/(y - 1)^2 = -T dn/d omega (dy/d omega = y/T)
    y = RF.var()
    one = RF.const(1)
    nf, nb = one / (y + one), one / (y - one)
    GA.check("Fermi-Dirac: n(1 - n) = -T dn/d omega", (nf * (one - nf)).eqrf(RF.const(-1) * y * nf.deriv()))
    GA.check("Bose-Einstein: n(1 + n) = -T dn/d omega", (nb * (one + nb)).eqrf(RF.const(-1) * y * nb.deriv()))
    # massless quanta: int d^3p p^2 (-T dn/dp) = 4 T int d^3p p n (one integration by parts: d(p^4)/dp = 4 p^3),
    # so Var(E)/V = 4 rho T, P_delta = 4 T/rho, and Var(P_i)/V = (1/3) 4 rho T = T (rho + p), P_v = T/(rho + p)
    GA.check("P_v/P_delta = (1/(rho + p))/(4/rho) = 3/16 for p = rho/3", (1 / (1 + F(1, 3))) / 4 == F(3, 16))
    # Delta_zeta^2 = (9/4)(aH/k)^4 (k^3/(2 pi^2)) (4 T/rho), rho = (pi^2/30) g T^4: coefficient 135/(pi^4 g)
    GA.check("coefficient (9/4)(4)(30)/2 = 135", F(9, 4) * 4 * 30 / 2 == 135)
    # with H = pi sqrt(g/90) T^2/M_P (reduced mass): [135/(pi^4 g)]^2 (pi^2 g/90)^3 = g/(40 pi^2)
    GA.check("135^2/90^3 = 1/40", F(135 ** 2, 90 ** 3) == F(1, 40))
    # pivot: a_d H_d/k_* = rho_d/kappa, rho_d^6 = (T_0/T_d)^6 (g_s0/g)^2 (pi^2 g/90)^3 T_d^12/(M_P H_0)^6, so pi drops:
    # Delta^2(k_*) = (g^4 g_s0^2)^(1/6)/60 (T_d/M_P)^4 T_0/(H_0 kappa)
    GA.check("(40^3 90^3)^(1/6) = 60", 60 ** 6 == 40 ** 3 * 90 ** 3)
    T0 = F("2.7255") * F("8.617333262e-14")                                       # GeV
    H0 = F("67.4") * 1000 / F("3.0856775814913673e22") * F("6.582119569e-25")     # GeV
    MP = F("2.435e18")
    GS0 = F(1)
    KAPPA = F("0.05") * F("299792.458") / F("67.4")
    AS = F("2.1e-9")
    def amp6(Td, g):
        """sixth power of Delta_zeta^2 at the pivot"""
        return g ** 4 * GS0 ** 2 / F(60) ** 6 * (Td / MP) ** 24 * (T0 / (H0 * KAPPA)) ** 6
    g_hi, g_lo = F(10675, 100), F(1075, 100)
    ten = F(10)
    GA.check("1 MeV: between 2e-60 and 3e-60", (2 * ten ** -60) ** 6 < amp6(F(1, 1000), g_lo) < (3 * ten ** -60) ** 6)
    ceil = F(73, 10) * ten ** 8
    GA.check("window ceiling 7.3e8 GeV: between 3.4e-12 and 3.6e-12",
             (F(34, 10) * ten ** -12) ** 6 < amp6(ceil, g_hi) < (F(36, 10) * ten ** -12) ** 6)
    GA.check("at the ceiling the pivot amplitude is below A_s by more than 580 and less than 620",
             580 ** 6 * amp6(ceil, g_hi) < AS ** 6 < 620 ** 6 * amp6(ceil, g_hi))
    GA.check("1e12 GeV: between 12 and 13, not a perturbation", 12 ** 6 < amp6(ten ** 12, g_hi) < 13 ** 6)
    GA.check("A_s is reached between 3.6e9 and 3.7e9 GeV",
             amp6(F(36, 10) * ten ** 9, g_hi) < AS ** 6 < amp6(F(37, 10) * ten ** 9, g_hi))
    # index -1: at the present Hubble scale k = a_0 H_0 the amplitude is kappa times the pivot's
    GA.check("at the ceiling, k = a_0 H_0: between 0.36 and 0.39 of A_s",
             (F(36, 100) * AS) ** 6 < KAPPA ** 6 * amp6(ceil, g_hi) < (F(39, 100) * AS) ** 6)
    # the enhancement (9/4)(a_d H_d/k_*)^4 with the stored brackets of rho_d = a_d H_d/(a_0 H_0) and 222 < kappa < 223
    enh = lambda r, kap: F(9, 4) * (r / kap) ** 4
    GA.check("stored bracket of kappa", 222 < KAPPA < 223)
    GA.check("enhancement at 1 MeV between 5e21 and 7e21",
             5 * ten ** 21 < enh(F(496, 10) * ten ** 6, 223) and enh(F(521, 10) * ten ** 6, 222) < 7 * ten ** 21)
    GA.check("enhancement at 1e12 GeV between 2.5e82 and 3.2e82",
             F(25, 10) * ten ** 82 < enh(F(727, 100) * ten ** 22, 223) and enh(F(763, 100) * ten ** 22, 222) < F(32, 10) * ten ** 82)
    # infrared end: Delta^2 = 1 at k_1 = k_* Delta^2(k_*); in present Hubble radii 1/(kappa Delta^2(k_*))
    GA.check("at the ceiling the reading is a perturbation up to more than 1.2e9 present Hubble radii",
             (F(12, 10) * ten ** 9 * KAPPA) ** 6 * amp6(ceil, g_hi) < 1)
    # flat-slice reading of the same deposit: Delta_delta^2(k_*) = (60/(pi^4 g_s0)) (k_*/(a_0 T_0))^3 for the whole bath
    PI_LO, PI_HI = F(333, 106), F(355, 113)
    dd_hi = 60 / (PI_LO ** 4 * GS0) * (H0 * KAPPA / T0) ** 3
    dd_lo = 60 / (PI_HI ** 4 * GS0) * (H0 * KAPPA / T0) ** 3
    GA.check("Delta_delta^2(k_*) between 3.9e-82 and 4.1e-82", F(39, 10) * ten ** -82 < dd_lo and dd_hi < F(41, 10) * ten ** -82)
    # with thermal momentum noise it is (3/4)(a_d H_d/k_*)^2 times that: below 4e-41 at 1e12 GeV (rho_d < 7.63e22)
    GA.check("flat slice with momentum noise at 1e12 GeV: below 4e-41",
             F(3, 4) * (F(763, 100) * ten ** 22 / KAPPA) ** 2 * dd_hi < 4 * ten ** -41)
    return True
