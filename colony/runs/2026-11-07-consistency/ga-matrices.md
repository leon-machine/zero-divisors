# GA rewrite, kind = matrices (36 entities)

Validation: `tp check --layers 1,2,3 --author leon` filtered to ids_ga_matrices.txt shows only the three I213 findings already in baseline.log (mass.chart-form-spin-isomorphism, synthesis.clausius-..., synthesis.slot-module-...). A W222 on synthesis.duality-... from a second sl(2, C) in its proof was fixed. galang.scan: no unexcused stand-in on any of the 36 entities. Every equivalence beyond notation was verified exactly with lib/GA.py (scripts in the scratch folder gamat/v_*.py). check.py files were not touched, and no status, link, pin, assumes or ledger was changed.

## Rewritten (old -> new version)

- families.rigidity-pairing-sector-one-event 4 -> 5: the cross-product matrix [a]_x becomes contraction by a family bivector, w -> w.(I_f a) = -I_f(a ^ w). The channel cross products become -I_f(f_+ ^ f_-) and -I_f(u' ^ f_+). The triple-product identity becomes a.(abar ^ w) = |a|^2 w - abar(a.w). The matrix form of G G^dag is now a labelled reading. The Takagi factorisation of the pairing matrix and the 2 x 2 spinor epsilon stay, because the pairing matrix is the point of the result. The outside_ga declaration (other) is removed. Verified in Cl(3,0); the identities extend bilinearly over span{1, I_4}.
- note.families.setting-machine-verification 1 -> 2: the channel cross products are written as duals of outer products. GG^dag and the sparse matrices of Part F stay, because they describe what the script computes.
- mass.chart-form-spin-isomorphism 5 -> 6: the three block matrices become linear maps on the chart frame (grading element, b_x: S+ -> S-, c_x: S- -> S+), acting on Lambda^2 S as derivations. The block matrices stay as a labelled reading. Notation only.
- singularity.descent-what-it-erases 5 -> 6: the element is written x = a vv* + b v + c v* + d v*v and E(x) = a vv* + d v*v. Computed from the CAR, with vv*, v, v*, v*v as matrix units. The E_ij matrices become a labelled reading. Verified in Cl(1,1).
- singularity.descent-parity-average 4 -> 5: the proof computes alpha(x) = sigma x sigma from the CAR, with sigma = v*v - vv*. The matrix product becomes a labelled reading. Verified in Cl(1,1).
- std-algebra.cl11-matrix 1 -> 2: the isomorphism is stated by the matrix units uw, u, w, wu inside Cl(H), and by 1/2(1 +- e_1), 1/2(e_2 +- e_1e_2) for Cl(2,0). The matrices become a reading. Declared bridge. Verified.
- std-algebra.pauli-algebra 3 -> 4: matrix units over the centre span{1, I}, namely 1/2(1 +- e_3) and e_1 1/2(1 -+ e_3), with e_1, e_2, e_3 expanded in them. The Pauli matrices are a reading. The bridge declaration is kept. Verified.
- std-algebra.sta-matrix 1 -> 2: Hamilton's units are written as the spatial bivectors, with J = -gamma_1gamma_2gamma_3. The matrix units 1/2(1 +- gamma_0) and 1/2(1 +- gamma_0)J commute with H, and gamma_k = J q_k. The complexification is named as the store's odd extension Cl(2,3) with unit I_5. The Dirac matrices stay as a reading. Declared bridge. Verified (rank 16).
- obj.std-algebra.spacetime-algebra 1 -> 2: the technical sentence about Dirac matrices is reworded: the frame is a set of vectors, and the matrix representation is a labelled reading.
- synthesis.imported-dimensional-regularisation-and-the-bmhv-gamma5 2 -> 3 (imported, kept): clause (ii) now splits vectors into a four-dimensional part and an orthogonal evanescent part. The BMHV gamma_5 is written as I_4 acting on the left, with the unit outside the product: gamma_5 x = I_4 x I_4. Clause (iii) reads the trace as 4<.>_0. The source's form moved to source_formal. Verified in Cl(1,5).
- synthesis.imported-kaluza-klein-ansatz 1 -> 2 (imported, kept): the ansatz is now the gauge field hb^{-1}(a) = hb_4^{-1}(abar) + phi(a^y + kappa A.abar)e_5, with g_AB as its reading. sqrt(-g) becomes det(hb_4)^{-1}, F = nabla ^ A, and the gauge transformation is A -> A - nabla lambda. R and F_ab F^ab stay as the source writes them. The source's form moved to source_formal. Verified for both signs of Q(e_5).
- synthesis.kerr-ring-connection-limit-null-rotation-winding-three 1 -> 2: the spatial cross products are written -I_s(a ^ b), with I_s = e_x e_y e_Z. Verified. The commutator products stay; they are GA notation.
- synthesis.duality-complex-structure-does-not-reach-the-frozen-point 2 -> 3: sl(2, C) is written as sl(2) over span{id, J}, in both the formal level and the proof. The Gram and Hessian matrices and the 32 x 32 real matrix stay; they are explicit matrices that the computation is about.
- synthesis.normality-on-the-closed-generator-gives-the-vacuum-folium-not-the-ground-state 3 -> 4: the rotors' action is stated as Moebius maps, and the SL(2, R) matrices become a labelled reading.
- synthesis.majorana-scale-is-126-doublet-vev 2 -> 3, synthesis.no-120-excludes-hierarchical-second-stage 1 -> 2, synthesis.one-type-second-stages-are-twins 1 -> 2: "Dirac matrices" (meaning the Dirac mass matrices) now reads "Dirac mass matrices". This removes a detector false positive. Wording only.
- synthesis.slot-module-light-ray-arrays-are-weyl-components 2 -> 3: one sentence names the two units, at reader R08's request (see below). Its mass matrices stay.
- note.primer.setting-products-vectors-one-rule-3 1 -> 2: adds a ^ b = I(a x b). Declared bridge.
- synthesis.twisted-wall-induction-conserves-dying-line-class 1 -> 2: at reader R09's request, proof (3) now says that the rung (1,1) preserves both clock positions, matching the cited rung result. Wording only. Its Gram matrices stay.

## Declared, text unchanged (version +1, declaration only)

- note.primer.abstract, note.primer.setting-products-vectors-one-rule, note.primer.setting-products-vectors-one-rule-2 (1 -> 2), all bridge: the primer motivates the geometric product by comparing it with the cross product, so the cross product is what the passage is about.
- note.mass.what-nullity-fixes 4 -> 5, bridge: an explicit 2 x 2 matrix computation of the real slice in the chart frame, set beside its GA reading.
- tower.compatibility-connecting-maps-transported 6 -> 7, bridge: a statement about block matrices in the matrix picture of the tower, A (x) Mat_{2^k}(R).

## Not rewritten (no change, no version bump)

- Gram matrices, Schur complements and determinants of forms, which the conventions allow: sheaf.determinant-identity-blow-up-expansion, sheaf.schwarzschild-degeneration-boundary-tame, sheaf.wall-gram, three-routes.imported-boundary-gram-ladder, synthesis.tameness-splits-regularity-and-order, synthesis.transverse-corank-two-walls-are-wild (the stratification of symmetric matrices is the point). Reader R09 checked the mathematics of these and found no issue.
- Explicit numerical matrices that are the point of the result: synthesis.adiabatic-deposit-modulation-is-a-time-shift (rank and kernel of a 2 x 3 matrix), synthesis.clausius-is-window-first-law-plus-boost-charge-conservation (a rational rotation on two modes, a 4 x 4 density matrix).
- Mass and family matrices: synthesis.imported-left-right-bidoublet-two-yukawa-couplings (also the 2 x 2 bidoublet and epsilon of the source's model; reader R04 found no issue).
- Already declared bridge, nothing further to do: synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation.
- synthesis.unit-i4-keeps-its-three-properties-only-in-dimension-zero-mod-four: "chirality matrix" and "Pauli-Villars" only name the standard method it compares with, and the scan is clean. Not bumped, because many entities pin it.

## Possible errors found

1. mass.chart-form-spin-isomorphism has two `source_formal:` keys in its front matter, and the first is empty. YAML keeps the second.
2. synthesis.imported-kaluza-klein-ansatz says "up to the sign of g_yy". In fact the sign Q(e_5) multiplies all the fifth-direction terms (g_ay and the A_aA_b term as well). It is now stated as epsilon. In R^{1,4} itself, epsilon = -1.
3. families.rigidity-pairing-sector-one-event: as a matrix, the antisymmetric pq^T - qp^T equals -[p x q]_x. The proof's claim "p ^ q acts as [p x q]_x" holds for the contraction w -> w.(p ^ q), which is now stated explicitly. The entity also uses epsilon for both the 2 x 2 spinor and epsilon_ijk (pre-existing clash).
4. synthesis.duality-complex-structure-...: the "formal unit j" of clauses (ii) to (iv) is still a scalar adjoined to tau. This was left for the units owner and Leon.
5. The version bumps leave the dependants' pins one behind (for example singularity.descent-what-it-erases pins std-algebra.cl11-matrix@1). These are for the repin pass; the check raised no warnings for them.

## Reader issues addressed

- ga-issues-R08: slot-module, two units with no sentence saying which acts where. Fixed (version 3): Hestenes' right unit I_4 sigma_3 acts on the spinor values and span{1, I_4} on the slot module. They are not identified, and the count is independent of the choice. families and note.families: no remaining issue.
- ga-issues-R10 item 3: mass.chart-form-spin-isomorphism. No sentence added. Its levels use no imaginary unit, because the chart maps are real-linear in the frame. The I_6 versus I_7 orientation sign belongs with synthesis.attachment-... (R10 item 2, not mine). R10 found no issue on majorana, no-120 or one-type.
- ga-issues-R04: the bidoublet Fact. No issue.
- ga-issues-R09: twisted-wall, proof (3) wording. Fixed (see above). descent-what-it-erases: the stale unit_note ("stays a scalar i") is annotated as superseded (no i remains; the radial atom's unit is J = e2e3), within its version 6. descent-parity-average and the Gram entities: no issue.
