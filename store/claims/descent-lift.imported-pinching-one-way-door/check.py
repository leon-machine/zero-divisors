"""descent-lift.imported-pinching-one-way-door: exact checks in Cl(p+1, q+1) for the six signatures with
p + q <= 2 (GA blade engine), plus the block count for p + q <= 3.

(1) f, f^* are null with f f^* + f^* f = 1, P = f^* f is idempotent; the pinching E(x) = PxP + (1-P)x(1-P)
    is idempotent on every blade, E(1) = 1, its image has dimension 2^(n+1) = 2 dim A and equals the
    commutant of P (computed as the kernel of x -> xP - Px, of the same dimension, and fixed pointwise);
    E(c x c') = c E(x) c' for c, c' in the basis A + A f f^* of the commutant and x every blade.
(2) The kernel: E vanishes on A f and A f^*, which together have dimension 2^(n+1) = dim B - dim(image),
    so ker E = A f^* + A f, the ladder sector; E(f) = E(f^*) = 0.
(3) No unital homomorphism B -> A: every Wedderburn block of B has dimension 4 dim A (A simple) or
    2 dim A (A split), larger than dim A, for every p + q <= 3; a unital homomorphism would embed a block.
    The pinching is not multiplicative: E(f f^*) = f f^* while E(f) E(f^*) = 0, and the corner read-out
    D(x) = PxP has the defect D(xy) - D(x)D(y) = P x (1 - P) y P, nonzero at x = f^*, y = f.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]


def setup(p, q):
    """B = Cl(p+1, q+1): A's generators 0..n-1, e+ = n (square +1), e- = n+1 (square -1)."""
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    f = GA.scal(F(1, 2), GA.add(ep, em))
    fs = GA.scal(F(1, 2), GA.sub(ep, em))
    P = GA.mul(fs, f, sq)
    return n, sq, f, fs, P


def mul(sq, *xs):
    out = GA.sc(1)
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def pinch(x, P, sq):
    Q = GA.sub(GA.sc(1), P)
    return GA.add(mul(sq, P, x, P), mul(sq, Q, x, Q))


def rank(elems, m):
    rows = [GA.basis_vector_of(x, GA.all_blades(m)) for x in elems if x]
    return GA.rank_of_vectors(rows) if rows else 0


def blocks(sq, m):
    """Dimensions of the Wedderburn blocks of the (nondegenerate) Clifford algebra with squares sq."""
    cb = [b for b in GA.all_blades(m) if all(GA.commutes(GA.gen(i), {b: F(1)}, sq) for i in range(m))]
    if cb == [()]:
        return [2 ** m]
    om = {tuple(range(m)): F(1)}
    if GA.eq(GA.mul(om, om, sq), GA.sc(-1)):
        return [2 ** m]
    return [rank([GA.mul(GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(s, om))), {b: F(1)}, sq)
                  for b in GA.all_blades(m)], m) for s in (1, -1)]


def comm_basis(n, sq, f, fs):
    """A + A f f^*: the A blades and their products with f f^*."""
    ffs = GA.mul(f, fs, sq)
    base = [{b: F(1)} for b in GA.all_blades(n)]
    return base + [GA.mul(a, ffs, sq) for a in base]


def check_pinching_is_conditional_expectation():
    premise("transport.pinching-kernel")
    ok = True
    for (p, q) in SIGS:
        n, sq, f, fs, P = setup(p, q)
        m_ = n + 2
        ok = ok and GA.mul(f, f, sq) == {} and GA.mul(fs, fs, sq) == {}
        ok = ok and GA.add(GA.mul(f, fs, sq), GA.mul(fs, f, sq)) == GA.sc(1)
        ok = ok and GA.mul(P, P, sq) == P
        imgs = []
        for b in GA.all_blades(m_):
            x = {b: F(1)}
            Ex = pinch(x, P, sq)
            ok = ok and pinch(Ex, P, sq) == Ex and GA.commutes(Ex, P, sq)
            imgs.append(Ex)
        ok = ok and pinch(GA.sc(1), P, sq) == GA.sc(1)
        ok = ok and rank(imgs, m_) == 2 ** (n + 1)
        comm = [GA.sub(GA.mul({b: F(1)}, P, sq), GA.mul(P, {b: F(1)}, sq)) for b in GA.all_blades(m_)]
        ok = ok and 2 ** m_ - rank(comm, m_) == 2 ** (n + 1)
        C = comm_basis(n, sq, f, fs)
        ok = ok and rank(C, m_) == 2 ** (n + 1) and all(pinch(c, P, sq) == c for c in C)
        if n <= 1:
            for c in C:
                for c2 in C:
                    for b in GA.all_blades(m_):
                        x = {b: F(1)}
                        ok = ok and pinch(mul(sq, c, x, c2), P, sq) == mul(sq, c, pinch(x, P, sq), c2)
        else:
            for c in C[:4]:
                for c2 in C[-4:]:
                    for b in GA.all_blades(m_):
                        x = {b: F(1)}
                        ok = ok and pinch(mul(sq, c, x, c2), P, sq) == mul(sq, c, pinch(x, P, sq), c2)
    GA.check("pinching: idempotent conditional expectation onto the commutant of P (dimension 2 dim A)", ok)
    return ok


def check_kernel_is_ladder_sector():
    premise("transport.pinching-kernel")
    ok = True
    for (p, q) in SIGS:
        n, sq, f, fs, P = setup(p, q)
        m_ = n + 2
        ladder = [GA.mul({b: F(1)}, y, sq) for b in GA.all_blades(n) for y in (f, fs)]
        ok = ok and all(pinch(x, P, sq) == {} for x in ladder)
        ok = ok and rank(ladder, m_) == 2 ** (n + 1)
        imgs = [pinch({b: F(1)}, P, sq) for b in GA.all_blades(m_)]
        ok = ok and 2 ** m_ - rank(imgs, m_) == 2 ** (n + 1)
        ok = ok and pinch(f, P, sq) == {} and pinch(fs, P, sq) == {}
    GA.check("ker E = A f^* + A f, of dimension 2 dim A; E(f) = E(f^*) = 0", ok)
    return ok


def check_no_return_homomorphism():
    premise("transport.door-one-way")
    ok = True
    nsplit = 0
    for n in range(0, 4):
        for p in range(n + 1):
            q = n - p
            sqB = GA.sig(p, q) + (1, -1)
            bl = blocks(sqB, n + 2)
            if len(bl) == 2:
                nsplit += 1
                ok = ok and bl == [2 * 2 ** n, 2 * 2 ** n]
            else:
                ok = ok and bl == [4 * 2 ** n]
            ok = ok and min(bl) > 2 ** n
    ok = ok and nsplit == 3                     # (1,0), (2,1), (0,3)
    for (p, q) in SIGS:
        n, sq, f, fs, P = setup(p, q)
        ok = ok and pinch(GA.mul(f, fs, sq), P, sq) == GA.mul(f, fs, sq)
        ok = ok and GA.mul(pinch(f, P, sq), pinch(fs, P, sq), sq) == {}
        Q = GA.sub(GA.sc(1), P)
        x, y = fs, f
        D = lambda z: mul(sq, P, z, P)
        defect = GA.sub(D(GA.mul(x, y, sq)), GA.mul(D(x), D(y), sq))
        ok = ok and defect == mul(sq, P, x, Q, y, P) and defect == P
    GA.check("blocks of B exceed dim A (no unital B -> A); the pinching and the corner read-out are not multiplicative", ok)
    return ok
