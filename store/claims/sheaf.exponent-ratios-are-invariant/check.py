"""sheaf.exponent-ratios-are-invariant: exact checks.

(1) Transformation law: under tau = zeta(sigma) sigma^{a}, the b-derivative sigma d/dsigma of e log tau is
e (sigma zeta'/zeta + a), exact as a rational function of sigma (zeta = 1 + 3 sigma + sigma^2), with value a e at
sigma = 0: the exponent is rescaled by a, for polynomial a, e at three points x0; the ratios
(a e_i)/(a e_j) = e_i/e_j as identities of polynomials (cross-multiplied).
(2) Constant presentation iff constant ratios: with a = c/e_j (e_j > 0) every exponent becomes c e_i/e_j. On the
Kasner variety, as rational functions of the parameter u: p3/p2 = u and -p1/p2 = u/(1+u) exactly, the latter
with r(u) - r(v) = (u - v)/((1+u)(1+v)) and derivative 1/(1+u)^2 > 0 (strictly increasing for u > -1); the ratio
separates all sample parameter values. For constant u the reparametrised exponents are constants; for u(x) = 1 + x
they are not.
(3) Nonconstant exponents force logs: after the best reparametrisation (p2 -> 1) the exponent p3/p2 = u(x) is
nonconstant and d/dx sigma^{u(x)} has log coefficient u'(x) = 1 (the premise's clause (1)).
Not checked: smoothness and positivity of the unit zeta^{e} = exp(e log zeta), which is analysis.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

# generic samples: positive exponent polynomials and a positive rescaling a(x) near x = 0
EXP = [(F(1), F(2)), (F(2), F(-1), F(3)), (F(1, 3), F(1, 3))]
A_OF_X = (F(2), F(1))
U_SAMPLES = [F(1, 5), F(1, 2), F(1), F(2), F(3), F(7)]
X0_SAMPLES = (F(0), F(1, 2), F(-1, 3))
SIG = GA.RF.var()
ZETA = GA.RF1 + GA.RF.const(3) * SIG + SIG * SIG       # a smooth positive unit near sigma = 0


def poly(*c):
    return GA.ptrim([F(x) for x in c])


def check_ratios_are_the_invariants():
    ok = True
    a = poly(*A_OF_X)
    es = [poly(*e) for e in EXP]
    # sigma-exponent of tau^e at a point x0: the b-derivative sigma d/dsigma of e log tau, with
    # tau = zeta(sigma) sigma^a, is e (sigma zeta'/zeta + a), whose value at sigma = 0 is the exponent a e
    s, zeta = SIG, ZETA
    for x0 in X0_SAMPLES:
        a0 = GA.peval(a, x0)
        for e in es:
            e0 = GA.peval(e, x0)
            bdlog = s * zeta.deriv() / zeta + GA.RF.const(a0)
            ok = ok and (GA.RF.const(e0) * bdlog).eval(F(0)) == GA.peval(GA.pmul(a, e), x0)
            ok = ok and (s * zeta.deriv() / zeta).eval(F(0)) == 0
    # ratio invariance: (a e_i) e_j = (a e_j) e_i, and the leading coefficient of a e_0 = (2 + x)(1 + 2x)
    for i in range(3):
        for j in range(3):
            ok = ok and GA.pmul(GA.pmul(a, es[i]), es[j]) == GA.pmul(GA.pmul(a, es[j]), es[i])
    ok = ok and GA.pmul(a, es[0]) == poly(2, 5, 2)
    GA.check("quasi-homogeneous changes multiply every exponent by a(x); the ratios are invariant", ok)
    return ok


def check_kasner_ratio_monotone_and_separating():
    ok = True
    u = GA.RF.var()
    D = GA.RF1 + u + u * u
    p1, p2, p3 = -u / D, (GA.RF1 + u) / D, u * (GA.RF1 + u) / D
    r = -(p1 / p2)
    ok = ok and r.eqrf(u / (GA.RF1 + u))
    ok = ok and (p3 / p2).eqrf(u)
    ok = ok and r.deriv().eqrf(GA.RF1 / ((GA.RF1 + u) * (GA.RF1 + u)))
    for v in U_SAMPLES:
        rv = v / (1 + v)
        ok = ok and (r - GA.RF.const(rv)).eqrf((u - GA.RF.const(v)) / ((GA.RF1 + u) * GA.RF.const(1 + v)))
    vals = [r.eval(v) for v in U_SAMPLES]
    ok = ok and all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))
    ok = ok and len(set(vals)) == len(U_SAMPLES)
    GA.check("on the Kasner variety -p1/p2 = u/(1+u) is strictly increasing, p3/p2 = u: ratios separate u", ok)
    return ok


def check_constant_presentation_iff_constant_ratios():
    ok = True
    x = GA.RF.var()

    def exps_after(u_of_x):
        D = GA.RF1 + u_of_x + u_of_x * u_of_x
        p = (-u_of_x / D, (GA.RF1 + u_of_x) / D, u_of_x * (GA.RF1 + u_of_x) / D)
        a = GA.RF1 / p[1]                    # a = c / p2 with c = 1, so p2 becomes 1
        return [a * pi for pi in p]

    const = exps_after(GA.RF.const(F(2)))
    ok = ok and [c.eval(F(0)) for c in const] == [F(-2, 3), F(1), F(2)]
    ok = ok and all(c.deriv().is_zero() for c in const)
    moving = exps_after(GA.RF1 + x)
    ok = ok and moving[2].eqrf(GA.RF1 + x) and moving[1].eqrf(GA.RF1)
    ok = ok and not moving[0].deriv().is_zero() and not moving[2].deriv().is_zero()
    GA.check("a constant-exponent presentation exists iff the ratios are constant (u = 2 versus u = 1 + x)", ok)
    return ok


def check_varying_exponents_keep_their_logs():
    ex = premise("sheaf.differential-closure-filtration-conormality")
    ok = True
    pc, aterm, a_dx, logdeg = ex["pc"], ex["aterm"], ex["a_dx"], ex["logdeg"]
    # after the reparametrisation p2 -> 1 the third exponent is u(x) = 1 + x
    term = aterm(pc(1), pc(1, 1))
    d = a_dx(term)
    ok = ok and logdeg(d) == 1 and d == aterm(pc(1), pc(1, 1), 1)
    # at constant u the reparametrised monomial is log-free under d/dx (it is killed)
    ok = ok and a_dx(aterm(pc(1), pc(2))) == {}
    GA.check("nonconstant reparametrised exponents still produce log(sigma) under d/dx", ok)
    return ok
