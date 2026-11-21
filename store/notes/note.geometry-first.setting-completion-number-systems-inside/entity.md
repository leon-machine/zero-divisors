---
id: note.geometry-first.setting-completion-number-systems-inside
kind: note
version: 1
title: Completion, and the number systems inside
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-11-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: idea, direction and review
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T00a, deposited version
comments_on:
- synthesis.completion-recovers-the-real-clifford-algebras
locators:
  paper: T00a
  number: Setting
  section: Completion, and the number systems inside
  line: 271
---

## formal
This is the one step that is not algebraic, and it is the last premise. What it gives is proved here in three stages: square roots, and with them the classification of quadratic forms by their signs; roots of polynomials; and the list of the algebras in which division never fails. The results are classical \cite{Lam2005, Ebbinghaus1991}; the proofs are written out so that the step to the real numbers rests on (F4) and on nothing else.

Some vocabulary first. Let $F$ be an ordered field. A \emph{quadratic space} over $F$ is a finite-dimensional vector space $V$ with a map $Q : V \to F$ such that $Q(\lambda v) = \lambda^{2}Q(v)$ and
\[
B(u, v) \;=\; \tfrac12\bigl(Q(u + v) - Q(u) - Q(v)\bigr)
\]
is bilinear; then $Q(v) = B(v, v)$. Vectors $u, v$ are \emph{orthogonal} when $B(u,v) = 0$; in any algebra in which $v^{2} = Q(v)$, expanding $(u+v)^{2}$ gives $uv + vu = 2B(u,v)$, so orthogonal vectors are exactly those that anticommute. An \emph{isometry} is a linear bijection that preserves $Q$. The field $F$ is \emph{Euclidean} when every positive element is a square (and $0 = 0^{2}$, so then every element that is not negative is one). For $a \in F$, $|a|$ is $a$ or $-a$, whichever is not negative; one checks from the rules of the order, case by case on the signs, that $|ab| = |a|\,|b|$ and $|a + b| \leq |a| + |b|$. Finally, in an ordered field $1 = 1^{2} > 0$, so $m \cdot 1 > 0$ for every positive integer $m$: the field contains $\Q$, it is infinite, and division by $2$ is always possible.

## technical
pending

## lay
pending

## one-liner
pending
