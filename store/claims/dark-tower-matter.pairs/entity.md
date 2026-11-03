---
id: dark-tower-matter.pairs
kind: claim
version: 3
title: The ladder pairs of the causal towers
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [ladder-pairs, witt-index, two-readings]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T14c, the series'' standard disclaimer'
review: typed
derivations:
- name: main
  uses:
  - dark-tower-matter.constituents-field@2
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:D1a
  - id:D1b
- kind: check
  ref: check.py::check_real_witt_index
- kind: check
  ref: check.py::check_complex_witt_index
- kind: check
  ref: check.py::check_unit_fixed_up_to_sign
locators:
  paper: T14c
  number: Prop 4.1
  label: prop:pairs
  line: 435
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: two real CAR pairs and definite complement (real index 2) for all six conformal spaces; complex third pair over Q(i) in dims 6, 7 (index 2, 3, 3); unit of the C corner fixed up to sign, R and H controls. Version 2 -> 3.'
  env: proposition
  unresolved_refs:
  - rem:whyU
  typing:
    by: ai-typing-pass
    added:
    - dark-tower-matter.constituents-field
    note: 'Added the constituent''s field, which (ii) uses for ''the field is C'' in this tower and the
      mirror; the cited remark on why U is a note and cannot be a premise. Levels pass: levels written
      from scratch, keeping every condition and level qualifier of the formal statement.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - dark-tower-matter.constituents-field
---

## formal
\begin{enumerate}
\item[(i)] In the three-dimensional towers the real and complex Witt indices of $\hatV$ are both $2$: two real ladder pairs, and no unit is needed (check D1).
\item[(ii)] In this tower, the mirror and the five-dimensional towers the real Witt index is $2$ and the complex one $3$: the third pair needs a complex unit. In this tower and the mirror the field is $\C$ and the unit is fixed up to sign (Remark \ref{rem:whyU}).
\end{enumerate}

## technical
The conformal space $\hatV$ of a causal tower has signature $(p+1, q+1)$ with $\min(p,q) = 1$, so its real Witt index is $2$, while its complex Witt index is $\lfloor \dim\hatV/2 \rfloor$. In the three-dimensional towers both are $2$: two real ladder pairs, and no unit is needed. In this tower, the mirror and the five-dimensional towers the real index is $2$ and the complex one $3$, so the third pair needs a complex unit; in this tower and the mirror the field is $\C$ and the unit is fixed up to sign.

## lay
Each constituent carries internal ladder pairs, pairs of creation and annihilation operations built from the directions of its conformal algebra. In the three-dimensional towers there are two, built from real numbers alone. In the four- and five-dimensional towers there are three, and the third can only be built with a square root of minus one; in our tower and the mirror that root is fixed up to sign.

## one-liner
The three-dimensional towers have two real ladder pairs, while the four- and five-dimensional towers have a third pair that needs a complex unit, fixed up to sign where the field is $\C$.
