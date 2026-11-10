---
id: one-relation.record-chain-votes-measurement-without-collapse
kind: claim
version: 8
title: 'The record chain votes: measurement without collapse'
status: proved
region: one-relation
subject: one-relation
tags: [measurement-and-records, superselection, live-prediction]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: 'maintainer pass, the recording remark entered as a premise and assumed, at Leon''s decisions'
  version: 7
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'premise wording: the branch weights are those of the stored Born account in its version 4, which hold under Premise (P) for a state sharp on an atom'
  version: 8
  source: maintainer pass of 2026-11-10
review: draft
derivations:
- name: main
  uses:
  - one-relation.imported-flag-arrow-superselection@7
  - one-relation.imported-indifference-instrument@4
  - one-relation.measure-indifference-borns-rule-located@4
  - standard-model.trichotomy-what-kind-number@12
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation@7
  - dark-matter.orientation-arrow-seventeenth-refutation@10
  - standard-model.hyp-s-slot-statistics@10
  assumes:
  - one-relation.recording-irreversible-stated-so-it-can@1
  - dark-matter.premise-cpt-covariance@3
  - dark-matter.premise-flag-as-datum@4
  - one-relation.recorded-sectors-superselected-premise@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T16
  number: Prop 6.5
  label: prop:vote
  line: 833
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: 'Version 7 -> 8. The branch weights are cited from one-relation.measure-indifference-borns-rule-located, which in its version 4 (Leon''s decision 4 of 10 November 2026) no longer obtains the squared-norm measure from indifference by the imported envariance argument: it obtains the weights under Premise (P), positivity of values, for a state sharp on an atom and for projectors self-adjoint for the split, and is not a derivation of the Born rule. The pin is moved 3 -> 4 and each level now says under which premises the weights hold; (P) enters through that result and no assumes edge is added here. Not shown, and said so in the formal level: that the state of system and records is sharp on an atom, and that the record projectors are self-adjoint for the laboratory''s split. The two arguments of the vote (the transposition and the counting argument), the two gaps and the registered stance are unchanged.'
  maintainer_pass_pin_review:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Pin review (second round): dark-matter.asymmetry-arrow-counted-fifteenth-refutation repinned 6 -> 7 (an extraction note only (Leon confirmed the theta-angle reading); N).'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7. Leon''s answer 6 (B3): the step the formal took from T16''s Remark rem:recording (not a store entity; it stood under unresolved_refs) is now the postulate one-relation.recorded-sectors-superselected-premise, assumed here (new assumes edge) and cited where the Remark was; rem:recording dropped from unresolved_refs; status stays proved, given it. Levels name the premise.'
  open_problem: op.trichotomy-exhaustiveness
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Version 5 counts the one bit under the premises of the corrected seventeenth refutation (v6): CPT covariance (its action clause covering the gauge couplings), Hypothesis (S) and the reading that the flag is a datum of each solution. The trichotomy''s exhaustiveness is no longer used; the proof names the postulate where it says so. The assumes edge to dark-matter.premise-trichotomy-exhaustive is kept only because removing an assumes edge is a maintainer decision: it is now unused and should be dropped.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 6: the reading that the flag is a datum of each solution is now the named postulate dark-matter.premise-flag-as-datum, assumed here so holds_given tracks it; the unused assumes edge to dark-matter.premise-trichotomy-exhaustive is dropped (that postulate is retired); the CPT premise (v2) now states the action clause at the strength used, so the text no longer calls it stronger than the premise. Pins moved to the seventeenth refutation v7, the flag-arrow Fact v6 and the CPT premise v2.'
  locator_divergence: 'T16 Prop 6.5 counts the bit under T14 Prop 5.2''s three premises; this store version follows the corrected Proposition, whose premises for the bit are CPT covariance, Hypothesis (S) and the flag as a datum.'
  env: proposition
  context_refs:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - dark-matter.orientation-arrow-seventeenth-refutation
  - one-relation.measure-indifference-borns-rule-located
  - standard-model.trichotomy-what-kind-number
  typing:
    by: ai-typing-pass
    added:
    - one-relation.measure-indifference-borns-rule-located
    - standard-model.trichotomy-what-kind-number
    - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
    - dark-matter.orientation-arrow-seventeenth-refutation
    - standard-model.hyp-s-slot-statistics
    note: 'Added the Born-measure proposition (the branch weights) and the three imported counts the counting
      argument is arithmetic on; no standard Everett or decoherence result is in the store for a standard
      route. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics added because its statement
      holds under Hypothesis (S). Levels pass: the lay level now names the indifference and irreversible-recording
      premises and Hypothesis (S), keeps the recording-limit disanalogy and the named residue, and calls
      the result a conditional stance; the one-liner adds (S) and the recording limit.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
    - dark-matter.orientation-arrow-seventeenth-refutation
    - one-relation.measure-indifference-borns-rule-located
    - standard-model.trichotomy-what-kind-number
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: "Assumes CPT covariance and the trichotomy's exhaustiveness, new postulates: the statement counts the bit under the dark-matter paper's three premises, of which only Hypothesis (S) was assumed here. Cited in the proof where the three premises are named. The statement is unchanged."
  maintainer_pass_hyp_s:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The question left standing by Premise \claimref{one-relation.recorded-sectors-superselected-premise} (the paper's Remark on recording) has the exact shape of a question this series has already answered at cosmic scale, and the transposition is recorded with its premises stated with their costs. At the origin the descent faced multiple superselected sectors, and the conclusion was threefold, each clause with its own source: selecting one sector would be an uncaused preference the indifference premise forbids (Fact \claimref{one-relation.imported-indifference-instrument}); superselection renders the sectors mutually \emph{dark} rather than mutually exclusive (Fact \claimref{one-relation.imported-flag-arrow-superselection}); hence all flaggable sectors are occupied, weighted by the one measure, and ``why is ours the visible one'' is indexical, not dynamical, which is the dark-matter paper's premise form of indifference, scoped there to the reversal orbit and extended here to all flag sectors (Fact \claimref{one-relation.imported-indifference-instrument}). After a measurement, by Premise \claimref{one-relation.recorded-sectors-superselected-premise} under Premise \claimref{one-relation.recording-irreversible-stated-so-it-can}, the laboratory presents the identical structure in miniature: flag sectors dynamically disconnected by irreversible recording. The same premises force the same conclusion: all branches occupied, mutually dark, with the experienced single outcome the view from inside one record chain. The weights of the branches are those of Proposition \claimref{one-relation.measure-indifference-borns-rule-located}, and they are conditional as that proposition is from its version 4: squared norms under Premise (P), positivity of values, for a state that is sharp on an atom and for branch projectors that are self-adjoint for the laboratory's split; indifference alone gives equal weights on exact orbits only. That the state of system and records is sharp on an atom, and that the record projectors are of that kind, is not shown; neither is a derivation of the Born rule claimed.

A second, independent argument closes from the other side. The framework's freedom is a \emph{fixed and finite count}: two numbers and one bit, counted across the series (Fact \claimref{one-relation.imported-flag-arrow-superselection}, \cite[Prop.~7.6]{ButlerT12}, \cite[Prop.~5.1, Prop.~5.2]{ButlerT14}), the two numbers on the dark-matter paper's declared stance that the framework inherits its asymmetry rather than generating it, and the bit under the three premises of the corrected orientation argument (CPT covariance, an antilinear conjugation whose action clause covers the gauge couplings; Hypothesis (S); and the flag as a datum of each solution, \claimref{dark-matter.premise-flag-as-datum}); the exhaustiveness of a trichotomy, the third premise of that paper's version, is not used. Dynamical collapse produces a new uncaused bit per event, unboundedly many, outside that count; on the stance and under the premises, a mechanism that uses freedom the framework does not possess is not an open alternative within it.

Two gaps are named so the vote can be refuted. First, the \emph{disanalogy}: tower superselection is exact and algebraic, while laboratory decoherence is emergent, irreversibility on the modular period rather than a theorem of charge, so the transposition holds in the recording limit and is structural-conditional there. Second, the \emph{residue}: indexicality dissolves ``why this branch'' as a dynamical question without answering it as an experiential one, and this paper says so. The vote is nonetheless testable, and a conditional stance is registered: no objective-collapse signature at any sensitivity, no spontaneous-localisation noise and no gravitationally induced collapse \cite{GRW1986, Penrose1996}, since any confirmed collapse mechanism would be the uncaused selector this framework forbids. Continued null results are consistent with this stance; one confirmed signature refutes the stance, the counting argument, and the vote together.

## technical
After a measurement, under the irreversible-recording premise and the premise that recorded sectors are superselected in the recording limit, the laboratory has the structure the series met at cosmic scale: flag sectors dynamically disconnected. The same premises, indifference forbidding an uncaused selection and superselection making the sectors mutually dark, give the same conclusion: all branches are occupied, and the single experienced outcome is the view from inside one record chain. The branches are weighted by the squared-norm measure where the stored Born account gives it: under Premise (P), positivity of values, for a state sharp on an atom, both assumed; this is not a derivation of the Born rule.

A second argument: the framework's freedom is a fixed finite count, two numbers and one bit (on the inherited-asymmetry stance and under the premises behind the bit, including Hypothesis (S)), while dynamical collapse needs a fresh uncaused bit per event. Two gaps are named: laboratory decoherence is emergent rather than exact, so the transposition is structural-conditional in the recording limit, and indexicality dissolves the question of why this branch dynamically without answering it experientially. The stance is testable: one confirmed objective-collapse signature refutes it.

## lay
When a measurement is made, the framework, granting its stated premises (that an unexplained preference is forbidden, that recording is irreversible and that recorded outcomes then cannot interfere, and, behind its count of free numbers, Hypothesis (S) on the slots' statistics), says every possible outcome happens, each in its own branch that cannot see the others, rather than one outcome being picked by a physical collapse. The weights of the branches are the squared-size rule only under a further assumption about averages, called (P), and for a state that is certain on one of the finest yes-or-no questions; neither is derived. It argues this in two ways: picking one outcome would be an unexplained preference, and collapse would need an endless supply of new random choices the framework does not have. The parallel with the cosmic case holds only in the limit of ideal recording, since laboratory decoherence is approximate, and the account leaves open why this branch is the one experienced. This is a testable, conditional bet: any confirmed sign of real wavefunction collapse would refute it.

## one-liner
Under the indifference, superselection, irreversible-recording and recorded-sector premises, with Hypothesis (S) behind the count, and in the recording limit, measurement leaves all branches occupied and no objective collapse, with squared-norm weights where the stored Born account gives them (under Premise (P) for a state sharp on an atom, both assumed), a stance refuted by any confirmed collapse signature.
