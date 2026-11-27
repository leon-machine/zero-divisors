"""Null-plane data of the first-order gravitational field: exact checks.

Stored first-order curvature (Cl(1,3), signature (+,-,-,-)): R_p[h](B) = -1/2 p ^ h(B.p), Ricci map
Ric(a) = sum_b e^b . R(e_b ^ a), Einstein map G = Ric - 1/2 id tr Ric, on symmetric maps h. A symmetric map
is held as a matrix H with h(a) = sum H[m][n] (a.e_m) e_n. A constant-coefficient bilinear differential
identity holds for all fields exactly when its symbol identity holds for all vectors p1, p2 put in place of
the derivatives of the first and of the second field; the checks test the symbol identities.

Null plane N = {n.x = const}, n = e_0 + e_3, second null direction nbar = e_0 - e_3, transverse e_1, e_2.

(i)    the symplectic current of the first-order Einstein operator and its divergence;
(ii)   in the gauge h(n) = 0 its flux through N holds the two transverse trace-free components and a trace
       term of the opposite sign, and nothing else; the gauge is reached where n.p != 0; the equation along
       the generators is the first-order focusing equation;
(iii)  the focusing and shear equations of a null geodesic congruence, from the definition of the
       gravitational field: the Riccati equation, exactly, on a field that is not weak;
(iv)   the curvature form of the null datum is the rate of the first-order shear;
(v)    the second-order Lorentz-covariant operators on symmetric maps are five, those vanishing on
       displacements two, and the symmetric one is the Einstein map;
(vi)   the constant of the quadratic functional: the field of a body at rest solved exactly, its interaction
       matched to the stored Newtonian coupling, and the stored residue;
(vii)  the modes of a closed generator;
(viii) a rotation about the generator turns the two components by twice its angle.
"""
from fractions import Fraction as F

import GA
from GA import add, gen, mul, scal, sub
from tp_premise import premise
import gtg

D = 4
S = GA.sig(1, 3)
ETA = [1, -1, -1, -1]
E = [gen(i) for i in range(D)]
REC = [scal(ETA[i], E[i]) for i in range(D)]


def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x}


def dot(a, b):
    return GA.dot(a, b, S)


def g1(x):
    return {b: c for b, c in x.items() if len(b) == 1}


def wedge(a, b):
    return scal(F(1, 2), sub(mul(a, b, S), mul(b, a, S)))


def vdotB(a, B):
    return g1(scal(F(1, 2), sub(mul(a, B, S), mul(B, a, S))))


def upper(v):
    return [F(ETA[i]) * dot(v, E[i]) for i in range(D)]


def apply(H, a):
    out = {}
    for m in range(D):
        am = dot(a, E[m])
        if am == 0:
            continue
        for k in range(D):
            if H[m][k]:
                out = add(out, scal(am * H[m][k], E[k]))
    return out


def riem(H, p, B):
    return scal(F(-1, 2), wedge(p, apply(H, GA.neg(vdotB(p, B)))))


def trace(M):
    return sum(ETA[a] * M[a][a] for a in range(D))


def einstein(H, p):
    R = [[F(0)] * D for _ in range(D)]
    for m in range(D):
        img = {}
        for b in range(D):
            img = add(img, vdotB(REC[b], riem(H, p, wedge(E[b], REC[m]))))
        for k in range(D):
            R[m][k] = dot(img, REC[k])
    t = trace(R)
    return [[R[m][k] - (F(1, 2) * t * ETA[m] if m == k else 0) for k in range(D)] for m in range(D)]


def pair(A, B):
    return sum(ETA[a] * ETA[k] * A[a][k] * B[a][k] for a in range(D) for k in range(D))


def tr_map(H):
    return sum(dot(REC[a], apply(H, E[a])) for a in range(D))


def outer(x, y):
    """the symmetric map a -> (a.x) y + (a.y) x."""
    xu, yu = upper(x), upper(y)
    return [[xu[m] * yu[k] + yu[m] * xu[k] for k in range(D)] for m in range(D)]


def madd(A, B, c=1):
    return [[A[m][k] + c * B[m][k] for k in range(D)] for m in range(D)]


def mscal(c, A):
    return [[c * x for x in row] for row in A]


ZERO = [[F(0)] * D for _ in range(D)]
N = vec([1, 0, 0, 1])
NBAR = vec([1, 0, 0, -1])
M1 = vec([0, 1, 0, 0])
M2 = vec([0, 0, 1, 0])
NPLUS = mscal(F(1, 2), madd(outer(M1, M1), outer(M2, M2), -1))      # a -> (a.m1) m1 - (a.m2) m2
NCROSS = outer(M1, M2)                                              # a -> (a.m1) m2 + (a.m2) m1
GAUGE_BASIS = [outer(N, N), outer(N, M1), outer(N, M2), outer(M1, M1), outer(M1, M2), outer(M2, M2)]

# sample symbols: fixed integer data, generic (no vanishing invariant used below)
SYM = [[3, -1, 2, 5, 4, -2, 1, -3, 2, 1], [-2, 4, 1, -1, 3, 2, -5, 1, 4, -3],
       [1, 2, -3, 4, -1, 5, 2, -2, 3, 1], [5, -3, 1, 2, -4, 1, 3, 2, -1, 4]]
VECS = [(2, 1, -1, 3), (1, -2, 3, 4), (3, 2, 1, -1), (-1, 4, 2, 1), (4, -1, -3, 1)]
GAUGE = [[2, -1, 3, 4, 1, -2], [-3, 2, 1, -1, 5, 3], [1, 4, -2, 3, -1, 2], [5, 1, 2, -2, 3, -4]]


def sym(c):
    H = [[F(0)] * D for _ in range(D)]
    i = 0
    for m in range(D):
        for k in range(m, D):
            H[m][k] = H[k][m] = F(c[i])
            i += 1
    return H


def gauged(c):
    H = ZERO
    for x, B in zip(c, GAUGE_BASIS):
        H = madd(H, B, F(x))
    return H


def omega(H1, p1, H2, p2):
    """symbol of the symplectic current: derivatives of the first field -> p1, of the second -> p2."""
    t1, t2 = tr_map(H1), tr_map(H2)
    w = scal(F(1, 2) * pair(H1, H2), sub(p1, p2))
    w = add(w, scal(F(1, 2), sub(scal(t1, apply(H2, p1)), scal(t2, apply(H1, p2)))))
    w = add(w, scal(F(1, 2), sub(scal(t2, apply(H1, p1)), scal(t1, apply(H2, p2)))))
    w = add(w, sub(apply(H1, apply(H2, p2)), apply(H2, apply(H1, p1))))
    w = add(w, scal(F(-1, 2) * t1 * t2, sub(p1, p2)))
    return w


def tt(H):
    """the two transverse trace-free components: H = h1 NPLUS + h2 NCROSS + ..."""
    return pair(H, NPLUS) * F(1, 2), pair(H, NCROSS) * F(1, 2)


def check_symplectic_current_of_the_first_order_einstein_operator():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    premise("synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints")
    ok, count, nonzero = True, 0, 0
    for i, c1 in enumerate(SYM):
        for j, c2 in enumerate(SYM):
            if i == j:
                continue
            H1, H2 = sym(c1), sym(c2)
            p1, p2 = vec(VECS[i]), vec(VECS[(i + j + 1) % 5])
            lhs = dot(add(p1, p2), omega(H1, p1, H2, p2))
            rhs = pair(einstein(H1, p1), H2) - pair(H1, einstein(H2, p2))
            ok = ok and lhs == rhs
            nonzero += 1 if rhs != 0 else 0
            # antisymmetry of the current under exchange of the two fields
            ok = ok and GA.is_zero(add(omega(H1, p1, H2, p2), omega(H2, p2, H1, p1)))
            count += 1
    # the Einstein map is symmetric for the pairing at equal momentum (the stored clause (ii))
    for i in range(3):
        H1, H2, p = sym(SYM[i]), sym(SYM[i + 1]), vec(VECS[i])
        ok = ok and pair(einstein(H1, p), H2) == pair(H1, einstein(H2, p))
    ok = ok and count == 12 and nonzero == 12
    GA.check("(i) (p1 + p2).omega = <G_p1 h1, h2> - <h1, G_p2 h2> for twelve pairs of symbols, both sides "
             "nonzero; omega antisymmetric; G symmetric for the pairing at equal momentum", ok)
    return ok


def check_flux_through_the_null_plane_in_the_gauge():
    premise("synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints")
    ok = all(GA.is_zero(apply(B, N)) for B in GAUGE_BASIS)
    ok = ok and pair(NPLUS, NPLUS) == 2 and pair(NCROSS, NCROSS) == 2 and pair(NPLUS, NCROSS) == 0
    ok = ok and tr_map(NPLUS) == 0 and tr_map(NCROSS) == 0
    count = 0
    for i, c1 in enumerate(GAUGE):
        for j, c2 in enumerate(GAUGE):
            if i == j:
                continue
            H1, H2 = gauged(c1), gauged(c2)
            p1, p2 = vec(VECS[i]), vec(VECS[(i + j + 1) % 5])
            a1, b1 = tt(H1)
            a2, b2 = tt(H2)
            t1, t2 = tr_map(H1), tr_map(H2)
            flux = dot(N, omega(H1, p1, H2, p2))
            want = F(1, 2) * (dot(N, p1) - dot(N, p2)) * (2 * a1 * a2 + 2 * b1 * b2 - F(1, 2) * t1 * t2)
            ok = ok and flux == want and flux != 0
            # the components along n (the maps n(x)n, n(x)m1, n(x)m2) do not enter
            H1b = madd(H1, madd(outer(N, N), madd(outer(N, M1), outer(N, M2), 3), -2), 7)
            ok = ok and dot(N, omega(H1b, p1, H2, p2)) == flux
            count += 1
    ok = ok and count == 12
    GA.check("(ii) in the gauge h(n) = 0, n.omega = 1/2 (n.p1 - n.p2)(<h1TT, h2TT> - 1/2 tr h1 tr h2): the two "
             "transverse trace-free components and a trace term of the opposite sign, no component along n, "
             "no transverse momentum (twelve pairs)", ok)
    return ok


def check_gauge_is_reachable_and_the_generator_equation_is_first_order_focusing():
    premise("synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints")
    ok = True
    # displacements a -> (a.p) xi + (a.xi) p: the map xi -> disp(n) = (n.p) xi + (n.xi) p has rank 4 exactly
    # when n.p != 0, and rank 1 when n.p = 0
    for pc, want in (((2, 1, -1, 3), 4), ((1, -2, 3, 4), 4), ((3, 1, 2, 3), 1), ((5, 0, 0, 5), 1)):
        p = vec(pc)
        rows = [upper(apply(outer(p, E[j]), N)) for j in range(D)]
        ok = ok and GA.mat_rank([list(r) for r in rows]) == want
        ok = ok and (dot(N, p) != 0) == (want == 4)
    # n . G_p[h](n) = 1/2 (n.p)^2 tr h in the gauge: with theta = 1/2 d_n tr h this is d_n theta = n . Ric(n)
    seen = 0
    for i, c in enumerate(GAUGE):
        H, p = gauged(c), vec(VECS[i])
        nn = dot(N, apply(einstein(H, p), N))
        ok = ok and nn == F(1, 2) * dot(N, p) ** 2 * tr_map(H)
        seen += 1 if nn != 0 else 0
    ok = ok and seen >= 3
    GA.check("(ii) the gauge h(n) = 0 is reached by one displacement exactly where n.p != 0; there "
             "n.G[h](n) = 1/2 (n.p)^2 tr h, the first-order focusing equation for theta = 1/2 d_n tr h", ok)
    return ok


def gauge_field_not_weak():
    """A gravitational field (hb, Omega) with hb^{-1} = id + s, s symmetric, s(n) = 0, s a polynomial in x
    (not small); Omega solved from the torsion equation. Returns the field and the label jets' point."""
    up = [upper(N), upper(M1), upper(M2)]
    maps = [[[up[i][m] * up[j][k] + up[j][m] * up[i][k] for k in range(D)] for m in range(D)]
            for i, j in ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2))]

    def hbinv(X):
        t, x, y, z = X
        v = t + z
        cs = [F(1, 7) * v * x, F(1, 5) * v, F(1, 11) * y, F(1, 6) * v + F(1, 10) * v * v,
              F(1, 8) * v + F(1, 12) * y * v, F(-1, 9) * v + F(1, 14) * x]
        H = [[sum((cs[i] * maps[i][m][k] for i in range(6)), gtg.Jet.const(0, D)) for k in range(D)]
             for m in range(D)]
        return [[(1 if mu == a else 0) + ETA[mu] * H[mu][a] for a in range(D)] for mu in range(D)]

    x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
    return gtg.field_from_hbinv(hbinv, x0, S, order=1)


def check_riccati_equation_of_the_generators_on_a_field_that_is_not_weak():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    fld = gauge_field_not_weak()
    ok = fld.torsion_free()
    # K = hb^T(grad phi), phi = n.x: K . gamma_a = n . hb(gamma_a); in this gauge K = n, and hb^{-1}(n) = n
    Hi = fld.hb_matrix()
    nlow = [dot(N, E[mu]) for mu in range(D)]
    K = {}
    for a in range(D):
        ka = sum(Hi[mu][a] * nlow[mu] for mu in range(D))          # K . gamma_a
        if ka:
            K = add(K, scal(ETA[a] * ka, E[a]))
    ok = ok and GA.eq(K, N) and GA.eq(fld.hb_inv(N), N) and dot(K, K) == 0
    Kc = upper(K)
    # B(A) = (A . D) K on the physical frame: Omega(hb(gamma_c)) x K, K having constant components
    Bj = [gtg.comm(fld.om[c], K, S) for c in range(D)]
    Bv = [gtg.m_val(b) for b in Bj]

    def B(v):
        out = {}
        for blade, co in v.items():
            out = add(out, scal(co, Bv[blade[0]]))
        return out

    # symmetric, B(K) = 0, K . B(A) = 0
    ok = ok and all(dot(E[a], Bv[b]) == dot(E[b], Bv[a]) for a in range(D) for b in range(D))
    ok = ok and GA.is_zero(B(K)) and all(dot(K, Bv[a]) == 0 for a in range(D))
    ok = ok and any(not GA.is_zero(Bv[a]) for a in range(D))
    # the Riccati equation (K.D B)(A) = -B(B(A)) - R(K ^ A) . K on the four frame vectors
    Rop = gtg.as_op(fld.curvature())
    omK = {}
    for c in range(D):
        if Kc[c]:
            omK = add(omK, scal(Kc[c], gtg.m_val(fld.om[c])))
    nonzero = 0
    for a in range(D):
        lhs = sub(fld.cov_phys(Kc, Bj[a]), B(gtg.comm(omK, E[a], S)))
        curv = gtg.bdot(Rop(wedge(K, E[a])), K, S)
        ok = ok and GA.eq(lhs, sub(GA.neg(B(Bv[a])), curv))
        nonzero += 0 if GA.is_zero(lhs) else 1
    ok = ok and nonzero == 4
    # trace: sum_a gamma^a . (R(K ^ gamma_a) . K) = -K . R(K), so d theta/d lambda = -tr B^2 + K . R(K)
    tr_curv = sum(dot(REC[a], gtg.bdot(Rop(wedge(K, E[a])), K, S)) for a in range(D))
    kRk = dot(K, gtg.ricci(Rop, K, S))
    ok = ok and tr_curv == -kRk and kRk != 0
    theta = gtg.Jet.const(0, D)
    for c in range(D):
        theta = theta + Bj[c].get((c,), gtg.Jet.const(0, D))
    dtheta = theta.d(0).v + theta.d(3).v                              # hb(K) = n: K . D = n . grad on scalars
    trB2 = sum(dot(REC[c], B(Bv[c])) for c in range(D))
    ok = ok and dtheta == -trB2 + kRk and theta.v != 0
    # screen: the physical vectors gamma_1, gamma_2 span K-perp modulo K; S = B there
    Sc = [[dot(REC[a], Bv[b]) for b in (1, 2)] for a in (1, 2)]
    th = theta.v
    ok = ok and Sc[0][0] + Sc[1][1] == th
    trS2 = Sc[0][0] ** 2 + 2 * Sc[0][1] * Sc[1][0] + Sc[1][1] ** 2
    ok = ok and trS2 == trB2
    sig = [[Sc[0][0] - F(1, 2) * th, Sc[0][1]], [Sc[1][0], Sc[1][1] - F(1, 2) * th]]
    sig2 = sig[0][0] ** 2 + 2 * sig[0][1] * sig[1][0] + sig[1][1] ** 2
    ok = ok and trB2 == F(1, 2) * th * th + sig2 and sig2 > 0
    # trace-free part of S^2 is theta sigma (two dimensions), so the shear equation follows from Riccati
    S2 = [[sum(Sc[i][k] * Sc[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            ok = ok and S2[i][j] - (F(1, 2) * trS2 if i == j else 0) == th * sig[i][j]
    # on the screen the Weyl map and the curvature give forms differing by a multiple of the product
    dif = {}
    for a, b in ((1, 1), (1, 2), (2, 2)):
        full = mul(wedge(K, E[b]), Rop(wedge(K, E[a])), S).get((), F(0))
        dif[(a, b)] = full - gtg.weyl_null(Rop, K, E[a], E[b], S)
    ok = ok and dif[(1, 2)] == 0 and dif[(1, 1)] == dif[(2, 2)]
    # the reading in the derived metric: 1/2 d_n g(a, b) = hb^{-1}(a) . B(hb^{-1}(b)) for background a, b
    gj = [[sum((ETA[c] * fld.TH[c][m] * fld.TH[c][k] for c in range(D)), gtg.Jet.const(0, D))
           for k in range(D)] for m in range(D)]
    gv = [gtg.m_val(x) for x in fld.g]
    seen = 0
    for m in range(D):
        for k in range(D):
            half = F(1, 2) * (gj[m][k].d(0).v + gj[m][k].d(3).v)
            ok = ok and half == dot(gv[m], B(gv[k]))
            seen += 1 if half != 0 else 0
    ok = ok and seen >= 4
    GA.check("(iii) on a field (hb, Omega) that is not weak, with K = hb^T(grad n.x) null: B(A) = A.D K is "
             "symmetric, B(K) = 0, K.B = 0; the Riccati equation (K.D B)(A) = -B^2(A) - R(K^A).K holds on the "
             "frame; its trace is d theta/d lambda = -tr B^2 + K.R(K), tr B^2 = theta^2/2 + <sigma, sigma>; "
             "and 1/2 d_n g(a, b) = hb^{-1}(a).B(hb^{-1}(b))", ok)
    return ok


def check_curvature_form_of_the_null_datum_is_the_rate_of_shear():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    ok, count = True, 0
    for i, c in enumerate(GAUGE):
        H, p = gauged(c), vec(VECS[i])
        np2 = dot(N, p) ** 2
        for u in (M1, M2):
            # n . R(n ^ u) = 1/2 (n.p)^2 h(u): twice the second derivative along n of the map 1/2 h on u
            ok = ok and GA.eq(vdotB(N, riem(H, p, wedge(N, u))), scal(F(1, 2) * np2, apply(H, u)))
        for a, b in ((M1, M1), (M1, M2), (M2, M2)):
            # (n ^ b) . R(n ^ a) = - d_n sigma(a, b), sigma(a, b) = 1/2 d_n h(a).b  (the stored shear equation)
            lhs = mul(wedge(N, b), riem(H, p, wedge(N, a)), S).get((), F(0))
            ok = ok and lhs == -F(1, 2) * np2 * dot(apply(H, a), b)
        # displacements do not change the curvature, so the datum does not depend on the gauge
        Hd = madd(H, outer(p, vec(VECS[(i + 2) % 5])), 5)
        ok = ok and not GA.is_zero(apply(Hd, N))
        for u in (M1, M2):
            ok = ok and GA.eq(riem(Hd, p, wedge(N, u)), riem(H, p, wedge(N, u)))
        count += 1
    ok = ok and count == 4
    # the stored first-order formula against the definition, sign included: the field hb^{-1} = id + s with
    # s = 1/4 (p.x)^2 h0 (derived metric a.b + 1/2 (p.x)^2 h0(a).b to first order) has, at x = 0, where
    # s and Omega vanish, the curvature R(gamma_a ^ gamma_b) = R_p[h0](e_a ^ e_b) exactly
    H0, pc = sym(SYM[0]), (2, 1, -1, 3)

    def hbinv(X):
        P = sum((F(ETA[mu] * pc[mu]) * X[mu] for mu in range(D)), gtg.Jet.const(0, D))
        q = F(1, 4) * P * P
        return [[(1 if mu == c else 0) + ETA[mu] * H0[mu][c] * q for c in range(D)] for mu in range(D)]

    fld = gtg.field_from_hbinv(hbinv, (F(0), F(0), F(0), F(0)), S, order=1)
    Rc = fld.curvature()
    planes = 0
    for (i, j), val in Rc.items():
        want = riem(H0, vec(pc), wedge(E[i], E[j]))
        ok = ok and GA.eq(val, want)
        planes += 0 if GA.is_zero(want) else 1
    ok = ok and fld.torsion_free() and planes == 6
    GA.check("(iv) n.R(n^u) = 1/2 (n.p)^2 h(u) on transverse u in the gauge, unchanged by displacements; "
             "(n^b).R(n^a) = -d_n sigma(a,b) with sigma = 1/2 d_n h, the first-order shear equation; the "
             "stored first-order curvature is the linear part of the definition's curvature, in its sign", ok)
    return ok


PRIME = 1000003


def rank_mod(rows, p):
    """rank over the integers modulo the prime p of sparse integer rows {column: entry}."""
    piv, r = {}, 0
    for row in rows:
        row = {j: c % p for j, c in row.items() if c % p}
        while row:
            j = min(row)
            if j in piv:
                c = row[j]
                for k, v in piv[j].items():
                    nv = (row.get(k, 0) - c * v) % p
                    if nv:
                        row[k] = nv
                    else:
                        row.pop(k, None)
            else:
                inv = pow(row[j], p - 2, p)
                piv[j] = {k: (v * inv) % p for k, v in row.items()}
                r += 1
                break
    return r


def five_maps(H, p):
    """the five second-order maps built from p and h with the product of the algebra:
    Q(p) h,  Q(p) tr(h) id,  (p.h(p)) id,  tr(h) (a -> (a.p) p),  a -> (a.p) h(p) + (a.h(p)) p."""
    Qp, t, hp = dot(p, p), tr_map(H), apply(H, p)
    ident = [[F(ETA[m]) if m == k else F(0) for k in range(D)] for m in range(D)]
    return [mscal(Qp, H), mscal(Qp * t, ident), mscal(dot(p, hp), ident),
            mscal(t * F(1, 2), outer(p, p)), outer(p, hp)]


def flat(M):
    return [M[m][k] for m in range(D) for k in range(D)]


def check_second_order_covariant_operators_and_the_einstein_map():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    ok = True
    # (a) every linear map h -> E_p[h] of symmetric maps, quadratic in p, that commutes with the rotors is a
    # combination of five. The form F(k, h, p, p) = <k, E_p[h]> has coefficients on triples of symmetric
    # pairs of frame vectors; a bivector G acts on a vector by the commutator product G x v, and invariance
    # under the six unit bivectors is a linear system whose rank modulo a prime bounds the rational rank below.
    prs = [(a, b) for a in range(D) for b in range(a, D)]
    index, basis = {}, []
    for P1 in prs:
        for P2 in prs:
            for P3 in prs:
                index[(P1, P2, P3)] = len(basis)
                basis.append((P1, P2, P3))
    ok = ok and len(basis) == 1000

    def canon(t6):
        return (tuple(sorted(t6[0:2])), tuple(sorted(t6[2:4])), tuple(sorted(t6[4:6])))

    rows = []
    for mu in range(D):
        for nu in range(mu + 1, D):
            G = mul(E[mu], E[nu], S)
            # G x e_a = sum_b X[a][b] e_b, computed with the product
            X = []
            for a in range(D):
                img = g1(scal(F(1, 2), sub(mul(G, E[a], S), mul(E[a], G, S))))
                X.append([F(ETA[b]) * dot(img, E[b]) for b in range(D)])
            for I in basis:
                t6 = list(I[0] + I[1] + I[2])
                row = {}
                for slot in range(6):
                    for b in range(D):
                        c = X[t6[slot]][b]
                        if c:
                            t = list(t6)
                            t[slot] = b
                            j = index[canon(t)]
                            row[j] = row.get(j, 0) + int(c)
                row = {j: c for j, c in row.items() if c}
                if row:
                    rows.append(row)
    nullity = len(basis) - rank_mod(rows, PRIME)
    ok = ok and nullity == 5
    # the five maps are linearly independent (so the space is exactly five-dimensional over the rationals)
    samples = [(sym(SYM[i]), vec(VECS[i])) for i in range(4)]
    vals = [[] for _ in range(5)]
    for H, p in samples:
        for i, M in enumerate(five_maps(H, p)):
            vals[i].extend(flat(M))
    ok = ok and GA.mat_rank([list(v) for v in vals]) == 5
    # the stored Einstein map is 1/2 (first) - 1/2 (second) + 1/2 (third) + 1/2 (fourth) - 1/2 (fifth)
    ein = (F(1, 2), F(-1, 2), F(1, 2), F(1, 2), F(-1, 2))
    for H, p in samples:
        acc = ZERO
        for c, M in zip(ein, five_maps(H, p)):
            acc = madd(acc, M, c)
        ok = ok and flat(acc) == flat(einstein(H, p))
    # (b) vanishing on displacements a -> (a.p) xi + (a.xi) p: three conditions, a two-dimensional family
    cond = []
    for i in range(4):
        p, xi = vec(VECS[i]), vec(VECS[(i + 2) % 5])
        Ms = [flat(M) for M in five_maps(outer(p, xi), p)]
        for comp in range(D * D):
            cond.append([Ms[k][comp] for k in range(5)])
    ok = ok and GA.mat_rank(cond) == 3
    ric = (F(1, 2), F(0), F(0), F(1, 2), F(-1, 2))       # the Ricci map
    trc = (F(0), F(1), F(-1), F(0), F(0))                # id times its trace
    for row in cond:
        ok = ok and sum(r * c for r, c in zip(row, ric)) == 0 and sum(r * c for r, c in zip(row, trc)) == 0
    # (c) symmetry for the pairing adds one condition; so does conservation E_p[h](p) = 0; each leaves the
    # multiples of the Einstein map
    symc, cons = list(cond), list(cond)
    for i in range(3):
        H1, H2, p = sym(SYM[i]), sym(SYM[i + 1]), vec(VECS[i])
        A, B = five_maps(H1, p), five_maps(H2, p)
        symc.append([pair(A[k], H2) - pair(H1, B[k]) for k in range(5)])
        for comp in range(D):
            cons.append([upper(apply(A[k], p))[comp] for k in range(5)])
    ok = ok and GA.mat_rank(symc) == 4 and GA.mat_rank(cons) == 4
    for row in symc + cons:
        ok = ok and sum(r * c for r, c in zip(row, ein)) == 0
    GA.check("(v) the maps of symmetric maps, quadratic in p, commuting with the rotors form a space of "
             "dimension five (1000 coefficients, six bivector generators, nullity five modulo a prime, five "
             "independent maps); those vanishing on displacements are the combinations of the Ricci map and "
             "id times its trace; symmetry for the pairing, or conservation, leaves the Einstein map", ok)
    return ok


def conserved_sources_at_n():
    """symmetric maps T with T(n) = 0: spanned by x(x)y with x, y orthogonal to n."""
    basis = [outer(N, N), outer(N, M1), outer(N, M2), outer(M1, M1), outer(M1, M2), outer(M2, M2)]
    out = []
    for c in ([1, 2, -1, 3, 2, -2], [2, -1, 3, 1, -3, 4], [-1, 3, 2, 2, 1, 5]):
        T = ZERO
        for x, B in zip(c, basis):
            T = madd(T, B, F(x))
        out.append(T)
    return out


def sym_units():
    out = []
    for m in range(D):
        for k in range(m, D):
            H = [[F(0)] * D for _ in range(D)]
            H[m][k] = F(1)
            H[k][m] = F(1)
            out.append(H)
    return out


def solve_field(T, k, c):
    """one symmetric map h with G_k[h] = -T/(4c), by exact elimination (free coefficients set to zero);
    None if the equation has no solution."""
    units = sym_units()
    cols = [flat(einstein(U, k)) for U in units]
    rhs = [-x * F(c.denominator, 4 * c.numerator) for x in flat(T)]
    M = [[cols[j][i] for j in range(len(units))] + [rhs[i]] for i in range(D * D)]
    piv, r = [], 0
    for col in range(len(units)):
        p = None
        for i in range(r, len(M)):
            if M[i][col] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = F(M[r][col].denominator, M[r][col].numerator)
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                fct = M[i][col]
                M[i] = [x - fct * y for x, y in zip(M[i], M[r])]
        piv.append(col)
        r += 1
    if any(row[-1] != 0 for row in M[r:]):
        return None
    H = ZERO
    for i, col in enumerate(piv):
        H = madd(H, units[col], M[i][-1])
    return H


def functional(h, T, k, c):
    """the functional c <h, E h> - 1/2 <h, T> on a wave of momentum k, where E acts as -G_k."""
    return -c * pair(h, einstein(h, k)) - F(1, 2) * pair(h, T)


def static_interaction(m1, m2, k, c):
    """the interaction of two bodies at rest from the values of the functional on the solutions."""
    T1 = mscal(m1 * F(1, 2), outer(E[0], E[0]))
    T2 = mscal(m2 * F(1, 2), outer(E[0], E[0]))
    T12 = madd(T1, T2)
    h1, h2, h12 = solve_field(T1, k, c), solve_field(T2, k, c), solve_field(T12, k, c)
    if h1 is None or h2 is None or h12 is None:
        return None, None, None
    cross = functional(h12, T12, k, c) - functional(h1, T1, k, c) - functional(h2, T2, k, c)
    return -cross, F(1, 2) * pair(T1, h2), (T1, T2, h1, h2)


def check_constant_from_the_newtonian_coupling_and_the_stored_residue():
    premise("field-theory.operator-newtonian-coupling")
    premise("synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints")
    ok = True
    # constants are held as multiples of 1/(pi G) (the functional) and of pi G (couplings)
    c0 = F(-1, 32)
    m1, m2 = F(3), F(5)
    k = vec((0, 1, 2, 2))
    ksq = -dot(k, k)
    ok = ok and ksq == 9
    V, half_pair, data = static_interaction(m1, m2, k, c0)
    ok = ok and V is not None
    T1, T2, h1, h2 = data
    ok = ok and GA.eq(apply(T1, E[0]), scal(m1, E[0])) and GA.is_zero(apply(T1, k))
    # the solution is a stationary point of the functional: no linear term in any direction
    for U in sym_units():
        ok = ok and -2 * c0 * pair(U, einstein(h2, k)) - F(1, 2) * pair(U, T2) == 0
    # the interaction is 1/2 <T1, h[T2]>, and it does not see displacements of h
    ok = ok and V == half_pair
    ok = ok and F(1, 2) * pair(T1, madd(h2, outer(k, vec((2, -1, 3, 1))), 7)) == V
    # hypothesis (N): the transform of -G m1 m2/r is -4 pi G m1 m2/|k|^2; it is met exactly at c = -1/(32 pi G)
    ok = ok and V * ksq == -4 * m1 * m2
    for other in (F(-1, 16), F(-1, 64), F(1, 32)):
        Vo = static_interaction(m1, m2, k, other)[0]
        ok = ok and Vo is not None and Vo * ksq != -4 * m1 * m2
    # the field of the body: h = 16 pi G (T - 1/2 id tr T)/Q up to a displacement, and G_k[h] = 8 pi G T
    ident = [[F(ETA[m]) if a == m else F(0) for a in range(D)] for m in range(D)]
    closed = mscal(F(16, 1) * F(-1, 9), madd(T2, mscal(F(1, 2) * tr_map(T2), ident), -1))
    ok = ok and flat(einstein(closed, k)) == [8 * x for x in flat(T2)]
    ok = ok and flat(einstein(madd(h2, closed, -1), k)) == [F(0)] * (D * D)
    # off the cone, sources with transverse trace-free parts: p = (2, 0, 0, 1), Q(p) = 3, e_1, e_2 orthogonal to p
    p = vec((2, 0, 0, 1))
    Qp = dot(p, p)
    ok = ok and Qp == 3
    for eps in (NPLUS, NCROSS):
        ok = ok and GA.is_zero(apply(eps, p)) and flat(einstein(eps, p)) == [F(1, 2) * Qp * x for x in flat(eps)]
    xs = [vec((1, 0, 0, 2)), M1, M2]
    ok = ok and all(dot(x, p) == 0 for x in xs)
    srcs = []
    for cf in ([1, 2, -1, 3, 2, -2], [2, -1, 3, 1, -3, 4], [-1, 3, 2, 2, 1, 5]):
        T = ZERO
        i = 0
        for a in range(3):
            for b in range(a, 3):
                T = madd(T, outer(xs[a], xs[b]), F(cf[i]))
                i += 1
        srcs.append(T)
    seen = 0
    for Ta in srcs:
        for Tb in srcs:
            hb_ = solve_field(Tb, p, c0)
            ok = ok and hb_ is not None
            bform = pair(Ta, Tb) - F(1, 2) * tr_map(Ta) * tr_map(Tb)
            # interaction 8 pi G B/Q, and each component obeys Q h_i = 8 pi G <eps_i, T>
            ok = ok and F(1, 2) * pair(Ta, hb_) * Qp == 8 * bform
            ok = ok and Qp * F(1, 2) * pair(hb_, NPLUS) == 8 * pair(NPLUS, Tb)
            ok = ok and Qp * F(1, 2) * pair(hb_, NCROSS) == 8 * pair(NCROSS, Tb)
            seen += 1 if bform != 0 else 0
    ok = ok and seen >= 6
    # at a null momentum the stored form B is the sum of the two half-squares (the stored clause (iv)): the
    # residue of the exchange of the two components, 8 pi G times that sum, is the stored residue 8 pi G B
    Ts = conserved_sources_at_n()
    seen = 0
    for i in range(3):
        for j in range(3):
            S1, S2 = Ts[i], Ts[j]
            bform = pair(S1, S2) - F(1, 2) * tr_map(S1) * tr_map(S2)
            sq = pair(S1, NPLUS) * pair(S2, NPLUS) + pair(S1, NCROSS) * pair(S2, NCROSS)
            ok = ok and bform == F(1, 2) * sq
            seen += 1 if bform != 0 else 0
    ok = ok and seen >= 6
    GA.check("(vi) solving G_k[h] = -T/(4c) exactly for bodies at rest, the interaction read from the functional "
             "is 1/2 <T1, h[T2]>, blind to displacements, and equals -4 pi G m1 m2/|k|^2 at c = -1/(32 pi G) and "
             "not at three other values; then G_k[h] = 8 pi G T; off the cone the interaction is 8 pi G B/Q and "
             "each component obeys Q h_i = 8 pi G <eps_i, T>; at null momentum B is the stored sum of half-squares", ok)
    return ok


def fourier(a, b):
    """h(lam) = sum_k a_k cos(k lam) + b_k sin(k lam), k = 1..len(a)."""
    return (list(a), list(b))


def deriv(f):
    a, b = f
    return ([F(k + 1) * b[k] for k in range(len(a))], [-F(k + 1) * a[k] for k in range(len(a))])


def integral_over_pi(f, g):
    """the integral over [0, 2 pi] of f g, divided by pi (cos^2 and sin^2 integrate to pi)."""
    return sum(f[0][k] * g[0][k] + f[1][k] * g[1][k] for k in range(len(f[0])))


def check_modes_on_a_closed_generator():
    premise("field-theory.fock-space-maxwell-modes")
    ok = True
    r = F(3, 7)                                  # s/G: transverse cell area over Newton's constant
    # one component h_i on one generator, levels k = 1, 2, 3; h = h_i n_i has <h, h'> = 2 h_i h_i'
    f = fourier([F(2), F(-1), F(3)], [F(1), F(4), F(-2)])
    g = fourier([F(-3), F(2), F(1)], [F(5), F(-1), F(2)])
    # symplectic form: (1/16 pi G) s int (<h, d h'> - <d h, h'>)/2 = (s/8 pi G) int h_i d h_i'
    form = r * F(1, 8) * integral_over_pi(f, deriv(g))
    want = r * F(1, 8) * sum((k + 1) * (f[0][k] * g[1][k] - f[1][k] * g[0][k]) for k in range(3))
    ok = ok and form == want and form != 0
    # null energy: s int (1/32 pi G) <d h, d h> = (s/16 pi G) int (d h_i)^2 = (s/16 G) sum k^2 (a^2 + b^2)
    P = r * F(1, 16) * integral_over_pi(deriv(f), deriv(f))
    ok = ok and P == r * F(1, 16) * sum((k + 1) ** 2 * (f[0][k] ** 2 + f[1][k] ** 2) for k in range(3))
    ok = ok and P > 0
    # the translation lam -> lam + t has velocity X = d f; form(X, Y) = dP(Y) for every Y
    X = deriv(f)
    dP = r * F(1, 8) * integral_over_pi(deriv(f), deriv(g))
    ok = ok and r * F(1, 8) * integral_over_pi(X, deriv(g)) == dP
    ok = ok and X[0] == [F(1), F(8), F(-6)] and X[1] == [F(-2), F(2), F(-9)]
    # bracket {a_k, b_k} = 8 G/(s k); with [ , ] = U { , }, U^2 = -1, and alpha_k = (s/16G)^(1/2) k (a_k + U b_k):
    # [alpha, alpha*] = (s/16G) k^2 (-2 U [a, b]) = (s/16G) k^2 * 2 * 8G/(s k) = k
    U = GA.qi(0, 1)
    for k in (1, 2, 3, 5):
        br = F(8, 1) * F(r.denominator, r.numerator * k)                 # {a_k, b_k}
        comm_ab = U * GA.qi(br, 0)                                       # [a_k, b_k]
        val = GA.qi(r * F(1, 16) * k * k, 0) * (GA.qi(-2, 0) * U * comm_ab)
        ok = ok and val == GA.qi(k, 0)
        # [P, alpha_k] = -k alpha_k: [P, a] = -U k b, [P, b] = U k a from P = (s/16G) k^2 (a^2 + b^2)
        pa = GA.qi(r * F(1, 16) * k * k * 2, 0) * (GA.qi(-1, 0) * comm_ab)   # coefficient of b in [P, a]
        pb = GA.qi(r * F(1, 16) * k * k * 2, 0) * comm_ab                    # coefficient of a in [P, b]
        ok = ok and pa == GA.qi(-k, 0) * U and pb == GA.qi(k, 0) * U
        # then [P, a + U b] = -U k b + U (U k a) = -k (a + U b)
        ok = ok and U * pb == GA.qi(-k, 0)
        # with the other orientation of the unit in rule and modes the value is again +k
        Ub = GA.qi(0, -1)
        ok = ok and GA.qi(r * F(1, 16) * k * k, 0) * (GA.qi(-2, 0) * Ub * (Ub * GA.qi(br, 0))) == GA.qi(k, 0)
    GA.check("(vii) on a closed generator the flux is (s/8G) sum k (a b' - b a'), the null energy "
             "(s/16G) sum k^2 (a^2 + b^2) generates the translations, {a_k, b_k} = 8G/(s k), and "
             "alpha_k = (s/16G)^(1/2) k (a_k + U b_k) has [alpha_k, alpha_k*] = k, [P, alpha_k] = -k alpha_k", ok)
    return ok


def check_rotation_about_the_generator_turns_the_two_components_by_twice_the_angle():
    premise("synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints")
    ok = True
    # rotor R = 2 + e_1 e_2 (unnormalised, R R~ = 5): u -> R u R~/5 rotates the transverse plane by phi with
    # cos phi = 3/5, sin phi = 4/5
    Jp = mul(gen(1), gen(2), S)
    R = add(GA.sc(2), Jp)
    Rt = GA.reverse(R)
    ok = ok and GA.eq(mul(R, Rt, S), GA.sc(5))

    def rot(v):
        return g1(scal(F(1, 5), mul(mul(R, v, S), Rt, S)))

    def rotinv(v):
        return g1(scal(F(1, 5), mul(mul(Rt, v, S), R, S)))

    r1, r2 = rot(M1), rot(M2)
    ok = ok and GA.eq(r1, add(scal(F(3, 5), M1), scal(F(4, 5), M2)))
    ok = ok and GA.eq(r2, add(scal(F(-4, 5), M1), scal(F(3, 5), M2)))
    ok = ok and GA.eq(rot(N), N) and GA.eq(rot(NBAR), NBAR)

    def rotate_map(H):
        """h -> (a -> R h(R~ a R) R~)."""
        out = [[F(0)] * D for _ in range(D)]
        for m in range(D):
            img = rot(apply(H, rotinv(REC[m])))
            # H'[m][k] is the coefficient of (a.e_m) e_k: h'(e^m) = sum_k H'[m][k] e_k
            for k in range(D):
                out[m][k] = dot(img, REC[k])
        return out

    c2, s2 = F(-7, 25), F(24, 25)
    for h1, h2, t in ((F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(3), F(-2), F(5))):
        H = madd(madd(mscal(h1, NPLUS), NCROSS, h2), madd(outer(M1, M1), outer(M2, M2)), t)
        Hr = rotate_map(H)
        a, b = tt(Hr)
        ok = ok and a == c2 * h1 - s2 * h2 and b == s2 * h1 + c2 * h2
        ok = ok and tr_map(Hr) == tr_map(H)
        # the combinations h1 -+ U h2 are multiplied by cos 2phi -+ U sin 2phi (the two helicities)
        U = GA.qi(0, 1)
        z = GA.qi(c2, 0) + U * GA.qi(s2, 0)
        zb = GA.qi(c2, 0) + U * GA.qi(-s2, 0)
        ok = ok and GA.qi(a, 0) + U * GA.qi(b, 0) == z * (GA.qi(h1, 0) + U * GA.qi(h2, 0))
        ok = ok and GA.qi(a, 0) + U * GA.qi(-b, 0) == zb * (GA.qi(h1, 0) + U * GA.qi(-h2, 0))
    ok = ok and c2 == F(3, 5) ** 2 - F(4, 5) ** 2 and s2 == 2 * F(3, 5) * F(4, 5)
    # beta_+- = 2^(-1/2) (alpha_1 +- U alpha_2) with [alpha_i, alpha_j*] = k delta_ij and (U alpha)* = -U alpha*:
    # [beta_+, beta_-*] = 1/2 (k + U U k) = 0, [beta_+-, beta_+-*] = 1/2 (k - U U k) = k
    U = GA.qi(0, 1)
    for k in (1, 2, 5):
        kk = GA.qi(k, 0)
        ok = ok and GA.qi(F(1, 2), 0) * (kk + U * U * kk) == GA.qi(0, 0)
        ok = ok and GA.qi(F(1, 2), 0) * (kk - U * U * kk) == kk
        ok = ok and GA.qi(F(1, 2), 0) * (kk - (U * GA.qi(-1, 0)) * (U * GA.qi(-1, 0)) * kk) == kk
    GA.check("(viii) the rotation about the generator by phi (cos phi = 3/5) fixes n and nbar and turns the two "
             "transverse trace-free components by 2 phi (cos 2 phi = -7/25): h1 +- U h2 are multiplied by "
             "cos 2phi +- U sin 2phi; the trace is unchanged", ok)
    return ok
