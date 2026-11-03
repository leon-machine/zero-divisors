"""odd-extensions.imported-conformal-completion: exact checks.

(1) A shadow of signature (t, s) completes one rung up its own tower: adjoining the hyperbolic
    plane (n0, ninf with n0.ninf = -1, both null) gives ambient signature (t+1, s+1), the lifts
    X(x) are null, and the residue t - s mod 8 is unchanged; for this world (1,3) the ambient is
    (2,4). All 15 shadows with t + s <= 4.
(2) The conformal spinor space: in the real Cl(2,4), I_6 = e0...e5 squares to -1 and commutes with
    every even element; P = (1 + e0 e2)(1 + e1 e3)/4 is an idempotent of Cl^0(2,4) with
    Cl^0(2,4) P of real dimension 8 and corner P Cl^0 P = span(P, I_6 P), I_6 P squaring to -P
    (so P is primitive and the corner is C): CS = Cl^0(2,4) P = C^4 with complex unit I_6.
(3) The conformal spin group acts through Cl^0(2,4): the action of the even blades on CS is
    faithful (no nonzero even element kills all of Cl^0 P; rank 32 of the even-subalgebra action
    over R) and commutes with the complex structure I_6, so Cl^0(2,4) = Mat_4(C) of real
    dimension 32 = 2 x 4^2.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def check_shadow_completes_one_rung_up():
    premise("correspondence.imported-forced-completion-fibre-quadric")
    ok = True
    count = 0
    for n in range(0, 5):
        for t in range(n + 1):
            s = n - t
            sq = GA.sig(t, s) + (1, -1)
            ep, em = GA.gen(n), GA.gen(n + 1)
            n0 = GA.scal(F(1, 2), GA.sub(em, ep))
            ninf = GA.add(em, ep)
            ok = ok and GA.dot(n0, ninf, sq) == -1 and GA.is_zero(GA.mul(n0, n0, sq))
            G = [[GA.dot(GA.gen(i), GA.gen(j), sq) for j in range(n + 2)] for i in range(n + 2)]
            P, N, Z = GA.congruence_signature(G)
            ok = ok and (P, N, Z) == (t + 1, s + 1, 0) and (P - N) % 8 == (t - s) % 8
            x = {(i,): F(i + 2) for i in range(n)}
            Qx = GA.mul(x, x, sq).get((), F(0))
            X = GA.add(n0, x, GA.scal(Qx / 2, ninf))
            ok = ok and GA.is_zero(GA.mul(X, X, sq))
            count += 1
    sq = GA.sig(1, 3) + (1, -1)
    G = [[GA.dot(GA.gen(i), GA.gen(j), sq) for j in range(6)] for i in range(6)]
    ok = ok and GA.congruence_signature(G) == (2, 4, 0) and count == 15
    GA.check("shadow (t,s) completes to (t+1,s+1), same residue; this world (1,3) -> (2,4)", ok)
    return ok


def _P(sq):
    b1 = GA.mul(GA.gen(0), GA.gen(2), sq)
    b2 = GA.mul(GA.gen(1), GA.gen(3), sq)
    return GA.mul(GA.scal(F(1, 2), GA.add(GA.sc(1), b1)), GA.scal(F(1, 2), GA.add(GA.sc(1), b2)), sq)


def check_conformal_spinor_space_is_c4_with_unit_i6():
    premise("correspondence.spinor-identification")
    sq = GA.sig(2, 4)
    ok = True
    I6 = {tuple(range(6)): F(1)}
    ok = ok and GA.eq(GA.mul(I6, I6, sq), GA.sc(-1))
    evens = [b for b in GA.all_blades(6) if len(b) % 2 == 0]
    odds = [b for b in GA.all_blades(6) if len(b) % 2 == 1]
    ok = ok and all(GA.commutes(I6, {b: F(1)}, sq) for b in evens)
    ok = ok and all(GA.anticommutes(I6, {b: F(1)}, sq) for b in odds)
    P = _P(sq)
    ok = ok and GA.eq(GA.mul(P, P, sq), P) and all(len(b) % 2 == 0 for b in P)
    blades = GA.all_blades(6)
    left = [GA.basis_vector_of(GA.mul({b: F(1)}, P, sq), blades) for b in evens]
    ok = ok and GA.rank_of_vectors(left) == 8
    corner = [GA.basis_vector_of(GA.mul(GA.mul(P, {b: F(1)}, sq), P, sq), blades) for b in evens]
    ok = ok and GA.rank_of_vectors(corner) == 2
    J = GA.mul(I6, P, sq)
    ok = ok and GA.eq(GA.mul(J, J, sq), GA.scal(-1, P))
    ok = ok and GA.rank_of_vectors(corner + [GA.basis_vector_of(J, blades)]) == 2
    GA.check("CS = Cl^0(2,4) P is C^4 (real dimension 8), complex unit I_6, corner C", ok)
    return ok


def check_spin_group_acts_through_even_subalgebra():
    premise("standard-model.imported-fock-representation-clifford-algebra-bogoliubov")
    sq = GA.sig(2, 4)
    ok = True
    P = _P(sq)
    evens = [b for b in GA.all_blades(6) if len(b) % 2 == 0]
    blades = GA.all_blades(6)
    # a real basis of CS
    basis = []
    for b in evens:
        x = GA.mul({b: F(1)}, P, sq)
        if GA.rank_of_vectors([GA.basis_vector_of(y, blades) for y in basis + [x]]) > len(basis):
            basis.append(x)
    ok = ok and len(basis) == 8
    # matrix of left multiplication by each even blade on CS, in coordinates (solve against basis)
    B = [GA.basis_vector_of(y, blades) for y in basis]
    support = [i for i in range(len(blades)) if any(r[i] != 0 for r in B)]
    rows = []
    for b in evens:
        act = []
        for y in basis:
            z = GA.basis_vector_of(GA.mul({b: F(1)}, y, sq), blades)
            sys_ = [[B[k][i] for k in range(8)] for i in support]
            rhs = [z[i] for i in support]
            # least-squares-free exact solve: pick 8 independent rows
            chosen, crow = [], []
            for i, r in enumerate(sys_):
                if GA.rank_of_vectors(crow + [r]) > len(crow):
                    crow.append(r)
                    chosen.append(i)
                if len(crow) == 8:
                    break
            coeff = GA.field_solve([[F(v) for v in r] for r in crow], [rhs[i] for i in chosen])
            ok = ok and all(sum(coeff[k] * B[k][i] for k in range(8)) == z[i] for i in range(len(blades)))
            act.extend(coeff)
        rows.append(act)
    ok = ok and len(rows) == 32 and GA.rank_of_vectors(rows) == 32
    GA.check("Cl^0(2,4) acts faithfully on CS (rank 32 = 2 x 4^2): the spin group acts through it", ok)
    return ok
