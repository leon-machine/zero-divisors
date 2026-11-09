# Fixes C2A (fix round, run 2026-11-09-solvable)

check4: pending (orchestrator). Only runcheck.py was run. All edits are in place in proposals/<id>/.

## synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge (R1 section 4, SOUND WITH FIXES)

1. Normalisation and xi.
   - (iii) now writes the Lagrangian as (1/2) kappa_ab <F^a F^b>_0 = -(1/4) kappa F_mn F^mn, which is still s-invariant.
   - The wrong "-(1/4) kappa <F F>_0" in the proof of (v) is replaced by the canonical form, with the GA identity <F F>_0 = -(1/2) F_mn F^mn.
   - (v) now states that at xi = 1 the vector quadratic form is the Feynman form up to the total derivative (1/2) kappa d_mu(A_nu d^nu A^mu - A^mu d_nu A^nu). With the unhalved density this happens at xi = 1/2, as twice the Feynman form.
   - New check `check_vector_kinetic_form_is_feynman_at_xi_one` uses Euler derivatives. With the canonical density at xi = 1, 0 of 48 are nonzero. With the unhalved density at xi = 1, 48 of 48 are nonzero. With the unhalved density at xi = 1/2, compared against twice the Feynman form, 0 are nonzero. This confirms the referee's point by computation.
   - The one-liner and technical text now carry the canonical normalisation.
2. Stationarity hypothesis.
   - (v) is now stated for V = 0, or for v a stationary point of an invariant V. The proof shows that Hess V(v) W_a = -rho(T_a)^T grad V(v), which vanishes at a stationary point; otherwise there is a tadpole.
   - "t^5" now says it counts five massless scalars only for V = 0.
   - New check `check_stationary_vacuum_hessian_kills_the_goldstone_directions` uses V = (|phi_1|^2 - 1)^2 + (|phi_2|^2 - 4)^2 + <phi_1, phi_2 e_12>^2 at v = (1, 2). The gradient is 0, Hess kills every W_a, and Hess has rank 3. Shifting the first constant by 1 gives a tadpole.
3. Overlap (ruling: keep both, partitioned). Nilpotency is restored as clause (ii) ("Nilpotency; proved"). Per override 3, the extraction note names the sibling synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets (i) as the intended citation for the stationarity condition, and notes that the sibling is to cite (ii) here. No proposal is cited.

Coverage: two functions added. checked_by now lists 7 functions.

runcheck: 7/7 PASS.

## synthesis.joint-clifford-clause-is-an-instance-of-the-signed-direction-postulates (R1 section 8, SOUND WITH FIXES)

1. (F1) is now treated only as the index set F_2^10 = G/<c> of the ten direction labels, not the 2^5 occupation configurations of V, and is flagged as a reading. This is in the Reading paragraph, the extraction note and the proof (Status). Every "(F1) to (F3)" is now "(F2) and (F3)".
2. The qualifier of (iv) is now in the title, one-liner and lay text: the clause is an instance once the ten Klein-twisted Majoranas are declared the directions, and the postulates do not choose them.
   - New title: "Clause (f) is (F2) and (F3) once the ten twisted Majoranas are declared the directions". The id is unchanged.
3. The equivalence "CAR iff the Clifford relations of the Majoranas" is labelled classical prior art (Jordan and Wigner 1928). This is in the extraction note, beside the extraspecial-group citation, and in the proof.

Check unchanged. runcheck: 5/5 PASS.

## synthesis.gauge-factor-sugawara-parts-satisfy-virasoro-relations-on-the-band (R1 section 6, SOUND; optional fixes)

- Lay: "the full symmetry of a one-dimensional conformal field theory" is now "the conformal symmetry of motion along one light ray (one chiral half)".
- Extraction note: the related stored Fact dark-energy.imported-conformal-orthogonality-sugawara-construction@1 is mentioned as related but not a duplicate. It imports the Sugawara bilinear as the stress tensor and states no Virasoro relations. It is a text mention only and is not added to uses.

Check unchanged. runcheck: 7/7 PASS.
