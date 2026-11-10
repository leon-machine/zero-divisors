

# ---------------------------------------------------------------- version 4: the split in the algebra of the modes
ONE = GA.sc(F(1))
MODES3, MODES4 = 3, 4


def mode_algebra(m):
    """Cl(m, m): e_k (square +1), f_k (square -1); null pairs v, w; mode parity p = f e."""
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    v = [GA.scal(F(1, 2), GA.add(e[k], f[k])) for k in range(m)]
    w = [GA.scal(F(1, 2), GA.sub(e[k], f[k])) for k in range(m)]
    p = [GA.mul(f[k], e[k], sq) for k in range(m)]
    return sq, e, f, v, w, p


def gprod(xs, sq):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return r


def blade_projection(x, modes):
    keep = {i for k in modes for i in (2 * k, 2 * k + 1)}
    return {b: c for b, c in x.items() if set(b) <= keep and c != 0}


def reduced_moments(rho, modes, m, sq, nmax):
    red = GA.scal(F(2 ** (m - len(modes))), blade_projection(rho, modes))
    out, q = [], red
    for _ in range(2, nmax + 1):
        q = GA.mul(q, red, sq)
        out.append(2 ** len(modes) * q.get((), F(0)))
    return out


def pair_state(k, kk, c, s, sq, v, w, p):
    r = c * c - s * s
    diag = GA.mul(GA.scal(F(1, 4), GA.add(ONE, GA.mul(p[k], p[kk], sq))), GA.add(ONE, GA.scal(r, p[k])), sq)
    return GA.add(diag, GA.scal(c * s, GA.add(GA.mul(w[k], w[kk], sq), GA.mul(v[kk], v[k], sq))))


def sector_swap_traces(m, n):
    """Traces of F_A and of F F_A on the square of the sector {|ab>: parity(a) = parity(b)}."""
    par = lambda x: bin(x).count("1") % 2
    sec = [(a, b) for a in range(m) for b in range(n) if par(a) == par(b)]
    t_fa = sum(1 for (a1, b1) in sec for (a2, b2) in sec if a1 == a2)
    t_ffa = sum(1 for (a1, b1) in sec for (a2, b2) in sec if b1 == b2)
    return len(sec), t_fa, t_ffa


def check_mode_split_and_parity_sector_column():
    premise("tower.commuting-copies")
    premise("singularity.descent-parity-average")
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    ok = True
    # (a), (b): the twist by the parity blade on three modes, A = the first mode
    sq, e, f, v, w, p = mode_algebra(MODES3)
    gam_a = p[0]
    g_a = [e[0], f[0]]
    g_b = [e[1], f[1], e[2], f[2]]
    tw = [GA.mul(y, gam_a, sq) for y in g_b]
    ok = ok and GA.eq(GA.mul(gam_a, gam_a, sq), ONE)
    ok = ok and all(GA.eq(GA.mul(t, t, sq), GA.mul(y, y, sq)) for t, y in zip(tw, g_b))
    ok = ok and all(GA.commutes(t, x, sq) for t in tw for x in g_a)
    ok = ok and all(GA.anticommutes(y, x, sq) for y in g_b for x in g_a)
    ok = ok and all(GA.anticommutes(tw[i], tw[j], sq) for i in range(4) for j in range(i))
    in_a = 0
    odd_in_b = 0
    for bits in range(64):
        pick = [(bits >> i) & 1 for i in range(6)]
        x = gprod([g for g, on in zip(g_a + tw, pick) if on], sq)
        b = next(iter(x))
        in_a += 1 if set(b) <= {0, 1} and sum(pick[2:]) > 0 else 0       # none: only untwisted products lie in Cl(A)
        odd_in_b += 1 if set(b) <= {2, 3, 4, 5} and sum(pick) % 2 == 0 and sum(pick[:2]) > 0 else 0
    ok = ok and in_a == 0 and odd_in_b == 0
    # (c): a pure state that is not even has unequal purities; the pair states are even
    sq2, e2, f2, v2, w2, p2 = mode_algebra(2)
    bad = GA.mul(GA.scal(F(1, 2), GA.add(ONE, e2[0])), GA.scal(F(1, 2), GA.add(ONE, GA.mul(e2[1], p2[0], sq2))), sq2)
    ok = ok and GA.eq(GA.mul(bad, bad, sq2), bad)
    ok = ok and reduced_moments(bad, [0], 2, sq2, 2) == [F(1)] and reduced_moments(bad, [1], 2, sq2, 2) == [F(1, 2)]
    # (d), (e): two pairs (window modes 0, 1; radiated partners 2, 3)
    sq, e, f, v, w, p = mode_algebra(MODES4)
    gam = gprod(p, sq)
    c1, s1, c2, s2 = F(3, 5), F(4, 5), F(5, 13), F(12, 13)
    q1 = pair_state(0, 2, c1, s1, sq, v, w, p)
    q2 = pair_state(1, 3, c2, s2, sq, v, w, p)
    rho = GA.mul(q1, q2, sq)
    ok = ok and GA.eq(GA.mul(q1, q1, sq), q1) and GA.commutes(q1, q2, sq) and GA.commutes(rho, gam, sq)
    ok = ok and GA.eq(GA.scal(F(1, 2), GA.add(rho, gprod([gam, rho, gam], sq))), rho)
    r1, r2 = c1 * c1 - s1 * s1, c2 * c2 - s2 * s2
    win = GA.mul(GA.scal(F(1, 2), GA.add(ONE, GA.scal(r1, p[0]))), GA.scal(F(1, 2), GA.add(ONE, GA.scal(r2, p[1]))), sq)
    ok = ok and GA.eq(GA.scal(F(4), blade_projection(rho, [0, 1])), win)
    pur = (c1 ** 4 + s1 ** 4) * (c2 ** 4 + s2 ** 4)
    ok = ok and pur == F(337 * 21361, 625 * 28561)
    ok = ok and reduced_moments(rho, [0, 1], MODES4, sq, 3) == reduced_moments(rho, [2, 3], MODES4, sq, 3)
    ok = ok and reduced_moments(rho, [0, 1], MODES4, sq, 2) == [pur]
    # zero weight, one eviction: window = mode 0, radiation = modes 1, 2, 3: purity max(1/4, 1/2)
    z = GA.mul(pair_state(0, 2, F(1), F(1), sq, v, w, p), pair_state(1, 3, F(1), F(1), sq, v, w, p), sq)
    z = GA.scal(1 / (16 * z.get((), F(0))), z)
    ok = ok and GA.eq(GA.mul(z, z, sq), z)
    ok = ok and reduced_moments(z, [1, 2, 3], MODES4, sq, 2) == [F(1, 2)] == reduced_moments(z, [0], MODES4, sq, 2)
    ok = ok and reduced_moments(z, [2, 3], MODES4, sq, 2) == [F(1, 4)]
    # (iii), (iv) on a parity sector
    for m, n in ((2, 2), (2, 4), (4, 4), (2, 8), (4, 8), (8, 8)):
        dim, t_fa, t_ffa = sector_swap_traces(m, n)
        ok = ok and 2 * dim == m * n and 4 * t_fa == m * n * n and 4 * t_ffa == m * m * n
        sec = F(t_fa + t_ffa, dim * (dim + 1))
        ok = ok and sec == F(m + n, m * n + 2)
        ok = ok and max(F(1, m), F(1, n)) < sec < F(m + n, m * n + 1) < F(1, m) + F(1, n)
        ok = ok and F(1, m) + F(1, n) - sec == F(2 * (m + n), m * n * (m * n + 2))
    ok = ok and F(sum(sector_swap_traces(2, 2)[1:]), 2 * 3) == F(2, 3)
    for m in (2, 4, 8, 16):
        ratio = F(2 * m, m * m + 2) * m
        ok = ok and ratio == 2 - F(4, m * m + 2) and 2 - F(4, m * m) < ratio < 2
    GA.check("(i) to (iv) on the split in the algebra of the modes: the twisted generators commute with the other "
             "side; pair states are even and commute; window = product of (1 + r p)/2 with purity prod(c^4 + s^4) "
             "on both sides; one saddle after an eviction; on a parity sector the mean purity is (m + n)/(mn + 2), "
             "at the crossing 2m/(m^2 + 2)", ok)
    return ok
