"""synthesis.incidence-vacua-entanglement-light-cones-of-unit-diamond: exact checks.

Two-mode Fock space (ascent mode a, boost qubit b) with Jordan-Wigner matrices over the rationals: the vector
(1 - u a* b*)|0> has ascent marginal diag(1, u^2)/(1 + u^2), and (b* - v a*)|0> has diag(1, v^2)/(1 + v^2).
Entropy s(u) = ln(1 + u^2) - n ln(u^2), n = u^2/(1 + u^2), handled as rational-function coefficients of the two
logarithms: ds/du = -ln(u^2) dn/du exactly (the rational parts cancel), dn/du = 2u/(1 + u^2)^2, so the critical
points are u = 0 and u^2 = 1 and the sign of ds/du is that of u(1 - u^2). The maximal set |u| = 1 or |v| = 1 is
checked against the light cones of t = +-1. In Cl(2,4) with every generator unitary, the boost generator e1 e2
and the dilation generator e+ e- are self-adjoint, so the groups they generate are not unitary.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


mm = GA.mat_mul


def mv(A, x):
    return [sum(A[i][k] * x[k] for k in range(len(x))) for i in range(len(A))]


def kron(A, B):
    return [[A[i // len(B)][j // len(B)] * B[i % len(B)][j % len(B)] for j in range(len(A) * len(B))]
            for i in range(len(A) * len(B))]


def ascent_marginal(psi):
    """Reduced density matrix of mode a (first tensor factor) of a real vector on C^2 (x) C^2."""
    nrm = sum(c * c for c in psi)
    return [[sum(psi[2 * i + k] * psi[2 * j + k] for k in range(2)) / nrm for j in range(2)] for i in range(2)]


def adjoint(x, squares):
    """g* = g^{-1} on generators: e* = e if e^2 = 1, -e if e^2 = -1; reversed on products."""
    out = {}
    for b, c in GA.reverse(x).items():
        s = 1
        for k in b:
            s *= squares[k]
        out[b] = c * s
    return out


def check_incidence_entanglement():
    premise("synthesis.incidence-vacua-thermofield-real-capacity")
    premise("state-selection.partner-purification-are-canonical")
    premise("one-relation.spacetime-manifold-vacuum-lines")
    # Jordan-Wigner: a = sigma (x) 1, b = Z (x) sigma, with sigma = |0><1|, Z = diag(1, -1)
    sig = [[F(0), F(1)], [F(0), F(0)]]
    sigd = [[F(0), F(0)], [F(1), F(0)]]
    Zm = [[F(1), F(0)], [F(0), F(-1)]]
    I2 = [[F(1), F(0)], [F(0), F(1)]]
    ad = kron(sigd, I2)
    bd = kron(Zm, sigd)
    vac = [F(1), F(0), F(0), F(0)]
    for u in (F(1, 3), F(1), F(2), F(-5, 2)):
        om = [vac[i] - u * mv(mm(ad, bd), vac)[i] for i in range(4)]
        rho = ascent_marginal(om)
        assert rho == [[1 / (1 + u * u), F(0)], [F(0), u * u / (1 + u * u)]]
        ps = [mv(bd, vac)[i] - u * mv(ad, vac)[i] for i in range(4)]
        rho2 = ascent_marginal(ps)
        assert rho2 == [[1 / (1 + u * u), F(0)], [F(0), u * u / (1 + u * u)]]
    # entropy calculus: s = L1 - n L2, L1 = ln(1 + u^2), L2 = ln(u^2); d L1 = 2u/(1+u^2), d L2 = 2/u
    U = GA.RF.var()
    one = GA.RF1
    n = U * U / (one + U * U)
    dn = n.deriv()
    assert dn.eqrf(GA.RF.const(2) * U / ((one + U * U) * (one + U * U)))
    dL1 = GA.RF.const(2) * U / (one + U * U)
    dL2 = GA.RF.const(2) / U
    rational_part = dL1 - n * dL2                    # ds/du = rational_part - dn * L2
    assert rational_part.is_zero()                   # so ds/du = (-L2) dn = beta dn, beta = -ln u^2
    # critical points and monotonicity: sign(ds/du) = sign(-ln u^2) sign(dn) = sign((1 - u^2) u)
    for k in range(-20, 21):
        u = F(k, 7)
        if u == 0:
            continue
        beta_sign = (1 if u * u < 1 else (-1 if u * u > 1 else 0))
        dn_sign = 1 if dn.eval(u) > 0 else -1
        assert dn_sign == (1 if u > 0 else -1)
        expected = (1 - u * u) * u
        assert (beta_sign * dn_sign > 0) == (expected > 0) and (beta_sign == 0) == (expected == 0)
    assert n.eval(F(1)) == F(1, 2) and n.eval(F(-1)) == F(1, 2)
    # the maximal set: |t - r| = 1 or |t + r| = 1 with r >= 0, against the light cones of t = +-1 at r = 0
    for t2 in range(-12, 13):
        for r2 in range(0, 13):
            t, r = F(t2, 4), F(r2, 4)
            on_set = abs(t - r) == 1 or abs(t + r) == 1
            on_cones = any((t - tc) ** 2 == r * r for tc in (1, -1))
            assert on_set == on_cones
    # on t = 0: n(r) = r^2/(1 + r^2), entropy increasing on (0, 1), maximal at r = 1
    assert n.eval(F(1, 2)) < n.eval(F(1)) and n.eval(F(1)) == F(1, 2)
    # boost and dilation generators: self-adjoint, not unitary, for the Hermitian structure of the module
    sq = (1, -1, -1, -1, 1, -1)                       # e1, e2, e3, e4, e+, e-
    boost = GA.mul(GA.gen(0), GA.gen(1), sq)
    dil = GA.mul(GA.gen(4), GA.gen(5), sq)
    for gnr in (boost, dil):
        assert GA.eq(adjoint(gnr, sq), gnr)
        assert GA.eq(GA.mul(gnr, gnr, sq), GA.sc(1))  # squares to one: exp(s g) = cosh s + g sinh s
        # exp(s g) = c + s g with c^2 - s^2 = 1 is self-adjoint, so (exp)* exp = exp(2 s g) != 1: not unitary
        el = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), gnr))
        prod = GA.mul(adjoint(el, sq), el, sq)
        assert GA.eq(prod, GA.add(GA.sc(F(34, 16)), GA.scal(F(30, 16), gnr))) and not GA.eq(prod, GA.sc(1))
    for i in range(6):                                # every generator is unitary
        e = GA.gen(i)
        assert GA.eq(GA.mul(adjoint(e, sq), e, sq), GA.sc(1))
    return True
