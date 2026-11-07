# Sweep E: imaginary units the first detector missed (2026-11-07)

43 entities. 1 fully replaced, 34 declared (2 of them after a partial replacement), 8 unchanged (index-letter or text false positives only).
Validation: `tp check --layers 1,2,3` shows no error or warning on any E entity (only the pre-existing I213 notes, also in baseline.log). Extended re-scan (i followed by a letter or macro, plus the original detector): every remaining hit is on a declared entity or is an index letter.

The deciding point for most of this group: the boundary-mode algebra's defining object (obj.hawking.boundary-mode-algebra-windows-boost-dynamics, declared complex-analysis in pass A or D1) says its unit is not shown to be I_4. Its modes descend from the atom of the radial plane and anticommute with I_4 (conventions, known limits 1 and 2). Under rule 4 the store therefore does not tie these spaces to the field's unit, so I declared every phase or modular flow on boundary modes, atoms, windows or generic matrix factors.

## Replaced

- synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching, 2 -> 3: proof (ii), positive-frequency mode $u = e^{-is}/\sqrt2$ becomes $e^{-I_4 s}/\sqrt2$ (field theory's unit; numbers read in span{1, I_4}); nothing stays (the $\omega^{ij}$, $R^{ij}$ hits are indices).

## Declared

- angle.imported-singularity-papers-state-selection, 10 -> 11: $\operatorname{Ad}(e^{itK})$ on the boundary mode factor; complex-analysis.
- angle.imported-theorems-deliver-their-hypotheses, 1 -> 2: Borchers, Bisognano-Wichmann $\Delta^{it}$ as quoted; imported.
- dark-energy.acoustic-no-go-one-way-grip, 3 -> 4: U(1) characters $e^{iq\vartheta}$ on the s-wave boundary-mode current algebra; complex-analysis (Unsure 1).
- hawking.gibbs-states-are-kms-conversely-finite, 2 -> 3: $\operatorname{Ad}(e^{itH})$, $\alpha_{i\beta}$ on a general $\End(\C^m)$; complex-analysis.
- hawking.imported-modular-descent-premises-geometric-normalisation, 6 -> 7: $\operatorname{Ad}(e^{it\sigma/2})$ of the completed pair; complex-analysis.
- note.correspondence.abstract, 1 -> 2: replaced, $\omega = ix\pi$ -> $\omega = I_6\hat x\pi$ with "(Penrose's $\omega = ix\pi$)", and "the factor $i$" -> "the factor $I_6$, the complex unit of $\CS$". Stays: Penrose's quoted form; bridge.
- note.correspondence.setting-successor-problems, 1 -> 2: replaced, the same rewrite in problem (2). Stays: Penrose's quoted form; bridge.
- note.correspondence.what-factor-i-what-remains-conventional, 2 -> 3: stays Penrose's $i$ beside the derived $I_6$ (already written that way); bridge.
- note.singularity.euclidean-reading-sign-flagged, 1 -> 2: stays $R_{i\theta}$, $R_{2\pi i} = -1$, the Euclidean rotation of the $(\varrho,\tau)$ plane; complex-analysis (Unsure 3).
- obj.hawking.continuum-mode-space, 1 -> 2: stays $a(e^{ith}f)$ on a general complex $\mathfrak h$ whose countable case is the declared boundary-mode algebra; complex-analysis (Unsure 2).
- obj.singularity.geometric-modular-condition-g, 2 -> 3: stays $\operatorname{Ad}(e^{itK_{\mathrm{geo}}})$, contrasted in the text with the real rotor flow; complex-analysis.
- obj.synthesis.cosmological-horizon-boundary-modes, 1 -> 2: stays $e^{-it\omega_j}v_j$ on the complexification of $\Cl(|J|,|J|)$; complex-analysis.
- singularity.kms-uniqueness-factor, 4 -> 5: stays $\operatorname{Ad}(e^{itK})$, $\alpha_{i\beta}$ on a general matrix factor; complex-analysis.
- singularity.matching-steps-4b-4c-join-equation, 5 -> 6: stays $\operatorname{Ad}(e^{it\sigma/2})$; complex-analysis.
- singularity.modular-descent, 5 -> 6: stays $\operatorname{Ad}(e^{it\sigma/2})$, $\operatorname{Ad}(\rho^{it})$; complex-analysis.
- singularity.rate-discharge-hypothesis-iii, 4 -> 5: stays $e^{\mp it\omega}$ on the atom mode; complex-analysis.
- singularity.rate-rigidity-temperature-not-algebra-intrinsic, 4 -> 5: stays $\operatorname{Ad}(e^{itK})$ and the determinant argument; complex-analysis.
- singularity.two-kms-functionals-sign, 5 -> 6: stays $\operatorname{Ad}(e^{it\omega K})$, $\alpha_{i\beta}$; complex-analysis.
- std-algebra.bivector-exponential, 1 -> 2: stays the lay comparison with $e^{i\theta}$ in the complex plane; bridge.
- synthesis.affine-cell-boost-spreads-without-scrambling, 1 -> 2: stays Borchers' relation quoted from the imported Fact; complex-analysis.
- synthesis.boundary-mode-locality-is-descent-covariance, 1 -> 2: stays $\operatorname{Ad}(e^{itH})$ on windows (the $n_{\mathrm{in}}$ hit is text); complex-analysis.
- synthesis.clausius-heat-exceeds-created-modes-killing-energy, 2 -> 3: stays $\operatorname{Ad}(e^{itH_F})$ on $\End(\Lambda^\bullet\C^F)$ (the $\mathrm{inst}$ hits are text); complex-analysis.
- synthesis.cold-mirror-needs-non-equilibrium-descent, 1 -> 2: stays $\tau_{i\beta}$ in the check description; complex-analysis.
- synthesis.collar-kms-extension-completion-locus, 1 -> 2: stays $\operatorname{Ad}(e^{isf(r)K_P})$ on atoms; complex-analysis.
- synthesis.collar-kms-extension-three-flows, 1 -> 2: stays $\operatorname{Ad}(e^{itf(r_k)K_k})$ on atoms; complex-analysis.
- synthesis.collar-temperature-fixed-locally-by-r-loc, 2 -> 3: stays $\operatorname{Ad}(e^{\pm isK})$ on $\Cl(1,3)_\C$, $\Mat_2(\C)$; complex-analysis.
- synthesis.de-sitter-temperature-frozen-point-norm, 5 -> 6: stays $e^{\mp it\omega}$ on the cosmological boundary modes; complex-analysis.
- synthesis.imported-alvarez-gaume-witten-local-anomalies, 1 -> 2: stays $e^{iF/2\pi}$ as quoted; imported.
- synthesis.imported-buchholz-florig-summers-geometric-modular-action-and-modular-stability, 1 -> 2: stays $\Delta_W^{it}$ as quoted; imported.
- synthesis.imported-kuckert-modular-pct-spin-statistics-and-borchers-theorem, 1 -> 2: stays $\Delta^{it}$, Borchers as quoted; imported.
- synthesis.killing-clock-weights-binary-residue, 3 -> 4: stays $\operatorname{Ad}(e^{it\sum\omega_jK_j})$; complex-analysis.
- synthesis.r-le-i-independent-spectrum-condition-separates, 2 -> 3: stays $\operatorname{Ad}(e^{it\omega_kK_k})$, $ip$, Jordan-Wigner on $\C^2\otimes\C^2$; complex-analysis.
- synthesis.r-loc-independent-sets-matter-coupling, 3 -> 4: stays $a_j \mapsto e^{-isw_j}a_j$ on a local-horizon window; complex-analysis (Unsure 4).
- synthesis.wedge-reflections-compose-to-the-two-pi-rotor-so-geometric-modular-conjugations-give-interacting-spin-statistics, 2 -> 3: stays Borchers' relation for an interacting net; complex-analysis.

## Unchanged (false positives only)

dark-energy.variable-exponents-residue-pointwise-corrections-are ($\omega^{ij}$, $e^i$), interior.covariant-form-vacuum-equations ("that is" in \text), note.mass.setting-successor-problems, synthesis.massless-composites-de-sitter-conformal-boundary, synthesis.slot-covariance-forces-gram-square, synthesis.three-twistor-composites-massive (all $B^{il}_\Lambda$), synthesis.inverse-problem-for-the-clausius-route ($a^{ij}$), synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law ($g^{ij}$).

## Possible errors found

1. Inconsistency outside group E: synthesis.point-spectrum-boost-admits-no-half-sided-translations, from another group, now writes the boundary-mode unit as I_4 ("the unit of the mode space is $I_4$", $\operatorname{Ad}(e^{I_4 tK})$, $\Delta^{I_4 s}$). The defining object obj.hawking.boundary-mode-algebra-windows-boost-dynamics was declared instead, and so were these 30-odd E entities and my D2 entities.
   - This is more than notation. If $I_4$ is read as an algebra element multiplying from the left, and the mode $v$ anticommutes with $I_4$ (atom modes, limit 1), then $\operatorname{Ad}(e^{I_4 t\sigma/2})$ is the identity on $v$. The reason is that $I_4\sigma$ is a bivector of the dual plane, which commutes with $v$.
   - Also, $\operatorname{Ad}(e^{I_4 tK})$ then depends on the constant in $K = \sum\omega_j(N_j - \tfrac12)$, so the stored remark "a multiple of the identity does not change Ad" fails.
   - Only a right unit on the GNS module (rule 1's right unit, commuting with every left action) reproduces the complex phase.
   - Leon should rule on one reading for the whole store.
2. Detector: besides $i$ followed by a letter, the extended pattern still counts index superscripts ($\omega^{ij}$, $B^{il}$, $g^{ij}$) and \text words. All checked by hand.

## Unsure (for Leon)

1. All boundary-mode, atom and window flows (the large complex-analysis block above, and D2's synthesis.tower-charge-sector-label-temperature-not and synthesis.univalence-from-even-stationary-dynamics). They can become $I_4$ if Leon rules that the unit of these GNS spaces is the right unit $x \mapsto xI_4$, and says so once per entity. As a left algebra element they cannot (Possible error 1). dark-energy.acoustic-no-go-one-way-grip's $e^{iq\vartheta}$ belongs here too.
2. obj.hawking.continuum-mode-space: SWEEP rule 4 names "the continuum mode space of a horizon" as built from GA modes with unit $I_4$, and synthesis.positive-null-energy-gives-r-premises (another group) wrote it so. But this object is a general complex $\mathfrak h$ whose countable case is the declared boundary-mode algebra, so I declared it. If Leon follows rule 4 as written, $\tau_t(a(f)) = a(e^{I_4 th}f)$ with "(the unit of $\mathfrak h$ is the field's unit $I_4$)" is the replacement.
3. note.singularity.euclidean-reading-sign-flagged: rule 5 says write an imaginary-rapidity boost as the dual-plane rotation $I_4B$. Here $R_{i\theta}$ is the Euclidean rotation of the same $(\varrho,\tau)$ plane, which singularity.euclidean-rotor-where-it-lies (3) says no real rotor of $\Cl(1,3)$ realises. $I_4B$ would rotate a different plane, so I kept $i$.
4. synthesis.r-loc-independent-sets-matter-coupling: the window of local-horizon modes may be the field's canonical null component, whose unit Definition obj.field-theory.single-algebra-field fixes as $I_4$; synthesis.boost-evolution-on-generators-is-one-unitary-group was replaced on that basis. The entity does not say which modes it means, so I declared it.
