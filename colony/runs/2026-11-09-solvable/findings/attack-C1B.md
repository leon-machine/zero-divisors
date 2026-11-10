# Attack C1B (cluster C1, angle B: cross-pollinating and adversarial)

Status: attack round done. One proposal filed (T1). T2 and T3: nothing filed, reasons below.

## Target 1: op.wall-class-invariant (attack item 1: indefinite sides, dimension at least four)

Orientation. The store's k(Sigma) (synthesis.wall-rung-count-is-height-of-dying-line-class v2): least k with a
k-rung completion; necessity clause (1): a k-rung completion gives a rank k-1 bundle N with
N(Gbar) + L + N = N(Gbar) + R^k (an isomorphism of actual bundles). e(L) is the least k with L inside a trivial R^k,
an unstable embedding question. On a definite side N(Gbar) = 0 and clauses (1), (2) give k = e(L).

Routes considered.
- R1 (the lead: Adams on RP^n walls). Fails: on RP^n the only nontrivial line bundle is the tautological one, and there
  ht(x) = e(L) = n+1 (w(N) = (1+x)^{-1} forces rank N >= n), so k = n+1 on every side for every n. Adams' theorem
  (stable triviality of mL; 16 against 32 at n = 9) concerns multiples mL, which the rung count of an RP^n wall never
  asks about. Verdict (argued, elementary; recorded in the proposal's extraction note, not filed separately): Adams'
  RP^n theorem is irrelevant to the store's k. C1A reached the same verdict independently.
- R2 (other subject: K-theory of the dying line). Chosen. Any k-rung completion gives, by complexifying clause (1) and
  using lambda_t, (1 - xi)^k = 0 in K(Sigma), xi = complexified L; since xi^2 = 1, (1-xi)^k = 2^{k-1}(1-xi). So
  k >= 1 + log_2 ord(1 - xi), on EVERY side. This is where Adams-type input really enters: a stable obstruction, not
  the stable-range step.
- R3 (own: explicit family). Chosen with R2. Lens-space walls L^{2n+1}(4) with the order-2 dying line: x != 0 = x^2
  (ht = 2) in every dimension, while ord(1 - xi) grows with n.

Kill condition (pre-registered before computing): dies if (a) 2(1 - chi^2) lies in the ideal (chi^4 - 1, (chi-1)^4)
(exact lattice test), or (b) the method fails to reproduce the stored L(4,1) result (obstruction must vanish at n = 1),
or (c) no tame wall with cross-section L^7(4), dying line L and an indefinite side exists. Did not fire: (a) 2(1-chi^2)
is not in the lattice at n = 3; (b) it is at n = 1 and 2; (c) explicit walls built and checked.

Established (labelled):
- Proved (given classical inputs cited from memory: K-ring of lens spaces via the equivariant Thom isomorphism and
  Gysin sequence; lambda-operations; Sq^1 = 0 on classes lifting to Z4): clause (1) above, on every side.
- Proved: on L^{2n+1}(4), x^2 = 0 (ht = 2) and, via the ring map chi -> I = e1e2 to Z[I]/(pi^{n+1}), pi = I - 1,
  k >= 1 + floor(n/2) for every n. So k - ht is unbounded.
- Computed (exact lattice, n = 1..8): ord(1 - chi^2) = 2^{floor((n+1)/2)}, so k >= 1 + floor((n+1)/2): k >= 3 on L^7(4),
  4 on L^11(4), 5 on L^15(4). Beyond n = 8 the formula is computed only to n = 15 in work/C1B/klens.py (conjecture for
  all n). Control: the same code gives 2^n for chi - 1 on RP^{2n+1}.
- Proved and checked: for n odd, tame walls on L^{2n+1}(4) x R with either physical side ((2n+1,1) or (2n+2,0)): the
  field f(q) = e3e1 q on the unit sphere of H^r, which anticommutes with the generator B = e2e3, spans the twisted line
  inside T*Sigma; cometric (A - (1-t) A(pi_f., pi_f.)) perp (eps dt^2).
- Not established: the exact k of any lens wall of dimension >= 7 (only k >= bound and k <= e <= dim + 1); anything on
  L^5(4) from complex K (no obstruction there; C1A's spin class q1 does obstruct there, see below).

Proposal: synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height (filed; check4 0 errors 0 findings;
validate ok, findings [] apart from info I305).
Problem stays partial: exact rung counts and the deciding datum (conjecturally a KO-theoretic geometric dimension of
-L, stable range permitting) are open.

Overlap with C1A: C1A plans k >= 3 on L^5(4) and L^7(4) via the spin class q1(L + L) = 2y^2, and the comparison wall
L(4,1) x T^4 (the success clause's "not determined by" branch). I dropped my own comparison wall (L(4,1) x S^4, same
idea) and kept only the general K obstruction and the growing family; C1A explicitly left the K growth bound to C1B.
The two results agree at n = 3 and are complementary at n = 2 (q1 sees it, complex K does not).

Adversarial note for C1A's q1 argument (send to C1A / referees): q1 depends on the spin structure. To conclude that
L + L is stably nontrivial from q1(L + L) != 0 one must rule out that a stably trivial oriented bundle with a twisted
spin structure has the same q1. On a stably trivial bundle, the spin structure twisted by a in H^1(Sigma; Z2) has q1
pulled back from the fibre RP^infinity -> BSpin; through BZ2 -> BSpin(3) = BSU(2) this is +-c2(L_a tensor C + L_a
tensor C) = +-(beta a)^2, which vanishes on L^{2m+1}(4) because (beta x)^2 = 0 whenever x^2 = 0 (beta x = 2z, 4z = 0).
So the argument closes, but the step must be in the proof (argued here, from memory).
End-of-round reading: C1A filed synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial, whose clause (2)
requires q1 != 0 for EACH spin structure and clause (3) computes q1 = 2y^2 for both, which closes this gap. Overlap
with my proposal: both give k >= 3 on L^7(4) (by q1 there, by complex K here); C1A's also covers L^5(4) and the
k = e(L) definite-side remark; mine adds the general K obstruction 2^{k-1}(1 - xi) = 0 and the unbounded growth
k >= 1 + floor(n/2). If the orchestrator merges, keep mine's clauses (1), (2) growth and (3) walls for n odd as the
complement of C1A's.

## Target 2: op.helicity-per-boundary-mode (J3 at the horizon)

Routes and findings (adversarial; nothing filed, to avoid duplicating C1A's constructive GTG reduction, which already
pre-registers the main adversarial prediction):
- R1, the lead's uniform statement ("potential proportional to 1 - 2M/r, decaying as exp(2 kappa r_*)") fails for
  spin 1/2. Static-frame reduction: the rescaled spinor obeys a 2D Dirac equation in (t, r_*) with coupling
  W = sqrt(f) lambda / r, lambda = +-(j + 1/2); V_+- = W^2 +- dW/dr_*. Computed (work/C1B/dirac_rate.py, exact, with
  s = sqrt f, r = 2M/(1 - s^2)): V_+-/s -> +-lambda/(8 M^2) != 0 as s -> 0, so the spin-half potential is of exact order
  sqrt(f), decaying as exp(kappa r_*), half the integer-spin rate; the scalar V/f -> (l(l+1) + 1)/(4M^2), also massive.
  J3 still holds at the horizon (V -> 0), so this is a correction to the stored "known" text, not a failure of J3.
  The rate is the boost weight 1/2 of the stored spinor result (link below). Kill condition (pre-registered: dies if
  V_+-/sqrt f -> 0) did not fire. C1A's kill/prediction covers the same point; left to C1A.
- R2, massive fields: V = f(l(l+1)/r^2 + 2M/r^3 + mu^2) stays proportional to f; the massive Dirac coupling keeps the
  sqrt(f) factor. Mass does not break J3 at the horizon (argued; consistent with the stored "mass terms reach only the
  constraint" result).
- R3, spin 1 and 2: Regge-Wheeler (spin 1: f l(l+1)/r^2; spin 2: f(l(l+1)/r^2 - 6M/r^3)) and Zerilli potentials are
  proportional to f (from memory). No failure. But in the Teukolsky (Kinnersley-tetrad) form the spin-weight-s radial
  potential does not vanish at the horizon (solutions Delta^{-s} e^{-i omega r_*}, e^{+i omega r_*}): J3 is a statement
  about boost-weight-zero rescaled channels, and should say so (argued, from memory).
- R4 (own), non-uniformity in l: the region where channel l is free (V_l << omega^2) is r_* << (1/2 kappa)
  ln(omega^2 r_h^2 / l(l+1)) up to constants, which recedes to the horizon as l grows; no exterior region makes all
  channels two-dimensional at once. J3 holds channel by channel in the limit, not uniformly. At proper distance rho the
  free channels number about (A/4 pi)(omega/(kappa rho))^2, i.e. transverse modes per area at the local (Tolman)
  frequency: the per-light-ray count re-emerges from the channels (argued; possible bridge to C3's sea count).
Proposal: none (C1A covers the constructive proof and the spin-half rate; R2-R4 are argued from memory).

## Target 3: op.odd-towers attack item 1 (Fock ideals and mass formulas, dimensions 3 and 5)

Finding: answered in store. dark-tower-matter.constituents-field (proved) gives the ideals T, S with dimensions 4, 2
(n = 3, field R) and 16, 8 (n = 5, field H); dark-tower-matter.where-mass-begins (proved) gives the mass laws
m^2 = 2<x x^dagger>_0, x = psi_1~ psi_2 (n = 3, two constituents) and m^2 = (1/2)<x x^dagger>_0, x = psi~ psi
(n = 5, one constituent, massless on a proper cone). synthesis.gauge-algebra-by-tower takes exactly these (a, F) as
inputs, and the even conformal algebras agree: Cl+(3,2) = Cl+(2,3) = Cl(3,1) = M4(R), Cl+(5,2) = Cl+(2,5) = Cl(5,1) =
M4(H); the minimal ideal from 2 real null pairs (n = 3) is R^4 = 2^2, and from 2 real pairs plus the u-built third pair
(n = 5) is C^8 = H^4, matching b and K. Kill condition (pre-registered: a contradiction if the commutant differs from
K or the pair count from b) did not fire. No counter-model: the stored ideals cannot contradict the stored gauge
algebras, since the latter are computed from them. Proposal: none.

## Unexpected links
- The spin-half horizon decay rate exp(kappa r_*) is the boost weight 1/2 of
  synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays read in the radial equation (argued).
- T2 R4: the number of channels free at proper distance rho reproduces a per-area count at the local frequency;
  possible link to the light-ray sea of C3 (argued only).
- T1: the obstruction is K-theoretic (Adams-type) but lives in the torsion of lens spaces, not in Adams' RP^n theorem.

## Decisions for Leon
- Import as a Fact (for synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height): the complex K-ring of a
  lens space, K(S^{2n+1}/Z_m) = Z[chi]/(chi^m - 1, (chi - 1)^{n+1}) (Atiyah, K-Theory 1967, Section 2.7; Atiyah 1961;
  Kambe 1966), with the lambda-operations on K; and the Bockstein fact Sq^1 = 0 on mod-2 classes lifting to Z4
  (Hatcher 4.L). All cited from memory, unchecked against the sources.
- Problem record op.odd-towers: attack item 1 is answered by dark-tower-matter.constituents-field and
  dark-tower-matter.where-mass-begins; recommend moving it to "known" (same recommendation as C1A's kill route).
- Problem record op.helicity-per-boundary-mode: the "known" text says the potential is proportional to 1 - 2M/r for
  spins 0, 1/2, 1, 2; for spin 1/2 it is proportional to sqrt(1 - 2M/r) (decay exp(kappa r_*)). Recommend correcting
  the text whatever C1A files.
- Problem record op.wall-class-invariant: attack item 1 answered in the negative (k != ht on indefinite sides from
  dimension 7, unbounded excess); the open question becomes the exact count and its deciding datum.
