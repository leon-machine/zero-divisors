"""correspondence.no-real-lorentzian-vacuum-half-flat: exact checks.

The pointwise statement is checked on the whole space of algebraic Weyl maps, computed in GA.py as the
exact kernel of the Weyl conditions (symmetry under the scalar product <A B>, Ricci trace-freeness
d_a . W(a ^ b) = 0, first Bianchi d_a ^ W(a ^ b) = 0) on the six bivectors of a four-dimensional signature;
complexified bivectors are pairs (re, im) with the scalar i kept distinct from the pseudoscalar I.
(1) Cl(1,3): the Weyl maps form a 10-dimensional space, each commutes with I, I^2 = -1 on bivectors, and the
    +i and -i eigenspaces of I (Lambda^+, Lambda^-) have complex dimension 3 each;
(2) the restriction maps W -> W|Lambda^+ and W -> W|Lambda^- are injective on the real Weyl maps (rank 10),
    so a vanishing duality half forces W = 0;
(3) contrast: in the signatures with I^2 = +1 ((4,0), (2,2), (0,4)) the halves are real and the Weyl maps
    with a vanishing half form a 5-dimensional space, while (1,3) and (3,1) give 0; the Lorentzian
    statement is a statement about I^2 = -1;
(4) the black holes: the store's curvature operator of the static Schwarzschild gravitational field,
    computed from its gauge fields at rational points (flat background with labels (t, r, theta, phi),
    hb^{-1}(e_mu) = theta^a_mu gamma_a, the torsion-free Omega, field strength by the commutator formula,
    calR(B) = -R(hb(B)); exact first-order jets), is a nonzero Weyl map equal to -(M/r^3) S(B) with
    S = -(1/2)(B + 3 sigma_r B sigma_r) and both halves nonzero; the Kerr operator
    (M/2)(r - I a cos(theta))^{-3}(B + 3 sigma_r B sigma_r), computed in R + R I at rational (r, a cos(theta)),
    is a Weyl map, commutes with I, and has both halves nonzero.
The conformal-flatness reading (Weyl's theorem) is a literature equivalence and is not recomputed.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, Field, torsion, curvature) ----
gbiv, apply_op = gtg.biv, gtg.apply_op


# ---- algebraic Weyl maps on the bivectors of a four-dimensional signature (exact) ----
BLADES2 = gtg.bivector_blades(4)


def wop(X, B, sq):
    """Apply the bivector map with matrix X (X[i][j] = blade_i coefficient of W(blade_j)) to bivector B."""
    out = {}
    for j, bl in enumerate(BLADES2):
        c = B.get(bl, F(0))
        if c:
            out = GA.add(out, {BLADES2[i]: c * X[i][j] for i in range(6) if X[i][j]})
    return out


wedge_vb, dot_vb = gtg.outer, gtg.inner_vb                  # a ^ B and a . B for a vector a, bivector B


def weyl_constraints(X, sq):
    """Linear constraints of an algebraic Weyl map: symmetry, Ricci trace-free, first Bianchi."""
    rows = []
    for i in range(6):
        for j in range(i + 1, 6):
            A, B = {BLADES2[i]: F(1)}, {BLADES2[j]: F(1)}
            rows.append(GA.mul(A, wop(X, B, sq), sq).get((), F(0)) - GA.mul(wop(X, A, sq), B, sq).get((), F(0)))
    for nu in range(4):
        tr, bi = {}, {}
        for mu in range(4):
            if mu == nu:
                continue
            Bmn = GA.mul(GA.gen(mu), GA.gen(nu), sq)
            WB = wop(X, Bmn, sq)
            recip = GA.scal(F(1) / sq[mu], GA.gen(mu))
            tr = GA.add(tr, dot_vb(recip, WB, sq))
            bi = GA.add(bi, wedge_vb(recip, WB, sq))
        rows.extend(tr.get((k,), F(0)) for k in range(4))
        rows.extend(bi.get(t, F(0)) for t in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)])
    return rows


def weyl_space(sq):
    """Basis of the algebraic Weyl maps (6 x 6 matrices) of the signature sq, by an exact kernel."""
    cols = []
    for i in range(6):
        for j in range(6):
            X = [[F(1) if (a, b) == (i, j) else F(0) for b in range(6)] for a in range(6)]
            cols.append(weyl_constraints(X, sq))
    mat = [list(r) for r in zip(*cols)]
    return [[[v[6 * i + j] for j in range(6)] for i in range(6)] for v in GA.field_kernel(mat)]


def op_matrix(fn):
    """6 x 6 matrix of a bivector map given as a function on Fraction bivectors."""
    cols = [fn({bl: F(1)}) for bl in BLADES2]
    return [[cols[j].get(BLADES2[i], F(0)) for j in range(6)] for i in range(6)]


LOR = GA.sig(1, 3)
SIGS = {(4, 0): GA.sig(4, 0), (2, 2): GA.sig(2, 2), (0, 4): GA.sig(0, 4), (3, 1): GA.sig(3, 1), (1, 3): GA.sig(1, 3)}
SCHW = [(F(3, 5), F(3, 5), F(4, 5), F(1, 2)), (F(5, 13), F(4, 5), F(3, 5), F(3, 2))]
KERR = [(F(2), F(1), F(1, 2)), (F(3), F(-2), F(5, 2)), (F(1, 2), F(1, 3), F(1))]       # (r, a cos(theta), M)
HALVES = (1, -1)                             # sign of i labelling the two duality halves Lambda^+, Lambda^-


pseudo = gtg.pseudoscalar                    # gamma_0 gamma_1 gamma_2 gamma_3 of the signature sq


def coords(B):
    return [B.get(bl, F(0)) for bl in BLADES2]


def half_rows(X, sq, sign):
    """Row of the restriction of W to a duality half. I^2 = -1: half = {B - sign i I B}, stored (re, im);
    I^2 = +1: half = {B + sign I B} (real)."""
    I4 = pseudo(sq)
    row = []
    for bl in BLADES2:
        B = {bl: F(1)}
        IB = GA.mul(I4, B, sq)
        if GA.mul(I4, I4, sq) == GA.sc(-1):
            row += coords(wop(X, B, sq)) + coords(GA.scal(-sign, wop(X, IB, sq)))
        else:
            row += coords(wop(X, GA.add(B, GA.scal(sign, IB)), sq))
    return row


def static_field(F0, s0, c0, M):
    """Static Schwarzschild field (labels (t, r, theta, phi)) at the radius where sqrt(1 - 2M/r) = F0."""
    r0 = 2 * M / (1 - F0 * F0)
    return gtg.schwarzschild_static(M, r0, s0, c0), r0


def is_weyl(X, sq):
    return all(c == 0 for c in weyl_constraints(X, sq))


def check_weyl_space_and_duality():
    premise("correspondence.imported-weyl-commutes-duality")
    premise("correspondence.lorentzian-duality-complex-structure")
    Ws = weyl_space(LOR)
    I4 = pseudo(LOR)
    MI = op_matrix(lambda B: GA.mul(I4, B, LOR))
    ok = len(Ws) == 10 and GA.mat_eq(GA.mat_mul(MI, MI), [[-1 if i == j else 0 for j in range(6)] for i in range(6)])
    for X in Ws:
        ok = ok and GA.mat_eq(GA.mat_mul(X, MI), GA.mat_mul(MI, X))
    for s in (1, -1):
        shifted = [[GA.QI(MI[i][j]) - (GA.QI(0, s) if i == j else GA.QI(0)) for j in range(6)] for i in range(6)]
        ok = ok and len(GA.field_kernel(shifted)) == 3
    _tp_rv = (ok); assert _tp_rv is not False, "check_weyl_space_and_duality"; return _tp_rv


def check_vanishing_half_forces_vanishing_weyl():
    premise("correspondence.lorentzian-duality-complex-structure")
    Ws = weyl_space(LOR)
    _tp_rv = (all(GA.field_rank([half_rows(X, LOR, s) for X in Ws]) == 10 for s in HALVES)); assert _tp_rv is not False, "check_vanishing_half_forces_vanishing_weyl"; return _tp_rv


def check_signature_contrast():
    want = {(4, 0): 5, (2, 2): 5, (0, 4): 5, (3, 1): 0, (1, 3): 0}
    ok = True
    for pq, sq in SIGS.items():
        Ws = weyl_space(sq)
        ok = ok and len(Ws) == 10
        for s in (1, -1):
            ok = ok and len(Ws) - GA.field_rank([half_rows(X, sq, s) for X in Ws]) == want[pq]
    _tp_rv = (ok); assert _tp_rv is not False, "check_signature_contrast"; return _tp_rv


def check_schwarzschild_and_kerr_are_not_half_flat():
    premise("interior.exact-scale-decoupling")
    premise("interior.imported-kerr-curvature")
    ok = True
    sig_r = gbiv(0, 1)
    I4 = pseudo(LOR)

    def shape(B):
        return GA.scal(F(-1, 2), GA.add(B, GA.scal(3, GA.mul(GA.mul(sig_r, B, LOR), sig_r, LOR))))
    schw = []
    for F0, s0, c0, M in SCHW:
        fld, r0 = static_field(F0, s0, c0, M)
        ok = ok and fld.torsion_free()
        Rc = fld.curvature()
        X = op_matrix(lambda B: apply_op(Rc, B))
        ok = ok and is_weyl(X, LOR) and any(any(row) for row in X)
        ok = ok and GA.mat_eq(X, op_matrix(lambda B: GA.scal(-M / r0 ** 3, shape(B))))
        schw.append((r0, M, X))
        ok = ok and all(any(half_rows(X, LOR, s)) for s in HALVES)

    def kerr(r0, ac, M):
        n2 = r0 * r0 + ac * ac
        zi = GA.add(GA.sc(r0 / n2), GA.scal(ac / n2, I4))            # (r - I a cos)^{-1} = (r + I a cos)/(r^2 + a^2 cos^2)
        z3 = GA.mul(GA.mul(zi, zi, LOR), zi, LOR)
        inv_ok = GA.eq(GA.mul(GA.add(GA.sc(r0), GA.scal(-ac, I4)), zi, LOR), GA.sc(1))
        return inv_ok, op_matrix(lambda B: GA.scal(M / 2, GA.mul(z3, GA.add(B, GA.scal(3, GA.mul(GA.mul(sig_r, B, LOR), sig_r, LOR))), LOR)))
    # a = 0: the Kerr operator is the Schwarzschild curvature operator computed above from the gauge fields
    # (this pins the normalisation M/2 of the Kerr formula against an independent computation)
    for r0, M, Xs in schw:
        ok = ok and GA.mat_eq(kerr(r0, F(0), M)[1], Xs)
    for r0, ac, M in KERR:
        inv_ok, X = kerr(r0, ac, M)
        ok = ok and inv_ok
        MI = op_matrix(lambda B: GA.mul(I4, B, LOR))
        ok = ok and is_weyl(X, LOR) and GA.mat_eq(GA.mat_mul(X, MI), GA.mat_mul(MI, X))
        ok = ok and all(any(half_rows(X, LOR, s)) for s in HALVES)
    _tp_rv = (ok); assert _tp_rv is not False, "check_schwarzschild_and_kerr_are_not_half_flat"; return _tp_rv
