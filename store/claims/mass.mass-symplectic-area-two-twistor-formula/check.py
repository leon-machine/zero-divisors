"""mass.mass-symplectic-area-two-twistor-formula: exact checks over the Gaussian rationals (GA.QI).

Spinors pi are pairs of GA.QI; the momentum of a system is p_{AA'} = sum_i pi^i_A conj(pi^i)_{A'}
(a 2x2 Hermitian matrix: on the real slice the primed indices carry the conjugate spinor), and
p^2 = eps^{AB} eps^{A'B'} p_{AA'} p_{BB'} is formed by the epsilon contraction, never through det.
  (1) a single spinor has p^2 = 0 (null, massless) on every sample;
  (2) two spinors have p^2 = 2 |<pi1 pi2>|^2 exactly, real, on every pair of 7 samples, and the
      identity behind it, p = A A^dagger with A = [pi1 pi2] (Cauchy-Binet), det p = |det A|^2;
  (3) aligned spinors (pi2 = c pi1) give a null composite, and along pi2 = pi1 + t eta the mass
      is 2 t^2 |<pi1 eta>|^2, strictly increasing in |t| (mass grows with the misalignment).
The claim has no premises (no derivation uses), so no premise() call is made.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (no premises declared)

Q0 = GA.qi(0)
SPINORS = [
    [GA.qi(1), GA.qi(0)],
    [GA.qi(0), GA.qi(1)],
    [GA.qi(2, 1), GA.qi(1, -1)],
    [GA.qi(1, 3), GA.qi(-2, 1)],
    [GA.qi(1, 2), GA.qi(3, 5)],
    [GA.qi(F(1, 2), F(-1, 3)), GA.qi(4, F(2, 7))],
    [GA.qi(-3, 0), GA.qi(0, F(5, 4))],
]
ETAS = [[GA.qi(0), GA.qi(1)], [GA.qi(1, 1), GA.qi(-2, 3)]]
CS = [GA.qi(3), GA.qi(F(-1, 2), 2), GA.qi(0, 1)]


def eps2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def momentum(spinors):
    p = [[Q0, Q0], [Q0, Q0]]
    for s in spinors:
        for A in range(2):
            for Ap in range(2):
                p[A][Ap] = p[A][Ap] + s[A] * s[Ap].conj()
    return p


def p_squared(p):
    eps = ((0, 1, 1), (1, 0, -1))
    tot = Q0
    for A, B, s1 in eps:
        for Ap, Bp, s2 in eps:
            tot = tot + GA.qi(s1 * s2) * p[A][Ap] * p[B][Bp]
    return tot


def check_single_spinor_is_null():
    ok = all(p_squared(momentum([s])) == Q0 for s in SPINORS)
    # the momentum of one spinor is Hermitian and nonzero (a genuine null vector)
    for s in SPINORS:
        p = momentum([s])
        ok = ok and all(p[A][B] == p[B][A].conj() for A in range(2) for B in range(2))
        ok = ok and (p[0][0] + p[1][1]).re > 0
    GA.check("a single spinor carries null Hermitian momentum", ok)
    assert ok


def check_two_spinor_mass_is_symplectic_area():
    ok = True
    for i in range(len(SPINORS)):
        for j in range(i + 1, len(SPINORS)):
            s1, s2 = SPINORS[i], SPINORS[j]
            p = momentum([s1, s2])
            m2 = p_squared(p)
            br = eps2(s1, s2)
            ok = ok and m2 == GA.qi(2) * br * br.conj() and m2.im == 0
            # the identity behind it: p = A A^dagger (A = [pi1 pi2]) and det p = |det A|^2
            A = [[s1[0], s2[0]], [s1[1], s2[1]]]
            AAd = [[sum((A[r][k] * A[c][k].conj() for k in range(2)), Q0) for c in range(2)] for r in range(2)]
            ok = ok and AAd == p
            detp = p[0][0] * p[1][1] - p[0][1] * p[1][0]
            ok = ok and m2 == GA.qi(2) * detp and detp == br * br.conj()
    # hand value: pi1 = (1,0), pi2 = (0,1): p = identity, <pi1 pi2> = 1, m^2 = 2
    ok = ok and p_squared(momentum([SPINORS[0], SPINORS[1]])) == GA.qi(2)
    # hand value: pi1 = (2+i, 1-i), pi2 = (1+3i, -2+i): <> = (2+i)(-2+i) - (1-i)(1+3i) = -9 - 2i, m^2 = 2*85
    ok = ok and eps2(SPINORS[2], SPINORS[3]) == GA.qi(-9, -2)
    ok = ok and p_squared(momentum([SPINORS[2], SPINORS[3]])) == GA.qi(170)
    GA.check("two spinors: m^2 = p^2 = 2 |<pi1 pi2>|^2", ok)
    assert ok


def check_aligned_null_and_mass_grows_with_misalignment():
    ok = True
    for s in SPINORS:
        for c in CS:
            s2 = [c * s[0], c * s[1]]
            ok = ok and eps2(s, s2) == Q0 and p_squared(momentum([s, s2])) == Q0
    for s in SPINORS[:4]:
        for eta in ETAS:
            b = eps2(s, eta)
            vals = []
            for t in range(0, 4):
                s2 = [s[0] + GA.qi(t) * eta[0], s[1] + GA.qi(t) * eta[1]]
                m2 = p_squared(momentum([s, s2]))
                ok = ok and m2 == GA.qi(2 * t * t) * b * b.conj()
                vals.append(m2.re)
            if b != Q0:
                ok = ok and vals[0] == 0 and all(vals[k] < vals[k + 1] for k in range(3))
    GA.check("aligned spinors are null; mass grows with the misalignment", ok)
    assert ok
