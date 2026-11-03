"""The induced Newton coupling of the series' content: what the cut-off, the content at the cut-off and the masses
give. Exact checks.

(1) Proper-time integral: int_{1/Lambda^2}^oo s^-2 e^{-s m^2} ds = Lambda^2 E_2(x), x = m^2/Lambda^2, with
    E_1(x) = -gamma - ln x + sum_{k>=1} (-1)^(k+1) x^k/(k k!) and E_2 = e^{-x} - x E_1. Checked as power series
    with symbolic ln x and gamma: E_2' = -E_1, E_1' = -e^{-x}/x, E_2(0) = 1; the x^1 coefficient gives
    Lambda^2 - m^2 ln(Lambda^2/m^2) - (1 - gamma) m^2. The ln coefficient equals -m^2 tr(E + R/6) read from the
    t^2 heat-kernel term (cross term of e^{-t m^2} with t tr(E + R/6)).
(2) Content at the cut-off (Feynman gauge, alpha = 1): the chain's content between M_I and M_U (21 vectors, 48 Weyl
    fields, the bidoublet, the complex (10,1,3), optionally the complex (15,2,2)) B = -36 + sum (1 - 6 xi_R) over its
    real scalars; matching B Lambda^2 = 12 pi M_P^2. The weak-scale value 8(1 - 6 xi_R) enters as an input.
(3) Logarithmic remainder: (a) weak-scale content alone, B = 0: sum w m^2 ln > 0 for Lambda >= 10 m_t, size below
    10^-31 of 1/G at Lambda = M_P (24 fermions); the massive-vector log weight -(3 + 6 xi_R alpha) is -4 at
    xi_R = 1/6, alpha = 1 and the sum stays positive for alpha up to 5; the tree term of the doublets at
    xi_R = 1/6 is -8 pi xi_R v^2 = -(4/3) pi v^2, of the same sign. (b) Under (S), fields at M_I (nine vectors of
    weight -4, the chain's scalars, the Majorana neutrinos under (M)) enter with both signs; their total is below
    10^-12 of 1/G at Lambda = M_P for masses up to 6 x 10^11 GeV and weights of size at most 1 per scalar.
Exact arithmetic only.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise, quantity

SAKHAROV = "synthesis.imported-sakharov-induced-gravity-coefficients"
STORED = "synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations"
NSER = 9


# ------------------------------------------------------------------ helpers (no asserted values here)
def fact(j):
    out = 1
    for i in range(2, j + 1):
        out *= i
    return out


def ser(coeffs):
    """Truncated series {power: Fraction}, powers may be -1 .. NSER."""
    return {p: F(c) for p, c in coeffs.items() if c != 0 and p <= NSER}


def expo(c):
    return ser({k: F(c) ** k / fact(k) for k in range(NSER + 1)})


class LG(object):
    """A(x) + B(x) ln x + C(x) gamma with truncated Laurent series A, B, C."""

    def __init__(self, A=None, B=None, C=None):
        self.A, self.B, self.C = ser(A or {}), ser(B or {}), ser(C or {})

    def __add__(self, o):
        return LG(addd(self.A, o.A), addd(self.B, o.B), addd(self.C, o.C))

    def scale(self, c):
        return LG({p: c * v for p, v in self.A.items()}, {p: c * v for p, v in self.B.items()},
                  {p: c * v for p, v in self.C.items()})

    def times_x(self):
        sh = lambda d: {p + 1: v for p, v in d.items()}
        return LG(sh(self.A), sh(self.B), sh(self.C))

    def deriv(self):
        d = lambda s: {p - 1: p * v for p, v in s.items() if p != 0}
        # (B ln x)' = B' ln x + B / x
        A = addd(d(self.A), {p - 1: v for p, v in self.B.items()})
        return LG(A, d(self.B), d(self.C))

    def trunc(self, n):
        t = lambda s: {p: v for p, v in s.items() if p <= n}
        return LG(t(self.A), t(self.B), t(self.C))

    def eq(self, o):
        return self.A == o.A and self.B == o.B and self.C == o.C


def addd(a, b):
    out = dict(a)
    for p, v in b.items():
        out[p] = out.get(p, F(0)) + v
    return {p: v for p, v in out.items() if v != 0}


def E1():
    A = {k: F((-1) ** (k + 1), k * fact(k)) for k in range(1, NSER + 1)}
    return LG(A, {0: F(-1)}, {0: F(-1)})


def E2():
    return LG(expo(-1)) + E1().times_x().scale(F(-1))


def real_dim_su4(rep):
    return {"1": 1, "4": 4, "6": 6, "10": 10, "15": 15}[rep]


def real_scalars(rep4, rep2l, rep2r, cplx):
    n = real_dim_su4(rep4) * rep2l * rep2r
    return 2 * n if cplx else n


# ------------------------------------------------------------------ checks
def check_proper_time_integral_gives_the_universal_logarithm():
    premise(SAKHAROV)
    e1, e2 = E1(), E2()
    ok = e2.deriv().trunc(NSER - 2).eq(e1.scale(F(-1)).trunc(NSER - 2))
    minus_exp_over_x = LG({p - 1: -v for p, v in expo(-1).items()})
    ok = ok and e1.deriv().trunc(NSER - 2).eq(minus_exp_over_x.trunc(NSER - 2))
    # E_2(0) = 1: constant term 1, no constant ln or gamma term
    ok = ok and e2.A.get(0) == 1 and e2.B.get(0, 0) == 0 and e2.C.get(0, 0) == 0
    # x^1: -1 + gamma + ln x, i.e. Lambda^2 E_2 = Lambda^2 - m^2 ln(Lambda^2/m^2) - (1 - gamma) m^2 + ...
    ok = ok and e2.A.get(1) == -1 and e2.B.get(1) == 1 and e2.C.get(1) == 1
    # the same logarithm from the heat kernel: e^{-t m^2}(1 + t a1) has t^2 coefficient -m^2 a1 (+ a2):
    # its integral against t^-3 dt / (from the Lambda^2 term's t^-2) is logarithmic, coefficient -m^2 a1
    m2, a1 = F(7, 3), F(-5, 2)
    heat = GA.ps_mul([F(1), -m2, m2 * m2 / 2], [F(1), a1, F(0)], 3)
    ok = ok and heat[1] == a1 - m2 and heat[2] - m2 * m2 / 2 == -m2 * a1
    assert ok
    return ok


def check_content_at_the_cut_off():
    """Feynman-gauge weights (alpha = 1)."""
    premise(SAKHAROV)
    premise(STORED)
    premise("standard-model.connection-forced")
    premise("standard-model.chain")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    # the weak-scale coefficient B = 8(1 - 6 xi_R) is the Krein-quartet result's (Feynman-gauge value)
    premise("synthesis.krein-quartet-drops-from-the-induced-einstein-hilbert-coefficient-only-under-a-regulator-that-treats-it-alike")
    w_vec, w_weyl = -4, 1                      # Gupta-Bleuler vector with ghosts; Weyl fermion
    NW = 16 * 3
    sm_vectors = (3 * 3 - 1) + (2 * 2 - 1) + 1
    ps_vectors = (4 * 4 - 1) + (2 * 2 - 1) + (2 * 2 - 1)

    def B(nv, scalars):                         # scalars: list of (count, xi_R)
        return nv * w_vec + NW * w_weyl + sum(n * (1 - 6 * xi) for n, xi in scalars)
    ok = sm_vectors == 12 and ps_vectors == 21
    ok = ok and B(sm_vectors, [(8, F(1, 6))]) == 0 and B(sm_vectors, [(8, F(0))]) == 8
    bi_real = real_scalars("1", 2, 2, False)
    bi_cplx = real_scalars("1", 2, 2, True)
    t1013 = real_scalars("10", 1, 3, True)
    t1522 = real_scalars("15", 2, 2, True)
    ok = ok and (bi_real, bi_cplx, t1013, t1522) == (4, 8, 60, 120)
    ok = ok and B(ps_vectors, []) == -36
    for scal in ([bi_real, t1013], [bi_cplx, t1013], [bi_cplx, t1013, t1522]):
        conf = B(ps_vectors, [(n, F(1, 6)) for n in scal])
        mini = B(ps_vectors, [(n, F(0)) for n in scal])
        ok = ok and conf == -36 and mini == -36 + sum(scal)
    ok = ok and [B(ps_vectors, [(n, F(0)) for n in s]) for s in
                 ([bi_real, t1013], [bi_cplx, t1013], [bi_cplx, t1013, t1522])] == [28, 32, 152]
    # matching B Lambda^2 / (12 pi) = M_P^2: Lambda^2 / M_P^2 = 12 pi / B, in units of pi
    ok = ok and F(12, B(sm_vectors, [(8, F(0))])) == F(3, 2)
    assert ok
    return ok


def check_logarithmic_remainder_sign_and_size():
    premise(SAKHAROV)
    premise(STORED)
    premise("standard-model.chain")
    mt = quantity("quantity.top-quark-mass")
    mW = quantity("quantity.w-boson-mass")
    mZ = quantity("quantity.z-boson-mass")
    MP = quantity("quantity.planck-mass")
    v = quantity("quantity.fermi-scale")
    # (a) weak-scale content alone, B = 0 (xi_R = 1/6, alpha = 1). Massive vector in R_alpha gauge: transverse -3 at
    # M^2, longitudinal alpha, Goldstone (1 - 6 xi_R) alpha, ghosts -2 alpha, all at mass^2 alpha M^2.
    def vec_log_weight(xi, alpha):
        return -3 + alpha * 1 + (1 - 6 * xi) * alpha - 2 * alpha
    ok = vec_log_weight(F(1, 6), F(1)) == -4 and vec_log_weight(F(0), F(5)) == -3
    ok = ok and all(vec_log_weight(F(1, 6), a) == -3 - a for a in (F(0), F(2), F(5)))
    # S(Lambda) >= coeff_L L - const, L = ln(Lambda^2/m_t^2), l_V <= m_t^2/m_V^2 - 1; other fermions only add
    for alpha in (F(1), F(5)):
        wv = -vec_log_weight(F(1, 6), alpha)
        coeff_L = 2 * 3 * mt ** 2 - wv * (2 * mW ** 2 + mZ ** 2)
        const = wv * (2 * mW ** 2 * (mt ** 2 / mW ** 2 - 1) + mZ ** 2 * (mt ** 2 / mZ ** 2 - 1))
        # alpha = 1: for Lambda >= 10 m_t, L >= ln 100 > 4 (e < 3, 3^4 = 81 < 100), so S > 0;
        # alpha = 5: the coefficient of L stays positive, so S > 0 for a large enough cut-off
        ok = ok and coeff_L > 0 and (alpha != 1 or coeff_L * 4 - const > 0)
    coeff_1 = 2 * 3 * mt ** 2 - 4 * (2 * mW ** 2 + mZ ** 2)
    coeff_5 = 2 * 3 * mt ** 2 - 8 * (2 * mW ** 2 + mZ ** 2)
    ok = ok and 3 ** 4 < 10 ** 2 and coeff_1.numerator // coeff_1.denominator == 93747
    ok = ok and coeff_5.numerator // coeff_5.denominator == 8813
    # size at Lambda = M_P: |S| <= 48 m_t^2 ln(M_P^2/m_t^2) (24 Dirac fermions, none heavier than the top);
    # ln y < bit length of y; pi > 3
    y = MP ** 2 / mt ** 2
    bits = (y.numerator // y.denominator + 1).bit_length()
    ratio_bound = 48 * mt ** 2 * bits / (12 * 3 * MP ** 2)
    scaled = ratio_bound * 10 ** 34
    ok = ok and bits == 112 and ratio_bound < F(1, 10 ** 31) and scaled.numerator // scaled.denominator == 298
    # tree term at xi_R = 1/6: Delta(1/G) = -8 pi xi_R v^2 = -(4/3) pi v^2 (coefficient of pi), negative like -S/(12 pi)
    tree_pi = -8 * F(1, 6) * v ** 2
    ok = ok and tree_pi == -F(4, 3) * v ** 2 and tree_pi < 0
    ok = ok and (-tree_pi).numerator // (-tree_pi).denominator == 80832
    ok = ok and -tree_pi * 4 < F(1, 10 ** 32) * MP ** 2          # pi < 4: below 1e-32 of M_P^2
    # (b) under (S): nine heavy vectors (21 - 12) of weight -4 at M_I, the chain's 188 real scalars at most, three
    # Majorana neutrinos under (M); total |w| <= 36 + 188 + 3; masses <= 6 x 10^11 GeV
    n_heavy = ((4 * 4 - 1) + 3 + 3) - ((3 * 3 - 1) + 3 + 1)
    abs_w = 4 * n_heavy + 188 + 3
    MI = 6 * 10 ** 11
    y2 = MP ** 2 / MI ** 2
    bits2 = (y2.numerator // y2.denominator + 1).bit_length()
    bound2 = abs_w * MI ** 2 * bits2 / (12 * 3 * MP ** 2)
    ok = ok and n_heavy == 9 and abs_w == 227 and bits2 == 49 and bound2 < F(1, 10 ** 12)
    s2 = bound2 * 10 ** 13
    ok = ok and s2.numerator // s2.denominator == 7
    # the heavy vectors alone have the attractive sign: -4 x 9 < 0, opposite to the top's +6
    ok = ok and -4 * n_heavy < 0 < 2 * 3
    assert ok
    return ok
