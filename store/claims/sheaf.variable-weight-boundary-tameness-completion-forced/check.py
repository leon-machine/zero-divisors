"""sheaf.variable-weight-boundary-tameness-completion-forced: exact checks at three rational Kasner points
p = (-u, 1+u, u(1+u))/(1+u+u^2), u = 1, 2, 3, in the variable w = tau^(1/D), D = 1+u+u^2, so every tau-power is
a rational function of w; units c1 = 1 + w, c2 = 1 + w^2, c3 = 1 - w^3/2 (nonconstant boundary units).

(1) The frame d tau, sigma1, tau^p2 sigma2, tau^p3 sigma3 has Gram diag(1, -rho c1, -c2, -c3), rho = tau^(-2 p1),
computed from the raw cometric diag(1, -c1 tau^(-2p1), -c2 tau^(-2p2), -c3 tau^(-2p3)); the frame is independent
for tau > 0 (determinant tau^(p2+p3)); at tau = 0 the Gram is diag(1, 0, -1, -1): corank one, radical the
negative-exponent slot; the dying entry over rho tends to -c1(0) = -1 (exactly first order in rho).
(2) s = G^{-1}(e, e) = -1/(rho c1) for e dual to the dying slot; det h = det G (-(1 + 2 mu nu s)) for two
couplings (the determinant identity), and at mu nu = -1/2 det h = c2 c3 (1 + rho c1); F >= 1 at sample collar
points (no shadow wall); at E the wall Gram splits into V1 of signature (1,2) and the (k, n0, ninf) block of
signature (1,2) for mu nu < 0 (the wall Gram lemma), total (2,4), also (2,4) at three interior samples, while
mu nu > 0 gives (3,3).
(3) Weights: rescaling slot i by tau^(a_i) shifts its order by 2 a_i; the corank-one regime with the
negative-exponent slot dying at order rho forces a = (0, 0, p2, p3) and the nondegenerate regime forces
a = (0, p1, p2, p3) (unique solutions of the linear systems); the exceptional Gram is diag(1, -c1, -c2, -c3), at
tau = 0 diag(1, -1, -1, -1), signature (1,3).
(4) The boundary fibre: in the Clifford algebra of diag(1, 0, -1, -1) the ideal J = A k (k the dying generator)
has dimension 8 with J^2 = 0 and quotient Cl(1,2) (structure constants compared); the ladder pair
k* = n0/(2 nu) satisfies the CAR on all 64 states of the boundary ambient fibre.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

KASNER_U = (1, 2, 3)
W = GA.RF.var()


def C(x):
    return GA.RF.const(F(x))


def kasner(u):
    u = F(u)
    D = 1 + u + u * u
    return (-u / D, (1 + u) / D, u * (1 + u) / D), int(D)


def tau_pow(q, D):
    e = F(q) * D
    assert e.denominator == 1
    out = GA.RF1
    for _ in range(abs(e.numerator)):
        out = out * W
    return out if e >= 0 else GA.RF1 / out


COUPLINGS = ((1, F(-1, 2)), (2, F(-3, 4)))      # (nu, mu), mu nu < 0
COLLAR = (F(1, 10), F(1, 3), F(1, 2))
INTERIOR = (F(1, 3), F(1, 2), F(1))
UNITS = (GA.RF1 + W, GA.RF1 + W * W, GA.RF1 - C(F(1, 2)) * W * W * W)


def raw(p, D):
    c1, c2, c3 = UNITS
    return [GA.RF1, -(c1 * tau_pow(-2 * p[0], D)), -(c2 * tau_pow(-2 * p[1], D)), -(c3 * tau_pow(-2 * p[2], D))]


def diag(entries):
    n = len(entries)
    return [[entries[i] if i == j else GA.RF0 for j in range(n)] for i in range(n)]


def at(M, w0):
    return [[e.eval(w0) for e in row] for row in M]


def check_free_module_gram_corank_one():
    ok = True
    c1, c2, c3 = UNITS
    for u in KASNER_U:
        p, D = kasner(u)
        ok = ok and sum(p) == 1 and sum(x * x for x in p) == 1 and p[0] < 0
        wts = [F(0), F(0), p[1], p[2]]
        Gw = [raw(p, D)[i] * tau_pow(2 * wts[i], D) for i in range(4)]
        rho = tau_pow(-2 * p[0], D)
        ok = ok and Gw[0].eqrf(GA.RF1) and Gw[1].eqrf(-(rho * c1)) and Gw[2].eqrf(-c2) and Gw[3].eqrf(-c3)
        frame_det = tau_pow(p[1], D) * tau_pow(p[2], D)
        ok = ok and frame_det.eqrf(tau_pow(1 - p[0], D)) and frame_det.eval(F(1, 2)) != 0
        G0 = [g.eval(F(0)) for g in Gw]
        ok = ok and G0 == [1, 0, -1, -1]
        M0 = [[G0[i] if i == j else F(0) for j in range(4)] for i in range(4)]
        ok = ok and GA.mat_rank(M0) == 3 and GA.congruence_signature(M0) == (1, 2, 1)
        ok = ok and (Gw[1] / rho).eval(F(0)) == -1
    GA.check("W is free with Gram diag(1, -rho c1, -c2, -c3), corank one at E, dying entry first order in rho", ok)
    return ok


def hmat(G4, slot, nu, mu):
    h = [[GA.RF0] * 6 for _ in range(6)]
    for i in range(4):
        for j in range(4):
            h[i][j] = G4[i][j]
    h[slot][4] = h[4][slot] = C(nu)
    h[slot][5] = h[5][slot] = C(mu)
    h[4][5] = h[5][4] = C(-1)
    return h


def check_completion_without_shadow_wall():
    premise("sheaf.determinant-identity-blow-up-expansion")
    premise("sheaf.wall-gram")
    ok = True
    c1, c2, c3 = UNITS
    for u in KASNER_U:
        p, D = kasner(u)
        rho = tau_pow(-2 * p[0], D)
        G4 = diag([GA.RF1, -(rho * c1), -c2, -c3])
        detG = GA.rf_mat_det(G4)
        s = GA.rf_mat_solve(G4, [GA.RF0, GA.RF1, GA.RF0, GA.RF0])[1]
        ok = ok and s.eqrf(-(GA.RF1 / (rho * c1)))
        for nu, mu in COUPLINGS:
            Fn = GA.RF1 + C(2 * nu * mu) * s
            ok = ok and GA.rf_mat_det(hmat(G4, 1, nu, mu)).eqrf(detG * (-Fn))
            for w0 in COLLAR:
                ok = ok and Fn.eval(w0) >= 1
        h = hmat(G4, 1, 1, F(-1, 2))
        ok = ok and GA.rf_mat_det(h).eqrf(c2 * c3 * (GA.RF1 + rho * c1))
        h0 = at(h, F(0))
        V1 = [[h0[i][j] for j in (0, 2, 3)] for i in (0, 2, 3)]
        blk = [[h0[i][j] for j in (1, 4, 5)] for i in (1, 4, 5)]
        ok = ok and GA.congruence_signature(V1) == (1, 2, 0) and GA.congruence_signature(blk) == (1, 2, 0)
        ok = ok and GA.congruence_signature(h0) == (2, 4, 0)
        for w0 in INTERIOR:
            ok = ok and GA.congruence_signature(at(h, w0)) == (2, 4, 0)
        ok = ok and GA.congruence_signature(at(hmat(G4, 1, 1, F(1, 2)), F(0))) == (3, 3, 0)
    GA.check("mu nu < 0: signature (2,4) on the collar and at E, det h = c2 c3 (1 + rho c1), no shadow wall", ok)
    return ok


def check_weights_forced_pointwise():
    ok = True
    c1, c2, c3 = UNITS
    for u in KASNER_U:
        p, D = kasner(u)
        orders = [F(0), -2 * p[0], -2 * p[1], -2 * p[2]]
        two = [[F(2) if i == j else F(0) for j in range(4)] for i in range(4)]
        deg_target = [F(0), -2 * p[0], F(0), F(0)]
        exc_target = [F(0)] * 4
        a_deg = GA.field_solve(two, [deg_target[i] - orders[i] for i in range(4)])
        a_exc = GA.field_solve(two, [exc_target[i] - orders[i] for i in range(4)])
        ok = ok and GA.field_rank(two) == 4
        ok = ok and a_deg == [0, 0, p[1], p[2]] and a_exc == [0, p[0], p[1], p[2]]
        E = [raw(p, D)[i] * tau_pow(2 * a_exc[i], D) for i in range(4)]
        ok = ok and E[0].eqrf(GA.RF1) and E[1].eqrf(-c1) and E[2].eqrf(-c2) and E[3].eqrf(-c3)
        E0 = [[E[i].eval(F(0)) if i == j else F(0) for j in range(4)] for i in range(4)]
        ok = ok and [E0[i][i] for i in range(4)] == [1, -1, -1, -1]
        ok = ok and GA.congruence_signature(E0) == (1, 3, 0)
    GA.check("weights forced pointwise: (0,0,p2,p3) and (0,p1,p2,p3); exceptional Gram (1,3) at E", ok)
    return ok


def check_boundary_fibre_ideal_and_ladder():
    ok = True
    sq = [F(1), F(0), F(-1), F(-1)]                   # boundary Gram, the dying generator is e1
    k = GA.gen(1)
    reps = [GA.mul({I: F(1)}, k, sq) for I in GA.all_blades(4) if 1 not in I]
    blades = GA.all_blades(4)
    ok = ok and GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in reps]) == 8
    ok = ok and all(GA.is_zero(GA.mul(x, y, sq)) for x in reps for y in reps)
    # quotient by J: drop blades containing 1 and relabel (0, 2, 3) -> Cl(1,2) with squares (1, -1, -1)
    sq3 = [F(1), F(-1), F(-1)]
    relabel = {0: 0, 2: 1, 3: 2}
    small = [I for I in GA.all_blades(4) if 1 not in I]
    for I in small:
        for J in small:
            full = GA.mul({I: F(1)}, {J: F(1)}, sq)
            proj = {tuple(relabel[i] for i in b): c for b, c in full.items() if 1 not in b}
            ref = GA.mul({tuple(relabel[i] for i in I): F(1)}, {tuple(relabel[i] for i in J): F(1)}, sq3)
            ok = ok and GA.eq(proj, ref)
    ok = ok and len(small) == 8
    # ladder pair on the boundary ambient fibre, coupling nu = 1, mu = -1/2 on the dying slot
    h0 = [[F(0)] * 6 for _ in range(6)]
    for i, d in enumerate(sq):
        h0[i][i] = d
    h0[1][4] = h0[4][1] = F(1)
    h0[1][5] = h0[5][1] = F(-1, 2)
    h0[4][5] = h0[5][4] = F(-1)
    kv = [F(0), F(1), F(0), F(0), F(0), F(0)]
    ks = [F(0)] * 4 + [F(1, 2), F(0)]
    for S in GA.all_blades(6):
        st = {frozenset(S): F(1)}
        a = GA.ext_c(kv, h0, GA.ext_c(ks, h0, st))
        b = GA.ext_c(ks, h0, GA.ext_c(kv, h0, st))
        tot = dict(a)
        for T, c in b.items():
            tot[T] = tot.get(T, F(0)) + c
        ok = ok and GA.ext_state_eq({T: c for T, c in tot.items() if c != 0}, st)
        ok = ok and GA.ext_c(kv, h0, GA.ext_c(kv, h0, st)) == {} and GA.ext_c(ks, h0, GA.ext_c(ks, h0, st)) == {}
    GA.check("boundary fibre: J = Ak is 8-dimensional, square zero, quotient Cl(1,2); ladder CAR on 64 states", ok)
    return ok
