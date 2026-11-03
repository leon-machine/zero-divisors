"""families.alignment-computed-thirteenth-refutation-democracy-one: exact checks of the computable parts.

Clauses (2) and (4) (the redirection, and the naming of the residue) are readings with no computable content.
(1) The magnitude window from the stated inputs H = 10^-33 eV, M_P = 10^28 eV, weak scale 10^11 eV:
    H^2/M_P = 10^-94 eV, and (H^2/M_P)/weak = 10^-105, H/weak = 10^-44 exactly, both below 1; the tilt
    Lambda Omega_vac with any vacuum length L between the Planck length 1/M_P and the Hubble length 1/H
    (Lambda = H^2 in these units) lies between H^2/M_P and H (checked at the endpoints and at interior L).
(3) S3 invariance: the vectors of face space fixed by all six permutation matrices form exactly the
    democratic line (kernel dimension 1, spanned by (1,1,1)), so an S3-symmetric source lies on it
    (the indifference instrument, premise). The Gram square Y_0 = u' u'^T, u' = (1,1,1), has rank 1,
    trace 3, characteristic polynomial x^3 - 3x^2 (spectrum (3, 0, 0)), eigenvector u' with eigenvalue 3,
    and kernel the plane sum v = 0 (two light families); its eigenvectors are the democratic vector and
    the orthogonal plane, as the refinement of the faces conjecture states.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

H_EV, MP_EV, WEAK_EV = F(1, 10 ** 33), F(10 ** 28), F(10 ** 11)
PERMS = [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0), (2, 0, 1)]


def check_magnitude_window():
    premise("families.source-term-linear-tilt-mass-functional")
    lo, hi = H_EV * H_EV / MP_EV, H_EV
    ok = lo == F(1, 10 ** 94)
    ok = ok and lo / WEAK_EV == F(1, 10 ** 105) and hi / WEAK_EV == F(1, 10 ** 44) and hi / WEAK_EV < 1
    lam = H_EV * H_EV
    for L in (1 / MP_EV, 1 / H_EV, F(10 ** 5) / MP_EV, F(1, 10 ** 7) / H_EV):
        tilt = lam * L
        ok = ok and lo <= tilt <= hi and tilt / WEAK_EV < F(1, 10 ** 43)
    _tp_rv = (ok); assert _tp_rv is not False, "check_magnitude_window"; return _tp_rv


def check_democratic_line_and_rank_one_texture():
    premise("families.imported-indifference-instrument")
    rows = []
    for p in PERMS:
        rows += [[(1 if p[i] == j else 0) - (1 if i == j else 0) for j in range(3)] for i in range(3)]
    fixed = GA.field_kernel([[F(x) for x in r] for r in rows])
    ok = len(fixed) == 1 and fixed[0][0] == fixed[0][1] == fixed[0][2] != 0
    Y = [[F(1)] * 3 for _ in range(3)]
    ok = ok and GA.mat_rank(Y) == 1 and sum(Y[i][i] for i in range(3)) == 3
    # characteristic polynomial x^3 - tr x^2 + e2 x - det
    tr = sum(Y[i][i] for i in range(3))
    e2 = sum(Y[i][i] * Y[j][j] - Y[i][j] * Y[j][i] for i in range(3) for j in range(i + 1, 3))
    det = (Y[0][0] * (Y[1][1] * Y[2][2] - Y[1][2] * Y[2][1]) - Y[0][1] * (Y[1][0] * Y[2][2] - Y[1][2] * Y[2][0])
           + Y[0][2] * (Y[1][0] * Y[2][1] - Y[1][1] * Y[2][0]))
    ok = ok and (tr, e2, det) == (3, 0, 0)
    u = [F(1)] * 3
    ok = ok and [sum(Y[i][j] * u[j] for j in range(3)) for i in range(3)] == [3 * x for x in u]
    ker = GA.field_kernel(Y)
    ok = ok and len(ker) == 2 and all(sum(k) == 0 for k in ker)
    _tp_rv = (ok); assert _tp_rv is not False, "check_democratic_line_and_rank_one_texture"; return _tp_rv
