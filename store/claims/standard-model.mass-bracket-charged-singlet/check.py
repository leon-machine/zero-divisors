"""standard-model.mass-bracket-charged-singlet: exact checks over the Gaussian rationals (GA.QI), ported
from legacy verify_T12.py (prop:singlet) and widened (12 exact unitaries, 6 spinor pairs, the derivation
action of the hypercharge generator built from its matrix).

Two spinors pi^1, pi^2 are mixed by their slot index, pi'^i = sum_j U_ij pi^j, U in U(2). Exact unitaries:
rotations and phases from Pythagorean triples, their products, and the scalar phase lam I (lam =
(3+4i)/5).
  (1) <pi'^1 pi'^2> = det(U) <pi^1 pi^2> for every U and pair; SU(2) elements (det 1) fix it; the scalar
      phase lam I multiplies it by lam^2 (charge two), det(lam I) = lam^2.
  (2) Its modulus is the mass: the total momentum and m^2 = 2|<pi1 pi2>|^2 (the premise's formula, p^2 by
      epsilon contraction) are U(2)-invariant; the phase is pure gauge (a diagonal unitary makes the
      bracket real positive); the bracket vanishes exactly on the massless locus (p^2 = 0).
  (3) Hypercharge (the U(1) generator of the global form, X = 3i on C^2 and -2i on C^3, Y = q/6): its
      derivation action on Lambda^2 C^2 is multiplication by 6i (weight 6, Y = +1), the colour factor is
      Lambda^0 C^3 (weight 0), the class satisfies the Z_6 lattice condition 2t + 3 delta + q = 0 mod 6
      with t = delta = 0, and no weak doublet Lambda^1 C^2 (x) Lambda^k C^3 has weight 6: the quantum
      numbers are those of e^c.
The hypercharge assignment (X and Y = q/6) is the global form of standard-model.global-form-quotient-
determined, which this claim's derivation does not list, so (3) makes no premise() call; the declared
premise standard-model.imported-pair-systems-two-chirality-halves (spinors as pair-system vacua) has no
computable role in these identities and is not called.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

Q0, Q1 = GA.qi(0), GA.qi(1)
SPINORS = [[GA.qi(1), GA.qi(0)], [GA.qi(1, 1), GA.qi(2)], [GA.qi(2, -1), GA.qi(F(1, 3), 1)],
           [GA.qi(0), GA.qi(1)], [GA.qi(-1, 2), GA.qi(3, F(1, 2))]]
PAIRS = [(SPINORS[i], SPINORS[j]) for i in range(len(SPINORS)) for j in range(i + 1, len(SPINORS))][:6]
LAM = GA.qi(F(3, 5), F(4, 5))
R1 = [[GA.qi(F(3, 5)), GA.qi(F(4, 5))], [GA.qi(F(-4, 5)), GA.qi(F(3, 5))]]
R2 = [[GA.qi(F(5, 13)), GA.qi(0, F(12, 13))], [GA.qi(0, F(12, 13)), GA.qi(F(5, 13))]]
P1 = [[GA.qi(F(3, 5), F(4, 5)), Q0], [Q0, Q1]]
P2 = [[GA.qi(F(8, 17), F(15, 17)), Q0], [Q0, GA.qi(F(8, 17), F(-15, 17))]]
SCALAR = [[LAM, Q0], [Q0, LAM]]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(2)), Q0) for j in range(2)] for i in range(2)]


UNITARIES = [R1, R2, P1, P2, SCALAR, mm(R1, P1), mm(P2, R2), mm(R2, SCALAR), mm(mm(R1, R2), P2),
             mm(P1, mm(R2, R1)), mm(SCALAR, SCALAR), mm(P2, P1)]


def eps2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def det2(U):
    return U[0][0] * U[1][1] - U[0][1] * U[1][0]


def mix(U, s1, s2):
    return [[U[i][0] * s1[A] + U[i][1] * s2[A] for A in range(2)] for i in range(2)]


def momentum(sp):
    return [[sum((s[A] * s[B].conj() for s in sp), Q0) for B in range(2)] for A in range(2)]


def p_squared(p):
    tot = Q0
    for A, B, s1 in ((0, 1, 1), (1, 0, -1)):
        for Ap, Bp, s2 in ((0, 1, 1), (1, 0, -1)):
            tot = tot + GA.qi(s1 * s2) * p[A][Ap] * p[B][Bp]
    return tot


def check_bracket_transforms_by_determinant():
    ok = True
    for U in UNITARIES:
        Ud = [[U[j][i].conj() for j in range(2)] for i in range(2)]
        ok = ok and mm(U, Ud) == [[Q1, Q0], [Q0, Q1]]
        for s1, s2 in PAIRS:
            t1, t2 = mix(U, s1, s2)
            ok = ok and eps2(t1, t2) == det2(U) * eps2(s1, s2)
    # SU(2): det R1 = det R2 = 1 fix the bracket; the scalar phase has det lam^2
    ok = ok and det2(R1) == Q1 and det2(R2) == Q1 and det2(SCALAR) == LAM * LAM
    s1, s2 = PAIRS[1]
    t1, t2 = mix(SCALAR, s1, s2)
    ok = ok and eps2(t1, t2) == LAM * LAM * eps2(s1, s2) and LAM * LAM == GA.qi(F(-7, 25), F(24, 25))
    GA.check("the mass bracket transforms by det U: SU(2) singlet, charge 2 under the scalar phase", ok)
    assert ok


def check_modulus_is_mass_phase_is_gauge():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    ok = True
    for U in UNITARIES:
        for s1, s2 in PAIRS:
            t = mix(U, s1, s2)
            ok = ok and momentum(t) == momentum([s1, s2])
            b, bt = eps2(s1, s2), eps2(*t)
            ok = ok and bt * bt.conj() == b * b.conj()
            ok = ok and p_squared(momentum(t)) == GA.qi(2) * bt * bt.conj()
    # pure gauge phase: b = <(2+i, 1)... chosen with |b| = 5: b = 3 + 4i, U = diag(conj(b)/5, 1)
    s1, s2 = [GA.qi(3, 4), Q0], [Q0, Q1]
    b = eps2(s1, s2)
    U = [[b.conj() / GA.qi(5), Q0], [Q0, Q1]]
    ok = ok and b == GA.qi(3, 4) and eps2(*mix(U, s1, s2)) == GA.qi(5)
    # zero exactly on the massless locus
    for s1, s2 in PAIRS + [(SPINORS[1], [GA.qi(2) * c for c in SPINORS[1]])]:
        ok = ok and ((eps2(s1, s2) == Q0) == (p_squared(momentum([s1, s2])) == Q0))
    GA.check("modulus is the mass, phase pure gauge, zero exactly when massless", ok)
    assert ok


def check_hypercharge_weight_six_singlet():
    premise("standard-model.global-form-quotient-determined")
    X = [[GA.qi(0, 3), Q0], [Q0, GA.qi(0, 3)]]
    e = [[Q1, Q0], [Q0, Q1]]

    def wedge(u, v):
        return u[0] * v[1] - u[1] * v[0]

    def apply(M, v):
        return [M[i][0] * v[0] + M[i][1] * v[1] for i in range(2)]

    # derivation action on Lambda^2 C^2: X(e1 ^ e2) = X e1 ^ e2 + e1 ^ X e2
    act = wedge(apply(X, e[0]), e[1]) + wedge(e[0], apply(X, e[1]))
    q_weight = act.im
    ok = act.re == 0 and q_weight == 6 and F(q_weight, 6) == 1
    # SU(2) acts on Lambda^2 C^2 by det = 1 (singlet); colour factor Lambda^0 C^3 has weight 0
    ok = ok and det2(R1) == Q1 and det2(R2) == Q1
    t, delta = 0, 0
    ok = ok and (2 * t + 3 * delta + q_weight) % 6 == 0
    # weights of Lambda^j C^2 (x) Lambda^k C^3 are 3j - 2k: weight 6 occurs only at (j, k) = (2, 0)
    hits = [(j, k) for j in range(3) for k in range(4) if 3 * j - 2 * k == q_weight]
    ok = ok and hits == [(2, 0)]
    GA.check("the bracket is (1,1) with abelian weight 6, Y = +1: e^c, not a doublet", ok)
    assert ok
