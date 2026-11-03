"""field-theory.coupled-system-tree-level: exact checks.

Coupled states: dicts {photon occupation tuple: tower element} (Cl(1,3) ground, four tower planes 4..11: fermion
modes A k1 (plane 0), B k2 (1), A k3 (2), B k4 (3)); photon operators a_m = d/dz_m, a_m* = z_m act on the
polynomial index (Proposition field-theory.fock-space-maxwell-modes). Photon modes (q, h = +-1) and (-q, h) with
polarisations t1 - h I4 t2 on rational frames, mode factor N = 1/sqrt(4|q|) (|q| and 4|q| perfect squares). Vertex
H_int = e sum J^mu A_mu (component form, e = 1), each term (J(j,l) . eps or conj eps) N v_j w_l times a_m or a_m*;
Coulomb operator H_C = rho_A(p) rho_B(-p)/|p|^2 with rho = J^0 v w. H_0 = sum E_j v_j w_j + sum |q_m| a_m* a_m is
applied as an operator.
(1) H_int (component and GA-product vertex) is self-adjoint for the combined adjoint (T03's * on the tower,
    a <-> a*), H_C is self-adjoint, and every vertex term commutes with Q_A and Q_B.
(2) Second order H_int (E_i - H_0)^-1 H_int + H_C on |A1 B2>: the <A3 B4| component equals -J_A(3,1) . J_B(4,2)/t
    exactly at nine configurations, the rest of the no-photon component lies along |i>; dropping H_C, or one
    helicity, changes it (three configurations).
(3) The GA-product vertex proj(J_GA A_GA) gives the same amplitude, each intermediate state being the component
    vertex's with the helicity label swapped.
(4) Identical fermions (one species, eight photon modes at q = k1 - k3 and q' = k1 - k4, Coulomb operator
    (1/2) sum_p rho(p) rho(-p)/|p|^2): the amplitude is -(J31 . J42/t - J41 . J32/u), and not the bosonic
    -(J31 . J42/t + J41 . J32/u), at four configurations off the axes.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
S4 = (1, -1, -1, -1)
I4 = {(0, 1, 2, 3): F(1)}
IS3 = {(1, 2): F(-1)}                      # I sigma_3 = gamma_2 gamma_1
G0 = GA.gen(0)
EVEN = [{b: F(1)} for b in GA.all_blades(4) if len(b) % 2 == 0]
GUP = [GA.gen(0), GA.neg(GA.gen(1)), GA.neg(GA.gen(2)), GA.neg(GA.gen(3))]


def _scl(c, x):
    out = {}
    for b, v in x.items():
        w = c * v
        if w != 0:
            out[b] = w
    return out


def _star(x, s):
    """T03's *: reversion, sign -1 per negative-square generator, conjugation of Q(i) coefficients."""
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        out[b] = sign * (c.conj() if isinstance(c, QI) else c)
    return {b: c for b, c in out.items() if c != 0}


def _chi(e, p):
    return _scl(F(1, 2), GA.sub(p, _scl(F(e), GA.mul(GA.mul(I4, p, S4), IS3, S4))))


def _proj(x):
    """span{1, I4} part over the ground (tower blades carried along)."""
    out = {}
    for b, c in x.items():
        g = tuple(i for i in b if i < 4)
        if g == () or g == (0, 1, 2, 3):
            out[b] = c
    return out


def _kvec(k):
    return GA.add(*[_scl(F(k[i]), GA.gen(i)) for i in range(4) if k[i] != 0])


def _spinor(k, e=1):
    """The first nonzero (k g0 / 2k^0) chi_e(even blade): a chirality-e massless spinor in ker k."""
    for b in EVEN:
        f = _scl(F(1) / (2 * F(k[0])), GA.mul(GA.mul(_kvec(k), G0, S4), _chi(e, b), S4))
        if not GA.is_zero(f):
            return f


def _to_q(x):
    return QI(x.get((), F(0)), x.get((0, 1, 2, 3), F(0)))


def _qmv(z):
    return GA.add(GA.sc(z.re), _scl(z.im, I4))


def _cur(a, b):
    """GA current J^mu(a, b) = proj(a* g0 g^mu b) in span{1, I4}, as Gaussian rationals."""
    return [_to_q(_proj(GA.mul(GA.mul(GA.mul(_star(a, S4), G0, S4), GUP[mu], S4), b, S4))) for mu in range(4)]


def _mdot(J1, J2):
    return J1[0] * J2[0] - J1[1] * J2[1] - J1[2] * J2[2] - J1[3] * J2[3]


def _plane(q):
    e_, f_ = 4 + 2 * q, 5 + 2 * q
    return (GA.add(_scl(F(1, 2), GA.gen(e_)), _scl(F(1, 2), GA.gen(f_))),
            GA.add(_scl(F(1, 2), GA.gen(e_)), _scl(F(-1, 2), GA.gen(f_))))


def _isqrt(n):
    """Integer square root by Newton's method (integers only)."""
    if n < 2:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x



SPACE = tuple(list(S4) + [1, -1] * 4)
CONFIGS = [((6, 0, 0, 6), (7, 2, 6, -3), (9, 6, 6, 3), (4, -4, 0, 0)),
           ((7, 3, 2, 6), (9, -3, 6, -6), (10, 6, 8, 0), (6, -6, 0, 0)),
           ((9, 0, 0, -9), (9, 4, 8, -1), (12, 8, 4, -8), (6, -4, 4, -2)),
           ((9, 9, 0, 0), (12, -8, 8, 4), (12, 8, 4, 8), (9, -7, 4, -4)),
           ((5, -3, 0, 4), (9, 1, 8, 4), (12, -4, 8, 8), (2, 2, 0, 0)),
           ((6, 2, -4, -4), (12, -8, -8, 4), (9, 1, -8, 4), (9, -7, -4, -4)),
           ((3, 3, 0, 0), (5, 0, 3, -4), (5, 3, 0, -4), (3, 0, 3, 0)),
           ((3, 0, 0, -3), (5, 3, 4, 0), (5, 0, 4, -3), (3, 3, 0, 0)),
           ((3, 1, -2, 2), (3, 2, 2, -1), (3, 1, 2, 2), (3, 2, -2, -1))]
C4CONF = [((8, 0, 0, -8), (7, -6, -3, 2), (9, -6, 3, -6), (6, 0, -6, 0)),
          ((9, 0, -9, 0), (9, -4, 7, 4), (9, -8, -1, -4), (9, 4, -1, 8)),
          ((9, 4, -1, 8), (9, 4, -1, -8), (13, 12, -5, 0), (5, -4, 3, 0)),
          ((9, 4, 4, -7), (9, 4, -8, -1), (9, 0, 0, -9), (9, 8, -4, 1))]
SPECIES = {0: "A", 2: "A", 1: "B", 3: "B"}


def _sm(x, y):
    return GA.mul(x, y, SPACE)


TP = [_plane(j) for j in range(4)]


def _vac():
    V = {(): F(1)}
    for (v, w) in TP:
        V = _sm(V, _sm(w, v))
    return V


VAC = _vac()


def _frame(n):
    E = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    n = list(n)
    if n == E[2]:
        return E[0], E[1]
    if n == [F(0), F(0), F(-1)]:
        return E[1], E[0]
    m = [n[0], n[1], n[2] - 1]
    mm = sum(x * x for x in m)
    R = lambda x: [x[i] - 2 * sum(x[j] * m[j] for j in range(3)) * m[i] / mm for i in range(3)]
    return R(E[1]), R(E[0])


def _s_apply(X, op, st):
    out = {}
    for e, Y in st.items():
        if op is None:
            items = [(e, F(1))]
        elif op[0] == "a":
            m = op[1]
            items = [(e[:m] + (e[m] - 1,) + e[m + 1:], F(e[m]))] if e[m] > 0 else []
        else:
            m = op[1]
            items = [(e[:m] + (e[m] + 1,) + e[m + 1:], F(1))]
        for (e2, c) in items:
            out[e2] = GA.add(out.get(e2, {}), _scl(c, _sm(X, Y)))
    return {e: Y for e, Y in out.items() if not GA.is_zero(Y)}


def _s_add(*sts):
    out = {}
    for st in sts:
        for e, Y in st.items():
            out[e] = GA.add(out.get(e, {}), Y)
    return {e: Y for e, Y in out.items() if not GA.is_zero(Y)}


def _apply_terms(terms, st):
    return _s_add(*[_s_apply(X, op, st) for (X, op) in terms]) if terms else {}


def _H0_apply(sysd, st):
    out = _s_apply(sysd["H0"], None, st)
    for m, Qm in enumerate(sysd["Qm"]):
        out = _s_add(out, _s_apply(GA.sc(Qm), ("ad", m), _s_apply(GA.sc(1), ("a", m), st)))
    return out


def _energy(sysd, e, Y):
    res = _H0_apply(sysd, {e: Y})
    HY = res[e]
    b, c = next((b, c) for b, c in Y.items() if c != 0)
    E = HY.get(b, F(0)) / c
    return E if set(res) == {e} and GA.eq(HY, _scl(E, Y)) else None


def _adjoint_terms(terms):
    flip = {"a": "ad", "ad": "a"}
    return [(_star(X, SPACE), (flip[op[0]], op[1])) for (X, op) in terms]


def _same_operator(t1, t2):
    d1, d2 = {}, {}
    for (X, op) in t1:
        d1[op] = GA.add(d1.get(op, {}), X)
    for (X, op) in t2:
        d2[op] = GA.add(d2.get(op, {}), X)
    return all(GA.eq(d1.get(o, {}), d2.get(o, {})) for o in set(d1) | set(d2))


def _coeff(Y, X):
    """z in span{1, I4} with Y = z X, or None."""
    if GA.is_zero(Y):
        return QI(0)
    IX = GA.mul(I4, X, SPACE)
    keys = sorted(set(X) | set(IX))
    for b1 in keys:
        for b2 in keys:
            a11, a12, a21, a22 = X.get(b1, F(0)), IX.get(b1, F(0)), X.get(b2, F(0)), IX.get(b2, F(0))
            det = a11 * a22 - a12 * a21
            if det != 0:
                r1, r2 = Y.get(b1, F(0)), Y.get(b2, F(0))
                z = QI((r1 * a22 - a12 * r2) / det, (a11 * r2 - a21 * r1) / det)
                return z if GA.eq(Y, _sm(_qmv(z), X)) else None
    return None


def _build(cfg, vertex="component"):
    k = list(cfg)
    q = [k[0][i] - k[2][i] for i in range(4)]
    Q2 = q[1] ** 2 + q[2] ** 2 + q[3] ** 2
    Q = _isqrt(Q2)
    Nm = F(1, _isqrt(4 * Q))
    ok = Q * Q == Q2 and _isqrt(4 * Q) ** 2 == 4 * Q
    t1, t2 = _frame([F(x, Q) for x in q[1:]])
    modes = []
    for (qq, a1, a2) in ((q, t1, t2), ([-x for x in q], t2, t1)):
        for h in (1, -1):
            modes.append((qq, h, [QI(0)] + [QI(a1[i], -h * a2[i]) for i in range(3)]))
    u = [_spinor(kk) for kk in k]
    Jm = {(j, l): _cur(u[j], u[l]) for j in range(4) for l in range(4) if SPECIES[j] == SPECIES[l]}
    terms = []
    for (j, l), J in Jm.items():
        if j == l:
            continue
        dk = [k[j][i] - k[l][i] for i in range(1, 4)]
        gaJ = GA.add(*[GA.mul(_qmv(J[mu]), GA.gen(mu), S4) for mu in range(4) if J[mu] != QI(0)])
        for m, (qq, h, eps) in enumerate(modes):
            for (kind, sgn) in (("a", 1), ("ad", -1)):
                if dk != [sgn * x for x in qq[1:]]:
                    continue
                pol = eps if kind == "a" else [z.conj() for z in eps]
                if vertex == "component":
                    c = _mdot(J, pol)
                else:
                    gav = GA.add(*[GA.mul(_qmv(z), GA.gen(mu), S4) for mu, z in enumerate(pol) if z != QI(0)])
                    c = _to_q(_proj(GA.mul(gaJ, gav, S4)))
                terms.append((_sm(_qmv(c * QI(Nm)), _sm(TP[j][0], TP[l][1])), (kind, m)))
    H0 = GA.add(*[_scl(F(k[j][0]), _sm(TP[j][0], TP[j][1])) for j in range(4)])
    rho = {"A": {}, "B": {}}
    for (j, l), J in Jm.items():
        if j != l:
            dk = tuple(k[j][i] - k[l][i] for i in range(1, 4))
            rho[SPECIES[j]][dk] = GA.add(rho[SPECIES[j]].get(dk, {}), _sm(_qmv(J[0]), _sm(TP[j][0], TP[l][1])))
    HC = {}
    for p, rA in rho["A"].items():
        mp = tuple(-x for x in p)
        if mp in rho["B"]:
            HC = GA.add(HC, _scl(F(1, Q2), _sm(rA, rho["B"][mp])))
    return dict(k=k, q=q, Q=Q, Qm=[F(Q)] * 4, terms=terms, H0=H0, HC=HC, Jm=Jm, ok=ok)


def _second_order(S, drop=None):
    ini = {(0, 0, 0, 0): _sm(_sm(TP[0][0], TP[1][0]), VAC)}
    Ei = _energy(S, (0, 0, 0, 0), ini[(0, 0, 0, 0)])
    mid = _apply_terms(S["terms"], ini)
    mid2 = {}
    for e, Y in mid.items():
        if drop == "helicity" and e.index(1) in (1, 3):
            continue
        mid2[e] = _scl(1 / (Ei - _energy(S, e, Y)), Y)
    out = _apply_terms(S["terms"], mid2)
    if drop != "coulomb":
        out = _s_add(out, _s_apply(S["HC"], None, ini))
    Yf = out.get((0, 0, 0, 0), {})
    Ff, Fi = _sm(TP[2][0], TP[3][0]), _sm(TP[0][0], TP[1][0])
    br = lambda Fx, Y: _coeff(_sm(_sm(VAC, _star(Fx, SPACE)), Y), VAC)
    z = br(Ff, Yf) * QI(1 / br(Ff, _sm(Ff, VAC)).re)
    zi = br(Fi, Yf) * QI(1 / br(Fi, ini[(0, 0, 0, 0)]).re)
    rest = GA.sub(GA.sub(Yf, _sm(_qmv(z), _sm(Ff, VAC))), _sm(_qmv(zi), ini[(0, 0, 0, 0)]))
    return z, mid, GA.is_zero(rest)


def _cov(S):
    JA, JB = S["Jm"][(2, 0)], S["Jm"][(3, 1)]
    t = F(S["q"][0]) ** 2 - F(S["Q"]) ** 2
    return _mdot(JA, JB) * QI(-1 / t)


def check_vertex_self_adjoint_and_charge_conserving():
    premise("field-theory.fock-space-maxwell-modes")
    ok = True
    QA = GA.add(_sm(TP[0][0], TP[0][1]), _sm(TP[2][0], TP[2][1]))
    QB = GA.add(_sm(TP[1][0], TP[1][1]), _sm(TP[3][0], TP[3][1]))
    for cfg in CONFIGS[::2]:
        S, S2 = _build(cfg), _build(cfg, "ga")
        ok = ok and S["ok"] and _same_operator(S["terms"], _adjoint_terms(S["terms"]))
        ok = ok and _same_operator(S2["terms"], _adjoint_terms(S2["terms"])) and GA.eq(S["HC"], _star(S["HC"], SPACE))
        ok = ok and all(GA.eq(_sm(X, QA), _sm(QA, X)) and GA.eq(_sm(X, QB), _sm(QB, X)) for (X, op) in S["terms"])
    GA.check("H_int (both vertices) and H_C are self-adjoint; vertex terms conserve Q_A and Q_B", ok)
    return ok


def check_second_order_amplitude_distinguishable():
    premise("field-theory.fock-space-maxwell-modes")
    premise("field-theory.imported-standard-field-theory")
    ok = True
    for cfg in CONFIGS:
        S = _build(cfg)
        z, mid, along = _second_order(S)
        cov = _cov(S)
        ok = ok and z == cov and cov != QI(0) and along
        # intermediate states: A1 -> A3 emits q, B2 -> B4 emits -q, each in two helicities: four one-photon states
        ok = ok and len(mid) == 4 and all(sum(e) == 1 for e in mid)
    GA.check("second order on the coupled space gives -J_A(3,1).J_B(4,2)/t at nine configurations", ok)
    return ok


def check_coulomb_term_and_both_helicities_needed():
    premise("field-theory.fock-space-maxwell-modes")
    premise("field-theory.imported-standard-field-theory")
    ok = True
    for cfg in CONFIGS[::3]:
        S = _build(cfg)
        cov = _cov(S)
        ok = ok and _second_order(S)[0] == cov
        for drop in ("coulomb", "helicity"):
            ok = ok and _second_order(S, drop)[0] != cov
    GA.check("dropping the Coulomb operator or one helicity changes the amplitude (three configurations)", ok)
    return ok


def check_ga_product_vertex_same_amplitude():
    premise("field-theory.fock-space-maxwell-modes")
    ok = True
    swap = {0: 1, 1: 0, 2: 3, 3: 2}
    for cfg in CONFIGS[:5]:
        S, S2 = _build(cfg), _build(cfg, "ga")
        z1, m1, _ = _second_order(S)
        z2, m2, _ = _second_order(S2)
        ok = ok and z2 == z1 == _cov(S)
        for e, Y in m1.items():
            e2 = tuple(1 if i == swap[e.index(1)] else 0 for i in range(4))
            ok = ok and e2 in m2 and GA.eq(m2[e2], Y)
    GA.check("the GA-product vertex gives the same amplitude with the helicity label swapped", ok)
    return ok


def _build_same(k):
    qs = []
    for (a, b) in ((0, 2), (0, 3)):
        p = [k[a][i] - k[b][i] for i in range(4)]
        qs += [p, [-x for x in p]]
    modes = []
    good = True
    for p in qs:
        Q2 = p[1] ** 2 + p[2] ** 2 + p[3] ** 2
        Q = _isqrt(Q2)
        good = good and Q * Q == Q2
        t1, t2 = _frame([F(x, Q) for x in p[1:]])
        for h in (1, -1):
            modes.append((p, Q, [QI(0)] + [QI(t1[i], -h * t2[i]) for i in range(3)]))
    u = [_spinor(kk) for kk in k]
    Jm = {(j, l): _cur(u[j], u[l]) for j in range(4) for l in range(4)}
    terms = []
    for (j, l), J in Jm.items():
        if j == l:
            continue
        dk = [k[j][i] - k[l][i] for i in range(1, 4)]
        for m, (p, Q, eps) in enumerate(modes):
            for (kind, sgn) in (("a", 1), ("ad", -1)):
                if dk == [sgn * x for x in p[1:]]:
                    c = _mdot(J, eps if kind == "a" else [z.conj() for z in eps])
                    terms.append((_sm(_qmv(c), _sm(TP[j][0], TP[l][1])), (kind, m)))
    rho = {}
    for (j, l), J in Jm.items():
        if j != l:
            p = tuple(k[j][i] - k[l][i] for i in range(1, 4))
            rho[p] = GA.add(rho.get(p, {}), _sm(_qmv(J[0]), _sm(TP[j][0], TP[l][1])))
    HC = {}
    for p, r in rho.items():
        mp = tuple(-x for x in p)
        if mp in rho:
            HC = GA.add(HC, _scl(F(1, 2) / sum(x * x for x in p), _sm(r, rho[mp])))
    H0 = GA.add(*[_scl(F(k[j][0]), _sm(TP[j][0], TP[j][1])) for j in range(4)])
    return dict(k=k, modes=modes, terms=terms, H0=H0, HC=HC, Jm=Jm, Qm=[F(md[1]) for md in modes], ok=good)


def check_identical_fermions_exchange_sign():
    premise("field-theory.fock-space-maxwell-modes")
    premise("field-theory.imported-standard-field-theory")
    ok = True
    for cfg in C4CONF:
        S = _build_same(list(cfg))
        k = S["k"]
        ok = ok and S["ok"] and _same_operator(S["terms"], _adjoint_terms(S["terms"]))
        ok = ok and GA.eq(S["HC"], _star(S["HC"], SPACE))
        e0 = (0,) * 8
        ini = {e0: _sm(_sm(TP[0][0], TP[1][0]), VAC)}
        Ff = _sm(TP[2][0], TP[3][0])
        Ei = _energy(S, e0, ini[e0])
        mid = _apply_terms(S["terms"], ini)
        mid2 = {e: _scl(F(1, 4 * S["modes"][e.index(1)][1]) / (Ei - _energy(S, e, Y)), Y) for e, Y in mid.items()}
        out = _s_add(_apply_terms(S["terms"], mid2), _s_apply(S["HC"], None, ini))
        z = _coeff(_sm(_sm(VAC, _star(Ff, SPACE)), out.get(e0, {})), VAC)
        z = z * QI(1 / _coeff(_sm(_sm(VAC, _star(Ff, SPACE)), _sm(Ff, VAC)), VAC).re)
        J31, J42, J41, J32 = S["Jm"][(2, 0)], S["Jm"][(3, 1)], S["Jm"][(3, 0)], S["Jm"][(2, 1)]
        q = [k[0][i] - k[2][i] for i in range(4)]
        qp = [k[0][i] - k[3][i] for i in range(4)]
        t = F(q[0] ** 2 - q[1] ** 2 - q[2] ** 2 - q[3] ** 2)
        uu = F(qp[0] ** 2 - qp[1] ** 2 - qp[2] ** 2 - qp[3] ** 2)
        direct, exch = _mdot(J31, J42) * QI(-1 / t), _mdot(J41, J32) * QI(-1 / uu)
        ok = ok and z == direct - exch and direct != QI(0) and exch != QI(0) and z != direct + exch
    GA.check("identical fermions: -(J31.J42/t - J41.J32/u), not the bosonic sum, at four configurations", ok)
    return ok
