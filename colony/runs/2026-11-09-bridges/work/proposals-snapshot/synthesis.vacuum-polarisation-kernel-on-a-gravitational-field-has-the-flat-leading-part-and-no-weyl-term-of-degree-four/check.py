"""synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four: exact checks.

The one-loop vacuum-polarisation trace form of the Dirac Hadamard parametrix on a torsion-free gravitational field
(spacetime algebra Cl(1,3), exact rationals). Conventions of the store: the covariant field strength of the gauge
field is Rfs(a ^ b) = a.grad Omega(b) - b.grad Omega(a) + ..., and the curvature operator is Riem(B) = -Rfs(B).

  (1) the transport rotors cancel from the leading kernel: with s the physical tangent at x, R the transport rotor
      from x' to x, s' = -R~ s R the tangent at x' and b^ = R b R~,
          < a (s R) b (s' R~) >_0 = -( 2 (a.s)(b^.s) - (a.b^) Q(s) ),
      the flat trace in the vector s; the mass cross term < a (s R) b R~ >_0 vanishes and the mass-mass trace is a.b^;
  (2) the contraction gamma^mu Riem(e_mu ^ xi) is the Ricci vector, with no trivector part, for curvature operators
      obeying the protraction identity, and is zero for operators of Weyl type (type D and sums of rotated
      copies); a map violating the protraction identity has a trivector part (control);
  (3) the first-order covariant derivative of the transport rotor in the gauge Omega(a)(z) = -(1/2) Riem(z ^ a),
      whose field strength is -Riem (the stored sign): R(y, y') = 1 + (1/4) Riem(ybar ^ d) and
      a.D R = +(1/4) Riem(a ^ d); the gauge with the other sign has field strength +Riem and is rejected;
  (4) the first-order part of D_x U, U = Delta^{1/2} R: +(1/12) Ric(xi), zero for operators of Weyl type; the
      de Sitter test Riem(B) = (L/3) B gives D_x U = (L/12) xi; the wrong relative sign would give -(5/12);
  (5) the tidal map K(a) = Riem(a ^ xi) . xi of a Weyl-type operator has zero trace and nonzero trace of its square:
      the Van Vleck determinant carries the Weyl operator quadratically (degree 2 of the kernel);
  (6) degrees: the bookkeeping of the scaling degrees of the terms of the kernel.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
G = [GA.gen(i) for i in range(4)]                       # gamma_0, ..., gamma_3
GUP = [GA.scal(SQ[i], G[i]) for i in range(4)]          # reciprocal frame
BIV = [(i, j) for i in range(4) for j in range(i + 1, 4)]


def mul(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def s0(x):
    return x.get((), F(0))


def vec(c):
    return GA.add(*[GA.scal(F(x), G[i]) for i, x in enumerate(c) if x != 0]) if any(c) else {}


def wedge(a, b):
    return grade(GA.scal(F(1, 2), GA.sub(mul(a, b), mul(b, a))), 2)


def Q(v):
    return GA.dot(v, v, SQ)


def rotor(biv_coeffs):
    """Exact rotor by the Cayley transform R = (1 + B)(1 - B)^{-1}; B^2 = alpha + beta I commutes with B."""
    B = GA.add(*[GA.scal(F(c), mul(G[i], G[j])) for (i, j), c in zip(BIV, biv_coeffs) if c != 0])
    one = GA.sc(1)
    B2 = mul(B, B)
    den = GA.sub(one, B2)                                # alpha' + beta' I
    al, be = den.get((), F(0)), den.get((0, 1, 2, 3), F(0))
    I4 = mul(G[0], G[1], G[2], G[3])
    n2 = al * al + be * be                               # (al + be I)(al - be I) = al^2 + be^2 since I^2 = -1
    assert n2 != 0
    den_inv = GA.scal(1 / n2, GA.sub(GA.sc(al), GA.scal(be, I4)))
    num = mul(GA.add(one, B), GA.add(one, B))            # (1+B)/(1-B) = (1+B)^2/(1-B^2)
    R = mul(num, den_inv)
    assert GA.eq(mul(R, GA.reverse(R)), one)
    return R


ROTORS = [(F(1, 2), 0, 0, 0, 0, 0), (F(1, 3), 0, F(1, 5), 0, 0, 0), (0, 0, 0, F(2, 3), 0, F(-1, 5)),
          (F(1, 4), F(-1, 3), F(2, 5), F(1, 7), F(-3, 8), F(1, 2))]
VECS = [(1, 0, 0, 0), (2, 1, 0, 0), (1, 2, 3, 4), (F(3, 2), -1, F(1, 3), 2), (0, 1, 1, 0), (5, -2, F(7, 3), 1)]


def check_transport_rotors_cancel_from_the_leading_kernel():
    premise("synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field")
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    premise("synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants")
    n = 0
    for rc in ROTORS:
        R = rotor(rc)
        Rt = GA.reverse(R)
        for sv in VECS:
            s = vec(sv)
            sp = GA.neg(mul(Rt, s, R))                   # tangent at x'
            assert Q(sp) == Q(s)
            for av in VECS[:4]:
                for bv in VECS[2:]:
                    a, b = vec(av), vec(bv)
                    bh = mul(R, b, Rt)
                    assert all(len(k) == 1 for k in bh)  # the transported vector is a vector
                    lead = s0(mul(a, mul(s, R), b, mul(sp, Rt)))
                    flat = -(2 * GA.dot(a, s, SQ) * GA.dot(bh, s, SQ) - GA.dot(a, bh, SQ) * Q(s))
                    assert lead == flat
                    assert s0(mul(a, mul(s, R), b, Rt)) == 0            # mass cross term: odd, no scalar part
                    assert s0(mul(a, R, b, mul(sp, Rt))) == 0
                    assert s0(mul(a, R, b, Rt)) == GA.dot(a, bh, SQ)    # mass-mass term
                    n += 1
    assert n == 4 * 6 * 4 * 4
    # the flat trace of the stored result: < g_mu x g_nu x >_0 = 2 x_mu x_nu - g_mu_nu Q(x)
    x = vec((1, 2, 3, 4))
    for i in range(4):
        for j in range(4):
            gij = SQ[i] if i == j else 0
            xi_, xj_ = GA.dot(G[i], x, SQ), GA.dot(G[j], x, SQ)
            assert s0(mul(G[i], x, G[j], x)) == 2 * xi_ * xj_ - gij * Q(x)
    # control: with the tangent at x' not transported (s' = -s) the identity fails for a nontrivial rotor
    R = rotor(ROTORS[3]); Rt = GA.reverse(R)
    s, a, b = vec(VECS[2]), vec(VECS[1]), vec(VECS[3])
    bh = mul(R, b, Rt)
    assert s0(mul(a, mul(s, R), b, mul(GA.neg(s), Rt))) != -(2 * GA.dot(a, s, SQ) * GA.dot(bh, s, SQ) - GA.dot(a, bh, SQ) * Q(s))
    return True


# linear maps on bivectors: dict from basis bivector index pair to a bivector
def apply(Riem, B):
    out = {}
    for (i, j) in BIV:
        c = B.get((i, j), F(0))
        if c != 0:
            out = GA.add(out, GA.scal(c, Riem[(i, j)]))
    return out


def weyl_type_D(c, sigma):
    """B -> c (B + 3 sigma B sigma), sigma a unit timelike bivector (sigma^2 = 1)."""
    assert GA.eq(mul(sigma, sigma), GA.sc(1))
    return {(i, j): GA.scal(c, GA.add(mul(G[i], G[j]), GA.scal(3, mul(sigma, mul(G[i], G[j]), sigma)))) for (i, j) in BIV}


def ricci_type(P):
    """a ^ b -> (1/2)(P(a) ^ b + a ^ P(b)), P a symmetric linear map on vectors given by its matrix P[i][j] = e_i.P(e_j)."""
    def Pv(v):
        out = {}
        for j in range(4):
            vj = GA.dot(v, GUP[j], SQ)                   # component along e_j
            if vj != 0:
                out = GA.add(out, GA.scal(vj, GA.add(*[GA.scal(F(P[i][j]), GUP[i]) for i in range(4) if P[i][j] != 0])))
        return out
    return {(i, j): GA.scal(F(1, 2), GA.add(wedge(Pv(G[i]), G[j]), wedge(G[i], Pv(G[j])))) for (i, j) in BIV}


def add_maps(*Ms):
    return {k: GA.add(*[M[k] for M in Ms]) for k in BIV}


def rotate_map(M, R):
    """B -> R M(R~ B R) R~."""
    Rt = GA.reverse(R)
    return {(i, j): mul(R, apply(M, grade(mul(Rt, mul(G[i], G[j]), R), 2)), Rt) for (i, j) in BIV}


def contraction(Riem, xi):
    """gamma^mu Riem(e_mu ^ xi): returns (vector part, trivector part)."""
    tot = {}
    for m in range(4):
        tot = GA.add(tot, mul(GUP[m], apply(Riem, wedge(G[m], xi))))
    return grade(tot, 1), grade(tot, 3)


def ricci(Riem, xi):
    """The Ricci vector d_a . Riem(a ^ xi)."""
    return contraction(Riem, xi)[0]


SIG = mul(G[1], G[0])                                    # e_r e_t with e_r = gamma_1: unit timelike bivector
P_SYM = [[2, 1, 0, 3], [1, -1, 4, 0], [0, 4, 5, -2], [3, 0, -2, 1]]


def weyl_examples():
    W1 = weyl_type_D(F(-1, 2), SIG)
    W2 = rotate_map(weyl_type_D(F(3, 7), SIG), rotor(ROTORS[3]))
    W3 = rotate_map(weyl_type_D(F(2), SIG), rotor(ROTORS[2]))
    return [W1, W2, add_maps(W1, W2, W3)]


def check_contraction_of_the_field_strength_is_the_ricci_vector():
    premise("synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field")
    for W in weyl_examples():
        assert any(W[k] for k in BIV)                    # the field strength is not zero
        for xv in VECS:
            v, t = contraction(W, vec(xv))
            assert v == {} and t == {}                   # Weyl type: the whole contraction vanishes
    Rc = ricci_type(P_SYM)
    full = add_maps(Rc, weyl_examples()[2])
    nonzero = 0
    for xv in VECS:
        xi = vec(xv)
        v, t = contraction(full, xi)
        assert t == {}                                   # no trivector part (protraction identity)
        assert GA.eq(v, ricci(Rc, xi))                   # the Weyl part does not contribute
        nonzero += 1 if v else 0
    assert nonzero == len(VECS)
    # control: a map that violates the protraction identity (gamma_0 gamma_1 -> gamma_2 gamma_3 alone)
    bad = {k: {} for k in BIV}
    bad[(0, 1)] = mul(G[2], G[3])
    assert contraction(bad, vec((0, 1, 0, 0)))[1] != {}
    return True


def omega_gauge(a, z, M, sign=-1):
    """Omega(a)(x0 + z) = sign (1/2) Riem(z ^ a); sign = -1 is the gauge of the proof."""
    return GA.scal(F(sign, 2), apply(M, wedge(z, a)))


def transport(y, yp, M, sign=-1):
    """Transport rotor to second order from the stored Taylor datum R = 1 - (1/2) (ybar . grad) Omega(d)."""
    ybar, d = GA.scal(F(1, 2), GA.add(y, yp)), GA.sub(y, yp)
    return GA.sub(GA.sc(1), GA.scal(F(1, 2), omega_gauge(d, ybar, M, sign)))


def de_sitter(lam):
    """Riem(B) = (lam/3) B."""
    return {(i, j): GA.scal(F(lam, 3), mul(G[i], G[j])) for (i, j) in BIV}


def check_first_order_derivative_of_the_transport_rotor():
    premise("synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field")
    full = add_maps(ricci_type(P_SYM), weyl_examples()[2])
    half, quarter = F(1, 2), F(1, 4)
    for M in (full, weyl_examples()[0], de_sitter(3)):
        # the gauge against the stored sign: its field strength a.grad Omega(b) - b.grad Omega(a) is -Riem(a ^ b)
        for av in VECS[:3]:
            for bv in VECS[3:]:
                a, b = vec(av), vec(bv)
                fs = GA.sub(omega_gauge(b, a, M), omega_gauge(a, b, M))          # Omega is linear in z
                assert GA.eq(fs, GA.neg(apply(M, wedge(a, b))))
                fs_wrong = GA.sub(omega_gauge(b, a, M, sign=1), omega_gauge(a, b, M, sign=1))
                assert GA.eq(fs_wrong, apply(M, wedge(a, b))) and not GA.eq(fs_wrong, GA.neg(apply(M, wedge(a, b))))
        for yv in VECS[:4]:
            for ypv in VECS[2:5]:
                y, yp = vec(yv), vec(ypv)
                d = GA.sub(y, yp)
                ybar = GA.scal(half, GA.add(y, yp))
                assert GA.eq(transport(y, yp, M), GA.add(GA.sc(1), GA.scal(quarter, apply(M, wedge(ybar, d)))))
                for av in VECS[:3]:
                    a = vec(av)
                    # directional derivative of a quadratic polynomial, exact by the symmetric difference
                    dR = GA.scal(half, GA.sub(transport(GA.add(y, a), yp, M), transport(GA.sub(y, a), yp, M)))
                    cov = GA.add(dR, GA.scal(half, omega_gauge(a, y, M)))        # leading order: R = 1 in the connection term
                    assert GA.eq(cov, GA.scal(quarter, apply(M, wedge(a, d))))
        # D R = gamma^mu (e_mu . D R) = +(1/4) Ric(d)
        for dv in VECS:
            d = vec(dv)
            tot = {}
            for m in range(4):
                tot = GA.add(tot, mul(GUP[m], GA.scal(quarter, apply(M, wedge(G[m], d)))))
            assert GA.eq(tot, GA.scal(quarter, ricci(M, d)))
    return True


def first_order_DU(M, d, rotor_sign=1):
    """grad Delta^{1/2} + rotor_sign (1/4) Ric(d), Delta^{1/2} = 1 - (1/12) d . Ric(d)."""
    def root_delta(v):
        return 1 - F(1, 12) * GA.dot(v, ricci(M, v), SQ)
    grad = {}
    for m in range(4):                                   # gradient of a quadratic form: symmetric difference
        dm = (root_delta(GA.add(d, G[m])) - root_delta(GA.sub(d, G[m]))) / 2
        grad = GA.add(grad, GA.scal(dm, GUP[m]))
    return GA.add(grad, GA.scal(F(rotor_sign, 4), ricci(M, d)))


def check_first_order_part_of_the_derivative_of_the_leading_coefficient():
    """D_x U at first order, U = Delta^{1/2} R, Delta = 1 + (1/6) Ric0(d, d), Ric0(d, d) = -d . Ric(d)."""
    premise("synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field")
    premise("synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport")
    full = add_maps(ricci_type(P_SYM), weyl_examples()[2])
    for M, vacuum in ((full, False), (weyl_examples()[2], True), (weyl_examples()[0], True)):
        for dv in VECS:
            d = vec(dv)
            DU = first_order_DU(M, d)
            assert GA.eq(DU, GA.scal(F(1, 12), ricci(M, d)))
            assert (DU == {}) == vacuum
    # the de Sitter test: Riem(B) = (L/3) B, Ric(xi) = L xi, D_x U = (L/12) xi; the other relative sign gives -(5/12) L xi
    for lam in (3, 1, -6):
        M = de_sitter(lam)
        for dv in VECS:
            d = vec(dv)
            assert GA.eq(ricci(M, d), GA.scal(lam, d))
            assert GA.eq(first_order_DU(M, d), GA.scal(F(lam, 12), d))
            assert GA.eq(first_order_DU(M, d, rotor_sign=-1), GA.scal(F(-5 * lam, 12), d))
            assert not GA.eq(first_order_DU(M, d, rotor_sign=-1), GA.scal(F(lam, 12), d))
    return True


def check_tidal_map_of_a_weyl_type_operator():
    """K(a) = Riem(a ^ xi) . xi: trace zero and trace of the square not zero for Weyl type."""
    premise("synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field")
    def tidal(M, xi, a):
        B = apply(M, wedge(a, xi))
        return grade(GA.scal(F(1, 2), GA.sub(mul(B, xi), mul(xi, B))), 1)        # B . xi
    for W in weyl_examples():
        nonzero = 0
        for xv in VECS[2:]:
            xi = vec(xv)
            K = [[GA.dot(GUP[i], tidal(W, xi, G[j]), SQ) for j in range(4)] for i in range(4)]
            assert sum(K[i][i] for i in range(4)) == 0                            # Ricci-free
            tr2 = sum(K[i][j] * K[j][i] for i in range(4) for j in range(4))
            nonzero += 1 if tr2 != 0 else 0
        assert nonzero >= 3
    return True


def check_degrees_of_the_terms_of_the_kernel():
    premise("synthesis.imported-epstein-glaser-extension-theorem-and-ward-preserving-time-ordered-products")
    premise("synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants")
    dim = 4
    # scaling degree of (smooth vanishing to order j) / sigma^k is 2k - j; a logarithm adds nothing
    def deg(k, j):
        return 2 * k - j
    lead = deg(2, 1)                    # s / sigma^2
    mass = deg(1, 0)                    # m U / sigma
    dU = deg(1, 1)                      # (D U) / sigma, D U = O(xi)
    dU_vac = deg(1, 2)                  # vacuum field: D U = O(xi^2)
    vlog = deg(1, 1)                    # V s / sigma
    assert (lead, mass, dU, dU_vac, vlog) == (3, 2, 1, 0, 1)
    assert 2 * lead == 6 and 2 * lead - dim == 2                 # the flat degree of divergence
    assert lead + mass == 5                                       # odd trace: absent (check 1)
    assert max(2 * mass, lead + dU, lead + vlog) == 4 and 4 - dim == 0
    assert lead + dU_vac == 3                                     # grad Riem terms on a vacuum field
    assert 2 * lead - 4 == 2                                      # (Delta - 1) Pi^0 on a vacuum field: Delta - 1 = O(xi^4)
    n_local = sum(1 for a in range(3) for b in range(3) for c in range(3) for e in range(3) if a + b + c + e <= 2)
    assert n_local == 15                                          # derivatives of delta of order at most 2 in 4 dims
    return True
