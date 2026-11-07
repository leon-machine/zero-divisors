# Sweep A1: the imaginary unit and the GA pseudoscalar (maintainer pass 2026-11-07)

Totals: 1 entity changed (text, version bumped), 26 declared only (outside_ga plus the
`maintainer_pass_ga_units` extraction note; formal levels and proofs untouched, so no version bump and no
credit entry, since outside_ga and extraction are not substantive fields), 3 unchanged.
Validation (`tp check --layers 1,2,3 --keep-going --author leon`): no findings on any A1 entity.
Detector re-scan: every A1 entity still listed carries outside_ga, except
synthesis.cosmological-horizon-completed-pair (only $i^{\pm}$, timelike infinity: false positives).

## Per entity

- synthesis.boost-evolution-on-generators-is-one-unitary-group: 2 -> 3. Replaced by $I_4$ (the field's operator unit on even values, obj.field-theory.single-algebra-field, which the entity is about): Mellin modes $|u|^{-1/2 + I_4w}$, $D_\lambda f_w = e^{-I_4 w\lambda}f_w$, phase flow $e^{-I_4\kappa wt}$, $s \in \mathrm{span}\{1, I_4\}$, $\lambda = I_4\theta$, value rotor $B_{I_4\theta} = \cos + I_4e_1e_0\sin$ with $B_{I_4\theta}\Lambda(m) = e^{-I_4\theta/2}\Lambda(m)$ ($\Lambda(m)$ even), $u \mapsto e^{-I_4\theta}u$ into $\mathrm{span}\{1, I_4\}$, factor $-I_4$ at $\theta = \pi$, $e^{-I_4w(I_4\theta)} = e^{w\theta}$; "numbers are read in span{1, I_4}" added at first use. The proof's quoted window formula $a_j \mapsto e^{-i\omega_jt}a_j$ is now cited in words (the windows keep their own $i$). Nothing stays; not declared.
- angle.wedge-reflection-translations-are-ascent: 3 (unchanged). Stays: $\eta = i\pi/2$, rotor $iB$, $(iB)x(-iB) = BxB$. With $I_4$ the rotor $I_4B$ acts by $-BxB$ (dual-plane turn), not the wedge reflection. complex-analysis.
- hawking.i-state: 3. Stays: $\alpha_{i\beta}$ in the proof (KMS continuation in the complex boundary-mode algebra); the formal "i.e." is a false positive. complex-analysis.
- note.angle.abstract: 1. Stays: boost rotor at imaginary rapidity $i\pi$ (commuting scalar; $I_4$ would give the dual-plane turn). complex-analysis.
- note.angle.setting-claim-kill-conditions-fixed-before-2: 1. Stays: K4's rapidity $i\pi$, same reason. complex-analysis.
- note.angle.what-supplies-what-it-does-not: 1. Stays: Bisognano-Wichmann's "boost at rapidity $i\pi$" as its source states it. imported.
- note.decisions.two-boost-flows: 2. Stays: phase flow $e^{-i\omega_jt}$, $\mathrm{Ad}(e^{itK})$, $\lambda = it$, $R_{i\theta}$, $i\sigma$, $\rho^{it}$. The atom lies in the spacetime radial plane (I_4 anticommutes with its modes, conventions limit 1), and the note's claim "i sigma is not in the real algebra" would be false of $I_4\sigma$. complex-analysis.
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics: 2. Stays: $\tau_t(a_j) = e^{-i\omega_jt}a_j$ (all levels), $\End(\Lambda^\bullet\C^F)$. Defined over $\C$; modes descend from T05's atom (conventions limits 1, 2). complex-analysis.
- pairing.pairing-functional-pair-creation-amplitude: 5. Stays: $\so(4,\C)$ and the entries $0, \pm1, \pm i$ of the complex Fock matrices of $e_0..e_3$ (plain complexification, must commute with vectors). other.
- pairing.regular-frame-class-vanishes-horizon-changes: 5. Stays: classes $-i(1-\beta)/r$, $+i(1+\beta)/r$ on $m = e_2 + ie_3$ (complexified tangent space). other.
- pairing.static-frame-only-expansion-survives: 6. Stays: $-i\sqrt f/r$, $e_2 + ie_3$. other.
- singularity.euclidean-rotor-where-it-lies: 4. Stays: $\lambda = i\theta$, $R_{i\theta}$, $i\sigma$, $\mathrm{diag}(e^{\mp i\theta/2})$ in $\Mat_2(\C)$; clause (3) is exactly that $i\sigma \ne I_4\sigma_r$ (its existing note on values already gives the $I_4$ reading). complex-analysis.
- singularity.euclidean-section-period: 5. Stays: Wick rotation $t_s = -i\tau$ of a coordinate; "i.e." false positive. complex-analysis.
- singularity.r-regularity-fixed-locus: 3. Stays: KMS strip $F_{a,b}(t + ip)$ and $\mathrm{Ad}(e^{it\omega_kK_k})$ on T05's atom ladders (anticommute with $I_4$). complex-analysis.
- state-selection.euclidean-partner-curvature-selected: 4. Stays: $\lambda \mapsto i\theta$ (unit unfixed in (3), read as $I_6$ in (4)). complex-analysis.
- state-selection.rate-discharge-hypothesis-iii: 9. Stays: $i\beta$ (KMS strip), $\lambda \mapsto i\theta$ in the proof. complex-analysis.
- synthesis.boundary-mode-premises-finite-models: 3. Stays: $\Ad(e^{it\omega_kK_k})$, $e^{i\theta}v_k$ on T05's atoms $\Mat_2(\C)$; index letters $i, j$ false positives. complex-analysis.
- synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature: 1. Stays: kernels $\tfrac{i}{2\pi}(\lambda_1 - \lambda_2 + i0)^{-1}$, KMS continuation $-i\beta$, deficiency indices of $i\,d/d\lambda$. complex-analysis.
- synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet: 1. Stays: $1/(U - U' + i0)$, its powers, Mellin $|u|^{-1/2+iw}$. complex-analysis.
- synthesis.collar-isotropy-selects-t-boost: 1. Stays: $K = \tfrac12(B_b + iB_c)$, $\mathrm{Ad}(e^{itK})$ in $\Cl(1,3)_\C$ (acts on odd elements, where $I_4$ anticommutes). other.
- synthesis.cosmological-horizon-completed-pair: unchanged; only $i^{\pm}$ (timelike infinity).
- synthesis.dirac-causal-propagator-between-nearby-null-leaves-tends-to-the-generator-car-on-every-geodesic-null-hypersurface: 2. Stays: generator kernels, $\sigma + i\epsilon(t(x) - t(x'))$, $\log(is)$, boundary values. complex-analysis.
- synthesis.dirac-states-restrict-to-null-hypersurfaces-through-the-flux-contraction-and-are-thin-layer-limits-under-the-generator-car: 2. Stays: kernels, $i\epsilon$ regularisations, $(U_1 - U_2 - i\epsilon)^{-2}$. complex-analysis.
- synthesis.field-strength-cancels-from-the-leading-null-singularity-of-hadamard-dirac-states-on-null-hypersurfaces: 3. Stays: kernels, $\sigma + i\epsilon s$, $\log(-is)$, $\log(-i(u - u'))$. complex-analysis.
- synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state: unchanged; existing complex-analysis declaration covers every occurrence.
- synthesis.hadamard-dirac-states-scale-to-the-flat-massless-vacuum-at-every-point-of-a-gravitational-field: 3. Stays: $(iD_x + m_0)H_\pm e_0$, $\tfrac{i}{2\pi^2}(y - y')e_0/Q(y - y' - i0e_0)^2 = i\nabla D_+e_0$, $p = \pm i\nabla$, $e^{\mp ip\cdot z}$. complex-analysis.
- synthesis.hadamard-scaling-limit-premise: 4. Stays: generator kernels and the bulk limit $\pm i\nabla D_\pm e_0$. complex-analysis.
- synthesis.imported-modular-conjugation-of-the-chiral-fermi-field-is-the-twisted-reflection: unchanged; existing imported declaration.
- synthesis.local-normality-at-the-edge-gives-the-null-ground-state: 2. Stays: generator and thermal kernels. complex-analysis.
- synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state: 4. Stays: $W_\beta$, remainders $R$, Fourier integrals $e^{ip(u - v)}$. complex-analysis.

## Possible errors found

- synthesis.boost-evolution-on-generators-is-one-unitary-group, (iii) and proof (iii): the proof's convention makes $a(f)$ antilinear in $f$, so $\alpha(a(f_w)) = a(e^{-I_4\kappa wt}f_w) = e^{+I_4\kappa wt}a(f_w)$, while the text writes $e^{-I_4\kappa wt}a(f_w)$ "of one-particle Hamiltonian $\kappa w$". By that convention the Hamiltonian is $-\kappa w$. The spectrum is all of $\R$ in both readings, so the conclusions are not affected. This sign was already there with $i$; not fixed.

## Unsure (left as $i$, for Leon to rule)

1. The boundary-mode algebra, obj.hawking.boundary-mode-algebra-windows-boost-dynamics and hawking.i-state (also the windows quoted in note.decisions.two-boost-flows). SWEEP rule 4 names "the tower and boundary-mode CAR algebras" among the spaces with unit $I_4$. But the definition is over $\C$ ($\ell^2(J)$, $\End(\Lambda^\bullet\C^F)$), and the store records that T05's atom modes anticommute with $I_4$ and that this algebra is real in the scrambling results (conventions, known limits 1 and 2). So I could not tell that $e^{-I_4\omega_jt}$ preserves the meaning (with anticommuting modes, left and right $I_4$ give opposite phases). The parallel windows entity synthesis.phase-flow-is-time-rotor-flow-kms-continuation, done by another group, also kept $i$. If Leon rules that the ladders are tower or ascended-plane modes, so that $I_4$ commutes with them, the conversion is mechanical: $\tau_t(a_j) = e^{-I_4\omega_jt}a_j$, $\alpha_{I_4\beta}$, and $\C$ read as $\mathrm{span}\{1, I_4\}$.
2. Generator kernels on the continuum mode space. Affected: synthesis.collapse-in-vacuum-..., collapsing-hole-..., dirac-causal-propagator-..., dirac-states-restrict-..., field-strength-cancels-..., hadamard-scaling-limit-premise, local-normality-..., microlocal-..., and geometric-modular-conjugations-... (already declared). I kept $i$ under rule 5 (boundary values, Fourier, Pick and Laplace analysis). The rewrite is exact if one unit is used everywhere: with $P = I_4\,d/du$ the null vacuum kernel is $\tfrac{I_4}{2\pi}(u - v + I_4 0)^{-1}$, because the boundary value comes from the same Fourier exponent. Converting the prefactor alone would split one complex number between two units, so I did neither. Another group has written $P = I_4\,d/du$ in synthesis.n-plus-null-ground-state, so $P = i\,d/du$ in geometric-modular-conjugations (and in the imported Fact, which stays in its source's form) is now notationally out of step with it.
3. Dirac kernels: synthesis.hadamard-dirac-states-scale-... and the bulk clause of hadamard-scaling-limit-premise. Rule 1 calls for the right unit in $(iD_x + m_0)$. The same complex unit also sits in $1/\sigma_\pm$, $Q(y - y' - i0e_0)$ and $e^{-ip\cdot z}$, and the $i0$ shift of a spacetime vector cannot be a pseudoscalar. So I kept $i$ throughout instead of writing the prefactor as $xI_4$ next to an $i$ that the reader would have to identify with it.
4. state-selection.euclidean-partner-curvature-selected (3). Writing $\lambda \mapsto I_4\theta$ would turn "continuation in the sense that both are rotor flows of the pair" into the identity $\exp(I_4\theta\sigma_r/2) = R_\theta$, which is stronger than what is stated. Clause (4) already fixes the unit as $I_6$. I left the statement alone.
5. Imaginary rapidity in angle.wedge-reflection-translations-are-ascent and the three angle notes. Rule 5 says "write the rotation $I_4B$", but $\mathrm{Ad}(I_4B) = -\mathrm{Ad}(B)$ on vectors is the dual-plane turn, while the stated result is the reflection $x \mapsto BxB$. The exact GA form is $\mathrm{Ad}(B) = \mathrm{Ad}(I_4)\circ\mathrm{Ad}(I_4B)$ (synthesis.wedge-reflections-compose-..., (i)). Restating it that way would change the statement, so I kept $i$.
6. The Klein twist $Z = (1 + i\Theta)/(1 + i)$ in geometric-modular-conjugations-... is written with $I_4$ in synthesis.wedge-reflections-compose-..., (iv). It could be converted together with item 2.
