---
id: families.order-operations-matter-programme
kind: claim
version: 5
title: The order of operations in the matter programme
status: proved
region: families
subject: generations
tags: [ledger-audit, flavour-and-mixing]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T13, deposited version
review: typed
derivations:
- name: main
  uses:
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - families.imported-grade-three-direction-between-families@7
  - families.imported-tree-relations-family-no-go@6
  - standard-model.space-symmetric-doublet-mass-forms-two@5
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_family_breaking_first_fails
- kind: check
  ref: check.py::check_two_term_structure_fixes_both_ratios
- kind: check
  ref: check.py::check_one_sided_source_between_families
- kind: check
  ref: check.py::check_both_sources_carry_pair_number
- kind: proof
  derivation: main
locators:
  paper: T13
  number: Cor 8.3
  label: cor:order
  line: 927
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: 10 vev with a family matrix keeps m_e = m_d; the two-term coupling fixes both ratios jointly; the one-sided source acts only between families; both sources carry sum v_i^w_i. Version 4 -> 5.'
  env: corollary
  outside_pilot_cites:
  - ButlerT17
  typing:
    by: ai-typing-pass
    note: 'All four edges are the cited premises of the corollary and were kept; the E204 traces through
      the tree-relations fact to a Standard-Model premise outside this group. Hypothesis pass: assumes
      standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis (S). Levels
      pass: the lay now names Hypothesis (S), the 10-vev the no-go acts on, and the registered route.'
    added:
    - standard-model.hyp-s-slot-statistics
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), which supplies the species names, the family breaking cannot come first: by Fact \claimref{families.imported-tree-relations-family-no-go}(i) the family breaking acting on a $10$-vev leaves $m_{\mu} = m_{s}$ and $m_{e} = m_{d}$ exactly, and the observed second family needs the factor $3$ at the unification scale (Fact \claimref{families.imported-tree-relations-family-no-go}). Among one-family mass forms the factor is available in the module as the direction of Proposition \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}, and only there: the symmetric doublet mass forms of odd colour-singlet elements with the doublet's charges span the two-dimensional space of the $10$ form and the $T_{\mathrm{GJ}}$ form \cite[Prop.~9.32]{ButlerT12}. With three families there is a second source, the one-sided weighting of Proposition \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}(iii), whose antisymmetric form gives no one-family mass but does give entries between families through an antisymmetric family coupling (Fact \claimref{families.imported-grade-three-direction-between-families}). That direction requires the electroweak vev to couple not as a bare rung vector but as the rung vector wedged with the other rung's area bivector and with the pair-sector $\uu(1)$ generator. So the first result required of the weight programme is not a family texture but a \emph{pair-number-dependent rung coupling}: a derivation, from the mass mechanism, of a term of the form $w_{4}\wedge(v_{5}\wedge w_{5})\wedge\sum v_{i}\wedge w_{i}$ alongside the bare $w_{4}$, with the ratio of the two coefficients then fixing $m_{\mu}/m_{s}$ and $m_{e}/m_{d}$ jointly (the third family is where the bare $10$ relation $m_{b} \approx m_{\tau}$ is approximately right). Both sources carry the pair-number current, so the requirement stands on the route the Standard-Model paper registers, where the second family's factor comes through mixing with the third by the grade-three source and the role of that ratio passes to the coupling between the two families (Fact \claimref{families.imported-grade-three-direction-between-families}). The family breaking is the second step, acting on the resulting two-term structure; this is the order the capstone's table of open directions records for the matter programme \cite[Table~4]{ButlerT17}.

## technical
Under Hypothesis (S) the family breaking cannot come first: acting on a $10$-vev it leaves $m_{\mu} = m_{s}$ and $m_{e} = m_{d}$ exactly, while the second family needs the factor $3$ at unification. Among one-family mass forms that factor is available only through the $T_{\mathrm{GJ}}$ direction, since the symmetric doublet mass forms of odd colour-singlet elements with the doublet's charges span just the $10$ form and the $T_{\mathrm{GJ}}$ form. With three families the one-sided weighting is a second source, giving entries between families through an antisymmetric family coupling.

Both sources require the electroweak vev to couple as the rung vector wedged with the other rung's area bivector and the pair-sector generator. So the first requirement on the weight programme is a pair-number-dependent rung coupling, a term $w_{4} \wedge (v_{5} \wedge w_{5}) \wedge \sum_{i} v_{i} \wedge w_{i}$ beside the bare $w_{4}$, whose coefficient ratio fixes $m_{\mu}/m_{s}$ and $m_{e}/m_{d}$ jointly, or on the registered route passes to the coupling between the two families. The family breaking is the second step.

## lay
This result fixes the order in which the series' programme for explaining particle masses must proceed. Assuming the slots behave like the pairs (Hypothesis (S)), rearranging the three families acting on the simplest Higgs-type vacuum (the $10$) cannot fix the wrong mass equalities between leptons and quarks, so that cannot be the first step. Instead the first step must be a specific new coupling in the mass mechanism that treats leptons and quarks differently and supplies the needed factor of three (on the route the series has chosen, through the link between the second and third families). Only after that does the breaking of the symmetry among the families come in.

## one-liner
Under Hypothesis (S) the family breaking cannot come first: the weight programme must first derive a pair-number-dependent rung coupling supplying the Georgi-Jarlskog factor, with the family breaking acting second.
