"""synthesis.eviction-keeps-one-replica-saddle: exact checks (rational arithmetic only).

(i)   a window member's thermal marginal diag(c^2, s^2) is rho = (1 + r e3)/2 in the Pauli algebra
      Cl(3,0), r = c^2 - s^2, with purity Tr rho^2 = 2 <rho^2>_0 = (1 + r^2)/2 = c^4 + s^4; purities
      multiply over a product window (explicit Kronecker products); zero weight (r = 0) gives 1/2;
(ii)  at zero weight, the eviction configuration at stage j (j radiated qubits, window of w members
      each maximally entangled with a distinct radiated qubit, evicted pairs wholly in the
      radiation) has radiation purity exactly 2^{-w}; along a run with capacity n_cap(j) the window
      is w = min(j, n_cap) and the purity is max(2^{-j}, 2^{-n_cap}): one saddle;
(iii) the Haar average purity on C^m (x) C^n is (m + n)/(mn + 1), from the symmetric-subspace
      projector (I + F)/(D(D + 1)) and exact traces of the swap operators; it lies below the
      two-saddle planar value 1/m + 1/n by (m + n)/(mn(mn + 1));
(iv)  at the crossing (j = n_cap, m = n): eviction purity 1/m, two-saddle 2/m (ratio exactly 2,
      Renyi-2 deficit ln 2), Haar 2m/(m^2 + 1) (ratio 2m^2/(m^2 + 1) in (2 - 2/m^2, 2)); away from
      it the two-saddle ratio to eviction is 1 + 2^{-|j - n_cap|}.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def kron(A, B):
    return [[a * b for a in ra for b in rb] for ra in A for rb in B]


def mat_trace_sq(R):
    n = len(R)
    return sum(R[i][k] * R[k][i] for i in range(n) for k in range(n))


def check_member_purity_in_pauli_algebra():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    sq = (1, 1, 1)
    e3 = GA.gen(2)
    ok = True
    mats = []
    for c2 in (F(1, 2), F(2, 3), F(5, 7)):
        s2 = 1 - c2
        r = c2 - s2
        rho = GA.add(GA.sc(F(1, 2)), GA.scal(r / 2, e3))
        rho2 = GA.mul(rho, rho, sq)
        pur = 2 * rho2.get((), F(0))                 # Tr = 2 <.>_0 on the Pauli algebra
        ok = ok and pur == (1 + r * r) / 2 and pur == c2 * c2 + s2 * s2
        mats.append([[c2, F(0)], [F(0), s2]])
    ok = ok and mats[0][0][0] ** 2 + mats[0][1][1] ** 2 == F(1, 2)   # zero weight: 1/2
    P = kron(kron(mats[0], mats[1]), mats[2])
    prod = 1
    for M in mats:
        prod *= mat_trace_sq(M)
    ok = ok and mat_trace_sq(P) == prod
    GA.check("(i) member purity c^4 + s^4 = 2<rho^2>_0 in Cl(3,0); purities multiply over a "
             "product window; 1/2 at zero weight", ok)
    return ok


def eviction_state(j, w):
    """Qubits: radiation r_0..r_{j-1}, window members m_0..m_{w-1}; member i is maximally entangled
    with r_i; for i >= w the radiated qubit r_i is paired with an evicted partner, which is itself
    radiation (r_i and its partner e_i together in |00> + |11>). Returns the amplitude dict over
    (radiation bits incl. evicted partners, window bits) and the radiation register size."""
    amps = {}
    for bits in range(2 ** j):
        b = [(bits >> i) & 1 for i in range(j)]
        rad = tuple(b) + tuple(b[w:])          # evicted partners copy their radiated qubit
        win = tuple(b[:w])
        amps[(rad, win)] = amps.get((rad, win), 0) + 1
    return amps


def radiation_purity(amps):
    norm = sum(a * a for a in amps.values())
    # rho_R[rad, rad'] = sum_win a(rad, win) a(rad', win) / norm
    by_win = {}
    for (rad, win), a in amps.items():
        by_win.setdefault(win, {})[rad] = a
    rho = {}
    for win, col in by_win.items():
        for r1, a1 in col.items():
            for r2, a2 in col.items():
                rho[(r1, r2)] = rho.get((r1, r2), 0) + a1 * a2
    tr2 = sum(v * rho.get((r2, r1), 0) for (r1, r2), v in rho.items())
    return F(tr2, norm * norm)


def check_eviction_purity_is_one_saddle():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    premise("synthesis.eviction-deficit-against-page-deficit")
    ok = True
    for j in range(1, 7):
        for w in range(0, j + 1):
            ok = ok and radiation_purity(eviction_state(j, w)) == F(1, 2 ** w)
    # a run: capacity n_cap falls by one each stage from 6, radiated count j rises by one
    for j in range(0, 7):
        ncap = 6 - j
        w = min(j, ncap)
        pur = radiation_purity(eviction_state(j, w)) if j > 0 else F(1)
        ok = ok and pur == max(F(1, 2 ** j), F(1, 2 ** ncap))
    GA.check("(ii) zero weight: eviction radiation purity 2^{-w} exactly; along a run it is "
             "max(2^{-j}, 2^{-n_cap}), a single saddle", ok)
    return ok


def haar_purity(m, n):
    """<Tr rho_A^2> = (Tr[F_A] + Tr[F F_A]) / (D(D + 1)) on (C^m (x) C^n)^{(x) 2}."""
    D = m * n
    t1 = 0          # Tr F_A: |a1 b1 a2 b2> -> |a2 b1 a1 b2>, diagonal iff a1 = a2
    t2 = 0          # Tr F F_A: -> |a1 b2 a2 b1>, diagonal iff b1 = b2
    for a1 in range(m):
        for b1 in range(n):
            for a2 in range(m):
                for b2 in range(n):
                    t1 += 1 if a1 == a2 else 0
                    t2 += 1 if b1 == b2 else 0
    return F(t1 + t2, D * (D + 1))


def check_haar_purity_against_two_saddles():
    premise("singularity.imported-page-average-entropy-subsystem")
    premise("synthesis.eviction-deficit-against-page-deficit")
    ok = True
    table = {(2, 2): F(4, 5), (2, 3): F(5, 7), (3, 3): F(3, 5), (2, 4): F(2, 3),
             (3, 5): F(1, 2), (4, 4): F(8, 17)}
    for (m, n), want in table.items():
        h = haar_purity(m, n)
        ok = ok and h == want and h == F(m + n, m * n + 1)
        planar = F(1, m) + F(1, n)
        ok = ok and planar - h == F(m + n, m * n * (m * n + 1)) and planar > h
        ok = ok and h > max(F(1, m), F(1, n))          # strictly above the one-saddle value
    GA.check("(iii) Haar purity (m + n)/(mn + 1) exactly; below the two-saddle 1/m + 1/n by "
             "(m + n)/(mn(mn + 1)), above the single saddle", ok)
    return ok


def check_crossing_ratios():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    premise("singularity.imported-page-average-entropy-subsystem")
    ok = True
    for m in (2, 4, 8, 16):
        ev = F(1, m)
        two = F(1, m) + F(1, m)
        hr = haar_purity(m, m) / ev if m <= 8 else F(2 * m * m, m * m + 1)
        ok = ok and two / ev == 2
        ok = ok and hr == F(2 * m * m, m * m + 1) and 2 - F(2, m * m) < hr < 2
    for j in range(0, 7):
        ncap = 6 - j
        ev = max(F(1, 2 ** j), F(1, 2 ** ncap))
        two = F(1, 2 ** j) + F(1, 2 ** ncap)
        ok = ok and two / ev == 1 + F(1, 2 ** abs(j - ncap))
    GA.check("(iv) at the crossing two-saddle/eviction purity = 2 (Renyi-2 deficit ln 2), "
             "Haar/eviction = 2m^2/(m^2 + 1); elsewhere 1 + 2^{-|j - n_cap|}", ok)
    return ok


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


def pair_state(k, kk, r, cs, sq, v, w, p):
    """r = c^2 - s^2 and cs = c s of the amplitudes c on |00>, s on |11>."""
    diag = GA.mul(GA.scal(F(1, 4), GA.add(ONE, GA.mul(p[k], p[kk], sq))), GA.add(ONE, GA.scal(r, p[k])), sq)
    return GA.add(diag, GA.scal(cs, GA.add(GA.mul(w[k], w[kk], sq), GA.mul(v[kk], v[k], sq))))


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
    r1, r2 = c1 * c1 - s1 * s1, c2 * c2 - s2 * s2
    q1 = pair_state(0, 2, r1, c1 * s1, sq, v, w, p)
    q2 = pair_state(1, 3, r2, c2 * s2, sq, v, w, p)
    rho = GA.mul(q1, q2, sq)
    ok = ok and GA.eq(GA.mul(q1, q1, sq), q1) and GA.commutes(q1, q2, sq) and GA.commutes(rho, gam, sq)
    ok = ok and GA.eq(GA.scal(F(1, 2), GA.add(rho, gprod([gam, rho, gam], sq))), rho)
    win = GA.mul(GA.scal(F(1, 2), GA.add(ONE, GA.scal(r1, p[0]))), GA.scal(F(1, 2), GA.add(ONE, GA.scal(r2, p[1]))), sq)
    ok = ok and GA.eq(GA.scal(F(4), blade_projection(rho, [0, 1])), win)
    pur = (c1 ** 4 + s1 ** 4) * (c2 ** 4 + s2 ** 4)
    ok = ok and pur == F(337 * 21361, 625 * 28561)
    ok = ok and reduced_moments(rho, [0, 1], MODES4, sq, 3) == reduced_moments(rho, [2, 3], MODES4, sq, 3)
    ok = ok and reduced_moments(rho, [0, 1], MODES4, sq, 2) == [pur]
    # zero weight, one eviction: window = mode 0, radiation = modes 1, 2, 3: purity max(1/4, 1/2)
    z = GA.mul(pair_state(0, 2, F(0), F(1, 2), sq, v, w, p), pair_state(1, 3, F(0), F(1, 2), sq, v, w, p), sq)
    ok = ok and GA.eq(GA.mul(z, z, sq), z) and 16 * z.get((), F(0)) == 1
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


def run():
    return all([check_member_purity_in_pauli_algebra(), check_eviction_purity_is_one_saddle(),
                check_haar_purity_against_two_saddles(), check_crossing_ratios(),
                check_mode_split_and_parity_sector_column()])


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
