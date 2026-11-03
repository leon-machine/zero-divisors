"""interior.exact-scale-decoupling: exact checks.

The shape operator S(B) = -(B + 3 sigma_r B sigma_r)/2 on the six-dimensional bivector space of Cl(1,3)
(GA.py, signature (+,-,-,-)), sigma_r = gamma_1 gamma_0, is built as a 6 x 6 matrix on the blades
gamma_a gamma_b, a < b. Pi is the projector onto span{sigma_r, I sigma_r}, built independently from the
coefficients of those two blades.
(1) S = 1 - 3 Pi on every blade; S^2 + S = 2 as a matrix identity; the eigenspaces of -2 and +1 have
    dimensions 2 and 4 (computed kernels, summing to 6), trace 0.
(2) The factorisation R(B) = -(M/r^3) S(B): the store-sign curvature operator is computed from the
    Schwarzschild gauge fields (hb, Omega) on flat spacetime (jet engine, GTG sign, calR(B) = -R(hb(B)))
    in the static gauge at four (M, r) samples and in the Painleve-Gullstrand gauge at four more,
    two inside the horizon, and equals -(M/r^3) times the same matrix S each time: S depends on
    neither M nor r.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

# ---- GTG engine: lib/gtg.py (L12 names; jets, fields (hb, Omega), store-sign curvature, Ricci and Schouten
# ---- maps, Cl(2,4) tractors with generators 0..3 spacetime, 4 = e+, 5 = e-) ----
S13, static_field, fb, apply_op = gtg.S13, gtg.static_field, gtg.biv, gtg.apply_op


def pg_field(r0, s0, c0, M):
    """Schwarzschild in the Painleve-Gullstrand gauge hb = 1 - beta P, beta = sqrt(2M/r)."""
    return gtg.schwarzschild_pg(M, r0, s0, c0)

STATIC = [(F(3, 5), F(3, 5), F(4, 5), F(1)), (F(4, 5), F(5, 13), F(12, 13), F(1, 2)),
          (F(5, 13), F(4, 5), F(3, 5), F(3, 2)), (F(12, 13), F(8, 17), F(15, 17), F(7))]
PG = [(F(1, 2), F(3, 5), F(4, 5), F(1)), (F(9, 2), F(5, 13), F(12, 13), F(1)),
      (F(8), F(4, 5), F(3, 5), F(1, 4)), (F(1, 8), F(8, 17), F(15, 17), F(9, 4))]
PLANES = [(a, b) for a in range(4) for b in range(a + 1, 4)]
SIG = GA.mul(GA.gen(1), GA.gen(0), S13)


def shape(B):
    return GA.scal(F(-1, 2), GA.add(B, GA.scal(3, GA.mul(GA.mul(SIG, B, S13), SIG, S13))))


def matrix(op):
    """Matrix of a linear map on bivectors: column j is op(blade j)."""
    cols = [op({pl: F(1)}) for pl in PLANES]
    return [[cols[j].get(PLANES[i], F(0)) for j in range(6)] for i in range(6)]


def proj(B):
    """Pi: keep the gamma_0 gamma_1 and gamma_2 gamma_3 components (sigma_r and its dual)."""
    return {pl: c for pl, c in B.items() if pl in ((0, 1), (2, 3))}


def check_shape_operator_algebra():
    Sm = matrix(shape)
    Pm = matrix(proj)
    one = [[F(1 if i == j else 0) for j in range(6)] for i in range(6)]
    ok = Sm == [[one[i][j] - 3 * Pm[i][j] for j in range(6)] for i in range(6)]
    Sq = GA.mat_mul(Sm, Sm)
    ok = ok and [[Sq[i][j] + Sm[i][j] for j in range(6)] for i in range(6)] == [[2 * one[i][j] for j in range(6)]
                                                                            for i in range(6)]
    dims = {}
    for lam in (-2, 1):
        dims[lam] = len(GA.field_kernel([[Sm[i][j] - lam * one[i][j] for j in range(6)] for i in range(6)]))
    ok = ok and dims == {-2: 2, 1: 4}
    ok = ok and sum(Sm[i][i] for i in range(6)) == 0
    # on the pair and on a mixed plane by hand
    ok = ok and GA.eq(shape(SIG), GA.scal(-2, SIG)) and GA.eq(shape(fb(0, 2)), fb(0, 2))
    _tp_rv = (ok); assert _tp_rv is not False, "check_shape_operator_algebra"; return _tp_rv


def check_factorisation_at_every_radius():
    premise("interior.imported-schwarzschild-curvature-spectrum")
    Sm = matrix(shape)
    fields = []
    for F0, s0, c0, M in STATIC:
        r0 = 2 * M / (1 - F0 * F0)
        fields.append((static_field(r0, s0, c0, lambda r, M=M: 1 - 2 * M / r), M, r0))
    for r0, s0, c0, M in PG:
        fields.append((pg_field(r0, s0, c0, M), M, r0))
    ok = len(fields) == 8
    for fld, M, r0 in fields:
        Rc = fld.curvature()
        Rm = matrix(lambda B: apply_op(Rc, B))
        ok = ok and Rm == [[-(M / r0 ** 3) * Sm[i][j] for j in range(6)] for i in range(6)]
    # one sample by hand: PG at r = 1/2, M = 1: -M/r^3 = -8, eigenvalue 16 on sigma_r
    fld, M, r0 = fields[4]
    ok = ok and -(M / r0 ** 3) == -8 and apply_op(fld.curvature(), fb(0, 1)) == {(0, 1): F(16)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_factorisation_at_every_radius"; return _tp_rv
