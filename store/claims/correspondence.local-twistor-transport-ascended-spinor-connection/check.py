"""correspondence.local-twistor-transport-ascended-spinor-connection: exact checks in GTG form.

Everything is in Cl(2,4) with GA.py, using the model of the imported Fact
correspondence.imported-tractor-connection-local-twistor-transport (its EXPORTS): generators e0 (+1),
e1, e2, e3 (-1) for flat spacetime, e+ (+1), e- (-1); n0 = (e+ + e-)/2 = X_p, ninf = e+ - e- = u_p; the
conformal spinor space CS = Cl^+(2,4) P (real dimension 8, complex unit I6), S_pi = ker n0 and
S_omega = ker ninf in CS; rho(B) psi = B psi / 2.

Two gravitational fields on flat spacetime, in the store's GTG conventions (C2-C6, C10), at one point:
synchronous FLRW fields hb^{-1}(e0) = e0, hb^{-1}(e_i) = a e_i, Omega(e0) = 0, Omega(e_i) = -adot e0 e_i,
d_t Omega(e_i) = -addot e0 e_i: de Sitter in the flat slicing (a = 2, H = 1/2, adot = 1, addot = 1/2) and
dust (a = t^(2/3) at t = 8: a = 4, adot = 1/3, addot = -1/72).
(0) The fields are torsion-free, D_a hb^{-1}(b) = D_b hb^{-1}(a) with D_a = a.grad + Omega(a) x; the field
    strength R(a ^ b) = a.grad Omega(b) - b.grad Omega(a) + Omega(a) x Omega(b) gives the store curvature
    Rs(B) = -R(hb(B)); de Sitter: Rs(B) = H^2 B on all six planes (Lambda = 3 H^2); the Ricci map and
    scalar are contracted with the reciprocal frame and the Schouten map P = (Ric - (R/6) id)/2 is
    diag(alpha - beta/2, beta/2) with alpha = addot/a, beta = (adot/a)^2 (de Sitter: P = Lambda/6).
(1) Omega_T(a) = Omega(a) - ninf ^ e_a + n0 ^ P(e_a), e_a = hb^{-1}(a): Omega(a) commutes with n0 and ninf
    (Levi factor); the soldering summand is ninf ^ (vector orthogonal to n0, ninf) and the Schouten summand
    n0 ^ (such a vector), fixing n0, with abelian Schouten summands (nilradical); Omega_T(a) x V has the
    tractor slots (-mu.e_a, Omega(a) x mu + rho e_a - sigma P(e_a), P(e_a).mu) and preserves Q(V).
(2) E = ninf ^ n0 has E x (soldering) = +soldering, E x (Schouten) = -Schouten, E x Omega(a) = 0; rho(E) is
    +1/2 on S_omega and -1/2 on S_pi; the soldering summand maps S_pi into S_omega (nonzero) and kills
    S_omega, the Schouten summand maps S_omega into S_pi and kills S_pi, the Levi part keeps both planes, and
    all commute with I6 (complex-linear).
(3) On S_omega, sigma_a tau_c = rho(-ninf ^ e_a) rho(n0 ^ P(e_c)) = (1/2) e_a P(e_c) = (1/2) P_ac + rho(e_a ^ P(e_c)),
    P_ac = e_a . P(e_c), for all 16 pairs (a, c) and both fields; the soldering summand is Levi-equivariant,
    [rho(L), sigma(A)] = sigma(L x A) on S_pi for the six spacetime bivectors L.
The Penrose-Rindler index form and the comparison of conventions with it are an imported convention, not
computed; the uniqueness up to a scalar is correspondence.chiral-planes-summand-spaces(2).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
FIELDS = {"de Sitter": (F(2), F(1), F(1, 2)), "dust": (F(4), F(1, 3), F(-1, 72))}
SPACETIME = range(4)                         # indices of the spacetime generators e0..e3 in S
LORENTZ_PAIRS = tuple((k, l) for k in SPACETIME for l in SPACETIME if k < l)   # the six bivectors e_k e_l


def model():
    return premise("correspondence.imported-tractor-connection-local-twistor-transport")


def setup(M, a, adot, addot):
    E, mul, comm = M["E"], M["mul"], M["comm"]
    B = [None] + [mul(E[0], E[i]) for i in (1, 2, 3)]

    def hbinv(v):
        return GA.add(GA.scal(v.get((0,), F(0)), E[0]),
                      *[GA.scal(a * v.get((i,), F(0)), E[i]) for i in (1, 2, 3)])

    def hb(v):
        return GA.add(GA.scal(v.get((0,), F(0)), E[0]),
                      *[GA.scal(v.get((i,), F(0)) / a, E[i]) for i in (1, 2, 3)])

    def Omega(v):
        return GA.add(*[GA.scal(-adot * v.get((i,), F(0)), B[i]) for i in (1, 2, 3)]) if any(
            v.get((i,), F(0)) for i in (1, 2, 3)) else {}

    def dOmega(v, d):
        """(d . grad) Omega(v): only the time derivative is nonzero."""
        t = d.get((0,), F(0))
        return GA.add(*[GA.scal(-addot * t * v.get((i,), F(0)), B[i]) for i in (1, 2, 3)]) if t and any(
            v.get((i,), F(0)) for i in (1, 2, 3)) else {}

    def dhbinv(v, d):
        """(d . grad) hb^{-1}(v): a(t) differentiates to adot."""
        t = d.get((0,), F(0))
        return GA.add(*[GA.scal(adot * t * v.get((i,), F(0)), E[i]) for i in (1, 2, 3)]) if t else {}

    return E, mul, comm, B, hbinv, hb, Omega, dOmega, dhbinv


def curvature(M, field):
    E, mul, comm, B, hbinv, hb, Omega, dOmega, dhbinv = setup(M, *field)

    def R(x, y):
        return GA.add(dOmega(y, x), GA.neg(dOmega(x, y)), comm(Omega(x), Omega(y)))

    def Rs(i, j):
        """Store curvature of the physical plane e_i ^ e_j: -R(hb(e_i) ^ hb(e_j))."""
        return GA.neg(R(hb(E[i]), hb(E[j])))

    def dot(x, y):
        return GA.dot(x, y, S)

    def vdotb(v, Bv):
        return {k: c for k, c in GA.scal(F(1, 2), GA.sub(mul(v, Bv), mul(Bv, v))).items()}

    recip = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
    ric = []
    for b in range(4):
        tot = {}
        for m in range(4):
            if m != b:
                tot = GA.add(tot, vdotb(recip[m], Rs(m, b)))
        ric.append(tot)
    scalar = sum((dot(recip[b], ric[b]) for b in range(4)), F(0))
    P = [GA.scal(F(1, 2), GA.sub(ric[b], GA.scal(scalar / 6, E[b]))) for b in range(4)]
    return Rs, ric, scalar, P


def Pmap(P, v):
    """The Schouten map on a physical vector v = sum v^b e_b."""
    return GA.add(*[GA.scal(v.get((b,), F(0)), P[b]) for b in range(4) if v.get((b,), F(0))]) if any(
        v.get((b,), F(0)) for b in range(4)) else {}


def check_gtg_fields_torsion_free_and_store_curvature():
    premise("correspondence.imported-tractor-connection-local-twistor-transport")
    M = model()
    for name, field in FIELDS.items():
        a, adot, addot = field
        E, mul, comm, B, hbinv, hb, Omega, dOmega, dhbinv = setup(M, *field)
        for i in range(4):
            for j in range(4):
                lhs = GA.add(dhbinv(E[j], E[i]), comm(Omega(E[i]), hbinv(E[j])))
                rhs = GA.add(dhbinv(E[i], E[j]), comm(Omega(E[j]), hbinv(E[i])))
                assert GA.eq(lhs, rhs)
        assert GA.dot(hbinv(E[1]), hbinv(E[1]), S) == -a * a
        Rs, ric, scalar, P = curvature(M, field)
        alpha, beta = addot / a, (adot / a) * (adot / a)
        for i in (1, 2, 3):
            assert GA.eq(Rs(0, i), GA.scal(alpha, mul(E[0], E[i])))
            for j in (1, 2, 3):
                if i < j:
                    assert GA.eq(Rs(i, j), GA.scal(beta, mul(E[i], E[j])))
        assert GA.eq(ric[0], GA.scal(3 * alpha, E[0]))
        assert all(GA.eq(ric[i], GA.scal(alpha + 2 * beta, E[i])) for i in (1, 2, 3))
        assert scalar == 6 * alpha + 6 * beta
        assert GA.eq(P[0], GA.scal(alpha - beta / 2, E[0]))
        assert all(GA.eq(P[i], GA.scal(beta / 2, E[i])) for i in (1, 2, 3))
        if name == "de Sitter":
            H2 = F(1, 4)
            assert alpha == beta == H2
            assert GA.eq(P[0], GA.scal(3 * H2 / 6, E[0]))
        else:
            assert alpha == F(-1, 288) and beta == F(1, 144)
    return True


def omega_T_parts(M, field, P, v):
    E, mul, comm, B, hbinv, hb, Omega, dOmega, dhbinv = setup(M, *field)
    A = hbinv(v)
    return Omega(v), GA.neg(comm(M["NI"], A)), comm(M["N0"], Pmap(P, A)), A


def check_tractor_gauge_field_decomposition():
    premise("correspondence.imported-tractor-connection-local-twistor-transport")
    M = model()
    N0, NI, comm, mul = M["N0"], M["NI"], M["comm"], M["mul"]
    Ev = M["E"]
    V = GA.add(GA.scal(F(2), NI), Ev[0], GA.scal(F(3), Ev[2]), GA.scal(F(-7), N0))
    sig, mu, rh = F(2), GA.add(Ev[0], GA.scal(F(3), Ev[2])), F(-7)
    for field in FIELDS.values():
        Rs, ric, scalar, P = curvature(M, field)
        for i in range(4):
            lev, sold, sch, A = omega_T_parts(M, field, P, Ev[i])
            assert comm(lev, N0) == {} and comm(lev, NI) == {}
            assert GA.dot(A, N0, S) == 0 and GA.dot(A, NI, S) == 0
            assert GA.eq(sold, GA.neg(comm(NI, A)))
            assert comm(sch, N0) == {}
            for j in range(4):
                sch2 = omega_T_parts(M, field, P, Ev[j])[2]
                assert comm(sch, sch2) == {}
            full = GA.add(lev, sold, sch)
            DV = comm(full, V)
            PA = Pmap(P, A)
            s1, r1 = GA.dot(DV, N0, S), GA.dot(DV, NI, S)
            m1 = {k: c for k, c in DV.items() if len(k) == 1 and k[0] < 4}
            assert s1 == -GA.dot(mu, A, S)
            assert GA.eq(m1, GA.add(comm(lev, mu), GA.scal(rh, A), GA.scal(-sig, PA)))
            assert r1 == GA.dot(PA, mu, S)
            assert GA.dot(V, DV, S) == 0
    return True


def check_grading_weights_and_spinor_blocks():
    premise("correspondence.imported-tractor-connection-local-twistor-transport")
    premise("correspondence.clifford-side-ordering-shift")
    M = model()
    N0, NI, comm, mul, rho, I6 = M["N0"], M["NI"], M["comm"], M["mul"], M["rho"], M["I6"]
    in_span, kernel_in_cs, CS = M["in_span"], M["kernel_in_cs"], M["CS"]
    Egr = comm(NI, N0)
    Spi, Som = kernel_in_cs(N0), kernel_in_cs(NI)
    assert len(Spi) == 4 and len(Som) == 4
    assert all(GA.eq(rho(Egr, w), GA.scal(F(1, 2), w)) for w in Som)
    assert all(GA.eq(rho(Egr, p), GA.scal(F(-1, 2), p)) for p in Spi)
    for field in FIELDS.values():
        Rs, ric, scalar, P = curvature(M, field)
        for i in range(4):
            lev, sold, sch, A = omega_T_parts(M, field, P, M["E"][i])
            assert GA.eq(comm(Egr, sold), sold) and GA.eq(comm(Egr, sch), GA.neg(sch)) and comm(Egr, lev) == {}
            for p in Spi:
                assert in_span(rho(sold, p), Som) and not GA.is_zero(rho(sold, p))
                assert GA.is_zero(rho(sch, p)) and in_span(rho(lev, p), Spi)
            for w in Som:
                assert GA.is_zero(rho(sold, w)) and in_span(rho(lev, w), Som)
                assert in_span(rho(sch, w), Spi) and not GA.is_zero(rho(sch, w))
            full = GA.add(lev, sold, sch)
            for psi in CS:
                assert GA.eq(mul(full, I6, psi), mul(I6, full, psi))
    return True


def check_summand_composite_and_equivariance():
    premise("correspondence.imported-tractor-connection-local-twistor-transport")
    M = model()
    N0, NI, comm, mul, rho = M["N0"], M["NI"], M["comm"], M["mul"], M["rho"]
    in_span, kernel_in_cs = M["in_span"], M["kernel_in_cs"]
    Ev = M["E"]
    Spi, Som = kernel_in_cs(N0), kernel_in_cs(NI)
    for field in FIELDS.values():
        Rs, ric, scalar, P = curvature(M, field)
        E_, mul_, comm_, B, hbinv, hb, Omega, dOmega, dhbinv = setup(M, *field)
        for i in SPACETIME:
            Ea = hbinv(Ev[i])
            sig_a = GA.neg(comm(NI, Ea))
            for j in SPACETIME:
                PEc = Pmap(P, hbinv(Ev[j]))
                tau_c = comm(N0, PEc)
                Pac = GA.dot(Ea, PEc, S)
                for w in Som:
                    comp = rho(sig_a, rho(tau_c, w))
                    assert GA.eq(comp, GA.scal(F(1, 2), mul(Ea, PEc, w)))
                    assert GA.eq(comp, GA.add(GA.scal(Pac / 2, w), rho(comm(Ea, PEc), w)))
            for (k, l) in LORENTZ_PAIRS:
                L = mul(Ev[k], Ev[l])
                for p in Spi:
                    lhs = GA.sub(rho(L, rho(sig_a, p)), rho(sig_a, rho(L, p)))
                    assert GA.eq(lhs, rho(GA.neg(comm(NI, comm(L, Ea))), p))
    return True
