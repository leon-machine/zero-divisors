"""transport.no-go-level-elements: exact checks.

Setting (GA.py): V = R^{p,q} mixed with n >= 3, generators 0..p-1 square +1, p..n-1 square -1; the
null v = (e_0 + e_p)/2 and partner w0 = (e_0 - e_p)/2 (v.w0 = 1/2); U the span of the other
generators of V (nondegenerate, dimension n - 2); the extension V' = V + V-perp adds generators of
square +1, -1 or 0 (degenerate allowed), and U' = U + V-perp. Every element of Cl(V') is expanded in
the basis {1, v, w0, v w0} x blades(U') by an exact linear solve (Lemma
transport.splitting-along-hyperbolic-plane). Cases: (1,2), (2,1), (1,3), (2,2), (3,1), and the
ascents (1,2) + [0], (2,1) + [+1, -1], (1,3) + [+1].
  (1) Step 1: v sigma v = v gamma^ for sample sigma = alpha + v beta + w0 gamma + v w0 delta (using
      the commutation rule alpha v = v alpha^); the pseudo-inverses {sigma : v sigma v = v} form an
      affine space through w0 whose direction has dimension 3 * 2^k (k = dim U'): alpha, beta, delta
      free and gamma = 1.
  (2) Step 2: for u in U with Q(u) != 0, R = 1 + v u satisfies R R~ = 1, R = u'u/Q(u) with
      u' = u + Q(u) v and Q(u') = Q(u) (so R is a product of two vectors of equal square, and t u
      gives a path 1 + t v u in the group), R v R^-1 = v, R u'' R^-1 = u'' + 2(u.u'') v on U', and
      R w0 R^-1 = w0 - u - Q(u) v.
  (3) Step 3 and the no-go: the Cl(U') component of R sigma R^-1 is alpha - u for sample
      pseudo-inverses, and the joint affine system {v sigma v = v, R sigma R^-1 = sigma} has no
      solution in Cl(V') (rank of the augmented matrix exceeds the rank of the system), for each
      sample u: no pseudo-inverse of v is fixed by the stabiliser of v, so none is equivariant.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

CASES = [(1, 2, ()), (2, 1, ()), (1, 3, ()), (2, 2, ()), (3, 1, ()),
         (1, 2, (0,)), (2, 1, (1, -1)), (1, 3, (1,))]
# sample coefficients for alpha, beta, gamma, delta (blade index lists in U', coefficient)
SAMPLE = {"a": [((), 2), ((0,), -1), ((0, 1), 3)], "b": [((), 1), ((1,), 4)],
          "g": [((), -3), ((0,), 1)], "d": [((0,), 2), ((), 5)]}
U_COEFFS = [[1], [2, 1], [1, 0, -1], [3, 1]]


def setup(p, q, extra):
    n = p + q
    sq = GA.sig(p, q) + tuple(extra)
    m = n + len(extra)
    v = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(p)))
    w0 = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(p)))
    ugens = [i for i in range(n) if i not in (0, p)]
    uprime = [i for i in range(m) if i not in (0, p)]
    return sq, m, v, w0, ugens, uprime


def m3(x, y, z, sq):
    return GA.mul(GA.mul(x, y, sq), z, sq)


def ublades(uprime):
    out = []
    for b in GA.all_blades(len(uprime)):
        out.append(tuple(uprime[i] for i in b))
    return out


def expansion_basis(sq, v, w0, uprime):
    h = [GA.sc(1), v, w0, GA.mul(v, w0, sq)]
    return [GA.mul(hh, {b: F(1)}, sq) for hh in h for b in ublades(uprime)]


def coords(x, blades):
    return [x.get(b, F(0)) for b in blades]


def expand(x, basis, blades):
    """Coefficients of x in the expansion basis (exact solve)."""
    M = [[basis[j].get(b, F(0)) for j in range(len(basis))] for b in blades]
    return GA.field_solve(M, coords(x, blades))


def from_sample(key, uprime):
    out = {}
    for b, c in SAMPLE[key]:
        if all(i < len(uprime) for i in b):
            out = GA.add(out, {tuple(uprime[i] for i in b): F(c)})
    return out


def vec(coeffs, gens):
    return GA.add(*[GA.scal(c, GA.gen(i)) for c, i in zip(coeffs, gens) if c])


def lin_matrix(fn, blades):
    cols = [coords(fn({b: F(1)}), blades) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


def check_pseudo_inverse_normal_form():
    premise("transport.splitting-along-hyperbolic-plane")
    premise("primer.commutation-rule")
    ok = True
    for p, q, extra in CASES:
        sq, m, v, w0, ugens, uprime = setup(p, q, extra)
        al, be, ga, de = (from_sample(k, uprime) for k in "abgd")
        # the commutation rule used in Step 1
        ok = ok and GA.eq(GA.mul(al, v, sq), GA.mul(v, GA.grade_inv(al), sq))
        sigma = GA.add(al, GA.mul(v, be, sq), GA.mul(w0, ga, sq), m3(v, w0, de, sq))
        ok = ok and GA.eq(m3(v, sigma, v, sq), GA.mul(v, GA.grade_inv(ga), sq))
        # the solution set of v s v = v: affine, through w0, direction of dimension 3 * 2^k
        blades = GA.all_blades(m)
        k = len(uprime)
        ok = ok and GA.eq(m3(v, w0, v, sq), v)
        A = lin_matrix(lambda s: m3(v, s, v, sq), blades)
        ok = ok and len(blades) - GA.field_rank(A) == 3 * 2 ** k
        # and that direction is exactly gamma = 0: the expansion of every kernel element has no w0 slot
        basis = expansion_basis(sq, v, w0, uprime)
        for kv in GA.field_kernel(A):
            x = {b: c for b, c in zip(blades, kv) if c != 0}
            co = expand(x, basis, blades)
            nb = 2 ** k
            ok = ok and all(c == 0 for c in co[2 * nb:3 * nb])
    GA.check("v sigma v = v gamma^, and the pseudo-inverses of v are w0 + (alpha, beta, delta free)", ok)
    return ok


def check_null_rotations_fix_v_and_shear_w0():
    ok = True
    for p, q, extra in CASES:
        sq, m, v, w0, ugens, uprime = setup(p, q, extra)
        for uc in U_COEFFS:
            if len(uc) > len(ugens):
                continue
            u = vec(uc, ugens)
            Qu = GA.dot(u, u, sq)
            if Qu == 0:
                continue
            R = GA.add(GA.sc(1), GA.mul(v, u, sq))
            Rinv = GA.sub(GA.sc(1), GA.mul(v, u, sq))
            ok = ok and GA.eq(GA.mul(R, GA.reverse(R), sq), GA.sc(1)) and GA.eq(GA.reverse(R), Rinv)
            up = GA.add(u, GA.scal(Qu, v))
            ok = ok and GA.dot(up, up, sq) == Qu
            ok = ok and GA.eq(GA.scal(1 / Qu, GA.mul(up, u, sq)), R)
            for t in (F(1, 2), F(-3)):
                tu = GA.scal(t, u)
                tup = GA.add(tu, GA.scal(t * t * Qu, v))
                ok = ok and GA.eq(GA.scal(1 / (t * t * Qu), GA.mul(tup, tu, sq)),
                                  GA.add(GA.sc(1), GA.scal(t, GA.mul(v, u, sq))))
            ok = ok and GA.eq(m3(R, v, Rinv, sq), v)
            for i in uprime:
                ui = GA.gen(i)
                want = GA.add(ui, GA.scal(2 * GA.dot(u, ui, sq), v))
                ok = ok and GA.eq(m3(R, ui, Rinv, sq), want)
            ok = ok and GA.eq(m3(R, w0, Rinv, sq), GA.sub(GA.sub(w0, u), GA.scal(Qu, v)))
    GA.check("R = 1 + vu = u'u/Q(u) is a rotor fixing v, R u'' R^-1 = u'' + 2(u.u'')v, R w0 R^-1 = w0 - u - Q(u)v", ok)
    return ok


def check_no_pseudo_inverse_fixed_by_null_rotations():
    premise("transport.splitting-along-hyperbolic-plane")
    ok = True
    tried = 0
    for p, q, extra in CASES:
        sq, m, v, w0, ugens, uprime = setup(p, q, extra)
        blades = GA.all_blades(m)
        basis = expansion_basis(sq, v, w0, uprime)
        nb = 2 ** len(uprime)
        al, be, de = (from_sample(k, uprime) for k in "abd")
        sigma = GA.add(w0, al, GA.mul(v, be, sq), m3(v, w0, de, sq))
        A1 = lin_matrix(lambda s: m3(v, s, v, sq), blades)
        b1 = coords(v, blades)
        for uc in U_COEFFS[:2]:
            if len(uc) > len(ugens):
                continue
            u = vec(uc, ugens)
            if GA.dot(u, u, sq) == 0:
                continue
            R = GA.add(GA.sc(1), GA.mul(v, u, sq))
            Rinv = GA.sub(GA.sc(1), GA.mul(v, u, sq))
            # Step 3: the Cl(U') component of R sigma R^-1 is alpha - u
            co = expand(m3(R, sigma, Rinv, sq), basis, blades)
            want = coords(GA.sub(al, u), blades)
            got = {}
            for c, b in zip(co[:nb], ublades(uprime)):
                if c != 0:
                    got[b] = c
            ok = ok and coords(got, blades) == want
            # the joint system has no solution
            A2 = lin_matrix(lambda s: GA.sub(m3(R, s, Rinv, sq), s), blades)
            A = A1 + A2
            b = b1 + [F(0)] * len(blades)
            rA = GA.field_rank(A)
            rAb = GA.field_rank([row + [x] for row, x in zip(A, b)])
            ok = ok and rAb == rA + 1
            tried += 1
    ok = ok and tried == 12
    GA.check("no sigma with v sigma v = v is fixed by a null rotation R: the affine system is inconsistent", ok)
    return ok
