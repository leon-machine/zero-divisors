"""synthesis.majorana-element-is-null-blade-no-frozen-point-condition: exact checks.

The five-mode module as 32 x 32 rational matrices (lib fock, LSB order): creation v_m, annihilation w_m,
real-form Majoranas gamma_{2m} = v_m + w_m (square +1), gamma_{2m+1} = w_m - v_m (square -1), the real
Clifford algebra Cl(5,5) of the ten in its irreducible representation, scalar part <A>_0 = tr(A)/32.
T = v_0 v_1 v_2 v_3 v_4 is the Majorana element of the stored proposition. Checks:
  (1) T is a null blade: T^2 = 0, so the Clifford norm Q(T) = <T T~>_0 vanishes (reversion is the
      identity on grade five); the Fock norm <T T^dag>_0 is 1/32; [B - L, T] = -2 T (the weight that
      kills every holomorphic invariant on T);
  (2) the pseudoscalar I of the ten squares to +1, anticommutes with every generator, has T in its +1
      eigenspace on grade five, which is 126-dimensional; left multiplication by I is an anti-isometry
      of the form <A B>_0 on grade five, so the form vanishes on each eigenspace and pairs them;
  (3) rotors 1 + X with X nilpotent in the 21 move T inside the +1 eigenspace with Q(gTg^-1) = 0 and
      Q(gTg^-1, T) = 0; T^dag lies in the -1 eigenspace; the Fock adjoint fixes gamma_{2m} and negates
      gamma_{2m+1}, so it is not a Clifford anti-automorphism of the ten but depends on the split
      into the two fives (the Hermitian structure of the module).
"""
from fractions import Fraction as F
import itertools
import GA
import fock
from tp_premise import premise

NM = 5
DIM = 32
mm, madd, msc, msub, comm, meq = fock.mm, fock.madd, fock.msc, fock.msub, fock.comm, fock.meq
ONE = fock.eye(DIM)
V = [fock.cre(m, NM) for m in range(NM)]
W = [fock.ann(m, NM) for m in range(NM)]
G = [fock.majorana(p, NM) for p in range(2 * NM)]


def scalar_part(A):
    return fock.trace(A) / DIM


def Q(A, B=None):
    """The Clifford bilinear form <A B>_0 restricted to grade five, where reversion is the identity."""
    return scalar_part(mm(A, B if B is not None else A))


def T_el():
    return mm(V[0], V[1], V[2], V[3], V[4])


def pseudoscalar():
    return mm(*G)


def grade5_basis():
    return [mm(*[G[p] for p in c]) for c in itertools.combinations(range(2 * NM), 5)]


def BL():
    return fock.diag(lambda s: 1 - F(2, 3) * sum(1 for m in (0, 1, 2) if s >> m & 1), DIM)


def check_majorana_element_is_a_null_blade():
    premise("standard-model.majorana-element")
    T = T_el()
    for p in range(10):
        sq = mm(G[p], G[p])
        GA.check("gamma squares", sq == (ONE if p % 2 == 0 else msc(-1, ONE)))
    GA.check("T^2 = 0: a zero divisor", not mm(T, T))
    GA.check("Clifford norm of T vanishes", Q(T) == 0)
    # reversion is the identity on grade five: gamma_{p5}...gamma_{p1} = + gamma_{p1}...gamma_{p5}
    for c in ((0, 1, 2, 3, 4), (1, 3, 5, 7, 9), (0, 2, 4, 6, 8), (0, 3, 5, 6, 9)):
        fwd = mm(*[G[p] for p in c])
        rev = mm(*[G[p] for p in reversed(c)])
        GA.check("reversion trivial on a five-blade", meq(fwd, rev))
    GA.check("a non-null five-blade has Clifford norm 1", Q(mm(G[0], G[2], G[4], G[6], G[8])) == 1)
    Td = fock.dag(T)
    GA.check("Fock norm <T T^dag>_0 = 1/32", scalar_part(mm(T, Td)) == F(1, 32))
    GA.check("T T^dag is the projector on the full state", mm(T, Td) == {(31, 31): F(1)})
    GA.check("[B - L, T] = -2 T", meq(comm(BL(), T), msc(-2, T)))
    return True


def check_clifford_norm_vanishes_on_the_self_dual_half():
    premise("standard-model.majorana-element")
    premise("mass.imported-frozen-point-tractor-connection")
    I10 = pseudoscalar()
    GA.check("I^2 = +1 in Cl(5,5)", meq(mm(I10, I10), ONE))
    for p in range(10):
        GA.check("I anticommutes with every generator", not madd(mm(I10, G[p]), mm(G[p], I10)))
    T = T_el()
    GA.check("T is in the +1 eigenspace of I", meq(mm(I10, T), T))
    basis = grade5_basis()
    GA.check("252 five-blades", len(basis) == 252)
    plus = []
    keys = {}
    for A in basis:
        Ap = madd(A, mm(I10, A))
        plus.append(Ap)
        for k in Ap:
            keys.setdefault(k, len(keys))
    dense = []
    for Ap in plus:
        row = [F(0)] * len(keys)
        for k, x in Ap.items():
            row[keys[k]] = x
        dense.append(row)
    GA.check("the +1 eigenspace on grade five is 126-dimensional", GA.mat_rank(dense) == 126)
    # anti-isometry and vanishing on each half, on three sampled elements with nonzero norm
    samples = [
        madd(msc(F(2), basis[0]), msc(F(-1), basis[17]), msc(F(3), basis[100]), basis[251]),
        madd(basis[5], msc(F(1, 2), basis[77]), msc(F(-2), basis[150])),
        madd(msc(F(3), basis[1]), msc(F(5), basis[200]), msc(F(-1), basis[33]), msc(F(7), basis[128])),
    ]
    GA.check("pinned Clifford norms of the samples", [Q(A) for A in samples] == [F(13), F(11, 4), F(-34)])
    count = 0
    for p in range(10):
        count += 1 if not madd(mm(I10, G[p]), mm(G[p], I10)) else 0
    GA.check("ten generators anticommute with I", count == 10)
    for A in samples:
        GA.check("sample has nonzero Clifford norm", Q(A) != 0)
        Ap = msc(F(1, 2), madd(A, mm(I10, A)))
        Am = msc(F(1, 2), msub(A, mm(I10, A)))
        GA.check("I is an anti-isometry", Q(mm(I10, A), mm(I10, A)) == -Q(A))
        GA.check("norm vanishes on the +1 half", Q(Ap) == 0)
        GA.check("norm vanishes on the -1 half", Q(Am) == 0)
        GA.check("the halves are paired: <A+, A-> = Q(A)/2", Q(Ap, Am) == Q(A) / 2)
    return True


def check_orbit_norm_and_the_adjoint():
    premise("standard-model.majorana-element")
    premise("synthesis.majorana-scale-free-on-pati-salam-route")
    I10 = pseudoscalar()
    T = T_el()
    moved = 0
    nil = [mm(W[4], W[3]), mm(V[0], V[1]), mm(V[3], W[4]), mm(W[0], W[2])]
    rotors = [(madd(ONE, X), msub(ONE, X)) for X in nil]
    rotors.append((mm(rotors[0][0], rotors[3][0]), mm(rotors[3][1], rotors[0][1])))   # a composite rotor
    for X in nil:
        GA.check("X nilpotent", not mm(X, X))
    for g, gi in rotors:
        GA.check("g g^-1 = 1", meq(mm(g, gi), ONE))
        Tg = mm(g, T, gi)
        if not meq(Tg, T):
            moved += 1
        GA.check("orbit element stays self-dual", meq(mm(I10, Tg), Tg))
        GA.check("Q(g T g^-1) = 0", Q(Tg) == 0)
        GA.check("Q(g T g^-1, T) = 0", Q(Tg, T) == 0)
    GA.check("three of the five rotors move T", moved == 3)
    Td = fock.dag(T)
    GA.check("T^dag is in the -1 eigenspace", meq(mm(I10, Td), msc(-1, Td)))
    GA.check("Q(T, T^dag) = 1/32: the pairing of the halves is the Fock norm", Q(T, Td) == F(1, 32))
    for m in range(NM):
        GA.check("the adjoint fixes gamma_{2m}", meq(fock.dag(G[2 * m]), G[2 * m]))
        GA.check("the adjoint negates gamma_{2m+1}", meq(fock.dag(G[2 * m + 1]), msc(-1, G[2 * m + 1])))
    return True


EXPORTS = {}
