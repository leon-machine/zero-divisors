"""interior.unipotency-across-kerr-family: exact checks in Gauge Theory Gravity on Cl(1,3).

P_k(a) = (a . k) k for null background vectors k: the ingoing e_t - e_r, the outgoing e_t + e_r and two generic
null directions e_t + n with n a rational unit 3-vector; the Kerr-Schild gauge field hb = 1 + H P_k.
(1) P_k^2 = 0 on the frame; (1 + s H P_k)(1 + s' H P_k) = 1 + (s + s') H P_k; hb^{-1} = 1 - H P_k
    (hb hb^{-1} = 1 on the frame), for several H.
(2) hb(a) . hb(b) = a . b + 2H (a.k)(b.k) and hb^{-1}(a) . hb^{-1}(b) = a . b - 2H (a.k)(b.k) for all frame pairs,
    so g = eta - 2H k (x) k (signature (+,-,-,-)); control: the opposite sign fails. At a = 0, H = M/r,
    k = e_t - e_r: the derived metric on (dt, dr) is dt^2 - dr^2 - 2H (dt + dr)^2, which in v = t + r is
    (1 - 2M/r) dv^2 - 2 dv dr (ingoing Eddington-Finkelstein), checked as an identity of quadratic forms at
    several (M, r).
(3) The null shear: k lies in both the kernel and the image of P_k (P_k shears along the direction it projects
    onto), while for the PG map P(a) = (a . e_t) e_r the image e_r is not null (Q(e_r) = -1) and P^2 = 0 too.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
E = [GA.gen(i) for i in range(4)]
NULLS = [GA.sub(E[0], E[1]), GA.add(E[0], E[1]),
         GA.add(E[0], GA.add(GA.scal(F(3, 5), E[1]), GA.scal(F(4, 5), E[2]))),
         GA.add(E[0], GA.add(GA.scal(F(2, 7), E[1]), GA.add(GA.scal(F(3, 7), E[2]), GA.scal(F(-6, 7), E[3]))))]
HS = [F(7, 5), F(-1, 2), F(9, 4)]
# Parameter pairs (s, s') for the one-parameter group law hb_{sH} hb_{s'H} = hb_{(s + s')H}.
GROUP_PAIRS = ((F(1), F(2)), (F(-3), F(1, 2)))
MR = [(F(1), F(3)), (F(2), F(5)), (F(1, 2), F(1, 3))]


def P(a, k):
    return GA.scal(GA.dot(a, k, S13), k)


def hb(a, H, k, s=1):
    return GA.add(a, GA.scal(s * H, P(a, k)))


def check_null_shear_is_unipotent():
    premise("interior.gauge-trajectory-unipotent-ray")
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    ok = True
    for k in NULLS:
        ok = ok and GA.dot(k, k, S13) == 0
        for a in E:
            ok = ok and GA.is_zero(P(P(a, k), k))
            for H in HS:
                ok = ok and GA.eq(hb(hb(a, H, k, -1), H, k), a)
                for s, s2 in GROUP_PAIRS:
                    lhs = hb(hb(a, H * s2, k), H * s, k)
                    ok = ok and GA.eq(lhs, hb(a, H * (s + s2), k))
    _tp_rv = (ok); assert _tp_rv is not False, "check_null_shear_is_unipotent"; return _tp_rv


def check_kerr_schild_metric():
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    ok = True
    for k in NULLS:
        for H in HS:
            for a in E:
                for b in E:
                    ab, ak, bk = GA.dot(a, b, S13), GA.dot(a, k, S13), GA.dot(b, k, S13)
                    ok = ok and GA.dot(hb(a, H, k), hb(b, H, k), S13) == ab + 2 * H * ak * bk
                    ok = ok and GA.dot(hb(a, H, k, -1), hb(b, H, k, -1), S13) == ab - 2 * H * ak * bk
            ok = ok and GA.dot(hb(E[0], H, k, -1), hb(E[0], H, k, -1), S13) != 1 + 2 * H * GA.dot(E[0], k, S13) ** 2
    kin = NULLS[0]
    for M, r in MR:
        H = M / r
        # displacement dt e_t + dr e_r: g = Q(hb^{-1}(dx)), a quadratic form in (dt, dr); v = t + r: dt = dv - dr
        for dt, dr in ((F(1), F(0)), (F(0), F(1)), (F(1), F(1)), (F(2), F(-3))):
            x = GA.add(GA.scal(dt, E[0]), GA.scal(dr, E[1]))
            g = GA.dot(hb(x, H, kin, -1), hb(x, H, kin, -1), S13)
            ok = ok and g == dt * dt - dr * dr - 2 * H * (dt + dr) ** 2
            dv = dt + dr
            ok = ok and g == (1 - 2 * M / r) * dv * dv - 2 * dv * dr
    _tp_rv = (ok); assert _tp_rv is not False, "check_kerr_schild_metric"; return _tp_rv


def check_kernel_and_image_along_k():
    premise("interior.gauge-trajectory-unipotent-ray")
    ok = True
    for k in NULLS:
        ok = ok and GA.is_zero(P(k, k))
        imgs = [P(a, k) for a in E]
        nonzero = [x for x in imgs if x]
        ok = ok and nonzero and all(GA.rank_of_vectors([[x.get((i,), F(0)) for i in range(4)],
                                                        [k.get((i,), F(0)) for i in range(4)]]) == 1 for x in nonzero)
    Ppg = lambda a: GA.scal(GA.dot(a, E[0], S13), E[1])
    ok = ok and all(GA.is_zero(Ppg(Ppg(a))) for a in E) and GA.dot(E[1], E[1], S13) == -1
    ok = ok and GA.dot(E[0], E[0], S13) == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_kernel_and_image_along_k"; return _tp_rv
