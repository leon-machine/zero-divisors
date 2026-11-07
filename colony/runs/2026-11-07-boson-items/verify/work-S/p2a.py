"""Exact checks: brackets of collective modes on a tower level with the kernel unit, and the central limit of
fluctuation states.

Level Cl(m, m + 2): kernel generators g1 = gen(0), g2 = gen(1) (square -1); plane j has e_j = gen(2 + 2j)
(square +1) and f_j = gen(3 + 2j) (square -1); v_j = (e_j + f_j)/2 creator, w_j = (e_j - f_j)/2 annihilator,
n_j = v_j w_j; J = g1 g2; Gamma = prod_j e_j f_j; * = reversion with a sign per negative-square generator.
A block is two planes. A real block state with occupations p1, p2 has density
rho = prod (p n + (1 - p)(1 - n)); its J-linear extension is omega(X) = 2^b (<rho X>_0 - J <J rho X>_0),
returned as the pair (coefficient of 1, coefficient of J).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

BLOCKS = (1, 2, 3)


def _level(m):
    s = tuple([-1, -1] + [1, -1] * m)
    mul = lambda x, y: GA.mul(x, y, s)
    J = mul(GA.gen(0), GA.gen(1))
    v = [GA.add(GA.scal(F(1, 2), GA.gen(2 + 2 * k)), GA.scal(F(1, 2), GA.gen(3 + 2 * k))) for k in range(m)]
    w = [GA.add(GA.scal(F(1, 2), GA.gen(2 + 2 * k)), GA.scal(F(-1, 2), GA.gen(3 + 2 * k))) for k in range(m)]
    n = [mul(v[k], w[k]) for k in range(m)]
    gam = GA.sc(1)
    for k in range(m):
        gam = mul(gam, mul(GA.gen(2 + 2 * k), GA.gen(3 + 2 * k)))
    pss = GA.sc(1)
    for k in range(len(s)):
        pss = mul(pss, GA.gen(k))
    return s, mul, J, v, w, n, gam, pss


def _star(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sg = (-1) ** (g * (g - 1) // 2)
        for k in b:
            if s[k] == -1:
                sg = -sg
        out[b] = sg * c
    return {b: c for b, c in out.items() if c != 0}


def _comm(mul, x, y):
    return GA.sub(mul(x, y), mul(y, x))


def _acomm(mul, x, y):
    return GA.add(mul(x, y), mul(y, x))


def _copy(x, blk):
    """the copy of a block-0 element on block blk (planes shifted by two per block; the kernel fixed)"""
    return {tuple(k if k < 2 else k + 4 * blk for k in b): c for b, c in x.items()}


def _rho(mul, n, occ):
    out = GA.sc(1)
    for nk, p in zip(n, occ):
        out = mul(out, GA.add(GA.scal(p, nk), GA.scal(1 - p, GA.sub(GA.sc(1), nk))))
    return out


def _omega(mul, J, rho, X, planes):
    y = mul(rho, X)
    return (2 ** planes * y.get((), F(0)), -(2 ** planes) * mul(J, y).get((), F(0)))


def _trace(mul, J, X):
    return (X.get((), F(0)), -mul(J, X).get((), F(0)))


def _partitions(lst):
    if not lst:
        yield []
        return
    first, rest = lst[0], lst[1:]
    for p in _partitions(rest):
        yield [[first]] + p
        for k in range(len(p)):
            yield p[:k] + [[first] + p[k]] + p[k + 1:]


def _cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def _cumulant(mom, k):
    tot = (F(0), F(0))
    for p in _partitions(list(range(k))):
        r = len(p)
        coef = F(-1) ** (r - 1)
        for t in range(2, r):
            coef *= t
        term = (coef, F(0))
        for blk in p:
            term = _cmul(term, mom(tuple(sorted(blk))))
        tot = (tot[0] + term[0], tot[1] + term[1])
    return tot


def _block_fields(s, mul, J, v, w, n):
    b = mul(v[0], w[1])
    c = mul(w[0], w[1])
    phi = GA.add(b, _star(b, s))
    pi = mul(J, GA.sub(_star(b, s), b))
    chi = GA.add(c, _star(c, s))
    return b, c, phi, pi, chi


def check_graded_locality_reduces_collective_brackets_to_single_blocks():
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    premise("std-algebra.witt-basis-car")
    ok = True
    for NB in BLOCKS:
        s, mul, J, v, w, n, gam, pss = _level(2 * NB)
        b, c, phi, pi, chi = _block_fields(s, mul, J, v, w, n)
        odd = [w[0], mul(w[0], n[1]), GA.add(v[0], mul(mul(v[0], v[1]), w[1]))]
        even = [b, c, GA.add(phi, mul(J, chi))]
        for a in range(NB):
            for d in range(NB):
                if a == d:
                    continue
                for x in odd:
                    for y in odd:
                        ok = ok and GA.is_zero(_comm(mul, _copy(x, a), _copy(_star(y, s), d)))
                    for y in even:
                        ok = ok and GA.is_zero(_comm(mul, _copy(x, a), _copy(y, d)))
                for x in even:
                    for y in even:
                        ok = ok and GA.is_zero(_comm(mul, _copy(x, a), _copy(_star(y, s), d)))
        x = odd[1]
        Fx = GA.add(*[_copy(x, a) for a in range(NB)])
        ok = ok and GA.eq(_acomm(mul, Fx, _star(Fx, s)),
                          GA.add(*[_copy(_acomm(mul, x, _star(x, s)), a) for a in range(NB)]))
        y = even[2]
        Fy = GA.add(*[_copy(y, a) for a in range(NB)])
        ok = ok and GA.eq(_comm(mul, Fy, _star(Fy, s)),
                          GA.add(*[_copy(_comm(mul, y, _star(y, s)), a) for a in range(NB)]))
        if NB >= 2:
            Fw = GA.add(*[_copy(w[0], a) for a in range(NB)])
            ok = ok and not GA.eq(_comm(mul, Fw, _star(Fw, s)),
                                  GA.add(*[_copy(_comm(mul, w[0], v[0]), a) for a in range(NB)]))
        # law of large numbers for the odd bracket: C = {x, x*} on each block, product state (3/4, 1/5)
        occ = [F(3, 4), F(1, 5)] * NB
        rho = _rho(mul, n, occ)
        C = _acomm(mul, x, _star(x, s))
        om = lambda X: _omega(mul, J, rho, X, 2 * NB)
        mean = om(C)
        D = GA.sub(GA.scal(F(1, NB), _acomm(mul, Fx, _star(Fx, s))), GA.sc(mean[0]))
        var1 = om(mul(_star(C, s), C))[0] - mean[0] ** 2
        ok = ok and mean == (F(1, 5), 0) and om(D) == (0, 0)
        ok = ok and om(mul(_star(D, s), D)) == (var1 / NB, 0) and var1 == F(1, 5) * F(4, 5)
    GA.check("odd copies anticommute, even copies commute: collective (anti)commutators are block sums; LLN", ok)
    return ok


def check_commutators_have_no_scalar_part_and_anticommutators_can():
    premise("field-theory.no-canonical-commutation-relations-tower")
    ok = True
    s, mul, J, v, w, n, gam, pss = _level(2)
    b, c, phi, pi, chi = _block_fields(s, mul, J, v, w, n)
    elems = [v[0], w[1], b, c, phi, pi, mul(J, chi), GA.add(n[0], mul(J, b)), mul(w[0], n[1])]
    for x in elems:
        for y in elems:
            ok = ok and _trace(mul, J, mul(x, y)) == _trace(mul, J, mul(y, x))
            ok = ok and _trace(mul, J, _comm(mul, x, y)) == (0, 0)
    ok = ok and _trace(mul, J, GA.sc(1)) == (1, 0) and _trace(mul, J, J) == (0, 1)
    ok = ok and _trace(mul, J, _acomm(mul, w[0], v[0])) == (1, 0)
    GA.check("the span{1, J}-trace is cyclic: commutators have trace 0, the CAR anticommutator has trace 1", ok)
    return ok


def check_fluctuation_cumulants_scale_exactly_and_the_second_carries_the_form():
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    ok = True
    p1, p2 = F(3, 4), F(1, 5)
    s1, mul1, J1, v1, w1, n1, _, _ = _level(2)
    rho1 = _rho(mul1, n1, [p1, p2])
    fields1 = _block_fields(s1, mul1, J1, v1, w1, n1)
    names = {"phi": fields1[2], "pi": fields1[3], "chi": fields1[4], "n": n1[0],
             "mix": GA.add(fields1[2], GA.scal(2, mul1(n1[0], n1[1])))}
    cent = {}
    for key, x in names.items():
        mv = _omega(mul1, J1, rho1, x, 2)
        ok = ok and mv[1] == 0
        cent[key] = GA.sub(x, GA.sc(mv[0]))
    seqs = [("phi", "pi"), ("pi", "phi"), ("n", "n", "n"), ("phi", "pi", "pi", "phi"), ("mix", "chi", "pi"),
            ("mix", "mix", "mix", "mix")]
    kap = {}
    for NB in BLOCKS:
        s, mul, J, v, w, n, gam, pss = _level(2 * NB)
        rho = _rho(mul, n, [p1, p2] * NB)
        Fs = {key: GA.add(*[_copy(y, a) for a in range(NB)]) for key, y in cent.items()}
        for seq in seqs:
            ops = [Fs[key] for key in seq]

            def mom(idx, ops=ops):
                X = GA.sc(1)
                for t in idx:
                    X = mul(X, ops[t])
                return _omega(mul, J, rho, X, 2 * NB)
            kap[(NB, seq)] = _cumulant(mom, len(seq))
    for seq in seqs:
        k1 = kap[(1, seq)]
        for NB in BLOCKS:
            ok = ok and kap[(NB, seq)] == (NB * k1[0], NB * k1[1])
    # the second cumulant of (phi, pi) is (1/2) sigma = J (p1 - p2); the symmetric part vanishes
    ok = ok and kap[(1, ("phi", "pi"))] == (0, p1 - p2) and kap[(1, ("pi", "phi"))] == (0, p2 - p1)
    # the third cumulant of n is p(1 - p)(1 - 2p), nonzero: the rate N^(-1/2) is attained
    ok = ok and kap[(1, ("n", "n", "n"))] == (p1 * (1 - p1) * (1 - 2 * p1), 0) and kap[(1, ("n", "n", "n"))][0] != 0
    GA.check("ordered cumulants of block sums are N times the block cumulants; kappa_2(phi, pi) = J (p1 - p2)", ok)
    return ok


def check_the_extended_state_is_positive_blades_unitary_and_uncertainty_holds():
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    ok = True
    s, mul, J, v, w, n, gam, pss = _level(2)
    ok = ok and GA.eq(mul(J, J), GA.sc(-1)) and GA.eq(_star(J, s), GA.neg(J))
    ok = ok and all(GA.commutes(J, GA.gen(k), s) for k in range(2, 6))
    for k in range(len(s) + 1):
        for bl in combinations(range(len(s)), k):
            x = {bl: F(1)}
            ok = ok and GA.eq(mul(_star(x, s), x), GA.sc(1))
    b, c, phi, pi, chi = _block_fields(s, mul, J, v, w, n)
    for occ in ([F(3, 4), F(1, 5)], [F(1), F(0)], [F(1, 2), F(1, 3)]):
        rho = _rho(mul, n, occ)
        om = lambda X: _omega(mul, J, rho, X, 2)
        for X, Y in ((b, c), (phi, n[0]), (mul(v[0], w[1]), GA.add(n[1], chi))):
            z = GA.add(X, mul(J, Y))
            val = om(mul(_star(z, s), z))
            ok = ok and val[1] == 0 and val[0] == om(mul(_star(X, s), X))[0] + om(mul(_star(Y, s), Y))[0]
            ok = ok and val[0] >= 0
        # uncertainty: |sigma(phi, pi)|^2 <= 4 s(phi, phi) s(pi, pi), equality in the pure polarised state
        sp = om(mul(phi, phi))[0] - om(phi)[0] ** 2
        sq = om(mul(pi, pi))[0] - om(pi)[0] ** 2
        sig = om(_comm(mul, phi, pi))
        ok = ok and sig[0] == 0 and sig[1] == 2 * (occ[0] - occ[1])
        ok = ok and sp == occ[0] + occ[1] - 2 * occ[0] * occ[1] and sq == sp
        ok = ok and sig[1] ** 2 <= 4 * sp * sq
        if occ == [F(1), F(0)]:
            ok = ok and sig[1] ** 2 == 4 * sp * sq and sp == 1
    GA.check("blades are unitary; the J-linear extension is positive; sigma(phi, pi) = 2J(p1 - p2) obeys uncertainty", ok)
    return ok


def check_polarised_fluctuations_tend_to_the_fock_vacuum():
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    ok = True
    for NB in BLOCKS:
        s, mul, J, v, w, n, gam, pss = _level(2 * NB)
        rho = _rho(mul, n, [F(1), F(0)] * NB)
        b = mul(v[0], w[1])
        B = GA.add(*[_copy(b, a) for a in range(NB)])
        Bd = _star(B, s)
        for k in range(1, NB + 2):
            X, Y = GA.sc(1), GA.sc(1)
            for _ in range(k):
                X, Y = mul(X, B), mul(Y, Bd)
            for _ in range(k):
                X, Y = mul(X, Bd), mul(Y, B)
            expect = 1
            for j in range(k):
                expect *= (j + 1) * (NB - j)
            ok = ok and _omega(mul, J, rho, X, 2 * NB) == (expect, 0) and _omega(mul, J, rho, Y, 2 * NB) == (0, 0)
        phi = GA.add(B, Bd)

        def mom(idx):
            X = GA.sc(1)
            for _ in idx:
                X = mul(X, phi)
            return _omega(mul, J, rho, X, 2 * NB)
        ok = ok and _cumulant(mom, 3) == (0, 0) and _cumulant(mom, 4) == (-2 * NB, 0)
    GA.check("polarised blocks: omega(B^k B*^k) = k! N!/(N - k)!, normal order 0; kappa_4(phi) = -2N", ok)
    return ok
