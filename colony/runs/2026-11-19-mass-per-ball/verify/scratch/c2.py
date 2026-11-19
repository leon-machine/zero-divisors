"""dark-matter.contact-mechanism-returns-r3: exact checks.

Numbers of Q(pi) are Laurent polynomials in pi, {k: c} for sum c pi^k (pi transcendental, so
polynomial equality is equality of reals); decimals use rational bounds on pi. Unit-ball volumes
come from the recursion V_0 = 1, V_1 = 2, V_D = (2 pi / D) V_(D-2). The clauses C, I, S and O are
postulated; what is checked is the arithmetic and geometry the proposition derives from them.
Premise E gives the mass densities mu/(V_D d^D); the unit of length in (i) to (iii) is d, and the
last check puts d back and finds it cancels. No quantum's mass or number is used.

(i)   C: the ball of radius d (here 1) about a mass element at height h above the hyperplane
      x_4 = 0 meets it exactly when h^2 <= 1 (the squared distance from the centre to the
      hyperplane, computed as the minimum of |c - x|^2 over the hyperplane, is h^2); with mass
      density mu/V_4 (E) and one side (S), the mass per unit three-volume is int_0^1 mu dh / V_4 =
      mu/V_4, and f_5D = (mu/V_4)/(mu/V_3) = V_3/V_4 = 8/(3 pi) (mu cancels). Two-sided contact
      gives twice that, so S is the factor one half.
      Which side is immaterial: in Cl(1,4) the components (1 +- omega)/2 are central orthogonal
      idempotents on which e_4 acts as +-P^-1 (the sign names a side), and two components at half
      density, each sourcing its own side, give the one-component count 1/V_4.
(ii)  Downward count on the plane x_3 = 0: rho_us/rho_3D = (1/V_3)/(1/V_2) = V_2/V_3 = 3/4; sheets
      s apart give V_3/(s V_2) read on our space, and O (equality with V_3/V_2) solves to s = 1, so
      f_3D = V_3/V_2 = 4/3. A sheet holding both modules would be sourced at 2/V_3.
(iii) The total 1 + 2 f_3D + 2 f_5D is the unit-ball rule's (11 pi + 16)/(3 pi), 5.36432 to five
      places; the unit d_b cancels from every ratio (checked at two lengths); without S the total is
      T(2) = 5.729 (three places), more than 5.5 sigma high; cubic cells give 5; the side
      V_3^(1/3) of a cube of the ball's volume lies in (1.61, 1.62).
(iv)  Read on a quantum's own cell with R2 dropped: a five-dimensional tower that keeps E with
      quanta k times heavier and rarer has own cell radius a with a^4 = k d^4; at k = 16, a = 2d,
      the slab has width 2d and the share is 2 V_3/V_4 = 16/(3 pi), not 8/(3 pi); the total with
      both five-dimensional towers so filled is 11/3 + 32/(3 pi), about 7.06.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

PI_LO, PI_HI = F(314159265358, 10 ** 11), F(314159265359, 10 ** 11)
OBS = F(1200, 10000) / F(2237, 100000)
SIG = F(65, 1000)
HEIGHTS = [F(0), F(1, 3), F(-3, 4), F(1), F(-1), F(7, 6), F(-5, 2), F(2)]
FOOT_SAMPLES = [[F(0), F(0), F(0)], [F(1, 2), F(-1, 3), F(2)], [F(-3), F(1), F(1, 5)]]
UNITS = [F(1), F(49, 50)]                       # two choices of the common length d
MASS = F(938, 7)


def lp(c, k=0):
    return {k: F(c)} if c != 0 else {}


def ladd(*xs):
    out = {}
    for x in xs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def lmul(*xs):
    out = {0: F(1)}
    for b in xs:
        new = {}
        for k1, c1 in out.items():
            for k2, c2 in b.items():
                new[k1 + k2] = new.get(k1 + k2, F(0)) + c1 * c2
        out = {k: c for k, c in new.items() if c != 0}
    return out


def linv(a):
    assert len(a) == 1
    (k, c), = a.items()
    return {-k: 1 / c}


def bounds(x):
    lo = hi = F(0)
    for k, c in x.items():
        u, v = c * PI_LO ** k, c * PI_HI ** k
        lo += min(u, v)
        hi += max(u, v)
    return lo, hi


def ball(D):
    V = {0: lp(1), 1: lp(2)}
    for n in range(2, D + 1):
        V[n] = lmul(lp(F(2, n), 1), V[n - 2])
    return V[D]


def prod(gens, sq):
    x = GA.sc(1)
    for i in gens:
        x = GA.mul(x, GA.gen(i), sq)
    return x


def check_five_dimensional_count():
    premise("dark-matter.nesting")
    premise("dark-matter.e-equal-mass-per-unit-ball")
    met = 0
    for h in HEIGHTS:
        # squared distance from (0,0,0,h) to points (x,0) of the hyperplane; minimum at the foot x = 0
        dists = [sum(y * y for y in x) + h * h for x in FOOT_SAMPLES]
        assert min(dists) == h * h
        if h * h <= 1:
            met += 1
    assert met == 5
    # one-sided slab: the antiderivative of the constant density 1/V_4 is h/V_4, from 0 to 1
    def anti(h):
        return lmul(lp(h), linv(ball(4)))
    one_side = ladd(anti(1), lmul(lp(-1), anti(0)))
    two_side = ladd(anti(1), lmul(lp(-1), anti(-1)))
    f5 = lmul(lp(MASS), one_side, linv(lmul(lp(MASS), linv(ball(3)))))
    assert f5 == {-1: F(8, 3)}
    assert lmul(two_side, linv(one_side)) == {0: F(2)}
    return True


def check_side_is_immaterial():
    premise("dark-matter.direction-nesting-adds-algebra")
    premise("dark-matter.e-equal-mass-per-unit-ball")
    sq = GA.sig(1, 4)
    P, w = prod([0, 1, 2, 3], sq), prod([0, 1, 2, 3, 4], sq)
    Pinv = GA.scal(-1, P)                                   # P^2 = -1
    assert GA.eq(GA.mul(P, P, sq), GA.sc(-1))
    ep = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
    em = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
    assert GA.eq(GA.mul(ep, em, sq), {}) and GA.eq(GA.add(ep, em), GA.sc(1))
    assert all(GA.commutes(ep, GA.gen(i), sq) for i in range(5))
    assert GA.eq(GA.mul(GA.gen(4), ep, sq), GA.mul(Pinv, ep, sq))
    assert GA.eq(GA.mul(GA.gen(4), em, sq), GA.scal(-1, GA.mul(Pinv, em, sq)))
    half = lmul(lp(F(1, 2)), linv(ball(4)))
    assert ladd(half, half) == lmul(lp(1), linv(ball(4)))
    return True


def check_three_dimensional_sheets():
    premise("dark-matter.nesting")
    premise("dark-matter.e-equal-mass-per-unit-ball")
    premise("dark-matter.projection-every-towers-content-dilutes-ones")
    down = lmul(linv(ball(3)), linv(linv(ball(2))))          # (1/V_3)/(1/V_2)
    assert down == {0: F(3, 4)}
    inv_down = linv(down)
    # O: V_3/(s V_2) = 1/down; solve for s
    s = lmul(ball(3), linv(ball(2)), linv(inv_down))
    assert s == {0: F(1)}
    f3 = lmul(lp(MASS), linv(lmul(ball(2), s)), linv(lmul(lp(MASS), linv(ball(3)))))
    assert f3 == {0: F(4, 3)}
    both = ladd(linv(ball(3)), linv(ball(3)))
    assert lmul(both, ball(3)) == {0: F(2)}
    return True


def check_total_and_alternatives():
    premise("dark-matter.e-equal-mass-per-unit-ball")
    f3 = lmul(ball(3), linv(ball(2)))
    f5 = lmul(ball(3), linv(ball(4)))
    total = ladd(lp(1), lmul(lp(2), f3), lmul(lp(2), f5))
    assert total == {0: F(11, 3), -1: F(16, 3)}
    lo, hi = bounds(total)
    assert round(lo * 10 ** 5) == round(hi * 10 ** 5) == 536432
    for d in UNITS:
        # densities m/(V_D d^D), thickness one radius d, sheets d apart: d cancels
        r5 = lmul(lp(MASS / d ** 4), linv(ball(4)), lp(d))
        r3 = lmul(lp(MASS / d ** 2), linv(ball(2)), lp(1 / d))
        ru = lmul(lp(MASS / d ** 3), linv(ball(3)))
        assert lmul(r5, linv(ru)) == {-1: F(8, 3)} and lmul(r3, linv(ru)) == {0: F(4, 3)}
    both = ladd(lp(1), lmul(lp(2), f3, lp(F(1, 2))), lmul(lp(2), f5, lp(2)))
    assert both == {0: F(7, 3), -1: F(32, 3)}
    lo, hi = bounds(both)
    assert round(lo * 1000) == round(hi * 1000) == 5729
    assert (lo - OBS) / SIG > F(11, 2)
    cube = [F(1) ** 3 / F(1) ** D for D in (3, 2, 2, 4, 4)]   # unit-cube cells, shares 1^3/1^D
    assert sum(cube) == 5
    lo, hi = bounds(ball(3))
    assert F(161, 100) ** 3 < lo and hi < F(162, 100) ** 3
    return True


def check_own_cell_reading_differs():
    premise("dark-matter.e-equal-mass-per-unit-ball")
    d = F(49, 50)
    f5 = lmul(ball(3), linv(ball(4)))
    ru = lmul(lp(MASS / d ** 3), linv(ball(3)))                 # ours, by E
    for k, root in [(F(16), F(2)), (F(81), F(3)), (F(1), F(1))]:
        assert root ** 4 == k
        # the tower keeps E: quanta of mass k MASS, one per k balls of radius d
        number = lmul(lp(1 / (k * d ** 4)), linv(ball(4)))
        rho4 = lmul(lp(k * MASS), number)
        assert lmul(rho4, ball(4), lp(d ** 4)) == {0: MASS}
        a = root * d                                            # own cell radius: one quantum per ball of radius a
        assert lmul(number, ball(4), lp(a ** 4)) == {0: F(1)}
        on_common = lmul(rho4, lp(d), linv(ru))                 # contact read on E's ball
        on_own = lmul(rho4, lp(d), linv(ru))                    # contact read on the quantum's own cell
        assert on_common == f5
        assert on_own == lmul(f5, lp(root))
        assert (on_own == on_common) == (k == 1)
    total = ladd(lp(1), lmul(lp(2), ball(3), linv(ball(2))), lmul(lp(2), f5, lp(2)))
    assert total == {0: F(11, 3), -1: F(32, 3)}
    lo, hi = bounds(total)
    assert F(706, 100) < lo and hi < F(707, 100)
    return True
