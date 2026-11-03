"""families.faces-ordered-what-identification-requires-first: exact checks of the computable parts.

(1) Structural: the three faces (two-element subsets of three slots) are permuted transitively by S3, every
    two faces share exactly one slot, so identical faces need S3 to break. A face-space direction orders the
    faces by overlap: the stabiliser in S3 of the democratic vector is all of S3 (no ordering), of a vector
    with two equal components is of order 2, and of a generic vector (distinct components) is trivial,
    which orders all three faces.
(2) Texture arithmetic and the Cabibbo relation: for the nearest-neighbour block (0, A; A, B) the light-to-
    heavy eigenvalue ratio equals tan^2 theta of the mixing angle exactly (checked at (A, B) with rational
    eigenvalues, e.g. (2, 3) with eigenvalues 4, -1 and eigenvector (2, -1)), so theta_C = arctan
    sqrt(m_d/m_s), approximately sqrt(m_d/m_s). With m_d = 4.70, m_s = 93.5 MeV: 0.215^2 < m_d/m_s < 0.235^2,
    sqrt(m_d/m_s) lies in [0.22415, 0.22425) (prints as 0.2242, i.e. 0.224), and (0.225 - sqrt)/0.225 lies in
    (0.003, 0.004): agreement to 0.4 percent.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PERMS = [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0), (2, 0, 1)]
TEXTURES = [(F(2), F(3)), (F(6), F(5)), (F(4), F(6))]
MD, MS = F(470, 100), F(935, 10)


def stab(v):
    return [p for p in PERMS if [v[p[k]] for k in range(3)] == list(v)]


def check_faces_identical_and_direction_orders_them():
    premise("families.three-identical-families-mixing-shared-slots")
    premise("families.alignment-computed-thirteenth-refutation-democracy-one")
    premise("families.imported-face-valued-bracket-quantum-numbers")
    faces = [frozenset(c) for c in ((0, 1), (0, 2), (1, 2))]
    ok = all(len(a & b) == 1 for a in faces for b in faces if a != b)
    orbit = {frozenset(p[x] for x in faces[0]) for p in PERMS}
    ok = ok and orbit == set(faces)
    ok = ok and len(stab([F(1), F(1), F(1)])) == 6
    ok = ok and len(stab([F(1), F(1), F(3)])) == 2
    ok = ok and len(stab([F(1), F(2), F(5)])) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_faces_identical_and_direction_orders_them"; return _tp_rv


def check_texture_and_cabibbo_arithmetic():
    ok = True
    for A, B in TEXTURES:
        disc = B * B + 4 * A * A
        # the samples are chosen with a rational square root of the discriminant
        roots = [x for x in (F(5), F(13), F(10)) if x * x == disc]
        ok = ok and len(roots) == 1
        s = roots[0]
        lp, lm = (B + s) / 2, (B - s) / 2
        ok = ok and lp * lm == -A * A and lp + lm == B
        # eigenvector of the light eigenvalue: (A, lm); mixing angle tan theta = |lm|/A
        vec = (A, lm)
        ok = ok and A * vec[1] == lm * vec[0] and A * vec[0] + B * vec[1] == lm * vec[1]
        tan2 = (lm / A) ** 2
        ok = ok and tan2 == -lm / lp
    rr = MD / MS
    ok = ok and F(215, 1000) ** 2 < rr < F(235, 1000) ** 2
    ok = ok and F(22415, 10 ** 5) ** 2 <= rr < F(22425, 10 ** 5) ** 2
    # relative agreement: (0.225 - sqrt r)/0.225 in (0.003, 0.004), i.e. sqrt r in (0.225*0.996, 0.225*0.997)
    ok = ok and (F(225, 1000) * F(996, 1000)) ** 2 < rr < (F(225, 1000) * F(997, 1000)) ** 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_texture_and_cabibbo_arithmetic"; return _tp_rv
