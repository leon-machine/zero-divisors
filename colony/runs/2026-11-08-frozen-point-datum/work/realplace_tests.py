#!/usr/bin/env python3
"""Real-place / square-class tests for the D7 and D12 results of the finitist audit.

Exact arithmetic only (Fractions, GA.py). Run from anywhere:
    python3 realplace_tests.py
Uses /home/claude/phys-graph/lib/GA.py read-only.
"""
import sys
from fractions import Fraction as F
from itertools import product
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA

FAILS = []


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILS.append(label)


# ------------------------------------------------------------------ number theory
def isqrt(n):
    if n < 0:
        return None
    x = int(n ** 0.5) if n < 10 ** 30 else n
    while x * x > n:
        x = (x + n // x) // 2
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


def is_square(q):
    q = F(q)
    if q < 0:
        return False
    a, b = isqrt(q.numerator), isqrt(q.denominator)
    return a * a == q.numerator and b * b == q.denominator


def squarefree_int(q):
    """Representative of the square class of a nonzero rational: a squarefree integer."""
    q = F(q)
    n = q.numerator * q.denominator          # same square class
    s = -1 if n < 0 else 1
    n = abs(n)
    out, p = 1, 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e % 2:
            out *= p
        p += 1
    return s * out * n


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def val(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e, n


def hilbert(a, b, p):
    """Hilbert symbol (a, b)_p for nonzero rationals; p a prime or 'inf'."""
    a, b = squarefree_int(a), squarefree_int(b)
    if p == "inf":
        return -1 if (a < 0 and b < 0) else 1
    al, u = val(a, p)
    be, v = val(b, p)
    if p != 2:
        eps = (p - 1) // 2
        s = (-1) ** (al * be * eps)
        s *= legendre(u, p) ** be if be else 1
        s *= legendre(v, p) ** al if al else 1
        return s
    e = lambda x: ((x - 1) // 2) % 2
    w = lambda x: ((x * x - 1) // 8) % 2
    return (-1) ** ((e(u) * e(v) + al * w(v) + be * w(u)) % 2)


def primes_of(*qs):
    ps = {2}
    for q in qs:
        n = abs(squarefree_int(q))
        p = 2
        while p * p <= n:
            if n % p == 0:
                ps.add(p)
                while n % p == 0:
                    n //= p
            p += 1
        if n > 1:
            ps.add(n)
    return sorted(ps)


def quat_split_Q(a, b):
    return all(hilbert(a, b, p) == 1 for p in primes_of(a, b) + ["inf"])


def quat_split_Qi(a, b):
    """(a,b)_Q tensor Q(i) splits iff (a,b)_p = 1 at every p = 1 mod 4 (the places that split in Q(i))."""
    return all(hilbert(a, b, p) == 1 for p in primes_of(a, b) if p % 4 == 1)


def hasse(diag, p):
    s = 1
    for i in range(len(diag)):
        for j in range(i + 1, len(diag)):
            s *= hilbert(diag[i], diag[j], p)
    return s


def disc(diag):
    d = F(1)
    for x in diag:
        d *= F(x)
    return squarefree_int(d)


def isometric_Q(d1, d2):
    """Hasse-Minkowski: rank, discriminant, signature, Hasse invariants at all places."""
    if len(d1) != len(d2) or disc(d1) != disc(d2):
        return False
    if sum(1 for x in d1 if x > 0) != sum(1 for x in d2 if x > 0):
        return False
    return all(hasse(d1, p) == hasse(d2, p) for p in primes_of(*(list(d1) + list(d2))))


def isotropic_binary_Q(a, b):
    """<a, b> isotropic over Q iff -a b is a square."""
    return is_square(-F(a) * F(b))


def is_square_Qi(q):
    """A rational is a square in Q(i) iff q or -q is a rational square."""
    return is_square(q) or is_square(-F(q))


# ------------------------------------------------------------------ Clifford helpers
def omega(n):
    x = GA.sc(1)
    for i in range(n):
        x = GA.mul(x, GA.gen(i), None) if False else x
    return x


def pseudoscalar_square(squares):
    n = len(squares)
    w = {tuple(range(n)): F(1)}
    w2 = GA.mul(w, w, squares)
    assert set(w2) <= {()}
    return w2.get((), F(0))


# ================================================================== tests
print("== 0. Calibration: quaternion algebras (a,b)_Q from the brief")
for (a, b), expect_split in [((2, 3), False), ((3, 3), False), ((3, 5), False),
                             ((1, 1), True), ((2, 2), True), ((2, 7), True), ((6, 10), True)]:
    hs = quat_split_Q(a, b)
    # direct search for a x^2 + b y^2 = z^2, (x,y) != 0, small integers; a hit gives an idempotent and a zero divisor
    hit = None
    for x, y in product(range(-12, 13), repeat=2):
        if (x, y) == (0, 0):
            continue
        z2 = a * x * x + b * y * y
        if z2 > 0 and isqrt(z2) ** 2 == z2:
            hit = (x, y, isqrt(z2))
            break
    ok = hs == expect_split and ((hit is not None) == expect_split)
    if hit:
        x, y, z = hit
        sq = (F(a), F(b))
        u = GA.add(GA.scal(x, GA.gen(0)), GA.scal(y, GA.gen(1)))
        e = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(F(1, z), u)))
        zd1, zd2 = GA.sub(GA.sc(z), u), GA.add(GA.sc(z), u)
        ok = ok and GA.eq(GA.mul(e, e, sq), e) and GA.mul(zd1, zd2, sq) == {}
    check("(%d,%d)_Q %s (Hilbert symbols; direct search hit %s)" % (a, b, "splits" if hs else "is division", hit), ok)

print("\n== 1. Bott table transfers to Q for +-1 generators: symbols (+-1,+-1)_v")
tab = {}
for a, b in product((1, -1), repeat=2):
    tab[(a, b)] = {v: hilbert(a, b, v) for v in ["inf", 2, 3, 5, 7, 11, 13]}
ok = all(tab[k][3] == tab[k][5] == tab[k][7] == tab[k][11] == tab[k][13] == 1 for k in tab)
ok = ok and all(tab[k]["inf"] == tab[k][2] for k in tab) and tab[(-1, -1)]["inf"] == -1
check("(+-1,+-1)_v = 1 at odd v and inv_2 = inv_inf: Cl_Q(p,q) is determined by Cl_R(p,q) "
      "(R->Q, C->Q(i), H->H_Q ramified at {2,inf})", ok)
# type N and type C on the standard forms, over Q
ok = True
for p, q in [(1, 1), (1, 3), (2, 3), (1, 4), (2, 4), (3, 2)]:
    sq = GA.sig(p, q)
    w2 = pseudoscalar_square(sq)
    n = p + q
    if n % 2 == 1:
        # central idempotents (1 +- w)/2 rational exactly when w^2 = +1, i.e. p - q = 1 mod 4
        ok = ok and ((w2 == 1) == ((p - q) % 4 == 1))
    v = GA.add(GA.gen(0), GA.gen(p))           # e_1 + e_{p+1}: null in mixed signature
    ok = ok and GA.mul(v, v, sq) == {}
check("standard +-1 forms over Q: type N null vector e_1 + e_{p+1} rational; type C iff p - q = 1 mod 4", ok)

print("\n== 2. Transport criteria are statements about the +-1 forms, not about 'signature (p,q)' over Q")
check("<1,-3>: mixed signature (1,1) but anisotropic over Q (no type-N null vector)",
      not isotropic_binary_Q(1, -3))
sq = (F(1), F(-1), F(-1), F(-1), F(-1, 3))
w2 = pseudoscalar_square(sq)
check("Cl(1,3) + <-1/3>: p - q = 1 - 4 = 1 mod 4, but omega^2 = %s is not a rational square: "
      "no central idempotent over Q" % w2, w2 == F(1, 3) and not is_square(w2))

print("\n== 3. odd-extensions.exceptional-algebra-residue-completion-both-sides (i)")
L13 = [F(1), F(-1), F(-1), F(-1)]
cases = {
    "Cl(1,3)+<+1/3> (Lambda<0, rescaled by sqrt|Lambda|)": L13 + [F(1, 3)],
    "Cl(2,3) target": [F(1), F(1), F(-1), F(-1), F(-1)],
    "Cl(1,3)+<-1/3> (Lambda>0, rescaled)": L13 + [F(-1, 3)],
    "Cl(1,4) target": L13 + [F(-1)],
}
w = {k: pseudoscalar_square(v) for k, v in cases.items()}
for k in cases:
    print("      omega^2 in %-52s = %s (square class %d)" % (k, w[k], squarefree_int(w[k])))
check("AdS side: centre Q(sqrt(-3)) against Q(i): Cl(1,3)+<1/3> is NOT isomorphic to Cl(2,3) over Q",
      squarefree_int(w[list(cases)[0]]) == -3 and squarefree_int(w[list(cases)[1]]) == -1)
check("dS side: centre Q(sqrt 3) (a field) against Q x Q: Cl(1,3)+<-1/3> is NOT isomorphic to Cl(1,4) over Q",
      squarefree_int(w[list(cases)[2]]) == 3 and squarefree_int(w[list(cases)[3]]) == 1)
check("the quadratic spaces are not isometric over Q either (Hasse-Minkowski)",
      not isometric_Q(cases[list(cases)[0]], cases[list(cases)[1]])
      and not isometric_Q(cases[list(cases)[2]], cases[list(cases)[3]]))
check("over Q(i) the centres still differ: -3 and 3 are not squares in Q(i), -1 and 1 are",
      not is_square_Qi(-3) and not is_square_Qi(3) and is_square_Qi(-1))
check("over Q(sqrt 3) they agree, since 3 * (1/3) = 1 makes 1/3 a square there: the iso needs Q(sqrt 3)",
      F(1, 3) * 3 == 1 and squarefree_int(F(1, 3)) == 3)
# unrescaled family: w_Lambda has Q = -Lambda/3; Cl(1,3)+<-Lambda/3> = Cl(1,4) over Q iff Lambda/3 is a square
ok = True
for Lam in [F(3), F(12), F(27, 4), F(1), F(6), F(9), F(2, 3)]:
    d = Lam / 3
    iso = isometric_Q(L13 + [-d], L13 + [F(-1)])
    ok = ok and iso == is_square(d)
    print("      Lambda = %-5s  Lambda/3 square: %-5s  I^perp-type space isometric to (1,4): %s"
          % (Lam, is_square(d), iso))
check("I_Lambda^perp = Cl(1,3)+<-Lambda/3> is the standard (1,4) space over Q exactly when Lambda/3 = H^2, H in Q", ok)

print("\n== 4. de Sitter group / so(1,4) as a Q-form: similarity class of <1,-1,-1,-1,-d>")
# for odd rank, so(q) = so(q') iff q' = c q; scale by c = disc to normalise, then compare.
ok = True
for d in [F(1), F(2), F(5), F(3), F(6), F(7), F(1, 3), F(4, 3)]:
    q = L13 + [-d]
    c = disc(q)
    qs = [c * x for x in q]
    sim = isometric_Q(qs, L13 + [F(-1)]) or isometric_Q([-x for x in qs], L13 + [F(-1)])
    two_sq = any(F(x, z) ** 2 + F(y, z) ** 2 == d for x in range(0, 13) for y in range(0, 13) for z in range(1, 13))
    ok = ok and sim == two_sq
    print("      d = Lambda/3 = %-4s  so(I^perp) = so(1,4)_Q: %-5s  d a sum of two squares: %-5s  Cl centre split: %s"
          % (d, sim, two_sq, is_square(d)))
check("stabiliser so(I_Lambda^perp) is the standard so(1,4) over Q iff Lambda/3 is a sum of two rational squares;"
      " the Clifford algebra is the standard (doubled) Cl(1,4) iff Lambda/3 is a square", ok)

print("\n== 5. Mirror / doubled-complexified rule (synthesis.mirror-extensions-causal-convention (v))")
ok = True
for d in [F(1), F(4), F(2), F(3), F(1, 3)]:
    ours = pseudoscalar_square(L13 + [-d])                       # this world: complement adds square -d
    mirror = pseudoscalar_square([-x for x in L13] + [d])        # signature reversed
    doubled = is_square(ours)
    cplx_Qi = squarefree_int(mirror) == -1                       # centre is Q(i) exactly
    ok = ok and (doubled == is_square(d)) and (cplx_Qi == is_square(d))
    print("      d = %-4s ours: omega^2 = %-5s (%s)   mirror: omega^2 = %-5s (centre %s)"
          % (d, ours, "doubled Q x Q" if doubled else "field Q(sqrt %d)" % squarefree_int(ours),
             mirror, "Q(i)" if cplx_Qi else "Q(sqrt %d)" % squarefree_int(mirror)))
check("over Q, 'ours doubled, mirror complexified (by Q(i))' holds iff Lambda/3 is a rational square;"
      " otherwise both centres are other quadratic fields", ok)
# over Q(i) as base: Cl(2,3) and Cl(3,2) have split centres and split Brauer class: the distinction collapses
ok = all(is_square_Qi(pseudoscalar_square(GA.sig(p, q))) for p, q in [(2, 3), (3, 2), (1, 4), (4, 1)])
ok = ok and all(quat_split_Qi(a, b) for a, b in product((1, -1), repeat=2))
check("over Q(i) as the BASE field, Cl(2,3) = Cl(3,2) and Cl(1,4) = Cl(4,1) (split centres, split symbols):"
      " odd-extensions.twistor-algebra (iv) and the doubled/complexified rule hold over Q, not over Q(i)", ok)

print("\n== 6. synthesis.cosmological-horizon-completed-pair and de-sitter-static-boost-frozen-point")
# plane Pi = span(e0, W), Q(e0) = 1, Q(W) = -Lambda/3; B = e0 W
ok_pair = True
for H in [F(1), F(1, 2), F(3, 7)]:
    Lam = 3 * H * H
    sq = (F(1), -Lam / 3)
    e0, Wv = GA.gen(0), GA.gen(1)
    eW = GA.scal(1 / H, Wv)
    v = GA.scal(F(1, 2), GA.add(e0, eW))
    vs = GA.scal(F(1, 2), GA.sub(e0, eW))
    u = GA.mul(e0, eW, sq)
    ok_pair = ok_pair and GA.mul(v, v, sq) == {} and GA.mul(vs, vs, sq) == {}
    ok_pair = ok_pair and GA.eq(GA.add(GA.mul(v, vs, sq), GA.mul(vs, v, sq)), GA.sc(1))
    ok_pair = ok_pair and GA.eq(GA.sub(GA.mul(vs, v, sq), GA.mul(v, vs, sq)), u)
    ok_pair = ok_pair and GA.eq(GA.mul(u, u, sq), GA.sc(1))
check("H rational (Lambda = 3H^2): v = (e0 + W/H)/2, v* = (e0 - W/H)/2 rational, null, CAR, v*v - vv* = u, u^2 = 1",
      ok_pair)
ok = True
for Lam in [F(1), F(6), F(2), F(5), F(3, 2)]:
    d = Lam / 3
    iso = isotropic_binary_Q(1, -d)
    # brute force: x^2 = d y^2 with small integers
    hit = any(F(x * x) == d * y * y for x in range(1, 60) for y in range(1, 60))
    # ad_B on the plane: eigenvalues of x -> B x - x B
    sq = (F(1), -d)
    B = GA.mul(GA.gen(0), GA.gen(1), sq)
    cols = []
    for g in (GA.gen(0), GA.gen(1)):
        c = GA.sub(GA.mul(B, g, sq), GA.mul(g, B, sq))
        cols.append([c.get((0,), F(0)), c.get((1,), F(0))])
    M = [[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]]
    tr, det = M[0][0] + M[1][1], M[0][0] * M[1][1] - M[0][1] * M[1][0]
    discr = tr * tr - 4 * det            # rational eigenvectors iff discr is a square
    ok = ok and not iso and not hit and not is_square(discr) and pseudoscalar_square(sq) == d
    print("      Lambda = %-4s B^2 = %-4s  null vectors in Pi over Q: %s   ad_B char. discriminant %s (square: %s)"
          % (Lam, pseudoscalar_square(sq) if False else GA.mul(B, B, sq).get((), 0), iso, discr, is_square(discr)))
check("Lambda > 0 with Lambda/3 not a square: Pi is anisotropic over Q, no completed pair, the boost B has no"
      " rational eigen-directions (it behaves like a rotation plane over Q)", ok)
ok = isotropic_binary_Q(1, 1) is False and is_square_Qi(-1)
check("Lambda = -3 (B^2 = -1): no real null vectors over Q, but e0 + i e_W is null over Q(i);"
      " the claim's 'real' is the Q-form, so it stands", ok)

def sum3sq(q):
    n = squarefree_int(q)
    if n <= 0:
        return False
    while n % 4 == 0:
        n //= 4
    return n % 8 != 7
ok = True
for Lam, expect in [(F(3), True), (F(12), True), (F(7, 3), False), (F(28, 3), False), (F(1), True)]:
    r2 = 12 / Lam                                  # bifurcation sphere |x|^2 = 12/Lambda
    ok = ok and sum3sq(r2) == expect
    print("      Lambda = %-5s 12/Lambda = %-5s rational points on the bifurcation sphere: %s; endpoints x = +-sqrt(12/Lambda) e0 rational: %s"
          % (Lam, r2, sum3sq(r2), is_square(r2)))
check("the bifurcation sphere {x0 = 0, Q(x) = -12/Lambda} has no rational point at all for Lambda = 7/3 or 28/3"
      " (12/Lambda of the form 4^a(8b+7)); with H rational, 12/Lambda = (2/H)^2 and everything is rational", ok)

print("\n== 7. synthesis.operator-join-point-spectrum: pair form needs sqrt(lambda), lambda = Lambda/6 = H^2/2")
ok = True
for H in [F(1), F(2), F(3, 5)]:
    lam = H * H / 2
    ok = ok and not is_square(lam) and not is_square_Qi(lam)
check("with H rational, lambda = H^2/2 is a square neither in Q nor in Q(i) (1/2 needs sqrt 2 = zeta_8 + zeta_8^-1)", ok)
ok = all(is_square(F(L, 6)) and not is_square(F(L, 3)) for L in [6, F(3, 2), 24])
check("conversely the store's check points (Lambda = 6, 3/2) have sqrt(lambda) rational and H = sqrt(Lambda/3) irrational:"
      " the unitary pair form and a rational H need Q(sqrt 2) together", ok)

print("\n== 8. Democratic and Fourier normalisations (families, neutrino, circulant): projective only")
u3 = [F(1)] * 3
ok = sum(x * x for x in u3) == 3 and not is_square(3)
J = [[F(1)] * 3 for _ in range(3)]
Ju = [sum(J[i][j] * u3[j] for j in range(3)) for i in range(3)]
ok = ok and Ju == [3 * x for x in u3]
for v in ([F(1), F(-1), F(0)], [F(1), F(1), F(-2)]):
    ok = ok and [sum(J[i][j] * v[j] for j in range(3)) for i in range(3)] == [0, 0, 0]
ok = ok and isometric_Q([F(1)] * 3, [F(3), F(2), F(6)])
check("J has rational eigenlines (1,1,1) [3], (1,-1,0), (1,1,-2) [0]; <1,1,1> = <3,2,6> over Q, so the orthogonal"
      " eigen-decomposition exists over Q, only the orthonormal (tribimaximal) frame needs Q(sqrt2, sqrt3)", ok)
ok = not any(F(x * x) == 3 * y * y for x in range(1, 80) for y in range(1, 80))
check("no rational isometry carries e_1 to the democratic line (norm 1 vs norm-class 3): 'the faces up to the rotation"
      " the vacuum performs' is a statement over R (squared mixing moduli 1/3, 1/2, 1/6 are rational)", ok)

print("\n== 9. correspondence.spinor-identification: the sqrt 2 is a Fock-model convention")
# exterior model on W with c(w) = w^ and c(w') = 2 iota_{w'} (pairing delta/2 basis as in the check): c(u)^2 = Q(u)
# verified there over Q(i); the wedge-square constant becomes rational. Here: 1-mode toy check of the convention.
# basis |0>, |1>; c(w) = [[0,0],[1,0]], c(w') = [[0,a],[0,0]], {c(w), c(w')} = a * id must equal 2<w,w'>.
for a, pairing in [(F(1), F(1, 2)), (F(2), F(1))]:
    cw = [[F(0), F(0)], [F(1), F(0)]]
    cwp = [[F(0), a], [F(0), F(0)]]
    acomm = [[sum(cw[i][k] * cwp[k][j] + cwp[i][k] * cw[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    check("c(w) = w^, c(w') = %s iota: {c(w), c(w')} = %s id = 2<w,w'> with <w,w'> = %s (no sqrt 2)" % (a, a, pairing),
          acomm == [[a, F(0)], [F(0), a]] and a == 2 * pairing)

print("\nfailures: %d" % len(FAILS))
for f in FAILS:
    print("  " + f)
