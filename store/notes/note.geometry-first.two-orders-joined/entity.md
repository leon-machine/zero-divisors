---
id: note.geometry-first.two-orders-joined
kind: note
version: 1
title: The two orders, joined
status: remark
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
- synthesis.integer-clifford-algebras-contain-no-switch
locators:
  paper: T00a
  number: Rem 8.3
  label: rem:joined
  line: 575
---

## formal
The two orders of Remark \claimref{note.synthesis.two-orders-of-construction-ladder-and-switch} meet in the operations on a register, and $E$ tells them apart. The switch order starts from the $v_{i}$ and $w_{i}$. The ladder starts at (F1), which on the reading above is the image of $E$ without its scalars, and its premises (F2) and (F3) add, for each distinction, one combination of set and clear: the direction $L_{i} = v_{i} + \varepsilon_{i}w_{i}$ of part (vi), with the signature as the sign $\varepsilon_{i}$. The other combination $L_{i}'$, of the opposite square, is not a left multiplication, unless $2 = 0$ in $R$, when it coincides with $L_{i}$: if it were left multiplication by $y$ then $y = L_{i}'e_{\emptyset} = e_{i}$, and $L_{i} - L_{i}' = 2\varepsilon_{i}w_{i}$.

Nor does the ladder's algebra contain any test of its own distinctions, over any ring: by (vi) the pinching sends every left multiplication to its scalar part, so a left multiplication that commutes with every test is a scalar. (The tests that Theorem \claimref{synthesis.integer-clifford-algebras-contain-no-switch}(iii) supplies when $2$ is invertible belong to a different bit; they are not diagonal on the configurations.) Which end the foundation should take is still a choice, and (F1) to (F4) stand as stated.

The map is already in the series. For one switch,
\[
E(x) \;=\; PxP + (1-P)\,x\,(1-P)
\]
is the descent of T5 \cite{ButlerT5} (Proposition 5.5 there), and for $n$ switches it is T5's multi-mode descent (Definition 9.1 there), whose range T5 calls the classical algebra of occupation records. Read with Proposition \ref{prop:pinching}: the descent of a register returns the functions on the configurations of (F1), the bare bit on the reading above, and the ascent, which adjoins the pairs $(v_{i}, w_{i})$, supplies its operations. This is a comparison of definitions. T5's use of the descent, on the algebras and states of a black hole, is not treated here, and Proposition \ref{prop:pinching} does not depend on it.

\emph{Status.} Proposition \ref{prop:pinching} is proved, and every step of it is elementary. That it matters for physics is a reading. Nothing here uses a rule of transport, and none of it is evidence for the transport principle.

## technical
pending

## lay
pending

## one-liner
pending
