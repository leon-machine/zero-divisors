"""synthesis.slot-parity-decides-hypothesis-s: exact checks.

Operators are built in the real Clifford algebra Cl(6,6) with GA.py: for mode m = 0..5,
e_m = gen(m) (square +1), f_m = gen(6 + m) (square -1), creation a_m^* = (e_m - f_m)/2 and
annihilation a_m = (e_m + f_m)/2, so that {a_m, a_n^*} = delta_mn and {a_m, a_n} = 0.
Modes 0, 1 carry the slots, 2, 3, 4 the pairs, 5 is a spectator whose Majorana generator
K = e_5 serves as the Klein factor. The tower's grading is GA.grade_inv.
Slot operators of tower parity pi: pi = 1, s_i = a_i; pi = 0, s_i = a_i K (even, a boson
made of fermions in the sense of the no-CCR theorem). Vacuum: P0 = prod_m a_m a_m^*.
"""
import GA
from GA import mul, add, sub, scal, sc, gen, grade_inv, eq, is_zero, rank_of_vectors
from tp_premise import premise
from fractions import Fraction as F
from itertools import combinations, product

SQ = GA.sig(6, 6)
NMODE = 6


def m(*xs):
    out = sc(1)
    for x in xs:
        out = mul(out, x, SQ)
    return out


def acomm(x, y):
    return add(mul(x, y, SQ), mul(y, x, SQ))


def comm(x, y):
    return sub(mul(x, y, SQ), mul(y, x, SQ))


E = [gen(i) for i in range(NMODE)]
FF = [gen(NMODE + i) for i in range(NMODE)]
ANN = [scal(F(1, 2), add(E[i], FF[i])) for i in range(NMODE)]
CRE = [scal(F(1, 2), sub(E[i], FF[i])) for i in range(NMODE)]
K = E[5]
P0 = m(*[m(ANN[i], CRE[i]) for i in range(NMODE)])
PAIR_A = ANN[2:5]
PAIR_C = CRE[2:5]


GP = m(*[sub(sc(1), scal(2, m(CRE[k], ANN[k]))) for k in range(2, 5)])   # (-1)^(pair number), even


def slots(pi, flip):
    """(annihilators, creators) of the two slot modes at tower parity pi; flip = 1 multiplies by
    (-1)^(pair number), which swaps commuting and anticommuting with the pairs at fixed parity."""
    if pi == 1:
        sa, sc_ = ANN[0:2], CRE[0:2]
    else:
        sa, sc_ = [m(ANN[i], K) for i in range(2)], [m(K, CRE[i]) for i in range(2)]
    if flip:
        sa, sc_ = [m(x, GP) for x in sa], [m(GP, x) for x in sc_]
    return sa, sc_


def parity_of(x):
    """+1 if x is even under the tower grading, -1 if odd, 0 if inhomogeneous."""
    g = grade_inv(x)
    if eq(g, x):
        return 1
    if eq(g, scal(-1, x)):
        return -1
    return 0


def state(sc_, J, K_):
    out = sc(1)
    for i in J:
        out = mul(out, sc_[i], SQ)
    for k in K_:
        out = mul(out, PAIR_C[k], SQ)
    return mul(out, P0, SQ)


def vec(x, blades):
    return [x.get(b, F(0)) for b in blades]


# ----- content table: (j, k) -> (SU(2) dim, SU(3) label, Y) with Y = (3j - 2k)/6 -----
SU2 = {0: 1, 1: 2, 2: 1}
SU3 = {0: "1", 1: "3", 2: "3b", 3: "1"}
DIM3 = {"1": 1, "3": 3, "3b": 3}


def half(pi, sign):
    """Components (j, k) whose tower parity (-1)^(pi j + k) equals sign."""
    return [(j, k) for j in range(3) for k in range(4) if (-1) ** ((pi * j + k) % 2) == sign]


def anomalies(comps, a, b, g):
    """The four imported conditions for the generator a j + b k + g on left-handed comps."""
    s33 = sum((SU2[j] * (a * j + b * k + g) for (j, k) in comps if SU3[k] != "1"), F(0))
    s22 = sum((DIM3[SU3[k]] * (a * j + b * k + g) for (j, k) in comps if j == 1), F(0))
    grav = sum((SU2[j] * DIM3[SU3[k]] * (a * j + b * k + g) for (j, k) in comps), F(0))
    cub = sum((SU2[j] * DIM3[SU3[k]] * (a * j + b * k + g) ** 3 for (j, k) in comps), F(0))
    return s33, s22, grav, cub


def check_slot_parity_decides_s():
    premise("field-theory.no-canonical-commutation-relations-tower")
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    premise("standard-model.imported-cauchy-decomposition-exterior-power")
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.global-form-quotient-determined")
    # CAR of the ambient modes, and the pairs are odd (chirality halves of Lambda W by parity of k)
    for i in range(NMODE):
        for j in range(NMODE):
            assert eq(acomm(ANN[i], CRE[j]), sc(1 if i == j else 0))
            assert is_zero(acomm(ANN[i], ANN[j]))
    assert all(parity_of(x) == -1 for x in PAIR_A + PAIR_C)
    assert all(is_zero(mul(ANN[i], P0, SQ)) for i in range(NMODE))
    # (1) covariance lemma: commuting two-level slots h0 = a0, h1 = a1 (1 - 2 n0) are not U(2)-covariant
    n0 = m(CRE[0], ANN[0])
    h0, h1 = ANN[0], m(ANN[1], sub(sc(1), scal(2, n0)))
    assert is_zero(mul(h0, h0, SQ)) and is_zero(mul(h1, h1, SQ)) and is_zero(comm(h0, h1))
    hp = add(h0, h1)                                  # rotated mode (up to normalisation)
    assert eq(mul(hp, hp, SQ), scal(2, mul(h0, h1, SQ))) and not is_zero(mul(h0, h1, SQ))
    # the doubly occupied hard-core state picks up the permanent, not the determinant
    c, s_ = F(3, 5), F(4, 5)
    h0c, h1c = m(CRE[0]), m(sub(sc(1), scal(2, n0)), CRE[1])
    r0 = add(scal(c, h0c), scal(s_, h1c))
    r1 = add(scal(-s_, h0c), scal(c, h1c))
    two = mul(h0c, mul(h1c, P0, SQ), SQ)
    assert eq(mul(r0, mul(r1, P0, SQ), SQ), scal(c * c - s_ * s_, two))   # perm = -7/25, det = 1
    assert c * c - s_ * s_ == F(-7, 25)
    results = {}
    for (pi, flip) in ((1, 0), (0, 0), (1, 1), (0, 1)):
        sa, sc_ = slots(pi, flip)
        # slot parity, two-level CAR among slots, and +-commutation with the pairs
        assert all(parity_of(x) == (-1 if pi else 1) for x in sa + sc_)
        for i in range(2):
            for j in range(2):
                assert eq(acomm(sa[i], sc_[j]), sc(1 if i == j else 0))
                assert is_zero(acomm(sa[i], sa[j]))
            for k in range(3):
                rel = acomm if (pi + flip) % 2 else comm
                assert is_zero(rel(sa[i], PAIR_A[k])) and is_zero(rel(sa[i], PAIR_C[k]))
            assert is_zero(mul(sa[i], P0, SQ))
        # U(2)-covariance on a rational rotation: rotated slots still CAR, double state goes by det
        ra = [add(scal(c, sa[0]), scal(s_, sa[1])), add(scal(-s_, sa[0]), scal(c, sa[1]))]
        rc = [add(scal(c, sc_[0]), scal(s_, sc_[1])), add(scal(-s_, sc_[0]), scal(c, sc_[1]))]
        for i in range(2):
            for j in range(2):
                assert eq(acomm(ra[i], rc[j]), sc(1 if i == j else 0))
                assert is_zero(acomm(ra[i], ra[j]))
        assert eq(m(rc[0], rc[1], P0), m(sc_[0], sc_[1], P0))                 # det = 1
        # the 32 states s_J^* b_K^* P0: linearly independent, tower parity (-1)^(pi j + k)
        sts, tab = [], {}
        for J in [(), (0,), (1,), (0, 1)]:
            for kk in range(4):
                for Kset in combinations(range(3), kk):
                    x = state(sc_, J, Kset)
                    p = parity_of(x)
                    assert p == (-1) ** ((pi * len(J) + kk) % 2)
                    tab[(len(J), kk)] = p
                    sts.append(x)
        blades = sorted(set(b for x in sts for b in x))
        assert len(sts) == 32 and rank_of_vectors([vec(x, blades) for x in sts]) == 32
        if (pi, flip) in results:
            assert results[(pi, flip)] == tab
        results[(pi, flip)] = tab
        if flip:
            assert tab == results[(pi, 0)]          # the mutual sign is invisible to the grading
    # (2) the tower grading equals (S)'s parity of total mode number iff pi is odd
    assert all(results[(1, 0)][(j, k)] == (-1) ** ((j + k) % 2) for (j, k) in results[(1, 0)])
    assert any(results[(0, 0)][(j, k)] != (-1) ** ((j + k) % 2) for (j, k) in results[(0, 0)])
    # (3) anomalies. pi odd: the even half is the derived generation; Y = (3j - 2k)/6 passes all four
    Hodd = half(1, 1)
    assert sorted(Hodd) == [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]
    assert anomalies(Hodd, F(1, 2), F(-1, 3), F(0)) == (0, 0, 0, 0)
    # pi even: the even half is Qbar + Lbar + u^c + d^c + e^c + nu^c
    Hev = half(0, 1)
    assert sorted(Hev) == [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)]
    a33, a22, agr, acu = anomalies(Hev, F(1, 2), F(-1, 3), F(0))
    assert (a33, a22, agr, acu) == (F(-2, 3), F(0), F(0), F(4, 9))
    # same for the opposite half (conjugate listing): sums negate
    assert anomalies(half(0, -1), F(1, 2), F(-1, 3), F(0)) == (F(2, 3), F(0), F(0), F(-4, 9))
    # general abelian generator a j + b k + g: linear sums on each half, as linear forms in (a, b, g)
    def lin(comps):
        rows = []
        for idx in range(3):
            basis = [F(0)] * 3
            basis[idx] = F(1)
            rows.append(anomalies(comps, *basis)[:3])
        return [[rows[idx][t] for idx in range(3)] for t in range(3)]   # 3 conditions x (a, b, g)
    Lodd, Lev = lin(Hodd), lin(Hev)
    assert Lodd == [[4, 6, 4], [4, 6, 4], [16, 24, 16]]
    assert Lev == [[4, 8, 4], [4, 6, 4], [16, 24, 16]]
    assert rank_of_vectors(Lodd) == 1 and rank_of_vectors(Lev) == 2
    # pi even: kernel is a (j - 1); its cubic vanishes; every generator with b != 0 fails a linear one
    assert anomalies(Hev, F(1), F(0), F(-1)) == (0, 0, 0, 0)
    for (a, b, g) in product(range(-3, 4), range(-3, 4), range(-3, 4)):
        lv = anomalies(Hev, F(a), F(b), F(g))[:3]
        if lv == (0, 0, 0):
            assert b == 0 and g == -a
    # colour content of each half (cubic SU(3) anomaly, cited from memory: triplets minus antitriplets)
    def cubic3(comps):
        return sum(SU2[j] * (1 if SU3[k] == "3" else -1 if SU3[k] == "3b" else 0) for (j, k) in comps)
    assert cubic3(Hodd) == 0 and cubic3(Hev) == -4
    return True

