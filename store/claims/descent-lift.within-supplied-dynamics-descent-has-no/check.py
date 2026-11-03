"""descent-lift.within-supplied-dynamics-descent-has-no: exact checks (Fock matrices, Fractions).

On the pair plus two rungs (4 modes, Jordan-Wigner):
(1) Admissible generators conserve the total number: all hops a_i^dag a_j + a_j^dag a_i (i < j) and
    Cartan elements N_k, and the supplied class (the parity sections G_k and all their products, 16
    monomials), which is moreover joint-number-diagonal.
(2) Quadratic generators that stabilise the vacuum ray carry no pairing: the six states a_i^dag a_j^dag |0>
    are independent (rank 6), so X|0> = sum p_ij a_i^dag a_j^dag |0> + lambda|0> lies on the vacuum ray
    only if p = 0; checked on a sample Hermitian quadratic with and without a pairing part. The Hermitian
    a2 a3 + a3^dag a2^dag built from a pair annihilation carries the vacuum off its ray, to a multiple of
    |0011>.
(3) Theorem descent-lift.lift-costs-one-rung-per-mode(v): a number-conserving unitary keeps
    U(|A> (x) |00>) in total number |A|, so the record must stay |00> and no lift results; adding the
    pairing on the rungs, (1 + X)|00> = |00> + |11>, X = a2^dag a3^dag - a3 a2, followed by the supplied
    coupling C = 1 - 2 N2 N3 N0 induces 2E on the pair: a lift.
(4) The quartic control: K = N0 (a2^dag a3^dag - a3 a2) is real antisymmetric (so iK is Hermitian, the unit
    i commuting with every mode operator), even, kills the joint vacuum, does not commute with the total
    number, K^3 = -K, and exp((pi/2) K) = 1 + K + K^2 equals the closed form
    (1 - N0) + N0 (P^R_odd + a2^dag a3^dag - a3 a2), is orthogonal, and carries psi (x) |00> to the
    two-rung occupation copy P00 psi (x) |00> + P11 psi (x) |11>.
Not computed: the Bogoliubov algebra so(2(nu + k)) is named, not enumerated; the imaginary unit is
represented by the scalar i of the complex Fock space (the proof's I4).
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

# ---- exact fermionic Fock toolkit: lib/fock.py in MSB order (mode 0 the most significant bit, so
# |sys> (x) |rec> is the index sys * 2^k + rec when the system modes come first) ----
MSB = fock.MSB
dag, mm, madd, msc, eye, apply = fock.dag, fock.mm, fock.madd, fock.msc, fock.eye, fock.apply
vadd, vsc, outer, ptrace_rec = fock.vadd, fock.vsc, fock.outer, fock.ptrace_rec


def occ(i, m):
    return fock.occ(i, m, MSB)


def idx(t):
    return fock.idx(t, MSB)


def ann(k, m):
    return fock.ann(k, m, MSB)


def num(k, m):
    return fock.num(k, m, MSB)


def par(k, m):
    return fock.mode_parity(k, m, MSB)


def ket(t):
    return fock.ket(t, MSB)


def is_even_op(M, m):
    return fock.is_even_op(M)


def even_states(m):
    return fock.even_states(m, MSB)
# ---- end of toolkit ----

M4 = 4
SAMPLE_H = {(0, 1): F(2), (1, 2): F(-1, 3), (0, 3): F(5, 7), (2, 3): F(3)}
SAMPLE_CARTAN = [F(1), F(-2), F(1, 2), F(4)]
SAMPLE_P = {(0, 1): F(3, 2), (2, 3): F(-1)}
PSI = (F(4, 5), F(3, 5))


def ops():
    a = [ann(k, M4) for k in range(M4)]
    N = [num(k, M4) for k in range(M4)]
    return a, N


def hop(a, i, j):
    return madd(mm(dag(a[i]), a[j]), mm(dag(a[j]), a[i]))


def quadratic(a, N, with_pairing):
    X = {}
    for (i, j), c in SAMPLE_H.items():
        X = madd(X, msc(c, hop(a, i, j)))
    for k, c in enumerate(SAMPLE_CARTAN):
        X = madd(X, msc(c, N[k]))
    if with_pairing:
        for (i, j), c in SAMPLE_P.items():
            X = madd(X, msc(c, madd(mm(dag(a[i]), dag(a[j])), mm(a[j], a[i]))))
    return X


def check_admissible_generators_conserve_number():
    premise("descent-lift.imported-descent-modes-univalence-supplied-class")
    ok = True
    a, N = ops()
    Ntot = madd(*N)
    hops = [hop(a, i, j) for i in range(M4) for j in range(i + 1, M4)]
    ok = ok and len(hops) == 6
    ok = ok and all(mm(g, Ntot) == mm(Ntot, g) for g in hops + N)
    supplied = []
    for i in range(2 ** M4):
        G = eye(16)
        for k, b in enumerate(occ(i, M4)):
            if b:
                G = mm(G, par(k, M4))
        supplied.append(G)
    ok = ok and len({str(sorted(G.items())) for G in supplied}) == 16
    ok = ok and all(all(mm(G, Nk) == mm(Nk, G) for Nk in N) for G in supplied)
    GA.check("hops, Cartans and the 16 parity monomials conserve number; the monomials are joint-number-diagonal", ok)
    return ok


def check_vacuum_ray_stabilisers_have_no_pairing():
    premise("descent-lift.imported-descent-modes-univalence-supplied-class")
    ok = True
    a, N = ops()
    vac = ket((0, 0, 0, 0))
    pairs = [apply(mm(dag(a[i]), dag(a[j])), vac) for i in range(M4) for j in range(i + 1, M4)]
    rows = [[v.get(k, F(0)) for k in range(16)] for v in pairs]
    ok = ok and GA.field_rank(rows) == 6
    on_ray = lambda v: all(k == 0 for k in v)
    ok = ok and on_ray(apply(quadratic(a, N, False), vac))
    ok = ok and not on_ray(apply(quadratic(a, N, True), vac))
    Y = madd(mm(a[2], a[3]), mm(dag(a[3]), dag(a[2])))
    ok = ok and apply(Y, vac) == {idx((0, 0, 1, 1)): F(-1)}
    GA.check("vacuum-ray stabilisers among quadratics are pairing-free; a2 a3 + h.c. leaves the ray", ok)
    return ok


def check_lift_needs_pairing_on_rungs():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    premise("descent-lift.imported-descent-modes-univalence-supplied-class")
    ok = True
    a, N = ops()
    for A in even_states(2):
        reach = [occ(i, M4) for i in range(16) if occ(i, M4)[:2] == A and sum(occ(i, M4)) == sum(A)]
        ok = ok and reach == [A + (0, 0)]
    X = madd(mm(dag(a[2]), dag(a[3])), msc(-1, mm(a[3], a[2])))
    C = madd(eye(16), msc(-2, mm(N[2], N[3], N[0])))
    U = mm(C, madd(eye(16), X))
    for A in even_states(2):
        for B in even_states(2):
            rho = outer(ket(A + (0, 0)), ket(B + (0, 0)))
            out = ptrace_rec(mm(U, rho, dag(U)), 2)
            ok = ok and out == (msc(2, outer(ket(A), ket(B))) if A == B else {})
    GA.check("number conservation pins the record to |00>; the rung pairing plus C gives 2E", ok)
    return ok


def check_quartic_control():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    a, N = ops()
    Ntot = madd(*N)
    X = madd(mm(dag(a[2]), dag(a[3])), msc(-1, mm(a[3], a[2])))
    K = mm(N[0], X)
    ok = ok and dag(K) == msc(-1, K) and is_even_op(K, M4)
    ok = ok and apply(K, ket((0, 0, 0, 0))) == {}
    ok = ok and mm(K, Ntot) != mm(Ntot, K)
    ok = ok and mm(K, K, K) == msc(-1, K)
    U = madd(eye(16), K, mm(K, K))
    one = eye(16)
    Podd = madd(N[2], N[3], msc(-2, mm(N[2], N[3])))
    closed = madd(madd(one, msc(-1, N[0])), mm(N[0], madd(Podd, X)))
    ok = ok and U == closed
    ok = ok and mm(dag(U), U) == one
    c, s = PSI
    psi = vadd(vsc(c, ket((0, 0, 0, 0))), vsc(s, ket((1, 1, 0, 0))))
    copy = vadd(vsc(c, ket((0, 0, 0, 0))), vsc(s, ket((1, 1, 1, 1))))
    ok = ok and apply(U, psi) == copy
    GA.check("quartic N0(a2+a3+ - a3a2): even, kills vacuum, not number-conserving; its pi/2 rotation is the occupation copy", ok)
    return ok
