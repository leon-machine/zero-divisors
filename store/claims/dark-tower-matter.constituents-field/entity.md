---
id: dark-tower-matter.constituents-field
kind: claim
version: 2
title: The constituent's field in each tower
status: proved
region: dark-tower-matter
subject: dark-matter
tags: [towers-by-residue, clifford-classification]
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
  - dark-tower-matter.imported-clifford-structure@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: legacy
  script: verify_T14c.py
  tags:
  - id:A1
  - id:A2
  - id:A3
  - id:A4
  - id:A5
- kind: check
  ref: check.py::check_fields_by_corner_at_both_levels
- kind: check
  ref: check.py::check_fields_by_direct_commutant
- kind: check
  ref: check.py::check_field_is_not_a_function_of_omega_squared
locators:
  paper: T14c
  number: Thm 3.2
  label: thm:fields
  line: 218
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the field table at tower and conformal level by the corner f Cl^0 f and by the directly solved commutant, the ideal dimensions, and Q(omega) of the conformal pseudoscalar. Version 1 -> 2.'
  env: theorem
  typing:
    by: ai-typing-pass
    added:
    - obj.dark-tower-matter.ideals-fields-momentum
    note: 'Kept the Clifford-structure fact (the proof reads the field off its three clauses). The source
      calls the theorem a corollary of the periodicity table; the main derivation already rests only on
      that imported fact, so no separate standard-route derivation was added. Levels pass: levels written
      from scratch, keeping every condition and level qualifier of the formal statement.'
about:
- obj.dark-tower-matter.ideals-fields-momentum
---

## formal
In tower $r$ the fields $\F(T)$ and $\F(S)$ are equal, and equal to the division algebra of residue $r + 1$:
\begin{center}\small
\begin{tabular}{@{}lccccccccc@{}}
\toprule
$r$ & $6$ & $2$ & $1$ & $7$ & $3$ & $5$ & $0$ & $4$ \\
tower & $(1,3)$ & $(3,1)$ & $(2,1)$ & $(1,2)$ & $(4,1)$ & $(1,4)$ & $(2,2)$ & $(4,0)$, $(0,4)$ \\
conformal & $(2,4)$ & $(4,2)$ & $(3,2)$ & $(2,3)$ & $(5,2)$ & $(2,5)$ & $(3,3)$ & $(5,1)$, $(1,5)$ \\
field & $\C$ & $\C$ & $\R$ & $\R$ & $\HH$ & $\HH$ & $\R$ & $\HH$ \\
$\dim_{\R} T$, $\dim_{\R} S$ & $8, 4$ & $8, 4$ & $4, 2$ & $4, 2$ & $16, 8$ & $16, 8$ & $4, 2$ & $8, 4$ \\
\bottomrule
\end{tabular}
\end{center}
In particular the field is not a function of the conformal pseudoscalar's square: $Q(\omega) = -1$ at $r = 7$ (field $\R$) and at $r = 3$ (field $\HH$).

## technical
For a tower $V = \R^{p,q}$ of residue $r = p - q \bmod 8$, the commutant of the spin action on the constituent ideal $T = \Cl^0(\hatV)\hf$ of the conformal algebra and the commutant on the spinor ideal $S = \Cl^0(V)f$ are equal, and both are the division algebra of residue $r + 1$, since $\Cl^0(p,q) \cong \Cl(p,q-1)$ shifts the residue by one. The field is $\C$ at $r = 6, 2$, $\R$ at $r = 1, 7, 0$ and $\HH$ at $r = 3, 5, 4$, with the ideal dimensions of the table.

The field is not a function of the square of the conformal pseudoscalar: $Q(\omega) = -1$ both at $r = 7$, with field $\R$, and at $r = 3$, with field $\HH$.

## lay
Each of the eight towers has its own kind of number for its basic constituents: real numbers, complex numbers or quaternions. This theorem reads off which from the classification of real Clifford algebras: complex for our tower and its mirror, real for the three-dimensional towers and one sterile tower, quaternionic for the five-dimensional towers and the other sterile tower. The answer is the same in the larger conformal algebra and in the tower itself.

## one-liner
In tower $r$ the constituent's field, at the conformal and the tower level alike, is the division algebra of residue $r + 1$: $\C$, $\R$ or $\HH$ as the causal tower's dimension is four, three or five.
