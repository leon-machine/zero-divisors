"""synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling: exact checks.

Diagonal Kasner approach, synchronous time T (or tau), metric -dT^2 + sum_a T^(2P_a)(dx^a)^2 in the mostly-plus
reading used for the linearised computation (the store's sign d tau^2 - sum ... differs by an overall sign, which
changes no mode equation), sum_a P_a = 1 over all spatial directions (three observed, any hidden).
(1) Points: the 5D vacuum sphere K5 (sum P = sum P^2 = 1) at the two isotropic points (1/2,1/2,1/2,-1/2) and
    (0,0,0,1) and a generic point (1/5,2/5,4/5,-2/5); 4D vacuum points of the BKL circle; the stored reduction
    p_i = (P_i + P_4/2)/k, k = 1 + P_4/2, c^2 = 3 P_4^2/(2 k^2) sends both isotropic 5D points to
    (1/3,1/3,1/3), c^2 = 2/3.
(2) Linearised field equation of an off-diagonal metric mode h_ab = T^(2 P_b) A(T) cos(k x_j) (a, b, j distinct):
    computed exactly with a formal engine (terms c T^n A^(d) trig(k x_j) k^m, first order in the perturbation):
    delta R_ab = (1/2) T^(2 P_b) [A'' + (1 + 2P_b - 2P_a) A'/T + k^2 T^(-2 P_j) A] cos(k x_j), every other
    component of delta R vanishes, and the background Ricci tensor vanishes on K5 and on the circle.
    Control: with the exponent 1 + 2P_a - 2P_b the identity fails.
(3) Bessel order: for F = tau^(1+w) the operator chi'' + (1+w) chi'/tau + (k^2 tau^(-2p) - xi c^2/tau^2) chi,
    with chi = s^(-alpha) s^n, s = tau^(1-p) (k = 1 - p), alpha = w/(2(1-p)), equals
    k^2 tau^(-2p) s^(-alpha) [(n^2 - nu^2) s^(n-2) + s^n] with nu^2 = (w^2 + 4 xi c^2)/(4(1-p)^2), on every sampled
    (w, xi, c^2, p); control: a shifted nu^2 fails. The Ricci scalar on the disk is R tau^2 = sum p^2 - 1 = -c^2;
    at the isotropic stiff point xi = 1/6 gives nu^2 = 1/4 (conformal coupling, conformally flat point).
(4) Table: off-diagonal mode nu = |P_a - P_b|/(1 - P_j); on the BKL circle the three axes give
    |1-u|/(1+u), (2+u)/u, 1+2u (indices 3 - 2 nu spread by at least 4); the Kaluza-Klein vector (b hidden) has
    nu = 2 at (1/2,1/2,1/2,-1/2) (index -1) and nu = 1 at (0,0,0,1) (index 1); the curvature-coupled scalar at the
    isotropic stiff point has nu^2 = 3 xi/2; the measured index (3 sigma) needs xi in [1.5225, 1.5481].
(7) Equal observed exponents: P = (p,p,p,1-3p) lies in the closed disk exactly for 0 <= p <= 1/2 (vacuum ends p = 0,
    1/2); the Kaluza-Klein vector has nu = |1 - 4p|/(1 - p) in [0, 2], index (5 - 11p)/(1 - p) for p >= 1/4, sweeping [-1, 3];
    the potential's index meets the 3 sigma window only for p in (0.4556, 0.4570), but the field strength's index
    5 - 2 nu lies in [1, 5] on the whole segment (in [1.9523, 1.9775] at the window): blue.
(5) Clifford reading: in Cl(1,4) the residue B5 = sum_a P_a e0 e_a is a unit boost on K5 and
    (e_a B5 - B5 e_a)/2 = P_a e0, so the order's numerator |P_a - P_b| is the difference of the residue weights of
    e_a and e_b.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

NS1, SIG = F("-0.0351"), F("0.0042")

# ---------------------------------------------------------------- formal engine
# key (n, d, tr, m): coefficient * T^n * A^(d)(T) * trig_tr(k x_j) * k^m ; d = -1 means no A factor (order 0),
# tr = 0 none, 1 cos, 2 sin. Products of two first-order terms are dropped.


def eadd(*xs):
    out = {}
    for x in xs:
        for key, v in x.items():
            out[key] = out.get(key, 0) + v
            if out[key] == 0:
                del out[key]
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
            out[key] = out.get(key, 0) + v1 * v2
            if out[key] == 0:
                del out[key]
    return out


def ediff(x, coord, j):
    """coord 0 = T; coord j = the momentum axis; any other coordinate gives 0"""
    out = {}
    for (n, d, t, m), v in x.items():
        if coord == 0:
            if n != 0:
                out = eadd(out, {(n - 1, d, t, m): v * n})
            if d >= 0:
                out = eadd(out, {(n, d + 1, t, m): v})
        elif coord == j and t:
            out = eadd(out, {(n, d, 2, m + 1): -v} if t == 1 else {(n, d, 1, m + 1): v})
    return out


def mono(c, n):
    return {(F(n), -1, 0, 0): F(c)} if c != 0 else {}


def first_order(x):
    return {key: v for key, v in x.items() if key[1] >= 0}


def zeroth_order(x):
    return {key: v for key, v in x.items() if key[1] < 0}


def ricci_offdiag(P, a, b, j, ex_b=None):
    """metric -dT^2 + sum T^(2P)dx^2 + 2 h_ab dx^a dx^b, h_ab = T^(2P_b) A(T) cos(k x_j); coordinates 0..D,
    spatial axis i is coordinate i+1. Returns the full Ricci tensor (dict of index pairs) to first order."""
    D = len(P) + 1
    a, b, j = a + 1, b + 1, j + 1
    G = [[{} for _ in range(D)] for _ in range(D)]
    Gi = [[{} for _ in range(D)] for _ in range(D)]
    G[0][0] = mono(-1, 0)
    Gi[0][0] = mono(-1, 0)
    for i, p in enumerate(P):
        G[i + 1][i + 1] = mono(1, 2 * p)
        Gi[i + 1][i + 1] = mono(1, -2 * p)
    pb = P[b - 1] if ex_b is None else ex_b
    h = {(2 * pb, 0, 1, 0): F(1)}
    G[a][b] = G[b][a] = h
    # inverse to first order: G^ab = -h_ab G^aa G^bb
    inv = escal(-1, emul(emul(h, Gi[a][a]), Gi[b][b]))
    Gi[a][b] = Gi[b][a] = inv
    dG = [[[ediff(G[x][y], c, j) for c in range(D)] for y in range(D)] for x in range(D)]
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
                acc = eadd(acc, ediff(Gam[s][x][y], s, j), escal(-1, ediff(Gam[s][x][s], y, j)))
                for l in range(D):
                    acc = eadd(acc, emul(Gam[s][s][l], Gam[l][x][y]), escal(-1, emul(Gam[s][y][l], Gam[l][x][s])))
            Ric[(x, y)] = acc
    return Ric, Gi


def expected_offdiag(P, a, b, j):
    """(1/2) T^(2P_b) [A'' + (1 + 2P_b - 2P_a) A'/T + k^2 T^(-2P_j) A] cos(k x_j)"""
    pb, pa, pj = P[b], P[a], P[j]
    return {(2 * pb, 2, 1, 0): F(1, 2), (2 * pb - 1, 1, 1, 0): (1 + 2 * pb - 2 * pa) / 2,
            (2 * pb - 2 * pj, 0, 1, 2): F(1, 2)}


def bkl(u):
    d = 1 + u + u * u
    return (-u / d, (1 + u) / d, u * (1 + u) / d)


ISO5_A = (F(1, 2), F(1, 2), F(1, 2), F(-1, 2))
ISO5_B = (F(0), F(0), F(0), F(1))
GEN5 = (F(1, 5), F(2, 5), F(4, 5), F(-2, 5))
SEG_A = (F(1, 4), F(1, 4), F(1, 4), F(1, 4))
SEG_B = (F(5, 12), F(5, 12), F(5, 12), F(-1, 4))


def reduce5(P):
    k = 1 + P[3] / 2
    return tuple((P[i] + P[3] / 2) / k for i in range(3)), 3 * P[3] * P[3] / (2 * k * k)


def check_points_and_reduction():
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    premise("synthesis.bkl-bounce-invariant-holonomy-and-bound")
    for P in (ISO5_A, ISO5_B, GEN5):
        GA.check("K5 point %s: sum 1 and sum of squares 1" % (P,), sum(P) == 1 and sum(x * x for x in P) == 1)
    for P in (ISO5_A, ISO5_B):
        p, c2 = reduce5(P)
        GA.check("isotropic 5D point reduces to (1/3,1/3,1/3), c^2 = 2/3", p == (F(1, 3),) * 3 and c2 == F(2, 3))
        GA.check("disk relations sum p = 1, sum p^2 + c^2 = 1", sum(p) == 1 and sum(x * x for x in p) + c2 == 1)
    p, c2 = reduce5(GEN5)
    GA.check("generic K5 point reduces onto the disk", sum(p) == 1 and sum(x * x for x in p) + c2 == 1)
    GA.check("generic K5 point is anisotropic in the observed directions", len(set(GEN5[:3])) == 3)
    for u in (F(1), F(2), F(7, 3)):
        q = bkl(u)
        GA.check("BKL u = %s on the circle" % u, sum(q) == 1 and sum(x * x for x in q) == 1)
    # equal observed exponents on K5 with sum 1, sum squares 1: 3p + h = 1, 3p^2 + h^2 = 1 -> 12 p^2 - 6 p = 0
    roots = [F(0), F(1, 2)]
    for r in roots:
        GA.check("equal-exponent K5 root p = %s" % r, 12 * r * r - 6 * r == 0 and (r, r, r, 1 - 3 * r) in (ISO5_A, ISO5_B))
    return True


def check_offdiagonal_mode_equation():
    premise("interior.kasner-form-interior")
    premise("synthesis.unit-ball-clauses-hold-at-one-epoch-unless-hidden-direction-co-expands")
    cases = [(ISO5_A, 0, 3, 1), (ISO5_B, 0, 3, 1), (GEN5, 0, 3, 1), (GEN5, 2, 3, 0), (GEN5, 1, 0, 2),
             (bkl(F(2)), 0, 2, 1), (bkl(F(2)), 1, 2, 0), ((F(-1, 3), F(2, 3), F(2, 3)), 0, 2, 1),
             ((F(1, 3), F(1, 3), F(1, 3)), 0, 1, 2), ((F(3, 5), F(1, 5), F(1, 5)), 1, 0, 2),
             (SEG_A, 0, 3, 1), (SEG_B, 1, 3, 2)]
    for P, a, b, j in cases:
        Ric, _ = ricci_offdiag(P, a, b, j)
        lin = first_order(Ric[(min(a, b) + 1, max(a, b) + 1)])
        GA.check("delta R_ab = (1/2) T^(2P_b)[A'' + (1+2P_b-2P_a)A'/T + k^2 T^(-2P_j)A] at %s" % (P,),
                 lin == expected_offdiag(P, a, b, j))
        others = [key for key, v in Ric.items() if key != (min(a, b) + 1, max(a, b) + 1) and first_order(v)]
        GA.check("every other component of delta R vanishes at %s" % (P,), others == [])
        if sum(x * x for x in P) == 1:
            bg = [key for key, v in Ric.items() if zeroth_order(v)]
            GA.check("background Ricci-flat at vacuum point %s" % (P,), bg == [])
        else:
            bg = [key for key, v in Ric.items() if zeroth_order(v)]
            GA.check("disk point %s: background Ricci only along T T (scalar's d phi d phi)" % (P,), bg == [(0, 0)])
    # control: the wrong exponent (a and b exchanged in the pump) fails at an anisotropic point
    P, a, b, j = GEN5, 0, 3, 1
    Ric, _ = ricci_offdiag(P, a, b, j)
    wrong = {(2 * P[b], 2, 1, 0): F(1, 2), (2 * P[b] - 1, 1, 1, 0): (1 + 2 * P[a] - 2 * P[b]) / 2,
             (2 * P[b] - 2 * P[j], 0, 1, 2): F(1, 2)}
    GA.check("control: exchanged pump exponent fails", first_order(Ric[(1, 4)]) != wrong)
    return True


def tau_op(n, w, xi, c2, p):
    """chi'' + (1+w) chi'/tau + (k^2 tau^(-2p) - xi c^2 tau^(-2)) chi for chi = tau^((1-p)(n - alpha)), k = 1-p"""
    k = 1 - p
    alpha = w / (2 * k)
    e = k * (n - alpha)
    coef = e * (e - 1) + (1 + w) * e - xi * c2
    return {e - 2: coef, e + 2 * k - 2: k * k} if coef != 0 else {e + 2 * k - 2: k * k}


def bessel_side(n, w, xi, c2, p, nu2):
    """k^2 tau^(-2p) s^(-alpha) [(n^2 - nu^2) s^(n-2) + s^n] in tau, s = tau^(1-p)"""
    k = 1 - p
    alpha = w / (2 * k)
    out = {}
    e1 = -2 * p + k * (n - 2 - alpha)
    e2 = -2 * p + k * (n - alpha)
    if n * n - nu2 != 0:
        out[e1] = k * k * (n * n - nu2)
    out[e2] = out.get(e2, 0) + k * k
    return {x: v for x, v in out.items() if v != 0}


def nu2_of(w, xi, c2, p):
    return (w * w + 4 * xi * c2) / (4 * (1 - p) ** 2)


def check_bessel_order():
    premise("synthesis.kasner-approach-gives-horizon-exit-and-index-three")
    samples = []
    for p in (F(1, 3), F(-1, 3), F(2, 3), F(1, 5), F(0), F(1, 2)):
        for w in (F(0), F(-2), F(2), F(3, 2), F(-1, 3)):
            for xi, c2 in ((F(0), F(0)), (F(1, 6), F(2, 3)), (F(3, 2), F(2, 3)), (F(1), F(1, 4))):
                samples.append((w, xi, c2, p))
    GA.check("120 parameter sets", len(samples) == 120)
    finger = F(0)
    for (w, xi, c2, p) in samples:
        nu2 = nu2_of(w, xi, c2, p)
        for n in (F(0), F(1), F(2), F(5, 2), F(-1, 2), F(7, 3)):
            finger += sum(tau_op(n, w, xi, c2, p).values()) + nu2
        for n in (F(0), F(1), F(2), F(5, 2), F(-1, 2), F(7, 3)):
            GA.check("operator = Bessel order nu^2 = %s (w=%s, xi=%s, c2=%s, p=%s, n=%s)" % (nu2, w, xi, c2, p, n),
                     tau_op(n, w, xi, c2, p) == bessel_side(n, w, xi, c2, p, nu2))
        # control: a shifted order fails
        GA.check("control: nu^2 + 1/4 fails",
                 tau_op(F(1), w, xi, c2, p) != bessel_side(F(1), w, xi, c2, p, nu2 + F(1, 4)))
    GA.check("pinned fingerprint of the sampled operators and orders", finger == F(3469679, 1080))
    GA.check("pinned instance p = 1/3, w = -2, xi = 3/2, c^2 = 2/3, n = 5/2: nu^2 = 9/2, coefficients 7/9 and 4/9",
             nu2_of(F(-2), F(3, 2), F(2, 3), F(1, 3)) == F(9, 2)
             and tau_op(F(5, 2), F(-2), F(3, 2), F(2, 3), F(1, 3)) == {F(2, 3): F(7, 9), F(2): F(4, 9)})
    # Ricci scalar on the disk, mostly-plus reading: R tau^2 = sum p^2 - 1 = -c^2 (from the engine at order 0)
    for P in ((F(1, 3), F(1, 3), F(1, 3)), (F(3, 5), F(1, 5), F(1, 5)), (F(1, 2), F(1, 2), F(0))):
        Ric, Gi = ricci_offdiag(P, 0, 1, 2)
        Rs = {}
        for x in range(4):
            Rs = eadd(Rs, emul(Gi[x][x], zeroth_order(Ric[(x, x)])))
        c2 = 1 - sum(t * t for t in P)
        GA.check("R tau^2 = -c^2 at %s" % (P,), Rs == {(F(-2), -1, 0, 0): -c2})
    # conformal consistency: xi = 1/6 at the isotropic stiff point gives nu = 1/2 (conformally flat, conformal field)
    GA.check("xi = 1/6, w = 0 at (1/3,1/3,1/3), c^2 = 2/3: nu^2 = 1/4", nu2_of(F(0), F(1, 6), F(2, 3), F(1, 3)) == F(1, 4))
    GA.check("scalar at the isotropic stiff point: nu^2 = 3 xi/2", nu2_of(F(0), F(5, 7), F(2, 3), F(1, 3)) == F(15, 14))
    return True


def nu_off(P, a, b, j):
    return abs(P[a] - P[b]) / (1 - P[j])


def check_index_table():
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    # off-diagonal mode order is |w|/(2(1-p_j)) with w = 2(P_b - P_a): the pump exponent of check (2)
    for P, a, b, j in ((GEN5, 0, 3, 1), (ISO5_A, 0, 3, 1)):
        w = 2 * P[b] - 2 * P[a]
        GA.check("off-diagonal order nu^2 = w^2/(4(1-P_j)^2)", nu2_of(w, F(0), F(0), P[j]) == nu_off(P, a, b, j) ** 2)
    # Kaluza-Klein vector (b = hidden index 3) at the two isotropic 5D points, every observed (a, j) pair
    for P, nu in ((ISO5_A, F(2)), (ISO5_B, F(1))):
        vals = {nu_off(P, a, 3, j) for a in range(3) for j in range(3) if a != j}
        GA.check("KK vector order %s at %s for every polarisation and axis" % (nu, P), vals == {nu})
    GA.check("KK vector index at (1/2,1/2,1/2,-1/2): 3 - 2 nu = -1", 3 - 2 * F(2) == -1)
    GA.check("KK vector index at (0,0,0,1): 3 - 2 nu = 1", 3 - 2 * F(1) == 1)
    # observed-observed off-diagonal (graviton) modes at the isotropic points: order 0
    for P in (ISO5_A, ISO5_B, (F(1, 3), F(1, 3), F(1, 3))):
        GA.check("graviton cross mode at isotropic point has order 0", {nu_off(P, 0, 1, 2), nu_off(P, 1, 2, 0)} == {0})
    # BKL circle: orders per axis and their spread
    for u in (F(1), F(3, 2), F(2), F(4), F(7, 3), F(10)):
        p = bkl(u)
        nus = (nu_off(p, 1, 2, 0), nu_off(p, 0, 2, 1), nu_off(p, 0, 1, 2))
        GA.check("BKL u = %s cross-mode orders (|1-u|/(1+u), (2+u)/u, 1+2u)" % u,
                 nus == (abs(1 - u) / (1 + u), (2 + u) / u, 1 + 2 * u))
        idx = [3 - 2 * x for x in nus]
        GA.check("BKL u = %s: largest-exponent axis index 1 - 4u <= -3" % u, idx[2] == 1 - 4 * u and idx[2] <= -3)
        GA.check("BKL u = %s: index spread between axes at least 4" % u, max(idx) - min(idx) >= 4)
    # measured window, 3 sigma
    lo, hi = NS1 - 3 * SIG, NS1 + 3 * SIG
    GA.check("window [-0.0477, -0.0225]", (lo, hi) == (F("-0.0477"), F("-0.0225")))
    fixed = {"minimal scalar or graviton cross mode at an isotropic point (nu = 0, index in [2,3])": F(2),
             "conformal scalar or 4D gauge vector (nu = 1/2)": F(2),
             "KK vector at (1/2,1/2,1/2,-1/2)": F(-1), "KK vector at (0,0,0,1)": F(1)}
    for name, val in fixed.items():
        GA.check("fixed coupling outside the 3 sigma window: %s" % name, not (lo <= val <= hi))
    GA.check("KK vector at the 5D isotropic wall: more than 229 sigma from the measured index",
             abs(F(-1) - NS1) > 229 * SIG)
    # curvature coupling needed at the isotropic stiff point: n - 1 = 3 - sqrt(6 xi), xi = (3 - (n-1))^2/6
    xlo, xhi = (3 - hi) ** 2 / 6, (3 - lo) ** 2 / 6
    GA.check("xi window bounds", F("1.5225") < xlo < F("1.5226") and F("1.5480") < xhi < F("1.5481"))
    GA.check("xi = 3/2 gives nu = 3/2 exactly (scale invariance), outside the window",
             nu2_of(F(0), F(3, 2), F(2, 3), F(1, 3)) == F(9, 4) and not (xlo <= F(3, 2) <= xhi))
    premise("synthesis.imported-einstein-cartan-matter-coupling")
    GA.check("minimal (0) and conformal (1/6) couplings outside the xi window", not (xlo <= 0 <= xhi) and not (xlo <= F(1, 6) <= xhi))
    GA.check("minimal coupling: index 3 - sqrt(6 * 0) = 3; conformal: 3 - sqrt(6/6) = 2",
             nu2_of(F(0), F(0), F(2, 3), F(1, 3)) == 0 and 3 - 2 * F(1, 2) == 2 and nu2_of(F(0), F(1, 6), F(2, 3), F(1, 3)) == F(1, 2) ** 2)
    return True


def check_clifford_weights():
    premise("synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall")
    SQ = (1, -1, -1, -1, -1)
    for P in (ISO5_A, ISO5_B, GEN5):
        B = GA.add(*[GA.scal(P[a], GA.mul(GA.gen(0), GA.gen(a + 1), SQ)) for a in range(4)])
        GA.check("B5 is a unit boost at %s" % (P,), GA.eq(GA.mul(B, B, SQ), GA.sc(1)))
        for a in range(4):
            ea = GA.gen(a + 1)
            comm = GA.scal(F(1, 2), GA.add(GA.mul(ea, B, SQ), GA.scal(-1, GA.mul(B, ea, SQ))))
            GA.check("(e_a B5 - B5 e_a)/2 = P_a e0", GA.eq(comm, GA.scal(P[a], GA.gen(0))))
    return True


def seg_point(p):
    return (p, p, p, 1 - 3 * p)


def check_isotropic_segment():
    premise("synthesis.kasner-wall-matter-maxwell-bounces-stiff-moves-residue")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    grid = [F(n, 120) for n in range(-60, 121)]
    for p in grid:
        P = seg_point(p)
        s2 = sum(x * x for x in P)
        GA.check("sum of squares 1 + 12p^2 - 6p at p = %s" % p, s2 == 1 + 12 * p * p - 6 * p)
        GA.check("in the closed disk iff 0 <= p <= 1/2 (p = %s)" % p, (s2 <= 1) == (0 <= p <= F(1, 2)))
        GA.check("on the vacuum sphere iff p in {0, 1/2} (p = %s)" % p, (s2 == 1) == (p in (F(0), F(1, 2))))
    seg = [p for p in grid if 0 <= p <= F(1, 2)]
    GA.check("segment grid has 61 points", len(seg) == 61)
    for p in seg:
        P = seg_point(p)
        r = abs(1 - 3 * p) / (1 - p)
        GA.check("hidden-to-observed ratio |1 - 3p|/(1 - p) <= 1 at p = %s" % p, r <= 1 and r == abs(P[3]) / (1 - P[0]))
        nkk = nu_off(P, 0, 3, 1)
        GA.check("KK vector order |1 - 4p|/(1 - p) at p = %s" % p, nkk == abs(1 - 4 * p) / (1 - p) and 0 <= nkk <= 2)
        if p >= F(1, 4):
            GA.check("KK vector index (5 - 11p)/(1 - p) at p = %s" % p, 3 - 2 * nkk == (5 - 11 * p) / (1 - p))
    GA.check("KK vector index sweeps [-1, 3]: -1 at p = 1/2, 3 at p = 1/4",
             3 - 2 * nu_off(seg_point(F(1, 2)), 0, 3, 1) == -1 and 3 - 2 * nu_off(seg_point(F(1, 4)), 0, 3, 1) == 3)
    # window: index x in [lo, hi] -> p = (5 - x)/(11 - x), decreasing in x
    lo, hi = NS1 - 3 * SIG, NS1 + 3 * SIG
    plo, phi = (5 - hi) / (11 - hi), (5 - lo) / (11 - lo)
    GA.check("KK transverse potential index meets the window only for p in (0.4556, 0.4570)",
             F("0.4556") < plo < phi < F("0.4570") and (5 - 11 * plo) / (1 - plo) == hi and (5 - 11 * phi) / (1 - phi) == lo)
    GA.check("the window's p is interior to the segment, not a vacuum end or the static point",
             F(1, 3) < plo and phi < F(1, 2))
    # field strength: magnetic part d_j A_a carries one more power of k, index 5 - 2 nu; blue on the whole segment
    fs = [5 - 2 * nu_off(seg_point(p), 0, 3, 1) for p in seg]
    GA.check("KK field-strength index 5 - 2 nu in [1, 5] on the segment, minimum 1 at p = 1/2 only",
             min(fs) == 1 and max(fs) == 5 and [p for p in seg if 5 - 2 * nu_off(seg_point(p), 0, 3, 1) == 1] == [F(1, 2)])
    GA.check("KK field-strength index at p = 1/4 is 5 and at p = 5/12 is 19/7",
             5 - 2 * nu_off(seg_point(F(1, 4)), 0, 3, 1) == 5 and 5 - 2 * nu_off(seg_point(F(5, 12)), 0, 3, 1) == F(19, 7))
    # at the window ends the potential index is x, nu = (3 - x)/2, field strength 5 - 2 nu = 2 + x in [1.9523, 1.9775]
    for pp, x in ((plo, hi), (phi, lo)):
        nu = nu_off(seg_point(pp), 0, 3, 1)
        GA.check("at the window end p = %s: nu = (3 - x)/2 and field-strength index 2 + x" % pp,
                 nu == (3 - x) / 2 and 5 - 2 * nu == 2 + x)
    GA.check("field-strength index at the window lies in [1.9523, 1.9775], blue",
             (2 + lo, 2 + hi) == (F("1.9523"), F("1.9775")) and 2 + lo > 1)
    # leading superhorizon branch s^(-alpha - nu) is constant in time for the KK vector exactly when p > 1/4
    for p in seg:
        P = seg_point(p)
        alpha = (2 * P[3] - 2 * P[0]) / (2 * (1 - P[1]))
        GA.check("alpha = -nu iff p >= 1/4 (p = %s)" % p, (alpha == -nu_off(P, 0, 3, 1)) == (p >= F(1, 4)))
    return True
