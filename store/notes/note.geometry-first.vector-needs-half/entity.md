---
id: note.geometry-first.vector-needs-half
kind: note
version: 1
title: A vector that needs a half
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
- synthesis.division-gives-the-rationals
locators:
  paper: T00a
  number: Ex C
  label: ex:half
  line: 254
---

## formal
With $n = 2$ and $N$ empty, the integer vector $v = e_{1} + e_{2}$ has $v^{2} = 2$, so
\[
v \cdot \tfrac12\,v \;=\; 1 ,
\]
and its inverse $\tfrac12(e_{1} + e_{2})$ exists over $\Q$ but not over $\Z$. In $\Cl(1,1)$, by contrast, the null vector $e_{1} + e_{2}$ of Example~\claimref{note.geometry-first.one-rule-hand} has no inverse over any nonzero coefficient ring: if $vu = 1$ then $v = v(vu) = v^{2}u = 0$, which is false.

## technical
pending

## lay
pending

## one-liner
pending
