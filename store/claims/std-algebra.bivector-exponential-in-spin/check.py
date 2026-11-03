from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def _fact(k):
    out = 1
    for j in range(2, k + 1):
        out *= j
    return out


def _binom(m, j):
    return _fact(m) // (_fact(j) * _fact(m - j))


def _bv(sq, terms):
    return {tuple(b): F(c) for b, c in terms}


# non-simple bivectors (B ^ B != 0), sampled across signatures, degenerate included
GENERAL = [
    ((4, 0, 0), [((0, 1), 2), ((2, 3), 3), ((0, 2), 1)]),
    ((1, 3, 0), [((0, 1), 1), ((2, 3), 2), ((0, 3), -1), ((1, 2), 1)]),
    ((2, 2, 0), [((0, 2), 1), ((1, 3), -2), ((0, 1), 1)]),
    ((3, 2, 0), [((0, 3), -1), ((1, 2), -1), ((1, 3), 1), ((3, 4), 1), ((0, 4), 2)]),
    ((2, 1, 1), [((0, 1), 1), ((2, 3), 1), ((0, 3), 2)]),
    ((3, 0, 2), [((0, 1), 1), ((2, 3), 1), ((1, 4), -1)]),
    ((0, 0, 4), [((0, 1), 1), ((2, 3), 1)]),
]

# non-simple nilpotent bivectors of nondegenerate spaces: the exponential series terminates
NILPOTENT = [
    ((2, 4, 0), [((0, 2), -1), ((1, 4), -1), ((2, 5), 1), ((3, 4), 1)], 3),
    ((2, 4, 0), [((0, 1), -1), ((0, 4), 1), ((0, 5), 1), ((2, 5), 1)], 4),
    ((3, 2, 0), [((0, 3), -1), ((1, 2), -1), ((1, 3), 1), ((3, 4), 1)], 4),
    ((3, 3, 0), [((0, 1), 1), ((0, 4), 1), ((2, 5), 1), ((3, 5), 1)], 3),
]


def _exp_terminating(B, sq, k):
    out, P = GA.sc(1), GA.sc(1)
    for j in range(1, k):
        P = GA.mul(P, B, sq)
        out = GA.add(out, GA.scal(F(1, _fact(j)), P))
    return out


def _vector_image_matrix(R, sq):
    """Columns: R e_i R^{-1} for R with R R~ = 1 (so R^{-1} = R~)."""
    n = len(sq)
    cols = []
    for i in range(n):
        y = GA.mul(GA.mul(R, GA.gen(i), sq), GA.reverse(R), sq)
        if S.grades(y) not in ([1], []):
            return None
        cols.append([y.get((j,), F(0)) for j in range(n)])
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def _apply(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v))), F(0)) for i in range(len(M))]


def _bil(u, v, sq):
    return sum((F(s) * a * b for s, a, b in zip(sq, u, v)), F(0))


def _reflect_matrix(u, sq):
    n = len(sq)
    qu = _bil(u, u, sq)
    cols = []
    for j in range(n):
        e = [F(int(i == j)) for i in range(n)]
        c = 2 * _bil(e, u, sq) / qu
        cols.append([e[i] - c * u[i] for i in range(n)])
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def _reflections(M, sq):
    """Exact Cartan-Dieudonne factorisation of an isometry M of a diagonal nondegenerate form:
    returns u_1, ..., u_k with M = s_{u_1} ... s_{u_k}."""
    n = len(sq)
    us = []
    cur = [row[:] for row in M]
    for i in range(n):
        x = [F(int(j == i)) for j in range(n)]
        y = _apply(cur, x)
        if y == x:
            continue
        d = [a - b for a, b in zip(y, x)]
        if _bil(d, d, sq) != 0:
            steps = [d]
        else:
            s = [a + b for a, b in zip(y, x)]
            steps = [s, x]
        for u in steps:
            cur = GA.mat_mul(_reflect_matrix(u, sq), cur)
            us.append(u)
    ident = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    return us if GA.mat_eq(cur, ident) else None


def check_series_identities_for_general_bivectors():
    """Order by order in the series: e^B e^-B = 1 (Cauchy product), (B^k)~ = (-B)^k, and
    e^B x e^-B = e^{ad_B} x with ad_B(V) in V skew-adjoint, for non-simple and degenerate B."""
    premise("std-algebra.involution-properties")
    premise("std-algebra.bivector-lie-algebra")
    ok = True
    terms = 0
    for (p, q, r), tb in GENERAL:
        sq = GA.sig(p, q, r)
        n = len(sq)
        B = _bv(sq, tb)
        ok = ok and S.grades(B) == [2]
        ok = ok and S.grade(GA.mul(B, B, sq), 4) != {}
        mB = GA.neg(B)
        pw, mpw = [GA.sc(1)], [GA.sc(1)]
        for k in range(1, 8):
            pw.append(GA.mul(pw[-1], B, sq))
            mpw.append(GA.mul(mpw[-1], mB, sq))
            ok = ok and GA.eq(GA.reverse(pw[k]), mpw[k])
        for m in range(1, 8):
            tot = {}
            for j in range(m + 1):
                tot = GA.add(tot, GA.scal(F(1, _fact(j) * _fact(m - j)), GA.mul(pw[j], mpw[m - j], sq)))
            ok = ok and tot == {}
            terms += 1
        for i in range(n):
            x = GA.gen(i)
            ad = x
            for m in range(1, 7):
                ad = GA.sub(GA.mul(B, ad, sq), GA.mul(ad, B, sq))
                ok = ok and S.grades(ad) in ([1], [])
                lhs = {}
                for j in range(m + 1):
                    lhs = GA.add(lhs, GA.scal(_binom(m, j), GA.mul(GA.mul(pw[j], x, sq), mpw[m - j], sq)))
                ok = ok and GA.eq(lhs, ad)
                terms += 1
            # skew-adjointness of ad_B on V: B(ad x, y) + B(x, ad y) = 0
            for j in range(n):
                y = GA.gen(j)
                ady = GA.sub(GA.mul(B, y, sq), GA.mul(y, B, sq))
                adx = GA.sub(GA.mul(B, x, sq), GA.mul(x, B, sq))
                ok = ok and GA.dot(adx, y, sq) + GA.dot(x, ady, sq) == 0
    ok = ok and terms == 7 * 7 + 6 * sum(sum(s) for s, _ in GENERAL)
    GA.check("series identities for non-simple bivectors: e^B e^-B = 1, (e^B)~ = e^-B, "
             "e^B x e^-B = e^{ad_B} x in V, ad_B skew (7 signatures, degenerate included)", ok)
    return ok


def _qscal(c, x):
    return {b: c * v for b, v in x.items() if c * v != 0}


def check_series_identities_over_the_complex_numbers():
    """The same identities with complex coefficients (Gaussian rationals): a non-simple complex
    bivector of Cl(V_C), V_C = C^4 with an orthonormal basis, and of the complexified Cl(2,4)."""
    premise("std-algebra.involution-properties")
    premise("std-algebra.bivector-lie-algebra")
    ok = True
    i_ = GA.QI(0, 1)
    cases = [
        ((1, 1, 1, 1), {(0, 1): GA.QI(1), (2, 3): i_, (0, 2): GA.QI(1, 1)}),
        (GA.sig(2, 4), {(0, 1): GA.QI(2), (2, 3): GA.QI(0, -1), (4, 5): GA.QI(1, 2), (0, 5): i_}),
    ]
    count = 0
    for sq, B in cases:
        n = len(sq)
        B2 = GA.mul(B, B, sq)
        ok = ok and S.grade(B2, 4) != {}
        mB = GA.neg(B)
        pw, mpw = [{(): GA.QI(1)}], [{(): GA.QI(1)}]
        for k in range(1, 7):
            pw.append(GA.mul(pw[-1], B, sq))
            mpw.append(GA.mul(mpw[-1], mB, sq))
            ok = ok and GA.eq(GA.reverse(pw[k]), mpw[k])
        for m in range(1, 7):
            tot = {}
            for j in range(m + 1):
                tot = GA.add(tot, _qscal(GA.QI(F(1, _fact(j) * _fact(m - j))), GA.mul(pw[j], mpw[m - j], sq)))
            ok = ok and GA.is_zero(tot)
            count += 1
        for idx in range(n):
            x = {(idx,): GA.QI(1)}
            ad = x
            for m in range(1, 6):
                ad = GA.sub(GA.mul(B, ad, sq), GA.mul(ad, B, sq))
                ok = ok and S.grades(ad) in ([1], [])
                lhs = {}
                for j in range(m + 1):
                    lhs = GA.add(lhs, _qscal(GA.QI(_binom(m, j)), GA.mul(GA.mul(pw[j], x, sq), mpw[m - j], sq)))
                ok = ok and GA.eq(lhs, ad)
                count += 1
    ok = ok and count == 6 + 6 + 5 * 4 + 5 * 6
    GA.check("over C (QI): e^B e^-B = 1, (e^B)~ = e^-B, e^B x e^-B = e^{ad_B} x in V_C, order by order", ok)
    return ok


def check_terminating_exponentials_are_spin_plus():
    """Non-simple nilpotent bivectors of Cl(2,4), Cl(3,2), Cl(3,3): e^B is a finite sum, a rotor,
    acts on V by an isometry, and equals +- a product of an even number of invertible vectors
    whose squares multiply to +1 after scaling, found by an exact Cartan-Dieudonne factorisation."""
    premise("std-algebra.cartan-dieudonne")
    premise("primer.twisted-adjoint-action")
    premise("primer.centre")
    ok = True
    lengths = []
    for (p, q, r), tb, k in NILPOTENT:
        sq = GA.sig(p, q, r)
        n = len(sq)
        B = _bv(sq, tb)
        ok = ok and S.grade(GA.mul(B, B, sq), 4) != {}
        Bk = GA.sc(1)
        for _ in range(k):
            Bk = GA.mul(Bk, B, sq)
        ok = ok and Bk == {}
        R = _exp_terminating(B, sq, k)
        ok = ok and GA.eq(GA.mul(R, GA.reverse(R), sq), GA.sc(1))
        ok = ok and all(len(b) % 2 == 0 for b in R)
        M = _vector_image_matrix(R, sq)
        ok = ok and M is not None
        if M is None:
            continue
        # isometry
        for i in range(n):
            for j in range(n):
                ci = [M[a][i] for a in range(n)]
                cj = [M[a][j] for a in range(n)]
                ok = ok and _bil(ci, cj, sq) == (sq[i] if i == j else 0)
        us = _reflections(M, sq)
        ok = ok and us is not None
        if us is None:
            continue
        g = GA.sc(1)
        prodq = F(1)
        for u in us:
            g = GA.mul(g, S.vec(u), sq)
            prodq *= _bil(u, u, sq)
        ok = ok and len(us) % 2 == 0 and prodq != 0
        # R g^{-1} commutes with every vector, so is central and even: a scalar lam
        ginv = GA.scal(F(1) / prodq, GA.reverse(g))
        lam = GA.mul(R, ginv, sq)
        ok = ok and S.grades(lam) == [0]
        lv = lam.get((), F(0))
        # R R~ = lam^2 g g~ = lam^2 prod Q(u_i) = 1: so prod Q(u_i) > 0 and R is in Spin+
        ok = ok and lv * lv * prodq == 1 and prodq > 0
        ok = ok and GA.eq(R, GA.scal(lv, g))
        lengths.append(len(us))
    ok = ok and len(lengths) == 4
    GA.check("terminating e^B for non-simple nilpotent B in Cl(2,4), Cl(3,2), Cl(3,3): rotor, "
             "isometry, = lam u1...u2j with lam^2 prod Q(u_i) = 1, prod Q(u_i) > 0", ok)
    return ok


def check_lorentzian_rotors_and_the_non_exponential():
    """Cl(1,3): even scalars span(1, I) are central in the even part with I^2 = -1; every bivector
    squares into them; C(z)^2 - z S(z)^2 = 1 as power series; -(1 + N) for a null bivector N is a
    rotor with scalar-pseudoscalar part -1 and F^2 = 0; -1 = e^{pi g1 g2} needs no exception."""
    premise("primer.sign")
    premise("primer.centre")
    premise("std-algebra.bivector-exponential")
    ok = True
    sq = GA.sig(1, 3)
    I = S.pseudoscalar(4)
    ok = ok and GA.eq(GA.mul(I, I, sq), GA.sc(-1))
    for b in GA.all_blades(4):
        if len(b) % 2 == 0:
            ok = ok and GA.commutes(I, {b: F(1)}, sq)
        else:
            ok = ok and GA.anticommutes(I, {b: F(1)}, sq)
    for seed in range(1, 7):
        Bs = S.sample(4, seed, grades_=(2,))
        ok = ok and set(S.grades(GA.mul(Bs, Bs, sq))) <= {0, 4}
    # C(z) = sum z^k/(2k)!, S(z) = sum z^k/(2k+1)!: C^2 - z S^2 = 1 to order 12
    N = 12
    C = [F(1, _fact(2 * k)) for k in range(N + 1)]
    Sz = [F(1, _fact(2 * k + 1)) for k in range(N + 1)]
    C2 = GA.ps_mul(C, C, N)
    zS2 = [F(0)] + GA.ps_mul(Sz, Sz, N)[:N]
    ok = ok and [a - b for a, b in zip(C2, zS2)] == [F(1)] + [F(0)] * N
    # the non-exponential rotor: R = -(1 + N), N = (g0 + g1) g2, null
    n_ = S.vec([1, 1, 0, 0])
    Nb = GA.mul(n_, GA.gen(2), sq)
    ok = ok and S.grades(Nb) == [2] and GA.mul(Nb, Nb, sq) == {}
    R = GA.neg(GA.add(GA.sc(1), Nb))
    ok = ok and GA.eq(GA.mul(R, GA.reverse(R), sq), GA.sc(1))
    s_part = GA.add(S.grade(R, 0), S.grade(R, 4))
    ok = ok and GA.eq(s_part, GA.sc(-1))
    # R is a product of six unit vectors with prod Q = +1: R = (g1 g3 g1 g3)(-g2)(g2 + n)
    a1, a2 = GA.gen(1), GA.gen(3)
    w = GA.add(GA.gen(2), n_)
    fac = GA.mul(GA.mul(GA.mul(a1, a2, sq), GA.mul(a1, a2, sq), sq), GA.mul(GA.neg(GA.gen(2)), w, sq), sq)
    ok = ok and GA.eq(fac, R)
    ok = ok and GA.dot(w, w, sq) == -1 and GA.dot(GA.gen(2), GA.gen(2), sq) == -1
    # -(1 + N) = -e^{N} and 1 + N = e^{N} since N^2 = 0; -1 alone is e^{pi g1 g2}: (g1 g2)^2 = -1
    g12 = S.blade(1, 2)
    ok = ok and GA.eq(GA.mul(g12, g12, sq), GA.sc(-1))
    GA.check("Cl(1,3): span(1, I) central in the even part, B^2 in it, C^2 - z S^2 = 1, "
             "and -(1 + N) a rotor with s = -1, F^2 = 0, F != 0", ok)
    return ok


def check_degenerate_exponential_is_not_a_versor():
    """Cl(0,0,2): every vector is null (Q = 0 identically), so no vector is invertible and the only
    versor is 1; e^{f1 f2} = 1 + f1 f2 exactly, with R R~ = 1 and R x R~ = x, and R != 1."""
    premise("std-algebra.inverse-of-vector")
    premise("std-algebra.involution-properties")
    ok = True
    sq = GA.sig(0, 0, 2)
    ok = ok and sq == (0, 0)
    # Q = 0 on the four vectors e1, e2, e1 + e2, 3 e1 - 2 e2: no vector is invertible
    vs = [S.vec([1, 0]), S.vec([0, 1]), S.vec([1, 1]), S.vec([3, -2])]
    sqs = [GA.mul(v, v, sq) for v in vs]
    ok = ok and sqs == [{}, {}, {}, {}]
    ok = ok and [sorted(v.values()) for v in vs] == [[1], [1], [1, 1], [-2, 3]]
    B = S.blade(0, 1)
    # powers of B: B^0 = 1, B^1 = f1 f2, B^2 = 0, so the series stops after two terms
    pw = [GA.sc(1)]
    for _ in range(3):
        pw.append(GA.mul(pw[-1], B, sq))
    ok = ok and [len(x) for x in pw] == [1, 1, 0, 0]
    ok = ok and len(pw) == 4
    R = GA.add(*[GA.scal(F(1, _fact(j)), pw[j]) for j in range(len(pw))])
    ok = ok and R == {(): F(1), (0, 1): F(1)}
    RR = GA.mul(R, GA.reverse(R), sq)
    ok = ok and GA.reverse(R) == {(): F(1), (0, 1): F(-1)} and RR == {(): F(1)}
    images = [GA.mul(GA.mul(R, GA.gen(i), sq), GA.reverse(R), sq) for i in range(2)]
    ok = ok and images == [{(0,): F(1)}, {(1,): F(1)}]
    # R is not a scalar, so it is not the empty versor 1
    ok = ok and S.grades(R) == [0, 2]
    GA.check("Cl(0,0,2): all vectors null, e^{f1 f2} = 1 + f1 f2 != 1 with R R~ = 1 and trivial action: not a versor", ok)
    return ok
