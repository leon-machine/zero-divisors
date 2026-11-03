---
id: transport.units-span
kind: claim
version: 2
title: Units span
status: proved
region: transport
subject: zero-divisors
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
review: typed
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T01.py
  tags:
  - num:6.3
- kind: check
  ref: check.py::check_every_element_is_a_sum_of_two_units
- kind: check
  ref: check.py::check_singular_sets_are_the_eigenvalues
locators:
  paper: T01
  number: Lem 6.3
  label: lem:sumofunits
  line: 1381
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for samples in six Clifford algebras, upper-triangular 3 x 3 matrices, Mat_2 and the dual numbers, the singular lambdas of L_a are at most dim A and a = (a - lambda) + lambda with both two-sided invertible; singular sets equal the eigenvalues on hand samples. Version 1 -> 2.'
  env: lemma
  typing:
    by: ai-typing-pass
    note: 'No premises: the proof is self-contained linear algebra.'
---

## formal
In a finite-dimensional unital $\R$-algebra $A$, every element is a sum of two invertible elements.

## technical
In a finite-dimensional unital $\R$-algebra $A$ every element is a sum of two invertible elements. For $a \in A$, the element $a - \lambda 1$ fails to be invertible only for the finitely many real $\lambda$ with $\det(L_a - \lambda\,\mathrm{id}) = 0$, so some $\lambda \neq 0$ makes both $a - \lambda 1$ and $\lambda 1$ invertible, and $a = (a - \lambda 1) + \lambda 1$.

## lay
In any finite-dimensional algebra over the real numbers, even an element that cannot be divided by is the sum of two elements that can. The trick is to subtract a suitable multiple of 1, which leaves something invertible for all but finitely many choices.

## one-liner
Every element of a finite-dimensional unital real algebra is a sum of two invertible elements.
