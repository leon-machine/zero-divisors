#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T08.py: exact-arithmetic verification of the computational identities of
"Black-Hole Entropy and Scrambling: The Singularity Ledger and the No-Echo Prediction"
(Transport Papers, T8).

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: dimensional quantities are represented as
exact monomials c * 2^a * 3^b * pi^p * M^e with rational c and rational
exponents, so every scaling claim is an identity of exponents, not a numerical
estimate; matrix computations are over the rationals.  Statement tags refer to
the compiled paper.  Units G = c = hbar = l_P = 1 throughout.
"""

from fractions import Fraction
import GA as g

# ---------------------------------------------------------------------------
# exact monomials  c * 2^a * 3^b * pi^p * M^e
# ---------------------------------------------------------------------------


class Mono(object):
    __slots__ = ("c", "a", "b", "p", "e")

    def __init__(self, c=1, a=0, b=0, p=0, e=0):
        c = Fraction(c)
        a, b = Fraction(a), Fraction(b)
        # normalise: fold all factors of 2 and 3 in c into the exponents,
        # so equal quantities have equal representations
        if c != 0:
            num_, den_ = c.numerator, c.denominator
            while num_ % 2 == 0:
                num_ //= 2
                a += 1
            while den_ % 2 == 0:
                den_ //= 2
                a -= 1
            while num_ % 3 == 0:
                num_ //= 3
                b += 1
            while den_ % 3 == 0:
                den_ //= 3
                b -= 1
            c = Fraction(num_, den_)
        self.c = c
        self.a = a             # exponent of 2
        self.b = b             # exponent of 3
        self.p = Fraction(p)   # exponent of pi
        self.e = Fraction(e)   # exponent of M

    def __mul__(self, o):
        return Mono(self.c * o.c, self.a + o.a, self.b + o.b,
                    self.p + o.p, self.e + o.e)

    def __truediv__(self, o):
        return Mono(self.c / o.c, self.a - o.a, self.b - o.b,
                    self.p - o.p, self.e - o.e)

    def pow(self, q):
        q = Fraction(q)
        if self.c != 1:
            raise ValueError("rational-power of nontrivial coefficient; "
                             "fold it into the prime exponents first")
        return Mono(1, self.a * q, self.b * q, self.p * q, self.e * q)

    def __eq__(self, o):
        return (self.c, self.a, self.b, self.p, self.e) == \
               (o.c, o.a, o.b, o.p, o.e)

    def __repr__(self):
        return "%s * 2^%s 3^%s pi^%s M^%s" % (self.c, self.a, self.b, self.p, self.e)


M = Mono(e=1)
PI = Mono(p=1)
TWO = Mono(a=1)
THREE = Mono(b=1)
HALF = Mono(c=Fraction(1, 2))


def num(x):
    return Mono(c=x)


# ---------------------------------------------------------------------------
# Part A: the count (lem:scheme, prop:volume, thm:count, prop:arealaw,
# prop:unique)
# ---------------------------------------------------------------------------

# r_c from the curvature cutoff 2M/r^3 = 1: r_c = (2M)^{1/3}
r_c = (TWO * M).pow(Fraction(1, 3))
g.check("lem:scheme: the curvature cutoff solves to r_c = 2^{1/3} M^{1/3} "
      "(cube equals 2M exactly)",
      r_c * r_c * r_c == TWO * M and r_c.e == Fraction(1, 3))

# Kretschmann 48 M^2 / r^6 = 1: r = 48^{1/6} M^{1/3}; 48 = 2^4 * 3
r_k = (TWO.pow(4) * THREE * M * M).pow(Fraction(1, 6))
g.check("lem:scheme: the Kretschmann cutoff gives r = 2^{2/3} 3^{1/6} M^{1/3} "
      "(the constant 48^{1/6}, order one)",
      r_k == Mono(1, Fraction(2, 3), Fraction(1, 6), 0, Fraction(1, 3)))

# proper time (2/3) r^{3/2} (2M)^{-1/2} = 1: r = (3/2)^{2/3} (2M)^{1/3}
r_t = ((THREE / TWO).pow(Fraction(2, 3))) * (TWO * M).pow(Fraction(1, 3))
g.check("lem:scheme: the unit-proper-time cutoff gives r = 3^{2/3} 2^{-1/3} "
      "M^{1/3} (order one), same M-exponent 1/3 in all three schemes",
      r_t == Mono(1, Fraction(-1, 3), Fraction(2, 3), 0, Fraction(1, 3))
      and r_c.e == r_k.e == r_t.e == Fraction(1, 3))

# slice volume per unit Killing time: 4 pi r_c^2 sqrt(2M/r_c) = 8 pi M exactly
def slice_volume(r):
    """4 pi r^2 sqrt(2M/r): the induced-metric slice volume per unit t."""
    return num(4) * PI * r * r * ((TWO * M / r).pow(Fraction(1, 2)))


vol = slice_volume(r_c)
g.check("prop:volume: 4 pi r_c^2 sqrt(2M/r_c) = 8 pi M exactly",
      vol == num(8) * PI * M)

# geometric anchors, derived rather than typed: r_s = 2M, A = 4 pi r_s^2,
# S_BH = A/4, kappa = 1/(4M), T_H = kappa/(2 pi)
r_s = TWO * M
A_horizon = num(4) * PI * r_s * r_s
S_BH = A_horizon / num(4)
kappa = num(Fraction(1, 4)) / M
T_H = kappa / (num(2) * PI)
g.check("sec:setting: S_BH = A/4 = 4 pi M^2 with A = 4 pi (2M)^2, and "
      "T_H = kappa/(2 pi) = 1/(8 pi M): the anchors derived, not typed",
      S_BH == num(4) * PI * M * M
      and A_horizon == num(16) * PI * M * M
      and T_H == num(Fraction(1, 8)) / (PI * M))

# thm:count: dN/dt = 8 pi nu M = nu / T_H, with T_H derived from kappa
g.check("thm:count: dN/dt = 8 pi nu M equals nu / T_H (the accrual rate is "
      "set by the Hawking temperature)", vol * T_H == num(1))

# prop:arealaw: 8 pi M * (nu dt) = S_BH  <=>  nu dt = M/2
lhs = vol * (HALF * M)                       # slice volume times nu*dt = M/2
g.check("prop:arealaw: N = 8 pi nu M dt equals S_BH exactly when "
      "nu dt = M/2", lhs == S_BH)

# prop:unique: the three scalings
sphere_only = num(4) * PI * r_c * r_c
g.check("prop:unique: the sphere-only count scales as M^{2/3}",
      sphere_only.e == Fraction(2, 3))
r0 = num(1)                                  # an M-independent cutoff radius
fixed_r = slice_volume(r0)                   # the same metric routine as vol
g.check("prop:unique: a fixed cutoff radius scales as M^{1/2}",
      fixed_r.e == Fraction(1, 2))
ADMISSIBLE = (Fraction(1), Fraction(3))      # exponents of M and M^3
g.check("prop:unique: matching the area law M^2 from the computed exponents "
      "p = 2/3 (sphere-only) and p = 1/2 (fixed radius) needs timescale "
      "exponents outside the admissible set {1, 3}; the internal cutoff's "
      "p = 1 needs exponent 1, which is admissible",
      all((Fraction(2) - p) not in ADMISSIBLE
          for p in (sphere_only.e, fixed_r.e))
      and (Fraction(2) - vol.e) in ADMISSIBLE)

# ---------------------------------------------------------------------------
# Part B: the epoch (thm:epoch, cor:holographic), and the clocks
# ---------------------------------------------------------------------------

beta = num(2) * PI / kappa
g.check("thm:epoch: beta = 2 pi / kappa = 8 pi M for Schwarzschild",
      beta == num(8) * PI * M)

# --- the clock inventory (lem:inventory): adjoint spectra, exactly.
# ad_X on the mode operators of a two-mode ledger is block-diagonal in 2x2
# rational blocks; the criterion of lem:inventory(iii): semisimple with real
# eigenvalues, all nonzero ones of equal magnitude.


def _isqrt(n):
    assert n >= 0
    if n == 0:
        return 0
    x, y = n, (n + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def _sqrt_frac(q):
    rn, rd = _isqrt(q.numerator), _isqrt(q.denominator)
    assert rn * rn == q.numerator and rd * rd == q.denominator
    return Fraction(rn, rd)


def block_class(a, b, c, d):
    """[[a,b],[c,d]] over Q -> ('real', eigs), ('complex', det) with
    |lambda|^2 = det, or ('nonsemisimple', None)."""
    a, b, c, d = Fraction(a), Fraction(b), Fraction(c), Fraction(d)
    tr, det = a + d, a * d - b * c
    D = tr * tr - 4 * det
    if D < 0:
        return ("complex", det)
    if D == 0 and not (b == 0 and c == 0):
        return ("nonsemisimple", None)
    r = _sqrt_frac(D)
    return ("real", ((tr + r) / 2, (tr - r) / 2))


def is_clock(blocks):
    mags = set()
    for blk in blocks:
        kind, data = block_class(*blk)
        if kind != "real":
            return False
        for e in data:
            if e != 0:
                mags.add(abs(e))
    return len(mags) == 1


HF = Fraction(1, 2)
g.check("lem:inventory(iii): the clock criterion on the inventory: E_11, "
      "E_12 + E_21 and the equal-coefficient sum are clocks (semisimple, "
      "real adjoint eigenvalues, nonzero ones all of magnitude 1); the "
      "compact E_12 - E_21, the nilpotent E_12, and the unequal-magnitude "
      "diagonals are not; the opposed pair E_11 - E_22 is a clock",
      is_clock([(1, 0, 0, 0), (-1, 0, 0, 0)])
      and is_clock([(0, 1, 1, 0), (0, -1, -1, 0)])
      and is_clock([(1, 0, 0, 1), (-1, 0, 0, -1)])
      and is_clock([(1, 0, 0, -1), (-1, 0, 0, 1)])
      and not is_clock([(0, 1, -1, 0)])
      and not is_clock([(0, 1, 0, 0)])
      and not is_clock([(1, 0, 0, 2), (-1, 0, 0, -2)]))
g.check("lem:inventory(iii): the pairing trichotomy by the sign of cd: "
      "2 psi+psi+ + (1/2) psi psi is a clock with adjoint eigenvalues +-1 "
      "(unit rapidity outright) and cd = 4 a clock at rapidity 2; "
      "cd = -6 is compact; cd = 0 nilpotent",
      is_clock([(0, 2, HF, 0), (0, -2, -HF, 0)])
      and block_class(0, 2, HF, 0)[1] == (Fraction(1), Fraction(-1))
      and is_clock([(0, 3, Fraction(4, 3), 0), (0, -3, -Fraction(4, 3), 0)])
      and not is_clock([(0, 3, -2, 0), (0, -3, 2, 0)])
      and not is_clock([(0, 5, 0, 0), (0, -5, 0, 0)]))
def is_clock_modulus_only(blocks):
    """The weakened criterion: nonzero eigenvalue MODULI all equal, reality
    and semisimplicity not required.  Exists only to be shown too weak."""
    mags2 = set()
    for blk in blocks:
        kind, data = block_class(*blk)
        if kind == "complex":
            mags2.add(data)                      # |lambda|^2 = det
        elif kind == "nonsemisimple":
            a, b, c, d = [Fraction(x) for x in blk]
            mags2.add(((a + d) / 2) ** 2)        # repeated eigenvalue
        else:
            for e in data:
                if e != 0:
                    mags2.add(e * e)
    return len(mags2) == 1


g.check("lem:inventory(iii): the exclusion clauses each have teeth: "
      "E_11 + E_12 - E_21 has every adjoint eigenvalue of modulus exactly "
      "1 (|lambda|^2 = det = 1 in both blocks) and none real, so the "
      "modulus-only variant (run here) admits it and the stated criterion "
      "excludes it; and E_11 + E_12 + E_22 has real adjoint eigenvalues, "
      "all nonzero and all of modulus 1, and is excluded by semisimplicity "
      "alone",
      block_class(1, 1, -1, 0)[0] == "complex"
      and block_class(1, 1, -1, 0)[1] == Fraction(1)
      and block_class(-1, 1, -1, 0)[0] == "complex"
      and block_class(-1, 1, -1, 0)[1] == Fraction(1)
      and is_clock_modulus_only([(1, 1, -1, 0), (-1, 1, -1, 0)])
      and not is_clock([(1, 1, -1, 0), (-1, 1, -1, 0)])
      and block_class(1, 1, 0, 1)[0] == "nonsemisimple"
      and not is_clock([(1, 1, 0, 1), (-1, 0, -1, -1)]))

# --- S4(b): the same conclusions derived rather than asserted: a two-mode CAR
# representation on the 4-dimensional Fock space, mode operators as exact
# rational matrices, ad_X computed by commutator, the criterion read off
# ad_X itself (A != 0 and A^3 = t A with t > 0 is exactly "semisimple, real
# eigenvalues, nonzero ones of equal magnitude sqrt(t)").


def _fock2():
    def cre(k):
        Mx = [[Fraction(0)] * 4 for _ in range(4)]
        for st in range(4):
            if not (st >> k) & 1:
                sgn = -1 if (k == 1 and (st & 1)) else 1
                Mx[st | (1 << k)][st] = Fraction(sgn)
        return Mx

    def ann(k):
        Mx = [[Fraction(0)] * 4 for _ in range(4)]
        for st in range(4):
            if (st >> k) & 1:
                sgn = -1 if (k == 1 and (st & 1)) else 1
                Mx[st & ~(1 << k)][st] = Fraction(sgn)
        return Mx
    return [cre(0), cre(1)], [ann(0), ann(1)]


def _mm4(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)]
            for i in range(4)]


def _comm4(A, B):
    AB, BA = _mm4(A, B), _mm4(B, A)
    return [[AB[i][j] - BA[i][j] for j in range(4)] for i in range(4)]


CRE, ANN = _fock2()
OPS = [CRE[0], CRE[1], ANN[0], ANN[1]]


def _ad_coeffs(X):
    """ad_X on the operator basis (psi1+, psi2+, psi1, psi2), coefficients
    via the trace pairing (the basis is orthogonal, each of norm 2), with
    the span membership of every commutator certified by reassembly."""
    A = [[Fraction(0)] * 4 for _ in range(4)]
    for j, O in enumerate(OPS):
        Y = _comm4(X, O)
        for k, Ok in enumerate(OPS):
            A[k][j] = sum(Ok[a][b] * Y[a][b]
                          for a in range(4) for b in range(4)) / 2
        R = [[sum(A[k][j] * OPS[k][a][b] for k in range(4))
              for b in range(4)] for a in range(4)]
        if R != Y:
            return None          # commutator left the operator span: not CAR
    return A


def _is_clock_ad(A):
    if all(x == 0 for r in A for x in r):
        return False
    A3 = _mm4(_mm4(A, A), A)
    t = None
    for i in range(4):
        for j in range(4):
            if A[i][j] != 0:
                t = A3[i][j] / A[i][j]
                break
        if t is not None:
            break
    if t is None or t <= 0:
        return False
    return A3 == [[t * A[i][j] for j in range(4)] for i in range(4)]


def _E(i, j):
    return _mm4(CRE[i], ANN[j])


def _lc(*terms):
    R = [[Fraction(0)] * 4 for _ in range(4)]
    for coef, Mx in terms:
        for a in range(4):
            for b in range(4):
                R[a][b] += Fraction(coef) * Mx[a][b]
    return R


def _P(c, d):
    return _lc((c, _mm4(CRE[0], CRE[1])), (d, _mm4(ANN[1], ANN[0])))


_clocks = [_E(0, 0),
           _lc((1, _E(0, 1)), (1, _E(1, 0))),
           _lc((1, _E(0, 0)), (1, _E(1, 1))),
           _lc((1, _E(0, 0)), (-1, _E(1, 1))),
           _P(2, Fraction(1, 2))]
_not_clocks = [_lc((1, _E(0, 1)), (-1, _E(1, 0))),
               _E(0, 1),
               _lc((1, _E(0, 0)), (2, _E(1, 1))),
               _lc((1, _E(0, 0)), (1, _E(0, 1)), (-1, _E(1, 0))),
               _lc((1, _E(0, 0)), (1, _E(0, 1)), (1, _E(1, 1))),
               _P(1, -1), _P(1, 0)]
def _verdict(X):
    A = _ad_coeffs(X)
    return None if A is None else _is_clock_ad(A)


g.check("lem:inventory(iii): the conclusions derived, not asserted: mode "
      "operators built as exact Fock matrices of a two-mode CAR "
      "representation (pairing generators built too), ad_X computed by "
      "commutator with its span membership certified, the criterion read "
      "off ad_X (A^3 = t A, t > 0): the five clocks and seven non-clocks "
      "above all reproduced",
      all(_verdict(X) is True for X in _clocks)
      and all(_verdict(X) is False for X in _not_clocks))

nu_pred = (HALF * M) / beta                  # nu = (M/2)/dt with dt = beta
g.check("thm:epoch: the conversion gives nu = 1/(16 pi) exactly",
      nu_pred == num(Fraction(1, 16)) / PI)

V = vol * beta
g.check("cor:holographic(1): the epoch three-volume V = 8 pi M * beta "
      "= 64 pi^2 M^2 = beta^2 in Planck units (one power of l_P hidden)",
      V == num(64) * PI * PI * M * M and V == beta * beta)

g.check("cor:holographic(2)-(3): nu V = S_BH (one fermion per four horizon "
      "cells per modular period) and the nu = 1 overshoot V/S_BH = 16 pi "
      "is exactly the horizon-area coefficient A/M^2",
      nu_pred * V == S_BH
      and V / S_BH == A_horizon / (M * M)
      and V / S_BH == num(16) * PI)

# ---------------------------------------------------------------------------
# Part C: the sphere (prop:n2), and the failed aggregations
# ---------------------------------------------------------------------------

n_sq = sphere_only                           # the same expression, aliased
g.check("prop:n2(1): the slice-cell count 4 pi r_c^2 = 4 pi (2M)^{2/3}: the "
      "fuzzy operator dimension scales as M^{2/3}",
      n_sq == num(4) * PI * TWO.pow(Fraction(2, 3)) * M.pow(Fraction(2, 3)))

spheres_per_t = vol / n_sq
g.check("prop:n2(3): the slice volume contains (2M)^{1/3} spheres per unit "
      "Killing time", spheres_per_t == (TWO * M).pow(Fraction(1, 3)))

# fundamental-per-slice: n = sqrt(n^2) ~ M^{1/3} per sphere, times the
# computed spheres/t, times the computed epoch dt = beta
n_fund_exp = n_sq.e / 2 + spheres_per_t.e + beta.e
g.check("prop:n2(3): fundamental-per-slice aggregation scales as M^{5/3}, "
      "breaking the area law", n_fund_exp == Fraction(5, 3))

# Kostant instance at n = 3: principal vs block embedding, exact kernels


def mat(*rows):
    return [[Fraction(x) for x in r] for r in rows]


def mmul3(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def msub3(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def comm3(A, B):
    return msub3(mmul3(A, B), mmul3(B, A))


E3 = mat([0, 2, 0], [0, 0, 1], [0, 0, 0])
F3 = mat([0, 0, 0], [1, 0, 0], [0, 2, 0])
H3 = mat([2, 0, 0], [0, 0, 0], [0, 0, -2])
ok = (comm3(E3, F3) == H3
      and comm3(H3, E3) == [[2 * x for x in r] for r in E3]
      and comm3(H3, F3) == [[-2 * x for x in r] for r in F3])
g.check("thm:sphere: the integer principal sl2 triple in M_3 satisfies "
      "[e,f] = h, [h,e] = 2e, [h,f] = -2f exactly", ok)


def ad_matrix(X):
    """ad_X on M_3 as a 9x9 rational matrix (basis e_ij row-major)."""
    out = []
    for i in range(3):
        for j in range(3):
            Eij = [[Fraction(1) if (r, c) == (i, j) else Fraction(0)
                    for c in range(3)] for r in range(3)]
            C = comm3(X, Eij)
            out.append([C[r][c] for r in range(3) for c in range(3)])
    # columns are images of basis vectors: transpose to act on coordinates
    return [[out[col][row] for col in range(9)] for row in range(9)]


def kernel_dim(A):
    return 9 - g.rank_of_vectors([row[:] for row in A])


adE = ad_matrix(E3)
g.check("thm:sphere: ad_e of the principal embedding has kernel dimension "
      "exactly 3: the adjoint decomposition of M_3 is multiplicity-free, "
      "1 + 3 + 5", kernel_dim(adE) == 3)

eigs = sorted(H3[i][i] - H3[j][j] for i in range(3) for j in range(3))
g.check("thm:sphere: the ad_h weight multiset is {0,0,0,+-2,+-2,+-4}: the "
      "weights of one spin-0, one spin-1 and one spin-2 multiplet",
      eigs == [-4, -2, -2, 0, 0, 0, 2, 2, 4])

Eb = mat([0, 1, 0], [0, 0, 0], [0, 0, 0])   # block (2+1) embedding
g.check("thm:sphere: the non-principal block embedding has ker(ad_e) of "
      "dimension 5 > 3: it carries partition data (multiplicities)",
      kernel_dim(ad_matrix(Eb)) == 5)

# ---------------------------------------------------------------------------
# Part D: the boundary mode space as matrix (prop:matrix) and the I-state's
# embedding-insensitivity
# (prop:consistency(iii)), on small Fock spaces
# ---------------------------------------------------------------------------

NW = 5


def popcount(m):
    return bin(m).count("1")


def psi_dag_psi(a, b, statevec):
    out = {}
    for s, c in statevec.items():
        if not (s >> b) & 1:
            continue
        sgn1 = -1 if popcount(s & ((1 << b) - 1)) % 2 else 1
        s1 = s & ~(1 << b)
        if (s1 >> a) & 1:
            continue
        sgn2 = -1 if popcount(s1 & ((1 << a) - 1)) % 2 else 1
        out[s1 | (1 << a)] = out.get(s1 | (1 << a), Fraction(0)) + \
            Fraction(sgn1 * sgn2) * c
    return {s: c for s, c in out.items() if c != 0}


def bilin_comm(i, j, k, l, s):
    sv = {s: Fraction(1)}
    t1 = psi_dag_psi(i, j, psi_dag_psi(k, l, sv))
    t2 = psi_dag_psi(k, l, psi_dag_psi(i, j, sv))
    out = dict(t1)
    for st, c in t2.items():
        out[st] = out.get(st, Fraction(0)) - c
    return {st: c for st, c in out.items() if c != 0}


ok = True
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                for s in range(1 << NW):
                    lhs = bilin_comm(i, j, k, l, s)
                    rhs = {}
                    if j == k:
                        for st, c in psi_dag_psi(i, l, {s: Fraction(1)}).items():
                            rhs[st] = rhs.get(st, Fraction(0)) + c
                    if l == i:
                        for st, c in psi_dag_psi(k, j, {s: Fraction(1)}).items():
                            rhs[st] = rhs.get(st, Fraction(0)) - c
                    rhs = {st: c for st, c in rhs.items() if c != 0}
                    ok = ok and lhs == rhs
g.check("prop:matrix: [E_ij, E_kl] = delta_jk E_il - delta_li E_kj as operator "
      "identities on the full 5-mode Fock space (indices over three modes)", ok)

ok = True
for i in range(NW):
    for j in range(NW):
        for k in range(NW):
            img = psi_dag_psi(i, j, {1 << k: Fraction(1)})
            expect = {1 << i: Fraction(1)} if j == k else {}
            ok = ok and img == expect
g.check("prop:matrix: on the one-particle subspace E_ij acts as the matrix "
      "unit e_ij (the boundary modes' bilinears restrict onto Mat_n)", ok)

# I-state insensitivity: rotate by the rational orthogonal
# U = [[3/5,4/5,0],[-4/5,3/5,0],[0,0,1]]; the state checks follow below
# (invariance at equal occupancies, a control at unequal ones)
U = mat([Fraction(3, 5), Fraction(4, 5), 0],
        [Fraction(-4, 5), Fraction(3, 5), 0],
        [0, 0, 1])


def gamma_U(statevec):
    """Second-quantised U on the 3-mode Fock space (8-dim), exact."""
    out = {}
    for s, c in statevec.items():
        modes = [k for k in range(3) if (s >> k) & 1]
        # expand product of rotated creation operators applied to vacuum
        terms = {0: c}
        for m_ in modes:
            new = {}
            for st, cc in terms.items():
                for tgt in range(3):
                    if U[tgt][m_] == 0:
                        continue
                    # creation of tgt on st:
                    if (st >> tgt) & 1:
                        continue
                    sgn = -1 if popcount(st & ((1 << tgt) - 1)) % 2 else 1
                    new_st = st | (1 << tgt)
                    new[new_st] = new.get(new_st, Fraction(0)) + \
                        Fraction(sgn) * U[tgt][m_] * cc
            terms = new
        for st, cc in terms.items():
            out[st] = out.get(st, Fraction(0)) + cc
    return {st: cc for st, cc in out.items() if cc != 0}


ok = True
for s in range(8):
    img = gamma_U({s: Fraction(1)})
    norm = sum(c * c for c in img.values())
    ok = ok and norm == 1  # Gamma(U) isometric on basis states (U orthogonal)
    ok = ok and all(popcount(t) == popcount(s) for t in img)
g.check("prop:consistency(iii): the second-quantised rational rotation is "
      "exact, isometric and particle-number preserving", ok)

# the state itself: Gamma(U) rho Gamma(U)^T computed entrywise.  At equal
# occupancies (the degenerate multiplet) the quasi-free product state must be
# invariant; at unequal occupancies the same rotation must move it, which is
# the degeneracy hypothesis of clause (iii) made visible.
G8 = [[Fraction(0)] * 8 for _ in range(8)]
for s_ in range(8):
    for t_, c_ in gamma_U({s_: Fraction(1)}).items():
        G8[t_][s_] = c_


def conjugated(diag):
    """Gamma(U) diag(w) Gamma(U)^T as a full 8x8 rational matrix."""
    return [[sum(G8[a][s_] * diag[s_] * G8[b][s_] for s_ in range(8))
             for b in range(8)] for a in range(8)]


n_eq = Fraction(1, 4)
rho_eq = [n_eq ** popcount(s_) * (1 - n_eq) ** (3 - popcount(s_))
          for s_ in range(8)]
rho_eq_t = conjugated(rho_eq)
g.check("prop:consistency(iii): Gamma(U) rho Gamma(U)^T = rho entrywise for "
      "the equal-occupancy quasi-free product state: the I-state itself is "
      "invariant, embedding-insensitive",
      all(rho_eq_t[a][b] == (rho_eq[a] if a == b else Fraction(0))
          for a in range(8) for b in range(8)))

n_mode = (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4))
rho_ne = []
for s_ in range(8):
    w_ = Fraction(1)
    for k_ in range(3):
        w_ *= n_mode[k_] if (s_ >> k_) & 1 else (1 - n_mode[k_])
    rho_ne.append(w_)
rho_ne_t = conjugated(rho_ne)
g.check("prop:consistency(iii) control: at unequal occupancies on the "
      "rotated pair the same rotation moves the state (degeneracy is what "
      "the hypothesis buys)",
      any(rho_ne_t[a][b] != (rho_ne[a] if a == b else Fraction(0))
          for a in range(8) for b in range(8)))

# ---------------------------------------------------------------------------
# Part E: dynamics (asm:spreading, asm:delay)
# ---------------------------------------------------------------------------

g.check("asm:spreading/asm:delay: beta/(2 pi) = 1/kappa = 4M: the "
      "scrambling coefficient is exact",
      beta / (num(2) * PI) == num(4) * M
      and (num(1) / kappa) == num(4) * M)


# ---------------------------------------------------------------------------
# Part F (v1.8, revised v1.10): the calibration factorised, and the quarter
# examined (Section 4.1, Props 4.8 to 4.13).  Sixteen checks, exact monomials
# and blade arithmetic; ln 2 enters only as a formal indeterminate L.  The
# transcendence of ln 2 (Hermite-Lindemann) is an import the paper states as
# such; no check here certifies it.
# ---------------------------------------------------------------------------

r_h = num(2) * M
A_h = num(16) * PI * M * M
S_bh = num(4) * PI * M * M
beta_m = num(8) * PI * M
slice_t = num(8) * PI * M
N_slice = slice_t * beta_m
g.check("Prop 4.8(i),(ii): slice cells per unit Killing time 8 pi M = 4 pi r_h = A/r_h; per modular period "
      "N_slice = 64 pi^2 M^2 and N_slice/S_BH = 16 pi (both at leading order in r_c/2M, as Prop 3.3)",
      slice_t == num(4) * PI * r_h and slice_t == A_h / r_h
      and N_slice == num(64) * PI * PI * M * M and N_slice / S_bh == num(16) * PI)
g.check("Prop 4.8(iii): 16 pi = (beta/r_h)(A/S_BH) = 4 pi x 4, with beta/r_h = 2 pi/(kappa r_h) universal",
      beta_m / r_h == num(4) * PI and A_h / S_bh == num(4)
      and (beta_m / r_h) * (A_h / S_bh) == num(16) * PI
      and num(2) * PI / ((num(1) / (num(2) * r_h)) * r_h) == num(4) * PI)
P1, P3 = N_slice, A_h
g.check("Prop 4.9: P1 (one fermion per slice cell) returns 16 pi S_BH and P3 (horizon-normalised sphere, once per "
      "period) returns A = 4 S_BH", P1 / S_bh == num(16) * PI and P3 / S_bh == num(4))
rt2 = [Fraction(1), Fraction(-1)]                       # (r^{1/2} sqrt(A))^2 = r (1/r - 1) = 1 - r
g.check("Prop 4.9 (P3): the horizon-normalised t-coframe squared is the polynomial 1 - r, value 1 at the exceptional "
      "set, and the sphere weight r^{-1} r = 1: the coframe there is (dt, r_h dtheta, r_h sin theta dphi)",
      g.peval(rt2, Fraction(0)) == 1 and g.peval(rt2, Fraction(1, 2)) == Fraction(1, 2)
      and (Mono(a=-1) * Mono(a=1)) == num(1))
c_curv = TWO.pow(Fraction(1, 3))
c_kret = (TWO * TWO * TWO * TWO * THREE).pow(Fraction(1, 6))
c_prop = (THREE * THREE / TWO).pow(Fraction(1, 3))
g.check("Prop 4.9 (P1): the slice count scales as c_0^{3/2}: the proper-time scheme returns 3/2 times the curvature "
      "scheme's count and the Kretschmann scheme 2^{1/2} 3^{1/4} = 12^{1/4}, an irrational multiple",
      (c_prop / c_curv).pow(Fraction(3, 2)) == num(Fraction(3, 2))
      and (c_kret / c_curv).pow(Fraction(3, 2)) == Mono(a=Fraction(1, 2), b=Fraction(1, 4))
      and (c_kret / c_curv).pow(Fraction(3, 2)).a.denominator != 1)
ok = True
for a_exp in (Fraction(1), Fraction(-2), Fraction(3, 2), Fraction(1, 3)):
    pc, pk, pp = c_curv.pow(a_exp), c_kret.pow(a_exp), c_prop.pow(a_exp)
    ok = ok and not (pc == pk) and not (pc == pp) and not (pk == pp)
g.check("Prop 4.10: for a != 0 the scheme constants c_0^a differ pairwise across the three schemes (a = 1, -2, 3/2, 1/3), "
      "so a count carrying r_c^a is scheme-bound and cannot equal the scheme-free S_BH", ok)
def kret_rational(a_exp):
    m = c_kret.pow(a_exp)                     # 48^{a/6} = 2^{2a/3} 3^{a/6}
    return m.a.denominator == 1 and m.b.denominator == 1
g.check("Prop 4.10: the Kretschmann constant 48^{a/6} = 2^{2a/3} 3^{a/6} to a rational power a is rational iff "
      "a is a multiple of 6: irrational at a = 1/4, 1/2, 3/4, 3/2 (= 2 * 3^{1/4}), 3; rational at a = 0, 6, -6",
      all(not kret_rational(a_exp) for a_exp in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(3, 2), Fraction(3)))
      and all(kret_rational(a_exp) for a_exp in (Fraction(0), Fraction(6), Fraction(-6)))
      and c_kret.pow(Fraction(3, 2)) == Mono(a=Fraction(1), b=Fraction(1, 4)))
r_star = r_h / num(2)
g.check("Prop 4.10: the two cutoff-free scales, as arithmetic: at r_h the sphere carries A = 4 S_BH cells and the "
      "residue is 1/4; at r_* = r_h/2 = M it carries 4 pi M^2 = S_BH cells and the residue is 1",
      num(4) * PI * r_h * r_h == A_h and S_bh / A_h == num(Fraction(1, 4))
      and r_star == M and num(4) * PI * r_star * r_star == S_bh and S_bh / (num(4) * PI * r_star * r_star) == num(1))
# pair = mode = qubit: two ladder pairs in Cl(2,4)
sq24 = g.sig(2, 4)
e6 = [g.gen(i) for i in range(6)]
v1 = g.scal(Fraction(1, 2), g.add(e6[0], e6[2])); w1 = g.scal(Fraction(1, 2), g.sub(e6[0], e6[2]))
v2 = g.scal(Fraction(1, 2), g.add(e6[1], e6[3])); w2 = g.scal(Fraction(1, 2), g.sub(e6[1], e6[3]))
def acomm24(x, y):
    return g.add(g.mul(x, y, sq24), g.mul(y, x, sq24))
one24 = g.sc(Fraction(1))
g.check("Prop 4.11: two ladder pairs in Cl(2,4), on two orthogonal hyperbolic planes, satisfy the CAR of two modes "
      "(all ten anticommutators): a pair is one fermionic mode, one qubit, no hidden factor of two",
      g.eq(acomm24(v1, w1), one24) and g.eq(acomm24(v2, w2), one24)
      and all(g.is_zero(acomm24(x, y)) for x, y in ((v1, w2), (v2, w1), (v1, v1), (w1, w1), (v2, v2), (w2, w2), (v1, v2), (w1, w2))))
# the calibration residue kappa_c in each convention: N_epoch = kappa_c * A * 1; ln 2 formal as the exponent of L in a dict {L-power: Mono}
kappa_nat = S_bh / A_h
g.check("Prop 4.12(i): 1-nat convention: N_epoch = S_BH (Cor 4.4(2)) gives kappa_c = S_BH/A = 1/4", kappa_nat == num(Fraction(1, 4)))
N_cap = {-1: S_bh}                                     # N ln 2 = S_BH  =>  N = S_BH L^{-1}
kappa_cap = {k: v / A_h for k, v in N_cap.items()}
g.check("Prop 4.12(ii): capacity convention: N ln 2 = S_BH gives kappa_c = (1/4) L^{-1} = 1/(4 ln 2), one mode per "
      "4 ln 2 Planck areas per period", kappa_cap == {-1: num(Fraction(1, 4))})
thinning_cap = {1: N_slice / S_bh}                     # N_slice / (S_BH / ln 2) = 16 pi ln 2
g.check("Prop 4.12(iii): the physical thinning is 16 pi ln 2 (the 1-nat 16 pi times L), the two conventions differing "
      "by exactly ln 2", thinning_cap == {1: num(16) * PI})
hom = {s: -2 * s - 2 for s in (-2, -1, 1, 2)}
g.check("Prop 4.12(iv): the helicity lift's homogeneities -2s-2 at s = +-1, +-2 are -4, 0, -6, +2, pairwise distinct: "
      "no single channel contains both helicities (that one boundary mode registers one helicity, so the capacity per "
      "mode is ln 2 not 2 ln 2, is the lift's modelling joint J3, not tested here)",
      hom == {-2: 2, -1: 0, 1: -4, 2: -6} and len(set(hom.values())) == 4)
g.check("Prop 4.13: the natural rules' residues kappa_c = N_epoch/A in the 1-nat convention are 4 pi (P1) and 1 (P3), "
      "neither the target 1/4", P1 / A_h == num(4) * PI and P3 / A_h == num(1)
      and not (P1 / A_h == num(Fraction(1, 4))) and not (P3 / A_h == num(Fraction(1, 4))))
# the rationality closure of a counting rule's residue, on a family of rules
# built from the paper's objects: modes per cell, cells of the exceptional set
# (A divided by a cell area that is a rational multiple of an integer power of
# pi), ticks per period, all L-free; the residue is N_epoch/A carried as a dict
# {L-power: Mono} like kappa_cap above
rules = []
for mpc in (num(1), num(Fraction(1, 2)), num(3), num(Fraction(1, 4))):
    for cell in (num(1), PI, num(4) * PI, num(Fraction(1, 2)) / PI, PI * PI):
        for ticks in (num(1), num(2), num(Fraction(1, 2)), num(Fraction(3, 7))):
            n_epoch = {0: mpc * (A_h / cell) * ticks}
            rules.append({k: v / A_h for k, v in n_epoch.items()})
target_cap = kappa_cap                                # {-1: 1/4}
target_nat = {0: kappa_nat}                           # {0: 1/4}
g.check("Prop 4.13: on 80 counting rules built from the paper's objects (rational modes per cell, cell areas q pi^k, "
      "rational ticks per period), every residue kappa_c = N_epoch/A is dimensionless with integer pi-exponent "
      "and rational coefficient, i.e. q pi^k with no ln 2; none equals the capacity target (1/4) L^{-1} as a formal "
      "expression in L, while the 1-nat target 1/4 is reached (the rule 1/4 mode per horizon cell, once per period): "
      "the formal exclusion is numerical at k = 0 by the imported transcendence of ln 2, not certified here",
      len(rules) == 80
      and all(list(r.keys()) == [0] and r[0].e == 0 and r[0].p.denominator == 1
              and isinstance(r[0].c, Fraction) for r in rules)
      and all(r != target_cap for r in rules)
      and any(r == target_nat for r in rules)
      and target_cap != target_nat
      and {0: P1 / A_h} in rules and {0: P3 / A_h} in rules)
g.check("Rem 4.14: the prediction in the capacity convention, nu = 1/(16 pi ln 2), is kappa_c/(4 pi) with kappa_c = 1/(4 ln 2): "
      "the same statement as nu = 1/16 pi in the 1-nat convention, one ln 2 apart",
      {k: v / (num(4) * PI) for k, v in kappa_cap.items()} == {-1: num(Fraction(1, 16)) / PI}
      and kappa_nat / (num(4) * PI) == num(Fraction(1, 16)) / PI)

# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------

print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    raise SystemExit(1)
print("All checks pass.")
