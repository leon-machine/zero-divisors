"""hawking.gibbs-states-are-kms-conversely-finite: exact checks on End(C^m), m = 1, 2, 3, 4.

H is diagonal with integer eigenvalues lambda_a, distinct or degenerate (spectra below, including
the fully degenerate one). The Boltzmann factor x = e^{-beta} is kept as an indeterminate (GA.RF,
rational functions in x), so every identity holds for all real beta at once; e^{-beta H} =
diag(x^{lambda_a}) and alpha_{i beta}(E_ab) = x^{lambda_a - lambda_b} E_ab.
(1) The Gibbs state omega_G = tr(e^{-beta H} .)/tr(e^{-beta H}) satisfies omega_G(x y) =
omega_G(y alpha_{i beta}(x)) on all m^4 pairs of matrix units, as rational-function identities.
(2) Uniqueness: the KMS constraints, linear in the m^2 entries of an unknown density matrix, have
over the field Q(x) a one-dimensional solution space spanned by diag(x^{lambda_a}), degenerate spectra
included; at the specialisation x = 1 (beta = 0) it is the tracial state, and at x = 2/3 and 3/2 the
rational kernel is again one-dimensional.
"""
from fractions import Fraction as F

import GA

SPECTRA = [[0], [0, 1], [1, 1], [0, 1, 1], [0, 1, 2], [0, 2, 2, 5]]
X = GA.RF.var()


def xpow(p):
    out = GA.RF1
    for _ in range(abs(p)):
        out = out * X if p > 0 else out / X
    return out


def rf_kernel(rows, ncols):
    m = [list(r) for r in rows]
    piv_cols, r0 = [], 0
    for c in range(ncols):
        piv = next((i for i in range(r0, len(m)) if not m[i][c].is_zero()), None)
        if piv is None:
            continue
        m[r0], m[piv] = m[piv], m[r0]
        pv = m[r0][c]
        m[r0] = [y / pv for y in m[r0]]
        for i in range(len(m)):
            if i != r0 and not m[i][c].is_zero():
                f = m[i][c]
                m[i] = [y - f * z for y, z in zip(m[i], m[r0])]
        piv_cols.append(c)
        r0 += 1
    out = []
    for fc in [c for c in range(ncols) if c not in piv_cols]:
        v = [GA.RF0] * ncols
        v[fc] = GA.RF1
        for i, pc in enumerate(piv_cols):
            v[pc] = GA.RF0 - m[i][fc]
        out.append(v)
    return out


def kms_rows(lam, factor):
    """Rows of omega(E_ab E_cd) - omega(E_cd alpha_{i beta}(E_ab)) = 0 in the unknowns rho[r][s]
    (omega = tr(rho .), unknown index m r + s). factor(p) is x^p."""
    m = len(lam)
    rows = []
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    row = [factor(0) - factor(0)] * (m * m)
                    if b == c:                       # tr(rho E_ad) = rho[d][a]
                        row[d * m + a] = row[d * m + a] + factor(0)
                    if d == a:                       # x^{la - lb} tr(rho E_cb) = x^{..} rho[b][c]
                        row[b * m + c] = row[b * m + c] - factor(lam[a] - lam[b])
                    rows.append(row)
    return rows


def check_gibbs_state_satisfies_kms_symbolically():
    pairs = 0
    for lam in SPECTRA:
        m = len(lam)
        Z = GA.RF0
        for la in lam:
            Z = Z + xpow(la)
        rho = [xpow(la) / Z for la in lam]                     # diagonal of the Gibbs matrix

        def om(a, b):
            return rho[a] if a == b else GA.RF0

        for a in range(m):
            for b in range(m):
                for c in range(m):
                    for d in range(m):
                        lhs = om(a, d) if b == c else GA.RF0
                        rhs = xpow(lam[a] - lam[b]) * om(c, b) if d == a else GA.RF0
                        assert lhs.eqrf(rhs)
                        pairs += 1
        # normalisation, and beta = 0 gives the tracial state
        tot = GA.RF0
        for r in rho:
            tot = tot + r
        assert tot.eqrf(GA.RF1)
        assert all(r.eval(F(1)) == F(1, m) for r in rho)
    assert pairs == 1 + 16 + 16 + 81 + 81 + 256, pairs


def check_kms_state_unique_degenerate_included():
    for lam in SPECTRA:
        m = len(lam)
        ker = rf_kernel(kms_rows(lam, xpow), m * m)
        assert len(ker) == 1, (lam, len(ker))
        k = ker[0]
        # proportional to diag(x^{lambda_a}): off-diagonal zero, diagonal ratios x^{la - l0}
        piv = 0
        for r in range(m):
            for s in range(m):
                if r != s:
                    assert k[r * m + s].is_zero()
        for r in range(m):
            assert k[r * m + r].eqrf(k[piv].__mul__(xpow(lam[r] - lam[0])))
        # rational specialisations, including beta = 0 (x = 1)
        for xv in (F(1), F(2, 3), F(3, 2)):
            rows = kms_rows(lam, lambda p, xv=xv: xv ** p)
            kr = GA.field_kernel(rows)
            assert len(kr) == 1
            want = [xv ** lam[r] if r == s else F(0) for r in range(m) for s in range(m)]
            assert GA.field_rank([kr[0], want]) == 1
