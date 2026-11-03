"""synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue: exact checks (Fractions and GA).

Homogeneous diagonal class: derived metric N^2 dT^2 - sum_l a_l(T)^2 (dx^l)^2, harmonic lapse N = a1 a2 a3,
alpha_l = log a_l, S = sum alpha_l', C = alpha1'alpha2' + alpha2'alpha3' + alpha3'alpha1' = -(1/2) G(alpha', alpha')
with the DeWitt form G(x, y) = sum x_l y_l - (sum x)(sum y), G = I - J, G^{-1} = I - J/2.
Ricci from the jets of the metric by the coordinate formula of the stored Bianchi II check (round-sphere-positive,
Ric_formula); the store's sign is Ric_store = -Ric_formula, and the field equations read
Ric_formula = 8 pi G (T - (1/2) tr(T) g) with T(a) the physical stress (kappa = 8 pi G kept as a rational).

  check_aligned_maxwell_stress   GA: T(a) = -(1/2) F a F for F = (E + I B) e1e0 is diag(rho, -rho, rho, rho),
                                 rho = (E^2 + B^2)/2, trace-free; a misaligned field has a Poynting component.
  check_bianchi_i_ricci          generic jets: N^2 Ric(e_l, e_l) = alpha_l'', Ric_TT = -sum alpha'' + 2C (pinned);
                                 conserved Maxwell fluxes: E a2 a3 and B a2 a3 constant along the field equation.
  check_matter_is_potential      Einstein-Maxwell, perfect fluid p = w rho, and Bianchi II (stored equations) are
                                 all alpha'' = -G^{-1} dV, C = V, with V = (kappa/2)(Qe^2+Qm^2) a1^2,
                                 V = kappa rho0 N^(1-w), V = a1^4/4; Ricci - kappa(T - tr T g/2) vanishes on these
                                 jets and not on perturbed ones; the constraint propagates exactly when rho ~ N^-(1+w).
  check_single_wall_bounce       V = c e^(2 k alpha1), k = 1 (Maxwell) and k = 2 (curvature): Liouville solution in
                                 s = tanh, BC = v^2, in/out velocities; the out velocity is the G-reflection of the in
                                 velocity in ker(alpha1), independent of k and c; normalised it is the BKL law,
                                 u -> u - 1 or 1/(u - 1); the earlier epoch has p1' > 0, so the aligned Maxwell
                                 term is subleading after one bounce.
  check_activity_and_residue     relative size V/S^2 ~ tau^(2 w(p)): Maxwell tau^(2 p_l), curvature tau^(4 p_l), fluid
                                 tau^(1 - w); G^{-1}(w, w) = 1/2 (Maxwell axis form), -3/2 (volume form, fluid: no
                                 bounce); stiff matter (V constant) puts the residue on the disk, B_w^2 = 1 - 2V/S^2,
                                 equal to the scalar's 1 - 8 pi G q^2 with rho0 = phi'^2/2 (GA residue square); the scalar's
                                 own field equations are checked on jets (stress diag(rho, rho, rho, rho)).
"""
from fractions import Fraction as F
import GA
from GA import mul, gen, add, scal, field_solve
from tp_premise import premise

SIG = [1, -1, -1, -1]
KAPPA = F(3, 2)


def inv(M):
    n = len(M)
    cols = [field_solve(M, [F(int(i == j)) for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def ricci(g, dg, ddg):
    n = len(g)
    gi = inv(g)
    dgi = [[[-sum(gi[a][e] * dg[c][e][f] * gi[f][b] for e in range(n) for f in range(n))
             for b in range(n)] for a in range(n)] for c in range(n)]
    G1 = [[[(dg[a][l][b] + dg[b][l][a] - dg[l][a][b]) / 2 for b in range(n)] for a in range(n)] for l in range(n)]
    dG1 = [[[[(ddg[c][a][l][b] + ddg[c][b][l][a] - ddg[c][l][a][b]) / 2 for b in range(n)]
             for a in range(n)] for l in range(n)] for c in range(n)]
    Gam = [[[sum(gi[k][l] * G1[l][a][b] for l in range(n)) for b in range(n)] for a in range(n)] for k in range(n)]
    dGam = [[[[sum(dgi[c][k][l] * G1[l][a][b] + gi[k][l] * dG1[c][l][a][b] for l in range(n))
               for b in range(n)] for a in range(n)] for k in range(n)] for c in range(n)]
    Ric = [[sum(dGam[k][k][a][b] - dGam[b][k][a][k] for k in range(n))
            + sum(Gam[k][k][l] * Gam[l][a][b] - Gam[k][b][l] * Gam[l][a][k] for k in range(n) for l in range(n))
            for b in range(n)] for a in range(n)]
    return Ric


def bianchi1_ricci(a, da, dda):
    """Coordinate Ricci of N^2 dT^2 - sum a_l^2 dx_l^2, N = a1 a2 a3, from alpha', alpha'' (T-jets only)."""
    A1 = [a[i] * da[i] for i in range(3)]
    A2 = [a[i] * (dda[i] + da[i] ** 2) for i in range(3)]
    N = a[0] * a[1] * a[2]
    S, Sdd = sum(da), sum(dda)
    N1, N2 = N * S, N * (Sdd + S * S)
    g = [[F(0)] * 4 for _ in range(4)]
    dg = [[[F(0)] * 4 for _ in range(4)] for _ in range(4)]
    ddg = [[[[F(0)] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    g[0][0], dg[0][0][0], ddg[0][0][0][0] = N * N, 2 * N * N1, 2 * (N1 * N1 + N * N2)
    for i in range(3):
        g[i + 1][i + 1] = -a[i] ** 2
        dg[0][i + 1][i + 1] = -2 * a[i] * A1[i]
        ddg[0][0][i + 1][i + 1] = -2 * (A1[i] ** 2 + a[i] * A2[i])
    return ricci(g, dg, ddg)


def cross(da):
    return da[0] * da[1] + da[1] * da[2] + da[2] * da[0]


def stress_ga(fe, fb, axis_e=1, axis_b=1):
    """Orthonormal T_ab = T(e_a).e_b, T(a) = -(1/2) F a F, F = fe sigma_{axis_e} + fb I sigma_{axis_b}."""
    I = mul(mul(gen(0), gen(1), SIG), mul(gen(2), gen(3), SIG), SIG)
    se = mul(gen(axis_e), gen(0), SIG)
    sb = mul(gen(axis_b), gen(0), SIG)
    Fb = add(scal(fe, se), scal(fb, mul(I, sb, SIG)))
    T = [[F(0)] * 4 for _ in range(4)]
    for a in range(4):
        Ta = scal(F(-1, 2), mul(mul(Fb, gen(a), SIG), Fb, SIG))
        for b in range(4):
            T[a][b] = mul(Ta, gen(b), SIG).get((), F(0))
    return T


def check_aligned_maxwell_stress():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.imported-maxwell-stress-spacetime-algebra")
    ok = True
    for fe, fb in ((F(3), F(0)), (F(0), F(2)), (F(5, 3), F(-7, 4))):
        T = stress_ga(fe, fb)
        rho = (fe * fe + fb * fb) / 2
        ok &= T == [[rho, 0, 0, 0], [0, -rho, 0, 0], [0, 0, rho, 0], [0, 0, 0, rho]]
        ok &= T[0][0] - T[1][1] - T[2][2] - T[3][3] == 0
    Tm = stress_ga(F(3), F(2), 1, 2)
    ok &= Tm[0][3] == -6 and Tm[0][0] == F(13, 2)
    ok &= stress_ga(F(5, 3), F(-7, 4))[0][0] == F(841, 288)
    GA.check("aligned Maxwell stress -F a F/2 = diag(rho,-rho,rho,rho), trace-free; misaligned: Poynting", ok)
    return ok


JETS = (([F(2, 3), F(5, 4), F(3, 7)], [F(-1, 5), F(2, 3), F(1, 4)], [F(1, 2), F(-3), F(2, 7)]),
        ([F(3, 2), F(1, 2), F(4)], [F(1), F(-2, 3), F(5)], [F(-1), F(1, 3), F(2)]))
PIN_RTT = (F(229, 105), F(2, 3))


def check_bianchi_i_ricci():
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for (a, da, dda), pin in zip(JETS, PIN_RTT):
        R = bianchi1_ricci(a, da, dda)
        N2 = (a[0] * a[1] * a[2]) ** 2
        ok &= R[0][0] == pin == -sum(dda) + 2 * cross(da)
        ok &= all(N2 * R[l + 1][l + 1] / a[l] ** 2 == dda[l] for l in range(3))
        ok &= all(R[i][j] == 0 for i in range(4) for j in range(4) if i != j)
        # Maxwell: sqrt|g| F^{T1} = N^2 g^TT g^11 F_T1 = -F_T1/a1^2; with F_T1 = Q a1^2 its T-derivative
        # F_T1' = 2 alpha1' F_T1 makes the flux constant; orthonormal E = F_T1/(N a1) = Q/(a2 a3)
        Q = F(7, 3)
        FT1, dFT1 = Q * a[0] ** 2, 2 * da[0] * Q * a[0] ** 2
        ok &= (dFT1 * a[0] ** 2 - FT1 * 2 * a[0] * a[0] * da[0]) == 0
        ok &= FT1 / (a[0] * a[1] * a[2] * a[0]) == Q / (a[1] * a[2])
    GA.check("Bianchi I harmonic lapse: N^2 Ric(e_l,e_l) = alpha_l'', Ric_TT = -sum alpha'' + 2C; flux constant", ok)
    return ok


def ginv(cov):
    s = sum(F(c) for c in cov)
    return [F(c) - s / 2 for c in cov]


def residual(a, da, dda, Tortho):
    """Ric_formula - kappa (T - tr T g / 2) in coordinates, T given orthonormal (lower, +---)."""
    R = bianchi1_ricci(a, da, dda)
    N = a[0] * a[1] * a[2]
    scale = [N] + list(a)
    eta = [1, -1, -1, -1]
    tr = sum(eta[i] * Tortho[i][i] for i in range(4))
    out = []
    for i in range(4):
        for j in range(4):
            Tij = scale[i] * scale[j] * Tortho[i][j]
            gij = eta[i] * scale[i] * scale[j] if i == j else 0
            out.append(R[i][j] - KAPPA * (Tij - tr * gij / 2))
    return out


def check_matter_is_potential():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.kasner-curvature-wall-is-negative-weight-helicity")
    ok = True
    a = [F(2, 3), F(5, 4), F(3, 7)]
    N = a[0] * a[1] * a[2]
    # Einstein-Maxwell, aligned on axis 1, fluxes Qe, Qm
    for Qe, Qm in ((F(1, 2), F(0)), (F(0), F(3)), (F(2, 3), F(5, 7))):
        fe, fb = Qe / (a[1] * a[2]), Qm / (a[1] * a[2])
        T = stress_ga(fe, fb)
        V = KAPPA * (Qe ** 2 + Qm ** 2) * a[0] ** 2 / 2
        ok &= V == KAPPA * N * N * T[0][0]
        dV = [2 * V, F(0), F(0)]
        dda = [-x for x in ginv(dV)]
        ok &= dda == [-V, V, V]
        d1, d2 = F(-1, 3), F(4, 5)
        d3 = (V - d1 * d2) / (d1 + d2)
        da = [d1, d2, d3]
        ok &= cross(da) == V
        ok &= all(x == 0 for x in residual(a, da, dda, T))
        ok &= any(x != 0 for x in residual(a, da, [dda[0] + F(1, 11), dda[1], dda[2]], T))
        ok &= any(x != 0 for x in residual(a, [d1, d2, d3 + F(1, 13)], dda, T))
        # constraint propagation C' = V' along alpha'' = -G^{-1} dV: C' = sum alpha_l''(S - alpha_l')
        S = sum(da)
        ok &= sum(dda[l] * (S - da[l]) for l in range(3)) == 2 * da[0] * V
    # perfect fluid p = w rho, rho = rho0 N^-(1+w); N = 27/8 so that N^(1/3) is rational
    af = [F(9, 4), F(2, 3), F(9, 4)]
    Nf = af[0] * af[1] * af[2]
    ok &= Nf == F(27, 8)
    for w, Npow in ((F(0), Nf), (F(1, 3), Nf * F(3, 2)), (F(1), Nf * Nf)):
        rho0 = F(5, 2)
        rho = rho0 / Npow
        T = [[rho, 0, 0, 0], [0, w * rho, 0, 0], [0, 0, w * rho, 0], [0, 0, 0, w * rho]]
        V = KAPPA * Nf * Nf * rho
        dda = [-x for x in ginv([(1 - w) * V] * 3)]
        ok &= dda == [(1 - w) * V / 2] * 3
        d1, d2 = F(-1, 3), F(4, 5)
        d3 = (V - d1 * d2) / (d1 + d2)
        da = [d1, d2, d3]
        ok &= all(x == 0 for x in residual(af, da, dda, T))
        ok &= any(x != 0 for x in residual(af, da, [y + F(1, 7) for y in dda], T))
        ok &= any(x != 0 for x in residual(af, da, dda, [[y * F(9, 10) for y in r] for r in T]))
        # propagation: C' = sum alpha_l''(S - alpha_l') equals V' = (1 - w) S V, the scaling rho ~ N^-(1+w);
        # a different exponent would not
        S = sum(da)
        ok &= sum(dda[l] * (S - da[l]) for l in range(3)) == (1 - w) * S * V
        ok &= sum(dda[l] * (S - da[l]) for l in range(3)) != (F(4, 5) - w) * S * V
    # Bianchi II as stored: 2 alpha1'' = -a1^4, 2 alpha2'' = 2 alpha3'' = a1^4, 4C = a1^4: V = a1^4/4
    V = a[0] ** 4 / 4
    ok &= [-x for x in ginv([4 * V, F(0), F(0)])] == [-a[0] ** 4 / 2, a[0] ** 4 / 2, a[0] ** 4 / 2]
    GA.check("Maxwell, fluid and Bianchi II are alpha'' = -G^{-1} dV, C = V; residual zero on, nonzero off", ok)
    return ok


def kasner(u):
    d = 1 + u + u * u
    return [-u / d, (1 + u) / d, u * (1 + u) / d]


def bkl(p):
    return [-p[0] / (1 + 2 * p[0])] + [(p[b] + 2 * p[0]) / (1 + 2 * p[0]) for b in (1, 2)]


def greflect(v, cov):
    """Reflection of the velocity v in ker(cov) for the DeWitt form G."""
    sh = ginv(cov)
    wv = sum(c * x for c, x in zip(cov, v))
    ww = sum(c * x for c, x in zip(cov, sh))
    return [x - 2 * wv * y / ww for x, y in zip(v, sh)]


def check_single_wall_bounce():
    premise("synthesis.bkl-bounces-no-framewise-invariant")
    premise("synthesis.kasner-curvature-wall-is-negative-weight-helicity")
    ok = True
    pins = {(F(1, 2), F(3, 4)): [F(6, 7), F(3, 7), F(-2, 7)], (F(2, 3), F(5)): [F(30, 199), F(195, 199), F(-26, 199)],
            (F(1), F(7, 3)): [F(21, 37), F(28, 37), F(-12, 37)]}
    vsum = F(0)
    for k, c in ((1, F(3, 4)), (2, F(1, 4)), (1, F(5))):
        for v, B in ((F(1, 2), F(3, 4)), (F(2, 3), F(5)), (F(1), F(7, 3))):
            B3 = v * v / B
            # alpha1' = -v s, s = tanh(k v (T - T0)); c e^{2k alpha1} = v^2 (1 - s^2); alpha1'' = -k v^2 (1 - s^2)
            for s in (F(-9, 10), F(-1, 3), F(0), F(1, 2), F(7, 8)):
                d1 = -v * s
                V = v * v * (1 - s * s)
                vsum += V if (k, v) == (2, F(1, 2)) else 0
                dd1 = -k * v * v * (1 - s * s)
                ok &= dd1 == -k * V                      # alpha'' = -G^{-1} dV, dV = 2k V (1,0,0)
                ok &= [-x for x in ginv([2 * k * V, F(0), F(0)])] == [dd1, -dd1, -dd1]
                da = [d1, -d1 + B, -d1 + B3]
                ok &= cross(da) == V                      # constraint C = V
            late, early = [-v, B + v, B3 + v], [v, B - v, B3 - v]
            ok &= greflect(late, [k, 0, 0]) == early and greflect(late, [1, 0, 0]) == early
            Sp, Sm = sum(late), sum(early)
            p, pe = [x / Sp for x in late], [x / Sm for x in early]
            ok &= sum(p) == 1 and sum(x * x for x in p) == 1 and p[0] < 0
            ok &= pe == bkl(p) and pe[0] > 0 and pe == pins[(v, B)]
    for u in (F(3, 2), F(2), F(5), F(13, 4)):
        q = bkl(kasner(u))
        ok &= sorted(q) == sorted(kasner(u - 1) if u >= 2 else kasner(1 / (u - 1)))
    ok &= bkl(kasner(F(13, 4)))[0] == F(52, 133) and vsum == F(44111, 57600)
    GA.check("single exponential wall in alpha1 (k = 1 Maxwell, k = 2 curvature): out = G-reflection = BKL law", ok)
    return ok


def check_activity_and_residue():
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    premise("synthesis.unit-boost-residue-needs-nonpositive-exponent")
    ok = True
    # wall forms and their DeWitt norms
    ok &= sum(c * x for c, x in zip([1, 0, 0], ginv([1, 0, 0]))) == F(1, 2)
    ok &= sum(c * x for c, x in zip([1, 1, 1], ginv([1, 1, 1]))) == F(-3, 2)
    for u in (F(1), F(3, 2), F(2), F(7, 2)):
        p = kasner(u)
        maxw = [2 * x for x in p]          # V/S^2 ~ tau^(2 w(p)), w = alpha_l
        curv = [4 * x for x in p]          # w = 2 alpha_l
        ok &= [x < 0 for x in maxw] == [x < 0 for x in curv] == [True, False, False]
        for w in (F(0), F(1, 3)):
            ok &= (1 - w) * sum(p) > 0
        pe = bkl(p)
        ok &= 2 * pe[0] > 0                 # aligned field on axis 1 subleading after the bounce
    # stiff matter: V constant, C = V, sum p^2 = 1 - 2 V / S^2; residue square in Cl(1,3) via GA
    for da, V in (([F(1, 3), F(1, 3), F(1, 3)], F(1, 3)), ([F(1, 5), F(3, 10), F(1, 2)], F(31, 100))):
        S = sum(da)
        ok &= cross(da) == V
        p = [x / S for x in da]
        Bw = add(*[scal(p[i], mul(gen(0), gen(i + 1), SIG)) for i in range(3)])
        sq = mul(Bw, Bw, SIG)
        ok &= set(sq) == {()} and sq[()] == sum(x * x for x in p) == 1 - 2 * V / S ** 2
        # massless scalar phi(T) in harmonic time: wave equation phi'' = 0; its stress in the frame is
        # diag(rho, rho, rho, rho), rho = phi'^2/(2 N^2); the field equations on jets with alpha'' = 0 and
        # C = kappa phi'^2/2 (zero residual, nonzero off), so q = phi'/S gives sum p^2 = 1 - kappa q^2
        a_s = [F(2, 3), F(5, 4), F(3, 7)]
        Ns = a_s[0] * a_s[1] * a_s[2]
        phi1 = F(2, 3)
        rho_s = phi1 * phi1 / (2 * Ns * Ns)
        Ts = [[rho_s, 0, 0, 0], [0, rho_s, 0, 0], [0, 0, rho_s, 0], [0, 0, 0, rho_s]]
        d1, d2 = da[0], da[1]
        d3 = (KAPPA * phi1 * phi1 / 2 - d1 * d2) / (d1 + d2)
        das = [d1, d2, d3]
        ok &= all(x == 0 for x in residual(a_s, das, [F(0)] * 3, Ts))
        ok &= any(x != 0 for x in residual(a_s, [d1, d2, d3 + F(1, 9)], [F(0)] * 3, Ts))
        Ss = sum(das)
        ok &= sum(x * x for x in das) / Ss ** 2 == 1 - KAPPA * (phi1 / Ss) ** 2
        # stiff fluid with rho0 = phi'^2/2 has the same V = kappa N^2 rho
        ok &= KAPPA * Ns * Ns * rho_s == KAPPA * (phi1 * phi1 / 2)
    ok &= cross([F(1, 5), F(3, 10), F(1, 2)]) == F(31, 100)
    GA.check("activity: Maxwell tau^(2p_l) and curvature tau^(4p_l) active on the same axis; stiff: disk residue", ok)
    return ok
