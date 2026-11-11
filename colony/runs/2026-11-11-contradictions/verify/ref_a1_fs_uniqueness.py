#!/usr/bin/env python3
"""Referee check for A1, by an independent route (written before reading the author's script).

Exact arithmetic throughout (Fractions via GA.py, jets via gtg.py).

Part 1. Pointwise algebra of A_rho = Omega - u ^ E,  u = ninf - rho n0, E = hb^{-1}(a), in Cl(2,4).
Part 2. Field strength of A_rho computed from jets on actual fields (de Sitter, FLRW fluids, Schwarzschild),
        compared with -(calR - 2 rho id) in the store's sign; kernel ranks.
Part 3. Common kernel of the curvature on the tractor fibre, and the full parallel-tractor count.
Part 4. The mirror: Cl(2,4) against Cl(4,2), two ways of renormalising the null pair.
Part 5. Torsion: a pointwise counterexample to "L kernel-free => mu = 0".
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA
import gtg
from gtg import m_add, m_neg, m_sub, m_scal, comm, m_d, m_val, S24, S13

check = GA.check
S42 = tuple(-s for s in S24)
n0, ninf = gtg.null_pair(S24)
e = GA.gen


def vec(*c):
    return {(i,): F(x) for i, x in enumerate(c) if x}


def lorentz_biv(cs):
    out = {}
    k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if cs[k]:
                out = GA.add(out, GA.scal(cs[k], GA.mul(e(i), e(j), S24)))
            k += 1
    return out


def dot(x, y, sq=S24):
    return GA.dot(x, y, sq)


def u_of(rho):
    return GA.sub(ninf, GA.scal(rho, n0))


def I_of(rho):
    return GA.add(ninf, GA.scal(rho, n0))


def A_rho(Om, E, rho, sq=S24):
    return GA.sub(Om, comm(u_of(rho), E, sq))   # u ^ E = u x E since u . E = 0


# ---------------- Part 1 ----------------
Om = lorentz_biv([F(3, 7), F(-2), F(5, 3), F(1, 4), F(-6, 5), F(2)])
Avec = vec(2, F(-1, 3), F(5, 2), 7)
Bvec = vec(F(-4, 9), 1, 0, F(3, 2))
mu = vec(F(1, 5), 3, F(-2), F(7, 3))
for rho in (F(0), F(1, 3), F(-5, 2), F(7)):
    u, I = u_of(rho), I_of(rho)
    lhs = comm(GA.outer(u, Avec, S24) if hasattr(GA, 'outer') else comm(u, Avec, S24), comm(u, Bvec, S24), S24)
    lhs = comm(comm(u, Avec, S24), comm(u, Bvec, S24), S24)
    check(f"P1 rho={rho}: (u^A)x(u^B) = 2 rho A^B", GA.eq(lhs, GA.scal(2 * rho, comm(Avec, Bvec, S24))))
    A = A_rho(Om, Avec, rho)
    check(f"P1 rho={rho}: A_rho x I_rho = 0 (any Omega, any frame)", GA.is_zero(comm(A, I, S24)))
    sgm, tau = F(5, 3), F(-2, 7)
    W = GA.add(GA.scal(sgm, ninf), GA.scal(tau, n0))
    check(f"P1 rho={rho}: A_rho x (s ninf + t n0) = (t - rho s) E",
          GA.eq(comm(A, W, S24), GA.scal(tau - rho * sgm, Avec)))
    # action on the mu slot: Omega.mu (spacetime) minus (E.mu) u
    exp = GA.sub(comm(Om, mu, S24), GA.scal(dot(Avec, mu), u))
    check(f"P1 rho={rho}: A_rho x mu = Omega x mu - (E.mu) u", GA.eq(comm(A, mu, S24), exp))
    check(f"P1 rho={rho}: Q(I)=2rho, Q(u)=-2rho, u.I=0, <X,cI>=c",
          dot(I, I) == 2 * rho and dot(u, u) == -2 * rho and dot(u, I) == 0
          and dot(n0, GA.scal(F(9, 4), I)) == F(9, 4))


# ---------------- Part 2: field strengths on fields ----------------
def fs_connection(fld, rho):
    """A_rho(e_mu) as jets in the conformal algebra."""
    u = u_of(rho)
    return [m_sub(fld.Om[m], comm(u, fld.g[m], S24)) for m in range(4)]


def fs_strength_frame(fld, rho):
    """F(hb(gamma_a) ^ hb(gamma_b)) on the frame planes (values)."""
    A = fs_connection(fld, rho)
    Fb = {}
    for m in range(4):
        for n in range(m + 1, 4):
            Fb[(m, n)] = m_val(m_add(m_d(A[n], m), m_neg(m_d(A[m], n)), comm(A[m], A[n], S24)))
    Hi = fld.hb_matrix()
    out = {}
    for a in range(4):
        for b in range(a + 1, 4):
            acc = {}
            for (m, n), Fm in Fb.items():
                c = Hi[m][a] * Hi[n][b] - Hi[n][a] * Hi[m][b]
                if c and Fm:
                    acc = m_add(acc, m_scal(c, Fm))
            out[(a, b)] = acc
    return out


def store_curv(fld):
    return {k: m_val(v) for k, v in fld.curvature().items()}


def kernel_dim_L(Lop):
    """dim of {v : L(X).v = 0 for all frame planes X} (spacetime vectors)."""
    rows = []
    blades = GA.all_blades(6)
    for i in range(4):
        v = e(i)
        col = []
        for k in sorted(Lop):
            col += GA.basis_vector_of(comm(Lop[k], v, S24), blades)
        rows.append(col)
    return 4 - GA.rank_of_vectors(rows)


def fibre_kernel_dim(Fop):
    blades = GA.all_blades(6)
    rows = []
    for i in range(6):
        col = []
        for k in sorted(Fop):
            col += GA.basis_vector_of(comm(Fop[k], e(i), S24), blades)
        rows.append(col)
    return 6 - GA.rank_of_vectors(rows)


def compare(fld, rho, label):
    Fop = fs_strength_frame(fld, rho)
    R = store_curv(fld)
    ok = True
    for (a, b), Fv in Fop.items():
        X = GA.mul(e(a), e(b), S24)
        target = m_neg(m_sub(R[(a, b)], m_scal(2 * rho, X)))   # -(calR - 2 rho) X
        if not GA.eq(Fv, target):
            ok = False
    check(f"P2 {label}: F_FS(hb X) = -(calR - (Lambda/3)) X, Lambda = 6 rho, Lorentz block only", ok)
    return Fop


# de Sitter, flat slicing, H = 1/2: Lambda = 3/4, rho = 1/8. F must vanish.
H = F(1, 2)
ds = gtg.de_sitter_flat(H, F(1), order=2)
Fds = compare(ds, H * H / 2, "de Sitter H=1/2, same Lambda")
check("P2 de Sitter at the same Lambda: F_FS = 0, fibre kernel 6 (all tractors flat)",
      all(GA.is_zero(v) for v in Fds.values()) and fibre_kernel_dim(Fds) == 6)
Fds2 = compare(ds, F(1, 3), "de Sitter H=1/2, other rho=1/3")
print("    de Sitter at a different rho: kernel of L =", kernel_dim_L(Fds2))
check("P2 de Sitter at another rho: L = -(Lambda_dS/3 - 2rho) id, no kernel", kernel_dim_L(Fds2) == 0)

# FLRW perfect fluids.  kappa rho_m := 8 pi G rho_m. H0 = 1, Lambda = 3/2 -> kappa rho_m = 3 - 3/2 = 3/2.
H0, Lam = F(1), F(3, 2)
krho = 3 * H0 ** 2 - Lam
for w, expect in ((F(0), 0), (F(1, 3), 0), (F(1), 0), (F(-1, 3), 1), (F(-1), 0), (F(-2, 3), 0)):
    addot = -krho * (1 + 3 * w) / 6 + Lam / 3          # a = 1 at the instant
    fl = gtg.flrw_flat(1, H0, addot)
    Fop = compare(fl, Lam / 6, f"FLRW w={w}")
    kd = kernel_dim_L(Fop)
    check(f"P2 FLRW w={w}: kernel of de Sitter-subtracted L has dim {expect} (found {kd}); fibre kernel {2 + kd}",
          kd == expect and fibre_kernel_dim(Fop) == 2 + kd)
    # same field, normal tractor connection: Weyl = 0, so the stored Weyl condition fails everywhere
    # (conformally flat): the stored theorem gives no uniqueness on FLRW at all.
# vacuum: rho_m = 0 with Lambda: de Sitter, kernel 4 (already above)

# Schwarzschild in Kerr-Schild form, Lambda = 0, rho = 0: L = -W, kernel 0 (stored Weyl condition).
sch = gtg.schwarzschild_ks(F(1), (F(0), F(3), F(4), F(12)), order=2)
Fsch = compare(sch, F(0), "Schwarzschild KS M=1 at r=13, rho=0")
W = gtg.weyl_op(store_curv(sch))
Wm = {k: m_neg(m_val(v)) for k, v in W.items()}
check("P2 Schwarzschild: F_FS = -Weyl on frame planes (Einstein field at the same Lambda)",
      all(GA.eq(Fsch[k], Wm[k]) for k in Fsch))
check("P2 Schwarzschild: no kernel vector (rank 4), fibre kernel 2", kernel_dim_L(Fsch) == 0 and fibre_kernel_dim(Fsch) == 2)
# Schwarzschild with a nonzero rho (Lambda mismatch): L = -W + 2 rho id: still kernel-free here
Fsch2 = compare(sch, F(1, 10), "Schwarzschild with rho=1/10 (field not Einstein at that Lambda)")
print("    kernel dim at mismatched rho:", kernel_dim_L(Fsch2))


# ---------------- Part 3: the parallel condition, derivative step ----------------
# With mu = 0 near the point, D_a V = (a.grad s) ninf + (a.grad t) n0 + (t - rho s) E(a).  Checked
# pointwise in Part 1 (A_rho x (s ninf + t n0) = (t - rho s) E).  Since E is injective (invertible region),
# s, t constant and t = rho s.  No use of rho != 0 anywhere.
check("P3 rho = 0 case: I_0 = ninf parallel, same argument (no rho != 0 needed)",
      GA.is_zero(comm(A_rho(Om, Avec, F(0)), ninf, S24)))


# ---------------- Part 4: the mirror ----------------
Bgen = GA.add(Om, GA.scal(F(2, 3), GA.mul(e(1), e(4), S24)), GA.scal(F(-5), GA.mul(e(4), e(5), S24)),
              GA.scal(F(1, 7), GA.mul(e(0), e(5), S24)))
Vgen = GA.add(vec(1, 2, -3, F(1, 2)), GA.scal(F(4), e(4)), GA.scal(F(-1, 3), e(5)))
check("P4 a bivector acts with opposite sign in Cl(4,2): B x' V = -(B x V)",
      GA.eq(comm(Bgen, Vgen, S42), GA.neg(comm(Bgen, Vgen, S24))))
rho = F(3, 5)
A = A_rho(Om, Avec, rho)
# Convention (ii): keep X = n0, flip ninf.  Reversed tower's FS form with Omega' = -Omega, rho' = -rho.
n0b, ninfb, rhob = n0, GA.neg(ninf), -rho
check("P4(ii) n0' . ' ninf' = 1 in Cl(4,2)", GA.dot(n0b, ninfb, S42) == 1)
ub = GA.sub(ninfb, GA.scal(rhob, n0b))
Ab = GA.sub(GA.neg(Om), comm(ub, Avec, S42))
check("P4(ii) reversed FS form A' = -A_rho as an element, so the same covariant derivative",
      GA.eq(Ab, GA.neg(A)) and GA.eq(comm(Ab, Vgen, S42), comm(A, Vgen, S24)))
Ib = GA.add(ninfb, GA.scal(rhob, n0b))
check("P4(ii) reversed frozen point I' = -I_rho, <X,I'>' = 1, Q'(I') = 2 rho' = -2 rho",
      GA.eq(Ib, GA.neg(I_of(rho))) and GA.dot(n0b, Ib, S42) == 1 and GA.dot(Ib, Ib, S42) == -2 * rho)
check("P4(ii) soldering A' x' X' = E (same as A x X)", GA.eq(comm(Ab, n0b, S42), Avec) and GA.eq(comm(A, n0, S24), Avec))
# Convention (i), the author's: flip n0, keep ninf: u and I_rho unchanged as vectors.
n0a, ninfa = GA.neg(n0), ninf
check("P4(i) n0'.'ninf' = 1", GA.dot(n0a, ninfa, S42) == 1)
ua = GA.sub(ninfa, GA.scal(rhob, n0a))
check("P4(i) u' = u and I' = I_rho as vectors", GA.eq(ua, u_of(rho)) and GA.eq(GA.add(ninfa, GA.scal(rhob, n0a)), I_of(rho)))
Aa = GA.sub(GA.neg(Om), comm(ua, Avec, S42))
same_op = GA.eq(comm(Aa, Vgen, S42), comm(A, Vgen, S24))
check("P4(i) the reversed FS form is NOT the same operator as A_rho", not same_op)
Aflip = GA.add(Om, comm(u_of(rho), Avec, S24))   # A_rho with E -> -E
check("P4(i) it is A_rho with the frame reversed, E -> -E", GA.eq(comm(Aa, Vgen, S42), comm(Aflip, Vgen, S24)))
I4 = GA.mul(GA.mul(e(0), e(1), S24), GA.mul(e(2), e(3), S24), S24)
I4inv = GA.neg(I4)   # I4^2 = -1
conj = GA.mul(GA.mul(I4, A, S24), I4inv, S24)
check("P4(i) related to A_rho by Ad(I4) (-1 on spacetime vectors, +1 on the added plane), which fixes I_rho",
      GA.eq(conj, Aflip) and GA.eq(GA.mul(GA.mul(I4, I_of(rho), S24), I4inv, S24), I_of(rho)))
check("P4(i) soldering A' x' X' = E in its own convention", GA.eq(comm(Aa, n0a, S42), Avec))


# ---------------- Part 5: torsion ----------------
# F = L - u ^ T (Lorentz block L, torsion block T(X)); F x V = L(X).mu - u (T(X).mu) + T(X) (u.V).
# Choose T(X) := -(L(X).mu0)/c with c = u.V0: then V0 = mu0 + (s ninf + t n0), t - rho s = c, is in the
# pointwise common kernel although L has no kernel vector.
Fl = fs_strength_frame(fl, Lam / 6) if False else None
fl0 = gtg.flrw_flat(1, H0, -krho / 6 + Lam / 3)          # dust, L kernel-free
L0 = fs_strength_frame(fl0, Lam / 6)
rho = Lam / 6
mu0 = vec(1, F(1, 2), F(-1, 3), 2)
s, c = F(2), F(1)
t = c + rho * s
V0 = GA.add(mu0, GA.scal(s, ninf), GA.scal(t, n0))
Ft = {}
for k, Lk in L0.items():
    Tk = GA.scal(F(-1) / c, comm(Lk, mu0, S24))        # Lk x mu0 = Lk . mu0
    Ft[k] = GA.sub(Lk, comm(u_of(rho), Tk, S24))
check("P5 with torsion T = -(L.mu0)/c, V0 (mu0 != 0) is in the curvature kernel though L has no kernel",
      kernel_dim_L(L0) == 0 and all(GA.is_zero(comm(Fk, V0, S24)) for Fk in Ft.values()))

print("FAILURES:", GA.FAILURES)
