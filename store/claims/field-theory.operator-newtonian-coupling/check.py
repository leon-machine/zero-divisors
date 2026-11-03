"""field-theory.operator-newtonian-coupling: exact checks.

Tower planes over the ground Cl(1,3): v = (e + f)/2 creates, w = (e - f)/2 annihilates, N = v w; the
vacuum projector is the product of the w v. G = 1, M_A = 2, M_B = 3; modes A1, A2 (body A's two
branches) and B1, B2; three layouts (r11, r22, r12, r21) = (4, 4, 5, 5), (10, 10, 12, 8), (7, 7, 10, 4).
Phi/t = G M_A M_B (1/r11 + 1/r22 - 1/r12 - 1/r21).
(1) H_N = -G sum M_i M_j N_i N_j / r_ij (GA, four planes) is self-adjoint, commutes with every N, has
the four branch states v_a v_b P0 as eigenstates with real energies, and E11 + E22 - E12 - E21 = -Phi/t,
so the relative phase arg(c11 c22/(c12 c21)) under exp(-I4 H t) is +Phi. The entangling determinant
c11 c22 - c12 c21 of an evolved product state is c12 c21 (u - 1), zero iff the phase ratio u = 1
(rational unit-circle samples).
(2) No interaction between a body's own branches: N_A1 N_A2 and N_B1 N_B2 annihilate every one-body
state. Control: the mean-field (Schrodinger-Newton) source <N> = 1/2 gives E11 + E22 - E12 - E21 = 0
(no entanglement) and a self term -G (M_A^2/r_A + M_B^2/r_B)/2 from the body's own other branch.
(3) Massive modes (premise: the mass block's quasi-particle numbers and block charges are conserved):
on one mass block (K = 0, mu = 1, two planes a, c) gamma = w_a - v_c annihilates the massive vacuum
Omega, N_q = gamma* gamma/2 and Q = n_a - n_c have eigenvalue 0 on Omega and 1 on gamma* Omega, and
H_free = w_a w_c + v_c v_a has gamma* Omega as an eigenstate; operators on different blocks commute
(two blocks). So with either source the branch states are eigenstates with occupations 0/1 and the
phase is again +Phi at all three layouts.
(4) Rigid composites (two unit-mass constituents per body at +-a/2, collinear, D = 20, separation 4):
the internal terms are branch independent and cancel; Phi - Phi_monopole(M = 2) is an exact rational
function f(a) with f(0) = f'(0) = 0 and f''(0) != 0 (a correction of relative order (a/R)^2), and
halving a divides f by a ratio in (7/2, 9/2).
"""
from fractions import Fraction as F

import GA
from GA import mul, add, sub, sc, gen, eq, is_zero, QI
from tp_premise import premise

S4 = (1, -1, -1, -1)
I4 = {(0, 1, 2, 3): F(1)}
G_, MA, MB = F(1), F(2), F(3)
LAYOUTS = [(F(4), F(4), F(5), F(5)), (F(10), F(10), F(12), F(8)), (F(7), F(7), F(10), F(4))]
SELF_R = [F(5), F(2), F(3)]
UNITS = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(1), F(0))]


def scl(c, x):
    return {b: c * v for b, v in x.items() if c * v != 0}


def star(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        out[b] = sign * c
    return {b: c for b, c in out.items() if c != 0}


def planes(n):
    out = []
    for q in range(n):
        e_, f_ = 4 + 2 * q, 5 + 2 * q
        out.append((add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_))),
                    add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_)))))
    return out


def vacuum(pl, S):
    vac = {(): F(1)}
    for (v, w) in pl:
        vac = mul(vac, mul(w, v, S), S)
    return vac


def comm(x, y, S):
    return sub(mul(x, y, S), mul(y, x, S))


def eigen(Y, X):
    """Rational lambda with Y = lambda X, or None."""
    if is_zero(Y):
        return F(0)
    b, c = next(iter(X.items()))
    lam = Y.get(b, F(0)) / c
    return lam if eq(Y, scl(lam, X)) else None


ST4 = tuple(list(S4) + [1, -1] * 4)


def setup4():
    PL = planes(4)
    return PL, [mul(v, w, ST4) for (v, w) in PL], vacuum(PL, ST4)


BRANCHES = ((0, 2), (0, 3), (1, 2), (1, 3))


def check_operator_coupling_gives_registered_phase():
    PL, N4, VAC = setup4()
    for (r11, r22, r12, r21) in LAYOUTS:
        R = {(0, 2): r11, (1, 3): r22, (0, 3): r12, (1, 2): r21}
        HN = {}
        for (i, j), r in R.items():
            HN = add(HN, scl(-G_ * MA * MB / r, mul(N4[i], N4[j], ST4)))
        assert eq(star(HN, ST4), HN) and all(is_zero(comm(HN, n, ST4)) for n in N4)
        E = {}
        for (a, b) in BRANCHES:
            st = mul(mul(PL[a][0], PL[b][0], ST4), VAC, ST4)
            assert not is_zero(st)
            E[(a, b)] = eigen(mul(HN, st, ST4), st)
            assert E[(a, b)] is not None
        dE = E[(0, 2)] + E[(1, 3)] - E[(0, 3)] - E[(1, 2)]
        Phi = G_ * MA * MB * (1 / r11 + 1 / r22 - 1 / r12 - 1 / r21)
        assert -dE == Phi and Phi != 0
    for (x, y) in UNITS:
        u = QI(x, y)
        c12 = c21 = c22 = QI(F(1, 2))
        c11 = QI(F(1, 2)) * u
        det = c11 * c22 - c12 * c21
        assert det == c12 * c21 * (u - 1)
        assert (det == 0) == (u == 1)


def check_no_self_interaction_unlike_mean_field():
    PL, N4, VAC = setup4()
    for (a, b) in BRANCHES:
        st = mul(mul(PL[a][0], PL[b][0], ST4), VAC, ST4)
        assert is_zero(mul(mul(N4[0], N4[1], ST4), st, ST4)) and is_zero(mul(mul(N4[2], N4[3], ST4), st, ST4))
    Mass = [MA, MA, MB, MB]
    for (r11, r22, r12, r21), rs in zip(LAYOUTS, SELF_R):
        R = {(0, 2): r11, (1, 3): r22, (0, 3): r12, (1, 2): r21}
        allR = dict(R)
        allR.update({(0, 1): rs, (2, 3): rs})

        def mean_field(Rs):
            H = {}
            for (i, j), r in Rs.items():
                H = add(H, scl(-G_ * Mass[i] * Mass[j] * F(1, 2) / r, add(N4[i], N4[j])))
            return H

        HSN, HSN0 = mean_field(allR), mean_field(R)
        ESN, E0 = {}, {}
        for (a, b) in BRANCHES:
            st = mul(mul(PL[a][0], PL[b][0], ST4), VAC, ST4)
            ESN[(a, b)] = eigen(mul(HSN, st, ST4), st)
            E0[(a, b)] = eigen(mul(HSN0, st, ST4), st)
        assert ESN[(0, 2)] + ESN[(1, 3)] - ESN[(0, 3)] - ESN[(1, 2)] == 0
        for (a, b) in ((0, 2), (1, 3)):
            selfterm = ESN[(a, b)] - E0[(a, b)]
            assert selfterm == -G_ * F(1, 2) * (MA * MA / rs + MB * MB / rs) and selfterm != 0


def check_massive_sources_quasi_particles_and_block_charges():
    premise("field-theory.conserved-numbers-mass-block")
    ST2 = tuple(list(S4) + [1, -1, 1, -1])
    (va, wa), (vc, wc) = planes(2)
    P0 = vacuum([(va, wa), (vc, wc)], ST2)
    Om = add(P0, mul(mul(va, vc, ST2), P0, ST2))
    g = sub(wa, vc)
    gs = star(g, ST2)
    assert is_zero(mul(g, Om, ST2)) and eq(add(mul(g, gs, ST2), mul(gs, g, ST2)), sc(2))
    Nq = scl(F(1, 2), mul(gs, g, ST2))
    Q = sub(mul(va, wa, ST2), mul(vc, wc, ST2))
    Hfree = add(mul(wa, wc, ST2), mul(vc, va, ST2))
    one = mul(gs, Om, ST2)
    assert not is_zero(one)
    for op in (Nq, Q):
        assert is_zero(comm(Hfree, op, ST2))
        assert eigen(mul(op, Om, ST2), Om) == 0 and eigen(mul(op, one, ST2), one) == 1
    eO, e1 = eigen(mul(Hfree, Om, ST2), Om), eigen(mul(Hfree, one, ST2), one)
    assert eO is not None and e1 is not None and e1 - eO == 1           # the rest energy m = 1
    # operators on different blocks commute: two blocks on four planes
    PL = planes(4)
    g1 = sub(PL[0][1], PL[1][0])
    g2 = sub(PL[2][1], PL[3][0])
    N1 = scl(F(1, 2), mul(star(g1, ST4), g1, ST4))
    N2 = scl(F(1, 2), mul(star(g2, ST4), g2, ST4))
    Q2 = sub(mul(PL[2][0], PL[2][1], ST4), mul(PL[3][0], PL[3][1], ST4))
    assert is_zero(comm(N1, N2, ST4)) and is_zero(comm(N1, Q2, ST4))
    # the phase from the occupations: branch (a, b) occupies blocks a and b
    for (r11, r22, r12, r21) in LAYOUTS:
        R = {(0, 2): r11, (1, 3): r22, (0, 3): r12, (1, 2): r21}
        E = {}
        for (a, b) in BRANCHES:
            n = [1 if k in (a, b) else 0 for k in range(4)]
            E[(a, b)] = sum((-G_ * MA * MB / r * n[i] * n[j] for (i, j), r in R.items()), F(0))
        dE = E[(0, 2)] + E[(1, 3)] - E[(0, 3)] - E[(1, 2)]
        assert -dE == G_ * MA * MB * (1 / r11 + 1 / r22 - 1 / r12 - 1 / r21)


def composite_energy_rf(a_is_var, D, sep, a_val=None):
    """Branch energies (as GA.RF in a, or rationals) for two rigid two-constituent unit-mass bodies.
    Positions: body A at 0 or sep, body B at D or D + sep, constituents at -+a/2."""
    X = GA.RF.var() if a_is_var else None

    def lin(c0, c1):                      # c0 + c1 a
        if a_is_var:
            return GA.RF.const(c0) + GA.RF.const(c1) * X
        return F(c0) + F(c1) * a_val

    E, Eint = {}, set()
    for ba in (0, 1):
        for bb in (0, 1):
            pos = []
            for body, br in ((0, ba), (1, bb)):
                base = (F(0) if br == 0 else sep) if body == 0 else (D if br == 0 else D + sep)
                pos += [(body, (base, F(-1, 2))), (body, (base, F(1, 2)))]
            tot = GA.RF0 if a_is_var else F(0)
            internal = GA.RF0 if a_is_var else F(0)
            for i in range(4):
                for j in range(i + 1, 4):
                    (bi, (pi0, pi1)), (bj, (pj0, pj1)) = pos[i], pos[j]
                    d0, d1 = pj0 - pi0, pj1 - pi1          # pos_j - pos_i, positive for small a
                    term = (GA.RF0 - GA.RF1 / lin(d0, d1)) if a_is_var else -1 / lin(d0, d1)
                    tot = tot + term
                    if bi == bj:
                        internal = internal + term
            E[(ba, bb)] = tot
            Eint.add(internal.eval(F(1, 7)) if a_is_var else internal)
    return E, Eint


def check_rigid_composites_monopole_plus_a_squared():
    D, sep = F(20), F(4)
    mono = F(2) * F(2) * (1 / D + 1 / D - 1 / (D + sep) - 1 / (D - sep))
    E, Eint = composite_energy_rf(True, D, sep)
    assert len(Eint) == 1                                      # internal terms branch independent
    phi = GA.RF0 - (E[(0, 0)] + E[(1, 1)] - E[(0, 1)] - E[(1, 0)])
    f = phi - GA.RF.const(mono)
    assert f.eval(F(0)) == 0
    assert f.deriv().eval(F(0)) == 0
    assert f.deriv().deriv().eval(F(0)) != 0
    diffs = []
    for a in (F(2), F(1)):
        Ea, Ei = composite_energy_rf(False, D, sep, a)
        assert len(Ei) == 1
        diffs.append(-(Ea[(0, 0)] + Ea[(1, 1)] - Ea[(0, 1)] - Ea[(1, 0)]) - mono)
        assert diffs[-1] == f.eval(a)
    ratio = diffs[0] / diffs[1]
    assert diffs[1] != 0 and F(7, 2) < ratio < F(9, 2)
