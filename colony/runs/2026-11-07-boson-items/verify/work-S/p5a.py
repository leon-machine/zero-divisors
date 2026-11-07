"""synthesis.ladder-states-are-locally-product-with-non-gaussian-fluctuations: exact checks.

N blocks of two tower planes; plane j has e_j = gen(2j) (square +1), f_j = gen(2j + 1) (square -1),
v_j = (e_j + f_j)/2 = a*_j, w_j = (e_j - f_j)/2 = a_j, n_j = v_j w_j; block i has lower mode 2i and upper mode 2i + 1,
hopping b_i = v_(2i) w_(2i+1), K = sum_i b_i (= sqrt(N) B), P = prod_i n_(2i)(1 - n_(2i+1)) the polarised element,
psi_k = (K*)^k P. Vectors are elements of the left regular representation with <x, y> = <x* y>_0, the scalar part;
the basis blades are orthonormal for it. omega_k(X) = <psi_k, X psi_k> / <psi_k, psi_k>.
(1) Blades orthonormal (N = 1, 2); for N = 1, 2, 3 and k = 0..N: K psi_k = k(N - k + 1) psi_(k-1), K psi_0 = 0,
    <psi_k, psi_k> = k(N - k + 1) <psi_(k-1), psi_(k-1)>, and |K^m psi_k|^2 / (N^m |psi_k|^2) =
    (k)_m (N - k + 1)^(m) / N^m for m = 0..N + 1 (zero for m > k); omega_k(B) = omega_k(B^2) = 0.
(2) Marginals: omega_k(n_upper,0) = k/N; the probability that blocks 0..m-1 are all polarised is
    C(N - m, k)/C(N, k); omega_k((K*)^a K^c) = 0 for a != c <= 2; omega_k(b_0* b_1) = k(N - k)/(N(N - 1)); omega_k(n_upper,0 n_upper,1) = k(k - 1)/(N(N - 1)).
(3) The polarised element of one block is a minimal projection: P X P = pol(X) P for all 16 blades X of the block,
    pol(X) = <P X>_0 / <P>_0.
(4) Limit moments (k)_m against the quasi-free values m! k^m: they differ at m = 2 for every k >= 1 (k = 1..40),
    and at m = k + 1 the ladder value is 0.
"""
from fractions import Fraction as F
import itertools

import GA
from tp_premise import premise


def _dag(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b)
        s = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        out[b] = c * s
    return {b: c for b, c in out.items() if c != 0}


def _prod(xs, sq):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, sq)
    return r


def _ip(x, y):
    return sum((c * y.get(b, 0) for b, c in x.items()), F(0))


def _ff(a, m):
    r = 1
    for i in range(m):
        r *= a - i
    return r


def _rf(a, m):
    r = 1
    for i in range(m):
        r *= a + i
    return r


def _binom(a, m):
    if m < 0 or m > a:
        return F(0)
    return F(_ff(a, m), _ff(m, m))


def _blocks(Nb):
    sq = tuple([1, -1] * (2 * Nb))
    v = [GA.scal(F(1, 2), GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(2 * Nb)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(2 * Nb)]
    n = [GA.mul(v[j], w[j], sq) for j in range(2 * Nb)]
    b = [GA.mul(v[2 * i], w[2 * i + 1], sq) for i in range(Nb)]
    K = GA.add(*b)
    Ks = _dag(K, sq)
    P = _prod([GA.mul(n[2 * i], GA.sub(GA.sc(1), n[2 * i + 1]), sq) for i in range(1, Nb)] + [GA.mul(n[0], n[1], sq)], sq)
    return sq, v, w, n, b, K, Ks, P


def check_ladder_moments_are_boson_number_moments():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    for Nb in (1, 2):
        sq = tuple([1, -1] * (2 * Nb))
        for r in range(len(sq) + 1):
            for bl in itertools.combinations(range(len(sq)), r):
                assert GA.mul(_dag({bl: F(1)}, sq), {bl: F(1)}, sq) == GA.sc(1)
    for Nb in (1, 2, 3):
        sq, v, w, n, b, K, Ks, P = _blocks(Nb)
        prev = None
        psi = P
        for k in range(Nb + 1):
            nrm = _ip(psi, psi)
            assert nrm != 0
            if prev is None:
                assert GA.mul(K, psi, sq) == {}
            else:
                assert GA.eq(GA.mul(K, psi, sq), GA.scal(F(k * (Nb - k + 1)), prev))
                assert nrm == k * (Nb - k + 1) * _ip(prev, prev)
            phi = psi
            for m in range(Nb + 2):
                assert _ip(phi, phi) / (nrm * F(Nb) ** m) == F(_ff(k, m) * _rf(Nb - k + 1, m), Nb ** m)
                phi = GA.mul(K, phi, sq)
            assert _ip(psi, GA.mul(K, psi, sq)) == 0
            assert _ip(psi, GA.mul(K, GA.mul(K, psi, sq), sq)) == 0
            prev = psi
            psi = GA.mul(Ks, psi, sq)
    return True


def check_ladder_marginals_tend_to_the_polarised_product_state():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    for Nb in (1, 2, 3):
        sq, v, w, n, b, K, Ks, P = _blocks(Nb)
        psi = P
        for k in range(Nb + 1):
            nrm = _ip(psi, psi)

            def E(X):
                return _ip(psi, GA.mul(X, psi, sq)) / nrm
            assert E(n[1]) == F(k, Nb)
            assert E(n[0]) == F(Nb - k, Nb)
            for m in range(1, Nb + 1):
                Pm = _prod([GA.mul(n[2 * i], GA.sub(GA.sc(1), n[2 * i + 1]), sq) for i in range(m)], sq)
                assert E(Pm) == _binom(Nb - m, k) / _binom(Nb, k)
            ab = [GA.mul(_prod([Ks] * a, sq), _prod([K] * c, sq), sq) for a in range(3) for c in range(3) if a != c]
            assert all(E(x) == 0 for x in ab)
            if Nb >= 2:
                assert E(GA.mul(_dag(b[0], sq), b[1], sq)) == F(k * (Nb - k), Nb * (Nb - 1))
                assert E(GA.mul(n[1], n[3], sq)) == F(k * (k - 1), Nb * (Nb - 1))
            psi = GA.mul(Ks, psi, sq)
    sq, v, w, n, b, K, Ks, P = _blocks(1)
    p0 = P.get((), F(0))
    assert p0 == F(1, 4)
    for r in range(5):
        for bl in itertools.combinations(range(4), r):
            X = {bl: F(1)}
            lam = GA.mul(P, X, sq).get((), F(0)) / p0
            assert GA.eq(_prod([P, X, P], sq), GA.scal(lam, P))
    return True


def check_limit_moments_are_not_quasi_free():
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    for k in range(1, 41):
        assert _ff(2, 2) * k * k - _ff(k, 2) == k * (k + 1)
        assert _ff(k, k + 1) == 0
        assert _ff(k + 1, k + 1) * k ** (k + 1) - _ff(k, k + 1) == _rf(1, k + 1) * k ** (k + 1)
        assert [_ff(k, m) for m in range(4)] == [1, k, k * k - k, k ** 3 - 3 * k * k + 2 * k]
    assert [_ff(0, m) for m in range(1, 5)] == [0, 0, 0, 0]
    return True
