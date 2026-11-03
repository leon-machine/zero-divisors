"""interior.transport-level-convergence-along-tangential-curves: exact checks of the algebraic core.

The Gronwall inequalities themselves are analytic (norm estimates of solutions of linear equations) and are not
checked; the two identities and the bound the proof rests on are. Generators act on physical vectors of Cl(1,3)
through v -> B . v, as 4 x 4 rational matrices in the frame gamma_a; norms are Euclidean operator norms in that frame.
(1) Variation of constants: for time-dependent generators G(s) = G0 + s G1, H(s) = H0 + s H1 built from sample
    bivectors (boosts, rotations, a null rotation), the solutions T' = G T, T0' = H T0, T(0) = T0(0) = 1 and the
    inverse S = T^{-1} (S' = -S G) are computed as exact power series in lambda to order 7, S T = 1, and
    T(lambda) - T0(lambda) = T(lambda) int_0^lambda S(s) (G(s) - H(s)) T0(s) ds holds coefficient by coefficient.
(2) The model generator: H = sum_i u^i p_i B_i on a unit direction u (B_i = gamma_0 ^ gamma_i) has
    X = H^T H with X (X - |w|^2) = 0, w = (u^i p_i), so ||H||^2 = |w|^2; and |w|^2 <= (sum |u^i||p_i|)^2 <= 1 for
    rational unit directions u and rational points p of the Kasner circle (sum p = sum p^2 = 1), with
    sum |u^i||p_i| = 1 at u = |p|; ||B_i|| = 1 (B_i^T B_i is a nonzero projector).
"""
from fractions import Fraction as F

import GA

S13 = GA.sig(1, 3)
NORD = 7
BIVS = {"B1": (0, 1), "B2": (0, 2), "B3": (0, 3), "R12": (1, 2), "R23": (2, 3)}
UNITS = [(F(1), F(0), F(0)), (F(3, 5), F(4, 5), F(0)), (F(0), F(3, 5), F(-4, 5)), (F(2, 7), F(3, 7), F(6, 7)),
         (F(1, 3), F(2, 3), F(2, 3)), (F(-1, 3), F(2, 3), F(-2, 3))]
KASNER_U = [F(1), F(2), F(1, 2), F(-3)]


def act(B):
    """Matrix of v -> B . v = (Bv - vB)/2 on the frame gamma_0..gamma_3."""
    cols = []
    for j in range(4):
        v = GA.scal(F(1, 2), GA.sub(GA.mul(B, GA.gen(j), S13), GA.mul(GA.gen(j), B, S13)))
        cols.append([v.get((i,), F(0)) for i in range(4)])
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def blade(name, c=1):
    return {BIVS[name]: F(c)}


def madd(A, B, c=1):
    return [[a + c * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mz():
    return [[F(0)] * 4 for _ in range(4)]


def meye():
    return [[F(1 if i == j else 0) for j in range(4)] for i in range(4)]


def solve_left(G0, G1, N):
    """T' = (G0 + s G1) T, T(0) = 1: coefficients T_k."""
    T = [meye()]
    for k in range(N):
        nxt = GA.mat_mul(G0, T[k])
        if k >= 1:
            nxt = madd(nxt, GA.mat_mul(G1, T[k - 1]))
        T.append([[x / (k + 1) for x in r] for r in nxt])
    return T


def solve_inverse(G0, G1, N):
    """S' = -S (G0 + s G1), S(0) = 1."""
    S = [meye()]
    for k in range(N):
        nxt = GA.mat_mul(S[k], G0)
        if k >= 1:
            nxt = madd(nxt, GA.mat_mul(S[k - 1], G1))
        S.append([[-x / (k + 1) for x in r] for r in nxt])
    return S


def smul(A, B, N):
    out = [mz() for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1 - i):
            out[i + j] = madd(out[i + j], GA.mat_mul(A[i], B[j]))
    return out


# Sample generator data (G0, G1, H0, H1): boosts, rotations and a null rotation, with H1 = 0 in the first case.
VOC_CASES = [(blade("B3", F(2, 3)), blade("R23", F(1, 2)), blade("B3", F(2, 3)), {}),
             (GA.add(blade("B1", -1), blade("R12", 2)), blade("B2", 3), blade("B1", -1), blade("B1", F(1, 4))),
             (GA.add(blade("B2"), blade("R12")), blade("R23", -1), blade("B3", F(1, 3)), blade("B2", 2))]


def check_variation_of_constants_identity():
    ok = True
    N = NORD
    for g0, g1, h0, h1 in VOC_CASES:
        G0, G1, H0, H1 = act(g0), act(g1), act(h0), act(h1)
        T = solve_left(G0, G1, N)
        T0 = solve_left(H0, H1, N)
        S = solve_inverse(G0, G1, N)
        ST = smul(S, T, N)
        ok = ok and all(ST[k] == (meye() if k == 0 else mz()) for k in range(N + 1))
        E = [madd(G0, H0, -1), madd(G1, H1, -1)] + [mz()] * (N - 1)
        integrand = smul(smul(S, E, N), T0, N)
        # int_0^lambda s^k ds = lambda^(k+1)/(k+1); orders above N are dropped
        integral = [mz()] + [[[x / (k + 1) for x in r] for r in c] for k, c in enumerate(integrand[:N])]
        rhs = smul(T, integral, N)
        ok = ok and all(rhs[k] == madd(T[k], T0[k], -1) for k in range(N + 1))
        ok = ok and any(c != mz() for c in rhs)
    _tp_rv = (ok); assert _tp_rv is not False, "check_variation_of_constants_identity"; return _tp_rv


def kasner_point(t):
    d = 1 + t + t * t
    return (-t / d, (1 + t) / d, t * (1 + t) / d)


def check_model_generator_bounded_by_one():
    ok = True
    for name in ("B1", "B2", "B3"):
        M = act(blade(name))
        X = GA.mat_mul([list(r) for r in zip(*M)], M)
        ok = ok and GA.mat_mul(X, X) == X and X != mz()
    for t in KASNER_U:
        p = kasner_point(t)
        ok = ok and sum(p) == 1 and sum(x * x for x in p) == 1
        for u in UNITS:
            ok = ok and sum(x * x for x in u) == 1
            Hb = GA.add(*[blade("B%d" % (i + 1), u[i] * p[i]) for i in range(3)])
            M = act(Hb)
            X = GA.mat_mul([list(r) for r in zip(*M)], M)
            w2 = sum((u[i] * p[i]) ** 2 for i in range(3))
            ok = ok and GA.mat_mul(X, madd(X, meye(), -w2)) == mz()
            l1 = sum(abs(u[i]) * abs(p[i]) for i in range(3))
            ok = ok and w2 <= l1 * l1 <= 1
        up = tuple(abs(x) for x in p)
        ok = ok and sum(abs(up[i]) * abs(p[i]) for i in range(3)) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_model_generator_bounded_by_one"; return _tp_rv
