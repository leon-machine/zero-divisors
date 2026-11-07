"""synthesis.phase-flow-is-time-rotor-flow-kms-continuation: exact checks.

Clifford level (GA.py, Fractions): the frame *-structure of the tower (x* = x for Q(x) = 1,
x* = -x for Q(x) = -1, reversed order), the form E(x, y) = <x y*>_0 on vectors, and for fixed
rational bivectors B in Cl(1,1), Cl(2,2), Cl(3,3), Cl(1,3), Cl(3,1), Cl(2,4): the E-adjoint of
ad_B is ad_{B*}; the compact part is E-antisymmetric; the atom boost sigma = v*v - vv* is
*-symmetric with ad-weights -2, +2 on v, v*; its rotor at e^{lambda/2} = 2 scales v, v* by 1/4, 4
and is not a *-map.

Fock level (Jordan-Wigner matrices over Q): the rotor flow at common rapidity sends an even
thermofield pair to a functional negative on some X*X, for three rapidities; at rapidity beta the
rotor flow is the KMS swap of the Gibbs state of K = N - 1/2 for three values of e^{beta/2}; the
pairing generator with boost detuning has (ad_H)^2 = Omega^2 on (a1, a2*), so the unitary flow
is trigonometric with transfer at most g^2/Omega^2 and the real-parameter flow hyperbolic; a
gauge-invariant hop commutes with the total boost.
"""
import itertools
from fractions import Fraction as F
import GA
import fock
from GA import mul, add, sub, scal, sc, gen
from tp_premise import premise


# ------------------------------------------------------------------ Clifford level
def star(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b)
        s = F(-1) ** (g * (g - 1) // 2)
        for i in b:
            if sq[i] == -1:
                s = -s
        out[b] = s * c
    return {b: c for b, c in out.items() if c != 0}


def ad(B, x, sq):
    return sub(mul(B, x, sq), mul(x, B, sq))


def ad_matrix(B, sq):
    n = len(sq)
    M = [[F(0)] * n for _ in range(n)]
    for j in range(n):
        for b, c in ad(B, gen(j), sq).items():
            assert len(b) == 1
            M[b[0]][j] = c
    return M


def transpose(M):
    return [list(r) for r in zip(*M)]


def E(x, y, sq):
    return mul(x, star(y, sq), sq).get((), F(0))


# fixed rational test data (no sampling): bivector coefficients and vector components
COEFFS = [F(3, 2), F(-2), F(1, 3), F(5, 4), F(-1, 2), F(2, 3), F(-7, 4), F(1), F(-3, 5), F(4),
          F(-5, 3), F(1, 4), F(3), F(-1, 3), F(7, 2)]
VECS = [F(2), F(-1), F(3), F(1, 2), F(-3), F(1), F(-2, 3), F(5)]
# (number of compact bivectors, number of boost bivectors) = (C(p,2) + C(q,2), p q)
COUNTS = {(1, 1): (0, 1), (2, 2): (2, 4), (3, 3): (6, 9), (1, 3): (3, 3), (3, 1): (3, 3),
          (2, 4): (7, 8)}


def check_star_adjoint_and_compact_part():
    premise("tower.structure-tower-c-norms")
    premise("scrambling.clock-inventory-boundary-modes")
    for (p, q) in [(1, 1), (2, 2), (3, 3), (1, 3), (3, 1), (2, 4)]:
        sq = GA.sig(p, q)
        n = p + q
        # the frame is E-orthonormal, so E is positive definite on V
        for i in range(n):
            for j in range(n):
                assert E(gen(i), gen(j), sq) == (1 if i == j else 0)
        biv = list(itertools.combinations(range(n), 2))
        compact = [b for b in biv if star({b: F(1)}, sq) == {b: F(-1)}]
        boost = [b for b in biv if star({b: F(1)}, sq) == {b: F(1)}]
        assert (len(compact), len(boost)) == COUNTS[(p, q)]
        for (i, j) in biv:
            B = {(i, j): F(1)}
            assert star(B, sq) == (scal(-1, B) if sq[i] == sq[j] else B)
            # ad_{e_i e_j} e_j = 2 Q(e_j) e_i and ad_{e_i e_j} e_i = -2 Q(e_i) e_j
            assert ad(B, gen(j), sq) == scal(2 * sq[j], gen(i))
            assert ad(B, gen(i), sq) == scal(-2 * sq[i], gen(j))
        for shift in range(5):
            B = {b: COEFFS[(shift + 3 * k) % len(COEFFS)] for k, b in enumerate(biv)}
            M = ad_matrix(B, sq)
            assert transpose(M) == ad_matrix(star(B, sq), sq)          # E-adjoint of ad_B is ad_{B*}
            Bc = {b: c for b, c in B.items() if b in compact}
            Bh = {b: c for b, c in B.items() if b in boost}
            assert add(Bc, Bh) == B and star(Bc, sq) == scal(-1, Bc) and star(Bh, sq) == Bh
            Mc = ad_matrix(Bc, sq)
            assert transpose(Mc) == [[-x for x in r] for r in Mc]        # compact part: antisymmetric
            Mh = ad_matrix(Bh, sq)
            assert transpose(Mh) == Mh                                   # boost part: symmetric
            assert (Mh == [[F(0)] * n for _ in range(n)]) == (Bh == {})
            # the identity E(ad_B x, y) = E(x, ad_{B*} y) on fixed vectors
            x = {(k,): VECS[(shift + k) % len(VECS)] for k in range(n)}
            y = {(k,): VECS[(shift + 2 * k + 1) % len(VECS)] for k in range(n)}
            assert E(ad(B, x, sq), y, sq) == E(x, ad(star(B, sq), y, sq), sq)
    return True


def check_atom_boost_rotor_not_star():
    premise("field-theory.boost-modes")
    premise("tower.structure-tower-c-norms")
    sq = GA.sig(1, 1)
    v = scal(F(1, 2), add(gen(0), gen(1)))
    vs = star(v, sq)
    assert mul(v, v, sq) == {} and add(mul(v, vs, sq), mul(vs, v, sq)) == sc(1)
    sigma = sub(mul(vs, v, sq), mul(v, vs, sq))
    assert mul(sigma, sigma, sq) == sc(1) and star(sigma, sq) == sigma
    assert ad(sigma, v, sq) == scal(-2, v) and ad(sigma, vs, sq) == scal(2, vs)
    # R = exp(lambda sigma / 2) with e^{lambda/2} = 2: cosh = 5/4, sinh = 3/4
    R = add(sc(F(5, 4)), scal(F(3, 4), sigma))
    Ri = add(sc(F(5, 4)), scal(F(-3, 4), sigma))
    assert mul(R, Ri, sq) == sc(1)
    al = lambda x: mul(mul(R, x, sq), Ri, sq)
    assert al(v) == scal(F(1, 4), v) and al(vs) == scal(4, vs)
    assert star(al(v), sq) != al(star(v, sq))
    assert star(R, sq) == R and mul(star(R, sq), R, sq) != sc(1)        # R is *-symmetric, not unitary
    return True


# ------------------------------------------------------------------ Fock level
mm = GA.mat_mul


def T(A):
    return [list(r) for r in zip(*A)]


def madd(*Ms):
    return [[sum(x) for x in zip(*rows)] for rows in zip(*Ms)]


def msc(c, A):
    return [[c * x for x in r] for r in A]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def comm(X, Y):
    return madd(mm(X, Y), msc(-1, mm(Y, X)))


a1, a2 = [fock.to_dense(fock.ann(k, 2, fock.MSB), 4) for k in range(2)]   # Jordan-Wigner annihilators
c1, c2 = T(a1), T(a2)
I4 = eye(4)


def expect(psi, Y):
    return sum(psi[i] * Y[i][j] * psi[j] for i in range(4) for j in range(4))


def check_rotor_flow_not_positive():
    premise("field-theory.boost-modes")
    for X, Y in [(a1, c1), (a2, c2)]:
        assert madd(mm(X, Y), mm(Y, X)) == I4
    assert madd(mm(a1, a2), mm(a2, a1)) == msc(0, I4) and madd(mm(a1, c2), mm(c2, a1)) == msc(0, I4)
    n1n2 = mm(mm(c2, c1), mm(a1, a2))
    for (x, c, s) in [(F(4), F(4, 5), F(3, 5)), (F(2), F(12, 13), F(5, 13)),
                      (F(11, 10), F(899, 901), F(60, 901))]:
        # x = e^{2 lambda}; the rotor flow a_j -> e^{-lambda} a_j sends a1 a2 -> a1 a2 / x,
        # a2* a1* -> x a2* a1*, n1 n2 -> n1 n2. X = a1 a2 - t, alpha(X* X) = alpha(X*) alpha(X).
        assert c * c + s * s == 1
        psi = [c, F(0), F(0), s]                       # even pure state c|00> + s|11>
        eps = expect(psi, mm(a1, a2)) / (c * s)
        assert eps in (1, -1)
        ch = (x + 1 / x) / 2                           # cosh(2 lambda)
        t = eps * c * s * ch
        aXX = madd(n1n2, msc(-t * x, mm(c2, c1)), msc(-t / x, mm(a1, a2)), msc(t * t, I4))
        val = expect(psi, aXX)
        assert val == s * s * (1 - c * c * ch * ch) and val < 0
        XX = madd(n1n2, msc(-t, mm(c2, c1)), msc(-t, mm(a1, a2)), msc(t * t, I4))
        assert expect(psi, XX) >= 0                    # at lambda = 0 the same functional is positive
    return True


def check_rotor_at_beta_is_kms_swap():
    premise("singularity.kms-uniqueness-factor")
    premise("singularity.euclidean-rotor-where-it-lies")
    units = [[[F(int((i, j) == (r, s))) for j in range(2)] for i in range(2)] for r in range(2) for s in range(2)]
    for y in [F(2), F(3, 2), F(7, 5)]:
        # K = N - 1/2 = diag(-1/2, 1/2); e^{-beta K} = diag(y, 1/y), y = e^{beta/2}
        S = [[y, F(0)], [F(0), 1 / y]]
        Si = [[1 / y, F(0)], [F(0), y]]
        Zp = tr(S)
        for A in units:
            for B in units:
                lhs = tr(mm(S, mm(A, mm(S, mm(B, Si))))) / Zp      # omega(A Ad(e^{-beta K})(B))
                rhs = tr(mm(S, mm(B, A))) / Zp                     # omega(B A)
                assert lhs == rhs
        # the occupation of the Gibbs state, 1/(y^2 + 1), at the three sample points
        Nop = [[F(0), F(0)], [F(0), F(1)]]
        assert tr(mm(S, Nop)) / Zp == {F(2): F(1, 5), F(3, 2): F(4, 13), F(7, 5): F(25, 74)}[y]
        # control: the rotor at any other rapidity (y' = 2y) is not the KMS swap of this state
        S2 = [[2 * y, F(0)], [F(0), 1 / (2 * y)]]
        S2i = [[1 / (2 * y), F(0)], [F(0), 2 * y]]
        A, B = units[1], units[2]                                    # matrix units e_01, e_10
        assert tr(mm(S, mm(A, mm(S2, mm(B, S2i))))) != tr(mm(S, mm(B, A)))
    return True


def check_detuned_pairing_and_hop():
    premise("rungs.imported-fock-representation-bogoliubov-group")
    Ktot = madd(mm(c1, a1), mm(c2, a2), msc(-1, I4))          # n1 + n2 - 1
    W = madd(mm(c1, c2), mm(a2, a1))                            # pairing, self-adjoint
    assert W == T(W)
    for (kap, g, Om) in [(F(3), F(4), F(5)), (F(5), F(12), F(13)), (F(0), F(1), F(1))]:
        H = madd(msc(kap, Ktot), msc(g, W))
        assert H == T(H)
        # ad_H on (a1, a2*)
        assert comm(H, a1) == madd(msc(-kap, a1), msc(-g, c2))
        assert comm(H, c2) == madd(msc(-g, a1), msc(kap, c2))
        M = [[-kap, -g], [-g, kap]]
        assert mm(M, M) == msc(Om * Om, eye(2))
        # unitary flow: exp(i t M) = cos(Om t) + i sin(Om t) M/Om; weight moved to a2*: (g/Om)^2 sin^2 <= (g/Om)^2
        bound = (g / Om) ** 2
        assert bound <= 1 and (kap == 0 or bound < 1)
        for (co, si) in [(F(3, 5), F(4, 5)), (F(0), F(1)), (F(5, 13), F(12, 13))]:
            w_a1 = co * co + (si * kap / Om) ** 2                  # |cos - i sin(-kap)/Om|^2
            w_a2 = (si * g / Om) ** 2
            assert w_a1 + w_a2 == 1 and w_a2 <= bound
    # a gauge-invariant hop commutes with the total boost: the boost contributes a common phase only
    Hop = madd(mm(c1, a2), mm(c2, a1))
    Ktot = madd(mm(c1, a1), mm(c2, a2), msc(-1, I4))
    assert comm(Ktot, Hop) == msc(0, I4)
    assert comm(Ktot, a1) == msc(-1, a1) and comm(Ktot, a2) == msc(-1, a2)
    return True


# ------------------------------------------------------------------ added in the fix round
def check_conjugated_clocks_not_star():
    """Clause (ii) beyond the atom: clocks conjugated by boost rotors in Cl(2,2) keep a real
    nonzero ad-eigenvalue, carry a nonzero boost part, and ad_X is not E-antisymmetric."""
    premise("scrambling.clock-inventory-boundary-modes")
    premise("tower.structure-tower-c-norms")
    sq = GA.sig(2, 2)                                   # e0, e1 square +1; e2, e3 square -1
    sigma = {(0, 2): F(1)}                              # an atom boost (mixed plane)
    v = add(gen(0), gen(2))                             # null eigenvector of ad_sigma
    lam = [c for c in [F(2), F(-2)] if ad(sigma, v, sq) == scal(c, v)]
    assert lam
    rotors = []
    for (i, j) in [(1, 2), (1, 3), (0, 3)]:             # mixed planes: boost rotors
        B = {(i, j): F(1)}
        assert mul(B, B, sq) == sc(1)
        rotors.append((add(sc(F(5, 4)), scal(F(3, 4), B)), add(sc(F(5, 4)), scal(F(-3, 4), B))))
    for (i, j) in [(0, 1), (2, 3)]:                     # compact planes: rotations
        B = {(i, j): F(1)}
        assert mul(B, B, sq) == sc(-1)
        rotors.append((add(sc(F(3, 5)), scal(F(4, 5), B)), add(sc(F(3, 5)), scal(F(-4, 5), B))))
    for R, Ri in rotors:
        assert mul(R, Ri, sq) == sc(1)
        X = mul(mul(R, sigma, sq), Ri, sq)
        x = mul(mul(R, v, sq), Ri, sq)
        assert all(len(b) == 2 for b in X) and all(len(b) == 1 for b in x)
        assert ad(X, x, sq) == scal(lam[0], x)          # real nonzero eigenvalue survives
        Xb = {b: c for b, c in X.items() if sq[b[0]] != sq[b[1]]}
        assert Xb != {} and star(X, sq) != scal(-1, X)
        assert E(ad(X, x, sq), x, sq) != -E(x, ad(X, x, sq), sq)
        # the first-order *-compatibility fails on some generator: (ad_X g)* != ad_X(g*)
        assert any(star(ad(X, gen(k), sq), sq) != ad(X, star(gen(k), sq), sq) for k in range(4))
    return True


def check_pairing_flow_exponentiated():
    """Clause (iii) by an exact one-parameter group: on the Fock space of two modes,
    H = kappa (N1 + N2 - 1) + g (a1* a2* + a2 a1) is zero on the odd sector and has square
    Omega^2 on the even sector, so e^{itH} = cos(Omega t) P_even + i sin(Omega t) H / Omega + P_odd.
    At rational points (cos, sin) the script builds e^{itH} over Q(i), checks the group law and
    unitarity, evolves a1 by conjugation and compares with exp(i t ad_H) on (a1, a2*)."""
    premise("rungs.imported-fock-representation-bogoliubov-group")
    from GA import QI

    def q(x):
        return x if isinstance(x, QI) else QI(x)

    def qmm(A, B):
        return [[sum((q(A[i][l]) * q(B[l][j]) for l in range(len(B))), QI(0)) for j in range(len(B[0]))]
                for i in range(len(A))]

    def qadd(*Ms):
        return [[sum((q(x) for x in t), QI(0)) for t in zip(*rows)] for rows in zip(*Ms)]

    def qsc(c, A):
        return [[q(c) * q(x) for x in r] for r in A]

    def dag(A):
        return [[q(A[j][i]).conj() for j in range(len(A))] for i in range(len(A[0]))]

    I = QI(0, 1)
    Ktot = madd(mm(c1, a1), mm(c2, a2), msc(-1, I4))
    W = madd(mm(c1, c2), mm(a2, a1))
    Peven = [[F(int(i == j and i in (0, 3))) for j in range(4)] for i in range(4)]
    Podd = [[F(int(i == j and i in (1, 2))) for j in range(4)] for i in range(4)]
    for (kap, g, Om) in [(F(3), F(4), F(5)), (F(5), F(12), F(13))]:
        H = madd(msc(kap, Ktot), msc(g, W))
        assert mm(H, Podd) == msc(0, I4)
        assert mm(H, H) == msc(Om * Om, Peven)
        def U(co, si):
            return qadd(qsc(co, Peven), qsc(I * si / Om, H), Podd)
        pts = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(-7, 25), F(24, 25))]
        for (co, si) in pts:
            Ut = U(co, si)
            assert qmm(Ut, dag(Ut)) == qadd(I4, msc(0, I4))                  # unitary
            for (co2, si2) in pts:                                           # group law
                assert qmm(Ut, U(co2, si2)) == U(co * co2 - si * si2, si * co2 + co * si2)
            evolved = qmm(qmm(Ut, a1), dag(Ut))                              # e^{itH} a1 e^{-itH}
            c_a1 = QI(co, -kap * si / Om)
            c_a2 = QI(0, -g * si / Om)
            assert evolved == qadd(qsc(c_a1, a1), qsc(c_a2, c2))
            w2 = c_a2 * c_a2.conj()
            assert (c_a1 * c_a1.conj() + w2) == QI(1) and w2.re <= (g / Om) ** 2
        assert U(F(1), F(0)) == qadd(I4, msc(0, I4))
    return True
