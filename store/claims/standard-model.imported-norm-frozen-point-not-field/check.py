"""standard-model.imported-norm-frozen-point-not-field: exact checks of the finite core.

The computable part is the unitary-gauge clause: every fluctuation of the constrained pair (I, V) is a
gauge transformation. In Cl(2,4) (GA.py; generators e_0 (+1), e_1..e_3 (-1), e_+ (+1), e_- (-1);
n_inf = e_+ + e_-, n_O = (e_+ - e_-)/2) take I = n_inf + (Lam/6) n_O, so Q(I) = Lam/3 (the
Stelle-West constraint), and V = X/sigma - (3/Lam) I with X = X(x) the null point of a sample event
and sigma = <X, I>, so that <V, I> = 0 and Q(V) = -3/Lam. For Lam = 3, 6, 3/2 and three events:
  (1) the linearised constraints (2<dI, I>, <dV, I> + <V, dI>, 2<dV, V>) have rank 3 on the 12
      components of (dI, dV): the constrained fluctuation space has dimension 9;
  (2) the infinitesimal action xi -> (xi . I, xi . V) of the 15 basis bivectors has rank 9 and every
      image satisfies the linearised constraints, so the action is onto the constrained space: unitary
      gauge dI = dV = 0 exists and is complete;
  (3) its kernel, the stabiliser, has dimension 6 and consists of bivectors of {I, V}-perp, a space of
      signature (1,3): so(1,3);
  (4) on I alone the image of the bivectors has rank 5 = dim I-perp.
The clauses about the action (no equation of motion for Lam, second variation in the connection
only) are statements about the functional and are not computed, nor is the covariant constancy of
the frozen point (the interior and vacuum-region premises). Both functions test the counting of
dark-energy.point-infinity-has-no-physical-fluctuation, the result the claim imports, and call
premise() for it.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
EP, EM = GA.gen(4), GA.gen(5)
NINF = GA.add(EP, EM)
NO = GA.scal(F(1, 2), GA.sub(EP, EM))
LAMS = [F(3), F(6), F(3, 2)]
EVENTS = [[0, 0, 0, 0], [F(1, 2), 1, 0, 0], [1, F(1, 3), 2, F(-1, 2)]]
BIV = [GA.mul(GA.gen(a), GA.gen(b), SQ) for a, b in combinations(range(6), 2)]


def vec4(x):
    return GA.add(*[GA.scal(F(x[i]), GA.gen(i)) for i in range(4) if x[i]]) if any(x) else {}


def Xof(x):
    Q = F(x[0]) ** 2 - F(x[1]) ** 2 - F(x[2]) ** 2 - F(x[3]) ** 2
    return GA.add(NO, vec4(x), GA.scal(-Q / 2, NINF))


def coords(v):
    return [v.get((i,), F(0)) for i in range(6)]


def dot(a, b):
    return GA.dot(a, b, SQ)


def act(xi, v):
    return GA.scal(F(1, 2), GA.sub(GA.mul(xi, v, SQ), GA.mul(v, xi, SQ)))


def pair(lam, x):
    I = GA.add(NINF, GA.scal(lam / 6, NO))
    X = Xof(x)
    sigma = dot(X, I)
    V = GA.sub(GA.scal(1 / sigma, X), GA.scal(3 / lam, I))
    return I, V


def check_unitary_gauge_exists_and_is_complete():
    premise("dark-energy.point-infinity-has-no-physical-fluctuation")
    ok = True
    for lam in LAMS:
        for x in EVENTS:
            I, V = pair(lam, x)
            ok = ok and dot(I, I) == lam / 3 and dot(V, I) == 0 and dot(V, V) == -3 / lam
            ci, cv = coords(I), coords(V)
            gI = [SQ[k] * ci[k] for k in range(6)]
            gV = [SQ[k] * cv[k] for k in range(6)]
            cons = [[2 * a for a in gI] + [F(0)] * 6,
                    gV + gI,
                    [F(0)] * 6 + [2 * a for a in gV]]
            ok = ok and GA.field_rank(cons) == 3
            images = []
            for xi in BIV:
                dI, dV = act(xi, I), act(xi, V)
                ok = ok and all(len(b) == 1 for b in GA.add(dI, dV))
                row = coords(dI) + coords(dV)
                ok = ok and all(sum(c * r for c, r in zip(con, row)) == 0 for con in cons)
                images.append(row)
            ok = ok and GA.field_rank(images) == 12 - 3
            ok = ok and GA.field_rank([coords(act(xi, I)) for xi in BIV]) == 5
    GA.check("the 15 bivectors act on the 9-dimensional constrained fluctuation space of (I, V) onto it", ok)
    return ok


def check_stabiliser_is_lorentz_of_the_complement():
    premise("dark-energy.point-infinity-has-no-physical-fluctuation")
    ok = True
    for lam in LAMS:
        for x in EVENTS:
            I, V = pair(lam, x)
            cols = [coords(act(xi, I)) + coords(act(xi, V)) for xi in BIV]
            M = [[cols[j][i] for j in range(15)] for i in range(12)]
            ker = GA.field_kernel(M)
            ok = ok and len(ker) == 6
            # {I, V}-perp: kernel of the two linear forms <., I>, <., V>; its signature
            rows = [[SQ[k] * coords(I)[k] for k in range(6)], [SQ[k] * coords(V)[k] for k in range(6)]]
            perp = GA.field_kernel(rows)
            ok = ok and len(perp) == 4
            gram = [[sum(SQ[k] * a[k] * b[k] for k in range(6)) for b in perp] for a in perp]
            ok = ok and GA.congruence_signature(gram) == (1, 3, 0)
            # each stabiliser bivector maps vectors into {I, V}-perp and kills I and V
            for kv in ker:
                xi = GA.add(*[GA.scal(c, b) for c, b in zip(kv, BIV) if c != 0])
                ok = ok and GA.is_zero(act(xi, I)) and GA.is_zero(act(xi, V))
                for k in range(6):
                    img = act(xi, GA.gen(k))
                    ok = ok and dot(img, I) == 0 and dot(img, V) == 0
    GA.check("the stabiliser of (I, V) is 6-dimensional, so(1,3) of the (1,3) complement {I, V}-perp", ok)
    return ok
