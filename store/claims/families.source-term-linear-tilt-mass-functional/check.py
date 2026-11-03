"""families.source-term-linear-tilt-mass-functional: exact checks of clause (1).

Clause (2) is a reading at observation level (the effective-potential assumption) and has no computable
content; it is not checked.
(1a) The expansion 2|b + (Lambda/6) Omega|^2 = 2|b|^2 + (2 Lambda/3) Re(conj(b) Omega) + (Lambda^2/18)|Omega|^2
     holds exactly over the Gaussian rationals; both sides are polynomials of degree 2 in Lambda, and they
     agree at 4 rational Lambda for every sample (b, Omega), so the identity holds for formal Lambda.
     The leading term of the join is 2|B_Lambda|^2 with B_Lambda = b + (Lambda/6) Omega (premise).
(1b) The Lambda-linear term L(b) = (Lambda/3)(conj(b) Omega + b conj(Omega)) is linear in b, and its
     conj(b)-coefficient (Wirtinger derivative at b = 0) is (Lambda/3) Omega: L(b) + i L(i b) = 2 c conj(b)
     with c = (Lambda/3) Omega, so the gradient in b is (2 Lambda/3) Omega, zero iff Lambda Omega = 0.
(1c) At fixed |b|, Re(conj(b) Omega) <= |b||Omega| (|b|^2|Omega|^2 - Re^2 = Im^2), with equality exactly for
     b a positive multiple of Omega: over 8 rational points b = 5u on the circle |b| = 5 (u rational unit),
     with Omega = 3 + 4i, the maximum of Re(conj(b) Omega) is 25 = |b||Omega|, attained only at u = Omega/5.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
BS = [QI(2, 1), QI(F(-1, 2), F(1, 3)), QI(0, -3), QI(F(5, 7), 2)]
OMS = [QI(1, -1), QI(3, 2), QI(F(-2, 5), F(1, 4))]
LAMS = [F(3), F(1, 7), F(-2), F(5, 3)]
UNITS = [QI(1, 0), QI(0, 1), QI(-1, 0), QI(0, -1), QI(F(3, 5), F(4, 5)), QI(F(4, 5), F(3, 5)),
         QI(F(-3, 5), F(4, 5)), QI(F(3, 5), F(-4, 5))]
OM_MAX = QI(3, 4)


def nsq(z):
    return (z * z.conj()).re


def check_source_expansion():
    premise("families.imported-dictionary-exact-join")
    ok = True
    for b in BS:
        for Om in OMS:
            for lam in LAMS:
                B = b + QI(lam / 6) * Om
                lhs = 2 * nsq(B)
                re_bOm = (b.conj() * Om).re
                rhs = 2 * nsq(b) + F(2, 3) * lam * re_bOm + lam * lam / 18 * nsq(Om)
                ok = ok and lhs == rhs
    _tp_rv = (ok); assert _tp_rv is not False, "check_source_expansion"; return _tp_rv


def check_wirtinger_gradient():
    premise("families.imported-dictionary-exact-join")
    ok = True
    for lam in LAMS:
        for Om in OMS:
            def lin(bb):
                B = bb + QI(lam / 6) * Om
                return QI(2) * B * B.conj() - QI(2) * bb * bb.conj() - QI(lam * lam / 18) * Om * Om.conj()
            for b in BS:
                two_c_bbar = lin(b) + QI(0, 1) * lin(QI(0, 1) * b)
                ok = ok and two_c_bbar == QI(2) * QI(lam / 3) * Om * b.conj()
                # linear in b: lin(2b) = 2 lin(b)
                ok = ok and lin(QI(2) * b) == QI(2) * lin(b)
            grad = QI(2 * lam / 3) * Om
            ok = ok and (grad == QI(0)) == (lam * nsq(Om) == 0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_wirtinger_gradient"; return _tp_rv


def check_phase_locking():
    ok = True
    best, arg = None, []
    for u in UNITS:
        b = QI(5) * u
        r = (b.conj() * OM_MAX).re
        im = (b.conj() * OM_MAX).im
        ok = ok and nsq(b) * nsq(OM_MAX) - r * r == im * im
        if best is None or r > best:
            best, arg = r, [u]
        elif r == best:
            arg.append(u)
    ok = ok and best == 25 and len(arg) == 1 and arg[0] == QI(F(3, 5), F(4, 5))
    _tp_rv = (ok); assert _tp_rv is not False, "check_phase_locking"; return _tp_rv
