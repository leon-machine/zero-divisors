---
id: std-algebra.involution-properties
kind: claim
version: 1
title: The three involutions on each grade
status: proved
region: std-algebra
programme: standard
subject: standard-algebra
tags:
- grading-and-parity
proposed_by:
  kind: ai
  session: algebra-core-2026-10-26
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: typed
trust: ai-proposed
about:
- obj.std-algebra.grade-involution
- obj.std-algebra.reversion
- obj.std-algebra.clifford-conjugation
derivations:
- name: main
  uses:
  - std-algebra.functoriality@1
  - std-algebra.existence-uniqueness@1
  - std-algebra.grade-decomposition@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_involutions_on_products_and_grades
locators:
  sources:
  - key: Lounesto2001
    locator: Ch. 14 (definitions of the Clifford algebra)
  - key: DoranLasenby2003
    locator: Ch. 4 (foundations of geometric algebra)
extraction:
  by: algebra-core-2026-10-26
---

## formal
The grade involution is an automorphism, reversion and Clifford conjugation are anti-automorphisms; all three are involutions and they commute. On $\Cl^{k}$ they act by
\begin{equation}
\hat{x} = (-1)^{k} x, \qquad \tilde{x} = (-1)^{k(k-1)/2} x, \qquad \bar{x} = (-1)^{k(k+1)/2} x .
\end{equation}
\texttt{GA.grade\_inv} and \texttt{GA.reverse} implement the first two.

## technical
The grade involution respects products, while reversion and conjugation reverse their order; each squares to the identity and they commute with one another. Each acts on a grade by a sign: the grade involution by $(-1)^{k}$, reversion by $(-1)^{k(k-1)/2}$ (so $+,+,-,-$ repeating), conjugation by $(-1)^{k(k+1)/2}$.

## lay
The three basic ways of "flipping" an element each multiply every grade by plus or minus one, according to a simple pattern in the grade. Reversion, for example, leaves numbers and arrows alone and changes the sign of planes and volumes.

## one-liner
On $\Cl^{k}$: $\hat{x} = (-1)^{k}x$, $\tilde{x} = (-1)^{k(k-1)/2}x$, $\bar{x} = (-1)^{k(k+1)/2}x$; the first is an automorphism, the others anti-automorphisms.
