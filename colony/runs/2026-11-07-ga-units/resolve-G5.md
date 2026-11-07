# Resolve sweep, group G5 (maintainer pass 2026-11-07, unit principle U1-U6)

47 entities. Versions run from the pre-pass commit 35714f6 to now. Per the coordinator's correction, every entity whose formal level or proofs changed gets version + 1 on its current version, plus a credit entry for the new version ("notation pass, imaginary units resolved by the unit principle"). Each one also carries the extraction note `maintainer_pass_resolve_units`. Every file is kept. Statuses, links, uses/assumes, pins and ledgers are unchanged. The core results are cited as mentions only (\claimref, no new uses edge).

Units chosen, by family:
- I_7 = I_6 e (U3): the T09 Fock module, CS and twistor module scalars.
- I_5 = I_4 e (U3): spacetime complexifications, the Dirac-matrix reading, vector i0 shifts.
- J = e_2 e_3 (U2): the completed-pair atom and the boundary modes. It is written out as e_2 e_3 where the entity uses J for the mode set.
- I_4 (U1): abstract Hilbert spaces and matrix factors, the field theory's numbers, and scalar-form shifts.
- I_2 = e_1 e_2 (a real plane's unit bivector): one Euclidean-plane note.

## Entities
- correspondence.chirality-split-ordering-insensitivity-asd-sector: 5 -> 6. Scalar of so(1,3)_C inside so(2,4)_C -> I_7 (U3): +-I_7 eigenspaces, A^(1,2)_i = (R_i +- I_7 B_i)/2, *A = -+I_7 A; says the duality lemma is read with this complexification. Declaration (other) removed.
- correspondence.fock-model-complexified-ascended-algebra: 8 -> 9. V_C and w_3 = b_3 + i b_4: unit I_7 = I_6 e of Cl(3,4) = Cl(2,4)_C (U3): w_3 = b_3 + I_7 b_4, Q(w_3) = Q(b_3) - Q(b_4) + 2<b_3,b_4> I_7 = 0, scalars span{1, I_7}. Declaration (other) removed.
- correspondence.incidence-relation-chart: 5 -> 6. Penrose's omega = ix pi only in the existing source_formal (U5); "I_6 acts as -i on CS" -> "-I_7", I_7 = I_6 e the scalar of Cl(3,4) = Cl(2,4)_C (U3); says I_6 acts by left multiplication and I_7 is the module's scalar. Declaration (bridge) removed.
- correspondence.local-twistor-transport-ascended-spinor-connection: 8 -> 9. Penrose's composite i eps (i P omega) in the proof -> I_7 eps (I_7 P omega) = -eps P omega, his unit acting on the fibre CS as the module's scalar I_7 (U3/U4). Declaration (imported) removed.
- correspondence.lorentzian-duality-complex-structure: 4 -> 5. Complexification of 2-forms by I_5 = I_4 e (U3): Lambda^2_C = Lambda^2 + I_5 Lambda^2, eigenvalues +-I_5, conjugation I_5 -> -I_5; says * is I_4 (up to sign) on real bivectors and I_5 is a different element. Declaration (other) removed.
- correspondence.reality-conjugation-twistor-form-factor: 7 -> 8. Fock module's scalar i -> I_7 = I_6 e, centre of Cl(3,4) = Cl(2,4)_C (U3): b_3 - I_7 b_4, b_4 = -(I_7/2)(w_3 + 2w_3'), e^{I_7 theta}, (3+4I_7)/5, m(I_7 x-hat); I_6 stays the incidence factor (left multiplication), clause (5) says I_6 = +-I_7 on CS, not identified. Declaration (other) removed.
- dark-matter.premise-flag-as-datum: 2 -> 3. Flag as +I_7 eigenspace of J on R^{2,4} + I_7 R^{2,4}; sign of J relative to the Fock module's I_7 (U3). Declaration (other) removed. Status (postulate) unchanged.
- hawking.gibbs-states-are-kms-conversely-finite: 3 -> 4. General End(C^m) over span{1, I_4} (U1): Ad(e^{I_4 tH}), alpha_{I_4 beta}. Declaration (complex-analysis) removed.
- hawking.imported-modular-descent-premises-geometric-normalisation: 7 -> 8. Phase flow of the completed pair (U2): Ad(e^{J t sigma/2}) in formal, technical, proof. Declaration (complex-analysis) removed.
- note.correspondence.abstract: 2 -> 3. Penrose's omega = ix pi moved to extraction.source_formal (the source writes i for I_6, the conformal spinors' unit, U5); text says his unit is written I_6. Declaration (bridge) removed.
- note.correspondence.setting-machine-verification: 3 -> 4. Script scalars Q(i), i x-hat, i-multiples, (3+4i)/5, +-i -> I_7 (U3, Fock model scalar), as in the results it covers. Declaration (other) removed.
- note.correspondence.setting-successor-problems: 2 -> 3. As above, problem (2). Declaration (bridge) removed.
- note.correspondence.what-factor-i-what-remains-conventional: 3 -> 4. Penrose's i stays only in the existing source_formal; I_6 named as the factor Penrose writes as his unit. Declaration (bridge) removed.
- note.pairing.setting-machine-verification: 2 -> 3. Class 2i of n e_3 -> 2 I_5 (U3, as in the stabiliser result). Declaration (other) removed.
- note.singularity.euclidean-reading-sign-flagged: 2 -> 3. R_{i theta}, R_{2 pi i} (rotor at imaginary rapidity in the atom's complexification) -> R_{J theta}, R_{2 pi J}, lambda = J theta (U2, J = e_2 e_3, cites the transverse-bivector result). Declaration (complex-analysis) removed. Depends on G1's notation for singularity.euclidean-rotor-where-it-lies (2).
- note.transport.setting-euclidean-plane-inversion-circle-riemann: 1 -> 2. z = x + iy -> z = e_1(x e_1 + y e_2) = x + I_2 y, I_2 = e_1 e_2 the plane's unit bivector (U1, phase in a real two-plane). Declaration (bridge) removed.
- pairing.stabiliser-parabolic-algebra-null-direction: 5 -> 6. Complex null tetrad and values of pv: unit I_5 of Cl(2,3) (U3): m = e_2 + I_5 e_3, pv(e_03) = I_5, pv(e_13) = -I_5, pv(n e_3) = 2 I_5, C^4 = R^{1,3} + I_5 R^{1,3}. Declaration (other) removed.
- rule2.rule-2-kaluza-klein-algebra: 6 (unchanged). No bare i; the declaration (bridge) is for the five-dimensional gamma-matrix representations of the imported Fact, not for i, so it stays as it was.
- scrambling.imported-modes-modular-inventory: 4 (unchanged). Not resolved (U6): see "Could not resolve". Declaration (complex-analysis) kept, reason narrowed.
- singularity.kms-uniqueness-factor: 5 -> 6. Matrix factor over span{1, I_4} (U1): Ad(e^{I_4 tK}), alpha_{I_4 beta} (also the merged proof file). Declaration (complex-analysis) removed.
- singularity.modular-descent: 6 -> 7. Atom pair (U2): phase flow Ad(e^{J t sigma/2}), modular flow Ad(rho^{J t}); proof says the matrix-factor lemma is read over span{1, J}. Declaration (complex-analysis) removed.
- singularity.modular-theory-matrix-factor-proved-outright: 5 -> 6. Abstract matrix factor and its Hilbert space: scalars span{1, I_4} (U1): rho^{I_4 t}, Delta^{I_4 t}. Basis indices i, j renamed k, l (index letters only; they were detector false positives). Declaration (complex-analysis) removed.
- singularity.schmidt-forcing-proved-outright: 5 -> 6. Doubled atom mode (U2): e^{J t G}, scalars span{1, J} on both factors; basis label |ij>, (i - j) renamed |jk>, (j - k) (index letters). Declaration (complex-analysis) removed.
- singularity.two-kms-functionals-sign: 6 -> 7. Atom mode factor (U2): Ad(e^{J t omega K}), alpha_{J beta}(a) = e^{-beta omega K} a e^{beta omega K}; proof reads the KMS-uniqueness lemma over span{1, J}. Declaration (complex-analysis) removed.
- synthesis.attachment-conformal-energy-is-generated-by-z: 3 -> 4. Module of three ladder pairs, CS and the oscillator Fock space: scalar I_7 = I_6 e (U3; one unit for the entity): h = <psi, I_7 Z phi>, Z = -+I_7 on T_+-, Q(Z/2) = -I_7 E, I_7 Q(P_a) >= 0, Jordan-Wigner e_k = I_7 g_k, (I_7/2) id, I_7 s. Declaration (complex-analysis) removed.
- synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form: 1 -> 2. Module scalar I_7 (U3; as G3's positive-structure entity): J = I_7 e_1 e_+, c = (e_1 + I_7 e_+)/2, H = S + I_7 A on span{1, I_7}^4 (removes a bare \mathbb{C}^4). Declaration (complex-analysis) removed.
- synthesis.cold-mirror-needs-non-equilibrium-descent: 2 -> 3. Boundary-mode KMS continuation (U2): tau_{beta e_2 e_3}(A) = e^{-beta H} A e^{beta H}, the unit written out as e_2 e_3 because J names the mode set. Declaration (complex-analysis) removed.
- synthesis.imported-alvarez-gaume-witten-local-anomalies: 2 -> 3. tr e^{iF/2pi} -> tr e^{I_4 F/2pi} (U1/U4, matrix entries in span{1, I_4}); source form to source_formal. Declaration (imported) removed.
- synthesis.imported-bochner-theorem-moment-lemma-and-whitney-even-functions: 1 -> 2. f: R -> span{1, I_4}, e^{-I_4 nu tau} (U1/U4); source form to source_formal; unit_note updated. Declaration (imported) removed.
- synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field: 2 -> 3. Dimock's factor -i in u = -i S p' gamma u_0 -> "a factor -I_4, the field's unit on spinor values" (U1/U4); source form to source_formal. Declaration (imported) removed.
- synthesis.imported-dirac-hadamard-form-propagates-and-adiabatic-states-are-hadamard: 2 -> 3. Clause (d): nabla-slash + im -> nabla-slash + I_5 m and fibres C^r -> span{1, I_5}^r (U3/U4: the bundle's scalar commutes with the Clifford action of vectors); source form to source_formal. Declaration (imported) removed.
- synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem: 1 -> 2. i0 shift written in scalar form with I_4 (U1, U3 allowance), D_+ = -1/(4 pi^2 (Q(xi) - I_4 0 xi_0)), as its users write D_+ = int e^{-I_4 k.xi}; says the vector-shift unit would be I_5. Source form to source_formal. Declaration (imported) removed.
- synthesis.imported-hadamard-parametrix-of-the-squared-dirac-operator-leads-with-van-vleck-root-times-spin-transport: 3 -> 4. i0 prescription -> I_5 0 prescription (U3/U4), flat regularisation (1/2) Q(x - x' - eps I_5 e_0) named; the right unit R_{I_4} of (b) unchanged, said to act elsewhere. Source form to source_formal. Declaration (imported) removed.
- synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem: 2 -> 3. Delta^{it} -> Delta^{I_4 t} (U1/U4, abstract Hilbert space scalars span{1, I_4}); says J is the modular conjugation. Source form to source_formal. Declaration (imported) removed.
- synthesis.imported-one-loop-integrals-and-pauli-villars-regulators: 1 -> 2. Wick rotation l_0 = I_4 l_{E,0} of the scalar variable, integral values -I_4/(32 pi^2 Delta), I_4/(16 pi^2)(...), photon propagator -I_4/(k^2 + I_4 0) (U1/U4; right unit on non-even values stated). Source form to source_formal. Declaration (imported) removed.
- synthesis.locality-of-the-attached-free-fields-fixes-their-statistics: 3 -> 4. i0 -> I_4 0 in scalar form (U1, the entity's own unit for D_+). Declaration (complex-analysis) removed.
- synthesis.modular-period-on-values-is-the-dual-plane-turn: 3 -> 4. (iii) phase flow on the completed pair a -> e^{-J w lambda} a (U2); says J acts in (iii), I_4 in (i)-(ii). Declaration (complex-analysis) removed.
- synthesis.one-loop-qed-in-the-spacetime-algebra: 3 -> 4. Matrix reading's scalar -> I_5 (U3/U5): I_5 gamma_0..gamma_3, -I_5 sigma^{mu nu} q_nu; says through (1+e)/2 it is the right unit x I_4. Declaration (bridge) kept: Dirac matrices are still named (galang pattern), reason narrowed.
- synthesis.positive-conformal-energy-gives-positive-null-translations: 6 -> 7. Generators -I_4 d pi(Y) on the GNS space (U1, abstract Hilbert space). Declaration (complex-analysis) removed.
- synthesis.positive-energy-selects-rule-2-sign: 3 -> 4. Spectrum condition generator -I_4 d pi(X) (U1, abstract Hilbert space). Declaration (complex-analysis) removed.
- synthesis.residues-zero-four-real-chirality-anomaly: 2 -> 3. +-i eigenspaces of the complex structure I at residues 2, 6 -> +-I_W on S + I_W S, I_W = I e central in the odd extension (U3); says I_W and I differ. Declaration (other) removed.
- synthesis.rule-2-fusing-plane-lorentzian: 2 (unchanged). No bare i; the declaration (other) is for the name C as the isomorphism type of span{1, omega x}, whose unit is already the volume element. Left for Leon (it could probably go, since \C is not flagged and the unit is named).
- synthesis.tower-charge-sector-label-temperature-not: 3 -> 4. Boundary-mode charge rotations (U2): a_j -> e^{theta e_2 e_3} a_j, e^{theta e_2 e_3 Q_F}, the unit written out as e_2 e_3 because J names the mode set here. Declaration (complex-analysis) removed.
- synthesis.triangle-anomaly-in-the-spacetime-algebra-is-the-pseudoscalar-part-of-the-field-square-and-cancels-per-generation: 3 -> 4. Dirac matrices over Q(i) -> over span_Q{1, I_5} (U3/U5). Declaration (bridge) kept for the named Dirac matrices, reason narrowed.
- synthesis.univalence-even-extension-split: 2 -> 3. Completed modes' Killing flow (U2): Ad(e^{J t omega_k N_k}), alpha_{Jp}, mode factor over span{1, J}. Declaration (complex-analysis) removed.
- synthesis.univalence-from-even-stationary-dynamics: 3 -> 4. Boundary-mode Fock space (U2): e_{2k} = J(a_k^* - a_k), (-J)^n B_1...B_n, Ad(e^{J theta N_k}), e^{J pi N_k} = 1 - 2N_k, Ad(e^{JtH}), Ad(rho^{Jt}). Declaration (complex-analysis) removed.
- synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics: 3 -> 4. Borchers' relation Delta^{I_4 t} (U1; the entity's unit of (iv); as the restated Fact). Declaration (complex-analysis) removed.

## Could not resolve
- scrambling.imported-modes-modular-inventory (U6). Formal level and proof: "the continuation's generator i sigma lies outside the real algebra" (T5 Prop. 7.21(3), which says outside Cl(1,3)). Every pseudoscalar choice changes the claim:
  - The atom's unit J (U2) gives J sigma = I_4.
  - I_4 gives I_4 sigma = e_2 e_3.
  - Both of these lie in Cl(1,3), so either one makes the statement false.
  - The central I_5 of Cl(2,3) would keep the statement true, but it would give the complexified atom a unit other than the J that U2 assigns to it.
  - The declaration (complex-analysis) is kept with this narrowed reason. The text and version are unchanged.
  - The same tension sits in G1's singularity.euclidean-rotor-where-it-lies (3), which this entity restates.

## Possible errors found
- None in the mathematics. Points for Leon to rule on:
  1. note.singularity.euclidean-reading-sign-flagged now writes R_{J theta} and R_{2 pi J} for the rotor of singularity.euclidean-rotor-where-it-lies (2) (G1's entity).
     - With J, R_{J theta} = exp(J theta sigma/2) = exp(I_4 theta/2) is an element of the real algebra Cl(1,3), which sits uneasily with that entity's clause (3) ("i sigma is not an element of Cl(1,3)").
     - The note only uses (2) and the period, which hold with J. If G1 keeps R_{i theta}, the note's notation will differ from its source.
  2. singularity.kms-uniqueness-factor and singularity.modular-theory-matrix-factor-proved-outright are stated over span{1, I_4} (U1, abstract matrix factors), but they are used on the atom over span{1, J}.
     - The core result uses them that way, and so do singularity.two-kms-functionals-sign and singularity.modular-descent.
     - The users now say that they read the lemma over span{1, J}. This is a transfer through the field isomorphism, which identifies no two units, but Leon may prefer the lemmas stated for a general complex field span{1, u}.
  3. correspondence.lorentzian-duality-complex-structure is stated with I_5 (odd extension of the 4-space). correspondence.chirality-split-ordering-insensitivity-asd-sector applies it inside so(2,4)_C with I_7, and says so.
  4. The i0 shift of the massless two-point function is written in scalar form with I_4, both in synthesis.imported-free-field-spin-statistics-and-guido-longo-theorem and in its user synthesis.locality-of-the-attached-free-fields-fixes-their-statistics.
     - The reason: the user writes D_+ = int e^{-I_4 k.xi}, and RESOLVE U3 allows the scalar form.
     - The Hadamard-parametrix Fact writes its regularisation as a vector shift with I_5. Leon may want one choice.
  5. In synthesis.positive-energy-selects-rule-2-sign, synthesis.clifford-conjugation-..., dark-matter.premise-flag-as-datum and the Kuckert Fact, the letter J already names other objects:
     - a complex structure (1/2) ad(Z);
     - the involution I_7 e_1 e_+;
     - an orthogonal complex structure;
     - a modular conjugation.
     - None of these is U2's J, and none was renamed. In the two boundary-mode entities (cold mirror, tower charge) J names the mode set, so the unit is written e_2 e_3.
  6. synthesis.rule-2-fusing-plane-lorentzian keeps its declaration (other). It is not about a bare i but about the name C for span{1, omega x}, whose unit is already the volume element; it could probably be dropped.
  7. rule2.rule-2-kaluza-klein-algebra (gamma matrices), synthesis.one-loop-qed-... and synthesis.triangle-anomaly-... keep bridge declarations only because Dirac matrices are named.
  8. Detector false positives that had been masked by declarations were fixed by renaming index letters, which changes no meaning:
     - |ij>, (i - j) in the matrix-factor and Schmidt lemmas;
     - \text{i.e.} inside math in the Fock model proof.

## Validation
`tp check --layers 1,2,3 --keep-going --author leon` gives no error or warning on any G5 entity. The 8 I213 infos are the same as in baseline.log. The detector finds no bare unit left except in scrambling.imported-modes-modular-inventory (declared, U6).

## Addendum: coordinator ruling on the Euclidean rotor
This applies the same ruling as for G1's singularity.euclidean-rotor-where-it-lies (3). T05 Prop. 7.21(3) concerns the continued rotor acting on spacetime vectors, the (rho, tau) plane. So by U3 the unit is I_5, the central pseudoscalar of Cl(2,3).
- scrambling.imported-modes-modular-inventory: 4 -> 5. The U6 entry above is withdrawn.
  - In the formal and technical levels and the proof, i sigma is now written I_5 sigma, and the text says it lies outside the real algebra Cl(1,3). This cites std-algebra.complexification-is-the-odd-extension.
  - One sentence is added: on the atom's modes the unit is J, and the continued flow there is conjugation by e^{I_4 theta/2}, a different object.
  - The source's form is now in source_formal. The declaration (complex-analysis) is removed.
- note.singularity.euclidean-reading-sign-flagged: 3 -> 4.
  - The Euclidean rotation of the (rho, tau) plane is now written R_{I_5 theta} = cos(theta/2) + I_5 sigma sin(theta/2). The text says it is not R_{J theta}, which equals e^{I_4 theta/2} in Cl(1,3).
  - The sign remark now reads R_{2 pi I_5} = -1, which holds.
  - This replaces the R_{J theta} reading of the first edit.
- tp check (layers 1, 2, 3): 0 errors and 0 warnings store-wide. The only finding on either entity is the I213 info on scrambling, which was already there before.

Could not resolve (G5): none now.
