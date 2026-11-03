"""descent-lift.kraus-form-descent-even-states: exact checks (Fock matrices, Jordan-Wigner, Fractions).

(1) For nu = 1, 2, 3 on the full Fock space, 2^(-nu) sum_kappa G^kappa rho G^kappa sends every matrix unit
    |A><B| to delta_AB |A><A|: the pinching (the composite of the mode-wise parity averages).
(2) Kraus rank as Choi rank: 2^nu on the full space (2, 4, 8) and 2^(nu-1) on the even sector (1, 2, 4).
(3) On the even sector G_nu = prod_{k<nu} G_k, so G^kappa and G^(kappa + (1,...,1)) agree there and the
    2^nu monomials give exactly 2^(nu-1) distinct operators; 2^(1-nu) sum_{kappa_nu = 0} G^kappa rho G^kappa is
    the pinching on the even sector; each Kraus operator is even and number-diagonal. For nu = 1 the even
    sector is the vacuum line and the descent is the identity there.
(4) The pair: (1/2)(rho + G0 rho G0) on span{|00>, |11>} takes (4/5)|00> + (3/5)|11> to diag(16/25, 9/25),
    removing the coherence 12/25, and G0, G1 agree on the even sector.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

# ---- exact fermionic Fock toolkit: lib/fock.py in MSB order (mode 0 the most significant bit, so
# |sys> (x) |rec> is the index sys * 2^k + rec when the system modes come first) ----
MSB = fock.MSB
mm, madd, msc, eye, vadd, vsc = fock.mm, fock.madd, fock.msc, fock.eye, fock.vadd, fock.vsc
outer = fock.outer


def occ(i, m):
    return fock.occ(i, m, MSB)


def idx(t):
    return fock.idx(t, MSB)


def par(k, m):
    return fock.mode_parity(k, m, MSB)


def ket(t):
    return fock.ket(t, MSB)


def is_even_op(M, m):
    return fock.is_even_op(M)


def even_states(m):
    return fock.even_states(m, MSB)
# ---- end of toolkit ----


def mono(kappa, m):
    M = eye(2 ** m)
    for k, b in enumerate(kappa):
        if b:
            M = mm(M, par(k, m))
    return M


def restrict(M, states):
    ids = [idx(s) for s in states]
    return [[M.get((i, j), F(0)) for j in ids] for i in ids]


def channel_full(nu):
    mons = [mono(occ(i, nu), nu) for i in range(2 ** nu)]

    def phi(rho):
        out = {}
        for G in mons:
            out = madd(out, mm(G, rho, G))
        return out
    return phi, mons


def choi_rank(phi, states, m):
    d = len(states)
    J = [[F(0)] * (d * d) for _ in range(d * d)]
    for a, A in enumerate(states):
        for b, B in enumerate(states):
            img = phi(outer(ket(A), ket(B)))
            for c, Cs in enumerate(states):
                for e, Ds in enumerate(states):
                    J[a * d + c][b * d + e] = img.get((idx(Cs), idx(Ds)), F(0))
    return GA.field_rank(J)


# Mode counts on which the pinching identity (1) is checked.
NU_PINCH = (1, 2, 3)
# Entry of each sample matrix unit; the pinching identity is linear, so any nonzero entry serves.
UNIT_ENTRY = F(1)


def check_kraus_sum_is_pinching():
    premise("descent-lift.imported-descent-modes-univalence-supplied-class")
    ok = True
    for nu in NU_PINCH:
        phi, mons = channel_full(nu)
        ok = ok and len(mons) == 2 ** nu
        dim = len(fock.states(nu))
        for i in range(dim):
            for j in range(dim):
                unit = {(i, j): UNIT_ENTRY}
                out = msc(F(1, 2 ** nu), phi(unit))
                ok = ok and out == (unit if i == j else {})
    GA.check("(1) 2^-nu sum_kappa G^kappa rho G^kappa is the pinching, nu = 1, 2, 3", ok)
    return ok


def check_kraus_rank_is_choi_rank():
    premise("descent-lift.imported-stinespring-kraus-choi")
    ok = True
    full = []
    even = []
    for nu in (1, 2, 3):
        phi, _ = channel_full(nu)
        full.append(choi_rank(phi, [occ(i, nu) for i in range(2 ** nu)], nu))
        even.append(choi_rank(phi, even_states(nu), nu))
    ok = ok and full == [2, 4, 8] and even == [1, 2, 4]
    GA.check("(2) Choi (Kraus) rank 2^nu on the full space, 2^(nu-1) on the even sector", ok)
    return ok


def check_even_sector_monomials_pair_up():
    premise("descent-lift.imported-descent-modes-univalence-supplied-class")
    ok = True
    for nu in (1, 2, 3, 4):
        ev = even_states(nu)
        Gtot = mono((1,) * nu, nu)
        ok = ok and all(Gtot.get((idx(A), idx(A))) == 1 for A in ev)
        rest = {}
        for i in range(2 ** nu):
            kap = occ(i, nu)
            comp = tuple(1 - b for b in kap)
            ok = ok and restrict(mono(kap, nu), ev) == restrict(mono(comp, nu), ev)
            rest[str(restrict(mono(kap, nu), ev))] = kap
        ok = ok and len(rest) == 2 ** (nu - 1)
        half = [mono(occ(i, nu - 1) + (0,), nu) for i in range(2 ** (nu - 1))]
        ok = ok and all(is_even_op(K, nu) and all(i == j for (i, j) in K) for K in half)
        for A in ev:
            for B in ev:
                rho = outer(ket(A), ket(B))
                out = {}
                for K in half:
                    out = madd(out, mm(K, rho, K))
                out = msc(F(2, 2 ** nu), out)
                ok = ok and out == (rho if A == B else {})
    ev1 = even_states(1)
    ok = ok and ev1 == [(0,)]
    GA.check("(3) on the even sector the monomials pair up: 2^(nu-1) even number-diagonal Kraus operators", ok)
    return ok


C_S = (F(4, 5), F(3, 5))


def check_pair_example():
    premise("descent-lift.imported-descent-modes-univalence-supplied-class")
    ok = True
    c, s = C_S
    psi = vadd(vsc(c, ket((0, 0))), vsc(s, ket((1, 1))))
    rho = outer(psi, psi)
    G0, G1 = par(0, 2), par(1, 2)
    ev = even_states(2)
    ok = ok and restrict(G0, ev) == restrict(G1, ev)
    out = msc(F(1, 2), madd(rho, mm(G0, rho, G0)))
    ok = ok and rho[(0, 3)] == F(12, 25)
    ok = ok and out == {(0, 0): F(16, 25), (3, 3): F(9, 25)}
    GA.check("(4) pair: (4/5)|00> + (3/5)|11> -> diag(16/25, 9/25), coherence 12/25 removed", ok)
    return ok
