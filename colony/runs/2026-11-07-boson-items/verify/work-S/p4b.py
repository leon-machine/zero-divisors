"""synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes: exact checks.

A tower level Cl(N, N+2): kernel generators g1 = gen(0), g2 = gen(1) (square -1), J = g1 g2; plane j has
e_j = gen(2 + 2j) (square +1), f_j = gen(3 + 2j) (square -1), v_j = (e_j + f_j)/2 = a*_j, w_j = (e_j - f_j)/2 = a_j,
n_j = v_j w_j, omega_j = e_j f_j, Gamma = prod_j omega_j. * is the CAR adjoint (reversion, a sign per negative-square
generator). A spin assignment s = (s_j), s_j in (1/2)Z, gives U(m pi) = prod_j (1 - n_j + exp(m pi J s_j) n_j), with
exp(m pi J s) = cos + J sin at a multiple of pi/2 (values 1, J, -1, -J).
(1) n_j = (1 - omega_j)/2; for N = 1, 2, 3 and every s in {-1/2, 0, 1/2, 1, 3/2}^N: U(pi)^2 = U(2 pi), U(pi) unitary
    and commuting with J, U(pi) w_j U(pi)* = exp(-pi J s_j) w_j, U(pi) v_j U(pi)* = exp(pi J s_j) v_j, and
    U(2 pi) = prod of omega_j over the half-integer s_j.
(2) Ad U(2 pi) = Ad Gamma on every mode exactly when every s_j is half-integer (N = 1, 2, 3, all assignments
    above); with all s_j = 1/2, U(2 pi) = Gamma; then every hopping, pairing and density element is 2 pi invariant
    and every mode is negated.
(3) Blocks (lower spin 1/2, upper spin 0), N_b = 1, 2, 3: each hopping element b = v_lower w_upper is negated
    by Ad U(2 pi); hopping elements and adjoints of distinct blocks commute; each upper mode is 2 pi invariant and
    anticommutes with the other modes; on (B*)^k P_pol, sum_i [b_i, b_i*] = N_b - 2k for k = 0..N_b and
    (B*)^(N_b + 1) P_pol = 0.
(4) J commutes with every plane generator (N = 1, 2), so Ad exp(phi J) fixes the transport algebra; the real
    rotation L = v_0 w_1 - v_1 w_0 equals (e_0 e_1 - f_0 f_1)/2, a sum of two commuting bivectors of square -1;
    [L, w_0 +- J w_1] = +-J (w_0 +- J w_1) (weights +-1); exp(pi L) = (e_0 e_1)(-f_0 f_1) = omega_0 omega_1 negates
    both modes and exp(2 pi L) = 1.
"""
from fractions import Fraction as F
import itertools

import GA
from tp_premise import premise


def _sq(N):
    return tuple([-1, -1] + [1, -1] * N)


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


def _setup(N):
    sq = _sq(N)
    J = GA.mul(GA.gen(0), GA.gen(1), sq)
    e = [GA.gen(2 + 2 * j) for j in range(N)]
    f = [GA.gen(3 + 2 * j) for j in range(N)]
    v = [GA.scal(F(1, 2), GA.add(e[j], f[j])) for j in range(N)]
    w = [GA.scal(F(1, 2), GA.sub(e[j], f[j])) for j in range(N)]
    n = [GA.mul(v[j], w[j], sq) for j in range(N)]
    om = [GA.mul(e[j], f[j], sq) for j in range(N)]
    return sq, J, e, f, v, w, n, om


def _phase(m, s, J):
    t = (2 * m * s) % 4
    return [GA.sc(1), J, GA.sc(-1), GA.neg(J)][int(t)]


def _U(m, spins, n, J, sq):
    return _prod([GA.add(GA.sub(GA.sc(1), nj), GA.mul(_phase(m, s, J), nj, sq)) for s, nj in zip(spins, n)], sq)


def _ad(u, x, sq):
    return GA.mul(GA.mul(u, x, sq), _dag(u, sq), sq)


SPINS = [F(1, 2), F(0), F(-1, 2), F(1), F(3, 2)]


def check_two_pi_rotation_is_the_product_of_half_integer_plane_volumes():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("tower.volume-elements-planes")
    premise("std-algebra.bivector-exponential")
    for N in (1, 2, 3):
        sq, J, e, f, v, w, n, om = _setup(N)
        assert all(GA.eq(GA.add(GA.mul(v[i], w[j], sq), GA.mul(w[j], v[i], sq)), GA.sc(1 if i == j else 0))
                  for i in range(N) for j in range(N))
        assert all(GA.eq(n[j], GA.scal(F(1, 2), GA.sub(GA.sc(1), om[j]))) for j in range(N))
        for spins in itertools.product(SPINS, repeat=N):
            U1 = _U(1, spins, n, J, sq)
            U2 = _U(2, spins, n, J, sq)
            assert GA.eq(GA.mul(U1, U1, sq), U2)
            assert GA.eq(GA.mul(_dag(U1, sq), U1, sq), GA.sc(1)) and GA.commutes(U1, J, sq)
            assert all(GA.eq(_ad(U1, w[j], sq), GA.mul(_phase(-1, spins[j], J), w[j], sq)) for j in range(N))
            assert all(GA.eq(_ad(U1, v[j], sq), GA.mul(_phase(1, spins[j], J), v[j], sq)) for j in range(N))
            half = [om[j] for j in range(N) if spins[j].denominator == 2]
            assert GA.eq(U2, _prod(half, sq))
    return True


def check_spin_statistics_holds_exactly_when_every_mode_is_half_integer():
    premise("tower.volume-elements-planes")
    count = 0
    for N in (1, 2, 3):
        sq, J, e, f, v, w, n, om = _setup(N)
        Gam = _prod(om, sq)
        for spins in itertools.product(SPINS, repeat=N):
            U2 = _U(2, spins, n, J, sq)
            same = all(GA.eq(_ad(U2, x, sq), _ad(Gam, x, sq)) for x in v + w)
            allhalf = all(s.denominator == 2 for s in spins)
            assert same == allhalf
            count += 1 if same else 0
        U2 = _U(2, [F(1, 2)] * N, n, J, sq)
        assert GA.eq(U2, Gam)
        pairs = [GA.mul(v[i], w[j], sq) for i in range(N) for j in range(N)] + \
                [GA.mul(w[i], w[j], sq) for i in range(N) for j in range(N)]
        assert all(GA.eq(_ad(U2, x, sq), x) for x in pairs)
        assert all(GA.eq(_ad(U2, x, sq), GA.neg(x)) for x in v + w)
    # all-half-integer assignments among the 5 + 25 + 125 tried: 3 + 9 + 27
    assert count == 39
    return True


def check_half_integer_spin_boson_from_a_spinor_and_a_scalar_mode():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    for Nb in (1, 2, 3):
        sq, J, e, f, v, w, n, om = _setup(2 * Nb)
        spins = [F(1, 2), F(1, 2)] * Nb
        U2 = _U(2, spins, n, J, sq)
        b = [GA.mul(v[2 * i], w[2 * i + 1], sq) for i in range(Nb)]
        assert all(GA.eq(_ad(U2, x, sq), GA.neg(x)) for x in b)
        assert all(GA.commutes(b[i], y, sq) for i in range(Nb) for j in range(Nb) if j != i
                  for y in (b[j], _dag(b[j], sq)))
        up = [w[2 * i + 1] for i in range(Nb)]
        assert all(GA.eq(_ad(U2, x, sq), x) for x in up)
        assert all(GA.anticommutes(up[0], y, sq) for y in w[1:] + v[2:])
        Bs = GA.add(*[_dag(x, sq) for x in b])
        Bc = GA.add(*b)
        C = GA.sub(GA.mul(Bc, Bs, sq), GA.mul(Bs, Bc, sq))
        P = _prod([GA.mul(n[2 * i], GA.sub(GA.sc(1), n[2 * i + 1]), sq) for i in range(Nb)], sq)
        x = P
        for k in range(Nb + 1):
            assert x != {} and GA.eq(GA.mul(C, x, sq), GA.scal(F(Nb - 2 * k), x))
            x = GA.mul(Bs, x, sq)
        assert x == {}
    return True


def check_rotations_of_the_level_itself_give_integer_spin():
    premise("std-algebra.bivector-exponential")
    for N in (1, 2):
        sq, J, e, f, v, w, n, om = _setup(N)
        assert GA.eq(GA.mul(J, J, sq), GA.sc(-1))
        assert all(GA.commutes(J, GA.gen(i), sq) for i in range(2, 2 + 2 * N))
    sq, J, e, f, v, w, n, om = _setup(2)
    L = GA.sub(GA.mul(v[0], w[1], sq), GA.mul(v[1], w[0], sq))
    B1 = GA.mul(e[0], e[1], sq)
    B2 = GA.mul(f[0], f[1], sq)
    assert GA.eq(L, GA.scal(F(1, 2), GA.sub(B1, B2)))
    assert GA.commutes(B1, B2, sq) and GA.eq(GA.mul(B1, B1, sq), GA.sc(-1)) and GA.eq(GA.mul(B2, B2, sq), GA.sc(-1))
    for sgn in (1, -1):
        y = GA.add(w[0], GA.scal(F(sgn), GA.mul(J, w[1], sq)))
        assert GA.eq(GA.sub(GA.mul(L, y, sq), GA.mul(y, L, sq)), GA.scal(F(sgn), GA.mul(J, y, sq)))
    R = GA.mul(B1, GA.neg(B2), sq)          # exp(pi L) = exp(pi B1/2) exp(-pi B2/2)
    assert GA.eq(R, GA.mul(om[0], om[1], sq))
    assert all(GA.eq(_ad(R, x, sq), GA.neg(x)) for x in w + v)
    assert GA.eq(GA.mul(R, R, sq), GA.sc(1))
    return True
