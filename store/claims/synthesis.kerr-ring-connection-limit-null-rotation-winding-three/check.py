"""synthesis.kerr-ring-connection-limit-null-rotation-winding-three: exact checks.

Signature (+,-,-,-). Kerr-Schild data as in the stored cover claims: x + i y = (r + i a) sin(theta) e^{i phi},
Z = r c, c = cos(theta); k^mu = (1, (r x + a y)/(r^2 + a^2), (r y - a x)/(r^2 + a^2), Z/r) (eta-null, flat-geodesic),
H = M r^3/(r^4 + a^2 Z^2), hb(b) = b + H (b.k) k. r(x, y, Z) is the root of r^4 - (x^2 + y^2 + Z^2 - a^2) r^2
- a^2 Z^2 = 0 and its first derivatives come from implicit differentiation, so every first jet is exact.
Points at phi = 0 (by axial symmetry no loss): c = (1 - q^2)/(1 + q^2), s = sin(theta) = 2q/(1 + q^2).
Curves to the ring: r = alpha t, q = 1 + gamma t; along them every quantity is an exact rational function of t
(GA.RF), z = r - i a c = t (alpha + i a gamma) + O(t^2), rho^2 = |z|^2 = rho1^2 t^2 + O(t^3).
Frame: k = e0 + v, l = (e0 - v)/2, e2 = (z-hat x v)/|z-hat x v| (|z-hat x v| = s), e1 = v x e2; at the ring
point (0, a, 0) of phi = 0: v = x-hat (ring tangent), e1 = z-hat, e2 = y-hat = varpi-hat (outward radial).
Gamma(A; B, C) = (D_{F_A} F_B) . F_C, D along hb(F_A). Weighted frame F = (rho^-1/2 k, rho^1/2 l, e1, e2).

  check_connection_formula:  Omega(a) = grad ^ (H (a.k) k) solves the torsion equation exactly, agrees with an
                             independent Koszul solution, and Omega(a).k = -(a.k)(k.grad H) k (both sheets).
  check_frame_components:    Gamma(k; ., .) = 0, Gamma(l; k, e) = 0, Gamma(l; l, e) = e.grad H,
                             Gamma(l; k, l) = -k.grad H, Gamma(e; k, l) = 0; grad H = -M Re((x, y, Z - i a) z^-3).
  check_forced_normalisation_and_limit: along rational curves, the weighted components (with the pure-gauge
                             boost of the weights) diverge at most like t^-2, attained exactly on (N; N, e_i) and on
                             the boost (e_i; K, N); all others are O(t^-3/2) or zero; the normalised limit on N is
                             L_varpi + i L_Z with (gamma_varpi + i gamma_Z)(alpha + i a gamma)^3 = -a M exactly,
                             i.e. L_varpi + i L_Z = -(M/2) e^{-3 i psi}; the radial boost limit has modulus 1/4.
  check_deck_reverses_limit: on the deck-image curve (-alpha, -gamma) the leading coefficients change sign.
  check_linking_loop_generator: for T = d/dpsi round the ring at fixed |z|, time and azimuth, the unweighted
                             components of the connection are O(t) except (T; l, e_i), whose limit G satisfies
                             (G_varpi + i G_Z)(alpha + i a gamma)^2 = i (M/a)(alpha^2 + a^2 gamma^2).
  check_null_rotation_plane: in Cl(1,3), K = e0 + e1: K^e3 = -(K^e2) I, the plane span(K^e2, K^e3) is abelian
                             (and R_u = 1 + K u compose additively), the weights' boost K^N acts on it with weight one,
                             closed under I, kills K, and its elements are nilpotent of order 3 on vectors; in
                             Cl(2,4) they commute with n_inf (the vacuum scale tractor).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

ETA = [1, -1, -1, -1]
RF = GA.RF
MODE = {'rf': False}


def C(x):
    return RF.const(F(x)) if MODE['rf'] else F(x)


def iz(x):
    return x.is_zero() if isinstance(x, RF) else x == 0


class D(object):
    """value and the four partials in X = (T, x, y, Z)."""
    def __init__(self, v, d=None):
        self.v = v
        self.d = d if d is not None else [C(0)] * 4

    def __add__(s, o):
        o = lift(o)
        return D(s.v + o.v, [p + q for p, q in zip(s.d, o.d)])
    __radd__ = __add__

    def __sub__(s, o):
        o = lift(o)
        return D(s.v - o.v, [p - q for p, q in zip(s.d, o.d)])

    def __rsub__(s, o):
        return lift(o) - s

    def __mul__(s, o):
        o = lift(o)
        return D(s.v * o.v, [p * o.v + s.v * q for p, q in zip(s.d, o.d)])
    __rmul__ = __mul__

    def __truediv__(s, o):
        o = lift(o)
        qv = s.v / o.v
        return D(qv, [(p - qv * q) / o.v for p, q in zip(s.d, o.d)])

    def __rtruediv__(s, o):
        return lift(o) / s

    def __neg__(s):
        return D(-s.v, [-p for p in s.d])


def lift(o):
    if isinstance(o, D):
        return o
    if isinstance(o, RF):
        return D(o)
    return D(C(o))


def setup(a, M, alpha, gamma, tval=None):
    """Kerr-Schild data at phi = 0 on the curve r = alpha t, q = 1 + gamma t (t a number, or the RF variable)."""
    MODE['rf'] = tval is None
    t = RF.var() if tval is None else F(tval)
    a, M = F(a), F(M)
    r0 = C(alpha) * t
    q = C(1) + C(gamma) * t
    c0 = (C(1) - q * q) / (C(1) + q * q)
    s0 = (C(2) * q) / (C(1) + q * q)
    x0, y0, Z0 = s0 * r0, s0 * C(a), r0 * c0
    S = x0 * x0 + y0 * y0 + Z0 * Z0 - C(a * a)
    Fr = C(4) * r0 * r0 * r0 - C(2) * S * r0
    rx = (C(2) * x0 * r0 * r0) / Fr
    ry = (C(2) * y0 * r0 * r0) / Fr
    rZ = (C(2) * Z0 * r0 * r0 + C(2 * a * a) * Z0) / Fr
    X = D(x0, [C(0), C(1), C(0), C(0)])
    Y = D(y0, [C(0), C(0), C(1), C(0)])
    Zd = D(Z0, [C(0), C(0), C(0), C(1)])
    R = D(r0, [C(0), rx, ry, rZ])
    H = (M * R * R * R) / (R * R * R * R + a * a * Zd * Zd)
    den = R * R + a * a
    k = [lift(1), (R * X + a * Y) / den, (R * Y - a * X) / den, Zd / R]
    rho2 = R * R + (a * a) * (Zd / R) * (Zd / R)
    return dict(r=r0, c=c0, s=s0, x=x0, y=y0, Z=Z0, H=H, k=k, rho2=rho2, a=a, M=M)


def ipv(u, w):
    out = C(0)
    for i in range(4):
        out = out + C(ETA[i]) * u[i] * w[i]
    return out


def ipd(u, w):
    out = lift(0)
    for i in range(4):
        out = out + lift(u[i]) * w[i] * ETA[i]
    return out


def dirder(u, f):
    out = C(0)
    for m in range(4):
        out = out + u[m] * f.d[m]
    return out


def hb_vec(u, dat):
    H, k = dat['H'], dat['k']
    uk = ipd(u, k)
    return [lift(u[i]) + H * uk * k[i] for i in range(4)]


def theta_vec(u, dat):
    H, k = dat['H'], dat['k']
    uk = ipd(u, k)
    return [lift(u[i]) - H * uk * k[i] for i in range(4)]


def omega_formula(dat, u):
    """bilinear form ((Omega(u).p).q) of Omega(u) = grad ^ (H (u.k) k), u a constant background vector."""
    H, k = dat['H'], dat['k']
    uk = ipd(u, k)
    Xv = [H * uk * k[i] for i in range(4)]
    dX = [[Xv[i].d[m] for i in range(4)] for m in range(4)]      # dX[m][i] = d_m X^i

    def form(p, q):
        qX = [sum((q[m] * dX[m][i] for m in range(4)), C(0)) for i in range(4)]
        pX = [sum((p[m] * dX[m][i] for m in range(4)), C(0)) for i in range(4)]
        return ipv(qX, p) - ipv(pX, q)
    return form


def omega_koszul(dat):
    """independent solve: omega_abc = ((Omega(E_a).e_b).e_c), E_a = hb(e_a), from the Lie brackets of E_a."""
    E = [hb_vec([1 if i == a_ else 0 for i in range(4)], dat) for a_ in range(4)]
    H, k = dat['H'].v, [x.v for x in dat['k']]
    Cv = {}
    for a_ in range(4):
        for b_ in range(4):
            if a_ != b_:
                Ea = [x.v for x in E[a_]]
                Eb = [x.v for x in E[b_]]
                br = [dirder(Ea, E[b_][m]) - dirder(Eb, E[a_][m]) for m in range(4)]
                brk = ipv(br, k)
                Cv[(a_, b_)] = [br[m] - H * brk * k[m] for m in range(4)]

    def Cabc(a_, b_, c_):
        return C(0) if a_ == b_ else C(ETA[c_]) * Cv[(a_, b_)][c_]
    W = [[[(Cabc(a_, b_, c_) - Cabc(b_, c_, a_) + Cabc(c_, a_, b_)) * C(F(1, 2)) for c_ in range(4)]
          for b_ in range(4)] for a_ in range(4)]

    def on(u):
        th = [x.v for x in theta_vec(u, dat)]

        def form(p, q):
            out = C(0)
            for a_ in range(4):
                for b_ in range(4):
                    for c_ in range(4):
                        out = out + th[a_] * p[b_] * q[c_] * W[a_][b_][c_]
            return out
        return form
    return on


def frame(dat):
    """smooth eta-null frame (k, l, e1, e2) as dual vectors."""
    k = dat['k']
    v = k[1:]
    l = [lift(F(1, 2))] + [-(F(1, 2) * x) for x in v]
    N = v[0] * v[0] + v[1] * v[1]
    sv = dat['s']
    sn = D(sv, [p / (C(2) * sv) for p in N.d])             # sqrt(N), N.v = s^2
    e2s = [-(v[1] / sn), v[0] / sn, lift(0)]
    e1s = [v[1] * e2s[2] - v[2] * e2s[1], v[2] * e2s[0] - v[0] * e2s[2], v[0] * e2s[1] - v[1] * e2s[0]]
    return [k, l, [lift(0)] + e1s, [lift(0)] + e2s]


def frame_components(dat, pairs=None):
    """Gamma[(A, B, C)] = (D_{F_A} F_B) . F_C (B < C), and dlr[A] = hb(F_A).grad log rho."""
    fr = frame(dat)
    vals = [[x.v for x in f] for f in fr]
    bg = [[x.v for x in hb_vec(f, dat)] for f in fr]
    G = {}
    for A in range(4):
        form = omega_formula(dat, bg[A])
        for B in range(4):
            der = [dirder(bg[A], fr[B][m]) for m in range(4)]
            for Cc in range(B + 1, 4):
                if pairs is None or (A, B, Cc) in pairs:
                    G[(A, B, Cc)] = ipv(der, vals[Cc]) + form(vals[B], vals[Cc])
    dlr = [dirder(bg[A], dat['rho2']) / (C(2) * dat['rho2'].v) for A in range(4)]
    return G, dlr, fr, vals, bg


def ord_lead(f):
    if f.is_zero():
        return None
    n = next(i for i, x in enumerate(f.num) if x != 0)
    d = next(i for i, x in enumerate(f.den) if x != 0)
    return n - d, f.num[n] / f.den[d]


def gmul(p, q):
    return (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])


WEIGHT = [F(-1, 2), F(1, 2), F(0), F(0)]
# sample data (a, M, alpha, gamma[, t]): points on both sheets (alpha < 0 is r < 0) and curves to the ring
POINTS_A = [(1, 2, F(1), F(1, 2), F(1, 7)), (2, 3, F(-1), F(1, 3), F(1, 50)), (F(1, 2), 1, F(3), F(-2), F(1, 1000))]
POINTS_B = [(1, 2, F(1), F(1, 2), F(1, 9)), (3, F(1, 2), F(-2), F(1, 3), F(1, 40)), (2, 5, F(1, 3), F(-3), F(1, 200))]
CURVES = [(1, 2, F(1), F(1, 2)), (3, F(1, 2), F(-2), F(1, 3))]
DECK_CURVE = (2, 3, F(1, 2), F(1))
LOOP_CURVES = [(1, 2, F(2), F(1)), (3, F(1, 2), F(-1), F(1, 2))]          # F_K = rho^-1/2 k, F_N = rho^1/2 l


def weighted_orders(dat):
    """leading (order in t, coefficient) of each weighted component; MC = boost term of the weights."""
    G, dlr, fr, vals, bg = frame_components(dat)
    out = {}
    for (A, B, Cc), g in G.items():
        w = WEIGHT[A] + WEIGHT[B] + WEIGHT[Cc]
        lead = ord_lead(g)
        out[('G', A, B, Cc)] = None if lead is None else (lead[0] + w, lead[1])
    for A in range(4):
        lead = ord_lead(dlr[A])
        out[('MC', A)] = None if lead is None else (lead[0] + WEIGHT[A], lead[1])
    return out


def check_connection_formula():
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    premise("interior.unipotency-across-kerr-family")
    premise("synthesis.imported-gtg-dictionary")
    for (a, M, al, ga, tv) in POINTS_A:
        dat = setup(a, M, al, ga, tv)
        H, k = dat['H'], dat['k']
        kv = [x.v for x in k]
        assert ipv(kv, kv) == 0
        assert all(dirder(kv, k[i]) == 0 for i in range(4))             # k flat-geodesic
        kos = omega_koszul(dat)
        units = [[F(1) if i == j else F(0) for i in range(4)] for j in range(4)]
        th = [theta_vec(u, dat) for u in units]
        for mu in range(4):
            f1, f2 = omega_formula(dat, units[mu]), kos(units[mu])
            for b in range(4):
                for c in range(4):
                    assert f1(units[b], units[c]) == f2(units[b], units[c])
            # Omega(e_mu).k = -(e_mu.k)(k.grad H) k  (form with second argument e_c)
            kgH = dirder(kv, H)
            for c in range(4):
                assert f1(kv, units[c]) == -ETA[mu] * kv[mu] * kgH * ipv(kv, units[c])
        for mu in range(4):
            for nu in range(mu + 1, 4):
                tm, tn = [x.v for x in th[mu]], [x.v for x in th[nu]]
                fm, fn = omega_formula(dat, units[mu]), omega_formula(dat, units[nu])
                for c in range(4):
                    torsion = (th[nu][c].d[mu] - th[mu][c].d[nu]
                               + ETA[c] * fm(tn, units[c]) - ETA[c] * fn(tm, units[c]))
                    assert torsion == 0
    return True


def check_frame_components():
    premise("synthesis.kerr-ring-blow-up-forced-cover-fixed-order")
    premise("synthesis.kerr-ring-double-cover-data")
    for (a, M, al, ga, tv) in POINTS_B:
        dat = setup(a, M, al, ga, tv)
        G, dlr, fr, vals, bg = frame_components(dat)
        H = dat['H']
        kv, lv = vals[0], vals[1]
        gram = [[ipv(vals[i], vals[j]) for j in range(4)] for i in range(4)]
        assert gram == [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
        assert all(G[(0, B, Cc)] == 0 for B in range(4) for Cc in range(B + 1, 4))
        for e in (2, 3):
            assert G[(1, 0, e)] == 0
            assert G[(1, 1, e)] == dirder(vals[e], H)
            assert G[(e, 0, 1)] == 0
        assert G[(1, 0, 1)] == -dirder(kv, H)
        assert G[(1, 1, 2)] != 0 and G[(1, 1, 3)] != 0
        # grad H = -M Re((x, y, Z - i a) z^-3), z = r - i a c, z^2 = x^2 + y^2 + (Z - i a)^2
        r, c, x, y, Z = dat['r'], dat['c'], dat['x'], dat['y'], dat['Z']
        z = (r, -a * c)
        assert gmul(z, z) == (x * x + y * y + Z * Z - a * a, -2 * a * Z)
        n2 = z[0] * z[0] + z[1] * z[1]
        zc = (z[0] / n2, -z[1] / n2)                      # 1/z
        z3 = gmul(zc, gmul(zc, zc))
        assert H.v == M * zc[0]
        assert H.d[1] == -M * x * z3[0] and H.d[2] == -M * y * z3[0]
        assert H.d[3] == -M * gmul((Z, -a), z3)[0] and H.d[0] == 0
    return True


def check_forced_normalisation_and_limit():
    premise("synthesis.kerr-ring-blow-up-forced-cover-fixed-order")
    premise("synthesis.kerr-ring-double-cover-data")
    premise("interior.complex-scale-inverse-cube-killing-spinor")
    for (a, M, al, ga) in CURVES:
        dat = setup(a, M, al, ga)
        o2 = ord_lead(dat['rho2'].v)
        rho1sq = al * al + a * a * ga * ga
        assert o2 == (2, rho1sq)
        out = weighted_orders(dat)
        worst = min(v[0] for v in out.values() if v is not None)
        assert worst == -2
        at_worst = sorted(key for key, v in out.items() if v is not None and v[0] == -2)
        assert at_worst == [('G', 1, 1, 2), ('G', 1, 1, 3), ('MC', 2), ('MC', 3)]
        assert all(v is None or v[0] >= F(-3, 2) for key, v in out.items() if key not in at_worst)
        gZ, gV = out[('G', 1, 1, 2)][1], out[('G', 1, 1, 3)][1]     # e1 -> z-hat, e2 -> varpi-hat
        zdir = (al, a * ga)
        assert gmul((gV, gZ), gmul(zdir, gmul(zdir, zdir))) == (-a * M, 0)
        # |L|^2 = rho1^6 (gV^2 + gZ^2)/(4 a^2) = M^2/4
        assert rho1sq ** 3 * (gV * gV + gZ * gZ) == a * a * M * M
        # radial boost: -1/2 d e.grad log rho, d = rho^2/(2a): squared modulus 1/16
        m1, m2 = out[('MC', 2)][1], out[('MC', 3)][1]
        assert rho1sq * rho1sq * (m1 * m1 + m2 * m2) == a * a
    return True


def check_deck_reverses_limit():
    premise("synthesis.kerr-ring-double-cover-data")
    a, M, al, ga = DECK_CURVE
    pairs = {(1, 1, 2), (1, 1, 3)}
    lead = []
    for sgn in (1, -1):
        dat = setup(a, M, sgn * al, sgn * ga, None)
        G, dlr, fr, vals, bg = frame_components(dat, pairs)
        lead.append([ord_lead(G[p]) for p in sorted(pairs)])
    for (o1, c1), (o2, c2) in zip(lead[0], lead[1]):
        assert o1 == o2 == -3 and c2 == -c1 and c1 != 0
    return True


def loop_generator(dat):
    """leading (order, coefficient) of (D_T F_B) . F_C for T = d/dpsi on |z| = const at fixed time and
    geometric azimuth (unweighted frame)."""
    r, c, s, a = dat['r'], dat['c'], dat['s'], C(dat['a'])
    dr = a * c                                   # dz/dpsi = i z: dr = a c dpsi, dc = -(r/a) dpsi
    dc = -(r / a)
    ds = -(c / s) * dc
    dphi = (a * dr) / (r * r + a * a)            # Kerr-Schild phi shifted so that arg(x + i y) is fixed
    T = [C(0), s * dr + r * ds - dphi * dat['y'], a * ds + dphi * dat['x'], c * dr + r * dc]
    fr = frame(dat)
    vals = [[x.v for x in f] for f in fr]
    form = omega_formula(dat, T)
    out = {}
    for B in range(4):
        der = [dirder(T, fr[B][m]) for m in range(4)]
        for Cc in range(B + 1, 4):
            out[(B, Cc)] = ord_lead(ipv(der, vals[Cc]) + form(vals[B], vals[Cc]))
    return out


def check_linking_loop_generator():
    premise("synthesis.kerr-ring-double-cover-data")
    premise("synthesis.kerr-ring-blow-up-forced-cover-fixed-order")
    for (a, M, al, ga) in LOOP_CURVES:
        out = loop_generator(setup(a, M, al, ga, None))
        assert all(v is None or v[0] >= 1 for key, v in out.items() if key not in ((1, 2), (1, 3)))
        (oZ, gZ), (oV, gV) = out[(1, 2)], out[(1, 3)]
        assert oZ == 0 and oV == 0
        zdir = (al, a * ga)
        # (G_varpi + i G_Z) (alpha + i a gamma)^2 = i (M/a) |alpha + i a gamma|^2, i.e. G = i (M/a) e^{-2 i psi}
        assert gmul((gV, gZ), gmul(zdir, zdir)) == (0, M * (al * al + a * a * ga * ga) / a)
    return True


def check_null_rotation_plane():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("transport.group-null-rotations")
    sq = GA.sig(1, 3)
    e0, e1, e2, e3 = (GA.gen(i) for i in range(4))
    Ip = GA.mul(GA.mul(e0, e1, sq), GA.mul(e2, e3, sq), sq)
    K = GA.add(e0, e1)
    B2, B3 = GA.mul(K, e2, sq), GA.mul(K, e3, sq)             # K^e2, K^e3 (K orthogonal to e2, e3)
    assert GA.eq(B3, GA.neg(GA.mul(B2, Ip, sq)))
    assert GA.eq(GA.mul(B3, Ip, sq), B2)
    assert GA.commutes(B2, B3, sq)
    one = GA.sc(1)
    R2, R3 = GA.add(one, B2), GA.add(one, B3)                 # R_u = 1 + K u, the group of null rotations about K
    assert GA.eq(GA.mul(R2, R3, sq), GA.add(one, GA.add(B2, B3)))
    assert GA.eq(GA.mul(R2, R3, sq), GA.mul(R3, R2, sq))
    # the boost of the weights acts on the plane with weight one: [K^N, K^e]/2 = K^e (so n + R K^N is solvable)
    Nn = GA.scal(F(1, 2), GA.sub(e0, e1))
    KN = GA.scal(F(1, 2), GA.sub(GA.mul(K, Nn, sq), GA.mul(Nn, K, sq)))
    for B in (B2, B3):
        assert GA.eq(GA.scal(F(1, 2), GA.sub(GA.mul(KN, B, sq), GA.mul(B, KN, sq))), B)

    def act(B, u):
        return GA.scal(F(1, 2), GA.sub(GA.mul(B, u, sq), GA.mul(u, B, sq)))
    N = GA.scal(F(1, 2), GA.sub(e0, e1))
    assert GA.eq(GA.scal(F(1, 2), GA.add(GA.mul(K, N, sq), GA.mul(N, K, sq))), GA.sc(1))
    for B in (B2, B3, GA.add(GA.scal(3, B2), GA.scal(-5, B3))):
        assert GA.is_zero(act(B, K))
        assert not GA.is_zero(act(B, act(B, N)))
        for u in (e0, e1, e2, e3):
            assert GA.is_zero(act(B, act(B, act(B, u))))
    sq6 = GA.sig(2, 4)                                         # generators 0, 1 square +1; 2..5 square -1
    ninf = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(5)))
    n0 = GA.sub(GA.gen(0), GA.gen(5))
    assert GA.is_zero(GA.mul(ninf, ninf, sq6)) and GA.is_zero(GA.mul(n0, n0, sq6))
    assert GA.eq(GA.scal(F(1, 2), GA.add(GA.mul(n0, ninf, sq6), GA.mul(ninf, n0, sq6))), GA.sc(1))
    Kc = GA.add(GA.gen(1), GA.gen(2))                          # spacetime W = span(gen 1..4), (+,-,-,-)
    assert GA.is_zero(GA.mul(Kc, Kc, sq6))
    for Bc in (GA.mul(Kc, GA.gen(3), sq6), GA.mul(Kc, GA.gen(4), sq6)):
        assert GA.commutes(Bc, ninf, sq6) and GA.commutes(Bc, n0, sq6)
        solder = GA.sub(GA.mul(ninf, Kc, sq6), GA.mul(Kc, ninf, sq6))   # 2 n_inf ^ K, the tractor coupling
        assert not GA.is_zero(solder) and not GA.commutes(solder, n0, sq6)
    return True


if __name__ == "__main__":
    import time
    for f in (check_connection_formula, check_frame_components, check_forced_normalisation_and_limit,
              check_deck_reverses_limit, check_linking_loop_generator, check_null_rotation_plane):
        t0 = time.time()
        print(f.__name__, f(), round(time.time() - t0, 1))
