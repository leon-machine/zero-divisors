"""one-relation.imported-single-mode-thermality-modular-period: exact checks of the finite cores of this Fact.

(1) Single-mode thermality: the ladder pair of the ascent, in Cl(1,1) as v = (e0 + e1)/2, v* = (e0 - e1)/2, has
    v^2 = v*^2 = 0, v v* + v* v = 1, and its boost generator e0 e1 / 2 = N - 1/2 (N = v* v); on the mode factor
    M_2 (a = [[0, 1], [0, 0]], N = diag(0, 1)) the KMS condition for the flow of K = N - 1/2 at Boltzmann factor
    q = e^{-beta w} has, among all 2 x 2 density matrices, the one-dimensional solution space spanned by
    diag(1, q) (exact Gibbs state, even: omega(a) = omega(a^dag) = 0, occupation q/(1 + q)), at sample q.
(2) The clock period: the boost of a completed pair moves the ladder with adjoint eigenvalues +1, -1 (unit
    rapidity), and the Euclidean period 2 pi in rapidity converts at the horizon rate kappa = f'(2M)/2 = 1/(4M)
    (f = 1 - 2M/r) to beta = 2 pi/kappa = 8 pi M: the coefficient of pi is 8M at sample M.
(3) The descent is a one-way conditional expectation (Proposition transport.pinching-kernel): in
    B = Cl(p+1, q+1) over A = Cl(p, q) with f = (e+ + e-)/2, f* = (e+ - e-)/2, P = f f*, the pinching
    E(x) = P x P + (1 - P) x (1 - P) is idempotent with E(1) = 1, fixes every base blade, kills A f and A f*, has
    rank 2^{n+1} = dim(A + A f f*) on the 2^{n+2} blades (so its kernel is exactly A f + A f*), is a bimodule map
    over the commutant on samples, and the corner read-out D(x) = P x P has the interposition defect
    D(x y) - D(x) D(y) = P x (1 - P) y P, nonzero at (x, y) = (f, f*): no descent through it is multiplicative.
Not checked here: the absence of any unital homomorphism B -> A (Theorem transport.door-one-way, which has its
own check), the trace-uniqueness clause (Takesaki), and the statement that no result at the singular boundary
can supply (R).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QS = [F(1, 2), F(9, 16), F(3)]
MASSES = [F(1, 2), F(2), F(5, 3)]
BASES = [(1, 1), (1, 2), (2, 1)]


mm = GA.mat_mul


def madd(a, b, c=1):
    return [[a[i][j] + F(c) * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def check_single_mode_thermality():
    premise("singularity.modular-descent")
    premise("singularity.p-univalence")
    premise("singularity.r-regularity-fixed-locus")
    sq = GA.sig(1, 1)
    e0, e1 = GA.gen(0), GA.gen(1)
    v = GA.scal(F(1, 2), GA.add(e0, e1))
    vs = GA.scal(F(1, 2), GA.sub(e0, e1))
    ok = GA.mul(v, v, sq) == {} and GA.mul(vs, vs, sq) == {}
    ok = ok and GA.add(GA.mul(v, vs, sq), GA.mul(vs, v, sq)) == {(): F(1)}
    ok = ok and GA.eq(GA.scal(F(1, 2), GA.mul(e0, e1, sq)), GA.sub(GA.mul(vs, v, sq), GA.sc(F(1, 2))))
    a = [[F(0), F(1)], [F(0), F(0)]]
    ad = [[F(0), F(0)], [F(1), F(0)]]
    ok = ok and madd(mm(a, ad), mm(ad, a)) == [[F(1), F(0)], [F(0), F(1)]] and mm(a, a) == [[F(0)] * 2] * 2
    for q in QS:
        G = [F(1), q]                                    # e^{-beta K} up to the factor q^{-1/2}
        rows = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        # tr(rho E_ij E_kl) - tr(rho E_kl G E_ij G^{-1}) over the 4 unknowns rho[r][c]
                        row = [F(0)] * 4
                        if j == k:
                            row[2 * l + i] += 1
                        if l == i:
                            row[2 * j + k] -= G[i] / G[j]
                        rows.append(row)
        ker = GA.field_kernel(rows)
        ok = ok and len(ker) == 1
        rho = ker[0]
        Z = rho[0] + rho[3]
        rho = [x / Z for x in rho]
        ok = ok and rho == [1 / (1 + q), F(0), F(0), q / (1 + q)]
        ok = ok and rho[1] == 0 and rho[2] == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_single_mode_thermality"; return _tp_rv


def check_clock_period_is_eight_pi_m():
    premise("scrambling.clock-inventory-boundary-modes")
    sq = GA.sig(1, 1)
    e0, e1 = GA.gen(0), GA.gen(1)
    v = GA.scal(F(1, 2), GA.add(e0, e1))
    vs = GA.scal(F(1, 2), GA.sub(e0, e1))
    K = GA.scal(F(1, 2), GA.mul(e0, e1, sq))
    ok = GA.eq(GA.sub(GA.mul(K, v, sq), GA.mul(v, K, sq)), GA.neg(v))
    ok = ok and GA.eq(GA.sub(GA.mul(K, vs, sq), GA.mul(vs, K, sq)), vs)
    for M in MASSES:
        rh = 2 * M
        kappa = (2 * M / (rh * rh)) / 2
        ok = ok and kappa == 1 / (4 * M) and 2 / kappa == 8 * M
    _tp_rv = (ok); assert _tp_rv is not False, "check_clock_period_is_eight_pi_m"; return _tp_rv


def setting(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    f = GA.scal(F(1, 2), GA.add(ep, em))
    fs = GA.scal(F(1, 2), GA.sub(ep, em))
    return n, sq, f, fs, GA.mul(f, fs, sq)


def bimodule_samples(n, sq, P, f, fs):
    base = [{b: F(1)} for b in GA.all_blades(n)]
    c1 = GA.add(base[1], GA.mul(base[-1], P, sq))
    c2 = GA.sub(GA.sc(2), GA.mul(base[2 % len(base)], P, sq))
    xs = [GA.add(f, base[1]), GA.add(GA.mul(fs, base[-1], sq), GA.sc(3)), GA.sub(fs, base[-1])]
    return c1, c2, xs


def check_descent_is_a_one_way_conditional_expectation():
    premise("transport.pinching-kernel")
    premise("singularity.imported-descent-one-way-conditional-expectation")
    ok = True
    for p, q in BASES:
        n, sq, f, fs, P = setting(p, q)
        Q = GA.sub(GA.sc(1), P)
        ok = ok and GA.eq(GA.mul(P, P, sq), P)

        def E(x):
            return GA.add(GA.mul(GA.mul(P, x, sq), P, sq), GA.mul(GA.mul(Q, x, sq), Q, sq))
        ok = ok and GA.eq(E(GA.sc(1)), GA.sc(1)) and E(f) == {} and E(fs) == {}
        base = [{b: F(1)} for b in GA.all_blades(n)]
        for a in base:
            ok = ok and GA.eq(E(a), a)
            ok = ok and E(GA.mul(a, f, sq)) == {} and E(GA.mul(a, fs, sq)) == {}
        allb = GA.all_blades(n + 2)
        images = [E({b: F(1)}) for b in allb]
        ok = ok and all(GA.eq(E(y), y) for y in images)
        rank = GA.rank_of_vectors([GA.basis_vector_of(y, allb) for y in images])
        ok = ok and rank == 2 ** (n + 1) and len(allb) == 2 ** (n + 2)
        # blades with exactly one of e+, e- are killed, the others fixed: 2^{n+1} each
        killed = [b for b in allb if E({b: F(1)}) == {}]
        fixed = [b for b in allb if GA.eq(E({b: F(1)}), {b: F(1)})]
        ok = ok and len(killed) == 2 ** (n + 1) and len(fixed) == 2 ** (n + 1)
        ok = ok and all((n in b) != (n + 1 in b) for b in killed)
        # bimodule property over the commutant, on samples
        c1, c2, xs = bimodule_samples(n, sq, P, f, fs)
        for x in xs:
            ok = ok and GA.eq(E(GA.mul(GA.mul(c1, x, sq), c2, sq)), GA.mul(GA.mul(c1, E(x), sq), c2, sq))

        def D(x):
            return GA.mul(GA.mul(P, x, sq), P, sq)
        for x, y in [(f, fs)] + [(xs[0], xs[1])]:
            defect = GA.sub(D(GA.mul(x, y, sq)), GA.mul(D(x), D(y), sq))
            ok = ok and GA.eq(defect, GA.mul(GA.mul(GA.mul(GA.mul(P, x, sq), Q, sq), y, sq), P, sq))
        ok = ok and GA.sub(D(GA.mul(f, fs, sq)), GA.mul(D(f), D(fs), sq)) != {}
    _tp_rv = (ok); assert _tp_rv is not False, "check_descent_is_a_one_way_conditional_expectation"; return _tp_rv
