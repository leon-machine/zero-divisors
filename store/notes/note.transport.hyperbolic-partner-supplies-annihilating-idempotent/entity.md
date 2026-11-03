---
id: note.transport.hyperbolic-partner-supplies-annihilating-idempotent
kind: note
version: 1
title: The hyperbolic partner supplies the annihilating idempotent
status: example
subject: zero-divisors
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
comments_on:
- transport.existence-locus-type-n
- transport.regularity-localises-zero-divisors-idempotents
- transport.no-go-level-elements
locators:
  paper: T01
  number: Ex 3.4
  label: ex:hyperbolic-idem
  line: 590
---

## formal
Let $v$ be null and $(v, w)$ a hyperbolic pair, $vw + wv = 1$. Then $e = wv$ is idempotent ($e^2 = w(vw)v = w(1 - wv)v = wv$, using $v^2 = w^2 = 0$), non-central (it fails to commute with $v$: $ev = wv\cdot v = wv^2 = 0$, while $ve = v(wv) = (vwv) = v \neq 0$), and
\[
v(1 - e)\;=\;v - vwv \;=\; v - v \;=\; 0 , \qquad (1-e) \ne 0.
\]
Thus the abstract annihilator idempotent of Lemma \claimref{transport.regularity-localises-zero-divisors-idempotents} is, for a type-N obstruction, realised by the geometry itself: the pseudo-inverse $w$ of Section \ref{subsec:null} produces it. Type N is in this sense a geometric refinement of type P: a null vector is a zero divisor \emph{whose annihilating idempotent comes from an isotropic line}. What Theorem \claimref{transport.no-go-level-elements} will prove is that this refinement carries an obstruction the generic type-P case does not: the choice of $w$, hence of $e$, is sheared by the null rotations, and no equivariant choice exists in any ascent.

## technical
pending

## lay
pending

## one-liner
pending
