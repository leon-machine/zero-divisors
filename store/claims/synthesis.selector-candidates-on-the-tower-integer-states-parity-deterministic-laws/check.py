"""synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws: exact checks.

Cl_Q(n,n) with generators in the order e_1, f_1, e_2, f_2, ... (squares +1, -1), ladder pairs
v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2, tests on_j = v_j w_j, off_j = w_j v_j. A state is given by a
density element rho: omega(x) = <rho x>_0 / <rho>_0. The adjoint of Premise (P) fixes each e_j,
negates each f_j and reverses products.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from GA import add, sub, scal, mul, gen, sc
from tp_premise import premise


def sq(n):
    return tuple([1, -1] * n)


def e(j):
    return gen(2 * j)


def f(j):
    return gen(2 * j + 1)


def v(j):
    return scal(F(1, 2), add(e(j), f(j)))


def w(j):
    return scal(F(1, 2), sub(e(j), f(j)))


def blades(idx):
    out = []
    for r in range(len(idx) + 1):
        for c in combinations(idx, r):
            out.append({tuple(c): F(1)})
    return out


def dagger(x):
    out = {}
    for b, c in x.items():
        g = len(b)
        out[b] = c * F(-1) ** (g * (g - 1) // 2) * F(-1) ** sum(1 for i in b if i % 2 == 1)
    return out


def s0(x):
    return x.get((), F(0))


def state(rho, S):
    n = s0(rho)
    return lambda x: s0(mul(rho, x, S)) / n


def psd(G):
    """Exact test that a symmetric rational matrix is positive semidefinite (Schur complements)."""
    G = [row[:] for row in G]
    n = len(G)
    for k in range(n):
        if G[k][k] < 0:
            return False
        if G[k][k] == 0:
            if any(G[k][j] != 0 for j in range(k + 1, n)):
                return False
            continue
        for i in range(k + 1, n):
            if G[i][k] != 0:
                m = G[i][k] / G[k][k]
                for j in range(k, n):
                    G[i][j] -= m * G[k][j]
    return True


def satisfies_p(Om, n, S):
    B = blades(range(2 * n))
    if Om(sc(1)) != 1:
        return False
    if any(Om(dagger(b)) != Om(b) for b in B):
        return False
    return psd([[Om(mul(a, dagger(b), S)) for b in B] for a in B])


def is_even(x):
    return all(len(k) % 2 == 0 for k in x)


def rank(M):
    M = [r[:] for r in M]
    rk = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                q = M[i][c] / M[rk][c]
                M[i] = [x - q * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk


def check_integer_states_of_one_rung_in_the_two_integer_forms():
    premise("synthesis.premise-positivity-of-values")
    premise("synthesis.integer-clifford-algebras-contain-no-switch")
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    S = sq(1)
    on = mul(v(0), w(0), S)
    found = []
    for a in (-1, 0, 1):
        for c in (-1, 0, 1):
            for b in (-1, 0, 1):
                # omega(e) = a, omega(f) = c, omega(f e) = b, so omega(e f) = -b
                vals = {(): F(1), (0,): F(a), (1,): F(c), (0, 1): F(-b)}

                def Om(x, vals=vals):
                    return sum(cc * vals[k] for k, cc in x.items())

                if satisfies_p(Om, 1, S):
                    found.append((a, c, b, Om(on), Om(v(0))))
    ok = len(found) == 5
    # ladder form: the weights on the on test are 0, 1/2 and 1, and 1/2 occurs three times
    ok = ok and sorted(r[3] for r in found) == [F(0), F(1, 2), F(1, 2), F(1, 2), F(1)]
    ok = ok and all(r[1] == 0 for r in found)
    # switch form (integer also on v, w and v w): only on and off survive
    sw = [r for r in found if r[3].denominator == 1 and r[4].denominator == 1]
    ok = ok and sorted((r[0], r[2], r[3]) for r in sw) == [(0, -1, F(0)), (0, 1, F(1))]
    # neither survivor has a weight strictly between 0 and 1 on the test or on the flip e
    ok = ok and all(r[0] == 0 and r[3] in (F(0), F(1)) for r in sw)
    GA.check("one rung: 5 integer states in the ladder form (weights 0, 1/2, 1), 2 in the switch form (on, off)", ok)
    return ok


def check_parity_gives_two_sectors_and_no_record_superselection():
    premise("synthesis.premise-positivity-of-values")
    premise("synthesis.records-keep-even-states-even-only-for-parity-homogeneous-observables")
    ok = True
    # (a) the centre of the even subalgebra of Cl(n,n) has dimension 2 (1 and the volume element), n = 2, 3
    for nn in (2, 3):
        Sn = sq(nn)
        allB = blades(range(2 * nn))
        evenB = [b for b in allB if is_even(b)]
        keys = [next(iter(b)) for b in allB]
        biv = [mul(gen(a), gen(b), Sn) for a, b in combinations(range(2 * nn), 2)]
        cols = []
        for b in evenB:
            col = []
            for Bv in biv:
                cm = sub(mul(b, Bv, Sn), mul(Bv, b, Sn))
                col += [cm.get(k, F(0)) for k in keys]
            cols.append(col)
        ok = ok and len(evenB) == 2 ** (2 * nn - 1)
        ok = ok and len(evenB) - rank([list(r) for r in zip(*cols)]) == 2
        Gam = sc(1)
        for j in range(nn):
            Gam = mul(Gam, mul(f(j), e(j), Sn), Sn)
        ok = ok and all(mul(Gam, Bv, Sn) == mul(Bv, Gam, Sn) for Bv in biv)
        ok = ok and all(mul(Gam, gen(i), Sn) == scal(-1, mul(gen(i), Gam, Sn)) for i in range(2 * nn))
    # (b) an even record coupling: system rungs 0, 1 (one quantum, weights 9/25 and 16/25), record
    # rungs 2, 3 (one quantum, moved from rung 2 to rung 3 when the system's quantum is on rung 0)
    S4 = sq(4)
    n = [mul(v(j), w(j), S4) for j in range(4)]
    one = sc(1)
    vac = one
    for j in range(4):
        vac = mul(vac, sub(one, n[j]), S4)
    y = mul(add(scal(F(3, 5), v(0)), scal(F(4, 5), v(1))), mul(v(2), vac, S4), S4)
    rho = mul(y, dagger(y), S4)
    ok = ok and mul(rho, rho, S4) == rho and is_even(rho)
    d = sub(n[2], n[3])
    X = add(sub(one, mul(d, d, S4)), mul(v(2), w(3), S4), mul(v(3), w(2), S4))
    ok = ok and mul(X, X, S4) == one and dagger(X) == X and is_even(X)
    U = add(sub(one, n[0]), mul(n[0], X, S4))
    ok = ok and mul(U, dagger(U), S4) == one and is_even(U)
    rho2 = mul(mul(U, rho, S4), dagger(U), S4)
    om = state(rho2, S4)
    R_a = mul(sub(one, n[2]), n[3], S4)        # record: quantum on rung 3 (system on rung 0)
    R_b = mul(n[2], sub(one, n[3]), S4)        # record: quantum on rung 2 (system on rung 1)
    ok = ok and om(R_a) == F(9, 25) and om(R_b) == F(16, 25)
    ok = ok and om(mul(R_a, n[0], S4)) == F(9, 25) and om(mul(R_b, n[1], S4)) == F(16, 25)
    # both record sectors have the same parity and the same total number
    Gam4 = one
    for j in range(4):
        Gam4 = mul(Gam4, mul(f(j), e(j), S4), S4)
    ok = ok and mul(Gam4, rho2, S4) == rho2
    ok = ok and mul(Gam4, mul(R_a, rho2, S4), S4) == mul(R_a, rho2, S4)
    ok = ok and mul(Gam4, mul(R_b, rho2, S4), S4) == mul(R_b, rho2, S4)
    N = add(*n)
    ok = ok and om(N) == 2 and om(mul(N, N, S4)) == 4
    # an even self-adjoint observable that sees the interference between the two records
    T = mul(mul(v(0), w(1), S4), mul(v(3), w(2), S4), S4)   # system quantum 1 -> 0, record quantum 2 -> 3
    O = add(T, dagger(T))
    ok = ok and is_even(O) and dagger(O) == O
    ok = ok and om(O) == F(24, 25)
    blockdiag = add(mul(mul(R_a, rho2, S4), R_a, S4), mul(mul(R_b, rho2, S4), R_b, S4))
    ok = ok and s0(blockdiag) == s0(rho2) and state(blockdiag, S4)(O) == 0
    # (c) a coupling that writes on a single rung changes parity: it is neither even nor odd, and it
    # sends an even state to a state that is not even
    S3 = sq(3)
    n0 = mul(v(0), w(0), S3)
    U1 = add(sub(sc(1), n0), mul(n0, e(2), S3))
    ok = ok and mul(U1, dagger(U1), S3) == sc(1)
    ev = {k: c for k, c in U1.items() if len(k) % 2 == 0}
    od = {k: c for k, c in U1.items() if len(k) % 2 == 1}
    ok = ok and ev != {} and od != {}
    vac3 = sc(1)
    for j in range(3):
        vac3 = mul(vac3, mul(w(j), v(j), S3), S3)
    y3 = mul(add(scal(F(3, 5), v(0)), scal(F(4, 5), v(1))), vac3, S3)
    rho3 = mul(y3, dagger(y3), S3)
    ok = ok and is_even(rho3)
    rho3b = mul(mul(U1, rho3, S3), dagger(U1), S3)
    ok = ok and not is_even(rho3b)
    GA.check("parity: two sectors; an even record coupling keeps both branches in one, interference 24/25 visible", ok)
    return ok


def check_no_deterministic_law_on_strings():
    premise("synthesis.premise-positivity-of-values")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    S = sq(2)
    one = sc(1)
    n1, n2 = mul(v(0), w(0), S), mul(v(1), w(1), S)
    P = {(0, 0): mul(sub(one, n1), sub(one, n2), S), (1, 0): mul(n1, sub(one, n2), S),
         (0, 1): mul(sub(one, n1), n2, S), (1, 1): mul(n1, n2, S)}
    Pi1 = add(P[(1, 0)], P[(0, 1)])
    h = sub(mul(v(0), w(1), S), mul(v(1), w(0), S))
    ok = mul(h, h, S) == scal(-1, Pi1) and dagger(h) == scal(-1, h)
    R = add(sub(one, Pi1), scal(F(3, 5), Pi1), scal(F(4, 5), h))
    # R is an even rotor: unit norm for the adjoint and for the reverse
    ok = ok and is_even(R) and mul(R, dagger(R), S) == one and mul(R, GA.reverse(R), S) == one
    om = state(P[(1, 0)], S)

    def moved(x):
        return om(mul(mul(dagger(R), x, S), R, S))

    wts = {s: moved(P[s]) for s in P}
    ok = ok and wts == {(0, 0): F(0), (1, 0): F(9, 25), (0, 1): F(16, 25), (1, 1): F(0)}
    # the start is one string with weight 1; a map of strings to strings gives every string weight 0 or 1
    ok = ok and sorted(om(P[s]) for s in P) == [0, 0, 0, 1]
    ok = ok and sum(1 for s in P if wts[s] not in (F(0), F(1))) == 2
    GA.check("an even rotor takes one string to weights 9/25 and 16/25 on two strings: no deterministic law", ok)
    return ok


def check_unread_rungs_carry_the_uniform_weight():
    premise("synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight")
    S = sq(3)
    one = sc(1)
    n = [mul(v(j), w(j), S) for j in range(3)]
    rho = mul(mul(sub(one, n[0]), scal(F(1, 2), one), S), scal(F(1, 2), one), S)   # rung 0 off, rungs 1, 2 symmetric
    om = state(rho, S)
    ok = om(n[0]) == 0
    for a in (0, 1):
        for b in (0, 1):
            Pab = mul(n[1] if a else sub(one, n[1]), n[2] if b else sub(one, n[2]), S)
            ok = ok and om(Pab) == F(1, 4)
    # invariance under the sign changes of the new generators: the state vanishes on every blade
    # containing a generator of rungs 1 or 2
    for b in blades(range(6)):
        (key,) = b.keys()
        if any(i >= 2 for i in key):
            ok = ok and om(b) == 0
    GA.check("two unread rungs in the symmetric extension: each of the 4 strings has weight 1/4", ok)
    return ok


def check_odd_coupling_and_the_stored_descent():
    premise("synthesis.premise-positivity-of-values")
    premise("tower.answers-iteration-question")
    ok = True
    S4 = sq(4)
    one = sc(1)
    n = [mul(v(j), w(j), S4) for j in range(4)]
    vac = one
    for j in range(4):
        vac = mul(vac, sub(one, n[j]), S4)
    amp = add(scal(F(3, 5), v(0)), scal(F(4, 5), v(1)))
    hop = mul(v(0), w(1), S4)
    O0 = add(hop, dagger(hop))                 # the system's own interference element

    def pinch(x):
        """The multi-mode descent: the sum of P_s x P_s over the 16 strings of four rungs."""
        out = {}
        for bits in range(16):
            P = one
            for j in range(4):
                P = mul(P, n[j] if (bits >> j) & 1 else sub(one, n[j]), S4)
            out = add(out, mul(mul(P, x, S4), P, S4))
        return out

    # (a) the odd homogeneous coupling: records on single rungs 2 and 3 (rungs 3 and 4 in the text)
    y = mul(amp, vac, S4)
    rho = mul(y, dagger(y), S4)
    ok = ok and mul(rho, rho, S4) == rho and is_even(rho)
    ok = ok and state(rho, S4)(O0) == F(24, 25)
    U = add(mul(sub(one, n[0]), e(3), S4), mul(n[0], e(2), S4))
    ok = ok and mul(U, dagger(U), S4) == one
    ok = ok and all(len(k) % 2 == 1 for k in U)                     # odd, so parity-homogeneous
    rho2 = mul(mul(U, rho, S4), dagger(U), S4)
    ok = ok and is_even(rho2)                                       # an even state stays even
    om = state(rho2, S4)
    R_a = mul(n[2], sub(one, n[3]), S4)                             # record on rung 2: system quantum on rung 0
    R_b = mul(sub(one, n[2]), n[3], S4)                             # record on rung 3: system quantum on rung 1
    ok = ok and om(R_a) == F(9, 25) and om(R_b) == F(16, 25)
    ok = ok and om(mul(R_a, n[0], S4)) == F(9, 25) and om(mul(R_b, n[1], S4)) == F(16, 25)
    O = mul(mul(U, O0, S4), dagger(U), S4)
    ok = ok and is_even(O) and dagger(O) == O and om(O) == F(24, 25)
    block = add(mul(mul(R_a, rho2, S4), R_a, S4), mul(mul(R_b, rho2, S4), R_b, S4))
    ok = ok and s0(block) == s0(rho2) and state(block, S4)(O) == 0
    # (b) the stored descent on the state after the coupling: record weights kept, interference gone
    d2 = pinch(rho2)
    od = state(d2, S4)
    ok = ok and s0(d2) == s0(rho2)
    ok = ok and od(R_a) == F(9, 25) and od(R_b) == F(16, 25) and od(O) == 0
    # (c) the stored descent on the state before any record: the system's own interference is gone too
    d0 = pinch(rho)
    ok = ok and s0(d0) == s0(rho) and state(d0, S4)(O0) == 0
    ok = ok and state(d0, S4)(n[0]) == F(9, 25) and state(d0, S4)(n[1]) == F(16, 25)
    GA.check("odd coupling keeps interference 24/25; the multi-mode descent removes it, keeps 9/25 and 16/25", ok)
    return ok
