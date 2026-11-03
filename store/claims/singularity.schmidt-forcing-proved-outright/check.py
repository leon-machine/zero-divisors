"""singularity.schmidt-forcing-proved-outright: exact checks over Q(i).

C^2 (x) C^2 with |ij> at index 2 i + j; the pair factor acts as A (x) 1; G = N (x) 1 - 1 (x) N.
(1) G is diagonal with eigenvalues (0, -1, +1, 0). At the exact unit-circle point u = e^{it} =
(3 + 4i)/5 (not a root of unity), e^{itG} = diag(1, conj(u), u, 1) has the three distinct eigenvalues
1, conj(u), u, so a vector is invariant up to phase under the group iff it lies in one eigenspace of
G. All 15 nonempty supports in the number basis are enumerated with generic Q(i) coefficients: the
invariant ones are exactly the 3 inside span{|00>, |11>} and the two product lines |01>, |10>.
(2) Cyclic and separating for the pair factor: the orbit {(A (x) 1) Omega} of a|00> + b|11> has
determinant a^2 b^2 (checked as a polynomial identity at samples), so it is cyclic and separating
iff ab != 0; the lines |01>, |10> have orbit rank 2 < 4. Among the 15 supports, only {|00>, |11>} is
both invariant and cyclic-separating.
(3) The phase convention: Omega = a|00> + b|11> with |a|^2 + |b|^2 = 1 equals e^{i phi}(cos theta|00> +
sin theta e^{i chi}|11>), cos theta = |a|, sin theta = |b|; checked for (a, b) = (3/5, 4i/5) and
((5/13)(3 + 4i)/5, -12/13): cos^2 + sin^2 = 1 with cos theta sin theta != 0, and the |11> phase i of
the first is the one the convention removes.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import QI

U = QI(F(3, 5), F(4, 5))
GENERIC = [QI(2, 1), QI(-1, 3), QI(5, -2), QI(1, 4)]
AB_SAMPLES = [(QI(1), QI(1)), (QI(2, 1), QI(-3)), (QI(F(1, 2)), QI(0, 5)), (QI(3, 4), QI(-1, 2))]


def act(A, v):
    out = [QI(0)] * 4
    for i in range(2):
        for j in range(2):
            for k in range(2):
                out[2 * i + j] = out[2 * i + j] + A[i][k] * v[2 * k + j]
    return out


def units():
    out = []
    for a in range(2):
        for b in range(2):
            out.append([[QI(1) if (i, j) == (a, b) else QI(0) for j in range(2)] for i in range(2)])
    return out


def orbit_rank(v):
    return GA.field_rank([act(A, v) for A in units()])


def det4(M):
    """Exact 4 x 4 determinant by cofactor expansion."""
    if len(M) == 1:
        return M[0][0]
    tot = QI(0)
    for c in range(len(M)):
        minor = [row[:c] + row[c + 1:] for row in M[1:]]
        term = M[0][c] * det4(minor)
        tot = tot + term if c % 2 == 0 else tot - term
    return tot


def proportional(u, v):
    return all(u[i] * v[j] == u[j] * v[i] for i in range(4) for j in range(4))


def check_invariance_forces_one_eigenspace():
    Gd = [i - j for i in range(2) for j in range(2)]
    assert Gd == [0, -1, 1, 0]
    phase = {0: QI(1), -1: U.conj(), 1: U}
    Ud = [phase[g] for g in Gd]
    assert U * U.conj() == 1 and U != 1 and U * U != 1 and U * U * U * U != 1
    assert len({(z.re, z.im) for z in Ud}) == 3
    invariant = []
    for r in range(1, 5):
        for supp in combinations(range(4), r):
            v = [GENERIC[i] if i in supp else QI(0) for i in range(4)]
            if proportional([Ud[i] * v[i] for i in range(4)], v):
                invariant.append(supp)
    assert invariant == [(0,), (1,), (2,), (3,), (0, 3)], invariant
    # each invariant support lies in one eigenspace of G
    for supp in invariant:
        assert len({Gd[i] for i in supp}) == 1


def pair_vec(a, b):
    """a|00> + b|11>."""
    return [a, QI(0), QI(0), b]


# Product vectors (orbit rank 2): two on the number-basis lines |00>, |11> and the lines |01>, |10>.
PRODUCT_SAMPLES = [[QI(3), QI(0), QI(0), QI(0)], [QI(0), QI(0), QI(0), QI(0, 2)],
                   [QI(0), QI(1), QI(0), QI(0)], [QI(0), QI(0), QI(1), QI(0)]]
# Diagonal of G = N (x) 1 - 1 (x) N on |ij> at index 2i + j.
G_DIAG = [i - j for i in range(2) for j in range(2)]
# Every nonempty support in the number basis, in order of size.
SUPPORTS = [supp for r in range(1, 5) for supp in combinations(range(4), r)]


def generic_vec(supp):
    """A vector with generic Q(i) coefficients on the support and 0 off it."""
    return [GENERIC[i] if i in supp else QI(0) for i in range(len(GENERIC))]


def check_cyclic_separating_only_on_the_number_basis():
    for a, b in AB_SAMPLES:
        v = pair_vec(a, b)
        M = [act(A, v) for A in units()]
        assert det4(M) == a * a * b * b
        assert orbit_rank(v) == 4
    for v in PRODUCT_SAMPLES:
        assert orbit_rank(v) == 2
    # among all 2^4 - 1 = 15 supports: invariant and cyclic-separating only for {|00>, |11>}
    assert len(SUPPORTS) == 15
    good = []
    for supp in SUPPORTS:
        v = generic_vec(supp)
        inv = len({G_DIAG[i] for i in supp}) == 1
        if inv and orbit_rank(v) == 4:
            good.append(supp)
    assert good == [(0, 3)], good


def check_phase_convention_gives_cos_sin():
    for a, b in ((QI(F(3, 5)), QI(0, F(4, 5))), (QI(F(5, 13)) * QI(F(3, 5), F(4, 5)), QI(F(-12, 13)))):
        n2 = a * a.conj() + b * b.conj()
        assert n2 == 1
        ca, sb = a * a.conj(), b * b.conj()          # cos^2 theta, sin^2 theta
        assert ca.im == 0 and sb.im == 0 and ca.re * sb.re != 0 and ca.re + sb.re == 1
    # (3/5)|00> + (4i/5)|11> = cos|00> + sin e^{i pi/2}|11>: the |11> phase i is removed by the convention
    a, b = QI(F(3, 5)), QI(0, F(4, 5))
    phase = b / QI(F(4, 5))
    assert phase == QI(0, 1) and a == QI(F(3, 5))
