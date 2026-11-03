"""synthesis.incidence-vacua-thermofield-real-capacity: exact checks in Gaussian-rational arithmetic.

Cl(2,4) on the 8-dim Fock module (Jordan-Wigner, three qubits). e1 (+), e2, e3, e4 (-), ep (+), em (-);
positive generators Hermitian, negative ones anti-Hermitian (g* = g^{-1}). a = n0, a* = ninf/2;
b = (e1+e2)/2, b* = (e1-e2)/2. At x = t e1 + r e2, u = t - r, v = t + r, X = n0 + x - (Q/2) ninf.
check_real_states_read_real_capacity tests (i) and (v) on Cl(2,4) for four sample real states (the
general p, q statement enters only through the integer criterion floor((p+q)/2) <= min(p,q) iff
|p - q| <= 1, enumerated for p + q <= 6); check_incidence_lines_thermofield tests (ii) to (iv) at
eight points.
"""
import GA
from tp_premise import premise

from fractions import Fraction as F
from itertools import combinations
from GA import QI, field_kernel, field_rank
import fock

Z0, ONE, I = QI(0), QI(1), QI(0, 1)


mm = GA.field_mat_mul


def madd(*Ms):
    return [[sum((M[i][j] for M in Ms), QI(0)) for j in range(len(Ms[0][0]))] for i in range(len(Ms[0]))]


def msc(c, A):
    c = c if isinstance(c, QI) else QI(c)
    return [[c * x for x in r] for r in A]


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def eye(n):
    return [[ONE if i == j else Z0 for j in range(n)] for i in range(n)]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def mv(A, v):
    return [sum((A[i][k] * v[k] for k in range(len(v))), QI(0)) for i in range(len(A))]


def ip(v, w):
    return sum((v[i].conj() * w[i] for i in range(len(v))), QI(0))


# Hermitian Majoranas of three Jordan-Wigner modes (mode 0 the leading tensor factor): the Pauli strings
# sx(x)1(x)1, sy(x)1(x)1, sz(x)sx(x)1, sz(x)sy(x)1, sz(x)sz(x)sx, sz(x)sz(x)sy
G = [[[QI(x) for x in r] for r in fock.to_dense(fock.majorana(p, 3, fock.MSB, kind="herm"), 8)] for p in range(6)]
mI = QI(0, -1)
e1, ep = G[0], G[1]
e2, e3, e4, em = msc(mI, G[2]), msc(mI, G[3]), msc(mI, G[4]), msc(mI, G[5])
GENS = [(e1, 1), (e2, -1), (e3, -1), (e4, -1), (ep, 1), (em, -1)]
E8 = eye(8)


def setup_checks():
    ok = True
    for i, (g, s) in enumerate(GENS):
        ok &= meq(mm(g, g), msc(s, E8))
        ok &= meq(dag(g), msc(s, g))            # g* = g^{-1} = s g
        for j, (h, _) in enumerate(GENS):
            if i < j:
                ok &= meq(madd(mm(g, h), mm(h, g)), [[Z0] * 8 for _ in range(8)])
    return ok


half = F(1, 2)
n0 = msc(half, madd(ep, em)); ninf = madd(ep, msc(-1, em))
a = n0; ad = msc(half, ninf)
b = msc(half, madd(e1, e2)); bd = msc(half, madd(e1, msc(-1, e2)))
N = mm(ad, a)
# chirality: product of the six Hermitian Majoranas times i^3 = -i; diagonal in this basis
chi = msc(QI(0, -1), mm(mm(mm(G[0], G[1]), mm(G[2], G[3])), mm(G[4], G[5])))


def car_checks():
    ok = meq(dag(a), ad) and meq(dag(b), bd)
    ok &= meq(madd(mm(a, ad), mm(ad, a)), E8) and meq(madd(mm(b, bd), mm(bd, b)), E8)
    ok &= meq(madd(mm(a, b), mm(b, a)), [[Z0] * 8 for _ in range(8)])
    ok &= meq(madd(mm(a, bd), mm(bd, a)), [[Z0] * 8 for _ in range(8)])
    ok &= meq(mm(chi, chi), E8) and all(chi[i][j] == Z0 for i in range(8) for j in range(8) if i != j)
    return ok


def vacua():
    """common kernel of a and b, split by chirality: one vacuum in each half"""
    M = a + b                                   # stacked rows: 16 x 8
    K = field_kernel(M)
    assert len(K) == 2
    out = {}
    for s in (1, -1):
        P = [[(E8[i][j] + (chi[i][j] if s == 1 else -chi[i][j])) * QI(half) for j in range(8)] for i in range(8)]
        vs = [mv(P, k) for k in K]
        vs = [w for w in vs if any(x != Z0 for x in w)]
        out[s] = vs[0]
    return out


def chir_of(v):
    w = mv(chi, v)
    if all(w[i] == v[i] for i in range(8)):
        return 1
    if all(w[i] == -v[i] for i in range(8)):
        return -1
    return 0


def expect(A, v):
    return ip(v, mv(A, v)) / ip(v, v)


def real_blades():
    gens = [e1, e2, ep, em]
    out = []
    for k in range(5):
        for c in combinations(range(4), k):
            M = E8
            for i in c:
                M = mm(M, gens[i])
            out.append((c, M))
    return out


def run_point(t, r, vac, blades):
    u, v = t - r, t + r
    Q = u * v
    X = madd(n0, msc(t, e1), msc(r, e2), msc(-Q * half, ninf))
    assert meq(mm(X, X), [[Z0] * 8 for _ in range(8)])          # X(x) null
    s0 = chir_of(vac[1])
    Om = madd(E8, msc(-u, mm(ad, bd)))
    Om = mv(Om, vac[1])
    Ps = mv(madd(bd, msc(-v, ad)), vac[-1])
    assert chir_of(Om) == chir_of(Ps) == s0 != 0                 # same half
    assert all(x == Z0 for x in mv(X, Om)) and all(x == Z0 for x in mv(X, Ps))
    # kernel of X on that half has dimension exactly two, spanned by Om, Ps
    P = [[(E8[i][j] + s0 * chi[i][j]) * QI(half) for j in range(8)] for i in range(8)]
    XP = mm(X, P)
    assert 8 - field_rank(XP) - 4 == 2                           # kernel of X on C^8 restricted to the half
    assert field_rank([Om, Ps]) == 2
    nO, nP = expect(N, Om), expect(N, Ps)
    assert nO == QI(F(u * u, 1 + u * u)) and nP == QI(F(v * v, 1 + v * v))
    assert ip(Om, Ps) == Z0 and ip(Om, mv(N, Ps)) == Z0          # N block-diagonal: range is the segment
    assert expect(a, Om) == Z0 and expect(a, Ps) == Z0           # marginal diagonal
    for st in (Om, Ps):
        for c, M in blades:
            assert expect(M, st).im == 0                         # real on Cl(2,2) of e1,e2,ep,em
        w = expect(mm(e3, e4), st)
        assert w.re == 0 and abs(w.im) == 1                      # spectator: +-i on e3 e4
    return nO, nP




def ab_purity(state):
    """purity tr(rho^2) of the (a,b) state, from the 16 monomials of the Hermitian Majoranas
    e1, i e2, ep, i em: tr(rho^2) = (1/4) sum_S |<gamma_S>|^2"""
    if not _AB_MONOS:                           # the 16 monomials are state-independent: build once
        maj = [e1, msc(I, e2), ep, msc(I, em)]
        for k in range(5):
            for S in combinations(range(4), k):
                M = E8
                for i in S:
                    M = mm(M, maj[i])
                _AB_MONOS.append(M)
    tot = F(0)
    for M in _AB_MONOS:
        z = expect(M, state)
        tot += z.re * z.re + z.im * z.im
    return tot / 4


_AB_MONOS = []


def purity_checks(t, r, vac):
    u, v = t - r, t + r
    Om = mv(madd(E8, msc(-u, mm(ad, bd))), vac[1])
    Ps = mv(madd(bd, msc(-v, ad)), vac[-1])
    assert ab_purity(Om) == 1 and ab_purity(Ps) == 1            # spanning vacua: (a,b) pure
    phi = [Om[i] + Ps[i] for i in range(8)]                    # a generic vacuum on L_x
    w1, w2 = 1 + u * u, 1 + v * v
    pur = ab_purity(phi)
    assert pur == (w1 * w1 + w2 * w2) / ((w1 + w2) * (w1 + w2)) and pur < 1   # mixed: spectator entangled
    return pur


def all_real_blades():
    """the 64 basis blades of Cl(2,4) (ordered products of the six real generators) as matrices"""
    out = []
    for k in range(7):
        for c in combinations(range(6), k):
            M = E8
            for i in c:
                M = mm(M, GENS[i][0])
            out.append(M)
    return out


def omega(rho, y):
    """omega(y) = tr(rho y)"""
    return sum((rho[i][j] * y[j][i] for i in range(8) for j in range(8)), QI(0))


def null_space_of_state(rho):
    """basis of {y in V_C : omega(y* y) = 0}, y = sum_i y_i g_i (the Hermitian form is positive)"""
    M = [[omega(rho, mm(dag(GENS[i][0]), GENS[j][0])) for j in range(6)] for i in range(6)]
    return field_kernel(M)


def sample_real_states():
    """four real density matrices: the trace; the projector onto ker a cap ker b (both chiralities),
    the vacuum of the two real null modes a, b; the projector onto ker a; and (1 + e1 e2/3 + ep/2)/8,
    where e1 e2 and ep are commuting self-adjoint involutions (eigenvalues 1 +- 1/3 +- 1/2 >= 0)"""
    Na, Nb = mm(ad, a), mm(bd, b)
    e12 = mm(e1, e2)
    return [msc(F(1, 8), E8),
            msc(half, mm(madd(E8, msc(-1, Na)), madd(E8, msc(-1, Nb)))),
            msc(F(1, 4), madd(E8, msc(-1, Na))),
            msc(F(1, 8), madd(E8, msc(F(1, 3), e12), msc(half, ep)))]


def check_real_states_read_real_capacity():
    premise("tower.witt-index-quantum-capacity")
    premise("one-relation.two-capacities-three-consequences")
    assert setup_checks() and car_checks()
    # orthogonal generators of equal square: gh is skew-adjoint; the mode (g + i h)/2 has c*c = (1 + i s gh)/2
    modes = []
    for i, (g, s) in enumerate(GENS):
        for j, (h, s2) in enumerate(GENS):
            if i < j and s == s2:
                gh = mm(g, h)
                assert meq(dag(gh), msc(-1, gh))
                c = msc(half, madd(g, msc(I, h)))
                assert meq(mm(c, c), [[Z0] * 8 for _ in range(8)])
                assert meq(madd(mm(c, dag(c)), mm(dag(c), c)), E8)
                assert meq(mm(dag(c), c), msc(half, madd(E8, msc(QI(0, s), gh))))
                modes.append((gh, mm(dag(c), c)))
            if i < j and s != s2:
                gh = mm(g, h)
                assert meq(dag(gh), gh)                         # a hyperbolic plane's bivector is self-adjoint
    assert len(modes) == 7                                      # C(2,2) + C(4,2) definite pairs
    # e1 e2 and ep: the commuting self-adjoint involutions of the fourth sample state
    e12 = mm(e1, e2)
    assert meq(mm(e12, e12), E8) and meq(dag(e12), e12) and meq(mm(e12, ep), mm(ep, e12))
    blades = all_real_blades()
    assert len(blades) == 64
    dims = []
    for rho in sample_real_states():
        assert meq(dag(rho), rho) and sum((rho[i][i] for i in range(8)), QI(0)) == ONE
        assert all(omega(rho, B).im == 0 for B in blades)       # rho is a real state
        for gh, occ in modes:
            assert omega(rho, gh) == Z0 and omega(rho, occ) == QI(half)   # occupation exactly 1/2
        K = null_space_of_state(rho)
        Kc = [[x.conj() for x in k] for k in K]
        if K:
            assert field_rank(K + Kc) == len(K)                  # complexification of a real subspace
        for k1 in K:
            for k2 in K:                                         # totally isotropic for Q
                assert sum((GENS[i][1] * k1[i] * k2[i] for i in range(6)), QI(0)) == Z0
        dims.append(len(K))
    assert dims == [0, 2, 1, 0] and max(dims) <= min(2, 4)
    # contrast: the chiral vacuum |0>_+ is pure on three modes (null space dimension 3 > min(2, 4))
    # and is not real (e3 e4 has value +-i)
    v = vacua()[1]
    rho_v = [[v[i] * v[j].conj() / ip(v, v) for j in range(8)] for i in range(8)]
    assert len(null_space_of_state(rho_v)) == 3
    assert any(omega(rho_v, B).im != 0 for B in blades)
    # the conclusion: a maximal isotropic subspace of V_C (dimension floor((p+q)/2)) can be the null
    # space of a real state only if floor((p+q)/2) <= min(p, q), i.e. |p - q| <= 1
    for n in range(1, 7):
        for p in range(n + 1):
            q = n - p
            assert ((n // 2) <= min(p, q)) == (abs(p - q) <= 1)
    GA.check("real states on Cl(2,4) (four samples): real on all 64 blades, omega(gh) = 0 and occupation 1/2 "
             "on the seven definite-plane modes, null space the complexification of a real totally isotropic "
             "subspace of dimension 0, 2, 1, 0 <= min(2,4); the chiral vacuum has null space 3 and is not real; "
             "floor((p+q)/2) <= min(p,q) iff |p - q| <= 1 for p + q <= 6; hyperbolic-plane bivectors self-adjoint",
             True)


def check_incidence_lines_thermofield():
    premise("one-relation.imported-pure-spinors-incidence-chart")
    premise("one-relation.spacetime-manifold-vacuum-lines")
    premise("singularity.descended-form-state-independent")
    premise("state-selection.partner-purification-are-canonical")
    assert setup_checks() and car_checks()
    vac = vacua()
    bl = real_blades()
    # (t, r) and the pinned exact values <N> on Omega_x, <N> on Psi_x, and the (a,b) purity of
    # Omega_x + Psi_x, so that a perturbed point or value cannot pass silently
    pts = [((F(0), F(0)), F(0), F(0), F(1, 2)),
           ((F(1), F(0)), F(1, 2), F(1, 2), F(1, 2)),
           ((F(0), F(1)), F(1, 2), F(1, 2), F(1, 2)),
           ((F(1, 2), F(1, 2)), F(0), F(1, 2), F(5, 9)),
           ((F(2), F(1, 3)), F(25, 34), F(49, 58), F(565, 1058)),
           ((F(-3, 2), F(5, 7)), F(961, 1157), F(121, 317), F(719569, 1086338)),
           ((F(5, 3), F(-2)), F(121, 130), F(1, 10), F(85, 98)),
           ((F(1, 7), F(3, 4)), F(289, 1073), F(625, 1409), F(1568305, 3080162))]
    for (t, r), pin_O, pin_P, pin_pur in pts:
        nO, nP = run_point(t, r, vac, bl)
        u, v = t - r, t + r
        assert nO == QI(u * u / (1 + u * u)) and nP == QI(v * v / (1 + v * v))
        assert nO == QI(pin_O) and nP == QI(pin_P)
        assert purity_checks(t, r, vac) == pin_pur
    GA.check("L_x = span{(1 - u a*b*)|0>, (b* - v a*)|0>} with ascent occupations u^2/(1+u^2), v^2/(1+v^2), "
             "N block-diagonal, real on the hyperbolic planes, +-i on e3 e4; (a,b) pure on the two spanning vacua "
             "and mixed on their superposition (purity (w1^2+w2^2)/(w1+w2)^2)", True)
