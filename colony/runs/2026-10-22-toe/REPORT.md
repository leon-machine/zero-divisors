# Colony run 2: premises, open problems and the Einstein route (2026-10-22-toe)

## The question
Leon asked for the colony to be run again, with the five improvements from the pilot. The run
covered every open problem and concentrated on two things: postulates that other theorems use,
which it tried to resolve, and a route to Einstein's equations from a quantum theory built out of
the series' own objects. He wanted cross-pollination between subjects, and he wanted gravity read
as transport, with no graviton: GR and QM as two readings of one relation.

## How it ran
- **Targets: 55.** These were the 39 store open problems, plus 11 premise targets (`pr.*`: derive a
  postulate, show two postulates equivalent, weaken one, or prove independence with a model), plus
  5 Einstein targets (`ein.*`). They are listed in `targets_extra.yaml`.
- **Split test.** `ant.py split --seed 2210 --include-housekeeping`, stratified by area and
  difficulty, gave 28 colony targets and 27 control targets.
- **Colony arm.**
  - Scouts: 4 rounds of 4 or 5 scouts.
  - Pheromone kinds: interesting, verified and dead, kept separately.
  - Similarity on formal statements only, with notes excluded.
  - The trail map was seeded from the pilot, with old marks faded.
  - 7 clusters (C1 to C7), each with two attackers: angle A constructive, angle B cross-pollinating
    and adversarial.
- **Control arm.** 7 clusters (K1 to K7), two attackers each, the same brief and the same filing
  gate, but no colony tools and no scout findings.
- **Referees.** Seven blind referees (R1 to R7) reviewed all 104 proposals with the arms mixed,
  grouped by subject so that overlaps between the arms would surface.
- **Fix round.** All 28 attackers were resumed with their referee reports.
- **Gate.** Every proposal passed the maintainer's evidence layer (check4), run centrally after the
  fix round, apart from environmental E401: a legacy paper script not visible in check4's
  temporary store. Four housekeeping corrections hit this; their scripts were run in the workspace
  and all pass (verify_T11 39/0, verify_T12 243/0, verify_T15 53/0). Final results:
  `verify/check4_final/`, `verify/validate_final.txt`.
  - validate_draft is ok on every proposal, apart from E102 on corrected entities, which keep
    `orig-proof-main.tex` as they must.
  - One proposal (c1-c2-forms) had claims in `about` (E203); the orchestrator moved them to
    `lineage.motivated_by`, and it was rechecked.
  - Three checks carry W413 (weak-check) warnings: q-splits, sudden-descent and
    tangential-derivative. These are bound checks that some perturbations leave passing; the
    referees accepted the first and last.
  - The changelog by-lines say `ai-colony-...`, which names the method, not an agent.

**Tokens (agent usage):**

| Item | Tokens |
|---|---|
| Control attackers | 4.52M |
| Scouts | 3.16M |
| Colony attackers | 4.79M |
| Referees | 2.19M |
| Fix round | 1.24M |
| **Total** | **about 15.9M, plus orchestration** |

**Proposals:** 105 in all (49 colony, 56 control).
- One of them, `mass.casimir-form-join` v4, was filed in the fix round on a referee's
  specification and has not been blind-refereed. The orchestrator diffed it against the stored v3:
  only the stated normalisation and the grip/de Sitter sentence change, and the proof files are
  byte-identical.
- No two proposals correct the same stored entity.

## Einstein's equations: where the route stands
Candid verdict: **no derivation of Einstein's equations yet.** The run located the gap precisely
and closed several side routes.

1. **Infinity-vacuum incidence** (`synthesis.einstein-condition-is-infinity-vacuum-incidence`,
   colony; SOUND WITH FIXES).
   - What it shows: the Einstein condition Ric = (R/4)g holds exactly when every Fock vacuum whose
     annihilator contains the pure-scale tractor ("infinity vacuum") is unexcited along its own
     null ray. Point vacua satisfy the same incidence automatically; Λ is an integration constant.
   - With conserved matter, the own-ray class equal to 4πG T(l,l) gives Einstein's equations with
     Λ, in the store's convention.
   - The referee's reading, adopted in the title: this is the standard null-cone form of the
     Einstein condition (P(l,l) = 0 for every null l), translated into vacuum language. That puts
     GR's condition and QM's vacuum notion on one object, but it is not a derivation.
   - The missing piece is a reason, on the CAR side, why infinity vacua obey the incidence that
     point vacua obey for free.
2. **Clausius route** (control; one OVERSTATED, now restated).
   - The epoch count gives Newton's constant only through the area-law condition. That is a
     consistency, not a determination of G, because the registered ν was itself fixed by the area
     law.
   - Black-hole thermodynamic data alone cannot fix the field equations
     (`synthesis.black-hole-data-do-not-fix-field-equations`).
3. **Entanglement equilibrium** (control; OVERSTATED, now restated). The boundary-mode algebra
   gives the first-law identities on its own windows. It does not supply the small-ball state that
   Jacobson's 2016 step needs.
4. **Euler term** (control). The series' MacDowell-Mansouri action shifts horizon entropy by
   −3π/(ΛG) for a spherical horizon, assuming Wald entropy.
   - The two arms and the referee agree on this constant.
   - It is invisible to Clausius relations between closed cuts of one topology.
   - Whether it affects a local Clausius relation on small open patches is not settled.
5. **Induced gravity** (colony; kill condition fired, no filing). The series' only non-Planck scale
   is H. Using it as the cutoff only rearranges the stored S = πM_P²/⟨I,I⟩, which is circular.
6. **CAR-side stress tensor** (colony, argued). A linear CAR-side T_ll needs a second algebra.

**The one premise every Einstein-route proposal names as missing:** a counting rule, temperature or
modular flow on local non-Killing horizons and small causal diamonds (call it C_loc). The store has
none. Adding it is a decision for Leon. With it, the Clausius route closes in the usual Jacobson
way. Without it, the series has Einstein's condition restated, not derived.

## Premises: what moved
- **Reductions proved.**
  - The folded state-selection note's (R) and (L_E) reduce to T05's. Retiring them takes the
    register from 42 physical postulates to 40.
  - The candidate rung (R) = (S) at n = 2 would make it 39.
- **Implications.**
  - (Q) implies (P) and (R), so wherever (Q) is assumed, (P) and (R) are redundant.
  - The geometric modular condition implies (P) (control, univalence result).
- **Independence shown by exact finite models.**
  - (P), (R), (L_E) and (I) are mutually independent.
  - (Q) is independent beyond (P) + (R).
  - Under a unique-ground-state condition, (R) and (L_E) exclude each other, so no single
    lowest-energy principle can replace both.
- **Restatements, not derivations.**
  - (L_E) is equivalent to "the dynamics commutes with the descent at all times", on finite windows.
  - Indifference is Curie covariance plus single-valuedness, for weights on finite orbits.
    Selecting a structure needs a measure principle instead (principality is genericity).
  - Tameness splits into a regularity clause and an order clause; the one-sided completion needs no
    order.
  - P1's metric clause, given a frozen point unique where the Weyl tensor has no kernel, becomes
    "parallel for the one tractor connection, with a common norm".
- **(S) narrowed to a residue.** Anomaly freedom, with the tower grading as chirality, forces odd
  slot parity and the slot content of (S) up to multiplicity m. What is still assumed:
  - the factorised shape (slot module times one pair system);
  - chirality equals the tower grading;
  - m = 1;
  - slots of definite parity.

  The no-spectator condition is a second, independent route to odd slots. A constituent
  (SL(4)-equivariant) count cannot produce (S)'s sectors.
- **CPT.** The algebra is confirmed:
  - I6² = −1 in Cl(2,4), and −1 lies in the identity component;
  - the flag conjugate is complex conjugation.

  Under the field-action convention, the action-preserving CPT is the pseudoscalar rotor times
  complex conjugation, which is antilinear. This holds for real tensor fields; spinors are
  excluded. The stored premise's wording, "real linear Z2 automorphism, not the antiunitary
  operator", should be reworded with the convention stated.
- **Trichotomy exhaustiveness.** No result uses it after the corrected one-relation v5 entities.
  It can be retired once the two `assumes` edges are dropped.
- **(U) independent.** Neither reading follows from the other premises or the stored fits. The
  stored (U)/(EW) "contradicts" edge holds only in the matrix-entry reading of (U).
- **Rule 2 sign.** Positive energy (the spectrum condition) selects the opposite-sign repair, given
  one imported theorem (the invariant-cone classification). The fused algebra and the extension
  alone cannot fix it.

## Per problem
Outcome scores: settled, proved-partial, negative, findings, none. "Verdict" is the referee verdict
on the main proposal before fixes.

| Problem | Arm | Outcome | Main proposal | Verdict |
|---|---|---|---|---|
| ein.two-readings | colony | findings | einstein-condition-is-infinity-vacuum-incidence | fixes |
| ein.induced-gravity | colony | findings (argued no-go) | none | - |
| op.cauchy-horizon-transport | colony | proved-partial | plane-wave-weak-null-crossing-null-shell-ambiguity; crossing-transport-tipler-threshold-sharp | sound; fixes |
| op.kerr-ring | colony | proved-partial | kerr-ring-blow-up-forced-cover-fixed-order; kerr-ring-count-misses-area-law | fixes |
| op.forcing-half-beyond-diagonal | colony | negative | unit-boost-residue-needs-nonpositive-exponent; nondiagonal-kasner-residue-weighted-shear | fixes |
| op.wall-class-invariant | colony | proved-partial | twisted-wall-induction-conserves-dying-line-class | sound |
| op.trichotomy-exhaustiveness | colony | proved-partial | one-relation v5 pair; trichotomy-descents-data v5 | fixes; sound |
| pr.cpt-and-intrinsic-clock | colony | proved-partial | cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation | fixes |
| op.collar-kms-extension | colony | proved-partial | collar-kms-extension-completion-locus; collar-isotropy-selects-t-boost | fixes |
| op.which-boost-flow-is-time | colony | proved-partial | number-diagonal-dynamics-spreads-nothing; affine-cell-boost-spreads-without-scrambling | overstated; fixes |
| pr.locality-and-interface | colony | proved-partial | boundary-mode-locality-is-descent-covariance; r-le-i-independent-spectrum-condition-separates | fixes |
| op.which-capacity | colony | proved-partial | twistor-form-states-only-off-the-real-slice; boost-stationary-incidence-vacua-read-interval | fixes |
| op.residue-killing-weights | colony | proved-partial (conditional on (K)) | killing-clock-weights-binary-residue | fixes |
| op.counted-mode-energy | colony | proved-partial | hole-mass-is-ground-energy-label; central-label-carries-mass-at-zero-weight | fixes; sound |
| op.folded-state-selection-note | colony | proved-partial | state-selection-r-and-le-against-t05 plus 3 corrections | fixes; sound |
| pr.minimal-premise-basis | colony | proved-partial | boundary-mode-premises-finite-models; injection-freshness-is-pair-purity | fixes |
| op.many-twistor-grip | colony | settled | three-twistor-composites-massive | sound |
| op.hypothesis-s | colony | proved-partial | anomaly-freedom-forces-slot-content; slot-count-not-from-constituent-fock-space | fixes |
| op.two-loops-two-thresholds | colony | none (needs an imported Fact) | none | - |
| op.rung-unit | colony | proved-partial | rung-unit-is-frame-boost; rung-unit-transverse-to-norm | fixes |
| op.non-gaussian-completion | colony | negative | cumulants-at-fixed-second-moments-keep-the-floor; light-pair-split-needs-broken-source-stabiliser | sound; fixes |
| op.second-order-breaking | colony | negative | no-120-excludes-hierarchical-second-stage; one-type-second-stages-are-twins | fixes; overstated |
| pr.u-equal-rank-one | colony | negative (independent) | stored-fits-are-models-of-not-u; two (U) readings results | fixes |
| op.rule-2-sign | colony | proved-partial (one import) | positive-energy-selects-rule-2-sign; rule-2-fusing-plane-lorentzian | fixes; sound |
| op.odd-towers | colony | findings | none | - |
| op.window-p3 | colony | proved-partial | lowest-causal-residues-zero-four-content | fixes |
| op.dark-sector-scopes | colony | proved-partial | dark-matter.imported-gravity-only-coupling v2 | fixes |
| op.pre-descent-theory | colony | negative | seeding-remainder-excludes-perturbative-pati-salam; untuned-fit-caps-lightest-heavy-neutrino; mirror-temperature-measures-deposit-under-r | fixes |
| ein.clausius-route | control | negative | black-hole-data-do-not-fix-field-equations; clausius-route-newton-constant-is-residue | fixes; overstated |
| ein.entanglement-equilibrium | control | findings | boundary-mode-first-law-of-entanglement; incidence-vacua-entanglement-light-cones-of-unit-diamond | overstated; fixes |
| ein.series-action-area-law | control | proved-partial | euler-term-horizon-entropy-shift; sds-clausius-fixes-area-constant | fixes |
| op.generic-weighted-limit | control | proved-partial | two BKL results; two tangential-derivative results | fixes |
| pr.tameness | control | proved-partial | transverse-corank-two-walls-are-wild; tameness-splits-regularity-and-order | sound; fixes |
| pr.p-univalence | control | proved-partial | univalence-from-even-stationary-dynamics; univalence-even-extension-split | fixes |
| pr.indifference | control | proved-partial | indifference-is-curie-plus-single-valuedness; principality-is-genericity | fixes; sound |
| pr.p1-single-frozen-point | control | proved-partial | frozen-point-unique-where-weyl-has-no-kernel; two-frozen-points-conformally-flat | fixes; sound |
| op.r-premises-external | control | negative | point-spectrum-boost-admits-no-half-sided-translations | fixes |
| op.helicity-per-boundary-mode | control | proved-partial | array-ln2-is-zero-mode-doublet-one-tower | fixes |
| pr.q-quasi-freeness | control | proved-partial | q-splits-maximum-entropy-affine-weights; half-integer-weight-array-carries-half-ln2 | fixes |
| op.island-dictionary | control | proved-partial | eviction-deficit-against-page-deficit | fixes |
| pr.c1-c2-placement | control | proved-partial | c1-c2-forms-forced-one-number; exceptional-boundary-measure-one-calibration | fixes |
| op.boundary-mode-provenance | control | proved-partial | s-wave-array-is-a-boundary-mode-set; obj.hawking v2 | fixes |
| op.descent-state-and-spectrum | control | negative | quadratic-flows-cannot-thermalise-descent; sudden-descent-feature-not-tilt | fixes |
| op.googly-analytic-half | control | negative | quartic-ordering-tensor-locally-trivial | fixes |
| pr.hypothesis-s | control | proved-partial | slot-parity-decides-hypothesis-s; even-slots-need-a-spectator-generator | fixes |
| op.operator-join | control | proved-partial | operator-join-casimir-shifts; massless-composites-de-sitter-conformal-boundary; mass.casimir-form-join v4 | fixes; unrefereed |
| op.pair-sector-current | control | proved-partial | residual-s2-fixes-120-family-form; georgi-jarlskog-square-of-majorana-element | fixes |
| op.majorana-scale | control | findings | majorana-scale-is-126-doublet-vev | overstated |
| op.no-dark-radiation-under-p2 | control | proved-partial | tower-charge-sector-label-temperature-not | fixes |
| op.thickness-deposit-rule | control | findings | none | - |
| op.mirror-reversal-at-tower-top | control | proved-partial | plane-grading-records-residue-sign | fixes |
| op.henneaux-teitelboim-promotion | control | proved-partial | promoted-norm-weyl-clock-flat-weight; promoted-norm-one-global-pair | fixes |
| op.t12-n-after-the-count | control | settled | five N-count corrections; smallness-monomials-exact-hierarchy-casimir | fixes |
| op.small-findings | control | settled | dark-matter and neutrino corrections | fixes |
| op.gram-square-and-face-space | control | proved-partial | slot-covariance-forces-gram-square; light-cone-koide-is-quarter-turn | fixes |

## Store errors found
- **`mass.casimir-form-join`@3.** It stipulated that the grip and the de Sitter mass normalisations
  differ by the conformal Casimir. They do not.
  - On the stored reading, the conformally invariant scalar m² = −H² would be a unitary de Sitter
    mass, which the stored Fact's own list excludes.
  - Correct statement: grip = de Sitter mass + H²·C_conf.
  - v4 is filed. The same gloss sits in `mass.imported-unitary-representations-de-sitter-group`
    (imported, maintainer-only) and in `note.mass.what-join-says`.
- **`dark-energy.vacuum-region-registration-condition`@3, clause (i).** It writes
  T^Λ = −(Λ/8πG)g in the mostly-minus signature, which is a negative vacuum energy (anti-de
  Sitter). It should be +. w = −1 is unaffected.
- **`synthesis.tractor-transport-weak-null-crossing`, note.** The sign of P_VV should be
  −4π(∂_Vφ)² in the store convention. This is note-only and does not affect the formal clauses.
- **`singularity.number-diagonal-dynamics-models-scrambling-derived`.** "Diagonal scrambling"
  means support growth, not exponential scrambling. Recorded as a tension.
- **`singularity.bosonisation-bridge-s-wave-sector` clause (2).** It silently uses (Q)'s weight
  clause: the span of the currents is invariant only for affine weights.
- **Housekeeping corrections** restored the original `proposed_by` provenance, which a first draft
  had overwritten.

## Unexpected cross-problem links
- **One bit, two readings.** CPT's only non-gauge part, complex conjugation, reads as time reversal
  on the GR side and as i → −i on the QM side. Under the field-action convention, keeping gravity
  attractive under C requires the antilinear form.
- **(L_E) is a hub.** It is equivalent to descent covariance, it forbids exponential real-time
  commutator growth, and it cannot yield the slice-product collar algebra. The choice between
  (L_E) and fast scrambling is now explicit.
- **Zero weight does three jobs at once.** It is where the black-hole mass is entirely a c-number
  label, where (R) stops fixing a temperature, and where pair purity stops fixing the thermofield
  form.
- **The rung unit is seen only by the sesquilinear structure.** The tractor (bilinear, GR) side
  does not see it; the Fock (sesquilinear, QM) side does. The weak scale sits in that gap.
  - The unitary choice gives v = H, which is 44 orders of magnitude off.
  - So the weak scale is a second free number beside N, unless a premise fixes the frame.
- **Twistor positivity and the KMS strip.** Twistor positivity under the invariant form is the
  geometric half of the KMS strip, and the store's own Σ is positive on 0 < θ < π. This links
  which-capacity to which-boost-flow.
- **Same symmetry obstruction twice.** Rule 2 and the light lepton pair share it: the algebra alone
  has a symmetry that a selection must break with outside structure (a grading for Rule 2, a real
  structure for the light pair).
- **Kerr.** The counting rule read literally misses the area law by a factor of order M^(−1/3) for
  spinning holes. Some ingredient must carry spin dependence.

## Split test: colony against control
- **Per problem.**
  - Colony: outcome score 52 over 28 problems (0.61 per 100k tokens).
  - Control: outcome score 53 over 27 problems (1.03 per 100k tokens).
  - Outcome mix: colony 1 settled, 18 proved-partial, 5 negative, 3 findings, 1 none. Control 2
    settled (both housekeeping), 18 proved-partial, 4 negative, 3 findings.
- **Per proposal.**
  - Colony: 10 of 49 SOUND as filed (20%), 37 sound with fixes, 2 overstated.
  - Control: 3 of 55 SOUND as filed (5%), 49 sound with fixes, 3 overstated.
- **Reading.** The colony bought cleaner proposals, not more outcomes. It spent 3.2M tokens on
  scouts, which made it about 67% more expensive per problem for the same outcome score. The
  higher clean-SOUND rate is the one signal in its favour.
- **Confounds** (the sample is too small to separate them):
  - The control arm ran first.
  - Colony scouts saw control proposal titles, and one colony attacker opened one control check
    file for its format (reported; nothing used).
  - Outcome labels were assigned by the orchestrator, who knew the arms.
  - The two arms had different problems by design.
- **Verdict.** On this run the colony did not beat the control arm on outcomes per token.

## Decisions for Leon
### Physics premises
1. **Adopt a local-horizon premise (C_loc)?** It would let the Einstein route through Clausius
   close.
2. **Is horizon entropy exactly the boundary-mode count?** If yes, the Euler term must leave the
   entropy functional.
3. **Collar algebra:** (C) slice-product, (E) completion locus, or the pointwise frame atom.
4. **Hermitian structure for the selected state:** positive (thermal at real points,
   e^(−β) = |Q|) or the invariant twistor form (no states at real points).
5. **Boundary-mode array offset:** κk (a zero-weight mode) or κ(k + ½) (exactly ½ ln 2 per array;
   matches R₂π = −1).
6. **The rung-frame boost (v/H):** a second free number beside N in the register?
7. **Restate (S)** as: slot module times one pair system, plus anomaly freedom, plus chirality as
   the tower grading. Also: may slot operators borrow generators from Cl(2,4) (the no-spectator
   condition)?
8. **Adopt (K)?** (The Killing flow on counted modes is a clock at unit rapidity.) It conflicts
   with (Q)'s weights for |k| ≥ 2.
9. **Choose between (L_E) and fast real-time scrambling.** They cannot both hold.
10. **P2 scope "labels, not states"?** If adopted, declare the deposited mode set finite.
11. **Restate (C1) + (C2) as the single premise (C2′).**
12. **Slot-U(3) covariance of the family mass law:** adopt it as a premise? It forces the Gram
    square.
13. **Name the flag-as-datum reading as a premise.** Holds_given does not track it today.

### Maintainer edits
1. **Retirements.**
   - The folded note's duplicate ids.
   - The note (R) and (L_E), after repointing two `assumes` edges.
   - The trichotomy-exhaustiveness postulate, after dropping its two unused `assumes` edges.
2. **Rewordings.**
   - The CPT premise and the seventeenth refutation's step 1, to the antilinear composite, with the
     convention stated.
   - Strengthen the CPT premise's action clause, or record the stronger clause as the one used.
   - The (U)/(EW) contradicts edge, to the entry reading.
3. **New imported Facts** (all currently cited from memory in proof text):
   - Wald / Jacobson-Myers entropy;
   - Jacobson 1995 and 2016;
   - the invariant-cone classification;
   - the theta-function identities (exact ½ ln 2);
   - Powers-Størmer and Takesaki disjointness;
   - Chern-Gauss-Bonnet;
   - the Mišković-Olea identity;
   - two classical Kerr facts;
   - Machacek-Vaughn two-loop Yukawa terms;
   - Pinsker;
   - the Jacobi triple product.
4. **`assumes` edges proposed in proposals, needing confirmation.**
   - (R) on seeding-remainder and untuned-fit.
   - P1 on gravity-only coupling.
   - (EW) on the Majorana proposal.
5. **Status.** Keep `dark-matter.imported-gravity-only-coupling` at proved now that it is derived
   from the T10 chain.
6. **Schema.** Should `about` accept claims and predictions, or is `lineage.motivated_by` the
   intended place? Several referee fixes hit E203 here.
7. **Notes needing text edits** (they cannot be proposed):
   - `note.mass.what-join-says`
   - `note.hawking.setting-mode-continuum`
   - three N-count notes (replacement text in `findings/attack-K7-B.md`)
8. **Optional merges** the referees suggested: the BKL pair, the tangential pair, c1-c2 with the
   exceptional calibration, and the two frozen-point results.
9. **After acceptance.** Repin dependants of accepted corrected entities. `fixes-*.md` files list
   "Repin on acceptance" per proposal. Then `tp lock` and rebuild.

## Process notes for next time
- **Load.** Two CPUs cannot take 28 agents each running check4. Fixers should run only `runcheck`,
  and the orchestrator should run check4 and validate_draft once, serially. This is now in
  FIXROUND.md.
- **runcheck fixed.** `runcheck.py` reported PASS for functions that signalled failure by returning
  False or through GA.check. It is fixed; check4 always counted these correctly.
- **Referee load.** 104 proposals for 7 referees was about 15 each and took 2.2M tokens. Referees
  again found most of the substantive problems.
- **Fairness.** The fairness rule held apart from the slips listed above. Future split tests should
  start both arms at the same time.

## Files
- `REPORT.md`: this report.
- `findings/`: scout, brief, attack and fixes files.
- `verify/R1.md` to `R7.md`: referee reports.
- `verify/verdicts.json`: per-proposal verdicts and arm.
- `verify/check4_final/`: final gate logs.
- `verify/validate_final.txt`: final validation pass.
- `ledger.jsonl`: one row per problem.
- `REFEREE.md`, `FIXROUND.md`, `RUN.md`: the run's briefs.
- `work/`: attackers' scripts.

## After review (2026-10-22 evening)
Leon accepted all 105 proposals, after reviewing the eight flagged ones individually. They are in
the store, with 85 new entities and 20 corrected ones. The 43 stale pins on the corrected entities
were re-confirmed. Only `synthesis.operator-join-casimir-shifts` needed a text change first, because
it cited the casimir entity's old normalisation remark.

### Leon's premise decisions, carried out by the maintainer pass
Full lists are in `maintainer-M1.md` to `maintainer-M4.md`.

**Adopted:**
- **C_loc** (`synthesis.c-loc-local-horizon-premise`, a Tier C postulate). With
  `synthesis.imported-jacobson-clausius-1995` it would give Einstein's equations. That conditional
  derivation is not proved in the store. It is registered as `op.derive-c-loc`.
- **v/H** (`synthesis.rung-unit-second-free-number`): a second free number beside N.
- **(S) restated.**
  - (S) is now a proved claim. It follows from the new postulate
    `standard-model.slot-module-hypothesis` and the anomaly theorem.
    - The postulate covers: slot module times one pair system, hypercharge from the centre, slots
      of one parity, chirality the tower grading, a unique slot vacuum, and slots and pairs forming
      one Clifford system.
    - The anomaly theorem gives the slot content and exclusion.
  - The past cone of the anomaly theorem contains no postulate, so this is not circular.
  - Its 54 dependants now `use` (S) instead of assuming it.
- **(L_E) kept** over fast scrambling, restated as descent covariance on finite windows.
- **P2 scoped** to "labels, not states", with a finite deposited mode set.
- **(C1) and (C2) kept**, each with a note on their reduction.
- **New postulates:**
  - `dark-matter.premise-flag-as-datum`, assumed by the seventeenth refutation and both one-relation
    entities;
  - `families.slot-covariance-of-mass-law`, assumed by the Gram-square result;
  - `standard-model.no-spectator-slots`.

**Left open, as new or updated open problems:**
- the horizon entropy functional (`op.horizon-entropy-functional`);
- the collar algebra;
- the Hermitian structure (`op.which-capacity`);
- the array offset (`op.array-offset`);
- (K), considered and not adopted (recorded in `op.residue-killing-weights`).

**Settled open problems:**
- `op.many-twistor-grip`
- `op.folded-state-selection-note`
- `op.trichotomy-exhaustiveness`

### Maintainer edits
- **CPT:** the premise (v2) and the seventeenth refutation (v7) are reworded to the antilinear
  composite, with the field-action convention stated. The refutation's check (a) now applies complex
  conjugation explicitly.
- **Retired** (in `store/tombstones.yaml`):
  - trichotomy exhaustiveness;
  - 11 duplicate state-selection-note ids;
  - the note's own (R) and (L_E).

  All references were repointed, including labels and the T05 recipe.
- **Store errors fixed:**
  - the dark-energy registration sign (now +Λ/8πG);
  - the crossing-theorem note;
  - the de Sitter Fact's gloss;
  - the gap in the bosonisation bridge;
  - five notes.
- **Twelve imported Facts created and wired in:**
  - Wald and Jacobson-Myers;
  - Jacobson 1995 and 2016;
  - Chern-Gauss-Bonnet;
  - Mišković-Olea;
  - Kerr;
  - invariant cones;
  - theta identities;
  - Jacobi triple product;
  - Powers-Størmer and Takesaki;
  - two-loop Yukawa terms;
  - Pinsker.
- **Edges and links:**
  - The (U)/(EW) edge rationale now says it holds in the entry reading only.
  - New (EW) and P1 `assumes` edges.
  - All 12 W503 condition-wording warnings fixed.

### Check, lock and rebuild
- **Full six-layer check** after the second repin (213 edges): 47 errors, all present in the
  baseline. Nothing new and nothing resolved.
  - 42 of them are environmental E401 errors (paper verify scripts not visible in the cloud).
  - The other five are two older proved claims with no proof text, and three references to
    `synthesis.tower-limit-forgets-residue`, an id that is missing from both stores.
- **Warnings:** 528, of which 521 are the per-function W405, 5 are W413 and 2 are W501.
- **The new W501:** the duplicate pair `note.singularity.two-clocks-one-calibration` /
  `note.state-selection.two-clocks-one-calibration`. That note should be merged or retired.
- **Then:** `tp build`, `tp.layout`, `tp.site` and `tp lock`, run in the workspace.

### Not done
- **The two cross-links.** `comments_on` is allowed only from notes, and `refines` is not a link kind.
  - `dark-matter.status-rule` already names the unit-ball rule in its lineage.
  - `standard-model.one-number-explain` (v4) now cites the smallness result in text.
- **Optional merges.** The referees suggested merging the BKL pair, the tangential pair, c1-c2 with
  the exceptional calibration, and the frozen-point pair. These are not done.
- **Remaining E107 and E216/E201 errors.** These predate the run and are untouched.
