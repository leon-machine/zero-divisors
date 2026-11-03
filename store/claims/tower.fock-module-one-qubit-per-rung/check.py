"""tower.fock-module-one-qubit-per-rung: exact checks.

Lambda W_k is modelled on subsets S of {0..k-1} (a basis state is the wedge of the v_j, j in S, in
increasing order), with v_j acting by wedge and w_j by contraction (Koszul signs). The plane
generators act as e_j = v_j + w_j and f_j = v_j - w_j. Everything is exact.
(1) W_k is maximal isotropic (computed in GA.py inside Cl(k,k), k <= 4): the v_j are independent,
    pairwise orthogonal and null, and the orthogonal complement of W_k has dimension k (so it is W_k).
(2) The Chevalley action is a module of B_k = Cl(k,k) (k <= 4): on every basis state e_j^2 = 1,
    f_j^2 = -1 and distinct generators anticommute; c(a)^2 = Q(a) for a general vector a. The
    vacuum is killed by every w_j, the creation monomials applied to it give all 2^k states (rank 2^k),
    and dim Lambda W_k = 2^k.
(3) Irreducibility: for k <= 3 the 4^k blades of B_k act by matrices of rank 4^k = dim End(Lambda W_k)
    (so B_k = Mat_{2^k}(R) acts fully); for k <= 4 also by the Fock criterion: the common kernel of
    the w_j is the vacuum line (dimension 1), and the vacuum is cyclic.
(4) Doubling: Lambda W_{k+1} has dimension 2 * 2^k, with basis S and S + {k}, and the operators of the
    first k planes act on it as (old operator) (x) id (computed on every basis state), while v_k, w_k
    change only the new slot (with the parity sign of the old part): one qubit per rung.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

KMAX = 4


def states(k):
    return [frozenset(c) for r in range(k + 1) for c in combinations(range(k), r)]


def wedge(j, st):
    out = {}
    for S, c in st.items():
        if j in S:
            continue
        T = frozenset(S | {j})
        out[T] = out.get(T, F(0)) + (-1) ** len([i for i in S if i < j]) * c
    return {S: c for S, c in out.items() if c != 0}


def contract(j, st):
    out = {}
    for S, c in st.items():
        if j not in S:
            continue
        T = frozenset(S - {j})
        out[T] = out.get(T, F(0)) + (-1) ** len([i for i in S if i < j]) * c
    return {S: c for S, c in out.items() if c != 0}


def add(*xs):
    out = {}
    for x in xs:
        for S, c in x.items():
            out[S] = out.get(S, F(0)) + c
    return {S: c for S, c in out.items() if c != 0}


def scal(c, x):
    return {S: c * v for S, v in x.items() if c * v != 0}


def act(gen, st):
    """gen = ('e', j) or ('f', j) or ('v', j) or ('w', j)."""
    t, j = gen
    if t == "v":
        return wedge(j, st)
    if t == "w":
        return contract(j, st)
    if t == "e":
        return add(wedge(j, st), contract(j, st))
    return add(wedge(j, st), scal(-1, contract(j, st)))


def act_word(word, st):
    for g in reversed(word):
        st = act(g, st)
    return st


def gens(k):
    return [(t, j) for j in range(k) for t in ("e", "f")]


# the numbers of rungs k checked
RUNGS = range(1, KMAX + 1)
# full-matrix-algebra test (4^k blades) up to this k (time)
FULL_ACTION_KMAX = 3
# the vacuum state (empty wedge)
VACUUM = {frozenset(): F(1)}


def basis_state(S):
    """The basis state of Lambda W_k labelled by the subset S."""
    return {S: F(1)}


def sample_vector(k):
    """Coefficients (alpha_j, beta_j) of a sample general vector a = sum alpha_j e_j + beta_j f_j."""
    return [F(2 * j + 1, 3) for j in range(k)], [F(1 - j, 2) for j in range(k)]


def ordered_words(G):
    """All increasing words in the generator list G (one per blade)."""
    return [w for r in range(len(G) + 1) for w in combinations(G, r)]


def check_w_is_maximal_isotropic():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    for k in range(1, KMAX + 1):
        S = tuple([1, -1] * k)
        vs = [GA.scal(F(1, 2), GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(k)]
        vecs = [[v.get((i,), F(0)) for i in range(2 * k)] for v in vs]
        assert GA.rank_of_vectors(vecs) == k
        for a in vs:
            for b in vs:
                assert GA.dot(a, b, S) == 0
        # orthogonal complement of W in R^(k,k): kernel of the k x 2k matrix of <v_j, e_i>
        M = [[GA.dot(v, GA.gen(i), S) for i in range(2 * k)] for v in vs]
        assert 2 * k - GA.rank_of_vectors(M) == k
    return True


def check_chevalley_module_and_vacuum():
    for k in RUNGS:
        sts = states(k)
        assert len(sts) == 2 ** k
        for S in sts:
            st = basis_state(S)
            for g in gens(k):
                want = st if g[0] == "e" else scal(-1, st)
                assert act_word([g, g], st) == want
                for h in gens(k):
                    if h != g:
                        assert add(act_word([g, h], st), act_word([h, g], st)) == {}
            # a general vector a = sum (alpha_j e_j + beta_j f_j): c(a)^2 = Q(a) = sum alpha^2 - beta^2
            al, be = sample_vector(k)

            def ca(x):
                return add(*[scal(al[j], act(("e", j), x)) for j in range(k)]
                           + [scal(be[j], act(("f", j), x)) for j in range(k)])
            Qa = sum(a * a for a in al) - sum(b * b for b in be)
            assert ca(ca(st)) == scal(Qa, st)
        vac = VACUUM
        for j in range(k):
            assert act(("w", j), vac) == {}
        imgs = [act_word([("v", j) for j in sorted(S)], vac) for S in sts]
        assert GA.rank_of_vectors([[x.get(T, F(0)) for T in sts] for x in imgs]) == 2 ** k
    return True


def check_irreducible():
    premise("tower.commuting-copies")
    for k in RUNGS:
        sts = states(k)
        if k <= FULL_ACTION_KMAX:
            mats = []
            for word in ordered_words(gens(k)):
                row = []
                for S in sts:
                    img = act_word(list(word), basis_state(S))
                    row.extend(img.get(T, F(0)) for T in sts)
                mats.append(row)
            assert len(mats) == 4 ** k
            assert GA.rank_of_vectors(mats) == 4 ** k
        # Fock criterion: common kernel of the contractions is the vacuum line
        rows = []
        for j in range(k):
            for T in sts:
                rows.append([act(("w", j), basis_state(S)).get(T, F(0)) for S in sts])
        assert 2 ** k - GA.rank_of_vectors(rows) == 1
        assert all(act(("w", j), VACUUM) == {} for j in range(k))
    return True


def check_one_qubit_per_rung():
    for k in range(1, KMAX):
        small, big = states(k), states(k + 1)
        assert len(big) == 2 * len(small)
        new = frozenset([k])
        assert set(big) == set(small) | {S | new for S in small}
        for S in small:
            for T in (frozenset(), new):
                for g in gens(k):
                    lhs = act(g, {S | T: F(1)})
                    rhs = {U | T: c for U, c in act(g, {S: F(1)}).items()}
                    assert lhs == rhs
                par = (-1) ** len(S)
                # the new pair moves only the new slot, with the parity sign of the old part
                assert act(("v", k), {S: F(1)}) == {S | new: F(par)}
                assert act(("w", k), {S | new: F(1)}) == {S: F(par)}
                assert act(("v", k), {S | new: F(1)}) == {} and act(("w", k), {S: F(1)}) == {}
    return True
