"""descent-lift.classical-record-reproduces-descent-stores-nothing: exact checks (Fock matrices, Fractions).

(1) Two rungs: the record pair in the even mixture (1/2)(|00><00| + |11><11|) and the coupling
    C = 1 - 2 P^R_11 N_0 of Theorem descent-lift.lift-costs-one-rung-per-mode(iv) induce, on every even
    matrix unit of the pair, Tr_R C (rho (x) rho_R) C^dag = (1/2)(rho + G0 rho G0) = E(rho). The joint
    output of the pure inputs (4/5, 3/5), (3/5, -4/5) and (5/13, 12/13) has purity 1/2, while the coherent
    lift W = C(. (x) phi), phi = |00> + |11>, gives purity 1.
(2) One rung: the rung in (1/2)(|0><0| + |1><1|) with the coupling 1 - 2 P^R_1 N_0 again induces E on the
    even sector; the joint output commutes with the total parity and has purity 1/2.
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
vadd = fock.vadd
vsc = fock.vsc
outer = fock.outer
ptrace_rec = fock.ptrace_rec
purity = fock.purity


def num(k, m):
    return fock.num(k, m, MSB)


def par(k, m):
    """Parity of mode k, (-1)^(N_k) = 1 - 2 N_k."""
    return fock.mode_parity(k, m, MSB)


def ket(t):
    return fock.ket(t, MSB)


def even_states(m):
    return fock.even_states(m, MSB)
# ---- end of toolkit ----

INPUTS = [(F(4, 5), F(3, 5)), (F(3, 5), F(-4, 5)), (F(5, 13), F(12, 13))]


def embed_sys(rho, k):
    """rho (x) |0..0><0..0| on the record of k rungs."""
    return {(i * 2 ** k, j * 2 ** k): c for (i, j), c in rho.items()}


def joint(rho, rhoR, k):
    return {(i * 2 ** k + r, j * 2 ** k + s): a * b for (i, j), a in rho.items() for (r, s), b in rhoR.items()}


def check_two_rung_classical_record():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    m = 4
    C = madd(eye(16), msc(-2, mm(num(2, m), num(3, m), num(0, m))))
    rhoR = msc(F(1, 2), madd(outer(ket((0, 0)), ket((0, 0))), outer(ket((1, 1)), ket((1, 1)))))
    for A in even_states(2):
        for B in even_states(2):
            rho = outer(ket(A), ket(B))
            out = ptrace_rec(mm(C, joint(rho, rhoR, 2), dag(C)), 2)
            ok = ok and out == (rho if A == B else {})
    phi = msc(1, outer(vadd(ket((0, 0)), ket((1, 1))), vadd(ket((0, 0)), ket((1, 1)))))
    for c, s in INPUTS:
        psi = vadd(vsc(c, ket((0, 0))), vsc(s, ket((1, 1))))
        rho = outer(psi, psi)
        out = mm(C, joint(rho, rhoR, 2), dag(C))
        ok = ok and purity(out) == F(1, 2)
        lift = mm(C, joint(rho, phi, 2), dag(C))
        ok = ok and purity(lift) == 1
    GA.check("two rungs: classical record induces E on the pair; joint purity 1/2 against 1 for the lift", ok)
    return ok


def check_one_rung_classical_record():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    m = 3
    C1 = madd(eye(8), msc(-2, mm(num(2, m), num(0, m))))
    rhoR = msc(F(1, 2), eye(2))
    Gtot = mm(par(0, m), par(1, m), par(2, m))
    for A in even_states(2):
        for B in even_states(2):
            rho = outer(ket(A), ket(B))
            out = ptrace_rec(mm(C1, joint(rho, rhoR, 1), dag(C1)), 1)
            ok = ok and out == (rho if A == B else {})
    for c, s in INPUTS:
        psi = vadd(vsc(c, ket((0, 0))), vsc(s, ket((1, 1))))
        out = mm(C1, joint(outer(psi, psi), rhoR, 1), dag(C1))
        ok = ok and mm(out, Gtot) == mm(Gtot, out)
        ok = ok and purity(out) == F(1, 2)
    GA.check("one rung: maximally mixed rung with 1 - 2 P1 N0 induces E; output parity-commuting, purity 1/2", ok)
    return ok
