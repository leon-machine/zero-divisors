"""synthesis.cosmological-horizon-completed-pair: exact checks in Cl(2,4).

Conventions of the de Sitter scale lemma: n0 . ninf = +1, X(x) = n0 + x - Q(x) ninf / 2,
I = ninf + (L/6) n0, W = ninf - (L/6) n0. Lambda = 3 h^2 with h rational, so that
e_W = W / h is rational.
"""
from fractions import Fraction as F
from itertools import product
import GA
from GA import mul, add, sub, scal, sc, gen, eq, is_zero
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)                 # e0 | e1 e2 e3 | e+ e-
MIRROR = tuple(-s for s in SQ)
HS = [F(1, 2), F(1), F(3), F(2, 7), F(5, 3)]
QS = [F(11, 10), F(2), F(1, 3), F(7, 4)]
# rational points of the unit 2-sphere (Pythagorean quadruples and triples)
UNIT = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(3, 5), F(4, 5), F(0)),
        (F(1, 3), F(2, 3), F(2, 3)), (F(2, 7), F(3, 7), F(6, 7)), (F(-4, 9), F(4, 9), F(7, 9))]


def dot(a, b, sq):
    return add(mul(a, b, sq), mul(b, a, sq)).get((), F(0)) / 2


def vec(xs):
    out = {}
    for i, c in enumerate(xs):
        if c:
            out = add(out, scal(c, gen(i)))
    return out


def frame():
    n0 = scal(F(1, 2), add(gen(4), gen(5)))
    ninf = sub(gen(4), gen(5))
    return gen(0), n0, ninf


def lift(xs, sq):
    e0, n0, ninf = frame()
    x = vec(xs)
    Q = dot(x, x, sq) if x else F(0)
    return add(add(n0, x), scal(-Q / 2, ninf)), Q


def ratio(a, b):
    """k with a = k b, or None."""
    k = None
    for bl in set(a) | set(b):
        ca, cb = a.get(bl, F(0)), b.get(bl, F(0))
        if ca == 0 and cb == 0:
            continue
        if cb == 0:
            return None
        if k is None:
            k = ca / cb
        elif k != ca / cb:
            return None
    return k


def rank(vectors):
    rows = [[v.get((i,), F(0)) for i in range(6)] for v in vectors]
    r = 0
    for c in range(6):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c] / rows[r][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


def rotor(q, u):
    return add(sc((q + 1 / q) / 2), scal((q - 1 / q) / 2, u)), \
        add(sc((q + 1 / q) / 2), scal(-(q - 1 / q) / 2, u))


def check_completed_pair():
    premise("synthesis.de-sitter-static-boost-frozen-point")
    premise("mass.de-sitter-scale-frozen-point")
    premise("dark-energy.imported-frozen-point-geometry")
    premise("singularity.pseudo-inverse-identities-hyperbolic-atom")
    premise("singularity.modular-structure-completed-pair")
    e0, n0, ninf = frame()
    for h in HS:
        L = 3 * h * h
        I = add(ninf, scal(L / 6, n0))
        W = sub(ninf, scal(L / 6, n0))
        eW = scal(1 / h, W)
        u = mul(e0, eW, SQ)
        B = mul(e0, W, SQ)
        assert eq(B, scal(h, u)) and eq(mul(u, u, SQ), sc(1))
        # (i) the Riemann tensor of g = sigma^{-2} eta from its Christoffel symbols, exactly,
        #     in the convention R^a_bcd = d_c G^a_db - d_d G^a_cb + G^a_ce G^e_db - G^a_de G^e_cb
        for xs in [(F(0), F(0), F(0), F(0)), (F(1, 3), F(-1, 2), F(0), F(2, 5)),
                   (F(-1), F(1, 4), F(3, 7), F(-2, 3)), (F(2), F(0), F(1), F(1))]:
            c = curvature_constant(xs, L)
            assert c == -L / 3
        # (ii) the bifurcation sphere: radius r with r^2 = 12/L, i.e. r = 2/h
        r = 2 / h
        for p in UNIT:
            s = [F(0)] + [r * c for c in p]
            X, Q = lift(s, SQ)
            assert Q == -12 / L
            sig = dot(X, I, SQ)
            assert sig == 2
            assert dot(e0, X, SQ) == 0 and dot(W, X, SQ) == 0
            # d(X/sigma)[y] = dX[y]/sigma - X dsigma[y]/sigma^2, dX[y] = y - eta(x,y) ninf,
            # dsigma[y] = -(L/6) eta(x,y)
            sv = vec(s)

            def dhat(y):
                yv = vec(y)
                ex = dot(sv, yv, SQ)
                dX = sub(yv, scal(ex, ninf))
                ds = -(L / 6) * ex
                return sub(scal(1 / sig, dX), scal(ds / sig ** 2, X))
            img_t = dhat([F(1), F(0), F(0), F(0)])
            img_r = dhat(s)
            assert eq(img_t, scal(F(1, 2), e0))
            assert eq(img_r, scal(3 / L, W))
            # two tangent directions of the sphere at s: spatial y with eta(s, y) = 0
            a, b, c = p
            cand = [(F(0), -c, b), (c, F(0), -a), (-b, a, F(0))]
            tang = [t for t in cand if any(t)][:3]
            imgs = [dhat([F(0)] + list(t)) for t in tang]
            for im in imgs:
                assert dot(im, X, SQ) == 0 and dot(im, I, SQ) == 0
                assert dot(im, e0, SQ) == 0 and dot(im, W, SQ) == 0
            assert rank([img_t, img_r] + imgs) == 4
            for y in ([F(1), F(0), F(0), F(0)], s, [F(0)] + list(tang[0])):
                im = dhat(y)
                assert dot(im, X, SQ) == 0 and dot(im, I, SQ) == 0
                yv = vec(y)
                assert dot(im, im, SQ) == dot(yv, yv, SQ) / sig ** 2
        # (iii) the pair
        v = scal(F(1, 2), add(e0, eW))
        vs = scal(F(1, 2), sub(e0, eW))
        assert is_zero(mul(v, v, SQ)) and is_zero(mul(vs, vs, SQ))
        assert eq(add(mul(v, vs, SQ), mul(vs, v, SQ)), sc(1))
        assert eq(sub(mul(vs, v, SQ), mul(v, vs, SQ)), u)
        # the other null ray gives occupation boost -u; other normalisations fail CAR
        for a in (F(1), F(1, 3), F(-1, 2)):
            va = scal(a, add(e0, eW))
            vas = scal(a, sub(e0, eW))
            assert eq(add(mul(va, vas, SQ), mul(vas, va, SQ)), sc(4 * a * a))
            wb = scal(a, sub(e0, eW))
            wbs = scal(a, add(e0, eW))
            assert eq(sub(mul(wbs, wb, SQ), mul(wb, wbs, SQ)), scal(-4 * a * a, u))
        # projectors: (1 + u)/2 = v* v, (1 - u)/2 = v v*
        assert eq(scal(F(1, 2), add(sc(1), u)), mul(vs, v, SQ))
        assert eq(scal(F(1, 2), sub(sc(1), u)), mul(v, vs, SQ))
        for q in QS:
            R, Rr = rotor(q, u)
            assert eq(mul(R, Rr, SQ), sc(1))
            assert eq(mul(mul(R, v, SQ), Rr, SQ), scal(1 / (q * q), v))
            assert eq(mul(mul(R, vs, SQ), Rr, SQ), scal(q * q, vs))
            Y = mul(mul(R, n0, SQ), Rr, SQ)
            x0 = (2 / h) * (q * q - 1) / (q * q + 1)
            Xt, _ = lift([x0, F(0), F(0), F(0)], SQ)
            k = ratio(Y, Xt)
            assert k is not None and k != 0
            assert (x0 > 0) == (q > 1)
        # (iv) conformal infinity
        assert dot(v, I, SQ) == 0 and dot(vs, I, SQ) == 0
        Xm, Qm = lift([-2 / h, F(0), F(0), F(0)], SQ)
        Xp, Qp = lift([2 / h, F(0), F(0), F(0)], SQ)
        assert eq(v, scal(-h / 4, Xm)) and eq(vs, scal(h / 4, Xp))
        assert dot(Xm, I, SQ) == 0 and dot(Xp, I, SQ) == 0 and Qm == 12 / L
        # (v) the mirror
        assert eq(mul(mul(e0, W, MIRROR), mul(e0, W, MIRROR), MIRROR), sc(L / 3))
        um = mul(e0, eW, MIRROR)
        assert eq(mul(um, um, MIRROR), sc(1))
        w = scal(F(1, 2), sub(e0, eW))
        ws = scal(F(-1, 2), add(e0, eW))
        assert is_zero(mul(w, w, MIRROR)) and is_zero(mul(ws, ws, MIRROR))
        assert eq(add(mul(w, ws, MIRROR), mul(ws, w, MIRROR)), sc(1))
        assert eq(sub(mul(ws, w, MIRROR), mul(w, ws, MIRROR)), um)
        for q in QS:
            R, Rr = rotor(q, um)
            assert eq(mul(mul(R, w, MIRROR), Rr, MIRROR), scal(1 / (q * q), w))
        # in the mirror the pair along i- with v* = frame adjoint has occupation boost -u
        vm = scal(F(1, 2), add(e0, eW))
        vms = scal(F(1, 2), sub(eW, e0))
        assert eq(add(mul(vm, vms, MIRROR), mul(vms, vm, MIRROR)), sc(1))
        assert eq(sub(mul(vms, vm, MIRROR), mul(vm, vms, MIRROR)), scal(-1, um))
    # (v) no pair for L <= 0
    for L in (F(0), F(-3), F(-12, 5)):
        W = sub(ninf, scal(L / 6, n0))
        g00, g0w, gww = dot(e0, e0, SQ), dot(e0, W, SQ), dot(W, W, SQ)
        det = g00 * gww - g0w * g0w
        if L == 0:
            assert det == 0                      # degenerate plane
        else:
            assert det > 0 and g00 > 0           # definite: no null vector
    return True


ETA = [1, -1, -1, -1]


def christoffel(xs, L):
    """G[a][b][c] and its derivative dG[e][a][b][c] = d_e G^a_bc for g = sigma^{-2} eta,
    sigma = 1 - L Q(x)/12, from G^a_bc = -(d^a_b s_c + d^a_c s_b - eta_bc eta^ad s_d)/sigma."""
    Q = sum(ETA[i] * xs[i] * xs[i] for i in range(4))
    sig = 1 - L * Q / 12
    s = [-(L / 6) * ETA[i] * xs[i] for i in range(4)]          # s_a = d_a sigma
    ss = [[-(L / 6) * ETA[i] if i == j else F(0) for j in range(4)] for i in range(4)]
    up = lambda d: [ETA[a] * d[a] for a in range(4)]           # raise with eta
    def num(a, b, c, sv):
        return (sv[c] if a == b else 0) + (sv[b] if a == c else 0) - \
            (ETA[b] if b == c else 0) * up(sv)[a]
    G = [[[-num(a, b, c, s) / sig for c in range(4)] for b in range(4)] for a in range(4)]
    dG = [[[[-num(a, b, c, ss[e]) / sig + num(a, b, c, s) * s[e] / sig ** 2
             for c in range(4)] for b in range(4)] for a in range(4)] for e in range(4)]
    return G, dG, sig


def curvature_constant(xs, L):
    """The constant c with R_abcd = c (g_ac g_bd - g_ad g_bc); asserts it exists."""
    G, dG, sig = christoffel(xs, L)
    g = [[(ETA[i] if i == j else 0) / sig ** 2 for j in range(4)] for i in range(4)]
    c = None
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                for d in range(4):
                    Rup = dG[cc][a][d][b] - dG[d][a][cc][b] + \
                        sum(G[a][cc][e] * G[e][d][b] - G[a][d][e] * G[e][cc][b] for e in range(4))
                    Rlow = g[a][a] * Rup
                    form = g[a][cc] * g[b][d] - g[a][d] * g[b][cc]
                    if form == 0:
                        assert Rlow == 0
                        continue
                    k = Rlow / form
                    if c is None:
                        c = k
                    assert k == c
    return c


# ---------------------------------------------------------------------------
# GTG proof of Step 1 (2026-11-07): the de Sitter field of the scale as the dilation hb^{-1}(a) = a/sigma,
# sigma = 1 - Lambda Q(x)/12, on flat spacetime; Omega solved from the torsion condition equals
# (c/sigma) x ^ a with c = -Lambda/6; the store-sign curvature is calR(B) = (Lambda/3) B, the Weyl part
# vanishes, and the round-sphere-positive Riemann tensor of C11 is -(Lambda/3)(g_ac g_bd - g_ad g_bc).
# ---------------------------------------------------------------------------
import gtg  # noqa: E402

GTG_LAMS = [F(3, 4), F(12), F(12, 49)]                     # Lambda = 3 h^2, h = 1/2, 2, 2/7
GTG_PTS = [(F(0), F(0), F(0), F(0)), (F(1, 3), F(-1, 4), F(1, 5), F(0)), (F(-1, 2), F(0), F(2, 3), F(1, 7))]
GTG_PLANES = gtg.bivector_blades(4)
GTG_QUADS = [(0, 1, 0, 1), (1, 2, 1, 2), (0, 3, 3, 0), (1, 2, 2, 3)]


def _dilation(lam, x0):
    def rows(X):
        qx = X[0] * X[0] - X[1] * X[1] - X[2] * X[2] - X[3] * X[3]
        inv = (1 - (lam / 12) * qx).inv()
        return [[inv if a == mu else F(0) for a in range(4)] for mu in range(4)]
    return gtg.field_from_hbinv(rows, x0)


def check_gtg_dilation_field_curvature_selects_no_plane():
    premise("mass.de-sitter-scale-frozen-point")
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    done = 0
    for lam in GTG_LAMS:
        for x0 in GTG_PTS:
            x = gtg.vec(list(x0))
            sigma = 1 - (lam / 12) * gtg.vdot(x, x)
            fld = _dilation(lam, x0)
            ok = ok and fld.torsion_free()
            for mu in range(4):
                ok = ok and gtg.m_sub(fld.Omega(mu), gtg.m_scal(-lam / (6 * sigma), gtg.wedge(x, gtg.e(mu)))) == {}
            Rc = fld.curvature()
            ok = ok and all(gtg.m_sub(Rc[pl], gtg.m_scal(lam / 3, gtg.biv(*pl))) == {} for pl in GTG_PLANES)
            ok = ok and all(not v for v in gtg.weyl_op(Rc).values())
            ok = ok and all(gtg.m_sub(gtg.ricci(Rc, gtg.e(m)), gtg.m_scal(lam, gtg.e(m))) == {} for m in range(4))
            for u, v, w, z in GTG_QUADS:
                eu, ev, ew, ez = gtg.e(u), gtg.e(v), gtg.e(w), gtg.e(z)
                want = -(lam / 3) * (gtg.vdot(eu, ew) * gtg.vdot(ev, ez) - gtg.vdot(eu, ez) * gtg.vdot(ev, ew))
                ok = ok and gtg.riem_o(Rc, eu, ev, ew, ez) == want
            done += 1
    # hand value: Lambda = 3/4 at x = (1/3, -1/4, 1/5, 0): Q(x) = 1/9 - 1/16 - 1/25, sigma = 1 - Q(x)/16
    x = gtg.vec(list(GTG_PTS[1]))
    ok = ok and gtg.vdot(x, x) == F(31, 3600) and done == 9
    ok = ok and gtg.m_sub(_dilation(F(3, 4), GTG_PTS[1]).Omega(0),
                          gtg.m_scal(F(-1, 8) / (1 - F(31, 57600)), gtg.wedge(x, gtg.e(0)))) == {}
    GA.check("GTG: dilation field Omega = -(Lambda/6 sigma) x ^ a, calR = (Lambda/3) id, Weyl zero", ok)
    assert ok
