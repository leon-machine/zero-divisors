"""dark-matter.two-reductions: exact checks.

Quantities in Q(pi) are Laurent monomials in pi, {power: Fraction}, so pi is never approximated.
  (i)   Wallis factors by two routes (the recursion W_n = (n-1)/n W_{n-2}, W_0 = pi, W_1 = 2, and the
        Fourier expansion of cos^n): W_2 = pi/2, W_4 = 3 pi/8, so G_4 = G_5/(l W_2) = 2 G_5/(pi l) and the
        zero-mode thickness l W_4 = (3 pi/8) l = (V_4/V_3) l, with the unit-ball volumes and sphere areas
        from |S^{n+1}| = |S^n| W_n. In five-dimensional GTG (flat R^(4,1), e0 timelike, e4 the theta
        direction) the field hb^{-1}(e_theta) = l e_theta, hb^{-1}(a) = c hb4^{-1}(a) has
        det(hb^{-1}) = l c^4 det(hb4^{-1}) (outermorphism: the wedge of the five frame vectors), derived
        metric l^2 dtheta^2 + c^2 g_4 in the signature (-,+,+,+,+) of eq:warp (its negative in the store
        sign (+,-,-,-,-), which the curvature computation uses), and its
        scalar contraction of a fixed field strength scales as c^{-2}: the gravitational term carries
        l c^2 and a bulk density l c^4, at the sample values c = cos theta = 3/5, 5/13, 1.
  (ii)  Comoving dust T(a) = rho (a.u) u with unit normal n, in the signature (-,+,+,+,+) of eq:warp
        (u^2 = -1): n.T(n) = 0, trace T = -rho, and the bracket of the induced equations contracted with u gives (2/3)(rho - rho/4) = rho/2, so with
        the G_4 of (i) the local thickness is (pi/4) l.
  (iii) W_3 = 4/3 = |S^4|/|S^3|: sheets at the three-dimensional density carry M_tot when s = (4/3) l.
        Under D: rho_5 l/rho_us = |S^4|/|S^5| = 8/(3 pi), shares f_5D = 1 (i) and 2/3 (ii), f_3D = 1 (iii)
        and 4/3 (sheets one radius apart), and Omega_dark/Omega_b = 1 + 2 f_3D + 2 f_5D gives 5, 13/3,
        17/3 and 5 (5.000, 4.333, 5.667, 5.000); neither thickness is l.
The global four-sphere of (iii) (beyond one flat chart) enters only through its area.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def mono(c, k=0):
    return {k: F(c)} if c else {}


def mmul(*xs):
    out = {0: F(1)}
    for x in xs:
        new = {}
        for k1, c1 in out.items():
            for k2, c2 in x.items():
                new[k1 + k2] = new.get(k1 + k2, F(0)) + c1 * c2
        out = {k: c for k, c in new.items() if c}
    return out


def madd(*xs):
    out = {}
    for x in xs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c}


def minv(x):
    (k, c), = x.items()
    return {-k: 1 / c}


def comb(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def wallis_recursion(n):
    w = [mono(1, 1), mono(2)]
    for m in range(2, n + 1):
        w.append(mmul(mono(F(m - 1, m)), w[m - 2]))
    return w


def wallis_fourier(n):
    """int_{-pi/2}^{pi/2} cos^n: cos^n = 2^-n sum_k C(n,k) cos((n-2k) t); int cos(m t) = pi (m = 0),
    2 sin(m pi/2)/m otherwise."""
    out = {}
    for k in range(n + 1):
        m = abs(n - 2 * k)
        term = mono(1, 1) if m == 0 else mono(F(2 * (0, 1, 0, -1)[m % 4], m))
        out = madd(out, mmul(mono(F(comb(n, k), 2 ** n)), term))
    return out


def spheres(n):
    W = wallis_recursion(n)
    A = [mono(2)]
    for m in range(n):
        A.append(mmul(A[m], W[m]))
    return A


ELL = F(7, 2)
# five-dimensional GTG data: Cl(1,4), e4 the theta direction
S5 = (1, -1, -1, -1, -1)          # the store sign
S5W = (-1, 1, 1, 1, 1)            # the signature of eq:warp
E5 = [GA.gen(i) for i in range(5)]
H4 = [[2, 1, 0, 0], [0, 1, 0, -1], [1, 0, 3, 0], [0, 0, 1, 1]]
CS = (F(3, 5), F(5, 13), F(1))
RFS = {(0, 1): [(0, 1, 2)], (0, 2): [(1, 2, 1), (0, 3, -1)], (0, 3): [(2, 3, 1)],
       (1, 2): [(0, 2, 3)], (1, 3): [(1, 3, -2), (0, 1, 1)], (2, 3): [(0, 3, 1)]}


def frame(c):
    g = []
    for mu in range(4):
        g.append(GA.add(*[GA.scal(F(H4[mu][n]) * c, E5[n]) for n in range(4)]))
    g.append(GA.scal(ELL, E5[4]))
    return g


def wedge_all(vs, sq):
    out = GA.sc(1)
    for k, v in enumerate(vs):
        out = {b: c for b, c in GA.mul(out, v, sq).items() if len(b) == k + 1}
    return out


def reciprocal(g):
    n = len(g)
    G = [[GA.dot(g[i], g[j], S5) for j in range(n)] for i in range(n)]
    out = []
    for i in range(n):
        col = GA.field_solve(G, [F(1) if r == i else F(0) for r in range(n)])
        out.append(GA.add(*[GA.scal(col[j], g[j]) for j in range(n)]))
    return out


def field_strength(mu, nu):
    if mu == nu:
        return {}
    sgn, key = (1, (mu, nu)) if mu < nu else (-1, (nu, mu))
    out = {}
    for (i, j, cf) in RFS[key]:
        out = GA.add(out, GA.scal(sgn * cf, GA.mul(E5[i], E5[j], S5)))
    return out


def scalar_curvature(c):
    """d_a . R(a) over the four physical frame vectors; R(g_mu ^ g_nu) = -R(e_mu ^ e_nu) (hb(g_mu) = e_mu)."""
    g = frame(c)[:4]
    gr = reciprocal(g)
    tot = F(0)
    for mu in range(4):
        for nu in range(4):
            Rb = GA.neg(field_strength(mu, nu))
            v = GA.scal(F(1, 2), GA.sub(GA.mul(gr[mu], Rb, S5), GA.mul(Rb, gr[mu], S5)))
            tot += GA.dot(gr[nu], v, S5)
    return tot


def check_wallis_factors_and_zero_mode_thickness():
    ok = True
    W, Wf = wallis_recursion(6), [wallis_fourier(n) for n in range(7)]
    ok = ok and all(W[n] == Wf[n] for n in range(7))
    ok = ok and W[2] == mono(F(1, 2), 1) and W[4] == mono(F(3, 8), 1) and W[3] == mono(F(4, 3))
    A = spheres(6)
    V = [None] + [mmul(A[n - 1], mono(F(1, n))) for n in range(1, 7)]
    ok = ok and V[4] == mono(F(1, 2), 2) and V[3] == mono(F(4, 3), 1)
    ok = ok and mmul(V[4], minv(V[3])) == W[4]
    G4_over_G5 = minv(mmul(mono(ELL), W[2]))
    ok = ok and G4_over_G5 == mono(2 / ELL, -1)                 # G_4 = 2 G_5/(pi l)
    L_eff = mmul(mono(ELL), W[4])
    ok = ok and L_eff == mono(F(3, 8) * ELL, 1) and L_eff != mono(ELL)
    GA.check("Wallis factors pi/2 and 3pi/8, G_4 = 2G_5/(pi l), zero-mode thickness (V_4/V_3) l", ok)
    assert ok


def check_warped_field_volume_and_curvature_weights():
    ok = True
    det4 = wedge_all([GA.add(*[GA.scal(F(H4[mu][n]), E5[n]) for n in range(4)]) for mu in range(4)], S5)
    d4 = det4.get((0, 1, 2, 3), F(0))
    ok = ok and d4 == 7                                            # det of H4, by hand
    R1 = scalar_curvature(F(1))
    ok = ok and R1 != 0
    for c in CS:
        g = frame(c)
        vol = wedge_all(g, S5).get((0, 1, 2, 3, 4), F(0))
        ok = ok and vol == ELL * c ** 4 * d4
        ok = ok and GA.dot(g[4], g[4], S5) == -ELL ** 2 and GA.dot(g[4], g[4], S5W) == ELL ** 2
        ok = ok and all(GA.dot(g[4], g[mu], S5) == 0 for mu in range(4))
        ok = ok and all(GA.dot(g[mu], g[nu], S5) == c ** 2 * GA.dot(frame(F(1))[mu], frame(F(1))[nu], S5)
                        for mu in range(4) for nu in range(4))
        Rc = scalar_curvature(c)
        ok = ok and Rc * c ** 2 == R1
        ok = ok and vol * Rc == ELL * c ** 2 * d4 * R1                # gravitational weight l c^2
    GA.check("warped GTG field: det(hb^{-1}) = l c^4 det4, curvature scalar ~ c^-2, so weights l c^2 and l c^4", ok)
    assert ok


def check_local_projection_thickness():
    premise("dark-matter.imported-induced-equations-hypersurface")
    rho = F(5, 3)
    u, n = E5[0], E5[4]
    T = lambda a: GA.scal(rho * GA.dot(a, u, S5W), u)
    recip = [GA.scal(F(1, S5W[i]), E5[i]) for i in range(5)]
    trace = sum(GA.dot(recip[i], T(E5[i]), S5W) for i in range(5))
    Tnn = GA.dot(n, T(n), S5W)
    ok = GA.dot(u, u, S5W) == -1 and GA.dot(n, n, S5W) == 1 and Tnn == 0 and trace == -rho
    energy = GA.dot(u, T(u), S5W) + (Tnn - trace / 4) * GA.dot(u, u, S5W)
    ok = ok and energy == F(3, 4) * rho
    bulk = F(2, 3) * energy                                         # times kappa_5^2
    ok = ok and bulk == rho / 2
    # 8 pi G_4 rho_eff = kappa_5^2 rho/2 = 8 pi G_5 rho/2, and G_5/G_4 = l W_2
    L_loc = mmul(mono(bulk / rho), mono(ELL), wallis_recursion(2)[2])
    ok = ok and L_loc == mono(F(1, 4) * ELL, 1)
    GA.check("local projection: (2/3)(rho - rho/4) = rho/2 and thickness (pi/4) l", ok)
    assert ok


def check_sheet_spacing_and_totals_under_democracy():
    premise("dark-matter.d-democracy-total-mass")
    ok = True
    A, W = spheres(6), wallis_recursion(4)
    ok = ok and mmul(A[4], minv(A[3])) == W[3] == mono(F(4, 3))
    s = mmul(mono(ELL), W[3])                                       # the spacing
    ok = ok and s == mono(F(4, 3) * ELL)
    family_over_M = mmul(mono(ELL), W[3], minv(s))                  # (4 l/3)/s
    ok = ok and family_over_M == mono(1)
    ratio = mmul(A[4], minv(A[5]))                                  # rho_5 l/rho_us under D
    ok = ok and ratio == mono(F(8, 3), -1)
    f5_i = mmul(W[4], ratio)
    f5_ii = mmul(mono(F(1, 4), 1), ratio)
    f3_iii, f3_one = mono(1), mmul(mono(ELL), W[3], minv(mono(ELL)))
    ok = ok and f5_i == mono(1) and f5_ii == mono(F(2, 3)) and f3_one == mono(F(4, 3))
    tot = lambda f3, f5: madd(mono(1), mmul(mono(2), f3), mmul(mono(2), f5))
    totals = [tot(f3_iii, f5_i), tot(f3_iii, f5_ii), tot(f3_one, f5_i), tot(f3_one, f5_ii)]
    ok = ok and totals == [mono(5), mono(F(13, 3)), mono(F(17, 3)), mono(5)]
    want = (F(5), F(4333, 1000), F(5667, 1000), F(5))
    ok = ok and (len(totals) == len(want) and all(abs(t[0] - d) < F(1, 2000) for t, d in zip(totals, want)))
    GA.check("sheet spacing (4/3) l and totals 5.000, 4.333, 5.667, 5.000 under D", ok)
    assert ok
