---
id: field-theory.imported-statistics-no-go-palatial-algebra
kind: claim
version: 2
title: 'Imported: the statistics no-go and the palatial algebra'
status: proved
region: field-theory
subject: quantum-fields
tags: [no-go, car-algebra, conformal-spinors]
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
locators:
  paper: FT
  number: Fact 2.2
  label: fact:statistics
  line: 78
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the trace obstruction (scalar part of all commutators in Cl(2,4) and truncated realisations) and the polynomial realisation [Z^a, Zbar_b] = hbar delta_ab in four variables. Version 1 -> 2.'
  env: fact
  flags:
  - citation taken from inline provenance (no \cite)
  source_imported_from:
  - citation: T09, Prop. prop:statistics and Lemma lem:weyl
  typing:
    by: ai-typing-pass
    added:
    - correspondence.statistics-no-go
    - correspondence.symmetrised-quadratics-palatial-algebra
    note: 'The fact restates the twistor paper''s statistics no-go and palatial-algebra lemma, both in
      the store, so it was made a restatement (status proved, uses both); the Wielandt-Wintner sentence
      is a literature result the source names without a store entry. Levels pass: levels written from
      scratch, keeping every condition and level qualifier of the formal statement.'
derivations:
- name: main
  uses:
  - correspondence.statistics-no-go@2
  - correspondence.symmetrised-quadratics-palatial-algebra@5
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_no_finite_dimensional_representation
- kind: check
  ref: check.py::check_polynomial_realisation
---

## formal
The palatial algebra $[Z^\alpha, \bar Z_\beta] = \hbar\,\delta^\alpha_\beta$ has no nonzero finite-dimensional representation and no embedding into any finite-dimensional algebra. It is realised on polynomials by $\bar Z_\beta = -\hbar\,\partial/\partial Z^\beta$. \emph{Provenance:} T09, Prop.~prop:statistics and Lemma lem:weyl. For the bounded CAR algebra the corresponding statement is the Wielandt-Wintner theorem: no bounded operators satisfy $[a, a^*] = 1$.

## technical
The palatial algebra $[Z^\alpha, \bar Z_\beta] = \hbar\,\delta^\alpha_\beta$ has no nonzero finite-dimensional representation and no embedding into any finite-dimensional algebra, and it is realised on polynomials by $\bar Z_\beta = -\hbar\,\partial/\partial Z^\beta$. For the bounded CAR algebra the corresponding statement is the Wielandt-Wintner theorem: no bounded operators satisfy $[a, a^*] = 1$.

## lay
The canonical commutation relations of bosons cannot be realised by finite matrices, nor inside any finite-dimensional algebra such as a floor of the tower; they need infinitely many states, as in the standard representation on polynomials. Even in the infinite tower they cannot be realised by bounded operators.

## one-liner
The palatial algebra has no finite-dimensional representation or embedding and is realised on polynomials, and no bounded operators satisfy $[a, a^*] = 1$.
