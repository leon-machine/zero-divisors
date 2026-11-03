"""synthesis.light-cone-koide-is-quarter-turn: exact checks over Q(i) (pairs of Fractions).

Face space C^3 with the bracket form C(v) = sum v_k^2, P_s = J/3, P_d = 1 - P_s. D_{a,b} = a P_s + b P_d.
"""
from fractions import Fraction as F
from tp_premise import premise
from GA import congruence_signature

# ---- Gaussian rationals ------------------------------------------------------------------
def g(re, im=0): return (F(re), F(im))
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def mul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def conj(x): return (x[0], -x[1])
def inv(x):
    n = x[0] * x[0] + x[1] * x[1]
    return (x[0] / n, -x[1] / n)
ZERO, ONE, I = g(0), g(1), g(0, 1)


def vadd(u, v): return [add(a, b) for a, b in zip(u, v)]
def vscal(s, v): return [mul(s, a) for a in v]
def vconj(v): return [conj(a) for a in v]
def bil(u, v):
    t = ZERO
    for a, b in zip(u, v):
        t = add(t, mul(a, b))
    return t
def Ps(v):
    m = mul(g(F(1, 3)), add(add(v[0], v[1]), v[2]))
    return [m, m, m]
def Pd(v): return [sub(a, b) for a, b in zip(v, Ps(v))]
def D(a, b, v): return vadd(vscal(a, Ps(v)), vscal(b, Pd(v)))
def sigma(x, y, v):
    vb = vconj(v)
    return vadd(vscal(x, Ps(vb)), vscal(y, Pd(vb)))
def real_vec(xs): return [g(t) for t in xs]


REALS = [real_vec(t) for t in ([1, 0, 0], [0, 1, 0], [0, 0, 1], [3, -1, 2], [F(1, 2), 5, F(-7, 3)],
                               [2, 2, 2], [1, -1, 0])]
CPLX = [[g(1, 2), g(0, -1), g(F(3, 4), 5)], [I, g(2), g(-1, F(1, 3))]] + REALS


def check_quarter_turn_conjugacy():
    """Every C-compatible S3-equivariant real structure sigma_{x,y} (x, y = +-1) is D sigma_{1,1} D^-1
    with D = a P_s + b P_d, a, b in {1, i}, x = a/conj(a), y = b/conj(b); and C(D v) = a^2 s^2 + b^2 Q(d)
    on real v (s^2 = C(P_s v), Q(d) = C(P_d v)). In particular C o D_{1,i} = q = s^2 - Q(d)."""
    premise("families.chart-computation-sign-twist-bracket-form")
    premise("families.koide-nullity-condition-one-member-invariant")
    premise("synthesis.coherent-face-vector-real-slices")
    seen = set()
    for a in (ONE, I):
        for b in (ONE, I):
            x, y = mul(a, inv(conj(a))), mul(b, inv(conj(b)))
            ai, bi = inv(a), inv(b)
            for v in CPLX:
                # D sigma_0 D^-1 v == sigma_{x,y} v
                lhs = D(a, b, vconj(D(ai, bi, v)))
                assert lhs == sigma(x, y, v)
            for v in REALS:
                s2, d2 = bil(Ps(v), Ps(v)), bil(Pd(v), Pd(v))
                assert bil(Ps(v), Pd(v)) == ZERO
                assert bil(D(a, b, v), D(a, b, v)) == add(mul(mul(a, a), s2), mul(mul(b, b), d2))
            seen.add((x, y))
            # the slice D(R^3): C restricted to it, in the basis D e_k, is a real symmetric matrix
            G = [[bil(D(a, b, REALS[i]), D(a, b, REALS[j])) for j in range(3)] for i in range(3)]
            assert all(z[1] == 0 for row in G for z in row)
            sig = congruence_signature([[z[0] for z in row] for row in G])
            exp = {(ONE, ONE): (3, 0, 0), (ONE, I): (1, 2, 0), (I, ONE): (2, 1, 0), (I, I): (0, 3, 0)}[(a, b)]
            assert sig == exp
    assert seen == {(ONE, ONE), (ONE, g(-1)), (g(-1), ONE), (g(-1), g(-1))}
    # discrimination: D with b = (1+i) is not C-compatible: C(D v) is not real on real v
    v = REALS[3]
    z = bil(D(ONE, g(1, 1), v), D(ONE, g(1, 1), v))
    assert z[1] != 0


def check_physical_vector_never_null():
    """C(v) does not depend on any real structure: for a face vector with real components it is
    sum v_k^2 > 0, so the physical sqrt(m) vector is C-null on no slice; its quarter-turned image
    D_{1,i} v is C-null exactly when q(v) = 0 (Koide)."""
    premise("families.chart-computation-sign-twist-bracket-form")
    premise("families.koide-nullity-condition-one-member-invariant")
    for v in REALS:
        n = bil(v, v)
        assert n[1] == 0 and n[0] == sum(t[0] * t[0] for t in v) and n[0] > 0
    # Koide on the physical vector is q(v) = 0, and q = C o D_{1,i}: the quarter-turned image is C-null
    # exactly when the physical vector is q-null.
    for v in REALS:
        q = sub(bil(Ps(v), Ps(v)), bil(Pd(v), Pd(v)))
        Dv = D(ONE, I, v)
        assert bil(Dv, Dv) == q
        assert (bil(Dv, Dv) == ZERO) == (q == ZERO)
    for v in REALS:
        Dv = D(ONE, I, v)
        assert sigma(ONE, g(-1), Dv) == Dv
        if bil(Pd(v), Pd(v)) != ZERO:
            assert bil(Dv, Dv) != bil(v, v)


# ---- 3x3 complex matrices -------------------------------------------------------------------
def mz(): return [[ZERO] * 3 for _ in range(3)]
def mmul(A, B):
    C = mz()
    for i in range(3):
        for j in range(3):
            t = ZERO
            for k in range(3):
                t = add(t, mul(A[i][k], B[k][j]))
            C[i][j] = t
    return C
def madd(A, B): return [[add(A[i][j], B[i][j]) for j in range(3)] for i in range(3)]
def msub(A, B): return [[sub(A[i][j], B[i][j]) for j in range(3)] for i in range(3)]
def mscal(s, A): return [[mul(s, A[i][j]) for j in range(3)] for i in range(3)]
def mdag(A): return [[conj(A[j][i]) for j in range(3)] for i in range(3)]
def tr(A): return add(add(A[0][0], A[1][1]), A[2][2])
def eye(): return [[ONE if i == j else ZERO for j in range(3)] for i in range(3)]
def diag(xs): return [[g(xs[i]) if i == j else ZERO for j in range(3)] for i in range(3)]
def comm(A, B): return msub(mmul(A, B), mmul(B, A))
def theta(X):                                   # -X^dagger + (2/3) conj(tr X) 1
    return madd(mscal(g(-1), mdag(X)), mscal(mul(g(F(2, 3)), conj(tr(X))), eye()))
def Dmat(A):                                    # A -> (tr A / 3) 1 + i A_0
    t = mscal(mul(g(F(1, 3)), tr(A)), eye())
    return madd(t, mscal(I, msub(A, t)))


def unitary_from(K):
    """Cayley transform U = (1 - K)(1 + K)^-1 of an anti-Hermitian K: exactly unitary over Q(i)."""
    A = msub(eye(), K)
    B = madd(eye(), K)
    # invert B by Gauss-Jordan over Q(i)
    M = [B[i][:] + eye()[i][:] for i in range(3)]
    for c in range(3):
        p = next(r for r in range(c, 3) if M[r][c] != ZERO)
        M[c], M[p] = M[p], M[c]
        iv = inv(M[c][c])
        M[c] = [mul(iv, z) for z in M[c]]
        for r in range(3):
            if r != c and M[r][c] != ZERO:
                f = M[r][c]
                M[r] = [sub(M[r][k], mul(f, M[c][k])) for k in range(6)]
    Binv = [row[3:] for row in M]
    return mmul(A, Binv)


KS = [[[g(0, 1), g(2, -1), g(0, F(1, 2))], [g(-2, -1), g(0, -3), g(1)], [g(0, F(1, 2)), g(-1), g(0, 2)]],
      [[g(0, F(1, 3)), g(1, 1), g(0)], [g(-1, 1), g(0), g(F(-2, 5), 3)], [g(0), g(F(2, 5), 3), g(0, -1)]]]


def check_basis_free_angle_and_lie_real_form():
    """For A = U diag(lambda) U^dagger Hermitian: tr A = sum lambda, tr A^2 = sum lambda^2, so
    cos^2(theta) = (tr A)^2 / (3 tr A^2) is the face-space angle of the eigenvalue vector to u whatever
    the eigenbasis. D(A) = (tr A/3) 1 + i A_0 lies in the real form R 1 + su(3) (fixed set of theta, an
    antilinear involutive Lie automorphism of gl(3, C)) and tr(D(A)^2) = (tr A)^2/3 - tr(A_0^2), the
    light-cone member; tr(X^2) has signature (1, 8) on R 1 + su(3) and (9, 0) on Herm(3)."""
    premise("families.koide-nullity-condition-one-member-invariant")
    premise("families.chart-computation-sign-twist-bracket-form")
    lams = [[1, 4, 9], [F(1, 2), -3, 7], [2, 2, 5]]
    for K in KS:
        assert madd(K, mdag(K)) == mz()
        U = unitary_from(K)
        assert mmul(U, mdag(U)) == eye()
        assert any(U[i][j] != ZERO for i in range(3) for j in range(3) if i != j)   # non-diagonal
        for lam in lams:
            A = mmul(mmul(U, diag(lam)), mdag(U))
            assert mdag(A) == A
            assert tr(A) == g(sum(lam)) and tr(mmul(A, A)) == g(sum(t * t for t in lam))
            # face-space data of the eigenvalue vector: s^2 = (sum)^2/3, Q(d) = sum sq - s^2
            v = real_vec(lam)
            assert bil(Ps(v), Ps(v)) == mul(g(F(1, 3)), mul(tr(A), tr(A)))
            X = Dmat(A)
            assert theta(X) == X
            A0 = msub(A, mscal(mul(g(F(1, 3)), tr(A)), eye()))
            lhs = tr(mmul(X, X))
            rhs = sub(mul(g(F(1, 3)), mul(tr(A), tr(A))), tr(mmul(A0, A0)))
            assert lhs == rhs
            q = sub(bil(Ps(v), Ps(v)), bil(Pd(v), Pd(v)))
            assert lhs == q                                   # = q of the eigenvalue vector
    # theta: antilinear involution and Lie automorphism
    for X in KS + [diag([1, 2, 3]), mscal(g(1, 2), KS[0])]:
        assert theta(theta(X)) == X
        for Y in KS:
            assert theta(comm(X, Y)) == comm(theta(X), theta(Y))
    # real bases and signatures of tr(XY)
    def E(i, j):
        M = mz(); M[i][j] = ONE; return M
    fixed = [eye(), mscal(I, msub(E(0, 0), E(1, 1))), mscal(I, msub(E(1, 1), E(2, 2)))]
    herm = [eye(), msub(E(0, 0), E(1, 1)), msub(E(1, 1), E(2, 2))]
    for i, j in ((0, 1), (0, 2), (1, 2)):
        fixed += [msub(E(i, j), E(j, i)), mscal(I, madd(E(i, j), E(j, i)))]
        herm += [madd(E(i, j), E(j, i)), mscal(I, msub(E(i, j), E(j, i)))]
    for basis, exp, inv_map in ((fixed, (1, 8, 0), theta), (herm, (9, 0, 0), mdag)):
        for X in basis:
            assert inv_map(X) == X
        G = [[tr(mmul(X, Y)) for Y in basis] for X in basis]
        assert all(z[1] == 0 for row in G for z in row)
        assert congruence_signature([[z[0] for z in row] for row in G]) == exp


def sqrt_interval(x, steps=120):
    lo, hi = F(0), max(F(1), x)
    for _ in range(steps):
        m = (lo + hi) / 2
        if m * m <= x:
            lo = m
        else:
            hi = m
    return lo, hi


def koide_interval(r):
    """Interval for Q = sum r_k^2 / (sum r_k)^2 from intervals r_k = (lo, hi) of signed roots."""
    num_lo = sum(min(a * a, b * b) if a * b > 0 else F(0) for a, b in r)
    num_hi = sum(max(a * a, b * b) for a, b in r)
    s_lo, s_hi = sum(a for a, b in r), sum(b for a, b in r)
    assert s_lo * s_hi > 0
    den_lo, den_hi = min(s_lo * s_lo, s_hi * s_hi), max(s_lo * s_lo, s_hi * s_hi)
    return num_lo / den_hi, num_hi / den_lo


def check_angle_selects_positive_root():
    """Every positive semidefinite H is A^2 for Hermitian A, with 2^3 choices of A when the spectrum is
    simple; the Koide angle of A depends on the choice. On the charged-lepton masses (m_tau over its
    stored range) only the positive root gives Q within 10^-5 of 2/3; each mixed-sign root is more than
    3/100 above it."""
    premise("families.alignment-computed-thirteenth-refutation-democracy-one")
    premise("families.koide-nullity-condition-one-member-invariant")
    # exact model: H = U diag(1, 16, 81) U^dagger, roots A = U diag(+-1, +-4, +-9) U^dagger
    U = unitary_from(KS[0])
    H = mmul(mmul(U, diag([1, 16, 81])), mdag(U))
    Qs = set()
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                A = mmul(mmul(U, diag([s1 * 1, s2 * 4, s3 * 9])), mdag(U))
                assert mmul(A, A) == H
                t = tr(A)
                Qs.add(tr(mmul(A, A))[0] / (t[0] * t[0]))
    assert Qs == {F(98, 196), F(98, 144), F(98, 36), F(98, 16)}
    assert H[0][1] == (F(32450, 4289), F(5950, 4289)) and H[0][0] == (F(24249, 4289), F(0))
    # charged leptons (MeV): m_tau = 1776.93 +- 0.09 as stored (families.linear-conjecture-refuted-data),
    # evaluated at the central value and both ends; m_e, m_mu PDG central values.
    # Each entry: floor(10^6 Q) for the root with the given signs, the interval of Q being narrower
    # than 10^-6 so that lo and hi share it.
    premise("families.linear-conjecture-refuted-data")
    me, mmu = F('0.51099895'), F('105.6583755')
    table = {'1776.84': {(1, 1, 1): 666659, (-1, 1, 1): 704027, (1, -1, 1): 1773072, (1, 1, -1): 1939516},
             '1776.93': {(1, 1, 1): 666664, (-1, 1, 1): 704032, (1, -1, 1): 1773041, (1, 1, -1): 1939476},
             '1777.02': {(1, 1, 1): 666669, (-1, 1, 1): 704036, (1, -1, 1): 1773009, (1, 1, -1): 1939436}}
    for mtau, rows in table.items():
        roots = [sqrt_interval(m) for m in (me, mmu, F(mtau))]
        for signs, fl in rows.items():
            r = [(s * a, s * b) if s > 0 else (s * b, s * a) for s, (a, b) in zip(signs, roots)]
            lo, hi = koide_interval(r)
            assert fl * F(1, 10 ** 6) <= lo and hi < (fl + 1) * F(1, 10 ** 6)
            if signs == (1, 1, 1):
                assert abs(lo - F(2, 3)) < F(1, 10 ** 5) and abs(hi - F(2, 3)) < F(1, 10 ** 5)
            else:
                assert lo - F(2, 3) > F(3, 100)
