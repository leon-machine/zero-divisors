"""synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five: exact checks.

On a definite side the rung count of a wall with cross-section L^{2n+1}(4) and twisted dying line is the least k
with a map F from the sphere to R^k minus the origin with F(J(v)) = -F(v), J the quarter turn. Checks:
  (1) the explicit map into five dimensions in Cl(6,0): F(v) = w0 e1 w0 - m e1 m + 2 (w0 . m) e3 + w2 e5 w2,
      w_r the plane components of v, m the mirror image of w1 in the first plane. F(J(v)) = -F(v), F has no
      e4 component and Q(F) = (Q(w0) + Q(w1))^2 + Q(w2)^2, as polynomial identities (grids that meet the degree
      bounds); on the three-sphere w2 = 0 the map has three components;
  (2) the twisted cochain complex of the stored cell model (the generator acting by -1 on the coefficients):
      cohomology Z_2 in odd degrees and 0 in even degrees, reduction modulo 2 injective;
  (3) the squaring operation on the Thom space of the line bundle of degree d over the complex projective plane,
      ring Z_2[h, U]/(h^3, U^2 - d h U): Sq^2(U h) = (d + 1) U h^2; the second Chern class a rank-two bundle would
      need, n U h with n d = -(d/2)^2; the table of d = 2, 4, 8, 12, 16 (for d = 0 mod 8 the test does not obstruct);
  (4) the formula Sq^2 c_2 = c_1 c_2 + c_3 modulo 2 from the Cartan formula on Chern roots;
  (5) a second route to (3): the Chern character lattice of the Thom space does not contain n U h for d = 4;
  (6) the upper bound ceil(3(n+1)/2) by blocks and the window it leaves.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ6 = GA.sig(6, 0)
E1, E2, E3, E4, E5, E6 = (GA.gen(i) for i in range(6))
QUARTER = 4          # order of the quarter turn
GRID5 = (F(-2), F(-1), F(0), F(1), F(2))       # five values: enough for degree 4 in one variable
GRID3 = (F(-1), F(0), F(2))                    # three values: enough for degree 2 in one variable


def vec(c):
    return GA.add(*[GA.scal(F(x), GA.gen(i)) for i, x in enumerate(c)])


def bivector_B():
    return GA.add(GA.mul(E1, E2, SQ6), GA.mul(E3, E4, SQ6), GA.mul(E5, E6, SQ6))


def J(v):
    w = GA.mul(v, bivector_B(), SQ6)
    return {k: c for k, c in w.items() if len(k) == 1}


def comp(v, a, b):
    """Component of v in the plane of the generators a, b."""
    return GA.add(GA.scal(GA.dot(v, a, SQ6), a), GA.scal(GA.dot(v, b, SQ6), b))


def Qs(v):
    return GA.dot(v, v, SQ6)


def Fmap(v, mirror=-1):
    w0, w1, w2 = comp(v, E1, E2), comp(v, E3, E4), comp(v, E5, E6)
    # mirror image of w1 in P0 (mirror = -1); mirror = +1 is the unreflected copy, used as a control
    m1 = GA.add(GA.scal(GA.dot(w1, E3, SQ6), E1), GA.scal(mirror * GA.dot(w1, E4, SQ6), E2))
    t1 = GA.mul(GA.mul(w0, E1, SQ6), w0, SQ6)
    t2 = GA.mul(GA.mul(m1, E1, SQ6), m1, SQ6)
    t3 = GA.scal(2 * GA.dot(w0, m1, SQ6), E3)
    t4 = GA.mul(GA.mul(w2, E5, SQ6), w2, SQ6)
    out = GA.add(GA.sub(t1, t2), t3, t4)
    return {k: c for k, c in out.items() if c != 0}


def check_explicit_map_into_five_dimensions():
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    # the map is a vector, quadratic in v, odd under the quarter turn (degree 2 in each variable: 3 values each)
    n_pts = 0
    for a1 in GRID3:
        for b1 in GRID3:
            for a2 in GRID3:
                for b2 in GRID3:
                    for a3 in GRID3:
                        for b3 in GRID3:
                            v = vec((a1, b1, a2, b2, a3, b3))
                            fv = Fmap(v)
                            assert all(len(k) == 1 for k in fv)
                            assert GA.eq(Fmap(J(v)), GA.neg(fv))
                            assert GA.dot(fv, E4, SQ6) == 0
                            n_pts += 1
    assert n_pts == 3 ** 6
    # the norm identity: the first three components depend on (a1, b1, a2, b2) only, the last two on (a3, b3)
    for a1 in GRID5:
        for b1 in GRID5:
            for a2 in GRID5:
                for b2 in GRID5:
                    v = vec((a1, b1, a2, b2, 0, 0))
                    fv = Fmap(v)
                    assert Qs(fv) == (a1 * a1 + b1 * b1 + a2 * a2 + b2 * b2) ** 2
                    assert GA.dot(fv, E5, SQ6) == 0 and GA.dot(fv, E6, SQ6) == 0     # three components on S^3
    for a3 in GRID5:
        for b3 in GRID5:
            v = vec((0, 0, 0, 0, a3, b3))
            fv = Fmap(v)
            assert Qs(fv) == (a3 * a3 + b3 * b3) ** 2
            assert all(GA.dot(fv, e, SQ6) == 0 for e in (E1, E2, E3, E4))
    # additivity of the two blocks, and the full identity at mixed points
    for c in ((1, 2, 3, 4, 5, 6), (2, -1, 0, 3, -2, 1), (F(1, 2), F(3, 5), -2, F(7, 3), 1, F(-4, 9))):
        v = vec(c)
        w0, w1, w2 = comp(v, E1, E2), comp(v, E3, E4), comp(v, E5, E6)
        assert Qs(Fmap(v)) == (Qs(w0) + Qs(w1)) ** 2 + Qs(w2) ** 2
        assert Qs(Fmap(v)) > 0
    # control: with the unreflected copy of w1 the norm identity still holds but the map is not odd
    v = vec((1, 2, 3, 4, 0, 0))
    bad = Fmap(v, mirror=1)
    assert Qs(bad) == (1 + 4 + 9 + 16) ** 2
    assert not GA.eq(Fmap(J(v), mirror=1), GA.neg(bad))
    return True


def twisted_coboundaries(top, m=QUARTER, sign=-1):
    """Coboundary numbers of the cochain complex Hom_G(C, Z_twisted): the invariant cochain eps_k takes the value
    sign^a on g^a e_k; delta eps_{k-1} = d_k eps_k with d_k = sign - 1 (k odd), sum of sign^a (k even)."""
    out = []
    for k in range(1, top + 1):
        if k % 2 == 1:
            out.append(sign - 1)
        else:
            out.append(sum(sign ** a for a in range(m)))
    return out


def cohomology_orders(d, top):
    """Orders of H^k (0 for infinite) of the complex Z -> Z -> ... with coboundaries d[0], d[1], ..."""
    H = []
    for k in range(top + 1):
        d_in = d[k - 1] if k >= 1 else 0
        d_out = d[k] if k < top else 0
        if d_out != 0:
            H.append(1)                 # no cocycles
        elif d_in == 0:
            H.append(0)                 # Z
        else:
            H.append(abs(d_in))
    return H


def check_twisted_cochain_complex():
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    top = 5
    d_tw = twisted_coboundaries(top)
    assert d_tw == [-2, 0, -2, 0, -2]
    assert cohomology_orders(d_tw, top) == [1, 2, 1, 2, 1, 2]          # 0, Z2, 0, Z2, 0, Z2
    d_un = twisted_coboundaries(top, sign=1)
    assert d_un == [0, 4, 0, 4, 0]
    assert cohomology_orders(d_un, top) == [0, 1, 4, 1, 4, 0]          # Z, 0, Z4, 0, Z4, Z
    # reduction modulo 2 of the twisted classes is injective: the generator eps_k (k odd) is not divisible by 2
    # modulo coboundaries, which are the even multiples
    for k in (1, 3, 5):
        assert abs(d_tw[k - 1]) == 2
    # the half-turn plane bundle has Euler class 2y, not zero in Z4: no section of two copies of the line
    assert (2 * 1) % 4 != 0 and (2 * 2) % 4 == 0
    return True


# polynomials over Z in h, U: dict {(i, j): c} for c h^i U^j, reduced with h^(m+1) = 0, U^2 = d h U
def reduce_thom(p, d, m=2, mod=2):
    out = {}
    for (i, j), c in p.items():
        while j >= 2:
            i, j, c = i + 1, j - 1, c * d
        if i <= m and j <= 1:
            out[(i, j)] = out.get((i, j), 0) + c
    return {k: v % mod for k, v in out.items() if v % mod}


def pmul2(p, q):
    out = {}
    for (i, j), c in p.items():
        for (k, l), e in q.items():
            out[(i + k, j + l)] = out.get((i + k, j + l), 0) + c * e
    return out


def sq2_monomial(i, j):
    """Sq^2 of h^i U^j by the Cartan formula with Sq^2 h = h^2, Sq^2 U = U^2, Sq^1 = 0 on integral classes:
    Sq^2 is a derivation here, so Sq^2(h^i U^j) = i h^(i+1) U^j + j h^i U^(j+1)."""
    out = {}
    if i:
        out[(i + 1, j)] = i
    if j:
        out[(i, j + 1)] = out.get((i, j + 1), 0) + j
    return out


def check_squaring_operation_on_the_thom_space():
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    def obstruction(d, n):
        """Coefficient of U h^2 in Sq^2(n U h), modulo 2."""
        s = reduce_thom({k: n * c for k, c in sq2_monomial(1, 1).items()}, d)
        return s.get((2, 1), 0)
    assert obstruction(4, -1) == 1                      # the quarter-turn lens space: obstructed
    assert obstruction(4, 1) == 1 and obstruction(4, 2) == 0
    assert obstruction(1, 1) == 0                       # control: d = 1 is the projective space CP^3, Sq^2 h^2 = 0
    assert obstruction(3, 1) == 0 and obstruction(2, 1) == 1
    for d in range(1, 13):
        assert obstruction(d, 1) == (d + 1) % 2
    # the class needed: n U h restricting to c_2 = -(d/2)^2 h^2, U restricting to d h, so n d = -(d/2)^2
    table = {}
    for d in (2, 4, 8, 12, 16):
        c2 = -F(d, 2) ** 2
        n = c2 / d
        if n.denominator != 1:
            table[d] = "primary"
        else:
            table[d] = "secondary" if obstruction(d, int(n)) else "none"
    assert table == {2: "primary", 4: "secondary", 8: "none", 12: "secondary", 16: "none"}
    # c_1 of the glued bundle: U restricts to d h, injective on degree two, so c_1 = 0; c_2 of the sum of the
    # line bundles of degrees +2 and -2 on the projective plane is -4 h^2
    assert (1 + 2) * (1 - 2) - 1 + 0 == -4 and 4 * (-1) == -4
    return True


def check_square_of_the_second_chern_class():
    """Sq^2 c_2 = c_1 c_2 + c_3 modulo 2 on Chern roots, for three and for two roots (c_3 = 0)."""
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    def mul(p, q):
        out = {}
        for a, c in p.items():
            for b, e in q.items():
                k = tuple(x + y for x, y in zip(a, b))
                out[k] = out.get(k, 0) + c * e
        return out

    def add(p, q):
        out = dict(p)
        for k, c in q.items():
            out[k] = out.get(k, 0) + c
        return out

    def mod2(p):
        return {k: c % 2 for k, c in p.items() if c % 2}

    def sq2(p, r):
        out = {}
        for a, c in p.items():
            for i in range(r):
                if a[i]:
                    b = tuple(x + (1 if t == i else 0) for t, x in enumerate(a))
                    out[b] = out.get(b, 0) + c * a[i]
        return out
    for r in (2, 3):
        x = [{tuple(1 if t == i else 0 for t in range(r)): 1} for i in range(r)]
        c1 = {}
        for xi in x:
            c1 = add(c1, xi)
        c2 = {}
        for i in range(r):
            for j in range(i + 1, r):
                c2 = add(c2, mul(x[i], x[j]))
        c3 = mul(mul(x[0], x[1]), x[2]) if r == 3 else {}
        assert mod2(sq2(c2, r)) == mod2(add(mul(c1, c2), c3))
        assert mod2(sq2(c2, r)) != mod2(mul(c1, c2)) or r == 2
    return True


def check_chern_character_lattice():
    """Second route: a rank-two bundle with c_1 = 0 has Chern character 2 - c_2 with no part of degree six.
    Lattice of the Thom space: ch of the Thom class is U (e^{d h} - 1)/(d h); times ch of t^i, t the hyperplane
    line minus one."""
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    def lattice(d):
        thom = [F(1), F(d, 2), F(d * d, 6)]             # coefficients of U, U h, U h^2
        t = [F(0), F(1), F(1, 2)]                       # ch(t) = h + h^2/2
        def trunc_mul(a, b):
            return [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(3)]
        t2 = trunc_mul(t, t)
        return [thom, trunc_mul(thom, t), trunc_mul(thom, t2)]
    def contains_pure_degree_four(d, n):
        """Is n U h (no U and no U h^2 part) an integer combination of the three lattice vectors?"""
        b1, b2, b3 = lattice(d)
        assert b1[0] == 1 and b2[:2] == [0, 1] and b3 == [0, 0, 1]
        a, b = F(0), F(n)                                # triangular solve
        c = -(a * b1[2] + b * b2[2])
        return c.denominator == 1
    assert lattice(4)[1] == [0, 1, F(5, 2)]
    assert not contains_pure_degree_four(4, -1)
    assert contains_pure_degree_four(4, 2) and contains_pure_degree_four(8, -2)
    assert not contains_pure_degree_four(12, -3)
    assert contains_pure_degree_four(1, 1)               # control: CP^3
    for d in range(1, 13):
        for n in range(-3, 4):
            assert contains_pure_degree_four(d, n) == ((n * (d + 1)) % 2 == 0)
    return True


def check_upper_bounds_by_blocks():
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    premise("synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial")
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    def upper(n):                    # n + 1 complex coordinates: pairs give 3 components, a single one gives 2
        pairs, single = divmod(n + 1, 2)
        return 3 * pairs + 2 * single
    assert [upper(n) for n in range(6)] == [2, 3, 5, 6, 8, 9]
    for n in range(12):
        assert upper(n) == -((-3 * (n + 1)) // 2)        # ceil(3(n+1)/2)
        assert upper(n) <= 2 * n + 2                     # never worse than the dimension bound
    assert upper(2) == 5 and upper(3) == 6
    return True
