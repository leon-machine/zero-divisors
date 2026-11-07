"""synthesis.promoted-norm-weyl-clock-flat-weight: exact checks.

Curvature tensors are 4x4x4x4 arrays of Fractions in an orthonormal frame. The Levi-Civita
symbol is read off the Clifford product of the four frame vectors (GA), so that
Q(F) = (1/4) eps_{abcd} eps^{efgh} F_{abef} F_{cdgh} is the density of
eps_{abcd} F^{ab} ^ F^{cd} against the volume form. Volumes are carried as rational multiples
of pi^2, and actions as rational multiples of pi N^2 = pi l^2 / G, so every comparison is exact.
"""
from fractions import Fraction as F
from itertools import permutations, product
import GA
from GA import mul, gen, sc
from tp_premise import premise

R4 = range(4)


def eps_table(squares):
    """eps[a][b][c][d]: coefficient of e0e1e2e3 in e_a e_b e_c e_d for distinct indices."""
    t = {}
    for p in permutations(R4):
        x = sc(1)
        for i in p:
            x = mul(x, gen(i), squares)
        t[p] = x.get((0, 1, 2, 3), F(0))
    return t


EPS = eps_table((1, 1, 1, 1))


def zero():
    return [[[[F(0)] * 4 for _ in R4] for _ in R4] for _ in R4]


def kn(h, k):
    """Kulkarni-Nomizu product of two symmetric 4x4 matrices."""
    T = zero()
    for a, b, c, d in product(R4, R4, R4, R4):
        T[a][b][c][d] = (h[a][c] * k[b][d] + h[b][d] * k[a][c]
                         - h[a][d] * k[b][c] - h[b][c] * k[a][d])
    return T


def ident():
    return [[F(1) if i == j else F(0) for j in R4] for i in R4]


def lin(*terms):
    T = zero()
    for c, X in terms:
        for a, b, cc, d in product(R4, R4, R4, R4):
            T[a][b][cc][d] += F(c) * X[a][b][cc][d]
    return T


D = lin((F(1, 2), kn(ident(), ident())))        # unit constant curvature: d_ac d_bd - d_ad d_bc


def ricci(T):
    return [[sum(T[c][a][c][b] for c in R4) for b in R4] for a in R4]


def scalar(T):
    return sum(ricci(T)[a][a] for a in R4)


def weyl(T):
    """W = Riem - (1/2) Ric o g + (R/12) g o g  (n = 4)."""
    return lin((1, T), (F(-1, 2), kn(ricci(T), ident())), (scalar(T) / 12, kn(ident(), ident())))


def norm2(T):
    return sum(T[a][b][c][d] ** 2 for a, b, c, d in product(R4, R4, R4, R4))


def Q(X, Y=None):
    """(1/4) eps_{abcd} eps_{efgh} X_{abef} Y_{cdgh}, Euclidean."""
    Y = X if Y is None else Y
    s = F(0)
    for (a, b, c, d), e1 in EPS.items():
        if e1 == 0:
            continue
        for (e, f, g, h), e2 in EPS.items():
            if e2 == 0 or X[a][b][e][f] == 0 or Y[c][d][g][h] == 0:
                continue
            s += e1 * e2 * X[a][b][e][f] * Y[c][d][g][h]
    return s / 4


def euler(T):
    Ric = ricci(T)
    return scalar(T) ** 2 - 4 * sum(Ric[a][b] ** 2 for a in R4 for b in R4) + norm2(T)


def s4(l2):
    return lin((F(1) / l2, D))


def s2s2(a2):
    """Product of two round 2-spheres of radius^2 a2 on frame pairs (0,1), (2,3)."""
    T = zero()
    for (i, j) in ((0, 1), (2, 3)):
        k = F(1) / a2
        T[i][j][i][j] = k
        T[j][i][j][i] = k
        T[i][j][j][i] = -k
        T[j][i][i][j] = -k
    return T


def cp2():
    """Fubini-Study, holomorphic sectional curvature 4 (Ric = 6 g), J e0 = e1, J e2 = e3."""
    J = [[F(0)] * 4 for _ in R4]
    J[1][0], J[0][1], J[3][2], J[2][3] = F(1), F(-1), F(1), F(-1)     # J[i][a]: component i of J e_a
    g = ident()

    def gJ(x, y):            # g(e_x, J e_y)
        return J[x][y]
    T = zero()
    for a, b, c, d in product(R4, R4, R4, R4):
        T[a][b][c][d] = (g[a][c] * g[b][d] - g[a][d] * g[b][c]
                         + gJ(a, c) * gJ(b, d) - gJ(a, d) * gJ(b, c)
                         + 2 * gJ(a, b) * gJ(c, d))
    return T


def is_algebraic_curvature(T):
    for a, b, c, d in product(R4, R4, R4, R4):
        if T[a][b][c][d] != -T[b][a][c][d] or T[a][b][c][d] != T[c][d][a][b]:
            return False
        if T[a][b][c][d] + T[a][c][d][b] + T[a][d][b][c] != 0:
            return False
    return True


# instantons: (name, Riemann, Lambda, volume / pi^2, Euler characteristic)
def instantons():
    return [("S4", s4(F(1)), F(3), F(8, 3), 2),
            ("S2xS2", s2s2(F(1)), F(1), F(16), 4),
            ("CP2", cp2(), F(6), F(1, 2), 3)]


def check_normalisation():
    """The store's MM expansion l^2 RR + 2 eeR + l^-2 eeee, with Q(R - s D) = E - 4 s R + 24 s^2,
    matched to -(1/16 pi G) int R, gives the cosmological term with Lambda = 3/l^2 exactly."""
    premise("synthesis.imported-chern-gauss-bonnet")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    assert Q(D) == 24
    for name, T, lam, vol, chi in instantons():
        assert is_algebraic_curvature(T)
        s = F(5, 7)                                  # arbitrary rational l^-2
        F_ = lin((1, T), (-s, D))
        assert Q(F_) == euler(T) - 4 * s * scalar(T) + 24 * s * s
        assert Q(T, D) == 2 * scalar(T)
    # k(-4) int R = -(1/16 pi G) int R  =>  k = 1/(64 pi G); then k * 24 l^-2 = 2 Lambda/(16 pi G)
    k_times_G = F(1, 64)                             # in units of 1/pi
    assert -4 * k_times_G == F(-1, 16)
    for l2 in (F(1), F(3), F(2, 5)):
        lam = 24 * k_times_G / l2 * 16 / 2
        assert lam == 3 / l2


def check_gauss_bonnet_cross():
    """chi = (1/32 pi^2) int E for the three instantons, from the tensors and volumes used."""
    premise("synthesis.imported-chern-gauss-bonnet")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    for name, T, lam, vol, chi in instantons():
        Ric = ricci(T)
        assert all(Ric[a][b] == (lam if a == b else 0) for a in R4 for b in R4), name
        assert vol * euler(T) / 32 == chi, name


def generic_weyl():
    h1 = [[F(1), F(2), F(0), F(-1)], [F(2), F(-3), F(1), F(0)],
          [F(0), F(1), F(2), F(5)], [F(-1), F(0), F(5), F(1)]]
    h2 = [[F(2), F(-1), F(3), F(0)], [F(-1), F(1), F(0), F(2)],
          [F(3), F(0), F(-2), F(1)], [F(0), F(2), F(1), F(4)]]
    R = lin((1, kn(h1, h1)), (F(1, 3), kn(h1, h2)), (-2, kn(h2, h2)))
    return weyl(R)


def check_pointwise_einstein_identity():
    """For every Einstein curvature R = W + (Lambda/3) D with l^2 = 3/Lambda:
    F = R - l^-2 D = W, Q(F) = |W|^2 / 1 (the volume terms cancel), and tr F = 0, so the
    on-shell l^2-derivative does not depend on whether the frame or the unit frame is held."""
    premise("synthesis.imported-chern-gauss-bonnet")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.under-action-written-norm-parameter-laws")
    W = generic_weyl()
    assert is_algebraic_curvature(W) and norm2(W) != 0
    assert all(x == 0 for row in ricci(W) for x in row)
    for lam in (F(3), F(1, 2), F(-6)):
        R = lin((1, W), (lam / 3, D))
        l2inv = lam / 3
        Fc = lin((1, R), (-l2inv, D))
        assert Q(Fc) == Q(W)
        assert scalar(Fc) == 0
    # Q(W) = (1/4) delta W W = R^2 - 4|Ric|^2 + |Riem|^2 evaluated on W, i.e. |W|^2 (full sum)
    assert Q(W) == norm2(W)


def check_instanton_actions():
    """I_MM / (pi N^2) = vol * Q(F) / 64 = I_EH/(pi N^2) + chi/2 = vol * |W|^2 / 64 >= 0."""
    premise("synthesis.imported-chern-gauss-bonnet")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.de-sitter-entropy-pi-n-squared")
    expect = {"S4": (F(0), F(-1)), "S2xS2": (F(4, 3), F(-2, 3)), "CP2": (F(3, 4), F(-3, 4))}
    for name, T, lam, vol, chi in instantons():
        l2inv = lam / 3
        Fc = lin((1, T), (-l2inv, D))
        i_mm = vol * Q(Fc) / 64
        i_eh = -lam * lam * vol / 24
        assert i_mm == i_eh + F(chi, 2), name
        assert i_mm == vol * norm2(weyl(T)) / 64, name
        assert (i_mm, i_eh) == expect[name], name
        assert i_mm >= 0


def non_einstein_curvature(W):
    """A curvature tensor that is not Einstein: Weyl part W plus a constant-curvature part plus a
    trace-free Ricci part built from a rank-two symmetric matrix."""
    h = [[F(1), F(1), F(0), F(0)], [F(1), F(0), F(0), F(0)],
         [F(0), F(0), F(0), F(0)], [F(0), F(0), F(0), F(0)]]
    return lin((1, W), (F(2, 3), D), (F(1, 5), kn(h, ident())))


def check_conjugate_time_density():
    """d/d(l^2) of l^2 Q(R - l^-2 D) at fixed R equals Q(F) + 4 l^-2 tr F (polynomial identity in
    s = l^-2, checked as a finite difference in exact arithmetic); on a vacuum solution tr F = 0
    and F = W, so the density conjugate to l^2 is Q(W) there, and holding the unit frame instead
    adds a multiple of tr F (with matter, see check_matter_density_frame_independent)."""
    premise("synthesis.imported-chern-gauss-bonnet")
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    premise("dark-energy.under-action-written-norm-parameter-laws")
    W = generic_weyl()
    R = non_einstein_curvature(W)
    # S(u) = u * Q(R - D/u) with u = l^2 is u E - 4 R + 24/u; dS/du = E - 24/u^2
    E, Rs = Q(R), scalar(R)
    assert Rs != 0 and ricci(R) != [[F(0)] * 4 for _ in R4]

    def S(u):
        return u * Q(lin((1, R), (-1 / u, D)))
    u1, u2 = F(3), F(7, 2)
    for u in (u1, u2):
        assert S(u) == u * E - 4 * Rs + 24 / u
    # exact secant of S: (S(u2) - S(u1)) / (u2 - u1) = E - 24 / (u1 u2), the derivative's secant form
    assert (S(u2) - S(u1)) / (u2 - u1) == E - 24 / (u1 * u2)
    for u in (u1, u2):
        Fc = lin((1, R), (-1 / u, D))
        dS = E - 24 / (u * u)
        assert dS == Q(Fc) + 4 / u * scalar(Fc)
        assert scalar(Fc) == Rs - 12 / u
    # on an Einstein tensor with matching l^2 the extra term vanishes
    Re = lin((1, W), (F(1), D))
    Fe = lin((1, Re), (-1, D))
    assert scalar(Fe) == 0 and Q(Fe) == norm2(W)


def lorentz_weyl_zero_flrw(a, ad, add, k):
    """FLRW in an orthonormal frame, metric diag(-1,1,1,1): R_{0i0j} = -(add/a) d_ij,
    R_{ijkl} = ((ad^2 + k)/a^2)(d_ik d_jl - d_il d_jk). Returns the Weyl tensor (all indices down)."""
    eta = [[F(-1) if i == j == 0 else (F(1) if i == j else F(0)) for j in R4] for i in R4]
    T = zero()
    A = -add / a
    B = (ad * ad + k) / (a * a)
    for i, j in product(range(1, 4), range(1, 4)):
        if i == j:
            T[0][i][0][j] = A
            T[i][0][j][0] = A
            T[0][i][j][0] = -A
            T[i][0][0][j] = -A
    for i, j, kk, l in product(range(1, 4), repeat=4):
        T[i][j][kk][l] = B * ((1 if i == kk and j == l else 0) - (1 if i == l and j == kk else 0))
    # raise one index pair with eta to form Ricci with signs
    Ric = [[sum(eta[c][c] * T[c][a_][c][b] for c in R4) for b in R4] for a_ in R4]
    Rs = sum(eta[a_][a_] * Ric[a_][a_] for a_ in R4)
    W = lin((1, T), (F(-1, 2), kn(Ric, eta)), (Rs / 12, kn(eta, eta)))
    return W, Rs


def check_clock_frozen_conformally_flat_and_kasner():
    """Vacuum clause (iv): the vacuum density k|W|^2 vanishes wherever W = 0 (the FLRW curvature
    form has W = 0 identically; with matter the density is not k|W|^2, see the matter checks)
    and near a Kasner wall equals the Kretschmann density, 64/(27 tau^4) times sqrt|g| = tau for
    (2/3, 2/3, -1/3)."""
    premise("synthesis.imported-chern-gauss-bonnet")
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    premise("dark-energy.frozen-point-datum-kasner-wall")
    for (a, ad, add, k) in ((F(2), F(3), F(5), 1), (F(1, 3), F(1), F(7), 0), (F(5), F(-2), F(1), -1)):
        W, Rs = lorentz_weyl_zero_flrw(a, ad, add, k)
        assert all(x == 0 for x in (W[i][j][kk][l] for i, j, kk, l in product(R4, R4, R4, R4)))
        assert Rs != 0
    p = (F(2, 3), F(2, 3), F(-1, 3))
    assert sum(p) == 1 and sum(x * x for x in p) == 1
    kret = 4 * sum((x * (x - 1)) ** 2 for x in p) + 4 * sum(
        (p[i] * p[j]) ** 2 for i in range(3) for j in range(3) if i < j)
    assert kret == F(64, 27)


# ---------------------------------------------------------------------------
# clause (v): matter. Lorentzian, metric diag(-1, 1, 1, 1), orthonormal frame, units 8 pi G = 1,
# so k = 1/(64 pi G) = 1/8. Curvature convention: de Sitter of radius l has R = l^-2 D_L with
# D_L = (1/2) KN(eta, eta), so Ric = Lambda g there and s = 4 Lambda (u = l^2 = 3/Lambda).
# ---------------------------------------------------------------------------

ETA = [F(-1), F(1), F(1), F(1)]
ETAM = [[ETA[i] if i == j else F(0) for j in R4] for i in R4]
K8 = F(1, 8)                                     # k in units 8 pi G = 1


def ric_L(T):
    return [[sum(ETA[c] * T[c][a][c][b] for c in R4) for b in R4] for a in R4]


def s_L(T):
    Ric = ric_L(T)
    return sum(ETA[a] * Ric[a][a] for a in R4)


def n2_L4(T):
    return sum(ETA[a] * ETA[b] * ETA[c] * ETA[d] * T[a][b][c][d] ** 2
               for a, b, c, d in product(R4, R4, R4, R4))


def n2_L2(M):
    return sum(ETA[a] * ETA[b] * M[a][b] ** 2 for a in R4 for b in R4)


def euler_L(T):
    return s_L(T) ** 2 - 4 * n2_L2(ric_L(T)) + n2_L4(T)


def weyl_L(T):
    return lin((1, T), (F(-1, 2), kn(ric_L(T), ETAM)), (s_L(T) / 12, kn(ETAM, ETAM)))


def traceless(M):
    t = sum(ETA[a] * M[a][a] for a in R4)
    return [[M[a][b] - t / 4 * ETAM[a][b] for b in R4] for a in R4], t


def flrw_L(h, q):
    """Flat FLRW in the comoving orthonormal frame: R_{0i0j} = -q d_ij, R_{ijkl} = h D_ijkl,
    h = H^2, q = addot/a."""
    T = zero()
    for i in range(1, 4):
        T[0][i][0][i] = -q
        T[i][0][i][0] = -q
        T[0][i][i][0] = q
        T[i][0][0][i] = q
    for i, j, kk, l in product(range(1, 4), repeat=4):
        T[i][j][kk][l] = h * ((1 if (i == kk and j == l) else 0) - (1 if (i == l and j == kk) else 0))
    return T


def friedmann(lam, rho, p):
    """h = (Lambda + rho)/3, q = Lambda/3 - (rho + 3p)/6 (8 pi G = 1); verified from the tensor below."""
    return (lam + rho) / 3, lam / 3 - (rho + 3 * p) / 6


def fluid_stress(rho, p):
    return [[(rho if a == b == 0 else (p if a == b else F(0))) for b in R4] for a in R4]


def einstein_holds(T, lam, Tm):
    Ric, s = ric_L(T), s_L(T)
    return all(Ric[a][b] - s / 2 * ETAM[a][b] + lam * ETAM[a][b] == Tm[a][b] for a in R4 for b in R4)


def matter_density_poly(lam, rho, p):
    return F(4, 3) * (lam * (rho - 3 * p) - rho * (rho + 3 * p))


GRID = (F(1, 2), F(3), F(-2))


def check_matter_flrw_density():
    """(v) on flat FLRW with a perfect fluid: E - 24/u^2 = (4/3)[Lambda(rho - 3p) - rho(rho + 3p)]
    from the curvature tensor, with Einstein's equations verified from the same tensor; the identity
    is of degree two in each of (Lambda, rho, p) and is checked on a 3x3x3 grid, which proves it.
    Radiation gives -(8/3) rho^2; dust gives (4/3) rho (Lambda - rho), zero only at rho = Lambda."""
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    premise("synthesis.imported-chern-gauss-bonnet")
    for lam, rho, p in product(GRID, GRID, GRID):
        h, q = friedmann(lam, rho, p)
        T = flrw_L(h, q)
        assert is_algebraic_curvature(T)
        assert einstein_holds(T, lam, fluid_stress(rho, p))
        assert euler_L(T) == 24 * h * q
        if lam != 0:
            u = 3 / lam
            assert euler_L(T) - 24 / (u * u) == matter_density_poly(lam, rho, p)
    for lam in (F(3), F(1, 5)):
        for rho in (F(1), F(7, 2)):
            assert matter_density_poly(lam, rho, rho / 3) == F(-8, 3) * rho * rho != 0
        assert matter_density_poly(lam, lam, F(0)) == 0
        assert matter_density_poly(lam, lam / 2, F(0)) > 0 > matter_density_poly(lam, 2 * lam, F(0))
        assert matter_density_poly(lam, F(0), F(0)) == 0                  # de Sitter: stands still


def check_matter_density_frame_independent():
    """(iii)/(v): at fixed frame the density is -k(E - 24/u^2) sqrt|g| (Lorentzian action
    -k(uE - 4s + 24/u) + L_m); holding the unit frame (g = u g_hat) gives -k Q(F) from gravity and
    t/(2u) from matter (T^ab = (2/sqrt|g|) d(sqrt|g| L_m)/d g_ab); they agree on shell because
    s(F) = s - 12/u = -t, the trace of Einstein's equations, with the matter term included."""
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    premise("dark-energy.under-action-written-norm-parameter-laws")
    for lam, rho, p, want in ((F(3), F(2), F(0), F(-1, 3)), (F(1, 2), F(7), F(7, 3), F(49, 3)),
                              (F(3), F(2), F(-1, 5), F(-5, 6))):
        h, q = friedmann(lam, rho, p)
        T = flrw_L(h, q)
        u = 3 / lam
        t = -rho + 3 * p
        E, s = euler_L(T), s_L(T)
        QF = E - 4 * s / u + 24 / (u * u)
        fixed_frame = -K8 * (E - 24 / (u * u))
        unit_frame = -K8 * QF + t / (2 * u)
        assert s - 12 / u == -t
        assert fixed_frame == unit_frame == want
        assert (-K8 * QF != fixed_frame) == (t != 0)   # gravity alone misses the matter trace


def lorentz_generic_curvature():
    h1 = [[F(1), F(2), F(0), F(-1)], [F(2), F(-3), F(1), F(0)],
          [F(0), F(1), F(2), F(5)], [F(-1), F(0), F(5), F(1)]]
    h2 = [[F(2), F(-1), F(3), F(0)], [F(-1), F(1), F(0), F(2)],
          [F(3), F(0), F(-2), F(1)], [F(0), F(2), F(1), F(4)]]
    return lin((1, kn(h1, h1)), (F(1, 3), kn(h1, h2)), (-2, kn(h2, h2)), (F(1, 2), kn(h1, ETAM)))


def check_lorentzian_decomposition_with_source():
    """(v) general form: E = |W|^2 - 2|Ric_tf|^2 + s^2/6 (Lorentzian norms) on a generic algebraic
    curvature tensor; with T := Ric - (s/2) g + Lambda g (Einstein's equations, 8 pi G = 1),
    E - (8/3) Lambda^2 = |W|^2 - 2|T_tf|^2 - (4/3) Lambda t + t^2/6, and the first-order term of the
    density conjugate to Lambda, (3k/Lambda^2)(E - 8 Lambda^2/3), is -t/(2 Lambda)."""
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    premise("synthesis.imported-chern-gauss-bonnet")
    R = lorentz_generic_curvature()
    assert is_algebraic_curvature(R)
    W = weyl_L(R)
    assert n2_L4(W) != 0
    Ric, s = ric_L(R), s_L(R)
    Rtf, _ = traceless(Ric)
    assert euler_L(R) == n2_L4(W) - 2 * n2_L2(Rtf) + s * s / 6
    for lam in (F(3), F(-1, 2), F(5, 7)):
        Tm = [[Ric[a][b] - s / 2 * ETAM[a][b] + lam * ETAM[a][b] for b in R4] for a in R4]
        Ttf, t = traceless(Tm)
        assert s == 4 * lam - t
        lhs = euler_L(R) - F(8, 3) * lam * lam
        assert lhs == n2_L4(W) - 2 * n2_L2(Ttf) - F(4, 3) * lam * t + t * t / 6
        first_order = 3 * K8 / (lam * lam) * (-F(4, 3) * lam * t)
        assert first_order == -t / (2 * lam)


if __name__ == "__main__":
    for fn in (check_normalisation, check_gauss_bonnet_cross, check_pointwise_einstein_identity,
               check_instanton_actions, check_conjugate_time_density,
               check_clock_frozen_conformally_flat_and_kasner, check_matter_flrw_density,
               check_matter_density_frame_independent, check_lorentzian_decomposition_with_source):
        fn()
        print("PASS", fn.__name__)


# ---- GTG derivation (maintainer pass 2026-11-07, GTG proofs) ----
# The instantons as gauge fields on the flat Euclidean background Cl(4,0) (lib/gtg.py, sq = (1,1,1,1)), with the
# rotation-gauge field SOLVED from the torsion equation and the store curvature calR(B) = -R(hb(B)) of its field
# strength: the round S^4 and S^2 x S^2 in stereographic gauges, CP^2 (Fubini-Study) in the cohomogeneity-one
# gauge f^0 = dr/(1 + r^2), f^{1,2} = r sigma_{1,2}/(2 sqrt(1 + r^2)), f^3 = r sigma_3/(2(1 + r^2)) at
# psi = 0, theta = pi/2. The GA density Q(X, Y) = 2 <X(a ^ b) I^{-1} Y(I d_b ^ d_a)> is eps_abcd X^ab ^ Y^cd / vol.
import gtg  # noqa: E402

E4 = (1, 1, 1, 1)


def q_ga(X, Y, sq):
    """Q(X, Y) = 2 <X(a ^ b) I^{-1} Y(I d_b ^ d_a)> for curvature operators given as frame-plane dicts."""
    I = gtg.pseudoscalar(sq)
    Ii = GA.scal(1 / gtg.sp(GA.mul(I, I, sq)), I)
    tot = F(0)
    for a in R4:
        for b in R4:
            if a != b:
                Xab = gtg.apply_op(X, gtg.wedge(gen(a), gen(b), sq))
                Yb = gtg.apply_op(Y, GA.mul(I, gtg.wedge(gtg.er(b, sq), gtg.er(a, sq), sq), sq))
                tot += gtg.sp(GA.mul(GA.mul(Xab, Ii, sq), Yb, sq))
    return 2 * tot


def euclid_var(i, x0):
    return gtg.J.var(i, x0, 4, 2)


def gauge_s4(x0):
    X = [euclid_var(i, x0[i]) for i in R4]
    phi = 2 / (1 + X[0] * X[0] + X[1] * X[1] + X[2] * X[2] + X[3] * X[3])
    z = gtg.J.const(0)
    return gtg.Field([[phi if a == m else z for m in R4] for a in R4], sq=E4)


def gauge_s2s2(x0):
    X = [euclid_var(i, x0[i]) for i in R4]
    p, q = 2 / (1 + X[0] * X[0] + X[1] * X[1]), 2 / (1 + X[2] * X[2] + X[3] * X[3])
    z, d = gtg.J.const(0), [p, p, q, q]
    return gtg.Field([[d[a] if a == m else z for m in R4] for a in R4], sq=E4)


def gauge_cp2(r0, root):
    r, z = euclid_var(0, r0), gtg.J.const(0)
    sps, cps = gtg.sincos(1, F(0), F(1), 4, 2)
    sth, cth = gtg.sincos(2, F(1), F(0), 4, 2)
    w = 1 + r * r
    A, C = r / (2 * w.pw(F(1, 2), root)), r / (2 * w)
    TH = [[1 / w, z, z, z], [z, z, A * sps, -(A * cps * sth)], [z, z, A * cps, A * sps * sth], [z, C, z, C * cth]]
    return gtg.Field(TH, sq=E4)


def frame_trivector(Fop, a, sq):
    """The MacDowell-Mansouri frame equation as a trivector: 2 d_b ^ F(I(a ^ b)) (eps_abcd e^b ^ F^cd)."""
    I = gtg.pseudoscalar(sq)
    out = {}
    for b in R4:
        out = gtg.m_add(out, gtg.outer(gtg.er(b, sq), gtg.apply_op(Fop, GA.mul(I, gtg.wedge(a, gen(b), sq), sq)), sq))
    return gtg.m_scal(2, out)


INSTANTON_LAMBDAS = (F(3), F(1), F(6))   # S^4, S^2 x S^2, CP^2 in these normalisations: calR(a) = -Lambda a


def check_gtg_instantons_as_euclidean_gauge_fields():
    premise("synthesis.imported-chern-gauss-bonnet")
    premise("synthesis.imported-gtg-dictionary")      # store-sign field strength, Weyl duality (row 5)
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.de-sitter-entropy-pi-n-squared")
    ok = True
    D = gtg.op_planes(gtg.op_const(-1), E4)          # the unit sphere's operator in the store sign on (4,0)
    out = []
    for fld, chi in ((gauge_s4([F(1, 2), F(0), F(1, 3), F(0)]), 2), (gauge_s2s2([F(1, 2), F(1, 3), F(0), F(2)]), 4),
                     (gauge_cp2(F(3, 4), F(5, 4)), 3)):
        ok = ok and fld.torsion_free()
        Rc = fld.curvature()
        lam = -gtg.ricci(Rc, gen(0), E4).get((0,), F(0))   # Einstein: calR(a) = -Lambda a on (4,0)
        ok = ok and lam == INSTANTON_LAMBDAS[len(out)]      # the store sign: positive Lambda gives calR(a) = -Lambda a
        ok = ok and all(GA.eq(gtg.ricci(Rc, gen(c), E4), GA.scal(-lam, gen(c))) for c in R4)
        Fop = gtg.op_planes(gtg.op_add(Rc, gtg.op_const(lam / 3)), E4)    # F = calR - (Lambda/3) D
        if not out:                                          # the unit S^4: calR(B) = -B = D(B) on every plane
            ok = ok and all(GA.eq(Rc[pl], D[pl]) for pl in D)
        I = gtg.pseudoscalar(E4)
        for c in R4:                                         # frame equation 2(G(a) - Lambda a) I = 0 on (4,0)
            a = gen(c)
            T = frame_trivector(Fop, a, E4)
            ok = ok and GA.eq(T, GA.scal(2, GA.mul(gtg.m_sub(gtg.einstein(Rc, a, E4), GA.scal(lam, a)), I, E4)))
            ok = ok and GA.is_zero(T) and not GA.is_zero(gtg.m_add(gtg.einstein(Rc, a, E4), GA.scal(lam, a)))
        W = gtg.weyl_op(Rc, E4)
        W2, E = gtg.kretschmann(W, E4), gtg.euler_density(Rc, E4)
        ok = ok and q_ga(Fop, Fop, E4) == W2 and q_ga(Rc, Rc, E4) == E and E == W2 + F(8, 3) * lam * lam
        ok = ok and q_ga(Rc, D, E4) == -2 * gtg.ricci_scalar(Rc, E4)
        out.append((chi * W2 / (2 * E), -4 * chi * lam * lam / (3 * E)))
    ok = ok and q_ga(D, D, E4) == 24
    ok = ok and out == [(F(0), F(-1)), (F(4, 3), F(-2, 3)), (F(3, 4), F(-3, 4))]
    assert ok
    return ok


def check_gtg_kasner_and_flrw_densities_from_gauge_fields():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    ok = True
    for tau in (F(1), F(2), F(1, 3)):
        p = [F(2, 3), F(2, 3), F(-1, 3)]
        # a_i = tau^{p_i} with the spatial labels rescaled so that a_i = 1 at the instant: adot/a = p/tau
        fld = gtg.synchronous_from_data([(F(1), p[i] / tau, p[i] * (p[i] - 1) / tau ** 2) for i in range(3)])
        Rc = fld.curvature()
        ok = ok and gtg.ricci_flat(Rc) and gtg.kretschmann(gtg.weyl_op(Rc)) == F(64, 27) / tau ** 4
    # (Lambda, rho~, p~, H) with H^2 = (Lambda + rho~)/3
    for lam, rho, prs, H in ((F(1, 2), F(1, 4), F(0), F(1, 2)), (F(1, 2), F(1, 4), F(1, 12), F(1, 2)),
                             (F(3), F(0), F(2), F(1)), (F(2), F(1), F(-1, 3), F(1)), (F(-1), F(4), F(1, 3), F(1))):
        h = (lam + rho) / 3
        ok = ok and H * H == h
        q = lam / 3 - (rho + 3 * prs) / 6
        fld = gtg.flrw_flat(F(1), H, q)
        Rc = fld.curvature()
        for c in R4:
            a = gen(c)
            Tt = GA.sub(GA.scal((rho + prs) * GA.dot(a, gen(0), gtg.S13), gen(0)), GA.scal(prs, a))
            ok = ok and GA.eq(gtg.einstein_residual(Rc, a, lam), GA.neg(Tt))
        ok = ok and gtg.weyl_op(Rc) == {k: {} for k in gtg.weyl_op(Rc)}
        E = gtg.euler_density(Rc)
        ok = ok and E == 24 * h * q and q_ga(Rc, Rc, gtg.S13) == E
        ok = ok and E - F(8, 3) * lam * lam == F(4, 3) * (lam * (rho - 3 * prs) - rho * (rho + 3 * prs))
    assert ok
    return ok
