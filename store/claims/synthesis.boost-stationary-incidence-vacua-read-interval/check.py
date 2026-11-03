"""synthesis.boost-stationary-incidence-vacua-read-interval: exact checks in Gaussian-rational arithmetic.

Same model as the check of synthesis.incidence-vacua-thermofield-real-capacity: Cl(2,4) on the
8-dim Fock module (Jordan-Wigner, three qubits); e1 (+), e2, e3, e4 (-), ep (+), em (-), g* = g^{-1};
a = n0, a* = ninf/2; b = (e1+e2)/2, b* = (e1-e2)/2; at x = t e1 + r e2, u = t - r, v = t + r.
Checked:
  (a) the boost rotor S = ch + sh e1e2 (ch^2 - sh^2 = 1) commutes with N, is not unitary, and
      S X(x) S^{-1} = X(x') with u' = (ch+sh)^2 u, v' = v/(ch+sh)^2: S maps L_x onto L_x';
  (b) <N> on lam Omega + mu Psi is (|lam|^2 u^2 + |mu|^2 v^2)/(|lam|^2 (1+u^2) + |mu|^2 (1+v^2));
  (c) along sampled boost orbits every occupation segment contains f(|Q|), f(s) = s/(1+s), and at
      the orbit point with |u| = |v| the segment is the single value f(|Q|);
  (d) the vacuum with |lam|^2 |u| = |mu|^2 |v| has <N> = f(|Q|) and a mixed (a,b) pair, purity
      (w1^2 + w2^2)/(w1 + w2)^2 with w1 = |v|(1+u^2), w2 = |u|(1+v^2), pinned values.
"""
import GA
from tp_premise import premise

from fractions import Fraction as F
from itertools import combinations
from GA import QI, field_kernel, field_rank

Z0, ONE, I = QI(0), QI(1), QI(0, 1)


def mat(rows):
    return [[QI(x) if not isinstance(x, QI) else x for x in r] for r in rows]


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


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


SX = mat([[0, 1], [1, 0]]); SY = [[Z0, -I], [I, Z0]]; SZ = mat([[1, 0], [0, -1]]); I2 = eye(2)


def k3(A, B, C):
    return kron(kron(A, B), C)


G = [k3(SX, I2, I2), k3(SY, I2, I2), k3(SZ, SX, I2), k3(SZ, SY, I2), k3(SZ, SZ, SX), k3(SZ, SZ, SY)]
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
    maj = [e1, msc(I, e2), ep, msc(I, em)]
    tot = F(0)
    for k in range(5):
        for S in combinations(range(4), k):
            M = E8
            for i in S:
                M = mm(M, maj[i])
            z = expect(M, state)
            tot += z.re * z.re + z.im * z.im
    return tot / 4




def f(s):
    return s / (1 + s)


B12 = mm(e1, e2)


def rotor(ch, sh):
    assert ch * ch - sh * sh == 1
    return madd(msc(ch, E8), msc(sh, B12)), madd(msc(ch, E8), msc(-sh, B12))


def tr(A):
    return sum((A[i][i] for i in range(8)), QI(0))


def coords(M):
    """M = t e1 + r e2 -> (t, r), using tr(e1 e1) = 8, tr(e2 e2) = -8"""
    return (tr(mm(M, e1)) / 8).re, (tr(mm(M, e2)) / (-8)).re


def X(t, r):
    Q = (t - r) * (t + r)
    return madd(n0, msc(t, e1), msc(r, e2), msc(-Q * half, ninf))


def spanning(u, v, vac):
    Om = mv(madd(E8, msc(-u, mm(ad, bd))), vac[1])
    Ps = mv(madd(bd, msc(-v, ad)), vac[-1])
    return Om, Ps


def check_boost_maps_lines_and_fixes_ascent():
    premise("one-relation.spacetime-manifold-vacuum-lines")
    premise("synthesis.incidence-vacua-thermofield-real-capacity")
    assert setup_checks() and car_checks()
    assert meq(mm(B12, B12), E8) and meq(dag(B12), B12)          # boost bivector: square 1, self-adjoint
    for (ch, sh, k) in [(F(5, 4), F(3, 4), F(4)), (F(5, 3), F(4, 3), F(9)), (F(13, 12), F(-5, 12), F(4, 9))]:
        S, Si = rotor(ch, sh)
        assert meq(mm(S, Si), E8)
        assert not meq(dag(S), Si)                                # not unitary for the Hermitian structure
        assert meq(mm(S, N), mm(N, S))                            # the ascent mode is boost-invariant
        assert (ch + sh) * (ch + sh) == k
        for (t, r) in [(F(2), F(1, 3)), (F(-3, 2), F(5, 7)), (F(1, 7), F(3, 4)), (F(0), F(1))]:
            x = madd(msc(t, e1), msc(r, e2))
            t2, r2 = coords(mm(mm(S, x), Si))
            assert t2 - r2 == k * (t - r) and (t2 + r2) * k == t + r
            assert meq(mm(mm(S, X(t, r)), Si), X(t2, r2))       # S maps L_x onto L_x'
    GA.check("the (t,r) boost rotor commutes with N, is not unitary, and carries X(x) to X(x') with "
             "u' = e^lam u, v' = e^-lam v, hence L_x onto L_x'", True)


def check_boost_stationary_section():
    premise("synthesis.incidence-vacua-thermofield-real-capacity")
    premise("singularity.descended-form-state-independent")
    assert setup_checks() and car_checks()
    vac = vacua()
    bl = real_blades()
    # (b) occupation of a general vacuum on the line, generic weights
    for (u, v) in [(F(2), F(-1, 3)), (F(1, 5), F(7, 2))]:
        t, r = (u + v) / 2, (v - u) / 2
        Om, Ps = spanning(u, v, vac)
        for (lam, mu) in [(QI(1), QI(2)), (QI(3, 1), QI(0, -1)), (QI(2, 5), QI(1, 1))]:
            A = (lam * lam.conj()).re
            B = (mu * mu.conj()).re
            phi = [lam * Om[i] + mu * Ps[i] for i in range(8)]
            assert all(z == Z0 for z in mv(X(t, r), phi))
            assert expect(N, phi) == QI((A * u * u + B * v * v) / (A * (1 + u * u) + B * (1 + v * v)))
    # (c) orbits: sampled boosts of x0, with pinned segment endpoints at the collapse point
    # x0 given by (u, v); k = e^lam rational; kc = sqrt|v/u| puts the orbit point on |u| = |v|
    orbits = [((F(1, 4), F(9)), F(6), F(9, 13)),
              ((F(-1, 9), F(4, 25)), F(6, 5), F(4, 229)),
              ((F(4), F(1, 16)), F(1, 8), F(1, 5))]
    for (u0, v0), kc, pin in orbits:
        Q = u0 * v0
        target = f(abs(Q))
        assert target == pin
        ks = [F(1, 16), F(1, 3), F(1), F(5, 2), F(16), kc]
        for k in ks:
            u, v = k * u0, v0 / k
            t, r = (u + v) / 2, (v - u) / 2
            nO, nP = run_point(t, r, vac, bl)                     # exact matrices: endpoints of the segment
            lo, hi = min(nO.re, nP.re), max(nO.re, nP.re)
            assert lo <= target <= hi
            if k == kc:
                assert abs(u) == abs(v) and lo == hi == target    # the segment collapses
            else:
                assert lo < target < hi
    # (d) the stationary vacuum: |lam|^2 |u| = |mu|^2 |v|, with exact square roots chosen
    cases = [((F(1, 4), F(9)), (F(3), F(1, 2)), F(130993, 231361)),
             ((F(-1, 9), F(4, 25)), (F(2, 5), F(1, 3)), F(100521361, 195132961)),
             ((F(4), F(1, 16)), (F(1, 4), F(2)), F(70673, 105625))]
    for (u, v), (lam, mu), pin in cases:
        assert lam * lam == abs(v) and mu * mu == abs(u)
        t, r = (u + v) / 2, (v - u) / 2
        Om, Ps = spanning(u, v, vac)
        phi = [lam * Om[i] + mu * Ps[i] for i in range(8)]
        assert all(z == Z0 for z in mv(X(t, r), phi))
        assert expect(N, phi) == QI(f(abs(u * v)))
        assert expect(a, phi) == Z0                               # diagonal ascent marginal
        w1, w2 = abs(v) * (1 + u * u), abs(u) * (1 + v * v)
        pur = ab_purity(phi)
        assert pur == (w1 * w1 + w2 * w2) / ((w1 + w2) * (w1 + w2)) == pin and pur < 1
        # the pure spanning vacua are not stationary: their occupations differ from f(|Q|)
        assert expect(N, Om) != QI(f(abs(u * v))) and expect(N, Ps) != QI(f(abs(u * v)))
    GA.check("along every sampled boost orbit the occupation segments meet only in f(|Q|); the vacuum "
             "|lam|^2|u| = |mu|^2|v| realises it with a mixed (a,b) pair (spectator entangled)", True)
