"""pairing.imported-two-readings-capacities-vacuum-null: exact checks (GA.py, Fractions and Gaussian
rationals GA.QI).

(1) Witt basis = CAR: for every signature with 2 <= n <= 6 a Witt basis is built from real hyperbolic
    pairs w = (e_i + e_j)/2, w' = (e_i - e_j)/2 (e_i^2 = +1, e_j^2 = -1) and complex pairs
    (e_a + i e_b)/2, -+(e_a - i e_b)/2 from two generators of one sign; in Cl(p,q) (x) C the relation
    {e_a, e_b} = 2 g_ab becomes {w_k, w_l} = {w'_k, w'_l} = 0, {w_k, w'_l} = delta_kl, with
    floor(n/2) modes. For (1,3): one real pair and one complex pair (the Dirac spinor as two modes).
(2) Capacities: the real isotropic W spanned by min(p,q) vectors e_i + e_{p+i} has W-perp of
    signature (p - m, q - m, m), m = min(p,q), so W-perp/W is definite and W is maximal: real capacity
    min(p,q). Over C, the isotropic W_C of the floor(n/2) creation vectors has W_C-perp/W_C of
    dimension n - 2 floor(n/2) <= 1 with a nonzero form, so it is maximal: complex capacity floor(n/2).
    For (1,3) these are 1 and 2.
(3) Purity for 2 nu <= 6: on the Fock space of nu modes (Jordan-Wigner over Q(i)), the annihilator
    {x in V_C : x s = 0} of a parity-definite state s, an exact kernel over Q(i), has dimension nu for
    every sample state at nu = 2 and nu = 3 (both parities, generic and special), so each is the
    vacuum of a Witt decomposition; at nu = 4 the even state |0> + |1234> has annihilator 0 (not pure)
    while |0> has 4: the bound 2 nu <= 6 is sharp.
The claim collects these from stored results; each function calls premise() for the result whose
statement it tests (two-presentations, the capacity theorem and its consequences, Cartan's purity
theorem). The clause that a vacuum is an extra
datum (a null direction to be supplied) is a reading and is not computed.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

QI = GA.QI


def cvec(n, coeffs):
    return {(i,): QI(c) if not isinstance(c, QI) else c for i, c in coeffs.items()}


def cadd(*xs):
    out = {}
    for x in xs:
        for b, c in x.items():
            out[b] = out.get(b, QI(0)) + c
    return {b: c for b, c in out.items() if c}


def cmul(x, y, sq):
    out = {}
    for b1, c1 in x.items():
        for b2, c2 in y.items():
            s, b = GA.blade_mul(b1, b2, sq)
            c = c1 * c2 * QI(s)
            if c:
                out[b] = out.get(b, QI(0)) + c
    return {b: c for b, c in out.items() if c}


def anti(x, y, sq):
    return cadd(cmul(x, y, sq), cmul(y, x, sq))


def witt_basis(p, q):
    """List of (w, w') pairs: real hyperbolic pairs first, then complex pairs."""
    pos, neg = list(range(p)), list(range(p, p + q))
    pairs = []
    while pos and neg:
        i, j = pos.pop(0), neg.pop(0)
        pairs.append((cvec(0, {i: F(1, 2), j: F(1, 2)}), cvec(0, {i: F(1, 2), j: F(-1, 2)})))
    for grp, sgn in ((pos, 1), (neg, -1)):
        while len(grp) >= 2:
            a, b = grp.pop(0), grp.pop(0)
            w = cvec(0, {a: QI(F(1, 2)), b: QI(0, F(1, 2))})
            wp = cvec(0, {a: QI(F(sgn, 2)), b: QI(0, F(-sgn, 2))})
            pairs.append((w, wp))
    return pairs


def check_witt_basis_relations_are_the_car():
    premise("one-relation.two-presentations")
    ok = True
    for n in range(2, 7):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p, q)
            pairs = witt_basis(p, q)
            ok = ok and len(pairs) == n // 2
            for k, (wk, wpk) in enumerate(pairs):
                for l, (wl, wpl) in enumerate(pairs):
                    ok = ok and anti(wk, wl, sq) == {} and anti(wpk, wpl, sq) == {}
                    want = {(): QI(1)} if k == l else {}
                    ok = ok and anti(wk, wpl, sq) == want
    p13 = witt_basis(1, 3)
    real13 = [all(c.im == 0 for c in w.values()) for w, wp in p13]
    ok = ok and real13 == [True, False]
    GA.check("Witt bases give the CAR with floor(n/2) modes (n <= 6); (1,3): one real and one complex pair", ok)
    return ok


def check_real_and_complex_capacities():
    premise("tower.witt-index-quantum-capacity")
    premise("one-relation.two-capacities-three-consequences")
    ok = True
    for n in range(2, 7):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p, q)
            mcap = min(p, q)
            W = []
            for i in range(mcap):
                v = [F(0)] * n
                v[i], v[p + i] = F(1), F(1)
                W.append(v)
            if W:
                rows = [[sq[k] * v[k] for k in range(n)] for v in W]
                perp = GA.field_kernel(rows)
            else:
                perp = [[F(1) if i == j else F(0) for i in range(n)] for j in range(n)]
            gram = [[sum(sq[k] * a[k] * b[k] for k in range(n)) for b in perp] for a in perp]
            ok = ok and all(sum(sq[k] * v[k] * v[k] for k in range(n)) == 0 for v in W)
            ok = ok and GA.congruence_signature(gram) == (p - mcap, q - mcap, mcap)
            # complex: W_C spanned by the w's of the Witt basis
            ccap = n // 2
            Wc = [[w.get((k,), QI(0)) for k in range(n)] for w, wp in witt_basis(p, q)]
            ok = ok and len(Wc) == ccap
            rows = [[QI(sq[k]) * v[k] for k in range(n)] for v in Wc]
            perp = GA.field_kernel(rows)
            ok = ok and len(perp) == n - ccap
            gram = [[sum((QI(sq[k]) * a[k] * b[k] for k in range(n)), QI(0)) for b in perp] for a in perp]
            ok = ok and GA.field_rank(gram) == n - 2 * ccap
    ok = ok and (min(1, 3), (1 + 3) // 2) == (1, 2)
    GA.check("real capacity min(p,q) and complex capacity floor(n/2): maximal isotropic subspaces (n <= 6)", ok)
    return ok


def fock(nu):
    d = 2 ** nu
    a = []
    for j in range(nu):
        M = [[QI(0)] * d for _ in range(d)]
        for s in range(d):
            if (s >> j) & 1:
                sign = -1 if bin(s & ((1 << j) - 1)).count("1") % 2 else 1
                M[s & ~(1 << j)][s] = QI(sign)
        a.append(M)
    ad = [[[M[c][r].conj() for c in range(d)] for r in range(d)] for M in a]
    return a, ad


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(len(v))), QI(0)) for i in range(len(M))]


def annihilator_dim(nu, state):
    a, ad = fock(nu)
    cols = [apply(M, state) for M in a + ad]
    M = [[cols[k][i] for k in range(2 * nu)] for i in range(len(state))]
    return 2 * nu - GA.field_rank(M)


STATES = {
    2: [{0: QI(1)}, {3: QI(1)}, {0: QI(2, -1), 3: QI(3, 1)}, {1: QI(1)}, {1: QI(1, 2), 2: QI(-3, 1)}],
    3: [{0: QI(1)}, {0: QI(1), 3: QI(2), 5: QI(-1, 1), 6: QI(0, 3)}, {3: QI(1), 6: QI(2, 1)},
        {1: QI(1), 2: QI(-2), 4: QI(1, 1), 7: QI(3, -2)}, {7: QI(1)}, {3: QI(1), 5: QI(1), 6: QI(1)}],
}


def vecstate(nu, d):
    return [d.get(i, QI(0)) for i in range(2 ** nu)]


def check_every_weyl_spinor_pure_up_to_six():
    premise("one-relation.imported-cartans-purity-theorem-thouless-form")
    ok = True
    for nu, states in STATES.items():
        for st in states:
            parities = {bin(i).count("1") % 2 for i in st}
            ok = ok and len(parities) == 1
            ok = ok and annihilator_dim(nu, vecstate(nu, st)) == nu
    ok = ok and annihilator_dim(4, vecstate(4, {0: QI(1), 15: QI(1)})) == 0
    ok = ok and annihilator_dim(4, vecstate(4, {0: QI(1)})) == 4
    GA.check("every parity-definite state is pure (annihilator of dimension nu) at nu = 2, 3; not at nu = 4", ok)
    return ok
