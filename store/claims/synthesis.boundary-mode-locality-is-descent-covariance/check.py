"""synthesis.boundary-mode-locality-is-descent-covariance: exact checks.

Three CAR modes in Cl(3,3): v_k = (e_k + e_{3+k})/2, v_k^* = (e_k - e_{3+k})/2, sigma_k = e_k e_{3+k},
P_k = v_k^* v_k = (1 + sigma_k)/2. Mode descent E_k(x) = P_k x P_k + (1 - P_k) x (1 - P_k); joint
descent D = E_0 E_1 E_2.
check_descent_is_joint_pinching: D is idempotent, fixes the eight joint-number projectors and every
sigma monomial, and kills every blade outside the algebra the sigma_k generate (rank of D = 8).
check_covariance_iff_diagonal: the linear map H -> D ad_H - ad_H D on the 64-dimensional algebra has
kernel of dimension exactly 8, containing the eight sigma monomials, so D ad_H = ad_H D iff H is
number-diagonal; hop, pairing and an odd single-mode term each fail, with explicit witnesses.
check_greybody_channel_covariant: a beam splitter (cos, sin) = (3/5, 4/5) between a horizon channel
and a vacuum in-channel gives on the transmitted channel rho -> [[r00 + s^2 r11, c r01], [c r10, c^2 r11]],
which commutes with the single-mode descent and carries occupation n -> (9/25) n.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

NM = 3
SQ = GA.sig(NM, NM)


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


def v(k):
    return GA.scal(F(1, 2), GA.add(GA.gen(k), GA.gen(NM + k)))


def vs(k):
    return GA.scal(F(1, 2), GA.sub(GA.gen(k), GA.gen(NM + k)))


def sig(k):
    return GA.sub(m(vs(k), v(k)), m(v(k), vs(k)))


def Pk(k):
    return m(vs(k), v(k))


def Ek(k, x):
    P = Pk(k)
    Q = GA.sub(GA.sc(1), P)
    return GA.add(m(P, x, P), m(Q, x, Q))


def D(x):
    for k in range(NM):
        x = Ek(k, x)
    return x


def ad(H, X):
    return GA.sub(m(H, X), m(X, H))


BLADES = GA.all_blades(2 * NM)


def coords(x):
    return [x.get(b, F(0)) for b in BLADES]


def sigma_monomials():
    out = []
    for mask in range(2 ** NM):
        x = GA.sc(1)
        for k in range(NM):
            if mask >> k & 1:
                x = m(x, sig(k))
        out.append(x)
    return out


def check_descent_is_joint_pinching():
    premise("singularity.descent-what-it-erases")
    premise("singularity.modular-structure-completed-pair")
    for k in range(NM):
        assert GA.eq(sig(k), GA.mul(GA.gen(k), GA.gen(NM + k), SQ))
        assert GA.eq(GA.scal(2, Pk(k)), GA.add(GA.sc(1), sig(k)))      # sigma = 2N - 1
    images = []
    for b in BLADES:
        x = {b: F(1)}
        y = D(x)
        assert GA.eq(D(y), y)                                         # idempotent
        images.append(coords(y))
    assert GA.mat_rank(images) == 2 ** NM                             # image = 8-dimensional
    for s in sigma_monomials():
        assert GA.eq(D(s), s)                                         # fixes the diagonal algebra
    # joint-number projectors: products of P_k or 1 - P_k, fixed and summing to 1
    tot = {}
    for mask in range(2 ** NM):
        x = GA.sc(1)
        for k in range(NM):
            x = m(x, Pk(k) if mask >> k & 1 else GA.sub(GA.sc(1), Pk(k)))
        assert GA.eq(D(x), x) and GA.eq(m(x, x), x)
        tot = GA.add(tot, x)
    assert GA.eq(tot, GA.sc(1))
    # coherences die: D(v_0^* v_1) = 0 and D(v_0^* v_1^*) = 0
    assert D(m(vs(0), v(1))) == {} and D(m(vs(0), vs(1))) == {}
    return True


def check_covariance_iff_diagonal():
    premise("singularity.descent-what-it-erases")
    premise("singularity.number-diagonal-dynamics-models-scrambling-derived")
    DX = {b: D({b: F(1)}) for b in BLADES}
    cols = []
    for hb in BLADES:
        H = {hb: F(1)}
        col = []
        for xb in BLADES:
            X = {xb: F(1)}
            col.extend(coords(GA.sub(D(ad(H, X)), ad(H, DX[xb]))))
        cols.append(col)
    # matrix with one column per basis element H: rank 64 - 8 means kernel dimension 8
    rows = [list(r) for r in zip(*cols)]
    assert GA.mat_rank(rows) == 4 ** NM - 2 ** NM
    mons = sigma_monomials()
    assert GA.mat_rank([coords(s) for s in mons]) == 2 ** NM
    for s in mons:
        for xb in BLADES:
            X = {xb: F(1)}
            assert GA.eq(D(ad(s, X)), ad(s, DX[xb]))
    # hop, pairing and an odd term fail, witnessed on a joint-number projector
    hop = GA.add(m(vs(0), v(1)), m(vs(1), v(0)))
    pair = GA.add(m(vs(0), vs(1)), m(v(1), v(0)))
    odd = GA.add(v(2), vs(2))
    P0 = Pk(0)
    for H in (hop, pair):
        assert not GA.eq(D(ad(H, P0)), ad(H, D(P0)))
        assert D(ad(H, P0)) == {}                                     # the descended side vanishes
    assert not GA.eq(D(ad(odd, Pk(2))), ad(odd, D(Pk(2))))
    # single-time covariance is weaker: the real hop rotation G = v0* v1 - v1* v0 (G^3 = -G) gives
    # U(theta) = 1 + sin G + (1 - cos) G^2; at theta = pi/2 (a basis permutation) Ad(U) commutes with D,
    # at (cos, sin) = (3/5, 4/5) it does not
    G = GA.sub(m(vs(0), v(1)), m(vs(1), v(0)))
    G2 = m(G, G)
    assert GA.eq(m(G2, G), GA.neg(G))
    def U(c, s):
        return GA.add(GA.sc(1), GA.scal(s, G), GA.scal(1 - c, G2))
    for (c, s), covariant in [((F(0), F(1)), True), ((F(3, 5), F(4, 5)), False)]:
        Uf, Ub = U(c, s), U(c, -s)
        assert GA.eq(m(Uf, Ub), GA.sc(1))
        ok = all(GA.eq(D(m(Uf, {xb: F(1)}, Ub)), m(Uf, DX[xb], Ub)) for xb in BLADES)
        assert ok == covariant
    # a diagonal generator with cross terms (the controlled-Z kind) passes
    cz = GA.add(GA.scal(3, m(sig(0), sig(1))), GA.scal(F(-2, 7), sig(2)), m(sig(0), sig(1), sig(2)))
    for xb in BLADES:
        X = {xb: F(1)}
        assert GA.eq(D(ad(cz, X)), ad(cz, DX[xb]))
    return True


def check_greybody_channel_covariant():
    premise("singularity.descent-what-it-erases")
    c, s = F(3, 5), F(4, 5)
    assert c * c + s * s == 1

    def phi(r):
        # basis |n_h n_in>; U|00> = |00>, U|10> = c|10> + s|01>; trace out the in/reflected slot
        (a, b), (cc, d) = r
        return [[a + s * s * d, c * b], [c * cc, c * c * d]]

    def E(r):
        return [[r[0][0], F(0)], [F(0), r[1][1]]]

    units = [[[F(int((i, j) == (p, q))) for j in range(2)] for i in range(2)] for p in range(2) for q in range(2)]
    for r in units:
        assert phi(E(r)) == E(phi(r))
    rho = [[F(2, 3), F(1, 5)], [F(1, 5), F(1, 3)]]
    out = phi(rho)
    assert out[1][1] == F(9, 25) * rho[1][1]                         # occupation carried with Gamma = c^2
    assert out[0][0] + out[1][1] == 1
    # the transmitted coherence is scaled by c, not erased: the channel is covariant without being the descent
    assert out[0][1] == F(3, 25) and phi(rho) != E(phi(rho))
    return True
