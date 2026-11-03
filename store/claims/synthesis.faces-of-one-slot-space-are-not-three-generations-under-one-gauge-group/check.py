"""The three faces of one three-spinor slot space as generations under one gauge group: exact checks.

Slot space S = span(e_0, e_1, e_2) (three slots), face planes S_F for F in {01, 02, 12}, realised in
the Euclidean algebra Cl(3,0) so that "X maps S_F into S_F" is the vanishing of X(e_a) ^ B_F for the
face blade B_F = e_a e_b and a in F (exact outer products from the library).
(i)   For each pair of faces the joint stabiliser {X in gl(3, Q) : X S_F in S_F, X S_G in S_G} is computed
      in full by exact elimination (dimension 5); every element maps the common slot line into itself,
      so in both planes the common line is invariant and neither plane is irreducible for any Lie
      algebra inside the joint stabiliser.  Contrast: the stabiliser of one plane (dimension 7) contains
      E_ab, E_ba, which act on S_F with no common eigenvector (an irreducible sl(2)).
(ii)  Weak weights: with the weak U(2) of face 01 (T_3 = (n_0 - n_1)/2 on the slot occupation numbers)
      the even half of face 01 has the symmetric T_3 multiset {-1/2: 4, 0: 8, 1/2: 4}; the even halves of
      faces 02 and 12 have {0: 8, 1/2: 8} and {-1/2: 8, 0: 8}, not symmetric, so they are not invariant.
(iii) Single state space V = Lambda(S + W), W = three pair modes (64 exterior states): the face modules
      Lambda(S_F + W) span 56 states; with chirality the mode-number parity their even halves (16 each)
      span 28 of the 32 even states; the four slot-free states lie in all three faces, the twelve
      one-slot states in two faces each, the twelve two-slot states in one face each; over all eight
      per-face choices of half the span is at most 40; three generations need 48.
(iv)  Separate pair modes per face (nine pair modes, slots shared): the even halves share only the
      vacuum and span 46, at most 47 over the eight per-face choices; still fewer than 48.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
import GA
from tp_premise import premise

SQ3 = GA.sig(3, 0)
FACES = [(0, 1), (0, 2), (1, 2)]
NSLOT = 3
NPAIR = 3


def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x != 0}


E = [vec([1 if i == j else 0 for i in range(NSLOT)]) for j in range(NSLOT)]


def wedge_vb(v, B):
    """Outer product of a vector with a bivector: (vB + Bv)/2."""
    return GA.scal(F(1, 2), GA.add(GA.mul(v, B, SQ3), GA.mul(B, v, SQ3)))


def apply(X, v):
    c = [v.get((j,), F(0)) for j in range(NSLOT)]
    return vec([sum(X[i][j] * c[j] for j in range(NSLOT)) for i in range(NSLOT)])


def unit(k):
    return [[F(1) if NSLOT * i + j == k else F(0) for j in range(NSLOT)] for i in range(NSLOT)]


def face_blade(Fc):
    return GA.mul(E[Fc[0]], E[Fc[1]], SQ3)


def stab_rows(Fc):
    B = face_blade(Fc)
    rows = []
    for a in Fc:
        cols = [wedge_vb(apply(unit(k), E[a]), B) for k in range(NSLOT * NSLOT)]
        for b in sorted({b for c in cols for b in c}):
            rows.append([c.get(b, F(0)) for c in cols])
    return rows


def nullspace(rows, n):
    M = [r[:] for r in rows]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    basis = []
    for fc in [c for c in range(n) if c not in piv]:
        x = [F(0)] * n
        x[fc] = F(1)
        for i, pc in enumerate(piv):
            x[pc] = -M[i][fc]
        basis.append(x)
    return basis


def as_mat(x):
    return [[x[NSLOT * i + j] for j in range(NSLOT)] for i in range(NSLOT)]


def preserves(X, Fc):
    B = face_blade(Fc)
    return all(GA.is_zero(wedge_vb(apply(X, E[a]), B)) for a in Fc)


def check_joint_stabiliser_keeps_the_common_line():
    premise("families.three-identical-families-mixing-shared-slots")
    premise("standard-model.hyp-s-slot-statistics")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    ok = True
    for F1, F2 in combinations(FACES, 2):
        basis = nullspace(stab_rows(F1) + stab_rows(F2), NSLOT * NSLOT)
        ok = ok and len(basis) == 5
        line = [i for i in F1 if i in F2][0]
        for x in basis:
            X = as_mat(x)
            ok = ok and preserves(X, F1) and preserves(X, F2)
            img = apply(X, E[line])
            # common line invariant: X e_line ^ e_line = 0
            ok = ok and GA.is_zero(GA.sub(GA.mul(img, E[line], SQ3), GA.mul(E[line], img, SQ3)))
        # completeness of the solved space: a matrix outside it fails (the swap of the two non-common slots)
        o1 = [i for i in F1 if i != line][0]
        o2 = [i for i in F2 if i != line][0]
        Z = [[F(0)] * NSLOT for _ in range(NSLOT)]
        Z[o1][line] = F(1)  # moves the common line into the first plane, out of the second
        ok = ok and preserves(Z, F1) and not preserves(Z, F2)
    # contrast: one plane's stabiliser has dimension 7 and contains an irreducible sl(2) on the plane
    single = nullspace(stab_rows((0, 1)), NSLOT * NSLOT)
    ok = ok and len(single) == 7
    Eab = [[F(0)] * NSLOT for _ in range(NSLOT)]
    Eab[0][1] = F(1)
    Eba = [[F(0)] * NSLOT for _ in range(NSLOT)]
    Eba[1][0] = F(1)
    ok = ok and preserves(Eab, (0, 1)) and preserves(Eba, (0, 1))
    # no common eigenline in the plane: Eab fixes only the line of e_0, Eba only that of e_1
    ok = ok and GA.is_zero(apply(Eab, E[0])) and not GA.is_zero(apply(Eba, E[0]))
    ok = ok and GA.is_zero(apply(Eba, E[1])) and not GA.is_zero(apply(Eab, E[1]))
    GA.check("joint stabiliser of two face planes fixes their common line; one plane carries sl(2)", ok)
    return ok


# ------------------------------------------------------------- exterior states of Lambda(S + W)
MODES = NSLOT + NPAIR
STATES = [frozenset(s) for k in range(MODES + 1) for s in combinations(range(MODES), k)]
INDEX = {s: i for i, s in enumerate(STATES)}


def face_states(Fc, parity=None):
    return [s for s in STATES if {m for m in s if m < NSLOT} <= set(Fc)
            and (parity is None or len(s) % 2 == parity)]


def span_dim(lists):
    vecs = []
    for s in set().union(*[set(L) for L in lists]):
        v = [F(0)] * len(STATES)
        v[INDEX[s]] = F(1)
        vecs.append(v)
    return GA.rank_of_vectors(vecs)


def check_weak_weights_of_the_other_faces():
    premise("standard-model.hyp-s-slot-statistics")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("families.three-identical-families-mixing-shared-slots")
    mult = {}
    for Fc in FACES:
        t3 = Counter()
        for s in face_states(Fc, 0):
            t3[F(int(0 in s) - int(1 in s), 2)] += 1
        mult[Fc] = t3
    ok = mult[(0, 1)] == Counter({F(-1, 2): 4, F(0): 8, F(1, 2): 4})
    ok = ok and mult[(0, 2)] == Counter({F(0): 8, F(1, 2): 8})
    ok = ok and mult[(1, 2)] == Counter({F(-1, 2): 8, F(0): 8})
    # a weight multiset of an su(2) representation is symmetric under T3 -> -T3
    sym = {Fc: all(m[w] == m[-w] for w in m) for Fc, m in mult.items()}
    ok = ok and sym[(0, 1)] and not sym[(0, 2)] and not sym[(1, 2)]
    GA.check("under the weak U(2) of one face the other faces' halves are not invariant", ok)
    return ok


def check_face_halves_span_twenty_eight():
    premise("standard-model.hyp-s-slot-statistics")
    premise("families.three-identical-families-mixing-shared-slots")
    ok = len(STATES) == 64
    ok = ok and all(len(face_states(Fc)) == 32 and len(face_states(Fc, 0)) == 16 for Fc in FACES)
    ok = ok and span_dim([face_states(Fc) for Fc in FACES]) == 56
    even_total = sum(1 for s in STATES if len(s) % 2 == 0)
    ok = ok and even_total == 32
    ok = ok and span_dim([face_states(Fc, 0) for Fc in FACES]) == 28
    # sharing pattern by slot number j
    cnt = Counter()
    for Fc in FACES:
        for s in face_states(Fc, 0):
            cnt[s] += 1
    pattern = Counter()
    for s, c in cnt.items():
        pattern[(len([m for m in s if m < NSLOT]), c)] += 1
    ok = ok and pattern == Counter({(0, 3): 4, (1, 2): 12, (2, 1): 12})
    best = max(span_dim([face_states(Fc, p) for Fc, p in zip(FACES, par)])
               for par in product((0, 1), repeat=3))
    ok = ok and best == 40 and best < 3 * 16
    GA.check("three face halves span 28 of 32 even states (at most 40 with mixed halves) < 48", ok)
    return ok


def sep_face_states(i, Fc, parity=None):
    """Separate pair modes: face i owns pair modes NSLOT + NPAIR*i + j; slots shared."""
    modes = list(Fc) + [NSLOT + NPAIR * i + j for j in range(NPAIR)]
    return [frozenset(s) for k in range(len(modes) + 1) for s in combinations(modes, k)
            if parity is None or k % 2 == parity]


def sep_span(lists):
    allst = sorted(set().union(*[set(L) for L in lists]), key=sorted)
    pos = {s: n for n, s in enumerate(allst)}
    vecs = []
    for L in lists:
        for s in L:
            v = [F(0)] * len(allst)
            v[pos[s]] = F(1)
            vecs.append(v)
    return GA.rank_of_vectors(vecs)


def check_separate_pair_modes_span_forty_six():
    premise("standard-model.hyp-s-slot-statistics")
    premise("families.three-identical-families-mixing-shared-slots")
    halves = [sep_face_states(i, Fc, 0) for i, Fc in enumerate(FACES)]
    ok = all(len(h) == 16 for h in halves)
    ok = ok and sep_span(halves) == 46
    # the only state common to two even halves is the vacuum
    common = set(halves[0]) & set(halves[1]) | set(halves[0]) & set(halves[2]) | set(halves[1]) & set(halves[2])
    ok = ok and common == {frozenset()}
    best = max(sep_span([sep_face_states(i, Fc, p) for (i, Fc), p in zip(enumerate(FACES), par)])
               for par in product((0, 1), repeat=3))
    ok = ok and best == 47 and best < 3 * 16
    GA.check("separate pair modes: even halves span 46 (at most 47) < 48", ok)
    return ok


if __name__ == "__main__":
    check_joint_stabiliser_keeps_the_common_line()
    check_weak_weights_of_the_other_faces()
    check_face_halves_span_twenty_eight()
    check_separate_pair_modes_span_forty_six()
