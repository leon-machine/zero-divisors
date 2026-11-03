#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T07.py: exact-arithmetic verification of the computational identities of
"Hawking Radiation from the Ledger" (Transport Papers, T7).

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rational arithmetic and rational functions
in a formal Boltzmann variable throughout, no floating point anywhere.

Conventions.  The formal variable x stands for the Boltzmann factor
e^{-beta*omega} of one mode (omega the Schwarzschild frequency; or of the
level spacing, Section 6); KMS
identities are checked as identities of rational functions in x.  Fock spaces
of n fermionic modes are represented on bitmasks 0..2^n-1; occupancies are
Fermi-Dirac fractions.  Statement tags refer to the compiled paper.
"""

from fractions import Fraction
import GA as g

# ---------------------------------------------------------------------------
# Part A: the single mode (prop:mode), in the blade engine over Cl(1,1)
# ---------------------------------------------------------------------------

SQ = g.sig(1, 1)                       # e0^2 = +1, e1^2 = -1
e0, e1 = g.gen(0), g.gen(1)
v = g.scal(Fraction(1, 2), g.add(e0, e1))
w = g.scal(Fraction(1, 2), g.sub(e0, e1))

g.check("prop:mode: v^2 = 0 and (v*)^2 = 0",
      g.is_zero(g.mul(v, v, SQ)) and g.is_zero(g.mul(w, w, SQ)))
g.check("prop:mode: vv* + v*v = 1",
      g.eq(g.add(g.mul(v, w, SQ), g.mul(w, v, SQ)), g.sc(1)))

sigma = g.sub(g.mul(w, v, SQ), g.mul(v, w, SQ))
g.check("prop:mode(1): sigma := v*v - vv* equals the unit boost bivector e0e1",
      g.eq(sigma, g.mul(e0, e1, SQ)))
g.check("prop:mode(1): sigma^2 = 1", g.eq(g.mul(sigma, sigma, SQ), g.sc(1)))
g.check("prop:mode(2): sigma v = -v and v sigma = +v (weight -1); "
      "sigma v* = +v* and v* sigma = -v* (weight +1)",
      g.eq(g.mul(sigma, v, SQ), g.scal(-1, v)) and g.eq(g.mul(v, sigma, SQ), v) and
      g.eq(g.mul(sigma, w, SQ), w) and g.eq(g.mul(w, sigma, SQ), g.scal(-1, w)))
g.check("prop:mode(3): (1 + sigma)/2 = v*v and (1 - sigma)/2 = vv*",
      g.eq(g.scal(Fraction(1, 2), g.add(g.sc(1), sigma)), g.mul(w, v, SQ)) and
      g.eq(g.scal(Fraction(1, 2), g.sub(g.sc(1), sigma)), g.mul(v, w, SQ)))
g.check("prop:mode(5): the bivector space of Cl(1,1) is one-dimensional "
      "(unique rotor flow up to reparametrisation and orientation)",
      len([b for b in g.all_blades(2) if len(b) == 2]) == 1)

# Finite conjugation at a rational rapidity: cosh(l/2) = 5/3, sinh(l/2) = 4/3,
# so e^{-l} = (5/3 - 4/3)^2 = 1/9.  R v R^{-1} = v/9 and R v* R^{-1} = 9 v*.
R_rot = g.add(g.sc(Fraction(5, 3)), g.scal(Fraction(4, 3), sigma))
R_inv = g.sub(g.sc(Fraction(5, 3)), g.scal(Fraction(4, 3), sigma))
g.check("prop:mode(2): finite conjugation R v R^{-1} = e^{-lambda} v at the "
      "rational rapidity (cosh, sinh) = (5/3, 4/3): scale factors 1/9 and 9",
      g.eq(g.mul(g.mul(R_rot, v, SQ), R_inv, SQ), g.scal(Fraction(1, 9), v)) and
      g.eq(g.mul(g.mul(R_rot, w, SQ), R_inv, SQ), g.scal(Fraction(9), w)))

# Fock representation of the mode: v = annihilation, v* = creation on C^2
V2 = [[Fraction(0), Fraction(1)], [Fraction(0), Fraction(0)]]
W2 = [[Fraction(0), Fraction(0)], [Fraction(1), Fraction(0)]]
N2 = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]]
ok = all((W2[i][0] * V2[0][j] + W2[i][1] * V2[1][j]) -
         (V2[i][0] * W2[0][j] + V2[i][1] * W2[1][j])
         == 2 * (N2[i][j] - (Fraction(1, 2) if i == j else 0)) * 1
         for i in range(2) for j in range(2))
g.check("prop:mode(4): in the Fock representation, sigma/2 = N - 1/2", ok)

# ---------------------------------------------------------------------------
# Part B: lem:gibbs on the mode algebra M_2, symbolically in x
# ---------------------------------------------------------------------------

x = g.RF.var()                          # the Boltzmann factor e^{-beta omega}
LAM = [0, 1]                          # eigenvalues of H in units of omega


def xpow(p):
    """x^p for integer p (possibly negative), as an RF."""
    out = g.RF1
    for _ in range(abs(p)):
        out = out * x if p > 0 else out / x
    return out


# Gibbs: rho = diag(1, x)/(1+x); KMS on all 16 matrix-unit pairs.
rho = [g.RF1 / (g.RF1 + x), x / (g.RF1 + x)]      # diagonal entries


def om_unit(a, b):
    """omega_G(E_ab) for the Gibbs state (diagonal rho)."""
    return rho[a] if a == b else g.RF0


ok = True
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                # omega(E_ab E_cd) = delta_bc omega(E_ad)
                lhs = om_unit(a, d) if b == c else g.RF0
                # omega(E_cd alpha_{i beta}(E_ab)) = x^{lam_a - lam_b} delta_da omega(E_cb)
                rhs = (xpow(LAM[a] - LAM[b]) * om_unit(c, b)) if d == a else g.RF0
                ok = ok and lhs.eqrf(rhs)
g.check("lem:gibbs: the Gibbs state satisfies the KMS identity on all 16 "
      "matrix-unit pairs, as identities in the formal Boltzmann factor", ok)

# Uniqueness: solve the KMS constraints for an arbitrary density matrix.
# Unknowns r[da] (4 entries).  Equation: delta_bc r_da = x^{lam_a-lam_b} delta_da r_bc.
rows = []
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                coeff = [g.RF0] * 4          # coefficients of r_00, r_01, r_10, r_11
                if b == c:
                    coeff[2 * d + a] = coeff[2 * d + a] + g.RF1
                if d == a:
                    coeff[2 * b + c] = coeff[2 * b + c] - xpow(LAM[a] - LAM[b])
                if not all(cf.is_zero() for cf in coeff):
                    rows.append(coeff)


def rf_kernel(rows, ncols):
    """Kernel basis of a matrix over the rational-function field."""
    m = [r[:] for r in rows]
    piv_cols, r0 = [], 0
    for ccol in range(ncols):
        piv = next((i for i in range(r0, len(m)) if not m[i][ccol].is_zero()), None)
        if piv is None:
            continue
        m[r0], m[piv] = m[piv], m[r0]
        pv = m[r0][ccol]
        m[r0] = [y / pv for y in m[r0]]
        for i in range(len(m)):
            if i != r0 and not m[i][ccol].is_zero():
                f = m[i][ccol]
                m[i] = [y - f * z for y, z in zip(m[i], m[r0])]
        piv_cols.append(ccol)
        r0 += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        vvec = [g.RF0] * ncols
        vvec[fc] = g.RF1
        for i, pc in enumerate(piv_cols):
            vvec[pc] = g.RF0 - m[i][fc]
        basis.append(vvec)
    return basis


ker = rf_kernel(rows, 4)
ok = (len(ker) == 1)
if ok:
    k = ker[0]
    # kernel vector (r00, r01, r10, r11) must be proportional to (1, 0, 0, x)
    ok = k[1].is_zero() and k[2].is_zero() and (k[3].eqrf(k[0] * x))
g.check("lem:gibbs: the KMS constraints have a one-dimensional solution space, "
      "spanned by the Gibbs density matrix (uniqueness, solved symbolically)", ok)

# Detailed balance / the derived symbol (thm:istate(2)):
n_occ = x / (g.RF1 + x)
g.check("thm:istate(3): the derived symbol satisfies n = e^{-beta omega}(1 - n), "
      "i.e. detailed balance n/(1-n) = x, as a rational-function identity",
      n_occ.eqrf((g.RF1 - n_occ) * x))

# ---------------------------------------------------------------------------
# Part C: window KMS (thm:istate(1)) on three modes at rational Boltzmann
# factors, fully symbolic in matrix units
# ---------------------------------------------------------------------------

XS = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
STATES = [(i, j, k) for i in range(2) for j in range(2) for k in range(2)]


def gibbs_weight(st):
    """e^{-beta H_F} eigenvalue on the occupation state st, built from the
    DYNAMICS alone (the Hamiltonian's Boltzmann factors), not from any state."""
    out = Fraction(1)
    for bit, xx in zip(st, XS):
        out *= xx if bit else 1
    return out


def fd_weight(st):
    """Diagonal entry of the FD-symbol product state tensor_j diag(1-n_j, n_j),
    built INDEPENDENTLY from the symbol n_j = x_j/(1+x_j), not from H_F."""
    out = Fraction(1)
    for bit, xx in zip(st, XS):
        n_j = xx / (1 + xx)
        out *= n_j if bit else (1 - n_j)
    return out


ZG = sum(gibbs_weight(st) for st in STATES)
g.check("thm:istate(1): the FD-symbol product state equals the Gibbs matrix of "
      "H_F, the two sides built independently, entry by entry on the 8 states "
      "of a three-mode window", all(fd_weight(st) == gibbs_weight(st) / ZG
                                    for st in STATES))

ok = True
for s1 in STATES:
    for t1 in STATES:
        for s2 in STATES:
            for t2 in STATES:
                # x = E_{s1 t1}, y = E_{s2 t2}; omega from the FD product state,
                # alpha_{i beta} from the DYNAMICS (gibbs_weight ratios): the
                # identity holds iff the state is Gibbs for the dynamics.
                lhs = fd_weight(s1) if (t1 == s2 and s1 == t2) else Fraction(0)
                rhs = ((gibbs_weight(s1) / gibbs_weight(t1)) * fd_weight(s2)) \
                    if (t2 == s1 and s2 == t1) else Fraction(0)
                ok = ok and lhs == rhs
g.check("thm:istate(1): the FD product state satisfies the KMS identity for "
      "the window dynamics on all 4096 matrix-unit pairs (state and dynamics "
      "supplied independently)", ok)

# thm:istate(2)-(3): solve the FULL KMS constraint system on a two-mode
# window for an arbitrary density matrix (16 unknowns rho_{ab}), against the
# window dynamics supplied independently.  The kernel must be one-dimensional
# and spanned by the Gibbs matrix; the unique solution must have vanishing
# pairing (gauge invariance forced) and the Fermi-Dirac symbol.
X2 = [Fraction(1, 2), Fraction(1, 3)]
ST2 = [(i, j) for i in range(2) for j in range(2)]
IDX = {st: n for n, st in enumerate(ST2)}


def w2(st):
    """e^{-beta H_F} eigenvalue on the occupation state st: the DYNAMICS."""
    out = Fraction(1)
    for bit, xx in zip(st, X2):
        out *= xx if bit else 1
    return out


# KMS on matrix units E_{s1 t1}, E_{s2 t2}, with omega(E_{ab}) = rho_{ba}:
#   [t1 == s2] rho_{t2 s1}  =  (w(s1)/w(t1)) [t2 == s1] rho_{t1 s2}.
rows2 = []
for s1 in ST2:
    for t1 in ST2:
        for s2 in ST2:
            for t2 in ST2:
                coeff = [Fraction(0)] * 16
                if t1 == s2:
                    coeff[4 * IDX[t2] + IDX[s1]] += 1
                if t2 == s1:
                    coeff[4 * IDX[t1] + IDX[s2]] -= w2(s1) / w2(t1)
                if any(c != 0 for c in coeff):
                    rows2.append(coeff)


def frac_kernel(rows, ncols):
    """Kernel basis of a rational matrix (Gaussian elimination over Q)."""
    m = [r[:] for r in rows]
    piv_cols, r0 = [], 0
    for ccol in range(ncols):
        piv = next((i for i in range(r0, len(m)) if m[i][ccol] != 0), None)
        if piv is None:
            continue
        m[r0], m[piv] = m[piv], m[r0]
        pv = m[r0][ccol]
        m[r0] = [y / pv for y in m[r0]]
        for i in range(len(m)):
            if i != r0 and m[i][ccol] != 0:
                f = m[i][ccol]
                m[i] = [y - f * z for y, z in zip(m[i], m[r0])]
        piv_cols.append(ccol)
        r0 += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        vv = [Fraction(0)] * ncols
        vv[fc] = Fraction(1)
        for i, pc in enumerate(piv_cols):
            vv[pc] = -m[i][fc]
        basis.append(vv)
    return basis


ker2 = frac_kernel(rows2, 16)
ok = (len(ker2) == 1)
if ok:
    kv = ker2[0]
    rho2 = [[kv[4 * a4 + b4] for b4 in range(4)] for a4 in range(4)]
    tr2 = sum(rho2[a4][a4] for a4 in range(4))
    ok = tr2 != 0
if ok:
    rho2 = [[rho2[a4][b4] / tr2 for b4 in range(4)] for a4 in range(4)]
    # (i) the unique solution is the Gibbs matrix of H_F, entry by entry
    Z2 = sum(w2(st) for st in ST2)
    ok = all(rho2[IDX[st]][IDX[tt]] == (w2(st) / Z2 if st == tt else 0)
             for st in ST2 for tt in ST2)
if ok:
    def cre2(j):
        """Creation operator a_j^dag as a 4x4 matrix, Jordan-Wigner signs."""
        M = [[Fraction(0)] * 4 for _ in range(4)]
        for st in ST2:
            if st[j]:
                continue
            below = sum(st[i] for i in range(j))
            new = tuple(1 if i == j else st[i] for i in range(2))
            M[IDX[new]][IDX[st]] = Fraction(-1 if below % 2 else 1)
        return M

    def ann2(j):
        Mc = cre2(j)
        return [[Mc[b4][a4] for b4 in range(4)] for a4 in range(4)]

    def mm2(A, B):
        return [[sum(A[a4][c4] * B[c4][b4] for c4 in range(4))
                 for b4 in range(4)] for a4 in range(4)]

    def expval2(M):
        return sum(rho2[a4][b4] * M[b4][a4]
                   for a4 in range(4) for b4 in range(4))

    # (ii) the pairing vanishes: omega(a_j^dag a_k^dag) = 0, both orders
    pair_ok = (expval2(mm2(cre2(0), cre2(1))) == 0 and
               expval2(mm2(cre2(1), cre2(0))) == 0)
    # (iii) the symbol is mode-diagonal Fermi-Dirac
    sym_ok = all(expval2(mm2(cre2(j), ann2(k))) ==
                 ((X2[j] / (1 + X2[j])) if j == k else 0)
                 for j in range(2) for k in range(2))
    ok = ok and pair_ok and sym_ok
g.check("thm:istate(2)-(3): on a two-mode window the full KMS constraint "
      "system has a one-dimensional kernel spanned by the Gibbs matrix, and "
      "the unique solution has vanishing pairing and the Fermi-Dirac symbol "
      "(state solved for; dynamics supplied independently)", ok)

# ---------------------------------------------------------------------------
# Part D: the finite window's currents (prop:edge), n = 8 modes on bitmasks
# ---------------------------------------------------------------------------

NW = 8


def popcount(m):
    return bin(m).count("1")


def psi_dag_psi(a, b, statevec):
    """Apply psi_a^dagger psi_b (0-indexed modes) to a dict state."""
    out = {}
    for s, c in statevec.items():
        if not (s >> b) & 1:
            continue
        sgn1 = -1 if popcount(s & ((1 << b) - 1)) % 2 else 1
        s1 = s & ~(1 << b)
        if (s1 >> a) & 1:
            continue
        sgn2 = -1 if popcount(s1 & ((1 << a) - 1)) % 2 else 1
        s2 = s1 | (1 << a)
        out[s2] = out.get(s2, Fraction(0)) + Fraction(sgn1 * sgn2) * c
    return {s: c for s, c in out.items() if c != 0}


def current(m, dagger=False):
    """Return the list of (a, b) bilinears composing a_m (or a_m^dagger)."""
    if not dagger:
        return [(k, k + m) for k in range(NW - m)]
    return [(k + m, k) for k in range(NW - m)]


def apply_bilin_sum(pairs, statevec):
    out = {}
    for (a, b) in pairs:
        for s, c in psi_dag_psi(a, b, statevec).items():
            out[s] = out.get(s, Fraction(0)) + c
    return {s: c for s, c in out.items() if c != 0}


def commutator_apply(p1, p2, statevec):
    t1 = apply_bilin_sum(p1, apply_bilin_sum(p2, statevec))
    t2 = apply_bilin_sum(p2, apply_bilin_sum(p1, statevec))
    out = dict(t1)
    for s, c in t2.items():
        out[s] = out.get(s, Fraction(0)) - c
    return {s: c for s, c in out.items() if c != 0}


def state_eq(u, vv):
    ks = set(u) | set(vv)
    return all(u.get(k, Fraction(0)) == vv.get(k, Fraction(0)) for k in ks)


ok = True
for m in (1, 2, 3):
    am, amd = current(m), current(m, True)
    B = [(k, k) for k in range(m)]
    T = [(k, k) for k in range(NW - m, NW)]
    for s in range(1 << NW):
        sv = {s: Fraction(1)}
        lhs = commutator_apply(am, amd, sv)
        bt = apply_bilin_sum(B, sv)
        for st, c in apply_bilin_sum(T, sv).items():
            bt[st] = bt.get(st, Fraction(0)) - c
        bt = {st: c for st, c in bt.items() if c != 0}
        ok = ok and state_eq(lhs, bt)
g.check("prop:edge: [a_m, a_m^dag] = B_m - T_m as an operator identity on all "
      "256 states of an 8-mode window, for m = 1, 2, 3", ok)

ok = True
for m in (1, 2, 3):
    am, amd = current(m), current(m, True)
    for s in range(1 << NW):
        bottom_ok = all((s >> k) & 1 for k in range(m))
        top_ok = all(not ((s >> k) & 1) for k in range(NW - m, NW))
        if not (bottom_ok and top_ok):
            continue
        sv = {s: Fraction(1)}
        lhs = commutator_apply(am, amd, sv)
        ok = ok and state_eq(lhs, {s: Fraction(m)})
g.check("prop:edge: on every edge-clean state the free-boson relation "
      "[a_m, a_m^dag] = m holds exactly", ok)

ok = True
for (m, mp) in ((1, 2), (1, 3), (2, 3)):
    am, amp = current(m), current(mp)
    for s in range(1 << NW):
        sv = {s: Fraction(1)}
        ok = ok and commutator_apply(am, amp, sv) == {}
g.check("prop:edge: [a_m, a_{m'}] = 0 exactly in the finite window, "
      "all pairs m != m'", ok)

ok = True
for (m, mp) in ((1, 2), (2, 3)):
    am, ampd = current(m), current(mp, True)
    edge = 3
    for s in range(1 << NW):
        bottom_ok = all((s >> k) & 1 for k in range(edge))
        top_ok = all(not ((s >> k) & 1) for k in range(NW - edge, NW))
        if not (bottom_ok and top_ok):
            continue
        sv = {s: Fraction(1)}
        ok = ok and commutator_apply(am, ampd, sv) == {}
g.check("prop:edge: the cross commutator [a_m, a_{m'}^dag] (m != m') vanishes "
      "on edge-clean states: its central part is delta_{mm'} m", ok)

# ---------------------------------------------------------------------------
# Part E: the Planck factor and the tails (prop:planck)
# ---------------------------------------------------------------------------

a_var = g.RF.var()
ok = True
for b in (2, 3, 8):                    # b = x^{-m}, rational instances
    B_ = g.RF.const(b)
    n_k = g.RF1 / (a_var + g.RF1)                     # n_k with a = x^{-k}
    n_km = g.RF1 / (a_var * B_ + g.RF1)               # n_{k+m}
    lhs = n_k - n_km
    rhs = (B_ - g.RF1) * n_km * (g.RF1 - n_k)
    ok = ok and lhs.eqrf(rhs)
g.check("prop:planck(1): the detailed-balance identity n_k - n_{k+m} = "
      "(x^{-m} - 1) n_{k+m}(1 - n_k), as a rational-function identity in "
      "the formal x^{-k}", ok)


def occ(k, xq):
    return Fraction(1) / (Fraction(xq) ** (-k) + 1)


ok = True
for xq in (Fraction(1, 2), Fraction(1, 3)):
    for m in (1, 2, 3):
        closed = Fraction(m) / (Fraction(xq) ** (-m) - 1)
        for K in (30, 40):
            S = sum(occ(k + m, xq) * (1 - occ(k, xq)) for k in range(-K, K - m + 1))
            tail_bound = 2 * m * Fraction(xq) ** (K - m) / (1 - Fraction(xq))
            ok = ok and (closed - S > 0) and (closed - S <= tail_bound)
g.check("prop:planck(2)-(3): the window sums approach the exact Planck factor "
      "m/(x^{-m} - 1) from below, within the proven tail bound "
      "2m x^{K-m}/(1-x), at rational instances (exact inequalities)", ok)

# Wick instance: <a_m^dag a_m> in the product FD state on the 8-mode window
ok = True
for m in (1, 2):
    xq = Fraction(1, 2)
    sea = NW // 2                       # modes 0..sea-1 filled at x -> 0
    nocc = [occ(k - sea, xq) for k in range(NW)]
    # nocc[k] = 1/(x^{-(k-sea)} + 1): occupancy DEcreasing with the mode index
    # k, sea between modes 3 and 4, matching prop:planck's ladder convention
    # density-matrix expectation of a_m^dag a_m, diagonal product state
    expct = Fraction(0)
    for s in range(1 << NW):
        wgt = Fraction(1)
        for k in range(NW):
            wgt *= nocc[k] if (s >> k) & 1 else (1 - nocc[k])
        sv = {s: Fraction(1)}
        img = apply_bilin_sum(current(m, True), apply_bilin_sum(current(m), sv))
        expct += wgt * img.get(s, Fraction(0))
    wick = sum(nocc[k + m] * (1 - nocc[k]) for k in range(NW - m))
    ok = ok and expct == wick
g.check("prop:planck(2): the Wick formula <a_m^dag a_m> = sum n_{k+m}(1-n_k) "
      "agrees exactly with the density-matrix expectation on the 8-mode "
      "window, m = 1, 2", ok)

# ---------------------------------------------------------------------------
# Part F: lift arithmetic (prop:homogeneity, the helicity and greybody assemblies)
# ---------------------------------------------------------------------------

g.check("prop:homogeneity / assembly (helicity lift): the table h = -2s-2 "
      "gives -4, 0, -6, +2 at s = 1, -1, 2, -2",
      [(-2 * s - 2) for s in (1, -1, 2, -2)] == [-4, 0, -6, 2])

# The operator identity q(id) = -hbar (Upsilon + 2) on twistor monomials.
# Monomials in Z^0..Z^3 as exponent tuples; Zbar_a = -hbar d/dZ^a, hbar = 1.
def mono_mul_Z(a, f):
    """Multiply by Z^a."""
    out = {}
    for ex, c in f.items():
        ex2 = list(ex); ex2[a] += 1
        out[tuple(ex2)] = out.get(tuple(ex2), Fraction(0)) + c
    return out


def mono_deriv(a, f):
    """d/dZ^a."""
    out = {}
    for ex, c in f.items():
        if ex[a] == 0:
            continue
        ex2 = list(ex); ex2[a] -= 1
        out[tuple(ex2)] = out.get(tuple(ex2), Fraction(0)) + c * ex[a]
    return out


def mono_add(f, gg, scale=Fraction(1)):
    out = dict(f)
    for ex, c in gg.items():
        out[ex] = out.get(ex, Fraction(0)) + scale * c
    return {ex: c for ex, c in out.items() if c != 0}


def q_id(f):
    """q(id) f = (1/2) sum_a (Z^a Zbar_a + Zbar_a Z^a) f, Zbar_a = -d/dZ^a."""
    out = {}
    for a4 in range(4):
        t1 = mono_mul_Z(a4, mono_deriv(a4, f))          # Z^a d_a f
        t2 = mono_deriv(a4, mono_mul_Z(a4, f))          # d_a (Z^a f)
        out = mono_add(out, mono_add(t1, t2), Fraction(-1, 2))
    return out


from itertools import product as iproduct
ok = True
for ex in iproduct(range(4), repeat=4):
    D = sum(ex)
    if D > 3:
        continue
    f = {tuple(ex): Fraction(1)}
    expect = {tuple(ex): Fraction(-(D + 2))}
    ok = ok and q_id(f) == expect
g.check("prop:homogeneity: q(id) = -hbar(Upsilon + 2) as an operator identity "
      "on all twistor monomials of degree <= 3 (so helicity s hbar <=> "
      "homogeneity -2s-2)", ok)

# For Bose-Einstein detailed balance we need the RECIPROCAL Boltzmann factor;
# to keep x's meaning fixed (x = e^{-beta omega} throughout), write it as 1/x.
# (The Fermi-Dirac form n/(1-n) = x is the thm:istate(3) check above; it is
# not re-counted here.)
NBE = g.RF1 / (g.RF1 / x - g.RF1)          # N = 1/(e^{+beta omega} - 1)
g.check("prop:planck(2) / greybody n_-: Bose-Einstein detailed balance "
      "nbar/(1+nbar) = e^{-beta omega} as a rational-function identity "
      "(applied at omega = eps m for the ladder's current occupancy; nbar, "
      "not N, which is the number operator in the paper)",
      (NBE / (g.RF1 + NBE)).eqrf(x))

# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------

print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    raise SystemExit(1)
print("All checks pass.")
