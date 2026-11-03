"""correspondence.lorentzian-duality-complex-structure: exact checks.

Both Lorentzian signatures, (1,3) and (3,1), each with its orientation e0 e1 e2 e3.
(1) The Hodge star on 2-forms, (*F)_ab = (1/2) eps_abcd eta^cc eta^dd F_cd, satisfies *^2 = -1 on all
    six basis 2-forms (hence on Lambda^2). The same operator in GA.py: on bivectors it is multiplication
    by the unit pseudoscalar I = e0e1e2e3 (I^2 = -1, I B again a bivector), *B = I B with sign +1, matched
    blade by blade with F_ab <-> the bivector with raised components.
(2) Over Q(i), the kernels of * - i and * + i on Lambda^2_C (6 x 6) are each three-dimensional and
    together span Lambda^2_C.
(3) Complex conjugation of components maps the +i eigenspace onto the -i eigenspace and back.
A Euclidean control (signature (4,0)) has *^2 = +1, so the Lorentzian sign is what is tested.
"""
from fractions import Fraction as F
from itertools import permutations

import GA

QI = GA.QI
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
SIGS = [(1, -1, -1, -1), (-1, 1, 1, 1)]


def eps4(idx):
    if len(set(idx)) < 4:
        return 0
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if idx[i] > idx[j])
    return -1 if inv % 2 else 1


def star_matrix(eta):
    """Matrix of * on the basis dx^a ^ dx^b (a < b) of 2-forms."""
    cols = []
    for (c, d) in PAIRS:
        col = []
        for (a, b) in PAIRS:
            # (*F)_ab with F = dx^c ^ dx^d (F_cd = 1, F_dc = -1)
            val = F(0)
            for (x, y, s) in ((c, d, 1), (d, c, -1)):
                val += F(eps4((a, b, x, y)) * s, eta[x] * eta[y])
            col.append(val / 2)
        cols.append(col)
    return [[cols[j][i] for j in range(6)] for i in range(6)]


mm = GA.mat_mul                         # dense matrix product


def check_star_squares_to_minus_one():
    for eta in SIGS:
        S = star_matrix(eta)
        S2 = mm(S, S)
        assert S2 == [[F(-1) if i == j else F(0) for j in range(6)] for i in range(6)]
    S = star_matrix((1, 1, 1, 1))
    assert mm(S, S) == [[F(1) if i == j else F(0) for j in range(6)] for i in range(6)]
    return True


def check_star_is_pseudoscalar_multiplication():
    for eta in SIGS:
        sq = tuple(eta)
        I = GA.mul(GA.mul(GA.gen(0), GA.gen(1), sq), GA.mul(GA.gen(2), GA.gen(3), sq), sq)
        assert GA.mul(I, I, sq) == {(): F(-1)}
        S = star_matrix(eta)
        signs = set()
        for j, (c, d) in enumerate(PAIRS):
            # the 2-form dx^c ^ dx^d corresponds to the bivector eta^cc eta^dd e_c e_d
            B = {(c, d): F(1, eta[c] * eta[d])}
            IB = GA.mul(I, B, sq)
            assert all(len(b) == 2 for b in IB)
            star_biv = {}
            for i, (a, b) in enumerate(PAIRS):
                if S[i][j]:
                    star_biv[(a, b)] = S[i][j] * F(1, eta[a] * eta[b])
            for s in (1, -1):
                if GA.eq(IB, GA.scal(s, star_biv)):
                    signs.add(s)
        assert signs == {1}
    return True


def check_eigenspaces_and_conjugation():
    for eta in SIGS:
        S = [[QI(v) for v in row] for row in star_matrix(eta)]
        kp = GA.field_kernel([[S[i][j] - (QI(0, 1) if i == j else QI(0)) for j in range(6)] for i in range(6)])
        km = GA.field_kernel([[S[i][j] + (QI(0, 1) if i == j else QI(0)) for j in range(6)] for i in range(6)])
        assert len(kp) == 3 and len(km) == 3
        assert GA.field_rank(kp + km) == 6
        conj_p = [[x.conj() for x in v] for v in kp]
        conj_m = [[x.conj() for x in v] for v in km]
        assert GA.field_rank(km + conj_p) == 3 and GA.field_rank(kp + conj_m) == 3
        assert GA.field_rank(kp + conj_p) == 6
    return True
