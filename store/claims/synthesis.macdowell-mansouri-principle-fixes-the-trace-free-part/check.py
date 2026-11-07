"""The series' MacDowell-Mansouri principle fixes the trace-free part: exact checks.

Cl(1,3) in the store signature (+,-,-,-), orthonormal frame e_a, reciprocal frame e^a = eta^{aa} e_a,
pseudoscalar I = e0 e1 e2 e3; eps_{abcd} is read off e_a ^ e_b ^ e_c ^ e_d = eps_{abcd} I. Curvature
components R_{abcd} (orthonormal, indices down) are sums of Kulkarni-Nomizu products of rational symmetric
matrices, which span the algebraic curvature tensors; Ric_{bd} = eta^{aa} R_{abad}, so the de Sitter
curvature (Lambda/3)(eta_ac eta_bd - eta_ad eta_bc) has Ric = Lambda eta (the sign of the stored MM claim).
(1) The frame equation. With the Lorentz block of the MacDowell-Mansouri field strength
    F_{cdef} = R_{cdef} - (Lambda/3)(eta_ce eta_df - eta_cf eta_de) and F^{cd} = 1/2 F^{cd}_{ef} e^e ^ e^f,
    the three-form E_a = eps_{abcd} e^b ^ F^{cd} of the Fact's second Euler-Lagrange equation equals
    2 (G(e_a) + Lambda e_a) I exactly, G the Einstein tensor, for every sample curvature and Lambda.
    It vanishes for the de Sitter curvature (F = 0).
(2) Ten conditions. As a linear map of the curvature (20 dimensions) the frame equation has rank 10 and
    kernel the Weyl part: the Weyl part of a sample curvature has Ric = 0 and E = 0, and the map from the
    Ricci part is injective (nine trace-free conditions and the trace).
(3) Restricted to pure dilations of hb (delta e^a = delta_w e^a) the frame equation becomes
    e^a ^ E_a = 2 (4 Lambda - R) I: one equation, the Yamabe trace of the stored scale-only no-go.
    As a map of the curvature it has rank 1.
(4) With an independent source, 8 pi G = k: G + Lambda eta + k T = 0 is clause (7),
    Ric + k T = (Lambda + k tau/2) eta, and on shell the Schouten tensor is
    P = Lambda eta/6 - (k/2)(T - tau eta/3): its trace-free part is -(k/2) T°, the stored middle slot of
    nabla I' (4 pi G T° = -P°), J/4 = rho_{I'} with Lambda = 6 rho_{I'} - (k/4) tau, and in vacuum
    P = Lambda eta/6 exactly, the Schouten slot of the de Sitter (Stelle-West) Cartan connection.
Exact arithmetic only (Fractions); no randomness: the sample matrices are fixed tables.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = (1, -1, -1, -1)
ETA = (1, -1, -1, -1)
R4 = range(4)


def _m(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, SQ)
    return out


def _grade(x, g):
    return {b: c for b, c in x.items() if len(b) == g}


def _wedge(*vs):
    out = vs[0]
    g = 1
    for v in vs[1:]:
        g += 1
        out = _grade(_m(out, v), g)
    return out


I4 = _m(GA.gen(0), GA.gen(1), GA.gen(2), GA.gen(3))


def _rec(i):
    return GA.scal(F(1, ETA[i]), GA.gen(i))


def _eps(a, b, c, d):
    return _wedge(GA.gen(a), GA.gen(b), GA.gen(c), GA.gen(d)).get((0, 1, 2, 3), F(0))


EPS = {(a, b, c, d): _eps(a, b, c, d) for a in R4 for b in R4 for c in R4 for d in R4}
W3 = {(b, e, f): _wedge(_rec(b), _rec(e), _rec(f)) for b in R4 for e in R4 for f in R4
      if len({b, e, f}) == 3}


def _kn(h, k):
    return {(a, b, c, d): h[a][c] * k[b][d] + h[b][d] * k[a][c] - h[a][d] * k[b][c] - h[b][c] * k[a][d]
            for a in R4 for b in R4 for c in R4 for d in R4}


def _sym(rows):
    M = [[F(0)] * 4 for _ in R4]
    for (i, j, v) in rows:
        M[i][j] = M[j][i] = F(v)
    return M


def _curv_add(*Rs):
    return {key: sum(R[key] for R in Rs) for key in Rs[0]}


ETAM = [[F(ETA[a]) if a == b else F(0) for b in R4] for a in R4]
H1 = _sym([(0, 0, 2), (0, 1, F(1, 3)), (1, 1, -1), (1, 2, F(5, 2)), (2, 3, 1), (3, 3, F(-7, 4)), (0, 3, 3)])
K1 = _sym([(0, 0, -1), (0, 2, F(2, 5)), (1, 1, 4), (1, 3, -2), (2, 2, F(1, 2)), (3, 3, 1), (2, 3, F(-3, 2))])
H2 = _sym([(0, 1, 1), (1, 1, F(3, 2)), (2, 2, -3), (0, 2, -1), (1, 3, F(4, 3)), (3, 3, 2)])
K2 = _sym([(0, 0, 3), (0, 3, F(-1, 2)), (1, 2, 2), (2, 2, 1), (3, 3, F(-5, 3)), (1, 1, F(1, 4))])
LAMBDA0 = F(0)
SPAN_LAMBDAS = (F(0), F(-5, 2))
LAMBDAS = (F(0), F(3, 7), F(-2))
DS_LAMBDAS = (F(3), F(1, 5))
DIL_LAMBDAS = (F(0), F(5, 3))
SOURCES = [_sym([(0, 0, 3), (0, 1, F(1, 2)), (1, 1, 1), (2, 2, F(2, 3)), (3, 3, -1), (2, 3, F(1, 4))]),
           _sym([(0, 0, 1), (1, 2, -2), (1, 1, F(-1, 3)), (3, 3, 5), (0, 3, F(3, 2))])]
LK = [(F(1, 3), F(2)), (F(-1), F(5, 7)), (F(0), F(1))]
VAC_LAMBDAS = (F(3), F(-1, 2))
SAMPLES = [_curv_add(_kn(H1, K1), _kn(H2, K2)), _kn(H1, H2), _curv_add(_kn(K1, K2), _kn(ETAM, H1))]


def _ric(R):
    return [[sum(F(1, ETA[a]) * R[a, b, a, d] for a in R4) for d in R4] for b in R4]


def _scalar(M):
    return sum(F(1, ETA[a]) * M[a][a] for a in R4)


def _einstein_plus(R, L):
    Ric = _ric(R)
    s = _scalar(Ric)
    return [[Ric[a][b] - s / 2 * ETAM[a][b] + L * ETAM[a][b] for b in R4] for a in R4]


def _lorentz_block(R, L):
    return {(c, d, e, f): R[c, d, e, f] - L / 3 * (ETAM[c][e] * ETAM[d][f] - ETAM[c][f] * ETAM[d][e])
            for (c, d, e, f) in R}


def _frame_eq(R, L):
    """E_a = eps_{abcd} e^b ^ F^{cd}, F^{cd} = 1/2 F^{cd}_{ef} e^e ^ e^f, as GA trivectors."""
    Fb = _lorentz_block(R, L)
    out = []
    for a in R4:
        tot = {}
        for b in R4:
            for c in R4:
                for d in R4:
                    ep = EPS[a, b, c, d]
                    if ep == 0:
                        continue
                    for e in R4:
                        for f in R4:
                            if len({b, e, f}) < 3:
                                continue
                            co = F(1, 2) * ep * F(1, ETA[c] * ETA[d]) * Fb[c, d, e, f]
                            if co != 0:
                                tot = GA.add(tot, GA.scal(co, W3[b, e, f]))
        out.append(tot)
    return out


def _dual_of_row(M, a):
    v = {}
    for f in R4:
        v = GA.add(v, GA.scal(M[a][f] * F(1, ETA[f]), GA.gen(f)))
    return _m(v, I4)


def _coeffs(trivs):
    blades = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    return [t.get(bl, F(0)) for t in trivs for bl in blades]


def check_frame_equation_is_twice_the_dual_of_einstein_plus_lambda():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("synthesis.series-wald-entropy-changes-without-flux-on-local-horizons")
    GA.check("I^2 = -1 in Cl(1,3)", GA.eq(_m(I4, I4), GA.sc(-1)))
    for R in SAMPLES:
        for L in LAMBDAS:
            E = _frame_eq(R, L)
            Gp = _einstein_plus(R, L)
            for a in R4:
                GA.check("E_a = 2 (G(e_a) + Lambda e_a) I", GA.eq(E[a], GA.scal(2, _dual_of_row(Gp, a))))
            GA.check("the frame equation is not trivially zero", any(not GA.is_zero(x) for x in E))
    for L in DS_LAMBDAS:
        dS = {(a, b, c, d): L / 3 * (ETAM[a][c] * ETAM[b][d] - ETAM[a][d] * ETAM[b][c])
              for a in R4 for b in R4 for c in R4 for d in R4}
        GA.check("de Sitter: Ric = Lambda eta", _ric(dS) == [[L * ETAM[a][b] for b in R4] for a in R4])
        GA.check("de Sitter: the Lorentz block vanishes", all(v == 0 for v in _lorentz_block(dS, L).values()))
        GA.check("de Sitter: frame equation satisfied", all(GA.is_zero(x) for x in _frame_eq(dS, L)))
        GA.check("wrong Lambda: frame equation fails", any(not GA.is_zero(x) for x in _frame_eq(dS, L + 1)))


def _basis_sym():
    out = []
    for i in R4:
        for j in range(i, 4):
            out.append(_sym([(i, j, 1)]))
    return out


def _weyl_part(R):
    Ric = _ric(R)
    s = _scalar(Ric)
    P = [[(Ric[a][b] - s / 6 * ETAM[a][b]) / 2 for b in R4] for a in R4]
    PK = _kn(P, ETAM)
    return {key: R[key] - PK[key] for key in R}


def _kn_space():
    B = _basis_sym()
    return [_kn(B[i], B[j]) for i in range(len(B)) for j in range(i, len(B))]


def check_frame_identity_on_the_spanning_set():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.series-wald-entropy-changes-without-flux-on-local-horizons")
    space = _kn_space()
    keys = sorted(next(iter(space)))
    GA.check("the spanning set has rank 20", GA.mat_rank([[R[k] for k in keys] for R in space]) == 20)
    for R in space:
        for L in SPAN_LAMBDAS:
            E = _frame_eq(R, L)
            Gp = _einstein_plus(R, L)
            GA.check("E_a = 2 (G(e_a) + Lambda e_a) I on every Kulkarni-Nomizu product",
                     all(GA.eq(E[a], GA.scal(2, _dual_of_row(Gp, a))) for a in R4))


def check_kernel_is_the_weyl_part_and_rank_is_ten():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    B = _basis_sym()
    space = []
    for i in range(len(B)):
        for j in range(i, len(B)):
            space.append(_kn(B[i], B[j]))
    keys = sorted(next(iter(space)))
    rows = [[R[k] for k in keys] for R in space]
    GA.check("Kulkarni-Nomizu products span the 20 algebraic curvature tensors", GA.mat_rank(rows) == 20)
    images = [_coeffs(_frame_eq(R, LAMBDA0)) for R in space]
    GA.check("frame equation has rank 10 on the curvature", GA.mat_rank(images) == 10)
    trace_images = [[_scalar(_ric(R))] for R in space]
    GA.check("the trace alone has rank 1", GA.mat_rank(trace_images) == 1)
    for R in SAMPLES:
        W = _weyl_part(R)
        GA.check("Weyl part is Ricci-flat", all(x == 0 for row in _ric(W) for x in row))
        GA.check("Weyl part nonzero for the sample", any(W.values()))
        GA.check("Weyl part drops out of the frame equation", all(GA.is_zero(x) for x in _frame_eq(W, LAMBDA0)))
    # injectivity on the Ricci part: the frame equation of P o eta for each basis symmetric P
    ric_images = [_coeffs(_frame_eq(_kn(P, ETAM), LAMBDA0)) for P in B]
    GA.check("the frame equation is injective on the ten Ricci components", GA.mat_rank(ric_images) == 10)
    tf = []
    for P in B:
        t = _scalar(P)
        Pt = [[P[a][b] - t / 4 * ETAM[a][b] for b in R4] for a in R4]
        tf.append(_coeffs(_frame_eq(_kn(Pt, ETAM), LAMBDA0)))
    GA.check("nine trace-free conditions", GA.mat_rank(tf) == 9)


def check_dilation_restriction_is_the_yamabe_trace():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale")
    for R in SAMPLES:
        for L in DIL_LAMBDAS:
            E = _frame_eq(R, L)
            tot = {}
            for a in R4:
                tot = GA.add(tot, _grade(_m(_rec(a), E[a]), 4))
            s = _scalar(_ric(R))
            GA.check("e^a ^ E_a = 2 (4 Lambda - R) I", GA.eq(tot, GA.scal(2 * (4 * L - s), I4)))
    imgs = []
    B = _basis_sym()
    for i in range(len(B)):
        for j in range(i, len(B)):
            E = _frame_eq(_kn(B[i], B[j]), LAMBDA0)
            tot = {}
            for a in R4:
                tot = GA.add(tot, _grade(_m(_rec(a), E[a]), 4))
            imgs.append([tot.get(next(iter(I4)), LAMBDA0)])
    GA.check("restricted to dilations: one equation (rank 1)", GA.mat_rank(imgs) == 1)


def check_on_shell_schouten_is_the_stored_tractor_derivative():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    premise("synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale")
    premise("synthesis.imported-gtg-dictionary")
    for T in SOURCES:
        for (L, k) in LK:
            tau = _scalar(T)
            Ric = [[-k * T[a][b] + (L + k * tau / 2) * ETAM[a][b] for b in R4] for a in R4]
            s = _scalar(Ric)
            Gp = [[Ric[a][b] - s / 2 * ETAM[a][b] + L * ETAM[a][b] for b in R4] for a in R4]
            GA.check("clause (7) <=> G + Lambda eta + k T = 0",
                     all(Gp[a][b] + k * T[a][b] == 0 for a in R4 for b in R4))
            P = [[(Ric[a][b] - s / 6 * ETAM[a][b]) / 2 for b in R4] for a in R4]
            GA.check("P = Lambda eta/6 - (k/2)(T - tau eta/3)",
                     all(P[a][b] == L / 6 * ETAM[a][b] - k / 2 * (T[a][b] - tau / 3 * ETAM[a][b])
                         for a in R4 for b in R4))
            J = _scalar(P)
            Pc = [[P[a][b] - J / 4 * ETAM[a][b] for b in R4] for a in R4]
            Tc = [[T[a][b] - tau / 4 * ETAM[a][b] for b in R4] for a in R4]
            GA.check("middle slot: -P° = (k/2) T° = 4 pi G T°",
                     all(-Pc[a][b] == k / 2 * Tc[a][b] for a in R4 for b in R4))
            GA.check("Lambda = 6 rho_{I'} - 2 pi G tau with rho_{I'} = J/4", 6 * (J / 4) - k / 4 * tau == L)
            GA.check("matter makes the Schouten slot differ from Lambda eta/6",
                     any(P[a][b] != L / 6 * ETAM[a][b] for a in R4 for b in R4))
    for L in VAC_LAMBDAS:
        Ric = [[L * ETAM[a][b] for b in R4] for a in R4]
        s = _scalar(Ric)
        P = [[(Ric[a][b] - s / 6 * ETAM[a][b]) / 2 for b in R4] for a in R4]
        GA.check("vacuum: P = Lambda eta/6 (the Stelle-West Cartan slot)",
                 all(P[a][b] == L / 6 * ETAM[a][b] for a in R4 for b in R4))


# ---- GTG derivation (maintainer pass 2026-11-07, GTG proofs) ----
# The frame equation as a trivector-valued linear function of the curvature OPERATOR (lib/gtg.py):
# E(a) = 2 d_b ^ F(I (a ^ b)), F = calR - (Lambda/3) id (store sign), with the GA identities
# d_b ^ calR(I (a ^ b)) = calG(a) I and d_b ^ (I (a ^ b)) = -3 a I, so E(a) = 2 (calG(a) + Lambda a) I.
import gtg  # noqa: E402


def frame_trivector(Rop, a, lam):
    """2 d_b ^ F(I (a ^ b)) with F(B) = Rop(B) - (Lambda/3) B."""
    R = gtg.as_op(Rop)
    out = {}
    for b in R4:
        X = _m(I4, gtg.wedge(a, GA.gen(b), SQ))
        Fx = GA.sub(R(X), GA.scal(lam / 3, X))
        out = GA.add(out, gtg.outer(_rec(b), Fx, SQ))
    return GA.scal(2, out)


def op_from_components(R):
    """calR(e_e ^ e_f) = (1/2) sum_cd R^{cd}_{ef} e_c ^ e_d from the orthonormal components R_{cdef}."""
    planes = {}
    for e in R4:
        for f in R4:
            if e < f:
                acc = {}
                for c in R4:
                    for d in R4:
                        co = F(1, 2) * F(1, ETA[c] * ETA[d]) * R[c, d, e, f]
                        if co != 0 and c != d:
                            acc = GA.add(acc, GA.scal(co, gtg.wedge(GA.gen(c), GA.gen(d), SQ)))
                planes[(e, f)] = acc
    return planes


def weyl_sample_fields():
    """Schwarzschild (PG, beta = 4/5), a Kasner vacuum (2/3, 2/3, -1/3) and a non-vacuum synchronous field."""
    return (gtg.schwarzschild_pg(F(1, 2), F(25, 16), F(3, 5), F(4, 5)),
            gtg.synchronous_from_data([(F(1), F(2, 3), F(-2, 9)), (F(1), F(2, 3), F(-2, 9)), (F(1), F(-1, 3), F(4, 9))]),
            gtg.synchronous_from_data([(F(1), F(1, 2), F(1, 7)), (F(2), F(-1, 3), F(2)), (F(1, 2), F(1), F(-3))]))


def check_gtg_frame_trivector_is_twice_dual_einstein_plus_lambda():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    e = [GA.gen(i) for i in R4]
    # the identity operator: d_b ^ (I (a ^ b)) = -3 a I
    ok = ok and all(GA.eq(frame_trivector(gtg.op_const(0), e[c], F(-3, 2)), GA.scal(-3, _m(e[c], I4))) for c in R4)
    # the Ricci part: the Kulkarni-Nomizu operators of the ten basis symmetric maps (linearity covers all)
    for S in _basis_sym():
        T = (lambda Sm: (lambda v: GA.add(*[GA.scal(sum(Sm[i][j] * GA.dot(v, e[j], SQ) * ETA[j] for j in R4) * ETA[i],
                                                     e[i]) for i in R4])))(S)
        op = gtg.op_kn(T, SQ)
        ok = ok and all(GA.eq(frame_trivector(op, e[c], F(0)), GA.scal(2, _m(gtg.einstein(op, e[c]), I4)))
                        for c in R4)
    # the Weyl part: W(IB) = I W(B) and trace-free give d_b ^ W(I (a ^ b)) = 0, on three gauge fields
    for fld in weyl_sample_fields():
        W = gtg.weyl_op(fld.curvature())
        ok = ok and any(v != {} for v in W.values())
        for (p, q) in gtg.bivector_blades(4):
            B = gtg.wedge(e[p], e[q], SQ)
            ok = ok and GA.eq(gtg.apply_op(W, _m(I4, B)), _m(I4, gtg.apply_op(W, B)))
        ok = ok and all(frame_trivector(W, e[c], F(0)) == {} for c in R4)
    # the component three-form of the Fact is this trivector, on the sample curvatures
    for R in SAMPLES:
        op = op_from_components(R)
        for L in LAMBDAS:
            E = _frame_eq(R, L)
            ok = ok and all(GA.eq(E[c], frame_trivector(op, e[c], L)) for c in R4)
            ok = ok and all(GA.eq(E[c], GA.scal(2, _m(gtg.einstein_residual(op, e[c], L), I4))) for c in R4)
    assert ok
    return ok


def check_gtg_frame_equation_on_gauge_fields_and_dilation_trace():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale")
    ok = True
    e = [GA.gen(i) for i in R4]
    ds = gtg.de_sitter_flat(F(1, 2), F(2)).curvature()            # Lambda = 3/4
    ok = ok and all(frame_trivector(ds, e[c], F(3, 4)) == {} for c in R4)
    ok = ok and any(frame_trivector(ds, e[c], F(7, 4)) != {} for c in R4)
    rows = []
    for S in _basis_sym():
        T = (lambda Sm: (lambda v: GA.add(*[GA.scal(sum(Sm[i][j] * GA.dot(v, e[j], SQ) * ETA[j] for j in R4) * ETA[i],
                                                     e[i]) for i in R4])))(S)
        op = gtg.op_kn(T, SQ)
        rows.append(_coeffs([frame_trivector(op, e[c], F(0)) for c in R4]))
    ok = ok and GA.mat_rank(rows) == 10
    for fld in (gtg.flrw_flat(F(1), F(1, 3), F(-1, 5)), gtg.schwarzschild_pg(F(1, 2), F(25, 16), F(3, 5), F(4, 5))):
        Rc = fld.curvature()
        for L in (F(0), F(5, 3)):
            tr = GA.add(*[gtg.outer(_rec(c), frame_trivector(Rc, e[c], L), SQ) for c in R4])
            ok = ok and GA.eq(tr, GA.scal(2 * (4 * L - gtg.ricci_scalar(Rc)), I4))
    assert ok
    return ok
