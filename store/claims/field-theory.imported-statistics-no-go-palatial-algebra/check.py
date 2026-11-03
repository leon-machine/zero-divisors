"""field-theory.imported-statistics-no-go-palatial-algebra: exact checks of the finite core.

hbar is a fixed nonzero rational (the statements are homogeneous in it).
(1) No finite-dimensional home. In Cl(2,4) (dimension 64) the left-regular trace of every basis blade
    is 64 for the unit and 0 otherwise, and the scalar part of [A, B] vanishes for all 4096 ordered
    blade pairs; by bilinearity no x, y in Cl(2,4) or its complexification satisfy [x, y] = hbar.
    The same trace obstruction in a matrix representation: the polynomial realisation truncated to
    degree <= d (d = 1..6) gives [Z, Zbar] = hbar diag(1, ..., 1, -d), of trace 0, never hbar times
    the identity; the failure sits at the top degree.
(2) The polynomial realisation. On polynomials in Z^1..Z^4 with Zbar_b = -hbar d/dZ^b,
    [Z^a, Zbar_b] p = hbar delta_ab p for all 16 pairs (a, b) and four sample polynomials, while the
    Z^a commute among themselves and so do the Zbar_b.
Not checked: the bounded infinite-dimensional case (Wielandt-Wintner), which has no finite core
beyond the trace argument in (1).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

HBAR = F(3, 7)
SQ = GA.sig(2, 4)
NV = 4
POLYS = (
    {(0, 0, 0, 0): F(1)},
    {(2, 1, 0, 0): F(3), (0, 0, 1, 3): F(-2), (1, 0, 0, 0): F(1, 2)},
    {(1, 1, 1, 1): F(5), (0, 4, 0, 0): F(1)},
    {(3, 0, 2, 0): F(-1, 3), (0, 0, 0, 1): F(7), (1, 2, 0, 0): F(2)},
)


def padd(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c != 0}


def zmul(a, p):
    return {tuple(e[i] + (i == a) for i in range(NV)): c for e, c in p.items()}


def zbar(b, p):
    out = {}
    for e, c in p.items():
        if e[b]:
            ne = tuple(e[i] - (i == b) for i in range(NV))
            out[ne] = out.get(ne, F(0)) - HBAR * e[b] * c
    return {e: c for e, c in out.items() if c != 0}


def scal(c, p):
    return {e: c * v for e, v in p.items() if c * v != 0}


def check_no_finite_dimensional_representation():
    premise("correspondence.statistics-no-go")
    ok = True
    blades = GA.all_blades(6)
    ok = ok and len(blades) == 64
    for b in blades:
        tr = sum((GA.blade_mul(b, c, SQ)[0] for c in blades if GA.blade_mul(b, c, SQ)[1] == c), F(0))
        ok = ok and tr == (64 if b == () else 0)
    for a in blades:
        for b in blades:
            ca, pa = GA.blade_mul(a, b, SQ)
            cb, pb = GA.blade_mul(b, a, SQ)
            s = (ca if pa == () else 0) - (cb if pb == () else 0)
            ok = ok and s == 0
    for d in range(1, 7):
        n = d + 1
        Z = [[F(1) if i == j + 1 else F(0) for j in range(n)] for i in range(n)]
        Zb = [[-HBAR * j if i == j - 1 else F(0) for j in range(n)] for i in range(n)]
        Cm = [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(GA.mat_mul(Z, Zb), GA.mat_mul(Zb, Z))]
        want = [[(HBAR if i < d else -d * HBAR) if i == j else F(0) for j in range(n)] for i in range(n)]
        ok = ok and Cm == want and sum(Cm[i][i] for i in range(n)) == 0
    GA.check("trace of every commutator vanishes in Cl(2,4) and in truncations: [x, y] = hbar has no solution", ok)
    return ok


def check_polynomial_realisation():
    premise("correspondence.symmetrised-quadratics-palatial-algebra")
    ok = True
    for p in POLYS:
        for a in range(NV):
            for b in range(NV):
                c = padd(zmul(a, zbar(b, p)), scal(F(-1), zbar(b, zmul(a, p))))
                ok = ok and c == (scal(HBAR, p) if a == b else {})
                ok = ok and padd(zmul(a, zmul(b, p)), scal(F(-1), zmul(b, zmul(a, p)))) == {}
                ok = ok and padd(zbar(a, zbar(b, p)), scal(F(-1), zbar(b, zbar(a, p)))) == {}
    GA.check("on polynomials, Zbar_b = -hbar d/dZ^b gives [Z^a, Zbar_b] = hbar delta_ab", ok)
    return ok
