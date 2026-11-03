"""synthesis.oriented-causal-towers-mirror-pair-every-window: exact checks.

check_oriented_causal: for every signature (p, q) with n = p + q <= 10, the family bit (oriented iff the
  conformal ambient has even dimension 2m with m odd), causality (min(p, q) = 1), the residue and the
  pseudoscalar square from the blade product; clauses (i) and (ii) by enumeration; for the oriented causal
  signatures of dimensions 4 and 8, clause (iii) in exact arithmetic: omega_n anticommutes with every tower
  vector and commutes with both ascended generators and every tower bivector, omega_{n+2}^2 = -1, and in the
  spacelike extension Cl(p, q+1) the volume element is central with square +1.
"""
import GA
from GA import mul, gen, sc, sig, eq, add, commutes, anticommutes
from tp_premise import premise
from fractions import Fraction as F


def omega(n):
    return {tuple(range(n)): F(1)}


def omega_sq(p, q):
    sq = sig(p, q)
    return mul(omega(p + q), omega(p + q), sq)


def oriented(p, q):
    n = p + q
    if (n + 2) % 2 == 1:
        return False                    # odd ambient dimension: one family
    m = (n + 2) // 2
    return m % 2 == 1                   # Witt pair in opposite families iff m odd


def causal(p, q):
    return min(p, q) == 1


def check_oriented_causal():
    premise("dark-matter.two-families-are-two-chiralities")
    premise("transport.sign")
    premise("odd-extensions.imported-conformal-completion")
    premise("rule2.where-obstruction-sits-commuting-square")
    premise("field-theory.where-each-lives")
    NMAX = 10
    for n in range(NMAX + 1):
        sigs = [(p, n - p) for p in range(n + 1)]
        oc = [(p, q) for (p, q) in sigs if oriented(p, q) and causal(p, q)]
        assert all(oriented(p, q) == (n % 4 == 0) for (p, q) in sigs)
        if n % 4 == 0 and n >= 4:
            assert sorted(oc) == sorted([(1, n - 1), (n - 1, 1)]) and len(oc) == 2
            assert sorted((p - q) % 8 for (p, q) in oc) == [2, 6]
        else:
            assert oc == []
        for (p, q) in sigs:
            r = (p - q) % 8
            s = omega_sq(p, q)
            assert s == sc((-1) ** (((p - q) * (p - q - 1)) // 2))          # Lemma transport.sign
            if r in (0, 4):
                assert (p, q) not in oc and s == sc(1)
                if n >= 2:                                                  # n is even here
                    sq = sig(p, q)
                    w = omega(n)
                    for i in range(n):
                        assert anticommutes(gen(i), w, sq)
                        for j in range(i + 1, n):
                            assert commutes(mul(gen(i), gen(j), sq), w, sq)
                    for sgn in (1, -1):
                        e = {(): F(1, 2), tuple(range(n)): F(sgn, 2)}
                        assert eq(mul(e, e, sq), e)
                    ep = {(): F(1, 2), tuple(range(n)): F(1, 2)}
                    em = {(): F(1, 2), tuple(range(n)): F(-1, 2)}
                    assert mul(ep, em, sq) == {} and eq(add(ep, em), sc(1))
            if (p, q) in oc:
                assert r in (2, 6)
    assert sorted(r for r in range(8) if (-r) % 8 == r) == [0, 4]
    GA.check("(i), (ii): oriented and causal force residues {2, 6} for n = 0 mod 4, n >= 4, and nothing else; "
             "residues 0 and 4 have omega^2 = +1 and central idempotents", True)

    for n in (4, 8):
        for (p, q) in [(1, n - 1), (n - 1, 1)]:
            sq = sig(p, q)
            w = omega(n)
            assert mul(w, w, sq) == sc(-1)
            amb = tuple(list(sq) + [1, -1])                                   # ascended plane e_+, e_-
            assert mul(omega(n + 2), omega(n + 2), amb) == sc(-1)
            for i in range(n):
                assert anticommutes(gen(i), w, amb)
                for j in range(i + 1, n):
                    assert commutes(mul(gen(i), gen(j), amb), w, amb)
            assert commutes(gen(n), w, amb) and commutes(gen(n + 1), w, amb)
            ext = tuple(list(sq) + [-1])                                      # spacelike extension Cl(p, q+1)
            v = omega(n + 1)
            assert mul(v, v, ext) == sc(1)
            assert all(commutes(gen(i), v, ext) for i in range(n + 1))
            assert (p - (q + 1)) % 4 == 1 and (p - q) % 4 == 2
    w4 = omega(4)
    assert mul(w4, w4, sig(1, 3)) == sc(-1)                                   # I_4 at (1, 3)
    GA.check("(iii): oriented causal towers of dimension 4 and 8 have omega_n^2 = omega_{n+2}^2 = -1, omega_n "
             "commutes with the ascended plane, and Cl(p, q+1) has a central volume element of square +1", True)
    return True
