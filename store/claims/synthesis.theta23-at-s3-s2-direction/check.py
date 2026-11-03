"""synthesis.theta23-at-s3-s2-direction: exact lepton textures at the S3 -> S2 direction."""
from fractions import Fraction as F
import GA
import series
from tp_premise import premise


def lcg(seed):
    while True:
        seed = (1103515245 * seed + 12345) % 2147483648
        yield seed


def mm(A, B): return GA.mat_mul(A, B)
def T(A): return [list(r) for r in zip(*A)]
def add(A, B, c=F(1)): return [[A[i][j] + c * B[i][j] for j in range(3)] for i in range(3)]
def sc(c, A): return [[c * x for x in r] for r in A]
def tr(A): return sum(A[i][i] for i in range(len(A)))
I3 = [[F(int(i == j)) for j in range(3)] for i in range(3)]
J = [[F(1)] * 3 for _ in range(3)]
E = [[F(0)] * 3 for _ in range(3)]; E[2][2] = F(1)
Pi = add(I3, sc(F(-1, 3), J))
one = [F(1)] * 3
def light(d, r):
    MD = add(J, E, d)
    MRinv = add(Pi, sc(1 / r, sc(F(1, 3), J)))
    return mm(mm(MD, MRinv), T(MD))
def charged(dc):
    Me = add(J, E, dc); return mm(Me, T(Me))

# the S2-symmetric plane: orthogonal rational basis s1 = (1,1,0), s2 = e3; kernel (1,-1,0)
s1 = [F(1), F(1), F(0)]; s2 = [F(0), F(0), F(1)]; k = [F(1), F(-1), F(0)]
def mv(A, v): return [sum(A[i][j] * v[j] for j in range(3)) for i in range(3)]
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def block(m):
    """Return (Delta, Bsq_sign_carrier, trace) of the 2x2 block in the orthonormal basis
    (s1/sqrt2, e3): A' = s1.m.s1/2, C' = m33, B' = s1.m.e3/sqrt2; we keep beta = s1.m.e3,
    so B'^2 = beta^2/2."""
    A_ = dot(s1, mv(m, s1)) / 2; C_ = dot(s2, mv(m, s2)); beta = dot(s1, mv(m, s2))
    return (A_ - C_) / 2, beta, A_ + C_
def Dq(m):  # discriminant/4: Delta^2 + B'^2 ; sqrt(D) = 2 sqrt(Dq)
    Dl, beta, t = block(m); return Dl * Dl + beta * beta / 2
def ratio_in(m, lo, hi):
    """lambda_-/lambda_+ in (lo, hi), lambda_pm = t/2 +- sqrt(Dq)."""
    Dl, beta, t = block(m); q = Dq(m)
    # (t/2 - s)/(t/2 + s) > lo  <=>  (1-lo) t/2 > (1+lo) s  <=> ((1-lo) t/2)^2 > (1+lo)^2 q (both sides >= 0)
    def gt(c): return ((1 - c) * t / 2) ** 2 > (1 + c) ** 2 * q and (1 - c) * t > 0
    return gt(lo) and not gt(hi)
def U2_cmp(me, mn, c):
    """Sign test of |U_tau3|^2 - c, |U|^2 = 1/2 + tr(C_e C_n)/(4 sqrt(Dq_e Dq_n)) in the plane
    (P = I/2 + C/sqrt(D), sqrt(D) = 2 sqrt(Dq))."""
    De, be, _ = block(me); Dn, bn, _ = block(mn)
    num = 2 * (De * Dn + be * bn / 2)              # tr(C_e C_n)
    den2 = 16 * Dq(me) * Dq(mn)                    # (4 sqrt(Dq_e Dq_n))^2
    # |U|^2 - c = (1/2 - c) + num/sqrt(den2)
    a = F(1, 2) - c
    # sign of a + num/sqrt(den2)
    if a >= 0 and num >= 0: return 1 if (a > 0 or num > 0) else 0
    if a <= 0 and num <= 0: return -1 if (a < 0 or num < 0) else 0
    lhs = a * a * den2; rhs = num * num
    if a > 0: return 1 if lhs > rhs else (-1 if lhs < rhs else 0)
    return 1 if rhs > lhs else (-1 if rhs < lhs else 0)

dc = F(143, 500)
me = charged(dc)


# ---------------------------------------------------------------------------
# certified enclosures in exact rationals (no floating point anywhere): square roots
# by integer Newton iteration, arctangents by the alternating Taylor series (whose
# partial sums bracket the value for 0 <= x <= 1), pi by Machin's formula; every
# rounding is outward to a dyadic, so each pair (lo, hi) is a rigorous enclosure.
# ---------------------------------------------------------------------------
isqrt = series.isqrt


def sqrt_encl(q, bits=64):
    """(lo, hi) with lo^2 <= q <= hi^2 and hi - lo = 2^(1-bits)."""
    n = (q.numerator << (2 * bits)) // q.denominator
    r = isqrt(n)
    lo, hi = F(r, 1 << bits), F(r + 2, 1 << bits)
    assert lo * lo <= q <= hi * hi
    return lo, hi


def rnd(x, bits, up):
    q, rem = divmod(x.numerator << bits, x.denominator)
    return F(q + (1 if (up and rem) else 0), 1 << bits)


def atan01(x, terms=60, bits=160):
    """(lo, hi) enclosing atan(x) for 0 <= x <= 1."""
    assert 0 <= x <= 1
    s, p, x2, lo, hi = F(0), x, x * x, None, None
    for k in range(terms):
        even = k % 2 == 0
        s = rnd(s + (p if even else -p) / (2 * k + 1), bits, even)
        if even:
            hi = s
        else:
            lo = s
        p = rnd(p * x2, bits, True)
    return lo, hi


_a5, _a239 = atan01(F(1, 5)), atan01(F(1, 239))
PI = (16 * _a5[0] - 4 * _a239[1], 16 * _a5[1] - 4 * _a239[0])
R2 = sqrt_encl(F(2))


def atan_deg(lo, hi):
    """Enclosure, in degrees, of atan over [lo, hi] with 0 <= lo <= hi (atan is increasing)."""
    assert 0 <= lo <= hi
    def one(x, up):
        if x <= 1:
            return atan01(x)[1 if up else 0]
        a = atan01(1 / x)
        return PI[1] / 2 - a[0] if up else PI[0] / 2 - a[1]
    a, b = one(lo, False), one(hi, True)
    return a * 180 / PI[1], b * 180 / PI[0]


def ang_deg(p, q):
    """Signed degrees from the direction of tangent q*sqrt2 to that of tangent p*sqrt2 (p, q >= 0,
    both directions in the first quadrant): tan of the difference is sqrt2 (p - q)/(1 + 2 p q)."""
    c = (p - q) / (1 + 2 * p * q)
    if c < 0:
        lo, hi = atan_deg(-c * R2[0], -c * R2[1])
        return -hi, -lo
    return atan_deg(c * R2[0], c * R2[1])


def tan2_coeff(m):
    """The heavy eigenvector of a plane block makes angle theta with s1 where
    tan 2 theta = B'/Delta = sqrt2 * beta/(2 Delta); return beta/(2 Delta) (needs Delta, beta > 0,
    so that 2 theta lies in (0, 90 degrees))."""
    Dl, beta, _ = block(m)
    assert Dl > 0 and beta > 0
    return beta / (2 * Dl)


def lam_D(d):        # lambda_D at d = alpha = 1: the coefficient of E in m (Step 1)
    return F(2, 3) * d * d


def r_max(d):        # the branch lambda_M >= lambda_D is M3/alpha <= r_max
    w = mv(add(J, E, d), one)
    return dot(w, w) / (3 * lam_D(d))


def nu_block_iv(d0, d1, s0, s1):
    """Interval enclosure over the box [d0, d1] x [s0, s1] of the plane block of
    s |w|^2 E + w w^T (proportional to m at lambda_D/lambda_M = s), w = (3, 3, u), u = 3 + d:
    A' = 18, C' = u^2 + s (18 + u^2), beta = 6 u.  C' is increasing and beta is increasing in
    u > 0 and s >= 0, so the corner values are exact bounds."""
    u0, u1 = 3 + d0, 3 + d1
    assert u0 > 0 and s0 >= 0
    C0, C1 = u0 * u0 + s0 * (18 + u0 * u0), u1 * u1 + s1 * (18 + u1 * u1)
    return ((18 - C1) / 2, (18 - C0) / 2), (6 * u0, 6 * u1)


def certify_branch(c, rho, maxdepth=16):
    """Adaptive bisection of d in [-1, 1], t = (M3/alpha)/r_max in [0, 1] (so s = rho t):
    on each box, a lower bound of tr(C_e C_nu) and an upper bound of Dq_nu certify
    |U_tau3|^2 - c > 0 by the squared inequality of U2_cmp; a box that fails is split.
    Returns (certified, boxes visited)."""
    De, be, _ = block(me)
    K = (F(1, 2) - c) ** 2 * 16 * Dq(me)
    assert c > F(1, 2)
    todo, n = [(F(-1), F(1), F(0), F(1))], 0
    while todo:
        d0, d1, t0, t1 = todo.pop()
        n += 1
        if n > 200000:
            return False, n
        (D0, D1), (b0, b1) = nu_block_iv(d0, d1, rho * t0, rho * t1)
        nlo = min(2 * De * D0, 2 * De * D1) + min(be * b0, be * b1)       # tr(C_e C_nu) >= nlo
        Dqhi = max(D0 * D0, D1 * D1) + b1 * b1 / 2                         # Dq_nu <= Dqhi (b0 > 0)
        if b0 > 0 and nlo > 0 and nlo * nlo > K * Dqhi:
            continue
        if d1 - d0 <= F(2, 1 << maxdepth):
            return False, n
        dm, tm = (d0 + d1) / 2, (t0 + t1) / 2
        todo += [(d0, dm, t0, tm), (dm, d1, t0, tm), (d0, dm, tm, t1), (dm, d1, tm, t1)]
    return True, n

def test_theta23():
    premise("neutrino.breaking-relation")
    # the observed window (0.39, 0.55) is data (NuFIT 2024), not a premise
    # 1. structure
    ok = all(x == 0 for x in mv(me, k))
    for d, r in [(dc, F(66)), (-dc, F(45)), (F(1, 3), F(7)), (F(-2), F(500))]:
        m = light(d, r)
        ok = ok and all(x == 0 for x in mv(m, k))
        lamD = F(2, 3) * d * d
        w = mv(add(J, E, d), one); W = [[w[i] * w[j] for j in range(3)] for i in range(3)]
        ok = ok and m == add(sc(lamD, E), sc(1 / (3 * r), W))
    GA.check("structure: m = (2 d^2/3) e3 e3^T + (1/3r) w w^T with w = M_D (1,1,1), exactly; (1,-1,0) is "
             "in the kernel of m and of M_e M_e^T (m_1 = m_e = 0), so both heavy eigenvectors lie in the "
             "S2-symmetric plane span{(1,1,0), e3}", ok)
    GA.check("charged calibration: m_mu/m_tau in (0.0594, 0.0596) at dc = 0.286 (exact singular-value ratio)",
             ratio_in(me, F(594, 10000) ** 2, F(596, 10000) ** 2))

    # 2. the instance of Remark rem:branch: d = dc, r = 66
    m1 = light(dc, F(66))
    GA.check("instance: m2/m3 in (0.168, 0.172) at d = 0.286, M3/alpha = 66", ratio_in(m1, F(168, 1000), F(172, 1000)))
    GA.check("instance: |U_tau3|^2 > 0.96 (heavy eigenvectors about 11 degrees apart), far above the "
             "window's 0.55: no near-maximal theta_23", U2_cmp(me, m1, F(96, 100)) > 0)

    # 3. mirror pairing of the two roots: lambda_M = |w|^2/(3r); the partner r' with
    #    lambda_M(r') = lambda_D^2/lambda_M(r) has the same m2/m3, and its heavy eigenvector is the
    #    reflection of r's across the bisector of w and e3: tr(P X) at r equals tr(P' Y) at r'.
    def partner(d, r):
        w = mv(add(J, E, d), one); w2 = dot(w, w); lamD = F(2, 3) * d * d
        lamM = w2 / (3 * r); lamM2 = lamD * lamD / lamM
        return w2 / (3 * lamM2)
    def heavy_overlap(m, v):
        """tr(P v v^T)/|v|^2 = 1/2 + tr(C V)/(2 sqrt(Dq)) in the plane; return (rational part num, Dq)
        with tr(C V) computed in the (s1/sqrt2, e3) basis: V = [[v1^2, v1 v2],[v1 v2, v2^2]]/|v|^2,
        v1 = v.s1/sqrt2, v2 = v3."""
        Dl, beta, _ = block(m)
        a1sq = dot(v, s1) ** 2 / 2; a2 = v[2]; cross = dot(v, s1) * a2   # = sqrt2 * v1 v2
        n2 = a1sq + a2 * a2
        trCV = (Dl * a1sq - Dl * a2 * a2 + 2 * (beta / 2) * cross) / n2   # B' v1 v2 *2 = (beta/sqrt2)(cross/sqrt2)*2
        return trCV, Dq(m)
    ok = True
    for d, r in [(dc, F(66)), (-dc, F(453, 10)), (F(1, 10), F(400)), (F(-1, 2), F(13))]:
        rp = partner(d, r)
        ma, mb = light(d, r), light(d, rp)
        # same ratio: t^2/Dq equal
        _, _, ta = block(ma); _, _, tb = block(mb)
        ok = ok and ta * ta / Dq(ma) == tb * tb / Dq(mb)
        w = mv(add(J, E, d), one)
        na, qa = heavy_overlap(ma, w); nb, qb = heavy_overlap(mb, s2)
        ok = ok and na * na / qa == nb * nb / qb and (na > 0) == (nb > 0)
    GA.check("mirror: the partner root r' = |w|^4/(9 lambda_D^2 r) has the same m2/m3, and its heavy "
             "eigenvector makes with e3 the angle r's makes with w: the two roots are reflections across "
             "the bisector, so tilt_1 + tilt_2 = tilt(w) + angle(u', e3)", ok)

    # 4. which root: the heavy eigenvector is nearer w than e3 iff lambda_M > lambda_D (sign test, exact)
    g = lcg(23)
    ok = True
    for _ in range(400):
        d = F((1 if next(g) % 2 else -1) * (1 + next(g) % 300), 300); r = F(1 + next(g) % 4000, 4)
        m = light(d, r); w = mv(add(J, E, d), one)
        lamM = dot(w, w) / (3 * r); lamD = F(2, 3) * d * d
        if lamM == lamD: continue
        na, qa = heavy_overlap(m, w); nb, qb = heavy_overlap(m, s2)
        # compare 1/2 + na/(2 sqrt qa) with 1/2 + nb/(2 sqrt qb): same qa = qb (same matrix)
        nearer_w = na > nb
        ok = ok and nearer_w == (lamM > lamD)
    GA.check("roots: on 400 random exact instances the heavy eigenvector is nearer w than e3 exactly "
             "when the seesaw term dominates, lambda_M > lambda_D (the perturbative root), and nearer "
             "e3 past the peak", ok)

    # 5. the second roots at the remark's size |d| = 0.286
    r2p = partner(dc, F(66))
    m2p = light(dc, r2p)
    GA.check("same sign, second root (M3/alpha about 470): m2/m3 in (0.168, 0.172) and |U_tau3|^2 in "
             "(0.55, 0.58): just outside the window", ratio_in(m2p, F(168, 1000), F(172, 1000))
             and U2_cmp(me, m2p, F(55, 100)) > 0 and U2_cmp(me, m2p, F(58, 100)) < 0)
    r1n = F(453, 10)
    m1n = light(-dc, r1n); r2n = partner(-dc, r1n); m2n = light(-dc, r2n)
    GA.check("opposite sign, first root (d = -0.286, M3/alpha = 45.3): m2/m3 in (0.168, 0.172) and "
             "|U_tau3|^2 > 0.98", ratio_in(m1n, F(168, 1000), F(172, 1000)) and U2_cmp(me, m1n, F(98, 100)) > 0)
    GA.check("opposite sign, second root (d = -0.286, M3/alpha about 530): m2/m3 in (0.168, 0.172), m1 = 0, "
             "and |U_tau3|^2 in (0.50, 0.55), inside the observed window (0.39, 0.55)",
             ratio_in(m2n, F(168, 1000), F(172, 1000)) and U2_cmp(me, m2n, F(50, 100)) > 0
             and U2_cmp(me, m2n, F(55, 100)) < 0)

    # 6. the perturbative branch over its whole domain |d| <= 1, lambda_M >= lambda_D (Step 3 of the
    #    proof), in exact rationals and certified enclosures, not by sampling.
    # 6a. the charged tilt, two-sided: the heavy eigenvectors of M_e M_e^T and of J (the direction u')
    #     have tan 2 theta = sqrt2 p; the tilt is half the difference of the two double angles
    pe, pu = tan2_coeff(me), tan2_coeff(J)
    te = ang_deg(pe, pu)
    tau_e = (te[0] / 2, te[1] / 2)
    GA.check("charged tilt: tan 2 tau_e = sqrt2 (p_e - p_u)/(1 + 2 p_e p_u) = 286 sqrt2/4357 exactly, so the "
             "charged heavy eigenvector lies between 2.65 and 2.66 degrees from u' towards e3 (certified)",
             (pe - pu) / (1 + 2 * pe * pu) == F(286, 4357) and F(265, 100) < tau_e[0] and tau_e[1] < F(266, 100))
    # 6b. the neutrino tilt is increasing in s: rho = lambda_D(read off m)/lam_D, so that
    #     M3/alpha = t r_max gives s = lambda_D/lambda_M = rho t; the certificate's block formulas agree
    #     exactly with block(3r m) on a grid that determines a polynomial of degree 2 in d and 1 in t
    rhos = []
    for d in [F(-1), F(-1, 2), F(1, 3), F(1)]:
        w = mv(add(J, E, d), one); m = light(d, F(1))
        lam = m[2][2] - w[2] * w[2] / 3                       # the coefficient of E in m at r = 1
        Wm = [[w[i] * w[j] for j in range(3)] for i in range(3)]
        rhos.append(lam / lam_D(d) if m == add(sc(lam, E), sc(F(1, 3), Wm)) else None)
    rho = rhos[0] if len(set(rhos)) == 1 else None
    ok = rho is not None and rho > 0
    for d in [F(-1), F(-1, 3), F(1, 3), F(1)]:
        for t in [F(1, 2), F(1)]:
            if not ok:
                break
            r = t * r_max(d)
            Dl, beta, _ = block(sc(3 * r, light(d, r)))
            (D0, D1), (b0, b1) = nu_block_iv(d, d, rho * t, rho * t)
            ok = ok and Dl == D0 == D1 and beta == b0 == b1
    (D0, D1), (b0, b1) = nu_block_iv(F(-1), F(1), F(0), F(0))
    ok = ok and b0 > 0 and 18 + (3 + F(-1)) ** 2 > 0
    for d in [F(-1), F(-1, 2), -dc, dc, F(1, 2), F(1)]:
        m = light(d, r_max(d)); w = mv(add(J, E, d), one)
        na, _ = heavy_overlap(m, w); nb, _ = heavy_overlap(m, s2)
        ok = ok and na == nb and na > 0
    GA.check("neutrino tilt monotone in s: in the (s1, e3) plane the heavy double angle is arg(Delta + i B') with "
             "B' = 6u/sqrt2 >= 12/sqrt2 > 0 fixed and Delta = (18 - u^2 - s(18 + u^2))/2 strictly decreasing in s "
             "for every |d| <= 1 (block formulas exact against 3r m); at s = 0 it is w-hat, at s = 1 the "
             "bisector of w-hat and e3 (exact equal overlaps)", ok)
    # 6c. the extreme tilts: tan theta_w = sqrt2 p_w, increasing in d; the bisector at d = 1 is the farthest
    #     neutrino direction on the e3 side, w-hat at d = -1 the farthest on the other
    def p_w(d):
        w = mv(add(J, E, d), one); return w[2] / dot(s1, w)
    q_u = one[2] / dot(s1, one)
    to_e3 = atan_deg(R2[0] / (2 * q_u), R2[1] / (2 * q_u))           # 90 degrees - theta_u = atan(sqrt2)
    a1 = ang_deg(p_w(F(1)), q_u)
    nu_hi = ((a1[0] + to_e3[0]) / 2, (a1[1] + to_e3[1]) / 2)
    nu_lo = ang_deg(q_u, p_w(F(-1)))
    sep_hi = nu_hi[1] - tau_e[0]; sep_lo = nu_lo[1] + tau_e[1]
    GA.check("separation: the neutrino heavy eigenvector lies between w-hat at d = -1 (10.02 to 10.03 degrees "
             "from u' away from e3) and the bisector at d = 1 (31.39 to 31.40 degrees towards it); with the charged "
             "tilt the separation is in (28.73, 28.75) degrees at the e3-side extreme and at most 12.69 on the other",
             p_w(F(-1)) < p_w(F(1)) and F(3139, 100) < nu_hi[0] and nu_hi[1] < F(3140, 100)
             and F(1002, 100) < nu_lo[0] and nu_lo[1] < F(1003, 100) and F(2873, 100) < nu_hi[0] - tau_e[1]
             and sep_hi < F(2875, 100) and sep_lo < F(1269, 100) and sep_lo < nu_hi[0] - tau_e[1])
    # 6d. so |U|^2 = cos^2(separation) is least at the extreme configuration d = 1, lambda_M = lambda_D
    m_top = light(F(1), r_max(F(1)))
    w_bot = mv(add(J, E, F(-1)), one); m_bot = [[w_bot[i] * w_bot[j] for j in range(3)] for i in range(3)]
    GA.check("perturbative branch, exact minimum: |U_tau3|^2 is least at d = 1, lambda_M = lambda_D, where it lies "
             "in (0.7687, 0.7688); at the other extreme (d = -1, s -> 0) it exceeds 0.95",
             U2_cmp(me, m_top, F(7687, 10000)) > 0 and U2_cmp(me, m_top, F(7688, 10000)) < 0
             and U2_cmp(me, m_bot, F(95, 100)) > 0)
    # 6e. an independent certificate that uses no monotonicity: adaptive bisection of the whole domain
    ok, nb = certify_branch(F(7687, 10000), rho) if rho is not None else (False, 0)
    GA.check(f"perturbative branch, certified over the whole domain d in [-1, 1], lambda_D/lambda_M in [0, 1] "
             f"({nb} boxes, rational interval bounds): |U_tau3|^2 > 0.7687 > 0.76 everywhere, so with 6d its "
             "infimum is in (0.7687, 0.7688) and attained: no near-maximal "
             "theta_23 on that branch at any size up to one", ok)
    # 7. the peak of m2/m3 in M3/alpha: at lambda_M = lambda_D, (lambda_+ - lambda_-)/(lambda_+ + lambda_-)
    #    = cos(phi), phi the angle between w and e3, so the peak ratio is tan^2(phi/2); at d = 0.286 it lies
    #    at M3/alpha = |w|^2/(3 lambda_D) = 176.0 with value in (0.240, 0.241)
    ok = True
    for d in [dc, -dc, F(1, 7), F(-3, 4)]:
        w = mv(add(J, E, d), one); lamD = F(2, 3) * d * d
        rpk = dot(w, w) / (3 * lamD)
        mp = light(d, rpk)
        _, _, t = block(mp)
        ok = ok and 4 * Dq(mp) / (t * t) == dot(w, s2) ** 2 / dot(w, w)
    w = mv(add(J, E, dc), one); rpk = dot(w, w) / (3 * F(2, 3) * dc * dc)
    ok = ok and F(1759, 10) < rpk < F(1761, 10) and ratio_in(light(dc, rpk), F(240, 1000), F(241, 1000))
    GA.check("peak: at lambda_M = lambda_D the light ratio is tan^2(phi/2); at d = 0.286 the peak sits at "
             "M3/alpha = 176.0 with m2/m3 in (0.240, 0.241), the remark's 'near 0.24 at about 176'", ok)
    assert not GA.FAILURES
