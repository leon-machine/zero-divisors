"""The frozen-point MacDowell-Mansouri density as the reduction of the five-dimensional Chern-Simons form of
the Pfaffian invariant of Cl(2,4): exact checks.

Cl(2,4) with generators e0 (+1), e1, e2, e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-;
frozen point I = ninf + (Lambda/6) n0, canonical tractor X = n0, Stelle-West vector V = X - (3/Lambda) I.
Forms: Clifford-valued exterior forms on five directions dx0..dx3, dy (index 4), stored as
{form blade: multivector}; the form product is the Grassmann product (GA.blade_mul with zero squares).
Pfaffian P(B1, B2, B3) = <B1 B2 B3>_6 I6^{-1} (the grade-6 part of three bivectors is their outer product).
Five-dimensional data: frame theta (vector-valued 1-form in V-perp), E = theta ^ V / Q(V) (the translational
part of the connection, store normalisation A = Omega - hb^{-1} ^ V / ell^2), K = sum_{mu<nu} E_mu x E_nu
dx^mu dx^nu, Lorentz curvature R valued in Lambda^2 {I, V}-perp.
Chern-Simons form in Lovelock (transgression) form: L5 = 3 int_0^1 P(E; (R + t^2 K)^2) dt
                                                      = P(E; 3 RR + 2 RK + (3/5) KK).
(1) Reduction: theta = theta4 + lam dy I gives L5 = (3 lam / Q(V)) P(I ^ V; (R + K4)^2) ^ dy, the frozen-point
    MacDowell-Mansouri density eps(I, V, F, F) ^ dy, and K4 = (Lambda/3) theta4 ^ theta4.
(2) The three Lovelock terms reduce with multiplicities 1, 3, 5; the reduced combination is a perfect square
    iff 9 b^2 = 20 a c, which holds on the Chern-Simons family and fails off it.
(3) Five-dimensional equations P(J; F5, F5) on the torsion-free ansatz: zero for J free of V; for J = u ^ V the
    frame equation (zero at Schwarzschild); for J = I ^ V the extra equation eps(I, V, F, F) = (Q(V)/3) dL5/dlam,
    equal to 48 m^2 = Kretschmann/4 at a Schwarzschild point (W(B) = m(B + 3 s B s), s = e1 e0) and 0 for a
    type N Weyl field.
(4) Signatures: V-perp is (2,3) for Lambda > 0 and (1,4) for Lambda < 0; {I, V}-perp is (1,3); in Cl(1,5)
    two orthogonal spacelike unit vectors give a (1,4) V-perp and a de Sitter (1,4) I-perp.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as Fr

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E6 = [GA.gen(i) for i in range(6)]
N0 = GA.scal(Fr(1, 2), GA.add(E6[4], E6[5]))
NI = GA.sub(E6[4], E6[5])
Z5 = (0, 0, 0, 0, 0)
ER = [GA.scal(Fr(1, S[i]), E6[i]) for i in range(4)]


def mul(x, y):
    return GA.mul(x, y, S)


I6 = mul(mul(mul(E6[0], E6[1]), mul(E6[2], E6[3])), mul(E6[4], E6[5]))
I6INV = GA.scal(Fr(1) / mul(I6, I6)[()], I6)


def cross(x, y):
    return GA.scal(Fr(1, 2), GA.sub(mul(x, y), mul(y, x)))


def dot(a, b):
    return GA.dot(a, b, S)


def sp(x):
    return x.get((), Fr(0))


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def fmul(X, Y):
    out = {}
    for a, A in X.items():
        for b, B in Y.items():
            s, g = GA.blade_mul(a, b, Z5)
            if s != 0:
                out[g] = GA.add(out.get(g, {}), GA.scal(s, mul(A, B)))
    return {g: v for g, v in out.items() if v}


def fadd(*Xs):
    out = {}
    for X in Xs:
        for g, v in X.items():
            out[g] = GA.add(out.get(g, {}), v)
    return {g: v for g, v in out.items() if v}


def fscal(c, X):
    return {g: GA.scal(c, v) for g, v in X.items()} if c != 0 else {}


def pf(X):
    out = {}
    for g, v in X.items():
        c = sp(mul(grade(v, 6), I6INV))
        if c:
            out[g] = c
    return out


def frozen(lam):
    I = GA.add(NI, GA.scal(lam / 6, N0))
    return I, GA.sub(N0, GA.scal(Fr(3) / lam, I))


def rng(seed):
    s = [seed]

    def nxt():
        s[0] = (s[0] * 1103515245 + 12345) % 2147483648
        return s[0] % 7 - 3
    return nxt


def sample(seed):
    r = rng(seed)
    th = {(mu,): GA.add(*[GA.scal(Fr(r()), E6[i]) for i in range(4)]) for mu in range(4)}
    R = {}
    for m in range(4):
        for n in range(m + 1, 4):
            R[(m, n)] = GA.add(*[GA.scal(Fr(r()), cross(E6[i], E6[j])) for i in range(4) for j in range(i + 1, 4)])
    return th, R


def E_of(th, V):
    q = dot(V, V)
    return {g: GA.scal(Fr(1) / q, cross(v, V)) for g, v in th.items()}


def K_of(Ef):
    out = {}
    keys = sorted(Ef)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            s, g = GA.blade_mul(a, b, Z5)
            out[g] = GA.add(out.get(g, {}), GA.scal(s, cross(Ef[a], Ef[b])))
    return {g: v for g, v in out.items() if v}


def wedge2(th, c):
    out = {}
    keys = sorted(th)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            s, g = GA.blade_mul(a, b, Z5)
            out[g] = GA.add(out.get(g, {}), GA.scal(s * c, cross(th[a], th[b])))
    return {g: v for g, v in out.items() if v}


def cs_coefficients():
    """3 int_0^1 t^{2k} dt for the RR, RK (with its multiplicity 2) and KK terms of (R + t^2 K)^2."""
    polys = ([Fr(1)], [Fr(0), Fr(0), Fr(2)], [Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)])
    return [3 * GA.peval(GA.ps_int(p), 1) for p in polys]


def lovelock(Ef, R, K, c):
    inner = fadd(fscal(c[0], fmul(R, R)), fscal(c[1], fmul(R, K)), fscal(c[2], fmul(K, K)))
    return pf(fmul(Ef, inner))


def mm_density(I, V, F4):
    return pf(fmul({(): cross(I, V)}, fmul(F4, F4)))


def ansatz(seed, lam, mu):
    I, V = frozen(lam)
    th, R = sample(seed)
    th5 = dict(th)
    th5[(4,)] = GA.scal(mu, I)
    E4, E5 = E_of(th, V), E_of(th5, V)
    return I, V, th, R, E4, E5, K_of(E4), K_of(E5)


def weyl_schwarzschild(m):
    s = mul(E6[1], E6[0])
    return lambda B: GA.scal(m, GA.add(B, GA.scal(3, mul(mul(s, B), s))))


def weyl_type_n():
    k = GA.add(E6[0], E6[3])
    N1, N2 = cross(k, E6[1]), cross(k, E6[2])
    return lambda B: GA.sub(GA.scal(sp(mul(B, N1)), N1), GA.scal(sp(mul(B, N2)), N2))


def is_weyl(W):
    tf = all(not grade(GA.add(*[cross(ER[m], W(cross(E6[m], E6[b]))) for m in range(4)]), 1) for b in range(4))
    bi = all(not grade(GA.add(*[mul(ER[m], W(cross(E6[m], E6[b]))) for m in range(4)]), 3) for b in range(4))
    return tf and bi


def kretschmann(W):
    return 2 * sum(sp(mul(W(cross(E6[a], E6[b])), W(cross(ER[b], ER[a])))) for a in range(4) for b in range(4))


def _premises():
    for pid in ("dark-energy.frozen-point-makes-stelle-west-vector",
                "dark-energy.imported-macdowell-mansouri-theorem-stelle-west",
                "synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection"):
        premise(pid)


def check_chern_simons_five_form_reduces_to_the_frozen_point_functional():
    _premises()
    c = cs_coefficients()
    ok = c == [Fr(3), Fr(2), Fr(3, 5)]
    top = (0, 1, 2, 3, 4)
    for lam in (Fr(3), Fr(-3, 2), Fr(12)):
        for mu in (Fr(1), Fr(2, 3)):
            for seed in (1, 7):
                I, V, th, R, E4, E5, K4, K5 = ansatz(seed, lam, mu)
                ok = ok and dot(I, I) == lam / 3 and dot(V, V) == -3 / lam and dot(I, V) == 0
                ok = ok and fadd(K4, fscal(-1, wedge2(th, lam / 3))) == {}
                L5 = lovelock(E5, R, K5, c)
                M4 = mm_density(I, V, fadd(R, K4)).get((0, 1, 2, 3), Fr(0))
                ok = ok and M4 != 0 and set(L5) == {top} and L5[top] == 3 * mu / dot(V, V) * M4
    GA.check("CS5 Lovelock form on theta4 + lam dy I is (3 lam/Q(V)) eps(I,V,F,F) ^ dy, F = R + (Lambda/3) theta^theta", ok)
    assert ok


def check_reduced_lovelock_terms_are_a_perfect_square_only_on_the_chern_simons_family():
    _premises()
    ok = True
    top = (0, 1, 2, 3, 4)
    for lam, seed in ((Fr(3), 3), (Fr(-3, 2), 5)):
        I, V, th, R, E4, E5, K4, K5 = ansatz(seed, lam, Fr(1))
        q = dot(V, V)
        pieces4 = [mm_density(I, V, X).get((0, 1, 2, 3), Fr(0)) for X in (R,)]
        rr = pf(fmul({(): cross(I, V)}, fmul(R, R))).get((0, 1, 2, 3), Fr(0))
        rk = pf(fmul({(): cross(I, V)}, fmul(R, K4))).get((0, 1, 2, 3), Fr(0))
        kk = pf(fmul({(): cross(I, V)}, fmul(K4, K4))).get((0, 1, 2, 3), Fr(0))
        ok = ok and pieces4[0] == rr and rr != 0 and rk != 0 and kk != 0
        mult = []
        for basis in ([Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)]):
            mult.append(lovelock(E5, R, K5, basis).get(top, Fr(0)) * q)
        ok = ok and mult == [rr, 3 * rk, 5 * kk]
        for (a, b, cc) in ((Fr(1), Fr(2, 3), Fr(1, 5)), (Fr(3), Fr(2), Fr(3, 5)), (Fr(1), Fr(2, 3), Fr(1, 3)),
                           (Fr(0), Fr(1), Fr(1)), (Fr(1), Fr(1, 2), Fr(1, 5))):
            red = a * rr + 3 * b * rk + 5 * cc * kk
            square = 9 * b * b == 20 * a * cc and a != 0
            matches = red == a * (rr + 2 * (3 * b / (2 * a)) * rk + (3 * b / (2 * a)) ** 2 * kk) if a != 0 else False
            ok = ok and (square == matches)
    GA.check("reduced Lovelock multiplicities 1, 3, 5; perfect square iff 9 b^2 = 20 a c (the CS family)", ok)
    assert ok


def check_five_dimensional_equations_on_the_ansatz_add_the_radion_equation():
    _premises()
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    ok = True
    for lam in (Fr(3), Fr(-3, 2)):
        I, V = frozen(lam)
        th = {(mu,): E6[mu] for mu in range(4)}
        th5 = dict(th)
        th5[(4,)] = I
        E4, E5 = E_of(th, V), E_of(th5, V)
        K4, K5 = K_of(E4), K_of(E5)
        for mval, expect in ((Fr(1), None), (Fr(-2, 3), None), (Fr(0), Fr(0))):
            Wmap = weyl_schwarzschild(mval) if expect is None else weyl_type_n()
            ok = ok and is_weyl(Wmap)
            F4 = {}
            for a in range(4):
                for b in range(a + 1, 4):
                    v = Wmap(cross(E6[a], E6[b]))
                    if v:
                        F4[(a, b)] = v
            R = fadd(F4, fscal(-1, K4))
            FF = fmul(fadd(R, K5), fadd(R, K5))
            eqIV = pf(fmul({(): cross(I, V)}, FF))
            frame = [pf(fmul({(): cross(E6[u], V)}, FF)) for u in range(4)]
            noV = [pf(fmul({(): cross(x, y)}, FF)) for x, y in
                   [(E6[u], E6[w]) for u in range(4) for w in range(u + 1, 4)] + [(I, E6[u]) for u in range(4)]]
            ok = ok and all(f == {} for f in frame) and all(f == {} for f in noV)
            val = eqIV.get((0, 1, 2, 3), Fr(0))
            ok = ok and set(eqIV) <= {(0, 1, 2, 3)}
            if expect is None:
                ok = ok and val == 48 * mval * mval and kretschmann(Wmap) == 192 * mval * mval
            else:
                ok = ok and val == expect and F4 != {}
        # generic curvature: radion equation = (Q(V)/3) d L5 / d lam = the MM density; frame equation nonzero
        c = cs_coefficients()
        for seed, want in ((2, Fr(140) if lam == 3 else Fr(-37)), (9, Fr(-108) if lam == 3 else Fr(33))):
            I, V, th, R, E4, E5, K4, K5 = ansatz(seed, lam, Fr(1))
            FF = fmul(fadd(R, K5), fadd(R, K5))
            eqIV = pf(fmul({(): cross(I, V)}, FF)).get((0, 1, 2, 3), Fr(0))
            d1 = lovelock(E5, R, K5, c).get((0, 1, 2, 3, 4), Fr(0))
            ok = ok and eqIV == want and eqIV == mm_density(I, V, fadd(R, K4)).get((0, 1, 2, 3), Fr(0))
            ok = ok and 3 * eqIV == dot(V, V) * d1
            ok = ok and any(pf(fmul({(): cross(E6[u], V)}, FF)) for u in range(4))
    GA.check("5D CS equations on the ansatz: frame equation plus eps(I,V,F,F) = 0; Schwarzschild value Kretschmann/4", ok)
    assert ok


def check_signature_of_the_five_dimensional_parent():
    _premises()
    premise("rule2.rule-2-kaluza-klein-algebra")
    ok = True
    for lam, want in ((Fr(3), (2, 3, 0)), (Fr(3, 4), (2, 3, 0)), (Fr(-3), (1, 4, 0)), (Fr(-9, 7), (1, 4, 0))):
        I, V = frozen(lam)
        vperp = E6[:4] + [I]
        ok = ok and all(dot(v, V) == 0 for v in vperp)
        ok = ok and GA.congruence_signature([[dot(a, b) for b in vperp] for a in vperp]) == want
        ok = ok and GA.congruence_signature([[dot(a, b) for b in E6[:4]] for a in E6[:4]]) == (1, 3, 0)
        iperp = E6[:4] + [V]
        ok = ok and GA.congruence_signature([[dot(a, b) for b in iperp] for a in iperp]) == (
            (1, 4, 0) if lam > 0 else (2, 3, 0))
    S15 = (1, -1, -1, -1, -1, -1)
    e = [GA.gen(i) for i in range(6)]
    d15 = lambda a, b: GA.dot(a, b, S15)
    Ip, Vp = e[4], e[5]
    ok = ok and GA.congruence_signature([[d15(a, b) for b in e[:4] + [Ip]] for a in e[:4] + [Ip]]) == (1, 4, 0)
    ok = ok and GA.congruence_signature([[d15(a, b) for b in e[:4] + [Vp]] for a in e[:4] + [Vp]]) == (1, 4, 0)
    GA.check("Cl(2,4): V-perp (2,3) for Lambda > 0, (1,4) for Lambda < 0; Cl(1,5): Lorentzian parent, de Sitter I-perp", ok)
    assert ok


if __name__ == "__main__":
    check_chern_simons_five_form_reduces_to_the_frozen_point_functional()
    check_reduced_lovelock_terms_are_a_perfect_square_only_on_the_chern_simons_family()
    check_five_dimensional_equations_on_the_ansatz_add_the_radion_equation()
    check_signature_of_the_five_dimensional_parent()


# ---------------------------------------------------------------------------
# GTG proof (2026-11-07): the base forms as multivector fields of a flat five-dimensional background
# Cl(1,4) (the d-dimensional clause of the GTG definition): dx^mu, dy are the background vectors e^0..e^4 and
# the form product is their outer product (the grade-additive part of the Clifford product), which is the
# Grassmann product used above; the reduction (i) recomputed in that reading.
# ---------------------------------------------------------------------------
BG5 = (1, -1, -1, -1, -1)
GTG_CASES = [(Fr(3), Fr(1), 1), (Fr(-3, 2), Fr(2, 3), 7), (Fr(12), Fr(1), 5)]


def fmul_bg(X, Y):
    """Form product with base parts multiplied by the outer product of background multivectors of Cl(1,4)."""
    out = {}
    for a, A in X.items():
        for b, B in Y.items():
            s, g = GA.blade_mul(a, b, BG5)
            if s != 0 and len(g) == len(a) + len(b):
                out[g] = GA.add(out.get(g, {}), GA.scal(s, mul(A, B)))
    return {g: v for g, v in out.items() if v}


def check_gtg_reduction_with_base_forms_as_background_multivectors():
    _premises()
    ok = True
    c = cs_coefficients()
    top = (0, 1, 2, 3, 4)
    for lam, mu, seed in GTG_CASES:
        I, V, th, R, E4, E5, K4, K5 = ansatz(seed, lam, mu)
        inner = fadd(fscal(c[0], fmul_bg(R, R)), fscal(c[1], fmul_bg(R, K5)), fscal(c[2], fmul_bg(K5, K5)))
        L5 = pf(fmul_bg(E5, inner))
        ok = ok and L5 == lovelock(E5, R, K5, c) and set(L5) == {top}
        F4 = fadd(R, K4)
        M4 = pf(fmul_bg({(): cross(I, V)}, fmul_bg(F4, F4))).get((0, 1, 2, 3), Fr(0))
        ok = ok and M4 != 0 and L5[top] == 3 * mu / dot(V, V) * M4
        ok = ok and fmul_bg(th, th) == fmul(th, th) and fmul_bg(R, K5) == fmul(R, K5)
    GA.check("base forms as background multivectors of Cl(1,4): L5 = (3 lam/Q(V)) eps(I,V,F,F) ^ dy", ok)
    assert ok
