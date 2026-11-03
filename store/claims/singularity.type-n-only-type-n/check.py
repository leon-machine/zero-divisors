"""singularity.type-n-only-type-n: exact checks of the computable diagnosis.

Cl(1,3) in GA.py (e_t = gamma_0 squares +1, gamma_1..gamma_3 square -1); the PG field hb = 1 - beta P,
P(a) = (a.e_t) e_r, and the limit form ghat(a,b) = -(a.e_t)(b.e_t) of singularity.degeneration-exactly.
(1) Type C cannot occur: p - q = -2 = 6 mod 8 and 6 != 1 mod 4; the centre of Cl(1,3), computed
    blade-wise (exhaustive for a diagonal form), is span{1}, so there is no nontrivial central
    idempotent; Cl(1,3) = Mat_2(H): e = (1 + e_t e_r)/2 is idempotent, e A e has dimension 4 and contains
    I = e_2 e_3 e, J = e_2 e with I^2 = J^2 = -e, IJ = -JI, A e has dimension 8, and 1 = e + e_t e e_t
    lies in A e A (e is full).
(2) Type N is present at r = 0: the folded direction e_r is ghat-null and in the radical of ghat (no
    ghat-partner), while in Cl(1,3) the null vector e_t + e_r squares to 0 and is a two-sided zero
    divisor ((e_t + e_r)(e_t + e_r) = 0) with no inverse.
(3) Type P is present and demands nothing: e and 1 - e are idempotents with e(1 - e) = 0, and the
    identity assignment sigma(e) = e satisfies e sigma(e) e = e and sigma(e) e sigma(e) = sigma(e).
(4) Rule 1 keeps the clock: the floors Cl(1+k, 3+k), k <= 2, have centre span{1} (blade-wise), so no
    floor of the tower develops a type-C obstruction.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)


def span_rank(elems, m):
    blades = GA.all_blades(m)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in elems])


def centre(S):
    m = len(S)
    return [b for b in GA.all_blades(m) if all(GA.commutes({b: F(1)}, GA.gen(i), S) for i in range(m))]


def idem():
    return GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(GA.gen(0), GA.gen(1), S13)))


def check_no_type_c_and_quaternionic_matrix_form():
    premise("transport.existence-classification-type-c")
    assert (1 - 3) % 8 == 6 and ((1 - 3) % 8) % 4 != 1
    assert centre(S13) == [()]
    e = idem()
    assert GA.eq(GA.mul(e, e, S13), e) and not GA.eq(e, GA.sc(1))
    corner = [GA.mul(GA.mul(e, {b: F(1)}, S13), e, S13) for b in GA.all_blades(4)]
    assert span_rank(corner, 4) == 4
    I = GA.mul(GA.mul(GA.gen(2), GA.gen(3), S13), e, S13)
    J = GA.mul(GA.gen(2), e, S13)
    for X in (I, J):
        assert GA.eq(GA.mul(e, X, S13), X) and GA.eq(GA.mul(X, e, S13), X)
        assert GA.eq(GA.mul(X, X, S13), GA.neg(e))
    assert GA.eq(GA.mul(I, J, S13), GA.neg(GA.mul(J, I, S13)))
    left = [GA.mul({b: F(1)}, e, S13) for b in GA.all_blades(4)]
    assert span_rank(left, 4) == 8
    # 1 - e = e_t e e_t^{-1} (e_t anticommutes with e_t e_r), so 1 = e + e_t e e_t lies in A e A
    x = GA.gen(0)
    assert GA.eq(GA.mul(x, x, S13), GA.sc(1))
    assert GA.eq(GA.add(e, GA.mul(GA.mul(x, e, S13), x, S13)), GA.sc(1))
    return True


def check_type_n_at_the_singularity():
    premise("singularity.degeneration-exactly")
    premise("transport.existence-locus-type-n")
    et, er = GA.gen(0), GA.gen(1)
    frame = [GA.gen(i) for i in range(4)]
    ghat_row = [-(GA.dot(er, et, S13) * GA.dot(c, et, S13)) for c in frame]
    assert ghat_row == [0, 0, 0, 0]
    assert -(GA.dot(et, et, S13) ** 2) == -1
    n = GA.add(et, er)
    assert GA.is_zero(GA.mul(n, n, S13)) and not GA.is_zero(n)
    rows = [[GA.mul(n, {b: F(1)}, S13).get(bb, F(0)) for bb in GA.all_blades(4)] for b in GA.all_blades(4)]
    assert GA.rank_of_vectors(rows) == 8
    return True


def check_type_p_present_and_self_repairing():
    premise("transport.type-p-self-repairing")
    e = idem()
    f = GA.sub(GA.sc(1), e)
    assert GA.eq(GA.mul(f, f, S13), f)
    assert GA.is_zero(GA.mul(e, f, S13)) and not GA.is_zero(e) and not GA.is_zero(f)
    sig = e
    assert GA.eq(GA.mul(GA.mul(e, sig, S13), e, S13), e)
    assert GA.eq(GA.mul(GA.mul(sig, e, S13), sig, S13), sig)
    return True


def check_tower_floors_have_no_type_c():
    premise("tower.rigidity-clock-frozen")
    for k in range(3):
        S = tuple([1] * (1 + k) + [-1] * (3 + k))
        assert centre(S) == [()]
        assert ((1 + k) - (3 + k)) % 8 == 6
    return True
