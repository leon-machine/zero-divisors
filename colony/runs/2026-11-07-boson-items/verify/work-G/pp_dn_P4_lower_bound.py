"""synthesis.density-modes-bosonise-only-along-one-null-direction: exact checks.

Modes a_x, x = (k, alpha), k in a finite window W of Z^d, alpha a channel, each a tower plane (e, f)
(squares +1, -1) with a* = v = (e + f)/2, a = w = (e - f)/2, n = v w; two kernel generators g_1, g_2
(squares -1, -1) give J = g_1 g_2 for channel matrices with J entries. The adjoint * fixes generators
of square +1 and negates those of square -1. rho_q(M) = sum_{k, k+q in W} a*_k M a_{k+q}.

(i)   [rho_q(M), rho_q(M')*] = sum_{W cap (W-q)} a*_k M M'* a_k - sum_{W cap (W+q)} a*_k M'* M a_k
      on a 2 x 3 window (one channel) and a 2 x 2 window with two channels (M = 1, sigma_3, sigma_1);
      |E_-(q)| = |E_+(q)| for boxes and irregular windows in d = 1, 2, 3;
(ii)  uniform total occupation on the strips gives zero form: the 1+1 Dirac sea (both chiralities) on a
      window of four momenta, a sea with a rotated channel state, a bounded sea, and counting in d = 3;
(iii) the half-space sea: c min(q_1, 2N - q_1) prod_j (2N - |q_j|), by counting in d = 2, 3 and in the
      algebra on a 4 x 2 window;
(iv)  the density-current term: for h(k) = k sigma_3 (d = 1) the value is 2q exactly; the Pauli-algebra
      projector of the lower band has spin expectation -k/|k| at rational unit vectors; in d = 3 each
      strip term |k_3|/|k| lies in ((N - q)/(2N), 1], with 2q (2N)^2 strip points.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as F
import itertools
import GA
from tp_premise import premise


class Modes(object):
    """Tower planes for a list of mode labels, after the two kernel generators."""

    def __init__(self, labels):
        self.labels = list(labels)
        self.pos = {lb: 2 + 2 * i for i, lb in enumerate(self.labels)}
        self.sq = tuple([-1, -1] + [1, -1] * len(self.labels))
        self.J = GA.mul(GA.gen(0), GA.gen(1), self.sq)

    def m(self, *xs):
        out = GA.sc(1)
        for x in xs:
            out = GA.mul(out, x, self.sq)
        return out

    def cr(self, lb):
        i = self.pos[lb]
        return GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(i + 1)))

    def an(self, lb):
        i = self.pos[lb]
        return GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(i + 1)))

    def num(self, lb):
        return self.m(self.cr(lb), self.an(lb))

    def star(self, x):
        out = {}
        for b, c in x.items():
            g = len(b)
            s = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if self.sq[i] == -1)
            out[b] = c * s
        return out

    def comm(self, a, b):
        return GA.sub(self.m(a, b), self.m(b, a))

    def projector(self, filled_modes, empty_modes):
        """Rank-one projector: the creators in filled_modes occupied, those in empty_modes empty
        (together an orthonormal family of all the modes)."""
        out = GA.sc(1)
        for x in filled_modes:
            out = self.m(out, x, self.star(x))
        for x in empty_modes:
            out = self.m(out, self.star(x), x)
        return out

    def expect(self, P, X, rank_modes):
        """2^m <P X>_0 for a rank-one projector built from all m modes, scalar part only."""
        val = F(0)
        for b, c in P.items():
            if b in X:
                s, bb = GA.blade_mul(b, b, self.sq)
                val += c * X[b] * s
        return val * 2 ** rank_modes


def vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def strips(W, q):
    Ws = set(W)
    lo = [k for k in W if vadd(k, q) in Ws]           # W cap (W - q)
    hi = [k for k in W if vsub(k, q) in Ws]           # W cap (W + q)
    return lo, hi


def rho(md, W, q, M, ch):
    Ws = set(W)
    out = {}
    for k in W:
        if vadd(k, q) in Ws:
            for (a, b), c in M.items():
                out = GA.add(out, md.m(c, md.cr((k, ch[a])), md.an((vadd(k, q), ch[b]))))
    return out


def site_sum(md, ks, M, ch):
    out = {}
    for k in ks:
        for (a, b), c in M.items():
            out = GA.add(out, md.m(c, md.cr((k, ch[a])), md.an((k, ch[b]))))
    return out


def box(N, d):
    return [k for k in itertools.product(range(-N, N), repeat=d)]


def check_window_identity_any_dimension():
    """(i) the strip identity in two dimensions, with one and with two channels; |E_-| = |E_+|."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("hawking.current-commutator-exactly-edge-split")
    # one channel, 2 x 3 window
    W = [(x, y) for x in range(3) for y in range(2)]
    md = Modes([(k, 0) for k in W])
    one = {(0, 0): GA.sc(1)}
    ch = {0: 0}
    counts = []
    for q in [(1, 0), (0, 1), (1, 1), (2, 0), (2, 1), (1, -1)]:
        R = rho(md, W, q, one, ch)
        lo, hi = strips(W, q)
        lhs = md.comm(R, md.star(R))
        assert GA.eq(lhs, GA.sub(site_sum(md, lo, one, ch), site_sum(md, hi, one, ch))), q
        counts.append(len(lo))
    assert counts == [4, 3, 2, 2, 1, 2], counts
    # two channels, 2 x 2 window: M = 1, M' = sigma_3, sigma_1
    W = [(x, y) for x in range(2) for y in range(2)]
    md = Modes([(k, c) for k in W for c in (0, 1)])
    ch = {0: 0, 1: 1}
    s0 = {(0, 0): GA.sc(1), (1, 1): GA.sc(1)}
    s3 = {(0, 0): GA.sc(1), (1, 1): GA.sc(-1)}
    s1 = {(0, 1): GA.sc(1), (1, 0): GA.sc(1)}
    for q in [(1, 0), (0, 1), (1, 1)]:
        lo, hi = strips(W, q)
        for Mp in (s0, s3, s1):
            lhs = md.comm(rho(md, W, q, s0, ch), md.star(rho(md, W, q, Mp, ch)))
            assert GA.eq(lhs, GA.sub(site_sum(md, lo, Mp, ch), site_sum(md, hi, Mp, ch))), q
    # |W cap (W - q)| = |W cap (W + q)| for boxes and an irregular window
    irregular = [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (1, 2), (3, 2)]
    for Wt in (box(2, 1), box(2, 2), box(2, 3), irregular):
        d = len(Wt[0])
        for q in itertools.product(range(-3, 4), repeat=d):
            lo, hi = strips(Wt, q)
            assert len(lo) == len(hi)
    return True


def check_uniform_occupation_gives_zero_form():
    """(ii) one particle per momentum on the strips (or none) gives omega([rho_q, rho_q*]) = 0."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("hawking.current-commutator-exactly-edge-split")
    I = [(k,) for k in range(-2, 2)]
    md = Modes([(k, c) for k in I for c in (0, 1)])
    ch = {0: 0, 1: 1}
    s0 = {(0, 0): GA.sc(1), (1, 1): GA.sc(1)}
    e00 = {(0, 0): GA.sc(1)}
    # 1+1 Dirac sea of h = k sigma_3: channel 0 (h = +k) filled for k < 0, channel 1 (h = -k) for k >= 0
    dirac = [md.cr((k, 0)) if k[0] < 0 else md.cr((k, 1)) for k in I]
    P = md.projector(dirac, [md.cr((k, 1)) if k[0] < 0 else md.cr((k, 0)) for k in I])
    # a sea with a rotated channel state (3/5, 4/5) at k = -1 and k = 0: still one particle per momentum
    rot = [md.cr((k, 0)) if k[0] < -1 else
           GA.add(GA.scal(F(3, 5), md.cr((k, 0))), GA.scal(F(4, 5), md.cr((k, 1)))) if k[0] < 1 else
           md.cr((k, 1)) for k in I]
    rot_empty = [md.cr((k, 1)) if k[0] < -1 else
                 GA.add(GA.scal(F(-4, 5), md.cr((k, 0))), GA.scal(F(3, 5), md.cr((k, 1)))) if k[0] < 1 else
                 md.cr((k, 0)) for k in I]
    P2 = md.projector(rot, rot_empty)
    for q in (1, 2, 3):
        R = rho(md, I, (q,), s0, ch)
        C = md.comm(R, md.star(R))
        assert md.expect(P, C, 8) == 0 and md.expect(P2, C, 8) == 0, q
        # one chirality alone carries +-q
        R0 = rho(md, I, (q,), e00, ch)
        assert md.expect(P, md.comm(R0, md.star(R0)), 8) == min(q, 4 - q), q
    # bounded sea away from the edges in d = 3 (counting): F inside W cap (W - q) cap (W + q)
    W = box(3, 3)
    Fsea = [k for k in W if sum(x * x for x in k) <= 2]
    for q in itertools.product(range(-1, 2), repeat=3):
        lo, hi = strips(W, q)
        assert sum(1 for k in lo if k in Fsea) - sum(1 for k in hi if k in Fsea) == 0
    # uniform total occupation (one per momentum) in d = 3: value |lo| - |hi| = 0
    for q in itertools.product(range(-2, 3), repeat=3):
        lo, hi = strips(W, q)
        assert len(lo) - len(hi) == 0
    return True


def check_half_space_sea_value():
    """(iii) half-space sea {k_1 < 0}: c min(q_1, 2N - q_1) prod (2N - |q_j|); zero for q_1 = 0."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("hawking.current-commutator-exactly-edge-split")

    def formula(N, q, c):
        if q[0] < 0:
            return -formula(N, tuple(-x for x in q), c)
        out = c * min(q[0], 2 * N - q[0])
        for x in q[1:]:
            out *= max(2 * N - abs(x), 0)
        return out
    for N, d in ((2, 2), (2, 3), (3, 2), (3, 3)):
        W = box(N, d)
        for q in itertools.product(range(-2 * N + 1, 2 * N), repeat=d):
            lo, hi = strips(W, q)
            val = sum(1 for k in lo if k[0] < 0) - sum(1 for k in hi if k[0] < 0)
            assert val == formula(N, q, 1), (N, d, q, val)
    # in the algebra: window {-2..1} x {0, 1}, one channel
    W = [(x, y) for x in range(-2, 2) for y in range(2)]
    md = Modes([(k, 0) for k in W])
    one = {(0, 0): GA.sc(1)}
    ch = {0: 0}
    P = md.projector([md.cr((k, 0)) for k in W if k[0] < 0], [md.cr((k, 0)) for k in W if k[0] >= 0])
    got = []
    for q in [(1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, -1)]:
        R = rho(md, W, q, one, ch)
        got.append(md.expect(P, md.comm(R, md.star(R)), 8))
    assert got == [2, 4, 2, 0, 1, 2], got
    return True


def check_density_current_term():
    """(iv) the density-current commutator: 2q in d = 1; spin -k/|k| of the lower band; d = 3 bounds."""
    premise("tower.ladder-pairs-satisfy-car-vectors")
    premise("std-algebra.orthogonal-anticommute")
    I = [(k,) for k in range(-3, 3)]
    md = Modes([(k, c) for k in I for c in (0, 1)])
    ch = {0: 0, 1: 1}
    s0 = {(0, 0): GA.sc(1), (1, 1): GA.sc(1)}
    s3 = {(0, 0): GA.sc(1), (1, 1): GA.sc(-1)}
    P = md.projector([md.cr((k, 0)) if k[0] < 0 else md.cr((k, 1)) for k in I],
                     [md.cr((k, 1)) if k[0] < 0 else md.cr((k, 0)) for k in I])
    for q in (1, 2):
        C = md.comm(rho(md, I, (q,), s0, ch), md.star(rho(md, I, (q,), s3, ch)))
        assert md.expect(P, C, 12) == 2 * q, q
    # Pauli algebra Cl(3,0): P_- = (1 - khat)/2, khat P_- = -P_-, 2 <P_- e_i>_0 = -khat_i
    sq3 = (1, 1, 1)
    for kh in ((F(2, 3), F(1, 3), F(2, 3)), (F(3, 5), F(0), F(4, 5)), (F(-6, 7), F(2, 7), F(3, 7))):
        khat = GA.add(*[GA.scal(kh[i], GA.gen(i)) for i in range(3)])
        assert GA.eq(GA.mul(khat, khat, sq3), GA.sc(1))
        Pm = GA.scal(F(1, 2), GA.sub(GA.sc(1), khat))
        assert GA.eq(GA.mul(Pm, Pm, sq3), Pm) and GA.eq(GA.mul(khat, Pm, sq3), GA.neg(Pm))
        for i in range(3):
            assert 2 * GA.mul(Pm, GA.gen(i), sq3).get((), F(0)) == -kh[i]
    # d = 3 cube, q along axis 3: strip terms |k_3|/|k| in ((N - q)/(2N), 1]
    for N in (2, 3, 4):
        W = box(N, 3)
        for q in range(1, N):
            lo, hi = strips(W, (0, 0, q))
            E = [k for k in lo if (k[0], k[1], k[2] - q) not in set(W)] + \
                [k for k in hi if (k[0], k[1], k[2] + q) not in set(W)]
            assert len(E) == 2 * q * (2 * N) ** 2
            for k in E:
                r2 = sum(x * x for x in k)
                assert k[2] * k[2] <= r2 and 4 * N * N * k[2] * k[2] > (N - q + 1) ** 2 * r2
    return True
