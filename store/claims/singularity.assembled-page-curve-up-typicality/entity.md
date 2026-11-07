---
id: singularity.assembled-page-curve-up-typicality
kind: claim
version: 3
title: 'Assembled: the Page curve, up to typicality'
status: proved
region: singularity
subject: entropy
tags:
- radiation-spectrum
- entanglement
- classical-theorem
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
review: typed
derivations:
- name: main
  uses:
  - singularity.eviction-window-thermal-product-radiation-entropy@7
  - singularity.stretched-singularity-count@8
  - singularity.area-law-test@5
  - singularity.imported-page-average-entropy-subsystem@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_schmidt_equal_marginal_spectra
- kind: check
  ref: check.py::check_envelope_min_thermal_capacity
locators:
  paper: T05
  number: Fact 11.1
  label: thm:pagecurve
  line: 2225
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: equal nonzero marginal spectra of pure bipartite states with rank and purity bounds, and the envelope min(Sth, C) with turnover at half the initial entropy on an exact maximally entangled qubit model. Version 2 -> 3.'
  env: fact
  context_refs:
  - singularity.area-law-test
  - singularity.eviction-window-thermal-product-radiation-entropy
  - singularity.stretched-singularity-count
  typing:
    by: ai-typing-pass
    note: 'Left as imported with no derivations, Page''s theorem being the imported ingredient; the store has no
      separate imported entry for Page''s result to use as a standard route. Levels pass: lay now states the three
      hypotheses (purity, Page typicality, eviction-theorem inputs) and ''up to subleading corrections''.'
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - singularity.rate-models-kinematic-inputs-l-u
    added_about: []
    verdict: standalone
    note: 'Kept as imported, so no derivation: no proof uses it, the rate model being built to replace its typicality;
      that model''s premise (U) is taken from its hypothesis (i), recorded as lineage on the premise.'
  source_formal: 'Assume (i) the ascended description is globally pure, (ii) at each stage the joint state on radiation
    $\otimes$ partner-mode space is Page-typical, and (iii) the inputs of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy},
    whose clause (2) supplies the thermal arm. Let $\Sth(t)$ be the thermal accumulation of the emitted radiation
    and $C(t) = N_{\mathrm{6a}}(M(t))\ln 2 \approx S_{\mathrm{BH}}(M(t))$ the boundary-mode capacity of Step 6a,
    $N_{\mathrm{6a}}$ its mode count. Then

    \[

    S_{\mathrm{rad}}(t) \;=\; \min\bigl(\Sth(t),\, C(t)\bigr)

    \]

    up to subleading corrections: rising along Hawking''s curve, turning over at the crossing (about half the initial
    entropy), falling along the shrinking capacity, vanishing at complete evaporation. \emph{Assembly and provenance:}
    the capacity arm is the Schmidt inequality, self-contained (a pure bipartite state has equal marginal spectra,
    so $S_R = S_L \leq \ln\dim L = C$); the thermal arm is Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}(2)
    and needs boundary-mode locality, which is why (iii) is in the hypothesis line; saturation for typical states
    is Page''s theorem \cite{Page1993}, the imported ingredient and the reason this is a Fact rather than a theorem
    of this paper; hypothesis (i) supplies purity, the emission count supplies $\dim R$, Proposition \claimref{singularity.stretched-singularity-count}
    with the epoch supplies $\dim L$, Proposition \claimref{singularity.area-law-test} identifies the capacity with
    the area law, and monotone mass loss makes $C$ decreasing.'
  provenance_import:
    citation: D. N. Page, Average entropy of a subsystem, Phys. Rev. Lett. 71 (1993), 1291--1294.
    key: Page1993
    moved_to: singularity.imported-page-average-entropy-subsystem
  decision_pass:
    by: ai-decision-pass
    date: '2026-10-21'
    decision: 8
    note: Was status imported with no derivation; it is an assembly of three series results (eviction (2), the count,
      the area law) and Page's theorem, so it is now proved, with Page's theorem the separate import singularity.imported-page-average-entropy-subsystem.
      The proof is the paper's own 'Assembly and provenance' paragraph set out as steps.
---

## formal
Assume (i) the ascended description is globally pure, (ii) at each stage the joint state on radiation $\otimes$ partner-mode space is Page-typical, and (iii) the inputs of Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}, whose clause (2) supplies the thermal arm. Let $\Sth(t)$ be the thermal accumulation of the emitted radiation and $C(t) = N_{\mathrm{6a}}(M(t))\ln 2 \approx S_{\mathrm{BH}}(M(t))$ the boundary-mode capacity of Step 6a, $N_{\mathrm{6a}}$ its mode count. Then
\[
S_{\mathrm{rad}}(t) \;=\; \min\bigl(\Sth(t),\, C(t)\bigr)
\]
up to subleading corrections: rising along Hawking's curve, turning over at the crossing (about half the initial entropy), falling along the shrinking capacity, vanishing at complete evaporation. \emph{Assembly and provenance:} the capacity arm is the Schmidt inequality, self-contained (a pure bipartite state has equal marginal spectra, so $S_R = S_L \leq \ln\dim L = C$); the thermal arm is Theorem \claimref{singularity.eviction-window-thermal-product-radiation-entropy}(2) and needs boundary-mode locality, which is why (iii) is in the hypothesis line; saturation for typical states is Page's theorem \cite{Page1993} (\claimref{singularity.imported-page-average-entropy-subsystem}), the imported ingredient and the reason this is a Fact rather than a theorem of this paper; hypothesis (i) supplies purity, the emission count supplies $\dim R$, Proposition \claimref{singularity.stretched-singularity-count} with the epoch supplies $\dim L$, Proposition \claimref{singularity.area-law-test} identifies the capacity with the area law, and monotone mass loss makes $C$ decreasing.

## technical
Assume the ascended description is globally pure, that at each stage the joint state on radiation and partner modes is Page-typical, and the inputs of the eviction theorem. With $\Sth(t)$ the thermal accumulation of the emitted radiation and $C(t) = N_{\mathrm{6a}}(M(t))\ln 2 \approx \SBH(M(t))$ the boundary-mode capacity, the radiation entropy is $S_{\mathrm{rad}}(t) = \min(\Sth(t), C(t))$ up to subleading corrections.

The capacity arm is the Schmidt bound for a pure bipartite state, the thermal arm comes from the eviction theorem and needs boundary-mode locality, and saturation for typical states is imported from Page's theorem on the average entropy of a subsystem.

## lay
The Page curve describes how the entropy of a black hole's radiation should behave if no information is lost: it rises, turns over at about half the initial entropy, and falls back to zero. This entry assembles that curve in the framework, up to small corrections, using the count of modes at the singularity as the black hole's capacity. It assumes that the full description stays pure, that the joint state of radiation and partner modes is typical in Page's sense, and that the inputs of the eviction theorem hold. The key step, that typical states reach the largest allowed entropy, is taken from Page's result rather than proved here.

## one-liner
Under purity, Page typicality and the eviction-theorem inputs, the radiation entropy is $\min(\Sth(t), C(t))$ up to subleading corrections, by Page's theorem.
