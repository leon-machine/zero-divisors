"""dark-tower-matter.three-dimensional-content: exact checks.

(i)   The cells of R^2 (x) R^2 and their weights are computed: with J = [[0,-1],[1,0]] the slot and
      pair rotations are J (x) 1 and 1 (x) J on R^4; over Q(i) (GA.QI) the four simultaneous
      eigenvectors (1, -s i) (x) (1, -p i) have eigenvalues (i s, i p), so the weights are
      {+-1}^2. With q_+- = (s +- p)/2 the cell (1,1) is A with (q_+, q_-) = (1, 0), (1,-1) is B
      with (0, 1), the other two are their conjugates; each is charged under one factor only, and
      p -> -p exchanges A and B.
(ii)  All 16 states of the exterior algebra of the cells: every weight has s + p even, and
      (+-1, 0), (0, +-1) do not occur; q_+- are integers exactly on the lattice s + p even (checked
      for |s|, |p| <= 4).
(iii) The weights (+-1, 0) (constituent level under (S), rung directions) and (0, +-1) (pair
      directions) are off the lattice; the neutral (0, 0) is on it. (The transported directions'
      weights are imported from the supplementary script D3R; only the lattice test is checked.)
(iv)  No chirality: in Cl(1,2) and Cl(2,1) no nonzero element anticommutes with every vector
      (exact kernel of x -> (x e_a + e_a x)_a), while in Cl(1,3) the pseudoscalar does (control);
      a Dirac mass Abar A has weight zero; over all occupations (0..2 per two-component species)
      of A, B and their conjugates, a state is gauge-neutral exactly when the net number of each
      cell vanishes.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise

QI = GA.QI
J2 = [[0, -1], [1, 0]]
I2 = [[1, 0], [0, 1]]


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(2) for l in range(2)] for i in range(2) for k in range(2)]


def matvec(M, v):
    return [sum((QI(M[i][j]) * v[j] for j in range(len(v))), QI(0)) for i in range(len(M))]


def cell_weights():
    slot, pair = kron(J2, I2), kron(I2, J2)
    out = []
    for s in (1, -1):
        for p in (1, -1):
            a = [QI(1), QI(0, -s)]
            b = [QI(1), QI(0, -p)]
            v = [a[i] * b[k] for i in range(2) for k in range(2)]
            ws = [x for x in (1, -1) if matvec(slot, v) == [QI(0, x) * c for c in v]]
            wp = [x for x in (1, -1) if matvec(pair, v) == [QI(0, x) * c for c in v]]
            assert len(ws) == 1 and len(wp) == 1
            out.append((ws[0], wp[0]))
    return out


def charges(w):
    s, p = w
    return (F(s + p, 2), F(s - p, 2))


def check_cells_and_charges():
    premise("dark-tower-matter.gauge-algebras")
    cells = cell_weights()
    assert sorted(cells) == [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    A, B = charges((1, 1)), charges((1, -1))
    assert A == (1, 0) and B == (0, 1)
    assert charges((-1, -1)) == (-1, 0) and charges((-1, 1)) == (0, -1)
    for w in cells:
        qp, qm = charges(w)
        assert (qp == 0) != (qm == 0)                         # one factor only
    refl = [(w[0], -w[1]) for w in ((1, 1), (1, -1))]          # p -> -p swaps A and B
    assert charges(refl[0]) == B and charges(refl[1]) == A
    return True


def check_exterior_weights_on_lattice():
    premise("dark-tower-matter.gauge-algebras")
    cells = cell_weights()
    weights = set()
    nstates = 0
    for k in range(5):
        for sub in combinations(range(4), k):
            weights.add((sum(cells[i][0] for i in sub), sum(cells[i][1] for i in sub)))
            nstates += 1
    assert nstates == 16
    assert all((s + p) % 2 == 0 for s, p in weights)
    for bad in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        assert bad not in weights
    assert (0, 0) in weights
    for s in range(-4, 5):
        for p in range(-4, 5):
            qp, qm = charges((s, p))
            assert (qp.denominator == 1 and qm.denominator == 1) == ((s + p) % 2 == 0)
    # (iii): constituent level / rung directions (+-1, 0), pair directions (0, +-1) are off the
    # lattice; the neutral leftover direction (0, 0) is on it
    for w in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        assert (w[0] + w[1]) % 2 == 1
    return True


def check_no_chirality_and_neutral_states():
    premise("dark-matter.two-families-are-two-chiralities")
    for (p, q, expect) in ((1, 2, 0), (2, 1, 0), (1, 3, 1)):
        n = p + q
        S = GA.sig(p, q)
        blades = GA.all_blades(n)
        rows = []
        for a in range(n):
            imgs = [GA.add(GA.mul({K: F(1)}, GA.gen(a), S), GA.mul(GA.gen(a), {K: F(1)}, S)) for K in blades]
            for b in blades:
                rows.append([img.get(b, F(0)) for img in imgs])
        assert len(GA.field_kernel(rows)) == expect
    # a Dirac mass term Abar A is neutral
    A = charges((1, 1))
    Abar = charges((-1, -1))
    assert (A[0] + Abar[0], A[1] + Abar[1]) == (0, 0)
    # gauge-neutral states have zero net number of each cell
    species = [charges((1, 1)), charges((-1, -1)), charges((1, -1)), charges((-1, 1))]   # A, Abar, B, Bbar
    neutral = 0
    for occ in product(range(3), repeat=4):
        qp = sum(o * c[0] for o, c in zip(occ, species))
        qm = sum(o * c[1] for o, c in zip(occ, species))
        if qp == 0 and qm == 0:
            neutral += 1
            assert occ[0] == occ[1] and occ[2] == occ[3]
    assert neutral == 9
    return True
