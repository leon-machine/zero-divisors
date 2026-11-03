"""synthesis.tower-top-pair-forgets-reversal: exact checks on truncations of the tower.

Layout: ground generators 0..n-1; plane j (j >= 1) has e_j = n + 2(j-1) (square +1) and
f_j = n + 2(j-1) + 1 (square -1). Phi: x_i -> y_i e_1, e_1 -> e_1, e_j -> e_1 f_{j-1} (j >= 2),
f_j -> e_1 e_{j+1}; the target ground squares are the negatives of the source ones.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, scal, sc, gen, eq, grade_inv
from tp_premise import premise


def floor_squares(ground, k):
    return tuple(ground) + (1, -1) * k


def e_idx(n, j):
    return n + 2 * (j - 1)


def f_idx(n, j):
    return n + 2 * (j - 1) + 1


def phi_gen(n, g, sq):
    e1 = gen(e_idx(n, 1))
    if g < n:
        return mul(gen(g), e1, sq)
    j = (g - n) // 2 + 1
    if (g - n) % 2 == 0:
        return e1 if j == 1 else mul(e1, gen(f_idx(n, j - 1)), sq)
    return mul(e1, gen(e_idx(n, j + 1)), sq)


def phi(x, n, sq):
    out = {}
    for b, c in x.items():
        y = sc(c)
        for g in b:
            y = mul(y, phi_gen(n, g, sq), sq)
        out = add(out, y)
    return out


def star(x, sq):
    """frame *-structure: each generator unitary, g* = g^{-1} = Q(g) g; anti-multiplicative"""
    out = {}
    for b, c in x.items():
        y = sc(c)
        for g in reversed(b):
            y = mul(y, scal(sq[g], gen(g)), sq)
        out = add(out, y)
    return out


def reversal_ok(ground, K):
    n = len(ground)
    src = floor_squares(ground, K + 2)
    tgt = floor_squares([-c for c in ground], K + 2)
    gens = list(range(n + 2 * K))
    img = {g: phi_gen(n, g, tgt) for g in gens}
    for a in gens:
        assert eq(mul(img[a], img[a], tgt), sc(src[a]))                     # squares preserved
        for b in gens:
            if a < b:
                assert add(mul(img[a], img[b], tgt), mul(img[b], img[a], tgt)) == {}   # anticommute
        for blade in img[a]:
            assert max(blade) < n + 2 * (K + 1)                                # T_K -> T'_{K+1}
            if a >= n:
                assert min(blade) >= n                                         # B_K -> B'_{K+1}
        assert eq(phi(img[a], n, src), gen(a))                                 # Psi Phi = id
        pre = phi_gen(n, a, src)
        assert eq(phi(pre, n, tgt), gen(a))                                    # Phi Psi = id
        want = scal(-1, gen(a)) if a == e_idx(n, 1) else gen(a)
        assert eq(phi(grade_inv(pre), n, tgt), want)                           # Phi alpha Phi^-1 = theta'
    for a in gens:                                                             # images unitary for the frame *
        assert eq(mul(star(img[a], tgt), img[a], tgt), sc(1))
    assert phi_gen(n, f_idx(n, K), tgt) == mul(gen(e_idx(n, 1)), gen(e_idx(n, K + 1)), tgt)  # leaves T'_K
    for i in range(n):
        for j in range(i + 1, n):
            assert eq(phi(mul(gen(i), gen(j), src), n, tgt), scal(-1, mul(gen(i), gen(j), tgt)))
    return True


def check_reversal_isomorphism_of_pairs():
    premise("synthesis.plane-commutant-even-ground")
    premise("tower.structure-tower-c-norms")
    premise("tower.car-limit-even-charge")
    premise("transport.classification-real-clifford-algebras")
    grounds = [(1,), (-1,), (1, 1), (1, -1), (1, 1, -1), (1, -1, -1), (1, 1, 1, -1), (1, -1, -1, -1),
               (1, 1, 1, 1), (1, 1, -1, -1, -1), (1, 1, 1, 1, -1)]
    for ground in grounds:
        for K in (1, 2):
            if len(ground) + 2 * (K + 2) <= 13:
                assert reversal_ok(ground, K)
    GA.check("x_i -> y_i e_1 with the planes re-paired is an isomorphism of tower-top pairs (p,q) -> (q,p) "
             "on every tested truncation, with inverse given by the same formula", True)
    # the supercommutant of the planes is the whole ground algebra: blade test on T_2 over (1,3) and (3,1)
    for ground in [(1, -1, -1, -1), (1, 1, 1, -1), (1, 1, -1)]:
        n = len(ground)
        sq = floor_squares(ground, 2)
        planes = list(range(n, n + 4))
        sup = []
        for B in GA.all_blades(len(sq)):
            x = {B: F(1)}
            ok = all(eq(mul(gen(g), x, sq), mul(grade_inv(x), gen(g), sq)) for g in planes)
            if ok:
                sup.append(B)
        assert sorted(sup) == sorted(GA.all_blades(n))
    GA.check("the graded supercommutant of the planes is the whole ground algebra Cl(p,q)", True)
def check_shift_and_rule2():
    premise("synthesis.plane-commutant-even-ground")
    premise("rule2.imported-rule-2-matrix-units-forgotten")
    # shift (p,q) -> (p-4,q+4): z_i = x_i omega_4 on four positive generators; planes fixed
    for ground in [(1, 1, 1, 1), (1, 1, 1, 1, -1), (1, 1, 1, 1, 1)]:
        n = len(ground)
        sq = floor_squares(ground, 2)
        w4 = mul(mul(gen(0), gen(1), sq), mul(gen(2), gen(3), sq), sq)
        assert eq(mul(w4, w4, sq), sc(1))
        new = [mul(gen(i), w4, sq) for i in range(4)] + [gen(i) for i in range(4, len(sq))]
        want = [-1, -1, -1, -1] + list(sq[4:])
        for a in range(len(new)):
            assert eq(mul(new[a], new[a], sq), sc(want[a]))
            for b in range(a + 1, len(new)):
                assert add(mul(new[a], new[b], sq), mul(new[b], new[a], sq)) == {}
        prod = mul(mul(new[0], new[1], sq), mul(new[2], new[3], sq), sq)
        assert eq(prod, w4)                                                     # z1 z2 z3 z4 = omega_4
    GA.check("the four-generator shift presents L_{p,q} as L_{p-4,q+4} fixing every plane generator", True)
    # Rule 2: for p - q = 1 mod 4 the repairs' even algebras have centres C and R + R
    for (p, q) in [(1, 0), (0, 3), (3, 2), (1, 4), (2, 1)]:
        if (p - q) % 4 != 1:
            continue
        cents = []
        for (pp, qq) in [(p + 1, q), (p, q + 1)]:
            sq = tuple([1] * pp + [-1] * qq)
            m = pp + qq
            om = {tuple(range(m)): F(1)}
            cents.append(mul(om, om, sq))
        assert cents == [sc(-1), sc(1)]
    GA.check("the two Rule 2 repairs give planes' commutants with centres C (nu^2 = +1) and R + R (nu^2 = -1)",
             True)
