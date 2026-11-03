---
id: one-relation.imported-flag-arrow-superselection
kind: claim
version: 7
title: 'Imported: the flag, the arrow, and superselection'
status: proved
region: one-relation
subject: descent
tags: [matter-asymmetry, superselection, witt-index]
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
review: draft
about:
- obj.dark-matter.witt-flag
derivations:
- name: main
  uses:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation@5
  - dark-matter.orientation-arrow-seventeenth-refutation@9
  - dark-matter.superselected-hence-dark-exactly-stable@5
  - standard-model.hyp-s-slot-statistics@9
  assumes:
  - dark-matter.premise-cpt-covariance@2
  - dark-matter.premise-flag-as-datum@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_witt_flags_of_three_pairs
- kind: check
  ref: check.py::check_single_orientation_bit
- kind: check
  ref: check.py::check_conjugate_reverses_bit
locators:
  paper: T16
  number: Fact 2.5
  label: fact:flag
  line: 521
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: finite core on Cl(3,3): the 8 half-choices of three null pairs, their single orientation bit (volume-element sign, 4/4 split), and the flag conjugate reversing the bit while two swaps keep it. Version 6 -> 7.'
  open_problem: op.trichotomy-exhaustiveness
  correction:
    by: ai-correction
    date: '2026-10-22'
    note: 'Version 5 restates the bit''s premises at the strength of the corrected seventeenth refutation (v6): two premises (CPT covariance with its action clause covering the gauge couplings, stronger than the stored premise''s wording; Hypothesis (S)) and one reading (the flag is a datum of each solution). The exhaustiveness of the trichotomy is no longer used for the last step; the proof says so where it names the postulate. The assumes edge to dark-matter.premise-trichotomy-exhaustive is kept only because removing an assumes edge is a maintainer decision: it is now unused and should be dropped, after which the postulate has no user in this entity.'
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Version 6: the reading that the flag is a datum of each solution is now the named postulate dark-matter.premise-flag-as-datum, assumed here so holds_given tracks it; the unused assumes edge to dark-matter.premise-trichotomy-exhaustive is dropped (that postulate is retired); the CPT premise (v2) now states the action clause at the strength used here, so the text no longer calls it stronger than the premise. Pins moved to the seventeenth refutation v7 and the CPT premise v2.'
  locator_divergence: 'T16 Fact 2.5 restates T14 Prop 5.2 under its three premises; this store version follows the corrected Proposition, whose three premises are CPT covariance (with its full action clause), Hypothesis (S) and the flag as a datum, the trichotomy''s exhaustiveness not among them.'
  env: fact
  context_refs:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - dark-matter.orientation-arrow-seventeenth-refutation
  - dark-matter.superselected-hence-dark-exactly-stable
  outside_pilot_cites:
  - ButlerT12
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'kept all three dark-matter edges, which are the cited sources the fact restates; its E204 comes
      from an unsupported premise upstream in the dark-matter paper, outside this list Hypothesis pass:
      assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S). Levels pass: the lay level and one-liner now name Hypothesis (S) among the three premises,
      and the lay level marks the inherited asymmetry as a declared stance.'
    added:
    - standard-model.hyp-s-slot-statistics
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: "Assumes the two premises of the T14 orientation argument the statement names that had no store postulate (CPT covariance, the trichotomy's exhaustiveness), new postulates cited in the proof; Hypothesis (S), the third, was already assumed. The statement is unchanged."
  maintainer_pass_hyp_s:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The descent plants one Witt flag on the three-pair structure, a choice of half of each pair, whose single orientation bit is at once the arrow of time and the particle-antiparticle orientation. That this bit is initial data is a CPT-covariance argument the dark-matter paper states under three premises, the third of which, the exhaustiveness of its trichotomy, the corrected argument does not use. It rests on three premises: that CPT conjugation, an antilinear conjugation, is an isomorphism of every kinematic structure and leaves every action functional invariant, the gauge couplings included (premised for the derived gauge sector); Hypothesis (S), the Standard-Model paper's open premise that the composite's slots carry fermionic statistics; and the premise that the flag is a datum of each solution, planted by the descent, rather than part of the kinematic structure. Its last step reaches initial data directly, as a conjugation-odd bit on conjugation-stable solution spaces, which excludes a parameter of the laws without any exhaustiveness. The flag is a $\mathbb{Z}_{2}$ datum, an orientation, and not a choice of frame vector. That the framework inherits its asymmetry rather than generating it, with two unexplained continuous numbers, is a declared stance there and is carried as one here. Tower charge is superselected exactly, making sectors mutually dark rather than mutually exclusive. \emph{Provenance:} \cite[Def.~2.10, Prop.~4.1, Prop.~5.1 (stance), Prop.~5.2 (stated under three premises; the corrected argument replaces the exhaustiveness premise by the flag as a datum)]{ButlerT14}; Hypothesis (S) is declared in \cite[\S5]{ButlerT12}.

## technical
The descent plants a single Witt flag on the three-pair structure, a choice of one half of each pair. Its one orientation bit is at once the arrow of time and the particle-antiparticle orientation, and it is a $\Z_2$ datum, an orientation, not a choice of frame vector. That this bit is initial data is a CPT-covariance argument resting on three premises: that CPT conjugation, which is antilinear, is an isomorphism of every kinematic structure and leaves every action invariant, the gauge couplings included (premised for the derived gauge sector); Hypothesis (S), the open premise that the composite's slots carry fermionic statistics; and the premise that the flag is a datum of each solution rather than part of the kinematic structure. The exhaustiveness of a trichotomy, a premise of the paper's version, is not used: the bit is shown to be initial data directly, which rules out its being a parameter of the laws.

That the framework inherits its matter asymmetry rather than generating it, with two unexplained continuous numbers, is a declared stance and is carried over as one. Tower charge is superselected exactly, so the sectors are mutually dark rather than mutually exclusive.

## lay
The step down from the enlarged algebra to ordinary physics involves one binary choice, an orientation. That single bit is at once the direction of time's arrow and the distinction between matter and antimatter. Under three stated premises, a matter-antimatter (CPT) symmetry of the structures and laws, Hypothesis (S) that the composite's slots behave as fermions, and the assumption that the choice belongs to each universe rather than to the theory's fixed structure, it must be supplied as initial data rather than derived, and, as a declared stance, the framework takes its matter asymmetry as given rather than explaining it. A separate exact rule keeps different sectors invisible to one another rather than forbidden.

## one-liner
Imported: the descent's single Witt-flag orientation bit is both the arrow of time and the particle-antiparticle orientation, is initial data under three stated premises, CPT covariance, Hypothesis (S) and the flag as a datum, and tower charge is exactly superselected.
