---
id: transport.exceptional-division-algebras
kind: claim
version: 3
title: The exceptional division algebras
status: proved
region: transport
subject: zero-divisors
tags: [clifford-classification, classification]
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
  uses:
  - transport.classification-real-clifford-algebras@3
  - std-algebra.blade-basis@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_witnesses_exist_exactly_off_the_exceptional_lists
- kind: check
  ref: check.py::check_exceptional_algebras_are_sums_of_division_algebras
- kind: check
  ref: check.py::check_verdicts_match_the_classification_table
locators:
  paper: T01
  number: Prop 3.2
  label: prop:exceptions
  line: 572
extraction:
  maintainer_pass:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.blade-basis where the proof uses them. Version 2 -> 3.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: for all signatures with n <= 6, zero-divisor and nilpotent witnesses exist exactly off the two lists, the five exceptional algebras carry positive norm forms on each summand, and the verdicts match the d-table. Version 1 -> 2.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Edges kept: the proof reads the result off the classification alone.'
---

## formal
$\Cl(p,q)$ contains no zero divisors if and only if $(p,q) \in \{(0,0), (0,1), (0,2)\}$, where it is $\R$, $\C$, $\HH$ respectively. It contains no nilpotents if and only if $(p,q) \in \{(0,0), (0,1), (0,2), (1,0), (0,3)\}$: the three division algebras together with $\Cl(1,0) \cong \R \oplus \R$ and $\Cl(0,3) \cong \HH \oplus \HH$.

## technical
$\Cl(p,q)$ has no zero divisors exactly when $(p,q) \in \{(0,0), (0,1), (0,2)\}$, where it is $\R$, $\C$ or $\HH$. It has no nilpotents exactly for those three together with $\Cl(1,0) \cong \R \oplus \R$ and $\Cl(0,3) \cong \HH \oplus \HH$.

Both lists are read off the classification of real Clifford algebras: a matrix algebra $\Mat_k(\mathbb{F})$ with $k \geq 2$ contains the nilpotent matrix unit $E_{12}$, a direct sum contains the zero divisors $(x, 0)$, a division algebra contains neither, and a dimension count fixes the signatures.

## lay
In most Clifford algebras some nonzero elements multiply to zero, so division sometimes fails. This result lists the only exceptions: the real numbers, the complex numbers and the quaternions. Allowing pairs of these as well gives exactly the algebras in which no nonzero element has a power equal to zero.

## one-liner
The only real Clifford algebras without zero divisors are $\R$, $\C$ and $\HH$, and the only ones without nilpotents are these together with $\R \oplus \R$ and $\HH \oplus \HH$.
