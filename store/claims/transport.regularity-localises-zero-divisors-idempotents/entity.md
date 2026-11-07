---
id: transport.regularity-localises-zero-divisors-idempotents
kind: claim
version: 3
title: Regularity localises zero divisors at idempotents
status: proved
region: transport
subject: zero-divisors
tags: [idempotents]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, duplicate link at Leon''s decisions'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
review: typed
derivations:
- name: main
  uses:
  - transport.classification-real-clifford-algebras@3
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:2.8
- kind: check
  ref: check.py::check_regularity_and_idempotents
- kind: check
  ref: check.py::check_controls_invertible_and_quaternions
locators:
  paper: T01
  number: Lem 2.8
  label: lem:regular
  line: 547
extraction:
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Decision item E7 (routine; no retirement): the consequence clause overlaps std-algebra.zero-divisors-annihilated (d), (e), the general statement and home; recorded under extraction.overlaps_with (a clause-level overlap, no pinned link).'
  overlaps_with:
  - id: std-algebra.zero-divisors-annihilated
    note: 'Decision E7: the consequence clause here is clause (d), (e) of std-algebra.zero-divisors-annihilated, kept as the general statement; overlap in part, so no pinned link.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: a x a = a solved exactly for 23 certified zero divisors in eight real Clifford algebras; e = xa and f = ax idempotents with a(1 - e) = 0, (1 - f)a = 0, ae = a, fa = a, e, f not 0 or 1; invertible and quaternion controls. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'Edge kept: the classification supplies semisimplicity; Wedderburn-Artin and von Neumann regularity
      are standard but proved in the paper, and no imported claim for them is in the store.'
---

## formal
Every semisimple Artinian ring, in particular every real Clifford algebra of nondegenerate form, is von Neumann regular. Consequently, if $a$ is a nonzero zero divisor in such a ring $A$, and $x$ satisfies $axa = a$, then $e = xa$ and $f = ax$ are idempotents with
\[
a(1 - e) = 0, \qquad (1 - f)a = 0, \qquad e, f \notin \{0, 1\}.
\]
Moreover $ae = a$ and $fa = a$.

## technical
Every semisimple Artinian ring, in particular every real Clifford algebra of nondegenerate form, is von Neumann regular: each $a$ has some $x$ with $axa = a$. If $a$ is a nonzero zero divisor and $axa = a$, then $e = xa$ and $f = ax$ are idempotents with $a(1 - e) = 0$, $(1 - f)a = 0$ and $e, f \notin \{0, 1\}$; moreover $ae = a$ and $fa = a$.

## lay
In the algebras of the series every element has a weak kind of inverse that undoes it partway. Applying that weak inverse to an element that cannot be divided by produces elements equal to their own squares, which pin down exactly where the failure sits. This is the step that turns every failure of division into a statement about such elements.

## one-liner
Real Clifford algebras of nondegenerate form are von Neumann regular, so a nonzero zero divisor $a$ with $axa = a$ is annihilated on each side by the nontrivial idempotents $xa$ and $ax$.
