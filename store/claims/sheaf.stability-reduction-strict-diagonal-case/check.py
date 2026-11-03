"""sheaf.stability-reduction-strict-diagonal-case: exact checks at the Kasner point u = 2 (p = (-2/7, 3/7, 6/7)),
in w = tau^(1/7), so rho = tau^(4/7) = w^4 and rho^(1/2) = w^2; strict diagonal data diag(1, -rho c1, -c2, -c3)
with units c1 = 1 + w, c2 = 1 + w^2, c3 = 1 - w^3/2, perturbed by a relatively admissible error Xi (each entry
of positive relative order: the dying-slot cross terms are rho^(1/2) times w^k, k >= 1, the dying entry rho w).

(1) Congruence: the nondegenerate block H' on slots (0, 2, 3) has leading principal minors that are units at
w = 0 (pivots invertible, by the boundary-unit lemma); the column x = H'^{-1} b is O(w) with b the cross column;
C = id - x into slot 1 has det C = 1 and C(0) = id (identity on the exceptional boundary); C^T G' C is block
diagonal with (1,1) entry the Schur complement; symmetric Gaussian elimination of H' with pivots at w = 0 equal
to 1, -1, -1 then gives diagonal data whose units at the boundary are the unperturbed c_i(0), and the Schur entry
over rho tends to -c1(0) = -1: c_i' = c_i (1 + O(tau^delta)).
(2) The conclusions of the variable-weight theorem hold verbatim: G' has corank one at E with radical the dying
slot, det G' = det H' x Schur, det G' / rho -> -1 (first-order dying eigenvalue with the unperturbed leading unit);
the completion with mu nu = -1/2 satisfies det h = det G' (-(1 - s)), det h(0) != 0, signature (2,4) at E and at
two collar points.
Control: an error of relative order zero in the cross term (Xi_12 = c rho^(1/2)) changes the leading unit
(c = 2: det G'/rho -> +3) or the order (c = 1: det G' = 3 w^8 + ...), so the admissibility hypothesis is exercised.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

w = GA.RF.var()


def C(x):
    return GA.RF.const(F(x))


def wp(k):
    out = GA.RF1
    for _ in range(k):
        out = out * w
    return out


RHO = wp(4)
C1, C2, C3 = GA.RF1 + w, GA.RF1 + wp(2), GA.RF1 - C(F(1, 2)) * wp(3)
G_STRICT = [[GA.RF1, GA.RF0, GA.RF0, GA.RF0], [GA.RF0, -(RHO * C1), GA.RF0, GA.RF0],
            [GA.RF0, GA.RF0, -C2, GA.RF0], [GA.RF0, GA.RF0, GA.RF0, -C3]]


def perturbed(cross12):
    """G + Xi; Xi has entries of positive relative order except possibly the (1,2) cross term passed in."""
    E = [[wp(1), wp(3), wp(2), GA.RF0],
         [wp(3), wp(5), cross12, wp(3)],
         [wp(2), cross12, wp(2), wp(3)],
         [GA.RF0, wp(3), wp(3), wp(1)]]
    return [[G_STRICT[i][j] + E[i][j] for j in range(4)] for i in range(4)]


ADMISSIBLE = wp(4)           # rho^(1/2) w^2


def at(M, w0):
    return [[e.eval(w0) for e in row] for row in M]


def congruence(Gp):
    H = [[Gp[i][j] for j in (0, 2, 3)] for i in (0, 2, 3)]
    b = [Gp[0][1], Gp[2][1], Gp[3][1]]
    x = GA.rf_mat_solve(H, b)
    Cm = [[GA.RF1 if i == j else GA.RF0 for j in range(4)] for i in range(4)]
    Cm[0][1], Cm[2][1], Cm[3][1] = -x[0], -x[1], -x[2]
    out = [[GA.RF0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc = GA.RF0
            for a in range(4):
                for c in range(4):
                    if not Cm[a][i].is_zero() and not Cm[c][j].is_zero():
                        acc = acc + Cm[a][i] * Gp[a][c] * Cm[c][j]
            out[i][j] = acc
    return H, b, x, Cm, out


def check_congruence_to_diagonal_data():
    premise("sheaf.boundary-units-invert")
    ok = True
    Gp = perturbed(ADMISSIBLE)
    H, b, x, Cm, CGC = congruence(Gp)
    # pivots: leading principal minors of H' are units at the boundary
    m1 = H[0][0]
    m2 = H[0][0] * H[1][1] - H[0][1] * H[1][0]
    m3 = GA.rf_mat_det(H)
    ok = ok and [m1.eval(F(0)), m2.eval(F(0)), m3.eval(F(0))] == [1, -1, 1]
    ok = ok and all(xi.eval(F(0)) == 0 for xi in x)
    ok = ok and GA.rf_mat_det(Cm).eqrf(GA.RF1) and at(Cm, F(0)) == [[1 if i == j else 0 for j in range(4)]
                                                                    for i in range(4)]
    ok = ok and all(CGC[i][1].is_zero() and CGC[1][i].is_zero() for i in (0, 2, 3))
    schur = Gp[1][1] - (b[0] * x[0] + b[1] * x[1] + b[2] * x[2])
    ok = ok and CGC[1][1].eqrf(schur)
    # diagonalise H' by symmetric elimination: pivots d1 = m1, d2 = m2/m1, d3 = m3/m2
    piv = [m1, m2 / m1, m3 / m2]
    ok = ok and [d.eval(F(0)) for d in piv] == [1, -1, -1]
    ok = ok and (schur / RHO).eval(F(0)) == -1
    # the perturbed units relative to the unperturbed ones tend to 1 (c_i' = c_i (1 + O(tau^delta)))
    ratios = [piv[0], piv[1] / (-C2), piv[2] / (-C3), (schur / RHO) / (-C1)]
    ok = ok and [r.eval(F(0)) for r in ratios] == [1, 1, 1, 1]
    GA.check("a unit congruence, identity on E, brings G + Xi to diagonal data with units c_i (1 + O(w))", ok)
    return ok


def check_conclusions_hold_verbatim():
    premise("sheaf.variable-weight-boundary-tameness-completion-forced")
    ok = True
    Gp = perturbed(ADMISSIBLE)
    H, b, x, Cm, CGC = congruence(Gp)
    detGp = GA.rf_mat_det(Gp)
    ok = ok and detGp.eqrf(GA.rf_mat_det(H) * CGC[1][1])
    ok = ok and (detGp / RHO).eval(F(0)) == -1
    G0 = at(Gp, F(0))
    ok = ok and GA.mat_rank(G0) == 3 and GA.congruence_signature(G0) == (1, 2, 1)
    ok = ok and all(G0[i][1] == 0 for i in range(4))
    s = GA.rf_mat_solve(Gp, [GA.RF0, GA.RF1, GA.RF0, GA.RF0])[1]
    h = [[GA.RF0] * 6 for _ in range(6)]
    for i in range(4):
        for j in range(4):
            h[i][j] = Gp[i][j]
    h[1][4] = h[4][1] = GA.RF1
    h[1][5] = h[5][1] = C(F(-1, 2))
    h[4][5] = h[5][4] = C(-1)
    deth = GA.rf_mat_det(h)
    ok = ok and deth.eqrf(detGp * (-(GA.RF1 - s)))
    ok = ok and deth.eval(F(0)) == 1
    for w0 in (F(0), F(1, 3), F(1, 2)):
        ok = ok and GA.congruence_signature(at(h, w0)) == (2, 4, 0)
    # control: relative order zero in the cross term corrupts the leading data
    d2 = GA.rf_mat_det(perturbed(C(2) * wp(2)))
    ok = ok and (d2 / RHO).eval(F(0)) == 3
    d1 = GA.rf_mat_det(perturbed(wp(2)))
    ok = ok and (d1 / RHO).eval(F(0)) == 0 and (d1 / wp(8)).eval(F(0)) == 3
    GA.check("perturbed data: corank one, same radical, det/rho -> -1, (2,4) completion with det h(0) = 1", ok)
    return ok
