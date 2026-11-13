"""Claim 1 (ii): which groups of 'symmetries of the step' make the invariant extension unique?
Route (G), own helpers. For each group we solve the linear system
   lambda = omega on old blades,  lambda(g x) = lambda(x) for generators g of the group,
optionally with reality lambda(x^dagger) = lambda(x), and report the dimension of the affine solution
space (0 = unique). Then: is Omega_{1/2} a solution, is Omega_{1/3}, and is there an invariant state that is
sharp (pure) on the new rung?"""
from myalg import *

def run(l, odd_old):
    n = l + 1
    new_e, new_f = l, n + l
    allb = blades_of(range(2 * n))
    idx = {b: i for i, b in enumerate(allb)}
    oldgens = [j for j in range(l)] + [n + j for j in range(l)]
    oldb = blades_of(oldgens)
    # old state: product over old rungs of (1 + a e_j + b p_j)/2, p_j = f_j e_j
    rho = {(): F(1)}
    for j in range(l):
        a = F(1, 3) if (odd_old and j == 0) else F(0)
        b = F(1, 2) - F(j, 7)
        pj = M(Fg(j, n), E(j, n), n=n)
        rho = M(rho, GA.add({(): F(1, 2)}, GA.scal(a / 2, E(j, n)), GA.scal(b / 2, pj)), n=n)
    def om(x):
        return scalar(M(rho, x, n=n)) / scalar(rho)
    Gam_old = {(): F(1)}
    for j in range(l):
        Gam_old = M(Gam_old, Fg(j, n), E(j, n), n=n)
    u_refl = M(E(l, n), Gam_old, n=n)
    u_rot = GA.add({(): F(3, 5)}, GA.scal(F(4, 5), M(Fg(l, n), Gam_old, n=n)))
    for u in (u_refl, u_rot):
        assert GA.eq(M(u, adj(u, n), n=n), {(): F(1)})                      # unitary for (P)
        assert all(GA.eq(M(u, {b: F(1)}, n=n), M({b: F(1)}, u, n=n)) for b in oldb)  # centralises A_l
    def vmap(img):
        return lambda b: apply_vector_map(img, b, n)
    def ad(u):
        ui = adj(u, n)
        return lambda b: M(u, {b: F(1)}, ui, n=n)
    sig_e = vmap({new_e: {(new_e,): F(-1)}})
    sig_f = vmap({new_f: {(new_f,): F(-1)}})
    joint = vmap({new_e: {(new_e,): F(-1)}, new_f: {(new_f,): F(-1)}})
    boost = vmap({new_e: {(new_e,): F(5, 4), (new_f,): F(3, 4)}, new_f: {(new_e,): F(3, 4), (new_f,): F(5, 4)}})
    # the boost really is an isometry of the plane
    be = boost((new_e,)); bf = boost((new_f,))
    assert GA.eq(M(be, be, n=n), {(): F(1)}) and GA.eq(M(bf, bf, n=n), {(): F(-1)})
    assert GA.is_zero(GA.add(M(be, bf, n=n), M(bf, be, n=n)))
    # boost does not commute with the adjoint (so it is excluded by the authors' definition)
    assert not GA.eq(adj(boost((new_e,)), n), boost((new_e,))) or not GA.eq(adj(bf, n), GA.neg(bf))
    groups = {
        "authors {s_e, s_f}": [sig_e, sig_f],
        "O(1,1)(Q): s_e, s_f, boost": [sig_e, sig_f, boost],
        "inner, adjoint-preserving: Ad(e Gam), Ad(3/5+4/5 f Gam)": [ad(u_refl), ad(u_rot)],
        "inner rotations only: Ad(3/5+4/5 f Gam)": [ad(u_rot)],
        "exchange s_f alone": [sig_f],
        "s_e alone": [sig_e],
        "joint flip s_e s_f alone": [joint],
        "switch-preserving: boost + joint flip": [boost, joint],
    }
    def solve(gs, real, extra=None):
        rows, rhs = [], []
        N = len(allb)
        for b in oldb:
            r = [F(0)] * N; r[idx[b]] = F(1); rows.append(r); rhs.append(om({b: F(1)}))
        for g in gs:
            for b in allb:
                r = [F(0)] * N
                for bb, c in g(b).items():
                    r[idx[bb]] += c
                r[idx[b]] -= 1
                rows.append(r); rhs.append(F(0))
        if real:
            for b in allb:
                s = adj({b: F(1)}, n)[b]
                if s != 1:
                    r = [F(0)] * N; r[idx[b]] = F(1); rows.append(r); rhs.append(F(0))
        if extra is not None:
            r = [F(0)] * N
            for bb, c in extra[0].items():
                r[idx[bb]] += c
            rows.append(r); rhs.append(extra[1])
        rk = rank(rows)
        rk_aug = rank([r + [c] for r, c in zip(rows, rhs)])
        return (N - rk) if rk == rk_aug else None
    def omega_t(t):
        # product extension: Omega_t(a + b e + c f + d p) = om(a) + (2t-1) om(d); here on blades
        p = M(Fg(l, n), E(l, n), n=n)
        def Om(x):
            tot = F(0)
            for b, c in x.items():
                hasE, hasF = new_e in b, new_f in b
                rest = tuple(i for i in b if i not in (new_e, new_f))
                if not hasE and not hasF:
                    tot += c * om({b: F(1)})
                elif hasE and hasF:
                    # b = sign * rest * p  ; find sign
                    prod = M({rest: F(1)}, p, n=n)
                    sgn = prod[b] if b in prod else None
                    assert sgn is not None
                    tot += c * (2 * t - 1) * om({rest: F(1)}) / sgn
            return tot
        return Om
    print(f"--- l = {l} (old rungs), old state {'with odd part' if odd_old else 'even'}")
    for name, gs in groups.items():
        d0 = solve(gs, False); d1 = solve(gs, True)
        on = M(V(l, n), W(l, n), n=n)
        forced = solve(gs, True, (on, F(1, 3))) is None
        inv = {}
        for t in (F(1, 2), F(1, 3)):
            Om = omega_t(t)
            inv[t] = all(Om(g(b)) == Om({b: F(1)}) for g in gs for b in allb)
        print(f"  {name:58s} free params: {d0} (no reality), {d1} (with reality);"
              f" Omega_1/2 inv: {inv[F(1,2)]}, Omega_1/3 inv: {inv[F(1,3)]}; weight on 'on' forced to 1/2: {forced}")
    return groups, n, allb, om

for l in (0, 1, 2):
    run(l, odd_old=True)

# sharp invariant extension under the exchange s_f alone: Omega = omega (x) state of (1+e)/2 on the new rung
print("--- a sharp extension invariant under s_f alone (old state even, so densities commute)")
for l in (0, 1, 2):
    n = l + 1
    rho = {(): F(1)}
    for j in range(l):
        rho = M(rho, GA.add({(): F(1, 2)}, GA.scal(F(1, 4) + F(j, 9), M(Fg(j, n), E(j, n), n=n))), n=n)
    dens_new = GA.add({(): F(1, 2)}, GA.scal(F(1, 2), E(l, n)))
    R = M(rho, dens_new, n=n)
    Om = lambda x: scalar(M(R, x, n=n)) / scalar(R)
    allb = blades_of(range(2 * n))
    G = [[Om(M({a: F(1)}, adj({b: F(1)}, n), n=n)) for b in allb] for a in allb]
    real = all(Om(adj({b: F(1)}, n)) == Om({b: F(1)}) for b in allb)
    sigf = lambda b: apply_vector_map({n + l: {(n + l,): F(-1)}}, b, n)
    sige = lambda b: apply_vector_map({l: {(l,): F(-1)}}, b, n)
    inv_f = all(Om(sigf(b)) == Om({b: F(1)}) for b in allb)
    inv_e = all(Om(sige(b)) == Om({b: F(1)}) for b in allb)
    on = M(V(l, n), W(l, n), n=n)
    print(f"  l={l}: state under (P): {is_psd(G) and real}; s_f-invariant: {inv_f}; s_e-invariant: {inv_e};"
          f" weight on 'on': {Om(on)}; value on e_new: {Om(E(l, n))}; new-rung density (1+e)/2 idempotent:"
          f" {GA.eq(M(dens_new, dens_new, n=n), dens_new)}")
