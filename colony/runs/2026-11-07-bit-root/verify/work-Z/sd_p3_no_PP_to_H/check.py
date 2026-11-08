"""synthesis.signed-directions-and-the-integer-clifford-algebra: exact checks.

A configuration S of the n directions is a bitmask; e_S is the increasing product. The group G of
the premise is built from its relations alone, by rewriting words in the letters c, e_1, ..., e_n
(c central, c^2 = 1, e_i e_i -> c^{s_i}, e_i e_j -> c e_j e_i for i > j); s is the sign vector
(s_i = 1 when e_i^2 = c). The algebra A = Z[G]/(c + 1) is built from the integer group ring.
Everything is exact: integers for Z, Fractions (GA.py) where an algebra over Q or R is compared.
(1) The sign: two directions force c^2 = 1 (the Heisenberg group mod k reads its relation both ways
    only for k = 2); for one direction the clause is independent (Z_{2m} with c = e^2).
(2) Normal form and table: the rewriting product is associative with 2^{n+1} elements, equals the
    GA product of blades with c -> -1, every square and commutator lies in {1, c}, and q, b have the
    closed forms C(|S|,2) + |S cap N| and |S||T| + |S cap T|.
(3) Centre: {1, c} for n even (extraspecial: centre = commutators = squares), {1, c, e_full,
    c e_full} for n odd; central involutions other than 1: c alone unless n odd and q(full) = 0.
(4) The integer algebra: the ideal (c + 1) is the Z-span of the (1 + c) e_S, the quotient is free
    of rank 2^n with blade basis, structure constants are integers equal to the GA ones, and
    v^2 = Q(v) for integer and rational vectors.
(5) Universal property: maps of the directions to anticommuting elements of square (-1)^{s_i} in
    Cl(p+1, q+1) (twisted generators), in rotor-conjugated frames and in A itself extend to
    algebra maps, multiplicative on every pair of blades; base change to F_2 gives the commutative
    group algebra of the configurations.
(6) Classification: for every pair of signatures of the same n <= 6, the forms are equivalent over
    F_2 exactly when the Gauss sums agree; an explicit F_2-isometry is built and lifted to anticommuting
    blades in GA, giving the algebra isomorphism over Z (blades to signed blades); the trace form
    Tr(L_{xy}) / 2^n is the scalar part and is diagonal in the blades with entries e_S^2.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise


# ---------------------------------------------------------------- helpers (not mutated)

def idx(mask, n):
    return [i for i in range(n) if mask >> i & 1]


def popcount(m):
    return bin(m).count("1")


def reduce_word(word, s):
    """Normal form (a, mask) of a word in 'c' and direction indices, from the relations only."""
    a = sum(1 for x in word if x == "c")
    lst = [x for x in word if x != "c"]
    i = 0
    while i < len(lst) - 1:
        if lst[i] < lst[i + 1]:
            i += 1
        elif lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]      # e_i e_j = c e_j e_i
            a += 1
            i = max(i - 1, 0)
        else:
            a += s[lst[i]]                                  # e_i e_i = c^{s_i}
            del lst[i:i + 2]
            i = max(i - 1, 0)
    mask = 0
    for x in lst:
        assert not mask >> x & 1
        mask |= 1 << x
    assert lst == sorted(lst)
    return (a % 2, mask)


def gmul(x, y, s):
    n = len(s)
    return reduce_word(["c"] * x[0] + idx(x[1], n) + ["c"] * y[0] + idx(y[1], n), s)


def elements(n):
    return [(a, m) for a in (0, 1) for m in range(2 ** n)]


def ginv(x, s):
    return [y for y in elements(len(s)) if gmul(x, y, s) == (0, 0)][0]


def squares_of(s):
    return tuple(1 if t == 0 else -1 for t in s)


def blade(mask, n):
    return tuple(idx(mask, n))


def ga_elem(x, n):
    return {blade(x[1], n): F(-1) ** x[0]}


def qf(s):
    n = len(s)
    return [reduce_word(idx(m, n) + idx(m, n), s)[0] for m in range(2 ** n)]


def bform(qv, x, y):
    return qv[x ^ y] ^ qv[x] ^ qv[y]


def gauss(qv):
    return sum(1 - 2 * t for t in qv)


def sign_vectors(n):
    return [tuple(v) for v in product((0, 1), repeat=n)]


# integer algebra A = Z[G]/(c + 1): elements {mask: int}
def amul(x, y, s):
    out = {}
    n = len(s)
    for m1, c1 in x.items():
        for m2, c2 in y.items():
            a, m = gmul((0, m1), (0, m2), s)
            out[m] = out.get(m, 0) + (-1) ** a * c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def quotient(z):
    """Z[G] -> A: c^a e_S -> (-1)^a e_S; z = {(a, mask): int}."""
    out = {}
    for (a, m), k in z.items():
        out[m] = out.get(m, 0) + (-1) ** a * k
    return {m: c for m, c in out.items() if c != 0}


def gring_mul(x, y, s):
    out = {}
    for g, c1 in x.items():
        for h, c2 in y.items():
            k = gmul(g, h, s)
            out[k] = out.get(k, 0) + c1 * c2
    return {k: c for k, c in out.items() if c != 0}


def det_int(M):
    """Exact determinant (Fractions, Bareiss-free elimination)."""
    M = [[F(v) for v in row] for row in M]
    n, d = len(M), F(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return F(0)
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            d = -d
        d *= M[col][col]
        for r in range(col + 1, n):
            f = M[r][col] / M[col][col]
            M[r] = [M[r][j] - f * M[col][j] for j in range(n)]
    return d


# F_2 linear algebra on bitmasks
def solve_f2(basis, x):
    """Coordinates of x in the F_2-basis (list of masks); exact Gaussian elimination."""
    n = len(basis)
    rows = [(basis[k], 1 << k) for k in range(n)]
    red = []
    for v, tag in rows:
        for (pv, pt, bit) in red:
            if v >> bit & 1:
                v ^= pv
                tag ^= pt
        if v:
            bit = v.bit_length() - 1
            red2 = []
            for (pv, pt, b2) in red:
                if pv >> bit & 1:
                    pv ^= v
                    pt ^= tag
                red2.append((pv, pt, b2))
            red = red2 + [(v, tag, bit)]
    assert len(red) == n
    coord = 0
    for (pv, pt, bit) in red:
        if x >> bit & 1:
            x ^= pv
            coord ^= pt
    assert x == 0
    return coord


def canon(qv, n):
    """A basis in which q is H + ... + H (+ P) (+ <z>), and its type (#P, q(z) or None)."""
    full = 2 ** n - 1
    z = full if n % 2 else None
    if z is not None:
        assert all(bform(qv, z, 1 << i) == 0 for i in range(n))
        W = [1 << i for i in range(n - 1)]
    else:
        W = [1 << i for i in range(n)]
    pairs = []

    def reduce_pairs(vecs):
        out = []
        vecs = list(vecs)
        while vecs:
            u = vecs.pop(0)
            k = next(k for k, w in enumerate(vecs) if bform(qv, u, w) == 1)
            w = vecs.pop(k)
            vecs = [v ^ (u if bform(qv, v, w) else 0) ^ (w if bform(qv, v, u) else 0) for v in vecs]
            if qv[u] == 0 and qv[w] == 1:
                w ^= u
            elif qv[u] == 1 and qv[w] == 0:
                u ^= w
            out.append((u, w))
        return out

    pairs = reduce_pairs(W)
    while True:
        Ps = [pr for pr in pairs if qv[pr[0]] == 1]
        if len(Ps) < 3:
            break
        (u1, w1), (u2, w2) = Ps[0], Ps[1]
        rest = [pr for pr in pairs if pr not in (Ps[0], Ps[1])]
        new = reduce_pairs([u1 ^ u2, w1 ^ u2, u1, w2])
        pairs = rest + new
    Ps = [pr for pr in pairs if qv[pr[0]] == 1]
    if z is not None and qv[z] == 1 and Ps:
        (u, w) = Ps[0]
        pairs = [pr for pr in pairs if pr != Ps[0]] + reduce_pairs([u ^ z, w])
        Ps = [pr for pr in pairs if qv[pr[0]] == 1]
    Hs = [pr for pr in pairs if qv[pr[0]] == 0]
    for (u, w) in Hs:
        assert qv[u] == 0 and qv[w] == 0 and bform(qv, u, w) == 1
    basis = [v for pr in Hs + Ps for v in pr] + ([z] if z is not None else [])
    return basis, (len(Ps), None if z is None else qv[z])


def isometry(s, t):
    """An F_2-linear bijection A with q_t(A x) = q_s(x), or None; built from the canonical bases."""
    n = len(s)
    qs, qt = qf(s), qf(t)
    bs, ts_ = canon(qs, n)
    bt, tt = canon(qt, n)
    if ts_ != tt:
        return None

    def A(x):
        c = solve_f2(bs, x)
        y = 0
        for k in range(n):
            if c >> k & 1:
                y ^= bt[k]
        return y
    return A


# ---------------------------------------------------------------- checks

def check_the_sign_bit_is_forced():
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    # two directions: Heisenberg group mod k, (x,y,z)(x',y',z') = (x+x', y+y', z+z'+x y');
    # e1 e2 = c e2 e1 with c = (0,0,1); the exchanged relation e2 e1 = c e1 e2 holds iff c^2 = 1
    both_ways = []
    for k in range(2, 8):
        def hm(u, v):
            return ((u[0] + v[0]) % k, (u[1] + v[1]) % k, (u[2] + v[2] + u[0] * v[1]) % k)
        e1, e2, c = (1, 0, 0), (0, 1, 0), (0, 0, 1)
        assert hm(e1, e2) == hm(c, hm(e2, e1))
        sym = hm(e2, e1) == hm(c, hm(e1, e2))
        csq = hm(c, c) == (0, 0, 0)
        assert sym == csq
        both_ways.append(sym)
    assert both_ways == [True, False, False, False, False, False]
    # in the group of the premise (n >= 2) the relation holds both ways and c^2 = 1
    for s in ((0, 0), (0, 1), (1, 1), (0, 1, 1)):
        c = (1, 0)
        assert gmul(c, c, s) == (0, 0)
        e1, e2 = (0, 1), (0, 2)
        assert gmul(e1, e2, s) == gmul(c, gmul(e2, e1, s), s)
        assert gmul(e2, e1, s) == gmul(c, gmul(e1, e2, s), s)
    # one direction: Z_{2m}, e = 1, c = e^2 = 2: c central, c != 1, G/<c> of order 2,
    # and c^2 = 1 exactly when m = 2: the order clause is independent at n = 1
    orders = []
    for m in range(2, 8):
        N = 2 * m
        c = 2 % N
        sub = {(c * t) % N for t in range(N)}
        assert c != 0 and N // len(sub) == 2
        orders.append(len(sub))
        assert ((2 * c) % N == 0) == (m == 2)
    assert orders == [2, 3, 4, 5, 6, 7]
    return True


def check_normal_form_table_squares_commutators():
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    count = 0
    for n in range(1, 6):
        for s in sign_vectors(n):
            if n == 5 and s != tuple(sorted(s)):
                continue
            Sq = squares_of(s)
            E = elements(n)
            assert len(set(E)) == 2 ** (n + 1)
            neg = sum(1 << i for i in range(n) if s[i])
            qv = qf(s)
            for x in E:
                for y in E:
                    xy = gmul(x, y, s)
                    # the rewriting product is the GA product of signed blades with c -> -1
                    assert GA.eq(ga_elem(xy, n), GA.mul(ga_elem(x, n), ga_elem(y, n), Sq))
                    yx = gmul(y, x, s)
                    comm = gmul(gmul(x, y, s), ginv(yx, s), s) if n <= 3 else None
                    if comm is not None:
                        assert comm in ((0, 0), (1, 0))
                    # commutator form b(S, T) = |S||T| + |S cap T|, read from xy = c^b yx
                    b = 0 if xy == yx else 1
                    assert xy == (yx[0] ^ b, yx[1])
                    assert b == (popcount(x[1]) * popcount(y[1]) + popcount(x[1] & y[1])) % 2
                    assert b == bform(qv, x[1], y[1])
                sq = gmul(x, x, s)
                assert sq[1] == 0 and sq[0] == qv[x[1]]
                k = popcount(x[1])
                assert qv[x[1]] == (k * (k - 1) // 2 + popcount(x[1] & neg)) % 2
            if n <= 3:
                for x in E:
                    for y in E:
                        for z in E:
                            assert gmul(gmul(x, y, s), z, s) == gmul(x, gmul(y, z, s), s)
            if n >= 2:
                sqs = {gmul(x, x, s) for x in E}
                assert sqs == {(0, 0), (1, 0)}
            count += 1
    assert count == 2 + 4 + 8 + 16 + 6
    return True


def check_centre_and_extraspecial():
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    seen = []
    for n in range(1, 6):
        for p in range(n + 1):
            s = tuple([0] * p + [1] * (n - p))
            E = elements(n)
            Z = [x for x in E if all(gmul(x, y, s) == gmul(y, x, s) for y in E)]
            full = 2 ** n - 1
            if n % 2 == 0:
                assert Z == [(0, 0), (1, 0)]
            else:
                assert sorted(Z) == [(0, 0), (0, full), (1, 0), (1, full)]
            invol = [x for x in Z if x != (0, 0) and gmul(x, x, s) == (0, 0)]
            qfull = qf(s)[full]
            assert len(invol) == (1 if n % 2 == 0 or qfull == 1 else 3)
            comms = {gmul(gmul(x, y, s), ginv(gmul(y, x, s), s), s) for x in E for y in E}
            sqs = {gmul(x, x, s) for x in E}
            if n % 2 == 0:
                # extraspecial: centre = commutator subgroup = squares = {1, c}, order 2^{1+n}
                assert set(Z) == comms == sqs == {(0, 0), (1, 0)} and len(E) == 2 ** (1 + n)
            seen.append((n, p, len(Z), len(invol)))
    assert len(seen) == 20
    assert [x for x in seen if x[0] == 3] == [(3, 0, 4, 3), (3, 1, 4, 1), (3, 2, 4, 3), (3, 3, 4, 1)]
    return True


def check_integer_algebra_free_and_contraction():
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    total = 0
    for n in range(1, 5):
        for s in sign_vectors(n):
            Sq = squares_of(s)
            E = elements(n)
            cp1 = {(1, 0): 1, (0, 0): 1}
            # the two-sided ideal (c + 1): every g (c + 1) h is (c + 1) gh, in the span of (1 + c) e_S
            span = {m: {(0, m): 1, (1, m): 1} for m in range(2 ** n)}
            for g in E:
                for h in E:
                    z = gring_mul(gring_mul({g: 1}, cp1, s), {h: 1}, s)
                    m = gmul(g, h, s)[1]
                    assert z == span[m]
                    assert quotient(z) == {}
            # a Z-basis of Z[G]: the (1 + c) e_S and the e_S (unimodular), so A is free on the e_S
            cols = [(0, m) for m in range(2 ** n)] + [(1, m) for m in range(2 ** n)]
            M = [[span[m].get(cc, 0) for cc in cols] for m in range(2 ** n)]
            M += [[1 if cc == (0, m) else 0 for cc in cols] for m in range(2 ** n)]
            assert abs(det_int(M)) == 1
            # quotient is a ring map; structure constants are integers and equal to GA's
            for x in E:
                for y in E:
                    lhs = quotient(gring_mul({x: 1}, {y: 1}, s))
                    rhs = amul(quotient({x: 1}), quotient({y: 1}), s)
                    assert lhs == rhs
            for m1 in range(2 ** n):
                for m2 in range(2 ** n):
                    pr = amul({m1: 1}, {m2: 1}, s)
                    ga = GA.mul({blade(m1, n): F(1)}, {blade(m2, n): F(1)}, Sq)
                    assert {blade(m, n): F(c) for m, c in pr.items()} == ga
            # v^2 = Q(v) for integer vectors with entries in [-2, 2]
            for a in product(range(-2, 3), repeat=n):
                v = {1 << i: a[i] for i in range(n) if a[i]}
                Qv = sum((-1) ** s[i] * a[i] ** 2 for i in range(n))
                assert amul(v, v, s) == ({0: Qv} if Qv else {})
                total += 1
    assert total == 2 * 5 + 4 * 25 + 8 * 125 + 16 * 625
    # over Q (base change): v^2 = Q(v) with rational coefficients in Cl(p,q)
    for p, q in ((3, 0), (1, 3), (2, 2)):
        S = GA.sig(p, q)
        coeffs = [F(1, 2), F(-2, 3), F(5, 7), F(3, 4)]
        v = GA.add(*[GA.scal(coeffs[i], GA.gen(i)) for i in range(p + q)])
        Qv = sum(S[i] * coeffs[i] ** 2 for i in range(p + q))
        assert GA.eq(GA.mul(v, v, S), GA.sc(Qv))
    return True


def check_universal_property_and_base_change():
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    cases = 0
    for p, q in ((1, 0), (0, 1), (2, 0), (1, 1), (0, 2), (3, 0), (1, 2), (2, 2), (1, 3)):
        n = p + q
        s = tuple([0] * p + [1] * q)
        Sq = squares_of(s)
        targets = []
        # (a) twisted generators x_i omega in Cl(p+1, q+1), omega = e f
        B1 = tuple(list(Sq) + [1, -1])
        om = {(n, n + 1): F(1)}
        targets.append((B1, [GA.mul(GA.gen(i), om, B1) for i in range(n)]))
        # (b) a frame conjugated by the rational rotor R = 2 + e_1 e_2 (or 2 + e_1 for n = 1)
        Rr = GA.add(GA.sc(2), {(0, 1): F(1)} if n >= 2 else {(0,): F(1)})
        Rb = GA.reverse(Rr) if n >= 2 else GA.grade_inv(Rr)
        RR = GA.mul(Rr, Rb, Sq)
        assert list(RR) == [()]
        Rinv = GA.scal(F(1) / RR[()], Rb)
        assert GA.eq(GA.mul(Rr, Rinv, Sq), GA.sc(1))
        targets.append((Sq, [GA.mul(GA.mul(Rr, GA.gen(i), Sq), Rinv, Sq) for i in range(n)]))
        # (c) the grade involution of A itself: e_i -> -e_i (integer coefficients)
        targets.append((Sq, [GA.neg(GA.gen(i)) for i in range(n)]))
        for B, u in targets:
            for i in range(n):
                assert GA.eq(GA.mul(u[i], u[i], B), GA.sc(Sq[i]))
                for j in range(i):
                    assert GA.anticommutes(u[i], u[j], B)
            # F(e_S) = product of the u_i; multiplicative on all blades
            def Fm(m):
                x = GA.sc(1)
                for i in idx(m, n):
                    x = GA.mul(x, u[i], B)
                return x
            for m1 in range(2 ** n):
                for m2 in range(2 ** n):
                    pr = amul({m1: 1}, {m2: 1}, s)
                    lhs = GA.add(*[GA.scal(c, Fm(m)) for m, c in pr.items()])
                    assert GA.eq(lhs, GA.mul(Fm(m1), Fm(m2), B))
            cases += 1
    assert cases == 27
    # base change to F_2: structure constants reduce to e_S e_T = e_{S xor T}, commutative
    for s in sign_vectors(3):
        for m1 in range(8):
            for m2 in range(8):
                pr = amul({m1: 1}, {m2: 1}, s)
                assert len(pr) == 1 and list(pr)[0] == m1 ^ m2 and pr[m1 ^ m2] % 2 == 1
    return True


def check_classification_by_gauss_sum():
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    pairs_iso = 0
    pairs_non = 0
    for n in range(1, 7):
        sigs = [tuple(v) for v in sign_vectors(n)] if n <= 3 else \
            [tuple([0] * p + [1] * (n - p)) for p in range(n + 1)]
        for s in sigs:
            for t in sigs:
                qs, qt = qf(s), qf(t)
                A = isometry(s, t)
                same = gauss(qs) == gauss(qt)
                assert (A is not None) == same
                if A is None:
                    pairs_non += 1
                    continue
                imgs = [A(1 << i) for i in range(n)]
                assert solve_f2(imgs, 2 ** n - 1) >= 0          # A is bijective
                for x in range(2 ** n):
                    y = 0
                    for i in idx(x, n):
                        y ^= imgs[i]
                    assert y == A(x) and qt[y] == qs[x]
                # lift: u_i = e'_{A(i)} in the algebra of t; Clifford relations of s
                if n <= 4:
                    Bt = squares_of(t)
                    u = [{blade(imgs[i], n): F(1)} for i in range(n)]
                    for i in range(n):
                        assert GA.eq(GA.mul(u[i], u[i], Bt), GA.sc(squares_of(s)[i]))
                        for j in range(i):
                            assert GA.anticommutes(u[i], u[j], Bt)
                    # images of the blades are signed blades, all distinct: an iso over Z
                    imgb = set()
                    for m in range(2 ** n):
                        x = GA.sc(1)
                        for i in idx(m, n):
                            x = GA.mul(x, u[i], Bt)
                        assert len(x) == 1 and abs(list(x.values())[0]) == 1
                        imgb.add(list(x)[0])
                    assert len(imgb) == 2 ** n
                pairs_iso += 1
    assert (pairs_iso, pairs_non) == (90, 104)
    # Cl(2,0) = Cl(1,1) over Z; Cl(1,0) and Cl(0,1) are not isomorphic (Gauss sums 2 and 0)
    assert isometry((0, 0), (0, 1)) is not None and isometry((0,), (1,)) is None
    # the trace form: Tr(L_{e_S}) = 2^n [S empty], so Tr(L_{xy}) / 2^n is the scalar part,
    # diagonal on the blades with entries e_S^2, signature P - M = Gauss sum
    for p, q in ((2, 0), (1, 1), (0, 2), (2, 1), (0, 3), (2, 2)):
        n = p + q
        S = GA.sig(p, q)
        bl = [blade(m, n) for m in range(2 ** n)]
        for m in range(2 ** n):
            tr = sum(GA.mul({bl[m]: F(1)}, {b: F(1)}, S).get(b, F(0)) for b in bl)
            assert tr == (2 ** n if m == 0 else 0)
        diag = [GA.mul({b: F(1)}, {b: F(1)}, S)[()] for b in bl]
        assert sum(diag) == gauss(qf(tuple([0] * p + [1] * q)))
    return True
