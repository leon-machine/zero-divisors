# Run 2026-11-07-consistency: apply agent D2 (Leon's second-round answer 7)

Acting for Leon as maintainer. No commits, no agents spawned, no processes touched. (My edits up to the first
validation were swept into commit 30be51b, made by someone else; the later pin edits are uncommitted.) Each changed
entity went to its locked version + 1 (store/.tp-lock.json, lock fb48481). Each has a credit entry, source "maintainer
pass 2026-11-07 (decisions, second round)", and an extraction note `maintainer_pass_decisions_2` (by
maintainer-2026-11-07: what changed, why, and the evidence). In every case the mathematics is unchanged: the GA form
comes first, the old form is kept as a labelled reading, and the two are proved equal exactly (lib/GA.py,
lib/gtg.py, Fractions).

Validation: `python3 -m tp check --store store --layers 1,2,3 --keep-going --author leon` was run twice, the second
time after all edits. Both runs gave 0 errors and 0 warnings store-wide. Every changed check file passes runcheck
(10/10, 4/4, 7/7, 7/7). The new check functions went through `tp mutants`:
- four-form: 0 of 6 perturbations survive;
- Ricci readings: 0 of 8;
- index readings: 0 of 8;
- Christoffel reading: 1 of 8 (a jet-order sample input). No W413.
No existing check encoded an old statement, so no check4 run was needed.

## Items

- **obj.interior.weighted-blow-up-hubble-normalisation-admissible 3 -> 4.**
  - The display is now the linear function hat Omega_tau(e_j) = tau omega(e_j) = tau Omega(hb(e_j)) =
    -p_j B_j + E_tau(e_j), on the unit tangential physical vectors. The coframe display and the Cartan forms are kept
    as readings, in the formal, technical and one-liner.
  - The outside_ga declaration is withdrawn, since nothing of its reason remains.
  - Evidence: work-D2/verify_weighted_blowup_display.py (all pass). An object carries no check, so the script stays
    in the run folder. It checks the coframe display on e_j, and the torsion-solved Kasner fields at
    (-1/3, 2/3, 2/3) and (-2/7, 3/7, 6/7), two times each, against the Cartan reading.
- **synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared 3 -> 4.**
  - A two-form is now a linear map of physical bivectors. The four-form is beta(F ^ G) =
    (1/2) beta(F(c ^ d), G(I4 (d_d ^ d_c))) vol, which covers eps(a, b, ., .) and K. The component definitions are
    kept as the reading.
  - The frame legs are now named as the map a ^ b -> 2 ((a . D)X) ^ ((b . D)X), and (v)'s Weyl square is written in GA.
  - Proof setting and (iv) updated to match.
  - New check: check_gtg_four_form_density_of_bivector_maps. It covers 15 cases (two generic maps, five pairings),
    a general frame with det H = -50, and (a . D)X = a.
  - outside_ga narrowed to the Chern-Simons form of (iv) and (v)'s global integrals and signature transfer.
- **synthesis.black-hole-data-do-not-fix-field-equations 7 -> 8.**
  - Conventions are now stated in GTG, with R^a_b = gamma^a . calR(gamma_b) and R = calR as the readings. The sign
    parenthetical is kept.
  - Ricci-map polynomial f; K = 2 <calR calR>; f = beta d_a . calR(calR(a)); the RN radial Ricci map; the entropy
    term with d_a . calR(P_sigma(a)).
  - New check: check_gtg_formal_readings_of_the_ricci_components. On three static fields, all 16 mixed components
    match the Christoffel computation, and so do the scalar, Ric^2, the radial trace and the Kretschmann scalar.
- **synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff 3 -> 4.**
  - Setting now in GA: the trace, the Ricci contraction, and the Einstein, Schouten and Weyl maps.
  - (iii) and (iv): the Weyl square and the interpolated density in GA, with the index forms kept as readings.
  - New check: check_gtg_formal_forms_equal_their_index_readings.
  - Found: with torsion, the GA Weyl map equals R - KN of the transposed Schouten matrix. The Weyl part is used only
    for torsion-free Omega, so the reading is labelled torsion-free (this is in the note).
- **synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet 3 -> 4.**
  - (ii): the ingoing velocity hb^{-1}(x') is D-parallel, D_{x'}k = 0, with Gamma^r_rr = 0 kept as the reading.
  - New check: check_gtg_affine_velocity_is_the_christoffel_reading. It verifies D_{X_a} hb^{-1}(X_b) =
    Gamma^c_ab hb^{-1}(X_c), 24 identities.
  - Also applied D3's items: zeta in the quotation of the companion, and r^2(dtheta^2 + sin^2 theta dvarphi^2) in
    three places.

## Pins reviewed (all class N, notation only)

- Repinned:
  - duality-complex-structure: integrand 3->4, stiffness 3->4.
  - frozen-point-integrand-gives-einstein-only: integrand 3->4.
  - stiffness: integrand 3->4.
  - collapsing-hole: positive-null-energy 8->9, D3's item.
- D1's R items applied, with D1's sentences in maintainer_pass_pin_review:
  - integrand: positive-structure 3->4, macdowell 3->4;
  - stiffness: macdowell 3->4.
- Claimed by others, so passed on:
  - to items-for-D1.md: curvature-only-tractor-actions, frozen-point-field-space-is-the-gtg-pair and
    inverse-problem-for-the-clausius-route (integrand@4), and parallel-frozen-point-on-matter-regions (stiffness@4).
  - to both items-for-D1.md and items-for-D3.md, since its claimant is not named:
    loc-independent-of-clausius-and-killing-data (black-hole-data@8).
  - If D1 has already finished, these five pins remain stale.

## Not applied exactly / for Leon

- The object's τ = 0 boundary is adjoined by the blow-up, together with a product extension of the boundary bundle.
  Should this get the dictionary section 14 "Beyond one flat chart" sentence and flag? I did not add it, because it
  is not part of answer 7.
