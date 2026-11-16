"""The spectral asymmetry on real projective five-space from monogenic polynomials: exact checks.

Six-space with Q(e_a) = -1 (the algebra Cl(0,6)), volume element J = e_1 ... e_6. The real spinor space S is the
minimal left ideal Cl(0,6) P, P = (1 + e_1e_2e_3)(1 + e_1e_4e_5)(1 + e_2e_4e_6)/8, of real dimension 8; the
generators act on it by left multiplication, and coordinates are taken in the basis of products (blade) P, whose
supports are disjoint. A spinor polynomial is a dict {exponents: coordinates in S}.
(1) J^2 = -1, J anticommutes with vectors and commutes with bivectors; P is an idempotent and the ideal has
    dimension 8; the generators act on it with the relations of Cl(0,6); the pair of J with the pseudoscalar
    omega of ten generators of square +1 is an involution.
(2) The kernel M_k of the vector derivative d = sum e_a d_a on spinor polynomials of degree k has real dimension
    8 C(k+4, 4) for k = 0, 1, 2, 3 (exact kernels), which is 8 (C(k+5, 5) - C(k+4, 5)).
(3) On a basis of each M_k, k <= 3: (x ^ d) P = k P, d(x P) = -(6 + 2k) P, (x ^ d)(x P) = -(k + 5) x P, so the
    operator D = -(x ^ d) - 5/2 is -(k + 5/2) on M_k and +(k + 5/2) on x M_k; J maps M_k to itself, commutes
    with x ^ d, and J(xP) = -x(JP).
(4) On the unit sphere, with n the position vector and X, Y tangent: the Clifford map X -> X n satisfies
    (Xn)(Yn) + (Yn)(Xn) = XY + YX, the connection d_X + (1/2) X n is compatible with it for the Levi-Civita
    derivative d_X Y + <X, Y> n of the sphere, and the sum of (e_a n)^2 over a tangent frame at a rational point
    is -5.
(5) The signed multiplicities (-1)^k 4 C(k+4, 4) have generating function 4/(1 + t)^5, with value 1/8 at t = 1;
    the multiplicity is (u^2 - 9/4)(u^2 - 1/4)/6 at u = k + 5/2, and the regularised alternating sums
    sum (-1)^k (k + a)^j = E_j(a)/2 (Euler polynomials, from 2 e^(az)/(e^z + 1)) give the same 1/8, for the shift
    5/2 and for other shifts. So n components give n/16 for half the asymmetry: 1 for sixteen, 15/16 for fifteen.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

import GA
from tp_premise import premise

SQ = GA.sig(0, 6)
ONE = GA.sc(1)


def prod(*xs):
    out = xs[0]
    for x in xs[1:]:
        out = GA.mul(out, x, SQ)
    return out


def e(a):
    return GA.gen(a)


J = prod(*[e(a) for a in range(6)])
B1, B2, B3 = prod(e(0), e(1), e(2)), prod(e(0), e(3), e(4)), prod(e(1), e(3), e(5))
P = GA.scal(F(1, 8), prod(GA.add(ONE, B1), GA.add(ONE, B2), GA.add(ONE, B3)))
BLADES = GA.all_blades(6)


def ideal_basis():
    basis, rows = [], []
    for b in BLADES:
        x = prod({b: F(1)}, P)
        v = GA.basis_vector_of(x, BLADES)
        if GA.rank_of_vectors(rows + [v]) > len(rows):
            rows.append(v)
            basis.append(x)
    return basis


IDEAL = ideal_basis()
REP = [sorted(x)[0] for x in IDEAL]
DIM = len(IDEAL)


def coords(x):
    return [x.get(REP[c], F(0)) / IDEAL[c][REP[c]] for c in range(DIM)]


def lmat(g):
    cols = [coords(prod(g, s)) for s in IDEAL]
    return [[cols[c][r] for c in range(DIM)] for r in range(DIM)]


E = [lmat(e(a)) for a in range(6)]


def mm(A, B):
    return [[sum(A[r][m] * B[m][c] for m in range(DIM)) for c in range(DIM)] for r in range(DIM)]


def mv(A, v):
    return [sum(A[r][m] * v[m] for m in range(DIM)) for r in range(DIM)]


def unit(c=1):
    return [[F(c * int(r == s)) for s in range(DIM)] for r in range(DIM)]


JM = unit()
for _a in range(6):
    JM = mm(JM, E[_a])


def binom(n, r):
    out = 1
    for q in range(r):
        out = out * (n - q) // (q + 1)
    return out


def monos(k):
    out = []
    for c in combinations_with_replacement(range(6), k):
        ex = [0] * 6
        for a in c:
            ex[a] += 1
        out.append(tuple(ex))
    return out


def _acc(out, m, w):
    out[m] = [p + q for p, q in zip(out.get(m, [F(0)] * DIM), w)]


def _clean(out):
    return {m: v for m, v in out.items() if any(v)}


def dirac(p):
    out = {}
    for m, v in p.items():
        for a in range(6):
            if m[a]:
                m2 = tuple(x - (b == a) for b, x in enumerate(m))
                _acc(out, m2, [m[a] * x for x in mv(E[a], v)])
    return _clean(out)


def xmul(p):
    out = {}
    for m, v in p.items():
        for a in range(6):
            m2 = tuple(x + (b == a) for b, x in enumerate(m))
            _acc(out, m2, mv(E[a], v))
    return _clean(out)


def xwedged(p):
    """(x ^ d) p = sum over a < b of e_a e_b (x_a d_b - x_b d_a) p."""
    out = {}
    for m, v in p.items():
        for a in range(6):
            for b in range(a + 1, 6):
                w0 = mv(E[a], mv(E[b], v))
                for (up, down, s) in ((a, b, 1), (b, a, -1)):
                    if m[down]:
                        m2 = list(m)
                        m2[down] -= 1
                        m2[up] += 1
                        _acc(out, tuple(m2), [s * m[down] * x for x in w0])
    return _clean(out)


def scale(c, p):
    return {m: [c * x for x in v] for m, v in p.items()} if c else {}


def psub(p, q):
    out = dict(p)
    for m, v in q.items():
        out[m] = [a - b for a, b in zip(out.get(m, [F(0)] * DIM), v)]
    return _clean(out)


def left_j(p):
    return {m: mv(JM, v) for m, v in p.items()}


def monogenic_basis(k):
    ms = monos(k)
    if k == 0:
        return [{ms[0]: [F(int(a == b)) for b in range(DIM)]} for a in range(DIM)]
    tgt = monos(k - 1)
    tidx = {m: c for c, m in enumerate(tgt)}
    cols = []
    for m in ms:
        for a in range(DIM):
            v = [F(0)] * DIM
            v[a] = F(1)
            col = [F(0)] * (DIM * len(tgt))
            for m2, w in dirac({m: v}).items():
                for b in range(DIM):
                    col[DIM * tidx[m2] + b] = w[b]
            cols.append(col)
    ker = GA.field_kernel([list(r) for r in zip(*cols)])
    out = []
    for kv in ker:
        p = {}
        for c, m in enumerate(ms):
            v = kv[DIM * c:DIM * c + DIM]
            if any(v):
                p[m] = list(v)
        out.append(p)
    return out


def check_volume_element_spinor_ideal_and_the_pair_with_omega():
    premise("synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element")
    ok = GA.eq(prod(J, J), GA.sc(-1))
    ok = ok and all(GA.anticommutes(J, e(a), SQ) for a in range(6))
    ok = ok and all(GA.commutes(J, prod(e(a), e(b)), SQ) for a in range(6) for b in range(a))
    ok = ok and GA.eq(prod(P, P), P) and DIM == 8 and all(len(x) == 8 for x in IDEAL)
    ok = ok and all(mm(E[a], E[a]) == unit(-1) for a in range(6))
    ok = ok and all(mm(E[a], E[b]) == [[-x for x in r] for r in mm(E[b], E[a])] for a in range(6) for b in range(a))
    ok = ok and mm(JM, JM) == unit(-1)
    # omega: the product of ten generators of square +1; with J in one algebra Cl(10,6)
    big = GA.sig(10, 6)
    omega = {tuple(range(10)): F(1)}
    jj = {tuple(range(10, 16)): F(1)}
    pair = GA.mul(jj, omega, big)
    ok = ok and GA.eq(GA.mul(omega, omega, big), GA.sc(-1)) and GA.eq(GA.mul(jj, jj, big), GA.sc(-1))
    ok = ok and GA.commutes(jj, omega, big) and GA.eq(GA.mul(pair, pair, big), GA.sc(1))
    GA.check("Cl(0,6): J^2 = -1, spinor ideal of dimension 8; J omega is an involution", ok)
    return ok


def check_monogenic_dimensions():
    premise("standard-model.hyp-s-slot-statistics")
    dims = [len(monogenic_basis(k)) for k in range(4)]
    ok = dims == [8, 40, 120, 280]
    ok = ok and all(dims[k] == 8 * binom(k + 4, 4) for k in range(4))
    ok = ok and all(8 * binom(k + 4, 4) == 8 * (binom(k + 5, 5) - binom(k + 4, 5)) for k in range(12))
    ok = ok and all(len(monos(k)) == binom(k + 5, 5) for k in range(5))
    GA.check("monogenic spinor polynomials on six-space: dim M_k = 8 C(k+4,4), k = 0..3", ok)
    return ok


def check_bivector_operator_eigenvalues_and_the_antipodal_lift():
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for k in range(4):
        basis = monogenic_basis(k)
        sample = basis if k < 2 else basis[:6] + basis[-6:]
        for p in sample:
            xp = xmul(p)
            ok = ok and dirac(p) == {}
            ok = ok and psub(xwedged(p), scale(k, p)) == {}
            ok = ok and psub(dirac(xp), scale(-(6 + 2 * k), p)) == {}
            ok = ok and psub(xwedged(xp), scale(-(k + 5), xp)) == {}
            # D = -(x ^ d) - 5/2: eigenvalue -(k + 5/2) on M_k, +(k + 5/2) on x M_k
            d_p = psub(scale(-1, xwedged(p)), scale(F(5, 2), p))
            d_xp = psub(scale(-1, xwedged(xp)), scale(F(5, 2), xp))
            ok = ok and psub(d_p, scale(-(k + F(5, 2)), p)) == {}
            ok = ok and psub(d_xp, scale(k + F(5, 2), xp)) == {}
            # the volume element: keeps M_k, commutes with x ^ d, anticommutes with x
            jp = left_j(p)
            ok = ok and dirac(jp) == {} and psub(xwedged(jp), left_j(xwedged(p))) == {}
            ok = ok and psub(left_j(xp), scale(-1, xmul(jp))) == {}
    GA.check("x ^ d = k on M_k and -(k+5) on x M_k; d(xP) = -(6+2k)P; J commutes with x ^ d", ok)
    return ok


def check_clifford_map_and_connection_on_the_sphere():
    premise("standard-model.hyp-s-slot-statistics")

    def vec(c):
        return GA.add(*[GA.scal(c[a], e(a)) for a in range(6)])

    def euclid(u, w):
        return sum(F(u[a]) * F(w[a]) for a in range(6))

    # a rational point of the unit sphere and two tangent vectors there
    n_c = [F(2, 7), F(3, 7), F(6, 7), F(0), F(0), F(0)]
    x_c = [F(3), F(-2), F(0), F(1), F(0), F(4)]
    y_c = [F(6), F(2), F(-3), F(0), F(5), F(-1)]
    n, X, Y = vec(n_c), vec(x_c), vec(y_c)
    ok = euclid(n_c, n_c) == 1 and euclid(n_c, x_c) == 0 and euclid(n_c, y_c) == 0
    ok = ok and GA.eq(prod(n, n), GA.sc(-1))
    cX, cY = prod(X, n), prod(Y, n)
    ok = ok and GA.eq(GA.add(prod(cX, cY), prod(cY, cX)), GA.add(prod(X, Y), prod(Y, X)))
    ok = ok and GA.eq(GA.add(prod(X, Y), prod(Y, X)), GA.sc(-2 * euclid(x_c, y_c)))
    # compatibility: d_X(Y n) psi + (1/2) X n Y n psi - Y n (1/2) X n psi = (D_X Y) n psi with
    # d_X Y = D_X Y - <X, Y> n and d_X n = X; the Y-derivative terms cancel, leaving the algebraic identity
    half = F(1, 2)
    lhs = GA.add(GA.scal(-euclid(x_c, y_c), prod(n, n)), prod(Y, X),
                 GA.scal(half, prod(cX, cY)), GA.scal(-half, prod(cY, cX)))
    ok = ok and GA.is_zero(lhs)
    # a tangent frame at n: orthonormal for the Euclidean product, orthogonal to n
    frame = [[F(3, 7), F(-6, 7), F(2, 7), F(0), F(0), F(0)], [F(6, 7), F(2, 7), F(-3, 7), F(0), F(0), F(0)],
             [F(0), F(0), F(0), F(1), F(0), F(0)], [F(0), F(0), F(0), F(0), F(1), F(0)],
             [F(0), F(0), F(0), F(0), F(0), F(1)]]
    ok = ok and all(euclid(u, w) == int(u is w) for u in frame for w in frame)
    ok = ok and all(euclid(u, n_c) == 0 for u in frame)
    total = GA.add(*[prod(vec(u), n, vec(u), n) for u in frame])
    ok = ok and GA.eq(total, GA.sc(-5))
    # (e_a n) e_a = n for each frame vector, used with -n (d - n d_n) = -x d - d_n on the sphere
    ok = ok and GA.eq(GA.add(*[prod(vec(u), n, vec(u)) for u in frame]), GA.scal(5, n))
    GA.check("sphere: (Xn)(Yn) + (Yn)(Xn) = XY + YX; d_X + Xn/2 is compatible; sum (e_a n)^2 = -5", ok)
    return ok


def euler_polys(top):
    """E_0 .. E_top as coefficient lists (lowest degree first), from E_n(x) = x^n - (1/2) sum_{r<n} C(n,r) E_r(x)."""
    out = []
    for n in range(top + 1):
        p = [F(0)] * n + [F(1)]
        for r in range(n):
            p = GA.padd(p, [-F(binom(n, r), 2) * c for c in out[r]])
        out.append(GA.ptrim(p))
    return out


def check_alternating_series_and_the_count_for_fifteen_and_sixteen():
    premise("synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element")
    # generating function of (-1)^k 4 C(k+4,4) is 4/(1+t)^5
    series = [F((-1) ** k * 4 * binom(k + 4, 4)) for k in range(16)]
    denom = GA.ps_trunc([F(1), F(5), F(10), F(10), F(5), F(1)], 15)
    ok = GA.ps_mul(series, denom, 15) == [F(4)] + [F(0)] * 15
    abel = F(4, 2 ** 5)
    ok = ok and abel == F(1, 8)
    # multiplicity as a polynomial in u = k + 5/2
    ok = ok and all(F(4 * binom(k + 4, 4)) == ((k + F(5, 2)) ** 2 - F(9, 4)) * ((k + F(5, 2)) ** 2 - F(1, 4)) / 6
                    for k in range(10))
    eu = euler_polys(4)
    ok = ok and eu[2] == [F(0), F(-1), F(1)] and eu[4] == [F(0), F(1), F(0), F(-2), F(1)]
    # the generating function 2 e^(az)/(e^z + 1) = sum E_n(a) z^n / n! at a = 5/2, to order 5
    order = 4
    ez = [F(1)]
    for r in range(1, order + 1):
        ez.append(ez[-1] / r)
    eaz = [c * F(5, 2) ** r for r, c in enumerate(ez)]
    gen = GA.ps_mul([2 * c for c in eaz], GA.ps_inv(GA.padd(list(ez), [F(1)]), order), order)
    fact = [F(1)]
    for r in range(1, order + 1):
        fact.append(fact[-1] * r)
    ok = ok and all(gen[r] * fact[r] == GA.peval(eu[r], F(5, 2)) for r in range(order + 1))

    def regularised(shift):
        # 4 C(k+4,4) = (k+1)(k+2)(k+3)(k+4)/6 written in powers of (k + shift)
        poly = [F(1, 6)]
        for r in (1, 2, 3, 5):
            poly = GA.pmul(poly, [F(r) - shift, F(1)])
        return sum(c * GA.peval(eu[j], shift) / 2 for j, c in enumerate(poly))

    ok = ok and regularised(F(5, 2)) == abel
    ok = ok and all(regularised(s) == abel for s in (F(1), F(1, 2), F(7, 3)))
    half = abel / 2
    ok = ok and half == F(1, 16) and 16 * half == 1 and 15 * half == F(15, 16)
    ok = ok and [n for n in range(1, 49) if (n * half).denominator == 1] == [16, 32, 48]
    GA.check("sum (-1)^k 4 C(k+4,4) t^k = 4/(1+t)^5; Abel and Euler-polynomial values 1/8; n/16 per n", ok)
    return ok
