"""synthesis.scalar-sector-at-the-isotropic-scalar-kasner-point-obeys-the-spectator-equation: exact checks.

Background: the isotropic point of the scalar Kasner disk, exponents (1/3, 1/3, 1/3), scalar phi_0 = q log T with
c^2 = 8 pi G q^2 = 2/3. The linearised computation uses the mostly-plus component reading
-dT^2 + T^(2/3) sum (dx^i)^2 (the store's sign dT^2 - ... differs by an overall sign, which changes no mode
equation), in which the Einstein-scalar equations read Ric = 8 pi G dphi dphi. Units: delta phi = q u, so every
coefficient is rational (only c^2 = 2/3 enters).

Perturbation in the gauge with unperturbed spatial metric, momentum k along x^1:
  g_00 = -(1 + 2 f(T) cos kx),  g_01 = b(T) sin kx,  g_ij = T^(2/3) delta_ij,  delta phi = q u(T) cos kx.
A formal engine holds terms  coeff * T^n * A^(d)(T) * trig(k x) * k^m  to first order in one unknown function A
(d = -1: no A factor; trig 0 none, 1 cos, 2 sin), and computes Christoffel symbols and the Ricci tensor exactly.

(1) Background: both five-dimensional isotropic vacuum points reduce to (1/3,1/3,1/3), c^2 = 2/3 (stored map);
    the background Ricci tensor is (2/3) T^-2 on T T only, equal to c^2 T^-2; epsilon = -H'/H^2 = 3.
(2) The three linear operators (f alone, b alone, u alone) of E = delta Ric - 8 pi G delta(dphi dphi): pinned
    component by component. The (0,1) component is (2/3)(k/T)(u - f) sin, the (2,2) component is
    -(1/3) T^(-1/3) f' - (1/3)(k/T) b, so f = u and b = -T^(2/3) u'/k are forced for k != 0.
(3) With f = u = A and b = -T^(2/3) A'/k the (0,0) component is -(A'' + A'/T + k^2 T^(-2/3) A) cos and the (1,1)
    component is T^(2/3) times the same operator; every other component vanishes identically. Modulo the
    spectator equation all ten vanish. Controls: the opposite sign of b, f = 2u, and friction 2 in place of 1 fail.
(4) Order zero: on A = T^(2n/3) (s = (3/2) k T^(2/3)) the operator is k^2 T^(-2/3) s-weights [n^2 s^(n-2) + s^n],
    Bessel order 0; control: order 1/2 fails. The comoving curvature perturbation in this gauge is
    (H/phi_0') delta phi = u/3 = f/3.
(5) Clifford reading: in Cl(1,3) the field hbar^-1(e_0) = (1 + eps F) e_0, hbar^-1(e_1) = a e_1 + eps B e_0,
    hbar^-1(e_i) = a e_i has derived metric with first-order parts 2F, B, 0 in (00, 01, 11), and the residue
    B_w = (1/3) sum e_0 e_i completed by c e_0 e_4 in Cl(1,4) is a unit boost exactly for c^2 = 2/3.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

P_ISO = F(1, 3)
C2 = F(2, 3)
D4 = 4


# ---------------------------------------------------------------- formal engine
def eadd(*xs):
    out = {}
    for x in xs:
        for key, v in x.items():
            nv = out.get(key, 0) + v
            if nv == 0:
                out.pop(key, None)
            else:
                out[key] = nv
    return out


def escal(c, x):
    return {key: c * v for key, v in x.items() if c * v != 0}


def emul(x, y):
    out = {}
    for (n1, d1, t1, m1), v1 in x.items():
        for (n2, d2, t2, m2), v2 in y.items():
            if d1 >= 0 and d2 >= 0:
                continue
            key = (n1 + n2, max(d1, d2), max(t1, t2), m1 + m2)
            nv = out.get(key, 0) + v1 * v2
            if nv == 0:
                out.pop(key, None)
            else:
                out[key] = nv
    return out


def ediff(x, coord):
    """coord 0 = T; coord 1 = the momentum axis; any other coordinate gives 0"""
    out = {}
    for (n, d, t, m), v in x.items():
        if coord == 0:
            if n != 0:
                out = eadd(out, {(n - 1, d, t, m): v * n})
            if d >= 0:
                out = eadd(out, {(n, d + 1, t, m): v})
        elif coord == 1 and t:
            out = eadd(out, {(n, d, 2, m + 1): -v} if t == 1 else {(n, d, 1, m + 1): v})
    return out


def mono(c, n):
    return {(F(n), -1, 0, 0): F(c)} if c != 0 else {}


def ricci(G, Gi):
    D = len(G)
    dG = [[[ediff(G[x][y], c) for c in range(D)] for y in range(D)] for x in range(D)]
    Gam = [[[{} for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for s in range(D):
        for x in range(D):
            for y in range(x, D):
                acc = {}
                for l in range(D):
                    if not Gi[s][l]:
                        continue
                    t = eadd(dG[l][y][x], dG[l][x][y], escal(-1, dG[x][y][l]))
                    if t:
                        acc = eadd(acc, emul(Gi[s][l], t))
                Gam[s][x][y] = Gam[s][y][x] = escal(F(1, 2), acc)
    Ric = {}
    for x in range(D):
        for y in range(x, D):
            acc = {}
            for s in range(D):
                acc = eadd(acc, ediff(Gam[s][x][y], s), escal(-1, ediff(Gam[s][x][s], y)))
                for l in range(D):
                    acc = eadd(acc, emul(Gam[s][s][l], Gam[l][x][y]), escal(-1, emul(Gam[s][y][l], Gam[l][x][s])))
            Ric[(x, y)] = acc
    return Ric


def residual(f_term, b_term, u_coeff, p=P_ISO):
    """E = Ric - 8 pi G dphi dphi for g_00 = -(1 + 2 f), g_01 = b, g_ii = T^(2p), phi = q (log T + u cos kx);
    f_term, b_term are engine expressions (cos and sin carried in the keys), u_coeff multiplies u = A."""
    G = [[{} for _ in range(D4)] for _ in range(D4)]
    Gi = [[{} for _ in range(D4)] for _ in range(D4)]
    G[0][0] = eadd(mono(-1, 0), escal(-2, f_term))
    Gi[0][0] = eadd(mono(-1, 0), escal(2, f_term))
    for i in range(1, D4):
        G[i][i] = mono(1, 2 * p)
        Gi[i][i] = mono(1, -2 * p)
    if b_term:
        G[0][1] = G[1][0] = b_term
        # g^{01} = - g^{00} g^{11} g_01 = T^(-2p) b to first order
        Gi[0][1] = Gi[1][0] = emul(b_term, mono(1, -2 * p))
    Ric = ricci(G, Gi)
    src = {(0, 0): eadd(mono(C2, -2), {(F(-1), 1, 1, 0): 2 * C2 * u_coeff}),
           (0, 1): {(F(-1), 0, 2, 1): -C2 * u_coeff}}
    return {key: eadd(Ric[key], escal(-1, src.get(key, {}))) for key in Ric}


def reduce_ode(x, friction, p=P_ISO):
    """replace A^(d), d >= 2, by derivatives of A'' = -friction A'/T - k^2 T^(-2p) A"""
    while True:
        hi = [key for key in x if key[1] >= 2]
        if not hi:
            return x
        key = max(hi, key=lambda q: q[1])
        n, d, t, m = key
        v = x[key]
        x = dict(x)
        del x[key]
        rhs = {(F(-1), 1, 0, 0): -F(friction), (-2 * p, 0, 0, 2): F(-1)}
        for _ in range(d - 2):
            rhs = ediff(rhs, 0)
        x = eadd(x, {(n + a, dd, t, m + mm): v * c for (a, dd, _, mm), c in rhs.items()})


COS_A = {(F(0), 0, 1, 0): F(1)}                        # A cos kx


def b_solution(sign):
    return {(F(1, 3), 1, 2, -1): F(sign)}              # sign * T^(2/3) A' sin(kx) / k


def spectator(prefactor_power, overall):
    """overall * T^prefactor_power * (A'' + A'/T + k^2 T^(-2/3) A) cos kx"""
    n = F(prefactor_power)
    return {(n, 2, 1, 0): F(overall), (n - 1, 1, 1, 0): F(overall), (n - F(2, 3), 0, 1, 2): F(overall)}


# ---------------------------------------------------------------- checks
def check_background_point():
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    for P in ((F(1, 2), F(1, 2), F(1, 2), F(-1, 2)), (F(0), F(0), F(0), F(1))):
        kk = 1 + P[3] / 2
        p = tuple((P[i] + P[3] / 2) / kk for i in range(3))
        c2 = 3 * P[3] * P[3] / (2 * kk * kk)
        GA.check("five-dimensional isotropic vacuum point %s reduces to (1/3,1/3,1/3), c^2 = 2/3" % (P,),
                 sum(P) == 1 and sum(x * x for x in P) == 1 and p == (P_ISO,) * 3 and c2 == C2)
    GA.check("disk relation at the isotropic point: sum p^2 + c^2 = 1", 3 * P_ISO * P_ISO + C2 == 1)
    E = residual({}, {}, 0)
    GA.check("background: Ric = c^2 T^-2 on T T and nothing else (no perturbation)", all(v == {} for v in E.values()))
    bare = residual({}, {}, 0, p=F(1, 2))
    GA.check("control: exponent 1/2 is not a solution with c^2 = 2/3", any(v for v in bare.values()))
    # epsilon = -H'/H^2 with H = p/T, and c^2 = 2 epsilon p^2 (units 8 pi G = 1)
    eps = 1 / P_ISO
    GA.check("epsilon = 3 and c^2 = 2 epsilon H^2 T^2", eps == 3 and 2 * eps * P_ISO * P_ISO == C2)
    return True


def check_three_operators_force_lapse_and_shift():
    premise("synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling")
    Ef = {k: v for k, v in residual(COS_A, {}, 0).items() if v}
    Eb = {k: v for k, v in residual({}, {(F(0), 0, 2, 0): F(1)}, 0).items() if v}
    Eu = {k: v for k, v in residual({}, {}, 1).items() if v}
    GA.check("lapse operator, pinned",
             Ef == {(0, 0): {(F(-2, 3), 0, 1, 2): F(-1), (F(-1), 1, 1, 0): F(1)},
                    (0, 1): {(F(-1), 0, 2, 1): F(-2, 3)},
                    (1, 1): {(F(-1, 3), 1, 1, 0): F(-1, 3), (F(0), 0, 1, 2): F(1)},
                    (2, 2): {(F(-1, 3), 1, 1, 0): F(-1, 3)},
                    (3, 3): {(F(-1, 3), 1, 1, 0): F(-1, 3)}})
    GA.check("shift operator, pinned",
             Eb == {(0, 0): {(F(-2, 3), 1, 1, 1): F(1)},
                    (1, 1): {(F(0), 1, 1, 1): F(-1), (F(-1), 0, 1, 1): F(-2, 3)},
                    (2, 2): {(F(-1), 0, 1, 1): F(-1, 3)},
                    (3, 3): {(F(-1), 0, 1, 1): F(-1, 3)}})
    GA.check("scalar operator, pinned",
             Eu == {(0, 0): {(F(-1), 1, 1, 0): F(-4, 3)}, (0, 1): {(F(-1), 0, 2, 1): F(2, 3)}})
    # (0,1): -(2/3)(k/T) f + (2/3)(k/T) u = 0 forces f = u
    GA.check("momentum constraint forces f = u",
             eadd(Ef[(0, 1)], Eu[(0, 1)]) == {} and Ef[(0, 1)] != {})
    # (2,2): -(1/3) T^(-1/3) f' - (1/3)(k/T) b = 0 forces b = -T^(2/3) f'/k
    b_from_f = residual({}, b_solution(-1), 0)[(2, 2)]
    GA.check("transverse diagonal component forces b = -T^(2/3) f'/k",
             eadd(Ef[(2, 2)], b_from_f) == {} and eadd(Ef[(2, 2)], residual({}, b_solution(1), 0)[(2, 2)]) != {})
    return True


def check_flat_gauge_solution_is_the_spectator_equation():
    premise("synthesis.kasner-approach-gives-horizon-exit-and-index-three")
    E = residual(COS_A, b_solution(-1), 1)
    nonzero = {k: v for k, v in E.items() if v}
    GA.check("only the (0,0) and (1,1) components survive", sorted(nonzero) == [(0, 0), (1, 1)])
    GA.check("(0,0) component is minus the spectator operator", nonzero[(0, 0)] == spectator(0, -1))
    GA.check("(1,1) component is T^(2/3) times the spectator operator", nonzero[(1, 1)] == spectator(F(2, 3), 1))
    GA.check("all ten components vanish modulo A'' + A'/T + k^2 T^(-2/3) A = 0",
             all(reduce_ode(v, 1) == {} for v in E.values()))
    GA.check("control: friction 2 does not solve the equations",
             any(reduce_ode(v, 2) != {} for v in E.values()))
    wrong_shift = residual(COS_A, b_solution(1), 1)
    GA.check("control: the opposite shift fails", any(reduce_ode(v, 1) != {} for v in wrong_shift.values()))
    wrong_lapse = residual(escal(2, COS_A), b_solution(-1), 1)
    GA.check("control: f = 2u fails", any(reduce_ode(v, 1) != {} for v in wrong_lapse.values()))
    return True


def check_order_zero_and_curvature_perturbation():
    premise("synthesis.kasner-approach-gives-horizon-exit-and-index-three")
    q = 1 - P_ISO

    def bessel(n, nu2):
        """k^2 T^(-2p) [(n^2 - nu^2) s^(n-2) + s^n] with s = T^q / q, in powers of T (k = 1)"""
        out = {-2 * P_ISO + q * (n - 2): q * q * (n * n - nu2), -2 * P_ISO + q * n: F(1)}
        return {x: v for x, v in out.items() if v != 0}

    for n in (F(0), F(1), F(2), F(5, 2), F(-1, 2), F(7, 3)):
        e = q * n                                        # A = T^e, a constant times s^n
        lhs = {e - 2: e * (e - 1) + e, e - 2 * P_ISO: F(1)}
        lhs = {x: v for x, v in lhs.items() if v != 0}
        GA.check("order zero on s^n, n = %s" % n, lhs == bessel(n, F(0)))
        GA.check("control: order 1/2 fails, n = %s" % n, lhs != bessel(n, F(1, 4)))
    GA.check("s = k T^q / q with q = 2/3", q == F(2, 3) and 1 / q == F(3, 2))
    # comoving curvature perturbation in the gauge of unperturbed spatial metric: (H/phi_0') q u = (p/T) u T = p u
    GA.check("curvature perturbation is u/3, the lapse perturbation over three", P_ISO == F(1, 3))
    # pump field of the curvature perturbation: z^2 = (phi_0'/H)^2 a^2 = (c^2/p^2) a^2 (units 8 pi G = 1)
    GA.check("z^2/a^2 = c^2/p^2 = 6, a constant", C2 / (P_ISO * P_ISO) == 6)
    return True


def check_clifford_frame_and_residue():
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    sq = (1, -1, -1, -1)
    a, Fv, Bv = F(7, 5), F(3, 11), F(-2, 13)
    met = {}
    for eps in (F(1, 9), F(-1, 9)):
        h = [GA.scal(1 + eps * Fv, GA.gen(0)), GA.add(GA.scal(a, GA.gen(1)), GA.scal(eps * Bv, GA.gen(0))),
             GA.scal(a, GA.gen(2)), GA.scal(a, GA.gen(3))]
        met[eps] = {(i, j): GA.dot(h[i], h[j], sq) for i in range(4) for j in range(i, 4)}
    e1, e2 = F(1, 9), F(-1, 9)
    lin = {key: (met[e1][key] - met[e2][key]) / (e1 - e2) for key in met[e1]}
    expect = {key: F(0) for key in lin}
    expect[(0, 0)] = 2 * Fv
    expect[(0, 1)] = Bv
    GA.check("first-order derived metric: 2F on (0,0), B on (0,1), nothing else", lin == expect)
    even = {key: (met[e1][key] + met[e2][key]) / 2 for key in met[e1]}
    GA.check("zeroth order diag(1, -a^2, -a^2, -a^2), corrections of second order only",
             even[(0, 0)] == 1 + e1 * e1 * Fv * Fv and even[(1, 1)] == -a * a + e1 * e1 * Bv * Bv
             and even[(2, 2)] == -a * a and even[(3, 3)] == -a * a and even[(1, 2)] == 0 and even[(0, 1)] == e1 * e1 * Fv * Bv)
    sq5 = (1, -1, -1, -1, -1)
    Bw = GA.scal(P_ISO, GA.add(GA.mul(GA.gen(0), GA.gen(1), sq5), GA.mul(GA.gen(0), GA.gen(2), sq5),
                             GA.mul(GA.gen(0), GA.gen(3), sq5)))
    B4 = GA.mul(GA.gen(0), GA.gen(4), sq5)
    GA.check("B_w^2 = 1/3, so 1 - B_w^2 = c^2 = 2/3", GA.eq(GA.mul(Bw, Bw, sq5), GA.sc(F(1, 3))) and 1 - F(1, 3) == C2)
    cross = GA.add(GA.mul(Bw, B4, sq5), GA.mul(B4, Bw, sq5))
    GA.check("B_w and e_0 e_4 anticommute and (e_0 e_4)^2 = 1: the completed residue squares to B_w^2 + c^2 = 1",
             GA.is_zero(cross) and GA.eq(GA.mul(B4, B4, sq5), GA.sc(1)))
    return True
