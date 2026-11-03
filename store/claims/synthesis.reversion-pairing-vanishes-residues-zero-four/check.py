"""synthesis.reversion-pairing-vanishes-residues-zero-four: exact checks.

Signatures (p, q): p generators of square +1, q of square -1; n = p + q, residue r = p - q mod 8,
causal when min(p, q) = 1, the time being the minority-sign generator. w is the pseudoscalar.
T14c's definitions (obj.dark-tower-matter.ideals-fields-momentum): f = (1 + e_t e_a)/2, spinor
ideal S = Cl0(V) f; in dimension six f carries the chiral factor (1 +- w)/2 to be primitive, and
in dimension two f = (1 + w)/2 already (the other chirality is 1 - f). Momentum j(psi) = vector
part of psi e_t rev(psi); m^2 = Q(e_t) Q(P) for a total momentum P.
The check:
  (a) for every signature with n <= 8: the centre of Cl0 is spanned by 1 alone (n odd) or by 1
      and w (n even); P = (1 + w)/2 is a central idempotent of Cl0 with rev(P) P = 0 exactly when
      n is even, w^2 = +1 and rev(w) = -w; and among causal signatures this happens exactly at
      residues 0 and 4, while for n <= 64 the sign rules give the same set in every dimension;
  (b) at the nine causal signatures with 2 <= n <= 6 (both chiralities at n = 2 and 6): the
      reversion pairing rev(psi) phi vanishes on all of S x S exactly at (1,1), (1,5), (5,1);
  (c) T14c's pair law m^2 = 2 <x x^dagger>_0, x = rev(psi_1) psi_2, holds on basis pairs at
      (1,2), (2,1), (1,3), (3,1); at (1,5) and (5,1) x = 0 for every pair while the momentum sum of
      two basis constituents has m^2 = 1/4, so the law fails there.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, gen, reverse, rank_of_vectors, all_blades
from tp_premise import premise


def squares(p, q):
    return tuple([1] * p + [-1] * q)


def pseudo(n):
    return {tuple(range(n)): F(1)}


def centre_of_even(p, q):
    """Even blades commuting with every even blade (the centre is spanned by blades)."""
    n, s = p + q, squares(p, q)
    even = [B for B in all_blades(n) if len(B) % 2 == 0]
    biv = [B for B in even if len(B) == 2]
    out = []
    for B in even:
        if all(mul({B: F(1)}, {C: F(1)}, s) == mul({C: F(1)}, {B: F(1)}, s) for C in biv):
            out.append(B)
    return out


def chiral_split_swapped(p, q):
    n, s = p + q, squares(p, q)
    w = pseudo(n)
    if n % 2:
        return False
    P = scal(F(1, 2), add(sc(1), w))
    return mul(P, P, s) == P and mul(reverse(P), P, s) == {}


def sign_rule(p, q):
    """w^2 = (-1)^(n(n-1)/2 + q), rev(w) = (-1)^(n(n-1)/2) w."""
    n = p + q
    w2 = (-1) ** ((n * (n - 1) // 2 + q) % 2)
    rv = (-1) ** ((n * (n - 1) // 2) % 2)
    return n % 2 == 0 and w2 == 1 and rv == -1


def setup(p, q, chiral=0):
    n, s = p + q, squares(p, q)
    t = 0 if p == 1 else p
    a = 1 if t == 0 else 0
    f = scal(F(1, 2), add(sc(1), mul(gen(t), gen(a), s)))
    if chiral:
        f = mul(f, scal(F(1, 2), add(sc(1), scal(chiral, pseudo(n)))), s)
    assert mul(f, f, s) == f
    blades = all_blades(n)
    even = [B for B in blades if len(B) % 2 == 0]
    rows, S = [], []
    for B in even:
        g = mul({B: F(1)}, f, s)
        cand = rows + [[g.get(C, F(0)) for C in blades]]
        if g and rank_of_vectors(cand) == len(cand):
            rows, S = cand, S + [g]
    return dict(n=n, s=s, t=t, f=f, S=S)


def mom(psi, D):
    x = mul(mul(psi, gen(D["t"]), D["s"]), reverse(psi), D["s"])
    return {B: c for B, c in x.items() if len(B) == 1}


def qv(u, v, s):
    return sum(c * v.get(B, F(0)) * s[B[0]] for B, c in u.items())


def pair_m2(D, x, y):
    P = add(mom(x, D), mom(y, D))
    return D["s"][D["t"]] * qv(P, P, D["s"])


def dagger(x, D):
    s, t = D["s"], D["t"]
    et = gen(t)
    return mul(mul(et, reverse(x), s), scal(F(1, s[t]), et), s)


def pairing_identically_zero(D):
    s = D["s"]
    return all(mul(reverse(a), b, s) == {} for a in D["S"] for b in D["S"])


CAUSAL_LOW = [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (1, 4), (4, 1), (1, 5), (5, 1)]


def ideals(p, q):
    n = p + q
    if n == 2:
        D = setup(p, q)
        D2 = dict(D)
        D2["S"] = [sub(sc(1), D["f"])]
        return [D, D2]
    if n == 6:
        return [setup(p, q, chiral=1), setup(p, q, chiral=-1)]
    return [setup(p, q)]


def check_reversion_pairing_vanishes_residues_zero_four():
    premise("dark-tower-matter.where-mass-begins")
    premise("synthesis.lowest-causal-residues-zero-four-content")
    premise("synthesis.oriented-causal-towers-mirror-pair-every-window")
    premise("dark-matter.imported-eight-towers-mod-8-clock")

    # (a) centre of Cl0, the swapped chiral split, and the residues where it occurs
    swapped_causal, seen = set(), 0
    for n in range(2, 9):
        for p in range(0, n + 1):
            q = n - p
            seen += 1
            z = centre_of_even(p, q)
            assert z == ([()] if n % 2 else [(), tuple(range(n))])
            sw = chiral_split_swapped(p, q)
            assert sw == sign_rule(p, q)
            if min(p, q) == 1 and sw:
                swapped_causal.add((p - q) % 8)
            if min(p, q) == 1:
                assert sw == ((p - q) % 8 in (0, 4))
    assert swapped_causal == {0, 4} and seen == 42
    tall = 0
    for n in range(2, 65):
        for (p, q) in ((1, n - 1), (n - 1, 1)):
            assert sign_rule(p, q) == ((p - q) % 8 in (0, 4))
            tall += sign_rule(p, q)
            if (p - q) % 8 in (0, 4):
                assert n % 4 == 2
            if (p - q) % 8 in (2, 6):
                assert n % 4 == 0
    assert tall == 32
    # the reversal r -> -r fixes exactly residues zero and four
    assert {r for r in range(8) if (-r) % 8 == r} == {0, 4}

    # (b) the pairing on S x S at the nine low causal signatures
    zero_at = set()
    for (p, q) in CAUSAL_LOW:
        for D in ideals(p, q):
            if pairing_identically_zero(D):
                zero_at.add((p, q))
    assert zero_at == {(1, 1), (1, 5), (5, 1)}
    dims = {(p, q): len(ideals(p, q)[0]["S"]) for (p, q) in CAUSAL_LOW}
    assert dims == {(1, 1): 1, (1, 2): 2, (2, 1): 2, (1, 3): 4, (3, 1): 4,
                    (1, 4): 8, (4, 1): 8, (1, 5): 8, (5, 1): 8}

    # (c) T14c's pair law where it holds, and its failure in dimension six
    LAW = {(1, 2): 2, (2, 1): 2, (1, 3): 8, (3, 1): 8}
    assert {(p - q) % 8 for (p, q) in LAW} == {1, 7, 2, 6}
    for (p, q) in LAW:
        D = ideals(p, q)[0]
        S, s = D["S"], D["s"]
        nonzero = 0
        for i in range(len(S)):
            for l in range(len(S)):
                x = mul(reverse(S[i]), S[l], s)
                law = 2 * mul(x, dagger(x, D), s).get((), F(0))
                assert pair_m2(D, S[i], S[l]) == law
                nonzero += law != 0
        assert nonzero == LAW[(p, q)]
    for (p, q) in ((1, 5), (5, 1)):
        for D in ideals(p, q):
            S, s = D["S"], D["s"]
            assert all(mul(reverse(S[i]), S[l], s) == {} for i in range(8) for l in range(8))
            assert pair_m2(D, S[0], S[1]) == F(1, 4)
    return True
