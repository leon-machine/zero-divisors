"""dark-matter.imported-frozen-point-de-sitter-radius: exact checks in Cl(2,4).

Conventions: e0 (+1), e1..e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-; tractors
sigma ninf + mu + rho n0. The Einstein field is a sample hb (through hb^{-1}) and Omega with curvature
operator R(B) = (Lambda/3) B + a Weyl part; its Schouten map is computed by contraction.
  (1) P = (Lambda/6) id, the scale tractor I = ninf + (Lambda/6) n0 is parallel for the tractor gauge
      field, Q(I) = Lambda/3, and I^perp has signature (1,4) for Lambda > 0.
  (2) The bivectors fixing I form a 10-dimensional algebra, equal to Lambda^2(I^perp), with nondegenerate
      trace form of signature (4,6): so(1,4) (the null case ninf, Lambda = 0, has a 4-dimensional
      radical instead: the parabolic case).
  (3) The flat-model section: the null lifts X(x) = n0 + x - Q(x) ninf/2 have X.I = 1 - Lambda Q(x)/12,
      and Y = X/(X.I) - I/Q(I) lies in I^perp with Q(Y) = -3/Lambda = -l^2 and Lorentzian tangent
      space {I, Y}^perp of signature (1,3): the de Sitter hyperboloid of radius l, l^2 = 3/Lambda.
  (4) Lambda is a parameter of the laws: with Lambda fixed, the constraints Q(I) = Lambda/3,
      I.V = 0, Q(V) = -3/Lambda on (dI, dV) leave 9 dimensions and the 9 broken generators B -> (B x I,
      B x V) fill them; letting Lambda vary adds exactly the norm mode (I/(2 Lambda), -V/(2 Lambda), 1),
      which no generator produces. The phrase "under the action as written" is the reading of (4).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
VB = [(i,) for i in range(6)]
BIV = [(i, j) for i in range(6) for j in range(i + 1, 6)]


def mul(*xs):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, S)
    return r


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S), GA.mul(Y, X, S)))


def dot(a, b):
    return GA.dot(a, b, S)


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def linmap(M):
    return lambda A: GA.add(*[GA.scal(sum(F(M[m][n]) * dot(A, ER[m]) for m in range(4)), E[n])
                              for n in range(4)])


def perp(vs):
    M = [[dot(E[i], v) for i in range(6)] for v in vs]
    return [GA.add(*[GA.scal(k[i], E[i]) for i in range(6) if k[i]]) for k in GA.field_kernel(M)]


def signature(basis):
    return GA.congruence_signature([[dot(u, v) for v in basis] for u in basis])


def stabiliser(I):
    bl = [{b: F(1)} for b in BIV]
    cols = [GA.basis_vector_of(comm(B, I), VB) for B in bl]
    M = [[cols[j][r] for j in range(15)] for r in range(6)]
    ker = [GA.add(*[GA.scal(k[j], bl[j]) for j in range(15) if k[j]]) for k in GA.field_kernel(M)]
    form = GA.congruence_signature([[mul(B, C).get((), F(0)) for C in ker] for B in ker])
    return ker, form


def curvature(lam):
    s = mul(E[1], E[0])
    return lambda B: GA.add(GA.scal(lam / 3, B), GA.scal(F(5, 4), GA.add(B, GA.scal(3, mul(s, B, s)))))


def ricci(R, b):
    return GA.add(*[grade(comm(ER[m], R(comm(E[m], b))), 1) for m in range(4)])


def schouten(R):
    sc = sum(dot(ER[m], ricci(R, E[m])) for m in range(4))
    return lambda A: GA.scal(F(1, 2), GA.sub(ricci(R, A), GA.scal(sc / 6, A)))


def lift(x):
    X = vec(x)
    return GA.add(N0, X, GA.scal(-dot(X, X) / 2, NI))


HINV = [[2, 1, 0, 0], [0, 1, 0, -1], [1, 0, 3, 0], [0, 0, 1, 1]]
OMEGA = [mul(E[0], E[1]), GA.add(mul(E[1], E[2]), mul(E[0], E[3])), mul(E[2], E[3]), mul(E[0], E[2])]
LAMS = (F(3, 4), F(2), F(9, 5))
POINTS = ([0, 0, 0, 0], [1, 2, 0, -1], [F(1, 2), 0, 3, 1], [0, -1, 1, 1])
DIRS = ([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [3, 1, -2, 5])


def omega_T(a, P):
    av = vec(a)
    A = linmap(HINV)(av)
    om = GA.add(*[GA.scal(dot(av, ER[m]), OMEGA[m]) for m in range(4)])
    return GA.add(om, GA.neg(comm(NI, A)), comm(N0, P(A)))


def check_parallel_scale_tractor_norm_and_complement():
    premise("interior.scale-tractor-leaves-cone")
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for lam in LAMS:
        P = schouten(curvature(lam))
        ok = ok and all(GA.eq(P(E[m]), GA.scal(lam / 6, E[m])) for m in range(4))
        I = GA.add(NI, GA.scal(lam / 6, N0))
        ok = ok and all(GA.is_zero(comm(omega_T(a, P), I)) for a in DIRS)
        ok = ok and dot(I, I) == lam / 3
        ok = ok and signature(perp([I])) == (1, 4, 0)
    # by hand at Lambda = 2: I = ninf + n0/3, Q(I) = 2/3
    ok = ok and dot(GA.add(NI, GA.scal(F(1, 3), N0)), GA.add(NI, GA.scal(F(1, 3), N0))) == F(2, 3)
    GA.check("Einstein region: parallel scale tractor with Q(I) = Lambda/3 and I^perp of signature (1,4)", ok)
    assert ok


def check_stabiliser_is_de_sitter_algebra():
    premise("interior.non-null-stabilisers-section-they-act")
    premise("interior.stabiliser-rotates-parabolic-reductive")
    ok = True
    for lam in LAMS:
        I = GA.add(NI, GA.scal(lam / 6, N0))
        ker, form = stabiliser(I)
        ok = ok and len(ker) == 10 and form == (4, 6, 0)
        pb = perp([I])
        wedges = [comm(pb[i], pb[j]) for i in range(5) for j in range(i + 1, 5)]
        blades = [b for b in GA.all_blades(6) if len(b) == 2]
        ok = ok and GA.rank_of_vectors([GA.basis_vector_of(w, blades) for w in wedges]) == 10
        ok = ok and GA.rank_of_vectors([GA.basis_vector_of(w, blades) for w in wedges + ker]) == 10
    ker0, form0 = stabiliser(NI)
    ok = ok and len(ker0) == 10 and form0[2] == 4                      # Lambda = 0: parabolic
    GA.check("stabiliser of the frozen point is Lambda^2(I^perp) = so(1,4); at Lambda = 0 it is parabolic", ok)
    assert ok


def check_section_is_de_sitter_hyperboloid_radius_l():
    premise("interior.non-null-stabilisers-section-they-act")
    ok = True
    for lam in LAMS:
        I = GA.add(NI, GA.scal(lam / 6, N0))
        ell2 = 3 / lam
        for x in POINTS:
            X = lift(x)
            xv = vec(x)
            ok = ok and dot(X, X) == 0 and dot(X, I) == 1 - lam * dot(xv, xv) / 12
            Y = GA.sub(GA.scal(1 / dot(X, I), X), GA.scal(1 / dot(I, I), I))
            ok = ok and dot(Y, I) == 0 and dot(Y, Y) == -ell2
            ok = ok and signature(perp([I, Y])) == (1, 3, 0)
    # by hand: Lambda = 3/4 gives l^2 = 4
    I = GA.add(NI, GA.scal(F(1, 8), N0))
    X = lift([1, 2, 0, -1])
    Y = GA.sub(GA.scal(1 / dot(X, I), X), GA.scal(1 / dot(I, I), I))
    ok = ok and dot(Y, Y) == -4
    GA.check("flat-model section is the de Sitter hyperboloid Q(Y) = -l^2, l^2 = 3/Lambda", ok)
    assert ok


def check_lambda_is_a_parameter_of_the_laws():
    premise("dark-energy.under-action-written-norm-parameter-laws")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    for lam in LAMS:
        I = GA.add(NI, GA.scal(lam / 6, N0))
        V = GA.sub(N0, GA.scal(3 / lam, I))
        ok = ok and dot(V, I) == 0 and dot(V, V) == -3 / lam
        rows = [[2 * dot(I, E[i]) for i in range(6)] + [F(0)] * 6 + [F(-1, 3)],
                [dot(V, E[i]) for i in range(6)] + [dot(I, E[i]) for i in range(6)] + [F(0)],
                [F(0)] * 6 + [2 * dot(V, E[i]) for i in range(6)] + [-3 / lam ** 2]]
        fixed = [r[:12] for r in rows]
        ok = ok and 12 - GA.mat_rank(fixed) == 9                       # constrained space, Lambda fixed
        ok = ok and 13 - GA.mat_rank(rows) == 10                       # Lambda free
        orbit = []
        for b in BIV:
            B = {b: F(1)}
            orbit.append(GA.basis_vector_of(comm(B, I), VB) + GA.basis_vector_of(comm(B, V), VB) + [F(0)])
        ok = ok and GA.mat_rank(orbit) == 9
        ok = ok and all(sum(r[k] * o[k] for k in range(13)) == 0 for r in rows for o in orbit)
        mode = ([c / (2 * lam) for c in GA.basis_vector_of(I, VB)]
                + [-c / (2 * lam) for c in GA.basis_vector_of(V, VB)] + [F(1)])
        ok = ok and all(sum(r[k] * mode[k] for k in range(13)) == 0 for r in rows)
        ok = ok and GA.mat_rank(orbit + [mode]) == 10
    GA.check("Lambda fixed: 9 constrained fluctuations, all gauge; Lambda free: one norm mode, not gauge", ok)
    assert ok
