"""Exact checks: local gauge transforms of the null vacuum share its modular data, not its ground state.

Generator CAR algebra over L^2(R, du) (x) K, null vacuum omega0 with symbol chi(P < 0), P = i d/du.
(1) The modular conjugation of a pure gauge-invariant quasi-free (Slater) state for the CAR algebra of a block of
    modes is the second quantisation of the polar part W of the off-diagonal block X = P_comp E P_block:
    J a(f) J = sigma Gamma a*(W f), Gamma the total parity, sigma = (-1)^(number of block modes). Checked on 1 + 1
    and 2 + 2 modes with exact Gaussian-rational data: the candidate J_c is an antiunitary involution fixing Omega,
    J_c S is Hermitian with positive leading minors (so J_c S = Delta^(1/2) and J_c = J by uniqueness of the
    polar decomposition), and J_c a J_c equals the stated operator.
(2) Fermi seas: alpha_k(a(f)) = a(e^{iku} f) carries chi(P < 0) to chi(P < k) (plane-wave bookkeeping); the
    reflection about a picks up the phase e^{2ik(a - u)}, constant in u only for k = 0; excitations of chi(P < k)
    above the sea: charge-zero pairs have positive energy, single holes at 0 < p < k negative energy;
    densities k/(2 pi) and k^2/(4 pi) as exact antiderivatives.
(3) Hankel phases: the reflected off-diagonal kernel h(t) = (1/(2 pi)) int_S e^{ipt} dp is -i/(2 pi t) for the
    vacuum (S = (-oo, 0)) and +i/(2 pi t) for the filled sea (S = (0, oo)); c = -i, +i make c-bar h = 1/(2 pi t).
    For the odd set S = (-oo, -1) u (0, 1), h(t) = i (1 - 2 cos t)/(2 pi t) changes sign on the diagonal
    (Taylor bounds at t = 1/10 and t = 2), so no constant phase makes the Hankel form positive.
(4) Geometric algebra Cl(1,3): I_4 B = J for B = g0 g3, J = g1 g2; J^2 = -1, J commutes with B; the transverse
    rotor 3/5 + (4/5) J fixes n = g0 + g3 and B (the lift datum is invisible to the boost and null direction);
    the transverse reflection fixes B and n and reverses J and I_4 (the sign datum).
"""
from fractions import Fraction as F
import GA
import fock
from tp_premise import premise

QI = GA.QI
I = GA.QI_I
ZERO = QI(0)
ONE = QI(1)


def q(x):
    return x if isinstance(x, QI) else QI(x)


def cj(x):
    return q(x).conj()


def dense(op, d):
    M = [[ZERO for _ in range(d)] for _ in range(d)]
    for (r, c), v in op.items():
        M[r][c] = q(v)
    return M


def mmul(A, B):
    return GA.field_mat_mul(A, B)


def madd(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def msc(c, A):
    return [[q(c) * a for a in r] for r in A]


def mconj(A):
    return [[cj(a) for a in r] for r in A]


def mdag(A):
    return [[cj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def meq(A, B):
    return all(a == b for ra, rb in zip(A, B) for a, b in zip(ra, rb))


def eye(d):
    return [[ONE if i == j else ZERO for j in range(d)] for i in range(d)]


def inverse(M):
    n = len(M)
    cols = [GA.field_solve(M, [ONE if i == j else ZERO for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def det(M):
    A = [list(r) for r in M]
    n, d = len(A), ONE
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != ZERO), None)
        if p is None:
            return ZERO
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d = d * A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != ZERO:
                f = A[r][c] / A[c][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return d


def apply(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v))), ZERO) for i in range(len(A))]


def slater(orbitals, m):
    """Omega = a*(phi_1) ... a*(phi_r) |0>, orbitals given as lists of mode coefficients."""
    d = 2 ** m
    vec = [ONE] + [ZERO] * (d - 1)
    for phi in reversed(orbitals):
        A = [[ZERO] * d for _ in range(d)]
        for k, c in enumerate(phi):
            A = madd(A, msc(c, dense(fock.cre(k, m), d)))
        vec = apply(A, vec)
    return vec


def modular_conjugation_case(orbitals, block, comp, W):
    """Exact test of J a(e_j) J = sigma Gamma a*(W e_j) for the CAR algebra of the block modes."""
    m = len(block) + len(comp)
    d = 2 ** m
    a = [dense(fock.ann(k, m), d) for k in range(m)]
    ad = [mdag(x) for x in a]
    Om = slater(orbitals, m)
    nrm = sum((cj(x) * x for x in Om), ZERO)
    assert nrm == ONE
    # two-point function <a_j* a_l> = E_lj with E = sum |phi><phi|
    for j in range(m):
        for l in range(m):
            lhs = sum((cj(x) * y for x, y in zip(Om, apply(mmul(ad[j], a[l]), Om))), ZERO)
            E_lj = sum((phi[l] * cj(phi[j]) for phi in orbitals), ZERO)
            assert lhs == E_lj
    # cyclic basis: monomials in the block modes, each factor one of 1, a, a*, a* a
    per = [[eye(d), a[k], ad[k], mmul(ad[k], a[k])] for k in block]
    mons = [eye(d)]
    for opts in per:
        mons = [mmul(x, o) for x in mons for o in opts]
    Gam = dense(fock.parity(m), d)
    sigma = F(-1) ** len(block)

    def ad_of(vec):  # a*(sum_l vec_l e_comp[l])
        A = [[ZERO] * d for _ in range(d)]
        for l, c in enumerate(vec):
            A = madd(A, msc(c, ad[comp[l]]))
        return A

    phi_a = [msc(sigma, mmul(Gam, ad_of([W[l][j] for l in range(len(comp))]))) for j in range(len(block))]
    phi_ad = [mdag(x) for x in phi_a]
    phis = [[eye(d), phi_a[j], phi_ad[j], mmul(phi_ad[j], phi_a[j])] for j in range(len(block))]
    images = [eye(d)]
    for opts in phis:
        images = [mmul(x, o) for x in images for o in opts]
    V = [[x[i] for x in [apply(mn, Om) for mn in mons]] for i in range(d)]
    Y = [[x[i] for x in [apply(mdag(mn), Om) for mn in mons]] for i in range(d)]
    Phi = [[x[i] for x in [apply(im, Om) for im in images]] for i in range(d)]
    Vinv = inverse(V)
    A_S = mmul(Y, mconj(Vinv))          # S = A_S K
    A_J = mmul(Phi, mconj(Vinv))        # J_c = A_J K
    assert meq(mmul(mdag(A_J), A_J), eye(d))          # antiunitary
    assert meq(mmul(A_J, mconj(A_J)), eye(d))         # involution
    assert apply(A_J, [cj(x) for x in Om]) == Om       # J_c Omega = Omega
    D = mmul(A_J, mconj(A_S))                          # J_c S, linear
    assert meq(D, mdag(D))                             # Hermitian
    for k in range(1, d + 1):                          # Sylvester: positive definite
        mk = det([r[:k] for r in D[:k]])
        assert mk.im == 0 and mk.re > 0
    for j, k in enumerate(block):                      # J_c a J_c = sigma Gamma a*(W e)
        assert meq(mmul(mmul(A_J, mconj(a[k])), mconj(A_J)), phi_a[j])
    return True


def check_polar_part_gives_the_modular_conjugation():
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    premise("synthesis.imported-powers-stormer-takesaki-disjointness")
    # 1 + 1 modes: phi = (3/5) e0 + (4i/5) e1; X = E_10 = 12i/25, polar part W = i
    c, s = QI(F(3, 5)), QI(0, F(4, 5))
    assert modular_conjugation_case([[c, s]], [0], [1], [[-I]])
    # 2 + 2 modes, block = modes 0, 1, complement = modes 2, 3; rotated Schmidt pairs
    r_a, r_b = [QI(F(3, 5)), QI(F(4, 5))], [QI(F(-4, 5)), QI(F(3, 5))]   # orthonormal in the block
    l_a, l_b = [ZERO, I], [ONE, ZERO]                                    # orthonormal in the complement
    (ca, sa), (cb, sb) = (QI(F(3, 5)), QI(0, F(4, 5))), (QI(F(5, 13)), QI(F(12, 13)))
    phi1 = [ca * r_a[0], ca * r_a[1], sa * l_a[0], sa * l_a[1]]
    phi2 = [cb * r_b[0], cb * r_b[1], sb * l_b[0], sb * l_b[1]]
    # W = (sa/|sa|)(ca/|ca|)^-  |l_a><r_a| + (sb/|sb|) |l_b><r_b| = i |l_a><r_a| + |l_b><r_b|
    W = [[I * l_a[i] * cj(r_a[j]) + ONE * l_b[i] * cj(r_b[j]) for j in range(2)] for i in range(2)]
    # sanity: W is the polar part of X = sum s c-bar |l><r|: X = W |X| with |X| >= 0 diagonal in r_a, r_b
    X = [[sa * cj(ca) * l_a[i] * cj(r_a[j]) + sb * cj(cb) * l_b[i] * cj(r_b[j]) for j in range(2)] for i in range(2)]
    absX = [[QI(F(12, 25)) * r_a[i] * cj(r_a[j]) + QI(F(60, 169)) * r_b[i] * cj(r_b[j]) for j in range(2)]
            for i in range(2)]
    assert meq(mmul(W, absX), X)
    assert modular_conjugation_case([phi1, phi2], [0, 1], [2, 3], W)
    return True


def check_fermi_sea_is_a_local_gauge_transform_of_the_vacuum():
    premise("synthesis.positive-null-energy-gives-r-premises")
    # plane wave e^{-ipu} has P-eigenvalue p; multiplication by e^{iku} sends p to p - k
    ks = (F(3, 2), F(-2, 7), F(0))
    ps = (F(-5), F(-1, 3), F(0), F(1, 4), F(1), F(13, 9), F(4))
    for k in ks:
        for p in ps:
            # symbol of omega0 o alpha_k: conj(m) chi(P < 0) m on e^{-ipu}: m shifts to p - k
            assert ((p - k) < 0) == (p < k)
    # field-level reflection phase: conj(m(u)) m(2a - u) = e^{i k (2a - u - u)} = e^{2ik(a - u)}
    for k in ks:
        for a in (F(0), F(5, 3)):
            exps = [-k * u + k * (2 * a - u) for u in (F(-2), F(1, 2), F(7))]
            assert all(e == 2 * k * (a - u) for e, u in zip(exps, (F(-2), F(1, 2), F(7))))
            assert (len(set(exps)) == 1) == (k == 0)        # constant phase only for k = 0
    # excitations of chi(P < k), k > 0: particle at p > k has energy p, hole at p < k energy -p
    k = F(3, 2)
    holes = [F(1, 4), F(1), F(-2)]
    parts = [F(2), F(5, 2), F(31, 20)]
    assert all(pp - ph > 0 for pp in parts for ph in holes)      # charge-zero pairs: positive
    assert -holes[0] < 0 and -holes[1] < 0                     # single holes in (0, k): negative
    assert -k * 7 < -holes[1] * 7 < 0                           # seven holes: energy unbounded below with number
    # k = 0: every excitation energy is nonnegative (particles p > 0, holes p < 0)
    assert all(p > 0 for p in parts) and all(-p > 0 for p in (F(-1, 3), F(-5)))
    # densities: int_0^k dp = k, int_0^k p dp = k^2/2, so k/(2 pi) and k^2/(4 pi)
    prim1 = lambda x: x
    prim2 = lambda x: x * x / 2
    assert prim1(k) - prim1(F(0)) == k and prim2(k) - prim2(F(0)) == F(9, 8)
    # zero net charge with K = C^2, k = diag(kappa, -kappa): charges cancel, energies add
    kap = F(5, 4)
    assert prim1(kap) + prim1(-kap) == 0 and prim2(kap) + prim2(-kap) == F(25, 16)
    return True


def cos_lower(t):
    """cos t >= 1 - t^2/2 for all real t."""
    return 1 - t * t / 2


def cos_upper(t):
    """cos t <= 1 - t^2/2 + t^4/24 for all real t."""
    return 1 - t * t / 2 + t ** 4 / 24


def check_hankel_phases_of_the_vacuum_and_the_filled_sea():
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("angle.imported-theorems-deliver-their-hypotheses")
    # int_{-oo}^0 e^{ipt} dp = 1/(it) = -i/t ; int_0^oo e^{ipt} dp = -1/(it) = i/t (Abel regularised)
    for t in (F(1, 3), F(2), F(17, 5)):
        h_vac = ONE / (I * QI(t))               # times 1/(2 pi)
        h_sea = -ONE / (I * QI(t))
        assert h_vac == QI(0, -1 / t) and h_sea == QI(0, 1 / t)
        c_vac, c_sea = QI(0, -1), QI(0, 1)
        assert cj(c_vac) * h_vac == QI(1 / t) and cj(c_sea) * h_sea == QI(1 / t)
        assert c_sea == cj(c_vac)
        # the other phase fails: c_sea-bar h_vac = -1/t < 0
        assert (cj(c_sea) * h_vac).re < 0
    # odd set S = (-oo, -1) u (0, 1): h(t) = (1/(2 pi)) [e^{-it}/(it) + (e^{it} - 1)/(it)] = i (1 - 2 cos t)/(2 pi t)
    # c-bar h real needs c = +-i; the factor (1 - 2 cos t)/t changes sign on the diagonal t = 2x:
    t1, t2 = F(1, 10), F(2)
    up1 = (1 - 2 * cos_lower(t1)) / t1          # upper bound at t1
    lo2 = (1 - 2 * cos_upper(t2)) / t2          # lower bound at t2
    assert up1 < 0 and lo2 > 0
    assert up1 == F(-99, 10) and lo2 == F(5, 6)
    return True


def check_lift_and_sign_data_in_geometric_algebra():
    premise("synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics")
    sq = GA.sig(1, 3)
    g = [GA.gen(i) for i in range(4)]

    def m(*xs):
        out = xs[0]
        for x in xs[1:]:
            out = GA.mul(out, x, sq)
        return out

    I4, B, J = m(g[0], g[1], g[2], g[3]), m(g[0], g[3]), m(g[1], g[2])
    n = GA.add(g[0], g[3])
    assert GA.eq(m(I4, B), J)                          # lead 2: I_4 B = J
    assert GA.eq(m(J, J), GA.sc(-1)) and GA.eq(m(B, B), GA.sc(1))
    assert GA.commutes(J, B, sq)
    R = GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), J))    # transverse rotor
    Rr = GA.reverse(R)
    assert GA.eq(m(R, Rr), GA.sc(1))
    assert GA.eq(m(R, n, Rr), n) and GA.eq(m(R, B, Rr), B)
    assert not GA.eq(m(R, g[1], Rr), g[1])            # it does rotate the transverse frame
    g1inv = GA.scal(-1, g[1])                          # g1^2 = -1
    refl_v = lambda v: GA.neg(m(g[1], v, g1inv))       # x1 -> -x1 on vectors
    refl_b = lambda X: m(g[1], X, g1inv)               # on even elements
    assert GA.eq(refl_v(n), n) and GA.eq(refl_b(B), B)
    assert GA.eq(refl_b(J), GA.neg(J)) and GA.eq(refl_b(I4), GA.neg(I4))
    # reflections about two cuts compose to a translation: r_a r_b (u) = u + 2(a - b)
    for a, b in ((F(0), F(1)), (F(-3, 2), F(2, 7))):
        for u in (F(5), F(-1, 3)):
            assert (2 * a - (2 * b - u)) == u + 2 * (a - b)
    # the collapse state's reflections are inversions V -> a^2/V, composing to dilations
    for a, b in ((F(2), F(3)), (F(1, 2), F(5))):
        for V in (F(7), F(1, 9)):
            assert a * a / (b * b / V) == (a * a / (b * b)) * V
    return True
