"""Scaling limit of Hadamard states of the Dirac field on a gravitational field: exact checks.

Gauge of the scaling: x0 = 0, hb(x0) = 1, Omega(x0) = 0; scaled points x = l y, x' = l y'. Two test
fields, given by coframe polynomials TH[a][mu] (hb^{-1}(e_mu) = sum_a TH[a][mu] gamma_a):
  F1, a plane wave in Kerr-Schild form, hb^{-1}(a) = a - H (a . k) k, k = e0 + e3,
     H = (x1^2 - x2^2)/2 + (k . x) x1 x2: Ricci-flat, Weyl-curved at x0;
  F2, a generic polynomial coframe delta + C(x) + B(x, x) with C symmetric (so Omega(x0) = 0), Ricci and
     Weyl curvature both nonzero at x0, and nonzero metric derivatives at x0 (the store gauge is not a
     normal gauge).
The geodesic boundary-value problem from l y' (t = 0) to l y (t = 1) is solved exactly as a truncated
power series in l with polynomial coefficients in t (Picard iteration of eta'' = -l Gamma(l eta) eta' eta',
gamma = l eta); sigma/l^2 = (1/2) int g(gamma)(eta', eta') dt; d sigma/dx^mu = l g_{mu a}(x) eta'^a(1);
the Van Vleck determinant from the mixed derivatives (an infinitesimal displacement of y'); the spinor
transport rotor from dR/dt = -(1/2) Omega(gamma') R (D_a psi = a . grad psi + Omega(a) psi / 2).
Checks:
 (0) the test fields are in the store gauge (hb(x0) = 1, Omega(x0) = 0 from the store's torsion-free solver,
     torsion-free), with nonzero Weyl curvature at x0; F1 Ricci-flat, F2 not.
 (1) sigma(l y, l y') = l^2 [Q(D)/2 + l D . [(ybar . grad) hb^{-1}](D) + O(l^2)], D = y - y' (index reading
     (l/4) d_r g_{mn}(x0) (y + y')^r D^m D^n, both forms checked),
     and the eikonal identity g^{mn}(x) sigma_m sigma_n = 2 sigma holds to the computed order.
 (2) Van Vleck: Delta = 1 + 0 l + (l^2/6) Ric^o(D, D) + O(l^3) with the store's Ricci (ric_o);
     transport rotor: R = 1 + 0 l - (l^2/2) d_r Omega(e_m)(x0) ybar^r D^m + O(l^3), ybar = (y + y')/2, and
     R reverse(R) = 1 to the computed order; so U = Delta^(1/2) R = 1 + O(l^2). In a gauge with Omega(x0) =
     W != 0 (constant bivectors added) R = 1 - (l/2) W(D) + O(l^2), and for every mu the O(1) parts of
     l^-1 d_{y^mu} R and Omega(e_mu)(l y) R/2 cancel: the D_x U and connection terms together are O(l^2) in
     every gauge with hb(x0) = 1.
 (3) The scaled leading Hadamard term: D_x sigma = l hb^{-1}(eta'(1)) (the physical tangent at x; the
     identity g^mu sigma_mu = hb^{-1}(gamma'(1)) checked against the reciprocal coframe). With Laurent series
     (sigma = l^2 sigma_l, D_x sigma = l v, weight 3) the leading term l^3 D_x(sigma) U/sigma^2 has l^0
     coefficient 4 D/Q(D)^2 (so -l^3 D_x(1/sigma) U -> the flat massless kernel -4 D/Q^2 = grad(1/sigma_flat))
     and the stated l^1 geometry coefficient (zero on the plane wave); the mass term l^3 m0 U/sigma, its power
     computed, starts at l^1 with coefficient m0/s0 for m0 = 1/2, 3 (and vanishes for m0 = 0).
 (4) The flat massless kernel: grad(z/Q(z)^2) = 0 off the cone (jets), grad(2/Q(z)) = -4 z/Q(z)^2,
     c^3 K(c z) = K(z); constants: -(1/8 pi^2)(1/sigma) with sigma = Q/2 is D_+ = -1/(4 pi^2 Q), and
     i grad D_+ e0 = (i/(2 pi^2)) z e0 / Q(z)^2 (coefficients of 1/pi^2).
 (5) Scaling powers at weight 3/2 + 3/2, computed as Laurent orders of the exact series on the generic
     field: leading 0, mass 1, connection 2, D_x U 2 (rotor part by an infinitesimal displacement, Van Vleck
     part from (2)); log term: the flat-field coefficient V(x0, x0) = -m0^2/2 is computed with second-order
     jets as the V that makes (box + m0^2)(1/sigma + V log sigma) free of 1/sigma, and the term
     l^3 V(x0, x0) D_x sigma/sigma has order 2 and coefficient -m0^2 D/Q(D). (On a Weyl-curved field V(x0, x0)
     acquires a curvature part, not computed; only the order is used. The C^1 remainder's l^3: proof only.)
 (6) Store dilation against normal-coordinate dilation: the initial velocity eta'(0) of the geodesic from
     x0 to l y is Phi_l(y) = y + (l/2) Gamma(x0)(y, y) + O(l^2) (normal coordinates of l y, divided by l), the
     Gauss lemma sigma(x0, l y) = l^2 Q(Phi_l(y))/2 holds to the computed order, and Gamma(x0)(a, b) =
     (a . grad hb^{-1})(b) (GA form, Omega(x0) = 0): Phi_l -> id.
Exact arithmetic only (Fractions); i and pi enter only as named constants in (4).
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

S = (1, -1, -1, -1)
ETA = [[F(S[i]) if i == j else F(0) for j in range(4)] for i in range(4)]
NL = 3
# ---------- polynomials in (l, t, s) ----------
def padd(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            v = out.get(e, F(0)) + c
            if v:
                out[e] = v
            elif e in out:
                del out[e]
    return out


def pscal(c, p):
    c = F(c)
    return {e: c * v for e, v in p.items()} if c else {}


def pmul(p, q):
    out = {}
    for (i1, j1, k1), c1 in p.items():
        for (i2, j2, k2), c2 in q.items():
            i, k = i1 + i2, k1 + k2
            if i > NL or k > 1:
                continue
            e = (i, j1 + j2, k)
            v = out.get(e, F(0)) + c1 * c2
            if v:
                out[e] = v
            elif e in out:
                del out[e]
    return out


def pc(c):
    c = F(c)
    return {(0, 0, 0): c} if c else {}


L = {(1, 0, 0): F(1)}
T = {(0, 1, 0): F(1)}
SV = {(0, 0, 1): F(1)}


def pint(p):
    """Integral from 0 to t."""
    return {(i, j + 1, k): c / (j + 1) for (i, j, k), c in p.items()}


def pdt(p):
    return {(i, j - 1, k): c * j for (i, j, k), c in p.items() if j}


def pat1(p):
    """Value at t = 1 (keeps l, s)."""
    out = {}
    for (i, j, k), c in p.items():
        e = (i, 0, k)
        out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def pdiv_l(p):
    """p / l when p has no l^0 term."""
    assert all(i >= 1 for (i, j, k) in p)
    return {(i - 1, j, k): c for (i, j, k), c in p.items()}


def coef(p, i, k=0):
    """Coefficient of l^i s^k (t-free part expected after pat1)."""
    return p.get((i, 0, k), F(0))


# ---------- polynomials in the labels x ----------
def xpoly_eval(xp, X):
    """Evaluate a label polynomial {exp4: c} at X = list of four (l,t,s)-polynomials."""
    out = {}
    pw = [[pc(1)] for _ in range(4)]
    for (a0, a1, a2, a3), c in xp.items():
        term = pc(c)
        for m, a in enumerate((a0, a1, a2, a3)):
            while len(pw[m]) <= a:
                pw[m].append(pmul(pw[m][-1], X[m]))
            term = pmul(term, pw[m][a])
        out = padd(out, term)
    return out


def xmul(p, q):
    out = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            out[e] = out.get(e, F(0)) + c1 * c2
    return {e: c for e, c in out.items() if c}


def xadd(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def xscal(c, p):
    return {e: F(c) * v for e, v in p.items() if F(c) * v}


def xd(p, m):
    out = {}
    for e, c in p.items():
        if e[m]:
            f = list(e)
            f[m] -= 1
            out[tuple(f)] = c * e[m]
    return out


def xval(p):
    return p.get((0, 0, 0, 0), F(0))


def xc(c):
    return {(0, 0, 0, 0): F(c)} if c else {}


def xv(m):
    return {tuple(1 if i == m else 0 for i in range(4)): F(1)}


def metric_of(TH):
    """g_{mu nu} = sum_a S[a] TH[a][mu] TH[a][nu] as label polynomials."""
    return [[xadd(*[xscal(S[a], xmul(TH[a][m], TH[a][n])) for a in range(4)]) for n in range(4)]
            for m in range(4)]


# ---------- the geodesic boundary-value problem ----------
def matinv_series(Mp):
    """Inverse of a 4x4 matrix of (l,t,s)-polys equal to ETA + O(l) (Neumann series)."""
    D = [[padd(Mp[i][j], pc(-ETA[i][j])) for j in range(4)] for i in range(4)]
    # (ETA + D)^-1 = sum_k (-ETA D)^k ETA, ETA^-1 = ETA
    term = [[pc(ETA[i][j]) for j in range(4)] for i in range(4)]
    out = [row[:] for row in term]
    for _ in range(NL):
        nt = [[{} for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                acc = {}
                for k in range(4):
                    if ETA[i][i] and D[i][k] and term[k][j]:
                        acc = padd(acc, pscal(-ETA[i][i], pmul(D[i][k], term[k][j])))
                nt[i][j] = acc
        term = nt
        out = [[padd(out[i][j], term[i][j]) for j in range(4)] for i in range(4)]
    return out


def geodesic(gx, dgx, y, yp, dy=None, dyp=None, iters=None):
    """eta(t) with gamma = l eta from l yp (t = 0) to l y (t = 1): label-polynomial metric gx,
    derivatives dgx[r][m][n]; optional infinitesimal displacement dy (of y) or dyp (of yp) along s.
    Returns (eta, etadot, gmat at gamma, ginv at gamma)."""
    iters = NL + 1 if iters is None else iters
    Y = [padd(pc(y[m]), pscal(dy[m], SV) if dy else {}) for m in range(4)]
    YP = [padd(pc(yp[m]), pscal(dyp[m], SV) if dyp else {}) for m in range(4)]
    eta0 = [padd(YP[m], pmul(T, padd(Y[m], pscal(-1, YP[m])))) for m in range(4)]
    eta = eta0
    for _ in range(iters):
        X = [pmul(L, eta[m]) for m in range(4)]
        G = [[xpoly_eval(gx[m][n], X) for n in range(4)] for m in range(4)]
        Gi = matinv_series(G)
        dG = [[[xpoly_eval(dgx[r][m][n], X) for n in range(4)] for m in range(4)] for r in range(4)]
        ed = [pdt(eta[m]) for m in range(4)]
        # Gamma_{m a b} ed^a ed^b with Gamma_{m a b} = (d_a g_mb + d_b g_ma - d_m g_ab)/2
        low = []
        for m in range(4):
            acc = {}
            for a in range(4):
                for b in range(4):
                    if not ed[a] or not ed[b]:
                        continue
                    gam = padd(pscal(F(1, 2), dG[a][m][b]), pscal(F(1, 2), dG[b][m][a]),
                               pscal(F(-1, 2), dG[m][a][b]))
                    if gam:
                        acc = padd(acc, pmul(gam, pmul(ed[a], ed[b])))
            low.append(acc)
        acc_up = [padd(*[pmul(Gi[m][n], low[n]) for n in range(4)]) for m in range(4)]
        # eta'' = -l Gamma(gamma) eta' eta'  (gamma = l eta, d/dgamma = l^-1 d/deta)
        f = [pscal(-1, pmul(L, acc_up[m])) for m in range(4)]
        new = []
        for m in range(4):
            I2 = pint(pint(f[m]))
            corr = padd(I2, pscal(-1, pmul(T, pat1(I2))))
            new.append(padd(eta0[m], corr))
        eta = new
    X = [pmul(L, eta[m]) for m in range(4)]
    G = [[xpoly_eval(gx[m][n], X) for n in range(4)] for m in range(4)]
    return eta, [pdt(e) for e in eta], G, matinv_series(G)


def synge_scaled(G, ed):
    """sigma / l^2 = (1/2) int_0^1 g(gamma)(eta', eta') dt."""
    acc = {}
    for m in range(4):
        for n in range(4):
            if G[m][n] and ed[m] and ed[n]:
                acc = padd(acc, pmul(G[m][n], pmul(ed[m], ed[n])))
    return pscal(F(1, 2), pat1(pint(acc)))


def end_momentum(G, ed):
    """p_mu = g_{mu a}(x) eta'^a(1) = (d sigma / d x^mu) / l."""
    G1 = [[pat1(G[m][n]) for n in range(4)] for m in range(4)]
    e1 = [pat1(e) for e in ed]
    return [padd(*[pmul(G1[m][a], e1[a]) for a in range(4)]) for m in range(4)]


# ---------- multivector-valued (l,t,s)-polynomials ----------
def mvadd(*xs):
    out = {}
    for x in xs:
        for b, p in x.items():
            q = padd(out.get(b, {}), p)
            if q:
                out[b] = q
            elif b in out:
                del out[b]
    return out


def mvmul(x, y):
    out = {}
    for b1, p1 in x.items():
        for b2, p2 in y.items():
            sg, b = GA.blade_mul(b1, b2, S)
            q = pmul(p1, p2)
            if q:
                out = mvadd(out, {b: pscal(sg, q)})
    return out


def mvscal_p(p, x):
    return {b: pmul(p, q) for b, q in x.items() if pmul(p, q)}


def mv_from_ga(x):
    return {b: pc(c) for b, c in x.items() if c}


def mv_at1(x):
    return {b: pat1(p) for b, p in x.items() if pat1(p)}


def mvrev(x):
    out = {}
    for b, p in x.items():
        r = len(b)
        sg = -1 if (r * (r - 1) // 2) % 2 else 1
        out[b] = pscal(sg, p)
    return out


def omega_polys(TH, order=3):
    """Omega(e_mu) as label polynomials (bivector dicts), from the store's torsion-free solver."""
    J = [[gtg.Jet(c=dict(TH[a][m]), nv=4, order=order) for m in range(4)] for a in range(4)]
    Fd = gtg.Field(J)
    out = []
    for m in range(4):
        out.append({b: dict(c.c) for b, c in Fd.Om[m].items() if isinstance(c, gtg.Jet) and c.c})
    return Fd, out


def transport_rotor(Om, eta, ed):
    """R(1) with dR/dt = -(1/2) Omega(gamma') R, gamma = l eta, R(0) = 1 (spinor transport x' -> x)."""
    X = [pmul(L, eta[m]) for m in range(4)]
    A = {}
    for m in range(4):
        for b, xp in Om[m].items():
            A = mvadd(A, {b: pscal(F(-1, 2), pmul(L, pmul(ed[m], xpoly_eval(xp, X))))})
    R = {(): pc(1)}
    for _ in range(NL + 1):
        integrand = mvmul(A, R)
        R = mvadd({(): pc(1)}, {b: pint(p) for b, p in integrand.items()})
    return R


def christoffel_at0(gx):
    """Gamma^r_{mn} as label polynomials truncated at degree 1, and Ricci_{sn}(0) (standard index formula)."""
    h1 = [[{e: c for e, c in gx[m][n].items() if sum(e) == 1} for n in range(4)] for m in range(4)]
    gi = [[xadd(xc(ETA[r][l]), xscal(-ETA[r][r] * ETA[l][l], h1[r][l])) for l in range(4)] for r in range(4)]
    low = [[[xscal(F(1, 2), xadd(xd(gx[l][n], m), xd(gx[l][m], n), xscal(-1, xd(gx[m][n], l))))
             for n in range(4)] for m in range(4)] for l in range(4)]
    def tr(p):
        return {e: c for e, c in p.items() if sum(e) <= 1}
    Gam = [[[tr(xadd(*[xmul(tr(gi[r][l]), tr(low[l][m][n])) for l in range(4)])) for n in range(4)]
            for m in range(4)] for r in range(4)]
    def at0(p):
        return xval(p)
    def d0(p, m):
        return xval(xd(p, m))
    Ric = [[F(0)] * 4 for _ in range(4)]
    for s_ in range(4):
        for n in range(4):
            acc = F(0)
            for r in range(4):
                # R^r_{s r n} = d_r Gam^r_{n s} - d_n Gam^r_{r s} + Gam^r_{r l} Gam^l_{n s} - Gam^r_{n l} Gam^l_{r s}
                acc += d0(Gam[r][n][s_], r) - d0(Gam[r][r][s_], n)
                for l in range(4):
                    acc += at0(Gam[r][r][l]) * at0(Gam[l][n][s_]) - at0(Gam[r][n][l]) * at0(Gam[l][r][s_])
            Ric[s_][n] = acc
    return Gam, Ric


def det4(M, mul, add, neg):
    """Determinant by Laplace expansion (generic ring ops)."""
    def det(rows, cols):
        if len(rows) == 1:
            return M[rows[0]][cols[0]]
        acc = None
        for j, c in enumerate(cols):
            sub = det(rows[1:], cols[:j] + cols[j + 1:])
            term = mul(M[rows[0]][c], sub)
            if j % 2:
                term = neg(term)
            acc = term if acc is None else add(acc, term)
        return acc
    return det(list(range(4)), list(range(4)))


def lseries(p):
    """Coefficient list in l of a t-free, s-free polynomial."""
    return [p.get((i, 0, 0), F(0)) for i in range(NL + 1)]


def van_vleck(gx, dgx, y, yp):
    """Delta(x, x') = -det(-sigma_{mu nu'}) / sqrt(det g(x) det g(x')) as an l-series (coefficient list)."""
    cols = []
    for nu in range(4):
        dyp = [F(1) if i == nu else F(0) for i in range(4)]
        eta, ed, G, Gi = geodesic(gx, dgx, y, yp, dyp=dyp)
        p = end_momentum(G, ed)
        cols.append([{(i, 0, 0): c for (i, j, k), c in pm.items() if k == 1} for pm in p])
    Mneg = [[pscal(-1, cols[n][m]) for n in range(4)] for m in range(4)]
    d = det4(Mneg, pmul, padd, lambda a: pscal(-1, a))
    Xx = [pmul(L, pc(y[m])) for m in range(4)]
    Xp = [pmul(L, pc(yp[m])) for m in range(4)]
    gxx = [[xpoly_eval(gx[m][n], Xx) for n in range(4)] for m in range(4)]
    gxp = [[xpoly_eval(gx[m][n], Xp) for n in range(4)] for m in range(4)]
    dd = pmul(det4(gxx, pmul, padd, lambda a: pscal(-1, a)), det4(gxp, pmul, padd, lambda a: pscal(-1, a)))
    inv_sqrt = GA.ps_pow_rat(lseries(dd), F(-1, 2), NL + 1)
    return GA.ps_mul([-c for c in lseries(d)], inv_sqrt, NL + 1)


# ---------- the two test fields ----------
def xm(c, *idx):
    e = [0, 0, 0, 0]
    for i in idx:
        e[i] += 1
    return {tuple(e): F(c)}


def field_plane_wave():
    H = xadd(xm(F(1, 2), 1, 1), xm(F(-1, 2), 2, 2), xm(1, 0, 1, 2), xm(-1, 3, 1, 2))
    klow, kup = (1, 0, 0, -1), (1, 0, 0, 1)
    return [[xadd(xc(1 if a == m else 0), xscal(-klow[m] * kup[a], H)) for m in range(4)] for a in range(4)]


def field_generic():
    TH = [[xc(1 if a == m else 0) for m in range(4)] for a in range(4)]

    def add(a, m, p):
        TH[a][m] = xadd(TH[a][m], p)
    for (a, m, n, c) in [(0, 0, 1, F(1, 2)), (1, 1, 2, F(1, 3)), (2, 3, 3, F(-1, 2)), (3, 0, 2, F(1, 4))]:
        add(a, m, xm(c, n))
        if m != n:
            add(a, n, xm(c, m))
    add(0, 0, xm(F(1, 3), 1, 1))
    add(2, 1, xm(F(1, 2), 0, 3))
    add(3, 3, xm(F(-1, 4), 2, 2))
    add(1, 0, xm(F(1, 5), 1, 2))
    return TH


def setup(TH):
    gx = metric_of(TH)
    dgx = [[[xd(gx[m][n], r) for n in range(4)] for m in range(4)] for r in range(4)]
    return gx, dgx


PAIRS = [([F(1, 2), F(1), F(-1, 3), F(2)], [F(-1), F(1, 4), F(1), F(0)]),
         ([F(2), F(1, 3), F(0), F(-1, 2)], [F(0), F(-1, 2), F(1, 5), F(1)]),
         ([F(1), F(0), F(1, 2), F(0)], [F(-1, 3), F(1, 3), F(0), F(1, 4)])]
MASSES = (F(0), F(1, 2), F(3))


def qf(v):
    return sum(S[i] * v[i] * v[i] for i in range(4))


def diff(y, yp):
    return [y[i] - yp[i] for i in range(4)]


def _gauge_premises():
    premise("synthesis.imported-gtg-dictionary")


def check_test_fields_are_in_the_store_gauge_and_weyl_curved():
    _gauge_premises()
    ok = True
    for TH, ricci_flat in ((field_plane_wave(), True), (field_generic(), False)):
        ok &= all(xval(TH[a][m]) == (1 if a == m else 0) for a in range(4) for m in range(4))
        Fd, Om = omega_polys(TH)
        ok &= all(gtg.m_val(Fd.Om[m]) == {} for m in range(4))
        ok &= Fd.torsion_free()
        Rc = Fd.curvature()
        W = gtg.weyl_op(Rc)
        ok &= any(v for v in W.values())
        ric = [[gtg.ric_o(Rc, GA.gen(m), GA.gen(n)) for n in range(4)] for m in range(4)]
        ok &= all(ric[m][n] == 0 for m in range(4) for n in range(4)) == ricci_flat
    GA.check("test fields: hb(x0) = 1, Omega(x0) = 0 (store torsion-free solver), Weyl curvature nonzero at "
             "x0; the plane wave Ricci-flat, the generic field not", ok)
    return ok


def check_synge_function_scales_to_half_the_flat_square():
    _gauge_premises()
    premise("synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard")
    ok = True
    for TH in (field_plane_wave(), field_generic()):
        gx, dgx = setup(TH)
        for y, yp in PAIRS:
            D = diff(y, yp)
            yb = [y[i] + yp[i] for i in range(4)]
            eta, ed, G, Gi = geodesic(gx, dgx, y, yp)
            st = synge_scaled(G, ed)
            ok &= coef(st, 0) == qf(D) / 2
            s1 = sum(xval(dgx[r][m][n]) * yb[r] * D[m] * D[n]
                     for r in range(4) for m in range(4) for n in range(4)) / 4
            ok &= coef(st, 1) == s1
            # GA reading: s1 = d . [(ybar . grad) hb^{-1}](d) at x0, hb^{-1}(d) = sum_a gamma_a TH[a][m] d^m
            ga1 = sum(S[a] * D[a] * sum(xval(xd(TH[a][m], r)) * yb[r] * D[m] for r in range(4) for m in range(4))
                      for a in range(4)) / 2
            ok &= ga1 == s1
            p = end_momentum(G, ed)
            Gi1 = [[pat1(Gi[m][n]) for n in range(4)] for m in range(4)]
            eik = padd(*[pmul(Gi1[m][n], pmul(p[m], p[n])) for m in range(4) for n in range(4)])
            ok &= padd(eik, pscal(-2, st)) == {}
            ok &= coef(st, 2) != 0
    GA.check("sigma(l y, l y') = l^2 [Q(D)/2 + l (1/4) dg(x0)(y + y') D D + O(l^2)] and the eikonal identity "
             "holds to order l^3 on both fields", ok)
    return ok


def check_van_vleck_determinant_and_transport_rotor_tend_to_one():
    _gauge_premises()
    premise("synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard")
    ok = True
    for TH in (field_plane_wave(), field_generic()):
        gx, dgx = setup(TH)
        Fd, Om = omega_polys(TH)
        Rc = Fd.curvature()
        ric = [[gtg.ric_o(Rc, GA.gen(m), GA.gen(n)) for n in range(4)] for m in range(4)]
        dOm = [[{b: xval(xd(p, r)) for b, p in Om[m].items() if xval(xd(p, r))} for r in range(4)]
               for m in range(4)]
        for y, yp in PAIRS[:2]:
            D = diff(y, yp)
            yb = [(y[i] + yp[i]) / 2 for i in range(4)]
            dl = van_vleck(gx, dgx, y, yp)
            ok &= dl[0] == 1 and dl[1] == 0
            ok &= dl[2] == sum(ric[m][n] * D[m] * D[n] for m in range(4) for n in range(4)) / 6
            eta, ed, G, Gi = geodesic(gx, dgx, y, yp)
            R1 = mv_at1(transport_rotor(Om, eta, ed))
            ok &= {b: coef(p, 0) for b, p in R1.items() if coef(p, 0)} == {(): F(1)}
            ok &= all(coef(p, 1) == 0 for p in R1.values())
            want = {}
            for m in range(4):
                for r in range(4):
                    for b, c in dOm[m][r].items():
                        want[b] = want.get(b, F(0)) - c * yb[r] * D[m] / 2
            got = {b: coef(p, 2) for b, p in R1.items() if b != () and coef(p, 2)}
            ok &= got == {b: c for b, c in want.items() if c} and bool(got)
            RR = mvmul(R1, mvrev(R1))
            ok &= {b: p for b, p in RR.items() if p} == {(): pc(1)}
            # a gauge with Omega(x0) != 0: add constant bivectors W_mu; then R = 1 - (l/2) W(d) + O(l^2)
            W = [{(0, 1): F(1, 3)}, {(1, 2): F(-1, 2)}, {(0, 3): F(2)}, {(2, 3): F(1, 5), (0, 2): F(1)}]
            Om2 = [dict(Om[m]) for m in range(4)]
            for m in range(4):
                for b, c in W[m].items():
                    Om2[m][b] = xadd(Om2[m].get(b, {}), xc(c))
            R2 = mv_at1(transport_rotor(Om2, eta, ed))
            want1 = {}
            for m in range(4):
                for b, c in W[m].items():
                    want1[b] = want1.get(b, F(0)) - c * D[m] / 2
            ok &= {b: coef(p, 1) for b, p in R2.items() if coef(p, 1)} == {b: c for b, c in want1.items() if c}
            RR2 = mvmul(R2, mvrev(R2))
            ok &= {b: p for b, p in RR2.items() if p} == {(): pc(1)}
            # in that gauge the O(1) parts of l^-1 d_{y^mu} R and (1/2) Omega(e_mu)(l y) R cancel for every mu,
            # so l^3 g^mu (d_mu U + Omega(e_mu) U/2)/sigma is O(l^2) whatever Omega(x0) is
            X = [pmul(L, pc(y[m])) for m in range(4)]
            for mu in range(4):
                dy = [F(1) if i == mu else F(0) for i in range(4)]
                et2, ed2, G2, Gi2 = geodesic(gx, dgx, y, yp, dy=dy)
                Rs = mv_at1(transport_rotor(Om2, et2, ed2))
                dR = {b: {(i, 0, 0): c for (i, j, k), c in q.items() if k == 1} for b, q in Rs.items()}
                ok &= all(coef(q, 0) == 0 for q in dR.values())
                conn = mvmul({b: pscal(F(1, 2), xpoly_eval(xp, X)) for b, xp in Om2[mu].items()}, R2)
                br = mvadd({b: pdiv_l(q) for b, q in dR.items() if q}, conn)
                ok &= all(coef(q, 0) == 0 for q in br.values())
                ok &= any(coef(q, 1) != 0 for q in dR.values())
    GA.check("Van Vleck Delta = 1 + 0 l + (l^2/6) Ric(D, D) + O(l^3) with the store's Ricci; transport rotor "
             "R = 1 + 0 l - (l^2/2) dOmega(x0)(ybar) (D) + O(l^3), R reverse(R) = 1: U -> 1; with Omega(x0) != 0 "
             "the O(1) parts of l^-1 d_y R and Omega(e_mu) R/2 cancel", ok)
    return ok


def lz(power, series):
    """A Laurent quantity l^power * series (series a coefficient list, leading term allowed zero)."""
    k = next((i for i, c in enumerate(series) if c), len(series))
    return (power + k, list(series[k:]) + [F(0)] * k)


def lzmul(a, b):
    n = len(a[1])
    return (a[0] + b[0], GA.ps_mul(a[1], b[1], n))


def lzinv(a):
    n = len(a[1])
    return (-a[0], GA.ps_inv(a[1], n))


def lzcoef(a, k):
    """Coefficient of l^k."""
    i = k - a[0]
    if i != int(i) or not 0 <= i < len(a[1]):
        return F(0)
    return a[1][int(i)]


def reciprocal_coframe_at_x(TH, y):
    """Hi[mu][a](l y) (hb(gamma_a) = sum Hi[mu][a] e_mu) as l-series: inverse of TH(l y)."""
    X = [pmul(L, pc(y[m])) for m in range(4)]
    THx = [[xpoly_eval(TH[a][m], X) for m in range(4)] for a in range(4)]
    # TH = I + N, N = O(l): inverse = sum (-N)^k
    N = [[padd(THx[a][m], pc(-1 if a == m else 0)) for m in range(4)] for a in range(4)]
    term = [[pc(1 if a == m else 0) for m in range(4)] for a in range(4)]
    inv = [row[:] for row in term]
    for _ in range(NL):
        term = [[pscal(-1, padd(*[pmul(term[i][k], N[k][j]) for k in range(4)])) for j in range(4)]
                for i in range(4)]
        inv = [[padd(inv[i][j], term[i][j]) for j in range(4)] for i in range(4)]
    return THx, inv  # inv[mu][a]: (TH^-1)[mu][a]


def lseries_div(num, den, n):
    return GA.ps_mul(num, GA.ps_inv(den, n), n)


def check_scaled_dirac_parametrix_tends_to_the_flat_massless_kernel():
    _gauge_premises()
    premise("synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard")
    premise("synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field")
    premise("field-theory.second-quantisation")
    ok = True
    n = NL + 1
    for TH, pw in ((field_plane_wave(), True), (field_generic(), False)):
        gx, dgx = setup(TH)
        Fd, Om = omega_polys(TH)
        Gam0 = christoffel_at0(gx)[0]
        for y, yp in PAIRS:
            D = diff(y, yp)
            Q = qf(D)
            s0 = Q / 2
            eta, ed, G, Gi = geodesic(gx, dgx, y, yp)
            p = end_momentum(G, ed)
            st = lseries(synge_scaled(G, ed))
            THx, Hi = reciprocal_coframe_at_x(TH, y)
            e1 = [pat1(e) for e in ed]
            # physical tangent hb^{-1}(eta'(1)) = sum_a gamma_a TH[a][al](x) eta'^al(1)
            v = [lseries(padd(*[pmul(pat1(THx[a][al]), e1[al]) for al in range(4)])) for a in range(4)]
            # g^mu p_mu with g^mu = sum_a Hi[mu][a] gamma^a, gamma^a = S[a] gamma_a
            gp = [lseries(pscal(S[a], padd(*[pmul(pat1(Hi[mu][a]), p[mu]) for mu in range(4)])))
                  for a in range(4)]
            ok &= gp == v
            dl = van_vleck(gx, dgx, y, yp) if not pw else None
            Uh = GA.ps_pow_rat(dl, F(1, 2), n) if dl else [F(1)] + [F(0)] * (n - 1)
            weight = F(3, 2) + F(3, 2)                       # l^(3/2) per leg
            sigma = lz(2, st)                                 # sigma = l^2 sigma_l
            dsig = [lz(1, v[a]) for a in range(4)]            # D_x sigma = hb^{-1}(gamma'(1)), gamma' = l eta'
            U = lz(0, Uh)
            isig = lzinv(sigma)
            lead = [lzmul((weight, [F(1)] + [F(0)] * (n - 1)), lzmul(lzmul(dsig[a], U), lzmul(isig, isig)))
                    for a in range(4)]
            for m0 in MASSES:
                mass = lzmul(lz(weight, [m0] + [F(0)] * (n - 1)), lzmul(U, isig))
                # vector part -l^3 D_x sigma U/sigma^2: l^0 coefficient -4 D/Q^2, the flat massless kernel
                ok &= all(-lzcoef(lead[a], 0) == -4 * D[a] / Q ** 2 for a in range(4))
                # scalar part l^3 m0 U/sigma: no l^0 term, l^1 coefficient m0/s0 (zero only for m0 = 0)
                ok &= lzcoef(mass, 0) == 0 and lzcoef(mass, 1) == m0 / s0
                ok &= (mass[0] == 1) == (m0 != 0)
                if pw:
                    ok &= all(lzcoef(lead[a], 1) == 0 for a in range(4)) and lzcoef(mass, 1) == 2 * m0 / Q
                else:
                    s1 = st[1]
                    v1 = [sum(xval(xd(TH[a][al], nu)) * y[nu] * D[al] for nu in range(4) for al in range(4))
                          - sum(xval(Gam0[a][b][c]) * D[b] * D[c] for b in range(4) for c in range(4)) / 2
                          for a in range(4)]
                    ok &= all(-lzcoef(lead[a], 1) == -(v1[a] / s0 ** 2 - 2 * s1 * D[a] / s0 ** 3)
                              for a in range(4))
                    ok &= any(lzcoef(lead[a], 1) != 0 for a in range(4))
    GA.check("scaled leading Hadamard term: D_x sigma = l hb^{-1}(eta'(1)); l^3 (D_x + m0)(U/sigma) has l^0 "
             "coefficient -4 D/Q(D)^2 (flat massless) on both fields; the mass term, its power computed from "
             "sigma = l^2 sigma_l and the weight, starts at l^1 with m0/s0; the l^1 coefficient of the leading "
             "term is the stated geometry term (zero on the plane wave)", ok)
    return ok


def jets_at(z0):
    """First-order jets of the four labels at the point z0."""
    return [gtg.Jet.var(i, z0[i], 4, 1) for i in range(4)]


def check_flat_massless_kernel_and_normalisation():
    premise("synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem")
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    premise("field-theory.second-quantisation")
    ok = True
    E = [GA.gen(i) for i in range(len(S))]
    for z0 in [diff(y, yp) for y, yp in PAIRS] + [list(y) for y, _ in PAIRS]:
        J = jets_at(z0)
        Qj = J[0] * J[0] - J[1] * J[1] - J[2] * J[2] - J[3] * J[3]
        ok &= Qj.v != 0
        Kc = [J[i] / (Qj * Qj) for i in range(len(S))]          # components of z/Q^2 (upper index)
        # grad = e^mu d_mu = sum S[mu] e_mu d_mu acting on the vector z/Q^2
        grad = {}
        for mu in range(len(S)):
            for a in range(len(S)):
                c = S[mu] * Kc[a].d(mu).v
                if c:
                    grad = GA.add(grad, GA.scal(c, GA.mul(E[mu], E[a], S)))
        ok &= GA.is_zero(grad)
        inv = 2 / Qj
        ok &= all(S[mu] * inv.d(mu).v == -4 * z0[mu] / Qj.v ** 2 for mu in range(len(S)))
        for c in MASSES[1:]:
            Qc = c * c * Qj.v
            ok &= all(c ** 3 * (c * z0[a]) / Qc ** 2 == z0[a] / Qj.v ** 2 for a in range(len(S)))
    # constants (coefficients of 1/pi^2): Hadamard -(1/8)(1/sigma), sigma = Q/2, is D_+ = -(1/4)/Q;
    # i grad D_+ = i (1/4) 2 z/Q^2 = i (1/2) z/Q^2, the kernel (i/(2 pi^2)) z e0/Q^2
    had, dplus = F(-1, 8), F(-1, 4)
    ok &= had * 2 == dplus and -dplus * 2 == F(1, 2)
    GA.check("flat massless kernel: grad(z/Q^2) = 0 off the cone, grad(2/Q) = -4 z/Q^2, weight 3 homogeneity; "
             "-(1/8 pi^2)/sigma = D_+, i grad D_+ e0 = (i/2 pi^2) z e0/Q^2", ok)
    return ok


def lowest(series):
    """(power, coefficient) of the lowest nonzero term of an l-series, or (None, 0)."""
    for k, c in enumerate(series):
        if c:
            return k, c
    return None, F(0)


def flat_log_coefficient(m0):
    """V(x0, x0) for the flat field: the coefficient V with (box + m0^2)(1/sigma + V log sigma) free of 1/sigma,
    sigma = Q(z)/2, computed with second-order jets at several points (box log sigma = box sigma/sigma -
    Q(grad sigma)/sigma^2); returns it if it is the same at every point, else None."""
    vals = set()
    for y, yp in PAIRS:
        z0 = diff(y, yp)
        J = [gtg.Jet.var(i, z0[i], 4, 2) for i in range(4)]
        sg = (J[0] * J[0] - J[1] * J[1] - J[2] * J[2] - J[3] * J[3]) / 2
        inv = 1 / sg
        box = lambda f: sum((S[m] * f.d(m).d(m).v for m in range(4)), F(0))
        grad2 = sum((S[m] * sg.d(m).v * sg.d(m).v for m in range(4)), F(0))
        boxlog = box(sg) / sg.v - grad2 / sg.v ** 2
        vals.add(-(box(inv) + m0 * m0 * inv.v) / boxlog)
    return vals.pop() if len(vals) == 1 else None


def check_scaling_powers_of_the_hadamard_terms():
    _gauge_premises()
    premise("synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard")
    premise("synthesis.imported-microlocal-hadamard-condition")
    ok = True
    n = NL + 1
    TH = field_generic()
    gx, dgx = setup(TH)
    Fd, Om = omega_polys(TH)
    Rc = Fd.curvature()
    ric = [[gtg.ric_o(Rc, GA.gen(m), GA.gen(k)) for k in range(4)] for m in range(4)]
    for y, yp in PAIRS[:2]:
        D = diff(y, yp)
        eta, ed, G, Gi = geodesic(gx, dgx, y, yp)
        st = lseries(synge_scaled(G, ed))
        inv_s = GA.ps_inv(st, n)
        THx, Hi = reciprocal_coframe_at_x(TH, y)
        e1 = [pat1(e) for e in ed]
        v = [lseries(padd(*[pmul(pat1(THx[a][al]), e1[al]) for al in range(4)])) for a in range(4)]
        dl = van_vleck(gx, dgx, y, yp)
        # leading term -l^3 (D_x sigma) U / sigma^2 = -v U / s~^2: power 0
        lead = [GA.ps_mul(v[a], GA.ps_mul(inv_s, inv_s, n), n) for a in range(4)]
        ok &= min(lowest(lead[a])[0] for a in range(4) if lowest(lead[a])[0] is not None) == 0
        # mass term l^3 m0 U/sigma, sigma = l^2 s~: power computed, 1
        weight = F(3, 2) + F(3, 2)
        isig = lzinv(lz(2, st))
        ok &= lzmul((weight, [F(1)] + [F(0)] * (n - 1)), lzmul(lz(0, dl), isig))[0] == 1
        # connection term l^3 g^mu Omega(e_mu)(l y) U / (2 sigma) = l (1/2) g^mu Omega_mu(l y)/s~: power 2
        X = [pmul(L, pc(y[m])) for m in range(4)]
        conn = {}
        for mu in range(4):
            gmu = {(a,): pscal(S[a], pat1(Hi[mu][a])) for a in range(4) if pat1(Hi[mu][a])}
            Omx = {b: xpoly_eval(xp, X) for b, xp in Om[mu].items()}
            conn = mvadd(conn, mvmul(gmu, {b: pmul(L, pscal(F(1, 2), q)) for b, q in Omx.items() if q}))
        cpow = [lowest(GA.ps_mul(lseries(q), inv_s, n))[0] for q in conn.values()]
        ok &= min(c for c in cpow if c is not None) == 2
        # D_x U term l^3 g^mu d_mu U/sigma = (d_y U)/s~ with U = 1 + l^2 u2: power 2 (rotor part by an
        # infinitesimal displacement of y, Van Vleck part from Delta_2 = Ric(D, D)/6)
        dpow = []
        for mu in range(4):
            dy = [F(1) if i == mu else F(0) for i in range(4)]
            et2, ed2, G2, Gi2 = geodesic(gx, dgx, y, yp, dy=dy)
            R1 = mv_at1(transport_rotor(Om, et2, ed2))
            dR = {b: [p.get((i, 0, 1), F(0)) for i in range(n)] for b, p in R1.items()}
            dDel = [F(0), F(0), sum(ric[mu][k] * D[k] for k in range(4)) / 6] + [F(0)] * (n - 3)
            dR[()] = [a + b / 2 for a, b in zip(dR.get((), [F(0)] * n), dDel)]
            dpow += [lowest(GA.ps_mul(c, inv_s, n))[0] for c in dR.values()]
        ok &= min(c for c in dpow if c is not None) == 2
        # log term l^3 D_x(V log sigma) = l^3 [(D_x V) log sigma + V D_x sigma/sigma]; with D_x V bounded the
        # first part is O(l^3 log l); the second, with V(x0, x0) = V0 computed below on the flat massive field,
        # has power 3 + 1 - 2 = 2 and l^2 coefficient V0 2 D/Q(D) = -m0^2 D/Q(D)
        for m0 in MASSES:
            V0 = flat_log_coefficient(m0)
            logt = [lzmul((weight, [V0] + [F(0)] * (n - 1)), lzmul(lz(1, v[a]), isig)) for a in range(4)]
            if m0:
                ok &= min(t[0] for t in logt) == 2
                ok &= all(lzcoef(logt[a], 2) == -m0 * m0 * D[a] / qf(D) for a in range(4))
            else:
                ok &= V0 == 0
    GA.check("scaling powers at weight 3/2 + 3/2, computed on the generic field: leading 0, mass 1, connection 2, "
             "D_x U 2, log term 2 with the flat coefficient V(x0, x0) = -m0^2/2 computed (l^3 log l beyond)", ok)
    return ok


def check_store_dilation_is_normal_dilation_up_to_a_map_tending_to_the_identity():
    _gauge_premises()
    ok = True
    for TH in (field_plane_wave(), field_generic()):
        gx, dgx = setup(TH)
        Gam0 = christoffel_at0(gx)[0]
        nonzero = False
        ok &= all(xval(Gam0[a][b][c]) == xval(xd(TH[a][c], b))
                  for a in range(4) for b in range(4) for c in range(4))
        for y, _ in PAIRS:
            zero = [F(0)] * 4
            eta, ed, G, Gi = geodesic(gx, dgx, y, zero)
            phi = [{(i, 0, k): c for (i, j, k), c in e.items() if j == 0} for e in ed]   # eta'(0)
            for a in range(4):
                ok &= coef(phi[a], 0) == y[a]
                want = sum(xval(Gam0[a][b][c]) * y[b] * y[c] for b in range(4) for c in range(4)) / 2
                ok &= coef(phi[a], 1) == want
                nonzero |= want != 0
            st = synge_scaled(G, ed)
            gauss = pscal(F(1, 2), padd(*[pscal(S[a], pmul(phi[a], phi[a])) for a in range(4)]))
            ok &= padd(st, pscal(-1, gauss)) == {}
        # the correction is nonzero exactly when the metric has nonzero first derivatives at x0
        ok &= nonzero == any(xval(dgx[r][m][n]) for r in range(4) for m in range(4) for n in range(4))
    GA.check("store dilation versus normal dilation: Phi_l(y) = y + (l/2) Gamma(x0) y y + O(l^2) and the Gauss "
             "lemma sigma(x0, l y) = l^2 Q(Phi_l(y))/2 to the computed order; Gamma(x0)(a, b) = (a . grad hb^{-1})(b)", ok)
    return ok
