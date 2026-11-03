"""one-relation.vector-derivative-covariant-first-order-operator: exact checks.

Cl(1,3) in GA.py (signature (+,-,-,-)), gamma^mu = eta^{mu mu} gamma_mu, I = gamma_0 gamma_1 gamma_2 gamma_3.
Covariance of D = A^mu d_mu under a rotor R is R^-1 A^mu R = M(R)^mu_nu A^nu, with M(R) defined by
R^-1 gamma^mu R = M(R)^mu_nu gamma^nu; a linear condition on the 64 real coordinates of (A^0..A^3).
(1) For six rational rotors (boosts 5/4 + 3/4 g0g1, 13/12 + 5/12 g0g2, 17/15 + 8/15 g0g3; rotations
    3/5 + 4/5 g1g2, 5/13 + 12/13 g1g3, 8/17 + 15/17 g2g3; each R R~ = 1) the stacked 384 x 64 system has
    a kernel of dimension exactly 2, equal to the span of A^mu = gamma^mu and A^mu = gamma^mu I. This is an
    upper bound for the full spin group, which both solutions meet (gamma^mu by definition of M, gamma^mu I
    since I commutes with even elements; checked for each rotor).
(2) gamma^mu (a + b I) = (a - b I) gamma^mu (I anticommutes with every vector), (a - bI)(a + bI) = a^2 + b^2
    (I^2 = -1), so a - bI is invertible for (a, b) != 0.
(3) Right multiplication: psi -> gamma^mu psi B with B = gamma_0 is not a left multiplication A^mu psi
    (A^mu would have to be gamma^mu B, which fails on psi = gamma_1); for B central (B = 1 or 2) it is.
"""
from fractions import Fraction as F

import GA

SQ = GA.sig(1, 3)
BL = GA.all_blades(4)
GAM = [GA.gen(i) for i in range(4)]
GUP = [GA.scal(F(SQ[i]), GAM[i]) for i in range(4)]
PS = GA.mul(GA.mul(GAM[0], GAM[1], SQ), GA.mul(GAM[2], GAM[3], SQ), SQ)
ROTORS = [(0, 1, F(5, 4), F(3, 4)), (0, 2, F(13, 12), F(5, 12)), (0, 3, F(17, 15), F(8, 15)),
          (1, 2, F(3, 5), F(4, 5)), (1, 3, F(5, 13), F(12, 13)), (2, 3, F(8, 17), F(15, 17))]
AB = [(F(1), F(0)), (F(2), F(3)), (F(-1, 2), F(5))]


def rotor(i, j, a, b):
    return GA.add(GA.sc(a), GA.scal(b, GA.mul(GAM[i], GAM[j], SQ)))


def vector_matrix(R, Ri):
    M = []
    for mu in range(4):
        y = GA.mul(GA.mul(Ri, GUP[mu], SQ), R, SQ)
        if any(len(b) != 1 for b in y):
            return None
        M.append([GA.dot(y, GAM[nu], SQ) for nu in range(4)])     # coefficient of gamma^nu
    return M


def condition_rows(R, Ri, M):
    rows = []
    for out_mu in range(4):
        for out_b in BL:
            row = []
            for mu in range(4):
                for b in BL:
                    val = F(0)
                    if mu == out_mu:
                        val += GA.mul(GA.mul(Ri, {b: F(1)}, SQ), R, SQ).get(out_b, F(0))
                    # M^out_mu_mu A^mu in the gamma^nu basis: A^mu = gamma^mu-type unknowns
                    if b == out_b:
                        val -= M[out_mu][mu]
                    row.append(val)
            rows.append(row)
    return rows


def sol_vec(mult):
    out = []
    for mu in range(4):
        y = GA.mul(GUP[mu], mult, SQ)
        out.extend(y.get(b, F(0)) for b in BL)
    return out


def check_covariant_operators_span_gamma_and_gamma_i():
    rows = []
    ok = True
    for i, j, a, b in ROTORS:
        R = rotor(i, j, a, b)
        Ri = GA.reverse(R)
        ok = ok and GA.eq(GA.mul(R, Ri, SQ), GA.sc(1))
        M = vector_matrix(R, Ri)
        ok = ok and M is not None
        rows.extend(condition_rows(R, Ri, M))
    ok = ok and len(rows) == 384 and len(rows[0]) == 64
    ker = GA.field_kernel(rows)
    s1, s2 = sol_vec(GA.sc(1)), sol_vec(PS)
    ok = ok and len(ker) == 2 and GA.field_rank([s1, s2]) == 2 and GA.field_rank(ker + [s1, s2]) == 2
    ok = ok and all(sum(r[k] * s[k] for k in range(64)) == 0 for r in rows for s in (s1, s2))
    _tp_rv = (ok); assert _tp_rv is not False, "check_covariant_operators_span_gamma_and_gamma_i"; return _tp_rv


def check_constant_factor_is_invertible():
    ok = GA.eq(GA.mul(PS, PS, SQ), GA.sc(-1)) and all(GA.anticommutes(PS, g, SQ) for g in GAM)
    for a, b in AB:
        x = GA.add(GA.sc(a), GA.scal(b, PS))
        y = GA.add(GA.sc(a), GA.scal(-b, PS))
        ok = ok and all(GA.eq(GA.mul(GUP[m], x, SQ), GA.mul(y, GUP[m], SQ)) for m in range(4))
        ok = ok and GA.eq(GA.mul(y, x, SQ), GA.sc(a * a + b * b))
    ok = ok and GA.mul(GA.add(GA.sc(2), GA.scal(3, PS)), GA.add(GA.sc(2), GA.scal(-3, PS)), SQ) == {(): F(13)}
    _tp_rv = (ok); assert _tp_rv is not False, "check_constant_factor_is_invertible"; return _tp_rv


# Sample right factors B with whether B is central (a non-central gamma_0 and two scalars), and the
# sample field psi on which psi -> gamma^mu psi B is compared with the left action A psi.
RIGHT_FACTORS = ((GAM[0], False), (GA.sc(1), True), (GA.sc(2), True))
PSI_SAMPLE = GAM[1]


def check_right_multiplication_is_outside_the_class():
    ok = True
    mismatches = 0
    for B, central in RIGHT_FACTORS:
        for mu in range(len(GUP)):
            A = GA.mul(GUP[mu], B, SQ)                              # forced by psi = 1
            psi = PSI_SAMPLE
            left = GA.mul(A, psi, SQ)
            right = GA.mul(GA.mul(GUP[mu], psi, SQ), B, SQ)
            ok = ok and GA.eq(left, right) == central
            mismatches += not GA.eq(left, right)
    # by hand: gamma_0 anticommutes with psi = gamma_1, so right = -left != left at all four mu; the
    # scalars give no mismatch
    ok = ok and mismatches == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_right_multiplication_is_outside_the_class"; return _tp_rv
