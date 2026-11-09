# Fixes C1A, run 2026-11-09-solvable

check4: pending (orchestrator). Only runcheck.py was run.

## synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (R1 section 1, SOUND WITH FIXES)
1. Classical inputs (L1)-(L3). Per FIXROUND override 1 these are not imported. Instead the formal level now opens
   "Given the classical facts (L1) to (L3) below, cited from memory and not in the store", and it lists them in full:
   - (L1): the cohomology rings and T Sigma + R = (m+1) eta;
   - (L2): q1 with 2q1 = p1, p1 = e^2, orientable iff w1 = 0, spin iff w2 = 0;
   - (L3): the K-ring, used only for the last sentence of (4).

   The formal level also says each clause that uses them is conditional on them. The proof's input paragraph says the
   same and adds (L2)'s orientable/spin clause. The extraction note says the result is conditional and that deriving
   (L1)-(L3) is an open item. The one-liner and lay level now say that classical facts are cited.
2. Whitney citation. The tools paragraph now cites synthesis.imported-whitney-product-formula-and-projective-space(i)
   for the multiplicativity of w, and sheaf.imported-real-line-bundles only for "equal w1 implies isomorphic". The
   Whitney Fact is added to `uses` at @1. Proof (2) now derives w(L + L) = (1 + x)^2 = 1 + x^2 from it. The check
   (check_spin_class_of_doubled_line_on_lens_spaces) calls premise() on it and asserts w(L + L) = [1, 0, 1] mod 2.
3. "The datum that decides" is gone from formal (4) and proof (4). Formal (4) now reads: "A necessary condition for two
   rungs is that L + L be stably trivial; on L^5(4) it fails, detected by q1 = 2y^2." The technical level and the
   extraction note now say that only necessity is proved.
4. The beta x wording is corrected in formal (4) and proof (4). Since q1 = 2a^2 for any a with 2a = beta x, q1 is a
   function of beta x through the integral cup product; what vanishes is (beta x)^2 = p1. Both levels now state that
   this result does not show k is undetermined by W(Sigma), beta x and the signature. The lay level no longer says
   "every simpler invariant": it names the simple twist class and the Pontryagin class.
5. The K-ring is now (L3) in the formal list, and the K sentence of (4) is marked as conditional on it.
6. Overlap. Per override 3 there is no claimref to the sibling. The extraction note and the (L3) line of the proof name
   synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height as the intended citation for the m = 3 K
   computation (its clause (1) at n = 3), and for the all-k obstruction and growth.

runcheck: 5/5 PASS (check_k_theory_cross_check, check_lens_action_and_walls,
check_quaternionic_odd_map_bounds_embedding_rank, check_spin_class_of_doubled_line_on_lens_spaces (now also touching
the Whitney Fact), check_spin_lift_of_doubled_line).

## synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional (R1 section 3, SOUND WITH FIXES)
1. The T~ repair. The referee is right: T = gamma^0 gamma^1 K maps even fields to odd ones. The sphere operator is now
   T~ Phi := gamma^0 gamma^1 (K Phi) gamma_0 in formal (2), the technical level, the proof and the extraction note.
   - The channel equation is (A Phi + lambda W gamma^{01} Phi gamma_0) I sigma_3 = m sqrt f Phi gamma_0.
   - The squared operator is d_t^2 - d_{r*}^2 + lambda^2 W^2 + lambda (d_{r*} W)[Phi -> gamma^0 Phi gamma_0].
   - V_+- live on the +-1 eigenspaces of that even involution.
   - The proof gives the cross-term cancellation with the right factor.

   check_angular_operator_and_squared_channel was rewritten. It now asserts:
   - parity: Phi is even, gamma^{01} K Phi has grades in {1, 3}, and T~ Phi is even;
   - T~ commutes with A and with right multiplication by I sigma_3 and by gamma_0;
   - T~^2 = K^2;
   - the squared identity holds for lambda = 1, -2, 3 and is even;
   - the identity fails without the right factor gamma_0.

   coverage.yaml was updated to match. All conclusions (potentials, rates) are unchanged.
2. J3 narrowed. Formal (4), the one-liner, the technical level and the proof now say: "the channel-reduction clause of
   joint J3 holds at the horizon for spins 0, 1/2 and 1; J3 is not discharged: spin 2 and its identification of the
   s-wave theory's current boson with these channels remain premise". The extraction note records Leon's decision
   (override 4) to narrow J3 to spin 2 once this is accepted. It also says that under J3 integer-weight channels are
   array currents and that nothing here counts them additively.
3. The classical inputs are now explicit hypotheses in the formal level. (C1) is completeness of the spherical and
   spinor spherical harmonics. (C2) is the exact/co-exact split of one-forms on S^2. The formal level says they enter
   "every channel" in (4) and are not used by the single-channel reductions (1)-(3), and the proof references them by
   label. The extraction note says deriving them is an open item.
4. The lay level adds that patterns winding more often reach the free form only closer to the horizon (non-uniform
   in angular momentum).
5. Formal (2) states that f^{-1/4} is the boost-weight-zero rescaling. It is labelled argued, as in the referee's
   item, since the frame-boost reading is not proved here.
6. Maintainer: the extraction note carries the correction to the op's known text. The potentials are proportional to
   1 - 2M/r for spins 0 and 1, and to sqrt(1 - 2M/r) for spin 1/2.

runcheck: 5/5 PASS (check_angular_operator_and_squared_channel, check_dirac_channel_reduction,
check_horizon_decay_orders, check_maxwell_channels_both_parities, check_scalar_channel_potential).

No rebuttals; every fix was applied.
