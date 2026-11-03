"""families.three-identical-families-mixing-shared-slots: exact checks of the combinatorial and
transport content, ported from legacy verify_T13.py (prop:identical) and widened.

Slots are 1..N; a face is a two-element subset. A three-spinor system is three conformal spinors
Z^1, Z^2, Z^3 in C^4 over GA.QI (omega, pi parts); the face-F composite is Z^a ^ Z^b (a < b in F), its
bracket <pi^a pi^b> and its mass 2|<pi^a pi^b>|^2. The face-F gauge action is U(2) on the two slots of F,
embedded in GL(3) as E_F(U).
  (1) At the three-spinor bound N = 3: C(3,2) = 3 faces, every two distinct faces share exactly one slot;
      for N = 4, 5, 6 there are disjoint faces, so the intersection count is a property of the bound.
  (2) S_3 acts transitively on the faces (orbit of each face is all three, stabiliser of order 2), and a
      slot permutation sigma carries the face-F copy onto the face-sigma(F) copy: relabelling the system
      (Z'^{sigma(i)} = Z^i) sends the composite on F to +-the composite on sigma(F) (sign = orientation),
      with the same bracket modulus and mass, and P_sigma E_F(U) P_sigma^{-1} = E_{sigma(F)}(U') with U' = U
      or its slot-swapped conjugate (an isomorphism of the face gauge actions), for all 6 sigma, 3 faces
      and 3 unitaries.
  (3) Observation-level structure, counted: the face overlap matrix |F cap F'| has no zero entry, every
      off-diagonal entry is 1, and passing between any two faces changes exactly one slot (no double
      transition between faces).
The identification of faces with physical families and the CKM reading are not computable and are not
tested; the lepton part under Hypothesis (S) enters only as part of the copy's content, which (2)
transports as a whole.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

import GA
from tp_premise import premise

Q0, Q1 = GA.qi(0), GA.qi(1)
SYSTEM = {1: [GA.qi(1), GA.qi(2, 1), GA.qi(0, 1), GA.qi(3)],
          2: [GA.qi(-1), GA.qi(0), GA.qi(2, -1), GA.qi(1, 1)],
          3: [GA.qi(F(1, 2)), GA.qi(1, 3), GA.qi(4), GA.qi(-2, F(1, 3))]}
UNITARIES = [[[GA.qi(F(3, 5)), GA.qi(F(4, 5))], [GA.qi(F(-4, 5)), GA.qi(F(3, 5))]],
             [[GA.qi(F(3, 5), F(4, 5)), Q0], [Q0, Q1]],
             [[GA.qi(F(5, 13)), GA.qi(0, F(12, 13))], [GA.qi(0, F(12, 13)), GA.qi(F(5, 13))]]]


def faces(n):
    return [frozenset(c) for c in combinations(range(1, n + 1), 2)]


def composite(system, face):
    a, b = sorted(face)
    za, zb = system[a], system[b]
    return [za[i] * zb[j] - za[j] * zb[i] for i in range(4) for j in range(i + 1, 4)]


def bracket(system, face):
    a, b = sorted(face)
    return system[a][2] * system[b][3] - system[a][3] * system[b][2]


def embed(face, U):
    a, b = sorted(face)
    M = [[Q1 if i == j else Q0 for j in range(3)] for i in range(3)]
    for r, i in enumerate((a, b)):
        for c, j in enumerate((a, b)):
            M[i - 1][j - 1] = U[r][c]
    return M


def perm_matrix(sig):
    return [[Q1 if sig[j + 1] == i + 1 else Q0 for j in range(3)] for i in range(3)]


mm = GA.field_mat_mul  # dense product over GA.QI


def check_three_faces_meet_in_one_slot():
    premise("families.imported-face-valued-bracket-quantum-numbers")
    f3 = faces(3)
    ok = len(f3) == 3 and all(len(a & b) == 1 for a, b in combinations(f3, 2))
    for n in (4, 5, 6):
        fn = faces(n)
        ok = ok and len(fn) == n * (n - 1) // 2 and min(len(a & b) for a, b in combinations(fn, 2)) == 0
    GA.check("three faces at the bound, pairwise sharing exactly one slot", ok)
    assert ok


def check_slot_permutations_carry_copies():
    premise("families.imported-one-derived-generation-hypothesis-s")
    f3 = faces(3)
    ok = True
    for F0 in f3:
        orbit = {frozenset(s[x - 1] for x in F0) for s in permutations((1, 2, 3))}
        stab = [s for s in permutations((1, 2, 3)) if frozenset(s[x - 1] for x in F0) == F0]
        ok = ok and orbit == set(f3) and len(stab) == 2
    for p in permutations((1, 2, 3)):
        sig = {i + 1: p[i] for i in range(3)}
        relabelled = {sig[i]: SYSTEM[i] for i in SYSTEM}
        P = perm_matrix(sig)
        Pinv = [[P[j][i] for j in range(3)] for i in range(3)]
        for Fc in f3:
            G = frozenset(sig[x] for x in Fc)
            a, b = sorted(Fc)
            orient = 1 if sig[a] < sig[b] else -1
            ok = ok and composite(relabelled, G) == [GA.qi(orient) * c for c in composite(SYSTEM, Fc)]
            br, br2 = bracket(SYSTEM, Fc), bracket(relabelled, G)
            ok = ok and br2 == GA.qi(orient) * br and br2 * br2.conj() == br * br.conj()
            for U in UNITARIES:
                Us = U if orient == 1 else [[U[1][1], U[1][0]], [U[0][1], U[0][0]]]
                ok = ok and mm(mm(P, embed(Fc, U)), Pinv) == embed(G, Us)
    GA.check("S3 transitive on faces; a slot permutation carries one copy onto another", ok)
    assert ok


def check_overlap_structure_single_slot():
    f3 = faces(3)
    O = [[len(a & b) for b in f3] for a in f3]
    ok = all(O[i][j] > 0 for i in range(3) for j in range(3))
    ok = ok and all(O[i][j] == 1 for i in range(3) for j in range(3) if i != j)
    ok = ok and all(O[i][i] == 2 for i in range(3))
    ok = ok and all(len(a - b) == 1 for a, b in permutations(f3, 2))
    GA.check("overlap matrix has no zero entry; faces differ by exactly one slot", ok)
    assert ok
