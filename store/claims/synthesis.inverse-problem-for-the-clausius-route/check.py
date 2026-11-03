"""Inverse variational problem for the Clausius route: exact checks.

Signature (1,3), eta = diag(1,-1,-1,-1), vectors of Cl(1,3) (lib/GA.py) give the momentum p of a
principal symbol (d_a -> p_a for every derivative; one convention throughout, so second-order symbols are
even in p and the adjoint of a first-order symbol is P(-p)^T). A symmetric tensor h (perturbation of the
derived metric, h_ab = delta g_ab) is a 4x4 rational matrix; the pairing is <k, h> = eta^ac eta^bd k_ab h_cd.
Lorentz-covariant second-order linear symbols on h span five terms
  A1 = p_a p_b tr h, A2 = eta_ab (p.h.p), A3 = eta_ab p^2 tr h, A4 = p^2 h_ab, A5 = p_a (hp)_b + p_b (hp)_a.
The linearised Riemann tensor (sphere-positive convention) is
  R_abcd = 1/2 (p_b p_c h_ad + p_a p_d h_bc - p_a p_c h_bd - p_b p_d h_ac),
its Ricci and Einstein symbols are computed from it and expressed in the A-basis.
(1) Helmholtz (self-adjoint Frechet derivative; for the principal symbol, symmetry of <k, E(p) h>):
    self-adjoint subspace dim 4; the Einstein symbol passes; the multiplier family
    M_beta(S) = S + beta tr(S) eta applied to it fails for every beta != 0, the asymmetry being beta times a
    fixed nonzero form; beta = -1/2 is the route's emitted form (Ricci), beta = -1/4 the Lambda-free
    trace-free form. Algebraic identity: M_{-1/2}(G + Lambda + k T) = Ric + k T - (Lambda + k tau/2) eta.
(2) The trace-free (Lambda-free) form passes on trace-free h, k (unimodular variations) and not on all;
    M_{-1/4} has rank 9 (kernel the trace). De Sitter curvatures at every Lambda' solve the trace-free form;
    the Einstein form with Lambda = 3 Q(I), I = ninf + (Lambda/6) n0 the frozen point in Cl(2,4), is
    solved only at Lambda' = Lambda.
(3) Linearised Lovelock: transverse (p^a E_ab = 0 for all h, the Noether identity the route's Bianchi
    step uses) dim 2; transverse and self-adjoint dim 1, spanned by the Einstein symbol.
(4) Matter, scalar field psi, Lagrangian sqrt(g)(1/2 g^ab d_a psi d_b psi - V(psi)) - 1/2 xi psi^2 sqrt(g) R,
    at the flat background: cross Helmholtz condition <k, K(p)> = L(-p)[k], K the psi-derivative of the
    metric Euler-Lagrange expression (the source), L the metric derivative of the matter equation.
    Minimal (background gradient u, V' = v1 constant) and nonminimal (constant background s) pass with the
    Hilbert stress; a source with an altered trace term, or the minimal stress with the xi-matter equation,
    fail.
(5) Field variable: for the reparametrised field psi with delta g = M_beta(delta psi) (beta != -1/4), the
    psi-derivative of M_beta(G) has symbol M_beta sigma(G) M_beta, self-adjoint for every sample beta; the
    Ricci form is of this kind for beta = -1/2. So (1) is a statement about the metric as the varied field.
(6) At the flat background the Euler density E4 = Riem.Riem - 4 Ric.Ric + R^2 has zero second variation
    (no field equations to second order), while the Weyl square Riem.Riem - 2 Ric.Ric + R^2/3 has second
    variation 2 Ric.Ric - (2/3) R^2, nonzero and fourth order in p (the linearised Bach operator).
Exact arithmetic only (Fractions); fixed sample tables, no randomness.
"""
from fractions import Fraction as Fr

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1)
ETA = (1, -1, -1, -1)
R4 = range(4)
S6 = (1, -1, -1, -1, 1, -1)


def _vec(cs):
    return GA.add(*[GA.scal(Fr(c), GA.gen(i)) for i, c in enumerate(cs)])


def _low(v):
    return [GA.dot(v, GA.gen(a), SQ) for a in R4]


MOMENTA = [_low(_vec(c)) for c in [(3, 1, -2, 5), (Fr(1, 2), 2, 3, -1)]]
U_BG = [Fr(2), Fr(-1), Fr(1, 3), Fr(3)]
V1_BG = Fr(5, 4)
S_BG = Fr(-3, 2)
XI = Fr(1, 6)
LAMS = (Fr(3), Fr(-6, 5))


def _e(a, b):
    return Fr(ETA[a]) if a == b else Fr(0)


def _tr(h):
    return sum(ETA[a] * h[a][a] for a in R4)


def _pair(k, h):
    return sum(ETA[a] * ETA[b] * k[a][b] * h[a][b] for a in R4 for b in R4)


def _up(p):
    return [ETA[a] * p[a] for a in R4]


def _hp(h, p):
    q = _up(p)
    return [sum(h[b][c] * q[c] for c in R4) for b in R4]


def _php(h, p):
    v, q = _hp(h, p), _up(p)
    return sum(q[b] * v[b] for b in R4)


def _psq(p):
    q = _up(p)
    return sum(q[a] * p[a] for a in R4)


def _A(i, h, p):
    t, P2, x, v = _tr(h), _psq(p), _php(h, p), _hp(h, p)
    terms = (lambda a, b: p[a] * p[b] * t, lambda a, b: _e(a, b) * x, lambda a, b: _e(a, b) * P2 * t,
             lambda a, b: P2 * h[a][b], lambda a, b: p[a] * v[b] + p[b] * v[a])
    return [[terms[i](a, b) for b in R4] for a in R4]


def _lin(c, h, p):
    out = [[Fr(0)] * 4 for _ in R4]
    for i, ci in enumerate(c):
        if ci:
            Ai = _A(i, h, p)
            out = [[out[a][b] + ci * Ai[a][b] for b in R4] for a in R4]
    return out


def _symbasis():
    out = []
    for a in R4:
        for b in range(a, 4):
            m = [[Fr(0)] * 4 for _ in R4]
            m[a][b] = m[b][a] = Fr(1)
            out.append(m)
    return out


SB = _symbasis()


def _traceless(m):
    t = _tr(m)
    return [[m[a][b] - t / 4 * _e(a, b) for b in R4] for a in R4]


TL = [_traceless(m) for m in SB[:-1]]


def _riem(h, p):
    return {(a, b, c, d): (p[b] * p[c] * h[a][d] + p[a] * p[d] * h[b][c]
                           - p[a] * p[c] * h[b][d] - p[b] * p[d] * h[a][c]) / 2
            for a in R4 for b in R4 for c in R4 for d in R4}


def _ric(h, p):
    R = _riem(h, p)
    return [[sum(ETA[a] * R[a, b, a, d] for a in R4) for d in R4] for b in R4]


def _ein(h, p):
    Ric = _ric(h, p)
    s = _tr(Ric)
    return [[Ric[a][b] - s / 2 * _e(a, b) for b in R4] for a in R4]


def _mult(beta, S):
    t = _tr(S)
    return [[S[a][b] + beta * t * _e(a, b) for b in R4] for a in R4]


def _nullspace(rows, n):
    m = [list(r) for r in rows]
    piv, row = [], 0
    for col in range(n):
        r0 = next((r for r in range(row, len(m)) if m[r][col] != 0), None)
        if r0 is None:
            continue
        m[row], m[r0] = m[r0], m[row]
        pv = m[row][col]
        m[row] = [x / pv for x in m[row]]
        for r in range(len(m)):
            if r != row and m[r][col] != 0:
                f = m[r][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[row])]
        piv.append(col)
        row += 1
    basis = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -m[i][fc]
        basis.append(v)
    return basis


def _coeffs(fn):
    """Coefficients of the symbol fn(h, p) in the A-basis (exists and is unique, else raises)."""
    rows = []
    for p in MOMENTA:
        for h in SB:
            Es, E = [_A(i, h, p) for i in range(5)], fn(h, p)
            rows.extend([Es[i][a][b] for i in range(5)] + [E[a][b]] for a in R4 for b in R4)
    ns = _nullspace(rows, 6)
    if len(ns) != 1 or ns[0][5] == 0:
        raise ValueError("symbol is not in the span of the five covariant terms")
    return [-x / ns[0][5] for x in ns[0][:5]]


def _selfadj_rows(space):
    return [[_pair(k, _A(i, h, p)) - _pair(h, _A(i, k, p)) for i in range(5)]
            for p in MOMENTA for k in space for h in space]


def _transverse_rows():
    rows = []
    for p in MOMENTA:
        q = _up(p)
        for h in SB:
            Es = [_A(i, h, p) for i in range(5)]
            rows.extend([sum(q[a] * Es[i][a][b] for a in R4) for i in range(5)] for b in R4)
    return rows


def _asym(c, space):
    return [_pair(k, _lin(c, h, p)) - _pair(h, _lin(c, k, p)) for p in MOMENTA for k in space for h in space]


def _asym_fn(fn, space):
    return [_pair(k, fn(h, p)) - _pair(h, fn(k, p)) for p in MOMENTA for k in space for h in space]


def _quad(h, k, p, w):
    """Quadratic part of w[0] Riem.Riem + w[1] Ric.Ric + w[2] R^2 at the flat background, as a bilinear
    form in (h, k) at momentum p (indices raised with eta)."""
    Rh, Rk, Ch, Ck = _riem(h, p), _riem(k, p), _ric(h, p), _ric(k, p)
    r4 = sum(ETA[a] * ETA[b] * ETA[c] * ETA[d] * Rh[a, b, c, d] * Rk[a, b, c, d]
             for a in R4 for b in R4 for c in R4 for d in R4)
    return w[0] * r4 + w[1] * _pair(Ch, Ck) + w[2] * _tr(Ch) * _tr(Ck)


SAMPLE_RIC = [[Fr(2), Fr(1, 3), Fr(0), Fr(3)], [Fr(1, 3), Fr(-1), Fr(5, 2), Fr(0)],
              [Fr(0), Fr(5, 2), Fr(1, 2), Fr(1)], [Fr(3), Fr(0), Fr(1), Fr(-7, 4)]]
SAMPLE_T = [[Fr(3), Fr(1, 2), Fr(0), Fr(0)], [Fr(1, 2), Fr(1), Fr(0), Fr(0)],
            [Fr(0), Fr(0), Fr(2, 3), Fr(1, 4)], [Fr(0), Fr(0), Fr(1, 4), Fr(-1)]]
K_COUPLING = Fr(7, 3)
REP_BETAS = (Fr(-1, 2), Fr(3, 7), Fr(-2))


def check_helmholtz_in_the_metric_selects_the_einstein_form():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    sa = _nullspace(_selfadj_rows(SB), 5)
    GA.check("self-adjoint covariant second-order symbols: dimension 4 of 5", len(sa) == 4)
    cG, cRic = _coeffs(_ein), _coeffs(_ric)
    GA.check("Einstein symbol = -1/2 (A1 + A2 - A3 + A4 - A5)",
             cG == [Fr(-1, 2), Fr(-1, 2), Fr(1, 2), Fr(-1, 2), Fr(1, 2)])
    GA.check("Ricci symbol = -1/2 (A1 + A4 - A5)", cRic == [Fr(-1, 2), Fr(0), Fr(0), Fr(-1, 2), Fr(1, 2)])
    GA.check("the Einstein form passes Helmholtz", not any(_asym(cG, SB)))
    GA.check("the route's emitted (Ricci) form fails Helmholtz", any(_asym(cRic, SB)))
    GA.check("route's form = M_{-1/2}(Einstein form) on symbols",
             _coeffs(lambda h, p: _mult(Fr(-1, 2), _ein(h, p))) == cRic)
    base = _asym(_coeffs(lambda h, p: _mult(Fr(1), _ein(h, p))), SB)
    base0 = _asym(cG, SB)
    lin_in_beta = True
    for beta in (Fr(-1, 2), Fr(-1, 4), Fr(3, 7)):
        cb = _coeffs(lambda h, p: _mult(beta, _ein(h, p)))
        ab = _asym(cb, SB)
        lin_in_beta = lin_in_beta and ab == [x0 + beta * (x - x0) for x, x0 in zip(base, base0)]
        lin_in_beta = lin_in_beta and any(ab)
    GA.check("asymmetry of M_beta(Einstein) is beta times a fixed nonzero form", lin_in_beta and any(base))
    rep_ok = True
    for beta in REP_BETAS:
        rep_ok = rep_ok and not any(_asym_fn(lambda h, p: _mult(beta, _ein(_mult(beta, h), p)), SB))
    GA.check("for the reparametrised field (delta g = M_beta delta psi) M_beta(Einstein) passes", rep_ok)
    GA.check("in that field the Ricci form's symbol is M_{-1/2} sigma(G) M_{-1/2}",
             all(_ric(_mult(Fr(-1, 2), h), p) == _mult(Fr(-1, 2), _ein(_mult(Fr(-1, 2), h), p))
                 for p in MOMENTA for h in SB))
    Ric, T, L, k = SAMPLE_RIC, SAMPLE_T, LAMS[0], K_COUPLING
    s, tau = _tr(Ric), _tr(T)
    Gp = [[Ric[a][b] - s / 2 * _e(a, b) + L * _e(a, b) + k * T[a][b] for b in R4] for a in R4]
    route = [[Ric[a][b] + k * T[a][b] - (L + k * tau / 2) * _e(a, b) for b in R4] for a in R4]
    GA.check("algebraic: M_{-1/2}(G + Lambda + kT) = Ric + kT - (Lambda + k tau/2) eta",
             _mult(Fr(-1, 2), Gp) == route)
    assert not GA.FAILURES


def check_lambda_free_form_needs_unimodular_variations():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    premise("dark-energy.imported-henneaux-teitelboim-promotion")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("synthesis.einstein-route-makes-n-initial-data")
    premise("synthesis.promoted-norm-one-global-pair")
    cTF = _coeffs(lambda h, p: _mult(Fr(-1, 4), _ein(h, p)))
    GA.check("trace-free form symbol = -1/2 A1 - 1/4 A2 + 1/4 A3 - 1/2 A4 + 1/2 A5",
             cTF == [Fr(-1, 2), Fr(-1, 4), Fr(1, 4), Fr(-1, 2), Fr(1, 2)])
    GA.check("trace-free form fails Helmholtz on all variations", any(_asym(cTF, SB)))
    GA.check("trace-free variations span 9 dimensions",
             GA.rank_of_vectors([[m[a][b] for a in R4 for b in R4] for m in TL]) == 9)
    GA.check("trace-free form passes Helmholtz on trace-free (unimodular) variations", not any(_asym(cTF, TL)))
    GA.check("M_{-1/4} has rank 9 (it drops the trace, and Lambda with it)",
             GA.rank_of_vectors([[x for r in _mult(Fr(-1, 4), m) for x in r] for m in SB]) == 9)
    E = [GA.gen(i) for i in range(6)]
    n0 = GA.scal(Fr(1, 2), GA.add(E[4], E[5]))
    ninf = GA.sub(E[4], E[5])
    ok = True
    for L in LAMS:
        I = GA.add(ninf, GA.scal(L / 6, n0))
        QI = GA.mul(I, I, S6).get((), Fr(0))
        ok = ok and QI == L / 3
        Lfp = 3 * QI
        for Lp in (L, L + 1, -L):
            ric = [[Lp * _e(a, b) for b in R4] for a in R4]
            s = _tr(ric)
            ein_form = [[ric[a][b] - s / 2 * _e(a, b) + Lfp * _e(a, b) for b in R4] for a in R4]
            tf_form = [[ric[a][b] - s / 4 * _e(a, b) for b in R4] for a in R4]
            ok = ok and not any(x for r in tf_form for x in r)
            ok = ok and (not any(x for r in ein_form for x in r)) == (Lp == L)
    GA.check("de Sitter fields of every Lambda' solve the Lambda-free form; the Einstein form with "
             "Lambda = 3 Q(I) only Lambda' = Lambda", ok)
    assert not GA.FAILURES


def check_linearised_lovelock_is_one_line():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    tv = _nullspace(_transverse_rows(), 5)
    GA.check("transverse covariant second-order symbols: dimension 2", len(tv) == 2)
    both = _nullspace(_selfadj_rows(SB) + _transverse_rows(), 5)
    GA.check("transverse and self-adjoint: dimension 1", len(both) == 1)
    cG = _coeffs(_ein)
    GA.check("the line is the Einstein symbol",
             all(x * cG[0] == y * both[0][0] for x, y in zip(both[0], cG)) and cG[0] != 0)
    odd = [Fr(1), Fr(0), Fr(-1), Fr(0), Fr(0)]
    GA.check("the transverse plane is spanned by the Einstein symbol and (p p - p^2 eta) tr h",
             GA.rank_of_vectors(tv + [odd, cG]) == 2)
    trans_ok = all(sum(r[i] * odd[i] for i in range(5)) == 0 for r in _transverse_rows())
    GA.check("(p p - p^2 eta) tr h: transverse", trans_ok and any(_asym(odd, SB)))
    assert not GA.FAILURES


def check_matter_cross_helmholtz_forces_the_hilbert_stress():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    premise("synthesis.imported-einstein-cartan-matter-coupling")
    u, v1, s, xi = U_BG, V1_BG, S_BG, XI
    uu = _up(u)
    results = {}
    for name, lam, xs, xm in (("minimal", 0, 0, 0), ("trace-altered", 1, 0, 0),
                              ("nonminimal", 0, 1, 1), ("xi only in matter", 0, 0, 1)):
        ok = True
        for p in MOMENTA:
            q = _up(p)
            up = sum(uu[a] * p[a] for a in R4)
            P2 = _psq(p)
            for k in SB:
                trk = _tr(k)
                ukp = sum(uu[c] * k[c][d] * q[d] for c in R4 for d in R4)
                pkp = _php(k, p)
                # source side: <k, D_psi E_g>, E_g = -1/2 sqrt(g) T_H (+ xi improvement), minimal part
                # at background gradient u, improvement part at constant background s
                lhs = Fr(1, 2) * trk * (up - v1) - ukp - lam * Fr(1, 2) * trk * up
                lhs += xs * xi * s * (P2 * trk - pkp)
                # matter side at -p: D_g E_psi[k], E_psi = -d(sqrt(g) g^ab d psi) - sqrt(g) V' - xi psi sqrt(g) R
                rhs = -(Fr(1, 2) * (-up) * trk + ukp) - Fr(1, 2) * v1 * trk
                rhs += -xm * xi * s * (pkp - P2 * trk)
                ok = ok and lhs == rhs
        results[name] = ok
    GA.check("minimal coupling: source = Hilbert stress passes", results["minimal"])
    GA.check("altered trace term in the source fails", not results["trace-altered"])
    GA.check("nonminimal: improved Hilbert stress with xi R psi passes", results["nonminimal"])
    GA.check("minimal stress with the xi-matter equation fails", not results["xi only in matter"])
    assert not GA.FAILURES


def check_euler_density_is_invisible_and_weyl_square_is_fourth_order():
    premise("synthesis.euler-term-horizon-entropy-shift")
    ok_e4, ok_pert, ok_w2, ok_scale = True, True, True, True
    for p in MOMENTA:
        p2 = [2 * x for x in p]
        for k in SB:
            for h in SB:
                ok_e4 = ok_e4 and _quad(h, k, p, (1, -4, 1)) == 0
                ok_pert = ok_pert and _quad(h, k, p, (1, -4, 2)) == _quad(h, k, p, (0, 0, 1))
                w = _quad(h, k, p, (1, -2, Fr(1, 3)))
                ok_w2 = ok_w2 and w == _quad(h, k, p, (0, 2, Fr(-2, 3)))
                ok_scale = ok_scale and _quad(h, k, p2, (1, -2, Fr(1, 3))) == 16 * w
    GA.check("the Euler density E4 has zero second variation at the flat background", ok_e4)
    GA.check("E4 + R^2 has the second variation of R^2 alone", ok_pert)
    GA.check("Weyl squared: second variation 2 Ric.Ric - (2/3) R^2, nonzero, fourth order in p",
             ok_w2 and ok_scale and any(_quad(h, k, MOMENTA[1], (0, 2, Fr(-2, 3))) for k in SB for h in SB))
    assert not GA.FAILURES
