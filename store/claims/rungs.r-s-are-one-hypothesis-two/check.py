"""rungs.r-s-are-one-hypothesis-two: exact checks.

Two exact Jordan-Wigner Fock models of five modes (basis states are bitmasks, a state is
a^dag_(m1) ... a^dag_(mk) |0> with m1 < ... < mk): model R is Lambda(W + R_2) with the pairs as modes 0, 1, 2
and the rungs as modes 3, 4; model S is Lambda(C^2 + W) with the slots as modes 0, 1 and the pairs as 2, 3, 4.
The identification Phi sends slot i to rung i and is the canonical isomorphism of exterior algebras: the
R-state a^dag(P) a^dag(G)|0> goes to the S-state built by the same creation operators in the same order.
(1) Phi is bijective on basis states up to signs and intertwines every creation and annihilation operator
    (the two CAR systems are one), hence every generator of gl(2) + gl(3) (sum X a^dag a over rungs/slots
    and over pairs), the (j, k) grading and the chirality (-1)^N = (-1)^(j+k); the (j, k) pieces have
    dimension C(2, j) C(3, k), total 32.
(2) The j = 1 sector is C^2 (x) Lambda W with the slot mixing acting once (X (x) 1) and y-weight
    3j - 2k = 3 - 2k: the constituent space of (C); the even half has dimension 16 with the components
    (0,0), (0,2), (1,1), (1,3), (2,0), (2,2) of hypercharge (3j - 2k)/6 = 0, -2/3, 1/6, -1/2, 1, 1/3:
    nu^c, u^c, Q, L, e^c, d^c, the derived generation.
(3) The Bogoliubov algebra: the ten real Majorana combinations a + a^dag, a - a^dag satisfy the Clifford
    relations of signature (5, 5); the 45 bilinears gamma_p gamma_q (p < q) are orthogonal for the trace form
    (Gram 32 times the identity, so independent), commute with the chirality, and close under the commutator
    with the so(10) structure constants [g_a g_b, g_c g_d] = 2(n_bc g_a g_d - n_ac g_b g_d - n_bd g_a g_c +
    n_ad g_b g_c): Spin(10) (complexified) acting on each chirality half.
"""
from fractions import Fraction as F
from itertools import combinations

import GA  # noqa: F401
import fock
from tp_premise import premise

NM = 5
DIM = 2 ** NM
R_PAIRS, R_RUNGS = [0, 1, 2], [3, 4]
S_SLOTS, S_PAIRS = [0, 1], [2, 3, 4]


# a_i^dag, a_i on sparse Fock states {bitmask: coefficient} (LSB, Jordan-Wigner) and their sum, from lib/fock.py
cre, ann, st_add = fock.cre_on, fock.ann_on, fock.vadd


def bilinear(X, modes, st):
    """sum_rs X_rs a^dag_(modes r) a_(modes s) on a Fock state."""
    terms = []
    for r in range(len(modes)):
        for s in range(len(modes)):
            if X[r][s]:
                terms.append({b: X[r][s] * c for b, c in cre(modes[r], ann(modes[s], st)).items()})
    return st_add(*terms) if terms else {}


def mask(modes):
    return sum(1 << m for m in modes)


def comb(n, k):
    return len(list(combinations(range(n), k)))


def r_to_s_mode(m):
    return S_PAIRS[R_PAIRS.index(m)] if m in R_PAIRS else S_SLOTS[R_RUNGS.index(m)]


def phi(st):
    """The canonical identification on a state of model R."""
    out = {}
    for b, c in st.items():
        modes = [m for m in range(NM) if b >> m & 1]
        img = {0: c}
        for m in reversed(modes):
            img = cre(r_to_s_mode(m), img)
        for bb, cc in img.items():
            out[bb] = out.get(bb, 0) + cc
    return {b: c for b, c in out.items() if c}


def unit(n, i, j):
    return [[1 if (a, b) == (i, j) else 0 for b in range(n)] for a in range(n)]


def jk_s(b):
    return bin(b & 3).count("1"), bin(b >> 2).count("1")


def check_r_and_s_are_the_same_module():
    premise("rungs.rung-spinor-module-mixings")
    premise("rungs.imported-tower-one-qubit-per-rung")
    premise("rungs.ladder-group-rung-mixing-group-one")
    ok = True
    images = [phi({b: 1}) for b in range(DIM)]
    ok = ok and all(len(im) == 1 and abs(next(iter(im.values()))) == 1 for im in images)
    ok = ok and sorted(next(iter(im)) for im in images) == list(range(DIM))
    for b in range(DIM):
        st = {b: 1}
        for m in range(NM):
            ok = ok and phi(cre(m, st)) == cre(r_to_s_mode(m), phi(st))
            ok = ok and phi(ann(m, st)) == ann(r_to_s_mode(m), phi(st))
        jr = bin(b >> 3).count("1"), bin(b & 7).count("1")
        tgt = next(iter(images[b]))
        ok = ok and jk_s(tgt) == jr and bin(b).count("1") % 2 == sum(jr) % 2
        for i in range(2):
            for j in range(2):
                X = unit(2, i, j)
                ok = ok and phi(bilinear(X, R_RUNGS, st)) == bilinear(X, S_SLOTS, phi(st))
        for a in range(3):
            for c in range(3):
                Y = unit(3, a, c)
                ok = ok and phi(bilinear(Y, R_PAIRS, st)) == bilinear(Y, S_PAIRS, phi(st))
    counts = {}
    for b in range(DIM):
        counts[jk_s(b)] = counts.get(jk_s(b), 0) + 1
    ok = ok and counts == {(j, k): comb(2, j) * comb(3, k) for j in range(3) for k in range(4)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_r_and_s_are_the_same_module"; return _tp_rv


def check_constituent_sector_and_generation():
    premise("rungs.ladder-group-rung-mixing-group-one")
    premise("standard-model.under-s-composites-state-space-spinor")
    ok = True
    for b in range(DIM):
        j, k = jk_s(b)
        y = st_add(bilinear([[3, 0], [0, 3]], S_SLOTS, {b: 1}), bilinear([[-2, 0, 0], [0, -2, 0], [0, 0, -2]], S_PAIRS, {b: 1}))
        ok = ok and y == ({b: 3 * j - 2 * k} if 3 * j - 2 * k else {})
        if j == 1:
            for i in range(2):
                for jj in range(2):
                    img = bilinear(unit(2, i, jj), S_SLOTS, {b: 1})
                    want = {(b & ~3) | (1 << i): 1} if (b & 3) == (1 << jj) else {}
                    ok = ok and img == want
    even = sorted({jk_s(b) for b in range(DIM) if bin(b).count("1") % 2 == 0})
    ok = ok and sum(1 for b in range(DIM) if bin(b).count("1") % 2 == 0) == 16
    ok = ok and even == [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]
    ok = ok and [F(3 * j - 2 * k, 6) for j, k in even] == [F(0), F(-2, 3), F(1, 6), F(-1, 2), F(1), F(1, 3)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_constituent_sector_and_generation"; return _tp_rv


def _op(f):
    """Sparse matrix of a linear map given on basis states: column b -> image state."""
    return {b: f({b: 1}) for b in range(DIM)}


def _apply(M, st):
    return st_add(*[{r: c * v for r, v in M[b].items()} for b, c in st.items()]) if st else {}


def _comp(A, B):
    return {b: _apply(A, B[b]) for b in range(DIM)}


def _lin(*terms):
    return {b: st_add(*[{r: c * v for r, v in M[b].items()} for c, M in terms]) for b in range(DIM)}


def check_bogoliubov_spin10():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    premise("rungs.rung-spinor-module-mixings")
    ok = True
    gam, eta = [], []
    for m in range(NM):
        gam.append(_op(lambda st, m=m: st_add(cre(m, st), ann(m, st))))
        gam.append(_op(lambda st, m=m: st_add(ann(m, st), {b: -c for b, c in cre(m, st).items()})))
        eta += [1, -1]
    ident = {b: {b: 1} for b in range(DIM)}
    zero = {b: {} for b in range(DIM)}
    for p in range(10):
        for q in range(10):
            anti = _lin((1, _comp(gam[p], gam[q])), (1, _comp(gam[q], gam[p])))
            ok = ok and anti == (_lin((2 * eta[p], ident)) if p == q else zero)
    pairs = list(combinations(range(10), 2))
    L = {pq: _comp(gam[pq[0]], gam[pq[1]]) for pq in pairs}
    gram = {}
    for pq in pairs:
        for rs in pairs:
            gram[(pq, rs)] = sum(c * L[rs][b].get(r, 0) for b in range(DIM) for r, c in L[pq][b].items())
    ok = ok and all(gram[(pq, rs)] == (DIM if pq == rs else 0) for pq in pairs for rs in pairs)
    chir = {b: {b: -1 if bin(b).count("1") % 2 else 1} for b in range(DIM)}
    ok = ok and all(_comp(L[pq], chir) == _comp(chir, L[pq]) for pq in pairs)

    def Lg(a, b):
        if a == b:
            return zero
        return L[(a, b)] if a < b else _lin((-1, L[(b, a)]))

    def d(x, y):
        return eta[x] if x == y else 0
    for (a, b) in pairs:
        for (c, e) in pairs:
            lhs = _lin((1, _comp(L[(a, b)], L[(c, e)])), (-1, _comp(L[(c, e)], L[(a, b)])))
            rhs = _lin((2 * d(b, c), Lg(a, e)), (-2 * d(a, c), Lg(b, e)), (-2 * d(b, e), Lg(a, c)), (2 * d(a, e), Lg(b, c)))
            ok = ok and lhs == rhs
    _tp_rv = (ok and len(pairs) == 45); assert _tp_rv is not False, "check_bogoliubov_spin10"; return _tp_rv
