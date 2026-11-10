"""Referee R2, own route (symbolic, sympy installed outside the repository).
Start from the Boyer-Lindquist Kerr line element (independent of the proposals' entered components), transform to the
Kerr-Schild chart, and recompute what the two proposals use."""
import sympy as sp
M, a, r, u, Om, Rp = sp.symbols('M a r u Omega Rp', real=True)
S = r**2 + a**2*u**2; P = r**2 + a**2; D = r**2 - 2*M*r + a**2
# Boyer-Lindquist, signature (-+++), coordinates (tB, r, u, phB), u = cos theta
s2 = 1 - u**2
gBL = sp.zeros(4, 4)
gBL[0, 0] = -(1 - 2*M*r/S)
gBL[0, 3] = gBL[3, 0] = -2*M*r*a*s2/S
gBL[1, 1] = S/D
gBL[2, 2] = S/s2
gBL[3, 3] = (P + 2*M*r*a**2*s2/S)*s2
# ingoing Kerr coordinates v, phK: dv = dtB + (P/D) dr, dphK = dphB + (a/D) dr; Kerr-Schild time t = v - r; the azimuth
# phi of the oblate chart in which the flat metric is diagonal is phK - arctan(a/r) up to orientation, so
# dt = dtB + (2Mr/D) dr and dphi = dphB + (a/D - a/P) dr = dphB + (2Mra/(D P)) dr
J = sp.eye(4); J[0, 1] = -2*M*r/D; J[3, 1] = -2*M*r*a/(D*P)          # d(xBL)/d(xKS)
gKS = sp.simplify(J.T*gBL*J)
eta = sp.diag(-1, S/P, S/s2, P*s2)
k = sp.Matrix([[-1, -S/P, 0, a*s2]])
H = M*r/S
gprop = eta + 2*H*(k.T*k)
print("A1 proposals' components equal Kerr (BL transformed):", sp.simplify(gKS - gprop) == sp.zeros(4, 4))
kflip = sp.Matrix([[-1, -S/P, 0, -a*s2]])
print("A1b with the other sign of a in k (and phB + a/D -> -a/D) also Kerr of opposite rotation; same-sign test:",
      sp.simplify(gKS - (eta + 2*H*(kflip.T*kflip))) == sp.zeros(4, 4))
g = gprop
print("A2 det g =", sp.factor(sp.simplify(g.det())))
gi = sp.simplify(g.inv())
print("A3 g^rr =", sp.factor(gi[1, 1]), "| g^ru =", gi[1, 2], "| g^uu =", sp.factor(gi[2, 2]),
      "| Sigma g^rr - Delta =", sp.simplify(S*gi[1, 1] - D))
def gram(vs):
    return sp.Matrix(len(vs), len(vs), lambda i, j: (sp.Matrix([vs[i]])*g*sp.Matrix([vs[j]]).T)[0, 0])
T = [1, 0, 0, Om]; U = [0, Rp, 1, 0]; Ph = [0, 0, 0, 1]
d0 = sp.factor(sp.simplify(gram([T, [0, 0, 1, 0], Ph]).det()))
print("B1 Gram det on r = const, any Omega:", d0, "| equals -Delta Sigma:", sp.simplify(d0 + D*S) == 0)
d1 = sp.simplify(gram([T, U, Ph]).det())
print("B2 Gram det on r = R(u), slope Rp, any Omega: minus Sigma (Delta + (1-u^2) Rp^2):",
      sp.simplify(d1 + S*(D + s2*Rp**2)) == 0)
# level set |z| = rho: r = R, Rp = -a^2 u / R, Sigma = rho^2
rho = sp.symbols('rho', positive=True)
Bexpr = r*(2*M - r) - a**2 - s2*a**4*u**2/r**2
lhs = (-S*(D + s2*(a**2*u/r)**2))
print("B3 on the level set det h - Sigma * B(u) == 0 (Sigma = rho^2):", sp.simplify(lhs - S*Bexpr) == 0)
# horizon: K = d_t + Omega_H d_phi null, orthogonal to d_phi, area element
rp = sp.symbols('r_p', positive=True)       # with a^2 = 2 M rp - rp^2
sub = {a**2: 2*M*rp - rp**2}
OmH = a/P
K = [1, 0, 0, OmH]
gKK = sp.simplify((sp.Matrix([K])*g*sp.Matrix([K]).T)[0, 0])
gKP = sp.simplify((sp.Matrix([K])*g*sp.Matrix([Ph]).T)[0, 0])
print("C1 g(K,K) with Omega = a/P:", sp.factor(gKK), "| g(K,d_phi):", sp.factor(gKP), " (both carry the factor Delta)")
Km = [1, 0, 0, -a/P]
print("C1b g(K,K) with Omega = -a/P at Delta = 0 (M = P/2r):",
      sp.factor(sp.simplify((sp.Matrix([Km])*g*sp.Matrix([Km]).T)[0, 0].subs(M, P/(2*r)))))
area2 = sp.simplify((g[2, 2]*g[3, 3] - g[2, 3]**2).subs(M, P/(2*r)))
print("C2 cross-section area element squared at Delta = 0:", sp.factor(area2), "(P^2 expected)")
# surface gravity from d(g(K,K)) = -2 kappa K_flat at the horizon, Omega held at Omega_H = a/(rp^2+a^2)
OH = sp.symbols('O_H')
Kc = sp.Matrix([[1, 0, 0, OH]])
N2 = (Kc*g*Kc.T)[0, 0]
Klow = (Kc*g)                                   # K_mu
grad = sp.Matrix([[sp.diff(N2, x) for x in (sp.Symbol('t'), r, u, sp.Symbol('phi'))]])
aa = sp.symbols('a', real=True)
hor = {OH: a/(rp**2 + a**2), r: rp, M: (rp**2 + a**2)/(2*rp)}
kap_r = sp.simplify((-grad[1]/(2*Klow[1])).subs(hor))
kap_u = sp.simplify(grad[2].subs(hor))
print("C3 kappa from grad(K.K) = -2 kappa K (r component):", sp.factor(kap_r),
      "| u component of grad at horizon:", kap_u, "| K_u:", sp.simplify(Klow[2].subs(hor)))
print("   compare (r_+ - r_-)/(2 P_+) with r_- = a^2/r_+:", sp.factor(sp.simplify((rp - a**2/rp)/(2*(rp**2 + a**2)))))
# ratios of clause (v)
s = sp.symbols('s', positive=True)
rP = M + s; kap = s/(2*M*rP); beta = 2*sp.pi/kap; SBH = 2*sp.pi*M*rP; nu = 1/(16*sp.pi)
print("D1 ratios:", [sp.simplify(x*beta/SBH) for x in (8*sp.pi*nu*M, nu*beta, 2*nu*kap*8*sp.pi*M*rP)])
e = sp.symbols('e', positive=True)
for ex in (1/sp.sqrt(1 - e**2), (1 + sp.sqrt(1 - e**2))/(2*(1 - e**2))):
    print("D2 series:", sp.series(ex, e, 0, 5))
# Smarr
aS = sp.sqrt(M**2 - s**2)
print("D3 M - 2 Omega_H J - s:", sp.simplify(M - 2*(aS/(2*M*rP))*aS*M - s))
# clause (vi) polynomial (edited line)
x = sp.symbols('x')
print("E1 ((1+x)^3 (1-x-x^2) - 1)/x =", sp.expand(sp.cancel(((1 + x)**3*(1 - x - x**2) - 1)/x)))
