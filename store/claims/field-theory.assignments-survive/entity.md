---
id: field-theory.assignments-survive
kind: claim
version: 3
title: The Standard-Model assignments survive
status: proved
region: field-theory
subject: quantum-fields
tags: [hypercharge-and-anomalies, pseudoscalar-and-centre]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of FT, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - standard-model.quarks-leptons-two-level-fermion-content@5
  - standard-model.hypercharge-global-form-pair-counting-consistency@5
  - standard-model.imported-anomaly-coefficients@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_SMC.py
  tags:
  - id:C3
  - id:C4
- kind: check
  ref: check.py::check_listing_and_conjugate_anomaly_free
- kind: check
  ref: check.py::check_exactly_four_patterns
- kind: check
  ref: check.py::check_conjugate_representations_with_i4
locators:
  paper: FT
  number: Prop 10.1
  label: prop:smsurvive
  line: 267
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the anomaly sums of the listing, its conjugate and the mixed listing, the four anomaly-free conjugation patterns of 64, and the conjugate SU(2) and SU(3) intertwiners. Version 2 -> 3.'
  env: proposition
  typing:
    by: ai-typing-pass
    added:
    - standard-model.hypercharge-global-form-pair-counting-consistency
    - standard-model.imported-anomaly-coefficients
    - standard-model.quarks-leptons-two-level-fermion-content
    note: 'Added the Standard-Model paper''s content and hypercharge results, the listing the proposition
      examines, and the imported anomaly conditions it applies to the 64 conjugation patterns. Levels
      pass: levels written from scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    stated_role:
    - standard-model.quarks-leptons-two-level-fermion-content
    - standard-model.hypercharge-global-form-pair-counting-consistency
    - standard-model.imported-anomaly-coefficients
---

## formal
T12's content, hypercharges and anomaly cancellation do not involve the complex unit: its listing and its conjugate differ by the outer automorphism $Y \mapsto -Y$, $3 \leftrightarrow \bar 3$, and both are anomaly-free. Of the 64 conjugation patterns of one generation exactly four are anomaly-free, so every multiplet except the self-conjugate $\nu^c$ must enter with the same status relative to $I_4$.

## technical
The Standard-Model paper's content, hypercharges and anomaly cancellation do not involve the complex unit: its listing and the conjugate listing differ by the outer automorphism $Y \mapsto -Y$, $3 \leftrightarrow \bar 3$, and both are anomaly-free. Of the $64$ conjugation patterns of one generation exactly four are anomaly-free, so every multiplet except the self-conjugate $\nu^c$ must enter with the same status relative to $I_4$.

## lay
Choosing the spacetime volume element as the complex unit could in principle disturb the series' derivation of the particle content. It does not: the content, the charges and their consistency do not depend on the unit, and the only freedom is to conjugate all the particles together. Mixed choices are inconsistent, except for the neutral right-handed neutrino.

## one-liner
The Standard-Model content, hypercharges and anomaly cancellation do not involve the complex unit, and only four of $64$ conjugation patterns are anomaly-free, so every multiplet but $\nu^c$ enters alike relative to $I_4$.
