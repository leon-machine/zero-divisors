"""synthesis.taub-nut-cauchy-horizon-is-taub-point-with-complex-residue: exact checks (Fractions and GA).

Diagonal Bianchi IX field: derived metric N^2 dT^2 - sum_l a_l(T)^2 sigma_l^2 with the left-invariant forms
sigma_1 = sin(psi) d(theta) - cos(psi) sin(theta) d(phi), sigma_2 = cos(psi) d(theta) + sin(psi) sin(theta) d(phi),
sigma_3 = d(psi) + cos(theta) d(phi), harmonic lapse N = a1 a2 a3, alpha_l = log a_l. Jets are truncated
polynomials in (T - T0, psi, theta - pi/2) at the point psi = 0, theta = pi/2, where every trigonometric jet is
rational. Ricci by the coordinate formula (round-sphere-positive, Ric_f; the store's sign is -Ric_f).

  check_bianchi_ix_frame_formulas  at two generic jets: frame components N^2 Ric_f(e_l, e_l) = alpha_l'' + (G^{-1} dV)_l
        with V = (1/4) sum e^{4 alpha} - (1/2) sum_{i<j} e^{2(alpha_i + alpha_j)}, Ric_f TT = -sum alpha'' + 2C, off-diagonal
        zero; the rotation-gauge field Omega(a) = -(1/2) e^b ^ D_a e_b has Omega(e0) = 0 and
        Omega(e_k) = -H_k B_k + (1/2)(mu_i + mu_j - mu_k) e_i e_j, H_k = alpha_k'/N, mu_i = a_i/(a_j a_k), (i j k) cyclic.
  check_taub_nut_vacuum   Taub region of Taub-NUT, a1 = a2 = (t^2 + l^2)^(1/2), a3 = 2 l U^(1/2),
        U = (-t^2 + 2 m t + l^2)/(t^2 + l^2), d/dT = 2 l U (t^2 + l^2) d/dt: alpha'' = -G^{-1} dV and C = V exactly at
        rational t, for (m, l) = (4, 3), (0, 1), (12, 5); a wrong mass in U breaks it.
  check_horizon_limit     at t_+ = m + (m^2 + l^2)^(1/2), the formula of (i) evaluated on the Taub-NUT data (harmonic
        time, squared scale factors, so every ratio is rational): H_1/H_3 and the e2e3 coefficient of Omega(e_1) over
        H_3 vanish, and the e1e2 coefficient of Omega(e_3) over |H_3| is t_+/l = (1 + cos phi)/sin phi = cot(phi/2), phi = arg(m + i l).
  check_generated_algebra GA: the limit value X = -B_3 + kappa e1e2 equals -(1 - kappa I) B_3 (I B_3 = e1e2); the values
        (0, 0, X) generate a one-dimensional Lie algebra, while the Kasner values -p_i B_i at p(1) generate six
        dimensions (Lambda^2 W); E = X + B_3 = kappa I B_3 is not zero, so the field is not admissible for the
        Taub Kasner model.
"""
from fractions import Fraction as F
import GA
from GA import mul, gen, add, scal, sub, field_solve, rank_of_vectors
from tp_premise import premise

SIG = [1, -1, -1, -1]
ZERO = {}


def P(d):
    return {k: F(v) for k, v in d.items() if v != 0}


def padd(*ps):
    o = {}
    for p in ps:
        for k, v in p.items():
            o[k] = o.get(k, F(0)) + v
    return {k: v for k, v in o.items() if v != 0}


def pmul(p, q):
    o = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])
            if sum(k) <= 2:
                o[k] = o.get(k, F(0)) + v1 * v2
    return {k: v for k, v in o.items() if v != 0}


def psc(c, p):
    return {k: F(c) * v for k, v in p.items()} if c != 0 else {}


SINPSI = P({(0, 1, 0): 1})
COSPSI = P({(0, 0, 0): 1, (0, 2, 0): F(-1, 2)})
SINTH = P({(0, 0, 0): 1, (0, 0, 2): F(-1, 2)})
COSTH = P({(0, 0, 1): -1})
DKEY = {0: (1, 0, 0), 1: (0, 1, 0), 2: (0, 0, 1)}


def coef(p, k):
    return p.get(k, F(0))


def coframe(a, da, dda):
    A = [P({(0, 0, 0): a[i], (1, 0, 0): a[i] * da[i], (2, 0, 0): a[i] * (dda[i] + da[i] ** 2) / 2}) for i in range(3)]
    N = pmul(pmul(A[0], A[1]), A[2])
    s1 = [ZERO, ZERO, SINPSI, psc(-1, pmul(COSPSI, SINTH))]
    s2 = [ZERO, ZERO, COSPSI, pmul(SINPSI, SINTH)]
    s3 = [ZERO, P({(0, 0, 0): 1}), ZERO, COSTH]
    return [[N, ZERO, ZERO, ZERO]] + [[pmul(A[i], c) for c in s] for i, s in enumerate((s1, s2, s3))]


def inv(M):
    n = len(M)
    cols = [field_solve(M, [F(int(i == j)) for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def jets(th):
    eta = [1, -1, -1, -1]
    g = [[padd(*[psc(eta[x], pmul(th[x][m], th[x][n])) for x in range(4)]) for n in range(4)] for m in range(4)]
    g0 = [[coef(g[m][n], (0, 0, 0)) for n in range(4)] for m in range(4)]
    dg = [[[coef(g[m][n], DKEY[c]) if c in DKEY else F(0) for n in range(4)] for m in range(4)] for c in range(4)]

    def d2(m, n, c, d):
        if c not in DKEY or d not in DKEY:
            return F(0)
        k = tuple(x + y for x, y in zip(DKEY[c], DKEY[d]))
        return coef(g[m][n], k) * (2 if c == d else 1)
    ddg = [[[[d2(m, n, c, d) for n in range(4)] for m in range(4)] for d in range(4)] for c in range(4)]
    return g0, dg, ddg


def ricci_and_gamma(g, dg, ddg):
    n = 4
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
    return Ric, Gam


def frame_data(a, da, dda):
    th = coframe(a, da, dda)
    g, dg, ddg = jets(th)
    Ric, Gam = ricci_and_gamma(g, dg, ddg)
    T0 = [[coef(th[x][m], (0, 0, 0)) for m in range(4)] for x in range(4)]
    dT = [[[coef(th[x][m], DKEY[c]) if c in DKEY else F(0) for m in range(4)] for x in range(4)] for c in range(4)]
    E = inv(T0)
    dE = [[[-sum(E[m][x] * dT[c][x][q] * E[q][b] for x in range(4) for q in range(4)) for b in range(4)]
           for m in range(4)] for c in range(4)]
    Rf = [[sum(E[m][x] * E[q][y] * Ric[m][q] for m in range(4) for q in range(4)) for y in range(4)] for x in range(4)]
    Om = []
    for cc in range(4):
        tot = {}
        for b in range(4):
            vec = [sum(E[nu][cc] * (dE[nu][mu][b] + sum(Gam[mu][nu][lam] * E[lam][b] for lam in range(4)))
                       for nu in range(4)) for mu in range(4)]
            fr = [sum(T0[x][mu] * vec[mu] for mu in range(4)) for x in range(4)]
            w = mul(scal(SIG[b], gen(b)), add(*[scal(fr[x], gen(x)) for x in range(4)]), SIG)
            tot = add(tot, scal(F(-1, 2), {k: v for k, v in w.items() if len(k) == 2}))
        Om.append(tot)
    return Ric, Rf, Om


def vix(e2):
    V = sum(x * x for x in e2) / 4 - (e2[0] * e2[1] + e2[1] * e2[2] + e2[2] * e2[0]) / 2
    dV = [e2[i] ** 2 - e2[i] * e2[(i + 1) % 3] - e2[i] * e2[(i + 2) % 3] for i in range(3)]
    s = sum(dV)
    return V, [x - s / 2 for x in dV]


def cross(d):
    return d[0] * d[1] + d[1] * d[2] + d[2] * d[0]


JETS = (([F(2, 3), F(5, 4), F(3, 7)], [F(-1, 5), F(2, 3), F(1, 4)], [F(1, 2), F(-3), F(2, 7)]),
        ([F(3, 2), F(1, 2), F(4)], [F(1), F(-2, 3), F(5)], [F(-1), F(1, 3), F(2)]))
PIN = (F(-35031809, 99574272), F(229, 105))


def check_bianchi_ix_frame_formulas():
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for idx, (a, da, dda) in enumerate(JETS):
        Ric, Rf, Om = frame_data(a, da, dda)
        N = a[0] * a[1] * a[2]
        V, gdV = vix([x * x for x in a])
        ok &= all(N * N * Rf[l + 1][l + 1] == dda[l] + gdV[l] for l in range(3))
        ok &= Ric[0][0] == -sum(dda) + 2 * cross(da)
        ok &= all(Rf[x][y] == 0 for x in range(4) for y in range(4) if x != y)
        if idx == 0:
            ok &= N * N * Rf[1][1] == PIN[0] and Ric[0][0] == PIN[1]
        ok &= Om[0] == {}
        mu = [a[i] / (a[(i + 1) % 3] * a[(i + 2) % 3]) for i in range(3)]
        for k in range(3):
            i, j = (k + 1) % 3, (k + 2) % 3
            want = add(scal(-da[k] / N, mul(gen(0), gen(k + 1), SIG)),
                       scal((mu[i] + mu[j] - mu[k]) / 2, mul(gen(i + 1), gen(j + 1), SIG)))
            ok &= sub(Om[k + 1], want) == {}
            ok &= (mu[i] + mu[j] - mu[k]) / 2 == rot_times_n([x * x for x in a], k) / N
    GA.check("Bianchi IX: N^2 Ric(e_l,e_l) = alpha_l'' + (G^-1 dV)_l; Omega(e_k) = -H_k B_k + (mu_i+mu_j-mu_k)/2 e_ie_j", ok)
    return ok


def taub_nut(t, m, l):
    q = t * t + l * l
    num, dnum = -t * t + 2 * m * t + l * l, -2 * t + 2 * m
    U = num / q
    Ut = (dnum * q - num * 2 * t) / q ** 2
    Utt = (-2 * q - num * 2) / q ** 2 - 2 * (2 * t) * (dnum * q - num * 2 * t) / q ** 3
    D = 2 * l * U * q
    d1, d3 = 2 * l * t * U, l * q * Ut
    dd1 = D * 2 * l * (U + t * Ut)
    dd3 = D * l * (2 * t * Ut + q * Utt)
    return U, Ut, [d1, d1, d3], [dd1, dd1, dd3], [q, q, 4 * l * l * U]


MLS = ((F(4), F(3), F(5)), (F(0), F(1), F(1)), (F(12), F(5), F(13)))


def check_taub_nut_vacuum():
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for m, l, r in MLS:
        ok &= r * r == m * m + l * l
        for t in (F(1, 2), F(2, 3), F(-3, 4), F(1, 5)):
            U, Ut, da, dda, e2 = taub_nut(t, m, l)
            if U <= 0:
                continue
            V, gdV = vix(e2)
            ok &= all(dda[i] + gdV[i] == 0 for i in range(3)) and cross(da) == V
            Uw, Utw, daw, ddaw, e2w = taub_nut(t, m + F(1, 3), l)
            Vw, gdVw = vix([e2[0], e2[1], e2w[2]])
            ok &= not (all(dda[i] + gdVw[i] == 0 for i in range(3)) and cross(da) == Vw)
    vtot, count = F(0), 0
    for m, l, r in MLS:
        for t in (F(1, 2), F(2, 3), F(-3, 4), F(1, 5)):
            U, Ut, da, dda, e2 = taub_nut(t, m, l)
            if U > 0:
                vtot += vix(e2)[0]
                count += 1
    ok &= count == 12 and vtot == F(4318977234418984058830475854971019751, 996528444004453013607892169722500)
    U, Ut, da, dda, e2 = taub_nut(F(1, 2), F(4), F(3))
    ok &= dda[2] == F(-1685448, 1369)
    U, Ut, da, dda, e2 = taub_nut(F(2), F(4), F(3))
    ok &= U == F(21, 13) and da[0] == F(252, 13) and da[2] == F(-96, 13)
    GA.check("Taub-NUT Taub region solves the Bianchi IX vacuum equations exactly; a wrong mass does not", ok)
    return ok


def rot_times_n(e2, k):
    """N times the e_ie_j coefficient (mu_i + mu_j - mu_k)/2 of Omega(e_k), from the squared scale factors."""
    i, j = (k + 1) % 3, (k + 2) % 3
    return (e2[i] + e2[j] - e2[k]) / 2


def horizon_ratios(m, l, r):
    """Evaluate the general formula of (i) on the Taub-NUT data at t_+: with H_k = alpha_k'/N in harmonic time,
    every value of Omega(e_k) over H_3 is rational in t: boost H_k/H_3 = alpha_k'/alpha_3', rotation
    rot_times_n(e2, k)/alpha_3'."""
    tp = m + r
    U, Ut, da, dda, e2 = taub_nut(tp, m, l)
    h1_over_h3 = da[0] / da[2]
    rot1_over_h3 = rot_times_n(e2, 0) / da[2]
    rot3_over_h3 = rot_times_n(e2, 2) / da[2]
    return tp, U, h1_over_h3, rot1_over_h3, rot3_over_h3


def check_horizon_limit():
    premise("synthesis.bkl-bounces-no-framewise-invariant")
    ok = True
    for m, l, r in MLS:
        tp, U, a, b, c = horizon_ratios(m, l, r)
        kappa = -c
        ok &= U == 0 and a == 0 and b == 0
        ok &= kappa == tp / l == (1 + m / r) / (l / r) and kappa > 0
    ok &= [horizon_ratios(*x)[4] for x in MLS] == [F(-3), F(-1), F(-5)]
    GA.check("Taub-NUT horizon, formula (i) on the data: H_1/H_3 -> 0, e2e3 part of Omega(e_1) -> 0, e1e2 part of Omega(e_3) over |H_3| -> t_+/l = cot(phi/2)", ok)
    return ok


def lie_dim(gens):
    blades = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    def vec(x):
        return [x.get(b, F(0)) for b in blades]
    basis = [g for g in gens if g]
    changed = True
    while changed:
        changed = False
        r0 = rank_of_vectors([vec(x) for x in basis]) if basis else 0
        for x in list(basis):
            for y in list(basis):
                c = sub(mul(x, y, SIG), mul(y, x, SIG))
                c = {k: v / 2 for k, v in c.items() if len(k) == 2}
                if c and rank_of_vectors([vec(z) for z in basis + [c]]) > r0:
                    basis.append(c)
                    r0 += 1
                    changed = True
    return rank_of_vectors([vec(x) for x in basis]) if basis else 0


def check_generated_algebra():
    premise("synthesis.bkl-bounce-invariant-holonomy-and-bound")
    ok = True
    I = mul(mul(gen(0), gen(1), SIG), mul(gen(2), gen(3), SIG), SIG)
    B3 = mul(gen(0), gen(3), SIG)
    e12 = mul(gen(1), gen(2), SIG)
    ok &= mul(I, B3, SIG) == e12
    for m, l, r in MLS:
        kappa = horizon_ratios(m, l, r)[0] / l
        X = add(scal(-1, B3), scal(kappa, e12))
        ok &= sub(X, scal(-1, sub(B3, scal(kappa, mul(I, B3, SIG))))) == {}
        ok &= lie_dim([{}, {}, X]) == 1
        ok &= add(X, B3) == scal(kappa, e12) and add(X, B3) != {}
        sq = mul(X, X, SIG)
        ok &= sq.get((), F(0)) == 1 - kappa * kappa and sq.get((0, 1, 2, 3), F(0)) == -2 * kappa
    p = [F(-1, 3), F(2, 3), F(2, 3)]
    kas = [scal(-p[i], mul(gen(0), gen(i + 1), SIG)) for i in range(3)]
    ok &= lie_dim(kas) == 6
    ok &= lie_dim([{}, {}, scal(-1, B3)]) == 1
    GA.check("horizon values (0, 0, -(1 - kappa I) B_3) generate a 1-dim algebra; Kasner values at p(1) generate 6", ok)
    return ok


# ---- GTG derivation (maintainer pass 2026-11-07, GTG proofs) ----
# The same Bianchi IX field built as a gauge field on flat spacetime with the shared engine (lib/gtg.py): labels
# (T, psi, theta, phi) = 0..3 about (T0, 0, pi/2, 0); coframe hb^{-1}(e_mu) = sum_a TH[a][mu] gamma_a with
# f^0 = N grad T, f^l = a_l sigma_l; the rotation-gauge field is SOLVED from the torsion equation (Field with no
# om) and the curvature is the store's calR(B) = -R(hb(B)) of its field strength. No Christoffel symbol is used.
import gtg  # noqa: E402


def gtg_bianchi_ix(a, da, dda):
    """Field from instant data a_l, alpha_l' = da_l, alpha_l'' = dda_l (harmonic time, N = a1 a2 a3)."""
    J = gtg.J
    sc = [J.from_taylor(0, [a[l], a[l] * da[l], a[l] * (dda[l] + da[l] * da[l]) / 2]) for l in range(3)]
    N = sc[0] * sc[1] * sc[2]
    sps, cps = gtg.sincos(1, F(0), F(1), 4, 2)
    sth, cth = gtg.sincos(2, F(1), F(0), 4, 2)
    z = J.const(0)
    TH = [[N, z, z, z],
          [z, z, sc[0] * sps, -(sc[0] * cps * sth)],
          [z, z, sc[1] * cps, sc[1] * sps * sth],
          [z, sc[2], z, sc[2] * cth]]
    return gtg.Field(TH), N.v


def check_gtg_bianchi_ix_torsion_solution_and_field_strength():
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for (a, da, dda) in JETS:
        fld, N = gtg_bianchi_ix(a, da, dda)
        ok = ok and fld.torsion_free() and fld.torsion_rank() == 24
        mu = [a[i] / (a[(i + 1) % 3] * a[(i + 2) % 3]) for i in range(3)]
        ok = ok and fld.omega(0) == {}
        for k in range(3):
            i, j = (k + 1) % 3, (k + 2) % 3
            want = add(scal(-da[k] / N, mul(gen(0), gen(k + 1), SIG)),
                       scal((mu[i] + mu[j] - mu[k]) / 2, mul(gen(i + 1), gen(j + 1), SIG)))
            ok = ok and GA.eq(fld.omega(k + 1), want)
        Rc = fld.curvature()
        V, gdV = vix([x * x for x in a])
        rico = [[gtg.ric_o(Rc, gen(x), gen(y)) for y in range(4)] for x in range(4)]
        ok = ok and all(N * N * rico[l + 1][l + 1] == dda[l] + gdV[l] for l in range(3))
        ok = ok and N * N * rico[0][0] == -sum(dda) + 2 * cross(da)
        ok = ok and all(rico[x][y] == 0 for x in range(4) for y in range(4) if x != y)
    assert ok
    return ok


def check_gtg_taub_nut_is_a_vacuum_gauge_field():
    premise("synthesis.imported-gtg-dictionary")
    ok, ran = True, 0
    # (m, l, t) with t^2 + l^2 and U(t) rational squares, t_- < t < t_+
    for m, l, t in ((F(2), F(3), F(4)), (F(3), F(4), F(3)), (F(6), F(5), F(12)), (F(0), F(1), F(0)),
                    (F(5), F(12), F(5))):
        U, Ut, da, dda, e2 = taub_nut(t, m, l)
        roots = [isq(x) for x in e2]
        ok = ok and U > 0 and None not in roots
        if not ok:
            break
        ran += 1
        fld, N = gtg_bianchi_ix(roots, da, dda)
        ok = ok and gtg.ricci_flat(fld.curvature())
        fw, Nw = gtg_bianchi_ix(roots, da, [dda[0], dda[1], dda[2] + F(1, 3)])
        ok = ok and not gtg.ricci_flat(fw.curvature())
    ok = ok and ran == 5
    assert ok
    return ok


def _isqrt(n):
    lo, hi = 0, n + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * mid < n:
            lo = mid + 1
        else:
            hi = mid
    return lo


def isq(x):
    """Exact rational square root of a nonnegative rational, or None."""
    if x < 0:
        return None
    u, v = _isqrt(x.numerator), _isqrt(x.denominator)
    return F(u, v) if F(u * u, v * v) == x else None
