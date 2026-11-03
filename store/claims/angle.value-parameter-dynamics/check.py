"""angle.value-parameter-dynamics: exact checks.

Two fermionic modes in the Jordan-Wigner basis |n0 n1> (index n0 + 2 n1), H = eps N0 - t (a0^dag a1 + a1^dag a0).
(1) At the seven sample points of the proof, (c, s) = (3/5, 4/5), (5/13, 12/13), (8/17, 15/17), (7/25, 24/25),
    (24/25, 7/25), (-3/5, -4/5) at t = 60 and (3/5, -4/5) at t = -60: eps = t (s^2 - c^2)/(c s) against
    hand-tabulated values, c|10> + s|01> an eigenvector with eigenvalue -t c/s (tabulated), the other
    eigenvalues 0, eps and t s/c above it with the three gaps t s/c + t c/s, t c/s, t s/c positive, the four
    eigenvectors a basis (so the ground state is unique), and the left marginal diag(s^2, c^2), Gibbs for N0 at
    q = c^2/s^2 (tabulated).
(2) The gap identities as polynomial identities: on a grid of (c, s, t) the gaps equal t(c^2 + s^2)/(c s),
    t c/s, t s/c, so all are positive exactly when t c s > 0 (sign table on the grid).
(3) The determination clause, in its corrected form: with r = c/s, eps/t = 1/r - r, so r is a root of
    r^2 + (eps/t) r - 1 = 0, whose roots have product -1; the root is the one with the sign of t (t c s > 0), and
    q = r^2. Hence q is fixed by eps/t together with the sign of t, but not by eps/t alone: (c, s) = (4/5, 3/5)
    at t = 60 and (3/5, -4/5) at t = -60 share eps/t = -7/12 and have q = 16/9 and 9/16. (Reported: the formal
    statement's last sentence and the proof's "positive root" hold for t > 0 only.)
"""
from fractions import Fraction as F

import GA
import fock

DIM = 4
POINTS = [((3, 5), (4, 5), 60), ((5, 13), (12, 13), 60), ((8, 17), (15, 17), 60), ((7, 25), (24, 25), 60),
          ((24, 25), (7, 25), 60), ((-3, 5), (-4, 5), 60), ((3, 5), (-4, 5), -60)]
GRID_CS = [(F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(8, 17), F(-15, 17)), (F(-7, 25), F(-24, 25))]
GRID_T = [F(60), F(-2), F(1, 3), F(-7, 4)]


def zero():
    return [[F(0)] * DIM for _ in range(DIM)]


mm = GA.mat_mul                         # dense matrix product


def madd(*ms):
    return [[sum(m[i][j] for m in ms) for j in range(DIM)] for i in range(DIM)]


def msc(c, a):
    return [[F(c) * a[i][j] for j in range(DIM)] for i in range(DIM)]


def tr(a):
    return [[a[j][i] for j in range(DIM)] for i in range(DIM)]


def mv(a, v):
    return [sum(a[i][k] * v[k] for k in range(DIM)) for i in range(DIM)]


def ann(j):
    """a_j in the Jordan-Wigner basis (index n0 + 2 n1), dense: lib/fock.py in LSB order."""
    return fock.to_dense(fock.ann(j, 2), DIM)


A0, A1 = ann(0), ann(1)
C0, C1 = tr(A0), tr(A1)
N0 = mm(C0, A0)
HOP = madd(mm(C0, A1), mm(C1, A0))


def ham(eps, t):
    return madd(msc(eps, N0), msc(-t, HOP))


def check_ground_state_eigenvalue_and_marginal():
    expected = [(F(35), F(-45), F(9, 16)), (F(119), F(-25), F(25, 144)), (F(161, 2), F(-32), F(64, 225)),
                (F(2635, 14), F(-35, 2), F(49, 576)), (F(-2635, 14), F(-1440, 7), F(576, 49)),
                (F(35), F(-45), F(9, 16)), (F(35), F(-45), F(9, 16))]
    ok = len(expected) == len(POINTS)
    for (cc, ss, tt), (eps_x, lam_x, q_x) in zip(POINTS, expected):
        c, s, t = F(*cc), F(*ss), F(tt)
        ok = ok and c * c + s * s == 1 and t * c * s > 0
        eps = t * (s * s - c * c) / (c * s)
        ok = ok and eps == eps_x
        H = ham(eps, t)
        psi = [F(0), c, s, F(0)]
        lam = -t * c / s
        ok = ok and lam == lam_x and mv(H, psi) == [lam * x for x in psi]
        other = [F(0), s, -c, F(0)]
        top = t * s / c
        ok = ok and mv(H, other) == [top * x for x in other]
        vac, both = [F(1), F(0), F(0), F(0)], [F(0), F(0), F(0), F(1)]
        ok = ok and mv(H, vac) == [F(0)] * DIM and mv(H, both) == [eps * x for x in both]
        ok = ok and GA.field_rank([vac, both, psi, other]) == 4
        ok = ok and top - lam > 0 and 0 - lam > 0 and eps - lam > 0
        n0 = sum(psi[i] * mv(N0, psi)[i] for i in range(DIM))
        ok = ok and (1 - n0, n0) == (s * s, c * c) and n0 / (1 - n0) == q_x
    _tp_rv = (ok); assert _tp_rv is not False, "check_ground_state_eigenvalue_and_marginal"; return _tp_rv


def check_gap_identities_and_sign_condition():
    ok = True
    positive = 0
    for c, s in GRID_CS:
        for t in GRID_T:
            eps = t * (s * s - c * c) / (c * s)
            lam = -t * c / s
            gaps = (eps - lam - lam, 0 - lam, eps - lam)            # other eigenvalue is eps - lam
            ok = ok and gaps == (t * (c * c + s * s) / (c * s), t * c / s, t * s / c)
            allpos = all(g > 0 for g in gaps)
            ok = ok and allpos == (t * c * s > 0)
            positive += allpos
    _tp_rv = (ok and positive == 8); assert _tp_rv is not False, "check_gap_identities_and_sign_condition"; return _tp_rv


def check_gibbs_parameter_fixed_by_ratio_and_sign_of_t():
    ok = True
    for (cc, ss, tt) in POINTS:
        c, s, t = F(*cc), F(*ss), F(tt)
        ratio = (s * s - c * c) / (c * s)
        r = c / s
        ok = ok and r * r + ratio * r - 1 == 0
        # the other root is -1/r: product of the roots is -1, so exactly one has the sign of t
        r2 = -1 / r
        ok = ok and r2 * r2 + ratio * r2 - 1 == 0 and r * r2 == -1
        ok = ok and (r > 0) == (t > 0) and (r2 > 0) != (t > 0)
    # counterexample to "fixed by eps/t alone": same ratio, opposite signs of t, different q
    c1, s1, t1 = F(4, 5), F(3, 5), F(60)
    c2, s2, t2 = F(3, 5), F(-4, 5), F(-60)
    e1 = t1 * (s1 * s1 - c1 * c1) / (c1 * s1)
    e2 = t2 * (s2 * s2 - c2 * c2) / (c2 * s2)
    ok = ok and e1 / t1 == e2 / t2 == F(-7, 12)
    ok = ok and (c1 / s1) ** 2 == F(16, 9) and (c2 / s2) ** 2 == F(9, 16)
    ok = ok and (e1, e2) == (F(-35), F(35))
    _tp_rv = (ok); assert _tp_rv is not False, "check_gibbs_parameter_fixed_by_ratio_and_sign_of_t"; return _tp_rv
