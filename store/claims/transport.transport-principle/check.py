"""transport.transport-principle: exact checks of the finite content of the three cases and of exhaustiveness.

GA.py, signatures (p, q) with n = p + q <= 3 unless stated.
(a) Isotropic vector: a null v has v^2 = 0 (so no inverse in any unital extension: v x = 1 forces v = v^2 x = 0);
    in the completion Cl(p+1, q+1) (nO = (e- - e+)/2, nInf = e- + e+) the reciprocal on points
    [N] -> [e+ N e+] sends every sample nonzero null vector to a nonzero null vector (total), and sends the lift of
    an invertible x to the lift of x/Q(x) (Theorem transport.totality). The increment (+1, +1): an added plane can
    carry the lift's pair (two independent null vectors with nO . nInf = -1) only if it is indefinite; the
    planes of signature (2, 0) and (0, 2) have no nonzero null vector (congruence signature).
(b) Central idempotent (p - q = 1 mod 4): adjoining nu with nu^2 = +1 or -1 makes the grade involution inner (the
    new volume element anticommutes with every generator), nu conjugates eps_+ to eps_- (the ideals fuse), the
    completion's centre is R (simple), the two signs give isomorphic completions (nu -> w nu, w the ground volume
    element: w nu squares to -1, anticommutes with the ground generators, and with them generates all 2^{n+1}
    dimensions, computed by rank), and the null ascent (nu^2 = 0) leaves the square-zero ideal A nu. Minimality
    among simple real algebras is not tested.
(c) Non-central idempotent: sigma(e) = e satisfies e sigma(e) e = e and sigma(e) e sigma(e) = sigma(e), and
    its conjugate by a sample invertible versor g is again an idempotent (sigma commutes with the conjugation),
    for sample non-central idempotents.
(d) Exhaustiveness on samples: v g (v null, g invertible) is annihilated on the right by the idempotent
    g^{-1} e g with e = (1 - e_i e_j)/2; a non-central idempotent e by 1 - e; in the split signatures eps_+ x is
    annihilated by the central eps_-.
Not checked: the element-level no-go and its cohomological form (Theorems transport.no-go-level-elements,
transport.cohomological-form-no-go), the representation- and embedding-independence of minimality, and the
continuity and uniqueness of the extended reciprocal.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(p, n - p) for n in range(1, 4) for p in range(n + 1)]
XS = [(1, 2, -1), (3, 0, 1), (2, -1, 5)]


def vol(n, sq):
    w = GA.sc(1)
    for i in range(n):
        w = GA.mul(w, GA.gen(i), sq)
    return w


def inverse_versor(g, sq):
    """Inverse of a product of non-null vectors: g~ / (g g~)."""
    gr = GA.reverse(g)
    nrm = GA.mul(g, gr, sq)
    return GA.scal(1 / nrm[()], gr)


def sample_unit(n, sq):
    """An invertible non-scalar sample element of Cl(p, q)."""
    if n > 2:
        return GA.add(GA.sc(2), GA.mul(GA.gen(0), GA.gen(n - 1), sq))
    return GA.add(GA.sc(3), GA.gen(0))


def sample_element(n):
    return GA.add(GA.gen(0), GA.sc(5), GA.gen(n - 1))


def check_isotropic_vector_repaired_on_points():
    premise("transport.totality")
    premise("transport.minimality")
    ok = True
    mixed = 0
    for p, q in SIGS:
        n = p + q
        sq = GA.sig(p, q) + (1, -1)
        ep, em = GA.gen(n), GA.gen(n + 1)
        no = GA.scal(F(1, 2), GA.sub(em, ep))
        ninf = GA.add(em, ep)
        ok = ok and GA.dot(no, ninf, sq) == -1
        if p * q:
            v = GA.add(GA.gen(0), GA.gen(p))
            ok = ok and GA.mul(v, v, sq) == {}
            mixed += 1
        for c in XS:
            x = {(i,): F(val) for i, val in enumerate(c[:n]) if val}
            Q = GA.mul(x, x, sq).get((), F(0))
            samples = [(F(1), Q / 2), (F(2), Q / 4)] + ([(F(0), F(1))] if Q == 0 else [])
            for s, t in samples:
                N = GA.add(GA.scal(s, no), x, GA.scal(t, ninf))
                M = GA.mul(GA.mul(ep, N, sq), ep, sq)
                ok = ok and GA.mul(N, N, sq) == {} and GA.mul(M, M, sq) == {} and M != {}
            if Q != 0:
                X = GA.add(no, x, GA.scal(Q / 2, ninf))
                xr = GA.scal(1 / Q, x)
                Xr = GA.add(no, xr, GA.scal(GA.mul(xr, xr, sq).get((), F(0)) / 2, ninf))
                ok = ok and GA.eq(GA.mul(GA.mul(ep, X, sq), ep, sq), GA.scal(-Q, Xr))
    planes = [((1, 1), [[F(1), F(0)], [F(0), F(-1)]], True), ((2, 0), [[F(1), F(0)], [F(0), F(1)]], False),
              ((0, 2), [[F(-1), F(0)], [F(0), F(-1)]], False)]
    for plane, gram, has_null in planes:
        pos, neg = GA.congruence_signature(gram)[:2]
        ok = ok and (pos, neg) == plane and (pos * neg != 0) == has_null
    _tp_rv = (ok and mixed == 3); assert _tp_rv is not False, "check_isotropic_vector_repaired_on_points"; return _tp_rv


def check_central_idempotent_repaired_one_dimension_up():
    premise("transport.rule-2-ideal-fusion-sharp-form")
    premise("transport.one-generator-minimal-minimal-completions-classified")
    ok = True
    done = 0
    for p, q in SIGS:
        if (p - q) % 4 != 1:
            continue
        n = p + q
        for gam in (1, -1):
            sq = GA.sig(p, q) + (gam,)
            w = vol(n, sq)
            ok = ok and GA.mul(w, w, sq) == {(): F(1)}
            epsp = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
            epsm = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
            nu = GA.gen(n)
            ok = ok and GA.eq(GA.mul(GA.mul(nu, epsp, sq), inverse_versor(nu, sq), sq), epsm)
            w2 = vol(n + 1, sq)
            ok = ok and all(GA.anticommutes(w2, GA.gen(i), sq) for i in range(n + 1))
            central = [b for b in GA.all_blades(n + 1)
                       if all(GA.commutes({b: F(1)}, GA.gen(i), sq) for i in range(n + 1))]
            ok = ok and central == [()]
            if gam == 1:
                # the two signs are isomorphic: nu' = w nu squares to -1 and anticommutes with every ground
                # generator, and the ground generators with nu' generate all 2^(n+1) dimensions (rank of words)
                nup = GA.mul(w, nu, sq)
                ok = ok and GA.mul(nup, nup, sq) == {(): F(-1)}
                ok = ok and all(GA.anticommutes(nup, GA.gen(i), sq) for i in range(n))
                gens = [GA.gen(i) for i in range(n)] + [nup]
                blades = GA.all_blades(n + 1)
                rows = []
                for mask in range(2 ** (n + 1)):
                    word = GA.sc(1)
                    for i in range(n + 1):
                        if (mask >> i) & 1:
                            word = GA.mul(word, gens[i], sq)
                    rows.append([word.get(b, F(0)) for b in blades])
                ok = ok and GA.rank_of_vectors(rows) == 2 ** (n + 1)
            done += 1
        sq0 = GA.sig(p, q, 1)
        nu = GA.gen(n)
        for b1 in GA.all_blades(n):
            for b2 in GA.all_blades(n):
                ok = ok and GA.mul(GA.mul({b1: F(1)}, nu, sq0), GA.mul({b2: F(1)}, nu, sq0), sq0) == {}
    _tp_rv = (ok and done == 6); assert _tp_rv is not False, "check_central_idempotent_repaired_one_dimension_up"; return _tp_rv


def check_non_central_idempotent_is_its_own_repair():
    premise("transport.type-p-self-repairing")
    ok = True
    count = 0
    for p, q in SIGS:
        n = p + q
        sq = GA.sig(p, q)
        if p == 0 or n < 2:
            continue
        g = GA.add(GA.gen(0), GA.scal(2, GA.gen(n - 1)))
        if GA.mul(g, g, sq).get((), F(0)) == 0:
            g = GA.add(GA.gen(0), GA.scal(3, GA.gen(n - 1)))
        gi = inverse_versor(g, sq)
        for e in (GA.scal(F(1, 2), GA.add(GA.sc(1), GA.gen(0))),):
            ok = ok and GA.eq(GA.mul(e, e, sq), e) and not GA.commutes(e, GA.gen(n - 1), sq)
            sig_e = e
            ok = ok and GA.eq(GA.mul(GA.mul(e, sig_e, sq), e, sq), e)
            ok = ok and GA.eq(GA.mul(GA.mul(sig_e, e, sq), sig_e, sq), sig_e)
            th = GA.mul(GA.mul(g, e, sq), gi, sq)
            ok = ok and GA.eq(GA.mul(th, th, sq), th)
            count += 1
    _tp_rv = (ok and count == 5); assert _tp_rv is not False, "check_non_central_idempotent_is_its_own_repair"; return _tp_rv


def check_trichotomy_exhaustive_on_samples():
    premise("transport.exhaustiveness-every-zero-divisor-annihilated-idempotent")
    premise("transport.no-fourth-rule")
    ok = True
    hits = 0
    for p, q in SIGS:
        n = p + q
        sq = GA.sig(p, q)
        if p * q:
            v = GA.add(GA.gen(0), GA.gen(p))
            e = GA.scal(F(1, 2), GA.sub(GA.sc(1), GA.mul(GA.gen(0), GA.gen(p), sq)))
            g = sample_unit(n, sq)
            # invert g by solving g y = 1 on the blade basis
            blades = GA.all_blades(n)
            M = [[GA.mul(g, {b: F(1)}, sq).get(r, F(0)) for b in blades] for r in blades]
            y = GA.field_solve(M, [F(1) if r == () else F(0) for r in blades])
            ginv = {b: c for b, c in zip(blades, y) if c != 0}
            ok = ok and GA.mul(g, ginv, sq) == {(): F(1)}
            a = GA.mul(v, g, sq)
            idem = GA.mul(GA.mul(ginv, e, sq), g, sq)
            ok = ok and a != {} and GA.eq(GA.mul(idem, idem, sq), idem) and GA.mul(a, idem, sq) == {}
            ok = ok and idem != {} and not GA.eq(idem, GA.sc(1))
            # a = v g has a right annihilator of dimension 2^{n-1}, the image of the idempotent's right ideal
            rows = [GA.basis_vector_of(GA.mul(a, {b: F(1)}, sq), blades) for b in blades]
            ok = ok and GA.rank_of_vectors(rows) == 2 ** (n - 1)
            hits += 1
        if p >= 1:
            e = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.gen(0)))
            ok = ok and GA.mul(e, GA.sub(GA.sc(1), e), sq) == {}
        if (p - q) % 4 == 1:
            w = vol(n, sq)
            epsp = GA.scal(F(1, 2), GA.add(GA.sc(1), w))
            epsm = GA.scal(F(1, 2), GA.sub(GA.sc(1), w))
            x = sample_element(n)
            ok = ok and GA.mul(epsm, GA.mul(epsp, x, sq), sq) == {}
            ok = ok and all(GA.commutes(epsm, GA.gen(i), sq) for i in range(n))
            hits += 1
    _tp_rv = (ok and hits == 6); assert _tp_rv is not False, "check_trichotomy_exhaustive_on_samples"; return _tp_rv
