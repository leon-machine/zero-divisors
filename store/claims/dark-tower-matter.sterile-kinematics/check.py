"""dark-tower-matter.sterile-kinematics: exact checks.

Vectors of R^(2,2) and R^(4,0) are GA.py vectors; Q(v) = v^2 and the bilinear form is GA.dot.
(i)  For every non-null v in the integer box {-2..2}^4 of R^(2,2): v-perp (an exact kernel) is
     three-dimensional and nondegenerate, of signature (1,2) if Q(v) > 0 and (2,1) if Q(v) < 0, so
     indefinite. The decomposition into two null vectors is constructed exactly: a rational null
     vector n0 = (t(u), x(u')) with t, x rational points of the unit circle and B(n0, v) != 0 is
     scaled to n1 with B(n1, v) = Q(v)/2; then w = v/2 - n1 is orthogonal to v with
     Q(w) = -Q(v)/4, and v/2 + w, v/2 - w are null with sum v. Both signs of Q(v) occur.
     Connectedness of the null cone minus the origin: the loop (t(u), t(u)) (u rational, t the
     rational parametrisation of the circle) consists of nonzero null vectors and joins
     n = (1,0,1,0) (u = 0) to -n (u = 1 gives (0,1,0,1); the parametrisation covers the circle), so
     no invariant future half exists; in R^(1,3), by contrast, every nonzero null vector in the box
     has t0 != 0 (the two nappes are separated by t0 = 0).
(ii) In R^(4,0) and R^(0,4) Q(v) = +-(sum of squares): checked as a polynomial identity on the
     generic vector, and Q(v) = 0 only at v = 0 on the whole box.
"""
from fractions import Fraction as F
from itertools import product

import GA

S22 = GA.sig(2, 2)
BOX = [v for v in product(range(-2, 3), repeat=4)]
CIRCLE_U = [F(0), F(1), F(1, 2), F(2), F(-1, 3), F(3)]


def vec(c):
    return GA.add(*[GA.scal(c[i], GA.gen(i)) for i in range(4) if c[i] != 0]) if any(c) else {}


def Q(v, S):
    return GA.mul(v, v, S).get((), F(0))


def circ(u):
    d = 1 + u * u
    return ((1 - u * u) / d, 2 * u / d)


def check_sums_of_null_vectors():
    signs = set()
    for c in BOX:
        v = vec([F(x) for x in c])
        qv = Q(v, S22)
        if qv == 0:
            continue
        # v-perp as an exact kernel, and its signature
        row = [GA.dot(v, GA.gen(i), S22) for i in range(4)]
        ker = GA.field_kernel([row])
        assert len(ker) == 3
        basis = [vec(k) for k in ker]
        gram = [[GA.dot(a, b, S22) for b in basis] for a in basis]
        sg = GA.congruence_signature(gram)
        assert sg == ((1, 2, 0) if qv > 0 else (2, 1, 0))
        # an explicit null decomposition
        done = False
        for u in CIRCLE_U:
            for u2 in CIRCLE_U:
                t, x = circ(u), circ(u2)
                n0 = vec([t[0], t[1], x[0], x[1]])
                assert Q(n0, S22) == 0
                b = GA.dot(n0, v, S22)
                if b != 0:
                    n1 = GA.scal(qv / (2 * b), n0)
                    w = GA.sub(GA.scal(F(1, 2), v), n1)
                    assert GA.dot(w, v, S22) == 0
                    assert Q(w, S22) == -qv / 4
                    a1, a2 = GA.add(GA.scal(F(1, 2), v), w), GA.sub(GA.scal(F(1, 2), v), w)
                    assert Q(a1, S22) == 0 and Q(a2, S22) == 0 and GA.eq(GA.add(a1, a2), v)
                    done = True
                    break
            if done:
                break
        assert done
        signs.add(1 if qv > 0 else -1)
    assert signs == {1, -1}
    return True


def check_null_cone_connected():
    # a loop of nonzero null vectors from n to -n in R^(2,2)
    pts = [F(0), F(1, 3), F(1), F(3), F(-3), F(-1, 3)]
    for u in pts:
        t = circ(u)
        n = vec([t[0], t[1], t[0], t[1]])
        assert Q(n, S22) == 0 and n != {}
    assert circ(F(0)) == (1, 0) and circ(F(1)) == (0, 1)
    # the continuation u -> infinity reaches (-1, 0): circ(u) -> (-1, 0) as u grows
    big = circ(F(10 ** 6))
    assert big[0] < F(-999999, 1000000) and big[1] < F(1, 10 ** 5)
    # (2,2): null vectors exist on t1 = 0, so t1 does not separate the cone
    assert Q(vec([F(0), F(1), F(1), F(0)]), S22) == 0
    # (1,3): every nonzero null vector in the box has t0 != 0
    S13 = GA.sig(1, 3)
    cnt = 0
    for c in BOX:
        v = vec([F(x) for x in c])
        if v and Q(v, S13) == 0:
            assert c[0] != 0
            cnt += 1
    assert cnt == 24
    return True


def check_definite_has_no_null_vector():
    # polynomial identity: Q(v) is the sum (resp. minus the sum) of the squares of the coordinates
    for (p, q, sgn) in ((4, 0, 1), (0, 4, -1)):
        S = GA.sig(p, q)
        for i in range(4):
            for j in range(4):
                bij = GA.dot(GA.gen(i), GA.gen(j), S)
                assert bij == (sgn if i == j else 0)
        for c in BOX:
            v = vec([F(x) for x in c])
            qv = Q(v, S)
            assert qv == sgn * sum(x * x for x in c)
            assert (qv == 0) == (not any(c))
    return True
