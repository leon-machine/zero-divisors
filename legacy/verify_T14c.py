#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T14c.py: machine verification for T14c, "The Matter in the Dark Towers".

Exact arithmetic throughout (fractions.Fraction, and a small multivariate polynomial ring over Q
used to verify identities symbolically, as polynomial identities in the coordinates of the
spinors), except Part K, which is labelled DECIMAL and gives the cosmological estimates in floating
point. Imports the series library GA.py (Clifford engine, exact linear algebra, check harness).

Parts, keyed to the paper:
  A  Section 3: the eight towers' constituent fields (commutants of the spin action), at tower and
     conformal level; the ambient pseudoscalars.
  B  Section 3: the norm law j(psi x) = N(x) j(psi), the mass laws (where mass begins), positivity.
  C  Section 3: the ladder (momentum-preserving mixings are the F-unitary group).
  D  Section 4: the ladder pairs; the third pair and its unit at r = 3 and r = 5.
  E  Section 5: the automorphism algebras of the hierarchies.
  F  Section 6: content: weights, lattices, the neutral row.
  G  Section 6: anomaly arithmetic (2+1 parity anomaly; 5D Chern-Simons integrality).
  H  Section 7: the residue-7 complex unit.
  I  Section 8: the mirror: the even isomorphism, I4' = I4, I6' = -I6, the real forms.
  J  Section 10: the sterile towers' kinematics.
  K  Sections 8, 9, 11: DECIMAL estimates.
  L  The supplementary derivation scripts deposited with the paper (run if present).

Run: python verify_T14c.py   (GA.py is found in this folder or any folder above it, up to four levels).
"""

import os as _os
import sys
for _k in range(0, 5):
    sys.path.append(_os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), *(['..'] * _k))))

import math
import random
import subprocess
from fractions import Fraction as F
from itertools import combinations, product

import GA
from GA import mul, add, sig, gen, reverse, grade_inv

NCHECK = [0]


def check(label, ok):
    NCHECK[0] += 1
    GA.check(label, bool(ok))


rng = random.Random(20261020)


def rq():
    return F(rng.randint(-6, 6), rng.randint(1, 3))


# =====================================================================================
# A small polynomial ring over Q, so that GA.mul can multiply multivectors with symbolic
# coefficients. An identity verified with it is a polynomial identity: it holds for every
# value of the coordinates, not on samples.
# =====================================================================================

class Poly(object):
    __slots__ = ('t',)

    def __init__(self, t=None):
        self.t = {k: v for k, v in (t or {}).items() if v != 0}

    @staticmethod
    def var(i, n):
        e = [0] * n
        e[i] = 1
        return Poly({tuple(e): F(1)})

    def _co(self, o):
        if isinstance(o, Poly):
            return o
        o = F(o)
        if o == 0:
            return Poly()
        n = len(next(iter(self.t))) if self.t else 0
        return Poly({(0,) * n: o})

    def __add__(self, o):
        o = self._co(o)
        if not self.t:
            return o
        if not o.t:
            return self
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, 0) + v
        return Poly(r)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()})

    def __sub__(self, o):
        return self + (-self._co(o))

    def __rsub__(self, o):
        return self._co(o) + (-self)

    def __mul__(self, o):
        if not isinstance(o, Poly):
            o = F(o)
            return Poly({k: v * o for k, v in self.t.items()}) if o != 0 else Poly()
        r = {}
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                r[k] = r.get(k, 0) + v1 * v2
        return Poly(r)

    __rmul__ = __mul__

    def __eq__(self, o):
        return (self - self._co(o)).t == {}

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return id(self)


def is_zero_mv(x):
    return all(v == 0 for v in x.values())


def mv_eq(x, y):
    keys = set(x) | set(y)
    return all((x.get(k, 0) - y.get(k, 0)) == 0 for k in keys)


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def scal_mv(c, x):
    return {b: c * v for b, v in x.items()}


# =====================================================================================
# Exact linear algebra on real matrices (lists of Fractions)
# =====================================================================================

def kernel_sparse(rows, ncols):
    piv = {}
    for r in rows:
        r = {k: v for k, v in r.items() if v != 0}
        while r:
            hit = [c for c in r if c in piv]
            if not hit:
                break
            c = min(hit)
            fct = r[c]
            for k, v in piv[c].items():
                r[k] = r.get(k, 0) - fct * v
            r = {k: v for k, v in r.items() if v != 0}
        if r:
            c = min(r)
            fct = r[c]
            piv[c] = {k: v / fct for k, v in r.items()}
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    order = sorted(piv, reverse=True)
    for fv in free:
        x = [F(0)] * ncols
        x[fv] = F(1)
        for c in order:
            s = F(0)
            for k, v in piv[c].items():
                if k != c:
                    s += v * x[k]
            x[c] = -s
        basis.append(x)
    return basis


def rank(vecs):
    return GA.rank_of_vectors([list(v) for v in vecs]) if vecs else 0


def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m) if A[i][k] != 0), F(0)) for j in range(p)] for i in range(n)]


def madd(A, B, s=1):
    return [[a + s * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mscal(c, A):
    return [[c * x for x in r] for r in A]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n):
    return [[F(0)] * n for _ in range(n)]


def flat(A):
    return [x for r in A for x in r]


def unflat(v, n):
    return [list(v[i * n:(i + 1) * n]) for i in range(n)]


def comm(A, B):
    return madd(mm(A, B), mm(B, A), -1)


def is_scalar(A):
    n = len(A)
    return all(A[i][j] == (A[0][0] if i == j else 0) for i in range(n) for j in range(n))


def commutant(gens, n):
    rows = []
    for G in gens:
        for i in range(n):
            for j in range(n):
                r = {}
                for k in range(n):
                    if G[k][j] != 0:
                        r[i * n + k] = r.get(i * n + k, 0) + G[k][j]
                    if G[i][k] != 0:
                        r[k * n + j] = r.get(k * n + j, 0) - G[i][k]
                rows.append(r)
    return [unflat(v, n) for v in kernel_sparse(rows, n * n)]


def division_type(basis):
    """Return 'R', 'C' or 'H' if the real matrix algebra spanned by basis is that division
    algebra (dimension 1, 2 or 4, every trace-free element squaring to a negative scalar),
    else a description."""
    d = len(basis)
    n = len(basis[0])
    if d == 1:
        return 'R'
    I = eye(n)
    pure = []
    for B in basis:
        t = sum(B[i][i] for i in range(n)) / n
        P = madd(B, mscal(t, I), -1)
        if any(x != 0 for x in flat(P)):
            if rank([flat(Q) for Q in pure + [P]]) > len(pure):
                pure.append(P)
    if len(pure) != d - 1:
        return 'dim %d (not a division algebra)' % d
    G = []
    for P in pure:
        row = []
        for Qm in pure:
            S2 = mscal(F(1, 2), madd(mm(P, Qm), mm(Qm, P)))
            if not is_scalar(S2):
                return 'dim %d (not a division algebra)' % d
            row.append(S2[0][0])
        G.append(row)
    sg = GA.congruence_signature(G)
    if sg[0] == 0 and sg[2] == 0:
        return {2: 'C', 4: 'H'}.get(d, 'dim %d' % d)
    return 'dim %d, square-form signature %s (not a division algebra)' % (d, sg)


class Ideal(object):
    """Left ideal Cl(p,q) f of a primitive idempotent f of the EVEN subalgebra (even_only=True)
    or of the whole algebra; reps = a basis e_K f; lmat(x) = matrix of left multiplication."""

    def __init__(self, p, q, even_only):
        self.p, self.q = p, q
        self.n = p + q
        self.S = sig(p, q)
        n = self.n
        blades = GA.all_blades(n)
        cands = [b for b in blades if len(b) > 0 and (len(b) % 2 == 0 or not even_only)]
        cands = [b for b in cands if mul({b: F(1)}, {b: F(1)}, self.S) == {(): F(1)}]
        f = {(): F(1)}
        chosen = []
        dim = 2 ** n
        for b in cands:
            if not all(GA.commutes({b: F(1)}, {c: F(1)}, self.S) for c in chosen):
                continue
            f2 = mul(f, {(): F(1, 2), b: F(1, 2)}, self.S)
            d2 = rank([[mul({K: F(1)}, f2, self.S).get(bb, F(0)) for bb in blades] for K in blades])
            if 0 < d2 < dim:
                f, dim, chosen = f2, d2, chosen + [b]
        self.f = f
        reps, cls_of = [], {}
        for K in blades:
            v = mul({K: F(1)}, f, self.S)
            items = sorted(v.items())
            s = 1 if items[0][1] > 0 else -1
            key = tuple((b, c * s) for b, c in items)
            if key not in cls_of:
                cls_of[key] = len(reps)
                reps.append((K, v))
        self.reps = reps
        self.N = len(reps)
        self.parity = [len(K) % 2 for K, _ in reps]

    def lmat(self, x):
        N = self.N
        M = zeros(N)
        for j, (K, v) in enumerate(self.reps):
            rem = dict(mul(x, v, self.S))
            while rem:
                b0 = min(rem)
                for i, (K2, v2) in enumerate(self.reps):
                    if b0 in v2:
                        c = rem[b0] / v2[b0]
                        M[i][j] += c
                        for b, cc in v2.items():
                            rem[b] = rem.get(b, F(0)) - c * cc
                        rem = {b: cc for b, cc in rem.items() if cc != 0}
                        break
                else:
                    raise AssertionError('decomposition failed')
        return M


def omega(n):
    return {tuple(range(n)): F(1)}


def restrict(A, idx):
    return [[A[i][j] for j in idx] for i in idx]


def spin_field(p, q):
    """Commutant of the even subalgebra (generated by e_0 e_a) on the even ideal T = Cl^0 f0."""
    I0 = Ideal(p, q, even_only=True)
    n = p + q
    G = [I0.lmat(gen(a)) for a in range(n)]
    ev = [i for i in range(I0.N) if I0.parity[i] == 0]
    od = [i for i in range(I0.N) if I0.parity[i] == 1]
    spin = [mm(G[0], G[a]) for a in range(1, n)]
    assert all(X[i][j] == 0 for X in spin for i in od for j in ev)
    C = commutant([restrict(X, ev) for X in spin], len(ev))
    return division_type(C), len(ev), I0, G


class Span(object):
    def __init__(self):
        self.piv = {}
        self.dim = 0

    def add(self, v):
        r = {i: x for i, x in enumerate(v) if x != 0}
        while r:
            hit = [c for c in r if c in self.piv]
            if not hit:
                break
            c = min(hit)
            fct = r[c]
            for k, x in self.piv[c].items():
                r[k] = r.get(k, 0) - fct * x
            r = {k: x for k, x in r.items() if x != 0}
        if r:
            c = min(r)
            fct = r[c]
            self.piv[c] = {k: x / fct for k, x in r.items()}
            self.dim += 1
            return True
        return False


def lie_closure(gens, cap=200):
    sp = Span()
    basis = []
    for g in gens:
        if sp.add(flat(g)):
            basis.append(g)
    changed = True
    while changed and len(basis) < cap:
        changed = False
        nb = len(basis)
        for i in range(nb):
            for j in range(i):
                c = comm(basis[i], basis[j])
                if sp.add(flat(c)):
                    basis.append(c)
                    changed = True
    return basis


# =====================================================================================
# Spinor ideals of the tower algebra Cl^0(V), symbolic elements
# =====================================================================================

def even_prim(p, q):
    S = sig(p, q)
    n = p + q
    ev = [b for b in GA.all_blades(n) if len(b) % 2 == 0]
    cands = [b for b in ev if len(b) > 0 and mul({b: F(1)}, {b: F(1)}, S) == {(): F(1)}]
    f = {(): F(1)}
    chosen = []

    def dim(f_):
        return rank([[mul({K: F(1)}, f_, S).get(b, F(0)) for b in ev] for K in ev])
    d = len(ev)
    for b in cands:
        if not all(GA.commutes({b: F(1)}, {c: F(1)}, S) for c in chosen):
            continue
        f2 = mul(f, {(): F(1, 2), b: F(1, 2)}, S)
        d2 = dim(f2)
        if 0 < d2 < d:
            f, d, chosen = f2, d2, chosen + [b]
    return S, n, f, ev


def ideal_basis(S, f, ev):
    vecs, B = [], []
    for K in ev:
        x = mul({K: F(1)}, f, S)
        v = [x.get(b, F(0)) for b in ev]
        if rank(vecs + [v]) > len(vecs):
            vecs.append(v)
            B.append(x)
    return B


def corner_basis(S, f, ev):
    """Basis of f Cl^0 f."""
    vecs, B = [], []
    for K in ev:
        x = mul(mul(f, {K: F(1)}, S), f, S)
        v = [x.get(b, F(0)) for b in ev]
        if any(c != 0 for c in v) and rank(vecs + [v]) > len(vecs):
            vecs.append(v)
            B.append(x)
    return B


def sym_combo(B, offset, nv):
    out = {}
    for i, b in enumerate(B):
        a = Poly.var(offset + i, nv)
        for k, v in b.items():
            out[k] = out.get(k, F(0)) + a * v
    return {k: v for k, v in out.items() if v != 0}


def tower_setup(p, q, t):
    S, n, f, ev = even_prim(p, q)
    B = ideal_basis(S, f, ev)
    C = corner_basis(S, f, ev)
    et = gen(t)
    Qt = S[t]
    inv = {b: c / Qt for b, c in et.items()}

    def dag(x):
        return mul(mul(et, reverse(x), S), inv, S)

    def j(psi):
        return grade(mul(mul(psi, et, S), reverse(psi), S), 1)

    def Q(v):
        return mul(v, v, S).get((), Poly())
    return dict(S=S, n=n, f=f, ev=ev, B=B, C=C, et=et, Qt=Qt, dag=dag, j=j, Q=Q)


CAUSAL = [  # (label, r, p, q, time index)
    ("r=7 (1,2)", 7, 1, 2, 0), ("r=1 (2,1)", 1, 2, 1, 2),
    ("r=6 (1,3)", 6, 1, 3, 0), ("r=2 (3,1)", 2, 3, 1, 3),
    ("r=5 (1,4)", 5, 1, 4, 0), ("r=3 (4,1)", 3, 4, 1, 4)]

# =====================================================================================
print("=" * 86)
print("A. The constituent fields (Section 3, thm:fields)")
print("=" * 86)
TOWERS = [  # r, tower (p,q), ambient (p,q), expected field
    (6, (1, 3), (2, 4), 'C'), (2, (3, 1), (4, 2), 'C'),
    (1, (2, 1), (3, 2), 'R'), (7, (1, 2), (2, 3), 'R'),
    (3, (4, 1), (5, 2), 'H'), (5, (1, 4), (2, 5), 'H'),
    (0, (2, 2), (3, 3), 'R'), (4, (4, 0), (5, 1), 'H'), (4, (0, 4), (1, 5), 'H')]
amb_ok, tow_ok, agree_ok = True, True, True
rows_out = []
for r, (p, q), (P, Qq), exp in TOWERS:
    fa, dT, _, _ = spin_field(P, Qq)
    ft, dS, _, _ = spin_field(p, q)
    S = sig(P, Qq)
    w = omega(P + Qq)
    Qw = mul(w, w, S).get((), F(0))
    central = all(GA.commutes(w, gen(a), S) for a in range(P + Qq))
    rows_out.append((r, (p, q), (P, Qq), fa, ft, dT, dS, Qw, central))
    amb_ok = amb_ok and fa == exp
    tow_ok = tow_ok and ft == exp
    agree_ok = agree_ok and fa == ft
    print("   r=%d tower %s ambient %s: conformal field %s (dim T = %d), tower field %s (dim S = %d), "
          "Q(omega_amb) = %s, central %s" % (r, (p, q), (P, Qq), fa, dT, ft, dS, Qw, central))
check("A1 the commutant of the spin action on the conformal constituent ideal is R, C or H as the table of "
      "thm:fields states, for all eight towers (and both representatives of r = 4)", amb_ok)
check("A2 the commutant of the spin action on the tower-level spinor ideal Cl^0(V) f is the same division "
      "algebra in every tower: the constituent's field does not depend on the level", tow_ok and agree_ok)
check("A3 ideal dimensions: conformal constituent ideal 8 (four-dimensional towers), 4 (three), 16 (five); "
      "tower spinor ideal 2 (R), 4 (C), 8 (H) in the causal towers",
      all(o[5] == {3: 4, 4: 8, 5: 16}[o[1][0] + o[1][1]] for o in rows_out if o[0] not in (0, 4)) and
      all(o[6] == {'R': 2, 'C': 4, 'H': 8}[o[3]] for o in rows_out if o[0] not in (0, 4)))
check("A4 the ambient pseudoscalar: Q = -1 for (2,4), (4,2), (2,3), (5,2); Q = +1 for (3,2), (2,5), (3,3), (5,1), "
      "(1,5); central exactly in odd ambient dimension",
      all(o[7] == (-1 if o[2] in ((2, 4), (4, 2), (2, 3), (5, 2)) else 1) for o in rows_out) and
      all(o[8] == ((o[2][0] + o[2][1]) % 2 == 1) for o in rows_out))
check("A5 the field is not a function of Q(omega): r = 7 has Q(omega) = -1 and field R; r = 3 has Q(omega) = -1 "
      "and field H; r = 5 has Q(omega) = +1 and field H",
      [(o[3], o[7]) for o in rows_out if o[0] in (7, 3, 5)] == [('R', -1), ('H', -1), ('H', 1)])

# =====================================================================================
print("=" * 86)
print("B. The norm law and where mass begins (Section 3, lem:norm, thm:onset)")
print("=" * 86)
okB0 = True
for lab, r, p, q, t in CAUSAL:
    S = sig(p, q)
    et = gen(t)
    inv = {b: c / S[t] for b, c in et.items()}
    for K in GA.all_blades(p + q):
        eK = {K: F(1)}
        prod_ = mul(eK, mul(mul(et, reverse(eK), S), inv, S), S)
        okB0 = okB0 and prod_ == {(): F(S[t]) ** len(K)}
check("B0 lem:norm(i): e_K e_K^dag = Q(e_t)^|K| for every basis blade in the six causal towers; = 1 on every even "
      "blade, so <x x^dag>_0 is the sum of squares of the coordinates of an even x", okB0)
okB1 = okB2 = okB3 = okB4 = okB5 = okB6 = True
for lab, r, p, q, t in CAUSAL:
    T = tower_setup(p, q, t)
    S, f, B, C, dag, j, Qf, Qt = T['S'], T['f'], T['B'], T['C'], T['dag'], T['j'], T['Q'], T['Qt']
    d, c = len(B), len(C)
    nv = 2 * d + c
    psi1 = sym_combo(B, 0, nv)
    psi2 = sym_combo(B, d, nv)
    x = sym_combo(C, 2 * d, nv)
    # dagger fixes f; x^dag x = N(x) f with N(x) = <x x^dag>_0 * 2
    xdx = mul(dag(x), x, S)
    xxd = mul(x, dag(x), S)
    Nx = xdx.get((), Poly()) * 2
    okB1 = okB1 and mv_eq(dag(f), f) and mv_eq(xdx, scal_mv(Nx, f)) and mv_eq(xxd, scal_mv(Nx, f))
    # norm law
    okB2 = okB2 and mv_eq(j(mul(psi1, x, S)), scal_mv(Nx, j(psi1)))
    # N(x) is a sum of squares of x's coordinates times a positive constant (N positive definite)
    sq = Poly()
    for i in range(c):
        v = Poly.var(2 * d + i, nv)
        sq = sq + v * v
    lead = Nx.t.get(tuple(2 if k == 2 * d else 0 for k in range(nv)), F(0))
    okB3 = okB3 and lead > 0 and Nx == sq * lead
    n = p + q
    if n in (3, 4):
        alt = is_zero_mv(mul(reverse(psi1), psi1, S))
        null = Qf(j(psi1)) == 0
        xx = mul(reverse(psi1), psi2, S)
        law = Qf(add(j(psi1), j(psi2))) == mul(xx, dag(xx), S).get((), Poly()) * (2 * Qt)
        okB4 = okB4 and alt and null and law
        print("   %s: reversion pairing alternating %s; j(psi) null %s; Q(j1 + j2) = 2 Q(e_t) <x x^dag>, "
              "x = rev(psi1) psi2: %s" % (lab, alt, null, law))
    else:
        xx = mul(reverse(psi1), psi1, S)
        law = Qf(j(psi1)) == mul(xx, dag(xx), S).get((), Poly()) * (F(1, 2) * Qt)
        okB5 = okB5 and law
        print("   %s: Q(j(psi)) = (1/2) Q(e_t) <x x^dag>, x = rev(psi) psi: %s" % (lab, law))
        # a nonzero massless constituent exists: search small integer combinations
        found = None
        for coeffs in product((-1, 0, 1), repeat=d):
            if all(cf == 0 for cf in coeffs):
                continue
            ps = {}
            for cf, b in zip(coeffs, B):
                if cf:
                    ps = add(ps, scal_mv(F(cf), b))
            if ps and mul(reverse(ps), ps, S) == {}:
                found = ps
                break
        okB6 = okB6 and found is not None
    print("   %s: dim S = %d, dim f Cl0 f = %d" % (lab, d, c))
check("B1 the adjoint x^dag = e_t rev(x) e_t^-1 fixes f, and for x in f Cl0(V) f, x^dag x = x x^dag = N(x) f "
      "(polynomial identity, six causal towers)", okB1)
check("B2 lem:norm: j(psi x) = N(x) j(psi) for psi in the spinor ideal and x in f Cl0(V) f (polynomial identity)", okB2)
check("B3 N(x) is a positive multiple of the sum of the squares of x's coordinates: the field's norm is "
      "positive definite", okB3)
check("B4 thm:onset(i): in dimensions three and four the reversion pairing is alternating, every single "
      "constituent's momentum is null, and Q(j(psi1) + j(psi2)) = 2 Q(e_t) <x x^dag>_0 with x = rev(psi1) psi2 "
      "(polynomial identity in both spinors' coordinates; r = 7, 1, 6, 2)", okB4)
check("B5 thm:onset(ii): in dimension five Q(j(psi)) = (1/2) Q(e_t) <x x^dag>_0 with x = rev(psi) psi "
      "(polynomial identity; r = 5, 3)", okB5)
check("B6 thm:onset(ii): in dimension five a nonzero constituent with rev(psi) psi = 0 exists (the massless "
      "locus is not empty)", okB6)

okB7 = True
for lab, r, p, q, t in CAUSAL:
    T = tower_setup(p, q, t)
    S, B, dag, j, Qt = T['S'], T['B'], T['dag'], T['j'], T['Qt']
    psi = sym_combo(B, 0, len(B))
    lhs = mul(j(psi), T['et'], S).get((), Poly()) * Qt
    rhs = mul(psi, dag(psi), S).get((), Poly())
    okB7 = okB7 and lhs == rhs
check("B7 thm:onset (last clause): Q(e_t) (j(psi) . e_t) = <psi psi^dag>_0 (polynomial identity, six causal towers), "
      "which is nonnegative by B0: every constituent momentum lies in the same closed half-space", okB7)
# =====================================================================================
print("=" * 86)
print("C. The ladder (Section 3, thm:ladder)")
print("=" * 86)
okC1 = okC2 = True
for lab, r, p, q, t in CAUSAL:
    T = tower_setup(p, q, t)
    S, f, B, C, dag, j = T['S'], T['f'], T['B'], T['C'], T['dag'], T['j']
    d = len(B)
    nv = 2 * d
    psi1 = sym_combo(B, 0, nv)
    psi2 = sym_combo(B, d, nv)
    # a unit u of the field with N(u) = 1 other than f (where one exists), and the rotation (3/5, 4/5)
    unit = f
    for c_ in C[1:]:
        Nn = mul(dag(c_), c_, S).get((), F(0)) * 2
        if Nn == 1:
            unit = c_
            break
    cs, sn = F(3, 5), F(4, 5)
    # U = [[c f, -s u^dag], [s u, c f]] acting psi'_i = sum_k psi_k U_ki
    U = [[scal_mv(cs, f), scal_mv(-sn, dag(unit))], [scal_mv(sn, unit), scal_mv(cs, f)]]
    psis = [psi1, psi2]
    newp = [add(mul(psis[0], U[0][i], S), mul(psis[1], U[1][i], S)) for i in range(2)]
    P0 = add(j(psi1), j(psi2))
    P1 = add(j(newp[0]), j(newp[1]))
    okC1 = okC1 and mv_eq(P0, P1)
    V = [[scal_mv(F(2), f), {}], [{}, f]]       # not unitary
    newq = [add(mul(psis[0], V[0][i], S), mul(psis[1], V[1][i], S)) for i in range(2)]
    okC2 = okC2 and not mv_eq(P0, add(j(newq[0]), j(newq[1])))
check("C1 thm:ladder: an F-unitary mixing (a rotation by 3/5, 4/5 coupled through a unit of the field) "
      "preserves the total momentum of two constituents (polynomial identity, six causal towers)", okC1)
check("C2 thm:ladder: a mixing that is not F-unitary (diag(2, 1)) changes the total momentum", okC2)

# =====================================================================================
print("=" * 86)
print("D. The pairs and the third pair's unit (Section 4, thm:pairs, thm:unit)")
print("=" * 86)


def module_irr(p, q):
    I1 = Ideal(p, q, even_only=False)
    n = p + q
    G = [I1.lmat(gen(a)) for a in range(n)]
    W = I1.lmat(omega(n))
    spin = [mm(G[0], G[a]) for a in range(1, n)]
    H = commutant(spin, I1.N)
    return I1, G, W, H


def car_ok(ws, wbs, N):
    Id = eye(N)
    ok = all(madd(mm(ws[i], wbs[j]), mm(wbs[j], ws[i])) == (Id if i == j else zeros(N))
             for i in range(len(ws)) for j in range(len(ws)))
    return ok and all(madd(mm(ws[i], ws[j]), mm(ws[j], ws[i])) == zeros(N) for i in range(len(ws)) for j in range(len(ws)))


def pair_u3(ws, wbs, U, N):
    half = F(1, 2)
    Id = eye(N)
    gens = []
    for i in range(3):
        gens.append(mm(U, madd(mm(wbs[i], ws[i]), mscal(half, Id), -1)))
    for i in range(3):
        for k in range(i + 1, 3):
            gens.append(madd(mm(wbs[i], ws[k]), mm(wbs[k], ws[i]), -1))
            gens.append(mm(U, madd(mm(wbs[i], ws[k]), mm(wbs[k], ws[i]))))
    return gens


def centraliser_dim(H, gens, N):
    d = len(H)
    rows = []
    for X in gens:
        cs_ = [flat(comm(h, X)) for h in H]
        for e in range(N * N):
            rr = {k: cs_[k][e] for k in range(d) if cs_[k][e] != 0}
            if rr:
                rows.append(rr)
    return len(kernel_sparse(rows, d))


def units_in(H, N, avoid=None):
    """Elements of H squaring to -1 (from +-combinations of basis elements with trace removed)."""
    out = []
    Id = eye(N)
    for X in H:
        t = sum(X[i][i] for i in range(N)) / N
        P = madd(X, mscal(t, Id), -1)
        if not any(v != 0 for v in flat(P)):
            continue
        P2 = mm(P, P)
        if is_scalar(P2) and P2[0][0] < 0:
            c = -P2[0][0]
            num, den = c.numerator, c.denominator
            if math.isqrt(num) ** 2 == num and math.isqrt(den) ** 2 == den:
                P = mscal(1 / F(math.isqrt(num), math.isqrt(den)), P)
                out.append(P)
    return out


half = F(1, 2)
# three-dimensional ambients: two real pairs
for (p, q, lab) in ((3, 2, 'r=1'), (2, 3, 'r=7')):
    I1, G, W, H = module_irr(p, q)
    N = I1.N
    pos = [a for a in range(p + q) if sig(p, q)[a] == 1]
    neg_ = [a for a in range(p + q) if sig(p, q)[a] == -1]
    ws = [mscal(half, madd(G[pos[i]], G[neg_[i]])) for i in range(2)]
    wbs = [mscal(half, madd(G[pos[i]], G[neg_[i]], -1)) for i in range(2)]
    check("D1%s %s: Cl(%d,%d) carries two real ladder pairs (w_i, v_i) obeying the CAR, built from real "
          "hyperbolic planes; no unit is needed" % ('a' if p == 3 else 'b', lab, p, q), car_ok(ws, wbs, N))
# r = 3: Cl(5,2)
I1, G, W, H = module_irr(5, 2)
N = I1.N
Id = eye(N)
check("D2 r=3: on the 16-dimensional Cl(5,2) module the spin commutant is H and the pseudoscalar I7 lies in it, "
      "squares to -1 and commutes with every vector",
      division_type(H) == 'H' and mm(W, W) == mscal(-1, Id) and all(comm(W, g) == zeros(N) for g in G))
ws = [mscal(half, madd(G[0], G[5])), mscal(half, madd(G[1], G[6])), mscal(half, madd(G[2], mm(W, G[3])))]
wbs = [mscal(half, madd(G[0], G[5], -1)), mscal(half, madd(G[1], G[6], -1)), mscal(half, madd(G[2], mm(W, G[3]), -1))]
check("D3 r=3: three CAR pairs, two from real hyperbolic planes and the third (e2 +- I7 e3)/2 built with the "
      "internal unit I7", car_ok(ws, wbs, N))
u3 = pair_u3(ws, wbs, W, N)
check("D4 r=3: the nine generators I7 (v_i w_i - 1/2), v_i w_k - v_k w_i, I7 (v_i w_k + v_k w_i) close on a "
      "nine-dimensional Lie algebra u(3)", len(lie_closure(u3)) == 9)
check("D5 r=3: the centraliser of that u(3) in the spin commutant H is span{1, I7}, of dimension 2",
      centraliser_dim(H, u3, N) == 2)
Js = [U_ for U_ in units_in(H, N) if madd(mm(U_, W), mm(W, U_)) == zeros(N)]
J = Js[0] if Js else None
check("D6 r=3: a unit J of H with J I7 = -I7 J exists and anticommutes with every vector (it acts as the grade "
      "involution), so J w_3 J^-1 is not in the span of the w_i",
      J is not None and all(madd(mm(J, g), mm(g, J)) == zeros(N) for g in G) and
      rank([flat(x) for x in ws + [mm(mm(J, ws[2]), mscal(-1, J))]]) == 4)
cl30 = lie_closure(u3 + [J])
check("D7 r=3: u(3) together with J generates a Lie algebra of dimension 30 (not a commuting sum su(2) + u(3), "
      "dimension 12)", len(cl30) == 30)
# r = 5: Cl(2,5)
I1b, Gb, Wb, Hb = module_irr(2, 5)
Nb = I1b.N
Idb = eye(Nb)
units = units_in(Hb, Nb)
check("D8 r=5: on the 16-dimensional Cl(2,5) module the spin commutant H is also the Clifford commutant, its "
      "centre is R (no internal unit commutes with all of H), and the pseudoscalar squares to +1",
      division_type(Hb) == 'H' and all(all(comm(h, g) == zeros(Nb) for g in Gb) for h in Hb) and
      mm(Wb, Wb) == Idb and len(units) >= 2)
u_ = units[0]
v_ = next(U_ for U_ in units[1:] if madd(mm(U_, u_), mm(u_, U_)) == zeros(Nb))
posb = [a for a in range(7) if sig(2, 5)[a] == 1]
negb = [a for a in range(7) if sig(2, 5)[a] == -1]
wsb = [mscal(half, madd(Gb[posb[0]], Gb[negb[0]])), mscal(half, madd(Gb[posb[1]], Gb[negb[1]])),
       mscal(half, madd(Gb[negb[2]], mm(u_, Gb[negb[3]])))]
wbsb = [mscal(half, madd(Gb[posb[0]], Gb[negb[0]], -1)), mscal(half, madd(Gb[posb[1]], Gb[negb[1]], -1)),
        mscal(-half, madd(Gb[negb[2]], mm(u_, Gb[negb[3]]), -1))]   # sign: e_a^2 = -1 for the third pair
# the third pair: (e_a + u e_b)/2 with e_a^2 = e_b^2 = -1 needs u^2 = -1 and Q(e_a) = -1: w^2 = (e_a^2 - e_b^2)/4 = 0
check("D9 r=5: with any unit u of H, two real pairs and the third pair (e_a +- u e_b)/2 obey the CAR",
      car_ok(wsb, wbsb, Nb))
u3b = pair_u3(wsb, wbsb, u_, Nb)
check("D10 r=5: the pair algebra u(3)_u built with u is nine-dimensional and its centraliser in H is span{1, u}: "
      "the choice of u cuts Sp(1) to the U(1) that u generates",
      len(lie_closure(u3b)) == 9 and centraliser_dim(Hb, u3b, Nb) == 2)
check("D11 r=5: a second unit v anticommuting with u, adjoined to u(3)_u, generates dimension 30, as at r = 3",
      len(lie_closure(u3b + [v_])) == 30)
g_ = madd(Idb, mm(v_, u_), -1)       # g = 1 - v u carries u to v: g u = v g
check("D12 r=5: any two units are conjugate in H: (1 - v u) u = v (1 - v u), so the choices of u form the "
      "sphere Sp(1)/U(1)", mm(g_, u_) == mm(v_, g_))

# =====================================================================================
print("=" * 86)
print("E. The automorphism algebras of the hierarchies (Section 5, thm:algebras)")
print("=" * 86)


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def real_of_complex(Re, Im):
    n = len(Re)
    return [[(Re[i][j] if (a == b) else (-Im[i][j] if a == 0 else Im[i][j])) for j in range(n) for b in range(2)]
            for i in range(n) for a in range(2)]


def u_basis(m):
    """u(m) as pairs (Re, Im) of anti-hermitian matrices."""
    out = []
    Z = [[F(0)] * m for _ in range(m)]
    for i in range(m):
        Im = [r[:] for r in Z]
        Im[i][i] = F(1)
        out.append((Z, Im))
    for i in range(m):
        for k in range(i + 1, m):
            Re = [r[:] for r in Z]
            Re[i][k], Re[k][i] = F(1), F(-1)
            out.append((Re, Z))
            Im = [r[:] for r in Z]
            Im[i][k] = Im[k][i] = F(1)
            out.append((Z, Im))
    return out


def image_rank_complex(m, k):
    gens = []
    Im_ = [[F(int(i == j)) for j in range(k)] for i in range(k)]
    Zk = [[F(0)] * k for _ in range(k)]
    Imm = [[F(int(i == j)) for j in range(m)] for i in range(m)]
    Zm = [[F(0)] * m for _ in range(m)]
    for Re, Im in u_basis(m):
        gens.append(real_of_complex(kron(Re, Im_), kron(Im, Im_)))
    for Re, Im in u_basis(k):
        gens.append(real_of_complex(kron(Imm, Re), kron(Imm, Im)))
    return rank([flat(g) for g in gens])


def o_basis(m):
    out = []
    for i in range(m):
        for k in range(i + 1, m):
            A = [[F(0)] * m for _ in range(m)]
            A[i][k], A[k][i] = F(1), F(-1)
            out.append(A)
    return out


ro = rank([flat(kron(A, eye(2))) for A in o_basis(2)] + [flat(kron(eye(2), A)) for A in o_basis(2)])
check("E1 thm:algebras(i): the automorphisms A (x) B of R^2 (x) R^2 with A, B orthogonal have Lie algebra of "
      "dimension 2 = so(2) + so(2) (abelian)", ro == 2)
# kernel of O(2) x O(2): pairs (A, B) with A (x) B = 1 are (1,1), (-1,-1)
I2_, I4_ = eye(2), eye(4)
mI2 = mscal(-1, I2_)
Rt = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
Rti = [[F(3, 5), F(4, 5)], [F(-4, 5), F(3, 5)]]
Rf = [[F(1), F(0)], [F(0), F(-1)]]
check("E2 thm:algebras(i): on R^2 (x) R^2, (-1) (x) (-1) is the identity while (-1) (x) 1, a rotation R (x) R^-1 "
      "(R by 3/5, 4/5) and a reflection pair F (x) F are not: the kernel is the discrete {(1,1), (-1,-1)}",
      kron(mI2, mI2) == I4_ and kron(mI2, I2_) != I4_ and kron(Rt, Rti) != I4_ and kron(Rf, Rf) != I4_)
check("E3 thm:algebras(ii): the automorphisms of C^1 (x) C^3 have Lie algebra of dimension 9 = u(3)",
      image_rank_complex(1, 3) == 9)
check("E4 control (our tower, T12 thm:algebra): C^2 (x) C^3 gives dimension 12; and C^2 (x) C^2 would give 7",
      image_rank_complex(2, 3) == 12 and image_rank_complex(2, 2) == 7)


def gl_basis(m):
    out = []
    for i in range(m):
        for k in range(m):
            A = [[F(0)] * m for _ in range(m)]
            A[i][k] = F(1)
            out.append(A)
    return out


rgl = rank([flat(kron(A, eye(3))) for A in gl_basis(2)] + [flat(kron(eye(2), A)) for A in gl_basis(3)])


def killing_sig(basis):
    nB = len(basis)
    sz = len(basis[0])
    flats = [flat(X) for X in basis]
    sp2, piv = Span(), []
    for e in range(sz * sz):
        row = [flats[k][e] for k in range(nB)]
        if sp2.add(row):
            piv.append(e)
        if len(piv) == nB:
            break
    A = [[flats[k][e] for k in range(nB)] for e in piv]
    Aug = [A[i][:] + [F(int(i == j)) for j in range(nB)] for i in range(nB)]
    for c in range(nB):
        pr = next(r_ for r_ in range(c, nB) if Aug[r_][c] != 0)
        Aug[c], Aug[pr] = Aug[pr], Aug[c]
        pv = Aug[c][c]
        Aug[c] = [x / pv for x in Aug[c]]
        for r_ in range(nB):
            if r_ != c and Aug[r_][c] != 0:
                fc = Aug[r_][c]
                Aug[r_] = [x - fc * y for x, y in zip(Aug[r_], Aug[c])]
    Ainv = [row[nB:] for row in Aug]

    def coords(X):
        v = flat(X)
        vp = [v[e] for e in piv]
        return [sum(Ainv[i][j] * vp[j] for j in range(nB)) for i in range(nB)]
    ad = [[coords(comm(X, Y)) for Y in basis] for X in basis]
    K = [[sum(ad[i][b][a] * ad[j][a][b] for a in range(nB) for b in range(nB)) for j in range(nB)] for i in range(nB)]
    return GA.congruence_signature(K)


sl2 = [[[F(1), F(0)], [F(0), F(-1)]], [[F(0), F(1)], [F(0), F(0)]], [[F(0), F(0)], [F(1), F(0)]]]
sl3 = []
for (i, k) in [(0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1)]:
    A = [[F(0)] * 3 for _ in range(3)]
    A[i][k] = F(1)
    sl3.append(A)
sl3 += [[[F(1), F(0), F(0)], [F(0), F(-1), F(0)], [F(0), F(0), F(0)]],
        [[F(0), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(-1)]]]
k2, k3 = killing_sig(sl2), killing_sig(sl3)
check("E5 prop:kleinian: on R^2 (x) R^3 with general linear slots the automorphism algebra has dimension 12 "
      "(gl(2,R) + gl(3,R) modulo the common scalar); the Killing forms of sl(2,R) and sl(3,R) have signatures "
      "%s and %s: indefinite, no positive gauge-kinetic form" % (k2, k3),
      rgl == 12 and k2 == (2, 1, 0) and k3 == (5, 3, 0))

# =====================================================================================
print("=" * 86)
print("F. Content (Section 6)")
print("=" * 86)
# three dimensions: weights (s, p) of single slot-pair excitations are (+-1, +-1)
cells = [(s, p_) for s in (1, -1) for p_ in (1, -1)]
tensor_weights = set()
for k in range(5):
    for sub in combinations(range(4), k):
        tensor_weights.add((sum(cells[i][0] for i in sub), sum(cells[i][1] for i in sub)))
check("F1 prop:content3: every weight (s, p) in the exterior algebra of R^2 (x) R^2 (complexified) has s + p even; "
      "the weights (+-1, 0) and (0, +-1) do not occur",
      all((s + p_) % 2 == 0 for s, p_ in tensor_weights) and (1, 0) not in tensor_weights and (0, 1) not in tensor_weights)
check("F2 prop:content3: the identity component of the global form is U(1)_+ x U(1)_- with q_+- = (s +- p)/2 "
      "integral exactly on the lattice s + p even; the cell (1,1) has (q_+, q_-) = (1, 0) and (1,-1) has (0, 1)",
      all(((s + p_) % 2 == 0) == (F(s + p_, 2).denominator == 1 and F(s - p_, 2).denominator == 1)
          for s in range(-3, 4) for p_ in range(-3, 4)) and
      (F(1 + 1, 2), F(1 - 1, 2)) == (1, 0) and (F(1 - 1, 2), F(1 + 1, 2)) == (0, 1))
# five dimensions: Lambda(C^1 + C^3), Y = s - k/3
states = [(s, k) for s in (0, 1) for k in range(4)]
mult = {(s, k): math.comb(3, k) for s, k in states}
Y = {(s, k): F(s) - F(k, 3) for s, k in states}
species = {'U': [(1, 1), (0, 2)], 'D': [(0, 1), (1, 2)], 'E': [(0, 3), (1, 0)], 'N': [(0, 0), (1, 3)]}
colour = {(s, k): {0: 1, 1: 3, 2: 3, 3: 1}[k] for s, k in states}
okF4 = sum(mult.values()) == 16
for nm, (a, b) in species.items():
    okF4 = okF4 and Y[a] == -Y[b] and colour[a] == colour[b] and (1 - a[0], 3 - a[1]) == b
okF4 = okF4 and [abs(Y[species[x][0]]) for x in 'UDEN'] == [F(2, 3), F(1, 3), F(1), F(0)] and Y[(1, 3)] == 0
check("F3 prop:content5: Lambda(C^1 + C^3) has 16 states; with Y = s - k/3 the complement (s, k) -> (1 - s, 3 - k) "
      "negates Y and pairs them into four vector-like species U (3, 2/3), D (3, -1/3), E (1, -1), N (1, 0)", okF4)
# U(3) acts on the state (s, k) through the section B -> ((det B)^-1, B): the centre lambda 1_3 acts by
# lambda^(k - 3s) = lambda^(-3Y); so 3Y is an integer and 3Y + k = 3s is divisible by 3 (k = triality)
okF5 = all((3 * Y[(s, k)]).denominator == 1 and (3 * Y[(s, k)] + k) % 3 == 0 and -3 * Y[(s, k)] == k - 3 * s
           for s, k in states)
check("F4 prop:content5: through the section B -> ((det B)^-1, B) the centre of U(3) acts on (s, k) by lambda^(k - 3s) "
      "= lambda^(-3Y): 3Y is an integer tied to the triality k by 3Y + k = 0 mod 3, the U(3) lattice", okF5)

# =====================================================================================
print("=" * 86)
print("G. Anomaly arithmetic (Section 6)")
print("=" * 86)
okG1 = all((F(sg, 2) * 1 * 1).denominator == 2 for sg in (1, -1))
check("G1 prop:anomaly(i): a unit-charge two-component fermion shifts its U(1) Chern-Simons level by "
      "sign(m)/2, so with one such fermion per U(1) (the cells A and B) the bare levels are half-integers", okG1)
okG2 = all(((F(1, 2) * sA) + F(sg, 2)).denominator == 1 for sA in (1, -1, 3, -3) for sg in (1, -1))
check("G2 prop:anomaly(i): with bare level k in Z + 1/2 the effective level k + sign(m)/2 is an integer for "
      "either mass sign", okG2)
qp = [F(2), F(-1), F(-3), F(0)]          # q' = 3Y for U, D, E, N
mults = [3, 3, 1, 1]
cube = sum(m_ * q ** 3 for m_, q in zip(mults, qp))
lin = sum(m_ * q for m_, q in zip(mults, qp))
check("G3 prop:anomaly(ii): in units q' = 3Y the content U, D, E, N has sum q'^3 = %s and sum q' = %s (with "
      "multiplicities); the induced 5D Chern-Simons coefficients (1/2) sign(m) q'^3 sum to integers for every "
      "choice of mass signs" % (cube, lin),
      cube == -6 and lin == 0 and all((sum(F(sg, 2) * m_ * q ** 3 for sg, m_, q in zip(sgs, mults, qp))).denominator == 1
                                     for sgs in product((1, -1), repeat=4)))

# =====================================================================================
print("=" * 86)
print("H. The residue-7 complex unit (Section 7, prop:omega7)")
print("=" * 86)
okH1 = True
for (p, q) in ((2, 3), (3, 4), (4, 5)):
    S = sig(p, q)
    w = omega(p + q)
    okH1 = okH1 and mul(w, w, S) == {(): F(-1)} and all(GA.commutes(w, gen(a), S) for a in range(p + q))
okH2 = True
for (p, q) in ((3, 2), (4, 3), (5, 4)):
    S = sig(p, q)
    w = omega(p + q)
    okH2 = okH2 and mul(w, w, S) == {(): F(1)} and all(GA.commutes(w, gen(a), S) for a in range(p + q))
check("H1 prop:omega7(i): along the residue-7 tower (Cl(2,3), Cl(3,4), Cl(4,5)) the pseudoscalar is central and "
      "squares to -1 at every rung", okH1)
check("H2 prop:omega7(i): along the residue-1 tower (Cl(3,2), Cl(4,3), Cl(5,4)) it is central and squares to +1", okH2)
S = sig(2, 3)
w = omega(5)
x0 = {(0, 1): F(1), (2, 3): F(2), (): F(3)}
check("H3 prop:omega7(ii): the pseudoscalar of Cl(2,3) is odd, so it carries the even ideal into the odd one, and "
      "the grade involution reverses it", all(len(b) % 2 == 1 for b in mul(w, x0, S)) and grade_inv(w) == {(0, 1, 2, 3, 4): F(-1)})
cth, sth = F(3, 5), F(4, 5)
Xs, Ys = {(0, 1): F(1)}, {(2, 3): F(1)}
lhs = mul(add({(): cth}, scal_mv(sth, w)), add(Xs, mul(w, Ys, S)), S)
rhs = add(add(scal_mv(cth, Xs), scal_mv(-sth, Ys)), mul(w, add(scal_mv(sth, Xs), scal_mv(cth, Ys)), S))
check("H4 prop:omega7(iii): left multiplication by c + s omega carries X + omega Y to (cX - sY) + omega (sX + cY): "
      "on a pair of real constituents it is the slot rotation", mv_eq(lhs, rhs))

# =====================================================================================
print("=" * 86)
print("I. The mirror (Section 8, thm:mirror)")
print("=" * 86)


def phi_even(x):
    return {b: c * (-1) ** (len(b) // 2) for b, c in x.items()}


okI1 = True
for (p, q) in ((3, 1), (4, 2)):
    Sm = sig(p, q)
    So = [-x for x in Sm]          # the signature-reversed algebra on the same generators
    ev = [b for b in GA.all_blades(p + q) if len(b) % 2 == 0]
    for a in ev:
        for b in ev:
            lhs_ = phi_even(mul({a: F(1)}, {b: F(1)}, Sm))
            rhs_ = mul(phi_even({a: F(1)}), phi_even({b: F(1)}), So)
            if not mv_eq(lhs_, rhs_):
                okI1 = False
check("I1 thm:mirror(i): e_K -> (-1)^(|K|/2) e_K on even blades is an algebra isomorphism Cl0(3,1) -> Cl0(1,3) and "
      "Cl0(4,2) -> Cl0(2,4) (checked on every pair of basis blades)", okI1)
check("I2 thm:mirror(ii): it carries I4' to +I4 and I6' to -I6",
      phi_even(omega(4)) == omega(4) and phi_even(omega(6)) == {(0, 1, 2, 3, 4, 5): F(-1)})
I13 = Ideal(1, 3, even_only=False)
I31 = Ideal(3, 1, even_only=False)
c13 = commutant([I13.lmat(gen(a)) for a in range(4)], I13.N)
c31 = commutant([I31.lmat(gen(a)) for a in range(4)], I31.N)
check("I3 thm:mirror(iii): the full algebras differ: the Clifford-irreducible module of Cl(1,3) has commutant H "
      "(dimension 8 module), that of Cl(3,1) has commutant R (dimension 4 module)",
      (I13.N, division_type(c13)) == (8, 'H') and (I31.N, division_type(c31)) == (4, 'R'))

# =====================================================================================
print("=" * 86)
print("J. The sterile towers' kinematics (Section 10, prop:sterile)")
print("=" * 86)


def Q22(v):
    return v[0] ** 2 + v[1] ** 2 - v[2] ** 2 - v[3] ** 2


okJ1 = True
eta = [F(1), F(1), F(-1), F(-1)]
for _ in range(40):
    v = [rq() for _ in range(4)]
    if Q22(v) == 0:
        continue
    perp = kernel_sparse([{i: eta[i] * v[i] for i in range(4) if v[i] != 0}], 4)
    Gm = [[sum(eta[i] * a[i] * b[i] for i in range(4)) for b in perp] for a in perp]
    sg = GA.congruence_signature(Gm)
    okJ1 = okJ1 and len(perp) == 3 and sg[2] == 0 and sg[0] >= 1 and sg[1] >= 1
check("J1 prop:sterile(i): in R^(2,2) the orthogonal complement of every non-null vector (40 random) is "
      "nondegenerate and indefinite (signature (1,2) or (2,1)), so Q(w) = -Q(v)/4 has a solution w in it and "
      "v = (v/2 + w) + (v/2 - w) is a sum of two null vectors, whatever the sign of Q(v)", okJ1)
n1, n2, n3 = [1, 0, 1, 0], [1, 0, -1, 0], [-1, 0, 1, 0]
check("J2 prop:sterile(i): null vectors whose sums have both signs: Q(n1 + n2) = 4 > 0, Q(n1 + n3) = -4 < 0",
      Q22([a + b for a, b in zip(n1, n2)]) == 4 and Q22([a + b for a, b in zip(n1, n3)]) == -4 and
      Q22(n1) == Q22(n2) == Q22(n3) == 0)
check("J3 prop:sterile(ii): in R^(4,0) the only null vector is 0 (Q is a sum of four squares); 25 random vectors "
      "have Q > 0", all(sum(x * x for x in v) > 0 for v in ([rq() + F(1, 7) for _ in range(4)] for _ in range(25))))

# =====================================================================================
print("=" * 86)
print("K. DECIMAL estimates (Sections 8, 9, 11; floating point)")
print("=" * 86)
pi = math.pi
total = 1 + 2 * 4 / 3 + 2 * 8 / (3 * pi)
shares = {'mirror': 1 / total, '3D each': (4 / 3) / total, '5D each': (8 / (3 * pi)) / total}
print("   unit-ball total %.4f; fractions of the dark matter: %s" % (total, {k: round(v, 4) for k, v in shares.items()}))
check("K1 DECIMAL shares: total (11 pi + 16)/(3 pi) = 5.364; mirror 18.6%%, each 3D tower 24.9%%, each 5D tower 15.8%%; "
      "mirror plus both 5D towers 50.2%%",
      abs(total - 5.364) < 1e-3 and abs(shares['mirror'] - 0.186) < 1e-3 and abs(shares['3D each'] - 0.249) < 1e-3
      and abs(shares['5D each'] - 0.158) < 1e-3 and abs(shares['mirror'] + 2 * shares['5D each'] - 0.502) < 1e-3)
dneff_hot = (8 / 7) * (11 / 4) ** (4 / 3) + 3.044
check("K2 DECIMAL prop:P2: a Standard-Model copy at the photon temperature adds Delta N_eff = (8/7)(11/4)^(4/3) + 3.044 "
      "= %.2f at recombination" % dneff_hot, abs(dneff_hot - 7.45) < 0.01)
# survival of a symmetric sheet relic under 2D s-wave annihilation, closed form
hbarc_GeVm = 1.97327e-16
d_b = 0.98
T0 = 2.7255 * 8.617333e-14     # GeV
MP = 1.2209e19
m = 0.938
N0 = hbarc_GeVm ** 2 / (pi * d_b ** 2)          # GeV^2, comoving sheet density (a = 1 today)


def a2H(gs, gstar):
    return 1.66 * math.sqrt(gstar) * T0 ** 2 * (3.91 / gs) ** (2 / 3) / MP


lnN = 25.8
fac = [N0 * 2 / m * lnN / a2H(g, g) for g in (3.36, 10.75, 106.75)]
Pmax = [0.01 / x for x in fac]
surv = 1 / (1 + max(fac))
print("   sheet annihilation: 1/N_f = 1/N_0 + (2P/m) ln(a_f/a_i)/(a^2 H); depletion factor per unit P %.1e to %.1e; "
      "P < %.1e to %.1e keeps 99%%; survival at P = 1: %.1e" % (min(fac), max(fac), min(Pmax), max(Pmax), surv))
check("K3 DECIMAL prop:sheetsurvival: a symmetric sheet relic at R2's density keeps 99%% of its number only if the "
      "absorption probability per encounter is below about 2e-16; at P = 1 about 2e-14 survives",
      1e-16 < min(Pmax) and max(Pmax) < 4e-16 and 1e-14 < surv < 4e-14)
check("K4 DECIMAL prop:phases: in the topologically massive phase contact processes scale as (m/e^2)^2, so survival "
      "needs e^2/m > 1/sqrt(2e-16) = %.1e, which exceeds the collisionless threshold 1/1.7e-7 = %.1e"
      % (1 / math.sqrt(2e-16), 1 / 1.7e-7), 6e7 < 1 / math.sqrt(2e-16) < 8e7 and 1 / 1.7e-7 < 1 / math.sqrt(2e-16))
hbarc_eVm = 1.97327e-7
LT0 = 0.98 * 2.7255 * 8.617333e-5 / hbarc_eVm
LT_early = LT0 * (3.91 / 106.75) ** (1 / 3)
check("K5 DECIMAL prop:fiveD(i): with a co-expanding fifth direction of extent d_b, L T runs from %.0f (g_s = 106.75) "
      "to %.0f today: the Kaluza-Klein spacing pi/L stays below T/120" % (LT_early, LT0),
      380 < LT_early < 400 and 1150 < LT0 < 1180)
try:
    from scipy.integrate import quad

    def rho_level(mT):
        fn = lambda p_: p_ * p_ * math.sqrt(p_ * p_ + mT * mT) / math.expm1(math.sqrt(p_ * p_ + mT * mT))
        return quad(fn, 0, 60 + 2 * mT, limit=200)[0] / (2 * pi ** 2)

    def rho_vector5(xL, dof=3):
        tot = rho_level(0.0) * dof
        k = 1
        while True:
            mT = 2 * pi * k / xL
            if mT > 60:
                break
            tot += 2 * dof * rho_level(mT)
            k += 1
        return tot
    rho_nu1 = 7 / 8 * (4 / 11) ** (4 / 3) * pi ** 2 / 15

    def dNeff(xi, nvec):
        return nvec * rho_vector5(LT0 * xi) * xi ** 4 / rho_nu1

    def thresh(nvec):
        lo, hi = 1e-4, 1.0
        for _ in range(40):
            mid = math.sqrt(lo * hi)
            if dNeff(mid, nvec) > 0.3:
                hi = mid
            else:
                lo = mid
        return lo
    t1, t9 = thresh(1), thresh(9)
    ra = dNeff(1 / 2.51, 9)
    print("   KK-summed caps: xi < %.3f (one 5D photon), %.3f (nine vectors); route (a) %.0f" % (t1, t9, ra))
    check("K6 DECIMAL prop:fiveD(iii): with the Kaluza-Klein tower populated, Delta N_eff < 0.3 needs T_D/T_gamma < 0.085 "
          "for nine 5D vectors (0.13 for one photon), and a sector decoupled at a GeV (xi = 1/2.51) gives about 670",
          0.08 < t9 < 0.09 and 0.12 < t1 < 0.14 and 500 < ra < 900)
except ImportError:
    check("K6 DECIMAL (scipy not available: skipped, recorded as a failure)", False)
b4 = 11.0                        # pure glue: below the quark mass only the gluons run
g52max = 24 * pi ** 3 / 3.0
L_fo = LT0 * (3.91 / 61.75) ** (1 / 3) / (m / 20)
expo = 8 * pi ** 2 / (b4 * g52max / L_fo)
check("K7 DECIMAL prop:fiveD(ii): even at the strong-coupling limit for a 1 GeV quark, the four-dimensional "
      "confinement scale at T = m/20 is below pi/L by exp(-%.0f)" % expo, expo > 200)

# =====================================================================================
print("=" * 86)
print("L. Supplementary derivation scripts deposited with the paper")
print("=" * 86)
here = _os.path.dirname(_os.path.abspath(__file__))
supp = [("MIR", "verify_MIR.py"), ("D3R", "verify_D3R.py"), ("D3C", "verify_D3C.py"), ("D5C", "verify_D5C.py"),
        ("D5Q", "verify_D5Q.py"), ("STE", "verify_STE.py"), ("CHECK_ALG", "check_commutants.py"),
        ("CHECK_ALG", "check_r3_r5.py"), ("CHECK_ALG", "check_helicity_cut.py"), ("CHECK_ALG", "check_arith.py"),
        ("CHECK_COS", "check_mirror_entropy.py"), ("CHECK_COS", "check_kk_sheets.py")]
if "--no-supplement" in sys.argv:
    print("   skipped (--no-supplement)")
else:
    for folder, script in supp:
        path = _os.path.join(here, folder, script)
        if not _os.path.exists(path):
            check("L %s/%s present beside this script (run with --no-supplement to omit Part L)" % (folder, script), False)
            continue
        res = subprocess.run([sys.executable, script], cwd=_os.path.join(here, folder), capture_output=True, text=True)
        out = res.stdout
        nfail = out.count("\nFAIL ") + (1 if out.startswith("FAIL ") else 0)
        npass = out.count("\nPASS ") + (1 if out.startswith("PASS ") else 0)
        check("L %s/%s runs cleanly: %d PASS lines, %d FAIL lines" % (folder, script, npass, nfail),
              res.returncode == 0 and nfail == 0)

print()
print("verify_T14c: %d checks, %d failures" % (NCHECK[0], len(GA.FAILURES)))
if GA.FAILURES:
    for f_ in GA.FAILURES:
        print("FAILED:", f_)
    sys.exit(1)
