---
id: standard-model.spectrum-run
kind: claim
version: 6
title: The spectrum run
status: proved
region: standard-model
subject: standard-model
tags: [refutation, running-and-unification, confronted-with-data]
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
  - standard-model.imported-one-loop-running-trace-ratio@1
  - standard-model.weak-angle-over-derived-generation@5
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
  - label:prop:desert
- kind: check
  ref: check.py::check_closed_form_and_values
- kind: check
  ref: check.py::check_higgs_and_generations
- kind: check
  ref: check.py::check_no_common_meeting
- kind: check
  ref: check.py::check_scales_and_spread
locators:
  paper: T12
  number: Prop 6.2
  label: prop:desert
  line: 1217
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the exact one-loop solution and its values, the Higgs-free value, inert generations, distinct pairwise meetings, and the GeV scales and alpha_s spread by rigorous bounds. Version 4 -> 5. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 5 -> 6.'
  env: proposition
  context_refs:
  - standard-model.imported-one-loop-running-trace-ratio
  - standard-model.places-outside-state-space
  - standard-model.weak-angle-over-derived-generation
  outside_pilot_cites:
  - ButlerT14
  - ButlerT3
  typing:
    by: ai-typing-pass
    added:
    - standard-model.imported-one-loop-running-trace-ratio
    - standard-model.weak-angle-over-derived-generation
    note: 'Added the imported running Fact and the weak-angle proposition (which supplies the derived
      content as a representation of a simple group, so the unification condition applies); added a standard-route
      through the running Fact since the paper says these numbers are the grand-unification literature''s.
      Levels pass: lay now keeps one loop, the record inputs, the conditional survival of 3/8, (S) for
      the intermediate symmetry and the observation level; one-liner adds the record inputs and the only-if
      clause.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - standard-model.imported-one-loop-running-trace-ratio
    - standard-model.weak-angle-over-derived-generation
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: Hypothesis (S) added to the main derivation's assumes (the review found that (S) reached the seven
      partner-sector running results only through this proposition, which did not list it). The proof now
      says where the slot statistics enter, cited with claimref; the paper's proof is kept in orig-proof-main.tex.
      The standard-route derivation (the grand-unification literature's numbers) is left without (S).
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
The running Proposition \claimref{standard-model.weak-angle-over-derived-generation} deferred is performed here at one loop, in the normalisation and with the matching relations of Fact \claimref{standard-model.imported-one-loop-running-trace-ratio}(a): $a_{1} = \tfrac35\,\alpha_{Y}^{-1}$, $\alpha_{\mathrm{em}}^{-1} = \tfrac53 a_{1} + a_{2}$, $\sin^{2}\theta_{W}(M_{Z}) = \alpha_{\mathrm{em}}(M_{Z})/\alpha_{2}(M_{Z}) = \alpha_{\mathrm{em}}\,a_{2}$. The unification condition determines $\sin^{2}\theta_{W}(M_{Z})$ as an exact rational function of the inputs $\alpha_{\mathrm{em}}^{-1}(M_{Z})$, $\alpha_{s}^{-1}(M_{Z})$ and the coefficients $b_{i}$. With the Standard Model coefficients $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$, those of three derived generations and one Higgs doublet, the doublet being imported rather than derived (Observation \claimref{standard-model.places-outside-state-space}(b)), and the inputs $\alpha_{\mathrm{em}}^{-1}(M_{Z}) = 128$, $\alpha_{s}(M_{Z}) = 0.118$ (the record's values to this precision \cite{PDG2024}), the prediction is $\sin^{2}\theta_{W}(M_{Z}) = 78761/379488 = 0.2075\ldots$ with $M_{U} \approx 7 \times 10^{14}$ GeV, against the measured $0.2312$, whose record uncertainty is in the fourth decimal place \cite{PDG2024}: a ten-percent miss, about ninety times the spread the prediction inherits from the record's $\alpha_{s} = 0.1180 \pm 0.0009$ alone ($\pm 0.00027$), before two-loop and threshold effects; and the three couplings do not meet at a common scale, the pairwise meetings of $(a_{1}, a_{2})$, $(a_{1}, a_{3})$ and $(a_{2}, a_{3})$ falling at three different values of $L = \ln(M_{U}/M_{Z})$. So the natural conjecture, the desert (that the derived content, with the one imported doublet, alone connects the structural scale to experiment), is false, whatever the number of generations, complete multiplets being inert, and without the doublet the miss is larger, $\sin^{2}\theta_{W}(M_{Z}) = 3457/16992 = 0.2034$: as the precision era established for minimal unification generally \cite{Amaldi1991}, and as the framework, deriving the content, inherits. The refutation has a quantitative form: with partner-type intermediate content, the supersymmetric coefficients $(\tfrac{33}{5}, 1, -3)$ being the known working example, the same exact function returns $\sin^{2}\theta_{W}(M_{Z}) = 6539/28320 = 0.23089\ldots$ with $M_{U} \approx 2 \times 10^{16}$ GeV, the three pairwise meetings at the record falling at $2.0$, $2.2$ and $2.3 \times 10^{16}$ GeV, within about fifteen percent of one another in scale: agreement at the $10^{-3}$ level. The framework's $3/8$ therefore survives experiment only if the running between the weak and structural scales differs from that of the derived content: either the spectrum between the scales carries partner-like content, which this paper does not derive, or the gauge symmetry is enlarged at an intermediate scale, which Section \ref{sec:split} derives from the split between slots and pairs under Hypothesis (S); whether the framework's own pair and tower structure, every mode already paired and eight towers derived \cite{ButlerT3, ButlerT14}, supplies it is the running programme's question, stated here as its first exact target and flagged at observation level. The closed-form arithmetic is proved; the running, the coefficients and the measured values are Fact \claimref{standard-model.imported-one-loop-running-trace-ratio}(a)'s, at assembly and record level.

## technical
At one loop $a_{i}(M_{Z}) = a_{U} + \tfrac{b_{i}}{2\pi}L$ with $L = \ln(M_{U}/M_{Z})$, and with the matching $\alpha_{\mathrm{em}}^{-1} = \tfrac53 a_{1} + a_{2}$ the unification condition fixes $\sin^{2}\theta_{W}(M_{Z})$ as an exact rational function of $\alpha_{\mathrm{em}}^{-1}$, $\alpha_{s}^{-1}$ and the $b_{i}$. With the Standard Model coefficients $(\tfrac{41}{10}, -\tfrac{19}{6}, -7)$, three derived generations and one imported Higgs doublet, and $\alpha_{\mathrm{em}}^{-1} = 128$, $\alpha_{s} = 0.118$, it gives $\sin^{2}\theta_{W}(M_{Z}) = 78761/379488 \approx 0.2075$ against the measured $0.2312$, and the three couplings meet pairwise at three different scales, so the desert conjecture is false.

With the supersymmetric coefficients $(\tfrac{33}{5}, 1, -3)$ the same function gives $6539/28320 \approx 0.2309$ with $M_{U} \approx 2 \times 10^{16}$ GeV. So the framework's $3/8$ survives experiment only if the running between the weak and structural scales differs from that of the derived content, through partner-like content or an intermediate symmetry. The closed-form arithmetic is exact; the running, coefficients and measured values are imported.

## lay
The framework fixes how the electromagnetic and weak forces compare at a very high energy, but testing that means running the force strengths down to energies we can measure. In a one-loop calculation with the measured inputs, using only the particles the paper derives plus one imported Higgs doublet, the run misses the measured value by about ten percent and the three forces never meet at one point, as has been known for the simplest unified theories since the early 1990s. Supersymmetric-style partner particles bring the miss down to about one part in a thousand, so, if the framework's value is to survive, something beyond the derived content must change the running: partner-like particles, which the paper does not derive, or an enlarged symmetry at an intermediate energy, which it derives under Hypothesis (S). Whether the framework's own structure supplies this is left open at observation level.

## one-liner
At one loop with the record inputs, the derived content with one imported doublet predicts $\sin^{2}\theta_{W}(M_{Z}) = 78761/379488 \approx 0.2075$ against $0.2312$, refuting the desert, while the supersymmetric coefficients give $0.2309$; the framework's $3/8$ survives only if the running differs from that of the derived content.
