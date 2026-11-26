"""A field equation linear in the curvature with a conserved source is Einstein's: exact checks.

Cl(1,3), signature (+,-,-,-). A curvature operator is a linear map of the bivectors, held as a 6 x 6 matrix
M on the blades e_i e_j (i < j): R(B_I) = sum_J M[J][I] B_J. A linear map of the vectors is a 4 x 4 matrix
Fm with F(e_k) = sum_m Fm[m][k] e_m. A bivector G acts on vectors and bivectors by the commutator product
G x X = (GX - XG)/2, on a curvature operator by (G.R)(B) = G x R(B) - R(G x B), and on a map of vectors by
(G.F)(a) = G x F(a) - F(G x a): the derivatives of the action of the rotors.

(ii)  the operators obeying the cyclic identity R(a^b).c + R(b^c).a + R(c^a).b = 0 form a space of dimension
      twenty, and each is symmetric; every one of them is the curvature at a point of some field (with (vii));
(iv)  the linear maps from that space to the maps of vectors that commute with the rotors form a space of
      dimension two, spanned by the Ricci map and the identity times the scalar; the maps of vectors fixed
      by the rotors are the multiples of the identity;
(i), (iii) on a gravitational field (hb, Omega) that is not weak, with Omega solved from the torsion equation:
      the cyclic identity, the differential identity on the frame, and its contraction,
      div Ric = 1/2 D(scalar), div G = 0;
(v)   the divergence of a Ric + b (scalar) id + l id is (a/2 + b) D(scalar);
(vii) at first order the Einstein map of the field is the stored first-order Einstein map. The constant of
      (vii) has no check here: it rests on the proof and on clause (vi) of the first-order result.
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
BL = [(i, j) for i in range(D) for j in range(i + 1, D)]
BV = [mul(E[i], E[j], S) for i, j in BL]
PRIME = 1000003


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def comm(x, y):
    return scal(F(1, 2), sub(mul(x, y, S), mul(y, x, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def wedge(a, b):
    return grade(comm(a, b), 2)


def op_apply(M, B):
    out = {}
    for I, bl in enumerate(BL):
        c = B.get(bl, F(0))
        if c:
            for J in range(6):
                if M[J][I]:
                    out = add(out, scal(c * M[J][I], BV[J]))
    return out


def unit_op(J, I):
    M = [[F(0)] * 6 for _ in range(6)]
    M[J][I] = F(1)
    return M


def cyclic(R, a, b, c):
    """R(a^b).c + R(b^c).a + R(c^a).b for a callable R on bivectors."""
    return add(grade(comm(R(wedge(a, b)), c), 1), grade(comm(R(wedge(b, c)), a), 1),
               grade(comm(R(wedge(c, a)), b), 1))


def cyclic_rows():
    rows = []
    for a in range(D):
        for b in range(a + 1, D):
            for c in range(b + 1, D):
                comp = [[F(0)] * 36 for _ in range(D)]
                for J in range(6):
                    for I in range(6):
                        M = unit_op(J, I)
                        z = cyclic(lambda B: op_apply(M, B), E[a], E[b], E[c])
                        for bl, co in z.items():
                            comp[bl[0]][J * 6 + I] = co
                rows.extend(comp)
    return rows


def nullspace(rows, n):
    """reduced basis of the kernel: basis vector j is 1 at free column free[j] and 0 at the other free columns."""
    M = [list(r) for r in rows]
    piv, r = [], 0
    for c in range(n):
        p = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = F(M[r][c].denominator, M[r][c].numerator)
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [F(0)] * n
        v[f] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][f]
        basis.append(v)
    return basis, free


def mat_of(v):
    return [[v[J * 6 + I] for I in range(6)] for J in range(6)]


def act_op(G, M):
    out = [[F(0)] * 6 for _ in range(6)]
    for I in range(6):
        img = sub(grade(comm(G, op_apply(M, BV[I])), 2), op_apply(M, grade(comm(G, BV[I]), 2)))
        for J, bl in enumerate(BL):
            out[J][I] = img.get(bl, F(0))
    return out


def map_apply(Fm, v):
    out = {}
    for bl, co in v.items():
        for m in range(D):
            if Fm[m][bl[0]]:
                out = add(out, {(m,): co * Fm[m][bl[0]]})
    return out


def act_map(G, Fm):
    out = [[F(0)] * D for _ in range(D)]
    for k in range(D):
        img = sub(grade(comm(G, map_apply(Fm, E[k])), 1), map_apply(Fm, grade(comm(G, E[k]), 1)))
        for m in range(D):
            out[m][k] = img.get((m,), F(0))
    return out


def ricci_of(M):
    """Ric(e_k) = sum_a e^a . R(e_a ^ e_k), as a 4 x 4 matrix, and its scalar."""
    Fm = [[F(0)] * D for _ in range(D)]
    for k in range(D):
        img = {}
        for a in range(D):
            img = add(img, grade(comm(REC[a], op_apply(M, wedge(E[a], E[k]))), 1))
        for m in range(D):
            Fm[m][k] = img.get((m,), F(0))
    return Fm, sum(Fm[k][k] for k in range(D))


def rank_mod(rows, p):
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


def to_mod(x, p):
    x = F(x)
    return (x.numerator * pow(x.denominator, p - 2, p)) % p


def check_operators_with_the_cyclic_identity_are_twenty_and_symmetric():
    rows = cyclic_rows()
    K, free = nullspace(rows, 36)
    ok = len(rows) == 16 and len(K) == 20 and GA.mat_rank(rows) == 16
    for v in K:
        M = mat_of(v)
        for I in range(len(BL)):
            for J in range(I + 1, len(BL)):
                lhs = mul(BV[I], op_apply(M, BV[J]), S).get((), F(0))
                rhs = mul(BV[J], op_apply(M, BV[I]), S).get((), F(0))
                ok = ok and lhs == rhs
        # the Ricci map of a member is symmetric
        Fm, _ = ricci_of(M)
        ok = ok and all(ETA[m] * Fm[m][k] == ETA[k] * Fm[k][m] for m in range(D) for k in range(D))
    # the space is stable under the bivectors
    stable = 0
    for G in BV:
        for v in K:
            N = act_op(G, mat_of(v))
            flat = [N[J][I] for J in range(6) for I in range(6)]
            ok = ok and all(sum(r[i] * flat[i] for i in range(36)) == 0 for r in rows)
            stable += 1
    ok = ok and stable == 120
    # of the 36 unit operators B_I -> B_J exactly the six with J = I satisfy the identity
    triples = [(a, b, c) for a in range(D) for b in range(a + 1, D) for c in range(b + 1, D)]
    inside = []
    for J in range(len(BL)):
        for I in range(len(BL)):
            U = unit_op(J, I)
            if all(GA.is_zero(cyclic(lambda B: op_apply(U, B), E[a], E[b], E[c])) for a, b, c in triples):
                inside.append((J, I))
    ok = ok and len(inside) == 6 and all(J == I for J, I in inside) and len(triples) == 4
    GA.check("(ii) the linear maps R of the bivectors with R(a^b).c + R(b^c).a + R(c^a).b = 0 form a space of "
             "dimension 20 (16 independent conditions on 36), stable under the bivectors; each is symmetric "
             "for the product of bivectors and has a symmetric Ricci map", ok)
    return ok


def check_covariant_linear_maps_of_curvature_operators_are_ricci_and_scalar():
    K, free = nullspace(cyclic_rows(), 36)
    nK = len(K)
    ok = nK == 20
    units = [[[F(1) if (m, k) == (mm, kk) else F(0) for k in range(D)] for m in range(D)]
             for mm in range(D) for kk in range(D)]
    eqs, exact = [], []
    for G in BV:
        rho = [act_map(G, U) for U in units]                 # G acting on the unit maps of vectors
        for j in range(nK):
            Gk = act_op(G, mat_of(K[j]))
            c = [Gk[f // 6][f % 6] for f in free]             # coefficients of G.k_j on the reduced basis
            # G.k_j lies in the space: it is reproduced by those coefficients
            back = [sum(c[i] * K[i][q] for i in range(nK)) for q in range(36)]
            ok = ok and back == [Gk[q // 6][q % 6] for q in range(36)]
            ok = ok and all(x.denominator % PRIME != 0 for x in c)
            for m in range(D):
                for k in range(D):
                    row = {}
                    for i in range(nK):
                        if c[i]:
                            row[i * 16 + m * 4 + k] = c[i]
                    for u in range(16):
                        r = rho[u][m][k]
                        if r:
                            key = j * 16 + u
                            row[key] = row.get(key, F(0)) - r
                    row = {a: b for a, b in row.items() if b}
                    if row:
                        exact.append(row)
                        eqs.append({a: to_mod(b, PRIME) for a, b in row.items()})
    nullity = nK * 16 - rank_mod(eqs, PRIME)
    ok = ok and nullity == 2
    # the Ricci map and the identity times the scalar are two independent solutions
    sols = [[], []]
    for v in K:
        Fm, s = ricci_of(mat_of(v))
        sols[0].extend(Fm[m][k] for m in range(D) for k in range(D))
        sols[1].extend((s if m == k else F(0)) for m in range(D) for k in range(D))
    for sol in sols:
        ok = ok and all(sum(b * sol[a] for a, b in row.items()) == 0 for row in exact)
    ok = ok and GA.mat_rank([list(sols[0]), list(sols[1])]) == 2
    # the maps of vectors fixed by the rotors are the multiples of the identity
    inv_rows = []
    for G in BV:
        rho = [act_map(G, U) for U in units]
        for m in range(D):
            for k in range(D):
                inv_rows.append([rho[u][m][k] for u in range(16)])
    ok = ok and 16 - GA.mat_rank(inv_rows) == 1
    ident = [F(1) if (u // 4) == (u % 4) else F(0) for u in range(16)]
    ok = ok and all(sum(r[u] * ident[u] for u in range(16)) == 0 for r in inv_rows)
    GA.check("(iv) the linear maps from the twenty-dimensional space of curvature operators to the maps of "
             "vectors that commute with the rotors: 320 coefficients, six bivectors, nullity two modulo a "
             "prime, and the Ricci map and id times the scalar are two independent ones; the maps of vectors "
             "fixed by the rotors are the multiples of id", ok)
    return ok


def field_not_weak():
    """a gravitational field with hb^{-1} = id + a polynomial map (not symmetric, not small), Omega from torsion."""
    def hbinv(X):
        t, x, y, z = X
        P = [[F(1, 5) * x + F(1, 9) * t * y, F(1, 7) * z, 0, F(1, 6) * t],
             [F(1, 8) * y, F(1, 4) * t + F(1, 11) * x * z, F(1, 10) * x, 0],
             [0, F(1, 6) * z, F(1, 7) * y * t, F(1, 9) * x],
             [F(1, 12) * z, 0, F(1, 5) * t, F(1, 8) * x * y + F(1, 13) * z]]
        return [[(1 if mu == a else 0) + P[mu][a] for a in range(D)] for mu in range(D)]

    x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
    return gtg.field_from_hbinv(hbinv, x0, S, order=2)


def field_data():
    fld = field_not_weak()
    Rj = fld.curvature_jet()

    def Rop(B):
        out = {}
        for (a, b), c in B.items():
            out = gtg.m_add(out, gtg.m_scal(c, Rj[(a, b)]))
        return out

    Ric = [gtg.ricci(Rop, E[c], S) for c in range(D)]
    sc = gtg.Jet.const(0, D)
    for c in range(D):
        sc = sc + Ric[c].get((c,), gtg.Jet.const(0, D))
    return fld, Rop, Ric, sc


def divergence(fld, Mj, c):
    """sum_a gamma^a . ((gamma_a . D M)(gamma_c)) for a field M of maps of vectors given on the frame as jets."""
    Mv = [gtg.m_val(x) for x in Mj]
    tot = F(0)
    for a in range(D):
        A = [F(1) if i == a else F(0) for i in range(D)]
        turned = gtg.m_val(gtg.comm(gtg.m_val(fld.om[a]), E[c], S))      # gamma_a . D gamma_c
        back = {}
        for bl, co in turned.items():
            back = add(back, scal(co, Mv[bl[0]]))
        tot += dot(REC[a], sub(fld.cov_phys(A, Mj[c]), back))
    return tot


def check_bianchi_identities_on_a_field_that_is_not_weak():
    fld, Rop, Ric, sc = field_data()
    ok = fld.torsion_free()
    # the cyclic identity, on the four triples of frame vectors
    seen = 0
    for a in range(D):
        for b in range(a + 1, D):
            for c in range(b + 1, D):
                ok = ok and gtg.m_val(cyclic(Rop, E[a], E[b], E[c])) == {}
                seen += 0 if gtg.m_val(Rop(wedge(E[a], E[b]))) == {} else 1
    ok = ok and seen == 4
    # the differential identity on the four triples of frame vectors: the cyclic sum of
    # (gamma_a . D R)(gamma_b ^ gamma_c) = gamma_a . D (R(gamma_b ^ gamma_c)) - R(gamma_a . D (gamma_b ^ gamma_c))
    def dR(a, b, c):
        A = [F(1) if i == a else F(0) for i in range(D)]
        Bv = wedge(E[b], E[c])
        turned = grade(gtg.m_val(gtg.comm(gtg.m_val(fld.om[a]), Bv, S)), 2)
        return sub(fld.cov_phys(A, Rop(Bv)), gtg.m_val(Rop(turned)))

    terms = 0
    for a in range(D):
        for b in range(a + 1, D):
            for c in range(b + 1, D):
                parts = [dR(a, b, c), dR(b, c, a), dR(c, a, b)]
                ok = ok and GA.is_zero(add(*parts))
                terms += sum(0 if GA.is_zero(x) else 1 for x in parts)
    ok = ok and terms == 12
    # the Ricci map is symmetric, and neither it nor the scalar vanishes
    Rv = [gtg.m_val(r) for r in Ric]
    ok = ok and all(dot(E[a], Rv[b]) == dot(E[b], Rv[a]) for a in range(D) for b in range(D))
    ok = ok and sc.v != 0 and any(dot(E[0], Rv[b]) != 0 for b in range(1, D))
    # contracted second identity: div Ric = 1/2 D(scalar), so div G = 0
    Hi = fld.hb_matrix()
    half = F(1, 2)
    Gm = [gtg.m_sub(Ric[c], gtg.m_scal(half * sc, E[c])) for c in range(D)]
    nonzero = 0
    for c in range(D):
        dsc = sum(Hi[mu][c] * sc.d(mu).v for mu in range(D))            # gamma_c . D (scalar)
        dric = divergence(fld, Ric, c)
        ok = ok and dric == half * dsc and divergence(fld, Gm, c) == 0
        nonzero += 1 if dsc != 0 else 0
    ok = ok and nonzero == 4
    GA.check("(i), (iii) on a field (hb, Omega) that is not weak and not symmetric, Omega from the torsion "
             "equation: R(a^b).c + R(b^c).a + R(c^a).b = 0; the cyclic sum of (A.D R)(B^C) vanishes on the four "
             "triples of the frame, all twelve terms nonzero; the Ricci map is symmetric, div Ric = 1/2 D(scalar) "
             "with D(scalar) nonzero in all four directions, and div G = 0", ok)
    return ok


def check_divergence_of_the_two_parameter_family():
    fld, Rop, Ric, sc = field_data()
    Hi = fld.hb_matrix()
    ok = True
    # (a, b, l), with the coefficient a/2 + b of D(scalar) in the divergence, and a + 4b and 4l in the trace
    cases = ((F(1), F(0), F(0), F(1, 2), F(1), F(0)),
             (F(0), F(1), F(0), F(1), F(4), F(0)),
             (F(2), F(-3), F(5), F(-2), F(-10), F(20)),
             (F(1), F(-1, 2), F(7), F(0), F(-1), F(28)),
             (F(4), F(-1), F(-2), F(1), F(0), F(-8)),
             (F(6), F(-3), F(1), F(0), F(-6), F(4)))
    without = 0
    for al, be, la, cdiv, ctr, cl in cases:
        ok = ok and al * F(1, 2) + be == cdiv and al + 4 * be == ctr and 4 * la == cl
        Fam = [gtg.m_add(gtg.m_scal(al, Ric[c]), gtg.m_scal(be * sc + la, E[c])) for c in range(D)]
        zero = True
        for c in range(D):
            dsc = sum(Hi[mu][c] * sc.d(mu).v for mu in range(D))
            dv = divergence(fld, Fam, c)
            ok = ok and dv == cdiv * dsc and dsc != 0
            zero = zero and dv == 0
        ok = ok and zero == (be == -al * F(1, 2))
        without += 1 if zero else 0
        # the trace of the family is (a + 4b)(scalar) + 4l
        tr = sum(gtg.m_val(Fam[c]).get((c,), F(0)) for c in range(D))
        ok = ok and tr == ctr * sc.v + cl
    ok = ok and without == 2
    GA.check("(v) the divergence of a Ric + b (scalar) id + l id is (a/2 + b) D(scalar), for six choices of "
             "(a, b, l) on the field of the check of (i) and (iii); it vanishes exactly for the two with b = -a/2; the trace "
             "is (a + 4b)(scalar) + 4l", ok)
    return ok


def first_order_einstein(H, p):
    """the stored first-order Einstein map G_p[h] from R_p[h](B) = -1/2 p ^ h(B.p); H[m][k]: h(a) = sum (a.e_m) e_k."""
    def h(a):
        out = {}
        for m in range(D):
            am = dot(a, E[m])
            for k in range(D):
                if am and H[m][k]:
                    out = add(out, scal(am * H[m][k], E[k]))
        return out

    def riem(B):
        return scal(F(-1, 2), wedge(p, h(GA.neg(grade(comm(p, B), 1)))))

    Ric = []
    for k in range(D):
        img = {}
        for a in range(D):
            img = add(img, grade(comm(REC[a], riem(wedge(E[a], E[k]))), 1))
        Ric.append(img)
    s = sum(dot(REC[k], Ric[k]) for k in range(D))
    return [sub(Ric[k], scal(F(1, 2) * s, E[k])) for k in range(D)]


def check_first_order_limit_is_the_stored_einstein_map():
    premise("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-is-the-trace-free-channel")
    premise("synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators")
    ok = True
    H0 = [[F(3), F(-1), F(2), F(5)], [F(-1), F(4), F(-2), F(1)], [F(2), F(-2), F(-3), F(2)], [F(5), F(1), F(2), F(1)]]
    pc = (2, 1, -1, 3)
    p = {(i,): F(x) for i, x in enumerate(pc) if x}

    def hbinv(X):
        P = sum((F(ETA[mu] * pc[mu]) * X[mu] for mu in range(D)), gtg.Jet.const(0, D))
        q = F(1, 4) * P * P
        return [[(1 if mu == c else 0) + ETA[mu] * H0[mu][c] * q for c in range(D)] for mu in range(D)]

    fld = gtg.field_from_hbinv(hbinv, (F(0), F(0), F(0), F(0)), S, order=1)
    Rop = gtg.as_op(fld.curvature())
    want = first_order_einstein(H0, p)
    seen = 0
    for k in range(D):
        got = gtg.einstein(Rop, E[k], S)
        ok = ok and GA.eq(got, want[k])
        seen += 0 if GA.is_zero(want[k]) else 1
    ok = ok and seen == 4 and fld.torsion_free()
    ok = ok and sum(dot(REC[k], want[k]) for k in range(D)) == -21          # the trace of G_p[h0] on this sample
    # every operator with the cyclic identity is the curvature at a point of some field: the stored
    # first-order curvatures R_p[h0], each the curvature at x = 0 of the field above, span all twenty dimensions
    vecs = []
    singles = [E[i] for i in range(D)]
    momenta = singles + [add(E[i], E[j]) for i in range(D) for j in range(i + 1, D)]
    ranks = []
    for count, qv in enumerate(momenta):
        if count == len(singles):
            ranks.append(GA.mat_rank(vecs))
        for m in range(D):
            for k in range(m, D):
                v = []
                for I in range(6):
                    hB = {}
                    arg = GA.neg(grade(comm(qv, BV[I]), 1))
                    for bl, co in arg.items():
                        # h(a) for the symmetric unit map on (m, k): a -> (a.e_m) e_k + (a.e_k) e_m (once if m = k)
                        for (mm, kk) in ({(m, k), (k, m)}):
                            if bl[0] == mm:
                                hB = add(hB, scal(co * ETA[mm], E[kk]))
                    img = scal(F(-1, 2), wedge(qv, hB))
                    v.extend(img.get(bl2, F(0)) for bl2 in BL)
                vecs.append(v)
    ranks.append(GA.mat_rank(vecs))
    ok = ok and len(momenta) == 10 and ranks[-1] == 20 and ranks[0] < 20
    GA.check("(vii), (ii) the Einstein map of the field hb^{-1} = id + 1/4 (p.x)^2 h0 at x = 0, computed from the "
             "gauge fields, is the stored first-order Einstein map G_p[h0] on all four frame vectors; the stored "
             "first-order curvatures span the twenty dimensions of the operators with the cyclic identity "
             "(the constant of (vii) is not checked here)", ok)
    return ok
