"""descent-lift.lift-costs-one-rung-per-mode: exact checks (Fock matrices, Jordan-Wigner, Fractions).

(i)   For nu = 2, 3, 4 the matrix ((G^kappa)_AA), kappa over the 2^(nu-1) parity monomials with
      kappa_nu = 0 and A over the 2^(nu-1) even basis states, satisfies M M^T = 2^(nu-1) 1, so it is
      invertible: the record states r_kappa are combinations of the r_A, and a lift needs 2^(nu-1)
      orthonormal even record states. For the lifts of (iii) (nu = 2, 3) W|A> = |A> (x) r_A with
      r_A = sum_kappa (G^kappa)_AA |r_kappa>, every r_A even.
(ii)  The even sector of k rungs has 2^(k-1) basis states (k = 1..6), so the least k with room for
      2^(nu-1) orthonormal even records is k = nu (nu = 2..5); one rung never suffices.
(iii) W = sum_{kappa_nu = 0} G^kappa (x) |r_kappa> for nu = 2 (two rungs) and nu = 3 (three rungs) is
      even, W^dag W = 2^(nu-1), and Tr_R(W |A><B| W^dag) = 2^(nu-1) delta_AB |A><A| on every even
      matrix unit (2^(nu-1) times the descent).
(iv)  For the pair: C (|A> (x) phi) = W|A>, C = 1 - 2 P^R_11 N_0 = 1 - (1/4)(1 - G0)(1 - G2)(1 - G3),
      C diagonal, commuting with every N_k and the total parity, C^2 = 1; phi = |00> + |11> =
      exp(a2^dag a3^dag)|0> (the exponent squares to 0) and is annihilated by c2 = a2 - a3^dag,
      c3 = a3 + a2^dag, which satisfy {c_i, c_j^dag} = 2 delta_ij, {c_i, c_j} = 0: a Witt vacuum.
(v)   Ten number-conserving generators commute with the total number; for each even system state
      A of the pair the joint states with system part A, total number |A| and even parity have record
      part |00> only (one state), so r_00 and r_11 cannot be orthogonal. The record vacuum is killed
      by the hops, the pair annihilation and the Cartan elements. The pairing rotor
      (1 - P) + (3/5) P + (4/5) X, X = a2^dag a3^dag - a3 a2, P = -X^2, is orthogonal, even, and carries
      |00> to (3/5)|00> + (4/5)|11>. The system's pairing 1 + (a0^dag a1^dag - a1 a0), moved to the
      record by the swaps (beam splitters at (cos, sin) = (0, 1) between modes 0, 2 and 1, 3) and
      followed by C, is even and induces 2 E on the even sector.
Not computed: the Bogoliubov algebra so(2(nu + k)) is named, not enumerated.
The proof text now states this closed form, noting that (3/5) + (4/5) X alone is orthogonal only on the
record's even sector (where X^2 = -1).
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


def is_even_vec(v, m):
    return fock.is_even_vec(v)


def is_even_op(M, m):
    return fock.is_even_op(M)


def even_states(m):
    return fock.even_states(m, MSB)
# ---- end of toolkit ----


def mono(kappa, m):
    """G^kappa = prod_k G_k^kappa_k on m modes (kappa may be shorter than m)."""
    M = eye(2 ** m)
    for k, b in enumerate(kappa):
        if b:
            M = mm(M, par(k, m))
    return M


def kappas(nu):
    return [occ(i, nu - 1) + (0,) for i in range(2 ** (nu - 1))]


def lift_W(nu):
    """W = sum_{kappa_nu = 0} G^kappa (x) |r_kappa>, records = even basis of nu rungs (in order)."""
    recs = even_states(nu)
    W = {}
    for kap, r in zip(kappas(nu), recs):
        G = mono(kap, nu)
        ri = idx(r)
        for (i, j), c in G.items():
            W[(i * 2 ** nu + ri, j)] = W.get((i * 2 ** nu + ri, j), F(0)) + c
    return W, recs


def check_record_count_and_lift_form():
    premise("descent-lift.imported-stinespring-kraus-choi")
    premise("descent-lift.kraus-form-descent-even-states")
    ok = True
    for nu in (2, 3, 4):
        ev = even_states(nu)
        M = [[mono(kap, nu)[(idx(A), idx(A))] for A in ev] for kap in kappas(nu)]
        ok = ok and len(M) == 2 ** (nu - 1) and len(ev) == 2 ** (nu - 1)
        MMt = [[sum(a * b for a, b in zip(r1, r2)) for r2 in M] for r1 in M]
        ok = ok and all(MMt[i][j] == (2 ** (nu - 1) if i == j else 0)
                        for i in range(len(M)) for j in range(len(M)))
        ok = ok and GA.field_rank(M) == 2 ** (nu - 1)
    for nu in (2, 3):
        W, recs = lift_W(nu)
        for A in even_states(nu):
            out = apply(W, ket(A))
            ok = ok and all(i // 2 ** nu == idx(A) for i in out)        # system part stays |A>
            rA = {i % 2 ** nu: c for i, c in out.items()}
            ok = ok and is_even_vec(rA, nu)
            want = {}
            for kap, r in zip(kappas(nu), recs):
                want = vadd(want, vsc(mono(kap, nu)[(idx(A), idx(A))], ket(r)))
            ok = ok and rA == want
    GA.check("(i) ((G^kappa)_AA) M M^T = 2^(nu-1) for nu = 2,3,4; lifts have the form |A> (x) r_A, r_A even", ok)
    return ok


def check_even_sector_of_k_rungs():
    ok = True
    counts = [len(even_states(k)) for k in range(1, 7)]
    ok = ok and counts == [1, 2, 4, 8, 16, 32]
    for nu in range(2, 6):
        kmin = min(k for k in range(1, 7) if len(even_states(k)) >= len(even_states(nu)))
        ok = ok and kmin == nu
    ok = ok and len(even_states(1)) < len(even_states(2))           # one rung never suffices
    GA.check("(ii) even sector of k rungs has 2^(k-1) states; a lift needs k >= nu rungs", ok)
    return ok


def check_lift_with_nu_rungs():
    premise("descent-lift.imported-descent-modes-univalence-supplied-class")
    premise("descent-lift.kraus-form-descent-even-states")
    ok = True
    for nu in (2, 3):
        W, recs = lift_W(nu)
        m = 2 * nu
        ok = ok and all(sum(occ(i, m)) % 2 == sum(occ(j, nu)) % 2 for (i, j) in W)   # W even
        ok = ok and mm(dag(W), W) == msc(2 ** (nu - 1), eye(2 ** nu))
        for A in even_states(nu):
            for B in even_states(nu):
                rho = outer(ket(A), ket(B))
                out = ptrace_rec(mm(W, rho, dag(W)), nu)
                want = msc(2 ** (nu - 1), rho) if A == B else {}
                ok = ok and out == want
    W2, _ = lift_W(2)
    G0 = par(0, 2)
    explicit = {}
    for (i, j), c in eye(4).items():
        explicit[(i * 4 + 0, j)] = c                                   # 1 (x) |00>
    for (i, j), c in G0.items():
        explicit[(i * 4 + 3, j)] = explicit.get((i * 4 + 3, j), F(0)) + c   # G0 (x) |11>
    ok = ok and W2 == explicit
    GA.check("(iii) W even, W^dag W = 2^(nu-1), Tr_R W rho W^dag = 2^(nu-1) E(rho) on even units, nu = 2, 3", ok)
    return ok


def check_factorisation_and_coupling():
    premise("descent-lift.imported-thouless-states-witt-vacua")
    ok = True
    m = 4
    G = [par(k, m) for k in range(m)]
    N = [num(k, m) for k in range(m)]
    one = eye(16)
    C = madd(one, msc(-2, mm(N[2], N[3], N[0])))
    poly = madd(one, msc(F(-1, 4), mm(madd(one, msc(-1, G[0])), madd(one, msc(-1, G[2])),
                                      madd(one, msc(-1, G[3])))))
    ok = ok and C == poly
    ok = ok and all(i == j for (i, j) in C)
    ok = ok and all(mm(C, Nk) == mm(Nk, C) for Nk in N)
    Gtot = mm(*G)
    ok = ok and mm(C, Gtot) == mm(Gtot, C)
    ok = ok and mm(C, C) == one
    phi = vadd(ket((0, 0)), ket((1, 1)))
    W, _ = lift_W(2)
    for A in even_states(2):
        joint = {idx(A) * 4 + r: c for r, c in phi.items()}
        ok = ok and apply(C, joint) == apply(W, ket(A))
    a2, a3 = ann(0, 2), ann(1, 2)                                      # the record pair on its own
    X = mm(dag(a2), dag(a3))
    ok = ok and mm(X, X) == {}
    ok = ok and apply(madd(eye(4), X), ket((0, 0))) == phi
    c2 = madd(a2, msc(-1, dag(a3)))
    c3 = madd(a3, dag(a2))
    ok = ok and apply(c2, phi) == {} and apply(c3, phi) == {}
    cs = [c2, c3]
    for i in range(2):
        for j in range(2):
            ok = ok and madd(mm(cs[i], dag(cs[j])), mm(dag(cs[j]), cs[i])) == (msc(2, eye(4)) if i == j else {})
            ok = ok and madd(mm(cs[i], cs[j]), mm(cs[j], cs[i])) == {}
    GA.check("(iv) W = C(. (x) phi), C = 1 - 2 P11 N0 polynomial, diagonal, even, C^2 = 1; phi a Witt vacuum", ok)
    return ok


def rot(X, c, s, d):
    """exp(theta X) = 1 + sin X + (1 - cos) X^2 when X^3 = -X."""
    return madd(eye(d), msc(s, X), msc(1 - c, mm(X, X)))


def check_lift_needs_number_change():
    premise("descent-lift.imported-descent-modes-univalence-supplied-class")
    ok = True
    m = 4
    a = [ann(k, m) for k in range(m)]
    N = [num(k, m) for k in range(m)]
    Ntot = madd(*N)

    def hop(i, j):
        return madd(mm(dag(a[i]), a[j]), mm(dag(a[j]), a[i]))
    C = madd(eye(16), msc(-2, mm(N[2], N[3], N[0])))
    gens = [hop(2, 3), hop(0, 2), hop(1, 3), hop(0, 3), N[0], N[2], N[3], C,
            mm(par(0, m), par(1, m)), mm(N[0], N[2])]
    ok = ok and len(gens) == 10
    ok = ok and all(mm(g, Ntot) == mm(Ntot, g) for g in gens)
    for A in even_states(2):
        allowed = [occ(i, m)[2:] for i in range(16)
                   if occ(i, m)[:2] == A and sum(occ(i, m)) == sum(A)]
        ok = ok and allowed == [(0, 0)]
    vac = ket((0, 0, 0, 0))
    stab = [mm(dag(a[2]), a[3]), mm(dag(a[3]), a[2]), mm(a[3], a[2]), N[2], N[3]]
    ok = ok and all(apply(s_, vac) == {} for s_ in stab)
    X = madd(mm(dag(a[2]), dag(a[3])), msc(-1, mm(a[3], a[2])))
    ok = ok and mm(X, X, X) == msc(-1, X)
    R = rot(X, F(3, 5), F(4, 5), 16)
    ok = ok and mm(dag(R), R) == eye(16) and is_even_op(R, m)
    ok = ok and apply(R, vac) == vadd(vsc(F(3, 5), vac), vsc(F(4, 5), ket((0, 0, 1, 1))))
    Xs = madd(mm(dag(a[0]), dag(a[1])), msc(-1, mm(a[1], a[0])))
    Rs = madd(eye(16), Xs)
    B02 = rot(madd(mm(dag(a[0]), a[2]), msc(-1, mm(dag(a[2]), a[0]))), F(0), F(1), 16)
    B13 = rot(madd(mm(dag(a[1]), a[3]), msc(-1, mm(dag(a[3]), a[1]))), F(0), F(1), 16)
    S = mm(B02, B13)
    ok = ok and mm(dag(S), S) == eye(16)
    U = mm(C, dag(S), Rs, S)
    ok = ok and is_even_op(U, m)
    for A in even_states(2):
        for B in even_states(2):
            rho = outer(ket(A + (0, 0)), ket(B + (0, 0)))
            out = ptrace_rec(mm(U, rho, dag(U)), 2)
            want = msc(2, outer(ket(A), ket(B))) if A == B else {}
            ok = ok and out == want
    GA.check("(v) number-conserving generators allow only r_A = |00>; pairing rotor; system pairing moved by swaps", ok)
    return ok
