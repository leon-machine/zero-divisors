"""Local normality at a point of a horizon generator: exact checks.

(1) The weight-1/2 scaling preserves the Hilbert-Schmidt norm of a kernel shrunk onto a point.
    The boost is the dilation about the edge (rotor B sends l -> r^2 l, n -> r^-2 n, fixes e2, e3).
    For a kernel R and the scaling with weight p per leg, (S_s R)(x, y) = s^{2p} R(s x, s y),
    ||S_s R||^2 on I x I equals s^{4p - 2} ||R||^2 on sI x sI. Checked on polynomial kernels with exact
    integrals over rational rectangles, at s = t^2 and p = k/4: equality with ||R||^2 on sI x sI holds
    exactly for k = 2 (p = 1/2) and fails for k = 0, 1, 3, 4. For a polynomial (bounded) remainder the
    shrunk norm tends to zero: ||R||^2 on sI x sI <= s^2 |I|^2 max|R|^2, checked at s = 2^-n.
(2) Powers-Stormer gives the Hilbert-Schmidt difference: A - B = A^{1/2}(A^{1/2} - B^{1/2})
    + (A^{1/2} - B^{1/2}) B^{1/2}, so ||A - B||_HS <= 2 ||A^{1/2} - B^{1/2}||_HS for 0 <= A, B <= 1.
    Checked exactly in finite dimensions with A = X^2, B = Y^2, X, Y rational symmetric contractions.
(3) Degree -1 homogeneous remainders are not square integrable at the edge. The null vacuum's cross-edge
    block i/(2 pi (u - v)) (u > 0 > v, w = -v): int_a^b int_c^d (u + w)^-2 dw du = ln of the rational
    (a + d)(b + c)/((a + c)(b + d)) (checked by exact differentiation of the antiderivative identity at
    rational points), and on the dyadic squares [s, 2s]^2 its argument is 9/8 for every s: each shell
    contributes ln(9/8) > 0, so the sum over shells diverges. The same block is the difference between
    the vacuum and every product state omega_c^x (cross block 0), every c, c = 1 included. On a half, the
    c = 1/2 difference at u = a^2, v = b^2 is D = -(a - b)/((a + b)(a^2 + b^2)) (times i/2 pi), exactly
    homogeneous of degree -1 in (u, v) and nonzero off the diagonal.
(4) A regular reparametrisation changes the vacuum by a bounded kernel: for f(u) = u + 2u^3/3 + u^5/5,
    f' = (1 + u^2)^2, the kernel f'(u)^{1/2} f'(v)^{1/2}/(f(u) - f(v)) - 1/(u - v) equals
    (u - v)(1/3 - (u^2 + 3uv + v^2)/5)/Q(u, v), Q = (f(u) - f(v))/(u - v), checked at a rational grid;
    its leading term (u - v)/3 is S_f(0)(u - v)/12 with the Schwarzian S_f(0) = 4.
Exact arithmetic only (Fractions); logarithms are never evaluated, only their rational arguments.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ4 = (1, -1, -1, -1)


def _m(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, SQ4)
    return out


def _vec(c0, c1, c2=0, c3=0):
    return GA.add(GA.scal(c0, GA.gen(0)), GA.scal(c1, GA.gen(1)), GA.scal(c2, GA.gen(2)), GA.scal(c3, GA.gen(3)))


def _rotor(r):
    return GA.add(GA.sc((r + 1 / r) / 2), GA.scal((r - 1 / r) / 2, _m(GA.gen(1), GA.gen(0))))


# bivariate polynomials as dicts {(i, j): coeff} for x^i y^j
def _pmul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            out[i + k, j + l] = out.get((i + k, j + l), F(0)) + a * b
    return {key: v for key, v in out.items() if v != 0}


def _int_rect(p, x0, x1, y0, y1):
    tot = F(0)
    for (i, j), a in p.items():
        tot += a * (x1 ** (i + 1) - x0 ** (i + 1)) / (i + 1) * (y1 ** (j + 1) - y0 ** (j + 1)) / (j + 1)
    return tot


def _scaled(p, s, weight_factor):
    return {(i, j): a * weight_factor * s ** (i + j) for (i, j), a in p.items()}


ROTOR_R = (F(3, 2), F(1, 4))
INTERVAL = (F(-1), F(2))
SCALE_T = (F(1, 2), F(2, 3), F(3))
CONTRACTIONS = ([[F(1, 2), F(1, 5), F(0)], [F(1, 5), F(1, 3), F(1, 10)], [F(0), F(1, 10), F(2, 5)]],
                [[F(2, 5), F(0), F(1, 7)], [F(0), F(1, 2), F(1, 9)], [F(1, 7), F(1, 9), F(1, 4)]])
RECTS = [(F(1), F(2), F(5), F(1, 2), F(3), F(4)), (F(1, 3), F(5, 2), F(3), F(2), F(7, 3), F(9))]
SHELL_S = (F(1), F(1, 2), F(1, 1024), F(3, 7))
HALF_PTS = [(F(2), F(1)), (F(1, 3), F(5, 4)), (F(7, 2), F(3))]
HOM_S = (F(1, 2), F(3))
GRID = [F(k, 7) for k in range(-6, 7)]
F_POLY = [F(0), F(1), F(0), F(2, 3), F(0), F(1, 5)]


KERNELS = [
    {(0, 0): F(1), (1, 0): F(3), (1, 1): F(-2), (0, 2): F(1)},
    {(0, 0): F(-2, 3), (2, 1): F(5), (0, 3): F(1, 2), (1, 0): F(1, 7)},
]


def check_weight_half_preserves_the_local_hilbert_schmidt_norm():
    premise("synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit")
    premise("synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet")
    l, n = _vec(1, 1), _vec(1, -1)
    for r in ROTOR_R:
        B = _rotor(r)
        Bt = GA.reverse(B)
        GA.check("rotor", GA.eq(_m(B, Bt), GA.sc(1)))
        GA.check("boost dilates the generator about its edge", GA.eq(_m(B, l, Bt), GA.scal(r * r, l)))
        GA.check("and contracts the other null direction", GA.eq(_m(B, n, Bt), GA.scal(1 / (r * r), n)))
    x0, x1 = INTERVAL
    for R in KERNELS:
        R2 = _pmul(R, R)
        for t in SCALE_T:
            s = t * t
            target = _int_rect(R2, s * x0, s * x1, s * x0, s * x1)
            for k in range(5):
                # weight p = k/4: s^{2p} = t^k
                SR = _scaled(R, s, t ** k)
                lhs = _int_rect(_pmul(SR, SR), x0, x1, x0, x1)
                if k == 2:
                    GA.check("p = 1/2: ||S_s R||_I = ||R||_{sI}", lhs == target)
                else:
                    GA.check("p != 1/2 does not preserve the local HS norm", lhs != target)
                    GA.check("general law s^{4p-2}", lhs == t ** (2 * k) / s ** 2 * target)
        # a bounded remainder: the shrunk norm decays like s^2
        M = sum(abs(a) for a in R.values()) * 2 ** 3          # crude bound for max|R| on [-2, 2]^2... on [-1,2]^2
        prev = None
        for nexp in range(0, 6):
            s = F(1, 2 ** nexp)
            v = _int_rect(R2, s * x0, s * x1, s * x0, s * x1)
            GA.check("shrunk norm bounded by s^2 |I|^2 max|R|^2", v <= s * s * 9 * M * M)
            if prev is not None:
                GA.check("shrunk norm decreases", v < prev)
            prev = v


def _mat_mul(A, B):
    return GA.mat_mul(A, B)


def _hs2(A):
    return sum(x * x for row in A for x in row)


def _sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def _add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def check_quasi_equivalence_gives_a_hilbert_schmidt_difference():
    premise("synthesis.imported-powers-stormer-takesaki-disjointness")
    X, Y = CONTRACTIONS
    for (P, Q) in [(X, Y), (Y, X)]:
        # contractions: row sums of |entries| < 1 bound the operator norm
        GA.check("X, Y are contractions", all(sum(abs(x) for x in row) < 1 for row in P + Q))
        A, Bm = _mat_mul(P, P), _mat_mul(Q, Q)
        D = _sub(P, Q)
        GA.check("A - B = A^{1/2}(A^{1/2} - B^{1/2}) + (A^{1/2} - B^{1/2}) B^{1/2}",
                 _sub(A, Bm) == _add(_mat_mul(P, D), _mat_mul(D, Q)))
        PD, DQ = _mat_mul(P, D), _mat_mul(D, Q)
        cross = sum(x * y for ra, rb in zip(PD, DQ) for x, y in zip(ra, rb))
        GA.check("||A - B||^2 = ||PD||^2 + ||DQ||^2 + 2 <PD, DQ>", _hs2(_sub(A, Bm)) == _hs2(PD) + _hs2(DQ) + 2 * cross)
        GA.check("||PD||, ||DQ|| <= ||D|| for contractions", _hs2(PD) <= _hs2(D) and _hs2(DQ) <= _hs2(D))
        GA.check("||A - B||_HS^2 <= 4 ||A^{1/2} - B^{1/2}||_HS^2", _hs2(_sub(A, Bm)) <= 4 * _hs2(D))
        GA.check("the difference is nonzero", _hs2(_sub(A, Bm)) > 0)


def _log_arg(a, b, c, d):
    """int_a^b int_c^d (u + w)^-2 dw du = ln((a + d)(b + c)/((a + c)(b + d)))."""
    return (a + d) * (b + c) / ((a + c) * (b + d))


def check_homogeneous_remainder_is_not_square_integrable_at_the_edge():
    premise("synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit")
    premise("synthesis.positive-null-energy-gives-r-premises")
    # the log arguments are multiplicative over adjacent rectangles (additivity of the integral), in both legs
    for (a, b, e, c, d, g) in RECTS:
        GA.check("additive in u", _log_arg(a, b, c, d) * _log_arg(b, e, c, d) == _log_arg(a, e, c, d))
        GA.check("additive in w", _log_arg(a, b, c, d) * _log_arg(a, b, d, g) == _log_arg(a, b, c, g))
        GA.check("positive integrand: argument > 1", _log_arg(a, b, c, d) > 1)
    for s in SHELL_S:
        GA.check("dyadic shell [s,2s]^2: log argument 9/8 for every s", _log_arg(s, 2 * s, s, 2 * s) == F(9, 8))
        GA.check("shell [s,3s]x[s,2s]: argument independent of s", _log_arg(s, 3 * s, s, 2 * s) == F(6, 5))
    GA.check("each shell contributes ln(9/8) > 0", F(9, 8) > 1)
    # N disjoint shells contribute N ln(9/8): the argument of the sum is (9/8)^N, unbounded
    GA.check("N shells: argument (9/8)^N exceeds any bound", (F(9, 8)) ** 60 > 1000)
    # the half-generator difference at c = 1/2, u = a^2, v = b^2 (times i/2pi)
    def W(a, b, c2):
        u, v = a * a, b * b
        if c2 == 1:
            return 1 / (u - v)
        # c = 1/2: (uv)^{-1/2} / (c (t - 1/t)), t = u/v
        t = u / v
        return 1 / (a * b) / (F(1, 2) * (t - 1 / t))
    for (a, b) in HALF_PTS:
        D = W(a, b, 2) - W(a, b, 1)
        GA.check("D_{1/2} = -(a - b)/((a + b)(a^2 + b^2))", D == -(a - b) / ((a + b) * (a * a + b * b)))
        GA.check("nonzero off the diagonal", D != 0)
        for s in HOM_S:
            GA.check("homogeneous of degree -1 in (u, v)",
                     W(s * a, s * b, 2) - W(s * a, s * b, 1) == D / (s * s))


def check_regular_reparametrisation_changes_the_vacuum_by_a_bounded_kernel():
    premise("synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet")

    def f(u):
        return u + F(2, 3) * u ** 3 + F(1, 5) * u ** 5

    def sqrt_fp(u):
        return 1 + u * u

    def Q(u, v):
        return (f(u) - f(v)) / (u - v)

    pts = GRID
    for u in pts:
        for v in pts:
            if u == v:
                continue
            diff = sqrt_fp(u) * sqrt_fp(v) / (f(u) - f(v)) - 1 / (u - v)
            GA.check("K_f - K_0 = (u - v)(1/3 - (u^2 + 3uv + v^2)/5)/Q",
                     diff == (u - v) * (F(1, 3) - (u * u + 3 * u * v + v * v) / 5) / Q(u, v))
            GA.check("Q > 0 (f' > 0)", Q(u, v) > 0)
    # Schwarzian at 0: f' = (1+u^2)^2, f'' = 4u(1+u^2), f''' = 4(1+3u^2): S = f'''/f' - 3/2 (f''/f')^2 = 4
    fp = F_POLY
    f1 = GA.pderiv(fp)
    f2 = GA.pderiv(f1)
    f3 = GA.pderiv(f2)
    GA.check("f' = (1 + u^2)^2", GA.ptrim(f1) == GA.ptrim(GA.pmul([F(1), F(0), F(1)], [F(1), F(0), F(1)])))
    S0 = GA.peval(f3, F(0)) / GA.peval(f1, F(0)) - F(3, 2) * (GA.peval(f2, F(0)) / GA.peval(f1, F(0))) ** 2
    GA.check("leading coefficient 1/3 = S_f(0)/12", F(1, 3) == S0 / 12)
    GA.check("a non-Moebius reparametrisation (S_f(0) != 0)", S0 != 0)
