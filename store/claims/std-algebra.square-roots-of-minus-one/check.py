from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


# square roots of -1 in Cl(1,3) (sig: e0^2 = 1, e1, e2, e3 square to -1)
ROOTS13 = [S.vec([0, 1, 0, 0]), S.vec([0, F(3, 5), F(4, 5), 0]), S.blade(1, 2), S.blade(0, 1, 2),
           S.pseudoscalar(4)]


def invertible(g, sq):
    return GA.rank_of_vectors(S.left_matrix(g, sq)) == 2 ** len(sq)


def conjugator(f, f2, sq):
    """An invertible g with g f = f2 g, from the solution space of that linear equation."""
    n = len(sq)
    blades = GA.all_blades(n)
    cols = [S.coords(GA.sub(GA.mul({b: F(1)}, f, sq), GA.mul(f2, {b: F(1)}, sq)), n) for b in blades]
    rows = [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]
    basis = [{b: c for b, c in zip(blades, v) if c != 0} for v in S.nullspace(rows)]
    for t in range(1, 6):
        g = {}
        for k, x in enumerate(basis):
            g = GA.add(g, GA.scal(F((t * (k + 1)) % 7 + 1), x))
        if g and invertible(g, sq):
            return g, len(basis)
    return None, len(basis)


def check_spacetime_roots_all_conjugate_to_I():
    premise("std-algebra.periodicity")
    sq = GA.sig(1, 3)
    I4 = S.pseudoscalar(4)
    ok = True
    dims = []
    for f in ROOTS13:
        ok = ok and GA.eq(GA.mul(f, f, sq), GA.sc(-1))
        g, d = conjugator(f, I4, sq)
        ok = ok and g is not None
        ok = ok and GA.eq(GA.mul(g, f, sq), GA.mul(I4, g, sq))
        dims.append(d)
    # the solution space of g f = I g is the centraliser's size: 8 for every root (M_2(H): dim 16 / 2)
    ok = ok and dims == [8, 8, 8, 8, 8]
    GA.check("in Cl(1,3) = M_2(H) every sampled square root of -1 is conjugate to I", ok)
    return ok


def check_three_classes_in_pauli_algebra():
    premise("std-algebra.complexification")
    sq = GA.sig(3, 0)
    om = S.pseudoscalar(3)
    om_inv = GA.neg(om)
    ok = GA.eq(GA.mul(om, om, sq), GA.sc(-1))
    roots = [om, GA.neg(om), S.blade(0, 1), S.blade(1, 2), GA.add(GA.scal(F(3, 5), S.blade(0, 1)), GA.scal(F(4, 5), S.blade(0, 2)))]
    inv = []
    for f in roots:
        ok = ok and GA.eq(GA.mul(f, f, sq), GA.sc(-1))
        inv.append(GA.mul(f, om_inv, sq).get((), F(0)))
    ok = ok and inv == [1, -1, 0, 0, 0]
    # the three blades of mixed type are conjugate to each other, not to +-omega
    for f in roots[3:]:
        g, _ = conjugator(roots[2], f, sq)
        ok = ok and g is not None
    g, _ = conjugator(roots[2], om, sq)
    ok = ok and g is None
    # Cl(2,0) = M_2(R): e1e2 and -e1e2 are conjugate (one class)
    sq2 = GA.sig(2, 0)
    g, _ = conjugator(S.blade(0, 1), GA.neg(S.blade(0, 1)), sq2)
    ok = ok and g is not None
    GA.check("Cl(3,0) = M_2(C): three classes of square roots of -1; Cl(2,0) = M_2(R): one", ok)
    return ok


def check_existence_by_signature():
    premise("std-algebra.periodicity")
    ok = True
    without = []
    for n in range(1, 5):
        for q in range(n + 1):
            p = n - q
            sq = GA.sig(p, q)
            has = any(GA.blade_mul(b, b, sq)[0] == -1 for b in GA.all_blades(n))
            if not has:
                without.append((p, q))
    ok = ok and without == [(1, 0)]
    # Cl(1,0): (a + b e)^2 = a^2 + b^2 + 2ab e is never -1 (its scalar part is a sum of squares)
    sq = GA.sig(1, 0)
    for a in range(-3, 4):
        for b in range(-3, 4):
            x = GA.add(GA.sc(a), GA.scal(b, GA.gen(0)))
            ok = ok and GA.mul(x, x, sq).get((), F(0)) >= 0
    GA.check("among nondegenerate Cl(p,q), 1 <= n <= 4, only Cl(1,0) has no square root of -1", ok)
    return ok
