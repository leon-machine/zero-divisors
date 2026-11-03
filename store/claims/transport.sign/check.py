"""transport.sign: exact checks of omega^2 for the pseudoscalar of Cl(p,q).

The claim restates primer.sign (equivalent_to plus a uses edge), so no premise() call is made: the
checks recompute the content directly.

(1) For every (p,q) with 1 <= n = p + q <= 10, omega = e_1...e_n is squared with the blade engine
and compared with (-1)^(n(n-1)/2) (-1)^q and with (-1)^((p-q)(p-q-1)/2).
(2) The sign count behind the first form, done in GA: reversing omega gives
(-1)^(n(n-1)/2) omega, and omega times its reverse is the product of the Q(e_i), (-1)^q.
(3) The dependence on p - q alone: omega^2 is unchanged by (p,q) -> (p+1,q+1), and the residues
of p - q mod 4 with omega^2 = +1 are exactly {0, 1} (each residue class is reached in the range).
"""
from fractions import Fraction as F

import GA

NMAX = 10


def omega(n):
    return {tuple(range(n)): F(1)}


def omega_sq(p, q):
    n = p + q
    return GA.mul(omega(n), omega(n), GA.sig(p, q))


def check_omega_square_closed_forms():
    ok = True
    count = 0
    for n in range(1, NMAX + 1):
        for p in range(n + 1):
            q = n - p
            s = omega_sq(p, q)
            a = (-1) ** (n * (n - 1) // 2) * (-1) ** q
            b = (-1) ** ((p - q) * (p - q - 1) // 2)
            ok = ok and s == {(): F(a)} and s == {(): F(b)}
            count += 1
    ok = ok and count == 65
    GA.check("omega^2 = (-1)^(n(n-1)/2)(-1)^q = (-1)^((p-q)(p-q-1)/2), all (p,q), n <= 10", ok)
    return ok


def check_reversal_sign_count():
    ok = True
    for n in range(1, NMAX + 1):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p, q)
            w = omega(n)
            rev = GA.reverse(w)
            ok = ok and GA.eq(rev, GA.scal((-1) ** (n * (n - 1) // 2), w))
            prod_q = F(1)
            for s in sq:
                prod_q *= s
            ok = ok and GA.eq(GA.mul(w, rev, sq), GA.sc(prod_q)) and prod_q == (-1) ** q
            # omega^2 = (sign of reversal) * (omega reverse(omega))
            ok = ok and GA.eq(GA.mul(w, w, sq),
                              GA.scal((-1) ** (n * (n - 1) // 2), GA.mul(w, rev, sq)))
    GA.check("reverse(omega) = (-1)^(n(n-1)/2) omega and omega reverse(omega) = (-1)^q, n <= 10", ok)
    return ok


def check_depends_only_on_p_minus_q():
    ok = True
    plus_residues = set()
    minus_residues = set()
    for n in range(1, NMAX - 1):
        for p in range(n + 1):
            q = n - p
            s = omega_sq(p, q)[()]
            ok = ok and omega_sq(p + 1, q + 1)[()] == s
            (plus_residues if s == 1 else minus_residues).add((p - q) % 4)
    ok = ok and plus_residues == {0, 1} and minus_residues == {2, 3}
    GA.check("omega^2 depends on p - q only, and is +1 exactly for p - q = 0, 1 mod 4", ok)
    return ok
