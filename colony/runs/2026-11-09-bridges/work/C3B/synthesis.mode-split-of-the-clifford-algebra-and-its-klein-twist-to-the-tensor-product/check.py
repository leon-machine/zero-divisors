"""synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product: exact checks.

Modes are null pairs of Cl(m, m): generators e_k (square +1), f_k (square -1), v_k = (e_k + f_k)/2,
w_k = (e_k - f_k)/2, mode parity p_k = 1 - 2 w_k v_k = f_k e_k. A set A of modes has the sub-Clifford algebra
Cl(A); reduction is the projection onto its blades; tr = 2^m <.>_0.

(1) The twist by the parity blade of A gives commuting copies; the projection onto Cl(A) is the partial trace of
    the twisted tensor split; the two reductions onto the other side differ on stated blades only.
(2) Even pure states have equal moments on the two sides; a pure state that is not even need not.
(3) The eviction states of the stored comparisons are even products; their reductions and purities.
(4) The Renyi moments of a parity sector, by an exact trace count; the Catalan limit and the weights 4^g.
(5) The mean entropy of a parity sector against the imported value, an exact rational difference.
"""
from fractions import Fraction as F
from itertools import permutations, product

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
M2, M3, M4 = 2, 3, 4


def setup(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    v = [GA.scal(F(1, 2), GA.add(e[k], f[k])) for k in range(m)]
    w = [GA.scal(F(1, 2), GA.sub(e[k], f[k])) for k in range(m)]
    par = [GA.mul(f[k], e[k], sq) for k in range(m)]
    return sq, e, f, v, w, par


def prod(xs, sq):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return r


def dagger(x):
    """The anti-automorphism fixing every e_k and negating every f_k (it exchanges v_k and w_k)."""
    r = GA.reverse(x)
    return {b: (c if sum(1 for i in b if i % 2 == 1) % 2 == 0 else -c) for b, c in r.items()}


def idx(modes):
    return {i for k in modes for i in (2 * k, 2 * k + 1)}


def proj(x, modes):
    ok = idx(modes)
    return {b: c for b, c in x.items() if set(b) <= ok and c != 0}


def s0(x):
    return x.get((), F(0))


def fock_state(amps, m, sq, v, w):
    om = prod([GA.mul(v[k], w[k], sq) for k in range(m)], sq)
    psi = {}
    for occ, a in amps.items():
        psi = GA.add(psi, GA.scal(F(a), prod([w[k] for k in range(m) if occ[k]], sq)))
    rho = GA.mul(GA.mul(psi, om, sq), dagger(psi), sq)
    return GA.scal(1 / (2 ** m * s0(rho)), rho)


def reduced(rho, modes, m):
    return GA.scal(F(2 ** (m - len(modes))), proj(rho, modes))


def moments(rho, modes, m, sq, nmax):
    red = reduced(rho, modes, m)
    out, p = [], red
    for _ in range(2, nmax + 1):
        p = GA.mul(p, red, sq)
        out.append(2 ** len(modes) * s0(p))
    return out


# ------------------------------------------------------------------ (1) the twist
def check_parity_twist_gives_commuting_copies_and_the_projection_is_the_partial_trace():
    premise("tower.commuting-copies")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.blade-square-signs-f2-quadratic-form")
    premise("synthesis.joint-clifford-clause-is-a-klein-convention-on-the-composite-space")
    ok = True
    counts = []
    for m, A in ((M2, [0]), (M3, [0]), (M3, [0, 1])):
        sq, e, f, v, w, par = setup(m)
        B = [k for k in range(m) if k not in A]
        for k in range(m):                       # null pairs with the anticommutation relations
            ok = ok and GA.is_zero(GA.mul(v[k], v[k], sq)) and GA.is_zero(GA.mul(w[k], w[k], sq))
            ok = ok and GA.eq(GA.add(GA.mul(v[k], w[k], sq), GA.mul(w[k], v[k], sq)), ONE)
            ok = ok and GA.eq(par[k], GA.sub(ONE, GA.scal(F(2), GA.mul(w[k], v[k], sq))))
        gam = prod([par[k] for k in A], sq)
        ok = ok and GA.eq(GA.mul(gam, gam, sq), ONE)
        gA = [x for k in A for x in (e[k], f[k])]
        gB = [x for k in B for x in (e[k], f[k])]
        tw = [GA.mul(y, gam, sq) for y in gB]
        for y, t in zip(gB, tw):
            ok = ok and GA.eq(GA.mul(t, t, sq), GA.mul(y, y, sq))
            ok = ok and all(GA.commutes(t, x, sq) and GA.anticommutes(y, x, sq) for x in gA)
        ok = ok and all(GA.anticommutes(tw[i], tw[j], sq) for i in range(len(tw)) for j in range(i))
        seen = set()
        for S in product((0, 1), repeat=len(gA)):
            for T in product((0, 1), repeat=len(gB)):
                x = prod([gA[i] for i in range(len(gA)) if S[i]] + [tw[i] for i in range(len(gB)) if T[i]], sq)
                ok = ok and len(x) == 1
                b = next(iter(x))
                seen.add(b)
                in_a, in_b = set(b) <= idx(A), set(b) <= idx(B)
                ok = ok and in_a == (sum(T) == 0)            # twisted partial trace = projection onto Cl(A)
                want_b = (sum(S) == 0 and sum(T) % 2 == 0) or (sum(S) == len(gA) and sum(T) % 2 == 1)
                ok = ok and in_b == want_b
        ok = ok and len(seen) == 4 ** m
        # uniqueness: blades anticommuting with every generator of A and commuting with every generator of B
        blades = [{b: F(1)} for b in GA.all_blades(2 * m)]
        hits = [x for x in blades if all(GA.anticommutes(x, g, sq) for g in gA)
                and all(GA.commutes(x, g, sq) for g in gB)]
        counts.append(len(hits))
        ok = ok and all(GA.eq(x, gam) or GA.eq(GA.neg(x), gam) for x in hits)
    ok = ok and counts == [1, 1, 1]
    GA.check("(i), (ii), (iii) twisted generators commute with Cl(A), keep their squares and anticommute among "
             "themselves; the products of blades are the 4^m blades; the twisted partial trace keeps exactly the "
             "blades of Cl(A); the twist is the one blade with these commutation signs", ok)
    return ok


# ------------------------------------------------------------------ (2) even and non-even pure states
def check_even_pure_states_have_equal_moments_on_both_sides_and_a_non_even_one_does_not():
    premise("singularity.descent-parity-average")
    premise("tower.commuting-copies")
    sq, e, f, v, w, par = setup(M3)
    gam = prod(par, sq)
    rho = fock_state({(0, 0, 0): 1, (1, 1, 0): 2, (1, 0, 1): -3, (0, 1, 1): 5}, M3, sq, v, w)
    ok = GA.eq(GA.mul(rho, rho, sq), rho) and GA.commutes(rho, gam, sq)
    ok = ok and GA.eq(GA.scal(F(1, 2), GA.add(rho, prod([gam, rho, gam], sq))), rho)   # fixed by the parity average
    want = {0: [F(5, 9), F(1, 3), F(17, 81)], 1: [F(941, 1521), F(217, 507), F(717281, 2313441)]}
    for k in (0, 1):
        A = [k]
        B = [j for j in range(M3) if j != k]
        ok = ok and moments(rho, A, M3, sq, 4) == want[k] == moments(rho, B, M3, sq, 4)
        ok = ok and GA.commutes(reduced(rho, A, M3), par[k], sq)
    # a pure state that is not even: three modes, then the closed example on two modes
    gen = fock_state({(0, 0, 0): 1, (1, 0, 0): 2, (0, 1, 0): -3, (1, 1, 0): 1, (0, 0, 1): 2, (1, 1, 1): 1}, M3, sq, v, w)
    ok = ok and GA.eq(GA.mul(gen, gen, sq), gen) and not GA.commutes(gen, gam, sq)
    ok = ok and moments(gen, [0], M3, sq, 2) == [F(117, 200)] and moments(gen, [1, 2], M3, sq, 2) == [F(141, 200)]
    sq, e, f, v, w, par = setup(M2)
    x = GA.scal(F(1, 4), GA.add(ONE, e[0], GA.neg(GA.mul(f[0], e[1], sq)), prod([f[0], e[0], e[1]], sq)))
    ok = ok and GA.eq(GA.mul(x, x, sq), x) and 4 * s0(x) == 1
    tw = GA.mul(e[1], par[0], sq)                       # the twisted vector of the second mode
    ok = ok and GA.eq(x, GA.mul(GA.scal(F(1, 2), GA.add(ONE, e[0])), GA.scal(F(1, 2), GA.add(ONE, tw)), sq))
    ok = ok and moments(x, [0], M2, sq, 3) == [F(1), F(1)] and moments(x, [1], M2, sq, 3) == [F(1, 2), F(1, 4)]
    GA.check("(iv) an even pure state of three modes has the same moments two, three, four on both sides of each "
             "split and even reductions; pure states that are not even have purities 117/200 against 141/200, "
             "and 1 against 1/2", ok)
    return ok


# ------------------------------------------------------------------ (3) the eviction states
def pair_state(kl, kr, c, s, sq, v, w, par):
    r = c * c - s * s
    a = GA.mul(GA.scal(F(1, 4), GA.add(ONE, GA.mul(par[kl], par[kr], sq))), GA.add(ONE, GA.scal(r, par[kl])), sq)
    x = GA.add(GA.mul(w[kl], w[kr], sq), GA.mul(v[kr], v[kl], sq))
    return GA.add(a, GA.scal(c * s, x))


def check_eviction_states_are_even_products_with_the_stored_purities():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    premise("synthesis.eviction-keeps-one-replica-saddle")
    premise("synthesis.eviction-keeps-one-of-catalan-many-replica-saddles")
    sq, e, f, v, w, par = setup(M4)
    gam = prod(par, sq)
    c1, s1, c2, s2 = F(3, 5), F(4, 5), F(5, 13), F(12, 13)
    p1 = pair_state(0, 2, c1, s1, sq, v, w, par)
    p2 = pair_state(1, 3, c2, s2, sq, v, w, par)
    ok = GA.eq(GA.mul(p1, p1, sq), p1) and GA.commutes(p1, p2, sq)
    rho = GA.mul(p1, p2, sq)
    ok = ok and GA.eq(rho, fock_state({(0, 0, 0, 0): 15, (1, 0, 1, 0): 20, (0, 1, 0, 1): 36, (1, 1, 1, 1): -48},
                                      M4, sq, v, w))
    ok = ok and GA.commutes(rho, gam, sq) and 16 * s0(rho) == 1
    r1, r2 = c1 * c1 - s1 * s1, c2 * c2 - s2 * s2
    marg = GA.mul(GA.scal(F(1, 2), GA.add(ONE, GA.scal(r1, par[0]))),
                  GA.scal(F(1, 2), GA.add(ONE, GA.scal(r2, par[1]))), sq)
    ok = ok and GA.eq(reduced(rho, [0, 1], M4), marg)                  # the window is the product of marginals
    pur = (c1 ** 4 + s1 ** 4) * (c2 ** 4 + s2 ** 4)
    ok = ok and pur == F(337, 625) * F(21361, 28561)
    ok = ok and moments(rho, [0, 1], M4, sq, 3) == moments(rho, [2, 3], M4, sq, 3)
    ok = ok and moments(rho, [0, 1], M4, sq, 2) == [pur]
    # zero weight: flat window; then one member evicted, its pair wholly in the radiation
    h = F(1, 2)
    z1 = GA.add(GA.scal(F(1, 4), GA.add(ONE, GA.mul(par[0], par[2], sq))),
                GA.scal(h, GA.add(GA.mul(w[0], w[2], sq), GA.mul(v[2], v[0], sq))))
    z2 = GA.add(GA.scal(F(1, 4), GA.add(ONE, GA.mul(par[1], par[3], sq))),
                GA.scal(h, GA.add(GA.mul(w[1], w[3], sq), GA.mul(v[3], v[1], sq))))
    zero = GA.mul(z1, z2, sq)
    ok = ok and GA.eq(GA.mul(zero, zero, sq), zero)
    ok = ok and GA.eq(reduced(zero, [0, 1], M4), GA.sc(F(1, 4)))
    ok = ok and moments(zero, [2, 3], M4, sq, 4) == [F(1, 4), F(1, 16), F(1, 64)]
    ok = ok and moments(zero, [1, 2, 3], M4, sq, 3) == [F(1, 2), F(1, 4)] == moments(zero, [0], M4, sq, 3)
    GA.check("(v) the pair state is an even idempotent, pairs commute and multiply to the Fock state with the "
             "product amplitudes; the window is the product of the marginals (1 + r p_k)/2; purities "
             "prod(c^4 + s^4) on both sides; at zero weight the spectrum is flat of rank 2^w, also after an eviction",
             ok)
    return ok


# ------------------------------------------------------------------ (4) Renyi moments of a parity sector
def cycles(p):
    seen, c = set(), 0
    for i in range(len(p)):
        if i not in seen:
            c += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return c


def perm_data(n):
    """For each sigma in S_n: (#(sigma), #(sigma^{-1} eta)), eta the n-cycle i -> i + 1."""
    out = []
    for s in permutations(range(n)):
        inv = [0] * n
        for i, si in enumerate(s):
            inv[si] = i
        tau = tuple(inv[(i + 1) % n] for i in range(n))
        out.append((cycles(s), cycles(tau), s, tau))
    return out


def sector_trace(da, db, s, tau):
    """Number of n-tuples of sector basis states (a_i, b_i), parity(a_i) = parity(b_i), fixed when the a are
    permuted by tau and the b by s: the trace of P_sigma (P_eta on A) on the n-th power of the sector."""
    n = len(s)
    par = lambda x: bin(x).count("1") % 2
    count = 0
    for a in product(range(da), repeat=n):
        if any(a[tau[i]] != a[i] for i in range(n)):
            continue
        for b in product(range(db), repeat=n):
            if all(b[s[i]] == b[i] for i in range(n)) and all(par(a[i]) == par(b[i]) for i in range(n)):
                count += 1
    return count


def rising(x, n):
    r = F(1)
    for l in range(n):
        r *= x + l
    return r


def sector_moment(da, db, n, data):
    return 2 * sum(F(da, 2) ** ct * F(db, 2) ** cs for cs, ct, _, _ in data) / rising(F(da * db, 2), n)


def full_moment(da, db, n, data):
    return sum(F(da) ** ct * F(db) ** cs for cs, ct, _, _ in data) / rising(F(da * db), n)


def check_sector_renyi_moments_keep_the_catalan_limit_and_weight_genus_by_four():
    premise("synthesis.imported-haar-moments-of-random-pure-state")
    premise("synthesis.eviction-keeps-one-of-catalan-many-replica-saddles")
    premise("synthesis.eviction-keeps-one-replica-saddle")
    ok = True
    data = {n: perm_data(n) for n in (2, 3, 4, 5, 6)}
    # the trace count of the lemma, by enumeration
    for da, db, n in ((2, 2, 2), (2, 4, 2), (4, 4, 2), (2, 2, 3), (4, 2, 3), (2, 4, 3)):
        for cs, ct, s, tau in data[n]:
            ok = ok and sector_trace(da, db, s, tau) == 2 * F(da, 2) ** ct * F(db, 2) ** cs
    # index two: the sector purity, and the stored comparison of clauses (iii), (iv) recomputed
    for a in range(1, 6):
        for b in range(1, 6):
            m, n = 2 ** a, 2 ** b
            sec = sector_moment(m, n, 2, data[2])
            ok = ok and sec == F(m + n, m * n + 2) and full_moment(m, n, 2, data[2]) == F(m + n, m * n + 1)
            ok = ok and max(F(1, m), F(1, n)) < sec < F(m + n, m * n + 1) < F(1, m) + F(1, n)
            ok = ok and F(1, m) + F(1, n) - sec == F(2 * (m + n), m * n * (m * n + 2))
    ok = ok and sector_moment(2, 2, 2, data[2]) == F(2, 3) and sector_moment(4, 4, 2, data[2]) == F(4, 9)
    for m in (2, 4, 8, 16):
        ok = ok and sector_moment(m, m, 2, data[2]) * m == 2 - F(4, m * m + 2)
    # every index: genus counts, the weight 4^g, the Catalan limit, the bounds
    cat = {2: 2, 3: 5, 4: 14, 5: 42, 6: 132}
    genus1 = {2: 0, 3: 1, 4: 10, 5: 70, 6: 420}
    for n in (2, 3, 4, 5, 6):
        ng = {}
        for cs, ct, _, _ in data[n]:
            ok = ok and (n + 1 - cs - ct) % 2 == 0 and cs + ct <= n + 1
            g = (n + 1 - cs - ct) // 2
            ng[g] = ng.get(g, 0) + 1
        ok = ok and ng[0] == cat[n] and ng.get(1, 0) == genus1[n]
        for d in (2, 4, 8, 16, 32):
            u = F(1, d * d)
            sec = sector_moment(d, d, n, data[n])
            full = full_moment(d, d, n, data[n])
            den_s = F(1)
            den_f = F(1)
            for l in range(n):
                den_s *= 1 + 2 * l * u
                den_f *= 1 + l * u
            ok = ok and sec * d ** (n - 1) == sum(c * (4 * u) ** g for g, c in ng.items()) / den_s
            ok = ok and full * d ** (n - 1) == sum(c * u ** g for g, c in ng.items()) / den_f
            ok = ok and F(1, d ** (n - 1)) < sec < full < F(cat[n], d ** (n - 1))
            # first correction: C_n - (C_n n(n-1) - 4 N_1) u, from above, within 26000 u^2
            lead = cat[n] - (cat[n] * n * (n - 1) - 4 * genus1[n]) * u
            ok = ok and lead < sec * d ** (n - 1) < lead + 26000 * u * u
    ok = ok and sector_moment(2, 2, 3, data[3]) == F(1, 2) and full_moment(2, 2, 3, data[3]) == F(7, 10)
    GA.check("(vi) the sector trace count 2 (dA/2)^# (dB/2)^# by enumeration; sector purity (m + n)/(mn + 2) "
             "strictly between the one-saddle and the unrestricted values; the crossing coefficient is "
             "sum_g N_g (4/d^2)^g / prod(1 + 2l/d^2) with N_0 the Catalan numbers, for n <= 6", ok)
    return ok


# ------------------------------------------------------------------ (5) mean entropy of a parity sector
def harm(lo, hi):
    return sum(F(1, k) for k in range(lo + 1, hi + 1))


def page_mean(m, n):
    return harm(n, m * n) - F(m - 1, 2 * n)


def sector_mean(m, n):
    return harm(n // 2, m * n // 2) - F(m - 2, 2 * n)


def ln2_bracket():
    lo = sum(F(1, k * 2 ** k) for k in range(1, 40))
    return lo, lo + F(1, 2 ** 39)


def check_sector_mean_entropy_exceeds_the_imported_value_by_a_rational_amount():
    premise("singularity.imported-page-average-entropy-subsystem")
    premise("synthesis.eviction-deficit-against-page-deficit")
    premise("singularity.assembled-page-curve-up-typicality")
    ok = True
    ok = ok and sector_mean(2, 2) == F(1, 2) and page_mean(2, 2) == F(1, 3)
    ok = ok and sector_mean(2, 4) == F(7, 12) and sector_mean(4, 4) == F(271, 280)
    ok = ok and sector_mean(4, 4) - page_mean(4, 4) == F(6553, 144144)
    lo, hi = ln2_bracket()
    for a in range(1, 7):
        for b in range(a, 7):
            m, n = 2 ** a, 2 ** b
            # block form: weight Beta(mn/4, mn/4), two independent blocks of dimensions m/2 by n/2
            weight = harm(m * n // 4, m * n // 2)
            block = page_mean(m // 2, n // 2) if m > 2 else F(0)
            ok = ok and sector_mean(m, n) == weight + block
            diff = sector_mean(m, n) - page_mean(m, n)
            ok = ok and diff == F(1, 2 * n) - harm(m * n // 2, m * n) + harm(n // 2, n)
            ok = ok and F(1, 2 * m * n) < diff < F(1, 2 * (m * n + 1)) + F(1, 2 * n * (n + 1))
            # deficits against ln m = a ln 2, by a rational bracket of ln 2
            d_lo, d_hi = a * lo - sector_mean(m, n), a * hi - sector_mean(m, n)
            ok = ok and F(m - 2, 2 * n) + F(2 * (m - 1), 2 * m * n + m + 1) < d_lo
            ok = ok and d_hi < F(m, 2 * n) - F(1, m * n)
            p_hi = a * hi - page_mean(m, n)
            ok = ok and d_hi < a * lo - page_mean(m, n) and p_hi < F(m, 2 * n) - F(1, 2 * m * n)
            if m == n and m >= 4:
                ok = ok and F(2, 5) < d_lo and d_hi < F(1, 2)
            ok = ok and (d_lo > F(m - 1, 2 * n) if m >= 4 else d_hi < F(m - 1, 2 * n))
    # the two-dimensional side: the weight alone, its moments against the sector formula
    for n in (2, 4, 8):
        for j in (2, 3, 4, 5):
            beta = F(1)
            for i in range(j):
                beta *= F(n // 2 + i, n + i)
            ok = ok and 2 * beta == sector_moment(2, n, j, perm_data(j))
    GA.check("(vii) sector mean entropy sum_{k = n/2 + 1}^{mn/2} 1/k - (m - 2)/(2n): 1/2, 7/12, 271/280; it is "
             "the block weight plus the imported value on a block; above the imported value by between 1/(2mn) "
             "and 1/(2(mn + 1)) + 1/(2n(n + 1)); crossing deficit in (2/5, 1/2) for m >= 4", ok)
    return ok
