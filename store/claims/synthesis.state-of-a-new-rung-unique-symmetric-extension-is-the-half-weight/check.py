"""synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight: exact checks.

Cl_Q(n,n) with generators in the order e_1, f_1, e_2, f_2, ... (squares +1, -1), ladder pairs
v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2. A state is given by a density element rho:
omega(x) = <rho x>_0 / <rho>_0. The adjoint of Premise (P) fixes each e_j, negates each f_j and
reverses products.
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
        s = F(-1) ** (g * (g - 1) // 2) * F(-1) ** sum(1 for i in b if i % 2 == 1)
        out[b] = s * c
    return out


def flip(x, which):
    """The automorphism changing the sign of the generators whose indices are in `which`."""
    return {b: c * F(-1) ** sum(1 for i in b if i in which) for b, c in x.items()}


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
    G = [[Om(mul(a, dagger(b), S)) for b in B] for a in B]
    return psd(G)


def tau_el(j, t, S):
    return add(scal(t, mul(v(j), w(j), S)), scal(1 - t, mul(w(j), v(j), S)))


def old_densities(l, S):
    """Sample even states on the first l rungs: an atom (all off) and a mixed one."""
    off = sc(1)
    mixed = sc(1)
    for j in range(l):
        off = mul(off, mul(w(j), v(j), S), S)
        mixed = mul(mixed, tau_el(j, F(1, 3) + F(j, 5), S), S)
    return [off, mixed]


def check_both_values_extend_the_state_under_p():
    premise("synthesis.premise-positivity-of-values")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("rungs.imported-totality-minimality-completion")
    ok = True
    ts = (F(-1, 5), F(0), F(2, 5), F(1), F(6, 5))
    weights = (F(-1, 5), F(0), F(2, 5), F(1), F(6, 5))      # the weight on "on", stated independently
    positive = (False, True, True, True, False)             # (P) holds exactly for 0 <= t <= 1
    for l in (1, 2):
        n = l + 1
        S = sq(n)
        oldB = blades(range(2 * l))
        on_new = mul(v(l), w(l), S)
        on_old = mul(v(0), w(0), S)
        for rho in old_densities(l, S):
            om = state(rho, S)
            for t, wt, pos in zip(ts, weights, positive):
                Om = state(mul(rho, tau_el(l, t, S), S), S)
                ok = ok and all(Om(a) == om(a) for a in oldB)              # it extends omega
                ok = ok and Om(on_new) == wt                               # its weight on "on"
                ok = ok and Om(mul(on_old, on_new, S)) == wt * om(on_old)  # product with the old rung
                ok = ok and satisfies_p(Om, n, S) == pos
        # the mixed sample state gives the first old rung the weight 1/3
        ok = ok and state(old_densities(l, S)[1], S)(on_old) == F(1, 3)
        ok = ok and state(old_densities(l, S)[0], S)(on_old) == 0
    GA.check("on, off and every weight between them extend the state under (P); weights outside [0,1] do not", ok)
    return ok


def check_one_invariant_extension_with_weight_one_half():
    premise("synthesis.premise-positivity-of-values")
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    premise("synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state")
    ok = True
    for l in (1, 2):
        n = l + 1
        S = sq(n)
        ie, jf = 2 * l, 2 * l + 1
        allB = blades(range(2 * n))
        oldB = blades(range(2 * l))
        syms = [{ie}, {jf}, {ie, jf}]
        # the symmetries fix the old algebra pointwise and commute with the adjoint of (P)
        for g in syms:
            ok = ok and all(flip(a, g) == a for a in oldB)
            ok = ok and all(flip(dagger(b), g) == dagger(flip(b, g)) for b in allB)
        # the sign change of f exchanges set and clear, on and off; that of e does so up to a sign
        on, off = mul(v(l), w(l), S), mul(w(l), v(l), S)
        ok = ok and flip(v(l), {jf}) == w(l) and flip(on, {jf}) == off
        ok = ok and flip(v(l), {ie}) == scal(-1, w(l)) and flip(on, {ie}) == off
        ok = ok and flip(on, {ie, jf}) == on
        # every blade that contains a new generator is negated by one of the symmetries, so an
        # invariant linear functional vanishes on it: the invariant extension is unique
        for b in allB:
            (key,) = b.keys()
            if ie in key or jf in key:
                ok = ok and any(flip(b, g) == scal(-1, b) for g in syms)
        # its weight on "on" is the scalar part of v w, which is 1/2, not an integer
        ok = ok and s0(on) == F(1, 2) and s0(on).denominator == 2 and s0(off) == F(1, 2)
        for rho in old_densities(l, S):
            om = state(rho, S)
            half = state(mul(rho, tau_el(l, F(1, 2), S), S), S)
            for b in allB:
                (key,) = b.keys()
                if ie in key or jf in key:
                    ok = ok and half(b) == 0
                else:
                    ok = ok and half(b) == om(b)
            # among the weights t, only t = 1/2 is invariant
            for t in (F(0), F(1, 3), F(1, 2), F(2, 3), F(1)):
                Om = state(mul(rho, tau_el(l, t, S), S), S)
                inv = all(Om(flip(b, g)) == Om(b) for b in allB for g in syms)
                ok = ok and (inv == (t == F(1, 2)))
        # the density of weight t is idempotent (the state is sharp on that rung) exactly at t = 0, 1
        for t in (F(0), F(1, 3), F(1, 2), F(1)):
            d = tau_el(l, t, S)
            ok = ok and ((mul(d, d, S) == d) == (t in (F(0), F(1))))
    GA.check("one extension is invariant under the step's symmetries: weight 1/2 on 'on', not sharp, not integer", ok)
    return ok


def check_strings_form_one_orbit_and_two_rotor_classes():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.exchange-of-set-and-clear-is-inner-and-fixed-by-no-integer-state")
    m = 3
    S = sq(m)
    ok = True

    def proj(s):
        P = sc(1)
        for j in range(m):
            P = mul(P, mul(v(j), w(j), S) if s[j] else mul(w(j), v(j), S), S)
        return P

    strings = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    P = {s: proj(s) for s in strings}
    # the eight projectors are distinct, pairwise orthogonal idempotents summing to 1
    ok = ok and all(mul(P[s], P[s], S) == P[s] for s in strings)
    ok = ok and all(mul(P[s], P[r], S) == {} for s in strings for r in strings if s != r)
    ok = ok and add(*P.values()) == sc(1)
    # the sign change of f_j flips the j-th value: one orbit of size 8 from the all-off string
    reached = set()
    for g in strings:
        which = {2 * j + 1 for j in range(m) if g[j]}
        img = flip(P[(0, 0, 0)], which)
        hit = [s for s in strings if P[s] == img]
        ok = ok and hit == [g]
        reached.add(g)
    ok = ok and len(reached) == 8
    # two flips at once are conjugation by the rotor f_i f_j
    for i, j in ((0, 1), (0, 2), (1, 2)):
        R = mul(f(i), f(j), S)
        Rt = GA.reverse(R)
        ok = ok and mul(R, Rt, S) == sc(1)
        for s in strings:
            r = list(s)
            r[i] ^= 1
            r[j] ^= 1
            ok = ok and mul(mul(R, P[s], S), Rt, S) == P[tuple(r)]
    # the volume element commutes with every bivector (so with every rotor) and takes one sign on
    # the strings of even weight and the other on those of odd weight: exactly two classes
    Gam = sc(1)
    for j in range(m):
        Gam = mul(Gam, mul(f(j), e(j), S), S)
    for a, b in combinations(range(2 * m), 2):
        B = mul(gen(a), gen(b), S)
        ok = ok and mul(Gam, B, S) == mul(B, Gam, S)
    signs = {}
    for s in strings:
        GP = mul(Gam, P[s], S)
        ok = ok and (GP == P[s] or GP == scal(-1, P[s]))
        signs[s] = 1 if GP == P[s] else -1
    ok = ok and all(signs[s] == signs[(0, 0, 0)] * (-1) ** sum(s) for s in strings)
    ok = ok and sorted(signs.values()).count(1) == 4
    GA.check("the 8 strings on 3 rungs are one orbit of the sign changes and exactly 2 classes under rotors", ok)
    return ok


def check_a_string_is_a_weight_on_one_context():
    premise("synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them")
    S = sq(2)
    ok = True
    occ = []
    for a in (0, 1):
        for b in (0, 1):
            P = mul(mul(v(0), w(0), S) if a else mul(w(0), v(0), S),
                    mul(v(1), w(1), S) if b else mul(w(1), v(1), S), S)
            occ.append(P)
    # the four occupation projectors of two rungs form one context
    ok = ok and add(*occ) == sc(1)
    ok = ok and all(mul(occ[i], occ[j], S) == ({} if i != j else occ[i]) for i in range(4) for j in range(4))
    ok = ok and all(dagger(Pi) == Pi and s0(Pi) == F(1, 4) for Pi in occ)
    # a string gives this context the weights 1, 0, 0, 0
    Om = state(occ[2], S)
    ok = ok and sorted(Om(Pi) for Pi in occ) == [0, 0, 0, 1]
    # an atom of another context gets a weight strictly between 0 and 1 from the same string
    y = add(occ[2], mul(v(1), occ[2], S))          # rung 1 on, rung 2 in an equal combination
    Pi = scal(F(1, 2), mul(y, dagger(y), S))
    ok = ok and mul(Pi, Pi, S) == Pi and dagger(Pi) == Pi and Om(Pi) == F(1, 2)
    GA.check("a string of rung values is a two-valued weight on one context and gives 1/2 on an atom of another", ok)
    return ok
