---
id: neutrino.imported-ceiling-under-hypothesis-u-arrow
kind: claim
version: 6
title: 'Imported: the ceiling under Hypothesis (U), the arrow, and the flag covariance'
status: proved
region: neutrino
subject: neutrinos
tags: [hypothesis-u, matter-asymmetry, seesaw-and-majorana]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T15, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation@5
  - dark-matter.ceiling-valued-inherited-success@5
  - dark-matter.orientation-arrow-seventeenth-refutation@9
  - standard-model.hyp-s-slot-statistics@9
  assumes:
  - dark-matter.hyp-u-equal-rank-one-eigenvalues@3
  - dark-matter.premise-cpt-covariance@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_seesaw_inversion_and_light_root
- kind: check
  ref: check.py::check_two_ends_of_the_range
locators:
  paper: T15
  number: Fact 2.5
  label: fact:ceiling
  line: 570
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the seesaw inversion and light root, and the two ends m_b^2/m_3 = 3.5e11 GeV and m_t^2/m_3 = 6e14 GeV with ratio 1.7e3, at the record values and over the PDG input box. Version 5 -> 6.'
  source_formal: |-
    The dark-matter paper's rung scale is its Hypothesis (U): that the rank-one eigenvalues of the different sectors coincide at the ceiling, so that the neutrino's Dirac eigenvalue there equals the common leading-order value; under (U) the seesaw $m_{3} = m_{D}^{2}/M_{R}$, used there as standard physics and available here only under Premise (M) below, values $M_{\mathrm{rung}} = M_{R} = m_{D}^{2}/m_{3}$ from the observed $m_{3}$ in the range $m_{b}^{2}/m_{3} \approx 3.5 \times 10^{11}$ GeV to $m_{t}^{2}/m_{3} \approx 6 \times 10^{14}$ GeV, the ends being the two readings of (U), with the alignment of Fact \claimref{neutrino.imported-indifference-faces-democratic-alignment-rank} explicitly never equating magnitudes across sectors (this is a fit of the same quantity from the same datum as Remark \ref{rem:valuation} below, and is read there). The descent's asymmetry is inherited initial data, a declared stance, universal over the oriented towers by that paper's Premise P4 (a theorem for the mirror, void for the odd towers); the orientation is the only CP-violating mechanism the framework itself supplies, uniqueness among all conceivable mechanisms not being claimed there, with a relaxing $\theta$-angle named as unexcluded. The identification of $\nu_{R}$ with a singlet grade is flag-covariant (the flag conjugate exchanges the two singlet grades wholesale; that paper states this for the grade-three state, and the argument transfers unchanged to the grade-zero state this paper identifies), so no completion of the orientation can exclude it; this holds under Hypothesis (S) and with the gauge sector's CPT-evenness as a premise there. The descent reheating $T_{\mathrm{desc}}$ is taken there at the ceiling or below it. \emph{Provenance:} \cite[Prop.~6.4, Prop.~5.1, Prop.~5.2, App.~A]{ButlerT14}.
  env: fact
  context_refs:
  - dark-matter.asymmetry-arrow-counted-fifteenth-refutation
  - dark-matter.ceiling-valued-inherited-success
  - dark-matter.orientation-arrow-seventeenth-refutation
  - neutrino.imported-indifference-faces-democratic-alignment-rank
  unresolved_refs:
  - rem:valuation
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'edges unchanged: the three uses are the cited dark-matter results the fact restates; the families
      alignment is mentioned only as a comparison and was not added. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S); assumes dark-matter.hyp-u-equal-rank-one-eigenvalues
      added because the paper names Hypothesis (U) as a condition of this result. Levels pass: the lay
      replaced ''each comes with the conditions stated there'' by the named conditions ((U), (M), the
      declared stance, the own-CP-source scope, (S) and the gauge sector''s CPT-evenness); the one-liner
      now names (M), (S) and the stance; the technical names the stance.'
    added:
    - standard-model.hyp-s-slot-statistics
    - dark-matter.hyp-u-equal-rank-one-eigenvalues
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 12
    note: "Decisions 12 and 8. (12) The restatement said T14 states the flag covariance for the grade-three state and that the argument transfers to grade zero; T14 Prop 5.2 states it for the hypercharge-zero singlet at grade zero, so the formal level and the proof now say so (the technical, lay and one-liner levels did not carry the phrase). The paper's wording is kept in source_formal and orig-proof-main.tex. (8) Assumes CPT covariance, a new postulate, which the statement names as the premise on the gauge sector's CPT-evenness; cited in the proof."
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The dark-matter paper's rung scale is its Hypothesis (U): that the rank-one eigenvalues of the different sectors coincide at the ceiling, so that the neutrino's Dirac eigenvalue there equals the common leading-order value; under (U) the seesaw $m_{3} = m_{D}^{2}/M_{R}$, used there as standard physics and available here only under Premise (M) below, values $M_{\mathrm{rung}} = M_{R} = m_{D}^{2}/m_{3}$ from the observed $m_{3}$ in the range $m_{b}^{2}/m_{3} \approx 3.5 \times 10^{11}$ GeV to $m_{t}^{2}/m_{3} \approx 6 \times 10^{14}$ GeV, the ends being the two readings of (U), with the alignment of Fact \claimref{neutrino.imported-indifference-faces-democratic-alignment-rank} explicitly never equating magnitudes across sectors (this is a fit of the same quantity from the same datum as Remark \ref{rem:valuation} below, and is read there). The descent's asymmetry is inherited initial data, a declared stance, universal over the oriented towers by that paper's Premise P4 (a theorem for the mirror, void for the odd towers); the orientation is the only CP-violating mechanism the framework itself supplies, uniqueness among all conceivable mechanisms not being claimed there, with a relaxing $\theta$-angle named as unexcluded. The identification of $\nu_{R}$ with a singlet grade is flag-covariant (the flag conjugate exchanges the two singlet grades wholesale; that paper states this for the hypercharge-zero singlet at grade zero, the state this paper identifies), so no completion of the orientation can exclude it; this holds under Hypothesis (S) and with the gauge sector's CPT-evenness as a premise there. The descent reheating $T_{\mathrm{desc}}$ is taken there at the ceiling or below it. \emph{Provenance:} \cite[Prop.~6.4, Prop.~5.1, Prop.~5.2, App.~A]{ButlerT14}.

## technical
Imported from the dark-matter paper. Under its Hypothesis (U), that the rank-one eigenvalues of the different sectors coincide at the ceiling, the seesaw $m_{3} = m_{D}^{2}/M_{R}$ (standard physics there, available here only under Premise (M)) values $M_{\mathrm{rung}} = M_{R} = m_{D}^{2}/m_{3}$ between $m_{b}^{2}/m_{3} \approx 3.5 \times 10^{11}$ GeV and $m_{t}^{2}/m_{3} \approx 6 \times 10^{14}$ GeV, the ends being the two readings of (U); the families alignment never equates magnitudes across sectors.

The descent's asymmetry is inherited initial data, a declared stance, universal over the oriented towers by that paper's democracy premise; the orientation is the only CP-violating mechanism the framework itself supplies, uniqueness not being claimed and a relaxing $\theta$-angle named as unexcluded. The identification of $\nu_{R}$ with a singlet grade is flag-covariant, so no completion of the orientation can exclude it, under Hypothesis (S) and with the gauge sector's CPT-evenness as a premise. The descent reheating $T_{\mathrm{desc}}$ is taken at the ceiling or below it.

## lay
This collects the results from the companion dark-matter paper that the neutrino paper relies on. They are an estimate of the heavy neutrino scale, which assumes that the leading masses of all kinds of matter particle are equal at the highest energy (Hypothesis (U)) and, in this paper, that the framework supplies the heavy neutrino's Majorana mass (Premise (M)); the declared stance that the matter-antimatter imbalance was inherited rather than generated, with the framework's orientation as the only source of matter-antimatter asymmetry the framework itself supplies (a relaxing $\theta$-angle is not excluded); and a symmetry argument, holding if the slots behave like the pairs (Hypothesis (S)) and if the force sector respects the matter-antimatter symmetry, showing that fixing the framework's orientation cannot remove the right-handed neutrino.

## one-liner
Imported: the rung scale under Hypothesis (U) and Premise (M), the inherited asymmetry (a declared stance) with the orientation as the framework's own CP source, and the flag covariance of the $\nu_{R}$ identification under Hypothesis (S).
