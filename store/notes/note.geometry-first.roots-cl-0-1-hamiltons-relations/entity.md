---
id: note.geometry-first.roots-cl-0-1-hamiltons-relations
kind: note
version: 1
title: Roots in $\Cl(0,1)$, and Hamilton's relations
status: example
subject: clifford-structure
proposed_by:
  kind: extraction
  session: notes-2026-11-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: idea, direction and review
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00a, deposited version
comments_on:
- synthesis.frobenius-and-universality-in-clifford-algebras
- std-algebra.quaternions
locators:
  paper: T00a
  number: Ex D
  label: ex:roots
  line: 343
---

## formal
The polynomial $x^{2} - 2x + 5$ has no real root, and in $\C = \Cl(0,1)$, with $e^{2} = -1$, it has the roots $1 \pm 2e$:
\[
(1 + 2e)^{2} - 2(1 + 2e) + 5 \;=\; (1 + 4e - 4) - 2 - 4e + 5 \;=\; 0 ,
\]
and likewise for $1 - 2e$. In $\HH = \Cl(0,2)$ put $\mathbf{i} = e_{1}$, $\mathbf{j} = e_{2}$ and $\mathbf{k} = e_{1}e_{2}$. Then
\[
\mathbf{i}^{2} = \mathbf{j}^{2} = \mathbf{k}^{2} = -1, \qquad \mathbf{i}\mathbf{j} = \mathbf{k} = -\mathbf{j}\mathbf{i} ,
\]
since $\mathbf{k}^{2} = e_{1}e_{2}e_{1}e_{2} = -e_{1}e_{1}e_{2}e_{2} = -1$: these are Hamilton's relations. A third direction of square $-1$ breaks division, as Theorem~\claimref{synthesis.frobenius-and-universality-in-clifford-algebras} says it must. In $\Cl(0,3)$ the element $u = e_{1}e_{2}e_{3}$ has $u^{2} = 1$, and so
\[
(1 - u)(1 + u) \;=\; 1 - u^{2} \;=\; 0
\]
with both factors nonzero.

## technical
pending

## lay
pending

## one-liner
pending
