"""field-theory.where-each-lives: exact checks in the blade engine (real Clifford algebras, Fraction).

Cl(1,3): gamma_0..3 with squares (1, -1, -1, -1); Cl(2,4) adds e_+ (square +1) and e_- (square -1)
as generators 4, 5. I4 = gamma_0123, E = e_+ e_-, I6 = gamma_0123 e_+ e_-.
(1) The centres of Cl+(1,3) and Cl+(2,4), computed as the common kernel of the commutators with all
even bivectors: span{1, I4} and span{1, I6}; I4^2 = I6^2 = -1, I6 = I4 E, E^2 = 1, [I4, E] = 0.
(2) A reversion-invariant idempotent P = (1 + Q1)(1 + Q2)/4 (commuting 4-blades of square 1) gives
CS = Cl+(2,4) P of real dimension 8; Cl+(2,4) acts faithfully (32 independent 8 x 8 matrices, so
Cl+(2,4) = Mat_4(C) and CS = C^4, a minimal left ideal: sample nonzero elements generate all of CS).
The commutant of the action, computed as a kernel (64 unknowns), is span{1, I6}; an element
a + b I6 squares to -1 iff a = 0, b = +-1 (checked on the exact multiplication table of the
commutant basis), so the complex unit of CS is +-I6.
(3) The E = +1 and E = -1 eigenspaces L0, Linf of CS have real dimension 4 each, CS = L0 + Linf,
both are preserved by Lorentz rotors (boost, rotation, a product), and I6 = +I4 on L0, -I4 on Linf;
L0 = ker n_0 and Linf = ker n_inf in CS (n_0 = (e_- - e_+)/2, n_inf = e_+ + e_-).
(4) Massless fields in Cl(1,3): the null bivectors annihilated by k = gamma_0 + gamma_3 form an
I4-stable 2-dimensional space, and a rotation about gamma_3 acts on them as cos + h sin I4 with one
sign h: on the Maxwell sectors (f, g = -+I4 f) the complex structure J is +-I4 by helicity. Weyl: the
even phi with k phi = 0 form a 4-dimensional space; on Hestenes' positive-frequency solutions J is
right multiplication by I sigma_3 = gamma_2 gamma_1, and the chiral subspaces I4 phi = +-phi I sigma_3
(2 + 2) are exactly where J = +-I4. A mass term anticommutes with I4: right multiplication by
gamma_0 (the Dirac-Hestenes mass term) anticommutes with J = right I4 on even phi, and I4
anticommutes with the mass datum I4 gamma_3.
EXPORTS: twistor_data() (cached P, bases of the even and odd halves, helpers) for dependent checks.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import mul, add, sub, neg, sc, gen, reverse, eq, is_zero, commutes, anticommutes, all_blades

S4 = (1, -1, -1, -1)
S6 = (1, -1, -1, -1, 1, -1)
ALLB6 = all_blades(6)
ALLB4 = all_blades(4)


def blade(t):
    return {tuple(t): F(1)}


def scl(c, x):
    c = F(c)
    return {b: c * v for b, v in x.items()} if c != 0 else {}


def comm(x, y, s):
    return sub(mul(x, y, s), mul(y, x, s))


def vec(x, blades):
    return [x.get(b, F(0)) for b in blades]


def from_vec(c, elems):
    out = {}
    for ci, e in zip(c, elems):
        if ci != 0:
            out = add(out, scl(ci, e))
    return out


def span_rank(elems, blades):
    return GA.rank_of_vectors([vec(e, blades) for e in elems]) if elems else 0


def kernel_of_images(imgs, basis):
    """Combinations of basis whose images (list, same order) vanish."""
    allb = sorted({bb for im in imgs for bb in im})
    if not allb:
        return list(basis)
    rows = [[im.get(bb, F(0)) for im in imgs] for bb in allb]
    return [from_vec(v, basis) for v in GA.field_kernel(rows)]


def coords(y, elems, blades):
    """Coordinates of y in the span of the independent elems (exact), or None."""
    n = len(elems)
    rows = [[e.get(b, F(0)) for e in elems] + [-y.get(b, F(0))] for b in blades]
    for v in GA.field_kernel(rows):
        if v[n] != 0:
            return [a / v[n] for a in v[:n]]
    return None


def even_blades(n):
    return [b for b in all_blades(n) if len(b) % 2 == 0]


def centre_of_even(n, s):
    eb = even_blades(n)
    basis = [blade(b) for b in eb]
    rows = []
    for B in [blade(b) for b in eb if len(b) == 2]:
        imgs = [comm(x, B, s) for x in basis]
        allb = sorted({bb for im in imgs for bb in im})
        rows += [[im.get(bb, F(0)) for im in imgs] for bb in allb]
    return [from_vec(v, basis) for v in GA.field_kernel(rows)]


_CACHE = {}


def twistor_data():
    """P, the even half S = Cl+(2,4) P and the odd half S' = Cl-(2,4) P (bases), cached."""
    if _CACHE:
        return _CACHE
    eb = even_blades(6)
    g4 = [blade(b) for b in eb if len(b) == 4 and eq(mul(blade(b), blade(b), S6), sc(1))]
    P = None
    for Q1, Q2 in combinations(g4, 2):
        if not commutes(Q1, Q2, S6):
            continue
        PP = mul(scl(F(1, 2), add(sc(1), Q1)), scl(F(1, 2), add(sc(1), Q2)), S6)
        if eq(mul(PP, PP, S6), PP) and eq(reverse(PP), PP):
            if span_rank([mul(blade(b), PP, S6) for b in eb], ALLB6) == 8:
                P = PP
                break

    def basis_of(blist):
        out = []
        for b in blist:
            c = mul(blade(b), P, S6)
            if span_rank(out + [c], ALLB6) > len(out):
                out.append(c)
        return out

    ob = [b for b in all_blades(6) if len(b) % 2 == 1]
    _CACHE.update(P=P, S=basis_of(eb), Sodd=basis_of(ob), S6=S6, ALLB6=ALLB6, blade=blade, scl=scl,
                  span_rank=span_rank, coords=coords, kernel_of_images=kernel_of_images,
                  I4=blade((0, 1, 2, 3)), I6=blade((0, 1, 2, 3, 4, 5)), E=blade((4, 5)))
    return _CACHE


EXPORTS = {"twistor_data": twistor_data}

LORENTZ = [(F(5, 4), F(3, 4), (0, 1)), (F(3, 5), F(4, 5), (1, 2)), (F(13, 5), F(12, 5), (0, 3))]


def rotor(c, s, b):
    return add(sc(c), scl(s, blade(b)))


def check_centres_and_I6():
    I4, I6, E = blade((0, 1, 2, 3)), blade((0, 1, 2, 3, 4, 5)), blade((4, 5))
    Z4 = centre_of_even(4, S4)
    assert len(Z4) == 2 and span_rank(Z4 + [sc(1), I4], ALLB4) == 2
    Z6 = centre_of_even(6, S6)
    assert len(Z6) == 2 and span_rank(Z6 + [sc(1), I6], ALLB6) == 2
    assert eq(mul(I4, I4, S4), sc(-1)) and eq(mul(I6, I6, S6), sc(-1))
    assert eq(I6, mul(I4, E, S6)) and eq(mul(E, E, S6), sc(1)) and commutes(I4, E, S6)
    # I4 is not central in Cl+(2,4): it anticommutes with the mixed bivectors gamma_mu e_+-
    assert not commutes(I4, blade((0, 4)), S6)


def check_conformal_spinor_ideal_and_commutant():
    d = twistor_data()
    P, S, I6 = d["P"], d["S"], d["I6"]
    assert P is not None and len(S) == 8
    eb = even_blades(6)

    def lmat(a):
        cols = [coords(mul(a, z, S6), S, ALLB6) for z in S]
        return [[cols[j][i] for j in range(8)] for i in range(8)]

    mats = [lmat(blade(b)) for b in eb]
    assert GA.rank_of_vectors([[x for r in M for x in r] for M in mats]) == 32
    # minimality: sample nonzero elements generate all of CS
    for z in (S[0], add(S[1], scl(3, S[5])), sub(S[2], S[7])):
        assert span_rank([mul(blade(b), z, S6) for b in eb], ALLB6) == 8
    gens = [lmat(blade(b)) for b in eb if len(b) == 2]
    rows = []
    for G in gens:
        for i in range(8):
            for j in range(8):
                r = [F(0)] * 64
                for k in range(8):
                    r[8 * i + k] += G[k][j]
                    r[8 * k + j] -= G[i][k]
                rows.append(r)
    com = GA.field_kernel(rows)
    LI6 = lmat(I6)
    Id = [[F(1) if i == j else F(0) for j in range(8)] for i in range(8)]
    assert len(com) == 2
    assert GA.rank_of_vectors(com + [[x for r in Id for x in r], [x for r in LI6 for x in r]]) == 2
    # (a + b J)^2 = (a^2 - b^2) + 2ab J with J^2 = -1: = -1 iff a = 0, b = +-1
    J2 = GA.mat_mul(LI6, LI6)
    assert J2 == [[-x for x in r] for r in Id]
    for a, b in ((F(0), F(1)), (F(0), F(-1)), (F(1), F(1)), (F(0), F(2)), (F(1, 2), F(0))):
        M = [[a * Id[i][j] + b * LI6[i][j] for j in range(8)] for i in range(8)]
        sq = GA.mat_mul(M, M)
        is_unit = sq == [[-x for x in r] for r in Id]
        assert is_unit == (a == 0 and b * b == 1)


def check_two_chiral_doublets():
    d = twistor_data()
    S, I4, I6, E = d["S"], d["I4"], d["I6"], d["E"]
    Lp = kernel_of_images([sub(mul(E, z, S6), z) for z in S], S)
    Lm = kernel_of_images([add(mul(E, z, S6), z) for z in S], S)
    assert len(Lp) == 4 and len(Lm) == 4 and span_rank(Lp + Lm, ALLB6) == 8
    for c, s, b in LORENTZ:
        R = rotor(c, s, b)
        assert eq(mul(R, reverse(R), S6), sc(1))
        for z in Lp:
            assert eq(mul(E, mul(R, z, S6), S6), mul(R, z, S6))
        for z in Lm:
            assert eq(mul(E, mul(R, z, S6), S6), neg(mul(R, z, S6)))
    assert all(eq(mul(I6, z, S6), mul(I4, z, S6)) for z in Lp)
    assert all(eq(mul(I6, z, S6), neg(mul(I4, z, S6))) for z in Lm)
    n0 = scl(F(1, 2), sub(gen(5), gen(4)))
    ninf = add(gen(4), gen(5))
    K0 = kernel_of_images([mul(n0, z, S6) for z in S], S)
    Kinf = kernel_of_images([mul(ninf, z, S6) for z in S], S)
    assert len(K0) == 4 and span_rank(K0 + Lp, ALLB6) == 4
    assert len(Kinf) == 4 and span_rank(Kinf + Lm, ALLB6) == 4


def check_massless_complex_structure_is_pseudoscalar():
    I4 = blade((0, 1, 2, 3))
    k = add(gen(0), gen(3))
    B4 = [blade(b) for b in combinations(range(4), 2)]
    EV4 = [blade(b) for b in ALLB4 if len(b) % 2 == 0]
    Kf = kernel_of_images([mul(k, b, S4) for b in B4], B4)
    assert len(Kf) == 2 and all(coords(mul(I4, f, S4), Kf, ALLB4) is not None for f in Kf)
    c, s = F(3, 5), F(4, 5)
    R, Ri = rotor(c, s, (1, 2)), rotor(c, -s, (1, 2))
    cth, sth = c * c - s * s, 2 * c * s
    hs = set()
    for f in Kf:
        rf = mul(mul(R, f, S4), Ri, S4)
        found = [h for h in (1, -1) if eq(rf, add(scl(cth, f), scl(h * sth, mul(I4, f, S4))))]
        assert len(found) == 1
        hs.add(found[0])
        # Maxwell sectors (f, g): J (f, g) = (-g, f) equals +I4 on g = -I4 f and -I4 on g = +I4 f
        for sign in (1, -1):
            g = scl(-sign, mul(I4, f, S4))
            J = (neg(g), f)
            D = (scl(sign, mul(I4, f, S4)), scl(sign, mul(I4, g, S4)))
            assert eq(J[0], D[0]) and eq(J[1], D[1])
    assert len(hs) == 1
    # Weyl: even phi with k phi = 0
    Kp = kernel_of_images([mul(k, p, S4) for p in EV4], EV4)
    assert len(Kp) == 4
    Is3 = {(1, 2): F(-1)}
    assert eq(Is3, mul(I4, mul(gen(3), gen(0), S4), S4)) and eq(mul(Is3, Is3, S4), sc(-1))
    halves = []
    for sign in (1, -1):
        Cs = kernel_of_images([sub(mul(I4, p, S4), scl(sign, mul(p, Is3, S4))) for p in Kp], Kp)
        halves.append(Cs)
        for p in Cs:
            chi = neg(mul(p, Is3, S4))
            J = (neg(chi), p)                        # J = right multiplication by I sigma_3
            assert eq(J[0], mul(p, Is3, S4)) and eq(J[1], mul(chi, Is3, S4))
            D = (mul(I4, p, S4), mul(I4, chi, S4))
            assert eq(J[0], scl(sign, D[0])) and eq(J[1], scl(sign, D[1]))
    assert len(halves[0]) == 2 and len(halves[1]) == 2 and span_rank(halves[0] + halves[1], ALLB4) == 4
    # mass: right gamma_0 anticommutes with J = right I4 on even phi; I4 anticommutes with I4 gamma_3
    for p in EV4:
        assert eq(mul(mul(p, I4, S4), gen(0), S4), neg(mul(mul(p, gen(0), S4), I4, S4)))
    assert anticommutes(I4, gen(0), S4) and anticommutes(I4, mul(I4, gen(3), S4), S4)
