---
id: note.primer.boost-what-it-does-null-direction
kind: note
version: 1
title: A boost, and what it does to a null direction
status: example
subject: clifford-structure
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00, deposited version
comments_on:
- primer.commutation-rule
locators:
  paper: T00
  number: Ex 6.2
  label: ex:boost
  line: 386
---

## formal
In the hyperbolic plane $\Cl(1,1)$, even elements $R = a + b\, e_1 e_2$ have $R\tilde R = a^2 - b^2$, so rotors satisfy $a^{2} - b^{2} = 1$: they are the \emph{boosts}, the hyperbolic rotations of special relativity. Conjugating the null vector $v = \tfrac12(e_1 + e_2)$ of Example \claimref{note.primer.hyperbolic-plane}:
\[
R\,v\,R^{-1} \;=\; (a - b)^{2}\, v \qquad \text{(exactly, using } (a-b)(a+b) = 1\text{)}.
\]
A boost does not move the null direction; it \emph{rescales} it. The null lines are the boost's eigendirections, with reciprocal eigenvalues $(a \mp b)^{2}$. This one computation underlies a great deal of physics: it is why horizons redshift, and in the series it is why the completed algebra at a black-hole singularity carries a preferred one-parameter flow.

## technical
pending

## lay
pending

## one-liner
pending
