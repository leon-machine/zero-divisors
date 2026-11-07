# GA rewrite round 2, gravity side (run 2026-11-07-consistency)

List: ga2_gravity.txt (68) plus 15 reader-named entities not on another list (interior.imported-tractor-connection, mass.imported-frozen-point-tractor-connection, pairing.loop-classes-are-weyl-components, synthesis.einstein-condition-is-infinity-vacuum-incidence, standard-model.connection-forced, synthesis.frozen-point-unique-where-weyl-has-no-kernel, synthesis.two-frozen-points-conformally-flat, dark-matter.asymmetry-arrow-counted-fifteenth-refutation, dark-energy.gravity-pre-metric-forces-degenerate-exactly, synthesis.promoted-norm-one-global-pair, dark-energy.imported-frozen-point-geometry, dark-energy.stelle-west-vector-frozen-point, dark-energy.wall-counterterm, singularity.non-removability-invariant-argument, singularity.transport-schwarzschild-fibre): 83 entities.
Changed: 40 (9 rewritten, 31 declared outside_ga and otherwise left); unchanged: 43. Entities already bumped in this run kept their version (credit and note added to it).

Validation: tp check layers 1-3 (--author leon) filtered to my ids: no error or warning on them (only I213 subject notes, all in the baseline); galang.unexcused empty. The full run's 5 E206 and 3 W222 are on entities not on my lists.

## Rewritten

- synthesis.positive-null-energy-gives-r-premises: 8 -> 8; surface gravity as (K.D)K.
- interior.imported-tractor-connection: 2 -> 3; tractor connection as the Cl(2,4) gauge field.
- singularity.non-removability-invariant-argument: 2 -> 3; Kretschmann scalar of the curvature operator.
- singularity.computed: 4 -> 5; acceleration as (u.D)u.
- interior.imported-schwarzschild-curvature-spectrum: 6 -> 7; round-sphere line element renamed.
- pairing.imported-schwarzschild-connection-curvature: 5 -> 6; round-sphere line element renamed.
- standard-model.connection-forced: 4 -> 5; connection forms as gauge fields.
- pairing.imported-spin-coefficients-null-tetrad: 2 -> 3; complexification unit named.
- pairing.imported-weyl-scalars-petrov-type-schwarzschild: 2 -> 3; complexification unit named.

## Declared outside_ga (reason recorded in each entity)

- dark-energy.frozen-point-makes-stelle-west-vector (5 -> 6)
- dark-energy.gravity-pre-metric-forces-degenerate-exactly (4 -> 5)
- dark-energy.stelle-west-vector-frozen-point (5 -> 6)
- dark-energy.wall-counterterm (5 -> 5)
- obj.interior.weighted-blow-up-hubble-normalisation-admissible (2 -> 3)
- pairing.curvature-which-loops-move-vacuum (6 -> 6)
- pairing.loop-classes-are-weyl-components (4 -> 5)
- pairing.regular-frame-class-vanishes-horizon-changes (6 -> 6)
- pairing.static-frame-only-expansion-survives (7 -> 7)
- rule2.imported-gamma-matrices-odd-dimension (1 -> 2)
- singularity.transport-schwarzschild-fibre (8 -> 9)
- synthesis.black-hole-data-do-not-fix-field-equations (7 -> 7)
- synthesis.boundary-mode-first-law-of-entanglement (7 -> 7)
- synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet (2 -> 2)
- synthesis.cosmological-horizon-completed-pair (3 -> 4)
- synthesis.einstein-condition-is-infinity-vacuum-incidence (3 -> 4)
- synthesis.euler-entropy-of-a-horizon-patch-is-an-edge-term (2 -> 3)
- synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff (2 -> 3)
- synthesis.frozen-point-unique-where-weyl-has-no-kernel (4 -> 5)
- synthesis.imported-gauss-bonnet-with-corners-poincare-hopf-and-edge-term (1 -> 2)
- synthesis.kasner-curvature-wall-is-negative-weight-helicity (1 -> 2)
- synthesis.killing-horizon-value-factor-is-the-generator-boost (1 -> 2)
- synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part (3 -> 3)
- synthesis.nondiagonal-kasner-residue-weighted-shear (3 -> 4)
- synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale (2 -> 2)
- synthesis.promoted-norm-one-global-pair (4 -> 5)
- synthesis.promoted-norm-weyl-clock-flat-weight (6 -> 7)
- synthesis.series-wald-entropy-changes-without-flux-on-local-horizons (2 -> 3)
- synthesis.taub-nut-cauchy-horizon-is-taub-point-with-complex-residue (2 -> 2)
- synthesis.tractor-transport-weak-null-crossing (4 -> 5)
- synthesis.two-frozen-points-conformally-flat (3 -> 4)

## Unchanged, with reasons

- Already GTG-primary, components only as labelled readings: correspondence.imported-weyl-commutes-duality, correspondence.lorentzian-duality-complex-structure (already declared for its complexification note), dark-energy.imported-macdowell-mansouri-theorem-stelle-west (GA split of A(a) and F(B) stated first), dark-energy.imported-frozen-point-geometry and mass.imported-frozen-point-tractor-connection (Omega_T stated first), interior.imported-mass-inflation-stability (Christoffel mention labelled), synthesis.imported-lovelock-cartan-four-forms-and-holst-term (index readings labelled), synthesis.imported-taub-nut-field-and-misner-extension (line element with the SU(2) one-forms, flagged beyond one chart), sheaf.weighted-limit, sheaf.gauge-field-cometric, singularity.imported-interior-collar-kasner-form, dark-energy.imported-weighted-limit-schwarzschild-singularity-matching, singularity.euclidean-section-period, scrambling.slice-volume-exactly-per-unit-killing, synthesis.c1-c2-forms-forced-one-number, synthesis.exceptional-boundary-measure-one-calibration, synthesis.kerr-ring-double-cover-data.
- False positives of the scan (structure constants epsilon_ijk, Gram data h_il, t_il, spinor symplectic epsilon_ab, oscillator labels, the deformation product written as a star, Gamma as an operator name, matrix traces): correspondence.chirality-split-ordering-insensitivity-asd-sector, correspondence.reality-conjugation-twistor-form-factor, mass.exact-join, synthesis.many-twistor-join, synthesis.operator-join-casimir-shifts, synthesis.quartic-ordering-tensor-locally-trivial, synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise, synthesis.restricted-dirac-hadamard-parametrix-on-a-null-hypersurface-is-the-null-vacuum-plus-a-bounded-kernel, synthesis.spin-product-state-of-the-massless-dirac-field-is-odd-under-chirality-and-never-hadamard, synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays, synthesis.massless-frequency-sign-relative-to-i4-is-not-the-chirality, synthesis.univalence-from-even-stationary-dynamics, synthesis.spin10-clause-content-is-the-neutral-singlet-choice (its C is a matrices-side item), synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces (star = screen product), dark-matter.total-function-thickness, dark-matter.asymmetry-arrow-counted-fifteenth-refutation (tr F ^ F, characteristic classes: topology, R05 'fine').
- Notes recounting the papers (Newman-Penrose and spin coefficients named as prior art, line elements): note.correspondence.setting-machine-verification, note.pairing.abstract, note.pairing.reading-prior-art, note.pairing.setting-setting-what-imported, note.pairing.setting-what-does-two-claims-3, note.singularity.setting-metric-gauge-field-static-form, note.singularity.setting-schwarzschild-gauge-field-connection-where-2; note.pairing.setting-transport-moves-vacuum-transverse-derivative (index raising of omega^{ab} beside the bivector sum, a reading); note.rule2.what-kaluza-klein-obstruction-physically (gamma-matrix sign: matrices side).
- Already declared: rule2.rule-2-kaluza-klein-algebra.

## Round-1 entities: reader items addressed (versions kept)

- synthesis.hadamard-dirac-states-...: R02 1, proof Step 7. I checked it exactly in Cl(2,3), on four separations: (1/2)Q(z - eps I_5 e_0) = sigma - (1/2) I_5 eps h - eps^2/2, with h = 2 z_0. The regulator is now 1/(sigma_l - (1/2) I_4 eps h_l - eps^2/2) and the boundary value 1/(Q(z)/2 - I_4 0 h). The old +eps^2 regulator has real zeros: at z = (0,7,1,0) with eps = 5, -25 + 25 = 0. The formal statement and the conclusion are unchanged. R02 2-4 also done: the lay level is updated, (HS) is named as the Theorem it now is, and the one-liner is in LaTeX. R02 5 needs no change.
- synthesis.positive-null-energy-gives-r-premises (R02 7): proof (iii) in GTG ((K.D)K = kappa K), components as readings.
- R06 1 kasner-field-is-weyl-flat (signature declared; lambda_i are store-sign Weyl eigenvalues, consistency shown on Schwarzschild 2M/r^3 and de Sitter Lambda/3; R t^2 = -2/3 holds in the store sign); R06 2 radical-normal wall (signature and sign of R declared); R06 3 e+e- spin-sum wording (3 -> 4); R06 4 Q(i) written span_Q{1, I_5} (one-loop QED proof) and span_Q{1, I_4} (running coefficients, 2 -> 3); R06 6 two-loop 'Step 0' typo.

## For Leon

- dark-energy.wall-counterterm (R09): the Chern-Simons value 8 p1 p2 p3 is odd under omega -> -omega; whether its omega^{ab} are Cartan forms (minus Omega on vectors, C10) or the definition's Omega needs a check against T10 Prop 4.11 before a sign sentence is added.
- synthesis.imported-hadamard-parametrix-... (R06 5): the extraction note quotes Sahlmann-Verch's regulator with the opposite sign of the eps term to the store's flat form; recheck against the source.
- The declared entities with component, form or tractor-slot proofs would need GTG derivations through Omega, the field strength and Omega_T, which are new proofs rather than notation changes; the round-sphere symbol d Omega^2 beside the gauge field Omega remains in about ten entities (renamed only in the two R03 named).
- synthesis.einstein-condition-is-infinity-vacuum-incidence: the complexifications T_xM (x) C and T_x (x) C should carry I_5 and I_7 (U3); left to the matrices/complexification side.
