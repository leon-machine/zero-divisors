"""synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height: exact checks.

Integer and Fraction arithmetic, GA for the quaternion and Gaussian units. Checks:
  (1) the lambda-series step: in Z[xi]/(xi^2 - 1), the t^k coefficient of (1 + t)^k (1 + xi t)^{-1} is
      2^{k-1} (1 - xi), so a rank k - 1 bundle N with N = k - xi in K forces 2^{k-1}(1 - xi) = 0;
  (2) the order of 1 - chi^2 in Z[chi]/(chi^4 - 1, (chi - 1)^{n+1}) (the K-ring of L^{2n+1}(4), imported
      from memory in the proof) is 2^{floor((n+1)/2)} for n = 1..8, by an exact triangular lattice test; the
      lattice index is 4^n (the order of the reduced K-group), and the same code gives the classical order
      2^n of chi - 1 on RP^{2n+1};
  (3) the Gaussian bound: chi -> I (I = e1e2, I^2 = -1) kills chi^4 - 1, sends 1 - chi^2 to 2 = I pi^2
      with pi = I - 1, and 2^j has pi-adic valuation exactly 2j, so (1 - chi^2)^j != 0 when 2j <= n;
  (4) the walls exist: on the unit sphere of H^r (r-tuples of even elements of Cl(3,0)), B = e2e3 acting on the
      left generates the Z4 with quotient L^{4r-1}(4); f(q) = C q, C = e3e1 (BC = -CB), is a unit tangent field
      with f(Bq) = -B f(q), so its span descends to the twisted line; the cometric
      (I - (1 - t) f f^T/|f|^2) + (sign dt^2) is single valued, degenerate exactly along f at t = 0 with
      G_t(f, f) = t |f|^2 (first order), and of signature (2n+1, 1) or (2n+2, 0) on q-perp + R for t > 0
      (r = 2, 3: L^7(4) and L^11(4)).
"""
from fractions import Fraction as F
import GA
from GA import congruence_signature, mul, add, gen, sc, scal, reverse
from tp_premise import premise

E3 = (1, 1, 1)
E2 = (1, 1)


# ---------------------------------------------------------------- integer helpers (no literals asserted)

def binom(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for j in range(k):
        r = r * (n - j) // (j + 1)
    return r


def ideal_rows(n, m):
    """Z-basis (coordinates on s, s^2, .., s^n) of the ideal of (1+s)^m - 1 in Z[s]/(s^{n+1})."""
    f = [binom(m, j) for j in range(1, n + 1)]
    rows = []
    for sh in range(n):
        v = [0] * n
        for j in range(n - sh):
            v[j + sh] = f[j]
        rows.append(v)
    return rows


def in_ideal(rows, v):
    v = list(v)
    for i in range(len(v)):
        piv = rows[i][i]
        if v[i] % piv:
            return False
        c = v[i] // piv
        v = [a - c * b for a, b in zip(v, rows[i])]
    return all(a == 0 for a in v)


def power_minus_one(n, e):
    """chi^e - 1 = (1 + s)^e - 1 in coordinates s .. s^n."""
    return [binom(e, j) for j in range(1, n + 1)]


def log2_order(n, m, e):
    rows = ideal_rows(n, m)
    x = power_minus_one(n, e)
    for a in range(4 * n + 4):
        if in_ideal(rows, [(2 ** a) * c for c in x]):
            return a
    return None


def lattice_index(rows):
    d = 1
    for i, r in enumerate(rows):
        d *= r[i]
    return d


def lambda_coefficient(k):
    """t^k coefficient of (1+t)^k (1 + xi t)^{-1} in Z[xi]/(xi^2 - 1), as (c0, c1) for c0 + c1 xi."""
    inv = [(1, 0) if j % 2 == 0 else (0, 1) for j in range(k + 1)]      # xi^j
    inv = [((-1) ** j * a, (-1) ** j * b) for j, (a, b) in enumerate(inv)]
    c0 = sum(binom(k, k - j) * inv[j][0] for j in range(k + 1))
    c1 = sum(binom(k, k - j) * inv[j][1] for j in range(k + 1))
    return c0, c1


# ---------------------------------------------------------------- Gaussian units in GA

I2 = {(0, 1): F(1)}                                   # e1 e2 in Cl(2,0)
PI = add(I2, sc(-1))                                  # pi = I - 1
PI_INV_TIMES_2 = add(sc(-1), scal(-1, I2))            # (I - 1)(-1 - I) = 2


def gauss(x):
    return (x.get((), F(0)), x.get((0, 1), F(0)))


def pi_valuation(x):
    """pi-adic valuation of a nonzero Gaussian integer x (as a GA element)."""
    v = 0
    while True:
        y = mul(x, PI_INV_TIMES_2, E2)
        a, b = gauss(y)
        if a.denominator != 1 or b.denominator != 1 or a.numerator % 2 or b.numerator % 2:
            return v
        x = scal(F(1, 2), y)
        v += 1


# ---------------------------------------------------------------- quaternion tuples (S^{4r-1} in H^r)

def quat(w, x, y, z):
    return add(sc(w), scal(x, {(1, 2): F(1)}), scal(-y, {(0, 2): F(1)}), scal(z, {(0, 1): F(1)}))


QBASIS = [sc(1), {(1, 2): F(1)}, {(0, 2): F(-1)}, {(0, 1): F(1)}]
B = {(1, 2): F(1)}                                    # e2 e3: the Z4 generator, B^2 = -1
C = {(0, 2): F(-1)}                                   # e3 e1: anticommutes with B


def coords(q):
    return [q.get((), F(0)), q.get((1, 2), F(0)), -q.get((0, 2), F(0)), q.get((0, 1), F(0))]


def vec(qs):
    return [c for q in qs for c in coords(q)]


def left(U, qs):
    return [mul(U, q, E3) for q in qs]


def left_matrix(U, r):
    """Left multiplication by U on H^r as a 4r x 4r matrix (columns = images of basis vectors)."""
    cols = []
    for blk in range(r):
        for b in QBASIS:
            qs = [b if j == blk else sc(0) for j in range(r)]
            cols.append(vec(left(U, qs)))
    n = 4 * r
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def dotv(u, v):
    return sum(a * b for a, b in zip(u, v))


def matvec(M, v):
    return [dotv(row, v) for row in M]


def cometric(fv, t, sign):
    """(I - (1 - t) f f^T / |f|^2) + (sign dt^2) on R^{4r} + R(dt)."""
    n = len(fv)
    nf = dotv(fv, fv)
    G = [[(F(1) if i == j else F(0)) - (1 - t) * fv[i] * fv[j] / nf for j in range(n)] + [F(0)]
         for i in range(n)]
    G.append([F(0)] * n + [F(sign)])
    return G


QSAMPLES = [((1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0)), ((1, 2, 0, -1), (0, 1, 1, 3), (2, 0, 1, 1)),
            ((2, -1, 1, 0), (1, 0, -2, 1), (0, 0, 0, 1)), ((3, 1, -2, 1), (-1, 2, 2, 0), (1, -1, 1, -1))]


def wall_instance(qs, t, sign):
    """Returns (G at q, G at Bq pulled back by B, q, f, Bq, Cq data) on S^{4r-1} x R."""
    r = len(qs)
    Bm = left_matrix(B, r)
    qv = vec(qs)
    fv = vec(left(C, qs))
    gv = vec(left(C, left(B, qs)))
    G = cometric(fv, t, sign)
    GB = cometric(gv, t, sign)
    n = 4 * r + 1
    Bf = [row + [F(0)] for row in Bm] + [[F(0)] * (n - 1) + [F(1)]]
    pulled = [[sum(Bf[a][i] * GB[a][b] * Bf[b][j] for a in range(n) for b in range(n)) for j in range(n)]
              for i in range(n)]
    return G, pulled, qv, fv, gv, Bm


# ---------------------------------------------------------------- checks

def check_lambda_series_forces_power_of_two_multiple():
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    premise("sheaf.imported-real-line-bundles")
    table = [(1, 1), (2, 2), (3, 4), (4, 8), (5, 16)]
    for k, c in table:
        assert lambda_coefficient(k) == (c, -c)          # 2^{k-1} (1 - xi)
    return True


def check_k_ring_order_of_dying_line_on_lens_spaces():
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    premise("synthesis.lens-space-wall-rung-count-sees-the-integral-twist")
    m = 4
    orders = [1, 1, 2, 2, 3, 3, 4, 4]                    # log2 ord(1 - chi^2), n = 1, 2, ...
    for n, a in enumerate(orders, 1):
        assert lattice_index(ideal_rows(n, m)) == m ** n  # |K~(L^{2n+1}(4))| = 4^n
        assert log2_order(n, m, m // 2) == a
    # n = 1 (the stored L(4,1)): 2(1 - chi^2) = 0, no obstruction beyond ht = 2; n = 3: 2(1 - chi^2) != 0
    assert in_ideal(ideal_rows(1, m), [2 * c for c in power_minus_one(1, 2)])
    assert not in_ideal(ideal_rows(3, m), [2 * c for c in power_minus_one(3, 2)])
    # classical control: chi - 1 has order 2^n in K~(RP^{2n+1})
    for n in range(1, 6):
        assert log2_order(n, 2, 1) == n
    return True


def check_gaussian_bound_on_powers():
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    I4 = mul(mul(I2, I2, E2), mul(I2, I2, E2), E2)
    assert I4 == {(): F(1)}                                # chi^4 - 1 maps to 0
    assert add(sc(1), scal(-1, mul(I2, I2, E2))) == {(): F(2)}   # 1 - chi^2 maps to 2
    assert mul(I2, mul(PI, PI, E2), E2) == {(): F(2)}      # 2 = I pi^2
    assert mul(PI, PI_INV_TIMES_2, E2) == {(): F(2)}
    for j, v in [(1, 2), (2, 4), (3, 6), (4, 8)]:
        assert pi_valuation(sc(2 ** j)) == v
    # (chi - 1)^{n+1} maps to pi^{n+1}: so (1 - chi^2)^j survives in Z[I]/(pi^{n+1}) iff 2 j <= n
    assert pi_valuation(PI) == 1 and pi_valuation(add(sc(3), I2)) == 1
    return True


def check_lens_walls_exist_with_both_sides():
    premise("sheaf.tameness")
    premise("sheaf.degeneration-sheaf")
    premise("sheaf.imported-real-line-bundles")
    BC = mul(B, C, E3)
    assert mul(B, B, E3) == {(): F(-1)} and add(BC, mul(C, B, E3)) == {}     # B^2 = -1, BC = -CB
    for r in (2, 3):                                                           # L^7(4), L^11(4)
        n = 4 * r
        Bm = left_matrix(B, r)
        BtB = [[dotv([Bm[a][i] for a in range(n)], [Bm[a][j] for a in range(n)]) for j in range(n)]
               for i in range(n)]
        assert BtB == [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]   # isometry
        for smp in QSAMPLES:
            qs = [quat(*smp[j]) for j in range(r)]
            for sign in (-1, 1):                                               # indefinite, definite side
                for t in [F(0), F(1, 3), F(2)]:
                    G, pulled, qv, fv, gv, Bm = wall_instance(qs, t, sign)
                    assert dotv(qv, fv) == 0 and dotv(fv, fv) == dotv(qv, qv)  # unit tangent field Cq
                    assert gv == [-c for c in matvec(Bm, fv)]                  # f(Bq) = -B f(q): twisted line
                    assert pulled == G                                         # single valued on L^{4r-1}(4)
                    fx = fv + [F(0)]
                    assert dotv(fx, matvec(G, fx)) == t * dotv(fv, fv)         # first-order degeneration
                    assert matvec(G, qv + [F(0)]) == qv + [F(0)]               # the normal q decouples
                    sg = congruence_signature(G)
                    if sign == -1:
                        assert sg == ((n - 1, 1, 1) if t == 0 else (n, 1, 0))
                    else:
                        assert sg == ((n, 0, 1) if t == 0 else (n + 1, 0, 0))
    return True
