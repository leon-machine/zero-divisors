"""dark-matter.sourcing-rule-forced-not-chosen: exact checks of clause (ii).

Five-dimensional GTG on the vectors of Cl(1,4), signature (+,-,-,-,-), e0 = t, e1..e3 = x, e4 = y.
  (a) Continuity. The diagonal field hb^{-1}(e_x) = a e_x, hb^{-1}(e_y) = b e_y has volume factor
      det(hb^{-1}) = a^3 b (the wedge of the five frame vectors, at sample times), so dust conservation
      d_t(sqrt(g) rho) = 0 gives rho_5 = C/(a^3 b): in exact rational functions of t, rho' + rho (a^3 b)'/(a^3 b) = 0.
      With L proportional to b, rho_5 L a^3 is constant both for a co-expanding fifth direction (b ~ a)
      and for a static one (b const): the a^-3 dilution, although rho_5 itself goes as a^-4 and a^-3.
  (b) Kaluza-Klein. For a static fifth direction the block field hb^{-1} = hb4^{-1} + b e_y has
      det = b det(hb4^{-1}), so int sqrt(g_5) R_5 carries L = b y_0 and G_4 = G_5/L; with rho_4 = rho_5 L,
      G_4 rho_4 = G_5 rho_5 for every L.
  (c) Projection. Comoving five-dimensional dust T(a) = rho_5 (a.u) u projects to four-dimensional dust
      (no pressure, energy density rho_5 L); a quantum with five-momentum p, Q(p) = m^2, and momentum p_5
      along y has four-dimensional part p_4 with Q(p_4) = m^2 + p_5^2: a heavier particle at rest.
Clause (i) (sourcing by a local density, the integral being the only covariant four-dimensional
tensor) is the statement of the field equations and is not computed beyond (b) and (c).
"""
from fractions import Fraction as F

import GA

S5 = (1, -1, -1, -1, -1)
E5 = [GA.gen(i) for i in range(5)]
RF = GA.RF
T = RF.var()
A_T = RF([F(1), F(1, 2), F(1, 3)])          # a(t) = 1 + t/2 + t^2/3
H4 = [[2, 1, 0, 0], [0, 1, 0, -1], [1, 0, 3, 0], [0, 0, 1, 1]]
TIMES = (F(0), F(1), F(-2, 3), F(5, 2))
LS = (F(1, 3), F(2), F(17, 5))
SAMPLES = ((F(9), [1, 0, 2], F(4)), (F(13, 2), [0, 3, -1], F(-5, 3)), (F(20), [2, 2, 1], F(12)))


def wedge_all(vs):
    out = GA.sc(1)
    for k, v in enumerate(vs):
        out = {b: c for b, c in GA.mul(out, v, S5).items() if len(b) == k + 1}
    return out


def rf_pow(x, n):
    out = RF.const(1)
    for _ in range(n):
        out = out * x
    return out


def check_dust_dilution_exponents():
    ok = True
    for b_t, k5 in ((A_T * RF.const(F(3, 2)), 4), (RF.const(F(4)), 3)):
        vol = rf_pow(A_T, 3) * b_t
        for t in TIMES:
            a, b = A_T.eval(t), b_t.eval(t)
            frame = [E5[0]] + [GA.scal(a, E5[i]) for i in (1, 2, 3)] + [GA.scal(b, E5[4])]
            ok = ok and wedge_all(frame).get((0, 1, 2, 3, 4), F(0)) == vol.eval(t)
        rho = RF.const(1) / vol
        ok = ok and (rho.deriv() + rho * vol.deriv() / vol).is_zero()
        projected = rho * b_t * rf_pow(A_T, 3)                       # rho_5 L a^3, L ~ b
        ok = ok and projected.deriv().is_zero()
        ok = ok and (rho * rf_pow(A_T, k5)).deriv().is_zero()          # rho_5 itself ~ a^-4 or a^-3
        ok = ok and not (rho * rf_pow(A_T, 7 - k5)).deriv().is_zero()
    # by hand: at t = 1, a = 1 + 1/2 + 1/3 = 11/6, so a^3 b (b = 4) = 4 (11/6)^3 = 1331/54
    ok = ok and (rf_pow(A_T, 3) * RF.const(F(4))).eval(F(1)) == F(1331, 54)
    GA.check("dust in the diagonal GTG field: rho_5 = C/(a^3 b), projected density ~ a^-3 for b ~ a and b const", ok)
    assert ok


def check_kaluza_klein_newton_constant_cancels():
    ok = True
    v4 = [GA.add(*[GA.scal(F(H4[m][n]), E5[n]) for n in range(4)]) for m in range(4)]
    d4 = wedge_all(v4).get((0, 1, 2, 3), F(0))
    ok = ok and d4 == 7
    for L in LS:
        y0 = F(3)
        b = L / y0
        d5 = wedge_all(v4 + [GA.scal(b, E5[4])]).get((0, 1, 2, 3, 4), F(0))
        ok = ok and d5 == b * d4 and d5 * y0 == L * d4                 # int dy sqrt(g_5) = L sqrt(g_4)
        G5, rho5 = F(5, 7), F(11, 3)
        G4, rho4 = G5 / L, rho5 * L
        ok = ok and G4 * rho4 == G5 * rho5
    GA.check("Kaluza-Klein: sqrt(g_5) = b sqrt(g_4), G_4 = G_5/L and G_4 rho_4 = G_5 rho_5", ok)
    assert ok


def check_projected_dust_and_heavier_rest_mass():
    ok = True
    rho5, L = F(7, 2), F(3, 5)
    u = E5[0]
    T5 = lambda a: GA.scal(rho5 * GA.dot(a, u, S5), u)
    T4 = lambda a: GA.scal(L, T5(a))
    ok = ok and all(GA.is_zero(T4(E5[i])) for i in (1, 2, 3)) and GA.dot(u, T4(u), S5) == rho5 * L
    for E, p3, p5 in SAMPLES:
        p = GA.add(GA.scal(E, E5[0]), *[GA.scal(p3[i], E5[i + 1]) for i in range(3)], GA.scal(p5, E5[4]))
        m2 = GA.dot(p, p, S5)
        p4 = GA.add(p, GA.scal(GA.dot(p, E5[4], S5), E5[4]))          # remove the y component (Q(e4) = -1)
        ok = ok and GA.dot(p4, E5[4], S5) == 0 and GA.dot(p4, p4, S5) == m2 + p5 * p5
    # rest frame samples by hand: (m, p5) = (3, 4) -> 5, (5, 12) -> 13, (8, 15) -> 17
    for m, p5, M in ((3, 4, 5), (5, 12, 13), (8, 15, 17)):
        p = GA.add(GA.scal(M, E5[0]), GA.scal(p5, E5[4]))
        ok = ok and GA.dot(p, p, S5) == m * m
        p4 = GA.scal(M, E5[0])
        ok = ok and GA.dot(p4, p4, S5) == m * m + p5 * p5
    GA.check("projected comoving dust is dust; momentum along y appears as rest mass sqrt(m^2 + p5^2)", ok)
    assert ok
