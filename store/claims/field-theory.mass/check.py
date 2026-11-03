"""field-theory.mass: exact checks in the spacetime algebra Cl(1,3) (blade engine, Fraction).

I4 = gamma_0123, I sigma_3 = gamma_2 gamma_1; chi_e(phi) = (phi - e I4 phi I sigma_3)/2 projects the
even subalgebra onto the chirality spaces chi_+- ; proj keeps the span{1, I4} part.
(1) B_N(psi, phi) = proj(psi~ phi N): among the 16 basis right factors N, exactly the four even ones
gamma_01, gamma_02, gamma_13, gamma_23 (those anticommuting with I sigma_3) give a nonzero pairing on
chi_+ (N = 1 gives zero). For each of the four: antisymmetric, I4-bilinear in both slots, Lorentz
invariant under three rotors (boost, rotation, boost), nondegenerate (its real part has rank 4 on the
real 4-dimensional chi_+, which is I4-stable of complex dimension 2, so B_N is a nonzero multiple of
the epsilon pairing), and of charge two: B(e^{theta I4} psi, e^{theta I4} phi) = e^{2 theta I4} B at
the rational point (cos, sin) = (3/5, 4/5), while opposite charges leave it invariant.
(2) Massive plane wave p = 5 gamma_0 + 3 gamma_1 (p^2 = m^2 = 16): the positive-energy amplitudes
p psi = m psi gamma_0 form a real 4-dimensional space. For each N and each amplitude, eta = psi_- N
lies in chi_+, the Dirac equation is the coupled pair p chi = m eta N^{-1} gamma_0, p eta = m chi
gamma_0 N, chi has charge +1 and eta charge -1 under the Dirac phase (right exp(theta I sigma_3)),
and the mass density proj(psi~ psi) equals 2 proj(chi~ psi_-) = 2 B_{N^{-1}}(chi, eta).
(3) The one-datum fact: the massive solution space is stable under right multiplication by
I sigma_3 (the massive law's complex structure) but left I4 maps it to the solutions of
p psi = -m psi gamma_0 (zero intersection): I4 is not the massive law's complex structure. The mass
term (right gamma_0) anticommutes with right I4 on even elements, so the common I4 phase is axial.
"""
from fractions import Fraction as F

import GA
from GA import mul, add, sub, neg, sc, gen, reverse, eq, is_zero, all_blades
from tp_premise import premise

S4 = (1, -1, -1, -1)
ALL4 = all_blades(4)
I4 = {(0, 1, 2, 3): F(1)}
IS3 = {(1, 2): F(-1)}
G0 = gen(0)
LOR = [((F(5, 4), F(3, 4)), (0, 1)), ((F(3, 5), F(4, 5)), (1, 2)), ((F(13, 5), F(12, 5)), (0, 3))]
P_VEC = (5, 3)
PH = (F(3, 5), F(4, 5))
# The four right factors N with a nonzero pairing on chi_+ (found exhaustively in the first check).
FOUR_N = [(0, 1), (0, 2), (1, 3), (2, 3)]


def blade(t):
    return {tuple(t): F(1)}


def scl(c, x):
    c = F(c)
    return {b: c * v for b, v in x.items()} if c != 0 else {}


EVEN = [blade(b) for b in ALL4 if len(b) % 2 == 0]


def chi(e, p):
    return scl(F(1, 2), sub(p, scl(e, mul(mul(I4, p, S4), IS3, S4))))


def proj(x):
    return {b: c for b, c in x.items() if b in ((), (0, 1, 2, 3))}


def vecmv(x):
    return [x.get(b, F(0)) for b in ALL4]


def basis_of(elems):
    out = []
    for c in elems:
        if c and GA.rank_of_vectors([vecmv(x) for x in out + [c]]) > len(out):
            out.append(c)
    return out


def BN(a, b, N):
    return proj(mul(mul(reverse(a), b, S4), N, S4))


def rotor(cs, b):
    return add(sc(cs[0]), scl(cs[1], blade(b)))


def massive_amplitudes(m, sign=1):
    """Even psi with p psi = sign m psi gamma_0 (p = 5 g0 + 3 g1), as a basis (kernel)."""
    p = add(scl(P_VEC[0], gen(0)), scl(P_VEC[1], gen(1)))
    imgs = [sub(mul(p, b, S4), scl(sign * m, mul(b, G0, S4))) for b in EVEN]
    allb = sorted({bb for im in imgs for bb in im})
    rows = [[im.get(bb, F(0)) for im in imgs] for bb in allb]
    return p, [add(*[scl(v[i], EVEN[i]) for i in range(len(EVEN)) if v[i] != 0]) for v in GA.field_kernel(rows)]


def check_pairing_on_one_chirality():
    Cp = basis_of([chi(1, b) for b in EVEN])
    assert len(Cp) == 4
    # I4-stable: complex dimension 2
    assert GA.rank_of_vectors([vecmv(x) for x in Cp + [mul(I4, z, S4) for z in Cp]]) == 4
    good = []
    for t in ALL4:
        N = blade(t)
        if any(BN(a, b, N) for a in Cp for b in Cp):
            good.append(t)
    assert good == [(0, 1), (0, 2), (1, 3), (2, 3)], good
    for t in good:
        N = blade(t)
        assert eq(mul(N, IS3, S4), neg(mul(IS3, N, S4)))
        for a in Cp:
            for b in Cp:
                Bab = BN(a, b, N)
                assert eq(Bab, neg(BN(b, a, N)))
                assert eq(BN(mul(I4, a, S4), b, N), mul(I4, Bab, S4))
                assert eq(BN(a, mul(I4, b, S4), N), mul(I4, Bab, S4))
                for cs, bl in LOR:
                    R = rotor(cs, bl)
                    assert eq(mul(R, reverse(R), S4), sc(1))
                    assert eq(BN(mul(R, a, S4), mul(R, b, S4), N), Bab)
        realM = [[BN(a, b, N).get((), F(0)) for b in Cp] for a in Cp]
        assert GA.rank_of_vectors(realM) == 4


def check_charge_two_under_common_phase():
    Cp = basis_of([chi(1, b) for b in EVEN])
    assert len(Cp) == 4                                         # chi_+ is real 4-dimensional
    ph = add(sc(PH[0]), scl(PH[1], I4))
    phc = add(sc(PH[0]), scl(-PH[1], I4))
    ph2 = mul(ph, ph, S4)
    assert eq(ph2, add(sc(F(-7, 25)), scl(F(24, 25), I4)))      # (3/5 + 4/5 I4)^2 = -7/25 + 24/25 I4
    for t in FOUR_N:
        N = blade(t)
        for a in Cp:
            for b in Cp:
                assert eq(BN(mul(ph, a, S4), mul(ph, b, S4), N), mul(ph2, BN(a, b, N), S4))
                assert eq(BN(mul(ph, a, S4), mul(phc, b, S4), N), BN(a, b, N))


def check_massive_plane_wave_couples_opposite_charges():
    m = F(4)
    p, psis = massive_amplitudes(m)
    assert eq(mul(p, p, S4), sc(16)) and len(psis) == 4
    phr = add(sc(PH[0]), scl(PH[1], IS3))
    ph = add(sc(PH[0]), scl(PH[1], I4))
    phc = add(sc(PH[0]), scl(-PH[1], I4))
    for t in ((0, 1), (0, 2), (1, 3), (2, 3)):
        N = blade(t)
        Ninv = scl(1 / mul(N, N, S4)[()], N)
        for ps in psis:
            chp, chm = chi(1, ps), chi(-1, ps)
            eta = mul(chm, N, S4)
            assert eq(chi(1, eta), eta) and not is_zero(chp) and not is_zero(eta)
            assert eq(mul(p, chp, S4), scl(m, mul(mul(eta, Ninv, S4), G0, S4)))
            assert eq(mul(p, eta, S4), scl(m, mul(mul(chp, G0, S4), N, S4)))
            psr = mul(ps, phr, S4)
            assert eq(chi(1, psr), mul(ph, chp, S4))
            assert eq(mul(chi(-1, psr), N, S4), mul(phc, eta, S4))
            lhs = proj(mul(reverse(ps), ps, S4))
            assert eq(lhs, scl(2, proj(mul(reverse(chp), chm, S4))))
            assert eq(proj(mul(reverse(chp), chm, S4)), BN(chp, eta, Ninv))
            assert lhs                                                   # a nonzero mass density


def check_pseudoscalar_is_not_the_massive_complex_structure():
    premise("field-theory.imported-one-datum-massive-law")
    m = F(4)
    p, plus = massive_amplitudes(m, 1)
    _, minus = massive_amplitudes(m, -1)
    assert len(plus) == 4 and len(minus) == 4
    vp = [vecmv(x) for x in plus]
    vm = [vecmv(x) for x in minus]
    assert GA.rank_of_vectors(vp + vm) == 8                              # zero intersection
    for ps in plus:
        assert GA.rank_of_vectors(vp + [vecmv(mul(ps, IS3, S4))]) == 4   # right I sigma_3 preserves
        assert GA.rank_of_vectors(vm + [vecmv(mul(I4, ps, S4))]) == 4    # left I4 lands in the -m space
    for ph in EVEN:
        assert eq(mul(mul(ph, I4, S4), G0, S4), neg(mul(mul(ph, G0, S4), I4, S4)))
