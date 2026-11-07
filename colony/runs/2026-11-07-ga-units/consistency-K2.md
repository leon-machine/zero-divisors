# Consistency pass K2: rulings R3 and R4 (7 November 2026)

31 entities touched (ids in ids_K2.txt, all claimed in claimed.txt before editing). 15 had their text
converted from i to I_4 and their outside_ga declaration removed; 1 previously undeclared entity was
converted; 15 already-converted entities gained R3's one-line reading, with no version change.
Versions follow SWEEP.md: each entity is at most one above its 8eef5a4 version. Entities the sweep had
already bumped were not bumped again, and only their `maintainer_pass_ga_units` note was extended. Every
entity carries a credit entry for its current version.

Validation:
- `tp check --layers 1,2,3 --keep-going --author leon`: 0 errors and 0 warnings store-wide (110 info).
- The one W222 raised along the way (pre-existing words "the Dirac matrices in the matrix reading" in
  one-loop-vacuum-polarisation) was cleared by rewording, as groups B and C1 did.
- The bare-i detector, plus the i-followed-by-a-letter pattern, finds only index letters on these ids:
  `ij` in chart-computation and `p = (i, A)` in face-mass-form, both there before this pass.

The R3 sentence used (with I_4 or I_{4} as the entity writes it): "numbers and the module's complex
structure are read in span{1, I_4}, the module read on the tower's floors, where I_4 commutes with the
tower vectors". No text claims that this reading derives anything about Hypothesis (S).

## R3: declared only because of the module's plain complexification, now converted (declaration removed)

| id | version | what changed |
|---|---|---|
| note.standard-model.setting-content-charges-chirality-2 | 1 -> 2 | y = (3 I_4 1_2, -2 I_4 1_3), lambda = e^{I_4 theta}, action I_4 q; R3 sentence; the identity matrices I_2, I_3 of this note written 1_2, 1_3 so they are not read beside I_4 (two places) |
| note.standard-model.setting-intermediate-symmetry-slot-pair-split | 1 -> 2 | gamma_{2a-1} = I_4(v_a - w_a), a = 1..5; R3 sentence |
| standard-model.global-form-quotient-determined | 3 -> 4 | proof: det phases e^{I_4 alpha}, lambda = e^{2 pi I_4/6}, central characters e^{2 pi I_4 t/3}, e^{2 pi I_4 (p_1 - p_2)/3}, exp 2 pi I_4(...); R3 sentence in formal, with "I_2 and I_3 are identity matrices" |
| standard-model.raw-representation-content-state-space | 3 -> 4 | proof: e^{I_4 theta} I_3 (I_3 the identity) acting by e^{I_4 k theta}; R3 sentence in formal |
| synthesis.majorana-element-is-null-blade-no-frozen-point-condition | 2 -> 3 | exp(I_4 theta (B - L)), orbit e^{-2 I_4 theta} T, compact form I_4 times Hermitian elements (formal (iii), proof (iii)); R3 sentence. Exact because I_4 commutes with the ten tower vectors and so with T |
| synthesis.majorana-scale-not-carried-by-rung-frame-boost | 1 -> 2 | proof: compact flow exp(I_4 phi ad 2T_3R); R3 sentence |
| synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5 | 2 -> 3 | kappa sends I_4 to -I_4 and negates I_4(a^dagger_k - a_k); R3 sentence in formal (v) |
| synthesis.operator-join-positive-energy-no-finite-energy-zero-modes | 1 -> 2 | palatial Fock space: R3 sentence in formal; proof (v) exp((2 I_4/hbar) sum a^dagger b^dagger), I_4 b^dagger; mu in C read in span{1, I_4} |
| synthesis.operator-join-seed-has-no-diagonal-matrix-elements | 1 -> 2 | proof (3): determinant U(1) exp(I_4 phi tr h / hbar), with the R3 sentence at this, its only use |
| note.dark-tower-matter.neutral-row | 2 (stays; sweep had bumped 1 -> 2) | (k I_4, -I_4 1_k) on C^1 + C^k; R3 sentence |

## R3: the face space and slot space, already in I_4, given R3's reading once (no version change)

The first "numbers ... are read in span{1, I_4}" of each entity now also names the module's complex
structure and the floors clause. The note was extended and nothing else changed:
- families.chart-computation-sign-twist-bracket-form (6)
- families.rigidity-pairing-sector-one-event (4; its outside_ga `other` for the cross product is kept)
- families.skeleton-rank-one-plus-ordering-shift (6)
- note.families.setting-gaussian-theorems (2)
- synthesis.channel-phase-invisible-to-axially-covariant-completions (3)
- synthesis.coherent-face-vector-real-slices (2)
- synthesis.light-cone-koide-is-quarter-turn (2)
- synthesis.light-pair-split-needs-broken-source-stabiliser (2)
- synthesis.real-structure-breaks-source-stabiliser-to-z2 (3)
- synthesis.face-mass-form-unit-plus-gram (2)
- synthesis.koide-channel-phase-is-no-symmetry-angle (3)
- synthesis.faces-of-one-slot-space-are-not-three-generations-under-one-gauge-group (2, slot space)

## R4: one unit per entity

| id | version | what changed |
|---|---|---|
| synthesis.frozen-phase-spectrum-not-red | 3 (stays) | proof (ii): Fourier kernels e^{-I_4 k.x}, e^{-I_4 lambda k.x}, e^{-I_4 k.y}; declaration removed |
| synthesis.frozen-point-geometry-reads-descent-as-vacuum | 2 (stays) | Bunch-Davies mode e^{-I_4 k eta}(1 - I_4/k eta)/sqrt(2k) (formal, proof), reduced equation A'' - 2 I_4 k A', Fourier kernels e^{-I_4 k.r}, phase e^{2 I_4 u + I_4 theta}; "numbers are read in span{1, I_4}" added in formal; declaration removed |
| synthesis.hadamard-condition-leaves-the-deposit-spectrum-free-on-bounded-bands | 2 -> 3 | the entity already read its numbers as a + b I_4 but wrote i. Now in I_4: Wronskian = I_4 (formal, proof), modes e^{-I_4 k eta}/sqrt(2k), Bogoliubov phases e^{+-2 I_4 k eta_d}, sample points e^{-I_4 k eta_d}, control e^{-I_4 z}(1 - I_4/z) and its residual. "is read as I_4" became "is I_4". Declaration removed |
| synthesis.thermality-of-every-future-half-generator-fixes-the-period-and-the-null-ground-state | 3 (stays) | Step 1: (X/Y)^{I_4 w}, poles w = I_4 pi(2n + 1)/beta; the bridging remark "written with i for the unit I_4" removed; declaration removed |
| synthesis.one-loop-vacuum-polarisation-extends-without-a-regulator-and-ward-preserving-extensions-differ-only-by-the-renormalisation-constants | 2 -> 3 | missed by the sweep (detector blind to "iq"). Fourier rule d -> iq became d_mu -> I_4 q_mu on components, numbers in span{1, I_4}; written componentwise so it is not read as this entity's left-multiplication term q I_4. Also the W222 rewording above |
| synthesis.sudden-descent-feature-not-tilt | 3 -> 4 | see the scope note below. chi' = -I_4 k (2k)^{-1/2}, u(z) = e^{-I_4 z}(1 - I_4/z), Wronskian 2 I_4, chi_z = -I_4, alpha = e^{-I_4 x}A, A = 1 - I_4/x - ..., beta = -e^{I_4 x}B, and the whole matching computation; declaration removed |
| synthesis.kasner-approach-coupled-modes-reach-measured-tilt-only-by-a-fitted-curvature-coupling | 2 -> 3 | scope note. Hankel Wronskian -4 I_4/(pi s); declaration removed |
| synthesis.kasner-approach-gives-horizon-exit-and-index-three | 2 -> 3 | scope note. Modes e^{I_4 k x^i}, normalisation tau(phi phi-dot* - phi* phi-dot) = I_4, Wronskians -2 I_4 W[J_0, Y_0] = -4 I_4/(pi s); declaration removed |
| synthesis.kasner-hidden-scale-coupled-scalars-stay-blue | 2 -> 3 | scope note. Modes e^{I_4 k x^i}, normalisation = I_4, W = -4 I_4/(pi s), -4 I_4 q|N|^2/pi; declaration removed |

Scope note (a judgement for Leon). R4's first sentence covers entities "whose results use I_4". The
last four entities above did not use I_4. I converted them anyway, for two reasons:
- R4 names exactly their content: Bunch-Davies modes, Hankel Wronskians, and the normalisation
  phi phi-dot* - phi* phi-dot. Outside imports, these occur only in these entities.
- Leaving them would have left cross-entity mismatches:
  - frozen-point-geometry now writes "the modes Proposition sudden-descent expands in" with I_4,
    while sudden-descent wrote them with i;
  - synthesis.kasner-exit-needs-a-contracting-metric-stage-and-a-wall-matching (sweep E) already writes
    its positive-frequency mode with I_4.

To undo this, revert these four to their pre-pass text and declarations.

The de Sitter weight -3/2 +- I_4 nu is already uniform in every formal, technical, lay and one-liner level
and every proof. The i nu forms that remain are:
- `source_formal` quotations in front matter;
- `orig-proof-main.tex` files;
- the Dixmier/Higuchi import mass.imported-unitary-representations-de-sitter-group (Delta = 3/2 + i nu,
  imported, unchanged by ruling);
- an unrelated mode (epsilon + i nu)/2 in synthesis.incidence-vacua-thermofield-real-capacity
  (Cl(p,q)_C, declared).

No "written with i for the unit I_4" sentence remains anywhere in the store.

## Looked at and not converted

- synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise. Its modes are not tower modes: the parity
  average is over one ladder mode a_0 of the descent (singularity.descent-parity-average), on the
  boundary-mode algebra of hawking.i-state, so this is R1 territory. Its i stays, still declared `other`.
  R1 may want the kind changed to complex-analysis with R1's reason.
- rungs.rung-spinor-module-mixings. Its module is that of T_n tensor C, built through Cl(2,4) tensor
  C = M_8(C), a complexification that must commute with spacetime vectors (not changed by ruling). Kept.
- tower.structure-tower-c-norms and synthesis.plane-grading-records-residue-sign. The scalar of T_k^C is
  applied to ground generators, spacetime vectors among them (x_i -> i y_i). Kept.
- synthesis.operator-join-ordering-constants. Its operator coefficient I_6 (M_A = I_6 sum ..., F = I_6 A_U)
  quantises the classical twistor moment, and R3 says to leave twistor components on I_6. I left it.
  It does now sit beside positive-energy and seed, which put I_4 on the same palatial Fock space.
  Replacing I_6 by I_4 there would need the relative-sign datum, so Leon may want to rule on it. The
  constant -5N/2 lambda hbar^2 is the same with either unit (only I^2 = -1 enters).
- Already-converted rung-field entities, even-slots-need-a-spectator-generator and
  slot-parity-decides-hypothesis-s were left without the R3 sentence. They already say that I_4 commutes
  with every rung or tower vector (mode operator), which is R3's substance.
- synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase was left without it too:
  its numbers are quark mass-matrix entries, not face-space components.
- Definitional statements "the operator unit is i = I_4" (obj.field-theory.single-algebra-field and
  others) and the naming phrase "(i = I_4 on rung values ...)" in covariant-rung-coupling were left. They
  define the unit and are not the "written with i for I_4" bridging sentences R4 removes.

## Possible errors found

None in the mathematics.

## Work for the split-owned entities (not touched)

- synthesis.microlocal-condition-on-a-generator-gives-the-local-null-ground-state (R4): the proof still
  writes the Fourier integrals with i in two places, and one equation mixes units:
  R(x) = (1/2 pi) int e^{ipx} r(p) dp = -(I_4 c/pi) int ... Write e^{I_4 px} (also in the
  int_0^infty e^{ipx} dp of the W_0 line). There is no outside_ga, and W222 cannot see a bare i.
- synthesis.positive-null-energy-gives-r-premises (R4 appears done; R1/R2 question left). The contour
  steps of (ii) are no longer flagged. Remaining:
  - the Borchers relation Delta^{is}U(a)Delta^{-is}, declared imported;
  - the commutator component "... P_{jl} = i c P_{jl}" in the proof, which point-spectrum writes as
    [K, P] = I_4 c P (or i after the R1 revert).
  Under R2 (modular groups Delta^{I_4 t} on the continuum mode space) the Borchers line could become
  Delta^{I_4 s} unless kept as the import's form. Which unit [K, P] takes depends on whether its modes
  are R1's or R2's.
- synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations: its only i
  is the Mellin inversion 1/(2 pi i) int Gamma(u) ..., and the entity has no I_4. So R4 as worded leaves
  it, declared complex-analysis. Under the broader reading used for the four scalar-mode entities above,
  it would be 1/(2 pi I_4). It mentions the slot space but writes no number over it, so it needs no R3
  sentence.
- synthesis.slot-module-light-ray-arrays-are-weyl-components already carries the R3 sentence; nothing to do.
- No bare i remains in collapsing-hole-flux, local-normality-at-the-edge, stationary-horizon-state,
  bulk-hadamard-states-restrict, canonical-part-of-a-spinor, light-ray-good-part (only the definitional
  "with i = I_4") or krein-quartet. They need no R3/R4 work.
