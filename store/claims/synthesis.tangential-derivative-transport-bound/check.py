"""synthesis.tangential-derivative-transport-bound: exact checks.

The continuum bound is proved in the proof text by variation of constants and Gronwall. The check
verifies, in exact rational arithmetic, the discrete (Euler-product) form of the same argument:
transports T_{k+1} = (1 + h G_k) T_k on 4x4 matrices of so(1,3) (boosts B_i, rotations R_ij), a
one-parameter family of tangential curves (model generator -sum_i u^i p_i B_i, the displayed GTG-sign value) differentiated exactly with dual numbers, the discrete
variation-of-constants identities for T - T0 and for D - D0 (D = d/dy T), and the discrete bound
||D_n - D0_n|| <= (1 + h(1 + eps))^n (lam eps_y + eps c2 lam^2) in the max-row-sum norm.
"""
from fractions import Fraction as F
import GA
from GA import gen, mul, add, sub, scal, rank_of_vectors
from tp_premise import premise

# Kasner data with sum p = 1 and sum p^2 = 1: Schwarzschild and the u = 2 point of the Kasner circle
KASNER = [(F(-1, 3), F(2, 3), F(2, 3)), (F(-2, 7), F(3, 7), F(6, 7))]
# Selectors for part(): the value and the y-derivative (dual part) of a dual matrix.
VAL, DER = 0, 1
# Samples for the discrete bound: step h and count n (lam = n h = 1), base offsets y0, field scales.
C1_STEP, C1_STEPS = F(1, 8), 8
C1_Y0S = [F(0), F(1, 2)]
C1_SCALES = [F(1, 50), F(1, 7)]
# Tightness controls with the control field of scale 1/5: a short curve at y0 = 0 (where d_y u^0 = 0)
# and a long curve, 24 steps of 1/2, at y0 = 1/2.
SHORT_STEP, SHORT_STEPS, SHORT_Y0 = F(1, 4), 4, F(0)
LONG_STEP, LONG_STEPS, LONG_Y0 = F(1, 2), 24, F(1, 2)
CONTROL_SCALE = F(1, 5)


def growth_factor(h, n, eps):
    """(1 + h (1 + eps))^n, the discrete form of e^(lam (1 + eps)) with lam = n h; the 1 inside is the
    bound ||H|| <= 1 on the model generator."""
    return (1 + h * (1 + eps)) ** n


class Dn:
    """Dual number a + b e, e^2 = 0, with Fraction parts."""
    def __init__(self, a, b=F(0)):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        o = o if isinstance(o, Dn) else Dn(o)
        return Dn(self.a + o.a, self.b + o.b)
    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Dn) else Dn(o)
        return Dn(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return Dn(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, Dn) else Dn(o)
        return Dn(self.a * o.a, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, Dn) else Dn(o)
        return Dn(self.a / o.a, (self.b * o.a - self.a * o.b) / (o.a * o.a))


def zero4():
    return [[Dn(0) for _ in range(4)] for _ in range(4)]


def eye4():
    return [[Dn(1 if i == j else 0) for j in range(4)] for i in range(4)]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), Dn(0)) for j in range(4)] for i in range(4)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(4)] for i in range(4)]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(4)] for i in range(4)]


def msc(c, A):
    return [[A[i][j] * c for j in range(4)] for i in range(4)]


def part(A, which):
    return [[(A[i][j].a if which == 0 else A[i][j].b) for j in range(4)] for i in range(4)]


def norm(M):
    """max-row-sum norm of a rational matrix (submultiplicative)."""
    return max(sum(abs(x) for x in row) for row in M)


def boost(i):
    M = [[F(0)] * 4 for _ in range(4)]
    M[0][i] = M[i][0] = F(1)
    return M


def rot(i, j):
    M = [[F(0)] * 4 for _ in range(4)]
    M[i][j], M[j][i] = F(-1), F(1)
    return M


def lift(M):
    return [[Dn(x) for x in row] for row in M]


def setup():
    premise("interior.transport-level-convergence-along-tangential-curves")
    premise("interior.weighted-limit-theorem")


def check_generators_and_model_bound():
    setup()
    # the boosts and rotations are the bivectors e0 e_i, e_i e_j of Cl(1,3) acting on vectors:
    # check the matrix action against GA: [B, v] / 2 for B = e0 e1 on v = e1 gives e0
    sq = (1, -1, -1, -1)
    B01 = mul(gen(0), gen(1), sq)
    act = scal(F(1, 2), sub(mul(B01, gen(1), sq), mul(gen(1), B01, sq)))
    assert act == {(0,): F(-1)} or act == {(0,): F(1)}
    # the six generators are independent: so(1,3) has dimension 6
    gens = [boost(1), boost(2), boost(3), rot(1, 2), rot(1, 3), rot(2, 3)]
    assert rank_of_vectors([[x for row in M for x in row] for M in gens]) == 6
    assert all(norm(boost(i)) == 1 for i in (1, 2, 3))
    # Cauchy-Schwarz bound of the model generator on a rational unit direction: ||sum u_i p_i B_i|| <= 1
    units = [(F(3, 5), F(4, 5), F(0)), (F(2, 7), F(3, 7), F(6, 7)), (F(1), F(0), F(0))]
    for p in KASNER:
        assert sum(p) == 1 and sum(x * x for x in p) == 1
        for u in units:
            assert sum(x * x for x in u) == 1
            H = [[sum(-u[i] * p[i] * boost(i + 1)[r][c] for i in range(3)) for c in range(4)] for r in range(4)]
            assert norm(H) <= 1
    return True


def field_main(scale):
    """E(x)[u] = sum_i u^i M_i(x): M_0 = scale x^2 R23, M_1 = scale (x - 1/2) R12, M_2 = 0."""
    R, Rb = rot(2, 3), rot(1, 2)
    def M(x):
        return [mscal(scale * x * x, R), mscal(scale * (x - F(1, 2)), Rb), None]
    def dM(x):
        return [mscal(2 * scale * x, R), mscal(scale, Rb), None]
    return M, dM


def field_control(scale):
    """E(x)[u] = scale u^0 R23: no base-point dependence (a tightness control)."""
    R = rot(2, 3)
    def M(x):
        return [mscal(scale, R), None, None]
    def dM(x):
        return [None, None, None]
    return M, dM


def mscal(c, M):
    return [[c * v for v in row] for row in M]


def run_family(p, y0, h, n, field):
    """Transports along the family gamma_y(s) = x0 + y + s u(y)_0 (a coordinate family: y moves the base
    point in the coordinate x), direction u(y) on the unit circle (rational parametrisation), at
    y = y0 + e (dual). Returns the histories and the separate constants eps, eps1, c1, c2."""
    M, dM = field
    y = Dn(y0, 1)
    u = [(1 - y * y) / (1 + y * y), (2 * y) / (1 + y * y), Dn(0)]
    B = [lift(boost(1)), lift(boost(2)), lift(boost(3))]
    T, T0 = eye4(), eye4()
    Thist, T0hist, Ghist, Hhist = [], [], [], []
    eps = eps1 = c1 = F(0)
    for k in range(n):
        s = h * k
        x = F(1, 3) + y + u[0] * s                       # base coordinate of the curve point (dual)
        H = zero4()
        for i in range(3):
            H = madd(H, msc(u[i] * (-p[i]), B[i]))                # model -sum u^i p_i B_i (GTG sign)
        E = zero4()
        for i, Mi in enumerate(M(x.a)):
            if Mi is not None:
                # M_i evaluated at the dual point: M_i(x) + (x.b) dM_i(x) e
                dMi = dM(x.a)[i]
                Md = [[Dn(Mi[r][c], x.b * (dMi[r][c] if dMi is not None else 0)) for c in range(4)] for r in range(4)]
                E = madd(E, msc(u[i], Md))
        # operator-norm bounds over unit directions: ||sum u^i M_i|| <= sum_i ||M_i|| (|u^i| <= 1)
        eps = max(eps, sum(norm(Mi) for Mi in M(x.a) if Mi is not None))
        eps1 = max(eps1, sum(norm(Mi) for Mi in dM(x.a) if Mi is not None))
        c1 = max(c1, abs(x.b))                           # |d_y gamma| in the coordinate x
        G = madd(H, E)
        Thist.append(T); T0hist.append(T0); Ghist.append(G); Hhist.append(H)
        T = mmul(madd(eye4(), msc(h, G)), T)
        T0 = mmul(madd(eye4(), msc(h, H)), T0)
    Thist.append(T); T0hist.append(T0)
    c2 = 2 / (1 + y0 * y0)                               # Euclidean |d_y u| for the circle parametrisation
    return Thist, T0hist, Ghist, Hhist, eps, eps1, c1, c2


def voc_identity(Th, T0h, Gh, Hh, h, n):
    """Discrete variation of constants: T_n - T0_n = sum_k Phi(n, k+1) h (G_k - H_k) T0_k (values and
    y-derivatives at once, through the dual parts)."""
    one = eye4()
    acc = zero4()
    for k in range(n):
        Phi = one
        for i in range(k + 1, n):
            Phi = mmul(madd(one, msc(h, Gh[i])), Phi)
        acc = madd(acc, mmul(Phi, mmul(msc(h, msub(Gh[k], Hh[k])), T0h[k])))
    diff = msub(Th[n], T0h[n])
    assert part(acc, 0) == part(diff, 0) and part(acc, 1) == part(diff, 1)
    return diff


def check_discrete_c1_bound():
    setup()
    h, n = C1_STEP, C1_STEPS                             # Hubble-normalised length lam = n h = 1
    lam = n * h
    for p in KASNER:
        # the 1 in the growth factor is sharp: the model generator attains norm 1 at u = |p| (unit)
        u_star = [abs(x) for x in p]
        H_star = [[sum(-u_star[i] * p[i] * boost(i + 1)[r][c] for i in range(3)) for c in range(4)] for r in range(4)]
        assert sum(x * x for x in u_star) == 1 and norm(H_star) == 1
        for y0 in C1_Y0S:
            for scale in C1_SCALES:
                Th, T0h, Gh, Hh, eps, eps1, c1, c2 = run_family(p, y0, h, n, field_main(scale))
                diff = voc_identity(Th, T0h, Gh, Hh, h, n)
                X = part(diff, DER)
                delta = max(norm(part(msub(G, H), DER)) for G, H in zip(Gh, Hh))   # ||d_y E|| along the family
                assert max(norm(part(H, DER)) for H in Hh) <= c2                   # ||d_y H|| <= |d_y u|
                assert delta <= eps1 * c1 + eps * c2                              # the chain-rule bound
                # the Gronwall input: every step generator has norm at most 1 + eps
                assert all(norm(part(G, VAL)) <= 1 + eps for G in Gh)
                growth = growth_factor(h, n, eps)
                # the stated bound, in both forms
                assert norm(X) <= growth * (lam * delta + eps * c2 * lam * lam)
                assert norm(X) <= growth * (lam * (eps1 * c1 + eps * c2) + eps * c2 * lam * lam)
                assert norm(part(diff, VAL)) <= lam * eps * growth
                assert eps > 0 and delta > 0 and norm(X) > 0
    return True


def check_bound_terms_needed():
    setup()
    # (1) without the eps c2 lam^2 term the bound fails: a control error with no base-point dependence,
    # at y0 = 0 where d_y u^0 = 0, has delta = 0 but a nonzero derivative of the transport difference
    h, n = SHORT_STEP, SHORT_STEPS
    lam = n * h
    for p in KASNER:
        Th, T0h, Gh, Hh, eps, eps1, c1, c2 = run_family(p, SHORT_Y0, h, n, field_control(CONTROL_SCALE))
        diff = voc_identity(Th, T0h, Gh, Hh, h, n)
        X = part(diff, DER)
        delta = max(norm(part(msub(G, H), DER)) for G, H in zip(Gh, Hh))
        growth = growth_factor(h, n, eps)
        assert delta == 0 and eps1 == 0
        assert norm(X) > growth * lam * delta                                # the lam^2 term is needed
        assert norm(X) <= growth * (lam * delta + eps * c2 * lam * lam)       # and the full bound holds
    # (2) without the growth factor the bound fails over a long curve
    h, n = LONG_STEP, LONG_STEPS
    lam = n * h
    for p in KASNER[:1]:
        Th, T0h, Gh, Hh, eps, eps1, c1, c2 = run_family(p, LONG_Y0, h, n, field_control(CONTROL_SCALE))
        diff = voc_identity(Th, T0h, Gh, Hh, h, n)
        X = part(diff, DER)
        delta = max(norm(part(msub(G, H), DER)) for G, H in zip(Gh, Hh))
        growth = growth_factor(h, n, eps)
        assert norm(X) > lam * delta + eps * c2 * lam * lam                  # the growth factor is needed
        assert norm(X) <= growth * (lam * delta + eps * c2 * lam * lam)
    return True
