---
id: singularity.parity-protection
kind: claim
version: 2
title: Parity protection
status: proved
region: singularity
subject: entropy
tags: [finite-models]
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
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T05.py
  tags:
  - num:12.1
- kind: check
  ref: check.py::check_every_single_qubit_marginal_is_thermal
- kind: check
  ref: check.py::check_support_constraint_and_populations
- kind: check
  ref: check.py::check_non_diagonal_unitaries_break_protection
locators:
  paper: T05
  number: Lem 12.1
  label: lem:parity
  line: 2332
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: single-qubit marginals stay diag(c^2, s^2) under four programs of number-diagonal gates (complex phases included), the support constraint, and two non-diagonal controls. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: No store premises; a direct support-constraint argument on the model.
---

## formal
At every stage of the model, and for \emph{any} sequence of number-basis-diagonal window unitaries, the reduced density matrix of each individual qubit, radiation or window, early or evicted, is exactly its thermal matrix $\operatorname{diag}(c_k^2, s_k^2)$: diagonal, with the original populations, regardless of the scrambling.

## technical
In the model, for any sequence of number-basis-diagonal window unitaries, the reduced density matrix of every individual qubit, radiation or window, early or evicted, is exactly its thermal matrix $\operatorname{diag}(c_k^2, s_k^2)$.

The reason is a support constraint: each pair contributes only $|00\rangle$ and $|11\rangle$ components, diagonal unitaries preserve that constraint and every squared amplitude, so single-qubit coherences vanish and populations never change.

## lay
In the toy model, every individual quantum, whether in the radiation or still inside, looks exactly thermal on its own, however the inside is scrambled by phase gates. Any information is therefore invisible to measurements of one quantum at a time. It can only show up in correlations among several quanta.

## one-liner
In the model, under number-diagonal window unitaries every single qubit stays exactly in its thermal state $\operatorname{diag}(c_k^2, s_k^2)$.
