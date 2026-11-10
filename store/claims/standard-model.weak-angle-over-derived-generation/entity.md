---
id: standard-model.weak-angle-over-derived-generation
kind: claim
version: 5
title: The weak angle over the derived generation
status: proved
region: standard-model
subject: standard-model
tags: [running-and-unification, recovers-known-physics]
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
review: typed
derivations:
- name: main
  uses:
  - standard-model.imported-fock-representation-clifford-algebra-bogoliubov@1
  - standard-model.imported-one-loop-running-trace-ratio@1
  - standard-model.under-s-composites-state-space-spinor@6
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
- name: standard-route
  uses:
  - standard-model.imported-one-loop-running-trace-ratio@1
  proof: proof-standard-route.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:prop:unification
- kind: check
  ref: check.py::check_three_eighths_over_generation
- kind: check
  ref: check.py::check_without_lepton_doublet
- kind: check
  ref: check.py::check_fibre_and_doublets
locators:
  paper: T12
  number: Prop 6.1
  label: prop:unification
  line: 1205
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the trace ratios 3/8, 9/26, 9/10 and 3/4 by state-by-state sums with hypercharges from the generator. Version 4 -> 5.'
  env: proposition
  context_refs:
  - standard-model.hypercharge-global-form-pair-counting-consistency
  - standard-model.spectrum-run
  typing:
    by: ai-typing-pass
    added:
    - standard-model.hypercharge-global-form-pair-counting-consistency
    - standard-model.imported-one-loop-running-trace-ratio
    - standard-model.hyp-s-slot-statistics
    note: 'Added the hypercharge theorem whose content and hypercharges the sums run over; added a standard-route
      through the running Fact, since the paper calls 3/8 the classic value that SU(5) obtains by embedding
      the observed content in an assumed group. Hypothesis pass: assumes standard-model.hyp-s-slot-statistics
      added because its statement holds under Hypothesis (S). Levels pass: lay now names (S) and keeps
      the simple-group hypothesis behind reading 3/8 as the unification angle.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.hypercharge-global-form-pair-counting-consistency
    - standard-model.hyp-s-slot-statistics
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
payload:
- kind: value
  clause: 3/8
  python: '(lambda s: s[0] / s[3])(_sums(_generation())) == F(3, 8) and _sums(_generation())[0] == 2 and
    _sums(_generation())[3] == 2 + F(10, 3)'
  note: sum T3^2 / sum Q^2 = 2/(2 + 10/3) = 3/8 over one derived generation
- kind: value
  clause: 9/26 without the lepton doublet
  python: '(lambda s: s[0] / s[3])(_sums([c for c in _generation() if c[0] != ''L''])) == F(9, 26)'
---

## formal
Over one generation of the content of Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}, quark and lepton doublets and the four singlets (the lepton under Hypothesis (S)), with $Q = T_{3} + Y$,
\begin{equation}
\frac{\sum T_{3}^{2}}{\sum Q^{2}} \;=\; \frac{2}{2 + \tfrac{10}{3}} \;=\; \frac{3}{8},
\end{equation}
and this is $\sin^{2}\theta_{W}$ at the unification scale under the hypothesis of Fact \claimref{standard-model.imported-one-loop-running-trace-ratio}(b), the classic value, here over derived rather than assumed content. The value rests on (S) with the lepton doublet, which contributes $\tfrac12$ to each sum: over the unconditional content alone, the quark doublet and the four singlets, the same ratio is $9/26$. Over the fibre $\C^{2} \otimes \C^{3}$ alone the ratio is $9/10$, unconditionally, and over the two doublets alone $3/4$, again under (S). Comparison with the observed $0.2312$ requires renormalisation-group running from the unification scale (the structural scale $M_{U}$), which Proposition \claimref{standard-model.spectrum-run} performs.

## technical
Over one generation of the derived content, quark and lepton doublets and four singlets with the lepton under Hypothesis (S), and with $Q = T_{3} + Y$, one finds $\sum T_{3}^{2} = 2$ and $\sum Y^{2} = \tfrac{10}{3}$, so $\sum T_{3}^{2}/\sum Q^{2} = 3/8$. Under the imported hypothesis that the content forms a representation of a simple unifying group, this ratio is $\sin^{2}\theta_{W}$ at the unification scale: the classic value, here over derived rather than assumed content.

The value rests on (S): without the lepton doublet the ratio is $9/26$, over the fibre $\C^{2} \otimes \C^{3}$ alone it is $9/10$ unconditionally, and over the two doublets alone $3/4$ under (S). Comparison with the measured value needs running from the unification scale down to $M_{Z}$.

## lay
The weak mixing angle measures how the electromagnetic and weak forces share out between them. In unified theories it takes the value 3/8 at the unification energy, worked out from the charges of one family of particles. Here the same ratio comes out over the particle content the paper derives, provided one accepts the paper's hypothesis about the composite's modes (Hypothesis (S)), which is needed for the lepton; reading it as the weak angle at unification assumes, as unified theories do, that the particles fit into one simple larger symmetry group. Comparing with experiment requires running the value down to everyday energies, which is done separately.

## one-liner
Over one derived generation, with the lepton under Hypothesis (S), $\sum T_{3}^{2}/\sum Q^{2} = 3/8$, which is $\sin^{2}\theta_{W}$ at unification under the simple-group hypothesis.
