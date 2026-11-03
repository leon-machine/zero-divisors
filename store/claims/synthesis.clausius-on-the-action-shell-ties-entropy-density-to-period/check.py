"""On the joint premise set (the field-space action with one coupling G, and the Clausius relation on local
patches at rapidity period 2 pi c), the Clausius relation at a point where matter crosses is eta = c/(4G).

Gauge Theory Gravity on flat spacetime, store sign (lib/gtg.py): signature (+,-,-,-), calR(B) the store curvature,
the action's field equation G(b) + Lambda b + 4 G t(b) = 0 with t = 2 pi T (8 pi G T = 4 G t), the Clausius defect
on a thin pencil at period 2 pi c: t(k,k) + (eta/c) k.calR(k) (the stored defect of the integrated-(Loc) check at
c = 1, and of the period-c independence model with the temperature rescaled by 1/c).
(1) For Einstein fields at coupling G with arbitrary stress and Weyl part the defect is t(k,k)(1 - 4 G eta / c)
    exactly, at every null k; it vanishes at a k with t(k,k) != 0 only at eta = c/(4G).
(2) The null-cone values t(k,k) determine t up to a multiple of the metric (rank 9 on the 10 symmetric maps), so
    "some null k with t(k,k) != 0" is "t is not a multiple of the metric".
(3) The stored witness of the one-coupling clause's independence (Einstein static universe of radius 2, dust
    sigma = 1/4, eta = 1/2) solves the action's equations at G = 1/2 and at G = 1 for no Lambda; at G = 1 the
    universe of radius 2 needs sigma = 1/8, where eta = 1/4.
(4) On a flat dust Friedmann-Lambda instant on the action's shell at G = 1 with eta = 1/4 the defect vanishes only
    at c = 1; on de Sitter it vanishes for every eta and c.
(5) On a vacuum field with Weyl part and Lambda the defect vanishes for every eta and c (the relation is empty).
"""
from fractions import Fraction as F
import GA
import gtg
from tp_premise import premise

J = gtg.Jet
E = [GA.gen(i) for i in range(4)]
ER = [gtg.er(i) for i in range(4)]

# rational null directions k = gamma_0 + n, Q(n) = -1 (Pythagorean unit vectors and their negatives)
_NS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1),
       (F(3, 5), F(4, 5), 0), (0, F(3, 5), F(4, 5)), (F(4, 5), 0, F(3, 5)),
       (F(2, 3), F(2, 3), F(1, 3)), (F(2, 7), F(3, 7), F(6, 7)), (F(-2, 3), F(1, 3), F(2, 3))]
NULLS = [gtg.m_add(E[0], *[gtg.m_scal(F(n[i]), E[i + 1]) for i in range(3) if n[i] != 0]) for n in _NS]


def _tmap(S):
    """t(b) = sum S[m][n] (b . gamma_m) gamma_n for a symmetric rational array S."""
    def t(b):
        out = {}
        for m in range(4):
            bm = gtg.vdot(b, E[m])
            if bm != 0:
                for n in range(4):
                    if S[m][n] != 0:
                        out = gtg.m_add(out, gtg.m_scal(bm * S[m][n], E[n]))
        return out
    return t


def _trace(t):
    return sum((gtg.vdot(ER[m], t(E[m])) for m in range(4)), F(0))


def _einstein_field(t, lam, G, weyl_c):
    """The store-sign curvature operator with Ricci part fixed by G(a) + Lambda a + 4 G t(a) = 0 and Weyl part
    weyl_c (a + 3 s a s) with s = gamma_1 gamma_0 (a type-D Weyl operator)."""
    tau = _trace(t)
    sc = 4 * lam + 4 * G * tau
    ric = lambda a: gtg.m_sub(gtg.m_scal(lam + 2 * G * tau, a), gtg.m_scal(4 * G, t(a)))
    P = lambda a: gtg.m_scal(F(1, 2), gtg.m_sub(ric(a), gtg.m_scal(sc / 6, a)))
    sig = gtg.m_mul(E[1], E[0])
    return gtg.op_add(gtg.op_kn(P), gtg.op_type_d(F(weyl_c), sig))


def _on_shell(R, t, lam, G):
    return all(gtg.m_add(gtg.einstein_residual(R, E[b], lam), gtg.m_scal(4 * G, t(E[b]))) == {} for b in range(4))


def _defect(R, t, k, eta, c):
    return gtg.vdot(k, t(k)) + (F(eta) / F(c)) * gtg.vdot(k, gtg.ricci(R, k))


# sample stresses (symmetric), cosmological constants (nonzero, the range of the action), couplings, Weyl amplitudes
_SAMPLES = [
    ([[3, 1, 0, 2], [1, 5, -1, 0], [0, -1, 2, 1], [2, 0, 1, 7]], F(1, 3), F(1), 2),
    ([[F(1, 2), 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], F(3, 4), F(1, 2), 0),
    ([[2, -1, 1, 0], [-1, 1, 0, 3], [1, 0, 4, -2], [0, 3, -2, 1]], F(2, 7), F(5, 3), -3),
]
_ETAS = [F(1, 4), F(1, 2), F(3, 8), F(5, 12), F(1, 8)]
_CS = [F(1), F(2), F(1, 2), F(3, 2)]


def check_clausius_on_the_action_shell_is_eta_equals_c_over_4g():
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    premise("synthesis.imported-einstein-cartan-matter-coupling")
    premise("synthesis.r-loc-independent-sets-matter-coupling")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for S, lam, G, wc in _SAMPLES:
        t = _tmap(S)
        R = _einstein_field(t, lam, G, wc)
        ok = ok and _on_shell(R, t, lam, G)
        ok = ok and (wc == 0 or any(v != {} for v in gtg.weyl_op(R).values()))
        for k in NULLS:
            ok = ok and gtg.vdot(k, k) == 0
            tkk = gtg.vdot(k, t(k))
            for eta in _ETAS:
                for c in _CS:
                    d = _defect(R, t, k, eta, c)
                    ok = ok and d == tkk * (1 - 4 * G * eta / c)
                    if tkk != 0:
                        ok = ok and ((d == 0) == (eta == c / (4 * G)))
            if tkk != 0:
                for c in _CS:
                    ok = ok and _defect(R, t, k, c / (4 * G), c) == 0
    GA.check("on the action's shell at coupling G the Clausius defect at period 2 pi c is t(k,k)(1 - 4 G eta / c)", ok)
    return ok


def _rank(rows):
    M = [list(r) for r in rows]
    rk, col, ncol = 0, 0, len(M[0])
    while rk < len(M) and col < ncol:
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col] / M[rk][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rk])]
        rk += 1
        col += 1
    return rk


_SYM = [(m, n) for m in range(4) for n in range(m, 4)]


def _basis(m, n):
    S = [[F(0)] * 4 for _ in range(4)]
    S[m][n] = F(1)
    S[n][m] = F(1)
    return _tmap(S)


def check_null_cone_values_fix_the_stress_up_to_the_metric():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    premise("synthesis.imported-gtg-dictionary")
    rows = [[gtg.vdot(k, _basis(m, n)(k)) for (m, n) in _SYM] for k in NULLS]
    ok = len(_SYM) == 10 and _rank(rows) == 9
    # the metric, t(b) = b, has t(k,k) = 0 at every null k, and is the kernel direction
    g = lambda b: b
    ok = ok and all(gtg.vdot(k, g(k)) == 0 for k in NULLS)
    gvec = [F(1) if (m, n) == (0, 0) else (F(-1) if m == n else F(0)) for (m, n) in _SYM]
    gS = [[F(0)] * 4 for _ in range(4)]
    for (m, n), v in zip(_SYM, gvec):
        gS[m][n] = v
        gS[n][m] = v
    ok = ok and all(_tmap(gS)(E[b]) == E[b] for b in range(4))
    ok = ok and all(sum((r[i] * gvec[i] for i in range(10)), F(0)) == 0 for r in rows)
    # a stress with a pure-pressure part off the metric (dust) is seen by some null k
    ok = ok and any(gtg.vdot(k, _tmap([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])(k)) != 0 for k in NULLS)
    GA.check("t(k,k) over null k has rank 9 on symmetric maps, kernel the metric", ok)
    return ok


def _esu(A):
    X = [J.var(i, F(0), 4, 2) for i in range(4)]
    f = (2 * F(A)) * (1 + X[1] * X[1] + X[2] * X[2] + X[3] * X[3]).inv()
    TH = [[J.const(0, 4) for _ in range(4)] for _ in range(4)]
    TH[0][0] = J.const(1, 4)
    for i in (1, 2, 3):
        TH[i][i] = f
    return gtg.Field(TH).curvature()


def _dust(sigma):
    return lambda b: gtg.m_scal(F(sigma) * gtg.vdot(b, E[0]), E[0])


def _forced_lambda(R):
    """Lambda from the gamma_1 equation (dust has t(gamma_1) = 0): G(gamma_1) + Lambda gamma_1 = 0."""
    g1 = gtg.einstein(R, E[1])
    return gtg.vdot(g1, E[1])


def check_stored_witness_is_on_the_shell_of_a_different_coupling():
    premise("synthesis.integrated-loc-curvature-clause-forced-matter-clause-independent")
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    premise("synthesis.imported-gtg-dictionary")
    R = _esu(2)
    lam = _forced_lambda(R)
    ok = lam == F(1, 4)
    ok = ok and gtg.einstein_residual(R, E[1], lam) == {}
    # witness: dust sigma = 1/4 solves the action's equations at G = 1/2, not at G = 1
    ok = ok and _on_shell(R, _dust(F(1, 4)), lam, F(1, 2))
    ok = ok and not _on_shell(R, _dust(F(1, 4)), lam, F(1))
    # at G = 1 the gamma_1 equation fixes Lambda for every dust density, so no Lambda rescues the witness
    for L in (F(1, 16), F(1, 8), F(1, 4), F(1, 2), F(1)):
        ok = ok and not _on_shell(R, _dust(F(1, 4)), L, F(1))
    # at G = 1 the radius-2 universe needs sigma = 1/8
    ok = ok and _on_shell(R, _dust(F(1, 8)), lam, F(1))
    # the witness's density is the joint relation at its own coupling, and is not 1/(4G) at G = 1
    for k in NULLS[:4]:
        ok = ok and _defect(R, _dust(F(1, 4)), k, F(1, 2), F(1)) == 0
        ok = ok and _defect(R, _dust(F(1, 4)), k, F(1, 4), F(1)) != 0
        ok = ok and _defect(R, _dust(F(1, 8)), k, F(1, 4), F(1)) == 0
    GA.check("the stored one-coupling witness solves the action only at G = 1/2; at G = 1 the radius-2 universe has eta = 1/4", ok)
    return ok


def _frw(a1, a2):
    at = J.from_taylor(0, [F(1), F(a1), F(a2) / 2], 4)
    TH = [[J.const(0, 4) for _ in range(4)] for _ in range(4)]
    TH[0][0] = J.const(1, 4)
    for i in (1, 2, 3):
        TH[i][i] = at
    return gtg.Field(TH).curvature()


def check_period_factor_is_fixed_only_where_matter_crosses():
    premise("synthesis.r-loc-independent-sets-matter-coupling")
    premise("synthesis.integrated-loc-curvature-clause-forced-matter-clause-independent")
    premise("synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part")
    ok = True
    # flat dust Friedmann-Lambda instant: a1 = 1, s = kappa rho = 3/2, Lambda = 3/2, a2 = -s/6 + Lambda/3 = 1/4
    s, lam, G = F(3, 2), F(3, 2), F(1)
    ok = ok and F(1) == (s + lam) / 3
    R = _frw(1, F(1, 4))
    t = _dust(s / (4 * G))
    ok = ok and _on_shell(R, t, lam, G)
    for k in NULLS:
        for c in _CS + [F(3)]:
            ok = ok and ((_defect(R, t, k, F(1, 4), c) == 0) == (c == 1))
    # de Sitter (s = 0, Lambda = 3, a1 = a2 = 1): the relation is empty
    Rd = _frw(1, 1)
    t0 = _dust(0)
    ok = ok and _on_shell(Rd, t0, F(3), G)
    for k in NULLS:
        for eta in _ETAS:
            for c in _CS:
                ok = ok and _defect(Rd, t0, k, eta, c) == 0
    GA.check("with eta = 1/4 on the action's shell the period factor is 1 where matter crosses and free on de Sitter", ok)
    return ok


def check_vacuum_weyl_field_leaves_the_relation_empty():
    premise("synthesis.loc-independent-of-clausius-and-killing-data")
    premise("synthesis.r-loc-independent-sets-matter-coupling")
    zero = _tmap([[0] * 4 for _ in range(4)])
    # (Lambda, Weyl amplitude, G) with tabulated scalar curvature 4 Lambda, Weyl value 4 w on gamma_0 ^ gamma_1,
    # and the dust control defect (1 - G)/2 at eta = 1/4, c = 1, sigma = 1/2, k = gamma_0 + gamma_1
    rows = ((F(1, 2), 1, F(1), F(2), F(4), F(0)),
            (F(3, 5), -2, F(2), F(12, 5), F(-8), F(-1, 2)),
            (F(2), F(1, 3), F(1, 2), F(8), F(4, 3), F(1, 4)))
    ok = True
    for lam, wc, G, sc, w01, dctl in rows:
        R = _einstein_field(zero, lam, G, wc)
        ok = ok and _on_shell(R, zero, lam, G)
        ok = ok and gtg.ricci_scalar(R) == sc
        ok = ok and gtg.weyl_op(R)[(0, 1)] == gtg.m_scal(w01, gtg.biv(0, 1))
        for k in NULLS:
            ok = ok and gtg.vdot(k, gtg.ricci(R, k)) == 0
            for eta in _ETAS:
                for c in _CS:
                    ok = ok and _defect(R, zero, k, eta, c) == 0
        # negative control: the same Lambda and Weyl part with dust at coupling G
        dust = _dust(F(1, 2))
        Rm = _einstein_field(dust, lam, G, wc)
        ok = ok and _on_shell(Rm, dust, lam, G)
        ok = ok and _defect(Rm, dust, NULLS[0], F(1, 4), 1) == dctl
    GA.check("on vacuum fields with Weyl part and Lambda the Clausius defect vanishes for every eta and c", ok)
    return ok
