# GA rewrite, kind tensor (run 2026-11-07-consistency)

53 entities (the 52 of ga_tensor.txt plus synthesis.kerr-ring-count-misses-area-law, added by the coordinator from R08). 36 changed (version + 1 each, credit and extraction note maintainer_pass_ga_rewrite, every file kept, no status, link, pin, assumes or ledger change, no check.py edited); 9 of them now declare outside_ga; 17 unchanged.

Validation: `tp check --layers 1,2,3 --author leon` filtered on my ids: no error or warning (only the pre-existing I213 subject notes on three entities); galang.unexcused empty on all 53. The W222 that the first run showed on one-relation.schr-odinger-slow-shadow (the phrase cross product) is cleared. The one error in the full run (E206, synthesis.charged-vaidya-cauchy-horizon-tractor-threshold) is not on my list.

Criterion used: gravity in GTG (metric, Christoffel, Riemann/Ricci/Weyl components only as labelled readings); tensors that are linear or bilinear maps written as maps on vectors; g_{mu nu} of the polarisation algebra as gamma_mu . gamma_nu; components on the STA frame gamma_mu / gamma^mu (the algebra's own vectors), scalar components, Gram, mass and Yukawa matrices, structure constants and basis labels of oscillators kept, as the conventions allow.

## Changed (old -> new; what; what stays)

- correspondence.one-statement-three-languages: 5 -> 6; twistor-index name of the infinity bivector. stays: nothing tensorial left.
- dark-energy.sheaf-papers-wall-soldering-variables: 8 -> 9; coframe and metric components. stays: the stabiliser algebra {A : A eta + eta A^T = 0} and its block matrices (the dimension count is the result).
- dark-energy.walls-free-sector: 5 -> 6; derived metric; components declared. declared other: rank counts on components of torsion, curvature and connection one-forms at a point where hb^{-1} is degenerate. R09 fix: Cartan-form sign (C10) stated in the proof.
- dark-matter.imported-induced-equations-hypersurface: 2 -> 3; stress-energy and Einstein tensors as linear maps. source form in source_formal; signature (-,+,+,+,+) kept and named.
- dark-matter.imported-linear-momentum-equation-traceless-field: 2 -> 3; covariant conservation. conservation dot-T(dot-D) = 0; source form in source_formal; line element kept as the derived-metric reading.
- dark-matter.sourcing-rule-forced-not-chosen: 3 -> 4; field equations, action density, momentum square. G(a) = -8 pi G T(a) in the store sign; Q(p); det(hb)^{-1} R in the reduction.
- interior.exact-parallelism-convergence-rate: 5 -> 6; Christoffel computation as D on the physical frame. proof (1) via the Koszul identity for D on the physical frame; Gamma kept as reading.
- interior.kasner-form-interior: 5 -> 6; geodesic condition as D-parallelism. D_{e_tau} g_tau = 0 from the frame products.
- mass.casimir-form-join: 7 -> 8; Casimir contraction with the reciprocal basis. reciprocal-basis sums; Gram matrix h and matrices A(B) on CS stay.
- note.dark-energy.setting-which-wall-soldering-form-against: 1 -> 2; soldering form and derived metric.
- note.interior.setting-setting-conventions: 1 -> 2; de Sitter curvature. R03 fix: field equation in the store sign, LDG form as reading.
- one-relation.schr-odinger-slow-shadow: 7 -> 8; cross product in the Pauli identity. Pauli identity ab = a.b + a ^ b; R12 fix: I sigma_3 (right) is not I_4 (left).
- singularity.imported-equivalence-einstein-equations: 2 -> 3; curvature correspondence stated for the curvature operator. source form in source_formal; R03 fix: dangling eqrefs replaced by the Definition clauses (f), (d).
- synthesis.imported-gtg-dictionary: 1 -> 2; component forms marked as readings. declared bridge (it is the translation table); previous formal in source_formal; R03 fix to (iv).
- synthesis.imported-two-dimensional-covariant-gravitational-anomaly: 1 -> 2; covariant anomaly read in two-dimensional GTG. declared imported (consistent anomaly is in Christoffel symbols; epsilon, sqrt(-g) conventions of the source); R05 fix of the sign sentence.
- synthesis.imported-heat-kernel-coefficients-and-background-field-gauge: 1 -> 2; declared outside_ga. declared imported only, text unchanged (bundle over a closed manifold, Euclidean sign the store does not fix).
- synthesis.imported-sakharov-induced-gravity-coefficients: 1 -> 2; declared outside_ga. declared imported only, text unchanged (same reason).
- synthesis.imported-one-loop-integrals-and-pauli-villars-regulators: 2 -> 3; symmetric integration and photon propagator as vector forms. existing source_formal kept.
- synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport: 4 -> 5; principal part as the physical gradient. existing source_formal kept.
- synthesis.diagonal-kasner-momentum-constraint: 3 -> 4; declared outside_ga (coordinate Ricci computation). declared other, text unchanged: the result is about the coordinate components R_{0i}; a GTG proof via Omega would be a new derivation (for Leon).
- synthesis.kasner-approach-gives-horizon-exit-and-index-three: 3 -> 4; scalar wave equation in GTG. wave equation det(hb) nabla.(det(hb)^{-1} hb hb^T(nabla phi)) = 0, exact.
- synthesis.kasner-hidden-scale-coupled-scalars-stay-blue: 3 -> 4; scalar kinetic term in GTG. F_{mu y} F^{mu y} stays (field-strength components).
- synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points: 1 -> 2; Weyl eigenvalue stated for the Weyl map; proof route declared. declared other: proof and check go through coordinate Christoffel/Riemann/Weyl components.
- synthesis.radical-normal-tame-wall-is-a-regular-initial-surface-whose-smoothness-selects-no-state: 2 -> 3; Ricci square; coordinate curvature engine declared. declared other: curvature values from the check's coordinate engine.
- synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared: 2 -> 3; Weyl square as a scalar of the Weyl map. (1/4)W_abcd W^abcd = (1/2)<W(a^b)W(d_b^d_a)> checked exactly in scratch (212 = 212); declared other: proof uses bivector-valued two-forms and component Weyl bases; (v) on closed S^2 x S^2.
- synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field: 5 -> 6; geodesic equation as D-parallelism. check formulas (van Vleck, eikonal) described as the check's and kept.
- synthesis.two-loop-qed-in-the-spacetime-algebra-continued-in-dimension-gives-the-second-beta-coefficient: 3 -> 4; photon propagator and polarisation as linear maps. proof components on the Euclidean frame stay.
- synthesis.one-loop-qed-in-the-spacetime-algebra: 4 -> 5; photon propagator as a linear map. existing bridge declaration kept.
- synthesis.kerr-ring-count-misses-area-law: 5 -> 6; Kerr-Schild gauge field; unit named I_4. hb(a) = a + H(a.k)k, g = a.b - 2H(a.k)(b.k); Delta = -Sigma Q(hb^T(nabla r)) in the store product; unit of z = r - I a u written I_4 (it is the I of the Walker-Penrose scale, span{1, I_4}); induced metrics as Gram matrices; flag sentence kept.
- synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form: 2 -> 3; metric components as frame products.
- synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts: 3 -> 4; metric components as frame products.
- synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields: 2 -> 3; metric components as frame products.
- synthesis.locality-of-the-attached-free-fields-fixes-their-statistics: 4 -> 5; metric components as frame products.
- synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number: 3 -> 4; metric components as frame products.
- synthesis.residues-zero-four-real-chirality-anomaly: 3 -> 4; reader fixes: scalar-curvature sign remark, J named. R05 fixes only (no tensor rewrite needed): store scalar-curvature sign remark corrected, its J named as the unshared-plane bivector; anomaly-polynomial forms stay.
- synthesis.operator-join-ordering-constants: 3 -> 4; which unit acts where. R10 fix: sentence on I_6 (moment factor) vs I_4 (Fock scalars); oscillator indices are basis labels.

## Not rewritten (unchanged, with reasons)

- correspondence.ordering-filtration, synthesis.attachment-conformal-energy-is-generated-by-z: indices are basis labels of the palatial / twistor oscillators (Z^alpha, Zbar_beta, h^{-1} Gram), as in their premises; no tensor calculus.
- neutrino.rank-one-seesaw-ordering-sum-double, note.neutrino.abstract, pred.no-neutrinoless-double-beta, note.programme.setting-falsifiable-claims, note.programme.setting-machine-verification, note.programme.setting-series-paper-paper-2: false positives (m_{beta beta}, m_mu, U_{ei} are labels; the Dirac matrix is a mass matrix).
- note.singularity.setting-gauge-theory-exactly, obj.synthesis.gtg-flat-spacetime-gauge-fields: already GTG, components only as labelled readings.
- note.one-relation.setting-machine-verification: gamma^mu are STA vectors and {gamma^mu, gamma^nu} = 2 eta^{mu nu} is the defining relation; describes the legacy script.
- one-relation.dirac-current-conserved-density: already declared bridge (stated in a 4 x 4 matrix representation); a real-bilinear GA restatement changes the class of currents (R12), for Leon.
- synthesis.chiral-abelian-loops-..., synthesis.electron-positron-to-muon-pairs-..., synthesis.one-loop-running-coefficients-..., synthesis.one-loop-vacuum-polarisation-extends-..., synthesis.two-loop-running-cannot-fix-majorana-coupling: components on the STA frame (Pi^{mu nu}, g-bar^{mu nu}, S^{mu nu rho sigma}, T^{mu nu}), Yukawa traces and the matrix readings already declared; the conventions allow components; rewriting the loop proofs into multilinear maps would be a long change for no gain in content.

## Possible errors found

- mass.casimir-form-join, proof (2): 'each contributing -1, so Phi(E,E) = -1' omitted the factor 1/2 (two products -1, times 1/2); now stated explicitly. Result unchanged.
- interior.exact-parallelism-convergence-rate, formal: e_0, ..., e_3 names the normalised physical frame while e_mu (e_tau, e_t, ...) is the background frame in the same statement; a notation clash, not changed (for Leon).
- No mathematical error found in the rewritten entities.

## Reader issues addressed

- R03 2 (note.interior field-equation sign), 6 (dictionary (iv) tautology and sign), 7 (equivalence Fact dangling eqrefs): fixed. R03 8, 9: nothing to do.
- R05 2, 3, 5 (dark-matter Facts and sourcing rule): done as part of the rewrite. R05 7 (a), (b) (residues): fixed; (c) forms kept (characteristic classes). R05 8 (2D anomaly sign sentence): fixed.
- R08 (kerr-ring): rewritten.
- R09 (walls-free-sector Cartan sign; sheaf-papers-wall): fixed / nothing further.
- R10 1 (operator-join units): sentence added. R10 2 (attachment I_6 vs I_7 orientation): not applied; R10's exact computation should be re-run before a sentence is added (for Leon). R10 3: mass.chart-form-spin-isomorphism is the matrices rewriter's.
- R12 (Schrodinger cross product and unit sentence): fixed. R12 dirac-current: for Leon. R12 note.one-relation 'twistor space': no such phrase found in the stored text; nothing changed.
- R01, R04: nothing on my entities requiring change.

## For Leon

- GTG proofs (through Omega and the field strength) for the coordinate curvature computations of synthesis.diagonal-kasner-momentum-constraint, synthesis.kasner-field-is-weyl-flat-only-at-the-milne-and-isotropic-points, synthesis.radical-normal-tame-wall-..., and the forms proof of synthesis.frozen-point-integrand-...; dark-energy.walls-free-sector is a rank count on components and is best left declared.
- Heat-kernel and Sakharov Facts: a GTG restatement needs a store sign for Euclidean-signature curvature.
