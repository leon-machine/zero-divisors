"""synthesis.anomaly-freedom-forces-slot-content: exact checks.

The particle half of F (x) Lambda W, F a graded polynomial U(2)-module of slot quanta, W the
three-mode pair space, Y = (3n - 2k)/6, chirality the tower grading (-1)^(pi n + k), pi in {0, 1};
mixed sums in the normalisation of the imported Fact (doublet and triplet weight one). Anomaly sums are computed
by direct summation over components and compared with the closed forms; the classification is
confirmed by exhausting small multiplicities; parafermionic slot spaces are built from Green's
ansatz with exact integer matrices. Fractions only.
"""
from fractions import Fraction as F
from itertools import product

import GA
from pyutil import get_or_set
from tp_premise import premise

# pair grades k = 0..3: (colour dimension, cubic anomaly A with 3bar = -1, weight in the Fact's [SU(3)]^2 U(1) sum:
# 1 for a triplet or antitriplet, 0 for a singlet)
PAIR = {0: (1, 0, F(0)), 1: (3, 1, F(1)), 2: (3, -1, F(1)), 3: (1, 0, F(0))}


def irrep_data(l1, l2):
    n = l1 + l2
    j = F(l1 - l2, 2)
    d = l1 - l2 + 1
    tau = F(2, 3) * j * (j + 1) * (2 * j + 1)      # twice the Dynkin index: a doublet counts 1
    return n, j, d, tau


def sums(l1, l2, pi=1):
    """(grav, SU2^2 Y, SU3^2 Y, Y^3, SU3^3, Witten parity count) of the particle half of F_lambda (x) Lambda W,
    particle half = the +1 part of the tower grading (-1)^(pi n + k); mixed sums in the Fact's normalisation."""
    n, j, d, T = irrep_data(l1, l2)
    g = s2 = s3 = y3 = c3 = w = F(0)
    for k in range(4):
        if (pi * n + k) % 2:
            continue
        d3, A3, T3 = PAIR[k]
        Y = F(3 * n - 2 * k, 6)
        g += d * d3 * Y
        s2 += d3 * T * Y
        s3 += d * T3 * Y
        y3 += d * d3 * Y ** 3
        c3 += d * A3
        if j.denominator == 2:
            w += d3 * T
    return [g, s2, s3, y3, c3, w]


def total(mult, pi=1):
    tot = [F(0)] * 6
    for lam, m in mult.items():
        s = sums(lam[0], lam[1], pi)
        tot = [tot[i] + m * s[i] for i in range(6)]
    return tot


def four_conditions_hold(mult, pi=1):
    t = total(mult, pi)
    return t[0] == 0 and t[1] == 0 and t[2] == 0 and t[3] == 0


def green_slot_content(p):
    """Weight multiplicities of the order-p parafermionic Fock space on two modes (Green's ansatz)."""
    def create(i, vec):
        out = {}
        for st, amp in vec.items():
            for a in range(p):
                s = st[a]
                if (s >> i) & 1:
                    continue
                sign = -1 if (i == 1 and (s & 1)) else 1          # Jordan-Wigner inside one copy
                nst = st[:a] + (s | (1 << i),) + st[a + 1:]
                out[nst] = out.get(nst, 0) + sign * amp
        return {k: v for k, v in out.items() if v}
    frontier = [((0, 0), {tuple([0] * p): 1})]
    allv = list(frontier)
    for _ in range(2 * p):
        nxt = []
        for wgt, vec in frontier:
            for i in range(2):
                v2 = create(i, vec)
                if v2:
                    nxt.append(((wgt[0] + (i == 0), wgt[1] + (i == 1)), v2))
        frontier = nxt
        allv += nxt
    byw = {}
    for wgt, vec in allv:
        get_or_set(byw, wgt, []).append(vec)
    mult = {}
    for wgt, vecs in byw.items():
        keys = sorted({k for v in vecs for k in v})
        r = GA.rank_of_vectors([[F(v.get(k, 0)) for k in keys] for v in vecs])
        if r:
            mult[wgt] = r
    return mult


def decompose(weights):
    m = dict(weights)
    out = []
    while any(v > 0 for v in m.values()):
        top = max((w for w in m if m[w] > 0), key=lambda w: (w[0] + w[1], abs(w[0] - w[1])))
        l1, l2 = max(top), min(top)
        out.append((l1, l2))
        for a in range(l2, l1 + 1):
            m[(a, l1 + l2 - a)] -= 1
            assert m[(a, l1 + l2 - a)] >= 0
    return sorted(out)


def check_anomaly_freedom_forces_slot_content():
    premise("standard-model.imported-anomaly-coefficients")
    premise("standard-model.global-form-quotient-determined")
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    # (1) closed forms against direct sums, both slot parities
    for pi in (0, 1):
        for l1 in range(9):
            for l2 in range(l1 + 1):
                n, j, d, tau = irrep_data(l1, l2)
                g, s2, s3, y3, c3, w = sums(l1, l2, pi)
                assert g == 2 * d * (n - 1)
                assert s2 == 2 * tau * (n - 1)
                if pi == 1:
                    assert s3 == F(d, 6) * (3 * (n - 1) - (-1) ** n)
                    if l1 == l2:
                        a = l1
                        assert y3 == a ** 3 + 3 * (a - F(2, 3)) ** 3
                else:
                    assert s3 == F(d, 6) * (3 * n - 4)
                # (2) every term of the SU(2)^2 Y sum is >= 0, and > 0 exactly for weak multiplets with n >= 2
                assert s2 >= 0 and ((s2 > 0) == (l1 > l2 and n >= 2))
    # (2) the doublet is the Fact's unit: (1,0) at pi = 1 holds Q (3 colours) and L, tau = 1
    assert irrep_data(1, 0)[3] == 1 and irrep_data(2, 0)[3] == 4
    # (2) the reductions: x = sum (2a-1) z_a from gravity; y = +sum a z_a (pi = 1), -sum a z_a (pi = 0);
    # cubic g(a) = 2a(2a-1)(a-1) at pi = 1
    v00, v10 = sums(0, 0, 1), sums(1, 0, 1)
    assert v00[:4] == [-2, 0, F(-2, 3), F(-8, 9)] and v10[:4] == [0, 0, F(1, 3), F(-2, 9)]
    e00, e10 = sums(0, 0, 0), sums(1, 0, 0)
    assert e00[0] == -2 and e10[0] == 0 and e00[2] == F(-2, 3) and e10[2] == F(-1, 3)
    for a in range(1, 9):
        va = sums(a, a, 1)
        assert va[0] + (2 * a - 1) * v00[0] + a * v10[0] == 0
        assert va[2] + (2 * a - 1) * v00[2] + a * v10[2] == 0
        assert va[3] + (2 * a - 1) * v00[3] + a * v10[3] == 2 * a * (2 * a - 1) * (a - 1)
        ea = sums(a, a, 0)
        assert ea[0] + (2 * a - 1) * e00[0] == 0
        assert ea[2] + (2 * a - 1) * e00[2] - a * e10[2] == 0      # y = -sum a z_a
    # (2) m copies of Lambda C^2 are anomaly-free (four conditions, cubic SU(3), Witten parity)
    car = {(0, 0): 1, (1, 0): 1, (1, 1): 1}
    for m in range(1, 4):
        t = total({k: m * v for k, v in car.items()}, 1)
        assert t[:5] == [0, 0, 0, 0, 0] and t[5] % 2 == 0
        assert not four_conditions_hold({k: m * v for k, v in car.items()}, 0)
    # the listed content of one copy, (dim2, colour grade, Y) over the even components
    content = sorted((l1 - l2 + 1, k, F(3 * (l1 + l2) - 2 * k, 6)) for (l1, l2) in car for k in range(4)
                     if (l1 + l2 + k) % 2 == 0)
    assert content == sorted([(1, 0, F(0)), (1, 2, F(-2, 3)), (2, 1, F(1, 6)), (2, 3, F(-1, 2)),
                              (1, 0, F(1)), (1, 2, F(1, 3))])
    # (2) exhaust multiplicities 0..2 over the six lambda with lambda1 <= 2
    LAM = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]
    sols = {0: [], 1: []}
    for ms in product(range(3), repeat=len(LAM)):
        mult = {lam: m for lam, m in zip(LAM, ms) if m}
        for pi in (0, 1):
            if mult and four_conditions_hold(mult, pi):
                sols[pi].append(mult)
    assert sols[1] == [car, {k: 2 for k in car}] and sols[0] == []
    # (3) the highest weight (2,0) is not a weight of Lambda^2 C^2 (whose only weight is (1,1))
    lam2_weights = [(int(i == 0) + int(j == 0), int(i == 1) + int(j == 1)) for i in range(2) for j in range(i + 1, 2)]
    assert lam2_weights == [(1, 1)] and (2, 0) not in lam2_weights
    # (4) parafermionic slots: content and anomaly at p = 2
    dims = []
    for p in range(1, 5):
        irr = decompose(green_slot_content(p))
        assert irr == sorted((a, b) for a in range(p + 1) for b in range(a + 1))
        dims.append(sum(a - b + 1 for a, b in irr))
        assert ((2, 0) in irr) == (p >= 2)
        assert four_conditions_hold({lam: 1 for lam in irr}, 1) == (p == 1)
        assert not four_conditions_hold({lam: 1 for lam in irr}, 0)
    assert dims == [4, 10, 20, 35]
    t2 = total({lam: 1 for lam in decompose(green_slot_content(2))})
    assert t2[:4] == [20, 12, F(14, 3), F(254, 9)]
    return True
