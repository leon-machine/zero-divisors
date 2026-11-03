"""descent-lift.imported-thouless-states-witt-vacua: exact checks (Fock matrices, Fractions).

(1) For sample antisymmetric A on nu = 2, 3, 4 modes, T = sum_{i<j} A_ij a_i^dag a_j^dag, the Thouless state
    exp(T)|0> (T^2 = 0 for nu <= 3; the series is cut at T^2/2 on 4 modes, where T^3 = 0) is annihilated by
    the Bogoliubov-rotated operators b_i = a_i - sum_j A_ij a_j^dag, which satisfy {b_i, b_j} = 0 and
    {b_i, b_j^dag} = (1 + A A^T)_ij, positive definite (leading minors > 0): after a rational change of
    basis they are the annihilators of a Witt decomposition. On two modes exp(T)|0> = |00> + A_12 |11>.
(2) Purity by Cartan's count: the annihilator {L = sum x_i a_i + y_i a_i^dag : L psi = 0} of an even
    vector has dimension nu for every sample even vector on 2 and 3 modes, those with zero vacuum overlap
    included; the 4-mode control |0000> + |1111> has annihilator 0 (not pure).
(3) Exponential form iff nonzero vacuum overlap: a 3-mode even vector with overlap alpha != 0 equals
    alpha exp(T)|0> with A read off its pair amplitudes; |11> on two modes is annihilated by a1^dag, a2^dag
    (a Witt vacuum) but has zero overlap, while every exp(T)|0> has overlap 1.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

# ---- exact fermionic Fock toolkit: lib/fock.py in MSB order. Basis of m modes: occupation
# tuples; index = sum n_k 2^(m-1-k), so mode 0 is the most significant bit and |sys> (x) |rec>
# is the index sys * 2^k + rec when the system modes come first. ----
MSB = fock.MSB
dag = fock.dag
mm = fock.mm
madd = fock.madd
msc = fock.msc
eye = fock.eye
apply = fock.apply
vadd = fock.vadd
vsc = fock.vsc


def ann(k, m):
    return fock.ann(k, m, MSB)


def ket(t):
    return fock.ket(t, MSB)
# ---- end of toolkit ----

SAMPLE_A = {
    2: [[F(0), F(3, 4)], [F(-3, 4), F(0)]],
    3: [[F(0), F(1, 2), F(-2)], [F(-1, 2), F(0), F(5, 3)], [F(2), F(-5, 3), F(0)]],
    4: [[F(0), F(1), F(2), F(-1, 3)], [F(-1), F(0), F(1, 2), F(3)],
        [F(-2), F(-1, 2), F(0), F(4, 5)], [F(1, 3), F(-3), F(-4, 5), F(0)]],
}
EVEN3 = [  # (vacuum, |110>, |101>, |011>) amplitudes
    (F(1), F(2), F(-1, 3), F(5)),
    (F(0), F(1), F(2), F(-3)),
    (F(0), F(0), F(1), F(0)),
    (F(-2, 7), F(0), F(3), F(1, 2)),
]
EVEN2 = [(F(1), F(5)), (F(0), F(1)), (F(3, 5), F(4, 5))]


def thouless(A, nu):
    a = [ann(k, nu) for k in range(nu)]
    T = {}
    for i in range(nu):
        for j in range(i + 1, nu):
            T = madd(T, msc(A[i][j], mm(dag(a[i]), dag(a[j]))))
    vac = ket((0,) * nu)
    Tv = apply(T, vac)
    return vadd(vac, Tv, vsc(F(1, 2), apply(T, Tv))), T, a


def annihilator_dim(psi, nu):
    a = [ann(k, nu) for k in range(nu)]
    ops_ = a + [dag(x) for x in a]
    cols = [apply(o, psi) for o in ops_]
    rows = [[cols[c].get(r, F(0)) for c in range(2 * nu)] for r in range(2 ** nu)]
    return 2 * nu - GA.field_rank(rows)


def check_thouless_states_are_rotated_vacua():
    premise("one-relation.imported-cartans-purity-theorem-thouless-form")
    ok = True
    for nu, A in SAMPLE_A.items():
        psi, T, a = thouless(A, nu)
        ok = ok and (mm(T, T) == {}) == (nu <= 3)
        ok = ok and mm(T, T, T) == {}
        b = [madd(a[i], *[msc(-A[i][j], dag(a[j])) for j in range(nu)]) for i in range(nu)]
        ok = ok and all(apply(bi, psi) == {} for bi in b)
        G = [[F(0)] * nu for _ in range(nu)]
        for i in range(nu):
            for j in range(nu):
                ok = ok and madd(mm(b[i], b[j]), mm(b[j], b[i])) == {}
                ac = madd(mm(b[i], dag(b[j])), mm(dag(b[j]), b[i]))
                want = (1 if i == j else 0) + sum(A[i][k] * A[j][k] for k in range(nu))
                ok = ok and ac == msc(want, eye(2 ** nu))
                G[i][j] = want
        minors = []
        for r in range(1, nu + 1):
            minors.append(det([row[:r] for row in G[:r]]))
        ok = ok and all(mn > 0 for mn in minors)
    psi2, _, _ = thouless(SAMPLE_A[2], 2)
    ok = ok and psi2 == {0: F(1), 3: F(3, 4)}
    GA.check("Thouless states are killed by b_i = a_i - A_ij a_j^dag, a rotated Witt decomposition", ok)
    return ok


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    return sum(((-1) ** c) * M[0][c] * det([row[:c] + row[c + 1:] for row in M[1:]]) for c in range(n))


def check_every_even_vector_up_to_three_modes_is_pure():
    premise("one-relation.imported-cartans-purity-theorem-thouless-form")
    ok = True
    for v0, v3 in EVEN2:
        psi = vadd(vsc(v0, ket((0, 0))), vsc(v3, ket((1, 1))))
        ok = ok and annihilator_dim(psi, 2) == 2
    for amps in EVEN3:
        psi = vadd(*[vsc(c, ket(t)) for c, t in zip(amps, [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)])])
        ok = ok and annihilator_dim(psi, 3) == 3
    ctrl = vadd(ket((0, 0, 0, 0)), ket((1, 1, 1, 1)))
    ok = ok and annihilator_dim(ctrl, 4) == 0
    GA.check("even vectors of 2 and 3 modes have an annihilator of dimension nu; |0000> + |1111> has none", ok)
    return ok


def check_exponential_form_iff_vacuum_overlap():
    premise("one-relation.imported-cartans-purity-theorem-thouless-form")
    ok = True
    for amps in EVEN3:
        al, x01, x02, x12 = amps
        psi = vadd(*[vsc(c, ket(t)) for c, t in zip(amps, [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)])])
        if al != 0:
            A = [[F(0), x01 / al, x02 / al], [-x01 / al, F(0), x12 / al], [-x02 / al, -x12 / al, F(0)]]
            th, _, _ = thouless(A, 3)
            ok = ok and vsc(al, th) == psi
    ok = ok and sum(1 for amps in EVEN3 if amps[0] != 0) == 2
    a = [ann(k, 2) for k in range(2)]
    p11 = ket((1, 1))
    ok = ok and apply(dag(a[0]), p11) == {} and apply(dag(a[1]), p11) == {}
    for A in ([[F(0), F(7)], [F(-7), F(0)]], SAMPLE_A[2]):
        th, _, _ = thouless(A, 2)
        ok = ok and th.get(0) == 1
    ok = ok and p11.get(0, F(0)) == 0
    GA.check("nonzero vacuum overlap gives the exponential form; |11> is a Witt vacuum outside it", ok)
    return ok
