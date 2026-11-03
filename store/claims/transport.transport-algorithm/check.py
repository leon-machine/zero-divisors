"""transport.transport-algorithm: exact checks of the six steps in operational form.

All computations in GA.py (diagonal signatures, exact rationals). Signatures (p, q) with 1 <= n = p + q <= 5.
Step 1. A null vector v (mixed signatures) has v^2 = 0, so v x = 1 would give v = v^2 x = 0: no inverse in any unital
    algebra containing the base; left multiplication by v has rank 2^{n-1} on Cl(p, q). A nontrivial idempotent
    e has e (1 - e) = 0.
Step 2. Diagnosis loci, computed: null vectors exist exactly when p q != 0 (e_0 + e_p null; a definite form has
    no isotropic vector, by the congruence signature); the central blades are 1 (n even) or 1 and omega (n odd),
    and a nontrivial central idempotent exists exactly when n is odd and omega^2 = +1, i.e. p - q = 1 mod 4, and is
    then (1 +- omega)/2, each generating a proper two-sided ideal of dimension 2^{n-1} (not simple). The cautions: in Cl(2,0) x = e1 + e1 e2 is nilpotent with no null vector present;
    Cl(2,1) carries all three types (null e0 + e2, central (1 +- e0 e1 e2)/2, non-central (1 + e0)/2).
    Exhaustiveness on samples: a null basis pair v = e_i + e_j is annihilated by the idempotent (1 - e_i e_j)/2.
Step 3. Rule 1: in Cl(p+1, q+1) the ladder f = (e+ + e-)/2, f* = (e+ - e-)/2 gives matrix units
    (E11 = f f*, E22 = f* f, E12 = f, E21 = f*), and a -> a f f* is injective on Cl(p, q) (the corner is the base).
    Rule 2 (p - q = 1 mod 4, nu^2 = +1 or -1): the new volume element anticommutes with every generator (the grade
    involution becomes inner), nu exchanges eps_+ and eps_-, the completion has centre R; the null-generator
    ascent (nu^2 = 0) gives the ideal A nu with (A nu)^2 = 0. Type P: e e e = e for non-central idempotents.
Step 4. In the completion, e+ conjugation is (s, x, t) -> -(2t, x, s/2) on N = s nO + x + t nInf with
    nO = (e- - e+)/2, nInf = e- + e+, preserving Q(x) - 2 s t.
Step 5. Read-out [s nO + x + t nInf] -> x/s returns x/Q(x) on lifted invertible points and refuses (s = 0) on
    lifted null points; the pinching E(x) = P x P + (1-P) x (1-P), P = f f*, kills exactly the ladder f, f*.
Step 6. Rule 1 fixes p - q mod 8 and the computed type-C diagnosis; Rule 2 moves the residue by +-1 off the split
    classes; over all transport histories from n <= 3 up to n <= 5, Rule 2 is applied at most once (and is
    applied in some); every completion has zero divisors (null f; the non-central idempotent eps_+ after Rule 2).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(p, n - p) for n in range(1, 6) for p in range(n + 1)]
SMALL = [(p, n - p) for n in range(1, 4) for p in range(n + 1)]
XS = [(1, 2, -1, 3), (3, 0, 1, -2), (2, -1, 0, 5)]


def vol(n, sq):
    w = GA.sc(1)
    for i in range(n):
        w = GA.mul(w, GA.gen(i), sq)
    return w


def central_blades(n, sq):
    return [b for b in GA.all_blades(n)
            if all(GA.commutes({b: F(1)}, GA.gen(i), sq) for i in range(n))]


def type_c(p, q):
    n = p + q
    sq = GA.sig(p, q)
    cb = central_blades(n, sq)
    if len(cb) == 1:
        return False
    w = vol(n, sq)
    return GA.mul(w, w, sq) == {(): F(1)}


def check_step1_no_inverse_at_null_vectors_and_idempotents():
    premise("transport.noinverse")
    ok = True
    for p, q in SIGS:
        if p * q == 0 or p + q > 4:
            continue
        n, sq = p + q, GA.sig(p, q)
        v = GA.add(GA.gen(0), GA.gen(p))
        ok = ok and GA.mul(v, v, sq) == {} and v != {}
        blades = GA.all_blades(n)
        rows = [GA.basis_vector_of(GA.mul(v, {b: F(1)}, sq), blades) for b in blades]
        ok = ok and GA.rank_of_vectors(rows) == 2 ** (n - 1)
        e = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(GA.gen(0), GA.gen(p), sq)))
        ok = ok and GA.eq(GA.mul(e, e, sq), e) and GA.mul(e, GA.sub(GA.sc(1), e), sq) == {}
    _tp_rv = (ok); assert _tp_rv is not False, "check_step1_no_inverse_at_null_vectors_and_idempotents"; return _tp_rv


def check_step2_diagnosis_loci_and_cautions():
    premise("transport.existence-locus-type-n")
    premise("transport.existence-classification-type-c")
    premise("transport.exhaustiveness-every-zero-divisor-annihilated-idempotent")
    premise("transport.classification-real-clifford-algebras")
    ok = True
    n_c = 0
    for p, q in SIGS:
        n, sq = p + q, GA.sig(p, q)
        gram = [[F(sq[i]) if i == j else F(0) for j in range(n)] for i in range(n)]
        pos, neg = GA.congruence_signature(gram)[:2]
        ok = ok and (pos * neg != 0) == (p * q != 0)
        if p * q:
            for i in range(p):
                for j in range(p, n):
                    v = GA.add(GA.gen(i), GA.gen(j))
                    e = GA.scal(F(1, 2), GA.sub(GA.sc(1), GA.mul(GA.gen(i), GA.gen(j), sq)))
                    ok = ok and GA.mul(v, v, sq) == {} and GA.eq(GA.mul(e, e, sq), e)
                    ok = ok and GA.mul(v, e, sq) == {}
        cb = central_blades(n, sq)
        ok = ok and len(cb) == (2 if n % 2 else 1)
        tc = type_c(p, q)
        ok = ok and tc == ((p - q) % 4 == 1)
        if tc:
            w = vol(n, sq)
            for s in (1, -1):
                eps = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.scal(s, w)))
                ok = ok and GA.eq(GA.mul(eps, eps, sq), eps)
                ok = ok and all(GA.commutes(eps, GA.gen(i), sq) for i in range(n))
                # eps A is a proper nonzero two-sided ideal: the algebra is not simple
                blades = GA.all_blades(n)
                rows = [GA.basis_vector_of(GA.mul(eps, {b: F(1)}, sq), blades) for b in blades]
                ok = ok and GA.rank_of_vectors(rows) == 2 ** (n - 1)
            n_c += 1
    # cautions
    s20 = GA.sig(2, 0)
    x = GA.add(GA.gen(0), GA.mul(GA.gen(0), GA.gen(1), s20))
    ok = ok and GA.mul(x, x, s20) == {} and x != {}
    s21 = GA.sig(2, 1)
    null = GA.add(GA.gen(0), GA.gen(2))
    cen = GA.scal(F(1, 2), GA.add(GA.sc(1), vol(3, s21)))
    nc = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.gen(0)))
    ok = ok and GA.mul(null, null, s21) == {} and GA.eq(GA.mul(cen, cen, s21), cen)
    ok = ok and all(GA.commutes(cen, GA.gen(i), s21) for i in range(3))
    ok = ok and GA.eq(GA.mul(nc, nc, s21), nc) and not GA.commutes(nc, GA.gen(1), s21)
    _tp_rv = (ok and n_c == 6); assert _tp_rv is not False, "check_step2_diagnosis_loci_and_cautions"; return _tp_rv


def check_step3_the_three_rules():
    premise("transport.rule-1-morita-trivial")
    premise("transport.rule-2-ideal-fusion-sharp-form")
    premise("transport.one-generator-minimal-minimal-completions-classified")
    premise("transport.type-p-self-repairing")
    ok = True
    fused = 0
    for p, q in SIGS:
        n = p + q
        if n > 3:
            continue
        sq = GA.sig(p, q) + (1, -1)
        f = GA.scal(F(1, 2), GA.add(GA.gen(n), GA.gen(n + 1)))
        fs = GA.scal(F(1, 2), GA.sub(GA.gen(n), GA.gen(n + 1)))
        E = {(1, 1): GA.mul(f, fs, sq), (2, 2): GA.mul(fs, f, sq), (1, 2): f, (2, 1): fs}
        ok = ok and GA.add(E[1, 1], E[2, 2]) == {(): F(1)}
        for (i, j), a in E.items():
            for (k, l), b in E.items():
                ok = ok and GA.eq(GA.mul(a, b, sq), E[i, l] if j == k else {})
        blades = GA.all_blades(n)
        imgs = [GA.basis_vector_of(GA.mul({b: F(1)}, E[1, 1], sq), GA.all_blades(n + 2)) for b in blades]
        ok = ok and GA.rank_of_vectors(imgs) == 2 ** n
        if (p - q) % 4 == 1:
            for gam in (1, -1):
                sq2 = GA.sig(p, q) + (gam,)
                w = vol(n, sq2)
                epsp = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
                epsm = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
                nu = GA.gen(n)
                ok = ok and GA.eq(GA.mul(nu, epsp, sq2), GA.mul(epsm, nu, sq2))
                w2 = vol(n + 1, sq2)
                ok = ok and all(GA.anticommutes(w2, GA.gen(i), sq2) for i in range(n + 1))
                ok = ok and central_blades(n + 1, sq2) == [()]
                fused += 1
            sq0 = GA.sig(p, q, 1)
            nu = GA.gen(n)
            for b1 in GA.all_blades(n)[:4]:
                for b2 in GA.all_blades(n)[-4:]:
                    ok = ok and GA.mul(GA.mul({b1: F(1)}, nu, sq0), GA.mul({b2: F(1)}, nu, sq0), sq0) == {}
        for e in (GA.scal(F(1, 2), GA.add(GA.sc(1), GA.gen(0))),):
            sqb = GA.sig(p, q)
            if sqb[0] == 1:
                ok = ok and GA.eq(GA.mul(GA.mul(e, e, sqb), e, sqb), e)
    _tp_rv = (ok and fused == 6); assert _tp_rv is not False, "check_step3_the_three_rules"; return _tp_rv


def check_steps4_and_5_compute_then_descend():
    premise("transport.swap-rescale-normal-form")
    premise("transport.totality")
    premise("transport.descent-read-out-map")
    premise("transport.pinching-kernel")
    ok = True
    refusals = 0
    for p, q in ((1, 1), (2, 1), (1, 2)):
        n = p + q
        sq = GA.sig(p, q) + (1, -1)
        ep, em = GA.gen(n), GA.gen(n + 1)
        no = GA.scal(F(1, 2), GA.sub(em, ep))
        ninf = GA.add(em, ep)
        for c in XS + [(1, 1, 0, 0), (1, 0, 1, 0)]:
            x = {(i,): F(v) for i, v in enumerate(c[:n]) if v}
            Q = GA.mul(x, x, sq).get((), F(0))
            for s, t in ((F(1), F(2)), (F(-2), F(1, 3))):
                N = GA.add(GA.scal(s, no), x, GA.scal(t, ninf))
                M = GA.neg(GA.mul(GA.mul(ep, N, sq), ep, sq))
                ok = ok and -GA.dot(M, ninf, sq) == 2 * t and -GA.dot(M, no, sq) == s / 2
            X = GA.add(no, x, GA.scal(Q / 2, ninf))
            img = GA.mul(GA.mul(ep, X, sq), ep, sq)
            s_out = -GA.dot(img, ninf, sq)
            x_out = {b: c2 for b, c2 in img.items() if b[0] < n}
            if Q != 0:
                ok = ok and GA.eq(GA.scal(1 / s_out, x_out), GA.scal(1 / Q, x))
            else:
                ok = ok and s_out == 0
                refusals += 1
        f = GA.scal(F(1, 2), GA.add(ep, em))
        fs = GA.scal(F(1, 2), GA.sub(ep, em))
        P = GA.mul(f, fs, sq)
        Pc = GA.sub(GA.sc(1), P)

        def E(y):
            return GA.add(GA.mul(GA.mul(P, y, sq), P, sq), GA.mul(GA.mul(Pc, y, sq), Pc, sq))
        ok = ok and E(f) == {} and E(fs) == {} and GA.eq(E(GA.gen(0)), GA.gen(0))
    _tp_rv = (ok and refusals == 4); assert _tp_rv is not False, "check_steps4_and_5_compute_then_descend"; return _tp_rv


def check_step6_bookkeeping_and_no_termination():
    premise("transport.rule-1-morita-trivial")
    premise("transport.fusion-occurs-most-once")
    premise("transport.no-transport-terminates")
    ok = True
    cache = {}

    def tc(p, q):
        if (p, q) not in cache:
            cache[(p, q)] = type_c(p, q)
        return cache[(p, q)]
    max_rule2 = 0
    used = 0
    stack = [((p, q), 0) for p, q in SMALL]
    while stack:
        (p, q), k = stack.pop()
        nxt = [((p + 1, q + 1), k)]
        if tc(p, q):
            nxt += [((p + 1, q), k + 1), ((p, q + 1), k + 1)]
            used += 1
        for (a, b), kk in nxt:
            if a + b > 5:
                continue
            if kk == k:
                ok = ok and (a - b) % 8 == (p - q) % 8 and tc(a, b) == tc(p, q)
            else:
                ok = ok and ((a - b) - (p - q)) in (1, -1) and not tc(a, b)
            max_rule2 = max(max_rule2, kk)
            stack.append(((a, b), kk))
    ok = ok and max_rule2 == 1 and used > 0
    # no termination: Rule-1 completions carry the null f; Rule-2 completions the non-central eps_+
    for p, q in SMALL:
        n = p + q
        sq = GA.sig(p, q) + (1, -1)
        f = GA.scal(F(1, 2), GA.add(GA.gen(n), GA.gen(n + 1)))
        ok = ok and GA.mul(f, f, sq) == {} and f != {}
        if tc(p, q):
            sq2 = GA.sig(p, q) + (1,)
            eps = GA.scal(F(1, 2), GA.add(GA.sc(1), vol(n, sq2)))
            ok = ok and GA.eq(GA.mul(eps, eps, sq2), eps) and not GA.commutes(eps, GA.gen(n), sq2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_step6_bookkeeping_and_no_termination"; return _tp_rv
