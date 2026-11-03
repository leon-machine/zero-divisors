#!/usr/bin/env python3
"""
verify_T14a.py (formerly verify_T14_ext.py, briefly verify_T14a.py): exact-arithmetic verification of the computational
identities of the companion note to T14, "One Dimension at a Time: The Odd
Extensions of the Oriented Towers" (Transport Papers, companion note to T14),
v1.8.

Imports the series' shared exact-arithmetic library GA.py.  Everything is
exact rational arithmetic on basis blades; no floating point anywhere.

Parts: A the volume element of an odd extension (central, and the sign of
its square by the parity of q); B doubling and complexification of the four
single extensions of the oriented pair; C where the mirror sits (the
generated subalgebra, the even subalgebra, their intersection, the
Wick-rotated generators); D the rung's even subalgebra is the anti-de Sitter
algebra; E the clock (residues of the four extensions and of the odd towers'
representatives), the centres that separate reversed pairs, and the
sign-flip paths at dimension four; F the frozen point as the ascent's pair
(v1.1); G the transport run on Cl(1,3;1) and what it leaves free (v1.2);
H the dilation gauge and the two towers in one curved universe (v1.3);
I the Lambda line as a tame wall in the sheaf paper's sense (v1.4);
G7-G8 the null-pair dictionary (v1.6); A5-A6 and I9, generality checks
added at review (v1.7); gauges and ordering adjusted at re-review (v1.8).
Eighty-six checks.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
import GA as g

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

NCHECKS = [0]
_check = g.check


def counted_check(label, ok):
    NCHECKS[0] += 1
    _check(label, ok)


g.check = counted_check


def volume(n, sq):
    x = g.sc(1)
    for i in range(n):
        x = g.mul(x, g.gen(i), sq)
    return x


def central(x, n, sq):
    return all(g.commutes(x, g.gen(i), sq) for i in range(n))


def span_dim(elems, n):
    bl = g.all_blades(n)
    return g.rank_of_vectors([g.basis_vector_of(e, bl) for e in elems])


def generated(gens, sq):
    """All ordered products of subsets of a pairwise anticommuting generating
    set: a spanning set of the subalgebra they generate."""
    out = [g.sc(1)]
    for k in range(1, len(gens) + 1):
        for S in combinations(range(len(gens)), k):
            x = g.sc(1)
            for i in S:
                x = g.mul(x, gens[i], sq)
            out.append(x)
    return out


def square_scalar(x, sq):
    y = g.mul(x, x, sq)
    assert set(y.keys()) <= {()}, "square is not a scalar"
    return y.get((), F(0))


def even_part(elems):
    return [x for x in elems if all(len(b) % 2 == 0 for b in x)]


def residue(p, q):
    return (p - q) % 8


# The four single extensions of the oriented pair, in the series' convention
# (time = plus, this world (1,3), residue 6; the mirror (3,1), residue 2).
# The added generator is listed LAST, so the four-dimensional generators are
# indices 0..3 and the new one is index 4.
EXT = {
    "Cl(1,4) = this world + space": g.sig(1, 4),                       # (+,-,-,-,-)
    "Cl(2,3) = this world + time":  (1, -1, -1, -1, 1),                # (+,-,-,-,+)
    "Cl(3,2) = mirror + space":     (-1, 1, 1, 1, -1),                 # (-,+,+,+,-)
    "Cl(4,1) = mirror + time":      (-1, 1, 1, 1, 1),                  # (-,+,+,+,+)
}
PQ = {
    "Cl(1,4) = this world + space": (1, 4),
    "Cl(2,3) = this world + time":  (2, 3),
    "Cl(3,2) = mirror + space":     (3, 2),
    "Cl(4,1) = mirror + time":      (4, 1),
}

# ---------------------------------------------------------------------------
# Part A: the volume element of an odd extension
# ---------------------------------------------------------------------------
print("Part A: the volume element in odd dimension")

# A1: omega is central and omega^2 = (-1)^(n(n-1)/2 + q) on every diagonal
# signature of odd dimension up to seven (all q, one canonical ordering per (n, q)).
okc, oks = True, True
for n in (1, 3, 5, 7):
    for q in range(n + 1):
        sq = g.sig(n - q, q)
        w = volume(n, sq)
        okc = okc and central(w, n, sq)
        oks = oks and square_scalar(w, sq) == F(-1) ** ((n * (n - 1)) // 2 + q)
g.check("A1  omega central in every odd dimension 1,3,5,7 (all q)", okc)
g.check("A2  omega^2 = (-1)^(n(n-1)/2 + q) in every odd dimension 1,3,5,7 (all q)", oks)

# A3: at n = 5 the sign is (-1)^q: time-sign generator keeps q, space-sign
# generator changes it; from q odd (both oriented shadows) time complexifies
# and space doubles.
signs = {name: square_scalar(volume(5, sq), sq) for name, sq in EXT.items()}
g.check("A3  omega^2 = +1 for the two space extensions, -1 for the two time extensions",
        signs["Cl(1,4) = this world + space"] == 1 and signs["Cl(3,2) = mirror + space"] == 1
        and signs["Cl(2,3) = this world + time"] == -1 and signs["Cl(4,1) = mirror + time"] == -1)

# A4: omega is not in the even subalgebra (it is odd), and omega anticommutes
# with nothing: it commutes with the added generator too.
g.check("A4  omega commutes with the added generator in all four extensions",
        all(g.commutes(volume(5, sq), g.gen(4), sq) for sq in EXT.values()))

# A5 (v1.7): Theorem 2.3 in general: over every odd signature of dimension
# three and five, (i) with its specific sign assignment (P_+ e_n = +s P_+ omega',
# P_- e_n = -s P_- omega', s = e_n^2 = omega'^2) when omega^2 = +1, (ii) the
# spanning by Cl^0 + omega Cl^0 when omega^2 = -1, and (iii) the squares of
# e_i e_n; and the centre has dimension two over every odd signature of
# dimension at most five and one over every even signature of dimension at
# most six.
def centre_dim_general(n, sq):
    bl = g.all_blades(n)
    rows = []
    for b in bl:
        x = {b: F(1)}
        row = []
        for i in range(n):
            comm = g.sub(g.mul(x, g.gen(i), sq), g.mul(g.gen(i), x, sq))
            row.extend(g.basis_vector_of(comm, bl))
        rows.append(row)
    return len(bl) - g.rank_of_vectors([list(r) for r in zip(*rows)])
okA5 = True
for n in (3, 5):
    for q in range(n + 1):
        sq = g.sig(n - q, q)
        w = volume(n, sq); wp = volume(n - 1, sq); en = g.gen(n - 1)
        full = generated([g.gen(i) for i in range(n)], sq)
        ev = even_part(full)
        T = [g.mul(g.gen(i), en, sq) for i in range(n - 1)]
        # (iii): e_i e_n square to e_i^2 if e_n^2 = -1, to -e_i^2 if +1, and anticommute
        sgn = sq[n - 1]
        okA5 = okA5 and all(square_scalar(T[i], sq) == -sgn * sq[i] for i in range(n - 1))             and all(g.anticommutes(T[i], T[j], sq) for i in range(n - 1) for j in range(i + 1, n - 1))
        if square_scalar(w, sq) == 1:
            P = g.scal(F(1, 2), g.add(g.sc(1), w)); M = g.scal(F(1, 2), g.sub(g.sc(1), w))
            sval = square_scalar(en, sq)
            okA5 = okA5 and square_scalar(wp, sq) == sval                 and g.eq(g.mul(P, en, sq), g.scal(sval, g.mul(P, wp, sq)))                 and g.eq(g.mul(M, en, sq), g.scal(-sval, g.mul(M, wp, sq)))                 and span_dim([g.mul(P, x, sq) for x in full], n) == 2 ** (n - 1)
        else:
            okA5 = okA5 and span_dim(ev + [g.mul(w, x, sq) for x in ev], n) == 2 ** n
okC = all(centre_dim_general(n, g.sig(n - q, q)) == 2 for n in (1, 3, 5) for q in range(n + 1))     and all(centre_dim_general(n, g.sig(n - q, q)) == 1 for n in (2, 4, 6) for q in range(n + 1))
g.check("A5  Theorem 2.3(iii) and the identities behind (i) and (ii), with the specific signs, over every odd signature of dimensions 3 and 5", okA5)
g.check("A6  centre dimension 2 over every odd signature (n <= 5) and 1 over every even signature (n <= 6)", okC)

# ---------------------------------------------------------------------------
# Part B: doubling and complexification
# ---------------------------------------------------------------------------
print("Part B: doubling and complexification")

for name, sq in EXT.items():
    n = 5
    w = volume(n, sq)
    full = generated([g.gen(i) for i in range(n)], sq)
    base = generated([g.gen(i) for i in range(4)], sq)      # the four-dimensional shadow
    ev = even_part(full)
    tag = name.split(" =")[0]
    if square_scalar(w, sq) == 1:
        P = g.scal(F(1, 2), g.add(g.sc(1), w))
        M = g.scal(F(1, 2), g.sub(g.sc(1), w))
        idem = g.eq(g.mul(P, P, sq), P) and g.eq(g.mul(M, M, sq), M) and g.is_zero(g.mul(P, M, sq)) \
            and g.eq(g.add(P, M), g.sc(1))
        ideal_P = [g.mul(P, x, sq) for x in full]
        ideal_M = [g.mul(M, x, sq) for x in full]
        g.check("B   %s: (1 +/- omega)/2 are complementary central idempotents" % tag,
                idem and central(P, n, sq))
        g.check("B   %s: the two ideals have dimension 16 + 16 = 32" % tag,
                span_dim(ideal_P, n) == 16 and span_dim(ideal_M, n) == 16
                and span_dim(ideal_P + ideal_M, n) == 32)
        # on each ideal the added generator is +/- the four-dimensional pseudoscalar
        I4 = volume(4, sq)
        e5 = g.gen(4)
        sval = square_scalar(e5, sq)     # = omega'^2 when omega^2 = +1
        g.check("B   %s: e_5 = +s I_4 on the (1+omega)/2 ideal and -s I_4 on the other, s = e_5^2" % tag,
                square_scalar(I4, sq) == sval
                and g.eq(g.mul(P, e5, sq), g.scal(sval, g.mul(P, I4, sq)))
                and g.eq(g.mul(M, e5, sq), g.scal(-sval, g.mul(M, I4, sq))))
        # the even subalgebra and the shadow coincide as subspaces
        g.check("B   %s: the shadow (dim 16) meets the even subalgebra (dim 16) exactly in its even part (dim 8)" % tag,
                span_dim(ev, n) == 16 and span_dim(base, n) == 16 and span_dim(ev + base, n) == 24
                and span_dim(even_part(base) + ev, n) == 16)
    else:
        both = base + [g.mul(w, x, sq) for x in base]
        g.check("B   %s: Cl(p,q) + omega Cl(p,q) spans all 32 dimensions (complexification)" % tag,
                span_dim(base, n) == 16 and span_dim(both, n) == 32)
        g.check("B   %s: omega^2 = -1 and omega is central (a complex unit)" % tag,
                square_scalar(w, sq) == -1 and central(w, n, sq))

# ---------------------------------------------------------------------------
# Part C: where the mirror sits
# ---------------------------------------------------------------------------
print("Part C: where the mirror sits")

def signature_of_generators(gens, sq):
    sqs = [square_scalar(x, sq) for x in gens]
    anti = all(g.anticommutes(gens[i], gens[j], sq) for i in range(len(gens)) for j in range(i + 1, len(gens)))
    return sqs, anti

expected_T = {
    "Cl(1,4) = this world + space": [1, -1, -1, -1],    # generate Cl(1,3): this world
    "Cl(2,3) = this world + time":  [-1, 1, 1, 1],      # generate Cl(3,1): the mirror
    "Cl(3,2) = mirror + space":     [-1, 1, 1, 1],      # generate Cl(3,1): the mirror
    "Cl(4,1) = mirror + time":      [1, -1, -1, -1],    # generate Cl(1,3): this world
}
for name, sq in EXT.items():
    n = 5
    tag = name.split(" =")[0]
    e5 = g.gen(4)
    T = [g.mul(g.gen(i), e5, sq) for i in range(4)]          # the translation bivectors e_mu e_5
    sqs, anti = signature_of_generators(T, sq)
    g.check("C   %s: e_mu e_5 anticommute pairwise and square to %s" % (tag, expected_T[name]),
            anti and sqs == [F(s) for s in expected_T[name]])
    genT = generated(T, sq)
    full = generated([g.gen(i) for i in range(n)], sq)
    ev = even_part(full)
    g.check("C   %s: <e_mu e_5> is the whole even subalgebra (dim 16)" % tag,
            span_dim(genT, n) == 16 and span_dim(genT + ev, n) == 16)
    base = generated([g.gen(i) for i in range(4)], sq)
    g.check("C   %s: <e_mu> has dim 16 and meets the even subalgebra in dim 8" % tag,
            span_dim(base, n) == 16 and span_dim(base + ev, n) == 24)
    # the generators omega e_mu (omega central) square to omega^2 e_mu^2:
    # in a complexified extension they generate the reversed signature (the
    # Wick rotation), in a doubled one a second copy of the same signature
    w = volume(n, sq)
    w2 = square_scalar(w, sq)
    W = [g.mul(w, g.gen(i), sq) for i in range(4)]
    sqsW, antiW = signature_of_generators(W, sq)
    g.check("C   %s: omega e_mu anticommute and square to omega^2 (e_mu)^2 = %s" % (tag, [int(w2 * s) for s in sq[:4]]),
            antiW and sqsW == [w2 * F(s) for s in sq[:4]])

# C5: in Cl(2,3) the even subalgebra Cl(3,1) and the generated Cl(1,3) have
# non-isomorphic types (imported, T14 Thm 3.4); what the script adds is that
# the intersection is exactly the even part of the shadow, Cl^0(1,3).
sq = EXT["Cl(2,3) = this world + time"]
base = generated([g.gen(i) for i in range(4)], sq)
ev = even_part(generated([g.gen(i) for i in range(5)], sq))
base_even = even_part(base)
g.check("C5  Cl(2,3): <e_mu> meets Cl^0(2,3) exactly in Cl^0(1,3) (dim 8, contained)",
        span_dim(base_even, 5) == 8 and span_dim(base_even + ev, 5) == 16)

# ---------------------------------------------------------------------------
# Part D: the rung's even subalgebra is the anti-de Sitter algebra
# ---------------------------------------------------------------------------
print("Part D: the rung Cl(2,4) and its even subalgebra")

sq6 = g.sig(2, 4)   # (+,+,-,-,-,-)
n = 6
# D1: e_i e_5 for the spacelike e_5 anticommute and square to (+,+,-,-,-): Cl(2,3)
T = [g.mul(g.gen(i), g.gen(5), sq6) for i in range(5)]
sqs, anti = signature_of_generators(T, sq6)
g.check("D1  Cl(2,4): e_i e_5 (e_5 spacelike) generate signature (2,3)",
        anti and sqs == [F(1), F(1), F(-1), F(-1), F(-1)])
# D2: e_i e_0 for the timelike e_0 anticommute and square to (-,+,+,+,+): Cl(4,1)
T0 = [g.mul(g.gen(i), g.gen(0), sq6) for i in range(1, 6)]
sqs0, anti0 = signature_of_generators(T0, sq6)
g.check("D2  Cl(2,4): e_i e_0 (e_0 timelike) generate signature (4,1)",
        anti0 and sqs0 == [F(-1), F(1), F(1), F(1), F(1)])
# D3: both generate the even subalgebra (dim 32)
full6 = generated([g.gen(i) for i in range(6)], sq6)
ev6 = even_part(full6)
g.check("D3  both generated subalgebras are the even subalgebra Cl^0(2,4) (dim 32)",
        span_dim(generated(T, sq6), n) == 32 and span_dim(generated(T0, sq6), n) == 32
        and span_dim(ev6, n) == 32 and span_dim(generated(T, sq6) + ev6, n) == 32)
# D4: the rung's volume element is even, squares to -1, and is central in the
# even subalgebra: the complex unit of Mat(4,C)
w6 = volume(6, sq6)
g.check("D4  omega_6 is even, omega_6^2 = -1, and commutes with every even element",
        all(len(b) % 2 == 0 for b in w6) and square_scalar(w6, sq6) == -1
        and all(g.commutes(w6, x, sq6) for x in ev6))
# D5: omega_6 anticommutes with the vectors (so it is not central in Cl(2,4))
g.check("D5  omega_6 anticommutes with every vector of Cl(2,4)",
        all(g.anticommutes(w6, g.gen(i), sq6) for i in range(6)))
# D6: the shadow Cl(1,3) sits inside Cl(2,3) = Cl^0(2,4): the bivectors
# e_i e_5 for i = 1..4 (one time, three space, times the spacelike e_5)
# generate a Cl(1,3) inside the even subalgebra of the rung.
S = [g.mul(g.gen(i), g.gen(5), sq6) for i in (1, 2, 3, 4)]
sqsS, antiS = signature_of_generators(S, sq6)
g.check("D6  inside Cl^0(2,4): e_i e_5 (i = 1..4) generate a Cl(1,3), this world's shadow",
        antiS and sqsS == [F(1), F(-1), F(-1), F(-1)] and span_dim(generated(S, sq6), n) == 16)
# D7: and the mirror: e_i e_0 (i = 1..4; e_0 timelike, e_1 timelike, e_2..e_4
# spacelike) square to (-,+,+,+) and generate a Cl(3,1) inside the same even
# subalgebra
S0 = [g.mul(g.gen(i), g.gen(0), sq6) for i in (1, 2, 3, 4)]
sqsS0, antiS0 = signature_of_generators(S0, sq6)
g.check("D7  inside Cl^0(2,4): e_i e_0 (i = 1..4) generate a Cl(3,1), the mirror's shadow",
        antiS0 and sqsS0 == [F(-1), F(1), F(1), F(1)] and span_dim(generated(S0, sq6), n) == 16)

# ---------------------------------------------------------------------------
# Part E: the clock, the centres, and the sign-flip paths
# ---------------------------------------------------------------------------
print("Part E: the clock, the centres, and the paths")

# E1: residues of the four extensions
g.check("E1  residues: (1,4) -> 5, (4,1) -> 3, (2,3) -> 7, (3,2) -> 1",
        residue(1, 4) == 5 and residue(4, 1) == 3 and residue(2, 3) == 7 and residue(3, 2) == 1)
# E2: the oriented pair and the P3 representatives of the odd towers
g.check("E2  (1,3) -> 6, (3,1) -> 2; odd shadows (2,1) -> 1, (1,2) -> 7, (4,1) -> 3, (1,4) -> 5",
        residue(1, 3) == 6 and residue(3, 1) == 2 and residue(2, 1) == 1 and residue(1, 2) == 7
        and residue(4, 1) == 3 and residue(1, 4) == 5)
# E3: conformal completion adds (1,1) and preserves the residue: the
# three-dimensional shadows' ambients are the anti-de Sitter extensions
g.check("E3  ambients of (2,1) and (1,2) are (3,2) and (2,3), residues 1 and 7 preserved",
        residue(3, 2) == residue(2, 1) and residue(2, 3) == residue(1, 2))
# E4: the centres separate the reversed pairs: omega^2 = +1 in Cl(1,4) and
# Cl(3,2), -1 in Cl(4,1) and Cl(2,3), so Cl(1,4) is not isomorphic to Cl(4,1)
# and Cl(3,2) is not isomorphic to Cl(2,3) (an isomorphism carries the
# centre to the centre, R + R to R + R and C to C).
g.check("E4  centres: Cl(1,4), Cl(3,2) have omega^2 = +1 (R + R); Cl(4,1), Cl(2,3) have -1 (C)",
        signs["Cl(1,4) = this world + space"] == 1 and signs["Cl(3,2) = mirror + space"] == 1
        and signs["Cl(4,1) = mirror + time"] == -1 and signs["Cl(2,3) = this world + time"] == -1)
# E5: the centre of an odd Clifford algebra is spanned by 1 and omega (dim 2):
# checked by solving for the commutant of the generators in Cl(2,3) and Cl(1,4)
def centre_dim(n, sq):
    bl = g.all_blades(n)
    rows = []
    for b in bl:
        x = {b: F(1)}
        row = []
        for i in range(n):
            comm = g.sub(g.mul(x, g.gen(i), sq), g.mul(g.gen(i), x, sq))
            row.extend(g.basis_vector_of(comm, bl))
        rows.append(row)
    # kernel dimension of the map x -> ([x, e_i])_i
    return len(bl) - g.rank_of_vectors([list(r) for r in zip(*rows)]) if rows else 0
g.check("E5  the centre of each odd extension has dimension 2 (spanned by 1 and omega)",
        all(centre_dim(5, sq) == 2 for sq in EXT.values()))
# E6: and the centre of the rung Cl(2,4) has dimension 1 (simple, even dimension)
g.check("E6  the centre of the rung Cl(2,4) has dimension 1", centre_dim(6, sq6) == 1)

# E7: at dimension four, every path of single sign flips from (1,3) to (3,1)
# passes through (2,2): the signatures at dimension four are (p, 4-p), a flip
# moves p by one, and the walk from p = 1 to p = 3 visits p = 2.  Enumerated:
# all sign-flip walks of length at most six from (1,3) to (3,1) without
# revisiting a signature.
def walks(start, end, maxlen):
    out = []
    def rec(path):
        cur = path[-1]
        if cur == end:
            out.append(list(path)); return
        if len(path) > maxlen:
            return
        for nxt in ((cur[0] + 1, cur[1] - 1), (cur[0] - 1, cur[1] + 1)):
            if 0 <= nxt[0] <= 4 and nxt not in path:
                rec(path + [nxt])
    rec([start])
    return out
W = walks((1, 3), (3, 1), 6)
g.check("E7  exactly one non-revisiting sign-flip walk from (1,3) to (3,1) at dimension four, through (2,2)",
        len(W) == 1 and W[0] == [(1, 3), (2, 2), (3, 1)])
dead = walks((0, 4), (3, 1), 6)
g.check("E8  residues (1,3) = 6, (2,2) = 0, (3,1) = 2, (0,4) = 4; every walk from (0,4) to (3,1) passes back through (1,3)",
        residue(2, 2) == 0 and residue(0, 4) == 4 and residue(1, 3) == 6 and residue(3, 1) == 2
        and len(dead) >= 1 and all(w[1] == (1, 3) for w in dead))

# ---------------------------------------------------------------------------
# Part F: the frozen point splits the ascent's pair (v1.1)
# ---------------------------------------------------------------------------
print("Part F: the frozen point and the ascent's pair")

# Tractor basis of the rung Cl(2,4): e_0, e_1 timelike; e_2, ..., e_5
# spacelike. The frozen point I lies in the hyperbolic plane spanned by e_0
# and e_5, I = a e_0 + b e_5 with <I,I> = a^2 - b^2 playing the role of
# Lambda/3; the Stelle-West direction is the orthogonal vector w = b e_0 + a e_5
# in the same plane, with <w,w> = b^2 - a^2 = -<I,I>: the two are a hyperbolic
# pair with squares of opposite sign, for either sign of Lambda.
def ip6(x, y):
    return g.dot(x, y, sq6)

def frozen(a, b):
    I = g.add(g.scal(a, g.gen(0)), g.scal(b, g.gen(5)))
    w = g.add(g.scal(b, g.gen(0)), g.scal(a, g.gen(5)))
    basis = [g.gen(1), g.gen(2), g.gen(3), g.gen(4), w]   # a basis of I^perp
    return I, w, basis

def gram_sig(basis):
    G = [[ip6(x, y) for y in basis] for x in basis]
    return g.congruence_signature(G)

# F1: for every instance the basis is orthogonal to I and <I,I><w,w> = -<I,I>^2
okF1 = True
for a, b in [(2, 1), (3, 1), (1, 2), (1, 3), (1, 1), (2, 2)]:
    I, w, basis = frozen(F(a), F(b))
    okF1 = okF1 and all(ip6(x, I) == 0 for x in basis) and ip6(w, w) == -ip6(I, I) \
        and ip6(I, w) == 0
g.check("F1  I^perp is spanned by the Lorentz frame and w, with <w,w> = -<I,I> and <I,w> = 0",
        okF1)
# F2: signature of I^perp by the sign of <I,I>: (1,4) for Lambda > 0, (2,3)
# for Lambda < 0, degenerate (1,3;1) for Lambda = 0
I, w, b_pos = frozen(F(2), F(1)); s_pos = gram_sig(b_pos); n_pos = ip6(I, I)
I, w, b_neg = frozen(F(1), F(2)); s_neg = gram_sig(b_neg); n_neg = ip6(I, I)
I0, w0, b_zero = frozen(F(1), F(1)); s_zero = gram_sig(b_zero); n_zero = ip6(I0, I0)
g.check("F2  <I,I> > 0 gives I^perp of signature (1,4); < 0 gives (2,3); = 0 gives (1,3;1)",
        n_pos > 0 and s_pos == (1, 4, 0) and n_neg < 0 and s_neg == (2, 3, 0)
        and n_zero == 0 and s_zero == (1, 3, 1))
# F3: at Lambda = 0 the frozen point lies in its own complement (w = I)
g.check("F3  at <I,I> = 0 the frozen point is null and lies in I^perp (w = I)",
        g.eq(w0, I0) and g.is_zero(g.mul(I0, I0, sq6)))
# F4: the unit directions: e_I^2 = sign<I,I>, e_V^2 = -sign<I,I>, anticommuting;
# adjoining e_I to the five generators of I^perp gives back Cl(2,4)
for (a, b), lab in [((F(2), F(1)), "Lambda > 0"), ((F(1), F(2)), "Lambda < 0")]:
    I, w, basis = frozen(a, b)
    nI, nw = ip6(I, I), ip6(w, w)
    # rational rescaling to unit squares is not available (sqrt 3); the
    # squares' signs and the anticommutation are what the statement uses
    g.check("F4  %s: I^2 and w^2 have opposite signs and I, w anticommute" % lab,
            (nI > 0) != (nw > 0) and g.anticommutes(I, w, sq6)
            and all(g.anticommutes(I, x, sq6) for x in basis[:4]))
    full = generated(basis + [I], sq6)
    g.check("F5  %s: I^perp's five generators together with I generate all of Cl(2,4)" % lab,
            span_dim(full, 6) == 64)
# F6: the degenerate intermediate at Lambda = 0: Cl(1,3;1) has a nilpotent
# generator n, anticommuting with the Lorentz frame, and n Cl(1,3;1) is a
# two-sided ideal of dimension 16 with square zero (the sheaf paper's
# nilpotent ideal)
sqd = g.sig(1, 3, 1)      # e_0 time, e_1..e_3 space, e_4 null
nvec = g.gen(4)
fullD = generated([g.gen(i) for i in range(5)], sqd)
ideal = [g.mul(nvec, x, sqd) for x in fullD]
g.check("F6  Cl(1,3;1): n^2 = 0, n anticommutes with e_mu, n Cl is a 16-dimensional ideal",
        g.is_zero(g.mul(nvec, nvec, sqd)) and all(g.anticommutes(nvec, g.gen(i), sqd) for i in range(4))
        and span_dim(ideal, 5) == 16
        and all(g.eq(g.mul(nvec, x, sqd), g.mul(x, nvec, sqd)) or g.eq(g.mul(nvec, x, sqd), g.neg(g.mul(x, nvec, sqd))) for x in fullD))
g.check("F7  Cl(1,3;1): the ideal n Cl squares to zero",
        all(g.is_zero(g.mul(x, y, sqd)) for x in ideal for y in ideal))
# F8: the residue of the tangent image is unchanged by the frozen point: the
# Lorentz frame {I, w}^perp has signature (1,3) for every sign of <I,I>
g.check("F8  {I,w}^perp has signature (1,3) for <I,I> > 0, < 0 and = 0 alike",
        all(gram_sig(frozen(a, b)[2][:4]) == (1, 3, 0) for a, b in [(F(2), F(1)), (F(1), F(2)), (F(1), F(1))]))

# ---------------------------------------------------------------------------
# Part G: running the transport on the wall (v1.2)
# ---------------------------------------------------------------------------
print("Part G: the transport run on Cl(1,3;1), and what it leaves free")

# The projective-to-conformal paper's model of the minimal completion of a
# degenerate space: W = (Lorentz (1,3)) + (radical rho), completed by the
# dual phi with Q(rho, phi) = 1, Q(phi, phi) = 0, phi orthogonal to the
# Lorentz frame.  Basis order: e_1..e_4 (Lorentz), rho, phi.
GQ = [[F(0)] * 6 for _ in range(6)]
for i, s in enumerate([1, -1, -1, -1]):
    GQ[i][i] = F(s)
GQ[4][5] = GQ[5][4] = F(1)

def Q(x, y):
    return sum(x[i] * GQ[i][j] * y[j] for i in range(6) for j in range(6))

# G1: the completion has signature (2,4): the rung
g.check("G1  the minimal completion of Cl(1,3;1) has signature (2,4), the rung",
        g.congruence_signature(GQ) == (2, 4, 0))
# G2: the isometries of the completion fixing W pointwise are trivial: an
# image x of phi must satisfy Q(x, e_i) = 0, Q(x, rho) = 1 and Q(x, x) = 0;
# the linear conditions force x = phi + c rho, and Q(x, x) = 2c forces c = 0
lin = [[GQ[i][j] for j in range(6)] for i in range(5)]      # Q(x, w_i) for the five W-vectors
g.check("G2  the five linear conditions on the image of phi have a one-dimensional solution space",
        g.mat_rank(lin) == 5)
g.check("G3  on that line Q(phi + c rho, phi + c rho) = 2c identically (checked on instances), so it vanishes only at c = 0: the partner is canonical",
        all(Q([0, 0, 0, 0, c, F(1)], [0, 0, 0, 0, c, F(1)]) == 2 * c for c in [F(0), F(1), F(-3), F(5, 2), F(-1, 7)]))
# G4: a vector orthogonal to the Lorentz frame is a rho + b phi with norm 2ab:
# the sign of the norm is the sign of the product of the components along the
# null generator and its partner; the norm takes every rational value
g.check("G4  Q(a rho + b phi) = 2ab on instances, both signs and zero attained",
        all(Q([0, 0, 0, 0, F(a), F(b)], [0, 0, 0, 0, F(a), F(b)]) == 2 * F(a) * F(b)
            for a, b in [(1, 1), (2, 1), (1, -1), (3, -2), (1, 0), (0, 7)]))
# G5: the isometries fixing the Lorentz frame act on the plane as O(1,1):
# a rational boost (cosh, sinh) = (5/4, 3/4) in the orthogonal basis
# e_+ = (rho + phi)/sqrt2, e_- = (rho - phi)/sqrt2 acts on (a, b) as
# (a, b) -> (a t, b / t) with t = 2 (rho, phi are the eigenvectors of a
# boost), preserving 2ab; the reflection rho <-> phi swaps (a, b) -> (b, a),
# preserving 2ab; neither changes the sign of the norm
def boost(t, v):
    return [v[0], v[1], v[2], v[3], v[4] * t, v[5] / t]
def swap(v):
    return [v[0], v[1], v[2], v[3], v[5], v[4]]
okG5 = True
for a, b in [(F(2), F(1)), (F(1), F(-2)), (F(1), F(1))]:
    v = [F(0)] * 4 + [a, b]
    for w in (boost(F(2), v), boost(F(1, 3), v), swap(v)):
        okG5 = okG5 and Q(w, w) == Q(v, v) and all(Q(w, [F(1) if i == k else F(0) for i in range(6)]) == 0 for k in range(4))
    # and the boost moves the vector (not the identity)
    okG5 = okG5 and boost(F(2), v) != v
g.check("G5  boosts and the swap preserve the norm and keep the image orthogonal to the Lorentz frame; the norm's sign is invariant",
        okG5)
# G6: the two intermediate algebras for the two signs are not isomorphic
# (Part E4 by centres): the sign the transport leaves free is algebraically
# visible one level down, unlike the type-C forgotten bit of the root paper
g.check("G6  the sign left free is visible in the intermediate algebra (omega^2 = +1 against -1, as in E4)",
        signs["Cl(1,4) = this world + space"] == 1 and signs["Cl(2,3) = this world + time"] == -1)

# G7-G8 (v1.6): the null pair in the root paper's normalisation, and the
# frozen point and Stelle-West vector as sum and difference of one pair of
# null components.  v = (e_0 + e_5)/2, v* = (e_0 - e_5)/2: both null with
# v v* + v* v = 1 (the CAR pair); v = I_0 and v* = phi/2.
vN = g.scal(F(1, 2), g.add(g.gen(0), g.gen(5)))
vS = g.scal(F(1, 2), g.sub(g.gen(0), g.gen(5)))
I6 = g.scal(F(1, 2), g.add(g.gen(0), g.gen(5)))       # the canonical frame, as in Part H
ph6 = g.sub(g.gen(0), g.gen(5))
def ip6(x, y):
    return g.dot(x, y, sq6)
g.check("G7  v = (e_0+e_5)/2, v* = (e_0-e_5)/2 are null with v v* + v* v = 1; v = I_0 and v* = phi/2",
        g.is_zero(g.mul(vN, vN, sq6)) and g.is_zero(g.mul(vS, vS, sq6))
        and g.eq(g.add(g.mul(vN, vS, sq6), g.mul(vS, vN, sq6)), g.sc(1))
        and g.eq(vN, I6) and g.eq(vS, g.scal(F(1, 2), ph6)))
okG8 = True
for al, be in [(F(2), F(1)), (F(1), F(-3)), (F(1, 2), F(4)), (F(3), F(0))]:
    Ial = g.add(g.scal(al, vN), g.scal(be, vS))
    Val = g.sub(g.scal(al, vN), g.scal(be, vS))
    okG8 = okG8 and ip6(Ial, Ial) == al * be and ip6(Val, Val) == -al * be and ip6(Ial, Val) == 0 \
        and all(ip6(Ial, g.gen(i)) == 0 and ip6(Val, g.gen(i)) == 0 for i in range(1, 5))
g.check("G8  I = a v + b v* has norm ab (= Lambda/3), a v - b v* has norm -ab and is orthogonal to I: the Stelle-West direction",
        okG8)

# ---------------------------------------------------------------------------
# Part H: two doors closed (v1.3): the dilation gauge, and the two towers in
# one de Sitter universe
# ---------------------------------------------------------------------------
print("Part H: the dilation gauge, and the two towers in one curved universe")

# H1: the canonical null frame realised in the rung's diagonal basis
# (e_0 time, e_5 space): I = (e_0 + e_5)/2, phi = e_0 - e_5
I6 = g.scal(F(1, 2), g.add(g.gen(0), g.gen(5)))
ph6 = g.sub(g.gen(0), g.gen(5))
g.check("H1  I and phi are null, <I,phi> = 1, both orthogonal to the Lorentz frame e_1..e_4",
        g.is_zero(g.mul(I6, I6, sq6)) and g.is_zero(g.mul(ph6, ph6, sq6)) and ip6(I6, ph6) == 1
        and all(ip6(I6, g.gen(i)) == 0 and ip6(ph6, g.gen(i)) == 0 for i in range(1, 5)))
# H2: the bivector B = I ^ phi = (I phi - phi I)/2 equals -e_0 e_5, squares to +1,
# and commutes with every Lorentz bivector e_i e_j
B = g.scal(F(1, 2), g.sub(g.mul(I6, ph6, sq6), g.mul(ph6, I6, sq6)))
lor = [g.mul(g.gen(i), g.gen(j), sq6) for i in range(1, 5) for j in range(i + 1, 5)]
g.check("H2  B = I^phi = -e_0 e_5, B^2 = +1, and B commutes with the six Lorentz bivectors",
        g.eq(B, g.neg(g.mul(g.gen(0), g.gen(5), sq6))) and g.eq(g.mul(B, B, sq6), g.sc(1))
        and all(g.commutes(B, x, sq6) for x in lor))
# H3: the rotor R = 5/4 + (3/4) B is a unit rotor (R R~ = 1) that fixes the
# Lorentz frame and scales I and phi reciprocally: R I R~ = t I, R phi R~ = phi/t
R = g.add(g.sc(F(5, 4)), g.scal(F(3, 4), B))
Rt = g.reverse(R)
def sand(x):
    return g.mul(g.mul(R, x, sq6), Rt, sq6)
RI, Rph = sand(I6), sand(ph6)
tI = [c / I6[b] for b, c in RI.items() if b in I6]
okH3 = g.eq(g.mul(R, Rt, sq6), g.sc(1)) and all(g.eq(sand(g.gen(i)), g.gen(i)) for i in range(1, 5))
okH3 = okH3 and len(set(tI)) == 1 and g.eq(RI, g.scal(tI[0], I6)) and g.eq(Rph, g.scal(1 / tI[0], ph6))
g.check("H3  R = 5/4 + 3/4 B is a unit rotor fixing the Lorentz frame with R I R~ = t I, R phi R~ = phi/t (t = %s)" % (tI[0] if tI else None),
        okH3)
# H4: on a frozen point a I + b phi the rotor changes (a, b) and preserves 2ab
okH4 = True
for a, b in [(F(2), F(1)), (F(1), F(-2))]:
    x = g.add(g.scal(a, I6), g.scal(b, ph6))
    y = sand(x)
    okH4 = okH4 and (not g.eq(x, y)) and ip6(y, y) == ip6(x, x) == 2 * a * b
g.check("H4  the rotor moves the frozen point along its hyperbola: (a, b) changed, 2ab = <I,I> preserved",
        okH4)
# H5: B is the bivector of the plane orthogonal to the Lorentz frame: it
# anticommutes with e_0 and e_5 and commutes with e_1..e_4
g.check("H5  B anticommutes with e_0, e_5 and commutes with e_1..e_4: the dilation generator of the conformal model",
        all(g.anticommutes(B, g.gen(i), sq6) for i in (0, 5)) and all(g.commutes(B, g.gen(i), sq6) for i in range(1, 5)))

# The two towers in one curved universe.  The mirror's soldering negates the
# metric, so its tractor metric is (4,2) and its frozen point has norm
# -<I,I>.  Model: Lorentz frame (3,1) (e_0 space, e_1..e_3 time in the
# mirror's own labelling is not needed; use squares (-1,+1,+1,+1)) plus the
# hyperbolic plane (e_4 square -1, e_5 square +1); I' = a e_4 + b e_5 with
# <I',I'> = -a^2 + b^2 = -(a^2 - b^2) = -<I,I>.
sqm = (-1, 1, 1, 1, -1, 1)
def ipm(x, y):
    return g.dot(x, y, sqm)
def mirror_frozen(a, b):
    Ip = g.add(g.scal(a, g.gen(4)), g.scal(b, g.gen(5)))
    w = g.add(g.scal(b, g.gen(4)), g.scal(a, g.gen(5)))
    basis = [g.gen(0), g.gen(1), g.gen(2), g.gen(3), w]
    assert all(ipm(x, Ip) == 0 for x in basis)
    return Ip, w, basis
def gram_sig_m(basis):
    return g.congruence_signature([[ipm(x, y) for y in basis] for x in basis])
Ip, w, bm = mirror_frozen(F(2), F(1)); sm_dS = gram_sig_m(bm); nm_dS = ipm(Ip, Ip)
Ip, w, bm = mirror_frozen(F(1), F(2)); sm_AdS = gram_sig_m(bm); nm_AdS = ipm(Ip, Ip)
# H6: de Sitter (our <I,I> = 3 > 0, the mirror's -3): our I^perp is (1,4),
# the mirror's is (4,1); anti-de Sitter: (2,3) and (3,2)
g.check("H6  de Sitter: I^perp is (1,4) for this world and (4,1) for the mirror; anti-de Sitter: (2,3) and (3,2)",
        s_pos == (1, 4, 0) and nm_dS < 0 and sm_dS == (4, 1, 0)
        and s_neg == (2, 3, 0) and nm_AdS > 0 and sm_AdS == (3, 2, 0))
# H7: the two-by-two rule: doubled (omega^2 = +1) iff (de Sitter and this
# world) or (anti-de Sitter and mirror); complexified otherwise
g.check("H7  doubled iff (de Sitter, this world) or (anti-de Sitter, mirror); complexified otherwise",
        signs["Cl(1,4) = this world + space"] == 1 and signs["Cl(4,1) = mirror + time"] == -1
        and signs["Cl(2,3) = this world + time"] == -1 and signs["Cl(3,2) = mirror + space"] == 1)
# H8: the even subalgebras of Cl(1,4) and Cl(4,1) have the same presentation:
# e_mu e_5 anticommute and square to (+,-,-,-) in both, so the spin groups and
# the MacDowell-Mansouri bivector algebras coincide
def even_pres(sq):
    T = [g.mul(g.gen(i), g.gen(4), sq) for i in range(4)]
    sqs, anti = signature_of_generators(T, sq)
    return anti, sqs
a1, s1 = even_pres(g.sig(1, 4))
a2, s2 = even_pres((-1, 1, 1, 1, 1))
g.check("H8  Cl^0(1,4) and Cl^0(4,1): e_mu e_5 anticommute and square to (+,-,-,-) in both (same spin group)",
        a1 and a2 and s1 == [F(1), F(-1), F(-1), F(-1)] and s2 == [F(1), F(-1), F(-1), F(-1)])
# H9: what does differ is the bare fifth generator: e_5^2 = -1 in the doubled
# case and +1 in the complexified case, and e_5 is +/- the real pseudoscalar
# on the summands (B) against omega times the pseudoscalar's inverse (a
# central complex unit times it) in the complexified case
okH9 = square_scalar(g.gen(4), g.sig(1, 4)) == -1
for sqc in [(-1, 1, 1, 1, 1), (1, -1, -1, -1, 1)]:      # Cl(4,1) and Cl(2,3)
    wc = volume(5, sqc); wpc = volume(4, sqc)
    okH9 = okH9 and square_scalar(g.gen(4), sqc) == 1 and g.eq(wc, g.mul(wpc, g.gen(4), sqc)) \
        and central(wc, 5, sqc) and square_scalar(wc, sqc) == -1
g.check("H9  e_5^2 = -1 (doubled) against +1 (complexified); in Cl(4,1) and Cl(2,3), omega = omega' e_5 with omega central and omega^2 = -1",
        okH9)

# ---------------------------------------------------------------------------
# Part I: the wall in the cosmological constant as a T4 degeneration (v1.4)
# ---------------------------------------------------------------------------
print("Part I: the Lambda line as a tame wall, its exceptional algebra, its residue, its completion")

# The family over the Lambda line, in the smooth dilation gauge a = 1:
# I_L = I_0 + (L/6) phi, with I_0 = (e_0 + e_5)/2 and phi = e_0 - e_5 in the
# rung's diagonal basis (Part H), so <I_L, I_L> = L/3; the orthogonal
# direction in the plane is w_L = I_0 - (L/6) phi, and I_L^perp is spanned by
# the Lorentz frame e_1..e_4 and w_L.
def family(L, a=F(1)):
    b = L / (6 * a)
    IL = g.add(g.scal(a, I6), g.scal(b, ph6))
    wL = g.sub(g.scal(a, I6), g.scal(b, ph6))
    basis = [g.gen(1), g.gen(2), g.gen(3), g.gen(4), wL]
    return IL, wL, basis

def gram6(basis):
    return [[ip6(x, y) for y in basis] for x in basis]

Ls = [F(-3), F(-1), F(-1, 2), F(0), F(1, 2), F(1), F(3)]
# I1: the Gram of I_L^perp is diag(1,-1,-1,-1, -L/3): corank one exactly at L = 0
okI1 = True
for a in (F(1), F(2), F(1, 3), F(-5)):
    for L in Ls:
        IL, wL, basis = family(L, a)
        G = gram6(basis)
        diag = [G[i][i] for i in range(5)]
        off = all(G[i][j] == 0 for i in range(5) for j in range(5) if i != j)
        okI1 = okI1 and ip6(IL, IL) == L / 3 and all(ip6(x, IL) == 0 for x in basis) \
            and off and diag == [F(1), F(-1), F(-1), F(-1), -L / 3]
g.check("I1  in four gauges a, I_L^perp has Gram diag(1,-1,-1,-1,-L/3): corank one exactly at L = 0",
        okI1 and g.congruence_signature(gram6(family(F(0))[2])) == (1, 3, 1))
# I2: gauge independence: any nonvanishing a gives the same dying eigenvalue -L/3
g.check("I2  the dying eigenvalue -L/3 is independent of the dilation gauge a",
        all(ip6(family(L, a)[1], family(L, a)[1]) == -L / 3 for L in Ls for a in (F(1), F(2), F(1, 3), F(-5))))
# I3: transversality (T3): the crossing is first order, slope -1/3 exactly
g.check("I3  (T3): lambda(L) = -L/3 crosses zero at nonzero speed, (lambda(L) - lambda(0))/L = -1/3 for every L",
        all((ip6(family(L)[1], family(L)[1]) - 0) / L == F(-1, 3) for L in Ls if L != 0))
# I4: the signatures on the two sides: (2,3) for L < 0, (1,4) for L > 0
g.check("I4  signature (2,3) for L < 0 and (1,4) for L > 0: a signature-change wall between AdS and dS",
        all(g.congruence_signature(gram6(family(L)[2])) == ((2, 3, 0) if L < 0 else (1, 4, 0)) for L in Ls if L != 0))
# I5: the exceptional algebra: rescaling the dying direction by 1/sqrt(t)
# with t = -L (approach from L < 0) or t = L (from L > 0) gives the limit
# Gram Lorentz + (rate): rate = +1/3 from the AdS side, -1/3 from the dS
# side; the cross terms vanish identically here, so the limit is exact at
# every t (checked as the rescaled Gram's dying entry lambda/t)
okI5 = True
for L in Ls:
    if L == 0:
        continue
    t = -L if L < 0 else L
    lam = ip6(family(L)[1], family(L)[1])
    okI5 = okI5 and lam / t == (F(1, 3) if L < 0 else F(-1, 3))
g.check("I5  exceptional algebra: the rescaled dying entry lambda/t is +1/3 from the AdS side, -1/3 from the dS side",
        okI5 and g.congruence_signature([[1, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, F(1, 3)]]) == (2, 3, 0)
        and g.congruence_signature([[1, 0, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, F(-1, 3)]]) == (1, 4, 0))
# I6: the residue: L times the inverse Gram's dying entry is -3 for every L,
# so the pole of the inverse form at the wall is -3 w_0 (x) w_0, and -3/L is
# the Stelle-West norm <V,V>: the residue of the metric at the wall is the
# Stelle-West vector's norm
g.check("I6  residue: L * (inverse Gram)_{ww} = -3 for every L != 0 and every gauge (the Stelle-West norm -3/L); w_0 = a I_0",
        all(L * (1 / ip6(family(L, a)[1], family(L, a)[1])) == -3 for L in Ls if L != 0 for a in (F(1), F(2), F(1, 3), F(-5)))
        and all(g.eq(family(F(0), a)[1], g.scal(a, I6)) for a in (F(1), F(2), F(1, 3), F(-5))))
# I7: the rung is a two-sided nondegenerate completion of rank +1: the
# complement of I_L^perp is span(I_L) with K = <I_L,I_L> = L/3, whose sign
# switches across the wall, so sig(K) is (1,0) on one side and (0,1) on the
# other while the total stays (2,4): the case T4 Thm 5.1 excludes by
# hypothesis
okI7 = True
for L in Ls:
    IL, wL, basis = family(L)
    full = basis + [IL]
    tot = g.congruence_signature(gram6(full)) if L != 0 else None
    if L != 0:
        okI7 = okI7 and tot == (2, 4, 0) and ((L > 0 and ip6(IL, IL) > 0) or (L < 0 and ip6(IL, IL) < 0))
g.check("I7  the rung completes the family on both sides (total (2,4)) with the complement's sign switching across the wall",
        okI7 and g.congruence_signature(gram6(family(F(0))[2] + [family(F(0))[0]])) == (1, 3, 2))
# I8: at L = 0 the family's five vectors plus I_0 span only a five-dimensional
# space (I_0 is the radical and lies in I_0^perp); the completion at the wall
# is by the partner phi, and (Lorentz, I_0, phi) has signature (2,4)
g.check("I8  at L = 0 the completing direction is the partner phi, not I_0: (Lorentz, I_0, phi) has signature (2,4)",
        g.congruence_signature(gram6([g.gen(1), g.gen(2), g.gen(3), g.gen(4), I6, ph6])) == (2, 4, 0)
        and g.rank_of_vectors([g.basis_vector_of(x, g.all_blades(6)) for x in family(F(0))[2] + [family(F(0))[0]]]) == 5)

# I9 (v1.7): the general model of Theorem 10.3(iii): for (p,q) in a list, the
# hyperplane family span(f_1..f_n, u + (t/2) v) of R^{p,q} + H has dying
# eigenvalue t, complement u - (t/2) v of norm -t, and total signature
# (p+1, q+1) for every t, degenerate exactly at t = 0
okI9 = True
for (pp, qq) in [(1, 3), (2, 1), (3, 0), (0, 2), (2, 2)]:
    nn = pp + qq
    GQm = [[F(0)] * (nn + 2) for _ in range(nn + 2)]
    for i, sgn in enumerate([1] * pp + [-1] * qq):
        GQm[i][i] = F(sgn)
    GQm[nn][nn + 1] = GQm[nn + 1][nn] = F(1)       # u, v null with <u,v> = 1
    def Qm(x, y):
        return sum(x[i] * GQm[i][j] * y[j] for i in range(nn + 2) for j in range(nn + 2))
    for t in (F(-2), F(-1, 3), F(0), F(1, 2), F(3)):
        k = [F(0)] * nn + [F(1), t / 2]
        c = [F(0)] * nn + [F(1), -t / 2]
        fam = [[F(1) if j == i else F(0) for j in range(nn + 2)] for i in range(nn)] + [k]
        Gf = [[Qm(x, y) for y in fam] for x in fam]
        sig_f = g.congruence_signature(Gf)
        expect = (pp, qq + 1, 0) if t < 0 else ((pp + 1, qq, 0) if t > 0 else (pp, qq, 1))
        okI9 = okI9 and Qm(k, k) == t and Qm(c, c) == -t and Qm(k, c) == 0 and sig_f == expect \
            and g.congruence_signature([[Qm(x, y) for y in fam + [c]] for x in fam + [c]]) == ((pp + 1, qq + 1, 0) if t != 0 else (pp, qq, 2))
    okI9 = okI9 and g.congruence_signature(GQm) == (pp + 1, qq + 1, 0)
g.check("I9  the general model: hyperplane families in a fixed (p+1,q+1) space are tame walls completed on both sides, for five (p,q)",
        okI9)
# ---------------------------------------------------------------------------
print()
print("verify_T14a.py: %d checks, %d passed, %d failed"
      % (NCHECKS[0], NCHECKS[0] - len(g.FAILURES), len(g.FAILURES)))
if g.FAILURES:
    print("FAILED:", *g.FAILURES, sep="\n  ")
    raise SystemExit(1)
