"""std-algebra.complexification-is-the-odd-extension: exact checks.

V nondegenerate of even dimension n, orthonormal basis e_0 .. e_{n-1} (squares listed below),
I_V = e_0 ... e_{n-1}. Adjoin e = e_n orthogonal to V with Q(e) = -I_V^2, W = V + Re, I_W = I_V e
(the top blade of Cl(W)).

(i)   I_W^2 = -1 (and +1 for the other sign of Q(e)); I_W commutes with every generator of W, so it is
      central; for n = 2, 4 the centre of Cl(W) is exactly span{1, I_W} (commutant computed);
(ii)  a + b (unit) -> a + b I_W is an isomorphism Cl(V) (x) span{1, I_W} -> Cl(W): the images of the
      generators obey the defining relations, the map is onto (rank 2^(n+1)), and it is multiplicative
      on every pair of basis elements for n = 4; Cl(W) = Cl^0(W) + Cl^0(W) I_W;
(vi)  odd n: Cl(1,2) (x) span{1, I_W'} -> Cl(2,3) through V + R f is multiplicative and injective;
(iii) (a + I_W b)^2 = Q(a) - Q(b) + 2 <a, b> I_W, the shift (y + eps I_W a)^2 = Q(y) - eps^2 Q(a)
      + 2 eps <y, a> I_W, e_2 + I_5 e_3 is null, e_2 + I_4 e_3 squares outside span{1, I_4};
(iv)  with Q(e) = +1 and P_+- = (1 +- e)/2: (x P_+-) I_W = +-(x I_V) P_+- for every blade x of Cl(V),
      = +-(I_V x) P_+- on even x, = -+(I_V x) P_+- on vectors, and x -> x P_+ is injective.
Instances: Cl(1,3) -> Cl(2,3) with I_5 = I_4 e, Cl(2,4) -> Cl(3,4) with I_7 = I_6 e, I_6 = I_4 e_+ e_-.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def top(n):
    return {tuple(range(n)): F(1)}


def sq_of(x, sq):
    return GA.mul(x, x, sq)


def scalar(x):
    return x.get((), F(0))


def blades(n):
    return GA.all_blades(n)


def vec(coeffs):
    out = {}
    for k, c in enumerate(coeffs):
        if c != 0:
            out[(k,)] = F(c)
    return out


def form(a, b, sq):
    """<a, b> for vectors given as coefficient lists."""
    return sum(F(x) * F(y) * s for x, y, s in zip(a, b, sq))


def commutant_dim(gens, n, sq):
    """Real dimension of {x in Cl(n) : x g = g x for every g in gens}."""
    bl = blades(n)
    rows = []
    for g in gens:
        cols = [GA.sub(GA.mul({b: F(1)}, g, sq), GA.mul(g, {b: F(1)}, sq)) for b in bl]
        for c in bl:
            rows.append([cols[j].get(c, F(0)) for j in range(len(bl))])
    return len(bl) - GA.mat_rank(GA.frac_matrix(rows))


def check_added_vector_makes_a_central_unit():
    premise("odd-extensions.volume-element-odd-dimension")
    premise("primer.centre")
    ok = True
    # every signature of even dimension 2 and 4, and the conformal space (dimension 6)
    cases = [[1, 1], [1, -1], [-1, -1],
             [1, 1, 1, 1], [1, 1, 1, -1], [1, 1, -1, -1], [1, -1, -1, -1], [-1, -1, -1, -1],
             [1, -1, -1, -1, 1, -1]]
    for sq in cases:
        n = len(sq)
        q = sum(1 for s in sq if s < 0)
        iv2 = scalar(sq_of(top(n), tuple(sq)))
        ok &= iv2 == F(-1) ** ((n * (n - 1) // 2 + q) % 2)
        qe = -iv2
        sqw = tuple(sq + [qe])
        iw = top(n + 1)
        ok &= sq_of(iw, sqw) == GA.sc(-1)
        ok &= all(GA.commutes(iw, GA.gen(k), sqw) for k in range(n + 1))
        # the other sign of Q(e) gives a square +1 (the doubling case): the sign is forced
        ok &= sq_of(iw, tuple(sq + [-qe])) == GA.sc(1)
        if n <= 4:
            ok &= commutant_dim([GA.gen(k) for k in range(n + 1)], n + 1, sqw) == 2
    # the two instances: Q(e) = +1 for spacetime and for the conformal space
    for sq in ([1, -1, -1, -1], [1, -1, -1, -1, 1, -1]):
        ok &= -scalar(sq_of(top(len(sq)), tuple(sq))) == 1
    GA.check("(i) Q(e) = -I_V^2 makes I_W = I_V e central with square -1 (the other sign gives +1); the "
             "centre is span{1, I_W} (n = 2, 4); Q(e) = +1 for Cl(1,3) and Cl(2,4)", ok)
    return ok


def check_complexification_map_is_an_isomorphism():
    premise("std-algebra.complexification")
    premise("odd-extensions.doubling-or-complexification")
    ok = True
    for sq in ([1, -1, -1, -1], [1, -1, -1, -1, 1, -1]):
        n = len(sq)
        sqw = tuple(sq + [1])
        iw = top(n + 1)
        # relations of Cl(V) (x) C on generators: Clifford relations, a central unit of square -1
        for k in range(n):
            for m in range(n):
                anti = GA.add(GA.mul(GA.gen(k), GA.gen(m), sqw), GA.mul(GA.gen(m), GA.gen(k), sqw))
                ok &= anti == (GA.sc(2 * sq[k]) if k == m else {})
            ok &= GA.commutes(iw, GA.gen(k), sqw)
        ok &= sq_of(iw, sqw) == GA.sc(-1)
        # onto: the images of the real basis {x, x unit} span Cl(W)
        bl = blades(n)
        images = [{b: F(1)} for b in bl] + [GA.mul({b: F(1)}, iw, sqw) for b in bl]
        allw = blades(n + 1)
        ok &= GA.rank_of_vectors([[x.get(c, F(0)) for c in allw] for x in images]) == 2 ** (n + 1)
        # Cl(W) = Cl^0(W) + Cl^0(W) I_W, the second summand the odd part
        even = [b for b in allw if len(b) % 2 == 0]
        odd_images = [GA.mul({b: F(1)}, iw, sqw) for b in even]
        ok &= all(len(b) % 2 == 1 for x in odd_images for b in x)
        ok &= GA.rank_of_vectors([[x.get(c, F(0)) for c in allw] for x in
                                  [{b: F(1)} for b in even] + odd_images]) == 2 ** (n + 1)
    # multiplicativity on every pair of basis elements, n = 4: the abstract product of pairs
    # (a, b) = a + b u with u central, u^2 = -1, against the product in Cl(2,3)
    sq = [1, -1, -1, -1]
    sqv, sqw, iw = tuple(sq), tuple(sq + [1]), top(5)

    def phi(a, b):
        return GA.add(a, GA.mul(b, iw, sqw))

    basis = [({b: F(1)}, {}) for b in blades(4)] + [({}, {b: F(1)}) for b in blades(4)]
    for a1, b1 in basis:
        for a2, b2 in basis:
            pa = GA.sub(GA.mul(a1, a2, sqv), GA.mul(b1, b2, sqv))
            pb = GA.add(GA.mul(a1, b2, sqv), GA.mul(b1, a2, sqv))
            ok &= GA.mul(phi(a1, b1), phi(a2, b2), sqw) == phi(pa, pb)
    # (vi) odd dimension: V = R^{1,2} inside V' = V + R f (Q(f) = -1), W' = V' + R e (Q(e) = +1)
    sqv3, sqw5, iw5 = (1, -1, -1), (1, -1, -1, -1, 1), top(5)

    def phi3(a, b):
        return GA.add(a, GA.mul(b, iw5, sqw5))

    basis3 = [({b: F(1)}, {}) for b in blades(3)] + [({}, {b: F(1)}) for b in blades(3)]
    for a1, b1 in basis3:
        for a2, b2 in basis3:
            pa = GA.sub(GA.mul(a1, a2, sqv3), GA.mul(b1, b2, sqv3))
            pb = GA.add(GA.mul(a1, b2, sqv3), GA.mul(b1, a2, sqv3))
            ok &= GA.mul(phi3(a1, b1), phi3(a2, b2), sqw5) == phi3(pa, pb)
    ok &= GA.rank_of_vectors([[phi3(a, b).get(c, F(0)) for c in blades(5)] for a, b in basis3]) == 16
    GA.check("(ii) e_k -> e_k, unit -> I_W is an isomorphism Cl(V) (x) span{1, I_W} -> Cl(W) for "
             "Cl(1,3) -> Cl(2,3) and Cl(2,4) -> Cl(3,4); Cl(W) = Cl^0(W) + Cl^0(W) I_W", ok)
    return ok


def check_complex_vectors_and_shifted_squares():
    premise("odd-extensions.volume-element-odd-dimension")
    ok = True
    sq = [1, -1, -1, -1]
    sqw, i5 = tuple(sq + [1]), top(5)
    i4 = top(4)
    # each sample with its square computed by hand: (Q(a) - Q(b), 2<a, b>)
    samples = [([1, 2, 0, -3], [0, 1, 4, 1], F(6), F(2)),
               ([F(1, 2), 0, 3, 1], [2, -1, 0, F(2, 3)], F(-443, 36), F(2, 3)),
               ([0, 0, 1, 0], [0, 0, 0, 1], F(0), F(0))]
    for a, b, p0, q0 in samples:
        z = GA.add(vec(a), GA.mul(i5, vec(b), sqw))
        want = GA.add(GA.sc(form(a, a, sq) - form(b, b, sq)), GA.scal(2 * form(a, b, sq), i5))
        ok &= sq_of(z, sqw) == want
        ok &= sq_of(z, sqw) == GA.add(GA.sc(p0), GA.scal(q0, i5))
    # complex null vector e_2 + I_5 e_3; the left unit I_4 does not complexify vectors
    z = GA.add(GA.gen(2), GA.mul(i5, GA.gen(3), sqw))
    ok &= sq_of(z, sqw) == {}
    w = GA.add(GA.gen(2), GA.mul(i4, GA.gen(3), sqw))
    w2 = sq_of(w, sqw)
    ok &= w2 == GA.add(GA.sc(-2), GA.scal(2, GA.mul(GA.gen(0), GA.gen(1), sqw)))
    # the shift: (y + eps I_5 e_0)^2 = Q(y) - eps^2 + 2 eps y_0 I_5, a number of span{1, I_5}
    for y, eps, p0, q0 in (([3, 1, -2, 5], F(1, 3), F(-190, 9), F(2)),
                           ([F(1, 2), 4, 0, -1], F(-2, 7), F(-3299, 196), F(-2, 7))):
        a = [1, 0, 0, 0]
        z = GA.add(vec(y), GA.scal(eps, GA.mul(i5, vec(a), sqw)))
        p = form(y, y, sq) - eps * eps * form(a, a, sq)
        qq = 2 * eps * form(y, a, sq)
        ok &= (p, qq) == (p0, q0)
        ok &= sq_of(z, sqw) == GA.add(GA.sc(p), GA.scal(qq, i5))
        num = GA.add(GA.sc(p), GA.scal(qq, i5))
        conj = GA.sub(GA.sc(p), GA.scal(qq, i5))
        ok &= GA.mul(num, conj, sqw) == GA.sc(p * p + qq * qq)
    GA.check("(iii) (a + I_5 b)^2 = Q(a) - Q(b) + 2<a,b> I_5; e_2 + I_5 e_3 is null and e_2 + I_4 e_3 is "
             "not; (y + eps I_5 e_0)^2 = Q(y) - eps^2 + 2 eps y_0 I_5 lies in the field span{1, I_5}", ok)
    return ok


def check_relation_to_the_right_unit():
    ok = True
    for sq in ([1, -1, -1, -1], [1, -1, -1, -1, 1, -1]):
        n = len(sq)
        sqw = tuple(sq + [1])
        iv, iw = top(n), top(n + 1)
        e = GA.gen(n)
        pp = GA.scal(F(1, 2), GA.add(GA.sc(1), e))
        pm = GA.scal(F(1, 2), GA.sub(GA.sc(1), e))
        ok &= GA.mul(pp, pp, sqw) == pp and GA.mul(pm, pm, sqw) == pm
        ok &= GA.commutes(pp, iv, sqw)
        rows = []
        for b in blades(n):
            x = {b: F(1)}
            xi = GA.mul(x, iv, sqw)
            ok &= GA.mul(GA.mul(x, pp, sqw), iw, sqw) == GA.mul(xi, pp, sqw)
            ok &= GA.mul(GA.mul(x, pm, sqw), iw, sqw) == GA.neg(GA.mul(xi, pm, sqw))
            ix = GA.mul(iv, x, sqw)
            if len(b) % 2 == 0:
                ok &= GA.mul(GA.mul(x, pp, sqw), iw, sqw) == GA.mul(ix, pp, sqw)
            if len(b) == 1:
                ok &= GA.mul(GA.mul(x, pp, sqw), iw, sqw) == GA.neg(GA.mul(ix, pp, sqw))
            rows.append(GA.mul(x, pp, sqw))
        allw = blades(n + 1)
        ok &= GA.rank_of_vectors([[x.get(c, F(0)) for c in allw] for x in rows]) == 2 ** n
    GA.check("(iv) (x P_+-) I_W = +-(x I_V) P_+- for every blade of Cl(V), the left unit on even x and its "
             "negative on vectors; x -> x P_+ injective; for Cl(1,3) (I_5, I_4) and Cl(2,4) (I_7, I_6)", ok)
    return ok
