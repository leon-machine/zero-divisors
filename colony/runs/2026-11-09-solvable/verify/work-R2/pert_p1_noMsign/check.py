"""synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays: exact checks.

Window modes as in the exact window Sugawara result: plane j has e_j = gen(2 + 2j) (square +1),
f_j = gen(3 + 2j) (square -1), v_j = (e_j + f_j)/2 the creator, w_j = (e_j - f_j)/2 the annihilator,
n_j = v_j w_j; the kernel g1 = gen(0), g2 = gen(1) (squares -1) gives J = g1 g2, J^2 = -1, commuting with every
plane generator. On a window of L = 2M planes the level k = j - M has weight k + 1/2, the sea k < 0 is filled and
H = sum_k (k + 1/2) n_k + M^2/2. The one-window flow at Killing time 2 pi/kappa is e^{2 pi J H}; by the stored
factorisation e^{JtH} = e^{J t M^2/2} prod_k (1 + (e^{J t (k + 1/2)} - 1) n_k) it is computed with exact powers of
the quarter turn e^{pi J/2} = J. Phases that are not powers of J are computed as rotors c + s J with c, s in the
field Q(sqrt 2, sqrt 3) (class Q23 below, four rational components), so e^{2 pi J/24} is exact.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def _modes(L):
    s = tuple([-1, -1] + [1, -1] * L)
    mul = lambda x, y: GA.mul(x, y, s)
    e = [GA.gen(2 + 2 * j) for j in range(L)]
    f = [GA.gen(3 + 2 * j) for j in range(L)]
    v = [GA.scal(F(1, 2), GA.add(e[j], f[j])) for j in range(L)]
    w = [GA.scal(F(1, 2), GA.sub(e[j], f[j])) for j in range(L)]
    n = [mul(v[j], w[j]) for j in range(L)]
    J = mul(GA.gen(0), GA.gen(1))
    return s, mul, e, f, v, w, n, J


def _jpow(mul, J, m):
    """J^m for an integer m (J^{-1} = -J)."""
    base = J if m >= 0 else GA.neg(J)
    out = GA.sc(1)
    for _ in range(abs(m)):
        out = mul(out, base)
    return out


def _vac(mul, v, w):
    out = GA.sc(1)
    for j in range(len(v)):
        out = mul(out, mul(w[j], v[j]))
    return out


def _state(mul, v, vac, occ):
    st = vac
    for j in reversed(range(len(occ))):
        if occ[j]:
            st = mul(v[j], st)
    return st


def _occupations(L):
    for m in range(2 ** L):
        yield [(m >> j) & 1 for j in range(L)]


class Q23:
    """a + b sqrt2 + c sqrt3 + d sqrt6, exact."""

    def __init__(self, a=0, b=0, c=0, d=0):
        self.x = (F(a), F(b), F(c), F(d))

    def __add__(self, o):
        return Q23(*[p + q for p, q in zip(self.x, o.x)])

    def __sub__(self, o):
        return Q23(*[p - q for p, q in zip(self.x, o.x)])

    def __mul__(self, o):
        a, b, c, d = self.x
        p, q, r, t = o.x
        return Q23(a * p + 2 * b * q + 3 * c * r + 6 * d * t,
                   a * q + b * p + 3 * c * t + 3 * d * r,
                   a * r + c * p + 2 * b * t + 2 * d * q,
                   a * t + d * p + b * r + c * q)

    def __eq__(self, o):
        return self.x == o.x


def _rmul(x, y):
    """(c + s J)(c' + s' J) with J^2 = -1."""
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def _rpow(x, m):
    out = (Q23(1), Q23(0))
    for _ in range(m):
        out = _rmul(out, x)
    return out


ONE = (Q23(1), Q23(0))
# e^{2 pi J/24} = cos(pi/12) + J sin(pi/12), cos = (sqrt6 + sqrt2)/4, sin = (sqrt6 - sqrt2)/4
R24 = (Q23(0, F(1, 4), 0, F(1, 4)), Q23(0, F(-1, 4), 0, F(1, 4)))


NMAX = 96
NS = range(1, NMAX + 1)
GS = range(1, 13)
GS2 = range(1, 25)
RS = range(0, 49)


def _is_one(m):
    return _rpow(R24, m) == ONE


def check_one_window_flow_is_the_grading_on_every_window():
    premise("synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves")
    premise("std-algebra.witt-basis-car")
    ok = True
    for L in (2, 4):
        M = L // 2
        s, mul, e, f, v, w, n, J = _modes(L)
        ok = ok and GA.eq(mul(J, J), GA.sc(-1)) and all(GA.commutes(J, x, s) for x in e + f)
        U = _jpow(mul, J, 2 * M * M)                           # e^{J pi M^2}
        U0 = GA.sc(1)                                          # the zero offset, weights k
        for j in range(L):
            k = j - M
            U = mul(U, GA.add(GA.sc(1), mul(GA.sub(_jpow(mul, J, 2 * (2 * k + 1)), GA.sc(1)), n[j])))
            U0 = mul(U0, GA.add(GA.sc(1), mul(GA.sub(_jpow(mul, J, 4 * k), GA.sc(1)), n[j])))
        G = GA.sc(1)
        for j in range(L):
            G = mul(G, mul(e[j], f[j]))                        # (-1)^M prod_j e_j f_j
        ok = ok and GA.eq(U, G) and GA.eq(U0, GA.sc(1))
        ok = ok and GA.eq(mul(G, G), GA.sc(1)) and GA.commutes(G, J, s)
        ok = ok and all(GA.anticommutes(G, x, s) for x in v + w)
        vac = _vac(mul, v, w)
        H = GA.add(GA.sc(F(M * M, 2)), *[GA.scal(F(2 * (j - M) + 1, 2), n[j]) for j in range(L)])
        for occ in _occupations(L):
            st = _state(mul, v, vac, occ)
            h = F(M * M, 2) + sum(F(2 * (j - M) + 1, 2) * occ[j] for j in range(L))
            Q = sum(occ) - M
            ok = ok and GA.eq(mul(H, st), GA.scal(h, st))
            ok = ok and GA.eq(mul(G, st), GA.scal((-1) ** Q, st))
            ok = ok and (h - F(Q, 2)).denominator == 1 and h >= F(Q * Q, 2)
            if occ == [1] * M + [0] * M:
                ok = ok and h == 0 and Q == 0                  # the sea: H = 0, even
    GA.check("one-window flow e^{2 pi J H} = (-1)^M prod e_j f_j = (-1)^Q on windows L = 2, 4; identity at offset 0", ok)
    return ok


def _finite_part_hurwitz(a, N=4):
    """Finite part of sum_{n>=0} (n + a) e^{-eps (n + a)}: -c_2 with eps h_a(eps) = sum c_j eps^j."""
    ex = [F(1)]
    for j in range(1, N + 1):
        ex.append(ex[-1] * F(-a) / j)                          # e^{-eps a}
    den = [F(1)]
    for j in range(1, N + 1):
        den.append(den[-1] * F(-1) / (j + 1))                  # (1 - e^{-eps})/eps = sum (-eps)^j/(j+1)!
    c = GA.ps_mul(ex, GA.ps_inv(den, N), N)
    return -c[2]


def _b2(a):
    return a * a - a + F(1, 6)


def check_window_reading_zero_is_minus_one_twenty_fourth_per_array():
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")
    premise("synthesis.counted-unit-energy-at-half-offset")
    ok = True
    for a in (F(1, 2), F(1, 3), F(1, 4), F(2, 3), F(1, 5)):
        ok = ok and _finite_part_hurwitz(a) == -_b2(a) / 2
    half = F(1, 2)
    sea = -(_finite_part_hurwitz(half) + _finite_part_hurwitz(1 - half)) / 2   # symmetric sea, units of kappa
    ok = ok and sea == F(-1, 24)
    # equality with the null-ordered window value -1/24 exactly at delta = 1/2
    for d in (F(0), F(1, 2), F(1, 3), F(1, 4), F(3, 4), F(1, 6)):
        val = _b2(d) / 2
        ok = ok and val + F(1, 24) == (d - half) ** 2 / 2 and ((val == F(-1, 24)) == (d == half))
    # null-ordered energy of n arrays over one window, in units of kappa, on the sea: -n/24, so the flow's
    # eigen-angle over 2 pi on a window state is n/24 - h with h - Q/2 an integer
    for n in (1, 16, 24, 48):
        ok = ok and n * sea == F(-n, 24)
    GA.check("symmetric sea at the half offset is -kappa/24 per array (Hurwitz finite part), equal to the null-ordered value only at 1/2", ok)
    return ok


def check_joint_flow_is_the_parity_exactly_when_twenty_four_divides_the_array_count():
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    ok = True
    pw = [ONE]
    for _ in range(NMAX * 4):
        pw.append(_rmul(pw[-1], R24))                          # pw[m] = e^{2 pi J m/24}, computed, not reduced
    unit = lambda m: pw[m] == ONE
    c, sn = R24
    ok = ok and c * c + sn * sn == Q23(1)
    ok = ok and pw[6] == (Q23(0), Q23(1)) and pw[12] == (Q23(-1), Q23(0))   # e^{pi J/2} = J, e^{pi J} = -1
    # U = e^{2 pi J n/24} Gamma equals Gamma iff the phase is 1
    ok = ok and [n for n in NS if unit(n)] == [24, 48, 72, 96]
    # U^2 = e^{2 pi J n/12} is 1 iff 12 | n
    ok = ok and [n for n in NS if unit(2 * n)] == [12, 24, 36, 48, 60, 72, 84, 96]
    # sixteen arrays per generation: a phase of order 3
    gen = pw[16]
    ok = ok and gen != ONE and _rmul(_rmul(gen, gen), gen) == ONE
    ok = ok and [g for g in GS if unit(16 * g)] == [3, 6, 9, 12]
    # without the neutral singlet: fifteen per generation; at three generations, r singlets
    ok = ok and [g for g in GS2 if unit(15 * g)] == [8, 16, 24]
    ok = ok and [r for r in RS if unit(45 + r)] == [3, 27]
    GA.check("U = e^{2 pi J n/24} Gamma equals Gamma iff 24 | n; U^2 = 1 iff 12 | n; 16 n_g needs 3 | n_g, 15 n_g needs 8 | n_g", ok)
    return ok


def check_integer_weight_content_on_the_light_ray():
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    premise("synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators")
    ok = True
    # a complex CCR array, weights kappa (k + delta): symmetric zero point +1/2 sum |omega| = -B_2(delta)/2;
    # at delta = 0 the towers k >= 1 and k + 1 >= 1 give -1/12, a real component -1/24
    zeta_m1 = _finite_part_hurwitz(F(1))
    ok = ok and zeta_m1 == F(-1, 12)
    for d in (F(0), F(1, 2), F(1, 3), F(1, 4), F(2, 3)):
        zp = zeta_m1 if d == 0 else (_finite_part_hurwitz(d) + _finite_part_hurwitz(1 - d)) / 2
        ok = ok and zp == -_b2(d) / 2 and zp + F(1, 12) == d * (1 - d) / 2
        ok = ok and ((zp == F(-2, 24)) == (d == 0))
    ok = ok and zeta_m1 / 2 == F(-1, 24)
    # integer weights: the one-window flow on excitations is the identity, e^{2 pi J k} = J^{4k} = 1
    s, mul, e, f, v, w, n, J = _modes(2)
    ok = ok and all(GA.eq(_jpow(mul, J, 4 * k), GA.sc(1)) for k in range(-3, 4))
    ok = ok and not GA.eq(_jpow(mul, J, 2), GA.sc(1))
    # c_B real integer-weight components with 16 n_g arrays: U = Gamma iff 8 | c_B and n_g = c_B/8 mod 3
    for cb in range(0, 48):
        sols = [g for g in range(1, 13) if _is_one((16 * g + cb) % 24)]
        want = [g for g in range(1, 13) if cb % 8 == 0 and (g - cb // 8) % 3 == 0]
        ok = ok and sols == want
    ok = ok and [cb for cb in range(0, 48) if _is_one((48 + cb) % 24)] == [0, 24]
    ok = ok and [g for g in range(1, 13) if _is_one((16 * g + 8) % 24)] == [1, 4, 7, 10]
    GA.check("CCR arrays: zero point -B_2(delta)/2, null value only at delta = 0; SM integer-weight content fails for every n_g", ok)
    return ok
