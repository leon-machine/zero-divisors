"""Lead 3 (Kerr ring), exact tests of kill condition K3. Run: python3 kerr_ring.py  (needs lib/ on the path).

Tests, at rational points of both sheets:
 (a) z = r - I a cos(theta), w = z^2 = x^2 + y^2 + (Z - I a)^2;
 (b) the plane family G_w(v, v) = Re(w~ v^2), matrix [[Re w, Im w], [Im w, -Re w]] (the stored example
     [[x, y], [y, -x]] in the normal coordinate w): z spans its positive eigenline, value Q(z); I z the negative one;
 (c) H = M r^3/(r^4 + a^2 Z^2) = M <1, z>/Q(z): linear in the unit eigenvector, odd under the deck map z -> -z;
     H^2 = M^2 (1 + Re w/|w|)/(2|w|) = M^2 <1, P_+ 1>/|w| is a function of w;
 (d) the scale -M z^-3 is odd under the deck map (homogeneous of odd degree in z); -M z^-2 would be even;
 (e) the Kerr-Schild cometric eta^-1 + 2 H k k has the determinant and signature of eta^-1 wherever H is finite:
     it does not degenerate, so the stored completion statements have no degeneration set to apply to.
"""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..', 'lib'))
import GA
QI = GA.QI

M = F(7, 3)
# (a, r, cos, sin): r^2 + a^2 a rational square, (cos, sin) a rational point; both signs of r (both sheets)
POINTS = [(F(4), F(3), F(3, 5), F(4, 5)), (F(3), F(4), F(5, 13), F(12, 13)), (F(4), F(-3), F(-3, 5), F(4, 5)),
          (F(5), F(12), F(-4, 5), F(3, 5)), (F(8), F(6), F(7, 25), F(24, 25)), (F(3), F(-4), F(-5, 13), F(12, 13)),
          (F(4), F(3, 1), F(0), F(1)), (F(3, 2), F(2), F(8, 17), F(15, 17))]
AZIMUTHS = [(F(1), F(0)), (F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13))]
ROOTS = {(F(4), F(3)): F(5), (F(3), F(4)): F(5), (F(4), F(-3)): F(5), (F(5), F(12)): F(13), (F(8), F(6)): F(10),
         (F(3), F(-4)): F(5), (F(3, 2), F(2)): F(5, 2)}
ok = True
for (a, r, c, s) in POINTS:
    root = ROOTS[(a, r)]
    assert root * root == r * r + a * a
    z = QI(r, -a * c)
    w = z * z
    Z = r * c
    rho2 = (r * r + a * a) * s * s                      # x^2 + y^2
    ok &= (w == QI(rho2 + Z * Z - a * a, -2 * a * Z))    # (a)
    qz = r * r + a * a * c * c                           # Q(z) = |w|
    ok &= (qz * qz == w.re * w.re + w.im * w.im)
    g = [[w.re, w.im], [w.im, -w.re]]
    ok &= (GA.mat_mul(g, [[z.re], [z.im]]) == [[qz * z.re], [qz * z.im]])          # (b) positive eigenline
    ok &= (GA.mat_mul(g, [[-z.im], [z.re]]) == [[qz * z.im], [-qz * z.re]])        # negative eigenline
    H = M * r ** 3 / (r ** 4 + a * a * Z * Z) if r != 0 else F(0)
    ok &= (H == M * z.re / qz) and (H == (QI(M) / z).re)                           # (c)
    ok &= (H * H == M * M * (1 + w.re / qz) / (2 * qz))
    zm = QI(-r, a * c)                                    # deck map (r, theta) -> (-r, pi - theta)
    ok &= (zm * zm == w) and ((QI(M) / zm).re == -H)
    scale = QI(-M) / (z * z * z)
    ok &= (QI(-M) / (zm * zm * zm) == QI(0) - scale) and (QI(-M) / (zm * zm) == QI(-M) / (z * z))   # (d)
    for (cp, sp) in AZIMUTHS:
        x, y = root * s * cp, root * s * sp
        ok &= (x * x + y * y == rho2)
        if r == 0:
            continue
        k = [F(1), (r * x + a * y) / (r * r + a * a), (r * y - a * x) / (r * r + a * a), Z / r]
        eta = [[(F(1) if i == 0 else F(-1)) if i == j else F(0) for j in range(4)] for i in range(4)]
        kk = k[0] * k[0] - k[1] * k[1] - k[2] * k[2] - k[3] * k[3]
        ok &= (kk == 0)
        # cometric eta^-1 + 2 H k^# k^#, k^# = eta^-1 k; eta^-1 = eta in this frame
        ks = [k[0], -k[1], -k[2], -k[3]]
        com = [[eta[i][j] + 2 * H * ks[i] * ks[j] for j in range(4)] for i in range(4)]
        ok &= (GA.congruence_signature(com) == (1, 3, 0))                               # (e)
        for big in (F(10 ** 6), F(-10 ** 6)):                                           # any finite coefficient
            com = [[eta[i][j] + 2 * big * ks[i] * ks[j] for j in range(4)] for i in range(4)]
            ok &= (GA.congruence_signature(com) == (1, 3, 0))
print("kerr ring identities (a)-(e):", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
