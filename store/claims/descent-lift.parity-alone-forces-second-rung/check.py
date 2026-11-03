"""descent-lift.parity-alone-forces-second-rung: exact checks (Fock matrices, Fractions).

(1) The pair with one rung: the Stinespring dilation W_S psi = psi (x) |0> + G0 psi (x) |1> induces
    Tr_R W_S rho W_S^dag = rho + G0 rho G0 = 2 E(rho), and the occupation copy
    W_O psi = P00 psi (x) |0> + P11 psi (x) |1> induces E(rho), on all four even matrix units.
(2) Both are odd: on the even basis W G_S differs from (G_S (x) G_R) W; the Stinespring records
    |0> +- |1> have both parities, and W_O sends the even |11> to a joint state of odd parity.
(3) No even one-rung lift: the rung's even sector is the single state |0>, so any even map
    |A> -> |A> (x) r_A has r_A on that line and the r_A are not orthogonal (the induced map keeps the
    coherence), as Theorem descent-lift.lift-costs-one-rung-per-mode(i), (ii) says.
(4) Parity is the only obstruction: with two rungs the occupation copy P00 psi (x) |00> + P11 psi (x) |11>
    is even and induces E, and on the even sector the lift W = 1 (x) |00> + G0 (x) |11> of (iii) equals
    P00 (x) (|00> + |11>) + P11 (x) (|00> - |11>).
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

# ---- exact fermionic Fock toolkit: lib/fock.py in MSB order (mode 0 the most significant bit, so
# |sys> (x) |rec> is the index sys * 2^k + rec when the system modes come first) ----
MSB = fock.MSB
dag, mm, msc, eye, apply, vadd = fock.dag, fock.mm, fock.msc, fock.eye, fock.apply, fock.vadd
vsc, outer, ptrace_rec = fock.vsc, fock.outer, fock.ptrace_rec


def occ(i, m):
    return fock.occ(i, m, MSB)


def idx(t):
    return fock.idx(t, MSB)


def par(k, m):
    return fock.mode_parity(k, m, MSB)


def ket(t):
    return fock.ket(t, MSB)


def even_states(m):
    return fock.even_states(m, MSB)
# ---- end of toolkit ----


def sysrec(blocks, k):
    """W = sum_r O_r (x) |r>, blocks = [(O_r, record vector)], record of k rungs."""
    W = {}
    for O, rv in blocks:
        for (i, j), c in O.items():
            for r, a in rv.items():
                key = (i * 2 ** k + r, j)
                W[key] = W.get(key, F(0)) + c * a
    return {key: v for key, v in W.items() if v != 0}


def proj(t, m):
    return outer(ket(t), ket(t))


def check_one_rung_candidates_induce_descent():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    G0 = par(0, 2)
    WS = sysrec([(eye(4), ket((0,))), (G0, ket((1,)))], 1)
    WO = sysrec([(proj((0, 0), 2), ket((0,))), (proj((1, 1), 2), ket((1,)))], 1)
    for A in even_states(2):
        for B in even_states(2):
            rho = outer(ket(A), ket(B))
            ok = ok and ptrace_rec(mm(WS, rho, dag(WS)), 1) == (msc(2, rho) if A == B else {})
            ok = ok and ptrace_rec(mm(WO, rho, dag(WO)), 1) == (rho if A == B else {})
    GA.check("one rung: Stinespring dilation induces 2E, occupation copy induces E, on the even sector", ok)
    return ok


def check_both_one_rung_candidates_are_odd():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    G0 = par(0, 2)
    GS = mm(par(0, 2), par(1, 2))
    GJ = mm(par(0, 3), par(1, 3), par(2, 3))
    WS = sysrec([(eye(4), ket((0,))), (G0, ket((1,)))], 1)
    WO = sysrec([(proj((0, 0), 2), ket((0,))), (proj((1, 1), 2), ket((1,)))], 1)
    bads = [[A for A in even_states(2) if apply(mm(W, GS), ket(A)) != apply(mm(GJ, W), ket(A))]
            for W in (WS, WO)]
    ok = ok and bads == [[(0, 0), (1, 1)], [(1, 1)]]
    recS = [{i % 2: c for i, c in apply(WS, ket(A)).items()} for A in even_states(2)]
    ok = ok and recS == [{0: F(1), 1: F(1)}, {0: F(1), 1: F(-1)}]
    out11 = apply(WO, ket((1, 1)))
    ok = ok and list(out11) == [idx((1, 1, 1))] and sum(occ(idx((1, 1, 1)), 3)) % 2 == 1
    ok = ok and len(even_states(1)) == 1
    GA.check("both one-rung candidates are odd; the rung's even sector is one line", ok)
    return ok


def check_two_rung_occupation_copy_is_even_lift():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    G0 = par(0, 2)
    P00, P11 = proj((0, 0), 2), proj((1, 1), 2)
    WO2 = sysrec([(P00, ket((0, 0))), (P11, ket((1, 1)))], 2)
    ok = ok and all(sum(occ(i, 4)) % 2 == sum(occ(j, 2)) % 2 for (i, j) in WO2)
    for A in even_states(2):
        for B in even_states(2):
            rho = outer(ket(A), ket(B))
            ok = ok and ptrace_rec(mm(WO2, rho, dag(WO2)), 2) == (rho if A == B else {})
    W = sysrec([(eye(4), ket((0, 0))), (G0, ket((1, 1)))], 2)
    Wrot = sysrec([(P00, vadd(ket((0, 0)), ket((1, 1)))), (P11, vadd(ket((0, 0)), vsc(-1, ket((1, 1)))))], 2)
    for A in even_states(2):
        ok = ok and apply(W, ket(A)) == apply(Wrot, ket(A))
    GA.check("two rungs: the occupation copy is even and induces E; W = P00 (x)(|00>+|11>) + P11 (x)(|00>-|11>)", ok)
    return ok
