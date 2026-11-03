"""synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law: exact checks.

Rotors of the weak factor: U = u0 + u1 B1 + u2 B2 + u3 B3 in the even subalgebra of Cl(3,0), B1 = g2g3,
B2 = g3g1, B3 = g1g2, multiplied by a four-component product that is first checked against GA.mul on every
pair of basis elements (as in synthesis.weak-factor-rotor-lattice-strong-coupling-area-law).
(a) Continuum: the stereographic rotor map q(x) = ((1 - r^2) + 2 x.B)/(1 + r^2) of R^3 onto the unit rotors;
    polynomials in x1, x2, x3 with Fraction coefficients; the round metric is Omega^2 delta, Omega = 2/(1 + r^2).
(b) Lattice: a 4 x 2 periodic square lattice, gauge functional F_U(g) = sum_links <g_x U_l g~_y>_0; the
    Faddeev-Popov form is minus the second variation along g_x = exp(eps w_x), w_x bivectors.
(c) Signed count: two sites, two links, g at one site fixed (global gauge).
(d) Strong coupling with a frozen fundamental doublet: Haar averages by the 24 Hurwitz units, checked against the
    exact Haar moments; the Haar moment formula of the stored rotor-lattice result.
Exact Fractions throughout.
"""
from fractions import Fraction as F
from itertools import product

import GA
from GA import mul, sc, gen, add, scal
from tp_premise import premise

S3 = (1, 1, 1)
BASIS = [sc(1), mul(gen(1), gen(2), S3), mul(gen(2), gen(0), S3), mul(gen(0), gen(1), S3)]


def to_ga(q):
    return add(*[scal(q[i], BASIS[i]) for i in range(4)])


def qmul(p, q):
    a0, a1, a2, a3 = p
    b0, b1, b2, b3 = q
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 - a2 * b3 + a3 * b2,
            a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1,
            a0 * b3 - a1 * b2 + a2 * b1 + a3 * b0)


def rev(q):
    return (q[0], -q[1], -q[2], -q[3])


def qadd(*qs):
    return tuple(sum(x) for x in zip(*qs))


def qsc(c, q):
    return tuple(c * x for x in q)


def product_matches_ga():
    for i in range(4):
        for j in range(4):
            ui = tuple(F(1) if k == i else F(0) for k in range(4))
            uj = tuple(F(1) if k == j else F(0) for k in range(4))
            if not GA.eq(to_ga(qmul(ui, uj)), mul(to_ga(ui), to_ga(uj), S3)):
                return False
    return True


ONE = (F(1), F(0), F(0), F(0))
B3 = (F(0), F(0), F(0), F(1))

# ------------------------------------------------------------------ (a) polynomials for the continuum copy


def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}


def pmul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            out[k] = out.get(k, 0) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def psc(c, p):
    return {k: c * v for k, v in p.items() if c * v != 0}


def pder(p, i):
    out = {}
    for k, v in p.items():
        if k[i] > 0:
            kk = list(k)
            kk[i] -= 1
            out[tuple(kk)] = out.get(tuple(kk), 0) + v * k[i]
    return {k: v for k, v in out.items() if v != 0}


def var(i):
    k = [0, 0, 0]
    k[i] = 1
    return {tuple(k): F(1)}


PONE = {(0, 0, 0): F(1)}


def pq_mul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (padd(pmul(a0, b0), psc(-1, pmul(a1, b1)), psc(-1, pmul(a2, b2)), psc(-1, pmul(a3, b3))),
            padd(pmul(a0, b1), pmul(a1, b0), psc(-1, pmul(a2, b3)), pmul(a3, b2)),
            padd(pmul(a0, b2), pmul(a1, b3), pmul(a2, b0), psc(-1, pmul(a3, b1))),
            padd(pmul(a0, b3), psc(-1, pmul(a1, b2)), pmul(a2, b1), pmul(a3, b0)))


def pq_rev(a):
    return (a[0], psc(-1, a[1]), psc(-1, a[2]), psc(-1, a[3]))


def pq_add(*qs):
    return tuple(padd(*[q[i] for q in qs]) for i in range(4))


def pq_scal(p, q):
    return tuple(pmul(p, x) for x in q)


def pq_der(q, i):
    return tuple(pder(x, i) for x in q)


R2 = padd(pmul(var(0), var(0)), pmul(var(1), var(1)), pmul(var(2), var(2)))
DEN = padd(PONE, R2)


def stereo_numerator(two):
    return (padd(PONE, psc(-1, R2)), psc(two, var(0)), psc(two, var(1)), psc(two, var(2)))


def divergence_numerator(P, weight):
    """sum_i d_i (Omega^w A_i) times DEN^(3 + w) up to a constant, A_i = q~ d_i q, q = P / DEN.
    q~ d_i q = P~ (d_i P DEN - P d_i DEN) / DEN^3; with Omega^w = (2/DEN)^w the numerator over DEN^(3 + w) is
    N_i = P~ (d_i P DEN - P d_i DEN), and d_i(N_i / DEN^(3+w)) DEN^(4+w) = d_i N_i DEN - (3 + w) N_i d_i DEN."""
    tot = ({}, {}, {}, {})
    for i in range(3):
        inner = pq_add(pq_scal(DEN, pq_der(P, i)), pq_scal(psc(-1, pder(DEN, i)), P))
        N = pq_mul(pq_rev(P), inner)
        tot = pq_add(tot, pq_scal(DEN, pq_der(N, i)), pq_scal(psc(-(3 + weight), pder(DEN, i)), N))
    return tot


def check_identity_rotor_map_is_a_coulomb_copy_of_zero_on_the_three_sphere():
    premise("synthesis.weak-factor-rotor-lattice-strong-coupling-area-law")
    P = stereo_numerator(2)
    unit = pq_mul(P, pq_rev(P))
    ok = product_matches_ga()
    ok = ok and unit[0] == pmul(DEN, DEN) and all(not x for x in unit[1:])           # q q~ = 1
    round_div = divergence_numerator(P, 1)                                           # sqrt(g) g^ij = Omega delta
    flat_div = divergence_numerator(P, 0)
    ok = ok and all(not x for x in round_div)                                         # Coulomb on the round S^3
    ok = ok and any(x for x in flat_div)                                              # not the flat condition
    # A is not zero: A_1 at the origin is 2 B1
    inner = pq_add(pq_scal(DEN, pq_der(P, 0)), pq_scal(psc(-1, pder(DEN, 0)), P))
    N1 = pq_mul(pq_rev(P), inner)
    ok = ok and [x.get((0, 0, 0), 0) for x in N1] == [0, 2, 0, 0]
    GA.check("identity rotor map: q~dq is divergence-free for the round metric, not for the flat one", ok)
    return ok


# ------------------------------------------------------------------ (b) lattice Landau gauge: a copy outside the Gribov region
LX, LY = 4, 2
SITES = [(x, y) for x in range(LX) for y in range(LY)]


def nb(s, mu, step=1):
    x, y = s
    return ((x + step) % LX, y) if mu == 0 else (x, (y + step) % LY)


def gauge(U, gfun):
    return {(s, mu): qmul(qmul(gfun[s], U[(s, mu)]), rev(gfun[nb(s, mu)])) for s in SITES for mu in (0, 1)}


def landau_residual_zero(U):
    for s in SITES:
        tot = (0, 0, 0, 0)
        for mu in (0, 1):
            a, b = U[(s, mu)], U[(nb(s, mu, -1), mu)]
            tot = qadd(tot, (0, a[1] - b[1], a[2] - b[2], a[3] - b[3]))
        if tot != (0, 0, 0, 0):
            return False
    return True


def second_variation(U, om):
    tot = F(0)
    for s in SITES:
        for mu in (0, 1):
            wx, wy, u = om[s], om[nb(s, mu)], U[(s, mu)]
            t = qadd(qsc(F(1, 2), qmul(qmul(wx, wx), u)), qsc(F(1, 2), qmul(u, qmul(wy, wy))),
                     qsc(-1, qmul(qmul(wx, u), wy)))
            tot += t[0]
    return tot


def fp_form(U):
    idx = [(s, k) for s in SITES for k in (1, 2, 3)]
    n = len(idx)

    def omega(v):
        om = {s: (F(0), F(0), F(0), F(0)) for s in SITES}
        for (s, k), c in zip(idx, v):
            if c:
                q = list(om[s])
                q[k] += c
                om[s] = tuple(q)
        return om

    def unitv(*ks):
        v = [0] * n
        for k in ks:
            v[k] = 1
        return v
    diag = [second_variation(U, omega(unitv(i))) for i in range(n)]
    M = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = -2 * diag[i]
        for j in range(i + 1, n):
            c = second_variation(U, omega(unitv(i, j)))
            M[i][j] = M[j][i] = -(c - diag[i] - diag[j])
    return M


def check_lattice_landau_gauge_has_a_copy_of_the_trivial_field_outside_the_gribov_region():
    premise("synthesis.weak-factor-rotor-lattice-strong-coupling-area-law")
    U1 = {(s, mu): ONE for s in SITES for mu in (0, 1)}
    powers = [ONE]
    for _ in range(LX - 1):
        powers.append(qmul(powers[-1], B3))
    ok = qmul(powers[-1], B3) == ONE                                                    # B3^4 = 1: periodic
    gfun = {s: powers[s[0]] for s in SITES}
    Uc = gauge(U1, gfun)
    ok = ok and all(Uc[(s, 0)] == (0, 0, 0, -1) and Uc[(s, 1)] == ONE for s in SITES)   # x links -B3, y links 1
    ok = ok and landau_residual_zero(U1) and landau_residual_zero(Uc)
    ok = ok and sum(u[0] for u in U1.values()) == 16 and sum(u[0] for u in Uc.values()) == 8
    sig_trivial = GA.congruence_signature(fp_form(U1))
    sig_copy = GA.congruence_signature(fp_form(Uc))
    ok = ok and sig_trivial == (21, 0, 3)                                               # positive up to global gauge
    ok = ok and sig_copy == (14, 2, 8)                                                  # two negative modes
    GA.check("lattice Landau gauge: -B3 links are a copy of the trivial field with an indefinite FP form", ok)
    return ok


# ------------------------------------------------------------------ (c) the signed count of copies is zero
def check_signed_faddeev_popov_count_is_the_euler_characteristic_zero():
    premise("synthesis.weak-factor-rotor-lattice-strong-coupling-area-law")
    U1 = ONE
    U2 = (F(7, 25), F(0), F(0), F(24, 25))
    ok = qmul(U2, rev(U2)) == ONE
    M = qadd(rev(U1), U2)                     # F(g) = <U1 g~>_0 + <g U2>_0 = <g M>_0 with g at the second site
    norm2 = qmul(M, rev(M))[0]
    ok = ok and norm2 == F(64, 25)
    nrm = F(8, 5)
    crit = [qsc(1 / nrm, rev(M)), qsc(-1 / nrm, rev(M))]
    signs = []
    for gst in crit:
        ok = ok and qmul(gst, rev(gst)) == ONE and qmul(gst, M)[1:] == (0, 0, 0)      # stationary: g M scalar
        H = [[F(0)] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                wa = tuple(F(1) if k == a + 1 else F(0) for k in range(4))
                wb = tuple(F(1) if k == b + 1 else F(0) for k in range(4))
                # second variation of <g* exp(w) M>_0: <g* (w_a w_b + w_b w_a)/2 M>_0
                sym = qsc(F(1, 2), qadd(qmul(wa, wb), qmul(wb, wa)))
                H[a][b] = qmul(qmul(gst, sym), M)[0]
        fp = [[-x for x in r] for r in H]
        p, n, z = GA.congruence_signature(fp)
        ok = ok and z == 0
        signs.append((-1) ** n)
    ok = ok and signs == [1, -1] and sum(signs) == 0
    # the stationary points are only these two: <g w M>_0 = 0 for all bivectors w forces g M scalar
    GA.check("two-site lattice: exactly two copies, FP determinant signs +1 and -1, sum zero", ok)
    return ok


# ------------------------------------------------------------------ (d) fundamental doublet: perimeter law at beta = 0
Q8 = [tuple(F(s) if j == i else F(0) for j in range(4)) for i in range(4) for s in (1, -1)]
HURWITZ = Q8 + [tuple(F(x, 2) for x in signs) for signs in product((1, -1), repeat=4)]


def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r


def haar_moment(alpha):
    if any(a % 2 for a in alpha):
        return F(0)
    num = 1
    for a in alpha:
        num *= dfact(a - 1)
    den = 1
    for j in range(sum(alpha) // 2):
        den *= 4 + 2 * j
    return F(num, den)


def hurwitz_mean(f):
    return sum((f(u) for u in HURWITZ), F(0)) / len(HURWITZ)


# polynomials in the components of R rotors: exponent tuples of length 4 R, integrated by the Haar moments
NR = 4


def rpvar(r, k):
    e = [0] * (4 * NR)
    e[4 * r + k] = 1
    return {tuple(e): F(1)}


def rpmul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2)) if k1 and k2 else (k1 or k2)
            out[k] = out.get(k, 0) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def rpadd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}


def rq(r):
    return tuple(rpvar(r, k) for k in range(4))


def rqmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    neg = lambda p: {k: -v for k, v in p.items()}
    return (rpadd(rpmul(a0, b0), neg(rpmul(a1, b1)), neg(rpmul(a2, b2)), neg(rpmul(a3, b3))),
            rpadd(rpmul(a0, b1), rpmul(a1, b0), neg(rpmul(a2, b3)), rpmul(a3, b2)),
            rpadd(rpmul(a0, b2), rpmul(a1, b3), rpmul(a2, b0), neg(rpmul(a3, b1))),
            rpadd(rpmul(a0, b3), neg(rpmul(a1, b2)), rpmul(a2, b1), rpmul(a3, b0)))


def rqrev(a):
    return (a[0],) + tuple({k: -v for k, v in x.items()} for x in a[1:])


def haar_poly(p):
    tot = F(0)
    for k, v in p.items():
        if not k:
            tot += v
            continue
        m = F(1)
        for r in range(NR):
            m *= haar_moment(k[4 * r:4 * r + 4])
            if m == 0:
                break
        tot += v * m
    return tot


def hop_poly(rx, ru, ry):
    """<phi_x~ U phi_y>_0 with phi_x, U, phi_y the rotors numbered rx, ru, ry."""
    return rqmul(rqmul(rqrev(rq(rx)), rq(ru)), rq(ry))[0]


def two_link_loop_coefficients():
    """Sites 0, 1 (rotors 0, 1), link 0 -> 1 (rotor 2), link 1 -> 0 (rotor 3), beta = 0, no gauge fixing.
    Returns the coefficients of kappa^0..kappa^4 of <<U_C>_0> = N(kappa)/D(kappa)."""
    wl = rqmul(rq(2), rq(3))[0]
    hsum = rpadd(hop_poly(0, 2, 1), hop_poly(1, 3, 0))
    pw = [{(): F(1)}]
    for _ in range(4):
        pw.append(rpmul(pw[-1], hsum))
    fact = [1, 1, 2, 6, 24]
    num = [haar_poly(rpmul(wl, pw[n])) / fact[n] for n in range(5)]
    den = [haar_poly(pw[n]) / fact[n] for n in range(5)]
    out = []
    for n in range(5):                                # series division N / D, D_0 = 1
        out.append(num[n] - sum((out[j] * den[n - j] for j in range(n)), F(0)))
    return out


def check_doublet_wilson_loop_has_a_perimeter_law_at_beta_zero():
    premise("synthesis.weak-factor-rotor-lattice-strong-coupling-area-law")
    premise("synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement")
    ok = product_matches_ga()
    # the Hurwitz units reproduce every Haar moment of degree at most 3
    for alpha in product(range(4), repeat=4):
        if sum(alpha) <= 3:
            ok = ok and hurwitz_mean(lambda u: u[0] ** alpha[0] * u[1] ** alpha[1] * u[2] ** alpha[2]
                                     * u[3] ** alpha[3]) == haar_moment(alpha)
    # unitary gauge, tested by Haar integration over the site rotors: the hopping term <phi_x~ U phi_y>_0 has the
    # moments of u0, and on the two-link loop 0 -> 1 -> 0 the kappa expansion of <W> without gauge fixing is c^2
    h = hop_poly(0, 2, 1)
    hn = {(): F(1)}
    for n in range(1, 5):
        hn = rpmul(hn, h)
        ok = ok and haar_poly(hn) == haar_moment((n, 0, 0, 0))
    loop = two_link_loop_coefficients()
    # pure gauge at beta = kappa = 0: E[U] = 0, so every Wilson loop with a link used once vanishes
    EU = tuple(hurwitz_mean(lambda u, k=k: u[k]) for k in range(4))
    ok = ok and EU == (0, 0, 0, 0)
    # one link with the hopping weight exp(kappa u0): E[U u0] = 1/4 (the gluing rule), so the order-kappa
    # mean link is (kappa/4) 1 and a loop of P distinct links has <W> = (kappa/4)^P + O(kappa^(P+2))
    EUu0 = tuple(hurwitz_mean(lambda u, k=k: u[k] * u[0]) for k in range(4))
    ok = ok and EUu0 == (F(1, 4), 0, 0, 0)
    # c(kappa) = E[u0 exp(kappa u0)] / E[exp(kappa u0)] to order kappa^3 from the exact moments
    m2, m4 = haar_moment((2, 0, 0, 0)), haar_moment((4, 0, 0, 0))
    ok = ok and m2 == F(1, 4) and m4 == F(1, 8)
    c1 = m2
    c3 = m4 / 6 - m2 * m2 / 2
    ok = ok and (c1, c3) == (F(1, 4), F(-1, 96))
    # the loop with two links (P = 2), integrated over sites and links with no gauge fixing, is c^2 to order kappa^4
    ok = ok and loop == [0, 0, c1 * c1, 0, 2 * c1 * c3] and loop[4] == F(-1, 192)
    # leading coefficient for the 1 x 1 and 1 x 2 loops (P = 4, 6) against the area law (A = 1, 2)
    perim = {P: c1 ** P for P in (4, 6)}
    ok = ok and perim == {4: F(1, 256), 6: F(1, 4096)}
    GA.check("frozen doublet at beta = 0: <W> = c(kappa)^P with c = kappa/4 - kappa^3/96 + ..., nonzero", ok)
    return ok
