---
id: standard-model.under-s-mirror-inherits-desert
kind: claim
version: 6
title: Under (S), the mirror inherits the desert
status: proved
region: standard-model
subject: dark-matter
tags: [running-and-unification, mirror-sector]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, mention of the coupling premise brought in line with Leon''s decisions'
  version: 6
  source: maintainer pass 2026-11-07 (decisions)
review: typed
about:
- obj.standard-model.one-threshold-spectrum-admissible
derivations:
- name: main
  uses:
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.imported-coefficient-sum-indices@1
  - standard-model.imported-one-loop-running-trace-ratio@1
  - standard-model.imported-sectors-superselection-mirror-copy@3
  - standard-model.no-tower-but-one-contributes-towers@3
  - standard-model.weak-angle-over-derived-generation@5
  - standard-model.hyp-s-slot-statistics@9
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_coefficients_with_and_without_lepton_doublet
- kind: check
  ref: check.py::check_trace_normalisations
- kind: check
  ref: check.py::check_anomaly_without_lepton_doublet
- kind: check
  ref: check.py::check_mirror_same_equations_no_sharing
locators:
  paper: T12
  number: Cor 8.6
  label: cor:mirror
  line: 1317
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 5 -> 6. Leon''s answer 2 (C1): the proof''s mention of the mirror''s coupling values now says the common ceiling and coupling are the store''s own premise (synthesis.common-ceiling-coupling-premise), not T14''s Premise P2, which as scoped does not reach a coupling; the corollary still asserts nothing about coupling values and takes no edge to it. Wording of a mention.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: one-loop coefficients and ratios with and without the lepton doublet, the trace normalisations, the anomaly sum, and the mirror copy giving the same equations with no cross-tower contribution. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    removed:
    - dark-matter.mirror-tower-copy-one
    added:
    - standard-model.imported-one-loop-running-trace-ratio
    - standard-model.weak-angle-over-derived-generation
    - standard-model.hyp-s-slot-statistics
    note: 'Removed the direct T14 copy theorem because the proof reaches the mirror copy only through
      the imported sectors fact and says the T14 item is not imported here; added the one-loop running
      fact (normalisation and equations) and the weak-angle proposition (which fixes k = 17/9 for the
      740/289 ratio), the latter being the least certain; no standard-route, since the paper does not
      present the corollary as a standard result. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: the lay now names Hypothesis
      (S) and keeps the one-loop qualifier.'
  env: corollary
  context_refs:
  - standard-model.imported-one-loop-running-trace-ratio
  - standard-model.weak-angle-over-derived-generation
  eqrefs: 1
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.imported-one-loop-running-trace-ratio
    - standard-model.weak-angle-over-derived-generation
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
Under Hypothesis (S), the mirror tower's one-loop coefficients are $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ with one mirror Higgs doublet, its ratio is $r_{0} = 218/115$, and its one-loop equations \eqref{eq:run} are this tower's: from any boundary values at which this tower's couplings fail to meet, the mirror's fail to meet in the same way. Without (S) the mirror copy has no lepton doublet; its coefficients in the normalisation of Fact \claimref{standard-model.imported-one-loop-running-trace-ratio}(a) are $(\tfrac72, -\tfrac{25}{6}, -7)$, with ratio $46/17$, but that normalisation is the one (S) supplies through $\mathrm{Spin}(10)$. The content's own trace normalisation, that of the ratio $9/26$ of Proposition \claimref{standard-model.weak-angle-over-derived-generation}, gives the ratio $740/289$ instead, and without the lepton doublet the content is anomalous, its $[SU(2)]^{2}U(1)_{Y}$ sum being $\tfrac12$ per generation; so without (S) the content poses no meeting question. Whatever content resolves the desert in this tower, the mirror carries a copy of it by Fact \claimref{standard-model.imported-sectors-superselection-mirror-copy}, so the resolution is duplicated, never shared: no content of this tower enters the mirror's run and none of the mirror's enters this one's.

## technical
Under Hypothesis (S) the mirror tower has the same particle listing as ours, so its one-loop coefficients are $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ with one mirror Higgs doublet, its ratio is $r_{0} = 218/115$, and its one-loop running equations are ours: from any boundary values at which our couplings fail to meet, the mirror's fail in the same way. The statement concerns the equations, not the values of the mirror's couplings.

Without (S) the mirror copy has no lepton doublet; its coefficients are $(\tfrac72, -\tfrac{25}{6}, -7)$ with ratio $46/17$ in the normalisation that (S) supplies, or ratio $740/289$ in the content's own trace normalisation, and the content is anomalous, with $[SU(2)]^{2}U(1)_{Y}$ sum $\tfrac12$ per generation, so it poses no meeting question. Whatever content resolves the desert in our tower, the mirror carries its own copy: the resolution is duplicated, never shared.

## lay
The three forces of the Standard Model change strength with energy, and in the minimal theory they fail to meet at a single point, the problem known as the desert. Assuming the slots behave like the pairs (Hypothesis (S)), the mirror sector has exactly the same particles, so at one loop it has exactly the same problem. Whatever fixes it in our sector must be copied in the mirror; the two sectors cannot help each other.

## one-liner
Under Hypothesis (S) the mirror tower's one-loop running is this tower's, with coefficients $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$ and $r_{0} = 218/115$, so any resolution of the desert is duplicated in the mirror, never shared.
