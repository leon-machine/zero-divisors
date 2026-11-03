"""Exact checks: thermality of the future halves of a horizon generator about every point fixes the period 2 pi
and the null vacuum.

Generator CAR algebra over L^2(R, du) (x) K; boost about a: psi(u) -> e^(t/2) psi(a + e^t (u - a)) (weight 1/2).
(1) Affine maps: dilations about two distinct points compose to a translation, D_a(l) o D_b(1/l) = T((l - 1)(b - a)).
(2) The null vacuum kernel w(u, v) = 1/(u - v) is translation invariant and weight-1/2 dilation invariant about
    every point: l w(a + l(u - a), a + l(v - a)) = w(u, v).
(3) The I-state kernel at period beta about a, (XY)^(-1/2)/sinh(c s), c = pi/beta, X = u - a, Y = v - a,
    s = ln(X/Y): with E = e^s, X = dE/(E - 1), Y = d/(E - 1), d = X - Y, so XY = d^2 E/(E - 1)^2 and the kernel is
    2 sinh(s/2)/(d sinh(c s)). At c = 1/2 (beta = 2 pi) it is 2/d = 2/(u - v) for every E; at c = 1/4, 3/4, 1,
    3/2, 2 it changes with E at fixed d, so it is not translation invariant (E = q^4, all values rational).
(4) The Fermi transform's residue series: sum_{n >= 0} r^(2n+1) = r/(1 - r^2) = 1/(r^-1 - r), r = e^(-pi x/beta),
    i.e. 1/(2 sinh(pi x/beta)): partial sums with exact remainder r^(2N+1)/(1 - r^2).
(5) A set of points bounded below does not suffice: a symbol equal to the vacuum's compression on [b, oo) and
    arbitrary below b has the vacuum's compressions on every [a, oo), a >= b, and differs from it (finite model).
"""
from fractions import Fraction as Fr
import GA
from tp_premise import premise


def affine(lam, centre):
    """x -> centre + lam (x - centre) as the pair (slope, offset)."""
    return (lam, centre - lam * centre)


def compose(f, g):
    """(f o g)(x) = f(g(x)) for affine pairs (slope, offset)."""
    return (f[0] * g[0], f[0] * g[1] + f[1])


def check_two_dilation_groups_generate_translations():
    premise("hawking.i-state-continuum")
    for a, b in ((Fr(0), Fr(1)), (Fr(-3), Fr(2, 5)), (Fr(7, 2), Fr(-1, 3))):
        for lam in (Fr(2), Fr(1, 3), Fr(5, 4)):
            m = compose(affine(lam, a), affine(1 / lam, b))
            assert m[0] == 1
            assert m[1] == (lam - 1) * (b - a)
            assert m[1] != 0                           # a genuine translation when a != b, lam != 1
    return True


SAMPLE_UV = ((Fr(3), Fr(1)), (Fr(5, 2), Fr(-7, 3)), (Fr(11), Fr(10)))
CENTRES = (Fr(-4), Fr(0), Fr(1, 2), Fr(9))
FACTORS = (Fr(2), Fr(3, 7), Fr(13, 5))
SHIFTS = (Fr(1), Fr(-5, 2))


def check_null_vacuum_kernel_is_dilation_invariant_about_every_point():
    premise("hawking.i-state-continuum")
    n = 0
    for (u, v) in SAMPLE_UV:
        w = 1 / (u - v)
        for a in CENTRES:
            for lam in FACTORS:
                uu = a + lam * (u - a)
                vv = a + lam * (v - a)
                # weight 1/2 on each leg: lam^(1/2) lam^(1/2) = lam
                assert lam ** (2 * Fr(1, 2)) * (1 / (uu - vv)) == w
                n += 1
        for t in SHIFTS:
            assert 1 / ((u + t) - (v + t)) == w           # translation invariant
    assert n == 36
    return True


def sinh_q(q, k):
    """sinh(k s/4) for e^s = q^4: (q^k - q^-k)/2."""
    return (q ** k - q ** (-k)) / 2


def i_state_kernel(q, d, k):
    """(XY)^(-1/2)/sinh(c s) with c = k/4, e^s = E = q^4, X = d E/(E - 1), Y = d/(E - 1)."""
    E = q ** 4
    X = d * E / (E - 1)
    Y = d / (E - 1)
    assert X - Y == d
    assert X * Y == d * d * E / (E - 1) ** 2
    root = d * q * q / (E - 1)                        # (XY)^(1/2), with sqrt(E) = q^2
    assert root * root == X * Y
    return 1 / (root * sinh_q(q, k))


def check_only_period_two_pi_is_translation_invariant():
    premise("hawking.i-state-continuum")
    premise("hawking.imported-ideal-fermi-gas-uniqueness")
    qs = (Fr(2), Fr(3), Fr(5, 2), Fr(7, 3))
    for d in (Fr(1), Fr(3, 2)):
        # beta = 2 pi (c = 1/2, k = 2): the kernel is 2/d whatever the position
        for q in qs:
            assert i_state_kernel(q, d, 2) == 2 / d
        # other periods: the kernel moves with the position at fixed separation d
        for k in (1, 3, 4, 6, 8):
            vals = {i_state_kernel(q, d, k) for q in qs}
            assert len(vals) == len(qs)
    return True


def check_fermi_transform_residue_series():
    premise("hawking.i-state-continuum")
    for r in (Fr(1, 2), Fr(1, 3), Fr(4, 5)):
        target = 1 / (1 / r - r)
        assert r / (1 - r * r) == target
        s = Fr(0)
        for n in range(12):
            s += r ** (2 * n + 1)
            assert target - s == r ** (2 * n + 3) / (1 - r * r)
    return True


# a rational orthogonal projector of rank 3 on Q^6 standing for the vacuum symbol (finite model)
VS = ((Fr(1), Fr(1), Fr(0), Fr(1), Fr(0), Fr(1)),
      (Fr(1), Fr(-1), Fr(1), Fr(0), Fr(1), Fr(0)),
      (Fr(0), Fr(1), Fr(2), Fr(-1), Fr(0), Fr(1)))


def projector(vs):
    ortho = []
    for v in vs:
        w = list(v)
        for o in ortho:
            c = sum(x * y for x, y in zip(w, o)) / sum(x * x for x in o)
            w = [x - c * y for x, y in zip(w, o)]
        ortho.append(w)
    m = len(vs[0])
    return [[sum(o[i] * o[j] / sum(x * x for x in o) for o in ortho) for j in range(m)] for i in range(m)]


def check_points_bounded_below_do_not_suffice():
    premise("hawking.imported-ideal-fermi-gas-uniqueness")
    n = 6
    P = projector(VS)
    assert GA.mat_eq(GA.mat_mul(P, P), P)
    assert sum(P[i][i] for i in range(n)) == 3          # rank 3
    b = 3                                              # sites >= b form the half-line [b, oo)
    T = [[P[i][j] if (i >= b and j >= b) else (Fr(1, 2) if i == j else Fr(0)) for j in range(n)]
         for i in range(n)]
    agree = [a for a in range(n) if all(T[i][j] == P[i][j] for i in range(a, n) for j in range(a, n))]
    assert agree == [3, 4, 5]                          # same compression exactly on [a, oo), a >= b
    diff = sum(1 for i in range(n) for j in range(n) if T[i][j] != P[i][j])
    assert diff == 27                                  # every entry touching a site below b
    # the state below b is a valid symbol, (1/2) id, uncorrelated with the half-line: T - T^2 = (1/4) id there
    for i in range(b):
        for j in range(n):
            tt = sum(T[i][k] * T[k][j] for k in range(n))
            assert T[i][j] - tt == (Fr(1, 4) if i == j else 0)
    return True


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("check_"):
            print(name, fn())
