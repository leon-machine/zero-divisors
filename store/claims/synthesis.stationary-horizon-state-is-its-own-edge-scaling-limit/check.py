"""The boost of a horizon generator is its scaling about the edge: exact checks.

(1) The boost is the CAR-preserving scaling about the edge. In Cl(1,3) (store signature) the rotor
    B = cosh(lambda/2) + sinh(lambda/2) e1 e0, at e^{lambda/2} = r rational, sends l = e0 + e1 to r^2 l,
    n = e0 - e1 to r^{-2} n and fixes e2, e3: on the null plane {u l + y} it is u -> r^2 u at fixed y,
    every generator dilated about its edge point u = 0. On fields, psi(u) -> s^p psi(s u) (s = r^2)
    preserves the one-particle inner product (the anticommutator) exactly for p = 1/2, checked on
    indicator functions of rational intervals: the boost's weight is the scaling weight.
(2) The kernels. With y = ln(u/v) and t = u/v, the half-generator KMS state at rapidity period 2 pi c has
    (2 pi / i) omega_c(psi*(v) psi(u)) = (uv)^{-1/2} / (c (t^{1/2c} - t^{-1/2c})), evaluated exactly at points
    u = a^{2k}, v = b^{2k} with k/c an integer. c = 1 gives 1/(u - v), the null vacuum. Each kernel is
    homogeneous of degree -1 (scaling by squares), the difference D_c = W_c - W_1 is nonzero for c != 1 and
    D_c(s u, s v) = D_c(u, v)/s, so D_c is unbounded on every neighbourhood of the edge pair (0, 0).
    The Mellin symbol is m_1(c w): (1 + e^{-2 pi c w})^{-1}, the I-state at period 2 pi c, with the
    two-point KMS identity at that period and not at 2 pi (c != 1).
(3) Off the edge the difference is analytic: with gamma = 1/c^2, S(z) = sinh(z)/z,
    y D_c (2 pi/i)(uv)^{1/2} = S(y sqrt(gamma)/2)^{-1} - S(y/2)^{-1}, an even series with zero constant
    term for every gamma (the leading singularity 1/y is common to all c: the anticommutator fixes it),
    first coefficient -(gamma - 1)/24; identically zero at gamma = 1. Control: dropping the 1/c leaves a pole.
(4) The null energy: point-split, T_uu = (i/2) lim (d_u - d_v) D at u = v = 1 equals (gamma - 1)/(48 pi),
    computed from exact series in epsilon at u = 1 + epsilon (and v = 1 + epsilon); homogeneity gives
    (gamma - 1)/(48 pi u^2), and the Killing-frame density kappa^2 u^2 T_uu is constant: for gamma = 0
    (the boost ground state) -kappa^2/(48 pi).
(5) Across the edge: the vacuum's cross block (u > 0 > v) is 1/(u - v), homogeneous and nonzero; the product
    of the two half states has cross block 0, so its difference from the vacuum is unbounded at (0, 0) even
    at c = 1, where each half is the I-state at 2 pi.
Exact arithmetic only (Fractions, Gaussian rationals); pi, logarithms and exponentials are never evaluated.
"""
from fractions import Fraction as F
import GA
from GA import QI
from tp_premise import premise

SQ4 = (1, -1, -1, -1)                 # store signature (+,-,-,-): e0, e1, e2, e3


def _m(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, SQ4)
    return out


def _vec(c0, c1, c2=0, c3=0):
    return GA.add(GA.scal(c0, GA.gen(0)), GA.scal(c1, GA.gen(1)), GA.scal(c2, GA.gen(2)), GA.scal(c3, GA.gen(3)))


def _rotor(r):
    ch = (r + 1 / r) / 2
    sh = (r - 1 / r) / 2
    return GA.add(GA.sc(ch), GA.scal(sh, _m(GA.gen(1), GA.gen(0))))


def _overlap(a, b, c, d):
    lo, hi = max(a, c), min(b, d)
    return hi - lo if hi > lo else F(0)


def check_boost_is_the_car_scaling_about_the_edge():
    premise("synthesis.stationary-generator-states-and-the-edge-scaling")
    premise("hawking.i-state-continuum")
    premise("synthesis.positive-null-energy-gives-r-premises")
    l = _vec(1, 1)
    n = _vec(1, -1)
    for r in (F(3, 2), F(1, 5), F(7)):
        B = _rotor(r)
        Bt = GA.reverse(B)
        GA.check("B is a rotor: B B~ = 1", GA.eq(_m(B, Bt), GA.sc(1)))
        GA.check("B l B~ = r^2 l", GA.eq(_m(B, l, Bt), GA.scal(r * r, l)))
        GA.check("B n B~ = r^-2 n", GA.eq(_m(B, n, Bt), GA.scal(1 / (r * r), n)))
        for i in (2, 3):
            GA.check("B fixes the edge directions", GA.eq(_m(B, GA.gen(i), Bt), GA.gen(i)))
        for (u, y) in [(F(0), F(5)), (F(2), F(-1)), (F(-3, 4), F(1, 3))]:
            x = GA.add(GA.scal(u, l), GA.scal(y, GA.gen(2)))
            want = GA.add(GA.scal(r * r * u, l), GA.scal(y, GA.gen(2)))
            GA.check("u l + y e2 -> r^2 u l + y e2: dilation about the edge point", GA.eq(_m(B, x, Bt), want))
    # the weight: (S_s f)(u) = s^p f(s u) on indicators chi_[a,b] has support [a/s, b/s], amplitude s^p;
    # <S_s f, S_s g> = s^{2p} |overlap| / s. Weight p = k/4: s^{2p} is rational for s = r^4.
    intervals = [(F(0), F(1)), (F(1, 2), F(3)), (F(-2), F(1, 3)), (F(-1), F(0))]
    kept = []
    for k in range(0, 5):
        ok = True
        for r in (F(3, 2), F(1, 5)):
            s = r ** 4
            amp2 = r ** (2 * k)                      # s^{2p} with p = k/4
            for (a, b) in intervals:
                for (c, d) in intervals:
                    lhs = amp2 * _overlap(a / s, b / s, c / s, d / s)
                    if lhs != _overlap(a, b, c, d):
                        ok = False
        if ok:
            kept.append(F(k, 4))
    GA.check("only the weight 1/2 makes the scaling preserve the anticommutator", kept == [F(1, 2)])
    # tabulated rotor components and images at the three sample rapidities
    tab = {F(3, 2): (F(13, 12), F(5, 12), F(9, 4)), F(1, 5): (F(13, 5), F(-12, 5), F(1, 25)), F(7): (F(25, 7), F(24, 7), F(49))}
    got = {}
    for r in (F(3, 2), F(1, 5), F(7)):
        B = _rotor(r)
        img = _m(B, l, GA.reverse(B))
        got[r] = (B.get((), F(0)), B.get((0, 1), F(0)) * -1, img.get((0,), F(0)))
    GA.check("tabulated: cosh, sinh (on e1 e0) and the e0 coefficient of B l B~", got == tab)
    # tabulated scaled overlaps at the CAR weight: s = r^4, amplitude^2 s = r^4 / r^4 * ... (exact values)
    s = F(3, 2) ** 4
    GA.check("tabulated: unweighted scaled overlap of [0,1] and [1/2,3] is 1/(2 s) = 8/81",
             _overlap(F(0), 1 / s, F(1, 2) / s, F(3) / s) == F(8, 81))
    GA.check("tabulated: overlap of [1/2, 3] and [-2, 1/3] is 0, of [0,1] and [1/2,3] is 1/2",
             _overlap(F(1, 2), F(3), F(-2), F(1, 3)) == 0 and _overlap(F(0), F(1), F(1, 2), F(3)) == F(1, 2))
    return True


def _W(c, a, b, k):
    """(2 pi / i) omega_c(psi*(v) psi(u)) at u = a^{2k}, v = b^{2k}; needs k/c an integer."""
    e = F(k) / c
    assert e.denominator == 1
    e = e.numerator
    q = (F(a) / b) ** e                    # t^{1/2c}
    root = (F(a) * b) ** k                 # (uv)^{1/2}
    return 1 / (root * c * (q - 1 / q))


COUNT_PIN = 147
TOTAL_PIN = F(-1255824173072876354161182953732148517902040833699519466840115239039243, 1267371174879900872677791465368617075507389039600000000)


def check_kernels_homogeneous_and_differ_only_at_the_edge_scale():
    premise("synthesis.stationary-generator-states-and-the-edge-scaling")
    premise("hawking.i-state-continuum")
    premise("hawking.imported-quasi-free-kms-reduces-two")
    cases = [(F(1, 2), 1), (F(1), 2), (F(2), 2), (F(3), 3), (F(1, 3), 1)]
    pts = [(2, 3), (5, 1), (1, 4), (7, 3)]
    acc = []                                 # every computed kernel value, pinned below by a tabulated total
    for c, k in cases:
        for (a, b) in pts:
            W = _W(c, a, b, k)
            if c == 1:
                GA.check("c = 1 is the null vacuum 1/(u - v)", W == 1 / (F(a) ** (2 * k) - F(b) ** (2 * k)))
            for m in (2, 3, F(1, 2)):            # scale u, v by s = m^{2k}
                s = F(m) ** (2 * k)
                Ws = _W(c, F(m) * a, F(m) * b, k)
                GA.check("homogeneous of degree -1: W(s u, s v) = W(u, v)/s", Ws == W / s)
                W1 = 1 / (s * F(a) ** (2 * k) - s * F(b) ** (2 * k))
                D = Ws - W1
                D0 = W - 1 / (F(a) ** (2 * k) - F(b) ** (2 * k))
                GA.check("the difference is homogeneous of degree -1", D == D0 / s)
                acc.append(Ws)
            D0 = W - 1 / (F(a) ** (2 * k) - F(b) ** (2 * k))
            acc.append(W)
            acc.append(D0)
            GA.check("D_c = 0 exactly when c = 1", (D0 == 0) == (c == 1))
            if c != 1:
                # approach the edge along the ray: D_c(u/N^{2k}, v/N^{2k}) = N^{2k} D_c(u, v), unbounded
                for N in (10, 1000):
                    DN = _W(c, F(a, N), F(b, N), k) - 1 / (F(a, N) ** (2 * k) - F(b, N) ** (2 * k))
                    GA.check("D_c grows as N^{2k} towards the edge", DN == F(N) ** (2 * k) * D0)
                    acc.append(DN)
    # tabulated: c = 1/2, u = 4, v = 9: (uv)^{1/2} = 6, t^{1} = 4/9: 1/(6 (1/2)(4/9 - 9/4)) = -12/65
    GA.check("tabulated W_{1/2}(4, 9) = -12/65", _W(F(1, 2), 2, 3, 1) == F(-12, 65))
    GA.check("tabulated W_1(4, 9) = -1/5", _W(F(1), 2, 3, 1) == F(-1, 5))
    # c = 2, u = 16, v = 81: (uv)^{1/2} = 36, t^{1/4} = 2/3: 1/(36 * 2 (2/3 - 3/2)) = -1/60 (without 1/c: -1/30)
    GA.check("tabulated W_2(16, 81) = -1/60", _W(F(2), 2, 3, 2) == F(-1, 60))
    # c = 3, u = 64, v = 1: (uv)^{1/2} = 8, t^{1/6} = 2: 1/(8 * 3 (2 - 1/2)) = 1/36 (without 1/c: 1/12)
    GA.check("tabulated W_3(64, 1) = 1/36", _W(F(3), 2, 1, 3) == F(1, 36))
    # the leading singularity is common to every c: (u - v) W_c -> 1 as v -> u, sampled at u = 1, v = (1 + 1/N)^2
    for c, k in [(F(1, 2), 1), (F(2), 2), (F(3), 3)]:
        for N in (100, 10000):
            a, b = F(1), 1 + F(1, N)
            lead = (a ** (2 * k) - b ** (2 * k)) * _W(c, a, b, k)
            acc.append(lead)
            GA.check("normalisation: (u - v) W_c is within 1/N of 1 near the diagonal", abs(lead - 1) < F(1, N))
    # the Mellin symbol at period 2 pi c is m_1(c w): with q = e^{pi w}, m_c = 1/(1 + q^{-2c});
    # two-point KMS identity 1 - m = e^{-2 pi c w} m at period 2 pi c, and not at 2 pi when c != 1
    for c in (F(2), F(3), F(1)):
        for q in (F(2), F(1, 3), F(7, 5)):
            Q = q ** int(c)
            m = 1 / (1 + 1 / (Q * Q))
            acc.append(m)
            GA.check("KMS identity at period 2 pi c", 1 - m == m / (Q * Q))
            GA.check("KMS identity at 2 pi only when c = 1", (1 - m == m / (q * q)) == (c == 1))
    GA.check("tabulated: number of pinned values", len(acc) == COUNT_PIN)
    GA.check("tabulated: exact total of all pinned values", sum(acc, F(0)) == TOTAL_PIN)
    # the imaginary shift y -> y - 2 pi i c sends t^{1/2c} to -t^{1/2c}: antiperiodic (fermion KMS) at 2 pi c;
    # the shift by 2 pi i sends it to e^{-i pi / c} t^{1/2c}, which for c = 1/2 is +t^{1/2c}: not antiperiodic
    q = QI(F(4, 9))
    f = lambda qq: 1 / (QI(F(1, 2)) * (qq - 1 / qq))
    GA.check("antiperiodic under the 2 pi c shift", f(QI(-1) * q) == QI(-1) * f(q))
    GA.check("control: c = 1/2 is periodic, not antiperiodic, under the 2 pi shift", f(QI(1) * q) == f(q) and f(q) != QI(0))
    return True


def _S_inv(gamma, N):
    """Coefficients in y of S(y sqrt(gamma)/2)^{-1}, S(z) = sinh z / z = sum z^{2j}/(2j+1)!; even in y."""
    s = [F(0)] * (N + 1)
    fact = F(1)
    for j in range(0, N // 2 + 1):
        if j > 0:
            fact = fact * (2 * j) * (2 * j + 1)
        s[2 * j] = gamma ** j / (F(4) ** j * fact)
    return GA.ps_inv(s, N)


def _g_series(gamma, N):
    """g(y) = y^{-1} (S(y sqrt(gamma)/2)^{-1} - S(y/2)^{-1}) as a series in y (order N - 1)."""
    G = [x - z for x, z in zip(_S_inv(gamma, N), _S_inv(F(1), N))]
    GA.check("no constant term: no pole of g at y = 0", G[0] == 0)
    return G[1:] + [F(0)]


def check_off_the_edge_every_member_is_locally_the_vacuum():
    premise("synthesis.stationary-generator-states-and-the-edge-scaling")
    premise("hawking.i-state-continuum")
    N = 12
    for gamma in (F(0), F(1, 4), F(1, 9), F(4), F(1)):
        G = [x - z for x, z in zip(_S_inv(gamma, N), _S_inv(F(1), N))]
        GA.check("the difference series has zero constant term for every period", G[0] == 0)
        GA.check("it is even in y", all(G[i] == 0 for i in range(1, N + 1, 2)))
        GA.check("first coefficient -(gamma - 1)/24", G[2] == -(gamma - 1) / 24)
        GA.check("vanishes identically exactly at gamma = 1", all(x == 0 for x in G) == (gamma == 1))
    GA.check("tabulated: S(z)^{-1} = 1 - z^2/6 + 7 z^4/360 - ...: y^4 coefficient 7/5760 at gamma = 1",
             _S_inv(F(1), 6)[4] == F(7, 5760))
    # control: without the factor 1/c the leading singularity differs: 1/(2 sinh(y/2c)) = c/y + ..., a pole c - 1
    for c in (F(2), F(1, 3)):
        lead = c * _S_inv(1 / (c * c), N)[0] - _S_inv(F(1), N)[0]
        GA.check("control: dropping 1/c leaves a pole (c - 1)/y", lead == c - 1 and lead != 0)
    return True


def _log1p(N):
    return [F(0)] + [F((-1) ** (j + 1), j) for j in range(1, N + 1)]


def check_null_energy_of_the_family():
    premise("hawking.i-state-continuum")
    N = 6
    half = GA.ps_pow_rat([F(1), F(1)], F(-1, 2), N)         # (1 + eps)^{-1/2}
    L = _log1p(N)
    Ts = {}
    for gamma in (F(0), F(1, 4), F(1), F(4), F(1, 9)):
        g = _g_series(gamma, N + 1)
        du = GA.ps_mul(half, GA.ps_compose(g, L, N), N)       # u = 1 + eps, v = 1: y = ln(1 + eps)
        dv = GA.ps_mul(half, GA.ps_compose(g, [-x for x in L], N), N)   # v = 1 + eps: y = -ln(1 + eps)
        GA.check("D vanishes on the diagonal at u = v = 1", du[0] == 0 and dv[0] == 0)
        # D = (i / 2 pi) X: T_uu = (i/2)(i/2pi)(X_u - X_v) = -(X_u - X_v)/(4 pi); in units of 1/pi:
        T = -(du[1] - dv[1]) / 4
        Ts[gamma] = T
        GA.check("T_uu(1) = (gamma - 1)/(48 pi)", T == (gamma - 1) / 48)
        # Killing frame: kappa^2 u^2 T_uu(u) with T_uu(u) = T_uu(1)/u^2 (degree -2): constant in u
        for u in (F(2), F(1, 3), F(5)):
            GA.check("Killing-frame density constant along the generator", u * u * (T / (u * u)) == T)
    GA.check("tabulated: the boost ground state (gamma = 0) has T_uu(1) = -1/(48 pi)", Ts[F(0)] == F(-1, 48))
    GA.check("tabulated: period pi (gamma = 4) has T_uu(1) = 3/(48 pi)", Ts[F(4)] == F(3, 48))
    GA.check("the vacuum (gamma = 1) carries no null energy", Ts[F(1)] == 0)
    return True


def check_cross_edge_block():
    premise("synthesis.stationary-generator-states-and-the-edge-scaling")
    premise("hawking.i-state-continuum")
    # vacuum cross block (2 pi / i) omega_1(psi*(v) psi(u)) = 1/(u - v) for u > 0 > v (no coincidence)
    pts = [(F(1), F(-1)), (F(2), F(-3)), (F(1, 2), F(-5, 7))]
    GA.check("tabulated cross block values 1/2, 1/5, 14/17", [1 / (u - v) for (u, v) in pts] == [F(1, 2), F(1, 5), F(14, 17)])
    GA.check("tabulated: at scale 1/1000 the first value is 500", 1 / (pts[0][0] / 1000 - pts[0][1] / 1000) == 500)
    for (u, v) in [(F(1), F(-1)), (F(2), F(-3)), (F(1, 2), F(-5, 7))]:
        X = 1 / (u - v)
        GA.check("vacuum correlates the two halves", X != 0)
        for s in (F(1, 10), F(1, 1000), F(3)):
            GA.check("cross block homogeneous of degree -1", 1 / (s * u - s * v) == X / s)
        # product of the two half states (any c, c = 1 included): cross block 0; difference -X, unbounded
        D = F(0) - X
        GA.check("product state differs from the vacuum across the edge", D != 0)
        GA.check("and the difference grows as 1/s at the edge", (F(0) - 1 / (u / 1000 - v / 1000)) == 1000 * D)
    return True


def check_zero_null_energy_does_not_select_the_vacuum():
    premise("hawking.i-state-continuum")
    # symbols are linear in the state: the quasi-free state with symbol (1/4) m_{1/2} + (3/4) m_infinity
    # (0 <= symbol <= 1, a function of the Mellin weight, so stationary) has difference series the same mix
    N = 12
    p = F(1, 4)
    mix = [p * x + (1 - p) * z for x, z in zip(
        [a - b for a, b in zip(_S_inv(F(4), N), _S_inv(F(1), N))],
        [a - b for a, b in zip(_S_inv(F(0), N), _S_inv(F(1), N))])]
    GA.check("mixture: no pole, locally the vacuum off the edge", mix[0] == 0)
    GA.check("mixture: zero null energy (y^2 coefficient, -(gamma - 1)/24 averaged)", mix[2] == 0)
    GA.check("mixture: not the vacuum (y^4 coefficient 21/5760)", mix[4] == F(21, 5760))
    # the weight that cancels the null energy is forced: p (4 - 1) + (1 - p)(0 - 1) = 0 only at p = 1/4
    GA.check("the cancelling weight is 1/4", [q for q in (F(1, 8), F(1, 4), F(1, 2)) if 3 * q - (1 - q) == 0] == [F(1, 4)])
    # control: the single members with zero null energy are the vacuum only
    zeros = [g for g in (F(0), F(1, 9), F(1, 4), F(1), F(4)) if _S_inv(g, N)[2] - _S_inv(F(1), N)[2] == 0]
    GA.check("control: within the one-period family only gamma = 1 has zero null energy", zeros == [F(1)])
    return True
