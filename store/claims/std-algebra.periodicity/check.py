from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def to_mat(M):
    return S.mat(M)


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def right_matrix(x, sq):
    n = len(sq)
    blades = GA.all_blades(n)
    cols = [S.coords(GA.mul({b: F(1)}, x, sq), n) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


def flat(M):
    return [a for row in M for a in row]


# the derived table: d = (p - q) mod 8 -> (division algebra, number of simple summands)
TYPES = {0: ("R", 1), 1: ("R", 2), 2: ("R", 1), 3: ("C", 1), 4: ("H", 1), 5: ("H", 2), 6: ("H", 1), 7: ("C", 1)}
DIMD = {"R": 1, "C": 2, "H": 4}


def trace_form_excess(p, q):
    """(number of blades squaring to +1) - (number squaring to -1): the signature excess of the
    trace form x -> <x^2>_0, an isomorphism invariant (2^-n times the regular trace)."""
    sq = GA.sig(p, q)
    return sum(int(GA.blade_mul(b, b, sq)[0]) for b in GA.all_blades(p + q))


def predicted(p, q):
    n = p + q
    D, c = TYPES[(p - q) % 8]
    m2 = 2 ** n // (c * DIMD[D])
    m = 1
    while m * m < m2:
        m *= 2
    excess = {"R": c * m, "C": 0, "H": -2 * c * m}[D]
    centre = c * (2 if D == "C" else 1)
    return m * m == m2, excess, centre, D, c, m


def check_small_tensor_identities():
    premise("std-algebra.blade-basis")
    sqH = GA.sig(0, 2)
    H = [GA.sc(1), GA.gen(0), GA.gen(1), S.blade(0, 1)]
    L = {i: S.left_matrix(h, sqH) for i, h in enumerate(H)}
    R = {i: right_matrix(S.conj(h), sqH) for i, h in enumerate(H)}
    hh = [flat(GA.mat_mul(L[a], R[b])) for a in range(4) for b in range(4)]
    ok = GA.rank_of_vectors(hh) == 16
    # C (x) H acting on H: a (x) z -> x |-> a x z, z in span(1, i); all commute with right multiplication by i
    Ri = right_matrix(GA.gen(0), sqH)
    ch = []
    for a in range(4):
        for z in (GA.sc(1), GA.gen(0)):
            M = GA.mat_mul(L[a], right_matrix(z, sqH))
            ok = ok and GA.mat_mul(M, Ri) == GA.mat_mul(Ri, M)
            ch.append(flat(M))
    ok = ok and GA.rank_of_vectors(ch) == 8
    # C (x) C -> C + C, z (x) w -> (z w, z conj(w)) on the basis 1, i
    i = GA.QI(0, 1)
    pairs = []
    for z in (GA.QI(1), i):
        for w in (GA.QI(1), i):
            a, b = z * w, z * GA.QI(w.re, -w.im)
            pairs.append([a.re, a.im, b.re, b.im])
    ok = ok and GA.rank_of_vectors(pairs) == 4
    # control: H (x) H with the right action by b instead of conj(b) is not multiplicative
    Rb = {i_: right_matrix(h, sqH) for i_, h in enumerate(H)}
    ok = ok and GA.mat_mul(Rb[1], Rb[2]) != right_matrix(GA.mul(H[1], H[2], sqH), sqH)
    GA.check("H (x) H = M_4(R), C (x) H = M_2(C), C (x) C = C + C by exact ranks", ok)
    return ok


def check_table_invariants():
    """For every Cl(p,q) with 1 <= n <= 8 the predicted type is consistent with three computed
    invariants: dimension 2^n, the pseudoscalar's square (centre type for odd n), and the
    trace-form excess; for n <= 6 the dimension of the centre is solved for directly."""
    premise("std-algebra.tensor-rules")
    premise("std-algebra.cl11-matrix")
    ok = True
    tested = 0
    for n in range(1, 9):
        for q in range(n + 1):
            p = n - q
            fits, excess, centre, D, c, m = predicted(p, q)
            ok = ok and fits
            ok = ok and trace_form_excess(p, q) == excess
            om = S.pseudoscalar(n)
            w2 = GA.mul(om, om, GA.sig(p, q)).get((), F(0))
            if n % 2 == 1:
                ok = ok and (w2 == 1) == (c == 2) and (w2 == -1) == (D == "C")
            if n <= 6:
                ok = ok and len(S.centre_basis(GA.sig(p, q))) == centre
            tested += 1
    ok = ok and tested == 44
    # the two rows of the table, read from the derived types
    rowk0 = [predicted(k, 0)[3:] for k in range(1, 9)]
    row0k = [predicted(0, k)[3:] for k in range(1, 9)]
    ok = ok and rowk0 == [("R", 2, 1), ("R", 1, 2), ("C", 1, 2), ("H", 1, 2), ("H", 2, 2),
                          ("H", 1, 4), ("C", 1, 8), ("R", 1, 16)]
    ok = ok and row0k == [("C", 1, 1), ("H", 1, 1), ("H", 2, 1), ("H", 1, 2), ("C", 1, 4),
                          ("R", 1, 8), ("R", 2, 8), ("R", 1, 16)]
    GA.check("table of Cl(p,q), n <= 8: dimension, centre and trace-form excess as predicted", ok)
    return ok


def check_periodicity_of_the_invariant():
    ok = True
    tested = 0
    for n in range(0, 9):
        for q in range(n + 1):
            p = n - q
            t = trace_form_excess(p, q)
            if n + 2 <= 10:
                ok = ok and trace_form_excess(p + 1, q + 1) == 2 * t
            if n == 0 or n == 1:
                ok = ok and trace_form_excess(p + 8, q) == 16 * t
                ok = ok and trace_form_excess(p, q + 8) == 16 * t
            tested += 1
    ok = ok and tested == 45
    GA.check("trace-form excess doubles under (p,q) -> (p+1,q+1) and scales by 16 under +8", ok)
    return ok
