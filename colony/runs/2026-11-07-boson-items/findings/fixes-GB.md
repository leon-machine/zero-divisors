# Fixes, attacker GB (fix round)

check4: pending (orchestrator). runcheck: both proposals pass (quasi-spins 5/5 in about 11 s; density 4/4 in under 1 s).
No rebuttals: every referee point was accepted.

## 1. synthesis.helicity-one-pair-modes-on-a-null-generator-are-quasi-spins (SOUND WITH FIXES)
- Title: now "Helicity-one pair modes on a null generator are quasi-spins, not exact bosons". The id is unchanged.
- (KF) scope, applied at every level (formal (v), Reading, technical, lay, one-liner, extraction note). The exclusion
  now holds only for the tower's positive adjoint. The referee's counter-model is stated and proved in (v) and in its
  proof: two modes, eta = 1 - 2 n_2, X = a_1* a_2, Omega = mode 1 filled and mode 2 empty, X Omega = 0,
  eta X* eta = -X*, [X, eta X* eta] Omega = -Omega. So (v) does not exclude (KF); this cites
  synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts (ii).
- (v) now says that the positivity fact holds for every element of every algebra with a positive state, which is why
  Gupta and Bleuler need an indefinite form.
- Proof of (iv): the false sentence is replaced by the referee's wording. The target mode c_{k+q}(t_s) stays filled
  because negative-momentum modes change only in the directions u_{s'}, which are orthogonal to every t_s.
- Credits, per the overlap rulings:
  - (i) is labelled the level-one u(n) current algebra on a window, with (ii) its corollary; "new" is kept only for the
    window and matrix statements.
  - The window identity cites synthesis.density-modes-bosonise-only-along-one-null-direction (i).
  - The rotation is the mode rotation U(theta) = exp(theta J sum w n) of
    synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (i).
  - The unit J is justified by synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower.
  - The contraction is cross-cited to synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators (v).
    For uniform smearing over L generators, |B^p Omega|^2 = (p!)^2 C(qL, p)/L^p, which tends to p! q^p. This replaces
    the earlier "contraction reading is argued".
  - All sibling proposals are cited in plain text.
- Check additions:
  - The rank-two helicity-one case on four channels from the referee's own computation (K = [[1, J], [0, 2]], q = 1:
    1, 6, 16, 0), so the check no longer uses rank-one M only.
  - The Krein counter-model (eta^2 = 1, eta* = eta, Krein adjoint = -X*, X P = 0, [X, X^dag] P = -P).
  - coverage.yaml updated to match.

## 2. synthesis.density-modes-bosonise-only-along-one-null-direction (OVERSTATED, restated)
- Title: "Window density forms are strip differences; total densities of uniform seas carry none" (86 characters). The
  referee's wording is 99 characters, over the E124 limit of 90, so it was shortened with the same content. The id is
  kept, as allowed.
- (i) is extended to unequal shifts, as the overlap ruling asks:
  [rho_m(M), rho_l(M')] = sum_{k,k+m,k+m+l in W} a*_k M M' a_{k+m+l} - sum_{k,k+l,k+l+m in W} a*_k M' M a_{k+l+m}
  for all shifts m, l in Z^d (both signs), with rho_m(M)* = rho_{-m}(M*). The equal-shift form and the strip form follow
  from it. It is proved via S_m S_l and checked in the algebra for five (m, l) pairs and three array pairs with J
  entries.
- (ii) is restated per q:
  - The uniform sea (one filled channel state per momentum) is covered at every q.
  - A bounded sea is covered only for the q at which it is clear of the strips. The referee's example
    (d = 1, N = 3, F = {-2, -1, 0}: 0, 1, 1) is in the text and the check.
  - Added: forms at q != q' vanish in momentum-diagonal states (proved from the general identity, checked), so "no
    canonical pair" now concerns total densities only.
  - Added: channel-resolved densities can carry a pair (each chirality of the 1+1 sea; the spin-resolved density of
    the 3+1 sea).
- (iii) now records the counterexamples: quadrant 3 at (1, 0) and 5 at (1, 1); tilted half-space 5 at (1, 0). Both are
  checked by counting. A half-space is said to single out a sharp value, not a nonzero one.
- (iv): added omega([rho_q(P_+), rho_q(P_+)*]) = S/2 (proved; d = 1 value q checked in the algebra). The (2N)^(d-1)
  growth is now called the transverse mode count, with the per-transverse-momentum value in (q(N - q)/N, 2q]. The
  proof writes Q(k-hat) = 1, per house style.
- Reading, technical, lay and one-liner are rewritten to the referee's true statement:
  - "sharp" replaces "only".
  - "total densities" is used where it applies.
  - The approximate Fermi-surface patch case is mentioned.
  - The referee's floating-point relative defect for the spin-resolved 3+1 density is mentioned as a numerical
    observation, not part of the proof.
  - "not propagating 3 + 1 bosons" is replaced by "whether propagating 3 + 1 bosons arise is not addressed".
- Extraction credits: (iii) is credited as the finite-window form of the leading patch commutator (Haldane; Houghton
  and Marston; Castro Neto and Fradkin; from memory). (ii) is credited to Mattis and Lieb (stored imported Fact,
  clause (ii)). (iv) is credited to the classical quadratic divergence of the 3+1 Schwinger term (Schwinger 1959,
  stored clause (iii)). All are prior art, not premises. "Nonzero only through a half-space" is dropped.
- coverage.yaml updated to match.

## Gate fix (W413 on the quasi-spins proposal)
check_sea_annihilates_and_forms_are_nonnegative now asserts values stated by hand:
- A table of (q, q tr(M M*)) for the six samples: (1, [1, 1, 1, 1, 2, 2]) and (2, [2, 2, 2, 2, 4, 4]). It compares
  ω(ρρ*), ω([ρ, ρ*]) and −ω_reversed([ρ, ρ*]) with these values, plus ω(ρ*ρ) = 0.
- That ρ* does not annihilate the sea and ρ does not annihilate the reversed sea.
- The Krein modes taken from the window (the top sea mode and the next), not from literals.
- [X, X*] = +1 on |1, 0⟩ (positive adjoint).
- ‖X†Ω‖² = 1 and Krein norm ⟨X†Ω, ηX†Ω⟩ = −1.

The default literal F(0) in the trace lookup is gone. I perturbed seven literals by hand and every perturbation fails.
runcheck: 5/5 pass. check4: pending (orchestrator).
