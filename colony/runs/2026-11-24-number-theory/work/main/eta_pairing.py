# C2 (kill test).  Classical formula, cited from memory (Atiyah-Patodi-Singer; Donnelly; Gilkey): on S^(2n+1)/Z_4
# with the generator acting by the quarter turn J on each coordinate plane, the spin^c Dirac (Dolbeault)
# operator twisted by a virtual flat bundle rho of dimension 0 and a twist theta of dimension 0 has reduced
# spectral asymmetry   ind(rho, theta) = (1/4) sum_{g != 1} Tr rho(g) Tr theta(g) / (1 - conj(lam_g))^(n+1)  mod Z,
# lam_g the eigenvalue of g.  Gilkey: [V_rho] = 0 in K~ iff ind(rho, theta) = 0 mod Z for all theta in R_0.
# Exact Gaussian-rational arithmetic (GA.QI).
import sys
sys.path.insert(0, "/home/claude/leon-machine/zero-divisors/lib")
from fractions import Fraction as F
import GA
QI = GA.QI
I = GA.QI_I
one = GA.qi(1, 0)
def powi(z, k):
    out = one
    for _ in range(k % 4):
        out = out * z
    return out
def ind(n, rho, theta):
    """rho, theta: dicts exponent -> integer multiplicity (virtual characters of Z_4)."""
    tot = GA.qi(0, 0)
    for j in (1, 2, 3):
        lam = powi(I, j)
        tr_rho = sum((powi(lam, e) * GA.qi(c, 0) for e, c in rho.items()), GA.qi(0, 0))
        tr_th = sum((powi(lam, e) * GA.qi(c, 0) for e, c in theta.items()), GA.qi(0, 0))
        den = one
        for _ in range(n + 1):
            den = den * (one - lam.conj())
        tot = tot + tr_rho * tr_th / den
    return tot / GA.qi(4, 0)
for n in range(1, 9):
    out = []
    for m in range(0, 6):
        rho = {2: 2 ** m, 0: -(2 ** m)}            # 2^m (chi^2 - 1)
        vals = [ind(n, rho, {b: 1, 0: -1}) for b in (1, 2, 3)]
        integral = all(v.im == 0 and v.re.denominator == 1 for v in vals)
        out.append(integral)
    first = out.index(True)
    print("n =", n, " least m with all pairings of 2^m (chi^2 - 1) integral:", first, " ceil(n/2) =", -(-n // 2))
