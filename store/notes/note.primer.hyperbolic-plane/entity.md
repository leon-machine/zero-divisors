---
id: note.primer.hyperbolic-plane
kind: note
version: 1
title: The hyperbolic plane
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
  number: Ex 4.1
  label: ex:hyperbolic
  line: 315
---

## formal
The smallest mixed signature is $(1,1)$, the \emph{hyperbolic plane}, and it is the smallest unit from which the whole subject is built. Set
\[
v \;=\; \tfrac12 (e_1 + e_2), \qquad w \;=\; \tfrac12 (e_1 - e_2) \qquad (e_1^2 = 1,\ e_2^2 = -1).
\]
Then $v^{2} = w^{2} = 0$: both are null. But their cross terms survive:
\[
vw + wv \;=\; 2\, v\cdot w \;=\; 2\cdot\tfrac14\,(e_1 + e_2)\cdot(e_1 - e_2) \;=\; \tfrac12\bigl(Q(e_1) - Q(e_2)\bigr) \;=\; 1 .
\]
A pair of null vectors with $vw + wv = 1$ is a \emph{hyperbolic pair}, and it satisfies the identity
\[
v\,w\,v \;=\; (1 - wv)\,v \;=\; v - w v^2 \;=\; v .
\]
Multiplying by $v$, then $w$, then $v$ returns $v$ exactly. What this identity means for the failure of division is the opening theme of T1; here it is simply an exact computation worth checking by hand.

## technical
pending

## lay
pending

## one-liner
pending
