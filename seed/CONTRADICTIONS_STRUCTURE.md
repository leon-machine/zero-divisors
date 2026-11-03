# Contradictions audit: statements and structure

**Resolutions (maintainer decisions of 21 October 2026, seed/DECISIONS_2026-10-21.md).**
H1: `synthesis.wick-rotor-chiral-angular-rotor` accepted; the state-selection
note's Euclidean partner is narrowed to the action on spinors. H2: each result
records which boost flow it means (`extraction.flow_note`), and the remark
`note.decisions.two-boost-flows` sets out the distinction. H3: superseded by
T14c (confinement in phase (C) only). M4, M5: the two restatements corrected.
M8: as VALUES M1. M10: as VALUES M2. L6: the function-linearity citations now
name `sheaf.function-linearity-tame-constructions` only.
Resolved since, as the store stood on 26 October 2026 (op.small-findings, settled): M1: store/conventions.md, Notation (T09's n_0 and n_inf are T01's n_inf and n_0; both normalisations consistent). M2: `note.synthesis.what-n-is-counted` and the corrected T12 entities (`standard-model.what-derived-what-not`, the trichotomy, `standard-model.one-number-explain`; op.t12-n-after-the-count, settled). M3: `neutrino.empty-twistor` and `standard-model.hypercharge-global-form-pair-counting-consistency` name T12's "empty/full conformal spinor" (doublet components) against T15's grade-zero and grade-three singlets. M6: `synthesis.mirror-extensions-causal-convention`; T14a Cor 2.4 and both Rule 2 entities carry the causal-convention sentence. M7: op.boundary-mode-provenance (settled). M9: the state-selection note's premise is renamed (R_reg) (`synthesis.state-selection-r-and-le-against-t05`), the T05 (R) kept. M11: store/conventions.md names the two splittings apart (chirality halves CS, CSm of the Cl(2,4) Dirac module; chiral halves at a point), with `standard-model.imported-pair-systems-two-chirality-halves` and `standard-model.chirality-two-halves-spinor-module-conjugation` (four-dimensional halves). L1: `note.dark-tower-matter.t14s-types-are-different-commutant` (real type at r = 0, 1, 2, two modules at r = 1). L2: store/conventions.md (ladder pairs <v, v*> = 1 in T09's Clifford-side proposition and kk* + k*k = 1 elsewhere; T14's W annihilates the vacuum where T09's and T12's W creates). L3: `angle.imported-singularity-papers-state-selection` now carries "cyclic and separating". L4: `descent-lift.imported-thouless-states-witt-vacua` (Witt vacuum, of Thouless form exactly at nonzero overlap with |0>; |11> the counterexample). L5: `correspondence.symmetrised-quadratics-palatial-algebra` and `correspondence.shared-core-ordering-dictionary` give the signed shift -2 hbar. L7: `sheaf.conservation-degeneracy-located` (the physical side is where the dying eigenvalue is positive, r < 0 at Schwarzschild). L8: (L) to (L_E) in `angle.imported-singularity-papers-state-selection` and `descent-lift.imported-descent-modes-univalence-supplied-class`. L9: `angle.hop-across-cut` (a vector of definite parity defines an even state). L10: `dark-tower-matter.hypothesis-s-slot-statistics` ("used only where a result states it"). L11: `singularity.c2-cell-density` (nu left free, not of order one). L12: the state-selection definition is retired into `obj.singularity.geometric-modular-condition-g` (store/tombstones.yaml), which requires faithfulness, and `state-selection.rate-discharge-hypothesis-iii` says faithfulness is presupposed, not derived. Every finding of this report is resolved or recorded.


Scope: the whole store (`store/claims`, `store/objects`, `store/predictions`,
`store/notes`), read through `tp.ask` (`get_claim`, `find_text`,
`list_entities`) and the build's restatement map (every one of the 111
"Imported:" restatements was printed beside the formal text of each of its
`restates` originals and read). Paper sources were grepped, never read whole.
Nothing under `store/`, `tp/` or `documents/` was changed and no verify script
was run. Scratch files: `/tmp/claude-0/-home-claude/f5c21aa3-33bd-54d7-a8e9-4d9b5d6a3726/scratchpad/contra-2/`.

The four angles: (1) no-go against construction; (2) one object described
incompatibly in two places; (3) namesakes and restatements; (4) uniqueness
clashes. Every finding was checked by reading all the entities named.
Candidates that dissolved on reading are listed at the end so they are not
raised again.

Severity: **high**, the store asserts both sides, as held results, with no
link between them; **medium**, a reader is likely to be misled (a stale or
strengthened restatement, a namesake used for different objects, a convention
left unmarked where two papers meet); **low**, cosmetic, or a slip that changes
no conclusion.

Counts: **3 high, 11 medium, 12 low** (26 findings). Two medium findings
(M8, M10) overlap with `seed/CONTRADICTIONS_VALUES.md` (its M1 and M2); they
are kept here because the structural fault (a restatement, a shared id) is
different, and they are marked.

## Summary table

| # | Sev. | Topic | Main ids | Kind |
|---|---|---|---|---|
| H1 | high | Is the Euclidean rotation the second member of the curvature-selected pair? | `state-selection.euclidean-partner-curvature-selected`, `singularity.euclidean-rotor-where-it-lies` | genuine contradiction |
| H2 | high | "The boost flow" names two different one-parameter groups: the real rotor flow and the unitary phase flow | `singularity.modular-structure-completed-pair`, `singularity.rate-rigidity-temperature-not-algebra-intrinsic`, `singularity.euclidean-rotor-where-it-lies`, `obj.hawking.boundary-mode-algebra-windows-boost-dynamics`, `scrambling.clock-inventory-boundary-modes`, `scrambling.spreading-law-chaos-bound-saturated` | same object, incompatible descriptions |
| H3 | high | Every compact U(1) in the three-dimensional towers confines (T14) against "only in phase (C)" (T14c) | `dark-matter.radiation-audit-what-theorem-closes-what`, `dark-tower-matter.three-dimensional-phases`, `dark-tower-matter.anomalies` | genuine contradiction (acknowledged one way only) |
| M1 | medium | Which twistor half is E = +1: T09 puts the π-plane at E = -1/2, T12, the rungs note and FT at E = +1 | `correspondence.local-twistor-transport-ascended-spinor-connection`, `standard-model.internal-symmetry-ladder`, `rungs.mass-bracket-frozen-points-grip-slot`, `field-theory.where-each-lives`, `field-theory.orientation-relocated`, `standard-model.imported-fock-model-twistor-space` | convention difference (swapped null pair), unmarked |
| M2 | medium | N is the boundary-mode count, or its square root | `standard-model.what`, `standard-model.why-large`, `standard-model.largeness-number-universes-boundary-modes`, `standard-model.trichotomy-what-kind-number`, `dark-matter.stored-asymmetry-charge-not-number` | same object, incompatible descriptions |
| M3 | medium | "Empty conformal spinor" names the (1,0) doublet in T12 and the grade-zero singlet in T15 | `standard-model.hypercharge-global-form-pair-counting-consistency`, `standard-model.under-s-composites-state-space-spinor`, `neutrino.empty-twistor`, `neutrino.imported-mass-bracket-quantum-numbers` | namesake, disclaimer out of date |
| M4 | medium | T15 restates T14 as speaking of "the grade-three state"; T14 now says grade zero | `neutrino.imported-ceiling-under-hypothesis-u-arrow`, `dark-matter.orientation-arrow-seventeenth-refutation` | stale restatement |
| M5 | medium | T14a restates "the other six are populated" as T14's result; T14 holds only that six admit matter | `odd-extensions.imported-representatives-dimension-nearest-four-types`, `dark-matter.towers-are-residues-single-clock-filter`, `dark-matter.which-towers-are-populated` | restatement stronger than its originals |
| M6 | medium | Which extension of the mirror is "space": T14a and the Rule 2 note against T14's causal convention | `odd-extensions.four-extensions-oriented-pair`, `rule2.which-residues-obstruct-which-way`, `transport.which-residues-obstruct-which-way`, `dark-matter.towers-are-residues-single-clock-filter` | convention difference with a false-looking consequence |
| M7 | medium | Where the boundary modes come from: tower rungs (T7) or one ladder per point after a single ascent (T5, T3) | `obj.hawking.boundary-mode-algebra-windows-boost-dynamics`, `hawking.imported-algebra-boundary-modes-car-algebra`, `note.hawking.setting-mode-continuum`, `singularity.bosonisation-bridge-s-wave-sector`, `tower.answers-iteration-question` | same object, incompatible provenance |
| M8 | medium | T16 restates the clock period as "the modular period, unconditionally" beside "(R) is irreducible" | `one-relation.imported-single-mode-thermality-modular-period`, `scrambling.clock-inventory-boundary-modes`, `singularity.modular-descent`, `singularity.why-calibration-cannot-be-internal` | wording slip in a restatement (overlaps VALUES M1) |
| M9 | medium | Two premises called (R), "regularity at the fixed locus", with different content | `singularity.r-regularity-fixed-locus`, `state-selection.r-regularity-fixed-locus`, `singularity.rate-discharge-hypothesis-iii`, `state-selection.rate-discharge-hypothesis-iii` | namesake |
| M10 | medium | Two results with the same id suffix `area-law-test` disagree on whether the bare count matches S_BH | `scrambling.area-law-test`, `singularity.area-law-test` | convention difference, unmarked in the statement (overlaps VALUES M2) |
| M11 | medium | "Chirality halves" means S and S' in T12, and the two planes at a point in conventions.md and T9 | `standard-model.imported-pair-systems-two-chirality-halves`, `correspondence.incidence-relation-chart`, `field-theory.where-each-lives`, `store/conventions.md` | naming clash |
| L1 | low | T14's spinor type by residue against T14c's constituent field: every residue differs | `dark-matter.type-residue-what-each-tower-can`, `dark-tower-matter.constituents-field`, `note.dark-tower-matter.t14s-types-are-different-commutant` | scoping difference, reconciled by a note |
| L2 | low | Normalisations missing from conventions.md: n_0·n_∞ = +1 in more papers than listed; ladder pairs at 1/2 and at 1; T14's W annihilates where T9's creates | `interior.stabilisers-flat-model`, `correspondence.skew-lines-splittings-hyperbolic-planes-one`, `one-relation.imported-pure-spinors-incidence-chart`, `correspondence.clifford-side-ordering-shift`, `obj.dark-matter.null-blades-fock-ideal-chirality` | convention difference |
| L3 | low | Angle note's Fact 1.1 drops the cyclic-and-separating hypothesis of the Schmidt lemma | `angle.imported-singularity-papers-state-selection`, `singularity.schmidt-forcing-proved-outright` | wording slip in a restatement |
| L4 | low | "Every even state of at most three modes is such a vacuum" (Thouless form) | `descent-lift.imported-thouless-states-witt-vacua`, `one-relation.imported-cartans-purity-theorem-thouless-form` | wording slip in a restatement |
| L5 | low | Ordering shift: "-2ħ" (T7) against "2ħ" (T9) | `hawking.imported-twistor-storey-ordering-shift`, `correspondence.shared-core-ordering-dictionary`, `correspondence.symmetrised-quadratics-palatial-algebra` | sign wording |
| L6 | low | Three-routes cites the wrong entity for function-linearity and calls the proved half "diagonality" | `three-routes.class-relative-no-go`, `singularity.p-reduced-metric-level-reading-many`, `singularity.class-relative-no-go-no-supplied` | structural slip (mis-resolved reference) |
| L7 | low | "Displaced into the physical side" (T4 Prop 5.2) against "no shadow wall anywhere" (T4 Thm 8.12), same sign of μν | `sheaf.conservation-degeneracy-located`, `sheaf.one-sided-completion-singularity` | wording (side named by sign, not by physics) |
| L8 | low | (L) used for the boundary-mode locality premise (L_E) | `angle.imported-singularity-papers-state-selection`, `descent-lift.imported-descent-modes-univalence-supplied-class`, `singularity.rate-models-kinematic-inputs-l-u`, `singularity.l-boundary-mode-locality` | namesake slip in one-liners |
| L9 | low | "Physical states are even" against "ψ is odd, hence physical" | `singularity.p-univalence`, `angle.hop-across-cut` | wording |
| L10 | low | "(S) carried to every tower" against "why (S) fails in three dimensions" | `dark-tower-matter.hypothesis-s-slot-statistics`, `note.dark-tower-matter.why-s-fails-three-dimensions-not` | scoping, one-liner overstates |
| L11 | low | ν "an order-one constant" (T5) against the predicted ν = 1/(16π) (T8) | `singularity.c2-cell-density`, `scrambling.epoch-modular-period-two-unknowns-become` | wording |
| L12 | low | The geometric modular condition with and without faithfulness | `obj.singularity.geometric-modular-condition-g`, `obj.state-selection.geometric-modular-condition` | same object, differing definitions |

Known limits in `store/conventions.md`, checked: (1) T5's atom in the
spacetime radial plane, so I_4 anticommutes with its mode operators:
confirmed (`singularity.euclidean-rotor-where-it-lies`,
`obj.singularity.grading-parity-automorphism`). (2) Boundary-mode algebra over
C in the Hawking paper and real with scalar centre in the scrambling results:
confirmed (`obj.hawking.boundary-mode-algebra-windows-boost-dynamics` against
the proof of `scrambling.clock-inventory-boundary-modes`), and it has a
dynamical consequence that is H2 below. (3) Opposite signs for γ_7 in T12 and
its rungs note: not confirmable from the store. The only γ_7 in the store is a
slot Majorana label in `standard-model.left-right-parity-what-breaks-it`; the
rungs note writes chirality as (-1)^{j+k} and T12 its rung parity as
χ = -(-1)^{N_R}, and no stored entity states a γ_7 chirality sign.

---

## High

### H1. Is the Euclidean rotation the second member of the curvature-selected pair?

- `state-selection.euclidean-partner-curvature-selected` (T5 state-selection
  note, Prop 5.2, proved, pass-legacy): "The Euclidean rotation whose angle
  carries the periodicity is therefore not an imported device: it is the
  second member of the pair that Step 4b's curvature equation already
  selects", the member being Iσ_r with rotor exp(θ Iσ_r/2), described as "the
  analytic continuation of the boost rotor ... under λ ↦ iθ".
- `singularity.euclidean-rotor-where-it-lies` (T5 Prop 7.21(3), proved): "The
  dual member of the curvature-selected pair, Iσ_r = e_0e_1e_2e_3 e_0e_1 =
  e_2e_3, is the angular plane ... a rotation along the bifurcation sphere,
  not around it. The Euclidean rotation around the bifurcation sphere is
  therefore realised by no real rotor of Cl(1,3), and in particular not by
  the curvature-selected pair {σ_r, Iσ_r}".

Why they conflict: the same rotor, exp(θ Iσ_r/2), is the Euclidean rotation
in one and explicitly not the Euclidean rotation in the other. The note's
result is not a historical curiosity: it is used by
`state-selection.rate-discharge-hypothesis-iii` (T = κ/2π) and
`state-selection.where-fermi-dirac-comes`. The only trace of the conflict is
the extraction typing note on the state-selection entity ("conflicts with the
singularity paper's later proposition ... recorded here only as a doubt");
there is no `contradicts` or `refuted_by` link, and both are effective status
proved. Genuine contradiction. Severity high.

### H2. "The boost flow" names two different one-parameter groups

- Real rotor flow. `singularity.modular-structure-completed-pair` (T5 Thm 6.3):
  "the rotor flow R_λ = exp(λσ/2) acts by v ↦ e^{-λ}v ... K := σ/2 = N - 1/2
  ... the boost flow is the only one-parameter flow implemented by real
  rotors of the atom". `scrambling.clock-inventory-boundary-modes` (T8 Lem
  4.2): a clock is "hyperbolic (its adjoint action on the mode operators
  semisimple with real eigenvalues)", and in its proof "what is compact here
  is the phase circle e^{iθ n̂}, whose generator is i times a bivector, which
  the real Clifford algebra of the boundary modes excludes ... so the phase
  circle is not an intrinsic flow". `scrambling.spreading-law-chaos-bound-saturated`
  (T8 Asm 6.1) then runs the window's dynamics on that flow: "a quadratic
  generator containing the boost scales ladder operators by e^{±κt}".
- Unitary phase flow. `singularity.rate-rigidity-temperature-not-algebra-intrinsic`
  (T5 Thm 7.16): "Let α_t = Ad(e^{itK}) be the boost flow of the single-mode
  algebra". With K = σ/2 this is Ad(exp(itσ/2)), which
  `singularity.euclidean-rotor-where-it-lies` (T5 Prop 7.21) calls the boost
  rotor "continued to imaginary rapidity", "realised by no real rotor", the
  Euclidean rotation. `obj.hawking.boundary-mode-algebra-windows-boost-dynamics`
  (T7 Def 2.7) takes as the dynamics "τ_t(a_j) = e^{-iω_j t} a_j, with t
  Schwarzschild time", which is exactly a phase circle e^{-it Σ ω_j n̂_j}.

Why they conflict: the KMS and modular analysis (T5 Thms 7.3, 7.16; T7
throughout) is done for the unitary flow, whose adjoint eigenvalues are
imaginary (∓iω_j), while T8's clock theorem and its fast-scrambling law use
the real flow, with real eigenvalues ±κ, and say the unitary flow is not an
intrinsic flow of the boundary modes at all. Within T5 itself the group
Ad(exp(itσ/2)) is "the boost flow" in Thm 7.16 and the Euclidean rotation in
Prop 7.21. Each paper is self-consistent in its own algebra (this is the
dynamical face of known limit 2), but no entity says that two flows related
by λ ↔ it share the name, and T8 Asm 6.1 treats the real flow as the physical
time evolution in the very time t in which T7's dynamics is a phase. Same
object, incompatible descriptions. Severity high.

### H3. Every compact U(1) in the three-dimensional towers confines, or only in phase (C)

- `dark-matter.radiation-audit-what-theorem-closes-what` (T14 Prop 6.2(2),
  proved): "Closed at both levels, by Polyakov: vector-like (no chirality in
  odd dimension), so Dirac masses are unforbidden and, absent an imposed
  parity, generic; with no massless charged matter left, every compact U(1)
  in three dimensions ... confines by monopoles".
- `dark-tower-matter.anomalies` (T14c Prop 6.5(i), proved): "integrality of
  the effective level forces the bare levels into Z + 1/2. Parity is
  therefore broken by the gauge sector."
- `dark-tower-matter.three-dimensional-phases` (T14c Prop 9.1, assembly): phase (T) is
  "topologically massive", with "the absence of confinement at nonzero
  Chern-Simons level"; and "T14's Proposition 6.2 states that every compact
  U(1) in three dimensions confines; with the forced half-integral level that
  holds in phase (C) only."

Why they conflict: T14 asserts confinement for every compact U(1) and treats
parity as something that would have to be imposed; T14c proves the parity
anomaly forces a half-integral level and then holds that in phase (T) there is
no confinement. Both close the radiation channel, so the conclusion survives,
but the mechanism T14 states as proved is false in one of T14c's two phases.
T14c says so in its text; the T14 entity carries no note, link or caveat.
Genuine contradiction, acknowledged in one direction only. Severity high.

---

## Medium

### M1. Which twistor half is E = +1

- `correspondence.local-twistor-transport-ascended-spinor-connection` (T9 Prop
  4.10(2)): "with Spi the plane of Ψ(X_p) (the point's own line ...) and Som
  the plane of Ψ(u_p), the grading element E := u_p ∧ X_p acts with
  eigenvalue +1/2 on Som and -1/2 on Spi".
- `standard-model.internal-symmetry-ladder` (T12 Prop 3.1): momentum "built
  from the parts π^i in the E = +1 eigenspace";
  `rungs.mass-bracket-frozen-points-grip-slot` (T12 rungs, Lem 2.3): "CS =
  Som ⊕ Spi ..., the E = -1 and E = +1 eigenspaces";
  `field-theory.orientation-relocated`: "the momentum doublet ker n_0, the
  E = +1 doublet".
- `standard-model.imported-fock-model-twistor-space` (T12 Fact 9.2, restating
  T9): "the bivector of Som is the point at infinity n_∞", while
  `standard-model.frozen-point-first-rung-component` works "in the root
  paper's conventions ... n_0 = (e_- - e_+)/2, n_∞ = e_- + e_+".

Why they conflict: on its face T9 puts the π-plane at E = -1 (Clifford, ρ =
E/2) and T12, the rungs note and FT put it at E = +1. The resolution is a
labelling swap: T9 takes n_0 = e_+ + e_-, n_∞ = (e_+ - e_-)/2 (its Fock-model
choice n_0 := w_1, n_∞ := w_1'), so T9's origin vector is T1's infinity vector up to scale and
sign. Both use E = e_+e_- = n_∞ ∧ n_0. So "the bivector of Som is n_∞"
means different planes in T9 and in T12, and T12 imports T9's chart
statements while using T1's vectors. conventions.md says the two
normalisations "are both consistent" but does not record that they swap
which half is called the origin line. Convention difference, unmarked where
the papers meet. Severity medium.

### M2. N is the boundary-mode count, or its square root

- `standard-model.what` (T12 Obs 7.2(i)): "the de Sitter horizon entropy is of
  order N^2, so that N is the square root of the pair capacity of the
  universe's own boundary mode space"; `standard-model.trichotomy-what-kind-number`
  (T12 Prop 7.6): "exp(S_modes) = exp(N^2)".
- `standard-model.why-large` (T12 Obs 7.3(ii)): "what requires explanation is
  not why the universe's boundary mode space is large but why it is so small,
  of order 10^60"; `standard-model.largeness-number-universes-boundary-modes`:
  "'why is N large' is 'why does the universe have so many boundary modes'".
- `dark-matter.stored-asymmetry-charge-not-number` (T14 Prop 4.6): "the
  boundary mode count N common to the towers under P1 ... Q = εN".

Why they conflict: N ≈ M_P/H ≈ 10^60 (`standard-model.imported-frozen-point-dictionary`)
is both the number of boundary modes and the square root of that number,
inside one paper; T14 then uses N as a mode count in a charge formula.
Observation-level statements, but the factor is 10^60. Same object,
incompatible descriptions. Severity medium.

### M3. "Empty conformal spinor": a doublet in T12, a singlet in T15

- `standard-model.hypercharge-global-form-pair-counting-consistency` (T12 Thm
  5.5(1)): "the lepton doublet is the full conformal spinor, the component
  (1,3) ... and the empty conformal spinor, the component (1,0), appears only
  as its conjugate"; `standard-model.under-s-composites-state-space-spinor`:
  "the doublet of the empty conformal spinor (the empty-twistor doublet)
  (2,1)_{1/2} at (1,0)".
- `neutrino.empty-twistor` (T15 Prop 3.1(1)): ν_R "is the grade-zero state of
  the single-spinor sector, the empty conformal spinor (the empty twistor) in
  this paper's usage (T12 uses the phrase 'empty twistor' for the one-slot,
  no-pair doublet state, a different object) ... the grade-three state, the
  filled conformal spinor"; `neutrino.imported-mass-bracket-quantum-numbers`:
  "the slot-free grade-zero state, the empty conformal spinor".

Why they conflict: after the GA conversion both papers use the identical
phrase "empty conformal spinor" for different objects (a (2,1) doublet at
(1,0) against the (1,1)_0 singlet at (0,0)), and similarly "full" against
"filled" conformal spinor. T15's disclaimer still names the old phrase
"empty twistor" and appears at the formal level only (the technical level
drops it). Namesake. Severity medium.

### M4. T15 attributes "the grade-three state" to T14; T14 says grade zero

- `neutrino.imported-ceiling-under-hypothesis-u-arrow` (T15 Fact 2.5,
  restatement of T14 Props 5.1, 5.2, 6.4): "the identification of ν_R with a
  singlet grade is flag-covariant (... that paper states this for the
  grade-three state, and the argument transfers unchanged to the grade-zero
  state this paper identifies)".
- `dark-matter.orientation-arrow-seventeenth-refutation` (T14 Prop 5.2, one of
  its `restates` originals): "the identification of ν_R with the
  hypercharge-zero singlet at grade zero is flag-covariant".

Why they conflict: the restatement describes its original as saying something
the original no longer says. The T15 source header records the knock-on (K3:
"T14 Prop 5.2: 'the grade-three state' should read the hypercharge-zero
singlet"); T14 was corrected, T15's Fact was not. Stale restatement.
Severity medium.

### M5. T14a restates "the other six are populated"

- `odd-extensions.imported-representatives-dimension-nearest-four-types`
  (T14a Fact 1.2, proved, provenance T14 Prop 3.1, Thm 3.4): "the residues 0
  and 4 are sterile and the other six are populated".
- `dark-matter.towers-are-residues-single-clock-filter` (T14 Prop 3.1): "Six
  admit matter ... Which of the six the descent populated is a further
  question, answered for the mirror by P2 and for the odd towers only by the
  record"; `dark-matter.which-towers-are-populated` (status conjectured): "an
  inference at observation level, not a count".

Why they conflict: the restatement turns "admit matter" into "are populated"
and carries it as a proved restatement of a proved proposition, while the
store holds odd-tower population as conjectured. Restatement stronger than its
originals. Severity medium.

### M6. Which extension of the mirror is "space"

- `odd-extensions.four-extensions-oriented-pair` (T14a Cor 2.4): "mirror +
  space: Cl(3,2) ... mirror + time: Cl(4,1)", and "In both towers the
  generator of the time sign complexifies and the generator of the space sign
  doubles."
- `rule2.which-residues-obstruct-which-way` (T17 Rule 2 note, Cor 2.3) and its
  restatement `transport.which-residues-obstruct-which-way`: "it leaves residue
  6 only through a spacelike Kaluza-Klein direction ... The same holds at the
  mirror residue 2."
- `dark-matter.towers-are-residues-single-clock-filter` (T14 Prop 3.1): "Call
  a signature (p,q) causal if min(p,q) = 1: exactly one direction of the
  minority sign, the timelike one", the mirror reading (3,1) as "a mirror
  Minkowski".

Why they conflict: T14a and the Rule 2 note fix "time" as the + sign and
"space" as the - sign in both towers, which gives the mirror (3,1) three time
directions. Under T14's convention the mirror's single time is its minority
(-) direction, so the mirror's spatial extension is Cl(4,1) (residue 3,
complex type) and its time extension Cl(3,2) (residue 1, type C): the
mirror's space generator complexifies and its time generator doubles, the
opposite of Cor 2.4, and "the same holds at residue 2" fails for the mirror's
physical Kaluza-Klein direction. Convention difference with a consequence a
reader will take at face value. Severity medium.

### M7. Where the boundary modes come from

- `obj.hawking.boundary-mode-algebra-windows-boost-dynamics` (T7 Def 2.7):
  the boundary-mode algebra "is the CAR algebra over ℓ²(J) (Fact
  hawking.imported-algebra-boundary-modes-car-algebra)", which restates the
  tower's limit "the mode operators are the adjoined null pairs themselves
  ... the physical lineage has charge six, so the theorem applies";
  `note.hawking.setting-mode-continuum`: the space "has countably many modes
  because the tower adjoins them one rung at a time".
- `singularity.bosonisation-bridge-s-wave-sector` (T5 Thm 8.2): the
  filled-sea array's algebraic model is the tower limit "cited for the
  structure; its provenance here is the s-wave aggregation declared above,
  not a tower, the mod-8 clock having stopped after one ascent".
- `tower.answers-iteration-question` (T3 Cor 6.2): "On the physical closure,
  one ascent completes the description ... nothing on the physical side
  demands a second rung"; `sheaf.one-sided-completion-singularity` (T4 Thm
  8.12): one ladder pair "exists exactly over E".

Why they conflict: T7 grounds the boundary modes' countability in rungs of the
tower; T5, T3 and T4 say the physical closure has one ascent, one ladder pair
per point of E, aggregated over s-wave channels, and T5 says explicitly that
the tower is cited only for structure. Same object, incompatible provenance.
Severity medium.

### M8. "The modular period, unconditionally" beside "(R) is irreducible" (overlaps VALUES M1)

- `one-relation.imported-single-mode-thermality-modular-period` (T16 Fact
  2.4, restatement): "its exactness holds under the singularity paper's
  declared premises (P) and (R), and the value of T_H follows from (R). The
  entropy paper's clock inventory of the singularity's boundary modes gives
  the modular period β = 8πM unconditionally."
- `singularity.modular-descent` (T5 Thm 7.3): the normalisation "one modular
  period being one period 2π/κ of rapidity-time (the Bisognano-Wichmann
  normalisation, which Section ... names as premise (R) and proves
  irreducible)"; `singularity.why-calibration-cannot-be-internal` (T5 Prop
  7.25): "no strengthening of its statements at the singular boundary can
  supply (R)".

Why they conflict: T8's clock inventory gives the period of a flow (its
Euclidean continuation, converted at κ), not the modular period of a state;
T16 calls it the modular period and says it holds unconditionally, in the same
sentence that makes T_H depend on (R). Read literally the two halves of T16's
Fact contradict T5. Wording slip in a restatement. Severity medium.

### M9. Two premises called (R)

- `singularity.r-regularity-fixed-locus` (T5 Premise 7.19): "each single-mode
  marginal of the boundary-mode state is KMS for the Killing flow at the
  period 2π/κ dictated by regularity of the Euclidean section".
- `state-selection.r-regularity-fixed-locus` (T5 state-selection note, Premise
  5.1): "the state's two-point functions, continued in the rapidity of the
  boost flow, are single valued and regular at the flow's fixed locus".

Why they conflict: same letter, same title, same id suffix, different content.
T5's (R) asserts the KMS condition at the geometric period, so
`singularity.rate-discharge-hypothesis-iii` needs only "(P) and (R)"; the
note's (R) is the regularity condition, and
`state-selection.rate-discharge-hypothesis-iii` needs "(P) and (R), and ...
the GMC" to reach the same temperature. The `namesakes` field lists the pair,
but restatements elsewhere (angle Fact 1.1, T7 Fact 2.2, T16 Fact 2.4) cite
"(R)" without saying which. Namesake. Severity medium.

### M10. `area-law-test` in T5 and T8 (overlaps VALUES M2)

- `scrambling.area-law-test` (T8 Prop 3.5): "N = S_BH = 4πM² if and only if
  νΔt = M/2: the count reproduces the Bekenstein-Hawking entropy, coefficient
  included".
- `singularity.area-law-test` (T5 Prop 10.7): "C = S_BH = 4πM² if and only if
  νΔt = M/(2 ln 2) ... It is the capacity, not the bare count, that ...
  compare[s] with S_BH; the count itself then reads N = S_BH/ln 2."

Why they conflict: two results with the same id suffix and topic give
different coefficients and disagree on whether the bare count is the thing
compared. T8 works in a 1-nat convention, which it names only later
(`scrambling.epoch-modular-period-two-unknowns-become`: "Section ... shows the
capacity convention is the one with physical content"), so its own "coefficient
included" is stated in the convention it later sets aside. Convention
difference, unmarked in the statement. Severity medium.

### M11. "Chirality halves" for two different splittings

- `standard-model.imported-pair-systems-two-chirality-halves` (T12 Fact 2.2):
  "its two chirality halves are CS = Λ^even W and CS' = Λ^odd W, each of
  dimension four"; `dark-matter.mirror-tower-copy-one` (T14 Thm 4.3) copies
  "the same chirality halves" to the mirror.
- `store/conventions.md`: "\Som, \Spi the two chiral halves at a point";
  `correspondence.incidence-relation-chart` (T9 Thm 4.2(iv)): Som ⊕ Spi "as
  the two chiral 2-dimensional representations"; `field-theory.where-each-lives`:
  L_0, L_∞ "the two chiral doublets".

Why they conflict: one word names the Cl(2,4) chirality (S against S', the
parity of the Fock grade) and the spacetime chirality inside S (the
E-eigenplanes). The extraction note on
`standard-model.chirality-two-halves-spinor-module-conjugation` sees the
difference ("not TWGA's E = ±1 split inside S") but itself calls S and S'
"the six-dimensional chirality halves", which is wrong (each is
four-dimensional; the six is the ambient). conventions.md, the reader's first
stop, uses the T9 sense only. Naming clash. Severity medium.

---

## Low

### L1. Spinor type by residue (T14) against the constituent field (T14c)

`dark-matter.type-residue-what-each-tower-can` (T14 Thm 3.4): "this world
r = 6, and r = 4, 5, have quaternionic spinors ... no distinguished U(1)";
r = 3, 7 "complex ... exactly one intrinsic abelian charge each".
`dark-tower-matter.constituents-field` (T14c Thm 3.2): the field is "the
division algebra of residue r + 1": C at r = 6, 2; R at 1, 7, 0; H at 3, 5, 4.
Every residue's answer differs. Both are correct for their objects (the
commutant of Cl(V) on its module against the spin commutant on the even
ideal), and `note.dark-tower-matter.t14s-types-are-different-commutant` says
so; its technical, lay and one-liner levels are "pending", and it misquotes
T14 as assigning real type to "r = 1, 2" (T14: real at 0, 2 and two modules at
1). Scoping difference. Severity low.

### L2. Normalisations missing from conventions.md

conventions.md: "Some papers (T11, the pairing note) normalise n_0·n_∞ = +1".
The +1 normalisation is also used by T6 (`interior.stabilisers-flat-model`:
"⟨n_∞, n_0⟩ = 1"), T9 (`correspondence.skew-lines-splittings-hyperbolic-planes-one`,
its setting) and T16 (`one-relation.imported-pure-spinors-incidence-chart`),
and each paper picks its own null vectors (T1: n_0 = (e_- - e_+)/2; pairing:
n_0 = (e_+ + e_-)/2; T9: n_0 = e_+ + e_-), which is the root of M1; the frozen
point is n_∞ + (Λ/6)n_0 in T11 and n_∞ - (Λ/6)n_0 in T12. Ladder pairs are
normalised ⟨v, v*⟩ = 1 in `correspondence.clifford-side-ordering-shift` and
⟨k, k*⟩ = 1/2 (kk* + k*k = 1) in T3, T4, T7 and T16. In
`obj.dark-matter.null-blades-fock-ideal-chirality` W annihilates the vacuum
("wf = 0"), where in T9 and T12 W is the creating space (c(w) = √2 w∧).
Each paper is consistent within itself. Convention difference. Severity low.

### L3. Angle Fact 1.1 drops a hypothesis

`angle.imported-singularity-papers-state-selection`: "For the horizon pair, a
boost-invariant state has the form cos θ|00⟩ + sin θ|11⟩". Its original
`singularity.schmidt-forcing-proved-outright` (T5 Lem 7.2) needs the vector to
be "invariant up to phase ... and cyclic and separating"; without the second
condition |01⟩ and |10⟩ are also invariant up to phase (the proof says so:
"the eigenvectors for ±1 are product vectors"). Wording slip in a
restatement. Severity low.

### L4. Thouless form "for every even state"

`descent-lift.imported-thouless-states-witt-vacua`: "on two modes it is |00⟩ +
A_12|11⟩, and every even state of at most three modes is such a vacuum".
Original `one-relation.imported-cartans-purity-theorem-thouless-form`: every
Weyl spinor is pure for 2ν ≤ 6, and "every vacuum with nonzero overlap with
|0⟩ is of this form". Read as "a Thouless state", the restatement fails for
|11⟩; read as "a Witt vacuum", it is right. Wording slip. Severity low.

### L5. The sign of the ordering shift

`hawking.imported-twistor-storey-ordering-shift` (T7 Fact 2.6): "shifts ...
q(id) by -ħ/2 per complex dimension ... totalling -2ħ ... the two storeys
carry the same signed ordering shift". Originals
`correspondence.symmetrised-quadratics-palatial-algebra` (T9 Lem 5.5(3)) and
`correspondence.shared-core-ordering-dictionary` (T9 Thm 5.7(4)): "the shift
is 2ħ", "by ħ/2 per complex dimension". The formula
q(M) = ΣM Z Z̄ - (ħ/2) tr M is the same in both, so T7 is right and T9's
wording is unsigned. Severity low.

### L6. Three-routes' function-linearity reference

`three-routes.class-relative-no-go` (formal and proof): "Every generator the
tame machinery supplies is C^∞-linear (Fact
singularity.p-reduced-metric-level-reading-many(ii) ...)". That entity is T5
Prop 9.6 on the mode-wise descents and has no clause (ii) on function
linearity; the intended target is `sheaf.function-linearity-tame-constructions`.
The same claim calls the proved half "the diagonality half of T5's Premise
7.30" where `singularity.class-relative-no-go-no-supplied` (T5 Thm C.8) proves
"the no-hopping half" and leaves pairing, which is C^∞-linear in its
coefficients and not diagonal, to the premise; three-routes names only
"differential operators" as uncovered. Structural slip. Severity low.

### L7. "Displaced into the physical side"

`sheaf.conservation-degeneracy-located` (T4 Prop 5.2): "Choosing μν < 0
instead ... the degeneration is displaced into the physical side".
`sheaf.one-sided-completion-singularity` (T4 Thm 8.12), with "coupling
constants satisfying μν < 0": "nondegenerate ... at every point of M̃ ...
Moreover no shadow wall forms anywhere in the manifold". Prop 5.2's "physical
side" is the side where the dying eigenvalue is positive; at Schwarzschild
(g_k = -r) that is r < 0, outside the manifold, as
`note.sheaf.conservation-degeneracy-boundary-sharp-example` explains. The
word, not the mathematics, conflicts. Severity low.

### L8. (L) for (L_E)

The one-liners of `angle.imported-singularity-papers-state-selection`
("premises (Q) and (L) supply ... the ultralocal generator class") and
`descent-lift.imported-descent-modes-univalence-supplied-class` ("pairing
excluded by the locality premise (L)") mean T5's boundary-mode locality
`singularity.l-boundary-mode-locality`, (L_E). In T5, (L) is the rate model's
two-sector postulate (`singularity.rate-models-kinematic-inputs-l-u`), and
`singularity.envelope-endpoint-why-boundary-mode-locality` uses "(L), (U),
(C), (I) and (L_E)" side by side. The namesakes tool does not see (L_E),
because its pattern does not match "(L$_E$)". Severity low.

### L9. Even physical states and an odd physical ψ

`singularity.p-univalence` (T5 Premise 7.8): "physical states of the boundary
modes are even under the grading ... so they vanish on the odd sector".
`angle.hop-across-cut` (Prop 4.2(ii)): "ψ is odd, hence of definite parity and
physical under the univalence rule". A vector of definite parity defines an
even state, so both hold; the wording invites the opposite reading. Severity
low.

### L10. (S) in every tower

`dark-tower-matter.hypothesis-s-slot-statistics`: title "Hypothesis (S)
carried to every tower", one-liner "in every tower the constituent slots are
fermionic modes", formal "Used only where stated".
`note.dark-tower-matter.why-s-fails-three-dimensions-not`: "In three
dimensions ... the slot-level states are not representations of the global
form." The one-liner states more than the formal level. Severity low.

### L11. ν order one, or 1/(16π)

`singularity.c2-cell-density` (T5 Axiom 10.2): "ν fermionic modes per Planck
cell, with ν an order-one constant". `scrambling.epoch-modular-period-two-unknowns-become`
(T8 Thm 4.3) predicts ν = 1/(16π) ≈ 0.020 (1/(16π ln 2) ≈ 0.029 in T5's
convention). Not a contradiction of substance; the postulate's wording is
looser than the prediction it feeds. Severity low.

### L12. The geometric modular condition, with and without faithfulness

`obj.singularity.geometric-modular-condition-g` (T5): "A faithful state
satisfies (G) ... Faithfulness is part of the condition, not a consequence of
it". `obj.state-selection.geometric-modular-condition`: "A state ω satisfies
(GMC) if its modular automorphism group is the flow", with no faithfulness
clause, and `state-selection.rate-discharge-hypothesis-iii` then derives
faithfulness ("so the state is faithful"). Since a modular group presupposes
faithfulness, the note's derivation is circular as worded. Severity low.

---

## Checked and dissolved

These were raised as candidates and dissolved on reading. They are listed so
they are not raised again.

- `singularity.class-relative-no-go-no-supplied`, `three-routes.class-relative-no-go`
  (no supplied generator hops) against `angle.hop-across-cut`,
  `angle.hop-sea-filled-pairing`: the hop is stated to be outside the supplied
  class.
- `descent-lift.within-supplied-dynamics-descent-has-no` (no lift) against
  `descent-lift.lift-costs-one-rung-per-mode` (a lift "exists as a
  supplied-class coupling applied to a paired Thouless record"): the record's
  preparation needs the number-changing generator, as Thm 4.2 says.
- `transport.door-one-way`, `descent-lift.imported-pinching-one-way-door` (no
  unital homomorphism back) against the descent-lift note's reversible lift: a
  lift is a dilation, not a homomorphism.
- `field-theory.no-canonical-commutation-relations-tower` and
  `field-theory.imported-statistics-no-go-palatial-algebra` against
  `singularity.bosonisation-bridge-s-wave-sector` and
  `hawking.current-commutator-exactly-edge-split` (bosons from fermion
  bilinears): FT excludes bounded single-floor CCR pairs and says "bosons made
  of fermions are not excluded"; the currents are unbounded or act on an
  edge-clean subspace.
- `sheaf.no-equivariant-value-wall` (no canonical ladder partner) against
  `sheaf.one-sided-completion-singularity` (a ladder pair k* = n_0/2ν exists):
  exists against canonical; T5 Fact B.3 says the frame and partner "are
  choices inside it".
- `sheaf.conservation-degeneracy-absolute-form` against
  `odd-extensions.exceptional-algebra-residue-completion-both-sides`: the
  latter's complement changes type, which the absolute form allows.
- `standard-model.bracket-composite-lands` against
  `standard-model.under-s-bracket-direction-charged-not`: the bracket is not a
  vev; products with it give multiples of the 10 form.
- `correspondence.no-real-lorentzian-vacuum-half-flat` against the nonlinear
  graviton and the googly conjecture: complexified or palatial settings.
- `dark-matter.reduced-response-gravity-needs-supporting-stress` (g = 1)
  against T14b's averaged projector: T14b projects pressure forces, not
  gravity.
- Uniqueness: the minimal completions of T1 (type N: Cl(p+1,q+1); type C:
  two one-generator ascents, one algebra), T2 (Cl(p+r,q+r)), T14a's single
  extensions and the T12 "minimal massive" and T13 "maximal" composites are
  minimal for different questions; no two results claim to be the unique or
  minimal X for the same X with different answers.
- Numerical checks on restatements (unit-ball shares, Kasner exponents and
  densities, Clifford classification values, hypercharges and anomaly sums,
  the frozen point's norm, d_b, the Z_6 lattice): all agree with their
  originals.
