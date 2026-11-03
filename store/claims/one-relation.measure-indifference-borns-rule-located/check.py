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
The identification of this density with occupation weight beyond that, and the residual postulate, are
statements of level and are not computable.
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


def even(c):
    return {b: F(x) for b, x in zip(EVEN, c) if x}


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
