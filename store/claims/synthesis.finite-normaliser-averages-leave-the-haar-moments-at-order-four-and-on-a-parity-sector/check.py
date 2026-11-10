"""synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector: exact checks.

Signed directions e_0 .. e_{2m-1} of Cl(2m, 0) (two per mode); a string is a subset S, a blade e_S. The forms of
the stored theorem on signed directions, b(S, T) = |S||T| + |S cap T| and q(S) = binom(|S|, 2) (mod 2), are the
commutation and square signs. A quarter turn about a string w acts on strings by the transvection
x -> x + b(x, w) w. A state fixed by a maximal commuting family L (a Lagrangian subspace for b) has, on the
subalgebra A of the first 2a directions, tr rho_A^n = (|L_A| / 2^a)^(n-1), L_A the strings of L inside A.

(1) Two modes in Cl(4, 1) (central unit w, w^2 = -1): the sixty projectors, their partial traces as blade
    projections, mean tr rho_A^n = 4/5, 7/10, 13/20 for n = 2, 3, 4 against the Haar values 4/5, 7/10, 22/35.
(2) The count of Lagrangians by rank, and the moments for a, b <= 6: equal to Haar at n = 2, 3, never at n = 4;
    the crossing coefficient tends to the Galois numbers 2, 5, 16, 67, 374, not the Catalan numbers; the sum over
    spanned subspaces that proves the limit.
(3) A parity sector: the Haar moments of the sector, the orbit of the parity-preserving normaliser, and the mean
    purity (dA + dB)/(dA dB + 2) against (dA + dB)/(dA dB + 1).
(4) Bivector quarter turns alone: the full orbit at four and six directions, 105 of 135 at eight.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product

import GA
from tp_premise import premise


# ---------------------------------------------------------------- strings over F2 and the two stored forms
def wt(x):
    return bin(x).count("1")


def bform(x, y):
    return (wt(x) * wt(y) + wt(x & y)) % 2


def qform(x):
    return (wt(x) * (wt(x) - 1) // 2) % 2


def span(gens):
    s = {0}
    for g in gens:
        s |= {x ^ g for x in s}
    return frozenset(s)


def orbit(start, ws):
    seen = {start}
    todo = [start]
    while todo:
        L = todo.pop()
        for w in ws:
            M = frozenset(x ^ w if bform(x, w) else x for x in L)
            if M not in seen:
                seen.add(M)
                todo.append(M)
    return seen


def inside(L, a):
    low = (1 << (2 * a)) - 1
    return sum(1 for x in L if x & ~low == 0)


def orbit_moment(orb, a, n):
    return sum(F(inside(L, a), 2 ** a) ** (n - 1) for L in orb) / len(orb)


def vacuum(m):
    return span([3 << (2 * i) for i in range(m)])


# ---------------------------------------------------------------- counts
def gbin(n, k):
    num = den = 1
    for i in range(k):
        num *= 2 ** (n - i) - 1
        den *= 2 ** (i + 1) - 1
    return num // den


def n_isotropic(a, k):
    r = gbin(a, k)
    for i in range(k):
        r *= 2 ** (a - i) + 1
    return r


def order_sp(e):
    r = 2 ** (e * e)
    for i in range(1, e + 1):
        r *= 4 ** i - 1
    return r


def n_lagrangian(m):
    r = 1
    for i in range(1, m + 1):
        r *= 2 ** i + 1
    return r


def rank_count(a, b, e):
    return n_isotropic(a, a - e) * n_isotropic(b, b - e) * order_sp(e)


def finite_moment(a, b, n):
    return sum(F(rank_count(a, b, e), 2 ** ((n - 1) * e)) for e in range(min(a, b) + 1)) / n_lagrangian(a + b)


def cycles(p):
    seen = [False] * len(p)
    c = 0
    for i in range(len(p)):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return c


def perm_pairs(n):
    eta = tuple((i + 1) % n for i in range(n))
    for sg in permutations(range(n)):
        inv = [0] * n
        for i, x in enumerate(sg):
            inv[x] = i
        yield sg, tuple(inv[eta[i]] for i in range(n))


def haar_moment(dA, dB, n, sector=False):
    """The imported moment formula; with sector=True the same Schur average on the parity sector."""
    if sector:
        s = sum(2 * F(dA, 2) ** cycles(tau) * F(dB, 2) ** cycles(sg) for sg, tau in perm_pairs(n))
        D = F(dA * dB, 2)
    else:
        s = sum(F(dA) ** cycles(tau) * F(dB) ** cycles(sg) for sg, tau in perm_pairs(n))
        D = F(dA * dB)
    den = F(1)
    for l in range(n):
        den *= D + l
    return s / den


def spanned_sum(a, b, n):
    """<|L_A|^(n-1)> as a sum over the subspace spanned by an (n-1)-tuple of L_A."""
    m = a + b
    total = F(0)
    for r in range(min(a, n - 1) + 1):
        frac = F(1)
        for j in range(m - r + 1, m + 1):
            frac /= 2 ** j + 1
        tuples = 1
        for j in range(r):
            tuples *= 2 ** (n - 1) - 2 ** j
        total += n_isotropic(a, r) * frac * tuples
    return total


def galois(j):
    return sum(gbin(j, i) for i in range(j + 1))


def catalan(n):
    num = 1
    for i in range(1, n + 1):
        num = num * (n + i) // i
    return num // (n + 1)


# ---------------------------------------------------------------- Cl(4,1): two modes with a central unit
SQ5 = GA.sig(4, 1)
ONE = GA.sc(1)


def blade(S, squares):
    x = GA.sc(1)
    for i in S:
        x = GA.mul(x, GA.gen(i), squares)
    return x


OMEGA = blade(range(5), SQ5)


def hermitian(S):
    g = blade(S, SQ5)
    sq = GA.mul(g, g, SQ5)
    if GA.eq(sq, ONE):
        return g
    return GA.mul(OMEGA, g, SQ5)


def scalar_part(x):
    return x.get((), F(0))


def project_first_mode(x):
    """Blade projection onto the subalgebra of e_0, e_1 and the central unit (blades inside {0,1} or containing {2,3,4})."""
    keep = {}
    for bl, c in x.items():
        s = set(bl)
        if s <= {0, 1} or s >= {2, 3, 4}:
            keep[bl] = c
    return keep


def reduced_moment(rho, n):
    rA = GA.scal(F(2), project_first_mode(rho))
    p = rA
    for _ in range(n - 1):
        p = GA.mul(p, rA, SQ5)
    return 2 * scalar_part(p)


def bits(S):
    return sum(1 << i for i in S)


def check_sixty_two_mode_states_give_four_fifths_seven_tenths_and_thirteen_twentieths():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.imported-haar-moments-of-random-pure-state")
    premise("synthesis.quarter-turn-rotors-of-the-even-subalgebra-form-a-state-design-of-order-three")
    ok = GA.eq(GA.mul(OMEGA, OMEGA, SQ5), GA.sc(-1))
    ok = ok and all(GA.commutes(OMEGA, GA.gen(i), SQ5) for i in range(5))
    strings = [S for k in range(1, 5) for S in combinations(range(4), k)]
    ok = ok and len(strings) == 15
    # the stored forms are the commutation and square signs of the blades
    for S in strings:
        g = blade(S, SQ5)
        ok = ok and GA.eq(GA.mul(g, g, SQ5), GA.sc(1 - 2 * qform(bits(S))))
        for T in strings:
            ok = ok and (GA.commutes(g, blade(T, SQ5), SQ5) == (bform(bits(S), bits(T)) == 0))
    families = set()
    for S, T in combinations(strings, 2):
        if bform(bits(S), bits(T)) == 0:
            families.add(frozenset([bits(S), bits(T), bits(S) ^ bits(T)]))
    ok = ok and len(families) == 15
    by_bits = {bits(S): S for S in strings}
    moments = {2: F(0), 3: F(0), 4: F(0)}
    ranks = {1: 0, 2: 0}
    count = 0
    for fam in sorted(families, key=sorted):
        s, t = sorted(fam)[:2]
        hs, ht = hermitian(by_bits[s]), hermitian(by_bits[t])
        ok = ok and GA.commutes(hs, ht, SQ5)
        for s1, s2 in product((1, -1), repeat=2):
            rho = GA.scal(F(1, 4), GA.mul(GA.add(ONE, GA.scal(F(s1), hs)), GA.add(ONE, GA.scal(F(s2), ht)), SQ5))
            ok = ok and GA.eq(GA.mul(rho, rho, SQ5), rho) and scalar_part(rho) == F(1, 4)
            pur = reduced_moment(rho, 2)
            ok = ok and pur == F(inside(fam | {0}, 1), 2)
            ranks[1 if pur == 1 else 2] += 1
            for n in moments:
                moments[n] += reduced_moment(rho, n)
            count += 1
    ok = ok and count == 60 and ranks == {1: 36, 2: 24}
    mean = {n: moments[n] / count for n in moments}
    ok = ok and mean == {2: F(4, 5), 3: F(7, 10), 4: F(13, 20)}
    ok = ok and haar_moment(2, 2, 2) == F(4, 5) and haar_moment(2, 2, 3) == F(7, 10)
    ok = ok and haar_moment(2, 2, 4) == F(22, 35) and mean[4] - haar_moment(2, 2, 4) == F(3, 140)
    GA.check("every clause of this function holds", ok)


def check_rank_count_and_moments_agree_with_haar_at_two_and_three_and_never_at_four():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.imported-haar-moments-of-random-pure-state")
    ok = True
    # brute force: every Lagrangian of four and of six directions, counted by rank
    for m, a in ((2, 1), (3, 1), (3, 2)):
        ws = range(1, 1 << (2 * m))
        orb = orbit(vacuum(m), ws)
        ok = ok and len(orb) == n_lagrangian(m)
        b = m - a
        for e in range(min(a, b) + 1):
            ok = ok and sum(1 for L in orb if inside(L, a) == 2 ** (a - e)) == rank_count(a, b, e)
        for n in (2, 3, 4):
            ok = ok and orbit_moment(orb, a, n) == finite_moment(a, b, n)
    ok = ok and n_lagrangian(2) == 15 and n_lagrangian(3) == 135
    ok = ok and [rank_count(1, 1, e) for e in (0, 1)] == [9, 6]
    ok = ok and [rank_count(2, 2, e) for e in (0, 1, 2)] == [225, 1350, 720]
    for a in range(1, 7):
        for b in range(1, 7):
            ok = ok and sum(rank_count(a, b, e) for e in range(min(a, b) + 1)) == n_lagrangian(a + b)
            ok = ok and finite_moment(a, b, 2) == haar_moment(2 ** a, 2 ** b, 2) == F(2 ** a + 2 ** b, 2 ** (a + b) + 1)
            ok = ok and finite_moment(a, b, 3) == haar_moment(2 ** a, 2 ** b, 3)
            if a + b <= 8:
                ok = ok and finite_moment(a, b, 4) > haar_moment(2 ** a, 2 ** b, 4)
    ok = ok and finite_moment(2, 2, 4) == F(3, 17) and haar_moment(4, 4, 4) == F(52, 323)
    # the crossing: d^(n-1) <tr rho^n> against Catalan (Haar) and Galois (finite) numbers
    ok = ok and [catalan(n) for n in range(2, 7)] == [2, 5, 14, 42, 132]
    ok = ok and [galois(n - 1) for n in range(2, 7)] == [2, 5, 16, 67, 374]
    for n in range(2, 7):
        v16 = finite_moment(16, 16, n) * 2 ** (16 * (n - 1))
        v24 = finite_moment(24, 24, n) * 2 ** (24 * (n - 1))
        ok = ok and v16 < v24 < galois(n - 1)
        ok = ok and galois(n - 1) - v16 < F(1, 2 ** 16) and galois(n - 1) - v24 < F(1, 2 ** 32)
    # the sum over spanned subspaces (the proof of the limit) against the count by rank
    for a, b, n in ((1, 1, 2), (1, 1, 4), (1, 2, 3), (2, 2, 4), (2, 3, 5), (3, 3, 4), (4, 2, 6)):
        ok = ok and spanned_sum(a, b, n) == finite_moment(a, b, n) * 2 ** (a * (n - 1))
    ok = ok and spanned_sum(2, 2, 4) == F(192, 17) == 1 + F(105, 17) + F(70, 17)
    ok = ok and [gbin(3, r) for r in range(4)] == [1, 7, 7, 1] and galois(6) == 2825
    ok = ok and haar_moment(4, 4, 4) * 64 < 14 < 16
    GA.check("every clause of this function holds", ok)


def sector_trace(dA, dB, sg, tau):
    """Tr of P_tau on A times P_sg on B over n copies of the parity sector, by enumeration."""
    n = len(sg)
    total = 0
    for avals in product(range(dA), repeat=n):
        if any(avals[tau[i]] != avals[i] for i in range(n)):
            continue
        for bvals in product(range(dB), repeat=n):
            if any(bvals[sg[i]] != bvals[i] for i in range(n)):
                continue
            if all(wt(avals[i]) % 2 == wt(bvals[i]) % 2 for i in range(n)):
                total += 1
    return total


def check_parity_sector_moments_are_the_sector_values_not_the_imported_ones():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.imported-haar-moments-of-random-pure-state")
    ok = True
    # the trace count behind the sector moments
    for dA, dB, n in ((2, 2, 2), (2, 4, 2), (4, 4, 2), (2, 2, 3), (2, 4, 3)):
        for sg, tau in perm_pairs(n):
            ok = ok and sector_trace(dA, dB, sg, tau) == 2 * F(dA, 2) ** cycles(tau) * F(dB, 2) ** cycles(sg)
    for a in range(1, 6):
        for b in range(1, 6):
            dA, dB = 2 ** a, 2 ** b
            ok = ok and haar_moment(dA, dB, 2, sector=True) == F(dA + dB, dA * dB + 2)
            ok = ok and haar_moment(dA, dB, 2, sector=True) < haar_moment(dA, dB, 2)
    # the third sector moment in closed form, and the pair count behind it
    for a in range(1, 5):
        for b in range(1, 5):
            dA, dB = 2 ** a, 2 ** b
            D = dA * dB
            ok = ok and haar_moment(dA, dB, 3, sector=True) == F(dA * dA + dB * dB + 3 * D + 4, (D + 2) * (D + 4))
        evens = [x for x in range(1, 1 << (2 * a)) if wt(x) % 2 == 0]
        E = len(evens) + 1
        ok = ok and E == 2 ** (2 * a - 1)
        if a <= 3:
            npairs = sum(1 for x in evens for y in evens if x != y and bform(x, y) == 0)
            ok = ok and npairs == (E - 2) * (E // 2 - 1)
    # the orbit of the parity-preserving normaliser: Lagrangians containing the full string
    for m in (2, 3, 4):
        full = (1 << (2 * m)) - 1
        even = [x for x in range(1, full + 1) if wt(x) % 2 == 0]
        orb = orbit(vacuum(m), even)
        ok = ok and all(full in L for L in orb) and len(orb) == n_lagrangian(m - 1)
        for a in range(1, m):
            dA, dB = 2 ** a, 2 ** (m - a)
            for n in (2, 3):
                ok = ok and orbit_moment(orb, a, n) == haar_moment(dA, dB, n, sector=True)
                ok = ok and orbit_moment(orb, a, n) != haar_moment(dA, dB, n)
            ok = ok and orbit_moment(orb, a, 4) > haar_moment(dA, dB, 4, sector=True)
    ok = ok and haar_moment(2, 2, 2, sector=True) == F(2, 3) and haar_moment(4, 4, 2, sector=True) == F(4, 9)
    # two modes in Cl(4,1): the six states reached from the vacuum by the six bivector quarter turns
    h01 = hermitian((0, 1))
    h23 = hermitian((2, 3))
    parity = GA.mul(h01, h23, SQ5)
    rho0 = GA.scal(F(1, 4), GA.mul(GA.add(ONE, h01), GA.add(ONE, h23), SQ5))
    turns = []
    for i, j in combinations(range(4), 2):
        g = blade((i, j), SQ5)
        ok = ok and GA.eq(GA.mul(GA.add(ONE, g), GA.reverse(GA.add(ONE, g)), SQ5), GA.sc(2))
        turns.append(GA.add(ONE, g))
    states = [rho0]
    todo = [rho0]
    while todo:
        r = todo.pop()
        for R in turns:
            s = GA.scal(F(1, 2), GA.mul(GA.mul(R, r, SQ5), GA.reverse(R), SQ5))
            if not any(GA.eq(s, t) for t in states):
                states.append(s)
                todo.append(s)
    ok = ok and len(states) == 6
    ok = ok and all(GA.eq(GA.mul(parity, s, SQ5), s) and GA.eq(GA.mul(s, s, SQ5), s) for s in states)
    purities = sorted(reduced_moment(s, 2) for s in states)
    ok = ok and purities == [F(1, 2)] * 4 + [F(1)] * 2
    ok = ok and sum(purities) / 6 == F(2, 3) == F(2 + 2, 2 * 2 + 2) and F(2, 3) != F(4, 5)
    # the crossing bound of the stored comparison: ln 2 - ln(1 + 2/m^2) in place of ln 2 - ln(1 + 1/m^2)
    for mm in (2, 4, 8, 16):
        ok = ok and haar_moment(mm, mm, 2, sector=True) == F(2, mm) / (1 + F(2, mm * mm))
        ok = ok and haar_moment(mm, mm, 2) == F(2, mm) / (1 + F(1, mm * mm))
    GA.check("every clause of this function holds", ok)


def class_orbits_of_bivector_turns(m):
    full = (1 << (2 * m)) - 1
    pairs = [x for x in range(1, full + 1) if wt(x) == 2]
    reps = {min(x, x ^ full) for x in range(1, full) if wt(x) % 2 == 0}
    seen = set()
    sizes = []
    for c in sorted(reps):
        if c in seen:
            continue
        comp = {c}
        todo = [c]
        while todo:
            x = todo.pop()
            for w in pairs:
                y = x ^ w if bform(x, w) else x
                y = min(y, y ^ full)
                if y not in comp:
                    comp.add(y)
                    todo.append(y)
        seen |= comp
        sizes.append(len(comp))
    return sorted(sizes)


def check_bivector_quarter_turns_alone_fail_first_at_eight_directions():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    ok = True
    sizes = {}
    for m in (2, 3, 4):
        full = (1 << (2 * m)) - 1
        even = [x for x in range(1, full + 1) if wt(x) % 2 == 0]
        pairs = [x for x in even if wt(x) == 2]
        sizes[m] = (len(orbit(vacuum(m), pairs)), len(orbit(vacuum(m), even)))
        # orbits of the bivector transvections on the nonzero even strings modulo the full string
        classes = {frozenset([x, x ^ full]) for x in even if x != full}
        seen = set()
        orbs = []
        for c in sorted(classes, key=sorted):
            if c in seen:
                continue
            comp = {c}
            todo = [c]
            while todo:
                d = todo.pop()
                x = min(d)
                for w in pairs:
                    y = x ^ w if bform(x, w) else x
                    e = frozenset([y, y ^ full])
                    if e not in comp:
                        comp.add(e)
                        todo.append(e)
            seen |= comp
            orbs.append(len(comp))
        if m == 2:
            ok = ok and sorted(orbs) == [3]
        if m == 3:
            ok = ok and sorted(orbs) == [15]
        if m == 4:
            ok = ok and sorted(orbs) == [28, 35]
            ok = ok and sum(1 for c in classes if qform(min(c)) == 1) == 28
            ok = ok and all(qform(x) == qform(x ^ full) for x in even)
        ok = ok and qform(full) == m % 2
    ok = ok and sizes == {2: (3, 3), 3: (15, 15), 4: (105, 135)}
    ok = ok and class_orbits_of_bivector_turns(5) == [45, 210] and class_orbits_of_bivector_turns(4) == [28, 35]
    # six modes: the values of q on the classes (minus type), not their orbits
    full6 = (1 << 12) - 1
    reps = {min(x, x ^ full6) for x in range(1, full6) if wt(x) % 2 == 0}
    ok = ok and sum(1 for x in reps if qform(x) == 1) == 528 and sum(1 for x in reps if qform(x) == 0) == 495
    full = (1 << 8) - 1
    pairs = [x for x in range(1, full + 1) if wt(x) == 2]
    rot = orbit(vacuum(4), pairs)
    ok = ok and orbit_moment(rot, 2, 2) == F(17, 35)
    ok = ok and haar_moment(4, 4, 2, sector=True) == F(4, 9) and haar_moment(4, 4, 2) == F(8, 17)
    ok = ok and orbit_moment(rot, 1, 2) == F(4, 7) and haar_moment(2, 8, 2, sector=True) == F(5, 9)
    one_quartic = orbit(vacuum(4), pairs + [15])
    ok = ok and len(one_quartic) == 135 and orbit_moment(one_quartic, 2, 2) == F(4, 9)
    # in the algebra: which blades give unit-norm quarter turns, and the unit of the even subalgebra
    for nn, psq in ((6, -1), (8, 1)):
        sq = GA.sig(nn, 0)
        P = blade(range(nn), sq)
        ok = ok and GA.eq(GA.mul(P, P, sq), GA.sc(psq))
        two = GA.add(ONE, blade((0, 1), sq))
        four = GA.add(ONE, blade((0, 1, 2, 3), sq))
        six = GA.add(ONE, blade((0, 1, 2, 3, 4, 5), sq))
        ok = ok and GA.eq(GA.mul(two, GA.reverse(two), sq), GA.sc(2))
        ok = ok and GA.eq(GA.mul(six, GA.reverse(six), sq), GA.sc(2))
        ok = ok and not GA.eq(GA.mul(four, GA.reverse(four), sq), GA.sc(2))
        ok = ok and all(GA.commutes(P, blade((i, j), sq), sq) for i, j in combinations(range(nn), 2))
    sq6 = GA.sig(6, 0)
    P6 = blade(range(6), sq6)
    partner = GA.mul(P6, blade((0, 1, 2, 3), sq6), sq6)
    ok = ok and (GA.eq(partner, blade((4, 5), sq6)) or GA.eq(partner, GA.neg(blade((4, 5), sq6))))
    GA.check("every clause of this function holds", ok)


LN2_TERMS = 12
LN2_LOW = F(2, 3)
LN2_HIGH = F(7, 10)


def ln2_bracket(K):
    """Rational bracket of ln 2 = sum_{k>=1} 1/(k 2^k): partial sum and partial sum plus the tail bound."""
    s = sum(F(1, k * 2 ** k) for k in range(1, K + 1))
    return s, s + F(1, (K + 1) * 2 ** K)


def page_entropy(m, n):
    return sum(F(1, k) for k in range(n + 1, m * n + 1)) - F(m - 1, 2 * n)


def crossing_deficit(c):
    return sum(F((c - e) * rank_count(c, c, e)) for e in range(c + 1)) / n_lagrangian(2 * c)


def check_mean_entropy_of_the_finite_average_is_not_the_page_value():
    premise("singularity.imported-page-average-entropy-subsystem")
    lo, hi = ln2_bracket(LN2_TERMS)
    GA.check("ln 2 lies in (2/3, 7/10)", LN2_LOW < lo < hi < LN2_HIGH)
    # one against one: entropy e ln 2 on rank 2^e, mean (6/15) ln 2 against Page's 1/3
    mean_rank = sum(F(e * rank_count(1, 1, e)) for e in (0, 1)) / n_lagrangian(2)
    GA.check("mean rank exponent is 2/5", mean_rank == F(2, 5))
    GA.check("Page's value at 2 x 2 is 1/3", page_entropy(2, 2) == F(1, 3))
    GA.check("(2/5) ln 2 < 7/25 < 1/3", mean_rank * hi < F(7, 25) < page_entropy(2, 2))
    # at the crossing the finite average sits below the maximum by E[c - e] ln 2
    GA.check("deficit at c = 1 is 3/5", crossing_deficit(1) == F(3, 5))
    GA.check("deficit at c = 2 is 40/51", crossing_deficit(2) == F(40, 51))
    GA.check("deficit at c = 3 is 921/1105", crossing_deficit(3) == F(921, 1105))
    for c in (8, 16, 24):
        d = crossing_deficit(c)
        GA.check("deficit between 0.84 and 0.86 units of ln 2", F(21, 25) < d < F(43, 50))
        GA.check("deficit above 0.56 > 1/2", d * lo > F(14, 25) > F(1, 2))
    # Page's deficit ln d - <S> at d = 4, with ln 4 = 2 ln 2
    GA.check("Page's 4 x 4 value", page_entropy(4, 4) == F(664789, 720720))
    GA.check("Page's deficit at d = 4 lies in (2/5, 1/2)", F(2, 5) < 2 * lo - page_entropy(4, 4) and 2 * hi - page_entropy(4, 4) < F(1, 2))
