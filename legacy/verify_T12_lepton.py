#!/usr/bin/env python3
"""
verify_T12_lepton.py: exact-arithmetic verification of the computational
identities of "The Lepton Inside the Hierarchy: The Constituent Space of the
Minimal Massive Composite" (companion note to Transport Papers T12).

Imports the series' shared library GA.py.  Everything is exact: rationals and
Gaussian rationals; no floating point.  Statement tags refer to the compiled
note.  v1.1 (2026-09-03): 17 checks (was 15).  Per the v3 review: the
hollow K-weight identity replaced by a real non-self-duality check on the
five-mode ledger's (content, K-weight) multiset (L9); the twist check now
tests the claim of Obs 3.2 (self-conjugacy fails for every m != 0) over
m in [-3, 3] (L3(a)); Prop 3.1's biconditional over subgroups G tested on
five subgroups through the lattice of trivial central characters, showing
the k = 0 test alone misses G = SU(2) x U(3) while k = 1 decides (L4); the
span dimensions of Prop 2.3(2) computed as ranks rather than typed (L9);
the Hom(Lambda^4, Lambda^1) content of Rem 2.4 checked (L5, L11).
v2.0 (2026-10-07): one check added for obs:thirteen, the twisted action of
T12 Prop 5.8(3)(b) is self-conjugate on the five-mode ledger: 18 checks.
"""

from fractions import Fraction as F
from itertools import combinations
from math import comb

import GA as g

# ---------------------------------------------------------------------------
# the hypercharge generator y = (3i I_2, -2i I_3) and the constituent space
# C_k = C^2 ox Lambda^k W with the unit action A ox Lambda^k(B)
# ---------------------------------------------------------------------------

X_y = [[g.qi(0, 3) if i == j else g.qi(0) for j in range(2)] for i in range(2)]
Y_y = [[g.qi(0, -2) if i == j else g.qi(0) for j in range(3)] for i in range(3)]


def ext_diag(Y, k):
    """Eigenvalues of a diagonal Y on Lambda^k C^3 in the wedge basis."""
    return [sum((Y[j][j] for j in S), g.qi(0)) for S in combinations(range(3), k)]


def unit_weight(k):
    """y on C^2 ox Lambda^k W: X acts on the slot (scalar 3i), Y on the pairs."""
    slot = X_y[0][0]
    eig = ext_diag(Y_y, k)
    assert all(e == eig[0] for e in eig)
    return slot + eig[0]


weights = [unit_weight(k) for k in range(4)]
g.check("prop:content(1): the hypercharge generator acts on C^2 ox Lambda^k W "
      "as the scalar i(3 - 2k): weights 3, 1, -1, -3, so Y = 1/2, 1/6, -1/6, "
      "-1/2 for k = 0, 1, 2, 3",
      weights == [g.qi(0, 3), g.qi(0, 1), g.qi(0, -1), g.qi(0, -3)])

SU3 = {0: "1", 1: "3", 2: "3bar", 3: "1"}
CONJ = {"1": "1", "3": "3bar", "3bar": "3"}
odd = sorted((SU3[k], F(weights[k].im, 6)) for k in (1, 3))
even = sorted((SU3[k], F(weights[k].im, 6)) for k in (0, 2))
g.check("prop:content(2): the odd half C^2 ox T' is {(2,3)_{1/6}, (2,1)_{-1/2}} "
      "= Q + L, both of odd grade hence one chirality half",
      odd == sorted([("3", F(1, 6)), ("1", F(-1, 2))]))
g.check("prop:content(3): the even half C^2 ox T is {(2,1)_{1/2}, (2,3bar)_{-1/6}} "
      "= the conjugate multiset of the odd half (L*, Q*), and the dual weight "
      "-(3-2k) equals the weight 3-2(3-k) of the grade-(3-k) constituent",
      sorted((CONJ[c], -y) for c, y in odd) == even
      and all(-weights[k] == weights[3 - k] for k in range(4)))

# lattice residues 2t + 3 delta + q = 0 mod 6 with delta = 1, t = 0, 1, -1, 0
T = {0: 0, 1: 1, 2: -1, 3: 0}
g.check("prop:content(4): the lattice residue 2t + 3 delta + q vanishes mod 6 on "
      "every constituent (delta = 1; t = 0, 1, -1, 0; q = 3, 1, -1, -3)",
      all((2 * T[k] + 3 * 1 + weights[k].im) % 6 == 0 for k in range(4)))

# ---------------------------------------------------------------------------
# the K-weights and self-conjugacy (prop:selfconj, obs:thirteen)
# ---------------------------------------------------------------------------

X_K = [[g.qi(0, 1) if i == j else g.qi(0) for j in range(2)] for i in range(2)]
Y_K = [[g.qi(0, -1) if i == j else g.qi(0) for j in range(3)] for i in range(3)]


def K_weight(k):
    eig = ext_diag(Y_K, k)
    return X_K[0][0] + eig[0]


kw = [K_weight(k).im for k in range(4)]
g.check("prop:selfconj: K = (lambda, lambda^-1) acts on C^2 ox Lambda^k W with "
      "weight 1 - k: 1, 0, -1, -2 (nontrivial for k != 1)",
      kw == [1, 0, -1, -2])

# the dual of C_k has K-weight -(1-k) = k-1; matching content needs j = 3-k;
# then K-weights 1-(3-k) = k-2 vs k-1: never equal
g.check("prop:selfconj: the dual of the grade-k constituent has K-weight k - 1, "
      "the grade-(3-k) constituent (the only one of matching content) has "
      "K-weight k - 2: the two never agree, so C is not self-dual under "
      "U(2) x U(3)", all((-(kw[k])) != kw[3 - k] for k in range(4))
      and all(kw[3 - k] == k - 2 for k in range(4)))

# on the determinant-one subgroup the twist det(A)det(B) is trivial: the
# dual weights under y already matched above; here check that the twist
# (det A det B) has y-weight 6 - 6 = 0 and K-weight 2 - 3 = -1 != 0
g.check("prop:selfconj: the twist det(A) det(B) has weight 0 under y and "
      "weight -1 under K, so it is invisible on S(U(2) x U(3)) and visible "
      "on U(2) x U(3)",
      (2 * X_y[0][0] + 3 * Y_y[0][0]) == g.qi(0) and
      (2 * X_K[0][0] + 3 * Y_K[0][0]) == g.qi(0, -1))

# twisted sections: multiplying the action by det(A)^m shifts every weight by
# 6m (det(lam^3 a) = lam^6), so Y_L = -1/2 + m and Y_Q = 1/6 + m; the
# one-cell identification with the ledger (weight exactly 1) excludes m != 0
detA_weight = (2 * X_y[0][0]).im            # 6
twisted = {m: (F(weights[3].im + m * detA_weight, 6),
               F(weights[1].im + m * detA_weight, 6)) for m in (-2, 2)}
# self-conjugacy of the twisted section: the weight multiset {3, 1, -1, -3}
# shifted by 6m is closed under negation only at m = 0 (the twisted C is
# self-dual iff C = C ox det(A)^{-2m}, and det A is onto U(1))
base = [w.im for w in weights]
closed = {m: sorted(x + 6 * m for x in base) == sorted(-(x + 6 * m) for x in base)
          for m in range(-3, 4)}
g.check("obs:thirteen: twisting the section by det(A)^m shifts every weight by 6m "
      "(Y_L to -1/2 + m: -5/2 and 3/2 at m = -2, 2; Y_Q to 1/6 + m), and the "
      "shifted weight multiset is closed under negation only at m = 0, for m "
      "in [-3, 3]: self-conjugacy alone excludes every twist",
      detA_weight == 6 and twisted[-2] == (F(-5, 2), F(-11, 6))
      and twisted[2] == (F(3, 2), F(13, 6))
      and closed == {m: (m == 0) for m in range(-3, 4)})

# the five-mode ledger Lambda^*(C^2 + W): (j,k) has K-weight j - k, and the
# dual (2-j, 3-k) has K-weight -(j-k) - 1: never the negative of j - k
# the (j,k) component has SU(2) content Lambda^j C^2, SU(3) content
# Lambda^k C^3 and central character alpha^j beta^k on (alpha I_2, beta I_3)
# (K-weight j - k at alpha = beta^-1 = lambda); its dual has the conjugate
# contents and character alpha^-j beta^-k.  Self-conjugacy under U(2) x U(3)
# would need every dual to appear among the components: only the vacuum
# (0,0), the trivial representation, is its own dual; the other eleven
# duals are absent.  On the constituent space C_k (character alpha beta^k)
# no dual is present at all.
SU2 = {0: "1", 1: "2", 2: "1"}
SU3 = {0: "1", 1: "3", 2: "3bar", 3: "1"}
CONJ3 = {"1": "1", "3": "3bar", "3bar": "3"}
comps = sorted((SU2[j], SU3[k], j, k) for j in range(3) for k in range(4))
duals = sorted((SU2[j], CONJ3[SU3[k]], -j, -k) for j in range(3) for k in range(4))
overlap = [c for c in duals if c in comps]
con = sorted(("2", SU3[k], 1, k) for k in range(4))
con_duals = sorted(("2", CONJ3[SU3[k]], -1, -k) for k in range(4))
g.check("obs:thirteen: under U(2) x U(3), with the central character alpha^j beta^k "
      "tracked, exactly one of the twelve components of the five-mode ledger "
      "is its own dual (the vacuum (0,0)) and the other eleven duals are absent, "
      "and on the constituent space no dual is present: self-conjugacy fails "
      "under U(2) x U(3) in both; the Hodge partner (2-j, 3-k) has K-weight "
      "-(j-k) - 1, off by one",
      overlap == [("1", "1", 0, 0)] and len(comps) == 12
      and not any(c in con for c in con_duals)
      and all(((2 - j) - (3 - k)) == -(j - k) - 1 for j in range(3) for k in range(4)))

# v2.0: the twisted action T12 Prop 5.8(3)(b) shows the state space carries,
# Lambda ox (det A det B)^(-1/2): the (j,k) component has central character
# alpha^(j-1) beta^(k-3/2); its dual has the conjugate contents and the
# negated exponents, and every such dual is a component (the Hodge partner
# (2-j, 3-k)), so the twisted ledger is self-conjugate under U(2) x U(3).
tw = sorted((SU2[j], SU3[k], F(j) - 1, F(k) - F(3, 2)) for j in range(3) for k in range(4))
tw_duals = sorted((SU2[j], CONJ3[SU3[k]], 1 - F(j), F(3, 2) - F(k)) for j in range(3) for k in range(4))
g.check("obs:thirteen (v2.0): in the action twisted by (det A det B)^(-1/2) the "
        "(j,k) component has central character alpha^(j-1) beta^(k-3/2), and the "
        "dual of every one of the twelve components is a component: the twisted "
        "ledger is self-conjugate under U(2) x U(3), while the untwisted one is not",
        tw_duals == tw and len(tw) == 12 and overlap != comps)

# prop:selfconj, the biconditional over subgroups G with SU(2) x SU(3) <= G
# <= U(2) x U(3) (L4 of the v3 review).  Such a G is determined by which
# characters of the central torus (alpha I_2, beta I_3) it kills; encode G by
# the lattice L of exponent pairs (a, b) with alpha^a beta^b = 1 on G.  C_k
# has central character alpha beta^k and content (2, Lambda^k); its dual has
# alpha^-1 beta^-k and content (2, Lambda^{3-k} up to the det twist, i.e.
# conj).  C is self-dual on G iff for every k some C_j has matching content
# and the character ratio in L.
def in_lattice(v, gens):
    """Is the integer vector v in the lattice spanned by gens (2-d)?"""
    if not gens:
        return v == (0, 0)
    # brute force over small coefficients suffices for these generators
    rng = range(-6, 7)
    if len(gens) == 1:
        return any((c * gens[0][0], c * gens[0][1]) == v for c in rng)
    return any((c * gens[0][0] + d * gens[1][0], c * gens[0][1] + d * gens[1][1]) == v
               for c in rng for d in rng)


content = {0: "1", 1: "3", 2: "3bar", 3: "1"}
def self_dual_on(gens, ks=(0, 1, 2, 3)):
    ok = True
    for k in ks:
        dual_content = CONJ3[content[k]]
        dual_char = (-1, -k)
        found = any(content[j] == dual_content
                    and in_lattice((dual_char[0] - 1, dual_char[1] - j), gens)
                    for j in range(4))
        ok = ok and found
    return ok


groups = {
    "U(2) x U(3)": [],
    "S(U(2) x U(3))": [(2, 3)],
    "SU(2) x U(3)": [(2, 0)],
    "U(2) x SU(3)": [(0, 3)],
    "det A = det B^-2": [(2, 6)],
}
bicond = all(self_dual_on(gens) == in_lattice((2, 3), gens) for gens in groups.values())
k0_misses = self_dual_on(groups["SU(2) x U(3)"], ks=(0,)) and not self_dual_on(groups["SU(2) x U(3)"], ks=(1,))
g.check("prop:selfconj: on five subgroups G between SU(2) x SU(3) and U(2) x U(3), "
      "encoded by the lattice of central characters trivial on G, the "
      "constituent space is self-dual exactly when det A det B = 1 on G; and "
      "the k = 0 test alone is passed by G = SU(2) x U(3) (C_0^* = C_0 there) "
      "while the k = 1 test decides, as the corrected proof uses",
      bicond and k0_misses and self_dual_on(groups["S(U(2) x U(3))"])
      and not self_dual_on(groups["det A = det B^-2"]))

# ---------------------------------------------------------------------------
# the unit action and the cell action (prop:twoactions)
# ---------------------------------------------------------------------------

def wedge_coeffs(vecs):
    """Coefficients of v_1 ^ ... ^ v_k in the wedge basis of Lambda^k C^6."""
    k = len(vecs)
    out = {}
    for I in combinations(range(6), k):
        M = [[vecs[r][c] for c in I] for r in range(k)]
        out[I] = _det(M)
    return {I: d for I, d in out.items() if d}


def _det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    tot = F(0)
    for c in range(n):
        minor = [row[:c] + row[c + 1:] for row in M[1:]]
        tot += (-1) ** c * M[0][c] * _det(minor)
    return tot


def cell_row_state(alpha, beta, S):
    """Single-row k-pair state with the row in slot v = alpha e_0 + beta e_1,
    pairs S, under the CELL action: wedge of the cells (v ox f_a), a in S.
    Cells indexed 3*i + a."""
    vecs = []
    for a in S:
        v = [F(0)] * 6
        v[a] = alpha
        v[3 + a] = beta
        vecs.append(v)
    return wedge_coeffs(vecs)


ranks_cell, ranks_unit, weights_cell = [], [], []
for k in (1, 2, 3):
    S = tuple(range(k))
    states = [cell_row_state(F(a), F(b), S)
              for (a, b) in ((1, 0), (0, 1), (1, 1), (1, 2), (2, 1), (1, 3))]
    keys = sorted(set(K for st in states for K in st))
    mat = [[st.get(K, F(0)) for K in keys] for st in states]
    ranks_cell.append(g.mat_rank(mat))
    # unit action: the same six slot vectors, each state v ox f_S is the
    # vector v in C^2: rank 2
    unit_mat = [[F(a), F(b)] for (a, b) in ((1, 0), (0, 1), (1, 1), (1, 2), (2, 1), (1, 3))]
    ranks_unit.append(g.mat_rank(unit_mat))
    # cell weight: each cell has y-weight 3 - 2 = 1, k cells: k
    weights_cell.append(k * (X_y[0][0] + Y_y[0][0]).im)
g.check("prop:twoactions(2): the SU(2)-orbit of a single-row k-pair state has "
      "rank k + 1 = 2, 3, 4 under the cell action (in the wedge basis of "
      "Lambda^k C^6) and rank 2 under the unit action, for k = 1, 2, 3",
      ranks_cell == [2, 3, 4] and ranks_unit == [2, 2, 2])
g.check("prop:twoactions(2): the cell-action weight of a single-row k-pair "
      "state is k (one per cell) against the unit-action weight 3 - 2k: "
      "1 vs 1 at k = 1 (they agree), 2 vs -1, 3 vs -3",
      weights_cell == [1, 2, 3]
      and [w.im for w in weights[1:]] == [1, -1, -3])
# the full spans, as ranks: the cell action's U(2) x U(3)-span of all single-
# row k-pair states is generated by the slot vectors' images over all pair
# subsets (the U(3) part permutes and mixes the subsets, and Lambda^k C^3 is
# already spanned by the coordinate subsets), so its dimension is the rank
# of {cell_row_state(v, S)} over the six slot vectors and all subsets S;
# the unit action's span is C^2 ox Lambda^k W, rank 2 C(3,k)
span_cell, span_unit = [], []
for k in (1, 2, 3):
    subsets = list(combinations(range(3), k))
    states = [cell_row_state(F(a), F(b), S)
              for (a, b) in ((1, 0), (0, 1), (1, 1), (1, 2), (2, 1), (1, 3))
              for S in subsets]
    keys = sorted(set(K for st in states for K in st))
    span_cell.append(g.mat_rank([[st.get(K, F(0)) for K in keys] for st in states]))
    unit_states = [[F(a) if (i, T) == (0, S) else F(b) if (i, T) == (1, S) else F(0)
                    for i in (0, 1) for T in subsets]
                   for (a, b) in ((1, 0), (0, 1), (1, 1), (1, 2), (2, 1), (1, 3))
                   for S in subsets]
    span_unit.append(g.mat_rank(unit_states))
g.check("prop:twoactions(2): the cell-action span of the single-row k-pair states "
      "has rank (k+1) C(3,k) = 6, 9, 4 (S^k C^2 ox Lambda^k C^3) and the "
      "unit-action span has rank 2 C(3,k) = 6, 6, 2 (C^2 ox Lambda^k W), "
      "computed as ranks in the wedge basis: equal only at k = 1",
      span_cell == [6, 9, 4] and span_unit == [6, 6, 2])

# rem:operator (L5): the operators Hom(Lambda^4, Lambda^1) contain a (2,1) of
# weight -3, as a character computation: Lambda^4 = (3,3) + (1,6bar) (weight
# 4), Lambda^1 = (2,3) (weight 1); (2,3) ox (3,3bar) contains (2 ox 3) ox
# (3 ox 3bar) = (2 + 4) ox (1 + 8), so a (2,1) at weight 1 - 4 = -3.
# Dimensions: 2*3 = 2 + 4 and 3*3 = 1 + 8.
g.check("rem:operator (dimension identity only, not a decomposition): the "
      "Hom-space Hom(Lambda^4, Lambda^1) contains (2,3) ox (3,3bar), and the "
      "dimensions 2 x 3 = 2 + 4 and 3 x 3 = 1 + 8 are consistent with the "
      "(2 + 4) ox (1 + 8) decomposition in which the (2,1) sits, at weight "
      "1 - 4 = -3; the decomposition itself is proved in the note, not here",
      2 * 3 == 2 + 4 and 3 * 3 == 1 + 8 and 1 - 4 == -3)

# ---------------------------------------------------------------------------
# the relative handedness (prop:orientation)
# ---------------------------------------------------------------------------

def sums(fields):
    """fields: list of (colour content, SU(2) dim, Y) for left-handed Weyl
    fermions.  Returns ([SU(3)]^2 U(1), [SU(2)]^2 U(1), grav, cubic)."""
    su3 = sum((d2 * Y for c, d2, Y in fields if c in ("3", "3bar")), F(0))
    su2 = sum(({"1": 1, "3": 3, "3bar": 3}[c] * Y
               for c, d2, Y in fields if d2 == 2), F(0))
    dim = lambda c, d2: {"1": 1, "3": 3, "3bar": 3}[c] * d2
    grav = sum((dim(c, d2) * Y for c, d2, Y in fields), F(0))
    cube = sum((dim(c, d2) * Y ** 3 for c, d2, Y in fields), F(0))
    return (su3, su2, grav, cube)


Q = ("3", 2, F(1, 6))
L = ("1", 2, F(-1, 2))
free = {0: ("1", 1, F(0)), 1: ("3", 1, F(-1, 3)), 2: ("3bar", 1, F(-2, 3)),
        3: ("1", 1, F(-1))}


def conj(field):
    c, d2, Y = field
    return (CONJ[c], d2, -Y)


list1 = [Q, L, free[0], free[2], conj(free[1]), conj(free[3])]
list2 = [Q, L, free[1], free[3], conj(free[0]), conj(free[2])]
g.check("prop:orientation(1): listing the free T half (grades 0, 2) with the "
      "slot T' half gives Q, L, nu^c, u^c, d^c, e^c and all four anomaly "
      "sums vanish", sums(list1) == (0, 0, 0, 0))
g.check("prop:orientation(2): listing the free T' half (grades 1, 3) with the "
      "slot T' half gives [SU(3)]^2 U(1) = 2/3 and cubic = -4/9, the other "
      "two sums 0", sums(list2) == (F(2, 3), 0, 0, F(-4, 9)))
g.check("prop:orientation: the two lists are conjugate in their free parts "
      "(the free fields of list 2 are the conjugates of those of list 1)",
      sorted(list2[2:]) == sorted(conj(f) for f in list1[2:]))

# ---------------------------------------------------------------------------
print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    raise SystemExit(1)
print("All checks pass.")
