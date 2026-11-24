"""Wall-conjugation invariance, Hypothesis (CW), on the doubled radiation-type field: exact checks.

Setting.  Rescaled Dirac field chi (an even multivector of Cl(1,3)) with the mass function M(eta) = mu eta, odd in
the conformal time eta (wall at eta = 0).  A plane wave chi = phi(eta) exp(-I sigma_3 k.x) obeys phi' = G phi with
G = M A0 + B_k,  A0 phi = g0 phi g0 (I sigma_3)^-1,  B_k phi = -g0 kappa phi (I sigma_3)^-1  (the stored wall
result's mode operator).  One momentum-helicity sector is the stored two-level system I u' = H u,
H = M s3 + k s1, with Bloch form s' = -2 I (h ^ s) = 2 h x s, h = (k, 0, M).

(1) Cl(1,3): the wall reflection W phi = g0 phi g0 commutes with the mass part and with the right unit and
    anticommutes with the momentum part; the charge conjugation c phi = phi sigma_1 anticommutes with the unit;
    so W phi(-eta) solves the mode equation exactly when M is odd, and c W is an antilinear symmetry.
(2) Bloch vectors: among the eight diagonal sign maps O, s(eta) -> O s(-eta) preserves the Bloch equation with
    M odd exactly for O_A = diag(1, 1, -1) and O_B = diag(-1, -1, 1); the unitary s3 of the two-level system
    (the reduction of W) induces O_B; -1 is the point-fixing energy-reversing map.
(3) Power series in eta of the Bloch equation with M = mu eta: s is O_A-invariant exactly when s3(0) = 0 and
    O_B-invariant exactly when s(0) is along s3; the flow is isometric.
(4) The derivative-ordered adiabatic series S = sum_n delta^n d_n(c, sigma), c = k/w, sigma = M/w,
    delta = mu/w^2: solvable to every computed order, unit norm, residual of order delta^(N+1), and
    O_A-covariant, so at the wall it has no s3 part: the late-time vacuum is on the invariant circle to every
    order, and the wall-instant vacuum differs from it at order delta (the stored M_1^2/(16 k^4)).
(5) The circle of invariant pure states: equal occupation over the early-time and late-time vacua, occupation
    (1 - sqrt(1-q) cos chi)/2, minimum n0 with 4 n0 (1 - n0) = q, on rational points of the sphere.
(6) The Weber form of the mode equation and the bookkeeping of the transition probability exp(-pi k^2/mu):
    the reduction to Weber's equation and the arithmetic of the exponents only.  The special-function facts
    (asymptotic form, connection formula, reflection formula) are in the proof text and are not checked.
(7) Without isotropy the conjugation pairs the sectors of momenta k and -k: v_{-k}(0) = O_A v_k(0); the sum of the
    two occupations is 1 - sqrt(1-q) v_k(0).m >= 2 n0, and the pair (s_out, s_in) has occupations 0 and q.
"""
from fractions import Fraction as Fr
from itertools import product

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------------------------------------
# (1) spacetime algebra Cl(1,3): g0^2 = +1, g1^2 = g2^2 = g3^2 = -1
# ---------------------------------------------------------------------------------------------------------
SQ13 = GA.sig(1, 3)
G0, G1, G2, G3 = (GA.gen(i) for i in range(4))


def m13(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ13)
    return out


EVEN = [{b: Fr(1)} for b in GA.all_blades(4) if len(b) % 2 == 0]
ISIG3 = m13(G2, G1)                 # I sigma_3 = g2 g1, the right unit of the Hestenes form
ISIG3_INV = GA.neg(ISIG3)
SIG1 = m13(G1, G0)                  # sigma_1 = g1 g0
I4 = m13(G0, G1, G2, G3)


def kappa(kv):
    return GA.add(GA.scal(kv[0], G1), GA.scal(kv[1], G2), GA.scal(kv[2], G3))


def A0(phi):
    return m13(G0, phi, G0, ISIG3_INV)


def Bk(kv, phi):
    return GA.neg(m13(G0, kappa(kv), phi, ISIG3_INV))


def gen13(kv, M, phi):
    return GA.add(GA.scal(M, A0(phi)), Bk(kv, phi))


def Wall(phi):
    return m13(G0, phi, G0)


def Conj(phi):
    return m13(phi, SIG1)


def Junit(phi):
    return m13(phi, ISIG3)


def sprod(phi, chi):
    """(phi, chi) = <g0 rev(phi) g0 chi>_0, the positive scalar product of the even subalgebra."""
    return m13(G0, GA.reverse(phi), G0, chi).get((), Fr(0))


def check_wall_reflection_and_charge_conjugation_in_the_spacetime_algebra():
    premise("synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state")
    assert GA.eq(m13(ISIG3, ISIG3), GA.sc(-1)) and GA.eq(m13(I4, I4), GA.sc(-1))
    assert GA.commutes(G0, ISIG3, SQ13) and GA.anticommutes(SIG1, ISIG3, SQ13)
    # the reflection x -> -g0 x g0 in the wall: g0 -> -g0, g_i -> g_i; on even elements its outermorphism is W
    refl = [GA.neg(m13(G0, v, G0)) for v in (G0, G1, G2, G3)]
    assert refl == [GA.neg(G0), G1, G2, G3]
    for a in range(4):
        for b in range(a + 1, 4):
            assert GA.eq(Wall(m13((G0, G1, G2, G3)[a], (G0, G1, G2, G3)[b])), m13(refl[a], refl[b]))
    # the scalar product is the identity Gram matrix on the eight even blades
    for i, x in enumerate(EVEN):
        for j, y in enumerate(EVEN):
            assert sprod(x, y) == (1 if i == j else 0)
    samples = [((Fr(1), Fr(2), Fr(-3)), Fr(5, 7)), ((Fr(2, 3), Fr(0), Fr(1)), Fr(-4)),
               ((Fr(0), Fr(0), Fr(3)), Fr(1, 2)), ((Fr(-1, 5), Fr(7), Fr(2)), Fr(3))]
    for kv, M in samples:
        k2 = sum(x * x for x in kv)
        mk = tuple(-x for x in kv)
        for phi in EVEN:
            # the generator squares to -(k^2 + M^2) and preserves the even subalgebra
            g2 = gen13(kv, M, gen13(kv, M, phi))
            assert GA.eq(g2, GA.scal(-(k2 + M * M), phi))
            assert all(len(b) % 2 == 0 for b in gen13(kv, M, phi))
            # W: commutes with the mass part and the unit, anticommutes with the momentum part
            assert GA.eq(Wall(A0(phi)), A0(Wall(phi)))
            assert GA.eq(Wall(Bk(kv, phi)), GA.neg(Bk(kv, Wall(phi))))
            assert GA.eq(Wall(Junit(phi)), Junit(Wall(phi)))
            # hence W G(k, -M) = -G(k, M) W: phi(eta) -> W phi(-eta) is a symmetry exactly for M odd
            assert GA.eq(Wall(gen13(kv, -M, phi)), GA.neg(gen13(kv, M, Wall(phi))))
            assert not GA.eq(Wall(gen13(kv, M, phi)), GA.neg(gen13(kv, M, Wall(phi))))
            # c: antilinear, commutes with the mass part, carries momentum k to -k
            assert GA.eq(Conj(Junit(phi)), GA.neg(Junit(Conj(phi))))
            assert GA.eq(Conj(A0(phi)), A0(Conj(phi)))
            assert GA.eq(Conj(Bk(kv, phi)), Bk(mk, Conj(phi)))
            # theta = c W: antilinear, theta G(k, -M) = -G(-k, M) theta
            th = lambda x: Conj(Wall(x))
            assert GA.eq(th(gen13(kv, -M, phi)), GA.neg(gen13(mk, M, th(phi))))
            assert GA.eq(th(Junit(phi)), GA.neg(Junit(th(phi))))
            # left multiplication by I_4 flips the mass part (the conventions' statement), so it is no symmetry
            assert GA.eq(A0(m13(I4, phi)), GA.neg(m13(I4, A0(phi))))
            assert GA.eq(Bk(kv, m13(I4, phi)), m13(I4, Bk(kv, phi)))
        # W, c, the unit are orthogonal and the generator is antisymmetric (the norm is conserved)
        for x in EVEN:
            for y in EVEN:
                assert sprod(Wall(x), Wall(y)) == sprod(x, y) == sprod(Conj(x), Conj(y)) == sprod(Junit(x), Junit(y))
                assert sprod(x, gen13(kv, M, y)) == -sprod(gen13(kv, M, x), y)
    # the generator at k = (1, 2, -3), M = 5/7, as a matrix on the even blades 1, g0g1, g0g2, g0g3, g1g2, g1g3, g2g3, I_4
    kv, M = samples[0]
    assert sum(x * x for x in kv) == 14
    mat = [[sprod(x, gen13(kv, M, y)) for y in EVEN] for x in EVEN]
    assert mat[0] == [0, 2, -1, 0, Fr(-5, 7), 0, 0, -3]
    assert mat[3] == [0, 0, 0, 0, -3, -2, 1, Fr(5, 7)]
    assert mat[7] == [3, 0, 0, Fr(-5, 7), 0, 1, 2, 0]
    # the mass part alone: A0 = right multiplication by g1 g2 after the reflection W, with A0^2 = -1
    assert GA.eq(A0(GA.sc(1)), m13(G1, G2)) and GA.eq(A0(A0(m13(G0, G3))), GA.neg(m13(G0, G3)))
    assert GA.eq(Wall(m13(G0, G1)), GA.neg(m13(G0, G1))) and GA.eq(Wall(m13(G1, G2)), m13(G1, G2))
    return True


# ---------------------------------------------------------------------------------------------------------
# (2) Pauli algebra Cl(3,0): Bloch vectors
# ---------------------------------------------------------------------------------------------------------
SQ3 = GA.sig(3, 0)
S = [GA.gen(i) for i in range(3)]
IP = GA.mul(GA.mul(S[0], S[1], SQ3), S[2], SQ3)


def vec(a):
    return GA.add(*[GA.scal(a[i], S[i]) for i in range(3)])


def comps(x):
    return [x.get((i,), Fr(0)) for i in range(3)]


def bloch_rhs(h, s):
    """-2 I (h ^ s) as a component list; h, s component lists."""
    hv, sv = vec(h), vec(s)
    wedge = GA.scal(Fr(1, 2), GA.sub(GA.mul(hv, sv, SQ3), GA.mul(sv, hv, SQ3)))
    return comps(GA.scal(-2, GA.mul(IP, wedge, SQ3)))


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def dotv(a, b):
    return sum(x * y for x, y in zip(a, b))


def check_exactly_two_reflections_of_bloch_vectors_preserve_the_mode_equation():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    assert GA.eq(GA.mul(IP, IP, SQ3), GA.sc(-1))
    basis = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
    # the stored Bloch form: -2 I (h ^ s) = 2 h x s
    for h in basis:
        for s in basis:
            assert bloch_rhs(h, s) == [2 * x for x in cross(h, s)]
    samples = [(Fr(3), Fr(2, 5)), (Fr(1, 2), Fr(-7, 3)), (Fr(5), Fr(1))]      # (k, M) with M = mu eta
    good = []
    for signs in product((1, -1), repeat=3):
        O = lambda v, sg=signs: [sg[i] * v[i] for i in range(3)]
        ok = True
        for k, M in samples:
            hp, hm = [k, Fr(0), M], [k, Fr(0), -M]
            for s in basis:
                # s~(eta) = O s(-eta):  s~' = -O (2 h(-eta) x s(-eta)) must equal 2 h(eta) x O s(-eta)
                lhs = [-x for x in O(bloch_rhs(hm, s))]
                if lhs != bloch_rhs(hp, O(s)):
                    ok = False
        if ok:
            good.append(signs)
    assert sorted(good) == [(-1, -1, 1), (1, 1, -1)]
    # O_A = reflection along s3, v -> -s3 v s3;  O_B = half turn about s3, v -> s3 v s3 = Ad of the unitary s3
    for v in basis:
        oa = comps(GA.neg(GA.mul(GA.mul(S[2], vec(v), SQ3), S[2], SQ3)))
        ob = comps(GA.mul(GA.mul(S[2], vec(v), SQ3), S[2], SQ3))
        assert oa == [v[0], v[1], -v[2]] and ob == [-v[0], -v[1], v[2]]
    # s3 commutes with the mass part M s3 of H and anticommutes with the momentum part k s1 (as W does in (1))
    assert GA.commutes(S[2], S[2], SQ3) and GA.anticommutes(S[2], S[0], SQ3)
    # the point-fixing energy-reversing map s -> -s preserves the equation at fixed eta and fixes only s = 0
    for k, M in samples:
        for s in basis:
            assert [-x for x in bloch_rhs([k, Fr(0), M], s)] == bloch_rhs([k, Fr(0), M], [-x for x in s])
    # O_A fixes the wall-instant vacuum s1; O_B reverses it
    s1v = vec(basis[0])
    assert GA.eq(GA.neg(GA.mul(GA.mul(S[2], s1v, SQ3), S[2], SQ3)), s1v)
    assert GA.eq(GA.mul(GA.mul(S[2], s1v, SQ3), S[2], SQ3), GA.neg(s1v))
    return True


# ---------------------------------------------------------------------------------------------------------
# (3) power series in eta: s' = 2 h x s, h = (k, 0, mu eta)
# ---------------------------------------------------------------------------------------------------------
NS = 24


def bloch_series(k, mu, s0, N=NS):
    """coefficients s_n of s(eta) = sum s_n eta^n: (n+1) s_{n+1} = 2 (k e1 x s_n + mu e3 x s_{n-1})."""
    ser = [list(s0)]
    for n in range(N):
        t = [2 * k * x for x in cross([1, 0, 0], ser[n])]
        if n >= 1:
            u = cross([0, 0, 1], ser[n - 1])
            t = [t[i] + 2 * mu * u[i] for i in range(3)]
        ser.append([x / Fr(n + 1) for x in t])
    return ser


def series_dot(a, b, N):
    return [sum(dotv(a[i], b[n - i]) for i in range(n + 1)) for n in range(N + 1)]


def check_invariant_states_are_a_disk_per_mode_and_the_flow_is_isometric():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    for k, mu in [(Fr(3, 2), Fr(1)), (Fr(1), Fr(5, 3)), (Fr(2), Fr(0))]:
        inits = [[Fr(3, 5), Fr(4, 5), Fr(0)], [Fr(1), Fr(0), Fr(0)], [Fr(1, 4), Fr(-1, 3), Fr(0)],
                 [Fr(0), Fr(0), Fr(1)], [Fr(0), Fr(0), Fr(-2, 7)], [Fr(2, 3), Fr(1, 3), Fr(2, 3)],
                 [Fr(0), Fr(0), Fr(0)]]
        sers = [bloch_series(k, mu, s0) for s0 in inits]
        for s0, ser in zip(inits, sers):
            # the series solves the equation: residual of s' - 2 h x s vanishes coefficientwise
            for n in range(NS):
                rhs = [2 * k * x for x in cross([1, 0, 0], ser[n])]
                if n >= 1:
                    rhs = [rhs[i] + 2 * mu * cross([0, 0, 1], ser[n - 1])[i] for i in range(3)]
                assert [(n + 1) * x for x in ser[n + 1]] == rhs
            # O_A s(-eta) = s(eta): components 1, 2 even in eta, component 3 odd
            inv_a = all(ser[n][0] == 0 and ser[n][1] == 0 for n in range(1, NS + 1, 2)) and \
                all(ser[n][2] == 0 for n in range(0, NS + 1, 2))
            assert inv_a == (s0[2] == 0)
            # O_B s(-eta) = s(eta): components 1, 2 odd, component 3 even
            inv_b = all(ser[n][0] == 0 and ser[n][1] == 0 for n in range(0, NS + 1, 2)) and \
                all(ser[n][2] == 0 for n in range(1, NS + 1, 2))
            assert inv_b == (s0[0] == 0 and s0[1] == 0)
        # isometry: the scalar product of two solutions is constant in eta (a rotation), coefficientwise
        for a in range(len(inits)):
            for b in range(a, len(inits)):
                d = series_dot(sers[a], sers[b], NS)
                assert d[0] == dotv(inits[a], inits[b]) and all(x == 0 for x in d[1:])
    # massless (mu = 0): the stationary states are the multiples of s1, all O_A-invariant; s2(0) != 0 is invariant
    # and not stationary
    premise("synthesis.deposit-over-the-conformal-vacuum-is-hadamard-exactly-when-every-occupation-moment-is-finite")
    ser = bloch_series(Fr(2), Fr(0), [Fr(0), Fr(1), Fr(0)])
    assert ser[1] == [0, 0, 4] and ser[1] != [0, 0, 0]
    # explicit coefficients: k = 3/2, mu = 1, s(0) = (3/5, 4/5, 0) on the invariant circle
    ser = bloch_series(Fr(3, 2), Fr(1), [Fr(3, 5), Fr(4, 5), Fr(0)])
    assert ser[1] == [0, 0, Fr(12, 5)] and ser[2] == [Fr(-4, 5), -3, 0]
    assert ser[3] == [0, 0, -3] and ser[4] == [Fr(3, 2), Fr(37, 20), 0]
    # and the O_B-invariant Fock state s(0) = s3 at k = 1, mu = 5/3
    ser = bloch_series(Fr(1), Fr(5, 3), [Fr(0), Fr(0), Fr(1)])
    assert ser[1] == [0, -2, 0] and ser[2] == [0, 0, -2] and ser[3] == [Fr(20, 9), Fr(4, 3), 0]
    for t in (Fr(1), Fr(-1), Fr(1, 3), Fr(0)):
        ser = bloch_series(Fr(2), Fr(0), [t, Fr(0), Fr(0)])
        assert all(x == [0, 0, 0] for x in ser[1:])
    return True


# ---------------------------------------------------------------------------------------------------------
# (4) the derivative-ordered adiabatic series: polynomials in c, sigma, delta with c^2 + sigma^2 = 1
#     monomial key (a, b, n) = c^a sigma^b delta^n, a in {0, 1}
# ---------------------------------------------------------------------------------------------------------
def qred(p):
    out = {}
    for (a, b, n), v in p.items():
        # c^a = c^(a mod 2) (1 - sigma^2)^(a div 2)
        terms = {(a % 2, b, n): v}
        for _ in range(a // 2):
            nt = {}
            for (x, y, z), w in terms.items():
                nt[(x, y, z)] = nt.get((x, y, z), 0) + w
                nt[(x, y + 2, z)] = nt.get((x, y + 2, z), 0) - w
            terms = nt
        for m, w in terms.items():
            out[m] = out.get(m, 0) + w
    return {m: v for m, v in out.items() if v != 0}


def qadd(p, q, c=1):
    out = dict(p)
    for m, v in q.items():
        out[m] = out.get(m, 0) + c * v
    return {m: v for m, v in out.items() if v != 0}


def qmul(p, q):
    out = {}
    for (a, b, n), v in p.items():
        for (x, y, z), w in q.items():
            m = (a + x, b + y, n + z)
            out[m] = out.get(m, 0) + v * w
    return qred(out)


def qD(p):
    """D = (1/w) d/d eta:  D c = -delta c sigma,  D sigma = delta c^2,  D delta = -2 delta^2 sigma."""
    out = {}
    for (a, b, n), v in p.items():
        if a + 2 * n:
            m = (a, b + 1, n + 1)
            out[m] = out.get(m, 0) - (a + 2 * n) * v
        if b:
            m = (a + 2, b - 1, n + 1)
            out[m] = out.get(m, 0) + b * v
    return qred(out)


QC, QS, Q1 = {(1, 0, 0): Fr(1)}, {(0, 1, 0): Fr(1)}, {(0, 0, 0): Fr(1)}
HHAT = [QC, {}, QS]


def qcross(a, b):
    return [qadd(qmul(a[1], b[2]), qmul(a[2], b[1]), -1), qadd(qmul(a[2], b[0]), qmul(a[0], b[2]), -1),
            qadd(qmul(a[0], b[1]), qmul(a[1], b[0]), -1)]


def qdot(a, b):
    return qadd(qadd(qmul(a[0], b[0]), qmul(a[1], b[1])), qmul(a[2], b[2]))


def qorder(p, n):
    return {m: v for m, v in p.items() if m[2] == n}


NA = 6


def adiabatic_delta_series(N=NA):
    d = [HHAT]                                            # d[n] carries its factor delta^n
    for n in range(N):
        e = [qD(x) for x in d[n]]                         # order delta^(n+1)
        assert qdot(HHAT, e) == {}, ("solvability fails", n)
        perp = [{m: -v / 2 for m, v in x.items()} for x in qcross(HHAT, e)]
        nrm = {}
        for a in range(1, n + 1):
            nrm = qadd(nrm, qdot(d[a], d[n + 1 - a]))
        par = {m: -v / 2 for m, v in nrm.items()}
        d.append([qadd(perp[i], qmul(par, HHAT[i])) for i in range(3)])
    return d


def qeval(p, c, s, dl):
    return sum(v * c ** a * s ** b * dl ** n for (a, b, n), v in p.items())


def check_late_time_vacuum_series_is_on_the_invariant_circle_to_every_order():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    premise("synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard")
    premise("synthesis.imported-microlocal-hadamard-condition")
    d = adiabatic_delta_series()
    assert d[2] == [{(1, 2, 2): Fr(-5, 8), (1, 0, 2): Fr(-1, 8)}, {}, {(0, 1, 2): Fr(5, 8), (0, 3, 2): Fr(-5, 8)}]
    assert d[3] == [{}, {(1, 2, 3): Fr(-35, 16), (1, 0, 3): Fr(5, 16)}, {}]
    # first order: d_1 = (c/2) delta s2, i.e. mu k/(2 w^3) s2, at the wall mu/(2 k^2) s2 (the stored c_2 = M_1 s2/2)
    assert d[1] == [{}, {(1, 0, 1): Fr(1, 2)}, {}]
    for n in range(NA + 1):
        # each d_n is homogeneous of degree n in delta
        assert all(m[2] == n for x in d[n] for m in x)
        # unit norm order by order
        tot = {}
        for a in range(n + 1):
            tot = qadd(tot, qdot(d[a], d[n - a]))
        assert tot == (Q1 if n == 0 else {})
        # O_A covariance (sigma -> -sigma with the reflection along s3): parts 1, 2 even in sigma, part 3 odd
        assert all(m[1] % 2 == 0 for m in d[n][0]) and all(m[1] % 2 == 0 for m in d[n][1])
        assert all(m[1] % 2 == 1 for m in d[n][2])
        # so at the wall (sigma = 0, c = 1) the series has no s3 part: it lies on the invariant circle
        assert qeval(d[n][2], Fr(1), Fr(0), Fr(1)) == 0
    # residual of the truncated series: D S_N - 2 hhat x S_N has only the order delta^(N+1)
    SN = [{}, {}, {}]
    for n in range(NA + 1):
        SN = [qadd(SN[i], d[n][i]) for i in range(3)]
    res = [qadd(qD(SN[i]), {m: 2 * v for m, v in qcross(HHAT, SN)[i].items()}, -1) for i in range(3)]
    assert any(res) and all(m[2] == NA + 1 for x in res for m in x)
    # at the wall: S(0) = s1 + (delta/2) s2 - (delta^2/8) s1 + ..., so the wall-instant vacuum s1 has
    # 1 - S(0).s1 = delta^2/8 + O(delta^4): |beta|^2 = mu^2/(16 k^4), the stored value with M_1 = mu
    wall = [[qeval(d[n][i], Fr(1), Fr(0), Fr(1)) for i in range(3)] for n in range(NA + 1)]
    assert wall[0] == [1, 0, 0] and wall[1] == [0, Fr(1, 2), 0] and wall[2] == [Fr(-1, 8), 0, 0]
    assert wall[3][0] == 0 and wall[3][1] != 0
    # the bound: |d_n| <= C_n delta^n with c, sigma in [-1, 1]; sample points of the circle c^2 + sigma^2 = 1
    for (c, s) in [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(-12, 13)), (Fr(1), Fr(0))]:
        for n in range(NA + 1):
            bound = sum(abs(v) for x in d[n] for v in x.values())
            assert all(abs(qeval(x, c, s, Fr(1))) <= bound for x in d[n])
    return True


# ---------------------------------------------------------------------------------------------------------
# (5) the circle of invariant pure states (rational points of the sphere)
# ---------------------------------------------------------------------------------------------------------
def rat_circle(t):
    return Fr(1 - t * t, 1 + t * t), Fr(2 * t, 1 + t * t)


def check_invariant_circle_occupations_and_the_minimum():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    for ta, tp in [(Fr(1, 3), Fr(1, 2)), (Fr(2, 7), Fr(-3, 4)), (Fr(1, 9), Fr(5)), (Fr(4, 5), Fr(1, 6))]:
        ca, sa = rat_circle(ta)             # s_out(0) has s3 part sin(alpha), in-plane part cos(alpha) > 0
        cp, sp = rat_circle(tp)             # azimuth of the in-plane part
        s_out = [ca * cp, ca * sp, sa]
        s_in = [s_out[0], s_out[1], -s_out[2]]            # O_A image
        assert dotv(s_out, s_out) == 1
        q = Fr(1, 2) * (1 - dotv(s_in, s_out))
        assert q == sa * sa == s_out[2] ** 2
        mhat = [cp, sp, Fr(0)]                              # along s_in + s_out
        assert [s_in[i] + s_out[i] for i in range(3)] == [2 * ca * x for x in mhat]
        perp = [-sp, cp, Fr(0)]
        n0 = Fr(1, 2) * (1 - dotv(mhat, s_out))
        assert 4 * n0 * (1 - n0) == q and n0 == Fr(1, 2) * (1 - ca)
        for tc in [Fr(0), Fr(1, 5), Fr(-2, 3), Fr(3), Fr(1)]:
            cc, sn = rat_circle(tc)
            e = [cc * mhat[i] + sn * perp[i] for i in range(3)]
            assert dotv(e, e) == 1 and e[2] == 0
            # equal occupation over the early-time and the late-time vacuum
            assert dotv(e, s_in) == dotv(e, s_out)
            n = Fr(1, 2) * (1 - dotv(e, s_out))
            assert n == Fr(1, 2) * (1 - ca * cc)
            assert (n == n0) == (tc == 0) and n >= n0
            # the opposite point is invariant too, with occupation 1 - n: the circle does not tell vacuum from sea
            assert Fr(1, 2) * (1 + dotv(e, s_out)) == 1 - n
        # O_B-invariant pure states +-s3: occupation (1 -+ sin alpha)/2 over the late-time vacuum
        assert Fr(1, 2) * (1 - dotv([0, 0, 1], s_out)) == Fr(1, 2) * (1 - sa)
        # mixtures t e stay invariant, with occupation (1 - t cos(alpha) cos(chi))/2
        for tt in (Fr(0), Fr(1, 2), Fr(1)):
            v = [tt * x for x in mhat]
            assert v[2] == 0 and Fr(1, 2) * (1 - dotv(v, s_out)) == Fr(1, 2) * (1 - tt * ca)
    return True


def check_pair_bound_without_isotropy():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    OA = lambda v: [v[0], v[1], -v[2]]
    for ta, tp in [(Fr(1, 3), Fr(1, 2)), (Fr(2, 7), Fr(-3, 4)), (Fr(1, 9), Fr(5)), (Fr(4, 5), Fr(1, 6))]:
        ca, sa = rat_circle(ta)             # sqrt(1 - q) = ca > 0, s_out(0).s3 = sa
        cp, sp = rat_circle(tp)
        s_out = [ca * cp, ca * sp, sa]
        s_in = OA(s_out)
        mhat = [cp, sp, Fr(0)]
        q = sa * sa
        n0 = Fr(1, 2) * (1 - ca)
        occ = lambda v: Fr(1, 2) * (1 - dotv(v, s_out))
        vs = [[Fr(1, 2), Fr(1, 3), Fr(1, 4)], [Fr(0), Fr(0), Fr(1)], [Fr(-3, 5), Fr(0), Fr(4, 5)],
              [Fr(2, 3), Fr(2, 3), Fr(1, 3)], [Fr(0), Fr(0), Fr(0)], s_out, s_in, mhat, [-x for x in mhat]]
        for v in vs:
            assert dotv(v, v) <= 1
            w = OA(v)                        # the vector of the paired sector
            assert OA(w) == v                # the condition is an involution: one vector of each pair is free
            assert occ(w) == Fr(1, 2) * (1 - dotv(v, s_in))
            pair = occ(v) + occ(w)
            assert pair == 1 - ca * dotv(v, mhat)
            assert pair >= 2 * n0 and (pair == 2 * n0) == (v == mhat)
        # the pair (s_out, s_in): occupations 0 and q, so the floor fails in one sector and holds for the pair
        assert occ(s_out) == 0 and occ(OA(s_out)) == q and 0 < n0 < q
        assert q - 2 * n0 == ca * (1 - ca)
    # explicit values at tan(alpha/2) = 1/3: sqrt(1 - q) = 4/5, q = 9/25, n0 = 1/10
    ca, sa = rat_circle(Fr(1, 3))
    assert (ca, sa * sa, Fr(1, 2) * (1 - ca)) == (Fr(4, 5), Fr(9, 25), Fr(1, 10))
    return True


# ---------------------------------------------------------------------------------------------------------
# (6) Weber form and the transition probability (numbers in span{1, I}: Gaussian rationals)
#     reduction and exponent arithmetic only; the special-function facts are not checked
# ---------------------------------------------------------------------------------------------------------
def check_weber_form_and_transition_probability_bookkeeping():
    premise("synthesis.massive-dirac-instantaneous-vacuum-and-non-smooth-descents-are-not-hadamard")
    QI = GA.QI
    I = QI(0, 1)
    N = 16
    for k, mu, u0 in [(Fr(3, 2), Fr(2), (QI(1, 2), QI(-1, 3))), (Fr(1), Fr(1, 3), (QI(0, 1), QI(2, 0)))]:
        # I u1' = M u1 + k u2, I u2' = k u1 - M u2, M = mu eta: power series
        u1, u2 = [u0[0]], [u0[1]]
        for n in range(N):
            a = u2[n] * k + (u1[n - 1] * mu if n >= 1 else QI(0))
            b = u1[n] * k - (u2[n - 1] * mu if n >= 1 else QI(0))
            u1.append(a / I / (n + 1))
            u2.append(b / I / (n + 1))
        # second-order forms: u1'' + (k^2 + mu^2 eta^2 + I mu) u1 = 0, u2'' + (k^2 + mu^2 eta^2 - I mu) u2 = 0
        for n in range(N - 1):
            for u, sgn in ((u1, 1), (u2, -1)):
                r = u[n + 2] * ((n + 2) * (n + 1)) + u[n] * (QI(k * k) + I * (sgn * mu))
                if n >= 2:
                    r = r + u[n - 2] * (mu * mu)
                assert r == QI(0)
        # Weber variable z = exp(I pi/4) sqrt(2 mu) eta, z^2 = 2 I mu eta^2: the u2 equation becomes
        # w'' + (p + 1/2 - z^2/4) w = 0 with p = -1 - I k^2/(2 mu)
        nu = k * k / mu
        p = QI(-1) - I * (nu / 2)
        assert (QI(k * k) - I * mu) / (I * (2 * mu)) == p + Fr(1, 2)
        assert QI(mu * mu) / (I * (2 * mu)) == QI(0) - I * (mu / 2)          # mu^2 eta^2/(2 I mu) = -z^2/(4 eta^2)
        assert (I * (2 * mu)) / 4 == I * (mu / 2)
        assert QI(0) - p - 1 == I * (nu / 2)                                 # index of the second solution
    # moduli, in units of pi nu in the exponent: |exp(-I pi (p+1)/2)|^2 -> -1/2, |(I z)^(I nu/2)|^2 at
    # arg(I z) = -pi/4 -> +1/4, the norm (2/nu) exp(pi nu/4) -> -1/4; the Gamma factor gives (4/nu) sinh(pi nu/2)
    expo = Fr(-1, 2) + Fr(1, 4) - Fr(1, 4)
    assert expo == Fr(-1, 2)
    assert 2 * Fr(1, 2) * (Fr(-1, 4) - Fr(3, 4)) == Fr(-1)       # the same exponent from the arc pi/4 -> -3 pi/4
    for x in (Fr(1, 2), Fr(3, 7), Fr(9, 10)):                     # x = exp(-pi nu/2)
        sinh = (1 / x - x) / 2
        alpha2 = 2 * sinh * x                                    # 2 sinh(pi nu/2) exp(-pi nu/2)
        q = x * x
        assert alpha2 == 1 - q and alpha2 + q == 1
    # the floor n0 solves 4 n0 (1 - n0) = q and lies between q/4 and q/2 (rational points: q = s^2, sqrt(1-q) = c)
    for t in (Fr(1, 3), Fr(2, 5)):
        c, s = rat_circle(t)
        n0 = Fr(1, 2) * (1 - c)
        assert 4 * n0 * (1 - n0) == s * s and Fr(1, 4) * s * s <= n0 <= Fr(1, 2) * s * s
    return True
