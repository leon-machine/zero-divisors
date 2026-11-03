"""singularity.class-relative-no-go-no-supplied: exact checks in the three-point Fock model.

The Fock model (three points of E, one mode each, Jordan-Wigner 8 x 8 matrices) is taken from the
EXPORTS of singularity.bundle-maps-quantise-without-hopping.
(1) The supplied class. The one-particle maps that are function-linear are computed, not assumed:
    the common kernel of a -> [a, f] for two functions f (GA.field_kernel) has dimension 3 and
    consists of diagonal maps (Lemma: function-linear endomorphisms are bundle maps). Their second
    quantisations (the kernel basis and a generic combination) and the products of the parity
    sections sigma(x) over all 8 subsets of points are diagonal in the joint number basis
    (ultralocal) and commute with every N_x: no supplied generator hops.
(2) Pairing generators P_xy = psi_x^dag psi_y^dag + psi_y psi_x, for each of the 3 pairs x < y: they
    commute with the total parity Gamma = sigma_1 sigma_2 sigma_3, are not diagonal, do not commute
    with N_x, and carry |0 0> to |1 1> on the pair (total occupation changed by 2). Every dGamma(a),
    for all nine matrix units a, commutes with the total number N_tot, and P_xy does not, so P_xy is
    not of the form dGamma(a): it lies outside the class, as the statement says.
Not checked: Fact sheaf.function-linearity-tame-constructions (that the tame constructions supply
function-linear maps), which is a survey with no finite core.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

FUNCS = ((F(1), F(2), F(5)), (F(3), F(-1), F(0)))
COMBO = (F(2), F(-1, 3), F(7))


def model():
    return premise("singularity.bundle-maps-quantise-without-hopping")


def one_particle_function_linear(n):
    rows = []
    for f in FUNCS:
        for i in range(n):
            for j in range(n):
                row = [F(0)] * (n * n)
                row[i * n + j] = f[j] - f[i]          # ([a, M_f])_ij = a_ij (f_j - f_i)
                rows.append(row)
    return [[[v[i * n + j] for j in range(n)] for i in range(n)] for v in GA.field_kernel(rows)]


def is_diag(A):
    return all(A[i][j] == 0 for i in range(len(A)) for j in range(len(A)) if i != j)


def check_supplied_generators_commute_with_every_occupation():
    premise("singularity.function-linear-endomorphisms-are-bundle-maps")
    M = model()
    n, NOCC, comm, is_zero = M["NPTS"], M["NOCC"], M["comm"], M["is_zero"]
    ok = True
    ker = one_particle_function_linear(n)
    ok = ok and len(ker) == 3 and all(is_diag(a) for a in ker)
    combo = [[sum((COMBO[t] * ker[t][i][j] for t in range(3)), F(0)) for j in range(n)] for i in range(n)]
    gens = [M["dgamma"](a) for a in ker + [combo]]
    for subset in product((0, 1), repeat=n):
        P = M["eye"](M["DIM"])
        for j in range(n):
            if subset[j]:
                P = M["mm"](P, M["SIGMA"][j])
        gens.append(P)
    ok = ok and len(gens) == 12
    for G in gens:
        ok = ok and is_diag(G) and all(is_zero(comm(G, N)) for N in NOCC)
    GA.check("supplied class (dGamma of function-linear maps, parity products): diagonal, commutes with all N_x", ok)
    return ok


def check_pairing_generators_lie_outside_the_class():
    premise("singularity.bundle-maps-quantise-without-hopping")
    M = model()
    n, NOCC, comm, is_zero, mm, madd = M["NPTS"], M["NOCC"], M["comm"], M["is_zero"], M["mm"], M["madd"]
    PSI, PSID, bs = M["PSI"], M["PSID"], M["basis_state"]
    Gamma = mm(mm(M["SIGMA"][0], M["SIGMA"][1]), M["SIGMA"][2])
    Ntot = madd(madd(NOCC[0], NOCC[1]), NOCC[2])
    ok = True
    units = [[[F(1) if (r, c) == (i, j) else F(0) for c in range(n)] for r in range(n)]
             for i in range(n) for j in range(n)]
    ok = ok and len(units) == 9 and all(is_zero(comm(M["dgamma"](E), Ntot)) for E in units)
    for x in range(n):
        for y in range(x + 1, n):
            P = madd(mm(PSID[x], PSID[y]), mm(PSI[y], PSI[x]))
            ok = ok and is_zero(comm(P, Gamma))
            ok = ok and not is_diag(P)
            ok = ok and not is_zero(comm(P, NOCC[x])) and not is_zero(comm(P, NOCC[y]))
            ok = ok and not is_zero(comm(P, Ntot))
            occ = [0] * n
            occ2 = [0] * n
            occ2[x] = occ2[y] = 1
            col = [P[i][bs(occ)] for i in range(M["DIM"])]
            ok = ok and col[bs(occ2)] != 0 and sum(1 for c in col if c != 0) == 1
            # total occupation changes by exactly 2: [N_tot, P] = 2 (psi^dag psi^dag - psi psi)
            want = madd(mm(PSID[x], PSID[y]), mm(PSI[y], PSI[x]), -1)
            ok = ok and comm(Ntot, P) == [[2 * v for v in row] for row in want]
    GA.check("pairing generators commute with Gamma, are not diagonal, move N_x and N_tot by 2: not dGamma(a)", ok)
    return ok
