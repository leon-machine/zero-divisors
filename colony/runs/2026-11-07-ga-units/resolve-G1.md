# Resolve sweep, group G1 (unit principle U1-U6, maintainer pass 2026-11-07)

32 of 33 entities changed. Each one got a version bump relative to its current (re-locked) version, a credit entry for the new version and an extraction note `maintainer_pass_resolve_units`. One entity was left unchanged (only false positives). 31 declarations were removed. 1 was kept with a narrower reason (singularity.euclidean-rotor-where-it-lies, clause (3)).

Validation: `tp check --layers 1,2,3 --keep-going --author leon` reports no error or warning on any G1 entity. The two I213 findings (matching-steps-4b-4c, boundary-mode-locality) are informational and were already in baseline.log. The detector re-scan finds no bare i except in the kept clause and the false positive i^{-+} (timelike infinity).

Units used:
- J = e_2 e_3: the completed-pair atom and the boundary modes (U2). On the tower model, J also commutes with the further modes, because tower planes are orthogonal to spacetime.
- I_5 = I_4 e of Cl(2,3): every case where the unit must commute with all vectors (U3).
- hat-I = I_V e: the cosmological boundary modes (U3, matching G2's premise R_Lambda).
- I_4: abstract Hilbert spaces and the continuum (U1).

## Per entity (old -> new version; unit; declaration)
- angle.imported-singularity-papers-state-selection: 11 -> 12. J, for the phase flow Ad(e^{JtK}) on the horizon pair (U2). Removed.
- angle.imported-theorems-deliver-their-hypotheses: 2 -> 3. U4 with I_4: Delta^{I_4 t}, Hilbert-space scalars in span{1, I_4}. Original formal moved to source_formal with "the sources write i for I_4". Removed.
- angle.wedge-reflection-translations-are-ascent: 3 -> 4. I_5 (U3): eta = I_5 pi/2 and rotor I_5 B, whose twisted action is exactly BxB. Pinned uses edge std-algebra.complexification-is-the-odd-extension@1 added, because the proof uses I_5 central with square -1. Removed.
- hawking.i-state: 3 -> 4. J: alpha_{J beta}, which equals Ad(e^{-beta K}) on each mode. The false positive "\text{i.e.}" is now "\text{that is}". Removed.
- note.angle.abstract: 1 -> 2. I_5 pi (U3). Removed.
- note.angle.setting-claim-kill-conditions-fixed-before-2: 1 -> 2. I_5 pi in K4 (U3). Removed.
- note.angle.what-supplies-what-it-does-not: 1 -> 2. U4 with I_5. Source form moved to source_formal ("source writes i for this unit"). Removed.
- note.decisions.two-boost-flows: 2 -> 3. J: Ad(e^{JtK}), e^{-J omega_j t}, rho^{Jt}, lambda = Jt, R_{J theta} = exp(theta I_4/2). Removed.
- note.pairing.setting-transport-moves-vacuum-transverse-derivative: 1 -> 2. I_5: m = e_2 + I_5 e_3. Removed.
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics: 2 -> 3. The transverse unit, written e_2 e_3 because J is this definition's mode set: tau_t(a_j) = e^{-e_2e_3 omega_j t} a_j. Scalars are in span{1, e_2e_3}. Removed.
- obj.singularity.geometric-modular-condition-g: 3 -> 4. J: Ad(e^{J t K_geo}). Removed.
- obj.synthesis.cosmological-horizon-boundary-modes: 2 -> 3. hat-I = I_V e (U3, Q(e) = -1, so the algebra is Cl(|J|,|J|+1)). States once that hat-I is not identified with J. Removed.
- pairing.pairing-functional-pair-creation-amplitude: 5 -> 6. I_5: Fock-module scalars span{1, I_5}, and so(4,C) is the bivectors complexified by I_5. Removed.
- pairing.regular-frame-class-vanishes-horizon-changes: 5 -> 6. I_5: classes -I_5(1-beta)/r and +I_5(1+beta)/r. Removed.
- pairing.static-frame-only-expansion-survives: 6 -> 7. I_5: class -I_5 sqrt(f)/r, and the inner product is extended bilinearly in the proof. Removed.
- singularity.euclidean-rotor-where-it-lies: 4 -> 5. J in clauses (1) and (2), the note and the one-liner: R_{J theta} = cos + J sigma sin, J sigma = I_4, diag(e^{-+J theta/2}). Pinned uses edge to the transverse-bivector result @1 added. The note now says, as the coordinator asked, that exp(theta J/2) acts on values and exp(theta I_4/2) acts on mode operators. **Kept (complex-analysis), narrowed to clause (3)** (see below).
- singularity.euclidean-section-period: 5 -> 6. I_5: t_s = -I_5 tau, because the continued coordinate multiplies e_0 (U3). "i.e." is now "that is". Removed.
- singularity.matching-steps-4b-4c-join-equation: 6 -> 7. J: Ad(e^{J t sigma/2}). Also says that J, which equals the excluded dual I sigma_r as an element, is the flow's scalar and not its bivector. Removed.
- singularity.r-regularity-fixed-locus: 3 -> 4. J: Ad(e^{J t omega_k K_k}), F(t + Jp) = omega(alpha_t(b) a). The strip's J and the Euclidean section's I_5 are matched through the real period and are not identified. Removed.
- singularity.rate-discharge-hypothesis-iii: 5 -> 6. J: e^{-J t omega} v, F(t + Jp). Removed.
- singularity.rate-rigidity-temperature-not-algebra-intrinsic: 5 -> 6. J: Ad(e^{JtK}), with determinants taken over span{1, J}. Removed.
- state-selection.euclidean-partner-curvature-selected: 4 -> 5. I_4 in (3) (U1: the continuation multiplies the even rotor, as the proof's "differ by the factor I" already says). Clause (4) keeps I_6, and the entity says which acts where. Removed.
- state-selection.rate-discharge-hypothesis-iii: 9 -> 10. J for the phase flow and the strip J beta. The continuation on spinors is lambda -> I_6 theta. The units are matched through the real parameter and not identified. Removed.
- synthesis.affine-cell-boost-spreads-without-scrambling: 2 -> 3. I_4: Delta^{I_4 t}, the complex structure of the continuum mode space. Removed.
- synthesis.boost-evolution-on-generators-is-one-unitary-group: 3 -> 4. J for the quoted window dynamics; the continuum keeps I_4. The comparison is of frequencies, not of units. Removed.
- synthesis.boundary-mode-locality-is-descent-covariance: 2 -> 3. J: Ad(e^{JtH}), e^{JtH} = cos(tH) + J sin(tH). Removed.
- synthesis.boundary-mode-premises-finite-models: 3 -> 4. J for every flow, gauge phase and modular group. Matrix entries are in span{1, J}. Removed.
- synthesis.collar-isotropy-selects-t-boost: 1 -> 2. I_5: the frame atom Cl(1,3)_C = Cl(2,3), K = (B_b + I_5 B_c)/2, I_5* = -I_5 computed in the proof. Says this unit is not the modes' J. Pinned uses edge to the odd-extension result @1 added. Removed.
- synthesis.collar-kms-extension-completion-locus: 2 -> 3. J: Ad(e^{J s f(r) K_P}). Removed.
- synthesis.collar-kms-extension-three-flows: 2 -> 3. J: Ad(e^{J t f(r_k) K_k}). Removed.
- synthesis.collar-temperature-fixed-locally-by-r-loc: 3 -> 4. J: Ad(e^{+-J s K}), with Mat_2(C) over span{1, J}. Removed.
- synthesis.de-sitter-temperature-frozen-point-norm: 6 -> 7. hat-I, as in its defining object: e^{-hat-I t omega}. Removed.
- synthesis.cosmological-horizon-completed-pair: unchanged (3). The only hit is i^{-+}, the observer's endpoints at timelike infinity. It has no declaration and needs none.

## Could not resolve
- singularity.euclidean-rotor-where-it-lies, clause (3): its first sentence, the matching sentence in the technical level, and step (3) of the proof. The clause says "the generator i sigma is not an element of the real algebra Cl(1,3)" and "realised by the unitary R_{i theta}". With the atom's unit J (U2, the coordinator's ruling) the generator is J sigma = I_4, which lies in Cl(1,3), so the sentence would become false. Its conclusion still holds: R_{J theta} = e^{I_4 theta/2} is no rotor. With I_5 (U3) the clause holds exactly as stated (I_5 sigma = e_2 e_3 e, outside Cl(1,3)), but I_5 is not the atom's unit. The clause keeps the source's formal unit i, and the declaration says so. Leon to rule: restate clause (3) with J (no longer "not in Cl(1,3)" but "not a bivector, so no rotor"), or read this entity's complexification with I_5.

## Possible errors found
None in the mathematics. Three readings are for Leon to check:
1. state-selection.euclidean-partner-curvature-selected (3): with I_4 the continuation exp(I_4 theta sigma_r/2) is R_theta itself, so the clause's "in the sense that" now holds as an identity. The statement is unchanged, but the reading is stronger than the old formal unit gave.
2. state-selection.rate-discharge-hypothesis-iii, proof: the step carrying the KMS strip translation to the spinor rotation angle uses two units, J on the modes and I_6 on spinors. They are matched only through the real parameter. In the source one i did both jobs, so the step's justification is exposed rather than changed.
3. note.decisions.two-boost-flows: "whose generator is not in the real algebra" is now read as the atom's real algebra Cl(1,1) (true with J). The euclidean-rotor proposition's own clause (3) still speaks of Cl(1,3) in its formal unit.

Store consistency: the store now has hat-I (cosmological horizon, U3), J (Schwarzschild boundary modes and windows, U2) and I_5 (frame atom, complex vectors, Wick rotation, wedge reflection). Each entity says which unit it uses, and none identifies two of them.
