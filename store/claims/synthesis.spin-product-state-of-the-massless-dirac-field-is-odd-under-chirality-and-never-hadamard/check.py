"""Exact checks: the Dirac field's spin-product state (the Fewster-Lang weighted spin-product state) and the Hadamard deposit.

The state is selected by the spectral split of the weighted spacetime spin product <psi|phi>_F = int F psi-bar phi
against the flux (Hilbert) product on solutions: the one-particle projection is the positive spectral projection
of the operator A_F with (psi|A_F phi) = <psi|phi>_F.

(1) Spacetime algebra Cl(1,3): with the chirality psi -> psi s3 (s3 = g3 g0), the spin product <phi psi~>_0,4
    is odd, the Dirac current phi g0 psi~ is even, the mass term anticommutes, the spinor unit I s3 commutes;
    complete by bilinearity on all pairs of even basis blades.
(2) One momentum-helicity block (the stored two-level reduction): H = M s3 + k s1 in the Pauli algebra with
    i = I = s1 s2 s3; the spin-product density is dH/dM = s3; at M = 0 the chirality is s1, which commutes with H
    and anticommutes with s3.
(3) Massless block: U = exp(-I k s1 eta) gives U~ s3 U = cos(2k eta) s3 + sin(2k eta) s2, so every weighted sum
    A = sum_j w_j U_j~ s3 U_j has no s1 part: the spin-product state's Bloch vector is perpendicular to the
    conformal vacuum's (s1), |beta|^2 = 1/2; s1 A s1 = -A, so Q + s1 Q s1 = 1.
(4) Massive block, Pythagorean (k, M, omega): A.h^ = (M/omega) F^(0), |A|^2 = (M/omega)^2 F^(0)^2 +
    (k/omega)^2 |F^(2 omega)|^2 (the Fewster-Lang Xi^2), cos^2(2 theta) = (A.h^)^2/|A|^2.
(5) Sharp collar along omega T = (n + 1/2) pi: (1 - 2|beta|^2)^2 = M^2T^2 omega^2/(M^2T^2 omega^2 + k^2) -> 9/25
    at MT = 3/4, |beta|^2 -> 1/5; the softened bound |beta|^2 <= O^2/(4 D^2) (polynomial identity).
(6) Conformal weight: psi = a^(-3/2) chi, sqrt(-g) = a^4, so the weight on a Weyl-flat collar is F a.
"""
from fractions import Fraction as Fr
import GA
from tp_premise import premise

STA = (1, -1, -1, -1)
PAULI = (1, 1, 1)

PYTH = ((3, 4, 5), (4, 3, 5), (12, 5, 13), (5, 12, 13), (15, 8, 17), (8, 15, 17))
ANGLES = ((Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17)),
          (Fr(-7, 25), Fr(24, 25)), (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(20, 29), Fr(-21, 29)))
WEIGHT_SETS = (
    (Fr(1), Fr(2), Fr(3)),
    (Fr(1, 2), Fr(0), Fr(7, 3), Fr(5)),
    (Fr(2), Fr(2), Fr(2), Fr(2), Fr(2), Fr(2), Fr(2)),
    (Fr(3, 4), Fr(11, 6)),
)


def part(x, g):
    return {b: c for b, c in x.items() if len(b) == g}


def vec(x):
    """Components of the grade-1 part on e0, e1, e2 (Pauli algebra)."""
    return [x.get((i,), Fr(0)) for i in range(3)]


def pauli_vec(v):
    return GA.add(*[GA.scal(v[i], GA.gen(i)) for i in range(3)])


def dot3(u, v):
    return sum(a * b for a, b in zip(u, v))


def heis(U, X):
    """Heisenberg-picture operator U~ X U (reversion is the adjoint in the Pauli algebra with i = I)."""
    return GA.mul(GA.mul(GA.reverse(U), X, PAULI), U, PAULI)


def rotor(axis, c, s):
    """U = c - I axis s, a unit even element (c^2 + s^2 = 1, axis a unit vector)."""
    e = [GA.gen(i) for i in range(3)]
    I = GA.mul(GA.mul(e[0], e[1], PAULI), e[2], PAULI)
    return GA.sub(GA.sc(c), GA.scal(s, GA.mul(I, pauli_vec(axis), PAULI)))


def check_spin_product_is_odd_and_current_even_under_chirality():
    """Spinors acted on by left multiplication (the store's convention), unit i = right I4; the whole
    algebra Cl(1,3) is used as the module, so every identity holds on every left ideal closed under the maps.
    Chirality Gamma(psi) = I4 psi I4 (left I4 = the matrix g0 g1 g2 g3, right I4 = the unit): the matrix gamma5.
    Spin product s(psi, phi) = <e0 psi~ phi>_0 (the real part of psi-bar phi); flux h(psi, phi) = <e0 psi~ e0 phi>_0
    (the real part of psi-dagger phi). Complete on all 16 x 16 basis pairs, by bilinearity."""
    premise("synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field")
    g = [GA.gen(i) for i in range(4)]
    I4 = GA.mul(GA.mul(GA.mul(g[0], g[1], STA), g[2], STA), g[3], STA)
    assert GA.eq(GA.mul(I4, I4, STA), GA.sc(-1))

    def Gam(x):
        return GA.mul(GA.mul(I4, x, STA), I4, STA)

    def s_form(x, y):
        return GA.mul(GA.mul(g[0], GA.reverse(x), STA), y, STA).get((), Fr(0))

    def h_form(x, y):
        return GA.mul(GA.mul(GA.mul(g[0], GA.reverse(x), STA), g[0], STA), y, STA).get((), Fr(0))

    blades = [b for b in GA.all_blades(4)]
    assert len(blades) == 16
    for b in blades:
        x = {b: Fr(1)}
        assert GA.eq(Gam(Gam(x)), x)                              # involution
        assert GA.eq(Gam(x), GA.neg(GA.grade_inv(x)))             # Gamma = minus the grade involution
        assert h_form(x, x) == 1                                  # the flux form is positive on the basis
        assert GA.eq(Gam(GA.mul(x, I4, STA)), GA.mul(Gam(x), I4, STA))   # commutes with the unit
        for mu in range(4):
            # left vector action anticommutes with Gamma: the massless Dirac operator maps solutions to solutions
            assert GA.eq(Gam(GA.mul(g[mu], x, STA)), GA.neg(GA.mul(g[mu], Gam(x), STA)))
            for nu in range(mu + 1, 4):
                bv = GA.mul(g[mu], g[nu], STA)                   # connection terms commute with Gamma
                assert GA.eq(Gam(GA.mul(bv, x, STA)), GA.mul(bv, Gam(x), STA))
        for c in blades:
            y = {c: Fr(1)}
            assert s_form(Gam(x), Gam(y)) == -s_form(x, y)        # spin product odd
            assert h_form(Gam(x), Gam(y)) == h_form(x, y)         # current even
            assert h_form(x, y) == h_form(y, x)
            for mu in range(4):                                   # left vectors are s-symmetric (Dirac adjoint)
                gx = GA.mul(g[mu], x, STA)
                gy = GA.mul(g[mu], y, STA)
                assert s_form(gx, y) == s_form(x, gy)
    # the mass term (right unit times m against the left vector derivative) does not commute with Gamma:
    # Gamma(x I4) = Gamma(x) I4 while Gamma(g0 x) = -g0 Gamma(x), so D psi I4 = m psi is not Gamma-invariant
    x = {(): Fr(1)}
    assert not GA.eq(Gam(GA.mul(g[0], x, STA)), GA.mul(g[0], Gam(x), STA))
    return True


def check_block_density_and_block_chirality():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    e = [GA.gen(i) for i in range(3)]
    for (k, M, w) in PYTH:
        H = GA.add(GA.scal(M, e[2]), GA.scal(k, e[0]))
        assert GA.eq(GA.mul(H, H, PAULI), GA.sc(w * w))
        # dH/dM = s3: difference quotient exact (H linear in M)
        H2 = GA.add(GA.scal(M + 1, e[2]), GA.scal(k, e[0]))
        assert GA.eq(GA.sub(H2, H), e[2])
    # massless: chirality s1 commutes with H = k s1 and anticommutes with the density s3
    H0 = GA.scal(7, e[0])
    assert GA.commutes(e[0], H0, PAULI)
    assert GA.anticommutes(e[0], e[2], PAULI)
    # positive-frequency projector (1 + s1)/2 has eigenvalue +k: the conformal vacuum's Bloch vector is s1
    P = GA.scal(Fr(1, 2), GA.add(GA.sc(1), e[0]))
    assert GA.eq(GA.mul(H0, P, PAULI), GA.scal(7, P))
    assert GA.eq(GA.mul(P, P, PAULI), P)
    return True


def check_massless_spin_product_state_is_perpendicular_to_the_conformal_vacuum():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    premise("synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite")
    e = [GA.gen(i) for i in range(3)]
    x1 = [Fr(1), Fr(0), Fr(0)]
    rotated = []
    for (c, s) in ANGLES:
        assert c * c + s * s == 1
        U = rotor(x1, c, s)
        R = heis(U, e[2])
        # U~ s3 U = cos(2 theta) s3 + sin(2 theta) s2, no s1 part
        assert GA.eq(R, GA.add(GA.scal(c * c - s * s, e[2]), GA.scal(2 * c * s, e[1])))
        assert vec(R)[0] == 0
        rotated.append(R)
    nonzero = 0
    for ws in WEIGHT_SETS:
        A = GA.add(*[GA.scal(w, rotated[j % len(rotated)]) for j, w in enumerate(ws)])
        assert dot3(vec(A), x1) == 0              # A . h^ = 0 at M = 0
        assert GA.eq(GA.mul(e[0], GA.mul(A, e[0], PAULI), PAULI), GA.neg(A))   # s1 A s1 = -A
        n2 = dot3(vec(A), vec(A))
        assert GA.eq(GA.mul(A, A, PAULI), GA.sc(n2))
        if n2 != 0:
            nonzero += 1
            # unnormalised projector |A| + A: (|A| + A) + s1 (|A| + A) s1 = 2|A|, i.e. Q + s1 Q s1 = 1
            # (|A| enters linearly, so the identity is checked with a formal scalar t standing for |A|)
            for t in (Fr(1), Fr(5, 3)):
                Qt = GA.add(GA.sc(t), A)
                assert GA.eq(GA.add(Qt, GA.mul(e[0], GA.mul(Qt, e[0], PAULI), PAULI)), GA.sc(2 * t))
            # s = A/|A| has s.h^ = 0, so |beta|^2 = (1 - s.h^)/2 = 1/2, and the relative block energy
            # omega (1 - s.h^) = 2 omega |beta|^2 equals omega
            beta2 = (1 - dot3(vec(A), x1)) / 2
            assert beta2 == Fr(1, 2)
    assert nonzero == len(WEIGHT_SETS)
    # radiation-type collar: weights F(eta) a(eta) with a = eta are still weights (any real numbers work)
    etas = (Fr(1, 3), Fr(1), Fr(2))
    A = GA.add(*[GA.scal(eta, rotated[j]) for j, eta in enumerate(etas)])
    assert vec(A)[0] == 0
    return True


def check_massive_block_reproduces_the_fewster_lang_angle():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    premise("synthesis.imported-fewster-lang-spin-product-states-of-the-dirac-field")
    e = [GA.gen(i) for i in range(3)]
    for (k, M, w) in PYTH:
        hh = [Fr(k, w), Fr(0), Fr(M, w)]
        H = pauli_vec([Fr(k), Fr(0), Fr(M)])
        for ws in WEIGHT_SETS:
            A = {}
            F0 = Fr(0)
            Fc = Fr(0)
            Fs = Fr(0)
            for j, wt in enumerate(ws):
                c, s = ANGLES[j % len(ANGLES)]
                U = rotor(hh, c, s)
                # U = exp(-I h^ omega eta): it commutes with H
                assert GA.commutes(U, H, PAULI)
                A = GA.add(A, GA.scal(wt, heis(U, e[2])))
                F0 += wt
                Fc += wt * (c * c - s * s)
                Fs += wt * 2 * c * s
            a = vec(A)
            assert dot3(a, hh) == Fr(M, w) * F0
            Xi2 = Fr(M, w) ** 2 * F0 ** 2 + Fr(k, w) ** 2 * (Fc ** 2 + Fs ** 2)
            assert dot3(a, a) == Xi2
            assert GA.eq(GA.mul(A, A, PAULI), GA.sc(Xi2))
            if Xi2 != 0:
                cos2 = dot3(a, hh) ** 2 / Xi2
                assert cos2 == F0 ** 2 * M * M / (w * w * Xi2)
                assert 0 <= cos2 <= 1
    return True


def check_sharp_collar_does_not_decay_and_the_softened_bound():
    premise("synthesis.imported-microlocal-hadamard-condition")
    MT = Fr(3, 4)
    M = Fr(2)
    lim = MT * MT / (MT * MT + 1)
    assert lim == Fr(9, 25)
    # |beta|^2 = (1 - sqrt(lim))/2 = (1 - 3/5)/2 = 1/5 in the limit
    assert Fr(3, 5) ** 2 == lim and (1 - Fr(3, 5)) / 2 == Fr(1, 5)
    prev = None
    for kk in (Fr(1), Fr(10), Fr(100), Fr(1000), Fr(10 ** 6)):
        w2 = kk * kk + M * M
        r = MT * MT * w2 / (MT * MT * w2 + kk * kk)      # (1 - 2|beta|^2)^2 along omega T = (n + 1/2) pi
        assert lim <= r < 1
        if prev is not None:
            assert r < prev                              # decreasing to 9/25: |beta|^2 increases to 1/5
        prev = r
        if kk >= 3 * M:
            assert r <= Fr(1, 2)                         # so |beta|^2 >= (1 - 2^(-1/2))/2 > 0
    # softened bound: (1 + x)(1 - x/2)^2 = 1 - 3x^2/4 + x^3/4, so 1 - 1/sqrt(1+x) <= x/2 on [0, 3]
    lhs = GA.pmul(GA.pmul([Fr(1), Fr(1)], [Fr(1), Fr(-1, 2)]), [Fr(1), Fr(-1, 2)])
    assert GA.ptrim(lhs) == [Fr(1), Fr(0), Fr(-3, 4), Fr(1, 4)]
    for x in (Fr(0), Fr(1, 100), Fr(1, 2), Fr(1), Fr(2), Fr(3)):
        assert GA.peval(lhs, x) <= 1
    return True


def check_conformal_weight_of_the_spin_product():
    premise("synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite")
    # psi = a^(-3/2) chi on both factors, volume a^4: exponent -3/2 - 3/2 + 4 = 1
    assert Fr(-3, 2) + Fr(-3, 2) + 4 == 1
    # the current psi-dagger psi with the spatial volume a^3: -3 + 3 = 0, so the flux product is the flat one
    assert Fr(-3, 2) * 2 + 3 == 0
    return True


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("check_"):
            print(name, fn())
