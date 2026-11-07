"""synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom: exact checks in Cl(1,3).

Cl(1,3), e_0^2 = +1, e_k^2 = -1, I_4 = e_0 e_1 e_2 e_3. The completed pair in the radial plane:
v = (e_0 + e_1)/2, v* = (e_0 - e_1)/2, sigma = v* v - v v* = e_0 e_1, K = sigma/2, P_+ = v* v,
P_- = v v*. J = e_2 e_3. Frame *-structure x* = e_0 rev(x) e_0.

(i)   J^2 = -1, J commutes with e_0, e_1, v, v*, sigma; J sigma = sigma J = +I_4, J = I_4 sigma; J* = -J;
      the centraliser of e_0, e_1 is span{1, J, e_0e_1e_2, e_0e_1e_3} (dimension 4, even part span{1, J}),
      sigma e_2 squares to -1, commutes with the atom and anticommutes with J;
(ii)  A = Cl(1,1) + Cl(1,1) J has real dimension 8, is closed under products, has centre span{1, J}, and
      is spanned over span{1, J} by 1, v, v*, v* v; * is an antiautomorphism with v -> v*, sigma* = sigma;
(iii) I_4 anticommutes with e_0, e_1, v, v*; (I_4 a)(I_4 b) = +ab, (J a)(J b) = -ab; I_4 P_+- = +-J P_+-;
(iv)  [J K, v] = -J v, [J K, v*] = +J v*, J K = I_4/2, (2JK)^2 = -1; at rational points of the circle
      (Cayley form) U = c + s (2JK) is unitary, U U' is the rotor at the summed angle, and
      U v U^-1 = (C - S J) v, U v* U^-1 = (C + S J) v* with C = c^2 - s^2, S = 2cs (cos t, sin t);
      the rotor flow exp(lambda K) at rational e^(lambda/2) gives e^-lambda v, and t = -J lambda turns
      -J t into -lambda; at z = t + J theta, tau_z(v) = e^theta e^{-Jt} v and tau_z(v*) = e^-theta e^{Jt} v*;
(v)   with T(x) = 2<x>_0 - 2J<Jx>_0 and rho = P_+ + q P_- (q = e^beta rational), omega(x) = T(rho x)/T(rho)
      is KMS for tau_{J beta} = Ad(rho): omega(x rho y rho^-1) = omega(y x) on a basis, not for Ad(rho^-1);
      omega(v* v) = 1/(1 + q); omega(x* x) real and positive; the KMS densities form the J-line of rho;
      Ad(P_+ + w P_-) v = w v for w = C + S J (the modular flow Ad(rho^{Jt}) = tau_{-beta t} on v).
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = GA.sig(1, 3)


def g(i):
    return GA.gen(i)


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def scalar(x):
    return x.get((), F(0))


def star(x):
    return m(g(0), GA.reverse(x), g(0))


def comm(a, b):
    return GA.sub(m(a, b), m(b, a))


def build():
    v = GA.scal(F(1, 2), GA.add(g(0), g(1)))
    vs = GA.scal(F(1, 2), GA.sub(g(0), g(1)))
    sigma = GA.sub(m(vs, v), m(v, vs))
    J = m(g(2), g(3))
    I4 = m(g(0), g(1), g(2), g(3))
    return v, vs, sigma, J, I4


def atom_basis(J):
    """Real basis of A = Cl(1,1) + Cl(1,1) J."""
    cl11 = [GA.sc(1), g(0), g(1), m(g(0), g(1))]
    return cl11 + [m(x, J) for x in cl11]


def coords(xs):
    bl = GA.all_blades(4)
    return [[x.get(b, F(0)) for b in bl] for x in xs]


def trace(x, J):
    return GA.sub(GA.sc(2 * scalar(x)), GA.scal(2 * scalar(m(J, x)), J))


def check_transverse_plane_is_a_central_unit_of_the_atom():
    premise("singularity.modular-structure-completed-pair")
    premise("singularity.pseudo-inverse-identities-hyperbolic-atom")
    premise("primer.centre")
    v, vs, sigma, J, I4 = build()
    ok = m(v, v) == {} and m(vs, vs) == {} and GA.add(m(v, vs), m(vs, v)) == GA.sc(1)
    ok &= sigma == m(g(0), g(1))
    ok &= m(J, J) == GA.sc(-1)
    ok &= all(GA.commutes(J, x, SQ) for x in (g(0), g(1), v, vs, sigma))
    ok &= m(J, sigma) == I4 and m(sigma, J) == I4 and J == m(I4, sigma)
    # the algebra A over span{1, J}
    A = atom_basis(J)
    ok &= GA.rank_of_vectors(coords(A)) == 8
    span8 = coords(A)
    closed = all(GA.rank_of_vectors(span8 + coords([m(x, y)])) == 8 for x in A for y in A)
    ok &= closed
    # centre of A: c = sum a_k A_k commuting with e_0, e_1, J; solve the real linear system
    rows = []
    for gen_ in (g(0), g(1), J):
        cols = [comm(x, gen_) for x in A]
        for b in GA.all_blades(4):
            rows.append([c.get(b, F(0)) for c in cols])
    ok &= 8 - GA.mat_rank(GA.frac_matrix(rows)) == 2
    # spanned over span{1, J} by 1, v, v*, v* v
    gens = [GA.sc(1), v, vs, m(vs, v)]
    ok &= GA.rank_of_vectors(coords(gens + [m(J, x) for x in gens])) == 8
    # the centraliser of e_0, e_1 in Cl(1,3): dimension 4, spanned by 1, J, e_0e_1e_2, e_0e_1e_3
    bl = GA.all_blades(4)
    rows = []
    for gen_ in (g(0), g(1)):
        cols = [comm({b: F(1)}, gen_) for b in bl]
        for c in bl:
            rows.append([x.get(c, F(0)) for x in cols])
    ok &= 16 - GA.mat_rank(GA.frac_matrix(rows)) == 4
    cen = [b for b in bl if comm({b: F(1)}, g(0)) == {} and comm({b: F(1)}, g(1)) == {}]
    ok &= cen == [(), (2, 3), (0, 1, 2), (0, 1, 3)]
    ok &= [b for b in cen if len(b) % 2 == 0] == [(), (2, 3)]
    u = m(sigma, g(2))
    ok &= m(u, u) == GA.sc(-1) and GA.anticommutes(u, J, SQ)
    ok &= all(GA.commutes(u, x, SQ) for x in (v, vs, sigma))
    ok &= m(u, m(sigma, g(3))) == J
    GA.check("(i)-(ii) J = e_2 e_3: J^2 = -1, commutes with e_0, e_1, v, v*, sigma; J sigma = +I_4; the "
             "centraliser is the quaternions span{1, J, e_0e_1e_2, e_0e_1e_3} with even part span{1, J}; "
             "A = Cl(1,1) + Cl(1,1) J is an algebra of dimension 8 with centre span{1, J}, spanned over it "
             "by 1, v, v*, v* v", ok)
    return ok


def check_frame_star_is_conjugate_linear_in_the_unit():
    premise("tower.structure-tower-c-norms")
    v, vs, sigma, J, I4 = build()
    ok = star(g(0)) == g(0)
    ok &= all(star(g(k)) == GA.neg(g(k)) for k in (1, 2, 3))
    bl = GA.all_blades(4)
    ok &= all(star(m({a: F(1)}, {b: F(1)})) == m(star({b: F(1)}), star({a: F(1)})) for a in bl for b in bl)
    ok &= star(v) == vs and star(vs) == v
    ok &= star(J) == GA.neg(J)
    ok &= star(sigma) == sigma
    K = GA.scal(F(1, 2), sigma)
    ok &= star(m(J, K)) == GA.neg(m(J, K))
    ok &= star(I4) == GA.neg(I4)
    GA.check("(ii) the frame * (e_0 -> e_0, e_k -> -e_k, antiautomorphism) sends v to v*, fixes sigma and "
             "K, and sends J to -J and JK to -JK: conjugate-linear over span{1, J}", ok)
    return ok


def check_left_i4_is_not_a_scalar_of_the_atom():
    premise("singularity.modular-structure-completed-pair")
    v, vs, sigma, J, I4 = build()
    ok = all(GA.anticommutes(I4, x, SQ) for x in (g(0), g(1), v, vs))
    vecs = [g(0), g(1), v, vs, GA.add(GA.scal(3, g(0)), GA.scal(-2, g(1)))]
    for a in vecs:
        for b in vecs:
            ok &= m(m(I4, a), m(I4, b)) == m(a, b)
            ok &= m(m(J, a), m(J, b)) == GA.neg(m(a, b))
    pp, pm = m(vs, v), m(v, vs)
    ok &= pp == GA.scal(F(1, 2), GA.add(GA.sc(1), sigma))
    ok &= m(I4, pp) == m(J, pp) and m(I4, pm) == GA.neg(m(J, pm))
    GA.check("(iii) I_4 anticommutes with e_0, e_1, v, v*: (I_4 a)(I_4 b) = +ab while (J a)(J b) = -ab; "
             "I_4 P_+ = J P_+ and I_4 P_- = -J P_-", ok)
    return ok


def check_phase_flow_with_unit_J():
    premise("singularity.modular-structure-completed-pair")
    premise("std-algebra.bivector-exponential")
    v, vs, sigma, J, I4 = build()
    K = GA.scal(F(1, 2), sigma)
    JK = m(J, K)
    ok = comm(JK, v) == GA.neg(m(J, v)) and comm(JK, vs) == m(J, vs)
    ok &= JK == GA.scal(F(1, 2), I4)
    A2 = GA.scal(2, JK)
    ok &= m(A2, A2) == GA.sc(-1)

    def rot(u):
        u = F(u)
        c, s = (1 - u * u) / (1 + u * u), 2 * u / (1 + u * u)
        return c, s, GA.add(GA.sc(c), GA.scal(s, A2))

    for u in (F(1, 2), F(2, 3), F(-3)):
        c, s, U = rot(u)
        Ui = GA.sub(GA.sc(c), GA.scal(s, A2))
        ok &= m(U, Ui) == GA.sc(1) and star(U) == Ui
        C, S = c * c - s * s, 2 * c * s
        ok &= m(U, v, Ui) == m(GA.sub(GA.sc(C), GA.scal(S, J)), v)
        ok &= m(U, vs, Ui) == m(GA.add(GA.sc(C), GA.scal(S, J)), vs)
        ok &= m(U, v, Ui) != m(GA.add(GA.sc(C), GA.scal(S, J)), v)
        c2, s2, U2 = rot(F(1, 5))
        ok &= m(U, U2) == GA.add(GA.sc(c * c2 - s * s2), GA.scal(s * c2 + c * s2, A2))
    # the rotor flow exp(lambda K) = cosh(lambda/2) + sigma sinh(lambda/2) at a = e^(lambda/2) rational
    for a in (F(2), F(3, 5)):
        ch, sh = (a + 1 / a) / 2, (a - 1 / a) / 2
        R = GA.add(GA.sc(ch), GA.scal(sh, sigma))
        Ri = GA.sub(GA.sc(ch), GA.scal(sh, sigma))
        ok &= m(R, Ri) == GA.sc(1)
        ok &= m(R, v, Ri) == GA.scal(1 / (a * a), v) and m(R, vs, Ri) == GA.scal(a * a, vs)
    # continuation: at t = -J lambda the exponent -J t is -lambda, and J t K is lambda K
    # a mixed parameter z = t + J theta: e^{JzK} = e^{JtK} e^{-theta K}
    c, s, U = rot(F(1, 3))
    Ui = GA.sub(GA.sc(c), GA.scal(s, A2))
    C, S = c * c - s * s, 2 * c * s
    a = F(5, 2)
    ch, sh = (a + 1 / a) / 2, (a - 1 / a) / 2
    E = GA.sub(GA.sc(ch), GA.scal(sh, sigma))
    Ei = GA.add(GA.sc(ch), GA.scal(sh, sigma))
    Z, Zi = m(U, E), m(Ei, Ui)
    ok &= m(Z, Zi) == GA.sc(1)
    ok &= m(Z, v, Zi) == GA.scal(a * a, m(GA.sub(GA.sc(C), GA.scal(S, J)), v))
    ok &= m(Z, vs, Zi) == GA.scal(1 / (a * a), m(GA.add(GA.sc(C), GA.scal(S, J)), vs))
    lam = F(7, 4)
    t = GA.scal(-lam, J)
    ok &= GA.neg(m(J, t)) == GA.sc(-lam)
    ok &= m(J, t, K) == GA.scal(lam, K)
    GA.check("(iv)-(v) [JK, v] = -Jv, [JK, v*] = +Jv*, JK = I_4/2; Ad(e^{JtK}) v = e^{-Jt} v and v* -> "
             "e^{+Jt} v* at rational points, unitary, a group; e^{lambda K} v = e^{-lambda} v is the flow at "
             "t = -J lambda", ok)
    return ok


def check_gibbs_state_is_kms_for_the_J_flow():
    premise("singularity.kms-uniqueness-factor")
    premise("singularity.modular-structure-completed-pair")
    v, vs, sigma, J, I4 = build()
    A = atom_basis(J)
    pp, pm = m(vs, v), m(v, vs)
    ok = trace(GA.sc(1), J) == GA.sc(2) and trace(J, J) == GA.scal(2, J)
    ok &= all(trace(m(x, y), J) == trace(m(y, x), J) for x in A for y in A)
    for q in (F(3), F(2, 7)):
        rho = GA.add(pp, GA.scal(q, pm))
        rhoi = GA.add(pp, GA.scal(1 / q, pm))
        ok &= m(rho, rhoi) == GA.sc(1)
        Z = scalar(trace(rho, J))

        def omega(x):
            return GA.scal(1 / Z, trace(m(rho, x), J))

        ok &= omega(pp) == GA.sc(1 / (1 + q))
        kms = all(omega(m(x, rho, w, rhoi)) == omega(m(w, x)) for x in A for w in A)
        anti = all(omega(m(x, rhoi, w, rho)) == omega(m(w, x)) for x in A for w in A)
        ok &= kms and not anti
        samples = A + [GA.add(v, GA.scal(2, m(J, vs))), GA.add(GA.sc(1), GA.scal(-3, v), m(J, sigma))]
        for x in samples:
            val = omega(m(star(x), x))
            ok &= set(val) <= {()} and scalar(val) > 0
        # uniqueness: densities r in A with T(r x Ad(rho) w) = T(r w x) for all x, w form the J-line of rho
        rows = []
        for x in A:
            for w in A:
                lhs = [GA.sub(trace(m(r, x, rho, w, rhoi), J), trace(m(r, w, x), J)) for r in A]
                for b in ((), (2, 3)):
                    rows.append([c.get(b, F(0)) for c in lhs])
        ok &= 8 - GA.mat_rank(GA.frac_matrix(rows)) == 2
        # modular flow on v: Ad(P_+ + w P_-) v = w v, w = cos(beta t) + J sin(beta t) at a rational point
        u = F(1, 3)
        C, S = (1 - u * u) / (1 + u * u), 2 * u / (1 + u * u)
        w_ = GA.add(GA.sc(C), GA.scal(S, J))
        wb = GA.sub(GA.sc(C), GA.scal(S, J))
        Rm = GA.add(pp, m(w_, pm))
        Rmi = GA.add(pp, m(wb, pm))
        ok &= m(Rm, Rmi) == GA.sc(1)
        ok &= m(Rm, v, Rmi) == m(w_, v) and m(Rm, vs, Rmi) == m(wb, vs)
    GA.check("(vi) T is a span{1, J}-valued trace; the Gibbs state of K is a state, KMS for tau_{J beta} = "
             "Ad(e^{-beta K}) and not for Ad(e^{beta K}), with omega(v* v) = 1/(1 + e^beta), the only KMS "
             "density up to the field; Ad(rho^{Jt}) acts on v as e^{+J beta t} = tau_{-beta t}", ok)
    return ok
