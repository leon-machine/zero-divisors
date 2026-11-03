---
id: note.primer.euclidean-plane
kind: note
version: 1
title: The Euclidean plane
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
  number: Ex 2.1
  label: ex:plane
  line: 273
---

## formal
Let $e_1, e_2$ be an orthonormal basis of the Euclidean plane: $e_1^{2} = e_2^{2} = 1$ and $e_1 \cdot e_2 = 0$, so $e_1 e_2 = -e_2 e_1$. Multiply two general vectors $a = a_1 e_1 + a_2 e_2$ and $b = b_1 e_1 + b_2 e_2$:
\[
ab \;=\; (a_1 b_1 + a_2 b_2) \;+\; (a_1 b_2 - a_2 b_1)\, e_1 e_2 .
\]
The scalar part is the dot product; the coefficient of $e_1 e_2$ is the signed area. One product carries both. Now square the bivector:
\[
(e_1 e_2)^{2} \;=\; e_1 e_2 e_1 e_2 \;=\; - e_1 e_1 e_2 e_2 \;=\; -1 .
\]
The unit bivector of the Euclidean plane squares to $-1$. The even elements $\alpha + \beta\, e_1 e_2$ therefore multiply exactly like complex numbers: the complex plane is contained in the geometric algebra of the real plane, as its even half, and the imaginary unit is the plane's own unit of oriented area. The invertible product the plane has had since the eighteenth century, complex multiplication, is therefore not an ingredient of the construction but a consequence of it.

## technical
pending

## lay
pending

## one-liner
pending
