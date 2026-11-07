---
id: dark-matter.orientation-arrow-seventeenth-refutation
kind: claim
version: 9
title: 'The orientation is the arrow: the seventeenth refutation'
status: proved
region: dark-matter
subject: dark-matter
tags: [refutation, matter-asymmetry, undetermined-input]
proposed_by:
  kind: ai
  session: colony-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.dark-matter.witt-flag
- obj.dark-energy.four-ways-number-enters-theory-shape
derivations:
- name: main
  uses:
  - dark-matter.imported-derived-generation-flag@6
  - dark-matter.imported-inputs-standard-model-chain@6
  - standard-model.chirality-two-halves-spinor-module-conjugation@6
  - dark-energy.four-alternatives-are-exhaustive-three-are@2
  - synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation@4
  - standard-model.hyp-s-slot-statistics@9
  assumes:
  - dark-matter.premise-cpt-covariance@3
  - dark-matter.premise-flag-as-datum@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T14.py
  tags:
  - label:prop:orientation
- kind: check
  ref: check.py::check_parameter_not_moved
- kind: check
  ref: check.py::check_flag_conjugate_odd
- kind: check
  ref: check.py::check_definition_logic
- kind: proof
  derivation: main
locators:
  paper: T14
  number: Prop 5.2
  label: prop:orientation
  line: 518
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content. Fix round: check_flag_conjugate_odd applies C = Ad(I6) o kappa on C^{2,4} to a Witt flag and its pure vacuum (exchanged with the conjugate vacuum); docstring (b) reworded. Version 8 -> 9.'
  open_problem: op.trichotomy-exhaustiveness
  env: proposition
  context_refs:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - dark-matter.imported-trichotomy-descents-data
  - neutrino.seesaw-what-gauge-invariance-proves-what
  outside_pilot_cites:
  - ButlerT15
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Version 6 removes the third premise, the trichotomy''s exhaustiveness (dark-matter.premise-trichotomy-exhaustive),
      which dark-energy.four-alternatives-are-exhaustive-three-are shows false in general. The last step
      is now proved against Definition obj.dark-energy.four-ways-number-enters-theory-shape directly:
      the CPT premise already covers the action, so conjugation maps each solution space onto itself,
      and a conjugation-odd bit is not constant on any nonempty solution space, which is clause (I).
      This is the argument T14 Fact 2.8 gives in words (the bit is data if it is anything), promoted
      to a step of the proof; it excludes a parameter of the laws for the bit and needs no exhaustiveness.
      The conclusion is unchanged. Two readings are made explicit: the CPT premise''s clause for the
      action is read as S_mu composed with conjugation equal to S_mu for every mu, and the flag is a
      datum of each solution planted by the descent, not part of the kinematic structure (were it kinematic,
      the bit would be (D) within each of two isomorphic theories). Uses: the Fact dark-matter.imported-trichotomy-descents-data
      is no longer needed and moves to context; the Definition and the four-alternatives proposition
      are added. Restatements one-relation.imported-flag-arrow-superselection and one-relation.record-chain-votes-measurement-without-collapse
      still assume the exhaustiveness postulate and need the same edit once this version is accepted;
      the postulate then has no user. dark-matter.imported-trichotomy-descents-data still says the orientation
      claim uses its clause (3) for the last step and needs the matching edit; neutrino.imported-ceiling-under-hypothesis-u-arrow
      and synthesis.mirror-asymmetry-route-one were checked and carry no exhaustiveness wording.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 7: step 1 no longer calls CPT conjugation "a real linear Z2 automorphism"; it is the antilinear composite (an anti-automorphism acting on fields as Ad(I6) composed with complex conjugation, in the field-action convention now stated in dark-matter.premise-cpt-covariance v2, after synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation, now a used result). The two readings of v6 became premises: the action clause at full strength is the CPT premise''s own clause (v2), and the flag as a datum is the new postulate dark-matter.premise-flag-as-datum, now assumed, so holds_given tracks it. Check (a) applies complex conjugation explicitly in Gaussian rational arithmetic (antilinearity, conjugation of the complex integrand, real-linear control). Conclusion unchanged.'
  locator_divergence: 'T14 Prop 5.2 states three premises, the third being the trichotomy''s exhaustiveness, and
    describes CPT conjugation as real linear. This store version departs from the paper''s statement: it drops
    the exhaustiveness premise and strengthens the proof''s last step, at the price of the action clause of the
    CPT premise for every mu, gauge couplings included (stated in that premise since its version 2), and the
    premise that the flag is a datum of each solution (dark-matter.premise-flag-as-datum); CPT conjugation is
    the antilinear composite.'
  maintainer_pass_hyp_s:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The Standard-Model paper left one absolute bit undetermined, the particle-antiparticle orientation, expected to be fixed by the charge-zero condition. The expectation is refuted by a $\mathbb{Z}_{2}$ covariance argument parallel to the trichotomy's rescaling one, on three premises: that CPT conjugation $C$ is an isomorphism of every kinematic structure and leaves every action functional $S_{\mu}$ of Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape} invariant, $S_{\mu}\circ C = S_{\mu}$, the gauge couplings included (\claimref{dark-matter.premise-cpt-covariance}; checked in the proof for the metric, the completion, the pairing and the action; premised for the imported gauge sector and for structures later papers add); Hypothesis (S), under which the Standard-Model paper's chirality proposition, the source of the relative-versus-absolute split, is proved (Fact \claimref{dark-matter.imported-derived-generation-flag}); and that the orientation flag is a datum of each solution, the sign of its complex structure relative to the Fock module's unit planted by the descent and not part of the kinematic structure (\claimref{dark-matter.premise-flag-as-datum}; were it kinematic, the bit would be constant on every solution space, hence dynamically fixed within each of two isomorphic theories, and the conclusion below would fail). Here $C$ is the composite of grade involution, reversal and the flag conjugate, an anti-automorphism; acting on fields as a symmetry does (vectors by its vector part, connections through the induced Lie algebra automorphism), it is $\mathrm{Ad}(I_{6}) \circ \kappa$, with $\kappa$ complex conjugation, so it is antilinear (\claimref{synthesis.cpt-conjugation-pseudoscalar-rotor-times-complex-conjugation}).

Anything the structures determine is conjugation-invariant, and the orientation is not. The charge-zero condition fixes all \emph{relative} structure \cite[Prop.~5.6]{ButlerT12}; under that reading the absolute bit is not kinematic, and since conjugation maps each solution space onto itself and exchanges the two orientations, the bit takes both values on every nonempty solution space: it is initial data in the sense of clause (I) of Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape}, and so neither dynamically fixed nor a parameter of the laws (Proposition \claimref{dark-energy.four-alternatives-are-exhaustive-three-are}). No exhaustiveness of the kinematic, dynamical and initial-data alternatives is used. It is the Witt flag of Proposition \claimref{dark-matter.asymmetry-arrow-counted-fifteenth-refutation}: the open orientation of the content derivation and the arrow of time are one choice, made once.

The descent measure carries two numbers and one bit. The neutrino sector supplies no orientation refutation condition: the identification of $\nu_{R}$ with the hypercharge-zero singlet at grade zero is flag-covariant (the conjugate flag exchanges the singlet grades zero and three), so no completion of the orientation could exclude it \cite{ButlerT15}.

This is the seventeenth refutation (the sixteenth is the neutrino paper's \cite[Prop.~4.1(1)]{ButlerT15}), in the pattern of the thirteenth and the trichotomy: what the framework cannot determine, it can prove it cannot determine, and locate.

## technical
The particle-antiparticle orientation, the one absolute bit the Standard-Model derivation left open, is not fixed by the charge-zero condition. The argument rests on three premises: that the CPT composite of grade involution, reversal and flag conjugation is an isomorphism of every kinematic structure and leaves every action functional and its parameters, gauge couplings included, unchanged (checked for the metric, the completion, the pairing and the action, premised for the imported gauge sector); Hypothesis (S); and that the orientation flag belongs to each solution rather than to the kinematic structure. The composite reverses products, and acting on fields as a symmetry it is the pseudoscalar rotor followed by complex conjugation, so the conjugation is antilinear, not real linear. Anything the structures determine is invariant under this $\mathbb{Z}_{2}$ conjugation, while the orientation is exchanged by it.

So the charge-zero condition fixes all relative structure and leaves the absolute bit kinematically underdetermined. Because the conjugation leaves each action, and the value of its parameter, unchanged, it carries every solution to a solution of the same theory with the opposite orientation; the bit therefore varies within each solution space, which is what initial data means in the action paper's classification, and it is neither fixed by the dynamics nor a parameter of the laws. The earlier third premise, that kinematic, dynamical and initial data exhaust the possibilities, is not needed. The bit is the Witt flag, so that the orientation of the derived content and the arrow of time are one choice made once. The neutrino sector supplies no refutation condition, since identifying $\nu_{R}$ with the hypercharge-zero singlet is flag-covariant, the conjugate flag exchanging the singlet grades $0$ and $3$.

## lay
Our universe is made of matter rather than antimatter, and in this framework a single yes-or-no choice decides which is which. Assuming that the matter-antimatter symmetry (CPT) respects every structure of the theory, its laws included (checked for the core structures, assumed for the imported forces and later additions), that the slots behave like the pairs (Hypothesis (S)), and that the choice belongs to each possible universe rather than to the theory's fixed structure (all three stated as assumptions), this result shows that none of the framework's laws can make that choice: the symmetry turns any possible universe into another possible universe of the same theory with the choice reversed. So the choice differs between solutions of one and the same theory, which makes it a starting condition rather than a setting of the laws, and it is the same choice that sets the direction of time.

## one-liner
Under CPT covariance (an antilinear conjugation) of the kinematic structures and of every action (gauge couplings included), Hypothesis (S), and the premise that the flag is a datum of each solution, the particle-antiparticle orientation takes both values on every solution space, so it is initial data (not a parameter of the laws), one choice with the arrow of time.
