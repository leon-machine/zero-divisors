"""No principle on the scale alone selects the almost-Einstein scales: exact checks.

Cl(2,4) as in the stored conformal-energy result: e0 (+1), e1, e2, e3 (-1), nu (+1), e- (-1); n_inf = nu + e-,
n0 = (nu - e-)/2, X(x) = n0 + x - Q(x)/2 n_inf, Z = e0 nu. A constant tractor I gives the scale sigma = <X(x), I>
of the flat class (parallel tractors of the flat connection), with Q(I) = Lambda/3 for the normalisation of
the stored de Sitter tractor n_inf + (L/6) n0.
(1) Symmetry of the positive structure: the vectors commuting with Z are exactly span(e1, e2, e3, e-) (negative
    definite: Q(I) < 0, Lambda < 0 scales); the vectors fixed by the six bivectors of that span are exactly
    span(e0, nu) (positive definite: de Sitter scales), on which the rotor 1 + tZ acts by the Cayley rotation;
    the centraliser u(1) + so(4) of Z (seven bivectors, all commuting with Z) fixes no nonzero vector; a null I
    (Lambda = 0, e.g. n_inf) lies in neither span. Tabulated scales: I = nu gives (1 - Q)/2 (de Sitter, L = 12),
    I = e0 gives t, I = e- gives (1 + Q)/2 (anti de Sitter).
(2) Yamabe obstruction: for g = phi^2 eta (phi = 1/sigma) the Ricci tensor computed exactly from the Christoffel
    symbols at rational points satisfies sqrt|g| R = -6 phi box phi, so the Einstein-Hilbert action restricted to
    the class is int (6 eta(d phi, d phi) - 2 Lambda phi^4), with the single Euler-Lagrange equation
    box phi = -(2/3) Lambda phi^3 (the trace R = 4 Lambda). Counter-model phi = 1 + x1 x2 (Lambda = 0): box phi = 0,
    so R = 0 everywhere, while the trace-free Ricci tensor is nonzero at every sample point: a stationary scale
    that is not almost-Einstein.
(3) Tractor Dirichlet functional S[sigma] = int H0 : H0, H0 the trace-free Hessian (the middle slot of the
    derivative of D sigma in the flat splitting): Euler-Lagrange equation (3/2) box^2 sigma = 0; sigma = 1 + x1 x2
    is stationary with H0 != 0; sigma = (t + x1)^2 has H0 = 2 l l (l null) != 0 and H0 : H0 = 0, so in Lorentzian
    signature even a vanishing action does not force parallelism.
Controls: a perturbed Z, phi = 1 + x1^2 (box phi != 0), sigma = 1 - Q(x)/2 (almost-Einstein, H0 = 0).
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
NU, EM = E[4], E[5]
NINF = GA.add(NU, EM)
N0 = GA.scal(F(1, 2), GA.sub(NU, EM))
Z = GA.mul(E[0], NU, SQ)
ETA = (1, -1, -1, -1)


def _comm(A, B):
    return GA.sub(GA.mul(A, B, SQ), GA.mul(B, A, SQ))


def _vec_coords(v):
    return [v.get((i,), F(0)) for i in range(6)]


def _kernel_dim_on_vectors(bivs):
    """dimension of {v : [B, v] = 0 for all B in bivs}."""
    rows = []
    for B in bivs:
        cols = [_vec_coords(_comm(B, E[i])) for i in range(6)]
        for r in range(6):
            rows.append([cols[i][r] for i in range(6)])
    return 6 - GA.mat_rank(rows)


def _X(x):
    xv = GA.add(*[GA.scal(x[i], E[i]) for i in range(4)])
    Q = sum(ETA[i] * x[i] ** 2 for i in range(4))
    return GA.add(N0, xv, GA.scal(-F(1, 2) * Q, NINF)), Q


def check_positive_structure_symmetry_fixes_no_scale():
    premise("synthesis.positive-conformal-energy-gives-positive-null-translations")
    premise("synthesis.positive-structure-is-twistor-form-at-imaginary-time")
    premise("synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale")
    comp = [1, 2, 3, 5]
    so4 = [GA.mul(E[i], E[j], SQ) for i in comp for j in comp if i < j]
    GA.check("the so(4) bivectors commute with Z", all(GA.is_zero(_comm(B, Z)) for B in so4))
    # vectors commuting with Z: exactly the complement
    GA.check("Z fixes a 4-dim space of vectors", _kernel_dim_on_vectors([Z]) == 4)
    GA.check("each of e1, e2, e3, e- commutes with Z", all(GA.is_zero(_comm(Z, E[i])) for i in comp))
    GA.check("the complement is negative definite", all(SQ[i] == -1 for i in comp))
    GA.check("so(4) fixes a 2-dim space", _kernel_dim_on_vectors(so4) == 2)
    GA.check("e0, nu are fixed by so(4)", all(GA.is_zero(_comm(B, E[i])) for B in so4 for i in (0, 4)))
    GA.check("the plane is positive definite", SQ[0] == 1 and SQ[4] == 1)
    GA.check("the centraliser fixes no nonzero vector", _kernel_dim_on_vectors([Z] + so4) == 0)
    GA.check("control: e1 e2 alone fixes four vectors", _kernel_dim_on_vectors([GA.mul(E[1], E[2], SQ)]) == 4)
    Zbad = GA.add(Z, GA.mul(E[0], E[1], SQ))
    GA.check("control: a perturbed Z does not commute with so(4)",
             not all(GA.is_zero(_comm(B, Zbad)) for B in so4))
    # the U(1) of Z rotates the plane: R = 1 + t Z, R R~ = 1 + t^2, R nu R~ = (1 - t^2) nu + 2t(...) e0
    for t in (F(1, 2), F(3), F(-2, 7)):
        R = GA.add(GA.sc(1), GA.scal(t, Z))
        img = GA.mul(GA.mul(R, NU, SQ), GA.reverse(R), SQ)
        GA.check("R R~ = 1 + t^2", GA.eq(GA.mul(R, GA.reverse(R), SQ), GA.sc(1 + t ** 2)))
        c = _vec_coords(img)
        GA.check("U(1) keeps nu in the plane with unchanged norm",
                 c[1] == c[2] == c[3] == c[5] == 0 and c[0] ** 2 + c[4] ** 2 == (1 + t ** 2) ** 2 and c[0] != 0)
    # a boost K = e0 e1 (a datum outside the structure): the vectors fixed by K and by the so(4) are the ray of nu
    K = GA.mul(E[0], E[1], SQ)
    GA.check("K and so(4) together fix a 1-dim space", _kernel_dim_on_vectors([K] + so4) == 1)
    GA.check("that space is the ray of nu", GA.is_zero(_comm(K, NU)) and not GA.is_zero(_comm(K, E[0])))
    # tube point i rho e0: Re X = n0 + (rho^2/2) n_inf, Im X = rho e0; the boost-fixed vector of the positive
    # plane is proportional to the de Sitter tractor I_L = n_inf + (L/6) n0 with L = 12/rho^2
    for rho in (F(1), F(2), F(1, 3), F(5, 2)):
        reX = GA.add(N0, GA.scal(rho ** 2 / 2, NINF))
        L = 12 / rho ** 2
        IL = GA.add(NINF, GA.scal(L / 6, N0))
        GA.check("Re X(i rho e0) is the de Sitter tractor at L = 12/rho^2 (rho=%s)" % rho,
                 GA.eq(GA.scal(2 / rho ** 2, reX), IL))
        GA.check("Q(Re X) = rho^2 > 0, orthogonal to Im X, fixed by K",
                 GA.dot(reX, reX, SQ) == rho ** 2 and GA.dot(reX, E[0], SQ) == 0 and GA.is_zero(_comm(K, reX)))
    # null tractor (Minkowski scale) lies in neither span
    nc = _vec_coords(NINF)
    GA.check("n_inf is null", GA.dot(NINF, NINF, SQ) == 0)
    GA.check("n_inf is not in the plane nor in the complement",
             any(nc[i] != 0 for i in (0, 4)) and any(nc[i] != 0 for i in comp))
    # tabulated scales sigma = <X(x), I>
    for x in ((F(1, 2), F(1, 3), F(0), F(2)), (F(3), F(-1), F(1, 4), F(0))):
        Xx, Q = _X(x)
        GA.check("I = nu: sigma = (1 - Q)/2", GA.dot(Xx, NU, SQ) == (1 - Q) / 2)
        GA.check("I = e0: sigma = t", GA.dot(Xx, E[0], SQ) == x[0])
        GA.check("I = e-: sigma = (1 + Q)/2", GA.dot(Xx, EM, SQ) == (1 + Q) / 2)
        L = F(12)
        GA.check("nu is the de Sitter tractor at L = 12 up to the factor 1/2",
                 GA.eq(GA.scal(F(1, 2), GA.add(NINF, GA.scal(L / 6, N0))), NU))
    return True


# ---------------------------------------------------------------- polynomials in (t, x1, x2, x3)
def _pd(p, i):
    out = {}
    for m, c in p.items():
        if m[i]:
            mm = list(m); mm[i] -= 1
            out[tuple(mm)] = out.get(tuple(mm), F(0)) + c * m[i]
    return {k: v for k, v in out.items() if v != 0}


def _ev(p, x):
    tot = F(0)
    for m, c in p.items():
        term = c
        for i in range(4):
            term *= x[i] ** m[i]
        tot += term
    return tot


def _box(p):
    out = {}
    for i in range(4):
        for k, v in _pd(_pd(p, i), i).items():
            out[k] = out.get(k, F(0)) + ETA[i] * v
    return {k: v for k, v in out.items() if v != 0}


def _poly(terms):
    return {m: F(c) for m, c in terms}


ONE = (0, 0, 0, 0)
BB3 = [((0, 0, 0, 0), F(-96, 7))]


def _ricci_conformal(phi, x):
    """Ricci tensor of g = phi^2 eta at x, from the Christoffel symbols and their derivatives (exact)."""
    f = _ev(phi, x)
    d = [_ev(_pd(phi, a), x) for a in range(4)]
    dd = [[_ev(_pd(_pd(phi, a), b), x) for b in range(4)] for a in range(4)]
    w = [d[a] / f for a in range(4)]                                  # d omega
    ww = [[dd[a][b] / f - d[a] * d[b] / f ** 2 for b in range(4)] for a in range(4)]

    def delta(a, b):
        return 1 if a == b else 0

    def up(c):            # eta^{cd} w_d
        return ETA[c] * w[c]

    G = [[[delta(c, a) * w[b] + delta(c, b) * w[a] - (ETA[a] if a == b else 0) * up(c)
           for b in range(4)] for a in range(4)] for c in range(4)]
    # dG[e][c][a][b] = d_e Gamma^c_ab
    dG = [[[[delta(c, a) * ww[e][b] + delta(c, b) * ww[e][a] - (ETA[a] if a == b else 0) * ETA[c] * ww[e][c]
             for b in range(4)] for a in range(4)] for c in range(4)] for e in range(4)]
    Ric = [[sum(dG[c][c][a][b] for c in range(4)) - sum(dG[b][c][a][c] for c in range(4))
            + sum(G[c][c][dd_] * G[dd_][a][b] for c in range(4) for dd_ in range(4))
            - sum(G[c][b][dd_] * G[dd_][a][c] for c in range(4) for dd_ in range(4))
            for b in range(4)] for a in range(4)]
    return f, Ric


def check_yamabe_stationary_scale_is_not_almost_einstein():
    premise("synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale")
    premise("correspondence.imported-vacuum-equations-scale-tractor")
    premise("synthesis.imported-gtg-dictionary")
    pts = [(F(0), F(0), F(0), F(0)), (F(1, 2), F(1, 3), F(-2, 5), F(1)), (F(-1), F(2), F(1, 7), F(3, 4))]
    phis = {
        "1 + x1 x2": _poly([(ONE, 1), ((0, 1, 1, 0), 1)]),
        "1 + t/3 + x1^2 x3 - x2^2 x3": _poly([(ONE, 1), ((1, 0, 0, 0), F(1, 3)), ((0, 2, 0, 1), 1), ((0, 0, 2, 1), -1)]),
    }
    for name, phi in phis.items():
        GA.check("box phi = 0 for phi = %s" % name, _box(phi) == {})
        for x in pts:
            f, Ric = _ricci_conformal(phi, x)
            Rs = sum(ETA[a] * Ric[a][a] for a in range(4)) / f ** 2           # g^{ab} R_ab
            GA.check("sqrt|g| R = -6 phi box phi (%s, %s)" % (name, x), f ** 4 * Rs == -6 * f * _ev(_box(phi), x))
            GA.check("R = 0: stationary for the class-restricted action at Lambda = 0", Rs == 0)
            tf = [[Ric[a][b] - (Rs * f ** 2 / 4) * (ETA[a] if a == b else 0) for b in range(4)] for a in range(4)]
            GA.check("trace-free Ricci nonzero: not almost-Einstein (%s, %s)" % (name, x),
                     any(tf[a][b] != 0 for a in range(4) for b in range(4)))
    # control: phi = 1 + x1^2 is not harmonic, and the identity still holds with R != 0
    ctrl = _poly([(ONE, 1), ((0, 2, 0, 0), 1)])
    GA.check("control: box(1 + x1^2) != 0", _box(ctrl) != {})
    for x in pts:
        f, Ric = _ricci_conformal(ctrl, x)
        Rs = sum(ETA[a] * Ric[a][a] for a in range(4)) / f ** 2
        GA.check("control identity sqrt|g| R = -6 phi box phi", f ** 4 * Rs == -6 * f * _ev(_box(ctrl), x))
        GA.check("control R != 0", Rs != 0)
    # control: the Einstein scale phi = 1/sigma with sigma = 1 - Q/12 * L ... use the de Sitter phi^2 eta,
    # phi = 1/(1 - Q/12) is not polynomial; instead Minkowski phi = 1 has Ric = 0
    f, Ric = _ricci_conformal(_poly([(ONE, 1)]), pts[1])
    GA.check("control: phi = 1 is flat", all(Ric[a][b] == 0 for a in range(4) for b in range(4)))
    return True


def _hess(p):
    return [[_pd(_pd(p, a), b) for b in range(4)] for a in range(4)]


def _tf_hess_at(p, x):
    H = [[_ev(h, x) for h in row] for row in _hess(p)]
    tr = sum(ETA[a] * H[a][a] for a in range(4))
    return [[H[a][b] - tr / 4 * (ETA[a] if a == b else 0) for b in range(4)] for a in range(4)]


def _contract(H0):
    """H0 : H0 = eta^{ac} eta^{bd} H0_ab H0_cd."""
    return sum(ETA[a] * ETA[b] * H0[a][b] ** 2 for a in range(4) for b in range(4))


def check_tractor_dirichlet_stationary_points_are_not_parallel():
    premise("synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale")
    premise("correspondence.imported-vacuum-equations-scale-tractor")
    pts = [(F(0), F(0), F(0), F(0)), (F(1, 2), F(1, 3), F(-2, 5), F(1)), (F(-1), F(2), F(1, 7), F(3, 4))]
    s1 = _poly([(ONE, 1), ((0, 1, 1, 0), 1)])                              # 1 + x1 x2
    # Euler-Lagrange operator d_a d_b H0^{ab} = box^2 sigma - (1/4) box^2 sigma
    def el(p):
        H = _hess(p)
        out = {}
        for a in range(4):
            for b in range(4):
                term = _pd(_pd(H[a][b], a), b)
                for k, v in term.items():
                    out[k] = out.get(k, F(0)) + ETA[a] * ETA[b] * v
        bb = _box(_box(p))
        for k, v in bb.items():
            out[k] = out.get(k, F(0)) - F(1, 4) * v
        return {k: v for k, v in out.items() if v != 0}
    s3 = _poly([((2, 1, 0, 0), 1), ((0, 3, 0, 0), F(1, 5)), ((1, 1, 1, 1), 2), ((4, 0, 0, 0), F(2, 3)),
                ((0, 2, 2, 0), -3), ((2, 0, 0, 2), F(5, 7)), ((0, 0, 0, 2), -3)])
    bb3 = _box(_box(s3))
    el3 = el(s3)
    GA.check("EL operator is (3/4) box^2 on a generic cubic-quartic",
             set(el3) == set(bb3) and all(el3[k] == F(3, 4) * bb3[k] for k in bb3) and bb3 != {})
    GA.check("1 + x1 x2 is stationary", el(s1) == {})
    GA.check("tabulated box^2 of the quartic", sorted(bb3.items()) == BB3)
    for x in pts:
        H0 = _tf_hess_at(s1, x)
        GA.check("1 + x1 x2 has nonzero trace-free Hessian at %s" % (x,),
                 any(H0[a][b] != 0 for a in range(4) for b in range(4)))
        GA.check("1 + x1 x2: H0 is the (1,2) entry 1 only, H0 : H0 = 2",
                 H0[1][2] == 1 and H0[2][1] == 1 and _contract(H0) == 2
                 and sum(abs(v) for row in H0 for v in row) == 2)
    s2 = _poly([((2, 0, 0, 0), 1), ((1, 1, 0, 0), 2), ((0, 2, 0, 0), 1)])     # (t + x1)^2
    for x in pts:
        H0 = _tf_hess_at(s2, x)
        GA.check("(t + x1)^2: H0 != 0", any(H0[a][b] != 0 for a in range(4) for b in range(4)))
        GA.check("(t + x1)^2: H0 : H0 = 0 (null action density)", _contract(H0) == 0)
    GA.check("(t + x1)^2 is stationary", el(s2) == {})
    # control: the almost-Einstein scale 1 - Q(x)/2 has H0 = 0; a perturbation does not
    ae = _poly([(ONE, 1), ((2, 0, 0, 0), F(-1, 2)), ((0, 2, 0, 0), F(1, 2)), ((0, 0, 2, 0), F(1, 2)),
                ((0, 0, 0, 2), F(1, 2))])
    for x in pts:
        GA.check("control: 1 - Q/2 has H0 = 0", all(v == 0 for row in _tf_hess_at(ae, x) for v in row))
    bad = dict(ae); bad[(0, 0, 0, 2)] = F(1, 3)
    GA.check("control: perturbed coefficient gives H0 != 0",
             any(v != 0 for row in _tf_hess_at(bad, pts[1]) for v in row))
    return True
