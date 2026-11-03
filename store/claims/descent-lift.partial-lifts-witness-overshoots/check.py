"""descent-lift.partial-lifts-witness-overshoots: exact checks (Fock matrices, Fractions).

With the record pair prepared in |00> + A|11> and the coupling C = 1 - 2 P^R_11 N_0 of Theorem
descent-lift.lift-costs-one-rung-per-mode(iv):
(1) on every even matrix unit rho of the pair, Tr_R C (rho (x) r r^T) C^dag = rho + A^2 G0 rho G0, for
    A in {0, 1/2, 3/4, 1, 4/3, 2}; normalised by the record's norm 1 + A^2, the partial descent;
(2) the coherence of (4/5)|00> + (3/5)|11> is multiplied by the computed factor, which matches
    (1 - A^2)/(1 + A^2) at six points (numerator and denominator are polynomials of degree 2, so this is
    the identity), and takes the values 1, 7/25, 0, -7/25 at A = 0, 3/4, 1, 4/3;
(3) the factor vanishes exactly when A^2 = 1 (the numerator 1 - A^2 has the roots +-1 and none of the
    other sample points is a root): the descent is complete iff the record is maximally paired.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

# ---- exact fermionic Fock toolkit: lib/fock.py in MSB order (mode 0 the most significant bit, so
# |sys> (x) |rec> is the index sys * 2^k + rec when the system modes come first) ----
MSB = fock.MSB
dag, mm, madd, msc, eye, vadd = fock.dag, fock.mm, fock.madd, fock.msc, fock.eye, fock.vadd
vsc, outer, trace, ptrace_rec = fock.vsc, fock.outer, fock.trace, fock.ptrace_rec


def num(k, m):
    return fock.num(k, m, MSB)


def par(k, m):
    return fock.mode_parity(k, m, MSB)


def ket(t):
    return fock.ket(t, MSB)


def even_states(m):
    return fock.even_states(m, MSB)
# ---- end of toolkit ----

AMPS = [F(0), F(1, 2), F(3, 4), F(1), F(4, 3), F(2)]
PSI = (F(4, 5), F(3, 5))


def coupling():
    m = 4
    return madd(eye(16), msc(-2, mm(num(2, m), num(3, m), num(0, m))))


def induced(rho, A):
    r = vadd(ket((0, 0)), vsc(A, ket((1, 1))))
    rr = outer(r, r)
    J = {(i * 4 + a, j * 4 + b): x * y for (i, j), x in rho.items() for (a, b), y in rr.items()}
    C = coupling()
    return ptrace_rec(mm(C, J, dag(C)), 2)


def check_partial_descent_map():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    G0 = par(0, 2)
    for A in AMPS:
        for X in even_states(2):
            for Y in even_states(2):
                rho = outer(ket(X), ket(Y))
                ok = ok and induced(rho, A) == madd(rho, msc(A * A, mm(G0, rho, G0)))
    GA.check("record |00> + A|11>: induced map rho + A^2 G0 rho G0 on the pair's even units", ok)
    return ok


def factor(A):
    c, s = PSI
    psi = vadd(vsc(c, ket((0, 0))), vsc(s, ket((1, 1))))
    rho = outer(psi, psi)
    out = induced(rho, A)
    norm = trace(out)
    return out.get((0, 3), F(0)) / rho[(0, 3)], norm


def check_coherence_fraction():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    for A in AMPS:
        num_, norm = factor(A)
        ok = ok and norm == 1 + A * A
        ok = ok and num_ == 1 - A * A
    vals = [factor(A)[0] / factor(A)[1] for A in (F(0), F(3, 4), F(1), F(4, 3))]
    ok = ok and vals == [F(1), F(7, 25), F(0), F(-7, 25)]
    GA.check("coherence factor (1 - A^2)/(1 + A^2): 1, 7/25, 0, -7/25 at A = 0, 3/4, 1, 4/3", ok)
    return ok


def check_complete_iff_maximally_paired():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    zeros = [A for A in AMPS + [F(-1), F(-3, 4)] if factor(A)[0] == 0]
    ok = ok and zeros == [F(1), F(-1)]
    GA.check("the descent is complete exactly at A^2 = 1", ok)
    return ok
