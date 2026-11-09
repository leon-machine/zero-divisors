"""synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure: exact checks.

The sphere S^{2n+1} with the free action of Z_m (m = 4: the quarter turn J(v) = v . B in every coordinate plane)
has one free cell e_k in each dimension, with boundary (g - 1) e_{k-1} for k odd and N e_{k-1} for k even,
N = 1 + g + ... + g^{m-1}. Chains are dicts {(k, a): n} for n g^a e_k; tensors {(p, a, q, b): n}. Checks:
  (1) the quarter turn in GA (Cl(6,0)): J^2 = -1, orthogonal, free on the sphere, J(v) tangent at v;
  (2) the cell complex: d^2 = 0 and exactness in the middle degrees (ranks of g - 1 and N on the group ring);
  (3) the diagonal approximation is an equivariant chain map that preserves the augmentation; the four
      group-ring identities that prove it for every degree;
  (4) cup products and Bocksteins read from it: integral, mod 2 and mod 4; the m = 2 control (projective space);
  (5) the sections that compute the Euler classes of the quarter-turn and half-turn plane bundles;
  (6) the presented ring Z[s]/((1+s)^4 - 1, s^{n+1}): order 4^n of its augmentation ideal and the order of
      1 - (1+s)^2.
"""
from fractions import Fraction as F
import GA

M4 = 4
ORDERS = (2, 3, 4)        # group orders for which the diagonal is tested
TOP = 9                   # highest cell dimension tested
ID = 0                    # the identity translate g^0
MORE_ORDERS = (2, 3, 4, 5, 6, 8)   # group orders for the four group-ring identities


def bd(k, a, m):
    """Boundary of g^a e_k."""
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


def acc(A, B, s=1):
    C = dict(A)
    for x, v in B.items():
        C[x] = C.get(x, 0) + s * v
        if not C[x]:
            del C[x]
    return C


def bd_chain(ch, m):
    out = {}
    for (k, a), c in ch.items():
        out = acc(out, bd(k, a, m), c)
    return out


def delta(k, a, m, twist=1):
    """Delta(g^a e_k) = sum over p + q = k of: e_p (x) e_q (p even); e_p (x) g e_q (p odd, q even);
    sum_{i<j} g^i e_p (x) g^j e_q (p, q odd); all translated by g^a (diagonal action)."""
    out = {}
    for p in range(k + 1):
        q = k - p
        if p % 2 == 0:
            terms = [(0, 0)]
        elif q % 2 == 0:
            terms = [(0, twist)]
        else:
            terms = [(i, j) for i in range(m) for j in range(i + 1, m)]
        for (i, j) in terms:
            out[(p, (a + i) % m, q, (a + j) % m)] = 1
    return out


def bd_tensor(T, m):
    out = {}
    for (p, a, q, b), v in T.items():
        for (pp, aa), c in bd(p, a, m).items():
            out = acc(out, {(pp, aa, q, b): v * c})
        for (qq, bb), c in bd(q, b, m).items():
            out = acc(out, {(p, a, qq, bb): v * c * (-1) ** p})
    return out


def delta_chain(ch, m, twist=1):
    out = {}
    for (k, a), c in ch.items():
        out = acc(out, delta(k, a, m, twist), c)
    return out


def cup_coefficient(p, q, m):
    """(eps_p cup eps_q)(e_{p+q}) for the invariant cochains eps_k (value 1 on every g^a e_k)."""
    return sum(v for (pp, a, qq, b), v in delta(p + q, 0, m).items() if pp == p)


def check_quarter_turn_in_the_algebra():
    sq = GA.sig(6, 0)
    B = GA.add(GA.mul(GA.gen(0), GA.gen(1), sq), GA.mul(GA.gen(2), GA.gen(3), sq), GA.mul(GA.gen(4), GA.gen(5), sq))

    def J(v):
        w = GA.mul(v, B, sq)
        return {k: c for k, c in w.items() if len(k) == 1}
    vs = [GA.add(GA.scal(F(1 + i), GA.gen(i)), GA.scal(F(2 - i), GA.gen((i + 3) % 6)), GA.gen((i + 1) % 6))
          for i in range(6)]
    for v in vs:
        assert GA.eq(J(J(v)), GA.neg(v))                                     # J^2 = -1, so J^4 = 1
        assert GA.mul(J(v), J(v), sq) == GA.mul(v, v, sq)                    # Q(Jv) = Q(v)
        assert GA.dot(v, J(v), sq) == 0 and GA.dot(v, v, sq) != 0             # Jv tangent at v
        for a in (1, 2, 3):
            w = v
            for _ in range(a):
                w = J(w)
            assert not GA.eq(w, v)                                           # free on nonzero vectors
    # J^a - 1 is invertible on vectors for a = 1, 2, 3: rank 6
    for a in (1, 2, 3):
        rows = []
        for i in range(6):
            w = GA.gen(i)
            for _ in range(a):
                w = J(w)
            d = GA.sub(w, GA.gen(i))
            rows.append([d.get((j,), F(0)) for j in range(6)])
        assert GA.field_rank(rows) == 6


def check_cell_complex():
    for m in (2, 4):
        for k in range(2, 12):
            assert bd_chain(bd(k, 0, m), m) == {}
        # on the group ring: g - 1 has rank m - 1 and N has rank 1, so ker(g - 1) = im N and ker N = im(g - 1)
        gm1 = [[F(bd(1, a, m).get((0, b), 0)) for b in range(m)] for a in range(m)]
        nn = [[F(bd(2, a, m).get((1, b), 0)) for b in range(m)] for a in range(m)]
        assert GA.field_rank(gm1) == m - 1 and GA.field_rank(nn) == 1
        assert all(sum(row) == 0 for row in gm1) and all(row == nn[0] for row in nn)
    assert bd(2, 0, M4) == {(1, 0): 1, (1, 1): 1, (1, 2): 1, (1, 3): 1}
    assert bd(3, 1, M4) == {(2, 2): 1, (2, 1): -1}


def check_diagonal_approximation_is_a_chain_map():
    for m in ORDERS:
        for k in range(TOP + 1):
            assert bd_tensor(delta(k, ID, m), m) == delta_chain(bd(k, ID, m), m)
        assert delta(ID, ID, m) == {(ID, ID, ID, ID): 1}                    # augmentation preserved
    # term counts: e_4 has 3 even-even terms and 2 * 6 odd-odd ones; e_5 has 6 terms; e_9 has 10
    assert len(delta(4, ID, M4)) == 15 and len(delta(5, ID, M4)) == 6 and len(delta(TOP, ID, M4)) == 10
    assert sum(bd_tensor(delta(4, ID, M4), M4).values()) == 16 and len(bd_tensor(delta(3, ID, M4), M4)) == 10
    # the formula without the twist by g (e_p (x) e_q for p odd, q even), or with g^2, is not a chain map
    assert bd_tensor(delta(3, ID, M4, twist=ID), M4) != delta_chain(bd(3, ID, M4), M4, twist=ID)
    assert bd_tensor(delta(3, ID, M4, twist=2), M4) != delta_chain(bd(3, ID, M4), M4, twist=2)


def gg_mul(x, y, m):
    """Product in the group ring Z[G x G]: dicts {(a, b): n} for n g^a (x) g^b."""
    out = {}
    for (a1, b1), u in x.items():
        for (a2, b2), v in y.items():
            k = ((a1 + a2) % m, (b1 + b2) % m)
            out[k] = out.get(k, 0) + u * v
            if not out[k]:
                del out[k]
    return out


def gg_add(*xs):
    out = {}
    for sgn, x in xs:
        out = acc(out, x, sgn)
    return out


def check_four_group_ring_identities():
    """The chain-map condition in bidegree (p, q) depends on parities only: four identities in Z[G x G]."""
    for m in MORE_ORDERS:
        one = {(ID, ID): 1}
        g1 = {(1, ID): 1}                                   # g (x) 1
        g2 = {(ID, 1): 1}                                   # 1 (x) g
        gg = {(1, 1): 1}                                    # g (x) g
        N1 = {(a, ID): 1 for a in range(m)}                 # N (x) 1
        N2 = {(ID, a): 1 for a in range(m)}                 # 1 (x) N
        diag = {(a, a): 1 for a in range(m)}
        T = {(r, j): 1 for r in range(m) for j in range(r + 1, m)}
        assert len(T) == m * (m - 1) // 2
        # (even, even)
        assert gg_add((1, gg_mul(g2, gg_add((1, g1), (-1, one)), m)), (1, g2), (-1, one)) == gg_add((1, gg), (-1, one))
        # (odd, even): N (x) 1 - T (1 (x) g - 1) = diag (1 (x) g)
        assert gg_add((1, N1), (-1, gg_mul(T, gg_add((1, g2), (-1, one)), m))) == gg_mul(diag, g2, m)
        # (even, odd): T (g (x) 1 - 1) + 1 (x) N = diag
        assert gg_add((1, gg_mul(T, gg_add((1, g1), (-1, one)), m)), (1, N2)) == diag
        # (odd, odd): N (x) 1 - 1 (x) N = (g (x) g - 1) T
        assert gg_add((1, N1), (-1, N2)) == gg_mul(gg_add((1, gg), (-1, one)), T, m)
        # the form with N (x) g - 1 (x) N on the right is false
        if m > 2:
            assert gg_mul(gg_add((1, gg), (-1, one)), T, m) != gg_add((1, gg_mul(N1, g2, m)), (-1, N2))


def check_cup_products_and_bocksteins():
    m = M4
    n = 4                                                                    # L^9(4): cells e_0 .. e_9
    for p in range(0, 2 * n + 2):
        for q in range(0, 2 * n + 2 - p):
            c = cup_coefficient(p, q, m)
            assert c == (6 if (p % 2 and q % 2) else 1)
    # integral cochains: (delta eps_{2i-1})(e_{2i}) = eps_{2i-1}(N e_{2i-1}) = 4, delta eps_{2i} = 0
    for i in range(1, n + 1):
        assert sum(bd(2 * i, 0, m).values()) == 4 and sum(bd(2 * i + 1, 0, m).values()) == 0
    # H^{2i}(Z) = Z_4 generated by y^i = eps_{2i}: products of even cochains have coefficient 1
    assert all(cup_coefficient(2, 2 * i, m) == 1 for i in range(1, n))
    # mod 2: x = eps_1, x^2 = 6 eps_2 = 0; x u^i = eps_{2i+1} with coefficient 1
    assert cup_coefficient(1, 1, m) % 2 == 0
    assert all(cup_coefficient(1, 2 * i, m) % 2 == 1 for i in range(0, n + 1))
    # mod 4: the square of the degree-one generator is 2 eps_2, nonzero
    assert cup_coefficient(1, 1, m) % 4 == 2
    # Bocksteins: the integral Bockstein of x is (delta eps_1)/2 = 2 eps_2, of order two in Z_4;
    # the Bockstein of Z_2 -> Z_4 -> Z_2 is (delta eps_odd)/2 mod 2 = 0 in every degree
    d = sum(bd(2, 0, m).values())
    assert d // 2 == 2 and (d // 2) % 4 != 0 and (2 * (d // 2)) % 4 == 0
    assert (d // 2) % 2 == 0
    # control: m = 2 is real projective space, where x^2 = eps_2 is not zero and the Bockstein is not zero
    assert cup_coefficient(1, 1, 2) % 2 == 1 and (sum(bd(2, 0, 2).values()) // 2) % 2 == 1


def check_euler_class_sections():
    sq = GA.sig(2, 0)
    e1, e2 = GA.gen(0), GA.gen(1)
    B = GA.mul(e1, e2, sq)
    for (c, s) in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(-8, 17), F(15, 17))):
        v = GA.add(GA.scal(c, e1), GA.scal(s, e2))
        Jv = {k: x for k, x in GA.mul(v, B, sq).items() if len(k) == 1}
        assert GA.eq(Jv, GA.add(GA.scal(-s, e1), GA.scal(c, e2)))               # the quarter turn of the plane
        # s1(v) = v: s1(Jv) = J s1(v), one turn around the circle (the identity map): Euler number 1
        # s2(v) = v e1 v: s2(Jv) = -s2(v), and it is the double-angle map: two turns, Euler number 2
        s2 = GA.mul(GA.mul(v, e1, sq), v, sq)
        s2J = GA.mul(GA.mul(Jv, e1, sq), Jv, sq)
        assert GA.eq(s2J, GA.neg(s2))
        assert GA.eq(s2, GA.add(GA.scal(c * c - s * s, e1), GA.scal(2 * c * s, e2)))
        assert GA.mul(s2, s2, sq) == GA.mul(v, v, sq)                         # nowhere zero on the circle


def ideal_orders(n):
    """Augmentation ideal of Z[s]/((1+s)^4 - 1, s^{n+1}) on the basis s, ..., s^n: relation rows s^j R,
    R = 4s + 6s^2 + 4s^3 + s^4. Returns (order of the ideal, order of the element -(2s + s^2))."""
    R = [4, 6, 4, 1]
    T = [[R[c - j] if 0 <= c - j < 4 else 0 for c in range(n)] for j in range(n)]
    det = 1
    for j in range(n):
        det *= T[j][j]
    v = [F(-2) if c == 0 else (F(-1) if c == 1 else F(0)) for c in range(n)]
    w = []                                                                   # v = w T, T upper triangular
    for c in range(n):
        w.append((v[c] - sum(w[j] * T[j][c] for j in range(c))) / T[c][c])
    order = 1
    for x in w:
        den = x.denominator
        g, a, b = order, order, den
        while b:
            a, b = b, a % b
        order = g * den // a
    return det, order


def check_presented_ring_orders():
    want = {1: 2, 2: 2, 3: 4, 4: 4, 5: 8, 6: 8, 7: 16, 8: 16, 9: 32, 10: 32, 11: 64, 12: 64, 13: 128, 14: 128}
    for n in range(1, 15):
        det, order = ideal_orders(n)
        assert det == 4 ** n
        assert order == want[n] == 2 ** ((n + 1) // 2)
    # so 2(1 - xi) is zero in the presented ring for n = 1, 2 and not for n = 3
    assert ideal_orders(2)[1] == 2 and ideal_orders(3)[1] == 4
