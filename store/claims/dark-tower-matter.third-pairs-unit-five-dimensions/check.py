"""dark-tower-matter.third-pairs-unit-five-dimensions: exact checks.

The 16-dimensional irreducible real modules of Cl(5,2) (r = 3) and Cl(2,5) (r = 5) are built as
real 16 x 16 matrices in the basis of tensor words over {I, X, Z, E} (X, Z the real symmetric Pauli
matrices, E = [[0,1],[-1,0]]); these 256 words are a basis of M_16(R), and a product of two words is
+- a word (the table is computed from the 2 x 2 matrices). Seven mutually anticommuting words with
the right squares give the generators (the Clifford relations are verified). A word commutes or
anticommutes with each generator, so commutants are spans of words, computed exactly. The module is
irreducible: its Clifford commutant is a division algebra (C for Cl(5,2), H for Cl(2,5)).

(i)   r = 3: the spin commutant (commutant of the e_0 e_a) is H; I7 lies in it, I7^2 = -1, and I7
      commutes with every vector. With Q(e_a) = Q(e_b) = +1 the third pair (e_a +- I7 e_b)/2 and two
      real pairs from hyperbolic planes obey the CAR (all relations). The nine bilinears
      I7 (v_i w_i - 1/2), v_i w_k - v_k w_i, I7 (v_i w_k + v_k w_i) close on a 9-dimensional Lie
      algebra whose centraliser in H is span{1, I7}.
(ii)  r = 3: every unit J of H anticommuting with I7 (the circle c J1 + s J2 through the basis
      units, sampled) anticommutes with every vector, sends w_i to -w_i on the real pairs and w_3
      to -wbar_3; u(3) and J generate a Lie algebra of dimension 30, not 12.
(iii) r = 5: the spin commutant H equals the Clifford commutant, its centre is R, and omega^2 = +1.
      For every sampled unit u of H (the basis units and the combinations (3/5, 4/5)) the third pair
      w_3 = (e_a + u e_b)/2, v_3 = -(e_a - u e_b)/2 with Q(e_a) = Q(e_b) = -1 joins two real pairs
      in the CAR; u(3)_u is 9-dimensional with centraliser span{1, u} in H; with a unit anticommuting
      with u it generates dimension 30. For all ordered pairs of sampled units,
      (1 - u'u) u = u' (1 - u'u), 1 - u'u is invertible unless u' = -u, where it vanishes and u' is
      reached by conjugation with a unit anticommuting with u.
"""
from fractions import Fraction as F
from itertools import product

import GA
import fock
from tp_premise import premise

# ---- the word algebra M_16(R) = M_2(R)^(x4) -----------------------------------------------
_M2 = {'I': ((1, 0), (0, 1)), 'X': ((0, 1), (1, 0)), 'Z': ((1, 0), (0, -1)), 'E': ((0, 1), (-1, 0))}


def _m2mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


_TAB = {}
for _a in 'IXZE':
    for _b in 'IXZE':
        _P = _m2mul(_M2[_a], _M2[_b])
        for _c in 'IXZE':
            for _s in (1, -1):
                if _P == tuple(tuple(_s * x for x in r) for r in _M2[_c]):
                    _TAB[(_a, _b)] = (_s, _c)
L = 4
ID = 'I' * L


def wmul(u, v):
    s, out = 1, []
    for a, b in zip(u, v):
        t, c = _TAB[(a, b)]
        s *= t
        out.append(c)
    return s, ''.join(out)


def mul(x, y):
    out = {}
    for u, a in x.items():
        for v, b in y.items():
            s, w = wmul(u, v)
            out[w] = out.get(w, F(0)) + s * a * b
    return {w: c for w, c in out.items() if c != 0}


# sparse linear combinations of words: fock's helpers are key-agnostic
add = fock.madd
scal = fock.msc
sub = fock.msub


def comm(x, y):
    return sub(mul(x, y), mul(y, x))


def acomm(x, y):
    return add(mul(x, y), mul(y, x))


ONE = {ID: F(1)}


def word_sq(w):
    return wmul(w, w)[0]


def generators(p, q):
    """Seven mutually anticommuting words, p of square +1 then q of square -1 (first found)."""
    words = [''.join(t) for t in product('IXZE', repeat=L)][1:]
    need = [1] * p + [-1] * q

    def bt(ch):
        if len(ch) == len(need):
            return ch
        for w in words:
            if w not in ch and word_sq(w) == need[len(ch)] and all(wmul(w, c)[0] == -wmul(c, w)[0] for c in ch):
                r = bt(ch + [w])
                if r:
                    return r
        return None
    return [{w: F(1)} for w in bt([])]


def commutant_words(gens):
    """Span of the words commuting with every given element (each given element a +- word)."""
    out = []
    for t in product('IXZE', repeat=L):
        w = ''.join(t)
        if all(comm({w: F(1)}, g) == {} for g in gens):
            out.append({w: F(1)})
    return out


class Span(object):
    def __init__(self):
        self.piv = {}

    def add(self, x):
        r = dict(x)
        while r:
            hit = [w for w in r if w in self.piv]
            if not hit:
                break
            w = min(hit)
            c = r[w]
            r = sub(r, scal(c, self.piv[w]))
        if r:
            w = min(r)
            self.piv[w] = scal(1 / r[w], r)
            return True
        return False


def lie_closure_dim(gens):
    sp, basis = Span(), []
    for g in gens:
        if sp.add(g):
            basis.append(g)
    i = 0
    while i < len(basis):
        for j in range(i):
            c = comm(basis[i], basis[j])
            if sp.add(c):
                basis.append(c)
        i += 1
    return len(basis)


def span_dim(xs):
    sp = Span()
    return sum(1 for x in xs if sp.add(x))


def division_type(basis):
    pure = [{w: c for w, c in b.items() if w != ID} for b in basis]
    pure = [x for x in pure if x]
    if span_dim(pure) != len(basis) - 1:
        return None
    for x in pure:
        for y in pure:
            s = acomm(x, y)
            if any(w != ID for w in s):
                return None
    if not all(mul(x, x).get(ID, F(0)) < 0 for x in pure):
        return None
    if not all(acomm(x, y) == {} for i, x in enumerate(pure) for y in pure[:i]):
        return None
    return {0: 'R', 1: 'C', 3: 'H'}.get(len(pure))


def centraliser_dim(H, gens):
    """dim of {h in span H : [h, g] = 0 for all g}, as an exact kernel over the coefficients."""
    cols = [[comm(h, g) for g in gens] for h in H]
    keys = sorted({(gi, w) for c in cols for gi, x in enumerate(c) for w in x})
    rows = [[cols[k][gi].get(w, F(0)) for k in range(len(H))] for (gi, w) in keys]
    return len(GA.field_kernel(rows)) if rows else len(H)


def car(ws, vs):
    for i in range(3):
        for k in range(3):
            if acomm(ws[i], vs[k]) != (ONE if i == k else {}):
                return False
            if acomm(ws[i], ws[k]) != {} or acomm(vs[i], vs[k]) != {}:
                return False
    return True


def pair_u3(ws, vs, U):
    gens = [mul(U, sub(mul(vs[i], ws[i]), scal(F(1, 2), ONE))) for i in range(3)]
    for i in range(3):
        for k in range(i + 1, 3):
            gens.append(sub(mul(vs[i], ws[k]), mul(vs[k], ws[i])))
            gens.append(mul(U, add(mul(vs[i], ws[k]), mul(vs[k], ws[i]))))
    return gens


def setup(p, q):
    G = generators(p, q)
    S = [1] * p + [-1] * q
    for a in range(7):
        for b in range(7):
            assert acomm(G[a], G[b]) == (scal(2 * S[a], ONE) if a == b else {})
    om = ONE
    for g in G:
        om = mul(om, g)
    spin = [mul(G[0], G[a]) for a in range(1, 7)]
    H = commutant_words(spin)
    return G, S, om, H


def units(H):
    """Unit pure elements of H: the pure basis words (square -1) and their (3/5, 4/5) mixtures."""
    pure = [h for h in H if ID not in h]
    out = []
    for x in pure:
        out.extend([x, scal(-1, x)])
    for i in range(len(pure)):
        for j in range(i + 1, len(pure)):
            out.append(add(scal(F(3, 5), pure[i]), scal(F(4, 5), pure[j])))
    return [u for u in out if mul(u, u) == scal(-1, ONE)]


def check_r3_unit_and_three_pairs():
    premise("dark-tower-matter.constituents-field")
    G, S, I7, H = setup(5, 2)
    assert division_type(commutant_words(G)) == 'C'          # irreducible 16-dim module
    assert len(H) == 4 and division_type(H) == 'H'
    assert mul(I7, I7) == scal(-1, ONE)
    assert all(comm(I7, g) == {} for g in G)
    assert span_dim(H + [I7]) == 4                           # I7 lies in H
    half = F(1, 2)
    ws = [scal(half, add(G[0], G[5])), scal(half, add(G[1], G[6])), scal(half, add(G[2], mul(I7, G[3])))]
    vs = [scal(half, sub(G[0], G[5])), scal(half, sub(G[1], G[6])), scal(half, sub(G[2], mul(I7, G[3])))]
    assert S[2] == 1 and S[3] == 1
    assert mul(ws[2], ws[2]) == {}
    assert car(ws, vs)
    u3 = pair_u3(ws, vs, I7)
    assert lie_closure_dim(u3) == 9
    assert centraliser_dim(H, u3) == 2
    assert all(comm(I7, x) == {} for x in u3)               # I7 is in the centraliser
    return True


def check_r3_units_anticommuting_with_i7():
    premise("dark-tower-matter.constituents-field")
    G, S, I7, H = setup(5, 2)
    half = F(1, 2)
    ws = [scal(half, add(G[0], G[5])), scal(half, add(G[1], G[6])), scal(half, add(G[2], mul(I7, G[3])))]
    vs = [scal(half, sub(G[0], G[5])), scal(half, sub(G[1], G[6])), scal(half, sub(G[2], mul(I7, G[3])))]
    Js = [u for u in units(H) if acomm(u, I7) == {}]
    assert len(Js) == 4 + 1                                   # +-J1, +-J2 and (3 J1 + 4 J2)/5
    for J in Js:
        Jinv = scal(-1, J)
        assert all(acomm(J, g) == {} for g in G)              # acts as the grade involution
        for i in range(2):
            assert mul(mul(J, ws[i]), Jinv) == scal(-1, ws[i])
        assert mul(mul(J, ws[2]), Jinv) == scal(-1, vs[2])     # w3 -> -wbar3
    u3 = pair_u3(ws, vs, I7)
    assert lie_closure_dim(u3 + [Js[0]]) == 30
    return True


def check_r5_no_canonical_unit():
    premise("dark-tower-matter.constituents-field")
    G, S, om, H = setup(2, 5)
    assert len(H) == 4 and division_type(H) == 'H'
    assert all(comm(h, g) == {} for h in H for g in G)        # spin commutant = Clifford commutant
    assert centraliser_dim(H, H) == 1                          # centre of H is R
    assert mul(om, om) == ONE                                  # omega^2 = +1
    return True


def check_r5_third_pair_for_every_unit():
    premise("dark-tower-matter.constituents-field")
    G, S, om, H = setup(2, 5)
    half = F(1, 2)
    us = units(H)
    assert len(us) == 6 + 3
    for k, u in enumerate(us):
        assert all(comm(u, g) == {} for g in G)
        ws = [scal(half, add(G[0], G[2])), scal(half, add(G[1], G[3])), scal(half, add(G[4], mul(u, G[5])))]
        vs = [scal(half, sub(G[0], G[2])), scal(half, sub(G[1], G[3])), scal(-half, sub(G[4], mul(u, G[5])))]
        assert S[4] == -1 and S[5] == -1
        assert car(ws, vs)
        u3 = pair_u3(ws, vs, u)
        if k < 2:
            assert lie_closure_dim(u3) == 9
            assert centraliser_dim(H, u3) == 2
            v = next(x for x in us if acomm(x, u) == {})
            assert lie_closure_dim(u3 + [v]) == 30
    return True


def check_r5_units_conjugate():
    premise("dark-tower-matter.constituents-field")
    G, S, om, H = setup(2, 5)
    us = units(H)
    for u in us:
        for up in us:
            g = sub(ONE, mul(up, u))
            assert mul(g, u) == mul(up, g)
            if add(up, u) == {}:
                assert g == {}
            else:
                # g is invertible: g g^bar = |g|^2 with gbar = 1 - u u' (quaternion conjugate)
                gb = sub(ONE, mul(u, up))
                n = mul(g, gb)
                assert list(n) == [ID] and n[ID] > 0
        # u' = -u is reached by conjugation with a unit anticommuting with u
        v = next(x for x in us if acomm(x, u) == {})
        assert mul(mul(v, u), scal(-1, v)) == scal(-1, u)
    return True
