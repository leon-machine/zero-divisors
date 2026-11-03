"""synthesis.killing-clock-weights-binary-residue: exact checks.

Mode operators are built in the real Clifford algebra Cl(n, n) of GA.py, one hyperbolic atom
per mode: generators a_j (square +1) and b_j (square -1), v_j = (a_j + b_j)/2,
v_j^* = (a_j - b_j)/2. Everything is exact (Fractions); exponentials and logarithms enter
only through rational enclosures of pi, e^x and ln 2.

(i)   CAR for n = 3 modes; the adjoint action of X = sum_i c_i v_i^* v_i on v_j, v_j^* is
      -c_j, +c_j (so the adjoint spectrum on the mode operators is {+-c_j}); the atom boost
      sigma_j / 2 = N_j - 1/2 acts with -1, +1 (unit rapidity), the central shift invisible.
(ii)  over all c in {-2..2}^3: X is a clock (all nonzero |adjoint eigenvalues| equal) exactly
      when the nonzero |c_i| coincide, and then the normalised weights lie in {-1, 0, 1}.
(iii) the (Q) weights c_k = k on an array k = -j..j: a clock for j = 1, not for j = 2, 3.
(iv)  binary residue: with s = s(2 pi) bracketed, kappa_c(f) = 1/(4((1-f) ln 2 + f s)) is
      increasing in f, equals the registered bracket at f = 0, lies in (18.413, 18.414) at
      f = 1; ln 2 / s in (51.05, 51.06); de Sitter |J| / (pi N^2) = 1/s in (73.65, 73.66).
"""
from fractions import Fraction as F
from itertools import product
import GA
import series
from tp_premise import premise

PREMISES = (
    "scrambling.clock-inventory-boundary-modes",
    "hawking.modular-structure-completed-pair",
    "scrambling.boundary-mode-space-matrix",
    "singularity.plane-rate",
    "synthesis.boundary-mode-thermal-entropy",
    "synthesis.residue-from-mode-entropy",
    "synthesis.residue-common-weight-particle-hole",
)


def touch():
    for p in PREMISES:
        premise(p)


def modes(n):
    squares = tuple([1, -1] * n)
    half = F(1, 2)
    v = [GA.scal(half, GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(n)]
    vs = [GA.scal(half, GA.sub(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(n)]
    return squares, v, vs


def ad(X, y, sq):
    return GA.sub(GA.mul(X, y, sq), GA.mul(y, X, sq))


def eigen_coeff(x, y):
    """the scalar c with x = c y (y a nonzero element), or None."""
    b0, c0 = next(iter(y.items()))
    c = x.get(b0, F(0)) / c0
    return c if GA.eq(x, GA.scal(c, y)) else None


def adjoint_weights(c, sq, v, vs):
    X = {}
    for i, ci in enumerate(c):
        X = GA.add(X, GA.scal(ci, GA.mul(vs[i], v[i], sq)))
    out = []
    for j in range(len(c)):
        wv = eigen_coeff(ad(X, v[j], sq), v[j])
        ws = eigen_coeff(ad(X, vs[j], sq), vs[j])
        out.append((wv, ws))
    return out


def is_clock(weights):
    mags = set(abs(w) for pair in weights for w in pair if w != 0)
    return len(mags) == 1


def check_mode_algebra_and_unit_rapidity():
    touch()
    n = 3
    sq, v, vs = modes(n)
    one = GA.sc(1)
    for i in range(n):
        for j in range(n):
            acomm = GA.add(GA.mul(v[i], vs[j], sq), GA.mul(vs[j], v[i], sq))
            assert GA.eq(acomm, one if i == j else {})
            assert GA.is_zero(GA.add(GA.mul(v[i], v[j], sq), GA.mul(v[j], v[i], sq)))
    for j in range(n):
        sigma = GA.sub(GA.mul(vs[j], v[j], sq), GA.mul(v[j], vs[j], sq))
        assert GA.eq(GA.mul(sigma, sigma, sq), one)
        K = GA.scal(F(1, 2), sigma)
        Nm = GA.sub(GA.mul(vs[j], v[j], sq), GA.scal(F(1, 2), one))
        assert GA.eq(K, Nm)                                    # sigma/2 = N - 1/2
        assert eigen_coeff(ad(K, v[j], sq), v[j]) == -1        # unit rapidity, weight -1
        assert eigen_coeff(ad(K, vs[j], sq), vs[j]) == 1
        for k in range(n):
            if k != j:
                assert GA.is_zero(ad(K, v[k], sq))             # other modes untouched
    for c in ((F(2), F(-1), F(1, 2)), (F(0), F(3), F(-3))):
        w = adjoint_weights(c, sq, v, vs)
        for j in range(n):
            assert w[j] == (-c[j], c[j])
    return True


def check_clock_forces_binary_weights():
    touch()
    n = 3
    sq, v, vs = modes(n)
    seen_clock = seen_not = 0
    for c in product(range(-2, 3), repeat=n):
        if all(x == 0 for x in c):
            continue
        w = adjoint_weights([F(x) for x in c], sq, v, vs)
        nonzero = set(abs(x) for x in c if x != 0)
        assert is_clock(w) == (len(nonzero) == 1)
        if is_clock(w):
            seen_clock += 1
            m = nonzero.pop()
            normalised = [F(-a, m) for a, _ in w]
            assert set(normalised) <= {F(-1), F(0), F(1)}
        else:
            seen_not += 1
    assert seen_clock == 52 and seen_not == 72
    return True


def check_q_weights_not_a_clock():
    touch()
    for j, expect in ((1, True), (2, False), (3, False)):
        n = 2 * j + 1
        sq, v, vs = modes(n)
        c = [F(k) for k in range(-j, j + 1)]
        assert len(c) == n == len(v)
        w = adjoint_weights(c, sq, v, vs)
        assert is_clock(w) == expect
        mags = sorted(set(abs(a) for a, _ in w if a != 0))
        assert mags == [F(m) for m in range(1, j + 1)]
        assert sum(1 for a, _ in w if a == 0) == 1
    return True


PI_LO, PI_HI = F(314159265358979, 10 ** 14), F(314159265358980, 10 ** 14)


exp_bounds = series.exp_bounds          # rational bounds for e^x, x >= 0


def ln1p_bounds(y):
    return series.log_bounds(1 + y)


def ln2_bounds():
    return series.ln_bounds(2)


def s2pi_bounds():
    xl, xh = 2 * PI_LO, 2 * PI_HI
    el, _ = exp_bounds(xl)
    _, eh = exp_bounds(xh)
    ql, qh = 1 / eh, 1 / el
    a_lo, _ = ln1p_bounds(ql)
    _, a_hi = ln1p_bounds(qh)
    return a_lo + xl * ql / (1 + ql), a_hi + xh * qh / (1 + qh)


def check_binary_residue():
    touch()
    slo, shi = s2pi_bounds()
    llo, lhi = ln2_bounds()
    assert F(13577, 10 ** 6) < slo and shi < F(13578, 10 ** 6)
    assert shi < llo
    prev_hi = None
    for f in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
        lo = 1 / (4 * ((1 - f) * lhi + f * shi))
        hi = 1 / (4 * ((1 - f) * llo + f * slo))
        if prev_hi is not None:
            assert lo > prev_hi                       # strictly increasing in f
        prev_hi = hi
        if f == 0:
            assert F(3606, 10 ** 4) < lo and hi < F(3608, 10 ** 4)
        if f == 1:
            assert F(18413, 1000) < lo and hi < F(18414, 1000)
    assert F(5105, 100) < llo / shi and lhi / slo < F(5106, 100)
    assert F(7365, 100) < 1 / shi and 1 / slo < F(7366, 100)
    return True
