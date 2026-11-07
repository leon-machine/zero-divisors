# Screening (exact, Fractions): continuation of massless modes through a radical-normal wall in its smooth coordinate t.
# tau = 2 sqrt(t) (physical side t>0), tau_E = 2 sqrt(-t) (Riemannian far side t<0).
# Even-in-tau part: cos(k tau) = sum_n (-1)^n k^(2n) 4^n t^n/(2n)!  -> analytic in t.
# At t = -s: sum_n k^(2n) 4^n s^n/(2n)! = cosh(k tau_E).  Check coefficientwise.
# Odd part: sin(k tau) = 2 sqrt(t) * sum_n (-1)^n k^(2n+1) 4^n t^n/(2n+1)!  ; sqrt(t) -> +- i sqrt(s): sinh(k tau_E) up to the factor -+i.
from fractions import Fraction as Fr
from math import factorial
import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
import GA  # house rule: import GA (not otherwise needed here)
k=Fr(3,2); N=12
for n in range(N):
    c_cos_t = Fr((-1)**n)*k**(2*n)*4**n/factorial(2*n)          # coefficient of t^n
    c_at_minus_s = c_cos_t*(-1)**n                               # coefficient of s^n after t=-s
    c_cosh = k**(2*n)*4**n/factorial(2*n)                        # cosh(2k sqrt s) coefficient
    assert c_at_minus_s == c_cosh
    c_sin = Fr((-1)**n)*k**(2*n+1)*4**n/factorial(2*n+1)        # sin(k tau)/(2 sqrt t)
    c_sinh = k**(2*n+1)*4**n/factorial(2*n+1)                    # sinh(k tau_E)/(2 sqrt s)
    assert c_sin*(-1)**n == c_sinh
print("even part -> cosh(k tau_E); odd part -> (+-i) sinh(k tau_E): exact through order", N)
# Decaying far-side mode e^{-k tau_E} = cosh - sinh  <->  cos(k tau) -+ i^{-1}... = e^{-+ i k tau}: branch of sqrt(t) = sign of i.
# Entropy screen for the stored tail n(p)=(1+p)^{-6}: s(n) <= n(1 - ln n) <= n(1+6p) , so p^2 s(n) <= (1+6p)p^2(1+p)^{-6}: integrable;
# third moment p^3 * p^2 n ~ p^{-1}: log-divergent.  Exact rational check of the integrable majorant's antiderivative limit omitted; argued.
