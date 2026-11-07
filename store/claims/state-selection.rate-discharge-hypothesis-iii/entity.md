---
id: state-selection.rate-discharge-hypothesis-iii
kind: claim
version: 9
title: The rate under the geometric modular condition, with hypothesis (iii) presupposed
status: proved
region: state-selection
subject: thermality
tags: [hawking-temperature, recovers-known-physics, modular-theory]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-state-selection, the series'' standard disclaimer'
review: typed
outside_ga:
  kind: complex-analysis
  why: 'the KMS strip i beta and the continuation lambda -> i theta in the proof are those of T05''s single-mode atoms in the spacetime radial plane and of the partner result, which keep a commuting complex unit; the atom''s modes anticommute with I_4 (conventions, known limit 1)'
about:
- obj.singularity.geometric-modular-condition-g
derivations:
- name: main
  uses:
  - singularity.plane-rate@4
  - state-selection.euclidean-partner-curvature-selected@4
  - singularity.kms-uniqueness-factor@5
  - singularity.universality-temperature-under-g@3
  assumes:
  - singularity.p-univalence@2
  - singularity.r-regularity-fixed-locus@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_kms_state_is_the_faithful_gibbs_state
- kind: check
  ref: check.py::check_one_beta_for_all_modes
- kind: check
  ref: check.py::check_conjugation_closes_at_two_pi
- kind: check
  ref: check.py::check_calibration_beta_is_eight_pi_m
locators:
  paper: T05-state-selection
  number: Thm 5.3
  label: thm:rate
  line: 282
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: i beta (KMS strip) and lambda -> i theta are the continuations of T05''s atom, whose modes anticommute with I_4. Declared complex-analysis.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: KMS forcing the faithful Gibbs state, one beta for all modes, the conjugation period 2 pi, and beta = 8 pi M. Version 8 -> 9.'
  env: theorem
  context_refs:
  - singularity.modular-descent
  - singularity.universality-temperature-under-g
  - synthesis.state-selection-r-and-le-against-t05
  typing:
    by: ai-typing-pass
    added:
    - state-selection.universality-temperature
    - state-selection.p-univalence
    - state-selection.r-regularity-fixed-locus
    note: 'Added the universality corollary the statement invokes and the hypotheses (P) and (R) as assumes;
      the cited modular descent theorem is the target of the discharge, not a premise. Levels pass: lay
      now names premises (P) and (R).'
  i4_conversion:
    by: ai-i4-pass
    date: '2026-10-21'
    converted: []
    kept:
    - $i\beta$ (KMS strip) and $\lambda \mapsto i\theta$ (analytic continuation)
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - state-selection.universality-temperature
    - state-selection.p-univalence
    note: "Cited (P) at the graded-sign clause of the KMS condition, the one step where evenness of the state under the parity automorphism enters."
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: [7, 2, 4]
    note: 'Id replacement only: the assumes edge (pin @2 kept) and the proof claimref moved from the retired state-selection.p-univalence to singularity.p-univalence, the same premise (merge of duplicates); version 5 -> 6.
      Decisions 2 and 4 (second agent, same day; version not bumped again, the bump to 6 already marks
      this pass): the proof now reads the continued translation on each chiral half of the spinors,
      as narrowed state-selection.euclidean-partner-curvature-selected clause (4) states, rather than
      as a rotation of the curvature-selected plane on vectors, which T05 Prop 7.21(3) excludes; the
      proof and technical level name the KMS flow as the boost''s phase flow Ad(e^{itK}); flow_note recorded.'
  correction_pass:
    by: ai-colony-2026-10-22-toe
    date: '2026-10-22'
    open_problem: op.folded-state-selection-note
    note: 'Circularity removed: the GMC presupposes faithfulness (a modular group exists only for a faithful
      state; T05 Def 7.12 says so), so the theorem cannot discharge hypothesis (iii). Formal, technical,
      lay, one-liner and proof now say it is presupposed, and point to T05 Thm 7.20 for the discharge.
      Title changed so that this entity and singularity.rate-discharge-hypothesis-iii, which differ in
      content, no longer share a title. No edge changed; version 6 -> 7.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 8: the state-selection note''s duplicates were retired (merged into the T05 entities), so the
      uses move to singularity.kms-uniqueness-factor and singularity.universality-temperature-under-g and the about link
      to obj.singularity.geometric-modular-condition-g; the assumes edge moves from the note''s own (R)
      (state-selection.r-regularity-fixed-locus, retired) to T05''s (R), singularity.r-regularity-fixed-locus, since the
      theorem''s single-mode conclusions need only T05''s (R) with (P) (synthesis.state-selection-r-and-le-against-t05 (iv)).
      Formal and proof now say which (R) is assumed. Conclusion unchanged.'
  namesake_note: 'The id names a discharge of hypothesis (iii) that this result no longer claims: since version 7
    it presupposes faithfulness, which the geometric modular condition contains, and the discharge is T05''s
    Theorem 7.20, singularity.rate-discharge-hypothesis-iii. Ids are permanent, so the id is kept; read the title.'
  flow_note: 'both: the KMS condition and the Gibbs state are for the phase flow e^{-i omega t} on the modes
    (T05 Thm 7.16, T07 Def 2.7), the Euclidean rotation of T05 Prop 7.21, through the GMC; the continuation
    lambda -> i theta starts from the rotor flow exp(lambda sigma/2) (T05 Thm 6.3, T08 Lem 4.2), whose rapidity
    is the flow parameter in which the period 2 pi is read.'
---

## formal
Assume (P) and (R), the latter in T05's form (\claimref{singularity.r-regularity-fixed-locus}: on each mode the two orderings of every ladder correlator meet after one period of the regular Euclidean section), and that the state satisfies the GMC of Definition \claimref{obj.singularity.geometric-modular-condition-g}. Then the modular period in rapidity is exactly $2\pi$, so by Corollary \claimref{singularity.universality-temperature-under-g} and the calibration of \cite[Prop.~6.2]{ButlerT5},
\[
\beta \;=\; \frac{2\pi}{\kappa} \;=\; 8\pi M , \qquad T \;=\; \frac{\kappa}{2\pi} \;=\; \frac{1}{8\pi M} \;=\; \TH ,
\]
Hypothesis (iii) of \cite[Thm.~7.3]{ButlerT5}, that the state be faithful, that is cyclic and separating for the one-sided algebra, is presupposed here and not derived: a state has a modular automorphism group only if it is faithful, so the GMC contains it. Its discharge without the GMC is T05's Theorem \claimref{singularity.rate-discharge-hypothesis-iii}, from T05's (R) on each mode.

## technical
Assume (P), the regularity premise (R) in the form the main paper states it, mode by mode, and that the state satisfies the geometric modular condition. By KMS uniqueness the state is the Gibbs state of the boost's phase flow $\operatorname{Ad}(e^{itK})$ at some $\beta$, and regularity of the continued correlation functions at the fixed locus forces the modular period in rapidity to be exactly $2\pi$, the angle at which the conjugation action of the curvature-selected Euclidean rotor closes, that rotor carrying the continued boost on each chiral half of the spinors. With the universality of the temperature and the calibration of rapidity against Schwarzschild time, $\beta = 2\pi/\kappa = 8\pi M$ and $T = \kappa/2\pi = 1/8\pi M = \TH$.

The cyclic-and-separating hypothesis of modular descent is not derived here. The geometric modular condition speaks of the state's modular automorphism group, which exists only for a faithful state, so the condition already contains that hypothesis; the full-rank Gibbs matrix at finite nonzero $\beta$ is consistent with it but cannot discharge it. The main paper discharges it from its own form of (R), mode by mode, without the modular condition.

## lay
Given the univalence and regularity premises (P) and (R), and the condition that the modes' internal clock runs along the black hole's time symmetry, smoothness at the horizon forces the clock's period to be exactly one full turn. Converting that turn into ordinary time gives the Hawking temperature. A technical condition, that the state be faithful, is built into the modular condition and so is assumed here, not derived; the main paper derives it separately.

## one-liner
Under (P), (R) and the geometric modular condition the modular period in rapidity is $2\pi$, so $T = \kappa/2\pi = 1/8\pi M = \TH$; faithfulness, hypothesis (iii) of modular descent, is presupposed by the condition, not derived.
