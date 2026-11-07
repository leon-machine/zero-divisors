"""Frequency sign relative to I4 against the chirality of massless even spinors: exact checks.

Conventions of the store: Cl(1,3), g0^2 = +1, g1^2 = g2^2 = g3^2 = -1, I4 = g0 g1 g2 g3, spinors are even
multivectors, the field theory's unit is I4 (central in the even algebra, so L_I4 = R_I4 on spinors),
I sigma3 = I4 g3 g0 = g2 g1. For a future null k = w (g0 + n), n spatial with Q(n) = -1, B_k = g0 n (for
k = g0 + g1 this is the stored wedge boost B = g0 g1) and D_k = I4 B_k (the stored identity I4 B = D = g2 g3).
S_k = {psi even : k psi = 0}; a mode is exp(-s I4 k.x) psi0 with psi0 in S_k and s = +1 or -1.
Gamma(psi) = I4 psi I sigma3 is the chirality; the store's projectors chi_e (field-theory.fock-space-maxwell-
modes) project onto Gamma = -e.

(i)  On S_k: dim 4, L_{B_k} = -1, L_{D_k} = -L_I4; the right-handed rotor about n, cos - sin I sigma_n with
     I sigma_n = -D_k, acts as cos - sin I4 (helicity +1/2 along n relative to I4); a Lorentz rotor R carries
     S_k onto S_{R k R~}. Samples: k = g0 + g1 and its images under rational rotors (rotations and a boost).
(ii) Gamma^2 = 1, L_I4 = -Gamma R_{I sigma3} on all of Cl+(1,3), Gamma commutes with the left bivector action,
     preserves S_k with 2-dimensional eigenspaces there, and Gamma = -e on the store's chi_e.
(iii) The real-linear maps of Cl+(1,3) commuting with left multiplication by the six bivectors form an
     8-dimensional space containing the 8 right multiplications by even blades, and every one commutes with L_I4.
(iv) For psi(x) -> a psi(Lambda^{-1} x) b, a, b blades of the same parity, Lambda in {1, P, T, PT}: the
     massless equation is preserved on the samples exactly for a in {1, I4} (Lambda = 1, PT) and a in
     {g0, g0 I4} (Lambda = P, T); for those, s' = s (-1)^{|a|} sgn(g0 . Lambda k), flipped exactly for P and PT;
     Gamma' = Gamma (-1)^{|a|} c(b), c(b) = +1 or -1 as b commutes or anticommutes with I sigma3; Hestenes
     C (b = sigma1) flips Gamma and not s, a CP map (a = g0, b = g0 sigma1) flips s and not Gamma.
Exact arithmetic only.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
G = [GA.gen(i) for i in range(4)]
BL = GA.all_blades(4)
EVEN = [b for b in BL if len(b) % 2 == 0]


def _m(*xs):
    r = GA.sc(1)
    for x in xs:
        r = GA.mul(r, x, SQ)
    return r


I4 = _m(*G)
ISIG3 = _m(I4, G[3], G[0])
SIG1 = _m(G[1], G[0])


def _bl(b):
    return {tuple(b): F(1)}


def _vec(x):
    return [x.get(b, F(0)) for b in EVEN]


def _unvec(v):
    return {b: c for b, c in zip(EVEN, v) if c != 0}


def _L(a):
    return lambda x: GA.mul(a, x, SQ)


def _R(b):
    return lambda x: GA.mul(x, b, SQ)


def _gamma(x):
    return GA.mul(GA.mul(I4, x, SQ), ISIG3, SQ)


def _mat(f):
    cols = [_vec(f(_bl(b))) for b in EVEN]
    return [[cols[j][i] for j in range(len(EVEN))] for i in range(len(EVEN))]


def _ident():
    n = len(EVEN)
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def _null_kernel(k):
    """Basis of S_k: even psi with k psi = 0 (k psi is odd, all coordinates kept)."""
    cols = [[GA.mul(k, _bl(b), SQ).get(c, F(0)) for c in BL] for b in EVEN]
    M = [[cols[j][i] for j in range(len(EVEN))] for i in range(len(BL))]
    return [_unvec(v) for v in GA.field_kernel(M)]


def _cayley(biv, t):
    return GA.add(GA.sc(1), GA.scal(t, biv))


def _sandwich(R, x):
    nrm = GA.mul(R, GA.reverse(R), SQ).get((), F(0))
    return GA.scal(F(1) / nrm, _m(R, x, GA.reverse(R)))


K0 = GA.add(G[0], G[1])
ROTORS = [_cayley(_m(G[1], G[3]), F(1, 2)), _cayley(_m(G[1], G[2]), F(2, 3)),
          _cayley(_m(G[2], G[3]), F(3, 5)), _cayley(_m(G[0], G[1]), F(1, 3))]
KS = [K0] + [_sandwich(R, K0) for R in ROTORS[:3]]
BOOSTED = _sandwich(ROTORS[3], K0)


def _time(k):
    return k.get((0,), F(0))


def _bk(k):
    n = GA.scal(F(1) / _time(k), {b: c for b, c in k.items() if b != (0,)})
    return _m(G[0], n)


def _modes(k):
    """Gamma eigenvectors in S_k, one per eigenvalue."""
    out = {}
    for psi in _null_kernel(k):
        for gm in (1, -1):
            p = GA.scal(F(1, 2), GA.add(psi, GA.scal(F(gm), _gamma(psi))))
            if not GA.is_zero(p) and gm not in out:
                out[gm] = p
    return out


def check_null_kernel_locks_helicity_to_the_frequency_sign():
    premise("field-theory.fock-space-maxwell-modes")
    ok_dim = ok_b = ok_d = ok_rot = ok_cov = True
    c, s = F(4, 5), F(3, 5)
    for k in KS + [BOOSTED]:
        Sk = _null_kernel(k)
        Bk = _bk(k)
        Dk = _m(I4, Bk)
        isn = GA.neg(Dk)
        ok_dim = ok_dim and len(Sk) == 4
        for psi in Sk:
            ok_b = ok_b and GA.eq(_m(Bk, psi), GA.neg(psi))
            ok_d = ok_d and GA.eq(_m(Dk, psi), GA.neg(_m(I4, psi)))
            rot = GA.sub(GA.sc(c), GA.scal(s, isn))
            ok_rot = ok_rot and GA.eq(_m(rot, psi), GA.sub(GA.scal(c, psi), GA.scal(s, _m(I4, psi))))
            for R in ROTORS:
                ok_cov = ok_cov and GA.is_zero(_m(_sandwich(R, k), R, psi))
    GA.check("(i) dim S_k = 4 on every sample", ok_dim)
    GA.check("(i) L_{B_k} = -1 on S_k", ok_b)
    GA.check("(i) L_{D_k} = -L_I4 on S_k, D_k = I4 B_k", ok_d)
    GA.check("(i) right-handed rotor about n acts as cos - sin I4: helicity +1/2 along n", ok_rot)
    GA.check("(i) a rotor R carries S_k into S_{R k R~}", ok_cov)
    GA.check("(i) stored identity: I4 g0 g1 = g2 g3", GA.eq(_m(I4, G[0], G[1]), _m(G[2], G[3])))
    GA.check("(i) B_k of g0 + g1 is g0 g1", GA.eq(_bk(K0), _m(G[0], G[1])))
    GA.check("(i) Q(I sigma_n) = -1 for k = g0 + g1", GA.eq(_m(_m(G[3], G[2]), _m(G[3], G[2])), GA.sc(-1)))
    # the rotor cos + sin D_k (half angle 4/5, 3/5) turns g2 towards g3 about n = g1: right-handed for
    # the spatial orientation I3 = g1 g2 g3 = g0 I4 (cos = 7/25, sin = 24/25)
    rot = GA.add(GA.sc(c), GA.scal(s, _m(G[2], G[3])))
    img = _sandwich(rot, G[2])
    GA.check("(i) the rotor is right-handed about g1 for I3 = g0 I4",
             GA.eq(img, GA.add(GA.scal(F(7, 25), G[2]), GA.scal(F(24, 25), G[3])))
             and GA.eq(_m(G[1], G[2], G[3]), _m(G[0], I4)))


def check_the_unit_is_minus_chirality_times_the_charge_rotation():
    premise("field-theory.fock-space-maxwell-modes")
    Gm = _mat(_gamma)
    LI = _mat(_L(I4))
    RH = _mat(_R(ISIG3))
    GA.check("(ii) Gamma^2 = 1", GA.mat_eq(GA.mat_mul(Gm, Gm), _ident()))
    GA.check("(ii) L_I4 = -Gamma R_{I sigma3}",
             GA.mat_eq(LI, [[-x for x in r] for r in GA.mat_mul(Gm, RH)]))
    GA.check("(ii) L_I4 = R_I4 on even spinors", GA.mat_eq(LI, _mat(_R(I4))))
    ok = all(GA.mat_eq(GA.mat_mul(Gm, _mat(_L(_m(G[i], G[j])))), GA.mat_mul(_mat(_L(_m(G[i], G[j]))), Gm))
             for i in range(4) for j in range(i + 1, 4))
    GA.check("(ii) Gamma commutes with left multiplication by every bivector", ok)
    ok_pres, dims = True, set()
    for k in KS:
        Sk = _null_kernel(k)
        ok_pres = ok_pres and all(GA.is_zero(_m(k, _gamma(p))) for p in Sk)
        for gm in (1, -1):
            imgs = [_vec(GA.scal(F(1, 2), GA.add(p, GA.scal(F(gm), _gamma(p))))) for p in Sk]
            dims.add(GA.rank_of_vectors(imgs))
    GA.check("(ii) Gamma preserves S_k", ok_pres)
    GA.check("(ii) both Gamma eigenspaces in S_k are 2-dimensional", dims == {2})
    # the store's chirality projector, as the premise's check builds it with its own literal
    # IS3 = {(1, 2): -1} (I sigma3 = g2 g1): chi_e(p) = (p - e I4 p IS3)/2 lands on Gamma = -e
    is3_store = {(1, 2): F(-1)}
    GA.check("(ii) the local I sigma3 = I4 g3 g0 is the premise's IS3 = g2 g1", GA.eq(ISIG3, is3_store))
    ok_chi = True
    for e in (1, -1):
        for b in EVEN:
            ch = GA.scal(F(1, 2), GA.sub(_bl(b), GA.scal(F(e), _m(I4, _bl(b), is3_store))))
            ok_chi = ok_chi and GA.eq(_gamma(ch), GA.scal(F(-e), ch))
    GA.check("(ii) the store's chi_e projects onto Gamma = -e", ok_chi)
    # s = -Gamma s_H: on a chirality-gamma vector of S_k, psi I4 = -gamma psi I sigma3
    ok_sh = True
    for k in KS:
        for gm, psi in _modes(k).items():
            ok_sh = ok_sh and GA.eq(_m(I4, psi), GA.scal(F(-gm), _m(psi, ISIG3)))
    GA.check("(ii) L_I4 = -gamma R_{I sigma3} on chirality-gamma modes (s = -gamma s_H)", ok_sh)


def check_lorentz_covariant_maps_are_right_multiplications():
    gens = [_mat(_L(_m(G[i], G[j]))) for i in range(4) for j in range(i + 1, 4)]
    n = len(EVEN)
    rows = []
    for Gq in gens:
        for i in range(n):
            for j in range(n):
                row = [F(0)] * (n * n)
                for l in range(n):
                    row[i * n + l] += Gq[l][j]
                    row[l * n + j] -= Gq[i][l]
                rows.append(row)
    comm = GA.field_kernel(rows)
    GA.check("(iii) the commutant of the left Lorentz action has dimension 8", len(comm) == 8)
    rights = [sum(_mat(_R(_bl(b))), []) for b in EVEN]
    GA.check("(iii) the 8 right multiplications by even blades are independent",
             GA.rank_of_vectors(rights) == 8)
    GA.check("(iii) they lie in the commutant (rank does not grow)",
             GA.rank_of_vectors(rights + comm) == 8)
    LI = _mat(_L(I4))
    ok = True
    for v in comm:
        T = [v[i * n:(i + 1) * n] for i in range(n)]
        ok = ok and GA.mat_eq(GA.mat_mul(T, LI), GA.mat_mul(LI, T))
    GA.check("(iii) every Lorentz-covariant real-linear map commutes with L_I4", ok)


def _lam(name, x):
    if name == "id":
        return x
    if name == "P":
        return _m(G[0], x, G[0])
    if name == "T":
        return GA.neg(_m(G[0], x, G[0]))
    return GA.neg(x)


def _image(name, a, b, k, s, psi0):
    """(k', s', psi0') with k' future for a exp(-s I4 (Lambda k).x) psi0 b."""
    kp = _lam(name, k)
    sp = s * (-1 if len(next(iter(a))) % 2 else 1)
    psi = _m(a, psi0, b)
    if _time(kp) < 0:
        kp, sp = GA.neg(kp), -sp
    return kp, sp, psi


def _gamma_sign(psi):
    g = _gamma(psi)
    return 1 if GA.eq(g, psi) else (-1 if GA.eq(g, GA.neg(psi)) else 0)


def check_discrete_maps_flip_frequency_sign_and_chirality_independently():
    premise("field-theory.fock-space-maxwell-modes")
    allowed = {"id": {(), (0, 1, 2, 3)}, "PT": {(), (0, 1, 2, 3)},
               "P": {(0,), (1, 2, 3)}, "T": {(0,), (1, 2, 3)}}
    sflip = {"id": 1, "P": -1, "T": 1, "PT": -1}
    modes = {id(k): _modes(k) for k in KS}
    ok_allowed = ok_s = ok_g = True
    counted = 0
    for name in ("id", "P", "T", "PT"):
        for ab in BL:
            a = _bl(ab)
            pres = all(GA.is_zero(_m(_lam(name, k), a, psi)) for k in KS for psi in _null_kernel(k))
            ok_allowed = ok_allowed and (pres == (ab in allowed[name]))
            if not pres:
                continue
            for bb in BL:
                if (len(ab) + len(bb)) % 2:
                    continue
                b = _bl(bb)
                cb = 1 if GA.commutes(b, ISIG3, SQ) else -1
                counted += 1
                for k in KS:
                    for gm, psi0 in modes[id(k)].items():
                        for s in (1, -1):
                            kp, sp, psi = _image(name, a, b, k, s, psi0)
                            ok_s = ok_s and GA.is_zero(_m(kp, psi)) and sp == s * sflip[name]
                            ok_g = ok_g and _gamma_sign(psi) == gm * (-1) ** len(ab) * cb
    GA.check("(iv) the equation is kept exactly for a in {1, I4} (1, PT) and {g0, g0 I4} (P, T)", ok_allowed)
    GA.check("(iv) 16 maps (a, b) per Lambda, 64 in all", counted == 64)
    GA.check("(iv) s' = s (-1)^{|a|} sgn(g0 . Lambda k): flipped exactly for P and PT", ok_s)
    GA.check("(iv) Gamma' = Gamma (-1)^{|a|} c(b)", ok_g)
    # Hestenes C: psi -> psi sigma1 (Lambda = 1); CP: psi -> g0 psi(Px) g0 sigma1
    k = KS[1]
    for gm, psi0 in modes[id(k)].items():
        kp, sp, psi = _image("id", GA.sc(1), SIG1, k, 1, psi0)
        GA.check("(iv) Hestenes C keeps s and flips Gamma", sp == 1 and _gamma_sign(psi) == -gm)
        kp, sp, psi = _image("P", G[0], _m(G[0], SIG1), k, 1, psi0)
        GA.check("(iv) CP flips s and keeps Gamma", sp == -1 and _gamma_sign(psi) == gm)
