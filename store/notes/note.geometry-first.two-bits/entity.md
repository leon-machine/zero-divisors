---
id: note.geometry-first.two-bits
kind: note
version: 1
title: Two bits
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
- synthesis.premise-minimal-non-commutativity
locators:
  paper: T00a
  number: Ex A
  label: ex:twobits
  line: 174
---

## formal
Take $n = 2$ with neither direction in $N$, so that $e_{1}^{2} = e_{2}^{2} = 1$. Premise (F2c) gives $e_{2}e_{1} = c\,e_{1}e_{2}$, and so
\[
(e_{1}e_{2})^{2} \;=\; e_{1}\,(e_{2}e_{1})\,e_{2} \;=\; c\,e_{1}e_{1}\,e_{2}e_{2} \;=\; c .
\]
In Theorem~\ref{thm:bitsign}(iii) this is $f(\{1,2\},\{1,2\}) = 1$: one pair $(2,1)$ with $2 > 1$, and nothing in $N$. So with two bits, and no sign put on either direction, the product of the two directions squares to the sign. When (F3) reads $c$ as $-1$ this is the unit bivector of the primer, the element that will play the complex unit. The whole multiplication table, row times column, is
\[
\begin{array}{c|cccc}
 & 1 & e_{1} & e_{2} & e_{1}e_{2} \\ \hline
1 & 1 & e_{1} & e_{2} & e_{1}e_{2} \\
e_{1} & e_{1} & 1 & e_{1}e_{2} & e_{2} \\
e_{2} & e_{2} & c\,e_{1}e_{2} & 1 & c\,e_{1} \\
e_{1}e_{2} & e_{1}e_{2} & c\,e_{2} & e_{1} & c
\end{array}
\]
and each $c$ in it counts one exchange of $e_{2}$ past $e_{1}$.

## technical
pending

## lay
pending

## one-liner
pending
