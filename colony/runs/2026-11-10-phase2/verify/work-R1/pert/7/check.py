"""synthesis.splits-adapted-to-the-null-pairs-and-the-states-common-to-all-of-them: exact checks.

Cl_Q(l,l): e_k (square +1, index 2k), f_k (square -1, index 2k+1), null pairs v_k = (e_k + f_k)/2,
w_k = (e_k - f_k)/2. For A in GL_l(Q) the adapted split has null pairs v'_j = sum_i A_ij v_i,
w'_j = sum_i (A^-1)_ji w_i and generators e'_j = v'_j + w'_j, f'_j = v'_j - w'_j; its adjoint is the
anti-automorphism that fixes the e'_j and negates the f'_j.

(i)   the adapted frames are orthonormal of squares +1, -1; l = 1, t = 4 is the stored boosted frame.
(ii)  the number element N, the total parity, the vacuum projector and the sector projectors are
      self-adjoint for every adapted split used.
(iii) the functionals real for all the splits used: dimension 2 (l = 1), 3 (l = 2), 4 (l = 3), equal to
      l + 1, spanned by the functionals of 1, N, ..., N^l; for diagonal A only: dimension 2^l (l = 2: 4).
(iv)  a stored pair state is not real for a second adapted split, and the common states give the CHSH
      element of the one-mode twisted directions the value Z * (value of the total parity) only.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
HALF = F(1, 2)


def clean(x):
    return {b: c for b, c in x.items() if c != 0}


def prod(sq, *xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, sq)
    return clean(r)


def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return clean(r)


def tau(x):
    return x.get((), F(0))


def blade(b):
    return {tuple(b): F(1)}


def modes(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    v = [lin((HALF, e[k]), (HALF, f[k])) for k in range(m)]
    w = [lin((HALF, e[k]), (-HALF, f[k])) for k in range(m)]
    return sq, e, f, v, w


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def shear(n, i, j):
    A, B = eye(n), eye(n)
    A[i][j], B[i][j] = F(1), F(-1)
    return A, B


def scale(n, i, t):
    A, B = eye(n), eye(n)
    A[i][i], B[i][i] = F(t), F(1) / F(t)
    return A, B


def frame(m, A, Ainv):
    sq, e, f, v, w = modes(m)
    vn = [lin(*[(A[i][j], v[i]) for i in range(m)]) for j in range(m)]
    wn = [lin(*[(Ainv[j][i], w[i]) for i in range(m)]) for j in range(m)]
    en = [clean(GA.add(vn[j], wn[j])) for j in range(m)]
    fn = [clean(GA.sub(vn[j], wn[j])) for j in range(m)]
    return sq, en, fn, vn, wn


def frame_is_orthonormal(m, A, Ainv):
    sq, en, fn, vn, wn = frame(m, A, Ainv)
    gens = en + fn
    ok = all(prod(sq, x, x) == ONE for x in en) and all(prod(sq, x, x) == GA.neg(ONE) for x in fn)
    return ok and all(GA.anticommutes(gens[i], gens[j], sq) for i in range(2 * m) for j in range(i))


def reflection(m, A, Ainv):
    """Images of the stored generators under the reflection fixing the e'_j and negating the f'_j."""
    sq, en, fn, vn, wn = frame(m, A, Ainv)
    out = []
    for i in range(2 * m):
        g = GA.gen(i)
        r = {}
        for x in en + fn:
            r = GA.add(r, GA.scal(tau(prod(sq, g, x)), x))
        out.append(clean(r))
    return sq, out


def adjoint(sq, images, x):
    r = {}
    for b, c in x.items():
        y = ONE
        for i in reversed(b):
            y = GA.mul(y, images[i], sq)
        r = GA.add(r, GA.scal(c, y))
    return clean(r)


def common_real(m, mats):
    """Kernel of the conditions omega(x - x^dagger_A) = 0 over all blades x and all splits A in mats."""
    sq = modes(m)[0]
    blades = GA.all_blades(2 * m)
    rows = []
    for A, Ainv in mats:
        _, images = reflection(m, A, Ainv)
        for b in blades:
            d = clean(GA.sub(blade(b), adjoint(sq, images, blade(b))))
            if d:
                rows.append([d.get(bb, F(0)) for bb in blades])
    return GA.field_kernel(rows), blades


def number(m):
    sq, e, f, v, w = modes(m)
    n = {}
    for k in range(m):
        n = GA.add(n, prod(sq, w[k], v[k]))
    return sq, clean(n)


def power_functionals(m):
    """Values on the blades of x -> tau(N^j x), j = 0..m."""
    sq, n = number(m)
    blades = GA.all_blades(2 * m)
    out, y = [], ONE
    for _ in range(m + 1):
        out.append([tau(prod(sq, y, blade(b))) for b in blades])
        y = prod(sq, y, n)
    return out


M1 = [(eye(1), eye(1)), scale(1, 0, 4)]
M2 = [(eye(2), eye(2)), scale(2, 0, 2), scale(2, 1, 3), shear(2, 0, 1)]
M2_DIAGONAL = [(eye(2), eye(2)), scale(2, 0, 2), scale(2, 1, 3)]
M3 = [(eye(3), eye(3)), scale(3, 0, 2), scale(3, 1, 3), scale(3, 2, 5), shear(3, 0, 1), shear(3, 1, 2)]


def check_adapted_frames_and_the_stored_boosted_frame():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    assert all(frame_is_orthonormal(1, *m) for m in M1) and all(frame_is_orthonormal(2, *m) for m in M2)
    assert all(frame_is_orthonormal(3, *m) for m in M3)
    sq, en, fn, vn, wn = frame(1, *scale(1, 0, 4))
    e, f = GA.gen(0), GA.gen(1)
    assert en[0] == lin((F(17, 8), e), (F(15, 8), f)) and fn[0] == lin((F(15, 8), e), (F(17, 8), f))
    assert prod(sq, fn[0], en[0]) == prod(sq, f, e)
    # the adjoint of the identity split is the blade inverse; of the boosted split it is not
    _, im0 = reflection(1, eye(1), eye(1))
    _, im4 = reflection(1, *scale(1, 0, 4))
    assert adjoint(sq, im0, e) == e and adjoint(sq, im0, f) == GA.neg(f)
    assert adjoint(sq, im4, en[0]) == en[0] and adjoint(sq, im4, e) != e


def check_number_parity_and_sector_projectors_are_self_adjoint_for_every_adapted_split():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    for m, mats in ((2, M2), (3, M3)):
        sq, n = number(m)
        gamma = ONE
        for k in range(m):
            gamma = prod(sq, gamma, GA.gen(2 * k + 1), GA.gen(2 * k))
        sectors = []
        for j in range(m + 1):
            q = ONE
            for i in range(m + 1):
                if i != j:
                    q = prod(sq, q, lin((F(1, j - i), n), (F(-i, j - i), ONE)))
            sectors.append(q)
        total = {}
        for q in sectors:
            total = GA.add(total, q)
        assert clean(total) == ONE and all(prod(sq, q, q) == q for q in sectors)
        assert [tau(q) * 2 ** m for q in sectors] == ([1, 2, 1] if m == 2 else [1, 3, 3, 1])
        for A, Ainv in mats:
            _, images = reflection(m, A, Ainv)
            assert adjoint(sq, images, n) == n and adjoint(sq, images, gamma) == gamma
            assert all(adjoint(sq, images, q) == q for q in sectors)
            _, en, fn, vn, wn = frame(m, A, Ainv)
            nn = {}
            for k in range(m):
                nn = GA.add(nn, prod(sq, wn[k], vn[k]))
            assert clean(nn) == n


def check_functionals_real_for_all_adapted_splits_are_functions_of_the_number():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("synthesis.premise-positivity-of-values")
    dims = []
    for m, mats in ((1, M1), (2, M2), (3, M3)):
        ker, blades = common_real(m, mats)
        powers = power_functionals(m)
        assert GA.rank_of_vectors(powers) == m + 1 == GA.rank_of_vectors(ker + powers)
        dims.append(len(ker))
    assert dims == [2, 3, 4]
    # one split only, and the diagonal splits only, leave more
    assert len(common_real(1, M1[:1])[0]) == 3 and len(common_real(2, M2[:1])[0]) == 10
    assert len(common_real(2, M2_DIAGONAL)[0]) == 4


def check_pair_state_depends_on_the_split_and_common_states_stay_at_two():
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    premise("synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate")
    sq, e, f, v, w = modes(2)
    p = [prod(sq, f[k], e[k]) for k in range(2)]
    gamma = prod(sq, p[0], p[1])
    c, s = F(3, 5), F(4, 5)
    rho = clean(GA.add(prod(sq, lin((F(1, 4), ONE), (F(1, 4), gamma)), lin((1, ONE), (c * c - s * s, p[0]))),
                       GA.scal(c * s, GA.add(prod(sq, w[0], w[1]), prod(sq, v[1], v[0])))))
    assert prod(sq, rho, rho) == rho and tau(rho) == F(1, 4)
    value = lambda x: tau(prod(sq, rho, x)) / tau(rho)
    _, im = reflection(2, *scale(2, 0, 1))
    x = prod(sq, w[0], w[1])
    assert value(x) == F(12, 25) and value(adjoint(sq, im, x)) == F(48, 25)
    # common functionals vanish on u = e_2 f_1 and on odd elements, so only Z Gamma contributes
    ker, blades = common_real(2, M2)
    u = prod(sq, e[1], f[0])
    twist = prod(sq, e[1], p[0])
    for kv in ker:
        om = lambda y: sum(kv[i] * y.get(b, F(0)) for i, b in enumerate(blades))
        assert om(u) == 0 and om(e[0]) == 0 and om(twist) == 0 and om(prod(sq, e[0], p[1])) == 0
        b1 = lin((F(3, 5), twist), (F(4, 5), p[1]))
        b2 = lin((F(4, 5), twist), (F(-3, 5), p[1]))
        chsh = clean(GA.add(prod(sq, e[0], b1), prod(sq, e[0], b2), prod(sq, p[0], b1), GA.neg(prod(sq, p[0], b2))))
        assert om(prod(sq, e[0], twist)) == 0 and om(chsh) == F(7, 5) * om(gamma)
