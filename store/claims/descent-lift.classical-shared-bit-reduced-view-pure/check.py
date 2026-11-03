"""descent-lift.classical-shared-bit-reduced-view-pure: exact checks (Fock matrices, Fractions).

For (c, s) = (4/5, 3/5) the two-rung lift W = 1 (x) |00> + G0 (x) |11> of Theorem
descent-lift.lift-costs-one-rung-per-mode(iii) gives the joint state
c|00>(|00> + |11>) + s|11>(|00> - |11>), which is checked entry by entry. It is even with squared norm 2;
normalised, its pair marginal is diag(16/25, 9/25) on {|00>, |11>} and equals the descent of the pair
state; each single mode of the pair has marginal diag(16/25, 9/25); the record marginal is supported on the
record's even sector with trace 1 and determinant 144/625, so spectrum (16/25, 9/25). The squared
Schmidt coefficients of the pair across the mode-mode cut (from psi psi^T) and of the joint state across
the pair-record cut (from the pair marginal) are both (16/25, 9/25). A control at (5/13, 12/13) gives
(25/169, 144/169) throughout.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

# ---- exact fermionic Fock toolkit: lib/fock.py in MSB order. Basis of m modes: occupation
# tuples; index = sum n_k 2^(m-1-k), so mode 0 is the most significant bit and |sys> (x) |rec>
# is the index sys * 2^k + rec when the system modes come first. ----
MSB = fock.MSB
mm = fock.mm
madd = fock.madd
msc = fock.msc
apply = fock.apply
vadd = fock.vadd
vsc = fock.vsc
outer = fock.outer
inner = fock.inner


def occ(i, m):
    return fock.occ(i, m, MSB)


def idx(t):
    return fock.idx(t, MSB)


def par(k, m):
    """Parity of mode k, (-1)^(N_k) = 1 - 2 N_k."""
    return fock.mode_parity(k, m, MSB)


def ket(t):
    return fock.ket(t, MSB)


def is_even_vec(v, m):
    return fock.is_even_vec(v)            # popcount parity; m kept for the call sites
# ---- end of toolkit ----

CS = (F(4, 5), F(3, 5))
CS_CONTROL = (F(5, 13), F(12, 13))


def keep_modes(M, keep, m):
    """Reduced operator on the modes in `keep` (occupation basis, even states)."""
    out = {}
    rest = [k for k in range(m) if k not in keep]
    for (i, j), c in M.items():
        ti, tj = occ(i, m), occ(j, m)
        if all(ti[k] == tj[k] for k in rest):
            key = (idx([ti[k] for k in keep]), idx([tj[k] for k in keep]))
            out[key] = out.get(key, F(0)) + c
    return {key: v for key, v in out.items() if v != 0}


def lift_state(c, s):
    W = {}
    for i in range(4):
        W[(i * 4, i)] = F(1)
    for (i, j), v in par(0, 2).items():
        W[(i * 4 + 3, j)] = W.get((i * 4 + 3, j), F(0)) + v
    psi = vadd(vsc(c, ket((0, 0))), vsc(s, ket((1, 1))))
    return apply(W, psi), psi


def marginals(c, s):
    out, psi = lift_state(c, s)
    rho = msc(F(1, 2), outer(out, out))
    pair = keep_modes(rho, [0, 1], 4)
    modes = [keep_modes(rho, [k], 4) for k in (0, 1)]
    rec = keep_modes(rho, [2, 3], 4)
    return out, psi, rho, pair, modes, rec


def check_joint_state_and_marginals():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    c, s = CS
    out, psi, rho, pair, modes, rec = marginals(c, s)
    want = {idx((0, 0, 0, 0)): c, idx((0, 0, 1, 1)): c, idx((1, 1, 0, 0)): s, idx((1, 1, 1, 1)): -s}
    ok = ok and out == want
    ok = ok and is_even_vec(out, 4) and inner(out, out) == 2
    ok = ok and pair == {(0, 0): F(16, 25), (3, 3): F(9, 25)}
    E = msc(F(1, 2), madd(outer(psi, psi), mm(par(0, 2), outer(psi, psi), par(0, 2))))
    ok = ok and pair == E
    ok = ok and all(md == {(0, 0): F(16, 25), (1, 1): F(9, 25)} for md in modes)
    ok = ok and all(sum(occ(i, 2)) % 2 == 0 and sum(occ(j, 2)) % 2 == 0 for (i, j) in rec)
    r = [[rec.get((a, b), F(0)) for b in (0, 3)] for a in (0, 3)]
    ok = ok and r[0][0] + r[1][1] == 1 and r[0][0] * r[1][1] - r[0][1] * r[1][0] == F(144, 625)
    GA.check("lift of (4/5, 3/5): pure even joint state; pair, mode and record marginals (16/25, 9/25)", ok)
    return ok


def spectrum_2(M):
    """(trace, determinant) of a 2 x 2 block."""
    return (M[0][0] + M[1][1], M[0][0] * M[1][1] - M[0][1] * M[1][0])


def check_schmidt_coefficients_move_to_pair_record_cut():
    premise("descent-lift.lift-costs-one-rung-per-mode")
    ok = True
    for (c, s), want in ((CS, (1, F(144, 625))), (CS_CONTROL, (1, F(3600, 28561)))):
        out, psi, rho, pair, modes, rec = marginals(c, s)
        mode_mode = [[psi.get(idx((a, b)), F(0)) for b in (0, 1)] for a in (0, 1)]
        mm_rdm = [[sum(mode_mode[a][x] * mode_mode[b][x] for x in (0, 1)) for b in (0, 1)] for a in (0, 1)]
        pr = [[pair.get((a, b), F(0)) for b in (0, 3)] for a in (0, 3)]
        ok = ok and spectrum_2(mm_rdm) == want and spectrum_2(pr) == want
        ok = ok and spectrum_2([[rec.get((a, b), F(0)) for b in (0, 3)] for a in (0, 3)]) == want
    GA.check("Schmidt data (trace, det) of the mode-mode cut equal those of the pair-record cut", ok)
    return ok
