"""synthesis.euler-term-horizon-entropy-shift: exact checks.

(i) The MacDowell-Mansouri square, expanded with F = R - s l^{-2} e^e (s = +1 de Sitter, -1 anti-de Sitter,
the sign that makes F vanish on the model), equals -4 s (R - 2 Lambda + alpha E_4) with alpha = -3/(4 Lambda), on
every test curvature tensor (constant curvature, a product of two two-spheres, a generic pair-curvature
tensor), in Lorentzian and Euclidean signature; the Levi-Civita symbol is read off from GA products of
generators. (ii) In two dimensions, for Omega(1 + e psi) with psi a bump vanishing to second order on the
boundary of the square, sqrt(h) R = -Lap ln Omega is verified from the Christoffel symbols as an identity of
rational functions in (x, y, e), and the integral of Lap psi over the square is zero, so the first variation of
the Euler part of the Jacobson-Myers functional vanishes. (iii) Euclidean actions of S^4 and S^2 x S^2 from the
curvature, against horizon sums, in units pi/(Lambda G); the nucleation exponents -1 and -4; the bound
r_b < 1/sqrt(Lambda) for Schwarzschild-de Sitter black-hole horizons.
"""
from fractions import Fraction as F
from itertools import permutations, product
import GA
from tp_premise import premise


def levi(squares):
    top = GA.gen(0)
    for k in range(1, 4):
        top = GA.mul(top, GA.gen(k), squares)
    eps = {}
    for p in permutations(range(4)):
        x = GA.gen(p[0])
        for k in p[1:]:
            x = GA.mul(x, GA.gen(k), squares)
        eps[p] = x[(0, 1, 2, 3)] / top[(0, 1, 2, 3)]
    return eps


def pair_tensor(K):
    """Mixed tensor R^{ab}_{cd} with R^{ab}_{ab} = K[(a, b)] (diagonal curvature operator)."""
    R = {}
    for (a, b), k in K.items():
        if k:
            R[(a, b, a, b)] = k
            R[(b, a, b, a)] = k
            R[(a, b, b, a)] = -k
            R[(b, a, a, b)] = -k
    return R


def g(R, i):
    return R.get(i, F(0))


def scalar_and_euler(R):
    Ric = {(a, c): sum(g(R, (a, b, c, b)) for b in range(4)) for a in range(4) for c in range(4)}
    Rs = sum(Ric[(a, a)] for a in range(4))
    riem2 = sum(g(R, (a, b, c, d)) * g(R, (c, d, a, b)) for a, b, c, d in product(range(4), repeat=4))
    ric2 = sum(Ric[(a, c)] * Ric[(c, a)] for a in range(4) for c in range(4))
    return Rs, Rs * Rs - 4 * ric2 + riem2


def eps_pair(eps, A, B):
    """epsilon_{abcd} A^{ab} wedge B^{cd} per unit volume, A, B bivector-valued two-forms."""
    s = F(0)
    for (a, b, c, d), e1 in eps.items():
        for (e, f, h, k), e2 in eps.items():
            x = g(A, (a, b, e, f))
            if x:
                y = g(B, (c, d, h, k))
                if y:
                    s += e1 * e2 * x * y
    return s / 4


def combo(c1, A, c2, B):
    out = {}
    for k in set(A) | set(B):
        v = c1 * g(A, k) + c2 * g(B, k)
        if v:
            out[k] = v
    return out


# ---- trivariate polynomials (x, y, e) and unreduced rational functions, for the 2D check
def padd(a, b, s=1):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, F(0)) + s * v
        if o[k] == 0:
            del o[k]
    return o


def pmul(a, b):
    o = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])
            o[k] = o.get(k, F(0)) + v1 * v2
    return {k: v for k, v in o.items() if v != 0}


def pd(a, i):
    o = {}
    for k, v in a.items():
        if k[i]:
            kk = list(k)
            kk[i] -= 1
            o[tuple(kk)] = o.get(tuple(kk), F(0)) + v * k[i]
    return {k: v for k, v in o.items() if v != 0}


def pc(c):
    return {(0, 0, 0): F(c)} if c else {}


def radd(r, s, sg=1):
    return (padd(pmul(r[0], s[1]), pmul(s[0], r[1]), sg), pmul(r[1], s[1]))


def rmul(r, s):
    return (pmul(r[0], s[0]), pmul(r[1], s[1]))


def rd(r, i):
    return (padd(pmul(pd(r[0], i), r[1]), pmul(r[0], pd(r[1], i)), -1), pmul(r[1], r[1]))


def req(r, s):
    return padd(pmul(r[0], s[1]), pmul(s[0], r[1]), -1) == {}


def sqrt_h_R(Om):
    """sqrt(h) times the scalar curvature of Om (dx^2 + dy^2), from the Christoffel symbols."""
    dO = [pd(Om, 0), pd(Om, 1)]

    def Gam(k, i, j):
        n = {}
        if k == i:
            n = padd(n, dO[j])
        if k == j:
            n = padd(n, dO[i])
        if i == j:
            n = padd(n, dO[k], -1)
        return (n, pmul(pc(2), Om))
    r = radd(rd(Gam(0, 1, 1), 0), rd(Gam(0, 1, 0), 1), -1)
    for m in range(2):
        r = radd(r, rmul(Gam(0, 0, m), Gam(m, 1, 1)))
        r = radd(r, rmul(Gam(0, 1, m), Gam(m, 1, 0)), -1)
    return rmul((pc(2), pc(1)), r)        # sqrt(h) * 2K = 2 R^x_{yxy}


def square_integral(p):
    s = F(0)
    for (i, j, k), v in p.items():
        if k == 0 and i % 2 == 0 and j % 2 == 0:
            s += v * F(2, i + 1) * F(2, j + 1)
    return s


def check_euler_shift():
    premise("synthesis.imported-wald-noether-charge-entropy")
    premise("synthesis.imported-chern-gauss-bonnet")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("synthesis.imported-gibbons-hawking-entropy")
    premise("synthesis.de-sitter-entropy-pi-n-squared")
    premise("dark-energy.wall-counterterm")
    # (i) the coefficient of the Euler density, both signatures, both branches
    ee = pair_tensor({(a, b): F(1) for a in range(4) for b in range(a + 1, 4)})
    for squares in ((-1, 1, 1, 1), (1, 1, 1, 1)):
        eps = levi(squares)
        assert eps_pair(eps, ee, ee) == 24
        for l2 in (F(1), F(3), F(7, 2)):
            for s in (1, -1):
                Lam = s * 3 / l2
                alpha = -3 / (4 * Lam)
                model = {(a, b): s / l2 for a in range(4) for b in range(a + 1, 4)}
                tests = [model,
                         {(0, 1): F(2), (2, 3): F(5), (0, 2): F(-1), (1, 3): F(1, 3), (1, 2): F(7)},
                         {(0, 1): 3 * s / l2, (2, 3): 3 * s / l2}]
                for K in tests:
                    R = pair_tensor(K)
                    Fc = combo(F(1), R, -s / l2, ee)
                    Rs, E4 = scalar_and_euler(R)
                    assert l2 * eps_pair(eps, Fc, Fc) == -4 * s * (Rs - 2 * Lam + alpha * E4)
                # the square vanishes on the model, and that alone fixes alpha
                Rs, E4 = scalar_and_euler(pair_tensor(model))
                assert Rs - 2 * Lam == -alpha * E4 and Rs - 2 * Lam != 0
    # (ii) two dimensions: sqrt(h) R = -Lap ln Omega on Omega (1 + e psi), and int Lap psi = 0
    X, Y, E = {(1, 0, 0): F(1)}, {(0, 1, 0): F(1)}, {(0, 0, 1): F(1)}
    Om = padd(padd(pc(1), pmul(X, X)), pmul(pc(2), pmul(Y, Y)))
    bx = padd(pc(1), pmul(X, X), -1)
    by = padd(pc(1), pmul(Y, Y), -1)
    psi = pmul(pmul(bx, bx), pmul(by, by))
    Ome = pmul(Om, padd(pc(1), pmul(E, psi)))
    lap = padd(pd(pd(Ome, 0), 0), pd(pd(Ome, 1), 1))
    grad2 = padd(pmul(pd(Ome, 0), pd(Ome, 0)), pmul(pd(Ome, 1), pd(Ome, 1)))
    assert req(sqrt_h_R(Ome), (padd(pmul(Ome, lap), grad2, -1), pmul(pc(-1), pmul(Ome, Ome))))
    lap_psi = padd(pd(pd(psi, 0), 0), pd(pd(psi, 1), 1))
    assert square_integral(lap_psi) == 0 and square_integral(psi) == F(256, 225)
    # scope: a deformation whose gradient does not vanish at the edge leaves an edge flux
    psi1 = pmul(bx, by)
    lap1 = padd(pd(pd(psi1, 0), 0), pd(pd(psi1, 1), 1))
    assert square_integral(lap1) == F(-32, 3)
    # psi and its gradient vanish on the edges x = +-1, y = +-1
    for i in (0, 1):
        dpsi = pd(psi, i)
        for edge in (1, -1):
            for q in (psi, dpsi):
                ev = {}
                for (a, b, c), v in q.items():
                    key = (b, c) if i == 0 else (a, c)
                    ev[key] = ev.get(key, F(0)) + v * F(edge) ** (a if i == 0 else b)
                assert all(v == 0 for v in ev.values())
    # (iii) values in units pi/(Lambda G); Lambda = 1 without loss (everything scales as 1/Lambda)
    Lam = F(1)
    alpha = -3 / (4 * Lam)
    shift = 2 * alpha * 2 / 1          # 2 pi alpha chi / G with chi = 2, in units pi/G
    # de Sitter: radius^2 = 3/Lambda, A/4G = pi * 3/Lambda / G
    S_dS_EH = 3 / Lam
    assert S_dS_EH + shift == 0
    # Nariai: two horizons of area 4 pi / Lambda
    S_N_EH = 2 * (1 / Lam)
    S_N_MM = S_N_EH + 2 * shift
    assert (S_N_EH, S_N_MM) == (2, -4)
    # Euclidean actions from the curvature: I = -(1/16 pi G) int (R - 2 Lambda + alpha E4); unit pi/(Lambda G)
    # S^4 of radius^2 = 3/Lambda: vol = (8/3) pi^2 r^4; S^2 x S^2 of radius^2 = 1/Lambda: vol = 16 pi^2 r^4
    l2 = 3 / Lam
    Rs, E4 = scalar_and_euler(pair_tensor({(a, b): 1 / l2 for a in range(4) for b in range(a + 1, 4)}))
    vol = F(8, 3) * l2 * l2                       # in units pi^2
    assert E4 * vol == 32 * 2                     # Gauss-Bonnet: int E4 = 32 pi^2 chi, chi(S^4) = 2
    I_EH_S4 = -(Rs - 2 * Lam) * vol / 16          # pi^2 / (16 pi G) = pi/(16 G)
    I_GB_S4 = -alpha * E4 * vol / 16
    a2 = 1 / Lam
    Rn, E4n = scalar_and_euler(pair_tensor({(0, 1): 1 / a2, (2, 3): 1 / a2}))
    voln = 16 * a2 * a2
    assert Rn == 4 * Lam and E4n * voln == 32 * 4  # chi(S^2 x S^2) = 4
    I_EH_N = -(Rn - 2 * Lam) * voln / 16
    I_GB_N = -alpha * E4n * voln / 16
    assert (I_EH_S4, I_GB_S4, I_EH_N, I_GB_N) == (-3, 3, -2, 6)
    assert I_EH_S4 == -S_dS_EH and I_EH_S4 + I_GB_S4 == -(S_dS_EH + shift)
    assert I_EH_N == -S_N_EH and I_EH_N + I_GB_N == -S_N_MM
    # nucleation exponents S_N - S_dS: Einstein-Hilbert -1, series' action -4, ratio 4
    assert S_N_EH - S_dS_EH == -1 and S_N_MM - (S_dS_EH + shift) == -4
    # anti-de Sitter branch: the shift is positive
    assert 2 * (-3 / (4 * F(-1))) * 2 > 0
    # SdS: h(r) = r f(r) = r - 2M - Lambda r^3/3 increases on (0, 1/sqrt(Lambda)) (h' = 1 - Lambda r^2),
    # h(0) = -2M < 0, so the smaller root r_b lies below 1/sqrt(Lambda): A_b/4G < pi/(Lambda G), and
    # S_MM(r_b) < 1 + shift = -2 in units pi/(Lambda G)
    for M in (F(1, 10), F(1, 6), F(19, 100)):     # 27 M^2 Lambda < 1 for two horizons
        h = lambda r: r - 2 * M - Lam * r ** 3 / 3
        assert h(F(0)) < 0 and 27 * M * M * Lam < 1 and h(F(1)) > 0
        lo, hi = F(0), F(1)
        for _ in range(40):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if h(mid) < 0 else (lo, mid)
        assert hi < 1 and hi * hi + shift < -2 + F(1, 10)
    assert 1 + shift == -2
    return True
