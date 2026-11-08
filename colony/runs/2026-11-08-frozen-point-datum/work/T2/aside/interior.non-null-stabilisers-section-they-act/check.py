"""interior.non-null-stabilisers-section-they-act: exact checks in Cl(2,4).

V = the vectors of Cl(2,4) (GA.py: generators 0..3 of squares +1, -1, -1, -1, then e+ (+1), e- (-1);
n0 = (e+ + e-)/2, ninf = e+ - e-). Bivectors act on V by the commutator product, B(v) = B x v. Sample
non-null I of both signs: ninf + rho n0 (Q = 2 rho) and two off-axis vectors.
(1) The stabiliser {B : B x I = 0} is computed as a kernel: dimension 10; it equals the span of the
    wedges of a basis of I-perp (rank 10, same span); I-perp has signature (1,4) if Q(I) > 0 and (2,3) if
    Q(I) < 0; the scalar-part form <XY> is nondegenerate on the stabiliser (semisimple: reductive with
    trivial nilradical).
(2) Points X of M_I (null with X.I = 1, built from point tractors n0 + x - Q(x)/2 ninf rescaled) map to
    Y = X - I/Q(I) with Y.I = 0 and Q(Y) = -1/Q(I), and back. At each Y the tangent space
    {v in I-perp : v.Y = 0} has signature (1,3); B -> B x Y maps the stabiliser onto it (rank 4,
    transitive) and the isotropy has dimension 6 and acts faithfully on the tangent space: a
    four-dimensional Lorentzian space with a 10-dimensional isometry algebra, de Sitter (Q(Y) < 0 in
    R^{1,4}) for Q(I) > 0 and anti-de Sitter (Q(Y) > 0 in R^{2,3}) for Q(I) < 0.
(3) Null X with X.I = 0: the form on X-perp in I-perp has signature (0,3) plus the null direction X for
    Q(I) > 0 (a Riemannian conformal 3-space: spacelike infinity) and (1,2) plus X for Q(I) < 0
    (Lorentzian: timelike infinity).
(4) Square norms: for Q(I) = h^2 (resp. -h^2) with h rational, one of n = I/h -+ t is non-null, t the
    basis vector of square +1 (resp. -1), and the reflection x -> -n x n^{-1} carries I/h to +-t, I-perp
    isometrically onto t-perp (the standard (1,4), resp. (2,3), space) and the stabiliser onto the span of
    the coordinate bivectors of t-perp: the standard so(1,4), resp. so(2,3), over Q.
Completeness and the global topology (S^3, S^1 x S^2) are not computed.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S24 = (1, -1, -1, -1, 1, -1)
N0 = GA.scal(F(1, 2), GA.add(GA.gen(4), GA.gen(5)))
NI = GA.sub(GA.gen(4), GA.gen(5))
BL2 = [b for b in GA.all_blades(6) if len(b) == 2]
VB = [(i,) for i in range(6)]


def vec(c):
    return GA.add(*[GA.scal(F(c[i]), GA.gen(i)) for i in range(6)])


def cm(X, Y):
    return GA.scal(F(1, 2), GA.sub(GA.mul(X, Y, S24), GA.mul(Y, X, S24)))


def dt(a, b):
    return GA.dot(a, b, S24)


def coords(x, basis):
    return [x.get(b, F(0)) for b in basis]


def kernel_space(vectors_in, rows_of):
    """Kernel basis of the linear map given by columns rows_of(v) for v in vectors_in."""
    cols = [rows_of(v) for v in vectors_in]
    return GA.field_kernel([list(r) for r in zip(*cols)])


def perp_basis(I, extra=()):
    """Basis of {v : v.I = 0 and v.w = 0 for w in extra}."""
    vecs = [GA.gen(i) for i in range(6)]
    rows = [[dt(w, v) for v in vecs] for w in (I,) + tuple(extra)]
    ker = GA.field_kernel(rows)
    return [GA.add(*[GA.scal(k[i], vecs[i]) for i in range(6) if k[i]]) for k in ker]


def gram_sig(basis):
    return GA.congruence_signature([[dt(u, v) for v in basis] for u in basis])


def stab(I):
    ker = kernel_space(BL2, lambda b: coords(cm({b: F(1)}, I), VB))
    return [{BL2[i]: k[i] for i in range(15) if k[i]} for k in ker]


SAMPLES = [GA.add(NI, GA.scal(F(1, 8), N0)), GA.add(NI, GA.scal(F(3), N0)),
           GA.add(NI, GA.scal(F(-1, 8), N0)), GA.add(NI, GA.scal(F(-2), N0)),
           vec([1, 2, 0, 0, 3, 1]), vec([0, 1, 1, 2, 1, 0])]
XS = [[F(0), F(0), F(0), F(0)], [F(1), F(2), F(0), F(-1)], [F(1, 2), F(0), F(3), F(1)], [F(2), F(1), F(1), F(1)]]


def point(x):
    xv = GA.add(*[GA.scal(x[i], GA.gen(i)) for i in range(4)])
    return GA.add(N0, xv, GA.scal(-GA.dot(xv, xv, S24) / 2, NI))


def check_stabiliser_is_so_of_the_complement():
    ok = True
    signs = []
    for I in SAMPLES:
        q = dt(I, I)
        st = stab(I)
        pb = perp_basis(I)
        wedges = [cm(pb[i], pb[j]) for i in range(len(pb)) for j in range(i + 1, len(pb))]
        ok = ok and len(st) == 10 and len(pb) == 5 and len(wedges) == 10
        ok = ok and all(GA.is_zero(cm(W, I)) for W in wedges)
        ok = ok and GA.rank_of_vectors([coords(W, BL2) for W in wedges]) == 10
        ok = ok and GA.rank_of_vectors([coords(W, BL2) for W in wedges + st]) == 10
        sg = gram_sig(pb)
        ok = ok and sg == ((1, 4, 0) if q > 0 else (2, 3, 0))
        form = [[GA.mul(X, Y, S24).get((), F(0)) for Y in st] for X in st]
        ok = ok and GA.field_rank(form) == 10
        signs.append(q > 0)
    ok = ok and signs == [True, True, False, False, True, False]
    ok = ok and dt(SAMPLES[4], SAMPLES[4]) == 1 - 4 + 9 - 1 and dt(SAMPLES[5], SAMPLES[5]) == -6 + 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_stabiliser_is_so_of_the_complement"; return _tp_rv


def check_section_is_the_pseudosphere_with_transitive_isometries():
    ok = True
    for I in SAMPLES:
        q = dt(I, I)
        st = stab(I)
        for x in XS:
            X0 = point(x)
            s = dt(X0, I)
            if s == 0:
                continue
            X = GA.scal(1 / s, X0)
            ok = ok and dt(X, X) == 0 and dt(X, I) == 1
            Y = GA.sub(X, GA.scal(1 / q, I))
            ok = ok and dt(Y, I) == 0 and dt(Y, Y) == -1 / q
            ok = ok and GA.eq(GA.add(Y, GA.scal(1 / q, I)), X)
            tb = perp_basis(I, (Y,))
            ok = ok and len(tb) == 4 and gram_sig(tb) == (1, 3, 0)
            ok = ok and ((dt(Y, Y) < 0) == (q > 0))
            imgs = [coords(cm(B, Y), VB) for B in st]
            ok = ok and GA.rank_of_vectors(imgs) == 4
            ok = ok and all(dt(cm(B, Y), I) == 0 and dt(cm(B, Y), Y) == 0 for B in st)
            iso = GA.field_kernel([list(r) for r in zip(*imgs)])
            ok = ok and len(iso) == 6
            isob = [GA.add(*[GA.scal(k[i], st[i]) for i in range(10) if k[i]]) for k in iso]
            act = [sum((coords(cm(B, t), VB) for t in tb), []) for B in isob]
            ok = ok and GA.rank_of_vectors(act) == 6
    # by hand: I = ninf + n0/8, x = 0: X0 = n0, X.I = 1, Y = n0 - 4 I = n0 - 4 ninf - n0/2, Q(Y) = -4
    I = SAMPLES[0]
    Y = GA.sub(point(XS[0]), GA.scal(4, I))
    ok = ok and dt(Y, Y) == -4
    _tp_rv = (ok); assert _tp_rv is not False, "check_section_is_the_pseudosphere_with_transitive_isometries"; return _tp_rv


POLAR = [(F(1, 8), [1, 0, 0, 0], F(1, 2)), (F(9, 2), [3, 0, 0, 0], F(1)), (F(5, 2), [3, 2, 0, 0], F(1)),
         (F(-1, 8), [0, 1, 0, 0], F(1, 2)), (F(-2), [1, 1, 2, 0], F(1))]


def check_polar_infinity_spacelike_or_timelike():
    """X = (ninf - rho n0) + x with Q(x) = 2 rho is null and orthogonal to I = ninf + rho n0."""
    ok = True
    for rho, xc, s in POLAR:
        I = GA.add(NI, GA.scal(rho, N0))
        x = GA.scal(s, vec(xc + [0, 0]))
        X = GA.add(GA.sub(NI, GA.scal(rho, N0)), x)
        ok = ok and dt(X, X) == 0 and dt(X, I) == 0
        want = (0, 3, 1) if dt(I, I) > 0 else (1, 2, 1)
        ok = ok and gram_sig(perp_basis(I, (X,))) == want
    ok = ok and [dt(GA.add(NI, GA.scal(r, N0)), GA.add(NI, GA.scal(r, N0))) > 0 for r, _, _ in POLAR] == \
        [True, True, True, False, False]
    _tp_rv = (ok); assert _tp_rv is not False, "check_polar_infinity_spacelike_or_timelike"; return _tp_rv


# Sample inputs for check_square_norm_complement_is_standard: (I, h, index of the target basis vector),
# Q(I) = h^2 for target 0 (square +1) and Q(I) = -h^2 for target 1 (square -1).
SQUARE_SAMPLES = [(GA.add(NI, GA.scal(F(1, 8), N0)), F(1, 2), 0), (GA.add(NI, GA.scal(F(9, 2), N0)), F(3), 0),
                  (vec([3, 2, 0, 0, 2, 0]), F(3), 0), (GA.add(NI, GA.scal(F(-1, 8), N0)), F(1, 2), 1),
                  (GA.add(NI, GA.scal(F(-2), N0)), F(2), 1), (vec([0, 1, 2, 2, 0, 0]), F(3), 1)]


def check_square_norm_complement_is_standard():
    ok = True
    for I, h, tix in SQUARE_SAMPLES:
        t = GA.gen(tix)
        qt = dt(t, t)
        ok = ok and dt(I, I) == qt * h * h
        Ih = GA.scal(1 / h, I)
        ok = ok and dt(GA.sub(Ih, t), GA.sub(Ih, t)) + dt(GA.add(Ih, t), GA.add(Ih, t)) == 4 * qt
        n, sgn = GA.sub(Ih, t), 1
        if dt(n, n) == 0:
            n, sgn = GA.add(Ih, t), -1
        qn = dt(n, n)
        ok = ok and qn != 0

        def refl(x, odd=True):
            y = GA.scal(1 / qn, GA.mul(GA.mul(n, x, S24), n, S24))
            return GA.scal(-1, y) if odd else y
        ok = ok and GA.eq(refl(Ih), GA.scal(sgn, t))
        pb = perp_basis(I)
        im = [refl(v) for v in pb]
        ok = ok and all(dt(u, t) == 0 for u in im)
        ok = ok and all(dt(im[i], im[j]) == dt(pb[i], pb[j]) for i in range(5) for j in range(5))
        ok = ok and GA.rank_of_vectors([coords(u, VB) for u in im]) == 5
        st = stab(I)
        cst = [refl(B, odd=False) for B in st]
        ok = ok and all(all(v == 0 for b, v in X.items() if tix in b or len(b) != 2) for X in cst)
        ok = ok and GA.rank_of_vectors([coords(X, BL2) for X in cst]) == 10
        std = [GA.gen(i) for i in range(6) if i != tix]
        ok = ok and gram_sig(std) == ((1, 4, 0) if tix == 0 else (2, 3, 0))
    ok = ok and [tix for _, _, tix in SQUARE_SAMPLES] == [0, 0, 0, 1, 1, 1]
    _tp_rv = (ok); assert _tp_rv is not False, "check_square_norm_complement_is_standard"; return _tp_rv
