"""synthesis.no-quarter-turn-odd-map-from-the-five-sphere-to-four-components: exact checks.

The sphere bundle M = (S^5 x S^3)/Z_4, the generator acting by the quarter turn J on S^5 and by -1 on S^3 (the unit
sphere of the even subalgebra of Cl(3,0)), has the product cell model C (x) D: C the stored complex of S^5 (one free
cell e_k in each dimension, boundary (g - 1) e_{k-1} for k odd and N e_{k-1} for k even), D the same complex for
the group of order two (the antipodal three-sphere), the generator of Z_4 acting on D through the antipode.
Cells are tuples (k, a, q, b) for g^a e_k (x) T^b d_q; invariant cochains are functions of the orbit
representative (k, 0, q, b - a). Modulo-2 chains are Python sets (addition is symmetric difference). Checks:
  (1) the quarter turn as a rotor sandwich in Cl(6,0), the even subalgebra of Cl(3,0) as the fibre, and the
      cells of the sphere in the algebra;
  (2) the product complex: the integral boundary squares to zero, 48 orbits of cells;
  (3) the higher diagonal Delta_1 on the two factors: explicit terms, carried by closed cells, and
      bd Delta_1 + Delta_1 bd = Delta_0 + (transpose of Delta_0) modulo 2 on every cell;
  (4) the same identity for the product higher diagonal on all 48 orbits, for both product formulas;
  (5) the integral fibre cocycle theta, and that the lens space has no integral class of degree three;
  (6) theta cup_1 theta = p^*(eps_5) modulo 2 up to a coboundary, for four choices of the higher diagonal;
  (7) a chain map C -> C (x) D that is a section of the projection exists (the obstruction is not in the chain
      complexes alone);
  (8) controls: orders 8 and 16 (no obstruction), 12 (obstruction), 2 and 6 (no integral fibre class), trivial
      action on the fibre and the three-dimensional base (nothing).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

STORED = "synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure"
QUARTER = 4               # order of the quarter turn
ANTI = 2                  # order of the antipode
BASE_TOP = 5              # top cell dimension of the base sphere S^5
FIBRE_TOP = 3             # top cell dimension of the fibre sphere S^3
DEG = 3                   # degree of the fibre class
ORBITS = 48               # orbits of cells of the product: 6 * 4 * 2
# sample vectors of R^6 with positive components along e5 and e6 (points of the cone over the open cell e_5)
SAMPLE_VECTORS = ((F(2), F(-1), F(0), F(3), F(3, 5), F(4, 5)), (F(0), F(1), F(-2), F(1), F(5, 13), F(12, 13)),
                  (F(-1), F(1, 2), F(2), F(0), F(15, 17), F(8, 17)), (F(1), F(1), F(1), F(-3), F(1), F(2)))
# sample elements of the even subalgebra of Cl(3,0): scalar part and three bivector parts
SAMPLE_EVEN = ((F(1), F(2), F(-1), F(3)), (F(2), F(0), F(1), F(-1)), (F(0), F(1), F(1), F(1)), (F(3), F(-2), F(0), F(1, 2)))


# ---------------------------------------------------------------- one factor: the stored complex for a group Z_m
def bd(k, a, m):
    """Boundary of g^a e_k as a dict cell -> integer (the stored formulas)."""
    out = {}
    if k == 0:
        return out
    if k % 2 == 1:
        out[(k - 1, (a + 1) % m)] = out.get((k - 1, (a + 1) % m), 0) + 1
        out[(k - 1, a)] = out.get((k - 1, a), 0) - 1
    else:
        for c in range(m):
            out[(k - 1, (a + c) % m)] = out.get((k - 1, (a + c) % m), 0) + 1
    return {x: v for x, v in out.items() if v}


def bd2(k, a, m):
    """Boundary modulo 2, as a list of cells."""
    return [x for x, v in bd(k, a, m).items() if v % 2]


def closure(k, a, m):
    """Cells of the closed cell g^a e_k: itself; for k odd its two ends g^a e_{k-1}, g^{a+1} e_{k-1} and the
    sphere of dimension k - 2; for k even the sphere of dimension k - 1."""
    out = {(k, a)}
    low = k
    if k % 2 == 1:
        out |= {(k - 1, a), (k - 1, (a + 1) % m)}
        low = k - 1
    for j in range(low):
        for c in range(m):
            out.add((j, c))
    return out


def toggle(S, items):
    for x in items:
        if x in S:
            S.remove(x)
        else:
            S.add(x)


def delta0(k, m):
    """The stored diagonal on e_k, modulo 2: a set of (p, a, q, b) for g^a e_p (x) g^b e_q."""
    out = set()
    for p in range(k + 1):
        q = k - p
        if p % 2 == 0:
            terms = [(0, 0)]
        elif q % 2 == 0:
            terms = [(0, 1)]
        else:
            terms = [(i, j) for i in range(m) for j in range(i + 1, m)]
        toggle(out, [(p, i % m, q, j % m) for (i, j) in terms])
    return out


def delta1(k, m, shape=0):
    """The higher diagonal on e_k, modulo 2. Terms by degree (N' = g + ... + g^{m-1} on the first factor):
    e_1: e_1 (x) e_1;  e_2: N e_1 (x) e_2;  e_3: e_3 (x) e_1 + N' e_1 (x) e_3;  e_4: N e_3 (x) e_2;
    e_5: e_1 (x) e_5 + N' e_3 (x) e_3 + e_5 (x) e_1.  shape = 1, 2 are wrong forms used as controls."""
    full = range(m)
    rest = range(1, m) if shape != 1 else range(m)
    table = {
        0: [],
        1: [(1, 0, 1, 0)],
        2: [(1, a, 2, 0) for a in full],
        3: [(3, 0, 1, 0)] + [(1, a, 3, 0) for a in rest],
        4: [(3, a, 2, 0) for a in full],
        5: [(1, 0, 5, 0), (5, 0, 1, 0)] + [(3, a, 3, 0) for a in rest],
    }
    out = set(table[k])
    if shape == 2 and k == 2:
        out = {(1, 0, 2, 0)}
    return out


def shift(T, s, m):
    return {(p, (a + s) % m, q, (b + s) % m) for (p, a, q, b) in T}


def swap(T):
    return {(q, b, p, a) for (p, a, q, b) in T}


def bd_tensor2(T, m):
    out = set()
    for (p, a, q, b) in T:
        toggle(out, [(pp, aa, q, b) for (pp, aa) in bd2(p, a, m)])
        toggle(out, [(p, a, qq, bb) for (qq, bb) in bd2(q, b, m)])
    return out


def carried(T, k, m):
    cl = closure(k, 0, m)
    return all((p, a) in cl and (q, b) in cl for (p, a, q, b) in T)


def homotopy_defect(k, m, h1):
    """bd h1(e_k) + h1(bd e_k) + Delta_0(e_k) + transpose Delta_0(e_k), modulo 2 (empty when the identity holds)."""
    out = bd_tensor2(h1(k), m)
    for (kk, aa) in bd2(k, 0, m):
        toggle(out, shift(h1(kk), aa, m))
    toggle(out, delta0(k, m))
    toggle(out, swap(delta0(k, m)))
    return out


# ---------------------------------------------------------------- the product complex C_m (x) C_2
class Bundle:
    """M = (S^top x S^3)/Z_m: g acts on the fibre cells by T^act (act = 1 the antipode, act = 0 trivially)."""

    def __init__(self, m, top=BASE_TOP, act=1, formula=0, transposed=False):
        self.m, self.top, self.act, self.formula, self.transposed = m, top, act, formula, transposed

    def reps(self, n):
        return [(k, 0, n - k, b) for k in range(self.top + 1) if 0 <= n - k <= FIBRE_TOP for b in range(ANTI)]

    def rep(self, c):
        k, a, q, b = c
        return (k, 0, q, (b - self.act * a) % ANTI)

    def bd(self, c):
        k, a, q, b = c
        out = {}
        for (kk, aa), v in bd(k, a, self.m).items():
            out[(kk, aa, q, b)] = out.get((kk, aa, q, b), 0) + v
        for (qq, bb), v in bd(q, b, ANTI).items():
            out[(k, a, qq, bb)] = out.get((k, a, qq, bb), 0) + v * (-1) ** k
        return {x: v for x, v in out.items() if v}

    def bd2(self, c):
        return [x for x, v in self.bd(c).items() if v % 2]

    def move(self, T, a, b):
        """Translate a set of pairs of cells by g^a on the base and T^b on the fibre."""
        m = self.m
        return {((k1, (a1 + a) % m, q1, (b1 + b) % ANTI), (k2, (a2 + a) % m, q2, (b2 + b) % ANTI))
                for ((k1, a1, q1, b1), (k2, a2, q2, b2)) in T}

    @staticmethod
    def interleave(TC, TD):
        return {((p, a, r, c), (q, b, s, d)) for (p, a, q, b) in TC for (r, c, s, d) in TD}

    def diag(self, c):
        k, a, q, b = c
        return self.move(self.interleave(delta0(k, self.m), delta0(q, ANTI)), a, b)

    def high(self, c):
        """Product higher diagonal: formula 0 is Delta_1 (x) tDelta_0 + Delta_0 (x) Delta_1, formula 1 is
        Delta_1 (x) Delta_0 + tDelta_0 (x) Delta_1 (t the transposition); transposed = True exchanges the
        two tensor factors of the result."""
        k, a, q, b = c
        m = self.m
        out = set()
        if self.formula == 0:
            toggle(out, self.interleave(delta1(k, m), swap(delta0(q, ANTI))))
            toggle(out, self.interleave(delta0(k, m), delta1(q, ANTI)))
        else:
            toggle(out, self.interleave(delta1(k, m), delta0(q, ANTI)))
            toggle(out, self.interleave(swap(delta0(k, m)), delta1(q, ANTI)))
        if self.transposed:
            out = {(y, x) for (x, y) in out}
        return self.move(out, a, b)

    def bd_pairs(self, T):
        out = set()
        for (x, y) in T:
            toggle(out, [(z, y) for z in self.bd2(x)])
            toggle(out, [(x, z) for z in self.bd2(y)])
        return out

    def defect(self, c):
        out = self.bd_pairs(self.high(c))
        for x in self.bd2(c):
            toggle(out, self.high(x))
        toggle(out, self.diag(c))
        toggle(out, {(y, x) for (x, y) in self.diag(c)})
        return out

    def theta(self):
        """The integral cochain of degree 3: 1 on e_0 (x) d_3 and on e_1 (x) d_2, -m/4 on e_2 (x) d_1 and on
        e_2 (x) T d_1, zero on the other orbit representatives."""
        n = F(-self.m, QUARTER)
        return {(0, 0, 3, 0): F(1), (1, 0, 2, 0): F(1), (2, 0, 1, 0): n, (2, 0, 1, 1): n}

    def coboundary(self, phi, n):
        """Coboundary of an invariant cochain of degree n - 1, on the representatives of degree n."""
        return {c: sum(v * phi.get(self.rep(x), 0) for x, v in self.bd(c).items()) for c in self.reps(n)}

    def cup_one_square(self, phi):
        """(phi cup_1 phi) modulo 2: the set of representatives of degree 2 DEG - 1 on which it is odd."""
        odd = {c for c, v in phi.items() if v % 2}
        out = set()
        for c in self.reps(2 * DEG - 1):
            n = sum(1 for (x, y) in self.high(c) if self.rep(x) in odd and self.rep(y) in odd)
            if n % 2:
                out.add(c)
        return out

    def coboundaries2(self, n):
        """Coboundaries modulo 2 of the basis cochains of degree n - 1, as sets of representatives of degree n."""
        gens = []
        for r in self.reps(n - 1):
            gens.append({c for c in self.reps(n) if sum(1 for x in self.bd2(c) if self.rep(x) == r) % 2})
        return gens

    def pullback_top(self):
        """p^*(eps_top): the cochain equal to 1 on e_top (x) (a vertex of the fibre)."""
        return {c for c in self.reps(self.top) if c[2] == 0}


def in_span(target, gens):
    """Is the set target a sum modulo 2 of some of the sets gens? (elimination over the field of two elements)"""
    piv = {}
    for g in gens:
        g = set(g)
        while g:
            key = min(g)
            if key in piv:
                g ^= piv[key]
            else:
                piv[key] = g
                break
    t = set(target)
    while t:
        key = min(t)
        if key not in piv:
            return False
        t ^= piv[key]
    return True


def integral(phi):
    return all(v.denominator == 1 for v in phi.values())


# ---------------------------------------------------------------- checks
def check_quarter_turn_rotor_and_quaternion_fibre():
    premise(STORED)
    sq = GA.sig(len(SAMPLE_VECTORS[0]), 0)
    e = [GA.gen(i) for i in range(len(SAMPLE_VECTORS[0]))]
    planes = [GA.mul(e[2 * r], e[2 * r + 1], sq) for r in range(len(e) // 2)]
    B = GA.add(*planes)
    one = GA.mul(e[0], e[0], sq)
    U, Urev = one, one
    for P in planes:
        U = GA.mul(U, GA.add(one, P), sq)                  # unnormalised rotor (1 + e1e2)(1 + e3e4)(1 + e5e6)
        Urev = GA.mul(Urev, GA.sub(one, P), sq)

    def J(v):
        w = GA.mul(v, B, sq)
        return {k: c for k, c in w.items() if len(k) == 1}
    for coords in SAMPLE_VECTORS:
        v = GA.add(*[GA.scal(c, g) for c, g in zip(coords, e)])
        sandwich = GA.mul(GA.mul(Urev, v, sq), U, sq)
        assert GA.eq(sandwich, GA.scal(F(8), J(v)))        # J(v) = U~ v U / 8: the quarter turn is a rotor
        assert GA.eq(J(J(v)), GA.neg(v))
        # the cells of the stored structure: with last-plane component strictly between e5 and J(e5) the
        # point is in the open cell e_5, and J carries it into the next quarter plane, the cell g e_5
        x, y = GA.dot(v, e[4], sq), GA.dot(v, e[5], sq)
        assert x > 0 and y > 0
        w = J(v)
        assert GA.dot(w, e[4], sq) == -y and GA.dot(w, e[5], sq) == x
    assert GA.eq(GA.mul(Urev, U, sq), GA.scal(F(8), one))
    # the fibre: the even subalgebra of Cl(3,0) is the quaternions, and the generator acts on it by the
    # rotor of a full turn, -1 = (e1e2)^2
    s3 = GA.sig(len(SAMPLE_EVEN[0]) - 1, 0)
    f = [GA.gen(i) for i in range(len(SAMPLE_EVEN[0]) - 1)]
    unit = GA.mul(f[0], f[0], s3)
    biv = [GA.mul(f[1], f[2], s3), GA.mul(f[2], f[0], s3), GA.mul(f[0], f[1], s3)]
    for X in biv:
        assert GA.eq(GA.mul(X, X, s3), GA.neg(unit))
        for Y in biv:
            if X is not Y:
                assert GA.eq(GA.mul(X, Y, s3), GA.neg(GA.mul(Y, X, s3)))

    def even(coords):
        return GA.add(*[GA.scal(c, g) for c, g in zip(coords, [unit] + biv)])

    def norm(q):
        rev = GA.sub(GA.scal(2 * q.get((), F(0)), unit), q)      # the reverse: bivector part changes sign
        return GA.mul(q, rev, s3)
    for c1 in SAMPLE_EVEN:
        for c2 in SAMPLE_EVEN:
            q1, q2 = even(c1), even(c2)
            n1, n2, n12 = norm(q1), norm(q2), norm(GA.mul(q1, q2, s3))
            assert set(n1) <= {()} and set(n12) <= {()}    # q q~ is a scalar: four components, one sphere
            assert n1[()] == sum(c * c for c in c1) and n12[()] == n1[()] * n2[()]
            assert norm(GA.neg(q1)) == n1                  # the deck action -1 preserves the unit sphere


def check_product_cell_complex():
    premise(STORED)
    M = Bundle(QUARTER)
    count = 0
    for n in range(BASE_TOP + FIBRE_TOP + 1):
        for c in M.reps(n):
            count += 1
            twice = {}
            for x, v in M.bd(c).items():
                for y, w in M.bd(x).items():
                    twice[y] = twice.get(y, 0) + v * w
            assert all(v == 0 for v in twice.values())
            assert all(sum(c2[0] + c2[2] for c2 in [x]) == n - 1 for x in M.bd(c))
    assert count == ORBITS
    # the stored boundary formulas
    assert bd(2, 0, QUARTER) == {(1, 0): 1, (1, 1): 1, (1, 2): 1, (1, 3): 1}
    assert bd(3, 1, QUARTER) == {(2, 2): 1, (2, 1): -1}
    assert bd(3, 0, ANTI) == {(2, 1): 1, (2, 0): -1} and bd(2, 0, ANTI) == {(1, 0): 1, (1, 1): 1}
    # the projection to the base is a chain map: it keeps e_k (x) (vertex) and kills the rest
    for n in range(1, BASE_TOP + 1):
        for c in M.reps(n):
            image = {}
            for x, v in M.bd(c).items():
                if x[2] == 0:
                    image[(x[0], x[1])] = image.get((x[0], x[1]), 0) + v
            image = {x: v for x, v in image.items() if v}
            want = bd(c[0], c[1], QUARTER) if c[2] == 0 else {}
            assert image == want


def check_higher_diagonal_on_the_factors():
    premise(STORED)
    for (m, top) in ((QUARTER, BASE_TOP), (ANTI, FIBRE_TOP)):
        for k in range(top + 1):
            assert carried(delta0(k, m), k, m)                              # the stored diagonal is carried
            assert carried(delta1(k, m), k, m)
            assert all(p + q == k + 1 for (p, a, q, b) in delta1(k, m))     # degree + 1
            assert homotopy_defect(k, m, lambda j: delta1(j, m)) == set()
            # the transposed higher diagonal is another solution
            assert homotopy_defect(k, m, lambda j: swap(delta1(j, m))) == set()
    # term counts of the explicit formulas for the quarter turn
    assert [len(delta1(k, QUARTER)) for k in range(BASE_TOP + 1)] == [0, 1, 4, 4, 4, 5]
    # controls: with the full norm element in place of g + g^2 + g^3, or one term in place of the norm
    # element on e_2, the identity fails
    assert homotopy_defect(3, QUARTER, lambda j: delta1(j, QUARTER, shape=1)) != set()
    assert homotopy_defect(2, QUARTER, lambda j: delta1(j, QUARTER, shape=2)) != set()
    # the diagonal itself is not symmetric: the right-hand side is not zero
    assert delta0(2, QUARTER) != swap(delta0(2, QUARTER))


def check_higher_diagonal_on_the_product():
    premise(STORED)
    for formula in (0, 1):
        M = Bundle(QUARTER, formula=formula)
        for n in range(BASE_TOP + FIBRE_TOP + 1):
            for c in M.reps(n):
                assert M.defect(c) == set()
                k, a, q, b = c
                clc = closure(k, 0, QUARTER)
                cld = closure(q, b, ANTI)
                for (x, y) in M.high(c) | M.diag(c):
                    assert (x[0], x[1]) in clc and (y[0], y[1]) in clc
                    assert (x[2], x[3]) in cld and (y[2], y[3]) in cld
    # equivariance: the value on a translated cell is the translate (the generator moves both factors)
    M = Bundle(QUARTER)
    c = (3, 0, 2, 1)
    moved = M.high((3, 1, 2, 0))
    assert moved == M.move(M.high(c), 1, 1) and M.rep((3, 1, 2, 0)) == c


def check_fibre_class_is_an_integral_cocycle():
    premise(STORED)
    M = Bundle(QUARTER)
    th = M.theta()
    assert integral(th) and th[(2, 0, 1, 0)] == -1
    assert all(v == 0 for v in M.coboundary(th, DEG + 1).values())
    # value on the fibre over the base point, the cycle d_3 + T d_3: one
    assert th.get((0, 0, 3, 0), 0) + th.get((0, 0, 3, 1), 0) == 1
    # perturbed cochains are not cocycles
    for c in M.reps(DEG):
        bad = dict(th)
        bad[c] = bad.get(c, 0) + 1
        assert any(v != 0 for v in M.coboundary(bad, DEG + 1).values())
    # stored: the integral coboundary on the lens space is 0 into odd degrees and 4 into even degrees, so
    # a cocycle of degree 3 (coboundary 4 times its value) is zero: no integral class of degree three
    assert sum(bd(4, 0, QUARTER).values()) == 4 and sum(bd(3, 0, QUARTER).values()) == 0
    # and eps_5 is not a coboundary modulo 2 (the coboundary of eps_4 is zero)
    assert sum(bd(5, 0, QUARTER).values()) % 2 == 0


def check_cup_one_square_is_the_top_class():
    premise(STORED)
    seen = []
    for formula in (0, 1):
        for transposed in (False, True):
            M = Bundle(QUARTER, formula=formula, transposed=transposed)
            square = M.cup_one_square(M.theta())
            cob = M.coboundaries2(2 * DEG - 1)
            top = M.pullback_top()
            assert len(top) == 2 and all(c[0] == BASE_TOP for c in top)
            assert in_span(square ^ top, cob)               # Sq^2(rho theta) = p^*(x u^2)
            assert not in_span(square, cob)                 # and it is not zero
            assert not in_span(top, cob)                    # p^*(x u^2) is not zero on M
            # the square is a cocycle: it vanishes on boundaries of cells of degree 6
            for c in M.reps(2 * DEG):
                assert sum(1 for x in M.bd2(c) if M.rep(x) in square) % 2 == 0
            seen.append(sorted(square))
    # all four choices give the same cochain: 1 on e_4 (x) d_1 and e_4 (x) T d_1 (from the single pair
    # (e_2 (x) d_1) (x) (e_2 (x) d_1) of Delta_0(e_4) (x) Delta_1(d_1)), zero elsewhere
    assert all(sq == [(4, 0, 1, 0), (4, 0, 1, 1)] for sq in seen) and len(seen) == 4
    # and it differs from p^*(eps_5) by the coboundary of the cochain equal to 1 on e_4 (x) d_0
    M = Bundle(QUARTER)
    beta = M.coboundary({(4, 0, 0, 0): F(1)}, 2 * DEG - 1)
    assert {c for c, v in beta.items() if v % 2} == set(seen[0]) ^ M.pullback_top()
    # twice theta has square zero, and theta plus a coboundary has the same square class
    double = {c: 2 * v for c, v in M.theta().items()}
    assert M.cup_one_square(double) == set()
    for r in M.reps(DEG - 1):
        shifted = dict(M.theta())
        for c, v in M.coboundary({r: F(1)}, DEG).items():
            shifted[c] = shifted.get(c, 0) + v
        assert all(v == 0 for v in M.coboundary(shifted, DEG + 1).values())
        assert in_span(M.cup_one_square(shifted) ^ M.pullback_top(), M.coboundaries2(2 * DEG - 1))


def check_chain_level_section_exists():
    """phi : C -> D with phi(e_0) = d_0, phi(e_1) = d_1, phi(e_2) = 2 d_2, phi(e_3) = (1 - T) d_3, phi(e_4) =
    phi(e_5) = 0, extended by phi(g c) = T phi(c), is an integral chain map; sigma = (1 (x) phi) Delta_0 is then
    an equivariant chain map C -> C (x) D with (projection) sigma = identity."""
    premise(STORED)
    table = {0: {(0, 0): 1}, 1: {(1, 0): 1}, 2: {(2, 0): 2}, 3: {(3, 0): 1, (3, 1): -1}, 4: {}, 5: {}}

    def phi(k, a):
        return {(q, (b + a) % ANTI): v for (q, b), v in table[k].items()}

    def add_to(out, key, v):
        out[key] = out.get(key, 0) + v
        if not out[key]:
            del out[key]
    for k in range(BASE_TOP + 1):
        lhs = {}                                            # bd phi(e_k)
        for (q, b), v in phi(k, 0).items():
            for x, w in bd(q, b, ANTI).items():
                add_to(lhs, x, v * w)
        rhs = {}                                            # phi(bd e_k)
        for (kk, aa), v in bd(k, 0, QUARTER).items():
            for x, w in phi(kk, aa).items():
                add_to(rhs, x, v * w)
        assert lhs == rhs
    # the projection of sigma(e_k): the terms e_k (x) (vertex) of (1 (x) phi) Delta_0(e_k), with integer signs
    # all +1 in bidegree (k, 0); phi of a vertex is a vertex with coefficient 1
    for k in range(BASE_TOP + 1):
        kept = [(p, a, q, b) for (p, a, q, b) in delta0(k, QUARTER) if q == 0]
        assert len(kept) == 1 and kept[0][:2] == (k, 0)
        assert list(phi(0, kept[0][3]).values()) == [1]
    # phi(e_3) = 2 d_3, the first solution of the chain-map equation in degree 3, does not extend over e_4
    bad = {}
    for (kk, aa), v in bd(4, 0, QUARTER).items():
        add_to(bad, (3, aa % ANTI), 2 * v)
    assert bad != {}



def check_controls_other_orders_and_trivial_action():
    premise(STORED)
    # the factor identity for the other orders used
    for m in (6, 8, 12, 16):
        for k in range(BASE_TOP + 1):
            assert homotopy_defect(k, m, lambda j: delta1(j, m)) == set() and carried(delta1(k, m), k, m)
    verdict = {}
    for m in (4, 8, 12, 16):
        M = Bundle(m)
        th = M.theta()
        assert integral(th) and all(v == 0 for v in M.coboundary(th, DEG + 1).values())
        square = M.cup_one_square(th)
        cob = M.coboundaries2(2 * DEG - 1)
        assert in_span(square, cob) != in_span(square ^ M.pullback_top(), cob)
        verdict[m] = not in_span(square, cob)
    assert verdict == {4: True, 8: False, 12: True, 16: False}       # obstructed exactly for order 4 modulo 8
    # orders 2 and 6: the cocycle equations force an even value on the fibre (the cochain theta is not integral)
    for m in (2, 6):
        M = Bundle(m)
        assert not integral(M.theta())
        assert all(v == 0 for v in M.coboundary(M.theta(), DEG + 1).values())
    # trivial action on the fibre (the product L x S^3, which has sections): the fibre cocycle 1 on e_0 (x) d_3
    # and e_0 (x) T d_3 ... has square a coboundary
    M = Bundle(QUARTER, act=0)
    th = {(0, 0, 3, 0): F(1)}
    assert all(v == 0 for v in M.coboundary(th, DEG + 1).values())
    assert in_span(M.cup_one_square(th), M.coboundaries2(2 * DEG - 1))
    assert not in_span(M.pullback_top(), M.coboundaries2(2 * DEG - 1))
    # base S^3 (the lens space L^3(4), stored count three): p^*(eps_5) does not exist and the square is zero
    M = Bundle(QUARTER, top=3)
    assert all(v == 0 for v in M.coboundary(M.theta(), DEG + 1).values())
    assert in_span(M.cup_one_square(M.theta()), M.coboundaries2(2 * DEG - 1))
