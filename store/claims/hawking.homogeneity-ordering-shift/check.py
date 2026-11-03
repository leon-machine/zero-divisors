"""hawking.homogeneity-ordering-shift: exact checks.

Polynomials in n complex variables Z^0..Z^{n-1} (dicts exponent tuple -> Fraction), with Z^mu acting by
multiplication and Zbar_nu = -hbar d/dZ^nu, at exact sample values of hbar. A first-order differential
operator with coefficients of degree <= 1 is fixed by its values on monomials of degree <= 1; all monomials
of degree <= 4 are used.
(a) The realisation satisfies the palatial sign [Z^mu, Zbar_nu] = +hbar delta^mu_nu.
(b) q(id) = (1/2) sum (Z^a Zbar_a + Zbar_a Z^a) equals -hbar(Upsilon + 2) for n = 4 (twistor space C^4),
    and -hbar(Upsilon + n/2) for n = 1..4: the offset is one half per complex dimension.
(c) On a homogeneous polynomial of degree h, s = q(id)/2 has eigenvalue -(h + 2) hbar/2, so the helicity
    s hbar occurs iff h = -2s - 2 (table s = 1, -1, 2, -2, 1/2, -1/2 gives h = -4, 0, -6, 2, -3, -1); an
    inhomogeneous sum is not an eigenfunction.
(d) Without the symmetric-ordering shift (normal ordering sum Z^a Zbar_a) the operator is -hbar Upsilon and
    the offset vanishes (h = -2s); the opposite-sign realisation Zbar = +hbar d/dZ flips it to h = 2s + 2.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

HBARS = [F(1), F(3, 2), F(-2, 7)]
TWISTOR_N = 4                 # twistor space C^4: (b) at n = 4 on all monomials of degree <= 4
TWISTOR_MAXDEG = 4
DIMS = range(1, 5)            # (b) for n = 1..4 on all monomials of degree <= DIMS_MAXDEG
DIMS_MAXDEG = 3


def unit_mono(e):
    """The monomial Z^e with coefficient 1."""
    return {e: F(1)}


def monos(n, maxdeg):
    return [e for e in product(range(maxdeg + 1), repeat=n) if sum(e) <= maxdeg]


def padd(f, g, c=F(1)):
    out = dict(f)
    for k, v in g.items():
        out[k] = out.get(k, F(0)) + c * v
    return {k: v for k, v in out.items() if v != 0}


def mulZ(a, f):
    out = {}
    for e, c in f.items():
        e2 = list(e)
        e2[a] += 1
        out[tuple(e2)] = out.get(tuple(e2), F(0)) + c
    return out


def dZ(a, f):
    out = {}
    for e, c in f.items():
        if e[a]:
            e2 = list(e)
            e2[a] -= 1
            out[tuple(e2)] = out.get(tuple(e2), F(0)) + e[a] * c
    return out


def Zbar(a, f, hbar, sign=-1):
    return {k: sign * hbar * v for k, v in dZ(a, f).items()}


def q_id(f, n, hbar, sign=-1):
    out = {}
    for a in range(n):
        out = padd(out, mulZ(a, Zbar(a, f, hbar, sign)), F(1, 2))
        out = padd(out, Zbar(a, mulZ(a, f), hbar, sign), F(1, 2))
    return out


def euler(f, n):
    out = {}
    for a in range(n):
        out = padd(out, mulZ(a, dZ(a, f)))
    return out


def check_palatial_sign_of_realisation():
    premise("hawking.imported-twistor-storey-ordering-shift")
    n = 4
    for hbar in HBARS:
        for e in monos(n, 3):
            f = {e: F(1)}
            for mu in range(n):
                for nu in range(n):
                    c = padd(mulZ(mu, Zbar(nu, f, hbar)), Zbar(nu, mulZ(mu, f), hbar), F(-1))
                    assert c == ({e: hbar} if mu == nu else {})
    return True


def check_charge_is_minus_hbar_euler_plus_two():
    premise("hawking.imported-twistor-storey-ordering-shift")
    for hbar in HBARS:
        for e in monos(TWISTOR_N, TWISTOR_MAXDEG):
            f = unit_mono(e)
            q = q_id(f, TWISTOR_N, hbar)
            assert q == padd({k: -hbar * v for k, v in euler(f, TWISTOR_N).items()}, f, -2 * hbar)
        for n in DIMS:
            for e in monos(n, DIMS_MAXDEG):
                f = unit_mono(e)
                rhs = padd({k: -hbar * v for k, v in euler(f, n).items()}, f, -hbar * F(n, 2))
                assert q_id(f, n, hbar) == rhs
    return True


def check_homogeneity_iff_helicity():
    premise("hawking.imported-twistor-storey-ordering-shift")
    hbar = HBARS[1]
    for h in range(0, 5):
        hom = [e for e in monos(4, h) if sum(e) == h]
        f = {}
        for i, e in enumerate(hom):
            f[e] = F(i + 1)
        sf = {k: v / 2 for k, v in q_id(f, 4, hbar).items()}
        lam = -F(h + 2, 2) * hbar
        assert sf == {k: lam * v for k, v in f.items()}
        s = lam / hbar
        assert h == -2 * s - 2
    table = {F(1): -4, F(-1): 0, F(2): -6, F(-2): 2, F(1, 2): -3, F(-1, 2): -1}
    for s, h in table.items():
        assert -2 * s - 2 == h
    g = {(1, 0, 0, 0): F(1), (0, 0, 0, 0): F(1)}
    sg = {k: v / 2 for k, v in q_id(g, 4, hbar).items()}
    assert GA.rank_of_vectors([[sg.get(k, F(0)) for k in sorted(g)], [g[k] for k in sorted(g)]]) == 2
    return True


def check_offset_is_the_ordering_shift():
    premise("hawking.imported-twistor-storey-ordering-shift")
    for hbar in HBARS:
        for e in monos(4, 3):
            f = {e: F(1)}
            normal = {}
            for a in range(4):
                normal = padd(normal, mulZ(a, Zbar(a, f, hbar)))
            assert normal == {k: -hbar * v for k, v in euler(f, 4).items()}
            shift = padd(q_id(f, 4, hbar), normal, F(-1))
            assert shift == {e: -2 * hbar}
            # opposite realisation Zbar = +hbar d/dZ: q(id) = +hbar(Upsilon + 2), so h = 2s + 2
            flipped = q_id(f, 4, hbar, sign=1)
            assert flipped == padd({k: hbar * v for k, v in euler(f, 4).items()}, f, 2 * hbar)
    return True
