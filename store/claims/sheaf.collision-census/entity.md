---
id: sheaf.collision-census
kind: claim
version: 2
title: Collision census
status: proved
region: sheaf
subject: walls
tags: [kasner, classification]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_repeated_exponent_census
- kind: check
  ref: check.py::check_zero_exponent_forces_a_second_zero
- kind: check
  ref: check.py::check_scan_of_rational_parametrisation
locators:
  paper: T04
  number: Lem 9.12
  label: lem:census
  line: 1285
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the repeated-exponent and zero-exponent reductions 2s(3s - 2) and 2t(t - 1) for every slot, and a scan of the rational parametrisation locating coincidences only on the Taub and Schwarzschild orbits. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: "Self-contained algebra on the Kasner constraints; no edges changed."
---

## formal
On the constraint variety: (i) triples with a repeated exponent are, up to permutation, exactly $(-\tfrac13, \tfrac23, \tfrac23)$ and $(0,0,1)$; (ii) if any exponent vanishes the triple is $(0,0,1)$ up to permutation. An exponent cannot cross zero alone: zeros come in pairs.

## technical
On the Kasner constraint variety, $p_1 + p_2 + p_3 = 1$ and $p_1^2 + p_2^2 + p_3^2 = 1$, the triples with a repeated exponent are, up to permutation, exactly $(-\tfrac13, \tfrac23, \tfrac23)$ and $(0,0,1)$, and any triple with a vanishing exponent is $(0,0,1)$ up to permutation. Hence an exponent cannot cross zero alone: zeros come in pairs.

## lay
Kasner geometries near a singularity are labelled by three exponents obeying two fixed relations. This result finds every case in which two exponents coincide: up to reordering there are only two. It also shows that one exponent can never pass through zero on its own; whenever one is zero, another is too.

## one-liner
On the Kasner constraint variety the only triples with a repeated exponent are $(-\tfrac13, \tfrac23, \tfrac23)$ and $(0,0,1)$ up to permutation, so exponents vanish only in pairs.
