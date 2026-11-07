# Sweep D1: imaginary unit to GA pseudoscalar (2026-11-07)

38 entities: 7 changed (version + 1), 29 declared only (outside_ga added, version and levels unchanged), 2 unchanged (index letters only). Of the 7 changed, 3 also carry a declaration for the i that stays. Validation: `tp check --layers 1,2,3` shows no errors or warnings on D1 entities (only the existing subject-neighbour info I213). Detector re-scan: every listed entity carries outside_ga except the two index-only ones.

## Changed

- standard-model.imported-frozen-point-dictionary, 7 -> 8: de Sitter weight -3/2 +- i nu now -3/2 +- I_4 nu, numbers read in span{1, I_4} (formal, technical, proof). It restates series results (T11), so it is not a literature import. Nothing stays.
- synthesis.frozen-phase-spectrum-not-red, 2 -> 3: weights -3/2 +- I_4 nu and oscillating factors k^{+-2 I_4 nu} (formal, proof). Stays: Fourier kernel e^{-i k.x} of the scalar correlators in proof (ii). complex-analysis.
- synthesis.smallness-monomials-exact-hierarchy-casimir, 2 -> 3: weight -3/2 +- I_4 nu (formal, proof). Nothing stays.
- synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point, 2 -> 3: weight -3/2 +- I_4 nu and coupling xi = 1/4 -+ I_4 nu/6 (formal, proof). Nothing stays.
- synthesis.half-integer-weight-array-carries-half-ln2, 4 -> 5: flow phase e^{-I_4 omega_k t}, e^{-2 pi I_4(k + delta)}, checked e^{2 pi I_4 K} (proof). Stays: tau = i, q = e^{2 pi i tau}, sqrt(-i tau), tau = i y/2 pi (theta functions). complex-analysis.
- synthesis.quadratic-flows-cannot-thermalise-descent, 1 -> 2: boundary-mode CAR unit is I_4 (rule 4): Ad(e^{I_4 t X_k}), e^{+-I_4(...)t} on coherences and pairings, U = e^{-I_4 t k}, Cayley form, Q(I_4) (formal, proof). Nothing stays.
- synthesis.frozen-point-geometry-reads-descent-as-vacuum, 1 -> 2: horizon-generator kernel D_c = (I_4/2 pi)(uv)^{-1/2} g_c (proof). Stays: Bunch-Davies mode e^{-ik eta}(1 - i/k eta)/sqrt(2k), Fourier kernels, phase e^{2iu + i theta}. complex-analysis.

## Declared only (version unchanged)

- note.mass.what-nullity-fixes: explicit complex 2 x 2 chart matrices (i/sqrt2 K eps, entries of K), with the GA reading as I_6 already given. bridge.
- note.pairing.setting-setting-what-imported: null tetrad e_2 +- i e_3, C^4, e_3 = -i(a_2 + a_2^dagger): i next to spacetime vectors. other.
- one-relation.dirac-current-conserved-density: Mat(4, C) gamma-matrix Dirac theory, Hestenes form cited beside it. bridge.
- scrambling.clock-inventory-boundary-modes: e^{i theta n} shown to lie outside the real algebra; eigenvalues +-i on the e0e1 atom (known limit 1). other.
- singularity.l-stabiliser-tangent: so(2nu) + C, Spin(2nu, C), gamma_{2i} = i(v_i - v_i^*) on the e0e1 atom (known limit 1). other.
- synthesis.boundary-mode-first-law-of-entanglement: Fock space as a tensor product of C^2, density matrices and GNS purification (the |i> are labels). complex-analysis.
- synthesis.counted-unit-energy-at-half-offset: modular parameter tau = i beta kappa/2 pi, self-dual point tau = i. complex-analysis.
- synthesis.de-sitter-field-fixes-the-observer-tube-point: tube points x_perp + i rho u, V(m) = i ell u, X(m) = alpha + i beta. complex-analysis.
- synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries: tube point x_perp + i rho u. complex-analysis.
- synthesis.twistor-form-states-only-off-the-real-slice: Fock-model unit, complex chart m = x + iy, A = i x^ - y^, imaginary boost. complex-analysis.
- synthesis.positive-structure-is-twistor-form-at-imaginary-time: Cl(2,4)_C, J = i e_1 e_+, points +-i e_1, imaginary boost. complex-analysis.
- synthesis.wick-rotated-boost-selects-observer-tube-point: W_theta = exp(i theta K) in Cl(2,4)_C, tube points. complex-analysis.
- synthesis.eviction-keeps-one-of-catalan-many-replica-saddles: Haar states on C^d (x) C^d (the i in prod(d^2 + i) is an index). complex-analysis.
- synthesis.finite-range-descent-deposit-cannot-seed-cmb: Fourier kernel e^{-i k.r}. complex-analysis.
- synthesis.hadamard-condition-leaves-the-deposit-spectrum-free-on-bounded-bands: Wronskian i, modes e^{-ik eta}/sqrt(2k), Bunch-Davies control. complex-analysis.
- synthesis.sudden-descent-feature-not-tilt: Bunch-Davies u(z), Wronskian 2i, Bogoliubov coefficients. complex-analysis.
- synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling: Hankel Wronskian -4i/(pi s). complex-analysis.
- synthesis.kasner-approach-gives-horizon-exit-and-index-three: modes e^{ikx}, normalisation i, Hankel Wronskian (axis label i is an index). complex-analysis.
- synthesis.kasner-hidden-scale-coupled-scalars-stay-blue: same as above. complex-analysis.
- synthesis.imported-bessel-reduction-and-small-argument-hankel-forms: Hankel forms quoted from source. imported.
- synthesis.imported-de-sitter-invariant-hadamard-state-unique: Hankel expansion quoted from source. imported.
- synthesis.imported-mehler-formula-hermite-rank-and-power-law-spectra: Fourier convention quoted from source. imported.
- synthesis.imported-theta-function-identities: q = e^{2 pi i tau}, sqrt(-i tau), quoted from source. imported.
- synthesis.incidence-vacua-thermofield-real-capacity: Cl(p,q)_C against its real form, modes (g + ih)/2, c = (e_3 + i e_4)/2, value +-i on e_3e_4. other.
- synthesis.injection-freshness-is-pair-purity: abstract qubit spaces C^2, phase e^{i phi}. complex-analysis.
- synthesis.number-diagonal-dynamics-spreads-nothing: phase flow and Gaussian unitaries on the completed pairs (scalar i by the unit_note of singularity.modular-structure-completed-pair, known limit 1). other.
- synthesis.pati-salam-chain-defects-cannot-source-spectrum: complex defining representations of SU(4), SU(2)_L, SU(2)_R, U(1)_Y, with the rotor form alongside. bridge.
- synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise: CAR algebra written as the complexified Clifford algebra with Majorana generator i(a^dagger - a). other.
- synthesis.residue-common-weight-particle-hole: C^n, Mat_n(C), e^{i theta^a J_a} on the completed pairs (known limit 1). other.

## Unchanged

- dark-energy.frozen-point-datum-kasner-wall: only index letters (omega^{i0}, R^{0i}, {0, i}).
- synthesis.imported-replica-wormhole-two-saddle-purity: only the label |i>_R.

## Possible errors found

- synthesis.quadratic-flows-cannot-thermalise-descent, formal (ii): it says the boost dynamics multiplies the coherence C_ij by e^{+(omega_i - omega_j)t} (with the unit), but the proof, with U = e^{-tk} (unit included) and C_ij = omega(a_j^* a_i), derives (UCU^*)_ij = e^{-(omega_i - omega_j)t} C_ij. The pairing sign -(omega_i + omega_j) agrees in both places, so the sign of the coherence phase in the formal level does not match the proof's convention. It does not affect the result, since only moduli and the diagonal matter. Not fixed.

## Unsure (left as i, for Leon to rule)

1. Scalar mode functions (hadamard-condition, sudden-descent, frozen-point-geometry, the three kasner entities): the Bunch-Davies modes, the Hankel Wronskians and the canonical normalisation (phi phi-dot* - phi* phi-dot) = i were kept as complex analysis of scalar functions. Rule 4 could instead read them as the field's one-particle complex structure, I_4. If so, the normalisation and the mode functions would have to change together, since they share one unit.
2. The tube family (positive-structure, wick-rotated-boost, twistor-form-states, de-sitter-field-fixes, tube-point-clause): kept because the text works in Cl(2,4)_C with complex points, and conventions keep plain complexification there. The module's unit could be written as R_{I_6} acting on the right (rule 2), but the complex points m in V_C would still need i. Rule 5's replacement of imaginary rapidity by I_4 B is not exact for W_theta = exp(i theta K): exp(theta I_4 K) is a real rotation of span(e_3, e_4), and it does not carry tube points to real points.
3. Window and boundary-mode Hilbert spaces kept as abstract: boundary-mode-first-law (a Fock space as a tensor product of C^2, whose script builds the modes as Cl(1,1) ascent pairs, which commute with I_4) and injection-freshness (qubit spaces C^2, phase e^{i phi}). Under rule 4 these could take I_4, if Leon rules them GA-built.
4. Completed pairs and Hawking boundary modes are treated differently. number-diagonal, residue-common-weight and scrambling.clock-inventory keep a scalar i (known limit 1, from the unit_note of singularity.modular-structure-completed-pair). quadratic-flows (Hawking boundary-mode CAR algebra, known limit 2) was converted to I_4 under rule 4. Both conventions' known limits apply, so Leon may want one ruling for both.
5. Pati-Salam: the phases exp(3 pi i(B - L)) and diag(e^{i theta/6}...) are kept as entries of the complex defining representations. If the internal U(1) phase on the 16 is to be the field's unit, they could be rewritten with I_4.
6. quasi-free-deposit: if the n modes are tower modes, the Majorana generator i(a^dagger - a) could be I_4(a^dagger - a), since I_4 commutes with tower modes. It was kept because the text says "complexified Clifford algebra".
7. Mixed entities: frozen-phase-spectrum and frozen-point-geometry now carry I_4 for the weights and the generator kernel, and i in the Fourier kernels of the same computation. Each occurrence follows the rules, but Leon may prefer one unit per entity.
