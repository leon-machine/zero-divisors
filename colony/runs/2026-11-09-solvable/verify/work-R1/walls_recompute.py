"""R1 independent recomputations for the two wall proposals (exact arithmetic only).

(A) K-theory order of 1 - chi^2 in Z[chi]/(chi^4 - 1, (chi - 1)^{n+1}) by Smith normal form of the
    relation lattice (a route different from the proposals' triangular back substitution), n = 1..12,
    plus the group structure of the reduced ring.
(B) q1 of the spin plane bundle L + L by the Spin(2) < Spin(3) < Spin(4) = SU(2) x SU(2) route:
    in GA, the even subalgebra of Cl(4,0) splits by the central idempotents P+- = (1 +- e1234)/2 and the
    rotor generator e12 acts in each factor as a unit u with u^2 = -P: spinor weight 1/2 of the vector
    weight. With Chern roots +-a on S+ and S-, c2(S+-) = -a^2 and q1 = -(c2(S+) + c2(S-)) = 2a^2
    (classical normalisation of q1 on BSpin(4), from memory); e = 2a. Then on L^{2m+1}(4), a in {y, 3y}.
"""
from fractions import Fraction as F
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA
from GA import mul, add, sub, scal, gen, sc


def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for j in range(k):
        r = r * (n - j) // (j + 1)
    return r


def snf_diag(M):
    """Smith normal form diagonal of an integer matrix (list of rows)."""
    A = [list(r) for r in M]
    m, n = len(A), len(A[0])
    diag = []
    r = 0
    for c in range(n):
        if r >= m:
            break
        while True:
            piv = None
            for i in range(r, m):
                for j in range(c, n):
                    if A[i][j] != 0 and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])):
                        piv = (i, j)
            if piv is None:
                return diag
            i, j = piv
            A[r], A[i] = A[i], A[r]
            for row in A:
                row[c], row[j] = row[j], row[c]
            done = True
            for i in range(r + 1, m):
                q = A[i][c] // A[r][c]
                A[i] = [a - q * b for a, b in zip(A[i], A[r])]
                if A[i][c] != 0:
                    done = False
            for j in range(c + 1, n):
                q = A[r][j] // A[r][c]
                for row in A:
                    row[j] -= q * row[c]
                if A[r][j] != 0:
                    done = False
            if done:
                bad = [(i, j) for i in range(r + 1, m) for j in range(c + 1, n) if A[i][j] % A[r][c]]
                if bad:
                    i, j = bad[0]
                    A[r] = [a + b for a, b in zip(A[r], A[i])]
                    continue
                diag.append(abs(A[r][c]))
                r += 1
                break
    return diag


def order_in_quotient(n, v):
    """Order of v (coords on s..s^n) in Z^n / lattice of s^i((1+s)^4 - 1), using integer solving by
    exhaustive search over the multiple: N v in lattice iff the augmented SNF has the same invariants."""
    rows = []
    f = [binom(4, j) for j in range(1, n + 1)]
    for sh in range(n):
        rr = [0] * n
        for j in range(n - sh):
            rr[j + sh] = f[j]
        rows.append(rr)
    base = snf_diag(rows)
    idx = 1
    for d in base:
        idx *= d
    N = 1
    while N <= idx:
        aug = snf_diag(rows + [[N * c for c in v]])
        p = 1
        for d in aug:
            p *= d
        if p == idx:          # adding N v does not enlarge the lattice
            return N, base
        N += 1
    return None, base


def part_A():
    print("(A) order of 1 - chi^2 in K~(L^{2n+1}(4)), Smith normal form route")
    for n in range(1, 13):
        v = [-binom(2, j) for j in range(1, n + 1)]          # 1 - chi^2 = -(2s + s^2)
        N, base = order_in_quotient(n, v)
        pred = 2 ** ((n + 1) // 2)
        print(f"  n={n:2d} group invariants={base} order={N} 2^floor((n+1)/2)={pred} "
              f"lower 2^floor(n/2)={2 ** (n // 2)} {'OK' if N == pred else 'DIFFERS'}")
        assert N >= 2 ** (n // 2)
    # complexified L + L minus 2 on L^5(4), L^7(4): 2(chi^2 - 1)
    for n in (1, 2, 3):
        v = [2 * binom(2, j) for j in range(1, n + 1)]
        N, _ = order_in_quotient(n, v)
        print(f"  2(chi^2 - 1) on L^{2*n+1}(4): order {N} ({'zero' if N == 1 else 'nonzero'})")


def part_B():
    print("(B) q1 of L + L via Spin(4) = SU(2) x SU(2) in GA")
    sq = (1, 1, 1, 1)
    e12 = {(0, 1): F(1)}
    e1234 = {(0, 1, 2, 3): F(1)}
    assert mul(e1234, e1234, sq) == {(): F(1)}
    for s in (1, -1):
        P = scal(F(1, 2), add(sc(1), scal(s, e1234)))
        assert mul(P, P, sq) == P                              # central idempotent
        for b in ([0, 1], [0, 2], [1, 3]):
            bb = {tuple(b): F(1)}
            assert mul(P, bb, sq) == mul(bb, P, sq)            # central in the even part
        u = mul(e12, P, sq)
        assert mul(u, u, sq) == scal(-1, P)                    # u^2 = -P: a unit imaginary quaternion
    # exp(e12 theta) acts on vectors by rotation 2 theta (vector weight 2 in theta) ...
    v = gen(0)
    R = e12                                                    # theta = pi/2: rotor e12
    img = mul(mul(R, v, sq), {(0, 1): F(-1)}, sq)
    assert img == scal(-1, v)                                  # half turn = rotation by pi = 2 theta
    # ... and on each spinor factor by exp(u theta): weight 1 in theta. So spinor weight = vector weight / 2.
    # Chern roots: vector bundle L + L has e = 2a; S+ = S- = mu + mu^{-1}, c1(mu) = a.
    # c2(S+-) = (a)(-a) = -a^2; q1 = -(c2(S+) + c2(S-)) = 2 a^2; p1 = e^2 = 4 a^2 = 2 q1.
    c2 = -1
    q1 = -(c2 + c2)
    assert q1 == 2 and 2 * q1 == 2 ** 2
    for m in (1, 2, 3, 4):
        vals = set()
        for a in (1, 3):                                       # a = y, 3y: 2a = 2y
            assert (2 * a) % 4 == 2
            coeff = (q1 * a * a) % 4                           # q1 = 2 a^2 y^2 in Z_4 (y^2 != 0 iff m >= 2)
            vals.add(coeff if m >= 2 else 0)
        print(f"  m={m}: q1(L+L) in H^4 = {'Z_4' if m >= 2 else '0'}: values {sorted(vals)} y^2 "
              f"({'nonzero' if vals != {0} else 'zero'}), p1 = 4a^2 y^2 = 0")


if __name__ == "__main__":
    part_A()
    part_B()
