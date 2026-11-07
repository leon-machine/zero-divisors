"""pairing.loop-classes-are-weyl-components: exact checks.

The vacuum curvature operators at a point are the algebraic Weyl maps of Cl(1,3) (GA.py, (+,-,-,-)): the
10-dimensional exact kernel of symmetry, Ricci trace-freeness d_a . W(a ^ b) = 0 and first Bianchi; for a
vacuum field calR = W. The loop bivector is R(u, v) = -calR(u ^ v) (LDG sign) and
C(u, v, w, z) = <R(u, v) . w, z>, bilinear over span{1, I5} (I5 the central unit of Cl(2,3), carried as pairs).
Unit tetrad l = e0 + e1, n = (e0 - e1)/2 (l . n = 1), m = (e2 + I5 e3)/sqrt 2 (m . mbar = -1); computed with
m0 = e2 + I5 e3 and the powers of sqrt 2 cleared, so every identity below is exact. Psi0 = C(l, m, l, m), Psi1 = C(l, n, l, m),
Psi2 = C(l, m, mbar, n), as in the premise Fact. Computed:
(1) on all 10 basis Weyl maps and on a generic combination: the classes C(u, v, l, m) of the six tetrad
    loops are Psi0, 0, -Psi1, Psi1, 0, -Psi2 for (l, m), (l, mbar), (m, mbar), (l, n), (n, m), (n, mbar);
(2) on the Weyl space, the joint kernel of the three null-cone classes ((l, m), (l, mbar), (m, mbar)) equals
    that of {Psi0, Psi1} (both of real codimension 4), and on it the (l, n) and (n, m) classes vanish and
    the (n, mbar) class is -Psi2;
(3) the Schwarzschild operator (M/2r^3)(B + 3 sigma_r B sigma_r) (store sign; sigma_r = e0 e1 the radial
    plane) is a Weyl map with Psi0 = Psi1 = Psi3 = Psi4 = 0 and Psi2 = -M/r^3 in the unit tetrad, so l is a
    repeated principal null direction and every loop in its null cone has zero class;
(4) the proof's GTG steps: C(u, v, w, z) = -W(u ^ v) . (w ^ z), the trace d_a . X(a ^ u) read in the null
    tetrad's reciprocal frame (equal for every bivector map X, zero on the Weyl maps), the pair symmetry, and
    the six classes in the tetrad with l . n = 2, m . mbar = -2.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


# ---- algebraic Weyl maps on the bivectors of a four-dimensional signature (exact) ----
BLADES2 = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def wop(X, B, sq):
    """Apply the bivector map with matrix X (X[i][j] = blade_i coefficient of W(blade_j)) to bivector B."""
    out = {}
    for j, bl in enumerate(BLADES2):
        c = B.get(bl, F(0))
        if c:
            out = GA.add(out, {BLADES2[i]: c * X[i][j] for i in range(6) if X[i][j]})
    return out


def wedge_vb(a, B, sq):
    return {k: v for k, v in GA.scal(F(1, 2), GA.add(GA.mul(a, B, sq), GA.mul(B, a, sq))).items() if len(k) == 3}


def dot_vb(a, B, sq):
    return {k: v for k, v in GA.scal(F(1, 2), GA.sub(GA.mul(a, B, sq), GA.mul(B, a, sq))).items() if len(k) == 1}


def weyl_constraints(X, sq):
    """Linear constraints of an algebraic Weyl map: symmetry, Ricci trace-free, first Bianchi."""
    rows = []
    for i in range(6):
        for j in range(i + 1, 6):
            A, B = {BLADES2[i]: F(1)}, {BLADES2[j]: F(1)}
            rows.append(GA.mul(A, wop(X, B, sq), sq).get((), F(0)) - GA.mul(wop(X, A, sq), B, sq).get((), F(0)))
    for nu in range(4):
        tr, bi = {}, {}
        for mu in range(4):
            if mu == nu:
                continue
            Bmn = GA.mul(GA.gen(mu), GA.gen(nu), sq)
            WB = wop(X, Bmn, sq)
            recip = GA.scal(F(1) / sq[mu], GA.gen(mu))
            tr = GA.add(tr, dot_vb(recip, WB, sq))
            bi = GA.add(bi, wedge_vb(recip, WB, sq))
        rows.extend(tr.get((k,), F(0)) for k in range(4))
        rows.extend(bi.get(t, F(0)) for t in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)])
    return rows


def weyl_space(sq):
    """Basis of the algebraic Weyl maps (6 x 6 matrices) of the signature sq, by an exact kernel."""
    cols = []
    for i in range(6):
        for j in range(6):
            X = [[F(1) if (a, b) == (i, j) else F(0) for b in range(6)] for a in range(6)]
            cols.append(weyl_constraints(X, sq))
    mat = [list(r) for r in zip(*cols)]
    return [[[v[6 * i + j] for j in range(6)] for i in range(6)] for v in GA.field_kernel(mat)]


def op_matrix(fn):
    """6 x 6 matrix of a bivector map given as a function on Fraction bivectors."""
    cols = [fn({bl: F(1)}) for bl in BLADES2]
    return [[cols[j].get(BLADES2[i], F(0)) for j in range(6)] for i in range(6)]


S = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]
LV = (GA.add(E[0], E[1]), {})
NV2 = (GA.scal(F(1, 2), GA.sub(E[0], E[1])), {})
M0 = (E[2], E[3])
MB0 = (E[2], GA.neg(E[3]))
GENERIC = [F(3), F(-1), F(2), F(1, 2), F(5), F(-4), F(1), F(7, 3), F(-2), F(1, 5)]
SCHW_K = [F(1, 8), F(-27, 2), F(4, 125)]                      # M/r^3 at sample points


def cwedge(u, v):
    def w(a, b):
        return GA.scal(F(1, 2), GA.sub(GA.mul(a, b, S), GA.mul(b, a, S)))
    return (GA.sub(w(u[0], v[0]), w(u[1], v[1])), GA.add(w(u[0], v[1]), w(u[1], v[0])))


def cdot(B, v):
    def d(Bx, a):
        return {k: c for k, c in GA.scal(F(1, 2), GA.sub(GA.mul(Bx, a, S), GA.mul(a, Bx, S))).items() if len(k) == 1}
    return (GA.sub(d(B[0], v[0]), d(B[1], v[1])), GA.add(d(B[0], v[1]), d(B[1], v[0])))


def cip(u, v):
    return GA.QI(GA.dot(u[0], v[0], S) - GA.dot(u[1], v[1], S), GA.dot(u[0], v[1], S) + GA.dot(u[1], v[0], S))


def C(X, u, v, w, z):
    B = cwedge(u, v)
    R = (GA.neg(wop(X, B[0], S)), GA.neg(wop(X, B[1], S)))
    return cip(cdot(R, w), z)


def scalars(X):
    """Classes and Weyl scalars with m = m0/sqrt 2, each multiplied by the power of sqrt 2 that clears it:
    returned values are exact; e.g. 'mmb' = 2 sqrt2 class(m, mbar), 'P1' = sqrt2 Psi1."""
    return {"lm": C(X, LV, M0, LV, M0), "P0": C(X, LV, M0, LV, M0),
            "lmb": C(X, LV, MB0, LV, M0), "mmb": C(X, M0, MB0, LV, M0),
            "ln": C(X, LV, NV2, LV, M0), "P1": C(X, LV, NV2, LV, M0),
            "nm": C(X, NV2, M0, LV, M0), "nmb": C(X, NV2, MB0, LV, M0), "P2": C(X, LV, M0, MB0, NV2),
            "P3": C(X, LV, NV2, MB0, NV2), "P4": C(X, NV2, MB0, NV2, MB0)}


def table_holds(X):
    s = scalars(X)
    return (s["lm"] == s["P0"] and s["lmb"] == 0 and s["mmb"] == -2 * s["P1"] and s["ln"] == s["P1"]
            and s["nm"] == 0 and s["nmb"] == -s["P2"])


def check_six_loop_classes():
    premise("pairing.imported-weyl-scalars-petrov-type-schwarzschild")
    premise("synthesis.imported-gtg-dictionary")
    Ws = weyl_space(S)
    gen = [[sum(c * X[i][j] for c, X in zip(GENERIC, Ws)) for j in range(6)] for i in range(6)]
    ok = len(Ws) == 10 and all(table_holds(X) for X in Ws) and table_holds(gen)
    s = scalars(gen)
    _tp_rv = (ok and s["P0"] != 0 and s["P1"] != 0 and s["P2"] != 0); assert _tp_rv is not False, "check_six_loop_classes"; return _tp_rv


def check_null_cone_classes_vanish_iff_repeated_pnd():
    premise("pairing.imported-weyl-scalars-petrov-type-schwarzschild")
    Ws = weyl_space(S)
    S_all = [scalars(X) for X in Ws]

    def rows(keys):
        out = []
        for k in keys:
            out.append([s[k].re for s in S_all])
            out.append([s[k].im for s in S_all])
        return out
    cone, psi = rows(["lm", "lmb", "mmb"]), rows(["P0", "P1"])
    ok = GA.field_rank(cone) == 4 and GA.field_rank(psi) == 4 and GA.field_rank(cone + psi) == 4
    ker = GA.field_kernel(cone)
    ok = ok and len(ker) == 6
    for v in ker:
        X = [[sum(c * W[i][j] for c, W in zip(v, Ws)) for j in range(6)] for i in range(6)]
        s = scalars(X)
        ok = ok and s["ln"] == 0 and s["nm"] == 0 and s["nmb"] == -s["P2"] and s["P0"] == 0 and s["P1"] == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_null_cone_classes_vanish_iff_repeated_pnd"; return _tp_rv


def check_schwarzschild_type_d():
    premise("pairing.imported-weyl-scalars-petrov-type-schwarzschild")
    ok = True
    sig_r = GA.mul(E[0], E[1], S)
    for k in SCHW_K:
        X = op_matrix(lambda B: GA.scal(k / 2, GA.add(B, GA.scal(3, GA.mul(GA.mul(sig_r, B, S), sig_r, S)))))
        ok = ok and all(c == 0 for c in weyl_constraints(X, S))
        s = scalars(X)
        ok = ok and s["P0"] == 0 and s["P1"] == 0 and s["P3"] == 0 and s["P4"] == 0
        ok = ok and s["P2"] == GA.QI(-2 * k)                # 2 Psi2 (two factors of m) = -2 M/r^3
        ok = ok and s["lm"] == 0 and s["lmb"] == 0 and s["mmb"] == 0 and table_holds(X)
    _tp_rv = (ok); assert _tp_rv is not False, "check_schwarzschild_type_d"; return _tp_rv


def _cscal(c, u):
    """A number c of span{1, I} (GA.QI) times a complex vector or bivector (re, im)."""
    return (GA.sub(GA.scal(c.re, u[0]), GA.scal(c.im, u[1])), GA.add(GA.scal(c.re, u[1]), GA.scal(c.im, u[0])))


def _cadd(*xs):
    return (GA.add(*[x[0] for x in xs]), GA.add(*[x[1] for x in xs]))


def _capply(X, B):
    return (wop(X, B[0], S), wop(X, B[1], S))


def _bdot_scalar(A, B):
    """A . B = <A B>_0 for complex bivectors."""
    re = GA.sub(GA.mul(A[0], B[0], S), GA.mul(A[1], B[1], S)).get((), F(0))
    im = GA.add(GA.mul(A[0], B[1], S), GA.mul(A[1], B[0], S)).get((), F(0))
    return GA.QI(re, im)


def _trace_flat(X, u, v):
    """v . (d_a . X(a ^ u)) with d_a = sum_mu e^mu (e_mu . d): the GTG contraction, orthonormal frame."""
    acc = ({}, {})
    for mu in range(4):
        rec = (GA.scal(F(1) / S[mu], E[mu]), {})
        W = _capply(X, cwedge((E[mu], {}), u))
        acc = _cadd(acc, _cscal(GA.QI(-1), cdot(W, rec)))      # c . B = -(B . c)
    return cip(acc, v)


def _trace_tetrad(X, tet, u, v):
    """sum_a C(f_a, u, f^a, v) over a null tetrad (l, n, m, mbar), reciprocal frame from its Gram data."""
    l, n, m, mb = tet
    lam, mu = cip(l, n), cip(m, mb)
    total = GA.QI(0)
    for fa, rec in ((l, _cscal(GA.QI(1) / lam, n)), (n, _cscal(GA.QI(1) / lam, l)),
                    (m, _cscal(GA.QI(1) / mu, mb)), (mb, _cscal(GA.QI(1) / mu, m))):
        total = total + C(X, fa, u, rec, v)
    return total


EXTRA_VEC = (GA.add(E[1], GA.scal(F(3), E[2])), GA.scal(F(2), E[0]))
ARBITRARY_MAP = [[F((7 * i + 3 * j) % 5 - 2) for j in range(6)] for i in range(6)]


def check_gtg_trace_and_pair_symmetry():
    """The proof's GTG steps: C(u, v, w, z) = -W(u ^ v) . (w ^ z); the trace d_a . W(a ^ u) = 0 read in the
    null tetrad's reciprocal frame (an identity for every bivector map, zero on the Weyl maps); the pair
    symmetry from the symmetry of W; and the six classes in the tetrad with l . n = 2, m . mbar = -2."""
    premise("pairing.imported-weyl-scalars-petrov-type-schwarzschild")
    premise("synthesis.imported-gtg-dictionary")
    Ws = weyl_space(S)
    ok = len(Ws) == 10
    N2 = (GA.sub(E[0], E[1]), {})                      # n with l . n = 2
    tet = (LV, N2, M0, MB0)
    ok = ok and cip(LV, N2) == GA.QI(2) and cip(M0, MB0) == GA.QI(-2)
    ok = ok and cip(M0, M0) == GA.QI(0) and cip(LV, M0) == GA.QI(0) and cip(N2, MB0) == GA.QI(0)
    vecs = [LV, N2, M0, MB0, EXTRA_VEC]
    arbitrary = ARBITRARY_MAP                          # not a Weyl map
    gen = [[sum(c * X[i][j] for c, X in zip(GENERIC, Ws)) for j in range(6)] for i in range(6)]
    for X in Ws + [gen, arbitrary]:
        weyl = X is not arbitrary
        for u in vecs:
            for v in vecs:
                t1, t2 = _trace_flat(X, u, v), _trace_tetrad(X, tet, u, v)
                ok = ok and t1 == t2 and (t1 == 0 or not weyl)
                for w in vecs[:2]:
                    for z in vecs[2:]:
                        lhs = C(X, u, v, w, z)
                        rhs = GA.QI(0) - _bdot_scalar(_capply(X, cwedge(u, v)), cwedge(w, z))
                        ok = ok and lhs == rhs
                        if weyl:
                            ok = ok and lhs == C(X, w, z, u, v)
    ok = ok and any(_trace_flat(arbitrary, u, v) != 0 for u in vecs for v in vecs)
    for X in Ws + [gen]:
        P0, P1, P2 = C(X, LV, M0, LV, M0), C(X, LV, N2, LV, M0), C(X, LV, M0, MB0, N2)
        cls = {("l", "m"): P0, ("l", "mb"): GA.QI(0), ("m", "mb"): GA.QI(0) - P1, ("l", "n"): P1,
               ("n", "m"): GA.QI(0), ("n", "mb"): GA.QI(0) - P2}
        T = {"l": LV, "n": N2, "m": M0, "mb": MB0}
        ok = ok and all(C(X, T[a], T[b], LV, M0) == w for (a, b), w in cls.items())
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_trace_and_pair_symmetry"; return _tp_rv
