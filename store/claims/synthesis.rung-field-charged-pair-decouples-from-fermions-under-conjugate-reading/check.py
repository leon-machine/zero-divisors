"""Charged pair of the rung field: fermion couplings under the series' Yukawa readings, and the phase on alpha.

Coordinates as in the stored D-term check (synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus):
c = sum_a alpha_a v_a + beta_a w_a over the Gaussian rationals (slots a = 4, 5 stored as indices 0, 1),
N, m, Q, G, the slot-mixing generators T_j, Y; lift locus L: Q(c) = -H^2; lift family
c_lambda = (alpha, beta) = ((H^2/lambda, 0), (-lambda, 0)).
Yukawa readings (standard-model.one-vev-vector-relations-breaking-pattern, on the five-mode module of
standard-model.yukawa-pattern-two-rung-module): down-type and charged-lepton entries are those of M_c on
(Q, d^c), (L, e^c); up-type and Dirac-neutrino entries are those of M_{c*} on (Q, u^c), (L, nu^c), with
c* the conjugate-linear swap v_j <-> w_j.
(1) Both readings see only the beta half of c (the w-coefficients of c and the v-coefficients of c*):
    they vanish on every pure-alpha vector and are unchanged by any phase on alpha; the c reading of up-type
    entries, which the series does not use, would see alpha.
(2) The charged plane at c_lambda (computed as the G-orthogonal complement of the gauge orbit and of the
    neutral line in the tangent space of L) has beta-part (H^2/lambda^2) conj(a): normalised, its Yukawa
    coupling relative to the vev's is exactly (H^2/lambda^2)^2 in |.|^2, that is cot(beta)^2 of a
    two-doublet reading with tan(beta) = |beta|/|alpha| = lambda^2/H^2.
(3) The gauge vertex W h H+: the projection of T_j(dc/dlambda) onto the physical charged plane relative to its
    projection onto the eaten plane is (2 H^2 lambda^2/(lambda^4 - H^4))^2 in |.|^2 = 1/sinh^2(2 eta).
(4) A phase u on alpha alone keeps N, m, |Q|^2, sum_j mu_j^2, mu_Y, the Hermitian form G, commutes with every
    T_j and Y, and keeps both Yukawa readings; it moves Q to u Q, so it preserves L only when H = 0.
(5) At H = 0 the charged plane lies wholly in the alpha half.
(6) No tree vertex of a W with Z or photon and the charged pair (seagull coefficients vanish).
(7) Top decay: with stored masses the ratio Gamma(t -> b H+)/Gamma(t -> b W) is below cot(beta)^2, and
    2.32e-89 < g^2 H^2/(4 M_W^2) < cot(beta) < g^2 H^2/(2 M_W^2) < 4.66e-89 with H^2 = Lambda/3 (stored).
Every clause concerns the per-sector reading (not su(2)_R covariant), the leading mass reading of the
covariant completion with one family matrix on c and one on c* as wholes.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise, quantity

QI = GA.QI
I = GA.QI_I


def q(re, im=0):
    return QI(F(re), F(im))


# ---------- rung-summand coordinates (as in the stored D-term check) ----------
def absq(v):
    return sum((z.re * z.re + z.im * z.im for z in v), F(0))


def hdot(u, v):
    return sum((a.conj() * b for a, b in zip(u, v)), QI(0))


def Nn(c):
    return (absq(c[0]) + absq(c[1])) / 2


def G(c, d):
    return (hdot(c[0], d[0]) + hdot(c[1], d[1])).re / 2


def Q(c):
    return sum((a * b for a, b in zip(c[0], c[1])), QI(0))


def Qb(c, d):
    return (sum((a * b for a, b in zip(c[0], d[1])), QI(0))
            + sum((a * b for a, b in zip(d[0], c[1])), QI(0)))


def mm(c):
    return (absq(c[0]) - absq(c[1])) / 2


S1 = [[q(0), q(1)], [q(1), q(0)]]
S2 = [[q(0), q(0, -1)], [q(0, 1), q(0)]]
S3 = [[q(1), q(0)], [q(0), q(-1)]]
ONE2 = [[q(1), q(0)], [q(0), q(1)]]


def mv(M, v):
    return [M[i][0] * v[0] + M[i][1] * v[1] for i in range(2)]


def mconj(M):
    return [[M[i][j].conj() for j in range(2)] for i in range(2)]


def msc(s, M):
    return [[s * M[i][j] for j in range(2)] for i in range(2)]


def gen(sig):
    A = msc(I * F(1, 2), sig)
    return lambda c: (mv(A, c[0]), mv(mconj(A), c[1]))


T = [gen(S1), gen(S2), gen(S3)]
Y = gen(ONE2)


def herm(gn):
    return lambda c: ([z * (-I) for z in gn(c)[0]], [z * (-I) for z in gn(c)[1]])


HT = [herm(t) for t in T]
HY = herm(Y)


def mu(c):
    return [G(c, h(c)) for h in HT] + [G(c, HY(c))]


def cadd(c, d, s=F(1)):
    return ([a + s * b for a, b in zip(c[0], d[0])], [a + s * b for a, b in zip(c[1], d[1])])


def clam(lam, h2):
    return ([q(h2 / lam), q(0)], [q(-lam), q(0)])


def dclam(lam, h2):
    return ([q(-h2 / (lam * lam)), q(0)], [q(-1), q(0)])


def basis_vec(k):
    al = [q(0), q(0)]
    be = [q(0), q(0)]
    comp = k // 2
    val = q(1) if k % 2 == 0 else q(0, 1)
    if comp < 2:
        al[comp] = val
    else:
        be[comp - 2] = val
    return (al, be)


E8 = [basis_vec(k) for k in range(8)]


def nullspace(M, n):
    M = [row[:] for row in M]
    piv_cols = []
    r = 0
    for ccol in range(n):
        p = next((rr for rr in range(r, len(M)) if M[rr][ccol] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][ccol]
        M[r] = [v / pv for v in M[r]]
        for rr in range(len(M)):
            if rr != r and M[rr][ccol] != 0:
                f = M[rr][ccol]
                M[rr] = [a - f * b for a, b in zip(M[rr], M[r])]
        piv_cols.append(ccol)
        r += 1
    free = [cc for cc in range(n) if cc not in piv_cols]
    vecs = []
    for fcol in free:
        v = [F(0)] * n
        v[fcol] = F(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -M[i][fcol]
        vecs.append(v)
    return vecs


def combo(coeffs):
    d = ([q(0), q(0)], [q(0), q(0)])
    for k in range(8):
        d = cadd(d, E8[k], coeffs[k])
    return d


def physical_dirs(cs):
    """G-orthogonal complement of the gauge orbit inside the tangent space of L at cs (Q(cs) fixed)."""
    gauge = [t(cs) for t in T] + [Y(cs)]
    rows = []
    for k in range(8):
        qb = Qb(cs, E8[k])
        rows.append([qb.re, qb.im] + [G(gv, E8[k]) for gv in gauge])
    M = [[rows[k][r] for k in range(8)] for r in range(6)]
    return [combo(v) for v in nullspace(M, 8)]


def charged_plane(cs, d0):
    out = []
    for d in physical_dirs(cs):
        dd = cadd(d, d0, -G(d, d0) / G(d0, d0))
        if Nn(dd) != 0:
            out.append(dd)
    return out


def gram_schmidt(vs):
    out = []
    for v in vs:
        w = v
        for u in out:
            w = cadd(w, u, -G(w, u) / G(u, u))
        if G(w, w) != 0:
            out.append(w)
    return out


def proj_sq(w, basis):
    """|P w|^2 in the G metric onto span(basis) (basis G-orthogonal)."""
    return sum((G(w, u) ** 2 / G(u, u) for u in basis), F(0))


# ---------- five-mode module and the Yukawa readings (as in the stored one-vev check) ----------
NM = 5
STATES = [frozenset(cc) for r in range(NM + 1) for cc in combinations(range(1, NM + 1), r)]
FULL = frozenset(range(1, NM + 1))
EVEN = [S for S in STATES if len(S) % 2 == 0]
NAMES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}
DOWN = {("Q", "d^c"), ("L", "e^c")}
UP = {("Q", "u^c"), ("L", "nu^c")}


def act(op, st):
    out = {}
    for (kind, i), cf in op.items():
        for S, a in st.items():
            if kind == "v" and i not in S:
                Tt = S | {i}
            elif kind == "w" and i in S:
                Tt = S - {i}
            else:
                continue
            sign = -1 if sum(1 for j in S if j < i) % 2 else 1
            out[Tt] = QI(0) + out.get(Tt, QI(0)) + cf * a * sign
    return {k: v for k, v in out.items() if v != 0}


def perm_sign(seq):
    s = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def Bp(psi, phi):
    tot = QI(0)
    for S, a in psi.items():
        Sc = FULL - S
        if Sc in phi:
            k = len(S)
            tot = tot + a * phi[Sc] * ((-1) ** (k * (k - 1) // 2) * perm_sign(sorted(S) + sorted(Sc)))
    return tot


def jk(S):
    return len(S & {4, 5}), len(S & {1, 2, 3})


def entries(x):
    """{(species pair, S, T): entry} over the nonzero entries of M_x(psi, phi) = B(psi, x phi)."""
    out = {}
    for S in EVEN:
        for Tt in EVEN:
            val = Bp({S: QI(1)}, act(x, {Tt: QI(1)}))
            if val != 0:
                key = tuple(sorted((NAMES[jk(S)], NAMES[jk(Tt)])))
                out[(key, S, Tt)] = val
    return out


def tovec(c):
    """(alpha, beta) -> the vector sum alpha_a v_a + beta_a w_a of the ten (rungs 4, 5)."""
    x = {("v", 4): c[0][0], ("v", 5): c[0][1], ("w", 4): c[1][0], ("w", 5): c[1][1]}
    return {k: v for k, v in x.items() if v != 0}


def star(x):
    swap = {"v": "w", "w": "v"}
    return {(swap[k], j): (QI(0) + z).conj() for (k, j), z in x.items()}


def reading(c):
    """The series' Yukawa entries: down-type from M_c, up-type from M_{c*}."""
    dn = {k: v for k, v in entries(tovec(c)).items() if k[0] in DOWN}
    up = {k: v for k, v in entries(star(tovec(c))).items() if k[0] in UP}
    return dn, up


def weight(ent):
    """Sum of |entry|^2 over a set of entries."""
    return sum((v.re * v.re + v.im * v.im for v in ent.values()), F(0))


ALPHAS = [([q(1, 2), q(-3, 1)], [q(0), q(0)]), ([q(F(2, 3), -1), q(0, 5)], [q(0), q(0)])]
GENERIC = [([q(1, 2), q(-3, 1)], [q(2, -1), q(F(1, 2), 3)]),
           ([q(F(1, 3)), q(2, 2)], [q(0, 1), q(-1)]),
           ([q(5, -2), q(0)], [q(1, 1), q(4, -3)])]
PHASES = [q(F(3, 5), F(4, 5)), q(F(5, 13), F(-12, 13))]
FRAMES = [(F(1), F(3)), (F(1), F(7, 2)), (F(2), F(5)), (F(1, 4), F(9))]   # (H^2, lambda), lambda^2 > H^2


def alpha_phase(u):
    return lambda c: ([u * z for z in c[0]], list(c[1]))


def check_yukawa_readings_see_only_beta():
    """Down-type entries of M_c and up-type entries of M_{c*} vanish on pure-alpha vectors, are unchanged by a
    phase on alpha, and depend on beta (nonzero on generic vectors); the up-type entries of M_c itself (the
    c reading, not used) see alpha."""
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.imported-tower-commuting-copies-fock-module")
    for c in ALPHAS:
        dn, up = reading(c)
        GA.check("series readings vanish on pure alpha", dn == {} and up == {})
        c_up = {k: v for k, v in entries(tovec(c)).items() if k[0] in UP}
        GA.check("the c reading of up-type entries sees alpha", weight(c_up) != 0)
    for c in GENERIC:
        dn, up = reading(c)
        GA.check("readings nonzero on generic c", weight(dn) != 0 and weight(up) != 0)
        b2 = absq(c[1])
        # each down and up pair carries |beta_4|^2 + |beta_5|^2 summed over its isospin entries (x multiplicity)
        GA.check("down weight is a fixed multiple of |beta|^2", weight(dn) == 8 * b2)
        GA.check("up weight is the same multiple of |beta|^2", weight(up) == 8 * b2)
        for u in PHASES:
            dn2, up2 = reading(alpha_phase(u)(c))
            GA.check("phase on alpha leaves both readings", dn2 == dn and up2 == up)
    return True


def check_charged_pair_coupling_is_cot_beta():
    """At c_lambda the computed charged plane has beta-part (H^2/lambda^2) conj(a); the Yukawa weight of a
    normalised charged direction over that of the normalised vev direction is (H^2/lambda^2)^2 exactly."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-on-the-lift-locus")
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    for h2, lam in FRAMES:
        cs = clam(lam, h2)
        GA.check("on L", Q(cs) == q(-h2))
        ch = charged_plane(cs, dclam(lam, h2))
        GA.check("charged plane two-dimensional", len(ch) == 2)
        cotb = h2 / (lam * lam)
        for d in ch:
            a = d[0][1]
            GA.check("charged direction in slot 5", d[0][0] == 0 and d[1][0] == 0)
            GA.check("beta-part (H^2/lambda^2) conj(a)", d[1][1] == a.conj() * cotb)
            dn_d, up_d = reading(d)
            dn_v, up_v = reading(cs)
            r_dn = (weight(dn_d) / (2 * Nn(d))) / (weight(dn_v) / (2 * Nn(cs)))
            r_up = (weight(up_d) / (2 * Nn(d))) / (weight(up_v) / (2 * Nn(cs)))
            GA.check("down coupling ratio = cot(beta)^2", r_dn == cotb ** 2)
            GA.check("up coupling ratio = cot(beta)^2", r_up == cotb ** 2)
    return True


def check_w_h_charged_vertex():
    """T_j applied to the neutral mode dc/dlambda, split between the physical charged plane and the eaten plane
    (T_1 c, T_2 c): ratio of squared projections 4 H^4 lambda^4/(lambda^4 - H^4)^2 for j = 1, 2."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-on-the-lift-locus")
    for h2, lam in FRAMES:
        cs = clam(lam, h2)
        d0 = dclam(lam, h2)
        phys = gram_schmidt(charged_plane(cs, d0))
        eaten = gram_schmidt([T[0](cs), T[1](cs)])
        GA.check("planes G-orthogonal", all(G(u, w) == 0 for u in phys for w in eaten))
        l4, h4 = lam ** 4, h2 ** 2
        for j in (0, 1):
            w = T[j](d0)
            pp, pe = proj_sq(w, phys), proj_sq(w, eaten)
            GA.check("T_j(dc/dlambda) lies in the charged sector", pp + pe == G(w, w))
            GA.check("vertex ratio 1/sinh^2(2 eta)", pp * (l4 - h4) ** 2 == pe * 4 * h4 * l4)
    return True


def check_alpha_phase_breaks_only_the_lift_constraint():
    """A phase u on alpha alone keeps N, m, |Q|^2, sum mu_j^2, mu_Y and G, commutes with T_j and Y, and sends Q to
    u Q: it preserves L = {Q = -H^2} only for H = 0."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    for u in PHASES:
        U = alpha_phase(u)
        GA.check("u is a unit phase not equal to 1", u * u.conj() == q(1) and u != q(1))
        for c in GENERIC:
            Uc = U(c)
            GA.check("N kept", Nn(Uc) == Nn(c))
            GA.check("m kept", mm(Uc) == mm(c))
            GA.check("Q moved to uQ", Q(Uc) == u * Q(c) and Q(Uc) != Q(c))
            Qc = Q(c)
            GA.check("|Q|^2 kept", (Q(Uc) * Q(Uc).conj()) == Qc * Qc.conj())
            m0, m1 = mu(c), mu(Uc)
            GA.check("sum mu_j^2 kept", sum(x * x for x in m0[:3]) == sum(x * x for x in m1[:3]))
            GA.check("mu_Y kept", m0[3] == m1[3])
            for d in GENERIC:
                GA.check("G kept", G(U(c), U(d)) == G(c, d))
            for t in T + [Y]:
                GA.check("commutes with gauge generators", t(Uc) == U(t(c)))
        zero = ([q(0), q(0)], [q(-3), q(0)])
        GA.check("H = 0: L_0 kept", Q(U(cadd(zero, E8[2]))) == q(0) == Q(cadd(zero, E8[2])))
    return True


def check_charged_plane_alpha_only_at_zero_h():
    """At H = 0 (vacuum alpha = 0, beta = (-lambda, 0), on L_0 = {Q = 0}) the charged plane has no beta-part."""
    premise("synthesis.rung-field-on-the-lift-locus")
    for lam in (F(3), F(7, 2)):
        cs = clam(lam, F(0))
        ch = charged_plane(cs, dclam(lam, F(0)))
        GA.check("two charged directions", len(ch) == 2)
        GA.check("pure alpha", all(d[1] == [q(0), q(0)] and d[0][1] != 0 for d in ch))
    return True


PI_UP = F(22, 7)
PI_LO = F(333, 106)


def check_top_decay_branching_negligible():
    """Gamma(t -> b H+)/Gamma(t -> b W) = cot^2(beta) K with K = (1 - x)^2/((1 - y)^2 (1 + 2 y)), x = m_pm^2/m_t^2,
    y = M_W^2/m_t^2 (b mass neglected; formula cited from memory), K < 1 on the stored masses and the
    m_pm bracket; H^2/(2 N*) < cot(beta) = H^2/lambda^2 < H^2/N*, N* = 2 M_W^2/g^2, g^2 = 4 pi alpha/sin^2 theta_W,
    H^2 = Lambda (hbar c)^2/3 from the stored values: lower end in [2.32, 2.33] x 10^-89, upper end below
    4.66 x 10^-89. For the covariant branch (coupling of the top's mass-coupling size) the branching K/(1+K)
    lies in (0.24, 0.25)."""
    premise("synthesis.rung-field-charged-scalar-sum-rule")
    mt = quantity("quantity.top-quark-mass")
    mw = quantity("quantity.w-boson-mass")
    lam_cc = quantity("quantity.cosmological-constant")          # m^-2
    hbarc = quantity("quantity.reduced-planck-constant-times-c") / 10 ** 18  # MeV fm -> GeV m
    ainv = quantity("quantity.inverse-fine-structure-mz")
    s2w = quantity("quantity.weak-mixing-angle-mz")
    y = mw ** 2 / mt ** 2
    for mpm2, lo, hi in ((F(13702), F(331, 1000), F(332, 1000)), (F(13803), F(327, 1000), F(328, 1000))):
        x = mpm2 / mt ** 2
        K = (1 - x) ** 2 / ((1 - y) ** 2 * (1 + 2 * y))
        GA.check("K in the computed bracket, below 1/2", lo < K < hi < F(1, 2))
        GA.check("covariant branch, coupling of top size: branching K/(1+K) in (0.24, 0.25)",
                 F(24, 100) < K / (1 + K) < F(25, 100))
    g2_up = 4 * PI_UP / (ainv * s2w)
    H2 = lam_cc * hbarc ** 2 / 3
    cotb_up = g2_up * H2 / (2 * mw ** 2)
    GA.check("H^2 in [1.414, 1.415] x 10^-84 GeV^2", F(1414, 10 ** 87) < H2 < F(1415, 10 ** 87))
    GA.check("cot(beta) bound in [4.65, 4.66] x 10^-89", F(465, 10 ** 91) < cotb_up < F(466, 10 ** 91))
    GA.check("so cot(beta)^2 K < 10^-176", cotb_up ** 2 * F(1, 2) < F(1, 10 ** 176))
    g2_lo = 4 * PI_LO / (ainv * s2w)
    cotb_lo = g2_lo * H2 / (4 * mw ** 2)       # H^2/(2 N*) < H^2/lambda^2 since lambda^2 < 2 N*
    GA.check("lower end H^2/(2N*) in [2.32, 2.33] x 10^-89", F(232, 10 ** 91) < cotb_lo < F(233, 10 ** 91))
    GA.check("lower end below the upper end", cotb_lo < cotb_up)
    return True


W_GENS = (0, 1)     # T_1, T_2: the charged generators
Z_GEN = 2           # T_3


def check_no_tree_vertex_with_w_and_a_neutral_gauge_field():
    """The seagull coefficient G(T_j c, T d) + G(T c, T_j d) of W_j (j = 1, 2), a neutral generator T in {T_3, Y}
    and a charged direction d vanishes at c_lambda: no tree vertex W Z H or W gamma H. The generators are pinned:
    T_1 c, T_2 c span a plane G-orthogonal to Y c, and T_3 c = Y c. The same coefficient with d the neutral
    mode and T = T_j is G(T_j c, T_j dc/dlambda) = (lambda^4 - H^4)/(8 lambda^3), nonzero (the W W h vertex)."""
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    premise("synthesis.rung-field-on-the-lift-locus")
    for h2, lam in FRAMES:
        cs = clam(lam, h2)
        d0 = dclam(lam, h2)
        wv = [T[j](cs) for j in W_GENS]
        GA.check("T_1 c, T_2 c are G-orthogonal to Y c and span a plane",
                 all(G(w, Y(cs)) == 0 for w in wv) and len(gram_schmidt(wv)) == len(W_GENS))
        zc = T[Z_GEN](cs)
        dch = charged_plane(cs, d0)
        GA.check("T_3 c = Y c (Y - T_3 unbroken), G-orthogonal to T_1 c, T_2 c; T_3 differs from Y on the charged plane",
                 zc == Y(cs) and all(G(zc, w) == 0 for w in wv) and all(T[Z_GEN](d) != Y(d) for d in dch))
        for d in dch:
            for j in W_GENS:
                for Tn in (T[Z_GEN], Y):
                    GA.check("no W-neutral-charged seagull", G(T[j](cs), Tn(d)) + G(Tn(cs), T[j](d)) == 0)
        for j in W_GENS:
            GA.check("W W h seagull (lambda^4 - H^4)/(8 lambda^3)",
                     G(T[j](cs), T[j](d0)) * 8 * lam ** 3 == lam ** 4 - h2 ** 2)
    return True
