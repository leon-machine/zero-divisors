"""synthesis.clausius-is-window-first-law-plus-boost-charge-deposit: exact checks.

Logarithms are exact: every logarithm that occurs is ln q for a positive rational q (Boltzmann factors
r = e^{beta omega} are taken rational, occupations are rational), and ln q is stored as its vector of
prime exponents {p: v_p(q)}. The ln p of distinct primes are linearly independent over Q (unique
factorisation and the transcendence of e are not needed: a rational relation sum c_p ln p = 0 with
integer c_p would give prod p^{c_p} = 1), so an identity among such combinations holds if and only if
it holds prime by prime.
CAR operators are built in GA: mode j is the ascent pair of Cl(n, n), a_j = (e+_j + e-_j)/2,
a_j* = (e+_j - e-_j)/2, with e+_j = gen(2j), e-_j = gen(2j+1).
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, gen, sc
from tp_premise import premise


# ----------------------------------------------------------------------------- exact logarithms

def _factor(n):
    out, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def ln(q):
    """ln q for a positive rational q, as {prime: Fraction exponent}."""
    q = F(q)
    assert q > 0
    out = {}
    for p, e in _factor(q.numerator).items():
        out[p] = out.get(p, F(0)) + e
    for p, e in _factor(q.denominator).items():
        out[p] = out.get(p, F(0)) - e
    return {p: c for p, c in out.items() if c != 0}


def ladd(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def lsc(c, x):
    return {k: F(c) * v for k, v in x.items() if F(c) * v != 0}


def lneg(x):
    return lsc(-1, x)


def h(q):
    """binary entropy -q ln q - (1-q) ln(1-q) of an occupation 0 < q < 1."""
    q = F(q)
    return ladd(lsc(-q, ln(q)), lsc(-(1 - q), ln(1 - q)))


def D(q, n):
    """relative entropy of the one-mode state of occupation q to that of occupation n."""
    q, n = F(q), F(n)
    return ladd(lsc(q, ln(q / n)), lsc(1 - q, ln((1 - q) / (1 - n))))


# ----------------------------------------------------------------------------- CAR in GA

def squares(n):
    return tuple([1, -1] * n)


def ann(j):
    return scal(F(1, 2), add(gen(2 * j), gen(2 * j + 1)))


def cre(j):
    return scal(F(1, 2), sub(gen(2 * j), gen(2 * j + 1)))


def dGamma(Mx, n):
    """second quantisation sum_ij M_ij a_i* a_j of a one-particle matrix M."""
    sq = squares(n)
    out = {}
    for i in range(n):
        for j in range(n):
            if Mx[i][j] != 0:
                out = add(out, scal(F(Mx[i][j]), mul(cre(i), ann(j), sq)))
    return out


def comm(x, y, sq):
    return sub(mul(x, y, sq), mul(y, x, sq))


def mcomm(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] - B[i][k] * A[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


# ----------------------------------------------------------------------------- the two-mode model

def model(r_F, r_m, p, c, s):
    """Window mode b (Boltzmann factor r_F, in its KMS state n_I = 1/(1 + r_F)), matter mode a
    (Boltzmann factor r_m, any occupation p), a number-conserving hopping that rotates (a, b) by the
    rational rotation (c, s), c^2 + s^2 = 1. Returns the occupations after the process and the
    joint state's eigenvalues, from the explicit 4 x 4 density matrix on the occupation basis."""
    assert c * c + s * s == 1
    nI = 1 / (1 + F(r_F))
    # occupation basis 00, 10 (a), 01 (b), 11; the product state is diagonal
    rho = [(1 - p) * (1 - nI), p * (1 - nI), (1 - p) * nI, p * nI]
    # U: identity on 00 and 11 (det of the rotation is 1), rotation on the one-particle block
    one = [[rho[1], F(0)], [F(0), rho[2]]]
    R = [[c, -s], [s, c]]
    RT = [[c, s], [-s, c]]
    blk = GA.mat_mul(GA.mat_mul(R, one), RT)
    occ_a = blk[0][0] + rho[3]
    occ_b = blk[1][1] + rho[3]
    # spectrum of the joint state: the unitary preserves it
    tr = blk[0][0] + blk[1][1]
    det = blk[0][0] * blk[1][1] - blk[0][1] * blk[1][0]
    assert tr == rho[1] + rho[2] and det == rho[1] * rho[2]
    return nI, occ_a, occ_b, [rho[0], rho[1], rho[2], rho[3]]


def S_spec(spec):
    return ladd(*[lsc(-x, ln(x)) for x in spec if x != 0])


# ----------------------------------------------------------------------------- checks

def check_second_quantisation_carries_conservation():
    premise("field-theory.second-quantisation")
    n = 3
    sq = squares(n)
    for j in range(n):
        assert add(mul(ann(j), cre(j), sq), mul(cre(j), ann(j), sq)) == sc(1)
        for k in range(n):
            if k != j:
                assert add(mul(ann(j), cre(k), sq), mul(cre(k), ann(j), sq)) == {}
    A = [[F(1), F(2), F(0)], [F(-1), F(3), F(1, 2)], [F(0), F(5), F(-2)]]
    B = [[F(0), F(1), F(-3)], [F(2), F(1, 3), F(0)], [F(1), F(0), F(4)]]
    assert comm(dGamma(A, n), dGamma(B, n), sq) == dGamma(mcomm(A, B), n)
    assert mcomm(A, B)[0][1] == F(41, 3) and mcomm(A, B)[2][1] == F(-61, 3)
    assert dGamma(mcomm(A, B), n) != dGamma(mcomm(B, A), n)
    # boost charge H = dGamma(diag weights): window mode 0 (weight 2), matter modes 1, 2 (weights 2, 5)
    w = [F(2), F(2), F(5)]
    H = dGamma([[w[i] if i == j else F(0) for j in range(n)] for i in range(n)], n)
    resonant = [[F(0), F(1), F(0)], [F(1), F(0), F(0)], [F(0), F(0), F(0)]]
    detuned = [[F(0), F(0), F(1)], [F(0), F(0), F(0)], [F(1), F(0), F(0)]]
    assert w[0] == w[1] and w[2] != w[0]
    assert comm(dGamma(resonant, n), H, sq) == {}
    assert comm(dGamma(detuned, n), H, sq) != {}
    # one-particle criterion: [v, diag w]_ij = v_ij (w_j - w_i)
    for v in (resonant, detuned):
        Wd = [[w[i] if i == j else F(0) for j in range(n)] for i in range(n)]
        zero = all(x == 0 for rowv in mcomm(v, Wd) for x in rowv)
        assert zero == (comm(dGamma(v, n), H, sq) == {})
    return True


def check_window_identity_and_joint_identity():
    premise("synthesis.boundary-mode-first-law-of-entanglement")
    premise("field-theory.second-quantisation")
    for (r, p, c, s) in ((F(3), F(1, 7), F(3, 5), F(4, 5)), (F(5, 2), F(4, 5), F(5, 13), F(12, 13)),
                         (F(1, 4), F(2, 3), F(8, 17), F(15, 17))):
        nI, na, nb, spec = model(r, r, p, c, s)
        premise("hawking.i-state")
        assert nI in (F(1, 4), F(2, 7), F(4, 5)) and (1 - nI) / nI == r    # Gibbs occupation, ratio r
        lnr = ln(r)
        dSF = ladd(h(nb), lneg(h(nI)))
        # resonance: the boost charge omega (N_a + N_b) is conserved
        assert na + nb == p + nI
        beta_dQ = lsc(p - na, lnr)                       # heat: boost energy matter lost, times beta
        beta_dHF = lsc(nb - nI, lnr)
        assert beta_dQ == beta_dHF
        # (a) window identity: Delta S_F = beta Delta<H_F> - D(rho_F' || rho_I)
        assert dSF == ladd(beta_dHF, lneg(D(nb, nI)))
        # (b) joint identity: Delta S_F = beta dQ + I(F:m)' + Delta D(rho_m || sigma_m)
        S_joint = S_spec(spec)
        assert S_joint == ladd(h(p), h(nI))
        I_after = ladd(h(na), h(nb), lneg(S_joint))
        dDm = ladd(D(na, nI), lneg(D(p, nI)))
        assert dSF == ladd(beta_dQ, I_after, dDm)
        # (c) together: D(rho_F'||rho_I) + I' = -Delta D_m, the matter's distance to its boost-KMS
        #     state falls by what the window and the correlations gain
        assert ladd(D(nb, nI), I_after) == lneg(dDm)
        assert dSF != beta_dQ                             # at finite rotation the defect is present
    return True


def check_detuned_coupling_breaks_clausius():
    premise("synthesis.boundary-mode-first-law-of-entanglement")
    rF, rm, p, c, s = F(3), F(7), F(1, 5), F(3, 5), F(4, 5)
    nI, na, nb, spec = model(rF, rm, p, c, s)
    assert na + nb == p + nI                              # number conserved, boost charge not
    dn = nb - nI
    assert dn == p - na and dn != 0
    # first order in tau: d S_F = ln(rF) dn, beta dQ = ln(rm) dn: different prime content
    assert lsc(dn, ln(rF)) != lsc(dn, ln(rm))
    # the window's first law itself still holds exactly
    assert ladd(h(nb), lneg(h(nI))) == ladd(lsc(dn, ln(rF)), lneg(D(nb, nI)))
    # the joint identity needs no conservation: matter's KMS state at its own weight, n_m = 1/(1 + rm)
    nm = 1 / (1 + rm)
    S_joint = S_spec(spec)
    I_after = ladd(h(na), h(nb), lneg(S_joint))
    dDm = ladd(D(na, nm), lneg(D(p, nm)))
    assert ladd(h(nb), lneg(h(nI))) == ladd(lsc(p - na, ln(rm)), I_after, dDm)
    return True


def check_zero_weight_window_absorbs_no_heat():
    premise("synthesis.residue-from-mode-entropy")
    premise("synthesis.boundary-mode-thermal-entropy")
    n = 2
    sq = squares(n)
    H0 = dGamma([[F(0), F(0)], [F(0), F(0)]], n)
    assert H0 == {}                                        # zero weights: H_F = 0
    # a conserving coupling only reaches matter modes of zero weight: heat 0
    r, p, c, s = F(1), F(1, 9), F(3, 5), F(4, 5)
    nI, na, nb, spec = model(r, r, p, c, s)
    assert nI == F(1, 2) and ln(r) == {}
    dSF = ladd(h(nb), lneg(h(nI)))
    assert dSF == lneg(D(nb, nI))                          # Delta S_F = -D <= 0 (Klein)
    assert dSF != {} and nb != nI
    assert h(F(1, 2)) == ln(F(2))                          # ln 2 per mode, the maximum
    # a detuned coupling moves matter boost energy but the window's entropy has zero first-order
    # coefficient: ln(1) dn = 0 while beta dQ = ln(rm) dn
    nI2, na2, nb2, _ = model(F(1), F(5), p, c, s)
    dn = nb2 - nI2
    assert lsc(dn, ln(F(1))) == {} and lsc(dn, ln(F(5))) != {}
    return True


def check_horizon_boost_charge_chiral():
    """On a horizon generator with affine coordinate v, chi = kappa v d_v, a chiral mode psi(v)
    (Gaussian-rational polynomial times (1 - v^2)^2, vanishing with its derivative at v = -1, 1) has
    int chi^v T_vv dv = kappa <psi, i(v d_v + 1/2) psi> for T_vv = (i/2)(conj(psi) psi' - conj(psi') psi),
    the one-particle generator of dilations of v; exact polynomial integration over [-1, 1]."""
    premise("field-theory.second-quantisation")
    from GA import QI

    def pm(a, b):
        out = [QI(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i + j] = out[i + j] + x * y
        return out

    def pd(a):
        return [a[k] * QI(k) for k in range(1, len(a))] or [QI(0)]

    def pc(a):
        return [x.conj() for x in a]

    def padd2(a, b):
        m = max(len(a), len(b))
        a2 = a + [QI(0)] * (m - len(a))
        b2 = b + [QI(0)] * (m - len(b))
        return [x + y for x, y in zip(a2, b2)]

    def integ(a):                                          # int_{-1}^{1} sum a_k v^k dv
        tot = QI(0)
        for k, x in enumerate(a):
            if k % 2 == 0:
                tot = tot + x * QI(F(2, k + 1))
        return tot

    bump = [QI(1), QI(0), QI(-2), QI(0), QI(1)]           # (1 - v^2)^2
    I_ = QI(0, 1)
    v = [QI(0), QI(1)]
    vals = []
    for core in ([QI(1), QI(2, -1), QI(0, 3)], [QI(F(1, 2), 1), QI(0), QI(-1, 2), QI(1)]):
        psi = pm(core, bump)
        T = [x * I_ * QI(F(1, 2)) for x in padd2(pm(pc(psi), pd(psi)), [-y for y in pm(pc(pd(psi)), psi)])]
        lhs = integ(pm(v, T))                              # int v T_vv dv (kappa = 1)
        gen_psi = [x * I_ for x in padd2(pm(v, pd(psi)), [y * QI(F(1, 2)) for y in psi])]
        rhs = integ(pm(pc(psi), gen_psi))
        assert lhs == rhs
        assert lhs.im == 0 and lhs != QI(0)                # real, nonzero: a genuine charge
        vals.append(lhs)
    assert vals == [QI(F(-512, 1155)), QI(F(-1024, 3465))]
    return True


def check_continuum_carrier_boost_charge():
    """The continuum carrier of a generator half u > 0 (the modes beyond the edge): the one-particle boost
    generator h = kappa i(u d_u + 1/2) of the dilation psi(u) -> e^{kappa t/2} psi(e^{kappa t} u) acts on
    the Mellin mode u^{-1/2 + i w} as -kappa w, and its polarised form is the boost flux bilinear
    int kappa u (i/2)(conj(f) g' - conj(f') g) du for modes vanishing at the edge u = 0 and at u = 1, so
    that dGamma(h) = int chi^u T_uu du on that half: the window's boost Hamiltonian and the matter's boost
    charge are one operator. Exact integration over [0, 1] with Gaussian rationals."""
    premise("field-theory.second-quantisation")
    premise("hawking.i-state-continuum")
    premise("synthesis.imported-null-plane-modular-hamiltonian-first-law")
    from GA import QI
    I_ = QI(0, 1)
    for w in (F(1, 3), F(-2), F(5, 7)):
        a = QI(F(-1, 2), w)                                 # exponent of u^{-1/2 + i w}
        assert I_ * (a + QI(F(1, 2))) == QI(-w)             # i(u d_u + 1/2) u^a = i(a + 1/2) u^a

    def pm(p, q):
        out = [QI(0)] * (len(p) + len(q) - 1)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                out[i + j] = out[i + j] + x * y
        return out

    def pd(p):
        return [p[k] * QI(k) for k in range(1, len(p))] or [QI(0)]

    def pc(p):
        return [x.conj() for x in p]

    def padd2(p, q):
        m = max(len(p), len(q))
        return [(p[k] if k < len(p) else QI(0)) + (q[k] if k < len(q) else QI(0)) for k in range(m)]

    def integ01(p):
        return sum((x * QI(F(1, k + 1)) for k, x in enumerate(p)), QI(0))

    bump = [QI(0), QI(0), QI(1), QI(-2), QI(1)]            # u^2 (1 - u)^2
    u = [QI(0), QI(1)]
    modes = [pm([QI(1), QI(2, -1)], bump), pm([QI(0, 1), QI(0), QI(-3, 1)], bump), pm([QI(F(1, 2))], bump)]
    kappa = QI(F(1, 4))
    vals = {}
    for i, f in enumerate(modes):
        for j, g in enumerate(modes):
            flux = integ01(pm(u, [x * I_ * QI(F(1, 2)) for x in
                                  padd2(pm(pc(f), pd(g)), [-y for y in pm(pc(pd(f)), g)])])) * kappa
            hg = [x * I_ * kappa for x in padd2(pm(u, pd(g)), [y * QI(F(1, 2)) for y in g])]
            assert flux == integ01(pm(pc(f), hg))         # <f, h g> = boost flux bilinear
            vals[(i, j)] = flux
    for i in range(3):
        for j in range(3):
            assert vals[(i, j)] == vals[(j, i)].conj()      # Hermitian: dGamma(h) is self-adjoint
    assert (vals[(0, 0)], vals[(0, 1)], vals[(1, 1)]) == (QI(F(1, 5040)), QI(F(3, 24640), F(-1, 2240)), QI(F(-1, 1540)))
    assert vals[(0, 1)] != QI(0) and vals[(0, 0)] != QI(0) and vals[(2, 2)] == QI(0)   # a real mode carries none
    # the modular Hamiltonian beta dGamma(h) is the Fact's 2 pi K(0) on the generator, for every kappa:
    # beta = 2 pi / kappa and the flux carries one factor kappa, so beta * flux(kappa) = 2 pi * flux(1);
    # 2 pi is carried as a formal rational stand-in (the identity is linear in it)
    two_pi = QI(F(13, 2))
    f, g = modes[0], modes[1]

    def flux_at(k):
        return integ01(pm(u, [x * I_ * QI(F(1, 2)) for x in
                              padd2(pm(pc(f), pd(g)), [-y for y in pm(pc(pd(f)), g)])])) * k
    ref = two_pi * flux_at(QI(1))
    for kq in (F(1, 4), F(2, 3), F(3)):
        k = QI(kq)
        beta = two_pi * QI(F(kq.denominator, kq.numerator))
        assert beta * flux_at(k) == ref
    assert ref == two_pi * QI(F(3, 24640), F(-1, 2240)) * QI(4)
    return True
