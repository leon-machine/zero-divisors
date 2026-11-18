"""Closed forms of the even-parity first-order Ricci vectors (Regge-Wheeler gauge), written so that they
evaluate on gtg.Jet (derivatives .d(0) = d/dt, .d(1) = d/dr) and on sym.LF alike."""
from fractions import Fraction as F


def even_parts(H0, H1, H2, K, r, f, M):
    """The pieces of the components: with DP = P'' + cot P',
       gamma_0 . R1(gamma_0)-component = P c00 + DP d00, gamma_0-component of R1(gamma_1) = P c01 + DP d01,
       gamma_0-component of R1(gamma_2) = -P' c02 / (2 r sqrt f), gamma_1-component of R1(gamma_2) =
       P' c12 / (2 r sqrt f), gamma_1-component of R1(gamma_1) = P c11 + DP d11,
       gamma_2 (gamma_3) components of R1(gamma_2) (R1(gamma_3)) = P c22 + DP dK + P'' cHH (cot P' cHH)."""
    r2 = r * r
    t, x = 0, 1
    c00 = (f / 2 * H0.d(x).d(x) + (2 * r - M) / (2 * r2) * H0.d(x) - H1.d(t).d(x)
           - (2 * r - 3 * M) / (r2 * f) * H1.d(t) + M / (2 * r2) * H2.d(x) + H2.d(t).d(t) / (2 * f)
           - M / r2 * K.d(x) + K.d(t).d(t) / f)
    d00 = H0 / (2 * r2)
    c01 = K.d(t).d(x) + (r - 3 * M) / (r2 * f) * K.d(t) - H2.d(t) / r
    d01 = H1 / (2 * r2)
    c02 = (f * H1).d(x) - H2.d(t) - K.d(t)
    c12 = f * (H0.d(x) - K.d(x)) - H1.d(t) - (r - 3 * M) / r2 * H0 + (r - M) / r2 * H2
    c11 = (f / 2 * H0.d(x).d(x) + 3 * M / (2 * r2) * H0.d(x) - H1.d(t).d(x) - M / (r2 * f) * H1.d(t)
           + (2 * r - 3 * M) / (2 * r2) * H2.d(x) + H2.d(t).d(t) / (2 * f)
           - (2 * r - 3 * M) / r2 * K.d(x) - f * K.d(x).d(x))
    d11 = -H2 / (2 * r2)
    c22 = (f / (2 * r) * (H0.d(x) + H2.d(x)) - H1.d(t) / r + (H2 - K) / r2
           - (2 * r - 3 * M) / r2 * K.d(x) - f / 2 * K.d(x).d(x) + K.d(t).d(t) / (2 * f))
    dK = -K / (2 * r2)
    cHH = (H0 - H2) / (2 * r2)
    return dict(c00=c00, d00=d00, c01=c01, d01=d01, c02=c02, c12=c12, c11=c11, d11=d11, c22=c22, dK=dK, cHH=cHH)
