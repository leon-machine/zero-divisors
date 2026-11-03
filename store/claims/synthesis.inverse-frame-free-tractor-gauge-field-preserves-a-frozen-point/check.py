"""No inverse frame forces the frozen point: exact checks.

Cl(2,4) with generators e0 (+1), e1, e2, e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-
(n0.ninf = 1); W = span(e0..e3), the physical vectors. GTG data at a point: the frame e = hb^{-1} (a 4x4
rational matrix, e(e_mu) = sum_i e[mu][i] W[i]) and the rotation-gauge field Omega (Omega(e_mu) in
Lambda^2 W). A tractor gauge field built from them has four slots:
  A(a) = Lor(a) + b(a) n0^ninf - ninf ^ tau(a) + n0 ^ S(a)
(Lorentz, dilation, translation, special-conformal). Soldering: D_a n0 = A(a) x n0 = tau(a).
(1) weights: under the displacement x -> lam x every jet factor of e or Omega of derivative order k
    scales as lam^(1+k), a factor of hb as lam^(k-1); a one-form slot has weight 1. Enumerated: without hb
    the weight-1 monomials are exactly the undifferentiated e and Omega; with hb there are weight-1
    monomials of every degree, the Schouten type hb hb dOmega e among them, of frame degree -1.
(2) Lorentz-equivariant linear maps between R, W, Lambda^2 W: Hom(W, W) = 1 (the commutant), all maps
    W -> R, W -> Lambda^2 W, Lambda^2 W -> W, Lambda^2 W -> R are zero, Hom(Lambda^2 W, Lambda^2 W) = 2.
(3) the slots allowed are Lor = Omega, b = 0, tau = e, S = rho e; the joint kernel of a -> A_rho(a) x .
    on Cl(2,4) vectors is span(I_rho), I_rho = ninf + rho n0, for generic data and rho in {3/14, -1/2, 0}.
(5) the normal tractor connection's slot is Sch(e(a)); for ℛ(a^b) = P(a)^b + a^P(b) the Schouten map
    returns P; the normal connection preserves I_rho iff P = rho id, while A_rho preserves it for every
    P; the normal slot has frame degree -1 (Sch(c e(a)) = Sch(e(a)) / c for the curvature
    ℛ(B) = -R(hb(B)) with R fixed).
(6) at a corank-one frame the normal slot has a simple pole while A_rho keeps I_rho; an independent slot
    field leaves no parallel tractor.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as Fr
from itertools import combinations, product

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
N0 = GA.scal(Fr(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
W = E[:4]
VEC = E[:]
L2W = [GA.mul(W[a], W[b], SQ) for a, b in combinations(range(4), 2)]
ONE = [GA.sc(Fr(1))]


def mul(x, y):
    return GA.mul(x, y, SQ)


def comm(x, y):
    return GA.scal(Fr(1, 2), GA.sub(mul(x, y), mul(y, x)))


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def wedge(x, y, r, s):
    return grade(mul(x, y), r + s)


def lin(cs, basis):
    out = {}
    for c, u in zip(cs, basis):
        if c != 0:
            out = GA.add(out, GA.scal(Fr(c), u))
    return out


def nullspace(rows, n):
    piv = {}
    for r in rows:
        r = list(r)
        for c, pr in piv.items():
            if r[c] != 0:
                f = r[c]
                r = [a - f * b for a, b in zip(r, pr)]
        c0 = next((c for c in range(n) if r[c] != 0), None)
        if c0 is None:
            continue
        p = r[c0]
        r = [a / p for a in r]
        for c, pr in list(piv.items()):
            if pr[c0] != 0:
                f = pr[c0]
                piv[c] = [a - f * b for a, b in zip(pr, r)]
        piv[c0] = r
    out = []
    for fc in [c for c in range(n) if c not in piv]:
        x = [Fr(0)] * n
        x[fc] = Fr(1)
        for c, pr in piv.items():
            x[c] = -pr[fc]
        out.append(x)
    return out


def coords(x, basis):
    blades = sorted({b for u in basis for b in u} | set(x))
    n = len(basis)
    m = [[u.get(b, Fr(0)) for u in basis] + [x.get(b, Fr(0))] for b in blades]
    cols, row = [], 0
    for col in range(n):
        p = next((r for r in range(row, len(m)) if m[r][col] != 0), None)
        if p is None:
            continue
        m[row], m[p] = m[p], m[row]
        pv = m[row][col]
        m[row] = [a / pv for a in m[row]]
        for r in range(len(m)):
            if r != row and m[r][col] != 0:
                f = m[r][col]
                m[r] = [a - f * b for a, b in zip(m[r], m[row])]
        cols.append(col)
        row += 1
    assert all(m[r][n] == 0 for r in range(row, len(m))), "not in span"
    out = [Fr(0)] * n
    for i, col in enumerate(cols):
        out[col] = m[i][n]
    return out


def act(xi, U):
    """Matrix of u -> xi x u on span(U) (columns = images); the trivial action on the scalars."""
    if U is ONE:
        return [[Fr(0)]]
    cols = [coords(comm(xi, u), U) for u in U]
    return [[cols[j][i] for j in range(len(U))] for i in range(len(U))]


def equivariant_maps(U, Vt, gens):
    """Linear L: span(U) -> span(Vt) with L(xi.u) = xi.L(u) for every generator."""
    k, m = len(U), len(Vt)
    rows = []
    for xi in gens:
        AU, AV = act(xi, U), act(xi, Vt)
        for i in range(m):
            for j in range(k):
                r = [Fr(0)] * (m * k)
                for p in range(k):
                    r[i * k + p] += AU[p][j]
                for q in range(m):
                    r[q * k + j] -= AV[i][q]
                rows.append(r)
    return nullspace(rows, m * k)


# ---------------------------------------------------------------- GTG data at a point
E_FRAME = [[2, 1, 0, -1], [0, 3, 1, 2], [1, 0, -2, 1], [-1, 2, 1, 1]]
OMEGA = [[1, -2, 0, 3, 1, -1], [0, 1, 2, -1, 3, 2], [2, 0, -1, 1, 0, 1], [-3, 1, 1, 2, -2, 0]]


def frame_vec(e, mu):
    return lin(e[mu], W)


def omega_biv(om, mu):
    return lin(om[mu], L2W)


def tractor_field(e, om, rho, b=None, lor_scale=1):
    """A(e_mu) = lor_scale Omega_mu + b_mu n0^ninf - ninf^e_mu + rho n0^e_mu."""
    out = []
    for mu in range(4):
        v = frame_vec(e, mu)
        A = GA.add(GA.scal(Fr(lor_scale), omega_biv(om, mu)), GA.neg(wedge(NI, v, 1, 1)),
                   wedge(N0, GA.scal(Fr(rho), v), 1, 1))
        if b is not None and b[mu] != 0:
            A = GA.add(A, GA.scal(Fr(b[mu]), wedge(N0, NI, 1, 1)))
        out.append(A)
    return out


def joint_kernel(As):
    rows = []
    for A in As:
        imgs = [comm(A, v) for v in VEC]
        for bb in sorted({k for im in imgs for k in im}):
            rows.append([im.get(bb, Fr(0)) for im in imgs])
    return nullspace(rows, 6)


def I_of(rho):
    return GA.add(NI, GA.scal(Fr(rho), N0))


def same_line(kernel, vec):
    if len(kernel) != 1:
        return False
    c = coords(vec, VEC)
    k = kernel[0]
    i0 = next(i for i in range(6) if c[i] != 0)
    if k[i0] == 0:
        return False
    return all(k[i] * c[i0] == c[i] * k[i0] for i in range(6))


# ---------------------------------------------------------------- Schouten map from a curvature operator
RECIP = [GA.scal(Fr(1, SQ[i]), W[i]) for i in range(4)]


def ricci(curv, b):
    """ℛ(b) = sum_mu gamma^mu . ℛ(gamma_mu ^ b) (vector part of the left contraction)."""
    out = {}
    for mu in range(4):
        out = GA.add(out, grade(mul(RECIP[mu], curv(wedge(W[mu], b, 1, 1))), 1))
    return out


def schouten(curv, a):
    rs = {}
    for mu in range(4):
        rs = GA.add(rs, grade(mul(RECIP[mu], ricci(curv, W[mu])), 0))
    s = rs.get((), Fr(0))
    return GA.scal(Fr(1, 2), GA.sub(ricci(curv, a), GA.scal(s / 6, a)))


def curvature_from_P(P):
    """ℛ(a ^ b) = P(a) ^ b + a ^ P(b) extended linearly; P a 4x4 matrix on W (columns images)."""
    def Pv(v):
        c = coords(v, W)
        return lin([sum(P[i][j] * c[j] for j in range(4)) for i in range(4)], W)

    def curv(B):
        c = coords(B, L2W)
        out = {}
        for (a, b), cb in zip(combinations(range(4), 2), c):
            if cb != 0:
                out = GA.add(out, GA.scal(cb, GA.add(wedge(Pv(W[a]), W[b], 1, 1), wedge(W[a], Pv(W[b]), 1, 1))))
        return out
    return curv


def mat_inv(M):
    n = len(M)
    A = [[Fr(M[i][j]) for j in range(n)] + [Fr(int(i == k)) for k in range(n)] for i in range(n)]
    for col in range(n):
        p = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[p] = A[p], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]


def weight_one_monomials(with_hb, max_factors, max_order):
    """Weight-one monomials in jet factors (kind, k): e and Omega of weight 1 + k (frame degree 1, 0) and,
    if allowed, hb of weight k - 1 (frame degree -1); returns {factor count: set of (monomial, frame degree)}."""
    kinds = [("e", 1, 1), ("Om", 1, 0)] + ([("hb", -1, -1)] if with_hb else [])
    factors = [(name, k, w0 + k, d) for (name, w0, d) in kinds for k in range(max_order + 1)]
    found = {}
    for n in range(1, max_factors + 1):
        for combo in multisets(len(factors), n):
            if sum(factors[i][2] for i in combo) == 1:
                d = sum(factors[i][3] for i in combo)
                found.setdefault(n, set()).add((tuple(factors[i][:2] for i in combo), d))
    return found


def multisets(m, n, start=0):
    if n == 0:
        yield ()
        return
    for i in range(start, m):
        for rest in multisets(m, n - 1, i):
            yield (i,) + rest


RMAT = [[1, 0, 2, -1, 0, 1], [0, 3, -1, 0, 1, 0], [2, 1, 0, 1, -2, 1], [0, -1, 1, 2, 0, 3], [1, 0, 0, -1, 2, 1], [-1, 2, 1, 0, 1, 1]]


def normal_slot(e):
    """Sch(e(e_mu)) for the curvature operator -R(hb(B)) with R(e_a ^ e_b) = sum_r RMAT[r] L2W[r], hb = e^{-1}."""
    hb = mat_inv([[e[mu][i] for mu in range(4)] for i in range(4)])

    def hbv(v):
        cv = coords(v, W)
        return lin([sum(hb[k][j] * cv[j] for j in range(4)) for k in range(4)], W)

    def curv(B):
        cb = coords(B, L2W)
        out = {}
        for (a, b), x in zip(combinations(range(4), 2), cb):
            if x != 0:
                ch = coords(wedge(hbv(W[a]), hbv(W[b]), 1, 1), L2W)
                img = lin([sum(Fr(RMAT[r][s]) * ch[s] for s in range(6)) for r in range(6)], L2W)
                out = GA.add(out, GA.scal(-x, img))
        return out
    return [coords(schouten(curv, frame_vec(e, mu)), W) for mu in range(4)]


def wall_frame(c):
    """E_FRAME with its physical component along e3 scaled by c: corank one at c = 0."""
    return [[Fr(x) * (c if i == 3 else 1) for i, x in enumerate(row)] for row in E_FRAME]


def interp_coeffs(pts):
    n = len(pts)
    coeffs = [Fr(0)] * n
    for i, (xi, yi) in enumerate(pts):
        basis = [Fr(1)]
        den = Fr(1)
        for j, (xj, _) in enumerate(pts):
            if j != i:
                basis = [(basis[k - 1] if k > 0 else 0) - xj * (basis[k] if k < len(basis) else 0) for k in range(len(basis) + 1)]
                den *= xi - xj
        for k in range(n):
            coeffs[k] += yi * basis[k] / den
    return coeffs


def kernel_is(As, expected):
    K = joint_kernel(As)
    return len(K) == 1 and K[0] == [Fr(x) for x in expected]


def lc_field(grad, f):
    """a ^ grad f / f on the background frame vectors."""
    g = lin(grad, W)
    return [GA.scal(1 / Fr(f), wedge(W[mu], g, 1, 1)) for mu in range(4)]


def torsion_zero(grad, f, om):
    g = lin(grad, W)
    for mu, nu in combinations(range(4), 2):
        t = GA.sub(GA.scal(GA.dot(W[mu], g, SQ), W[nu]), GA.scal(GA.dot(W[nu], g, SQ), W[mu]))
        t = GA.add(t, GA.scal(Fr(f), GA.sub(comm(om[mu], W[nu]), comm(om[nu], W[mu]))))
        if not GA.is_zero(t):
            return False
    return True


def torsion_map_kernel(f):
    rows = []
    for mu, nu in combinations(range(4), 2):
        for comp in range(4):
            r = []
            for k in range(4):
                for j in range(6):
                    if k == mu:
                        img = GA.scal(Fr(f), comm(L2W[j], W[nu]))
                    elif k == nu:
                        img = GA.neg(GA.scal(Fr(f), comm(L2W[j], W[mu])))
                    else:
                        img = {}
                    r.append(coords(img, W)[comp] if img else Fr(0))
            rows.append(r)
    return nullspace(rows, 24)


SLOT_FIELD = [[1, 0, -2, 1], [3, 1, 0, -1], [0, 2, 1, 1], [-1, 1, 1, 0]]


def scalar_curvature(curv):
    out = Fr(0)
    for mu in range(4):
        out += grade(mul(RECIP[mu], ricci(curv, W[mu])), 0).get((), Fr(0))
    return out


def slotted_field(slot_rows):
    return [GA.add(omega_biv(OMEGA, mu), GA.neg(wedge(NI, frame_vec(E_FRAME, mu), 1, 1)), wedge(N0, lin(slot_rows[mu], W), 1, 1))
            for mu in range(len(slot_rows))]


def jet(seed, n):
    """Deterministic sample rational first jets: jet(seed, n)[nu][mu] is a list of n rationals."""
    return [[[Fr(((seed * (nu + 2) + 5 * mu + 7 * i) % 11) - 5, 1 + (nu + i) % 3) for i in range(n)] for mu in range(4)] for nu in range(4)]


E1, OM1, S1 = jet(3, 4), jet(5, 6), jet(7, 4)


def values(e, om, slot):
    return [GA.add(lin(om[mu], L2W), GA.neg(wedge(NI, lin(e[mu], W), 1, 1)), wedge(N0, lin(slot[mu], W), 1, 1)) for mu in range(4)]


def field_strengths(slot0, slot1):
    """F(e_mu ^ e_nu) at x = 0 for A = A0 + x^nu A1_nu, A0 = values(E_FRAME, OMEGA, slot0), A1_nu = values(E1, OM1, slot1)[nu]."""
    A0 = values(E_FRAME, OMEGA, slot0)
    A1 = [values(E1[nu], OM1[nu], slot1[nu]) for nu in range(4)]
    return [GA.add(GA.sub(A1[mu][nu], A1[nu][mu]), comm(A0[mu], A0[nu])) for mu, nu in combinations(range(4), 2)]


def premises_gtg():
    """The gauge laws used are those of the Definition this result is about (not a derivation premise)."""
    return None


def premises_dictionary():
    premise("synthesis.imported-gtg-dictionary")


def premises_tractor():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premises_dictionary()


def premises_frozen():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")


# ---------------------------------------------------------------- checks
def check_displacement_weight_bounds_the_slot_only_without_inverse_frame():
    premises_gtg()
    p = weight_one_monomials(False, 5, 3)
    ok = set(p) == {1} and p[1] == {((("e", 0),), 1), ((("Om", 0),), 0)}
    q = weight_one_monomials(True, 5, 3)
    ok = ok and [len(q[n]) for n in range(1, 6)] == [3, 6, 14, 25, 47]
    sch = tuple(sorted([("hb", 0), ("hb", 0), ("Om", 1), ("e", 0)]))
    ok = ok and any(tuple(sorted(m)) == sch and d == -1 for (m, d) in q[4])
    GA.check("displacement weight one: without hb only e and Omega undifferentiated; with hb 3, 6, 14, 25, 47 monomials of 1..5 factors, Schouten type at frame degree -1", ok)
    assert ok


def check_lorentz_equivariant_maps_between_the_slots():
    premises_gtg()
    dims = [len(equivariant_maps(W, W, L2W)), len(equivariant_maps(W, ONE, L2W)), len(equivariant_maps(W, L2W, L2W)),
            len(equivariant_maps(L2W, W, L2W)), len(equivariant_maps(L2W, ONE, L2W)), len(equivariant_maps(L2W, L2W, L2W))]
    ok = dims == [1, 0, 0, 0, 0, 2]
    m = equivariant_maps(W, W, L2W)[0]
    ok = ok and m == [Fr(int(i == j)) for i in range(4) for j in range(4)]
    GA.check("Lorentz-equivariant maps W->W, W->R, W->L2, L2->W, L2->R, L2->L2 have dimensions 1, 0, 0, 0, 0, 2; the first is the identity", ok)
    assert ok


def check_the_admissible_field_determines_the_frozen_point():
    premises_gtg()
    premises_frozen()
    ok = kernel_is(tractor_field(E_FRAME, OMEGA, Fr(3, 14)), [0, 0, 0, 0, Fr(-31, 25), 1])
    ok = ok and kernel_is(tractor_field(E_FRAME, OMEGA, Fr(-1, 2)), [0, 0, 0, 0, Fr(-3, 5), 1])
    ok = ok and kernel_is(tractor_field(E_FRAME, OMEGA, Fr(0)), [0, 0, 0, 0, -1, 1])
    As = tractor_field(E_FRAME, OMEGA, Fr(3, 14))
    ok = ok and all(GA.eq(comm(As[mu], N0), frame_vec(E_FRAME, mu)) for mu in range(4))
    ok = ok and joint_kernel(tractor_field(E_FRAME, OMEGA, Fr(3, 14), b=[1, 0, 2, -1])) == []
    GA.check("A_rho has joint kernel the line of ninf + rho n0 (31 e+ - 25 e-, 3 e+ - 5 e-, e+ - e- at rho = 3/14, -1/2, 0); soldered; a dilation slot leaves none", ok)
    assert ok


def check_normal_tractor_connection_meets_the_family_only_on_einstein_fields():
    premises_gtg()
    premises_tractor()
    rho = Fr(3, 14)
    I = I_of(rho)
    ok = coords(I, VEC) == [0, 0, 0, 0, Fr(31, 28), Fr(-25, 28)]
    results = []
    for P in ([[rho * int(i == j) for j in range(4)] for i in range(4)],
              [[Fr(1, 3), 0, 0, 0], [0, rho, 0, 0], [0, 0, rho, 0], [0, 0, 0, Fr(-2, 5)]]):
        curv = curvature_from_P(P)
        sch_ok = all(GA.eq(schouten(curv, W[i]), lin([P[k][i] for k in range(4)], W)) for i in range(4))
        normal = []
        for mu in range(4):
            v = frame_vec(E_FRAME, mu)
            normal.append(GA.add(omega_biv(OMEGA, mu), GA.neg(wedge(NI, v, 1, 1)), wedge(N0, schouten(curv, v), 1, 1)))
        fam = tractor_field(E_FRAME, OMEGA, rho)
        results.append((scalar_curvature(curv), sch_ok, all(GA.is_zero(comm(A, I)) for A in normal), all(GA.is_zero(comm(A, I)) for A in fam),
                        all(GA.eq(a, b) for a, b in zip(normal, fam))))
    ok = ok and results == [(Fr(36, 7), True, True, True, True), (Fr(76, 35), True, False, True, False)]
    s1, s2, s3 = normal_slot(E_FRAME), normal_slot([[2 * x for x in r] for r in E_FRAME]), normal_slot([[Fr(-3, 2) * x for x in r] for r in E_FRAME])
    ok = ok and any(x != 0 for row in s1 for x in row)
    ok = ok and all(a == 2 * b for ra, rb in zip(s1, s2) for a, b in zip(ra, rb))
    ok = ok and all(a == Fr(-3, 2) * b for ra, rb in zip(s1, s3) for a, b in zip(ra, rb))
    GA.check("normal connection = A_rho and keeps I_rho parallel only when Sch = rho id; A_rho keeps it for both; normal slot scales as 1/c under e -> c e", ok)
    assert ok


def check_wall_regularity_separates_the_family_from_the_normal_connection():
    premises_gtg()
    premises_tractor()
    cs = [Fr(1), Fr(2), Fr(-1), Fr(1, 2), Fr(3)]
    slots = {c: normal_slot(wall_frame(c)) for c in cs}
    co = [[interp_coeffs([(c, c * c * slots[c][mu][k]) for c in cs]) for k in range(4)] for mu in range(4)]
    ok = all(co[mu][k][4] == 0 and co[mu][k][0] == 0 for mu in range(4) for k in range(4))
    ok = ok and co[0][0][1:4] == [Fr(-21, 22), Fr(23, 66), 0]
    ok = ok and kernel_is(tractor_field(wall_frame(Fr(0)), OMEGA, Fr(3, 14)), [0, 0, 0, 0, Fr(-31, 25), 1])
    ok = ok and GA.rank_of_vectors(wall_frame(Fr(0))) == 3
    GA.check("normal slot has a simple pole (residue -21/22 in one component) at a corank-one frame; A_rho is defined there and keeps I_rho parallel", ok)
    assert ok


def check_an_independent_slot_field_leaves_no_parallel_tractor():
    premises_gtg()
    ok = joint_kernel(slotted_field(SLOT_FIELD)) == []
    ok = ok and kernel_is(slotted_field([[Fr(-1, 2) * x for x in row] for row in E_FRAME]), [0, 0, 0, 0, Fr(-3, 5), 1])
    # integrability: a parallel tractor I obeys F x I = 0; for generic first jets of (e, Omega, S) the six
    # field-strength values annihilate no vector, while with S = -e/2 (and its jets) they annihilate I_{-1/2}
    ok = ok and joint_kernel(field_strengths(SLOT_FIELD, S1)) == []
    rho = Fr(-1, 2)
    ok = ok and kernel_is(field_strengths([[rho * x for x in row] for row in E_FRAME],
                                          [[[rho * x for x in r] for r in E1[nu]] for nu in range(4)]), [0, 0, 0, 0, Fr(-3, 5), 1])
    GA.check("an independent slot field (allowed by (P) alone): no constant tractor annihilated and the field strength annihilates no vector, so no parallel tractor; the slot -e/2 keeps the line of 3 e+ - 5 e-", ok)
    assert ok


def check_a_parallel_tractor_of_unit_pairing_is_gauged_to_the_constant_frozen_point():
    premises_gtg()
    # I = ninf + mu + t n0 with <X, I> = 1; the special-conformal rotor U = 1 + n0 y / 2 with y = mu fixes X and
    # carries I to ninf + rho n0 with rho = Q(I)/2; with y = -mu it does not
    mu = lin([1, 2, 0, -1], W)
    I = GA.add(NI, mu, GA.scal(Fr(3), N0))
    ok = GA.dot(I, N0, SQ) == 1 and GA.dot(I, I, SQ) == 2
    images = []
    for y in (mu, GA.neg(mu)):
        U = GA.add(GA.sc(Fr(1)), GA.scal(Fr(1, 2), mul(N0, y)))
        Ut = GA.add(GA.sc(Fr(1)), GA.scal(Fr(1, 2), mul(y, N0)))
        ok = ok and GA.eq(mul(U, Ut), GA.sc(Fr(1))) and GA.eq(mul(mul(U, N0), Ut), N0)
        images.append(mul(mul(U, I), Ut))
    ok = ok and GA.eq(images[0], I_of(Fr(1))) and not GA.eq(images[1], I_of(Fr(1)))
    GA.check("U = 1 + n0 mu / 2 fixes X and carries ninf + mu + 3 n0 (Q = 2) to ninf + n0; y = -mu does not", ok)
    assert ok
