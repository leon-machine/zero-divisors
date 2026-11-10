"""one-relation.measure-indifference-borns-rule-located: exact checks of the computable parts.

(1) The located density (GA.py, Cl(1,3), signature (+,-,-,-)): for even multivectors psi (Hestenes spinors,
    8 real components) the geometric current J = psi gamma_0 psi~ is a vector; its gamma_0 component is the
    sum of the squares of the 8 components of psi (positive, zero only at psi = 0); J^2 = a^2 + b^2 with
    psi psi~ = a + b I, so J is causal and future-pointing; for a boosted frame gamma_0' = R gamma_0 R~
    the component J . gamma_0' is again positive but differs: the density is frame-relative.
(2) Indifference on exact orbits: the weight vectors invariant under a permutation group of n equal-norm
    components form a space whose dimension is computed as a kernel and equals the number of orbits
    (computed independently by union-find): one (the uniform vector) for all transpositions with
    n = 2..5 and for the transitive Klein four-group; three and two for one and two disjoint
    transpositions on four components.
(3) Fine-graining: for squared amplitudes 9/25 + 16/25, 25/169 + 144/169, 64/289 + 225/289, the
    equal-weight assignment to N constituents (N the common denominator) returns the squared norms on the
    branches, given additivity (the presupposition the claim isolates).
    From version 4 the fine-graining route is prior art (the envariance argument) and is not a step of the
    statement; the check is kept because the same numbers are returned by (5) with no fine-graining.
(4) The density is the squared norm of the split: in Cl(1,3) the blade inverse is x -> gamma_0 x~ gamma_0;
    gamma_0 is the only blade of square +1 that commutes with gamma_0, so (1 + gamma_0)/2 is built from a
    maximal commuting set; for even psi the scalar part of psi^dagger psi is J . gamma_0 and the squared
    norm of the ideal element psi (1 + gamma_0)/2 is half of it; the atom of psi equals the atom of
    psi gamma_2 gamma_3 although the two spin vectors psi gamma_3 psi~ differ.
(5) The weights of a state sharp on an atom (the cited theorem's functional) are ratios of squared norms:
    on two modes the one-particle elements 3 w_1 + 4 w_2, 5 w_1 + 12 w_2, 8 w_1 + 15 w_2 give the number
    projectors the weights 9/25, 16/25 and so on, the numbers of (3); in Cl(1,3) the functional of the atom
    of a sample spinor gives three projectors the weights 23/34, 13/34, 11/17, equal to the squared-norm
    ratios. That a state of (P) sharp on the atom IS this functional is the cited theorem and is not
    recomputed here.
The identification of this density with occupation weight beyond that, Premise (P) and sharpness are
premises or statements of level and are not computable.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
EVEN = [b for b in GA.all_blades(4) if len(b) % 2 == 0]
PSIS = [[1, 2, 0, -1, 3, 0, 1, 1], [F(1, 2), 0, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 0, 2, 0, F(1, 3)],
        [2, 0, 1, 0, 0, 0, 0, -1]]
BOOST = (F(5, 4), F(3, 4))
GROUPS = [(n, [(i, i + 1) for i in range(n - 1)]) for n in (2, 3, 4, 5)] + \
         [(4, [(0, 1)]), (4, [(0, 1), (2, 3)]), (4, [(0, 1), (2, 3), (0, 2), (1, 3)])]
STATES = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17))]


ONE = GA.sc(F(1))
HALF = F(1, 2)
SQM = GA.sig(2, 2)
ONE_PARTICLE = [(3, 4), (5, 12), (8, 15)]
SPINOR_WEIGHTS = [F(23, 34), F(13, 34), F(11, 17)]


def even(c):
    return {b: F(x) for b, x in zip(EVEN, c) if x}


def dsign(b, sq):
    g = len(b)
    s = (-1) ** (g * (g - 1) // 2)
    for i in b:
        s *= sq[i]
    return s


def dagger(x, sq):
    return {b: c * dsign(b, sq) for b, c in x.items()}


def clean(x):
    return {b: c for b, c in x.items() if c != 0}


def prod(sq, *xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return clean(r)


def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return clean(r)


def tau(x):
    return x.get((), F(0))


def norm2(x, sq):
    return tau(prod(sq, dagger(x, sq), x))


def orbit_atom(psi, P, sq):
    n = tau(prod(sq, P, dagger(psi, sq), psi)) / tau(P)
    return GA.scal(F(1) / n, prod(sq, psi, P, dagger(psi, sq)))


def check_density_is_positive_and_frame_relative():
    premise("one-relation.dirac-current-conserved-density")
    g0 = GA.gen(0)
    R = GA.add(GA.sc(BOOST[0]), GA.scal(BOOST[1], GA.mul(GA.gen(0), GA.gen(1), SQ)))
    g0p = GA.mul(GA.mul(R, g0, SQ), GA.reverse(R), SQ)
    ok = GA.eq(GA.mul(R, GA.reverse(R), SQ), GA.sc(1))
    dens = []
    for c in PSIS:
        psi = even(c)
        J = GA.mul(GA.mul(psi, g0, SQ), GA.reverse(psi), SQ)
        ok = ok and all(len(b) == 1 for b in J)
        j0 = GA.dot(J, g0, SQ)
        ok = ok and j0 == sum(F(x) * F(x) for x in c) and j0 > 0
        pp = GA.mul(psi, GA.reverse(psi), SQ)
        a, b = pp.get((), F(0)), pp.get((0, 1, 2, 3), F(0))
        ok = ok and set(pp) <= {(), (0, 1, 2, 3)} and GA.dot(J, J, SQ) == a * a + b * b
        jp = GA.dot(J, g0p, SQ)
        ok = ok and jp > 0
        dens.append((j0, jp))
    ok = ok and any(j0 != jp for j0, jp in dens)
    ok = ok and dens[0][0] == 17 and dens[1] == (F(1, 4), F(17, 32))
    _tp_rv = (ok); assert _tp_rv is not False, "check_density_is_positive_and_frame_relative"; return _tp_rv


def orbits(n, gens):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i, j in gens:
        parent[find(i)] = find(j)
    return len({find(x) for x in range(n)})


def check_indifference_forces_equality_on_transitive_orbits():
    premise("one-relation.imported-indifference-instrument")
    dims = []
    ok = True
    for n, gens in GROUPS:
        rows = []
        for i, j in gens:
            row = [F(0)] * n
            row[i], row[j] = F(1), F(-1)
            rows.append(row)
        ker = GA.field_kernel(rows)
        ok = ok and len(ker) == orbits(n, gens)
        if len(ker) == 1:
            ok = ok and len(set(ker[0])) == 1
        dims.append(len(ker))
    ok = ok and dims == [1, 1, 1, 1, 3, 2, 1]
    _tp_rv = (ok); assert _tp_rv is not False, "check_indifference_forces_equality_on_transitive_orbits"; return _tp_rv


def check_fine_graining_returns_squared_norms():
    ok = True
    for a, b in STATES:
        ok = ok and a * a + b * b == 1
        N = (a * a).denominator
        na, nb = (a * a * N).numerator, (b * b * N).numerator
        ok = ok and na + nb == N
        w = [F(1, N)] * N
        ok = ok and sum(w[:na]) == a * a and sum(w[na:]) == b * b
    ok = ok and [(a * a).denominator for a, b in STATES] == [25, 169, 289]
    _tp_rv = (ok); assert _tp_rv is not False, "check_fine_graining_returns_squared_norms"; return _tp_rv


def check_squared_norm_of_the_split_is_the_dirac_density():
    premise("one-relation.dirac-current-conserved-density")
    premise("synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional")
    g = [GA.gen(i) for i in range(4)]
    blades = [{b: F(1)} for b in GA.all_blades(4)]
    ok = all(GA.eq(dagger(x, SQ), prod(SQ, g[0], GA.reverse(x), g[0])) for x in blades)
    plus = [x for x in blades if tau(prod(SQ, x, x)) == 1 and not GA.eq(x, ONE)]
    ok = ok and len(plus) == 5 and [x for x in plus if GA.commutes(x, g[0], SQ)] == [g[0]]
    P = lin((HALF, ONE), (HALF, g[0]))
    ok = ok and GA.eq(prod(SQ, P, P), P) and GA.eq(dagger(P, SQ), P) and tau(P) == HALF
    r = prod(SQ, g[2], g[3])
    ok = ok and GA.commutes(r, g[0], SQ) and GA.eq(prod(SQ, r, dagger(r, SQ)), ONE)
    spins_differ = 0
    for c in PSIS:
        psi = clean(even(c))
        J = prod(SQ, psi, g[0], GA.reverse(psi))
        j0 = GA.dot(J, g[0], SQ)
        ok = ok and norm2(psi, SQ) == j0 and 2 * norm2(prod(SQ, psi, P), SQ) == j0
        A = orbit_atom(psi, P, SQ)
        psir = prod(SQ, psi, r)
        ok = ok and GA.eq(prod(SQ, A, A), A) and GA.eq(dagger(A, SQ), A) and tau(A) == HALF
        ok = ok and GA.eq(A, orbit_atom(psir, P, SQ))
        s1 = prod(SQ, psi, g[3], GA.reverse(psi))
        s2 = prod(SQ, psir, g[3], GA.reverse(psir))
        spins_differ += 0 if GA.eq(s1, s2) else 1
    ok = ok and spins_differ == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_squared_norm_of_the_split_is_the_dirac_density"; return _tp_rv


def check_sharp_state_weights_are_squared_norm_ratios():
    premise("synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional")
    ok = True
    # two modes: e_j = gen(j), f_j = gen(2 + j); v_j annihilates the vacuum projector, w_j = v_j^dagger
    e, f = [GA.gen(0), GA.gen(1)], [GA.gen(2), GA.gen(3)]
    v = [lin((HALF, e[j]), (HALF, f[j])) for j in range(2)]
    w = [lin((HALF, e[j]), (-HALF, f[j])) for j in range(2)]
    par = [prod(SQM, f[j], e[j]) for j in range(2)]
    P0 = prod(SQM, lin((HALF, ONE), (HALF, par[0])), lin((HALF, ONE), (HALF, par[1])))
    num = [prod(SQM, w[j], v[j]) for j in range(2)]
    ok = ok and all(prod(SQM, v[j], P0) == {} and GA.eq(dagger(v[j], SQM), w[j]) for j in range(2))
    ok = ok and all(GA.eq(prod(SQM, n, n), n) and GA.eq(dagger(n, SQM), n) for n in num)
    ok = ok and prod(SQM, num[0], num[1], w[0], P0) == {} and tau(P0) == F(1, 4)
    for (a, b), (sa, sb) in zip(ONE_PARTICLE, STATES):
        psi = lin((a, w[0]), (b, w[1]))
        y = prod(SQM, psi, P0)
        A = orbit_atom(psi, P0, SQM)
        ok = ok and GA.eq(prod(SQM, lin((1, num[0]), (1, num[1])), y), y)
        got = []
        for n in num:
            z = prod(SQM, n, y)
            ratio = norm2(z, SQM) / norm2(y, SQM)
            ok = ok and tau(prod(SQM, A, n)) / tau(P0) == ratio
            got.append(ratio)
        ok = ok and got == [sa * sa, sb * sb] and sum(got) == 1
    # the Dirac algebra: the atom of a sample even spinor, three projectors of the algebra
    g = [GA.gen(i) for i in range(4)]
    P = lin((HALF, ONE), (HALF, g[0]))
    psi = clean(even(PSIS[0]))
    y = prod(SQ, psi, P)
    A = orbit_atom(psi, P, SQ)
    projs = [lin((HALF, ONE), (HALF, prod(SQ, g[0], g[1]))), lin((HALF, ONE), (HALF, prod(SQ, g[1], g[2], g[3]))), P]
    got = []
    for E in projs:
        ok = ok and GA.eq(prod(SQ, E, E), E) and GA.eq(dagger(E, SQ), E)
        z = prod(SQ, E, y)
        ratio = norm2(z, SQ) / norm2(y, SQ)
        ok = ok and tau(prod(SQ, A, E)) / tau(P) == ratio and 0 <= ratio <= 1
        got.append(ratio)
    ok = ok and got == SPINOR_WEIGHTS
    _tp_rv = (ok); assert _tp_rv is not False, "check_sharp_state_weights_are_squared_norm_ratios"; return _tp_rv
