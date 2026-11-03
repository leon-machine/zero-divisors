"""odd-extensions.exceptional-algebra-residue-completion-both-sides: exact checks.

Same GA model as the line-wall check: Cl(2,4) with Lorentz frame e_1 (+1), e_2, e_3, e_4 (-1) and the
hyperbolic plane e_+ (+1), e_- (-1), I_0 = e_+ + e_-, phi = (e_+ - e_-)/2; I_Lambda = a I_0 + b phi,
w_Lambda = a I_0 - b phi, 2ab = Lambda/3. Square roots are avoided by comparing squares.
(i) V = (3/Lambda) w_Lambda has Q(V) = -3/Lambda; (w_Lambda/sqrt|Lambda|)^2 = Q(w)/|Lambda| = -sign(Lambda)/3,
which is Q(e_V)/3 for the unit vector e_V = V/|V|: the two normalisations differ by the fixed factor
sqrt 3. The rescaled Gram of (e_1..e_4, w_Lambda/sqrt|Lambda|) is diag(1,-1,-1,-1, +1/3) for Lambda < 0 and
diag(1,-1,-1,-1, -1/3) for Lambda > 0 in every gauge: off-diagonal entries vanish identically, and the
exceptional signatures are (2,3) and (1,4).
(ii) The inverse Gram's dying entry is -3/Lambda (Lambda (G^-1)_ww = -3) and Lambda Q(V) = -3; the residue
-3 w_0 (x) w_0 equals -3 I_0 (x) I_0 exactly when a(0)^2 = 1; Q(I_Lambda) = Lambda/3 = H^2, and
Q(w_Lambda)/(|Lambda|/3) = -sign(Lambda) (the weightless normalisation by sqrt(|Lambda|/3)).
(iii) (e_1..e_4, w_Lambda, I_Lambda) has signature (2,4) for every Lambda != 0; at Lambda = 0 it spans only 5
dimensions and phi completes it to (2,4). General model, for (p,q) in {(1,3), (2,1), (0,2), (3,0)}:
in R^(p,q) + H (null u, v, <u,v> = 1), Q(u + t v/2) = t, the complement u - t v/2 has norm -t, the
hyperplane span(f, u + t v/2) has signature (p,q) + sign(t) and corank one at t = 0, and the whole space
is (p+1,q+1) for every t; the Lambda family is u = I_0, v = phi, t = -Lambda/3 in the gauge a = 1.
(iv) K = Q(I_Lambda) = Lambda/3 changes sign across the wall, and (2,3) + (0,1) = (1,4) + (1,0) = (2,4);
by contrast a completion G (+) K with K of constant signature has det of opposite signs on the two
sides, so it degenerates in between.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = [F(1), F(-1), F(-1), F(-1), F(1), F(-1)]
E = [GA.gen(i) for i in range(6)]
I0 = GA.add(E[4], E[5])
PHI = GA.scal(F(1, 2), GA.sub(E[4], E[5]))
LAMBDAS = (F(-6), F(-1), F(-1, 4), F(1, 5), F(3), F(12))
GAUGES = (F(1), F(-2), F(3, 7), F(5))


def frozen(L, a):
    b = L / (6 * a)
    return GA.add(GA.scal(a, I0), GA.scal(b, PHI)), GA.sub(GA.scal(a, I0), GA.scal(b, PHI))


def Q(x):
    return GA.dot(x, x, SQ)


def gram(vs):
    return [[GA.dot(x, y, SQ) for y in vs] for x in vs]


def sign(x):
    return (x > 0) - (x < 0)


def check_rescaled_family_and_exceptional_algebras():
    premise("odd-extensions.line-tame-wall")
    premise("odd-extensions.are-ascents-pair-signed")
    ok = True
    for L in LAMBDAS:
        for a in GAUGES:
            I, w = frozen(L, a)
            V = GA.scal(3 / L, w)
            ok = ok and Q(V) == -3 / L
            resc_sq = Q(w) / abs(L)                         # (w / sqrt|Lambda|)^2
            ok = ok and resc_sq == F(-sign(L), 3)
            ok = ok and resc_sq / sign(Q(V)) == F(1, 3)      # = Q(e_V)/3: factor sqrt 3
            G = gram(E[:4] + [w])
            Gr = [[G[i][j] / (abs(L) if i == 4 and j == 4 else 1) for j in range(5)] for i in range(5)]
            want = [[(SQ[i] if i < 4 else F(-sign(L), 3)) if i == j else F(0) for j in range(5)] for i in range(5)]
            ok = ok and Gr == want
            ok = ok and GA.congruence_signature(Gr) == ((2, 3, 0) if L < 0 else (1, 4, 0))
    GA.check("both sides (i): rescaled family exactly block diagonal; exceptional algebras Cl(2,3) and Cl(1,4)", ok)
    return ok


def check_residue_and_stelle_west_norm():
    premise("odd-extensions.imported-frozen-point")
    premise("odd-extensions.imported-tame-walls-exceptional-algebra-residue")
    premise("standard-model.imported-frozen-point-dictionary")
    ok = True
    for L in LAMBDAS:
        for a in GAUGES:
            I, w = frozen(L, a)
            G = gram(E[:4] + [w])
            inv_ww = 1 / G[4][4]
            ok = ok and inv_ww == -3 / L and L * inv_ww == -3
            ok = ok and L * Q(GA.scal(3 / L, w)) == -3
            ok = ok and Q(I) == L / 3                                     # H^2 = Q(I)
            ok = ok and Q(w) / (abs(L) / 3) == -sign(L)
    # T = d Q(w_Lambda)/d Lambda from the data, and the residue Lambda (G^-1)_ww = 1/T
    for L in LAMBDAS:
        T = Q(frozen(L, F(1))[1]) / L
        ok = ok and T == F(-1, 3) and L * (1 / Q(frozen(L, F(1))[1])) * T == 1
    # residue -3 w_0 (x) w_0 with w_0 = a(0) I_0: equal to -3 I_0 (x) I_0 exactly when a(0)^2 = 1
    def outer(x):
        cx = [x.get((i,), F(0)) for i in range(6)]
        return [[-3 * p * q for q in cx] for p in cx]
    for a in GAUGES + (F(-1),):
        w0 = frozen(F(0), a)[1]
        ok = ok and GA.eq(w0, GA.scal(a, I0))
        ok = ok and (outer(w0) == outer(I0)) == (a in (F(1), F(-1)))
    GA.check("both sides (ii): Lambda (G^-1)_ww = -3 = Lambda Q(V); residue -3 w_0 (x) w_0; H^2 = Q(I)", ok)
    return ok


MODELS = ((1, 3), (2, 1), (0, 2), (3, 0))
TS = (F(2), F(-2), F(1, 3), F(-5, 7), F(0))


def check_completion_on_both_sides():
    premise("odd-extensions.transport-constrains-frozen-point-only-through")
    premise("odd-extensions.imported-minimal-completion-degenerate-algebra-rule")
    ok = True
    for L in LAMBDAS:
        for a in GAUGES:
            I, w = frozen(L, a)
            ok = ok and GA.congruence_signature(gram(E[:4] + [w, I])) == (2, 4, 0)
    I, w = frozen(F(0), F(1))
    ok = ok and GA.mat_rank([[x.get((i,), F(0)) for i in range(6)] for x in E[:4] + [w, I]]) == 5
    ok = ok and GA.congruence_signature(gram(E[:4] + [w, PHI])) == (2, 4, 0)
    ok = ok and 5 + 1 == len(E)                                           # m + r = 6
    # the general model R^(p,q) + H
    for p, q in MODELS:
        n = p + q
        sq = [F(1)] * p + [F(-1)] * q + [F(1), F(-1)]
        f = [GA.gen(i) for i in range(n)]
        u = GA.add(GA.gen(n), GA.gen(n + 1))
        v = GA.scal(F(1, 2), GA.sub(GA.gen(n), GA.gen(n + 1)))
        ok = ok and GA.dot(u, u, sq) == 0 and GA.dot(v, v, sq) == 0 and GA.dot(u, v, sq) == 1
        for t in TS:
            x = GA.add(u, GA.scal(t / 2, v))
            y = GA.sub(u, GA.scal(t / 2, v))
            ok = ok and GA.dot(x, x, sq) == t and GA.dot(y, y, sq) == -t and GA.dot(x, y, sq) == 0
            hyp = [[GA.dot(s, r, sq) for r in f + [x]] for s in f + [x]]
            expect = (p + (t > 0), q + (t < 0), int(t == 0))
            ok = ok and GA.congruence_signature(hyp) == expect
            whole = f + [GA.gen(n), GA.gen(n + 1)]
            ok = ok and GA.congruence_signature([[GA.dot(s, r, sq) for r in whole] for s in whole]) == (p + 1, q + 1, 0)
    # the Lambda family is the model with u = I_0, v = phi, t = -Lambda/3 (gauge a = 1)
    for L in LAMBDAS:
        ok = ok and GA.eq(frozen(L, F(1))[1], GA.add(I0, GA.scal(-L / 6, PHI)))
    GA.check("both sides (iii): the rung (2,4) completes the family on both sides; the general (p,q) model", ok)
    return ok


def check_complement_switches_sign():
    premise("odd-extensions.imported-tame-walls-exceptional-algebra-residue")
    ok = True
    for L in LAMBDAS:
        I, w = frozen(L, F(1))
        K = Q(I)
        ok = ok and K == L / 3
        side = GA.congruence_signature(gram(E[:4] + [w]))
        ksig = (1, 0) if K > 0 else (0, 1)
        ok = ok and (side[0] + ksig[0], side[1] + ksig[1]) == (2, 4)
    # a standard completion G (+) K with K of constant signature: det changes sign across the wall
    for k in (F(1), F(-1), F(2, 3)):
        dets = []
        for L in (F(-1), F(1)):
            w = frozen(L, F(1))[1]
            G = gram(E[:4] + [w])
            dets.append(G[0][0] * G[1][1] * G[2][2] * G[3][3] * G[4][4] * k)
        ok = ok and dets[0] * dets[1] < 0
    GA.check("both sides (iv): K = Lambda/3 changes sign, totals (2,4); constant K would force degeneration", ok)
    return ok
