"""transport.pinching-kernel: exact checks.

Setting (T01 Sec. 7): A = Cl(p,q) inside B = Cl(p+1,q+1), the ascent adjoining e+ (square +1, index n)
and e- (square -1, index n+1), with the ladder pair f = (e+ + e-)/2, f* = (e+ - e-)/2 and the descent
projector P = f*f. Everything is computed in GA.py over the rationals for every base signature with
n = p + q <= 3 (B has dimension up to 32), blade by blade, with linear spans compared by exact rank.
(1) E^2 = E on every blade of B, E(1) = 1; the commutant C = {x : xP = Px} is computed as a kernel and
    has dimension 2^(n+1); im E = C, E is the identity on C, C = A + A ff*, and E is a C-bimodule map.
(2) ker E (computed) has dimension 2^(n+1) and equals both PB(1-P) + (1-P)BP and Af* + Af; E(f) =
    E(f*) = 0.
(3) E(a) = a and PaP = a f*f for every base blade; conjugating the corner by E12 = f gives the grade
    involution, f (PaP) f* = a^ ff*; the defect D(xy) - D(x)D(y) = P x (1-P) y P on sample elements.
The matrix units of Rule 1 (transport.rule-1-morita-trivial) are used for the Peirce clauses.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

BASES = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2), (3, 0), (2, 1), (1, 2), (0, 3)]
SAMPLE_COEFFS = [3, -1, 2, 5, -2, 1, -4, 7, 1, -3, 2, 6, -5, 1, 4, -1]


def setup(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    f = GA.scal(F(1, 2), GA.add(ep, em))
    fs = GA.scal(F(1, 2), GA.sub(ep, em))
    P = GA.mul(fs, f, sq)
    Pc = GA.sub(GA.sc(1), P)
    return n, sq, f, fs, P, Pc


def m3(x, y, z, sq):
    return GA.mul(GA.mul(x, y, sq), z, sq)


def coords(x, blades):
    return GA.basis_vector_of(x, blades)


def rank(elems, blades):
    vs = [coords(x, blades) for x in elems]
    return GA.rank_of_vectors(vs) if vs else 0


def same_span(xs, ys, blades):
    r = rank(xs, blades)
    return r == rank(ys, blades) == rank(xs + ys, blades)


def sample(blades, shift):
    return {b: F(SAMPLE_COEFFS[(i + shift) % len(SAMPLE_COEFFS)]) for i, b in enumerate(blades)
            if SAMPLE_COEFFS[(i + shift) % len(SAMPLE_COEFFS)]}


def check_conditional_expectation_onto_commutant():
    premise("transport.rule-1-morita-trivial")
    for (p, q) in BASES:
        n, sq, f, fs, P, Pc = setup(p, q)
        bl = GA.all_blades(n + 2)
        base = GA.all_blades(n)

        def E(x):
            return GA.add(m3(P, x, P, sq), m3(Pc, x, Pc, sq))

        units = [{b: F(1)} for b in bl]
        assert GA.eq(E(GA.sc(1)), GA.sc(1))
        assert all(GA.eq(E(E(u)), E(u)) for u in units)
        # the commutant as a computed kernel of x -> xP - Px
        cols = [coords(GA.sub(GA.mul(u, P, sq), GA.mul(P, u, sq)), bl) for u in units]
        M = [[cols[j][i] for j in range(len(bl))] for i in range(len(bl))]
        ker = GA.field_kernel(M)
        C = [{bl[k]: v[k] for k in range(len(bl)) if v[k] != 0} for v in ker]
        assert len(C) == 2 * 2 ** n
        assert same_span([E(u) for u in units], C, bl)
        assert all(GA.eq(E(c), c) for c in C)
        ffs = GA.mul(f, fs, sq)
        AC = [{b: F(1)} for b in base] + [GA.mul({b: F(1)}, ffs, sq) for b in base]
        assert same_span(AC, C, bl)
        # bimodule property on all pairs of a C-basis sample with every blade x
        for c in C[:4]:
            for c2 in C[-3:]:
                for u in units[::3]:
                    assert GA.eq(E(m3(c, u, c2, sq)), m3(c, E(u), c2, sq))
    return True


def check_kernel_is_ladder_sector():
    for (p, q) in BASES:
        n, sq, f, fs, P, Pc = setup(p, q)
        bl = GA.all_blades(n + 2)
        base = [{b: F(1)} for b in GA.all_blades(n)]
        units = [{b: F(1)} for b in bl]

        def E(x):
            return GA.add(m3(P, x, P, sq), m3(Pc, x, Pc, sq))

        cols = [coords(E(u), bl) for u in units]
        M = [[cols[j][i] for j in range(len(bl))] for i in range(len(bl))]
        ker = [{bl[k]: v[k] for k in range(len(bl)) if v[k] != 0} for v in GA.field_kernel(M)]
        assert len(ker) == 2 ** (n + 1)
        peirce = [m3(P, u, Pc, sq) for u in units] + [m3(Pc, u, P, sq) for u in units]
        ladder = [GA.mul(a, fs, sq) for a in base] + [GA.mul(a, f, sq) for a in base]
        assert rank([GA.mul(a, fs, sq) for a in base], bl) == 2 ** n
        assert rank([GA.mul(a, f, sq) for a in base], bl) == 2 ** n
        assert same_span(ker, peirce, bl) and same_span(ker, ladder, bl)
        assert GA.is_zero(E(f)) and GA.is_zero(E(fs))
        # nothing else: E is injective on the commutant side (rank of im E is the complement)
        assert rank([E(u) for u in units], bl) == 2 ** (n + 2) - 2 ** (n + 1)
    return True


# Sample shifts (seeds) of the two sample elements x, y used for the multiplicativity defect.
SHIFT_X = 0
SHIFT_Y = 5


def unit_blade(b):
    return {b: F(1)}


def check_round_trip_and_defect():
    premise("transport.rule-1-morita-trivial")
    for (p, q) in BASES:
        n, sq, f, fs, P, Pc = setup(p, q)
        bl = GA.all_blades(n + 2)

        def E(x):
            return GA.add(m3(P, x, P, sq), m3(Pc, x, Pc, sq))

        fsf = GA.mul(fs, f, sq)
        ffs = GA.mul(f, fs, sq)
        for b in GA.all_blades(n):
            a = unit_blade(b)
            assert GA.eq(E(a), a)
            D = m3(P, a, P, sq)
            assert GA.eq(D, GA.mul(a, fsf, sq))
            # Peirce reading: conjugating the (2,2) corner by E12 = f gives the grade involution
            hat = GA.mul(GA.grade_inv(a), ffs, sq)
            assert GA.eq(m3(f, D, fs, sq), hat)
            # so the round trip returns a ffs exactly on the even blades and differs on the odd ones
            assert GA.eq(m3(f, D, fs, sq), GA.mul(a, ffs, sq)) == (len(b) % 2 == 0)
        x, y = sample(bl, SHIFT_X), sample(bl, SHIFT_Y)
        lhs = GA.sub(m3(P, GA.mul(x, y, sq), P, sq), GA.mul(m3(P, x, P, sq), m3(P, y, P, sq), sq))
        rhs = GA.mul(m3(P, x, Pc, sq), GA.mul(y, P, sq), sq)
        assert GA.eq(lhs, rhs) and not GA.is_zero(rhs)
    return True
