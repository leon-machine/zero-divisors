"""transport.totality: exact checks.

Setting (T1, Section 4): the completion Cl(p+1, q+1) of Cl(p, q) adjoins e_+ (square +1) and e_- (square -1),
with the null pair nO = (e_- - e_+)/2, nInf = e_- + e_+ (nO . nInf = -1) and the lift
X(x) = nO + x + Q(x)/2 nInf. iota[N] = [e_+ N e_+].

(1) Conjugation by e_+ maps vectors to vectors, preserves N^2 and so sends nonzero null vectors to nonzero null
    vectors (well defined and total), and is an involution (e_+^2 = 1), on sample null vectors of the completion
    for five base signatures, definite and mixed.
(2) The key display e_+ X(x) e_+ = -(Q(x) nO + x + nInf/2) for every sample x, and for Q(x) != 0 the class is
    [X(x / Q(x))]: the representative equals -Q(x) X(x/Q(x)) exactly.
(3) For Q(x0) = 0 (null x0 and x0 = 0) the image is -(x0 + nInf/2), with nO-coefficient 0 (an ideal point), null,
    and [nInf] at x0 = 0. The limit clause: along x = x0 + t y the normalised representative J(x) =
    Q(x) nO + x + nInf/2 of iota[X(x)] equals Q(x) X(x/Q(x)) at every sample t with Q(x) != 0, and
    J(x0 + t y) - J(x0) = (2 t x0.y + t^2 Q(y)) nO + t y, a polynomial vanishing at t = 0, so the values converge
    to iota[X(x0)].
Not checked: the uniqueness sentence, which is topological (density of the lifted invertible points, Lemma
transport.density, and the Hausdorff property); no premise() call is made since no check uses that content.
"""
from fractions import Fraction as F

import GA

BASES = [(2, 0), (1, 1), (1, 2), (0, 3), (1, 3)]
SAMPLES = [(1, 2, -1, 3), (3, 0, 1, -2), (1, 1, 1, 1), (2, -1, 0, 5), (0, 1, 2, 0)]
TS = [F(1, 3), F(-1, 7), F(1, 50), F(2, 9)]


def setting(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    no = GA.scal(F(1, 2), GA.sub(em, ep))
    ninf = GA.add(em, ep)
    return n, sq, ep, no, ninf


def vec(coeffs, n):
    return {(i,): F(c) for i, c in enumerate(coeffs[:n]) if c != 0}


def quad(x, sq):
    return GA.mul(x, x, sq).get((), F(0))


def lift(x, sq, no, ninf):
    return GA.add(no, x, GA.scal(quad(x, sq) / 2, ninf))


def conj(ep, N, sq):
    return GA.mul(GA.mul(ep, N, sq), ep, sq)


def is_vector(x):
    return all(len(b) == 1 for b in x)


def null_samples(p, q):
    """Nonzero null vectors s nO + x + t nInf of the completion, with Q(x) = 2 s t."""
    n, sq, ep, no, ninf = setting(p, q)
    out = []
    for c in SAMPLES:
        x = vec(c, n)
        for t in (F(1), F(-2, 3)):
            s = quad(x, sq) / (2 * t)
            out.append(GA.add(GA.scal(s, no), x, GA.scal(t, ninf)))
        out.append(lift(x, sq, no, ninf))
    out.append(ninf)
    out.append(no)
    return out


def check_iota_well_defined_total_involution():
    ok = True
    count = 0
    for p, q in BASES:
        n, sq, ep, no, ninf = setting(p, q)
        ok = ok and GA.mul(ep, ep, sq) == {(): F(1)}
        for N in null_samples(p, q):
            ok = ok and quad(N, sq) == 0 and N != {}
            M = conj(ep, N, sq)
            # image is a nonzero vector, null, and iota^2 = id
            ok = ok and is_vector(M) and M != {} and quad(M, sq) == 0
            ok = ok and GA.eq(conj(ep, M, sq), N)
            # rays to rays: lambda N -> lambda M
            ok = ok and GA.eq(conj(ep, GA.scal(F(-5, 3), N), sq), GA.scal(F(-5, 3), M))
            count += 1
    _tp_rv = (ok and count == 85); assert _tp_rv is not False, "check_iota_well_defined_total_involution"; return _tp_rv


def check_reciprocal_on_invertible_vectors():
    ok = True
    hits = 0
    for p, q in BASES:
        n, sq, ep, no, ninf = setting(p, q)
        # columns of iota: e+ nO e+ = -nInf/2, e+ nInf e+ = -2 nO, e+ x e+ = -x
        ok = ok and GA.eq(conj(ep, no, sq), GA.scal(F(-1, 2), ninf))
        ok = ok and GA.eq(conj(ep, ninf, sq), GA.scal(-2, no))
        for i in range(n):
            ok = ok and GA.eq(conj(ep, GA.gen(i), sq), GA.neg(GA.gen(i)))
        for c in SAMPLES:
            x = vec(c, n)
            Q = quad(x, sq)
            img = conj(ep, lift(x, sq, no, ninf), sq)
            key = GA.neg(GA.add(GA.scal(Q, no), x, GA.scal(F(1, 2), ninf)))
            ok = ok and GA.eq(img, key)
            if Q != 0:
                xr = GA.scal(1 / Q, x)
                ok = ok and quad(xr, sq) == 1 / Q
                ok = ok and GA.eq(img, GA.scal(-Q, lift(xr, sq, no, ninf)))
                hits += 1
    _tp_rv = (ok and hits == 24); assert _tp_rv is not False, "check_reciprocal_on_invertible_vectors"; return _tp_rv


def check_null_points_go_to_ideal_points_continuously():
    ok = True
    nulls = 0
    for p, q in BASES:
        n, sq, ep, no, ninf = setting(p, q)
        x0s = [{}]
        if p and q:
            x0s.append(GA.add(GA.gen(0), GA.gen(p)))              # null in mixed signature
            x0s.append(GA.sub(GA.scal(3, GA.gen(0)), GA.scal(3, GA.gen(n - 1))))
        for x0 in x0s:
            ok = ok and quad(x0, sq) == 0
            img = conj(ep, lift(x0, sq, no, ninf), sq)
            ideal = GA.neg(GA.add(x0, GA.scal(F(1, 2), ninf)))
            ok = ok and GA.eq(img, ideal) and quad(img, sq) == 0
            # nO-coefficient: <img, nInf> = -s; zero means ideal point
            ok = ok and GA.dot(img, ninf, sq) == 0 and GA.dot(img, no, sq) == F(1, 2)
            if x0 == {}:
                ok = ok and GA.eq(img, GA.scal(F(-1, 2), ninf))
            J0 = GA.add(x0, GA.scal(F(1, 2), ninf))
            for c in SAMPLES[:3]:
                y = vec(c, n)
                for t in TS:
                    x = GA.add(x0, GA.scal(t, y))
                    Q = quad(x, sq)
                    J = GA.add(GA.scal(Q, no), x, GA.scal(F(1, 2), ninf))
                    ok = ok and GA.eq(conj(ep, lift(x, sq, no, ninf), sq), GA.neg(J))
                    if Q != 0:
                        ok = ok and GA.eq(J, GA.scal(Q, lift(GA.scal(1 / Q, x), sq, no, ninf)))
                    diff = GA.add(GA.scal(2 * t * GA.dot(x0, y, sq) + t * t * quad(y, sq), no),
                                  GA.scal(t, y))
                    ok = ok and GA.eq(GA.sub(J, J0), diff)
            nulls += 1
    _tp_rv = (ok and nulls == 11); assert _tp_rv is not False, "check_null_points_go_to_ideal_points_continuously"; return _tp_rv
