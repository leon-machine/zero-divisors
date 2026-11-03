"""odd-extensions.translation-bivectors-frozen-point: exact checks.

The rung as GA's Cl(2,4) (e_0 +1; e_1, e_2, e_3 -1; e_4 +1; e_5 -1). Frozen point I = c e_4 + d e_5,
Q(I) = Lambda/3 = c^2 - d^2, Stelle-West vector V = (1/Q(I))(d e_4 + c e_5) (orthogonal to I and the frame,
Q(V) = -3/Lambda). Samples with |Q(V)| a rational square, so that the unit direction u = V/|V| is exact:
Lambda/3 = 4 (Lambda > 0) and Lambda/3 = -1/4, -4/9 (Lambda < 0).
(1) u^2 = -1 for Lambda > 0 and +1 for Lambda < 0; {e_0..e_3, u} has signature (1,4), respectively (2,3), and its
    32 products are independent (Cl(I^perp) is the space or the time extension).
(2) The translation bivectors t_mu = e_mu u pairwise anticommute, and their squares have the signature (1,3) for
    Lambda > 0 and (3,1) for Lambda < 0; their 16 products are independent, so they generate Cl(1,3), respectively
    a copy of Cl(3,1); for Lambda < 0 the frame e_0..e_3 itself generates the (1,3) algebra.
(3) Contraction: t_mu / ell has square t_mu^2 / ell^2 with the same sign for sample ell, so the Clifford type of the
    translation algebra is unchanged as ell grows.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
SAMPLES = [(F(5, 2), F(3, 2), F(1, 2)), (F(0), F(1, 2), F(2)), (F(0), F(2, 3), F(3, 2))]   # (c, d, |V|)
ELLS = [F(2), F(7, 3), F(10)]
FRAME = [GA.gen(i) for i in range(4)]


def prods(gs):
    out = []
    for k in range(len(gs) + 1):
        for idx in combinations(range(len(gs)), k):
            x = {(): F(1)}
            for t in idx:
                x = GA.mul(x, gs[t], SQ)
            out.append(x)
    return out


def rank_mv(xs):
    keys = sorted({b for x in xs for b in x})
    return GA.rank_of_vectors([[x.get(k, F(0)) for k in keys] for x in xs])


def unit_sw(c, d, norm):
    qi = c * c - d * d
    V = GA.scal(1 / qi, {(4,): d, (5,): c})
    return qi, V, GA.scal(1 / norm, V)


def check_extension_by_sign_of_lambda():
    premise("odd-extensions.imported-frozen-point")
    ok = True
    for c, d, norm in SAMPLES:
        qi, V, u = unit_sw(c, d, norm)
        I = {(4,): c, (5,): d} if c else {(5,): d}
        ok = ok and GA.dot(V, V, SQ) == -1 / qi and GA.dot(I, V, SQ) == 0
        ok = ok and GA.mul(u, u, SQ) == GA.sc(-1 if qi > 0 else 1)
        G = [[GA.dot(a, b, SQ) for b in FRAME + [u]] for a in FRAME + [u]]
        ok = ok and GA.congruence_signature(G) == ((1, 4, 0) if qi > 0 else (2, 3, 0))
        ok = ok and rank_mv(prods(FRAME + [u])) == 32
    GA.check("Cl(I^perp) = Cl(1,4) for Lambda > 0 and Cl(2,3) for Lambda < 0", ok)
    return ok


def check_translation_bivectors_generate():
    premise("odd-extensions.imported-frozen-point")
    premise("odd-extensions.mirror-inside-complexified-extension-absent-doubled")
    ok = True
    for c, d, norm in SAMPLES:
        qi, _, u = unit_sw(c, d, norm)
        t = [GA.mul(e, u, SQ) for e in FRAME]
        ok = ok and all(GA.anticommutes(a, b, SQ) for a, b in combinations(t, 2))
        sq = [GA.mul(x, x, SQ) for x in t]
        ok = ok and all(set(s) == {()} for s in sq)
        pos = sum(1 for s in sq if s[()] == 1)
        neg = sum(1 for s in sq if s[()] == -1)
        ok = ok and (pos, neg) == ((1, 3) if qi > 0 else (3, 1))
        ok = ok and rank_mv(prods(t)) == 16
        if qi < 0:
            fsq = [GA.mul(e, e, SQ)[()] for e in FRAME]
            ok = ok and sorted(fsq) == [-1, -1, -1, 1] and rank_mv(prods(FRAME)) == 16
    GA.check("translation bivectors e_mu u generate Cl(1,3) (Lambda > 0) or Cl(3,1) (Lambda < 0)", ok)
    return ok


def check_contraction_keeps_type():
    premise("odd-extensions.imported-frozen-point")
    ok = True
    for c, d, norm in SAMPLES:
        qi, _, u = unit_sw(c, d, norm)
        t = [GA.mul(e, u, SQ) for e in FRAME]
        base = [GA.mul(x, x, SQ)[()] for x in t]
        for ell in ELLS:
            s = [GA.mul(GA.scal(1 / ell, x), GA.scal(1 / ell, x), SQ)[()] for x in t]
            ok = ok and all(s[i] * ell * ell == base[i] for i in range(4))
            ok = ok and all((s[i] > 0) == (base[i] > 0) for i in range(4))
        ok = ok and sum(1 for b in base if b > 0) == (1 if qi > 0 else 3)
    GA.check("rescaling the translation generators by 1/ell keeps the signs of their squares", ok)
    return ok
