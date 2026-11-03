"""standard-model.no-tower-but-one-contributes-towers: exact checks.

The finite core is the index bookkeeping. This tower's gauge generators act on a field's internal
space through its component in the hierarchy fibre H = C^2 (x) C^3 only (rho(X) = X_H (x) 1 on the
H-carrying part, 0 elsewhere). Indices are computed as traces of squares of the normalised Cartan
generators (weak T_3, colour H_8-type Cartan diag(1/2, -1/2, 0), hypercharge with T_1 = (3/5) tr Y^2).
A field of another tower, of any internal dimension (multiplicity) and either statistics, carries no
H component, so rho(X) = 0 and all three indices vanish; its contribution to (b_1, b_2, b_3) through
the imported coefficient formula is (0, 0, 0), and adding any such fields (the mirror tower's copy of
the generation and Higgs, four odd towers' content) leaves this tower's (41/10, -19/6, -7) unchanged.
Controls: H-carrying fields (the doublet, the triplet, the quark doublet) have nonzero indices.
The superselection itself (no H component for another tower's field) is the imported Fact's content,
used as the model's input; the sum over the seven other towers is a sum of zeros.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def diag(vals):
    n = len(vals)
    return [[F(vals[i]) if i == j else F(0) for j in range(n)] for i in range(n)]


def kron(A, B):
    return [[A[i // len(B)][j // len(B[0])] * B[i % len(B)][j % len(B[0])]
             for j in range(len(A[0]) * len(B[0]))] for i in range(len(A) * len(B))]


def zero(n):
    return [[F(0)] * n for _ in range(n)]


def trace_sq(M):
    M2 = GA.mat_mul(M, M)
    return sum((M2[i][i] for i in range(len(M))), F(0))


# normalised Cartan generators on the slot factor C^2 and the pair factor C^3
T3_SLOT = diag([F(1, 2), F(-1, 2)])
H_PAIR = diag([F(1, 2), F(-1, 2), F(0)])
I2, I3 = diag([1, 1]), diag([1, 1, 1])


def field(kind, d2, d3, Y, mult, carries_H):
    """Action of (Y, T_3, H) on a field's internal space: the H-carrying part C^d2 (x) C^d3 (x) C^mult,
    or, for another tower's field, a space of dimension d2 d3 mult on which this tower acts as 0."""
    n = d2 * d3 * mult
    if not carries_H:
        return kind, (zero(n), zero(n), zero(n))
    t2 = T3_SLOT if d2 == 2 else zero(d2)
    t3 = H_PAIR if d3 == 3 else zero(d3)
    Im = diag([1] * mult)
    i2, i3 = diag([1] * d2), diag([1] * d3)
    Ym = kron(kron(i2, i3), Im)
    Ym = [[Y * v for v in row] for row in Ym]
    return kind, (Ym, kron(kron(t2, i3), Im), kron(kron(i2, t3), Im))


def shift(fields):
    """Imported coefficient formula: Weyl 2/3, complex scalar 1/3, T_1 = (3/5) tr Y^2."""
    tot = [F(0)] * 3
    for kind, (Y, T3, Hc) in fields:
        w = F(2, 3) if kind == "weyl" else F(1, 3)
        for i, t in enumerate((F(3, 5) * trace_sq(Y), trace_sq(T3), trace_sq(Hc))):
            tot[i] += w * t
    return tuple(tot)


GAUGE = (F(0), F(-22, 3), F(-11))
GEN = [("weyl", 2, 3, F(1, 6)), ("weyl", 2, 1, F(-1, 2)), ("weyl", 1, 3, F(-2, 3)),
       ("weyl", 1, 3, F(1, 3)), ("weyl", 1, 1, F(1)), ("weyl", 1, 1, F(0))]
OTHER_TOWERS = [("weyl", 2, 3, F(1, 6), 3), ("weyl", 2, 1, F(-1, 2), 3), ("scalar", 2, 1, F(1, 2), 1),
                ("weyl", 1, 1, F(0), 7), ("scalar", 1, 3, F(2, 3), 5), ("weyl", 2, 3, F(5, 6), 2)]


def check_other_tower_fields_have_zero_index():
    premise("standard-model.connection-forced")
    premise("standard-model.imported-sectors-superselection-mirror-copy")
    premise("standard-model.imported-coefficient-sum-indices")
    ok = True
    n = 0
    for kind, d2, d3, Y, mult in OTHER_TOWERS:
        k, gens = field(kind, d2, d3, Y, mult, carries_H=False)
        ok = ok and all(trace_sq(g) == 0 for g in gens)
        ok = ok and shift([(k, gens)]) == (F(0), F(0), F(0))
        n += 1
    ok = ok and n == 6
    # controls: carrying an H component gives nonzero indices
    ok = ok and shift([field("weyl", 2, 1, F(1, 2), 1, True)]) == (F(1, 5), F(1, 3), F(0))
    ok = ok and shift([field("scalar", 1, 3, F(1, 3), 1, True)]) == (F(1, 15), F(0), F(1, 6))
    ok = ok and shift([field("weyl", 2, 3, F(1, 6), 1, True)]) == (F(1, 15), F(1), F(2, 3))
    GA.check("towers: a field of another tower has zero SU(2), SU(3), U(1)_Y index, either statistics", ok)
    return ok


def check_other_towers_leave_this_tower_running_unchanged():
    premise("standard-model.connection-forced")
    premise("standard-model.imported-sectors-superselection-mirror-copy")
    premise("standard-model.imported-coefficient-sum-indices")
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    this = [field(k, d2, d3, Y, 3, True) for k, d2, d3, Y in GEN] + [field("scalar", 2, 1, F(1, 2), 1, True)]
    b = tuple(GAUGE[i] + shift(this)[i] for i in range(3))
    ok = b == (F(41, 10), F(-19, 6), F(-7))
    # the mirror tower (a copy of the generation and Higgs) and four odd towers' content
    others = [field(k, d2, d3, Y, 3, False) for k, d2, d3, Y in GEN] + [field("scalar", 2, 1, F(1, 2), 1, False)]
    others += [field(k, d2, d3, Y, m, False) for k, d2, d3, Y, m in OTHER_TOWERS] * 4
    ok = ok and shift(others) == (F(0), F(0), F(0))
    b2 = tuple(GAUGE[i] + shift(this + others)[i] for i in range(3))
    ok = ok and b2 == b and len(others) == 31
    GA.check("towers: the other towers contribute Dl = (0, 0, 0); this tower's b stays (41/10, -19/6, -7)", ok)
    return ok
