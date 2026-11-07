"""synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower: exact checks.

Tower level Cl(N, N+2), generators in the order e_0 (+1), e_1 (-1), e_2 (-1), e_3 (-1), then for
j = 1, ..., N-1 the plane e_j' (+1), f_j' (-1). Transport (hyperbolic) planes: (e_0, e_1) and the
N-1 tower planes; kernel g_1 = e_2, g_2 = e_3, J = e_2 e_3. Ladder of plane P = (e, f):
v = (e + f)/2 (= a*), w = (e - f)/2 (= a), n = v w. omega_P = e f, Gamma = product of the omega_P.
The adjoint * is the antiautomorphism fixing generators of square +1 and negating those of square -1.

(i)   in Cl(N, N) the commutant of the even part is span{1, Gamma}, Gamma^2 = +1, and
      (alpha + beta Gamma)^2 = alpha^2 + beta^2 + 2 alpha beta Gamma (N = 1, 2, 3);
(ii)  J^2 = -1, J* = -J, J commutes with every plane generator; CAR of the ladder; * is an
      antiautomorphism with v* = w; J = I_4 sigma (N = 1, 2, 3);
(iii) the commutant of the plane generators in Cl(N, N+2) is span{1, J, Gamma g_1, Gamma g_2}, a
      quaternion algebra, even part span{1, J}; the kernel rotor fixes J and turns Gamma g_1;
      with (e_0, e_1) in the ground instead, the even commutant contains I_4 and J (N = 2);
(iv)  I_n = J Gamma, I_n^2 = -1, I_n* = -I_n, Gamma* = Gamma, Gamma = prod (1 - 2 n_j), Gamma
      anticommutes with modes and commutes with pairs, I_n (1 +- Gamma)/2 = +-J (1 +- Gamma)/2,
      Ad(I_n) negates every generator;
(v)   phi = S + S*, pi = J(S* - S), S = sum_k v_{2k} w_{2k+1}: self-adjoint, [phi, pi] = 2 J [S, S*]
      = 2 J sum_k (n_{2k} - n_{2k+1}); on (S*)^j P_pol it is 2 (M - 2j) J; density modes on a window
      of four modes: [phi_q, pi_q] = 2 J (edge operator), 2 q J on the edge-clean projector,
      [rho_1, rho_2] = 0 and the mixed identities;
(vi)  the reflection e_3 -> -e_3 fixes every plane generator and negates J, I_4, I_n and pi; the
      phase circle Ad(e^{theta J Q/2}) multiplies S by e^{theta J} and turns (phi, pi).
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F
import itertools
import GA
from tp_premise import premise


# ----------------------------------------------------------------------------- algebra set-up

def level(N):
    """Squares and planes of Cl(N, N+2): radial plane (0, 1), kernel (2, 3), tower planes after."""
    sq = [1, -1, 1, -1]
    planes = [(0, 1)]
    for _ in range(N - 1):
        i = len(sq)
        sq += [1, -1]
        planes.append((i, i + 1))
    return tuple(sq), planes


def hyperbolic(N):
    """Squares and planes of Cl(N, N) alone."""
    sq, planes = [], []
    for _ in range(N):
        i = len(sq)
        sq += [1, -1]
        planes.append((i, i + 1))
    return tuple(sq), planes


def g(i):
    return GA.gen(i)


def m(sq, *xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def comm(sq, a, b):
    return GA.sub(m(sq, a, b), m(sq, b, a))


def acomm(sq, a, b):
    return GA.add(m(sq, a, b), m(sq, b, a))


def star(x, sq):
    out = {}
    for b, c in x.items():
        k = len(b)
        s = (-1) ** (k * (k - 1) // 2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        out[b] = c * s
    return {b: c for b, c in out.items() if c != 0}


def ladder(sq, planes):
    v = [GA.scal(F(1, 2), GA.add(g(e), g(f))) for (e, f) in planes]
    w = [GA.scal(F(1, 2), GA.sub(g(e), g(f))) for (e, f) in planes]
    n = [m(sq, v[j], w[j]) for j in range(len(planes))]
    return v, w, n


def gamma(sq, planes):
    out = GA.sc(1)
    for (e, f) in planes:
        out = m(sq, out, g(e), g(f))
    return out


def blade(b):
    return {tuple(b): F(1)}


def commutant_blades(gens, sq):
    """Basis blades commuting with every element of gens. Conjugation by a basis blade maps every
    basis blade to plus or minus itself, so the commutant of a set of blades is spanned by blades."""
    n = len(sq)
    return [b for b in GA.all_blades(n) if all(GA.commutes(blade(b), x, sq) for x in gens)]


def blade_conjugation_is_diagonal(sq):
    n = len(sq)
    bl = GA.all_blades(n)
    for e in bl:
        for b in bl:
            p = m(sq, blade(e), blade(b))
            q = m(sq, blade(b), blade(e))
            if not (GA.eq(p, q) or GA.eq(p, GA.neg(q))):
                return False
    return True


# ----------------------------------------------------------------------------- (i)

def check_hyperbolic_tower_has_no_unit():
    premise("tower.volume-elements-planes")
    premise("synthesis.plane-commutant-even-ground")
    premise("std-algebra.orthogonal-anticommute")
    ok = True
    record = []
    for N in (1, 2, 3):
        sq, planes = hyperbolic(N)
        n = len(sq)
        diag = blade_conjugation_is_diagonal(sq)
        bivectors = [m(sq, g(a), g(b)) for a in range(n) for b in range(a + 1, n)]
        com = commutant_blades(bivectors, sq)
        G = gamma(sq, planes)
        full = tuple(range(n))
        sq_ok = GA.eq(m(sq, G, G), GA.sc(1)) and GA.eq(G, blade(full))
        units = True
        for (al, be) in ((0, 1), (1, 1), (3, -2), (F(1, 2), F(-5, 3))):
            z = GA.add(GA.sc(al), GA.scal(be, G))
            want = GA.add(GA.sc(al * al + be * be), GA.scal(2 * al * be, G))
            units = units and GA.eq(m(sq, z, z), want)
        record.append((N, len(com), com == [(), full], diag, sq_ok, units))
    ok = record == [(1, 2, True, True, True, True), (2, 2, True, True, True, True),
                    (3, 2, True, True, True, True)]
    GA.check("(i) Cl(N, N), N = 1, 2, 3: conjugation by basis blades is diagonal on blades; the commutant "
             "of the bivectors is span{1, Gamma} with Gamma the full blade, Gamma^2 = +1, and "
             "(alpha + beta Gamma)^2 = alpha^2 + beta^2 + 2 alpha beta Gamma: no unit", ok)
    return ok


# ----------------------------------------------------------------------------- (ii)

def check_kernel_bivector_commutes_with_transport_and_is_antihermitian():
    premise("tower.structure-tower-c-norms")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom")
    ok = True
    record = []
    for N in (1, 2, 3):
        sq, planes = level(N)
        n = len(sq)
        J = m(sq, g(2), g(3))
        v, w, nn = ladder(sq, planes)
        car = all(GA.eq(acomm(sq, w[j], v[k]), GA.sc(1 if j == k else 0))
                  and GA.is_zero(acomm(sq, v[j], v[k])) and GA.is_zero(acomm(sq, w[j], w[k]))
                  for j in range(N) for k in range(N))
        adj = all(GA.eq(star(v[j], sq), w[j]) for j in range(N))
        plane_gens = [g(i) for (e, f) in planes for i in (e, f)]
        jc = all(GA.commutes(J, x, sq) for x in plane_gens)
        js = GA.eq(m(sq, J, J), GA.sc(-1)) and GA.eq(star(J, sq), GA.neg(J))
        I4 = m(sq, g(0), g(1), g(2), g(3))
        sigma = m(sq, g(0), g(1))
        rel = GA.eq(J, m(sq, I4, sigma)) and GA.eq(m(sq, J, sigma), I4)
        anti = True
        if N <= 2:
            bl = GA.all_blades(n)
            anti = all(GA.eq(star(m(sq, blade(a), blade(b)), sq),
                             m(sq, star(blade(b), sq), star(blade(a), sq))) for a in bl for b in bl)
        record.append((N, car, adj, jc, js, rel, anti))
    ok = record == [(1, True, True, True, True, True, True), (2, True, True, True, True, True, True),
                    (3, True, True, True, True, True, True)]
    GA.check("(ii) N = 1, 2, 3: the ladder obeys the CAR with v* = w; J^2 = -1, J* = -J, J commutes with "
             "every plane generator; J = I_4 sigma; * is an antiautomorphism on all blade pairs (N <= 2)", ok)
    return ok


# ----------------------------------------------------------------------------- (iii)

def check_commutant_of_transport_is_a_quaternion_algebra():
    premise("tower.commuting-copies")
    premise("synthesis.plane-commutant-even-ground")
    premise("std-algebra.orthogonal-anticommute")
    premise("synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom")
    premise("std-algebra.bivector-exponential")
    record = []
    for N in (1, 2, 3):
        sq, planes = level(N)
        P = sorted(i for pl in planes for i in pl)
        plane_gens = [g(i) for i in P]
        com = commutant_blades(plane_gens, sq)
        expect = sorted([(), (2, 3), tuple(sorted(P + [2])), tuple(sorted(P + [3]))])
        G = gamma(sq, planes)
        J = m(sq, g(2), g(3))
        u1, u2 = m(sq, G, g(2)), m(sq, G, g(3))
        quat = (all(GA.eq(m(sq, x, x), GA.sc(-1)) for x in (J, u1, u2))
                and GA.eq(m(sq, u1, u2), J) and GA.eq(m(sq, u2, u1), GA.neg(J))
                and GA.eq(m(sq, J, u1), u2))
        even = [b for b in com if len(b) % 2 == 0]
        # the kernel rotor R = c + s J at a rational point of the circle fixes J, turns u1 by twice the angle
        c, s = F(3, 5), F(4, 5)
        R = GA.add(GA.sc(c), GA.scal(s, J))
        Ri = GA.sub(GA.sc(c), GA.scal(s, J))
        rot = (GA.eq(m(sq, R, Ri), GA.sc(1)) and GA.eq(m(sq, R, J, Ri), J)
               and GA.eq(m(sq, R, u1, Ri), GA.add(GA.scal(c * c - s * s, u1), GA.scal(2 * c * s, u2))))
        record.append((N, len(com), sorted(com) == expect, quat, even == [(), (2, 3)], rot))
    ok = record == [(1, 4, True, True, True, True), (2, 4, True, True, True, True),
                    (3, 4, True, True, True, True)]
    # N = 1 is the stored centraliser of e_0, e_1 in Cl(1,3)
    sq1, _ = level(1)
    stored = sorted(commutant_blades([g(0), g(1)], sq1)) == [(), (0, 1, 2), (0, 1, 3), (2, 3)]
    # contrast: ground Cl(1,3), only the tower plane (4, 5) as transport, N = 2
    sq2, _ = level(2)
    com2 = commutant_blades([g(4), g(5)], sq2)
    even2 = [b for b in com2 if len(b) % 2 == 0]
    neg_units = [b for b in even2 if GA.eq(m(sq2, blade(b), blade(b)), GA.sc(-1))]
    contrast = (len(com2), len(even2), sorted(neg_units)) == (16, 8, [(0, 1, 2, 3), (1, 2), (1, 3), (2, 3)])
    ok = ok and stored and contrast
    GA.check("(iii) N = 1, 2, 3: the commutant of the plane generators is span{1, J, Gamma e_2, Gamma e_3}, "
             "quaternion relations, even part span{1, J}; the kernel rotor fixes J and turns Gamma e_2; N = 1 "
             "is the stored centraliser; with (e_0, e_1) in the ground the even commutant of the tower plane "
             "has 8 blades and the units I_4, e_1e_2, e_1e_3, J", ok)
    return ok


# ----------------------------------------------------------------------------- (iv)

def check_level_pseudoscalar_is_J_on_each_parity_sector():
    premise("tower.volume-elements-planes")
    premise("std-algebra.pseudoscalar-commutation")
    premise("tower.structure-tower-c-norms")
    premise("synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom")
    record = []
    for N in (1, 2, 3):
        sq, planes = level(N)
        n = len(sq)
        J = m(sq, g(2), g(3))
        G = gamma(sq, planes)
        I = m(sq, *[g(i) for i in range(n)])
        v, w, nn = ladder(sq, planes)
        prod = GA.sc(1)
        for j in range(N):
            prod = m(sq, prod, GA.sub(GA.sc(1), GA.scal(2, nn[j])))
        basic = (GA.eq(I, m(sq, J, G)) and GA.eq(m(sq, I, I), GA.sc(-1))
                 and GA.eq(star(I, sq), GA.neg(I)) and GA.eq(star(G, sq), G) and GA.eq(G, prod))
        par = (all(GA.anticommutes(G, x, sq) for x in v + w)
               and all(GA.commutes(G, m(sq, a, b), sq) for a in v + w for b in v + w))
        Pp = GA.scal(F(1, 2), GA.add(GA.sc(1), G))
        Pm = GA.scal(F(1, 2), GA.sub(GA.sc(1), G))
        sect = GA.eq(m(sq, I, Pp), m(sq, J, Pp)) and GA.eq(m(sq, I, Pm), GA.neg(m(sq, J, Pm)))
        Iinv = GA.neg(I)
        grade = all(GA.eq(m(sq, I, g(i), Iinv), GA.neg(g(i))) for i in range(n))
        record.append((N, basic, par, sect, grade))
    ok = record == [(1, True, True, True, True), (2, True, True, True, True), (3, True, True, True, True)]
    GA.check("(iv) N = 1, 2, 3: I_n = J Gamma, I_n^2 = -1, I_n* = -I_n, Gamma* = Gamma = prod(1 - 2 n_j); "
             "Gamma anticommutes with modes, commutes with pairs; I_n = +J on Gamma = +1 and -J on "
             "Gamma = -1; Ad(I_n) negates every generator", ok)
    return ok


# ----------------------------------------------------------------------------- (v)

def hopping(sq, v, w, M):
    S = {}
    for k in range(M):
        S = GA.add(S, m(sq, v[2 * k], w[2 * k + 1]))
    return S


def check_hermitian_pair_with_unit_J():
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    premise("tower.structure-tower-c-norms")
    ok = True
    record = []
    for M in (1, 2):
        N = 2 * M
        sq, planes = level(N)
        J = m(sq, g(2), g(3))
        v, w, nn = ladder(sq, planes)
        S = hopping(sq, v, w, M)
        Sd = star(S, sq)
        phi = GA.add(S, Sd)
        pi = m(sq, J, GA.sub(Sd, S))
        herm = GA.eq(star(phi, sq), phi) and GA.eq(star(pi, sq), pi)
        edge = {}
        for k in range(M):
            edge = GA.add(edge, GA.sub(nn[2 * k], nn[2 * k + 1]))
        lhs = comm(sq, phi, pi)
        exact = GA.eq(comm(sq, S, Sd), edge) and GA.eq(lhs, GA.scal(2, m(sq, J, edge)))
        Ppol = GA.sc(1)
        for k in range(M):
            Ppol = m(sq, Ppol, nn[2 * k], GA.sub(GA.sc(1), nn[2 * k + 1]))
        X = Ppol
        lad = GA.is_zero(m(sq, S, Ppol))
        vals = []
        for j in range(M + 1):
            lad = lad and not GA.is_zero(X) and GA.eq(m(sq, lhs, X), GA.scal(2 * (M - 2 * j), m(sq, J, X)))
            vals.append(2 * (M - 2 * j))
            X = m(sq, Sd, X)
        lad = lad and GA.is_zero(X)
        record.append((M, herm, exact, lad, vals))
    ok = record == [(1, True, True, True, [2, -2]), (2, True, True, True, [4, 0, -4])]
    # the identity [X + X*, J(X* - X)] = 2 J [X, X*] for a generic element of the transport algebra
    sq, planes = level(2)
    J = m(sq, g(2), g(3))
    v, w, nn = ladder(sq, planes)
    X = GA.add(GA.scal(3, v[0]), GA.scal(-2, m(sq, w[0], w[1])), v[1], GA.scal(5, nn[0]),
               GA.scal(F(1, 3), m(sq, g(4), g(0), g(5))))
    Xd = star(X, sq)
    gen_id = GA.eq(comm(sq, GA.add(X, Xd), m(sq, J, GA.sub(Xd, X))), GA.scal(2, m(sq, J, comm(sq, X, Xd))))
    ok = ok and gen_id
    GA.check("(v) M = 1, 2 blocks: phi, pi self-adjoint; [S, S*] = sum (n_2k - n_2k+1) and [phi, pi] = "
             "2 J sum (n_2k - n_2k+1) exactly; on (S*)^j P_pol, j = 0..M, it acts as 2 (M - 2j) J, "
             "(S*)^(M+1) P_pol = 0; the identity [X + X*, J(X* - X)] = 2 J [X, X*] on a generic X", ok)
    return ok


def check_density_modes_with_unit_J():
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    premise("tower.structure-tower-c-norms")
    Mw = 4
    sq, planes = level(Mw)
    J = m(sq, g(2), g(3))
    v, w, nn = ladder(sq, planes)

    def rho(q):
        out = {}
        for k in range(Mw - q):
            out = GA.add(out, m(sq, v[k], w[k + q]))
        return out

    record = []
    fields = {}
    for q in (1, 2):
        r = rho(q)
        rd = star(r, sq)
        phi = GA.add(r, rd)
        pi = m(sq, J, GA.sub(rd, r))
        fields[q] = (r, rd, phi, pi)
        edge = {}
        for k in range(q):
            edge = GA.add(edge, nn[k])
        for k in range(Mw - q, Mw):
            edge = GA.sub(edge, nn[k])
        lhs = comm(sq, phi, pi)
        E = GA.sc(1)
        for k in range(q):
            E = m(sq, E, nn[k])
        for k in range(Mw - q, Mw):
            E = m(sq, E, GA.sub(GA.sc(1), nn[k]))
        record.append((q, GA.eq(lhs, GA.scal(2, m(sq, J, edge))),
                       GA.eq(m(sq, lhs, E), GA.scal(2 * q, m(sq, J, E))) and not GA.is_zero(E)))
    ok = record == [(1, True, True), (2, True, True)]
    r1, r1d, phi1, pi1 = fields[1]
    r2, r2d, phi2, pi2 = fields[2]
    c12 = comm(sq, r1, r2d)
    c21 = comm(sq, r2, r1d)
    mixed = (GA.is_zero(comm(sq, r1, r2))
             and GA.eq(comm(sq, phi1, pi2), m(sq, J, GA.add(c12, c21)))
             and GA.eq(comm(sq, phi1, phi2), GA.sub(c12, c21))
             and GA.eq(comm(sq, pi1, pi2), GA.sub(c12, c21)))
    ok = ok and mixed
    GA.check("(v) window of four modes, q = 1, 2: [phi_q, pi_q] = 2 J (sum_{k<q} n_k - sum_{k>=4-q} n_k), "
             "= 2 q J on the edge-clean projector; [rho_1, rho_2] = 0; [phi_1, pi_2] = J([rho_1, rho_2*] + "
             "[rho_2, rho_1*]) and [phi_1, phi_2] = [pi_1, pi_2] = [rho_1, rho_2*] - [rho_2, rho_1*]", ok)
    return ok


# ----------------------------------------------------------------------------- (vi)

def check_sign_of_J_and_the_phase_circle():
    premise("synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom")
    premise("std-algebra.bivector-exponential")
    premise("tower.structure-tower-c-norms")
    M = 2
    N = 2 * M
    sq, planes = level(N)
    n = len(sq)
    J = m(sq, g(2), g(3))
    I4 = m(sq, g(0), g(1), g(2), g(3))
    In = m(sq, *[g(i) for i in range(n)])
    sigma = m(sq, g(0), g(1))
    v, w, nn = ladder(sq, planes)

    def alpha(x):
        return {b: (-c if 3 in b else c) for b, c in x.items()}

    bl = GA.all_blades(n)
    sample = [b for b in bl if len(b) <= 3]
    hom = all(GA.eq(alpha(m(sq, blade(a), blade(b))), m(sq, alpha(blade(a)), alpha(blade(b))))
              for a in sample for b in sample)
    starc = all(GA.eq(alpha(star(blade(a), sq)), star(alpha(blade(a)), sq)) for a in bl)
    fixes = all(GA.eq(alpha(g(i)), g(i)) for (e, f) in planes for i in (e, f))
    S = hopping(sq, v, w, M)
    Sd = star(S, sq)
    phi = GA.add(S, Sd)
    pi = m(sq, J, GA.sub(Sd, S))
    flips = (GA.eq(alpha(J), GA.neg(J)) and GA.eq(alpha(I4), GA.neg(I4)) and GA.eq(alpha(In), GA.neg(In))
             and GA.eq(alpha(sigma), sigma) and GA.eq(alpha(phi), phi) and GA.eq(alpha(pi), GA.neg(pi)))
    # phase circle: U = prod_k (1 - n_2k + n_2k (c + sJ)) (1 - n_2k+1 + n_2k+1 (c - sJ)) = e^{theta J Q / 2}
    c, s = F(5, 13), F(12, 13)
    up = GA.add(GA.sc(c), GA.scal(s, J))
    dn = GA.sub(GA.sc(c), GA.scal(s, J))
    U = GA.sc(1)
    for k in range(M):
        a, b = nn[2 * k], nn[2 * k + 1]
        U = m(sq, U, GA.add(GA.sub(GA.sc(1), a), m(sq, a, up)), GA.add(GA.sub(GA.sc(1), b), m(sq, b, dn)))
    Ud = star(U, sq)
    C, Sn = c * c - s * s, 2 * c * s
    eJ = GA.add(GA.sc(C), GA.scal(Sn, J))
    unit = GA.eq(m(sq, U, Ud), GA.sc(1))
    phase = GA.eq(m(sq, U, S, Ud), m(sq, eJ, S))
    phi2 = m(sq, U, phi, Ud)
    pi2 = m(sq, U, pi, Ud)
    turn = (GA.eq(phi2, GA.sub(GA.scal(C, phi), GA.scal(Sn, pi)))
            and GA.eq(pi2, GA.add(GA.scal(Sn, phi), GA.scal(C, pi)))
            and GA.eq(comm(sq, phi2, pi2), comm(sq, phi, pi)))
    # e^{theta J} is central on transport: conjugation by it fixes every plane generator; e^{pi J} = -1
    trivial = all(GA.eq(m(sq, eJ, g(i), GA.sub(GA.sc(C), GA.scal(Sn, J))), g(i))
                  for (e, f) in planes for i in (e, f))
    half = GA.eq(m(sq, J, J), GA.sc(-1))
    ok = hom and starc and fixes and flips and unit and phase and turn and trivial and half
    GA.check("(vi) e_3 -> -e_3 is a *-automorphism fixing every plane generator and sigma, negating J, I_4, "
             "I_n and pi, fixing phi; U = e^{theta J Q/2} at (c, s) = (5/13, 12/13) is unitary, multiplies S "
             "by e^{theta J}, turns (phi, pi) by theta and keeps [phi, pi]; Ad(e^{theta J}) fixes transport", ok)
    return ok


if __name__ == "__main__":
    for f in (check_hyperbolic_tower_has_no_unit,
              check_kernel_bivector_commutes_with_transport_and_is_antihermitian,
              check_commutant_of_transport_is_a_quaternion_algebra,
              check_level_pseudoscalar_is_J_on_each_parity_sector,
              check_hermitian_pair_with_unit_J,
              check_density_modes_with_unit_J,
              check_sign_of_J_and_the_phase_circle):
        f()
    print("FAILURES:", GA.FAILURES)
