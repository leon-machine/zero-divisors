"""transport.matrix-units-peirce-isomorphism: exact checks.

Setting (T01 Sec. 5): A = Cl(p,q) with p - q = 1 mod 4, generators e_0..e_{n-1}; omega = e_0...e_{n-1}
is central with omega^2 = +1, eps_+- = (1 +- omega)/2; B_gamma adjoins nu = e_n with Q(nu) = gamma = +-1.
Every such signature with n <= 5 ((1,0), (2,1), (0,3), (3,2), (1,4), (5,0)) and both gamma are tested.
(1) E11 = eps_+, E22 = eps_-, E12 = eps_+ nu, E21 = gamma eps_- nu satisfy E11 + E22 = 1 and all 16
    relations E_ij E_kl = delta_jk E_il; the premise relation nu eps_+- = eps_-+ nu is computed; with the
    opposite sign on E21 the relation E12 E21 = E11 fails (control).
(2) phi(b) = (E_1i b E_j1)_ij: every entry lies in the corner E11 B E11, of dimension 2^(n-1);
    phi is injective on B (rank 2^(n+1) = 4 dim corner, so bijective), unital (phi(1) = diag(E11, E11)),
    multiplicative on sample pairs (the corner's unit is E11), and the displayed inverse
    sum_ij E_i1 c_ij E_1j recovers every basis blade of B.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(1, 0), (2, 1), (0, 3), (3, 2), (1, 4), (5, 0)]
SEEDS = (11, 29, 47)


def setup(p, q, g, e21_sign=1):
    n = p + q
    sq = GA.sig(p, q) + (g,)
    nu = GA.gen(n)
    omega = {tuple(range(n)): F(1)}
    ep = GA.scal(F(1, 2), GA.add(GA.sc(1), omega))
    em = GA.scal(F(1, 2), GA.sub(GA.sc(1), omega))
    E = {(1, 1): ep, (2, 2): em, (1, 2): GA.mul(ep, nu, sq),
         (2, 1): GA.scal(e21_sign * g, GA.mul(em, nu, sq))}
    return n, sq, nu, omega, ep, em, E


def prand(blades, seed):
    state, out = seed, {}
    for b in blades:
        state = (1103515245 * state + 12345) % (2 ** 31)
        c = (state % 7) - 3
        if c:
            out[b] = F(c)
    return out


def rank(elems, m):
    bl = GA.all_blades(m)
    rows = [GA.basis_vector_of(x, bl) for x in elems]
    return GA.rank_of_vectors(rows) if rows else 0


def check_matrix_unit_relations():
    premise("transport.ascent-renders-grade-involution-inner")
    ok = True
    for (p, q) in SIGS:
        for g in (1, -1):
            n, sq, nu, omega, ep, em, E = setup(p, q, g)
            # hypotheses of the setting, computed: omega central in A, omega^2 = 1
            ok = ok and GA.eq(GA.mul(omega, omega, sq), GA.sc(1))
            ok = ok and all(GA.commutes(omega, GA.gen(i), sq) for i in range(n))
            # premise: nu eps_+- = eps_-+ nu
            ok = ok and GA.eq(GA.mul(nu, ep, sq), GA.mul(em, nu, sq))
            ok = ok and GA.eq(GA.mul(nu, em, sq), GA.mul(ep, nu, sq))
            ok = ok and GA.eq(GA.add(E[(1, 1)], E[(2, 2)]), GA.sc(1))
            for (i, j), Eij in E.items():
                for (k, l), Ekl in E.items():
                    want = E[(i, l)] if j == k else {}
                    ok = ok and GA.eq(GA.mul(Eij, Ekl, sq), want)
            # control: E21 with the opposite sign breaks E12 E21 = E11
            _, _, _, _, _, _, Eb = setup(p, q, g, e21_sign=-1)
            ok = ok and not GA.eq(GA.mul(Eb[(1, 2)], Eb[(2, 1)], sq), Eb[(1, 1)])
    _tp_rv = (ok); assert _tp_rv is not False, "check_matrix_unit_relations"; return _tp_rv


def check_peirce_isomorphism():
    premise("transport.ascent-renders-grade-involution-inner")
    ok = True
    for (p, q) in SIGS:
        for g in (1, -1):
            n, sq, nu, omega, ep, em, E = setup(p, q, g)
            m = n + 1
            blades = GA.all_blades(m)
            E11 = E[(1, 1)]

            def phi(b):
                return {(i, j): GA.mul(GA.mul(E[(1, i)], b, sq), E[(j, 1)], sq)
                        for i in (1, 2) for j in (1, 2)}

            # corner dimension 2^(n-1)
            corner = [GA.mul(GA.mul(E11, {b: F(1)}, sq), E11, sq) for b in blades]
            dc = rank(corner, m)
            ok = ok and dc == 2 ** (n - 1) and 4 * dc == 2 ** m
            # phi lands in the corner, is injective (hence bijective) and is inverted by the display
            images = []
            for b in blades:
                Pb = phi({b: F(1)})
                ok = ok and all(GA.eq(GA.mul(GA.mul(E11, x, sq), E11, sq), x) for x in Pb.values())
                images.append([c for ij in sorted(Pb) for c in GA.basis_vector_of(Pb[ij], blades)])
                back = GA.add(*[GA.mul(GA.mul(E[(i, 1)], Pb[(i, j)], sq), E[(1, j)], sq)
                                for i in (1, 2) for j in (1, 2)])
                ok = ok and GA.eq(back, {b: F(1)})
            ok = ok and GA.rank_of_vectors(images) == 2 ** m
            # unital
            P1 = phi(GA.sc(1))
            ok = ok and GA.eq(P1[(1, 1)], E11) and GA.eq(P1[(2, 2)], E11)
            ok = ok and GA.is_zero(P1[(1, 2)]) and GA.is_zero(P1[(2, 1)])
            # multiplicative on sample pairs (matrix product over the corner)
            xs = [prand(blades, s) for s in SEEDS]
            for a in range(len(xs)):
                b2 = xs[(a + 1) % len(xs)]
                Pa, Pb, Pab = phi(xs[a]), phi(b2), phi(GA.mul(xs[a], b2, sq))
                for i in (1, 2):
                    for j in (1, 2):
                        s = GA.add(*[GA.mul(Pa[(i, k)], Pb[(k, j)], sq) for k in (1, 2)])
                        ok = ok and GA.eq(s, Pab[(i, j)])
    _tp_rv = (ok); assert _tp_rv is not False, "check_peirce_isomorphism"; return _tp_rv
