"""field-theory.second-quantisation: exact checks in the single algebra (blade engine, Fraction).

Ground Cl(1,3) (gamma_0..3, squares 1, -1, -1, -1) plus 12 tower planes (generators of square +1, -1;
v = (e + f)/2 creates, w = (e - f)/2 annihilates; the planes give the CAR, premise tower-limit).
Complex numbers enter only as rational points of the unit circle (GA.QI) used as real coefficients
with i acting as right I sigma_3 = gamma_2 gamma_1 on spinor values. Null momenta k = (1,0,0,1),
(5,3,4,0), (3,2,1,2); chi_eps(phi) = (phi - eps I4 phi I sigma_3)/2; proj keeps span{1, I4} of the
ground (tower parts carried along).
(1) Lambda(k) = k gamma_0/(2 k_0) is idempotent, self-adjoint for alpha(phi, u) = <phi^dagger u>_0,
complex linear, the identity on ker k, of rank 4 with range ker k: the orthogonal projector onto
ker k; it commutes with chi_+-, and f <f, phi> = alpha(f, f) Lambda(k) chi_eps(phi) (completeness).
(2) The field Psi = sum_j [f_j p_j w + f_j conj(p_j) v] (one chirality): the anticommutator
{Psi(x; phi1), Psi(y; phi2)^*}, computed in the algebra, has no tower part and equals
<phi1, sum_j 2 alpha_j cos(k_j.(x - y)) Lambda(k_j) chi phi2> with i -> eps I4, for eps = +1 and -1;
2 k_0 Lambda(k) = k gamma_0, the GA form of chi (nabla D) gamma_0 (the continuum limit is imported).
Without the projection the anticommutator has other ground components (control).
(3) The pairing <phi, u> is the projection of phi^dagger u onto span{1, I4} for chiral u (and fails
for a non-chiral u, control); proj(Psi^* M Psi) for the particle field equals
sum_cd <u_c, M u_d> a_c^* a_d for M = 1, gamma_01, gamma_12 (d Gamma(M)); with antiparticle terms
present a c-number sum_j alpha(f_j, f_j) appears (from w v = 1 - v w), which normal ordering removes.
(4) A field carrying both chiralities: the anticommutator is <phi1, S_R phi2> + conj <phi1, S_L phi2>
(the left-handed part conjugated), not <phi1, S phi2>; read through Hestenes' projection onto
span{1, I sigma_3} (I sigma_3 commutes with every tower vector) it reproduces <phi1, S phi2> for both
chiralities at once.
"""
from fractions import Fraction as F

import GA
from GA import mul, add, sub, sc, gen, eq, is_zero, commutes, all_blades, QI
from tp_premise import premise

S4 = (1, -1, -1, -1)
I4 = {(0, 1, 2, 3): F(1)}
IS3 = {(1, 2): F(-1)}
G0 = gen(0)
KS = [(1, 0, 0, 1), (5, 3, 4, 0), (3, 2, 1, 2)]
NPL = 4 * len(KS)
SB = tuple(list(S4) + [1, -1] * NPL)
PX = [QI(F(3, 5), F(-4, 5)), QI(F(5, 13), F(12, 13)), QI(F(-8, 17), F(15, 17))]
PY = [QI(F(7, 25), F(24, 25)), QI(F(-3, 5), F(-4, 5)), QI(F(20, 29), F(21, 29))]
PHIS = [{(): F(1), (0, 1): F(2), (1, 3): F(-1), (0, 1, 2, 3): F(1, 2)},
        {(0, 2): F(1), (2, 3): F(3), (): F(-2)},
        {(1, 2): F(1), (0, 3): F(-1, 3), (0, 1, 2, 3): F(2)}]


def scl(c, x):
    return {b: c * v for b, v in x.items() if c * v != 0}


def blade(t):
    return {tuple(t): F(1)}


EVEN = [blade(b) for b in all_blades(4) if len(b) % 2 == 0]


def star(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        out[b] = sign * c
    return {b: c for b, c in out.items() if c != 0}


def dag(phi, s=S4):
    return star(phi, s)


def alpha(phi, u):
    return mul(dag(phi), u, S4).get((), F(0))


def J(phi):
    return mul(phi, IS3, S4)


def cpair(phi, u):
    return QI(alpha(phi, u), alpha(J(phi), u))


def chi(eps, phi):
    return scl(F(1, 2), sub(phi, scl(F(eps), mul(mul(I4, phi, S4), IS3, S4))))


def rphase(u, z):
    return add(scl(z.re, u), scl(z.im, J(u)))


def kvec(k):
    return add(*[scl(F(k[m]), gen(m)) for m in range(4) if k[m] != 0])


def Lam(k, phi):
    return scl(F(1, 2 * k[0]), mul(mul(kvec(k), G0, S4), phi, S4))


def proj14(x):
    return {b: c for b, c in x.items() if tuple(i for i in b if i < 4) in ((), (0, 1, 2, 3))}


def projq(x):
    return {b: c for b, c in x.items() if tuple(i for i in b if i < 4) in ((), (1, 2))}


def cnum(z, eps, unit=None):
    return add(sc(z.re), scl(F(eps) * z.im, unit or I4))


def mat_rank(op):
    eb = [b for b in all_blades(4) if len(b) % 2 == 0]
    cols = [op(blade(b)) for b in eb]
    return GA.rank_of_vectors([[cols[j].get(eb[i], F(0)) for j in range(8)] for i in range(8)])


_F = {}


def spinor(k, eps):
    if (k, eps) not in _F:
        _F[(k, eps)] = next(c for c in (Lam(k, chi(eps, b)) for b in EVEN) if not is_zero(c))
    return _F[(k, eps)]


def plane(p):
    e_, f_ = 4 + 2 * p, 5 + 2 * p
    return add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_))), add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_)))


PL = [plane(p) for p in range(NPL)]
# CAR sample: two distinct tower planes.
CAR_PLANE_A, CAR_PLANE_B = PL[0], PL[1]
# Projection control: chirality + and the first two test spinors.
CONTROL_EPS, CONTROL_PHI1, CONTROL_PHI2 = 1, PHIS[0], PHIS[1]


def field(phase, chiralities, antiparticles=True):
    out = {}
    for j, k in enumerate(KS):
        for ci, eps in enumerate(chiralities):
            f = spinor(k, eps)
            pp = 4 * j + 2 * ci
            out = add(out, mul(rphase(f, phase[j]), PL[pp][1], SB))
            if antiparticles:
                out = add(out, mul(rphase(f, phase[j].conj()), PL[pp + 1][0], SB))
    return out


def comp(phi, Psi, pr=proj14):
    return pr(mul(dag(phi, SB), Psi, SB))


def anti(a, b):
    return add(mul(a, b, SB), mul(b, a, SB))


def expected(phi1, phi2, chiralities, conj_for=()):
    tot = QI(0)
    for j, k in enumerate(KS):
        for eps in chiralities:
            f = spinor(k, eps)
            term = QI(0)
            for (px, py) in ((PX[j], PY[j]), (PX[j].conj(), PY[j].conj())):
                term = term + cpair(phi1, rphase(f, px)) * cpair(rphase(f, py), phi2)
            tot = tot + (term.conj() if eps in conj_for else term)
    return tot


def check_lambda_is_orthogonal_projector_onto_ker_k():
    for k in KS:
        kv = kvec(k)
        assert is_zero(mul(kv, kv, S4))
        for b in EVEN:
            lb = Lam(k, b)
            assert eq(Lam(k, lb), lb) and is_zero(mul(kv, lb, S4)) and eq(Lam(k, J(b)), J(lb))
            if is_zero(mul(kv, b, S4)):
                assert eq(lb, b)
            for e in (1, -1):
                assert eq(Lam(k, chi(e, b)), chi(e, Lam(k, b)))
        for b1 in EVEN:
            for b2 in EVEN:
                assert alpha(Lam(k, b1), b2) == alpha(b1, Lam(k, b2))
        assert mat_rank(lambda p: Lam(k, p)) == 4
        assert eq(scl(F(2 * k[0]), Lam(k, sc(1))), mul(kv, G0, S4))
        for eps in (1, -1):
            f = spinor(k, eps)
            a_ = alpha(f, f)
            assert a_ != 0
            for phi in EVEN + PHIS:
                assert eq(rphase(f, cpair(f, phi)), scl(a_, Lam(k, chi(eps, phi))))
            assert mat_rank(lambda p, k=k, eps=eps: Lam(k, chi(eps, p))) == 2


def check_field_anticommutator_is_local_kernel():
    premise("field-theory.imported-tower-limit")
    v0, w0 = CAR_PLANE_A
    v1, w1 = CAR_PLANE_B
    assert eq(anti(v0, w0), sc(1)) and is_zero(anti(v0, w1)) and is_zero(mul(v0, v0, SB))
    for eps in (1, -1):
        PsiX, PsiY = field(PX, (eps,)), field(PY, (eps,))
        for phi1 in PHIS:
            for phi2 in PHIS:
                A = anti(comp(phi1, PsiX), star(comp(phi2, PsiY), SB))
                assert all(max(b) < len(S4) for b in A if b)          # no tower generator in A
                assert eq(A, cnum(expected(phi1, phi2, (eps,)), eps))
                tot = QI(0)
                for j, k in enumerate(KS):
                    cosv = (PX[j] * PY[j].conj()).re
                    f = spinor(k, eps)
                    tot = tot + QI(2 * alpha(f, f) * cosv) * cpair(phi1, Lam(k, chi(eps, phi2)))
                assert tot == expected(phi1, phi2, (eps,))
    PsiX, PsiY = field(PX, (CONTROL_EPS,)), field(PY, (CONTROL_EPS,))
    raw = anti(mul(dag(CONTROL_PHI1, SB), PsiX, SB), star(mul(dag(CONTROL_PHI2, SB), PsiY, SB), SB))
    assert not eq(proj14(raw), raw)              # without the projection other ground components remain


def check_bilinears_are_second_quantised_operators():
    premise("field-theory.imported-tower-limit")
    for eps in (1, -1):
        for b in EVEN:
            u = chi(eps, b)
            assert eq(chi(eps, u), u)
            if is_zero(u):
                continue
            assert eq(mul(I4, u, S4), scl(F(eps), mul(u, IS3, S4)))
            for phi in EVEN + PHIS:
                assert eq(proj14(mul(dag(phi), u, S4)), cnum(cpair(phi, u), eps))
    nonchiral = add(chi(1, blade(())), chi(-1, blade((0, 1))))
    for e in (1, -1):
        assert any(not eq(proj14(mul(dag(phi), nonchiral, S4)), cnum(cpair(phi, nonchiral), e))
                   for phi in EVEN + PHIS)
    Psi_p = field(PX, (1,), antiparticles=False)
    for M in (sc(1), blade((0, 1)), blade((1, 2))):
        lhs = proj14(mul(mul(star(Psi_p, SB), M, SB), Psi_p, SB))
        rhs = {}
        for c, kc in enumerate(KS):
            uc = rphase(spinor(kc, 1), PX[c])
            for d, kd in enumerate(KS):
                ud = rphase(spinor(kd, 1), PX[d])
                rhs = add(rhs, mul(cnum(cpair(uc, mul(M, ud, S4)), 1), mul(PL[4 * c][0], PL[4 * d][1], SB), SB))
        assert eq(lhs, rhs)
    # with antiparticles: proj(Psi^* Psi) = sum_cd <x_c, y_d> X_c^* Y_d over particle (a = w, a^* = v) and
    # antiparticle (b^* = v) parts, with the antiparticle bilinear in the order b_c b_d^*; normal ordering
    # b_c b_d^* = delta_cd - b_d^* b_c leaves the c-number sum_c <vm_c, vm_c> = sum_c alpha(f_c, f_c) != 0
    Psi = field(PX, (1,))
    full = proj14(mul(star(Psi, SB), Psi, SB))
    parts = []
    for j, k in enumerate(KS):
        f = spinor(k, 1)
        parts.append((rphase(f, PX[j]), PL[4 * j][0], PL[4 * j][1]))                 # (u, a^*, a)
        parts.append((rphase(f, PX[j].conj()), PL[4 * j + 1][1], PL[4 * j + 1][0]))  # (vm, b, b^*)
    expansion = {}
    for xc, Xs, _ in parts:
        for yd, _, Y in parts:
            expansion = add(expansion, mul(cnum(cpair(xc, yd), 1), mul(Xs, Y, SB), SB))
    assert eq(full, expansion)
    normal = {}
    for c, (xc, Xs, _) in enumerate(parts):
        for d, (yd, _, Y) in enumerate(parts):
            if c % 2 == 1 and d % 2 == 1:
                bdag_d, b_c = parts[d][2], parts[c][1]
                term = scl(F(-1), mul(bdag_d, b_c, SB))                          # :b_c b_d^*: = -b_d^* b_c
            else:
                term = mul(Xs, Y, SB)
            normal = add(normal, mul(cnum(cpair(xc, yd), 1), term, SB))
    cnumber = sum((alpha(spinor(k, 1), spinor(k, 1)) for k in KS), F(0))
    assert cnumber != 0 and eq(sub(full, normal), sc(cnumber))


def check_mixed_chirality_split_forced_by_i_equals_I4():
    premise("field-theory.imported-tower-limit")
    PsiX, PsiY = field(PX, (1, -1)), field(PY, (1, -1))
    bad = False
    for phi1 in PHIS:
        for phi2 in PHIS:
            A = anti(comp(phi1, PsiX), star(comp(phi2, PsiY), SB))
            if not eq(A, cnum(expected(phi1, phi2, (1, -1)), 1)):
                bad = True
            assert eq(A, cnum(expected(phi1, phi2, (1, -1), conj_for=(-1,)), 1))
    assert bad
    assert all(commutes(IS3, gen(i), SB) for i in range(4, 4 + 2 * NPL))
    ok = {}
    for sgn in (1, -1):
        ok[sgn] = all(eq(anti(comp(p1, PsiX, projq), star(comp(p2, PsiY, projq), SB)),
                         cnum(expected(p1, p2, (1, -1)), sgn, IS3)) for p1 in PHIS for p2 in PHIS)
    assert ok[1] != ok[-1] and (ok[1] or ok[-1])
