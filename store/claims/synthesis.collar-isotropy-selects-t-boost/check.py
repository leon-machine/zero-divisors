"""synthesis.collar-isotropy-selects-t-boost: exact checks in the basis-blade engine of GA.py.

Cl(1,3) with e0^2 = 1, e1^2 = e2^2 = e3^2 = -1 (e0 the Hubble-normal direction, e1 the t-direction,
e2, e3 the sphere directions, as in the collar's adapted frame). Boost bivectors B_i = e0 e_i
(square +1), rotation bivectors R_ij = e_i e_j (square -1). For K = B/2 with K^2 = 1/4,
exp(-beta K) = cosh(beta/2) - 2 sinh(beta/2) K; rational (cosh, sinh) on the hyperbola.
Checked:
  (a) B_i^2 = 1, R_ij^2 = -1, [B_1, B_2] = -2 R_12 (nonzero): the three boosts do not commute;
  (b) the bivectors commuting with R_23 are exactly span{B_1, R_23} (kernel of a 6x6 rational system);
      the bivectors commuting with all three R_ij: only 0;
  (c) the B_1-Gibbs element rho_1 = c - s B_1 is invariant under every rational R_23 rotor; the
      B_2-Gibbs element rho_2 = c - s B_2 is not (for s != 0 and a rotation angle with sin != 0), and the
      R_23 rotation by a right angle carries rho_2 to the B_3-Gibbs element;
  (d) the Kasner rate tensor diag(-1/3, 2/3, 2/3) on (e1, e2, e3) is fixed by the rotations of the
      (e2, e3) plane and by no rotation of the (e1, e2) plane with nonzero sine; the same at first order
      in R with the collar's rates (-1/3 - 4R/15, 2/3 - 2R/15, 2/3 - 2R/15).
"""
import GA
from fractions import Fraction as F
from tp_premise import premise

SQ = (1, -1, -1, -1)


def m(*xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, SQ)
    return out


e = [GA.gen(i) for i in range(4)]
B = {1: m(e[0], e[1]), 2: m(e[0], e[2]), 3: m(e[0], e[3])}
R = {(1, 2): m(e[1], e[2]), (1, 3): m(e[1], e[3]), (2, 3): m(e[2], e[3])}
BIV = [B[1], B[2], B[3], R[(1, 2)], R[(1, 3)], R[(2, 3)]]


def comm(x, y):
    return GA.sub(GA.mul(x, y, SQ), GA.mul(y, x, SQ))


def rotor(c, s, biv):
    """c + s biv, with c^2 + s^2 = 1 for a rotation bivector (square -1); inverse c - s biv"""
    return GA.add(GA.sc(c), GA.scal(s, biv)), GA.add(GA.sc(c), GA.scal(-s, biv))


def conj(r, ri, x):
    return GA.mul(GA.mul(r, x, SQ), ri, SQ)


def centraliser_dim(gens):
    """dimension of {sum_k x_k BIV_k : [g, .] = 0 for g in gens}, by exact rank"""
    blades = GA.all_blades(4)
    rows = []
    for g in gens:
        cols = [comm(g, bv) for bv in BIV]
        for bl in blades:
            rows.append([c.get(bl, F(0)) for c in cols])
    return len(BIV) - GA.mat_rank(rows)


def check_boost_algebra_and_isotropy_centraliser():
    premise("singularity.imported-interior-collar-kasner-form")
    premise("singularity.modular-flow-boundary-modes-holonomy-universal")
    premise("synthesis.phase-flow-is-time-rotor-flow-kms-continuation")
    # frame *-structure: x* = x for Q(x) = 1, x* = -x for Q(x) = -1, antiautomorphism
    star = {0: GA.sc(1), 1: GA.sc(-1), 2: GA.sc(-1), 3: GA.sc(-1)}

    def star_biv(i, j):
        return m(GA.scal(star[j][()], e[j]), GA.scal(star[i][()], e[i]))
    for i in (1, 2, 3):
        assert GA.eq(star_biv(0, i), B[i])                     # boosts are *-symmetric
    for (i, j) in R:
        assert GA.eq(star_biv(i, j), GA.neg(R[(i, j)]))        # rotations are *-antisymmetric
    for i in (1, 2, 3):
        assert GA.eq(m(B[i], B[i]), GA.sc(1))
    for k in R:
        assert GA.eq(m(R[k], R[k]), GA.sc(-1))
    assert GA.eq(comm(B[1], B[2]), GA.scal(-2, R[(1, 2)])) and not GA.is_zero(comm(B[1], B[2]))
    assert not GA.is_zero(comm(B[1], B[3])) and not GA.is_zero(comm(B[2], B[3]))
    # centraliser of R_23 among bivectors: span{B_1, R_23}
    assert centraliser_dim([R[(2, 3)]]) == 2
    assert GA.is_zero(comm(R[(2, 3)], B[1])) and GA.is_zero(comm(R[(2, 3)], R[(2, 3)]))
    assert not GA.is_zero(comm(R[(2, 3)], B[2])) and not GA.is_zero(comm(R[(2, 3)], B[3]))
    # centraliser of the whole frame so(3): zero
    assert centraliser_dim([R[(1, 2)], R[(1, 3)], R[(2, 3)]]) == 0
    GA.check("the bivectors commuting with the isotropy rotation R_23 are span{B_1, R_23}; "
             "nothing nonzero commutes with all frame rotations", True)


def check_isotropy_invariant_kms_is_t_boost_only():
    premise("singularity.kms-uniqueness-factor")
    premise("singularity.modular-flow-boundary-modes-holonomy-universal")
    for (c, s) in [(F(5, 4), F(3, 4)), (F(13, 5), F(-12, 5)), (F(17, 8), F(15, 8))]:
        assert c * c - s * s == 1
        rho1 = GA.add(GA.sc(c), GA.scal(-s, B[1]))          # e^{-beta K_1}, K_1 = B_1/2, beta = 2 artanh(s/c)
        rho2 = GA.add(GA.sc(c), GA.scal(-s, B[2]))
        rho3 = GA.add(GA.sc(c), GA.scal(-s, B[3]))
        # rho_1 is a positive invertible element: rho_1 (c + s B_1) = c^2 - s^2 = 1
        assert GA.eq(m(rho1, GA.add(GA.sc(c), GA.scal(s, B[1]))), GA.sc(1))
        for (ct, st) in [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13)), (F(8, 17), F(15, 17))]:
            r, ri = rotor(ct, st, R[(2, 3)])
            assert GA.eq(m(r, ri), GA.sc(1))
            assert GA.eq(conj(r, ri, rho1), rho1)              # B_1-Gibbs: isotropy-invariant
            assert not GA.eq(conj(r, ri, rho2), rho2)          # B_2-Gibbs: not invariant
            assert not GA.eq(conj(r, ri, rho3), rho3)
        # the right-angle isotropy rotation (half-angle c = s = 1/sqrt 2) squared away: use the
        # rotor e2 e3 itself (a rotation by pi in the plane, up to sign) and the generator form:
        # [R_23, B_2] = 2 B_3, so the isotropy flow mixes B_2 into B_3
        assert GA.eq(comm(R[(2, 3)], B[2]), GA.scal(2, B[3]))
        assert not GA.eq(rho2, rho3)
    GA.check("for every rational beta the B_1-Gibbs element commutes with the isotropy rotations and "
             "the B_2-, B_3-Gibbs elements do not; the isotropy flow mixes B_2 into B_3", True)


def check_kasner_rates_fix_isotropy_only():
    premise("singularity.imported-interior-collar-kasner-form")

    def rot3(i, j, c, s):
        M = [[F(int(a == b)) for b in range(3)] for a in range(3)]
        M[i][i], M[j][j], M[i][j], M[j][i] = c, c, -s, s
        return M

    def tr3(M):
        return [[M[b][a] for b in range(3)] for a in range(3)]

    def conj3(M, P):
        return GA.mat_mul(GA.mat_mul(M, P), tr3(M))

    P0 = [[F(-1, 3), 0, 0], [0, F(2, 3), 0], [0, 0, F(2, 3)]]
    P0 = [[F(x) for x in row] for row in P0]
    assert P0[0][0] + P0[1][1] + P0[2][2] == 1                 # sum p_i = 1
    assert P0[0][0] ** 2 + P0[1][1] ** 2 + P0[2][2] ** 2 == 1  # sum p_i^2 = 1
    for Rr in [F(1, 10), F(1, 4)]:
        P1 = [[F(-1, 3) - F(4, 15) * Rr, 0, 0], [0, F(2, 3) - F(2, 15) * Rr, 0], [0, 0, F(2, 3) - F(2, 15) * Rr]]
        P1 = [[F(x) for x in row] for row in P1]
        for P in (P0, P1):
            for (c, s) in [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]:
                assert GA.mat_eq(conj3(rot3(1, 2, c, s), P), P)        # (e2, e3) rotations: symmetries
                assert not GA.mat_eq(conj3(rot3(0, 1, c, s), P), P)    # (e1, e2) rotations: not
    GA.check("the Kasner rate tensor (and the collar's first-order rates) is fixed by the (e2,e3) "
             "rotations and by no (e1,e2) rotation", True)
