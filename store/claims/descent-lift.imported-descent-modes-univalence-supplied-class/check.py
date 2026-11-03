"""descent-lift.imported-descent-modes-univalence-supplied-class: exact checks of the finite content.

(1) One mode: (1/2)(x + G x G), G = (-1)^N, kills the off-diagonal matrix units and fixes the diagonal
    ones. On nu = 2, 3 modes the mode-wise averages commute and their composite is the pinching onto the
    joint-number-diagonal algebra (all matrix units).
(2) Univalence: the even subalgebra, the commutant of the total parity, has dimension 2^(2 nu - 1)
    (2, 8, 32 for nu = 1, 2, 3); an even state vanishes on the odd sector (sample density matrix).
(3) The supplied class: the 2^nu parity monomials are joint-number-diagonal, commute with every N_k, and
    span the whole diagonal algebra (rank 2^nu); a pairing generator lies outside (it moves the numbers).
(4) On nu = 2, 3, 4 modes the hops and pair annihilations annihilate the vacuum (so stabilise its ray)
    and the pair creations a_i^dag a_j^dag |0> span a space of dimension nu(nu - 1)/2 = 1, 3, 6 off the
    ray: the tangent of the orbit.
(5) The pairing rotor (1 - P) + (3/5) P + (4/5) X, X = a0^dag a1^dag - a1 a0, P = -X^2, is orthogonal and
    even and sends |00> to (3/5)|00> + (4/5)|11>.
(6) The thermofield pair c|00> + s|11> has both one-mode marginals diag(c^2, s^2), the Gibbs state
    diag(1, q)/(1 + q) with q = (s/c)^2; at q = e^(-omega/T) = 9/16 this forces (c^2, s^2) = (16/25, 9/25),
    so (c, s) = (4/5, 3/5).
Not computable: the univalence rule and the exclusion of pairing terms as premises, and the citations.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

# ---- exact fermionic Fock toolkit: lib/fock.py in MSB order. Basis of m modes: occupation
# tuples; index = sum n_k 2^(m-1-k), so mode 0 is the most significant bit and |sys> (x) |rec>
# is the index sys * 2^k + rec when the system modes come first. ----
MSB = fock.MSB
dag = fock.dag
mm = fock.mm
madd = fock.madd
msc = fock.msc
eye = fock.eye
apply = fock.apply
vadd = fock.vadd
vsc = fock.vsc
outer = fock.outer
trace = fock.trace


def occ(i, m):
    return fock.occ(i, m, MSB)


def ann(k, m):
    return fock.ann(k, m, MSB)


def num(k, m):
    return fock.num(k, m, MSB)


def par(k, m):
    """Parity of mode k, (-1)^(N_k) = 1 - 2 N_k."""
    return fock.mode_parity(k, m, MSB)


def ket(t):
    return fock.ket(t, MSB)


def is_even_op(M, m):
    return fock.is_even_op(M, m)
# ---- end of toolkit ----


# Mode counts on which the supplied class is checked (sample sizes; nu = 3 has a spectator mode).
NU_CLASS = (2, 3)
# The two modes the sample pairing generator a_i^dag a_j^dag + a_j a_i acts on.
PAIR = (0, 1)


def avg(k, m, rho):
    G = par(k, m)
    return msc(F(1, 2), madd(rho, mm(G, rho, G)))


def check_descent_is_parity_average_and_pinching():
    premise("singularity.descent-parity-average")
    premise("singularity.p-reduced-metric-level-reading-many")
    ok = True
    for i in range(2):
        for j in range(2):
            u = {(i, j): F(1)}
            ok = ok and avg(0, 1, u) == (u if i == j else {})
    for nu in (2, 3):
        d = 2 ** nu
        for i in range(d):
            for j in range(d):
                u = {(i, j): F(1)}
                x = u
                for k in range(nu):
                    x = avg(k, nu, x)
                y = u
                for k in reversed(range(nu)):
                    y = avg(k, nu, y)
                ok = ok and x == y and x == (u if i == j else {})
    GA.check("one-mode parity average; on 2, 3 modes the averages commute and compose to the pinching", ok)
    return ok


def check_even_subalgebra():
    premise("singularity.imported-univalence-superselection-rule")
    ok = True
    dims = []
    for nu in (1, 2, 3):
        d = 2 ** nu
        Gt = eye(d)
        for k in range(nu):
            Gt = mm(Gt, par(k, nu))
        dims.append(sum(1 for i in range(d) for j in range(d) if Gt[(i, i)] == Gt[(j, j)]))
    ok = ok and dims == [2, 8, 32]
    c, s = F(4, 5), F(3, 5)
    psi = vadd(vsc(c, ket((0, 0))), vsc(s, ket((1, 1))))
    rho = outer(psi, psi)
    odd_units = [(i, j) for i in range(4) for j in range(4) if (sum(occ(i, 2)) + sum(occ(j, 2))) % 2 == 1]
    ok = ok and len(odd_units) == 8 and all(trace(mm(rho, {(j, i): F(1)})) == 0 for (i, j) in odd_units)
    GA.check("even subalgebra of dimension 2^(2nu-1); an even state vanishes on the odd sector", ok)
    return ok


def check_supplied_class_is_joint_number_diagonal():
    premise("singularity.class-relative-no-go-no-supplied")
    ok = True
    for nu in NU_CLASS:
        d = 2 ** nu
        mons = []
        for i in range(d):
            G = eye(d)
            for k, b in enumerate(occ(i, nu)):
                if b:
                    G = mm(G, par(k, nu))
            mons.append(G)
        ok = ok and all(all(a == b for (a, b) in G) for G in mons)
        ok = ok and all(mm(G, num(k, nu)) == mm(num(k, nu), G) for G in mons for k in range(nu))
        ok = ok and GA.field_rank([[G[(r, r)] for r in range(d)] for G in mons]) == d
        a = [ann(k, nu) for k in range(nu)]
        i, j = PAIR
        create, annihilate = mm(dag(a[i]), dag(a[j])), mm(a[j], a[i])
        pairing = madd(create, annihilate)
        # [N_k, a_i^dag a_j^dag] = a_i^dag a_j^dag and [N_k, a_j a_i] = -a_j a_i for k in {i, j}:
        # the pairing moves exactly the two numbers it touches and commutes with every other N_k.
        moved = madd(create, msc(-1, annihilate))
        ok = ok and moved != {}
        ok = ok and all(fock.comm(num(k, nu), pairing) == (moved if k in PAIR else {}) for k in range(nu))
    GA.check("parity monomials span the joint-number-diagonal algebra; pairing is outside", ok)
    return ok


def check_vacuum_stabilisers_and_tangent():
    premise("singularity.l-stabiliser-tangent")
    ok = True
    dims = []
    for nu in (2, 3, 4):
        a = [ann(k, nu) for k in range(nu)]
        vac = ket((0,) * nu)
        hops = [mm(dag(a[i]), a[j]) for i in range(nu) for j in range(nu) if i != j]
        anns = [mm(a[i], a[j]) for i in range(nu) for j in range(i + 1, nu)]
        ok = ok and all(apply(h, vac) == {} for h in hops + anns)
        crs = [apply(mm(dag(a[i]), dag(a[j])), vac) for i in range(nu) for j in range(i + 1, nu)]
        rows = [[v.get(k, F(0)) for k in range(2 ** nu)] for v in crs]
        ok = ok and all(0 not in v for v in crs)
        dims.append(GA.field_rank(rows))
    ok = ok and dims == [1, 3, 6]
    GA.check("hops and pair annihilations kill the vacuum; pair creations span dimension 1, 3, 6", ok)
    return ok


def check_pairing_rotation_witness():
    premise("singularity.envelope-endpoint-why-boundary-mode-locality")
    ok = True
    a = [ann(k, 2) for k in range(2)]
    X = madd(mm(dag(a[0]), dag(a[1])), msc(-1, mm(a[1], a[0])))
    P = msc(-1, mm(X, X))
    ok = ok and mm(P, P) == P and mm(X, P) == X
    R = madd(eye(4), msc(-1, P), msc(F(3, 5), P), msc(F(4, 5), X))
    ok = ok and mm(dag(R), R) == eye(4) and is_even_op(R, 2)
    ok = ok and apply(R, ket((0, 0))) == {0: F(3, 5), 3: F(4, 5)}
    GA.check("pairing rotor: |00> -> (3/5)|00> + (4/5)|11>, orthogonal and even", ok)
    return ok


def check_thermofield_marginals_gibbs():
    premise("singularity.purity-output-partner-commutant")
    premise("singularity.schmidt-forcing-proved-outright")
    ok = True
    for c, s in ((F(4, 5), F(3, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17))):
        psi = vadd(vsc(c, ket((0, 0))), vsc(s, ket((1, 1))))
        rho = outer(psi, psi)
        for keep in (0, 1):
            red = {}
            for (i, j), v in rho.items():
                ti, tj = occ(i, 2), occ(j, 2)
                if ti[1 - keep] == tj[1 - keep]:
                    key = (ti[keep], tj[keep])
                    red[key] = red.get(key, F(0)) + v
            q = (s / c) ** 2
            gibbs = {(0, 0): F(1) / (1 + q), (1, 1): q / (1 + q)}
            ok = ok and red == gibbs
    q = F(9, 16)
    c2 = F(1) / (1 + q)
    ok = ok and (c2, 1 - c2) == (F(16, 25), F(9, 25))
    ok = ok and F(4, 5) ** 2 == c2 and F(3, 5) ** 2 == 1 - c2
    GA.check("thermofield marginals are Gibbs; e^(-omega/T) = 9/16 gives (c, s) = (4/5, 3/5)", ok)
    return ok
