"""synthesis.slot-count-not-from-constituent-fock-space: exact checks.

Constituent Fock spaces over C^K (x) C^4 (C^4 standing for the conformal spinor space CS as an
SL(4) = Spin(6) module), fermionic (exterior algebra, bitmask states with signs) and bosonic
(polynomials, monomial states). Multiplicity of the GL(K) x GL(4) highest weight (rows; cols) =
dimension of the joint kernel of the simple raising operators E_{i,i+1} (slot index) and
E_{a,a+1} (twistor index) on that weight space, by exact rank over Q (GA.rank_of_vectors).
An SL(K)-singlet (x) CS component has rows (m,...,m) and cols (c+1,c,c,c); (x) CS* has cols
(c+1,c+1,c+1,c).
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise


def _ferm_basis(K, rows, cols):
    n = sum(rows)
    out = []
    for S in combinations(range(4 * K), n):
        r, c = [0] * K, [0] * 4
        for m in S:
            r[m // 4] += 1
            c[m % 4] += 1
        if r == list(rows) and c == list(cols):
            out.append(frozenset(S))
    return out


def _hop(S, src, dst):
    if src not in S:
        return None
    sign = (-1) ** sum(1 for m in S if m < src)
    S1 = S - {src}
    if dst in S1:
        return None
    sign *= (-1) ** sum(1 for m in S1 if m < dst)
    return sign, S1 | {dst}


def _raising(K):
    ops = [[((i + 1) * 4 + a, i * 4 + a) for a in range(4)] for i in range(K - 1)]
    ops += [[(i * 4 + a + 1, i * 4 + a) for i in range(K)] for a in range(3)]
    return ops


def hw_ferm(K, rows, cols):
    """(multiplicity, weight-space dimension) in Lambda(C^K (x) C^4)."""
    basis = _ferm_basis(K, rows, cols)
    imgs = []
    for S in basis:
        vec = {}
        for oi, op in enumerate(_raising(K)):
            for (src, dst) in op:
                r = _hop(S, src, dst)
                if r:
                    key = (oi, tuple(sorted(r[1])))
                    vec[key] = vec.get(key, 0) + r[0]
        imgs.append(vec)
    keys = sorted({k for v in imgs for k in v})
    M = [[F(v.get(k, 0)) for v in imgs] for k in keys]
    rank = GA.rank_of_vectors(M) if M else 0
    return len(basis) - rank, len(basis)


def _compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for k in range(total + 1):
        for rest in _compositions(total - k, parts - 1):
            yield (k,) + rest


def _bos_basis(K, rows, cols):
    out = []

    def rec(i, rem, acc):
        if i == K:
            if all(x == 0 for x in rem):
                out.append(tuple(acc))
            return
        for row in _compositions(rows[i], 4):
            if all(row[a] <= rem[a] for a in range(4)):
                rec(i + 1, [rem[a] - row[a] for a in range(4)], acc + [row])
    rec(0, list(cols), [])
    return out


def hw_bos(K, rows, cols):
    """(multiplicity, weight-space dimension) in Sym(C^K (x) C^4); E = x_dst d/dx_src."""
    basis = _bos_basis(K, rows, cols)
    ops = [[((i + 1, a), (i, a)) for a in range(4)] for i in range(K - 1)]
    ops += [[((i, a + 1), (i, a)) for i in range(K)] for a in range(3)]
    imgs = []
    for e in basis:
        vec = {}
        for oi, op in enumerate(ops):
            for (src, dst) in op:
                ex = e[src[0]][src[1]]
                if ex:
                    m = [list(r) for r in e]
                    m[src[0]][src[1]] -= 1
                    m[dst[0]][dst[1]] += 1
                    key = (oi, tuple(tuple(r) for r in m))
                    vec[key] = vec.get(key, 0) + ex
        imgs.append(vec)
    keys = sorted({k for v in imgs for k in v})
    M = [[F(v.get(k, 0)) for v in imgs] for k in keys]
    return len(basis) - (GA.rank_of_vectors(M) if M else 0), len(basis)


def singlet_targets(K, nmax):
    """All (rows, cols) for SL(K)-singlet (x) CS or CS* up to total degree nmax."""
    out = []
    for n in range(nmax + 1):
        if n % K:
            continue
        for c in range(n + 1):
            for cols in ((c + 1, c, c, c), (c + 1, c + 1, c + 1, c)):
                if sum(cols) == n:
                    out.append(((n // K,) * K, cols))
    return out


def s_space_zero_slot_sector():
    """(S): Lambda(C^2 + W), modes 0,1 slots and 2,3,4 pairs. States killed by the slot sl(2)
    (s0^dag s1, s1^dag s0) with slot number 0 or 2, split by W parity."""
    out = {}
    for mask in range(32):
        j = (mask & 1) + ((mask >> 1) & 1)
        if j == 1:
            continue
        k = bin(mask >> 2).count("1")
        out[(j, k % 2)] = out.get((j, k % 2), 0) + 1
    return out


def check_slot_count_not_from_constituent_fock_space():
    premise("field-theory.twistor-attachment")
    premise("rungs.two-twistor-bivector-null-invites-one")
    premise("standard-model.under-s-composites-state-space-spinor")
    # controls: the method sees CS where it is (one constituent; doublets at K = 2)
    assert hw_ferm(1, (1,), (1, 0, 0, 0)) == (1, 1) and hw_bos(1, (1,), (1, 0, 0, 0)) == (1, 1)
    assert hw_ferm(2, (1, 0), (1, 0, 0, 0)) == (1, 1)
    assert hw_ferm(2, (4, 3), (2, 2, 2, 1)) == (1, 1)
    # every simple raising operator matters: (1,1,0,1) is killed only by E_{34}, (1,0,1,0) only by E_{23}
    assert hw_ferm(1, (3,), (1, 1, 0, 1)) == (0, 1) and hw_ferm(1, (2,), (1, 0, 1, 0)) == (0, 1)
    # K = 2, both statistics: an SL(2)-singlet has even degree, CS and CS* odd: no weight space at all
    assert singlet_targets(2, 8) == [] and singlet_targets(1, 3) == [((1,), (1, 0, 0, 0)), ((3,), (1, 1, 1, 0))]
    # K = 3 fermionic: the weight spaces exist (dimension 6) but carry no highest weight vector
    assert hw_ferm(3, (1, 1, 1), (1, 1, 1, 0)) == (0, 6)
    assert hw_ferm(3, (3, 3, 3), (3, 2, 2, 2)) == (0, 6)
    # K = 3 bosonic: det (x) CS* occurs once (the dual twistor of three constituents), CS does not
    assert hw_bos(3, (1, 1, 1), (1, 1, 1, 0)) == (1, 6)
    assert hw_bos(3, (3, 3, 3), (3, 2, 2, 2)) == (0, 132)
    # K = 4 fermionic: no singlet target meets the box (rows <= 4 per column)
    assert singlet_targets(4, 16) == [] and len(singlet_targets(3, 12)) == 2
    # (S): zero- and two-slot sectors carry the even W states (CS, dimension 4) and odd (CS*, 4)
    sec = s_space_zero_slot_sector()
    assert sec == {(0, 0): 4, (0, 1): 4, (2, 0): 4, (2, 1): 4}
    return True
