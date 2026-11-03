"""rungs.transported-module-holds-tuple-one-vector: exact checks.

The two-rung module as the five-mode Jordan-Wigner Fock model (rungs = modes 0, 1; pairs = modes 2, 3, 4;
exact integer signs), with the rung mixing sum X a^dag a over the rungs, the pair mixing over the pairs, the
y-generator 3 N_rung - 2 N_pair, and the su(2), sl(3) Casimirs C2 = EF + FE + H^2/2 (rungs) and
C3 = sum_ab E_ab E_ba - N_pair^2/3 (pairs).
(1) The sector (j, k) in {(1, 0), (1, 2)} is C^2 (x) CS, CS = Lambda^even W: dimension 8; the rung mixing acts
    on it as X (x) 1 on the slot index; y = 3 on (1, 0) and -1 on (1, 2) (Y = 1/2, -1/6); C2 = 3/2 (doublet)
    on both; C3 = 0 on (1, 0) and 8/3 on (1, 2), whose pair-torus weights are e_a + e_b (the 3b): the
    content (2,1)_{1/2} + (2,3b)_{-1/6} = L* + Q*.
(2) CS (x) CS is not equivariantly inside the module: the sl(3) Casimir takes only the values 0 and 8/3 on the
    whole module (contents 1, 3, 3b), while S^2(Lambda^2 W) (the symmetric square of the pair-torus action on
    Lambda^2 W, dimension 6 by exact rank) has Casimir 20/3 (the 6b) and contains the weights 2(e_a + e_b),
    whose sl(3) classes are not weights of the module (all of whose weights have coordinates in {0, 1}).
(3) The mass bracket Z^1 ^ Z^2 (the Lambda^2 C^2 (x) Lambda^2 CS component of Psi . Psi) is quadratic in Psi:
    B(c Psi) = c^2 B(Psi) and B is not additive, so no linear map from the module produces it; in the chart
    (e1, e2, pi1, pi2) its pairing with n_inf = e1 ^ e2 is <pi^1 pi^2>, exactly (samples over Q(i)).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock
from tp_premise import premise

RUNGS, PAIRS = [0, 1], [2, 3, 4]
DIM = 32
PSI_SAMPLES = [([GA.qi(1), GA.qi(2, -1), GA.qi(0, 1), GA.qi(3)], [GA.qi(-1, 1), GA.qi(0), GA.qi(2), GA.qi(1, 4)]),
               ([GA.qi(F(1, 2)), GA.qi(1, 1), GA.qi(-2), GA.qi(0, -3)], [GA.qi(5), GA.qi(-1, 2), GA.qi(1, 1), GA.qi(2)])]


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


def unit(n, i, j):
    return [[1 if (a, b) == (i, j) else 0 for b in range(n)] for a in range(n)]


def jk(b):
    return bin(b & 3).count("1"), bin(b >> 2).count("1")


scal = fock.vsc


def casimir2(st):
    E, Fm, H = unit(2, 0, 1), unit(2, 1, 0), [[1, 0], [0, -1]]
    ef = bilinear(E, RUNGS, bilinear(Fm, RUNGS, st))
    fe = bilinear(Fm, RUNGS, bilinear(E, RUNGS, st))
    hh = bilinear(H, RUNGS, bilinear(H, RUNGS, st))
    return st_add(scal(F(1), ef), scal(F(1), fe), scal(F(1, 2), hh))


def casimir3(st, act=None):
    act = act or (lambda Y, s: bilinear(Y, PAIRS, s))
    terms = []
    for a in range(3):
        for b in range(3):
            terms.append(scal(F(1), act(unit(3, a, b), act(unit(3, b, a), st))))
    Nst = act([[1, 0, 0], [0, 1, 0], [0, 0, 1]], st)
    terms.append(scal(F(-1, 3), act([[1, 0, 0], [0, 1, 0], [0, 0, 1]], Nst)))
    return st_add(*terms)


def check_two_spinor_configuration_is_the_one_rung_sector():
    premise("rungs.rung-spinor-module-mixings")
    premise("rungs.ladder-group-rung-mixing-group-one")
    premise("standard-model.under-s-composites-state-space-spinor")
    ok = True
    sector = [b for b in range(DIM) if jk(b) in ((1, 0), (1, 2))]
    ok = ok and len(sector) == 8
    weights02 = []
    for b in sector:
        j, k = jk(b)
        st = {b: 1}
        y = st_add(bilinear([[3, 0], [0, 3]], RUNGS, st), bilinear([[-2, 0, 0], [0, -2, 0], [0, 0, -2]], PAIRS, st))
        ok = ok and y == {b: 3 * j - 2 * k}
        ok = ok and casimir2(st) == {b: F(3, 2)}
        ok = ok and casimir3(st) == ({b: F(8, 3)} if k == 2 else {})
        for i in range(2):
            for jj in range(2):
                want = {(b & ~3) | (1 << i): 1} if (b & 3) == (1 << jj) else {}
                ok = ok and bilinear(unit(2, i, jj), RUNGS, st) == want
        if k == 2:
            weights02.append(tuple((b >> m) & 1 for m in PAIRS))
    ok = ok and sorted(set(weights02)) == [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
    ok = ok and [F(3 * 1 - 2 * k, 6) for k in (0, 2)] == [F(1, 2), F(-1, 6)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_two_spinor_configuration_is_the_one_rung_sector"; return _tp_rv


def _sym_square_states():
    """S^2(Lambda^2 W): symmetric tensors f_S (x) f_T + f_T (x) f_S, |S| = |T| = 2."""
    L2 = list(combinations(range(3), 2))
    out = []
    for i, S in enumerate(L2):
        for T in L2[i:]:
            st = {(S, T): 1}
            st[(T, S)] = st.get((T, S), 0) + 1
            out.append(st)
    return out


def _derive(Y, S):
    out = {}
    for t, s in enumerate(S):
        for r in range(3):
            if Y[r][s]:
                seq = S[:t] + (r,) + S[t + 1:]
                if len(set(seq)) < len(seq):
                    continue
                sign = 1
                lst = list(seq)
                for i in range(len(lst)):
                    for j in range(len(lst) - 1 - i):
                        if lst[j] > lst[j + 1]:
                            lst[j], lst[j + 1] = lst[j + 1], lst[j]
                            sign = -sign
                T = tuple(lst)
                out[T] = out.get(T, 0) + sign * Y[r][s]
    return {T: c for T, c in out.items() if c}


def _tensor_act(Y, st):
    out = {}
    for (S, T), c in st.items():
        for S2, d in _derive(Y, S).items():
            out[(S2, T)] = out.get((S2, T), 0) + c * d
        for T2, d in _derive(Y, T).items():
            out[(S, T2)] = out.get((S, T2), 0) + c * d
    return {k: v for k, v in out.items() if v}


def check_two_particle_product_not_in_module():
    premise("rungs.rung-spinor-module-mixings")
    ok = True
    module_cas = set()
    for b in range(DIM):
        c = casimir3({b: 1})
        vals = set(c.values()) if c else {F(0)}
        ok = ok and (not c or set(c) == {b})
        module_cas |= vals
    ok = ok and module_cas == {F(0), F(8, 3)}
    sym = _sym_square_states()
    keys = sorted({K for st in sym for K in st})
    ok = ok and GA.rank_of_vectors([[F(st.get(K, 0)) for K in keys] for st in sym]) == 6
    for st in sym:
        cas = casimir3(st, act=_tensor_act)
        ok = ok and cas == {K: F(20, 3) * v for K, v in st.items()}

    def sl3(w):
        m = F(sum(w), 3)
        return tuple(F(x) - m for x in w)
    module_classes = {sl3(tuple((b >> m) & 1 for m in PAIRS)) for b in range(DIM)}
    doubled = [tuple(2 * (i in S) for i in range(3)) for S in combinations(range(3), 2)]
    ok = ok and all(sl3(w) not in module_classes for w in doubled)
    _tp_rv = (ok); assert _tp_rv is not False, "check_two_particle_product_not_in_module"; return _tp_rv


def check_mass_bracket_is_quadratic():
    premise("rungs.mass-bracket-frozen-points-grip-slot")

    def wedge(Z1, Z2):
        return {(a, b): Z1[a] * Z2[b] - Z1[b] * Z2[a] for a, b in combinations(range(4), 2)}

    def det4(cols):
        """Exact determinant over Q(i) by Laplace expansion along the first column."""
        M = [[cols[c][r] for c in range(len(cols))] for r in range(len(cols))]

        def det(A):
            if len(A) == 1:
                return A[0][0]
            tot = GA.qi(0)
            for r in range(len(A)):
                minor = [row[1:] for i, row in enumerate(A) if i != r]
                term = A[r][0] * det(minor)
                tot = tot + term if r % 2 == 0 else tot - term
            return tot
        return det(M)
    E = [[GA.qi(1 if i == j else 0) for i in range(4)] for j in range(4)]   # chart basis e1, e2, pi1, pi2
    ok = det4(E) == GA.qi(1)

    for Z1, Z2 in PSI_SAMPLES:
        B = wedge(Z1, Z2)
        ok = ok and det4([E[0], E[1], Z1, Z2]) == Z1[2] * Z2[3] - Z1[3] * Z2[2]      # <pi^1 pi^2>
        ok = ok and det4([E[2], E[3], Z1, Z2]) == Z1[0] * Z2[1] - Z1[1] * Z2[0]      # <omega^1 omega^2>
        c = GA.qi(2, 1)
        Bc = wedge([c * z for z in Z1], [c * z for z in Z2])
        ok = ok and all(Bc[K] == c * c * B[K] for K in B) and any(Bc[K] != c * B[K] for K in B)
    (A1, A2), (C1, C2) = PSI_SAMPLES
    Bs = wedge([a + c for a, c in zip(A1, C1)], [a + c for a, c in zip(A2, C2)])
    BA, BC = wedge(A1, A2), wedge(C1, C2)
    ok = ok and any(Bs[K] != BA[K] + BC[K] for K in Bs)
    _tp_rv = (ok); assert _tp_rv is not False, "check_mass_bracket_is_quadratic"; return _tp_rv
