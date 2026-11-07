"""synthesis.null-vacuum-on-a-horizon-generator: exact checks.

The continuum mode space CAR(L^2(R, du) (x) K) of a generator, with the null translations nu_a and the
weight-1/2 boost beta_t; the unit of the one-particle space is I_4 (numbers in span{1, I_4}).
(1) The setup: beta_t nu_a beta_-t = nu_{e^{kappa t} a} as affine maps of the generator.
(2) The null vacuum: in the spectral representation of P = I_4 d/du a symbol value A(k) in [0, 1] meets
    k A(k) <= 0 and (1 - A(k)) k >= 0 exactly when A = 1 for k < 0 and A = 0 for k > 0 (rational grid);
    P acts on e^{I_4 k u} as -k (so chi(P < 0) keeps k > 0); the regularised kernel
    (1/2pi) int_0^inf e^{(I_4 x - eps) k} dk = (1/2pi)(eps - I_4 x)^{-1} equals (I_4/2pi)(x + I_4 eps)^{-1},
    and the two orderings add to the Poisson kernel 2 eps/(x^2 + eps^2) (the anticommutator), exactly in
    span{1, I_4} of Cl(1,3).
(3) The half-generator restrictions (copied from synthesis.positive-null-energy-gives-r-premises, clause
    (ii) there): the analytic strip at rapidity period 2 pi, the past half, and the Mellin symbol, with
    Gaussian rationals (QI) for the unit of the complex analysis.
Exact arithmetic only (Fractions, Gaussian rationals); pi is never evaluated.
"""
from fractions import Fraction as F
import GA
from GA import QI
from tp_premise import premise

SQ4 = (1, -1, -1, -1)                 # store signature (+,-,-,-): e0, e1, e2, e3
I4 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), SQ4), GA.mul(GA.gen(2), GA.gen(3), SQ4), SQ4)


def _num(a, b):
    """a + b I_4 in span{1, I_4}."""
    return GA.add(GA.sc(a), GA.scal(b, I4))


def _unit_circle(t):
    """z = e^{i theta} with t = tan(theta/2): exact Gaussian rational."""
    d = 1 + t * t
    return QI(F(1 - t * t) / d, F(2 * t) / d)


def _sign(x):
    return (x > 0) - (x < 0)


def check_boost_dilates_the_null_translations():
    # affine maps of the generator as (scale, shift): u -> s u + c; fields psi(u) -> psi(map(u))
    def comp(f, g):                    # (f o g)(u) = f(g(u))
        return (f[0] * g[0], f[0] * g[1] + f[1])
    ok = True
    # hand-computed shifts r a
    want = {(F(3, 2), F(2, 3)): F(1), (F(3, 2), F(-5)): F(-15, 2), (F(3, 2), F(1, 9)): F(1, 6),
            (F(1, 5), F(2, 3)): F(2, 15), (F(1, 5), F(-5)): F(-1), (F(1, 5), F(1, 9)): F(1, 45),
            (F(7), F(2, 3)): F(14, 3), (F(7), F(-5)): F(-35), (F(7), F(1, 9)): F(7, 9)}
    for (r, a), shift in want.items():              # r = e^{kappa t}
        # beta_t nu_a beta_-t (psi(u)) = psi(r ((u / r) + a)) up to the weight factors, which cancel
        m = comp((r, F(0)), comp((F(1), a), (1 / r, F(0))))
        ok = ok and m == (F(1), shift) and m != (F(1), a)
    ok = ok and len(want) == 9
    GA.check("beta_t nu_a beta_-t = nu_{e^{kappa t} a}", ok)
    return ok


def check_ground_state_symbol_is_the_filled_sea():
    # k -> the only allowed symbol value, tabulated
    want = {F(-3): F(1), F(-1, 2): F(1), F(-1, 100): F(1), F(1, 100): F(0), F(2, 3): F(0), F(5): F(0)}
    grid = [F(j, 8) for j in range(9)]
    ok = len(grid) == 9 and grid[3] == F(3, 8) and grid[-1] == 1
    for k, A0 in want.items():
        allowed = [A for A in grid if k * A <= 0 and (1 - A) * k >= 0]
        ok = ok and allowed == [A0]
        # control: the reversed orientation (k A >= 0, (1 - A) k <= 0) keeps the other end
        rev = [A for A in grid if k * A >= 0 and (1 - A) * k <= 0]
        ok = ok and rev == [1 - A0]
    # at k = 0 both conditions are empty (a null set)
    ok = ok and [A for A in grid if F(0) * A <= 0 and (1 - A) * F(0) >= 0] == grid
    # P = I_4 d/du on e^{I_4 k u}: d/du gives I_4 k, so P gives I_4 I_4 k = -k
    for k, Pk in ((F(1), F(-1)), (F(-2, 3), F(2, 3)), (F(7, 4), F(-7, 4))):
        ok = ok and GA.eq(GA.mul(I4, GA.scal(k, I4), SQ4), GA.sc(Pk))
    GA.check("ground-state conditions force the symbol chi(P < 0); P = -k on e^{I_4 k u}", ok)
    return ok


def check_null_vacuum_kernel_and_anticommutator():
    ok = GA.eq(GA.mul(I4, I4, SQ4), GA.sc(-1))
    # hand-computed Poisson kernel 2 eps / (x^2 + eps^2)
    poisson = {(F(1), F(1)): F(1), (F(1), F(1, 10)): F(20, 101), (F(1), F(1, 1000)): F(2000, 1000001),
               (F(-3, 2), F(1)): F(8, 13), (F(-3, 2), F(1, 10)): F(10, 113), (F(-3, 2), F(1, 1000)): F(2000, 2250001),
               (F(2, 7), F(1)): F(98, 53), (F(2, 7), F(1, 10)): F(980, 449), (F(2, 7), F(1, 1000)): F(98000, 4000049),
               (F(0), F(1)): F(2), (F(0), F(1, 10)): F(20), (F(0), F(1, 1000)): F(2000)}
    for (x, eps), pk in poisson.items():
        # (eps - I_4 x) * [I_4 (x + I_4 eps)^{-1}] = 1, checked as (eps - I_4 x) I_4 = x + I_4 eps
        ok = ok and GA.eq(GA.mul(_num(eps, -x), I4, SQ4), _num(x, eps))
        # (x + I_4 eps)(x - I_4 eps) = x^2 + eps^2, so the inverse is (x - I_4 eps)/(x^2 + eps^2)
        n2 = x * x + eps * eps
        ok = ok and GA.eq(GA.mul(_num(x, eps), _num(x, -eps), SQ4), GA.sc(n2))
        inv_p = GA.scal(1 / n2, _num(x, -eps))
        inv_m = GA.scal(1 / n2, _num(x, eps))
        w_minus = GA.mul(I4, inv_p, SQ4)                       # I_4 (x + I_4 eps)^{-1}
        w_plus = GA.neg(GA.mul(I4, inv_m, SQ4))                # -I_4 (x - I_4 eps)^{-1}
        # the two orderings add to the Poisson kernel 2 eps / (x^2 + eps^2), real
        ok = ok and GA.eq(GA.add(w_minus, w_plus), GA.sc(2 * eps / n2)) and 2 * eps / n2 == pk
        # its value at the diagonal is 2/eps: a delta of weight 2 pi after the factor 1/(2 pi)
        if x == 0:
            ok = ok and GA.eq(GA.add(w_minus, w_plus), GA.sc(2 / eps))
    GA.check("W_0 = (I_4/2pi)(x + I_4 0)^{-1} from the Fourier integral; the orderings add to the Poisson kernel", ok)
    return ok


def check_half_generator_strip_is_kms_at_two_pi():
    premise("hawking.imported-quasi-free-kms-reduces-two")
    premise("hawking.i-state-continuum")
    # coefficients of the two orderings, in units of 1/(2 pi), and their i0 directions
    c_minus, s_minus = QI(0, 1), +1      # omega(psi*(v) psi(u)) = (i/2pi)/(u - v + i0)
    c_plus, s_plus = QI(0, -1), -1       # omega(psi(u) psi*(v)) = (-i/2pi)/(u - v - i0)
    GA.check("CAR: the two coefficients add to zero off the diagonal", c_minus + c_plus == 0)
    ts_pos = [F(1, 50), F(1, 7), F(1, 2), F(1), F(3), F(40)]
    ts = ts_pos + [-t for t in ts_pos]
    samples = [(F(1), F(1), F(1)), (F(2), F(3), F(1, 2)), (F(5, 3), F(7, 4), F(9, 5)), (F(1, 9), F(4), F(3))]
    for (u, v, q) in samples:
        for t in ts:
            D = _unit_circle(t) * (q * u) - v
            GA.check("no zero of z q u - v in the open strip (u, v > 0)", bool(D))
            GA.check("Im(z q u - v) has the sign of t: + on (0, pi), - on (pi, 2 pi)", _sign(D.im) == _sign(t))
            GA.check("theta in (0, 2 pi) is not a return: z q u - v != q u - v", D != QI(q * u - v))
        Dpi = QI(-1) * (q * u) - v
        GA.check("theta = pi: the reflected point, still no zero", bool(Dpi) and Dpi.re < 0)
        # boundary approach: theta -> 0+ is t -> 0+, theta -> 2 pi- is t -> 0-
        GA.check("theta -> 0+: approach from above, the +i0 of W-", _sign(_unit_circle(F(1, 10 ** 6)).im) == s_minus)
        GA.check("theta -> 2 pi-: approach from below, the -i0 of W+", _sign(_unit_circle(F(-1, 10 ** 6)).im) == s_plus)
    # tabulated denominators z q u - v at hand-computed points (t, u, v, q) -> value
    table = [((F(1), F(2), F(3), F(1, 2)), QI(-3, 1)),          # z = i
             ((F(-1), F(2), F(3), F(1, 2)), QI(-3, -1)),        # z = -i
             ((F(1, 2), F(1), F(1), F(1)), QI(F(-2, 5), F(4, 5))),  # z = (3 + 4i)/5
             ((F(2), F(5, 3), F(7, 4), F(9, 5)), QI(F(-71, 20), F(12, 5)))]  # z = (-3 + 4i)/5
    for (t, u, v, q), want in table:
        GA.check("tabulated: z q u - v", _unit_circle(t) * (q * u) - v == want)
    # control: a point on the other side of the edge gives a zero inside the strip, at theta = pi
    for (u, v) in [(F(-1), F(1)), (F(-2), F(3)), (F(-5, 3), F(7, 4))]:
        q = v / (-u)
        GA.check("control: u < 0 < v puts a zero of z q u - v at theta = pi", not bool(QI(-1) * (q * u) - v))
    # the weight is forced by the anticommutator: e^{lambda w} psi(e^lambda u) preserves {psi, psi*} = delta
    # iff e^{2 lambda w} e^{-lambda} = 1; at e^{lambda/2} = rho this is rho^{4w} rho^{-2} = 1 (w = k/4: rho^{k-2})
    forced = [F(k, 4) for k in range(8) if all(rho ** (k - 2) == 1 for rho in (F(3, 2), F(1, 5)))]
    GA.check("only w = 1/2 preserves the CAR among quarter weights", forced == [F(1, 2)])
    # its factor at 2 pi is e^{i pi} = -1 (i^2), carrying c_- to c_+; an integer weight (i^0 or i^4) would not
    GA.check("e^{i pi} c_- = c_+", QI(0, 1) * QI(0, 1) * c_minus == c_plus)
    GA.check("control: e^{2 pi i} c_- != c_+", QI(1) * c_minus != c_plus)
    # control: the negative-energy prescription swaps the i0 directions; the forward strip then mismatches
    GA.check("control: with -i0 for W- the boundary at theta -> 0+ does not match",
             _sign(_unit_circle(F(1, 10 ** 6)).im) != -s_minus)
    return True


def check_past_half_is_kms_for_the_future_boost():
    premise("hawking.imported-quasi-free-kms-reduces-two")
    premise("hawking.i-state-continuum")
    # past half u, v < 0, future-directed boost there: u -> e^{-lambda} u, weight e^{-lambda/2}.
    # F(lambda) = e^{-lambda/2} (i/2pi)/(e^{-lambda} u - v + i0); continue lambda -> lambda + i theta:
    # denominator conj(z) q' u - v with q' = e^{-Re lambda}, conj(z) = e^{-i theta}.
    ts_pos = [F(1, 50), F(1, 7), F(1, 2), F(1), F(3), F(40)]
    ts = ts_pos + [-t for t in ts_pos]
    for (u, v, qp) in [(F(-1), F(-1), F(1)), (F(-2), F(-3), F(1, 2)), (F(-5, 3), F(-7, 4), F(9, 5))]:
        for t in ts:
            D = _unit_circle(t).conj() * (qp * u) - v
            GA.check("past half: no zero in the open strip", bool(D))
            GA.check("past half: Im has the sign of t (u < 0)", _sign(D.im) == _sign(t))
    # weight factor e^{-i theta/2} at theta = 2 pi is e^{-i pi} = -1: maps i to -i, as for the future half
    GA.check("past half: e^{-i pi} * i = -i", QI(-1) * QI(0, 1) == QI(0, -1))
    # tabulated: t = 1 (theta = pi/2), u = -2, v = -3, q' = 1/2: conj(i)(-1) + 3 = 3 + i
    GA.check("tabulated past-half denominator", _unit_circle(F(1)).conj() * (F(1, 2) * F(-2)) - F(-3) == QI(3, 1))
    # control: the past-directed boost on the past half (u -> e^{lambda} u) has Im of sign -t: KMS at -2 pi
    for t in ts_pos:
        D = _unit_circle(t) * (F(1) * F(-2)) - F(-3)
        GA.check("control: wrong orientation on the past half reverses the sign", _sign(D.im) == -1)
    # Mellin: under u -> -u the past-half kernel is the complex conjugate of the future-half one, so its
    # symbol on u^{-1/2 + i w} is m(-w) = (1 + e^{2 pi w})^{-1}, the I-state for the reversed generator +w
    for q in [F(2), F(1, 3), F(7, 5)]:
        m_plus = lambda qq: 1 / (1 + (1 / qq) ** 2)          # m(w) with qq = e^{pi w}
        GA.check("m(-w) = (1 + e^{2 pi w})^{-1}", m_plus(1 / q) == 1 / (1 + q * q))
        GA.check("m(w) + m(-w) = 1", m_plus(q) + m_plus(1 / q) == 1)
    return True


def check_mellin_symbol_is_the_i_state_at_two_pi():
    premise("hawking.i-state-continuum")
    premise("hawking.imported-ideal-fermi-gas-uniqueness")
    for q in [F(2), F(1, 3), F(7, 5), F(11), F(1)]:
        # q = e^{pi omega}; cos(pi s) = -i sinh(pi omega), sin(pi s) = cosh(pi omega)
        sinh = (q - 1 / q) / 2
        cosh = (q + 1 / q) / 2
        cot = QI(0, -1) * sinh / cosh
        m = QI(0, 1) / 2 * (cot - QI(0, 1))
        GA.check("symbol is real", m.im == 0)
        ebh = {k: (1 / q) ** k for k in (1, 2, 4)}   # e^{beta h} with h = -omega, beta = k pi
        GA.check("m = (1 + e^{2 pi h})^{-1}", m == QI(1 / (1 + ebh[2])))
        if q != 1:
            GA.check("m != (1 + e^{pi h})^{-1}", m != QI(1 / (1 + ebh[1])))
            GA.check("m != (1 + e^{4 pi h})^{-1}", m != QI(1 / (1 + ebh[4])))
        GA.check("two-point KMS identity 1 - m = e^{2 pi h} m", QI(1) - m == m * ebh[2])
        GA.check("0 < m < 1", 0 < m.re < 1)
    return True


def run():
    return all([check_boost_dilates_the_null_translations(), check_ground_state_symbol_is_the_filled_sea(),
                check_null_vacuum_kernel_and_anticommutator(), check_half_generator_strip_is_kms_at_two_pi(),
                check_past_half_is_kms_for_the_future_boost(), check_mellin_symbol_is_the_i_state_at_two_pi()])


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
