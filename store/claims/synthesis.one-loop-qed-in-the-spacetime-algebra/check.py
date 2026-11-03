"""One-loop QED in the spacetime algebra: exact checks.

Cl(1,3), signature (+,-,-,-), generators g0..g3 (GA.gen), I4 = g0 g1 g2 g3. A vector with upper
components v^mu is v = sum v^mu g_mu; the reciprocal frame is g^mu = g_mu / Q(g_mu). The Dirac
propagator numerator of momentum k is the multivector k + m, the vertex is g^mu, and the trace of the
Dirac matrices is four times the scalar part (checked against explicit Dirac matrices over Q(i)).

Part 1: chiral traces are 2 proj (span{1, I4} part), read with I4 -> -i (right) or +i (left).
Part 2: vacuum polarisation numerator after the shift and four-dimensional symmetric integration;
        Pauli-Villars removes the non-transverse part exactly; log coefficient 1/12 (times e^2/pi^2).
Part 3: vertex: contraction identities, on-shell sandwich, Gordon identity with the real bivector
        g^mu ^ q, magnetic numerator 2 m z (1 - z), F2(0) = e^2/(8 pi^2) = alpha/(2 pi).
Part 4: resolvent identity and the Ward-Takahashi identity integrand by integrand.
Part 5: the unit placed as I4 inside the product at each propagator flips the mass term (I4 anticommutes
        with the vertex vector, not with the even k g^nu): harmless for massless chiral lines, but for a
        massive loop it leaves a non-transverse remainder that Pauli-Villars does not remove.
Exact arithmetic only (Fractions, Gaussian rationals).
"""
from fractions import Fraction as Fr
from itertools import product

import GA
from GA import QI
from tp_premise import premise

S = (1, -1, -1, -1)
G = [GA.gen(i) for i in range(4)]
GU = [GA.scal(Fr(1, S[i]), G[i]) for i in range(4)]       # reciprocal frame g^mu
I4 = GA.mul(GA.mul(G[0], G[1], S), GA.mul(G[2], G[3], S), S)
PS = (0, 1, 2, 3)


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, S)
    return out


def vec(c):
    return GA.add(*[GA.scal(Fr(c[i]), G[i]) for i in range(4)])


def sc(x):
    return x.get((), Fr(0))


def ps(x):
    return x.get(PS, Fr(0))


def Q(v):
    return sc(mul(v, v))


def comp_up(v, mu):
    return v.get((mu,), Fr(0))


def comp_dn(v, mu):
    return S[mu] * comp_up(v, mu)


def num(c):
    return {(): Fr(c)} if c != 0 else {}


def eq(x, y):
    return GA.is_zero(GA.sub(x, y))


def inverse_dirac(k, m):
    """(k - m)^{-1} = (k + m)/(Q(k) - m^2)."""
    return GA.scal(Fr(1) / (Q(k) - m * m), GA.add(k, num(m)))


# sample data (module level, rational)
M = Fr(1)
P_IN = vec([Fr(5, 4), Fr(3, 4), 0, 0])          # Q = 1
P_OUT = vec([Fr(13, 12), 0, Fr(5, 12), 0])      # Q = 1
QT = GA.sub(P_OUT, P_IN)
P_IN2 = vec([Fr(5, 3), Fr(4, 3), 0, 0])          # Q = 1
P_OUT2 = vec([Fr(17, 15), 0, 0, Fr(8, 15)])     # Q = 1
QV = vec([Fr(2, 3), Fr(-1, 5), Fr(3, 7), Fr(1, 2)])
XS = [Fr(0), Fr(1, 3), Fr(1, 2), Fr(5, 7), Fr(1)]
VA, VB, VC = vec([1, 2, -1, 3]), vec([Fr(1, 2), 0, 1, -2]), vec([2, -1, Fr(1, 3), 1])
WARD_M = Fr(3, 2)
WARD_SAMPLES = [(vec([2, 1, 0, Fr(1, 2)]), vec([Fr(1, 3), 0, 1, 0]), vec([0, Fr(1, 2), Fr(1, 4), 1])),
                (vec([Fr(7, 5), 0, 1, 1]), vec([1, 1, Fr(-2, 3), 0]), vec([Fr(1, 2), Fr(1, 3), 0, 2]))]
UNIT_MASSES = (Fr(1), Fr(0), Fr(5, 2))
UNIT_LOOPS = (vec([0, 0, 0, 0]), vec([1, Fr(1, 2), -2, 3]))
PV_SQUARES = (1, 100, 300)
FOUR_VECTORS = (vec([1, 2, 0, 1]), vec([0, 1, 3, 1]), vec([2, 0, 1, 1]), vec([1, 1, 1, 5]))
SIMPLEX = [(Fr(1, 5), Fr(2, 5)), (Fr(1, 3), Fr(1, 3)), (Fr(1, 2), Fr(1, 4)), (Fr(0), Fr(3, 4)),
           (Fr(1, 7), Fr(5, 7)), (Fr(2, 3), Fr(1, 6)), (Fr(3, 8), Fr(1, 8))]


# ---------------------------------------------------------------- Dirac matrices over Q(i)
Z, ONE, IU = QI(0), QI(1), QI(0, 1)


def mzero():
    return [[Z] * 4 for _ in range(4)]


def mmul(A, B):
    return [[sum((A[r][t] * B[t][c] for t in range(4)), Z) for c in range(4)] for r in range(4)]


def madd(A, B):
    return [[A[r][c] + B[r][c] for c in range(4)] for r in range(4)]


def mscal(s, A):
    return [[s * A[r][c] for c in range(4)] for r in range(4)]


def mtr(A):
    return sum((A[r][r] for r in range(4)), Z)


def _block(a, b, c, d):
    out = mzero()
    for r in range(2):
        for cc in range(2):
            out[r][cc], out[r][cc + 2] = a[r][cc], b[r][cc]
            out[r + 2][cc], out[r + 2][cc + 2] = c[r][cc], d[r][cc]
    return out


SIG = [[[Z, ONE], [ONE, Z]], [[Z, QI(0, -1)], [IU, Z]], [[ONE, Z], [Z, QI(-1)]]]
I2, Z2 = [[ONE, Z], [Z, ONE]], [[Z, Z], [Z, Z]]
NEG = (lambda A: [[QI(-1) * e for e in row] for row in A])
GM = [_block(I2, Z2, Z2, NEG(I2))] + [_block(Z2, SIG[k], NEG(SIG[k]), Z2) for k in range(3)]
IDM = _block(I2, Z2, Z2, I2)


def matrix_of(x):
    out = mzero()
    for blade, c in x.items():
        mb = IDM
        for i in blade:
            mb = mmul(mb, GM[i])
        out = madd(out, mscal(QI(c), mb))
    return out


def _perm_sign(p):
    sgn, p = 1, list(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                sgn = -sgn
    return sgn


_PERMS = [(p, _perm_sign(p)) for p in __import__("itertools").permutations(range(4))]


def check_chiral_traces_are_two_proj():
    """Part 1: Tr M(X) = 4 <X>_0 on all sixteen blades; with gamma5 = i M(I4), the right-handed trace
    Tr((1 + gamma5)/2 M(X)) = 2(<X>_0 - i <X>_4) and the left-handed one 2(<X>_0 + i <X>_4): the chiral
    trace is 2 proj(X) read with I4 -> -i or +i."""
    premise("field-theory.second-quantisation")
    ok = True
    for mu, nu in product(range(4), repeat=2):
        anti = madd(mmul(GM[mu], GM[nu]), mmul(GM[nu], GM[mu]))
        ok &= anti == mscal(QI(2 * (S[mu] if mu == nu else 0)), IDM)
    g5 = mscal(IU, matrix_of(I4))
    ok &= mmul(g5, g5) == IDM
    PR = mscal(QI(Fr(1, 2)), madd(IDM, g5))
    PL = mscal(QI(Fr(1, 2)), madd(IDM, mscal(QI(-1), g5)))
    for blade in GA.all_blades(4):
        X = {blade: Fr(1)}
        ok &= mtr(matrix_of(X)) == QI(4 * sc(X))
        ok &= mtr(mmul(PR, matrix_of(X))) == QI(2 * sc(X), -2 * ps(X))
        ok &= mtr(mmul(PL, matrix_of(X))) == QI(2 * sc(X), 2 * ps(X))
    # a product of four sample vectors: the pseudoscalar part is the oriented volume
    a, b, c, d = FOUR_VECTORS
    X = mul(a, b, c, d)
    rows4 = [[comp_up(v, i) for i in range(4)] for v in (a, b, c, d)]
    det = sum(sgn * rows4[0][s0] * rows4[1][s1] * rows4[2][s2] * rows4[3][s3]
              for (s0, s1, s2, s3), sgn in _PERMS)
    ok &= ps(X) == det and det != 0
    ok &= sc(X) == (sc(mul(a, b)) * sc(mul(c, d)) - sc(mul(a, c)) * sc(mul(b, d))
                    + sc(mul(a, d)) * sc(mul(b, c)))
    GA.check("check_chiral_traces_are_two_proj", ok)
    return ok


# ---------------------------------------------------------------- part 2: vacuum polarisation
def bil_tensor(a, b, part):
    """T^{mu nu} = <g^mu a g^nu b>_part, part 0 (scalar) or 4 (pseudoscalar coefficient)."""
    f = sc if part == 0 else ps
    return [[f(mul(GU[mu], a, GU[nu], b)) for nu in range(4)] for mu in range(4)]


def tadd(*ts):
    return [[sum(t[mu][nu] for t in ts) for nu in range(4)] for mu in range(4)]


def tscal(s, t):
    return [[s * t[mu][nu] for nu in range(4)] for mu in range(4)]


GINV = [[Fr(S[mu]) if mu == nu else Fr(0) for nu in range(4)] for mu in range(4)]


def l_average(part):
    """Four-dimensional symmetric integration: l^a l^b -> Q(l) g^{ab}/4, so B(l, l) -> Q(l) A with
    A = (1/4) sum_a B(g_a, g^a)."""
    return tscal(Fr(1, 4), tadd(*[bil_tensor(G[a], GU[a], part) for a in range(4)]))


def vp_numerator_parts(q, x, m, part):
    """Dirac numerator 4 <g^mu (k + m) g^nu (k' + m)>_0 with k = l - x q, k' = l + (1 - x) q:
    returns (A, C) with numerator = Q(l) A + C after symmetric integration (odd terms dropped)."""
    A = tscal(4, l_average(part))
    C = tscal(4, bil_tensor(GA.scal(-x, q), GA.scal(1 - x, q), part))
    if part == 0:
        C = tadd(C, tscal(4 * m * m, GINV))
    return A, C


def check_vacuum_polarisation_transverse_with_log_coefficient_one_twelfth():
    """Part 2. Numerator = Q(l)(-2 g) + 8 x(1-x)(Q(q) g - q q) + 4 Delta g, Delta = m^2 - x(1-x)Q(q);
    the g-part is -2 g (Q(l) - 2 Delta), whose Euclidean radial integral is exactly
    F(L) = L - Delta + Delta^2/(L + Delta) (L the squared cutoff; F(0) = 0, F' the integrand), so under
    Pauli-Villars (sum c = sum c M^2 = 0) its cutoff-polynomial part vanishes identically; the
    pseudoscalar (I4) part of the massless chiral numerator vanishes; the transverse coefficient
    integrates to int 8 x (1-x) dx / 16 = 1/12."""
    premise("field-theory.second-quantisation")
    premise("field-theory.coupled-system-tree-level")
    ok = True
    q = QV
    for x in XS:
        A, C = vp_numerator_parts(q, x, M, 0)
        delta = M * M - x * (1 - x) * Q(q)
        ok &= A == tscal(-2, GINV)
        qq = [[comp_up(q, mu) * comp_up(q, nu) for nu in range(4)] for mu in range(4)]
        trans = tscal(8 * x * (1 - x), tadd(tscal(Q(q), GINV), tscal(-1, qq)))
        ok &= C == tadd(trans, tscal(4 * delta, GINV))
        # transversality of the transverse part: q_mu T^{mu nu} = 0
        ok &= all(sum(comp_dn(q, mu) * trans[mu][nu] for mu in range(4)) == 0 for nu in range(4))
        # chiral (massless) pseudoscalar part: both pieces vanish
        A4, C4 = vp_numerator_parts(q, x, 0, 4)
        ok &= all(v == 0 for row in A4 + C4 for v in row)
    # control: the pseudoscalar part of an unshifted product is not zero
    ok &= any(v != 0 for row in bil_tensor(G[0], G[1], 4) for v in row)
    # before symmetric integration the terms linear in l carry a nonzero I4 part (they integrate to zero)
    lin = tadd(bil_tensor(UNIT_LOOPS[1], GA.scal(1 - XS[1], q), 4), bil_tensor(GA.scal(-XS[1], q), UNIT_LOOPS[1], 4))
    ok &= any(v != 0 for row in lin for v in row)
    # radial integral of (u + 2 D) u/(u + D)^2 (Euclidean, measure pi^2 u du): F(L) = L - D + D^2/(L+D)
    for D in (Fr(1), Fr(7, 3), Fr(1, 5)):
        Fn = GA.RF(GA.padd(GA.pmul([-D, Fr(1)], [D, Fr(1)]), [D * D]), [D, Fr(1)])   # L - D + D^2/(L + D)
        integrand = GA.RF(GA.pmul([Fr(0), Fr(1)], [2 * D, Fr(1)]), GA.pmul([D, Fr(1)], [D, Fr(1)]))
        ok &= Fn.deriv().eqrf(integrand) and Fn.eval(Fr(0)) == 0
    # Pauli-Villars: c = (1, c1, c2), masses (m^2, M1^2, M2^2) with sum c = sum c M^2 = 0
    m2, M1, M2 = Fr(1), Fr(100), Fr(300)
    c2 = (m2 - M1) / (M1 - M2)
    c1 = -1 - c2
    cs = (Fr(1), c1, c2)
    ok &= sum(cs) == 0 and m2 + c1 * M1 + c2 * M2 == 0
    for x, q2 in ((Fr(1, 3), Fr(-2)), (Fr(1, 2), Fr(1, 3)), (Fr(1, 5), Fr(7))):
        deltas = [mi - x * (1 - x) * q2 for mi in (m2, M1, M2)]
        total = GA.RF0
        for c, d in zip(cs, deltas):
            total = total + GA.RF.const(c) * GA.RF(GA.padd(GA.pmul([-d, Fr(1)], [d, Fr(1)]), [d * d]), [d, Fr(1)])
        # the regulated g-part is a proper rational function of L: no L or constant term survives
        ok &= len(total.num) < len(total.den) and not total.is_zero()
        # control: a single regulator (c = (1, -1)) leaves the constant term M1 - m^2
        one = GA.RF(GA.padd(GA.pmul([-deltas[0], Fr(1)], [deltas[0], Fr(1)]), [deltas[0] ** 2]), [deltas[0], Fr(1)]) - \
            GA.RF(GA.padd(GA.pmul([-deltas[1], Fr(1)], [deltas[1], Fr(1)]), [deltas[1] ** 2]), [deltas[1], Fr(1)])
        ok &= len(one.num) == len(one.den)
    # transverse coefficient: int_0^1 8 x (1-x) dx / 16 = 1/12 (exact polynomial integration)
    poly = GA.pmul([Fr(8)], GA.pmul([Fr(0), Fr(1)], [Fr(1), Fr(-1)]))
    integral = GA.peval(GA.ps_int(poly), Fr(1)) - GA.peval(GA.ps_int(poly), Fr(0))
    ok &= integral / 16 == Fr(1, 12) and GA.peval(GA.ps_int([Fr(0), Fr(1), Fr(-1)]), Fr(1)) == Fr(1, 6)
    GA.check("check_vacuum_polarisation_transverse_with_log_coefficient_one_twelfth", ok)
    return ok


# ---------------------------------------------------------------- part 3: the vertex
def contract(*xs):
    """sum_nu g^nu X g_nu for X the product of xs."""
    X = mul(*xs) if len(xs) > 1 else xs[0]
    return GA.add(*[mul(GU[n], X, G[n]) for n in range(4)])


def vertex_numerator(mu, k, kp, m):
    """sum_nu g^nu (k' + m) g^mu (k + m) g_nu."""
    return contract(GA.add(kp, num(m)), GU[mu], GA.add(k, num(m)))


def solve_consistent(rows, rhs):
    """Exact solution of an overdetermined system through the normal equations (the caller then
    verifies the fit exactly)."""
    n = len(rows[0])
    AtA = [[sum(r[i] * r[j] for r in rows) for j in range(n)] for i in range(n)]
    Atb = [sum(r[i] * b for r, b in zip(rows, rhs)) for i in range(n)]
    return GA.field_solve(AtA, Atb)


def check_contraction_identities_four_dimensional():
    """Part 3a: g^nu a g_nu = -2a, g^nu a b g_nu = 4 a.b, g^nu a b c g_nu = -2 c b a (exact in d = 4)."""
    premise("field-theory.elementary-photon-ga")
    a, b, c = VA, VB, VC
    ok = eq(contract(a), GA.scal(-2, a))
    ok &= eq(contract(a, b), num(4 * sc(mul(a, b)) - 0)) and sc(mul(a, b)) == GA.dot(a, b, S)
    ok &= eq(contract(a, b, c), GA.scal(-2, mul(c, b, a)))
    ok &= eq(contract(num(1)), num(4))
    GA.check("check_contraction_identities_four_dimensional", ok)
    return ok


def check_vertex_magnetic_part_and_schwinger_coefficient():
    """Part 3b. With k = l - y q + z p, k' = l + (1-y) q + z p (x = 1 - y - z), the l-free part of the
    numerator sandwiched between the on-shell projectors (p' + m) ... (p + m) equals
    (p' + m)[a g^mu + b (p + p')^mu + c q^mu](p + m) with b = 2 m z(1-z) and c odd under x <-> y; the
    Gordon identity (p' + m)(p + p')^mu (p + m) = (p' + m)(2m g^mu + g^mu ^ q)(p + m) holds with the
    real bivector g^mu ^ q (= -i sigma^{mu nu} q_nu in the matrix reading); and
    m int_simplex b/Delta at q = 0 (Delta = (1-z)^2 m^2) is exactly 1, so F2(0) = e^2/(8 pi^2)."""
    premise("field-theory.elementary-photon-ga")
    premise("field-theory.coupled-system-tree-level")
    # the seven simplex points lie on no common conic (the quadratic monomials have rank 6 on them)
    mono = [[Fr(1), y, z, y * y, y * z, z * z] for (y, z) in SIMPLEX]
    ok = GA.rank_of_vectors(mono) == 6
    m = M
    for p, pp in ((P_IN, P_OUT), (P_IN2, P_OUT2)):
        q = GA.sub(pp, p)
        ok &= Q(p) == m * m and Q(pp) == m * m
        Pp, Pi = GA.add(pp, num(m)), GA.add(p, num(m))
        # on-shell projector property: (p - m)(p + m) = 0
        ok &= GA.is_zero(mul(GA.sub(p, num(m)), Pi)) and GA.is_zero(mul(Pp, GA.sub(pp, num(m))))
        # Gordon identity with the real bivector g^mu ^ q
        for mu in range(4):
            lhs = GA.scal(comp_up(GA.add(p, pp), mu), mul(Pp, Pi))
            wedge = {bl: c for bl, c in mul(GU[mu], q).items() if len(bl) == 2}
            rhs = mul(Pp, GA.add(GA.scal(2 * m, GU[mu]), wedge), Pi)
            ok &= eq(lhs, rhs)
            # control: the opposite sign of the bivector fails
            ok &= not eq(lhs, mul(Pp, GA.sub(GA.scal(2 * m, GU[mu]), wedge), Pi))
        for (y, z) in SIMPLEX:
            x = 1 - y - z
            k0 = GA.add(GA.scal(-y, q), GA.scal(z, p))
            kp0 = GA.add(GA.scal(1 - y, q), GA.scal(z, p))
            rows, rhs = [], []
            for mu in range(4):
                target = mul(Pp, vertex_numerator(mu, k0, kp0, m), Pi)
                basis = [mul(Pp, GU[mu], Pi),
                         GA.scal(comp_up(GA.add(p, pp), mu), mul(Pp, Pi)),
                         GA.scal(comp_up(q, mu), mul(Pp, Pi))]
                for bl in GA.all_blades(4):
                    rows.append([bv.get(bl, Fr(0)) for bv in basis])
                    rhs.append(target.get(bl, Fr(0)))
            a_, b_, c_ = solve_consistent(rows, rhs)
            # the fitted combination reproduces the sandwiched numerator exactly
            for mu in range(4):
                target = mul(Pp, vertex_numerator(mu, k0, kp0, m), Pi)
                fit = mul(Pp, GA.add(GA.scal(a_, GU[mu]), num(b_ * comp_up(GA.add(p, pp), mu)),
                                     num(c_ * comp_up(q, mu))), Pi)
                ok &= eq(target, fit)
            ok &= b_ == 2 * m * z * (1 - z)
            ok &= c_ == -2 * m * (z - 2) * (x - y)          # odd under x <-> y: integrates to zero
    # l^2 part: (1/4) sum_a g^nu g_a g^mu g^a g_nu = g^mu, a multiple of g^mu only (F1)
    for mu in range(4):
        lav = GA.scal(Fr(1, 4), GA.add(*[contract(G[a], GU[mu], GU[a]) for a in range(4)]))
        ok &= eq(lav, GU[mu])
    # exact Feynman-parameter integral: m int_0^1 dz int_0^{1-z} dy b/((1-z)^2 m^2) = int_0^1 2 z dz = 1
    inner = GA.pmul([Fr(0), Fr(2)], [Fr(1)])            # after the y-integral: (1-z) * 2 z (1-z)/(1-z)^2 = 2 z
    total = GA.peval(GA.ps_int(inner), Fr(1))
    ok &= total == 1
    # prefactor chain: (-i e^2) (vertex and propagator units) * 2 (Feynman parameters) * (-i/(32 pi^2))
    # (Wick-rotated integral of (l^2 - Delta)^{-3}) = -e^2/(16 pi^2), real; the Gordon term carries
    # b (g^mu ^ q) = -b (q ^ g^mu), and F2 multiplies q ^ g^mu/(2m): F2 = 2m (1/16) int b/Delta (e^2/pi^2)
    pref = QI(0, -1) * QI(2) * QI(0, -1) * QI(Fr(1, 32))
    ok &= pref == QI(Fr(-1, 16))
    F2_over_e2_pi2 = 2 * (-pref.re) * total
    ok &= F2_over_e2_pi2 == Fr(1, 8)                      # e^2/(8 pi^2) = alpha/(2 pi)
    GA.check("check_vertex_magnetic_part_and_schwinger_coefficient", ok)
    return ok


# ---------------------------------------------------------------- part 4: Ward identity
def check_resolvent_and_ward_takahashi_integrand():
    """Part 4: S(k) = (k - m)^{-1} = (k + m)/(Q(k) - m^2); S(k + h) - S(k) = -S(k + h) h S(k) exactly,
    so the self-energy integrand g^nu S(p - k) g_nu (photon momentum k, regulated in k only) satisfies
    Sigma(p + h) - Sigma(p) = -h_mu Lambda^mu(p + h, p) integrand by integrand: the Ward-Takahashi
    identity, and at h -> 0 Sigma'(p) = -Lambda(p, p), Z1 = Z2."""
    premise("field-theory.coupled-system-tree-level")
    m = WARD_M
    ok = True
    for p, h, k in WARD_SAMPLES:
        kk = GA.sub(p, k)
        Sk = inverse_dirac(kk, m)
        ok &= eq(mul(GA.sub(kk, num(m)), Sk), num(1))
        Skh = inverse_dirac(GA.add(kk, h), m)
        ok &= eq(GA.sub(Skh, Sk), GA.neg(mul(Skh, h, Sk)))
        sig_h = GA.add(*[mul(GU[n], Skh, G[n]) for n in range(4)])
        sig_0 = GA.add(*[mul(GU[n], Sk, G[n]) for n in range(4)])
        lam_h = GA.add(*[mul(GU[n], Skh, h, Sk, G[n]) for n in range(4)])
        ok &= eq(GA.sub(sig_h, sig_0), GA.neg(lam_h))
        # the identity holds in either order (both are the resolvent identity) ...
        ok &= eq(GA.sub(Skh, Sk), GA.neg(mul(Sk, h, Skh)))
        # ... and fails with the opposite sign, or without the second propagator
        ok &= not eq(GA.sub(Skh, Sk), mul(Skh, h, Sk)) and not eq(GA.sub(Skh, Sk), GA.neg(mul(h, Sk)))
    GA.check("check_resolvent_and_ward_takahashi_integrand", ok)
    return ok


# ---------------------------------------------------------------- part 5: where the unit sits
def prime_exponents(n):
    out, p = {}, 2
    while n > 1:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    return out


def check_unit_inside_massive_loop_breaks_transversality():
    """Part 5. Placing the unit as I4 at each propagator inside the Clifford product,
    4 <g^mu I4 (k + m) g^nu I4 (k' + m)>_0 = -N + 8 m^2 g^{mu nu} with N the numerator with a commuting
    unit (i i = -1 gives -N): the mass term changes sign because I4 anticommutes with g^nu but not with
    the even k g^nu. For m = 0 (chiral lines) the two agree. The extra 8 m^2 g multiplies the logarithmic
    integral, so under Pauli-Villars it leaves the non-transverse remainder proportional to
    sum_i c_i M_i^2 ln Delta_i, which is not zero: at q = 0 with M^2 = (1, 100, 300) it is
    c1 100 ln 100 + c2 300 ln 300 with c2 != 0, and ln 100, ln 300 are rationally independent
    (the prime 3 divides only 300)."""
    premise("field-theory.second-quantisation")
    ok = True
    q = QV
    for x in XS:
        for m in UNIT_MASSES:
            for l in UNIT_LOOPS:
                k = GA.sub(l, GA.scal(x, q))
                kp = GA.add(l, GA.scal(1 - x, q))
                for mu in range(4):
                    for nu in range(4):
                        n_c = 4 * sc(mul(GU[mu], GA.add(k, num(m)), GU[nu], GA.add(kp, num(m))))
                        n_i = 4 * sc(mul(GU[mu], I4, GA.add(k, num(m)), GU[nu], I4, GA.add(kp, num(m))))
                        ok &= n_i == -n_c + 8 * m * m * GINV[mu][nu]
    # Pauli-Villars weights and the remainder sum c_i M_i^2 ln M_i^2 at q = 0
    m2, M1, M2 = PV_SQUARES
    c2 = Fr(m2 - M1, M1 - M2)
    c1 = -1 - c2
    ok &= m2 + c1 * M1 + c2 * M2 == 0 and c1 * M1 != 0 and c2 * M2 != 0
    e1, e2 = prime_exponents(M1), prime_exponents(M2)
    # a ln M1 + b ln M2 = 0 with rational a, b forces b * e2[3] = 0 since 3 does not divide M1
    ok &= 3 in e2 and 3 not in e1 and e1 != {} and m2 == 1
    GA.check("check_unit_inside_massive_loop_breaks_transversality", ok)
    return ok
