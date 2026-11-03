"""correspondence.statistics-no-go: exact checks (GA blade engine, Fraction matrices).

The proof is the trace argument; its finite content is checked where the claim names an algebra.
(1) Matrices: tr(XY - YX) = 0 for sample rational X, Y of sizes 2, 3, 4, while tr(hbar 1_U) = hbar dim U is
    nonzero for every dim U = 1..6: no nonzero finite-dimensional U carries [Z, Zbar] = hbar 1_U.
(2) Cl(2,4), dimension 64: the left regular trace tr(L_x) equals 64 <x>_0 on all 64 blades, and the
    scalar part of every blade commutator [e_A, e_B] vanishes (all 4096 ordered pairs), so tr L of any
    commutator is 0 while tr L_(hbar 1) = 64 hbar: no pair x, y in Cl(2,4) (or Cl(2,4)_C, by linearity)
    satisfies [x, y] = hbar 1 with hbar != 0, hence no unital embedding of the palatial algebra.
(3) Contrast: the anticommutator escapes the argument. Cl(2,4) holds the two real ladder pairs
    f_k = (e_a + e_b)/2, f_k^* = (e_a - e_b)/2 (e_a^2 = +1, e_b^2 = -1), and Cl(2,4)_C a third,
    f_3 = (i e4 + e5)/2, f_3^* = (i e4 - e5)/2 (the real Witt index is 2): each has f^2 = f^*^2 = 0 and
    f f^* + f^* f = 1, pairs from different rungs anticommute, and <f f^*>_0 = <f^* f>_0 = 1/2 sum to 1.
"""
from fractions import Fraction as F

import GA

SQ = (1, 1, -1, -1, -1, -1)       # Cl(2,4): e0, e1 square +1; e2..e5 square -1
BLADES = GA.all_blades(6)
MATS = [
    ([[F(1), F(2)], [F(-3), F(1, 2)]], [[F(0), F(5)], [F(1), F(-1)]]),
    ([[F(1), F(0), F(2)], [F(3), F(-1), F(0)], [F(1, 3), F(1), F(1)]],
     [[F(2), F(1), F(0)], [F(0), F(1, 2), F(-1)], [F(4), F(0), F(3)]]),
    ([[F(i * j - 2) for j in range(4)] for i in range(4)], [[F(i + 2 * j, 3) for j in range(4)] for i in range(4)]),
]
PAIRS = [(0, 2), (1, 3)]


def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def check_trace_argument_in_finite_dimensions():
    ok = True
    traces = []
    for X, Y in MATS:
        XY, YX = mmul(X, Y), mmul(Y, X)
        traces.append(sum(XY[i][i] - YX[i][i] for i in range(len(X))))
        ok = ok and XY != YX
    ok = ok and traces == [0, 0, 0]
    hbar = F(1, 3)
    id_traces = [sum(hbar * (1 if i == j else 0) for i in range(d) for j in range(d) if i == j) for d in range(1, 7)]
    ok = ok and id_traces == [F(1, 3), F(2, 3), F(1), F(4, 3), F(5, 3), F(2)]
    GA.check("trace of a matrix commutator is 0, trace of hbar 1_U is hbar dim U != 0", ok)
    return ok


def left_trace(x):
    t = F(0)
    for b in BLADES:
        t += GA.mul(x, {b: F(1)}, SQ).get(b, F(0))
    return t


def check_cl24_commutators_have_no_scalar_part():
    ok = True
    ok = ok and len(BLADES) == 64
    ok = ok and all(left_trace({b: F(1)}) == (64 if b == () else 0) for b in BLADES)
    bad = 0
    for a in BLADES:
        for b in BLADES:
            s1, c1 = GA.blade_mul(a, b, SQ)
            s2, c2 = GA.blade_mul(b, a, SQ)
            sc = (s1 if c1 == () else 0) - (s2 if c2 == () else 0)
            bad += 1 if sc != 0 else 0
    ok = ok and bad == 0
    ok = ok and left_trace(GA.sc(F(1, 3))) == F(64, 3)
    GA.check("Cl(2,4): tr L_x = 64 <x>_0; no blade commutator has a scalar part, so [x, y] = hbar 1 is impossible", ok)
    return ok


def cmul(x, y):
    """Product in Cl(2,4)_C, elements as (real part, imaginary part)."""
    return (GA.sub(GA.mul(x[0], y[0], SQ), GA.mul(x[1], y[1], SQ)),
            GA.add(GA.mul(x[0], y[1], SQ), GA.mul(x[1], y[0], SQ)))


def cadd(x, y):
    return (GA.add(x[0], y[0]), GA.add(x[1], y[1]))


def check_ladder_pairs_satisfy_car_in_cl24():
    ok = True
    zero, one = ({}, {}), (GA.sc(1), {})
    fs = []
    for a, b in PAIRS:
        f = (GA.scal(F(1, 2), GA.add(GA.gen(a), GA.gen(b))), {})
        fd = (GA.scal(F(1, 2), GA.sub(GA.gen(a), GA.gen(b))), {})
        fs.append((f, fd))
    fs.append(((GA.scal(F(1, 2), GA.gen(5)), GA.scal(F(1, 2), GA.gen(4))),
               (GA.scal(F(-1, 2), GA.gen(5)), GA.scal(F(1, 2), GA.gen(4)))))
    for f, fd in fs:
        ok = ok and cmul(f, f) == zero and cmul(fd, fd) == zero
        ok = ok and cadd(cmul(f, fd), cmul(fd, f)) == one
        ok = ok and cmul(f, fd)[0].get(()) == F(1, 2) and cmul(fd, f)[0].get(()) == F(1, 2)
    for i in range(3):
        for j in range(3):
            if i != j:
                for x in fs[i]:
                    for y in fs[j]:
                        ok = ok and cadd(cmul(x, y), cmul(y, x)) == zero
    ok = ok and len(fs) == 3
    GA.check("two real and one complex ladder pair in Cl(2,4)_C satisfy the CAR; the anticommutator escapes", ok)
    return ok
