"""dark-tower-matter.residue-seven-unit: exact checks in GA.py.

(i)   Along the residue-seven tower Cl(2,3), Cl(3,4), Cl(4,5), Cl(5,6) the pseudoscalar omega is
      central with omega^2 = -1, and along the residue-one tower Cl(3,2), Cl(4,3), Cl(5,4), Cl(6,5)
      central with omega^2 = +1 (computed blade products). The formula
      Q(omega) = (-1)^(n(n-1)/2) (-1)^q is checked against the computed square for every (p,q) with
      p + q <= 9, and a rung step (p,q) -> (p+1,q+1) keeps Q(omega) for every such (p,q).
(ii)  At r = 7 (Cl(2,3)) omega is odd: omega e_K is odd for every even blade e_K, so on the
      constituent ideal T = Cl^0 hf (hf a primitive idempotent of Cl^0(2,3), found by a search over
      commuting even blades of square +1) omega T lies in the odd part, Cl(2,3) hf = T + omega T
      with dim Cl hf = 2 dim T; the grade involution sends omega to -omega.
(iii) On Cl(2,3) hf, left multiplication by c + s omega commutes with every generator and sends
      X + omega Y to (cX - sY) + omega(sX + cY), checked for X, Y running over a basis of T at
      (c, s) = (1, 0), (0, 1) (the identity is linear in c, s, X, Y) and at (3/5, 4/5).
      Charges: (omega)^2 = -1 on the module, so omega is a complex structure (cells have charge +-1),
      and (c + s omega)^2 = (c^2 - s^2) + 2cs omega is the rotation by the double angle (a charge-2
      bilinear is not invariant: at (3/5, 4/5) the square is (-7/25, 24/25)). The assembly-level
      clause about T12's operations is not computable.
"""
from fractions import Fraction as F

import GA

R7 = [(2, 3), (3, 4), (4, 5), (5, 6)]
R1 = [(3, 2), (4, 3), (5, 4), (6, 5)]


def omega(n):
    return {tuple(range(n)): F(1)}


def central(x, S, n):
    return all(GA.commutes(x, GA.gen(a), S) for a in range(n))


def even_primitive(S, n):
    ev = [b for b in GA.all_blades(n) if len(b) % 2 == 0]

    def dim(f):
        return GA.rank_of_vectors([[GA.mul({K: F(1)}, f, S).get(b, F(0)) for b in ev] for K in ev])
    f, d, chosen = GA.sc(1), len(ev), []
    for b in ev:
        if not b or GA.mul({b: F(1)}, {b: F(1)}, S) != {(): F(1)}:
            continue
        if not all(GA.commutes({b: F(1)}, {c: F(1)}, S) for c in chosen):
            continue
        f2 = GA.mul(f, GA.add(GA.sc(F(1, 2)), {b: F(1, 2)}), S)
        d2 = dim(f2)
        if 0 < d2 < d:
            f, d, chosen = f2, d2, chosen + [b]
    T = []
    vecs = []
    for K in ev:
        x = GA.mul({K: F(1)}, f, S)
        v = [x.get(b, F(0)) for b in GA.all_blades(n)]
        if GA.rank_of_vectors(vecs + [v]) > len(vecs):
            vecs.append(v)
            T.append(x)
    return f, T


def check_pseudoscalar_along_towers():
    for (p, q) in R7:
        S = GA.sig(p, q)
        w = omega(p + q)
        assert GA.mul(w, w, S) == {(): F(-1)} and central(w, S, p + q)
    for (p, q) in R1:
        S = GA.sig(p, q)
        w = omega(p + q)
        assert GA.mul(w, w, S) == {(): F(1)} and central(w, S, p + q)
    # the formula, and its constancy along a rung step
    for n in range(1, 10):
        for p in range(n + 1):
            q = n - p
            comp = GA.mul(omega(n), omega(n), GA.sig(p, q))[()]
            assert comp == (-1) ** (n * (n - 1) // 2) * (-1) ** q
            step = GA.mul(omega(n + 2), omega(n + 2), GA.sig(p + 1, q + 1))[()]
            assert step == comp
            assert ((n + 2) * (n + 1) // 2 - n * (n - 1) // 2) % 2 == 1
    return True


def check_omega_odd_at_r7():
    S = GA.sig(2, 3)
    w = omega(5)
    for K in GA.all_blades(5):
        if len(K) % 2 == 0:
            assert all(len(b) % 2 == 1 for b in GA.mul(w, {K: F(1)}, S))
    assert GA.eq(GA.grade_inv(w), GA.scal(-1, w))
    f, T = even_primitive(S, 5)
    assert len(T) == 4                                       # dim T = 4 at the conformal level
    oT = [GA.mul(w, x, S) for x in T]
    assert all(len(b) % 2 == 1 for x in oT for b in x)
    blades = GA.all_blades(5)
    full = [GA.mul({K: F(1)}, f, S) for K in blades]
    rk = lambda xs: GA.rank_of_vectors([[x.get(b, F(0)) for b in blades] for x in xs])
    assert rk(full) == 8 and rk(T + oT) == 8
    return True


def check_rotation_by_c_plus_s_omega():
    S = GA.sig(2, 3)
    w = omega(5)
    f, T = even_primitive(S, 5)

    def rot(c, s):
        return GA.add(GA.sc(c), GA.scal(s, w))
    for (c, s) in ((F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5))):
        R = rot(c, s)
        assert central(R, S, 5)
        for X in T + [{}]:
            for Y in T + [{}]:
                lhs = GA.mul(R, GA.add(X, GA.mul(w, Y, S)), S)
                rhs = GA.add(GA.sub(GA.scal(c, X), GA.scal(s, Y)),
                             GA.mul(w, GA.add(GA.scal(s, X), GA.scal(c, Y)), S))
                assert GA.eq(lhs, rhs)
    # omega is a complex structure on the module: charge +-1
    for x in T:
        assert GA.eq(GA.mul(w, GA.mul(w, x, S), S), GA.scal(-1, x))
    # a charge-2 bilinear sees the double angle
    R = rot(F(3, 5), F(4, 5))
    assert GA.eq(GA.mul(R, R, S), rot(F(-7, 25), F(24, 25)))
    assert not GA.eq(GA.mul(R, R, S), GA.sc(1)) and not GA.eq(GA.mul(R, R, S), GA.sc(-1))
    return True
