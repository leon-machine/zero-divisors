"""Referee G: a pair mode IS a Gupta-Bleuler timelike mode for a Krein form <x, eta y> built on the tower's
positive form (eta = (-1)^{n_2}, the construction (KF) itself uses: eta = (-1)^{n_0} on its polynomials).
X = a_1* a_2, Omega = |n_1 = 1, n_2 = 0>: X Omega = 0, and with the Krein adjoint X^dag = eta X* eta,
[X, X^dag] Omega = -Omega and <X^dag Omega, eta X^dag Omega> = -1."""
import sys; sys.path.insert(0, sys.path[0])
from fock import *
fk = Fock([1, 2])
Om = {frozenset([1]): ONE}
def eta(st): return {k: (v if 2 not in k else (-v[0], -v[1])) for k, v in st.items()}
X = Bilinear(fk, [(ONE, 1, 2)]); Xs = X.adj()
Xdag = lambda st: eta(Xs(eta(st)))
print('X Omega = 0:', X(Om) == {})
c = sadd(X(Xdag(Om)), sneg(Xdag(X(Om))))
print('[X, X^dag] Omega =', c, ' equals -Omega:', c == sneg(Om))
v = Xdag(Om)
print('Krein norm of X^dag Omega:', inner(v, eta(v)), '  positive norm:', norm2(v))
