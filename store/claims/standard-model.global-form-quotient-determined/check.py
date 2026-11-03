"""standard-model.global-form-quotient-determined: exact checks.

(1) Kernel K = {(lam I_2, lam^-1 I_3)} at the group level: for Gaussian-rational unitaries A, B and a unit
    Gaussian lam, (lam A) (x) (lam^-1 B) = A (x) B (while (lam A) (x) (lam B) differs) and det(lam A) det(lam^-1 B) = lam^-1 det A det B, so each coset
    of K contains exactly one pair with det A det B = 1 (lam = det A det B): (U(2) x U(3))/K = S(U(2) x U(3)), and
    the map (A, B) -> (cA, c^-1 B), c = det A det B, is constant on cosets.
(2) Z_6: in Q(zeta), zeta^2 = zeta - 1, zeta has order exactly 6; the six elements (zeta^-3j I_2, zeta^2j I_3,
    zeta^j) have det 1 factors and map to (I_2, I_3) under (a, b, lam) -> (lam^3 a, lam^-2 b); lam^3 a = I_2 forces
    lam^6 = 1 and x^6 - 1 = prod_j (x - zeta^j) over Q(zeta), so the kernel has exactly six elements. Each of the
    three proper subgroups Gamma of Z_6 misses a kernel element, so no proper cover acts faithfully.
(3) Splitting of C^5: the commutant of the projector onto C^2 in M_5 has dimension 13 = 4 + 9 (block diagonal),
    and a block-diagonal unitary has det = det A det B, so its SU(5) elements are S(U(2) x U(3)).
(4) Charge lattice: the generator (zeta^-3 I_2, zeta^2 I_3, zeta) acts on (Sym^s C^2) (x) (degree-d SU(3) rep)
    (x) (weight q) as zeta^(-3s + 2d + q), computed in Q(zeta); it is 1 iff 2t + 3 delta + q = 0 mod 6 (t = d mod 3,
    delta = s mod 2) over s <= 3, d <= 5, |q| <= 12. Every representation of the spectrum lies on the lattice and
    a colour singlet of hypercharge 1/3 does not.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
A_SAMPLE = [[QI(F(3, 5)), QI(0, F(4, 5))], [QI(0, F(4, 5)), QI(F(3, 5))]]
B_SAMPLE = [[QI(F(1, 3)), QI(F(2, 3)), QI(F(2, 3))], [QI(F(2, 3)), QI(F(1, 3)), QI(F(-2, 3))],
            [QI(0, F(2, 3)), QI(0, F(-2, 3)), QI(0, F(1, 3))]]
LAM = QI(F(5, 13), F(12, 13))
# (name, colour triality t, weak parity delta, Y)
SPECTRUM = [("Q", 1, 1, F(1, 6)), ("L", 0, 1, F(-1, 2)), ("L+", 0, 1, F(1, 2)), ("uc", 2, 0, F(-2, 3)),
            ("dc", 2, 0, F(1, 3)), ("ec", 0, 0, F(1)), ("nuc", 0, 0, F(0)), ("dR", 1, 0, F(-1, 3)),
            ("eR", 0, 0, F(-1))]


class Z6(object):
    """p + q zeta in Q(zeta_6), zeta^2 = zeta - 1."""

    def __init__(self, p=0, q=0):
        self.p, self.q = F(p), F(q)

    def __mul__(self, o):
        return Z6(self.p * o.p - self.q * o.q, self.p * o.q + self.q * o.p + self.q * o.q)

    def __sub__(self, o):
        return Z6(self.p - o.p, self.q - o.q)

    def __eq__(self, o):
        return self.p == o.p and self.q == o.q

    def __ne__(self, o):
        return not self == o

    def __hash__(self):
        return hash((self.p, self.q))

    def inv(self):
        conj = Z6(self.p + self.q, -self.q)
        n = (self * conj).p
        return Z6(conj.p / n, conj.q / n)

    def pw(self, n):
        out, b = Z6(1), (self if n >= 0 else self.inv())
        for _ in range(abs(n)):
            out = out * b
        return out


ZETA = Z6(0, 1)
ONE = Z6(1)


def _mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))] for i in range(len(A))]


def _dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def _ident(n):
    return [[QI(1) if i == j else QI(0) for j in range(n)] for i in range(n)]


def _det(A):
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def _kron(A, B):
    m, k = len(A), len(B)
    return [[A[a][c] * B[b][d] for c in range(m) for d in range(k)] for a in range(m) for b in range(k)]


def _scale(c, A):
    return [[c * x for x in r] for r in A]


def _pmul(a, b):
    out = [Z6(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            t = x * y
            out[i + j] = Z6(out[i + j].p + t.p, out[i + j].q + t.q)
    return out


def check_kernel_and_coset_rescaling():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    ok = _mm(_dag(A_SAMPLE), A_SAMPLE) == _ident(2) and _mm(_dag(B_SAMPLE), B_SAMPLE) == _ident(3)
    ok = ok and LAM * LAM.conj() == QI(1)
    inv = QI(1) / LAM
    # (lam A) x (lam^-1 B) = A x B, and the determinant product rescales by lam^2 lam^-3 = lam^-1
    ok = ok and _kron(_scale(LAM, A_SAMPLE), _scale(inv, B_SAMPLE)) == _kron(A_SAMPLE, B_SAMPLE)
    dA, dB = _det(A_SAMPLE), _det(B_SAMPLE)
    ok = ok and _det(_scale(LAM, A_SAMPLE)) * _det(_scale(inv, B_SAMPLE)) == inv * dA * dB
    # the normalising representative: c = det A det B gives det(cA) det(c^-1 B) = 1, and it is coset-independent
    c = dA * dB
    ok = ok and c * c.conj() == QI(1) and c != QI(1)
    rep = (_scale(c, A_SAMPLE), _scale(QI(1) / c, B_SAMPLE))
    ok = ok and _det(rep[0]) * _det(rep[1]) == QI(1)
    A2, B2 = _scale(LAM, A_SAMPLE), _scale(inv, B_SAMPLE)
    c2 = _det(A2) * _det(B2)
    ok = ok and (_scale(c2, A2), _scale(QI(1) / c2, B2)) == rep
    # a non-kernel scaling (lam A, lam B) changes the action
    ok = ok and _kron(_scale(LAM, A_SAMPLE), _scale(LAM, B_SAMPLE)) != _kron(A_SAMPLE, B_SAMPLE)
    GA.check("K = {(lam I2, lam^-1 I3)} acts trivially; each coset meets S(U(2) x U(3)) once", ok)
    return ok


def check_z6_kernel_exactly():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    powers = [ZETA.pw(j) for j in range(6)]
    ok = len(set(powers)) == 6 and ZETA.pw(6) == ONE and ZETA.pw(3) == Z6(-1) and ZETA.pw(2) == ZETA - ONE
    for j in range(6):
        a, b, lam = ZETA.pw(-3 * j), ZETA.pw(2 * j), ZETA.pw(j)
        # det a = a^2 (scalar 2 x 2), det b = b^3; image (lam^3 a, lam^-2 b)
        ok = ok and a * a == ONE and b * b * b == ONE
        ok = ok and lam.pw(3) * a == ONE and lam.pw(-2) * b == ONE
    ok = ok and ZETA.pw(3) * ONE != ONE                       # (I2, I3, zeta) is not in the kernel
    # lam^6 = 1 has exactly the six roots zeta^j: prod (x - zeta^j) = x^6 - 1
    poly = [ONE]
    for z in powers:
        poly = _pmul(poly, [Z6(0) - z, ONE])
    ok = ok and poly == [Z6(-1)] + [Z6(0)] * 5 + [ONE]
    kernel = set(powers)
    proper = [set(ZETA.pw(d * i) for i in range(6)) for d in (6, 3, 2)]  # {1}, Z2, Z3
    ok = ok and [len(g) for g in proper] == [1, 2, 3] and all(kernel - g for g in proper)
    GA.check("the kernel of SU(2) x SU(3) x U(1) -> S(U(2) x U(3)) is exactly Z6; proper covers are unfaithful", ok)
    return ok


def check_su5_splitting_subgroup():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    # commutant of P = diag(1, 1, 0, 0, 0) in M_5 (real coefficients suffice for the dimension count)
    P = [F(1) if i < 2 else F(0) for i in range(5)]
    rows = []
    for i in range(5):
        for j in range(5):
            row = [F(0)] * 25
            row[i * 5 + j] = P[j] - P[i]                     # (XP - PX)_ij = X_ij (P_j - P_i)
            rows.append(row)
    dim_comm = 25 - GA.rank_of_vectors(rows)
    blk = [[QI(0)] * 5 for _ in range(5)]
    for i in range(2):
        for j in range(2):
            blk[i][j] = A_SAMPLE[i][j]
    for i in range(3):
        for j in range(3):
            blk[2 + i][2 + j] = B_SAMPLE[i][j]
    # det of the block matrix by permutation expansion restricted to blocks equals det A det B
    dA, dB = _det(A_SAMPLE), _det(B_SAMPLE)
    c = dA * dB
    unit = _mm(_dag(blk), blk) == _ident(5)
    rescaled = [[c * blk[i][j] if i < 2 else blk[i][j] / c for j in range(5)] for i in range(5)]
    d_rescaled = _det([r[:2] for r in rescaled[:2]]) * _det([r[2:] for r in rescaled[2:]])
    ok = dim_comm == 13 == 2 * 2 + 3 * 3 and unit and c != QI(1) and d_rescaled == QI(1)
    GA.check("the splitting C^5 = C^2 + C^3 has commutant of dimension 13; det-one block unitaries = S(U2 x U3)", ok)
    return ok


def check_charge_lattice():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    gen2, gen3, genl = ZETA.pw(-3), ZETA.pw(2), ZETA
    ok = True
    count = 0
    for s in range(4):
        for d in range(6):
            for q in range(-12, 13):
                g = gen2.pw(s) * gen3.pw(d) * genl.pw(q)
                t, delta = d % 3, s % 2
                ok = ok and ((g == ONE) == ((2 * t + 3 * delta + q) % 6 == 0))
                count += 1
    ok = ok and count == 600
    for (_, t, delta, Y) in SPECTRUM:
        q6 = 6 * Y
        ok = ok and q6.denominator == 1 and (2 * t + 3 * delta + q6.numerator) % 6 == 0
        ok = ok and (F(t, 3) + F(delta, 2) + Y).denominator == 1
    bad = F(1, 3)                                            # colour singlet, doublet parity 0
    ok = ok and (6 * bad).numerator % 6 != 0 and (F(0, 3) + F(0, 2) + bad).denominator != 1
    GA.check("Z6 acts trivially iff 2t + 3 delta + q = 0 mod 6; the spectrum is on the lattice, Y = 1/3 singlet not", ok)
    return ok
