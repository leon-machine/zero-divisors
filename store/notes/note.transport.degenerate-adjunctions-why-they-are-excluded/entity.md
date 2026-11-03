---
id: note.transport.degenerate-adjunctions-why-they-are-excluded
kind: note
version: 1
title: Degenerate adjunctions, and why they are excluded
status: remark
subject: completion
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
- obj.transport.null-lift-completion
- transport.minimality
locators:
  paper: T01
  number: Rem 4.15
  label: rem:degenerate
  line: 951
---

## formal
Nondegeneracy of $\mathbb{W}$ is a hypothesis of Definition \claimref{obj.transport.null-lift-completion}, not a consequence, and it is worth being exact about its role, since the degenerate adjunction $\Cl(n,0,1)$ of projective geometric algebra is a familiar and useful construction.

Over a base of \emph{mixed} signature the hypothesis is idle: the parenthetical second argument in the proof shows $Q_{\mathbb{W}}$ attains both signs, so $\mathbb{W}$ has a positive and a negative direction whether or not it also carries a radical, and the increment $(+1,+1)$ is forced regardless.

Over a \emph{definite} base the hypothesis is essential to the proof. Take $\mathbb{V}$ positive definite and let $\mathbb{W} = \mathrm{span}\{r, b\}$ with $r$ spanning a radical ($Q_{\mathbb{W}}(r) = 0$, $r \cdot b = 0$) and $Q_{\mathbb{W}}(b) = -1$. Then $f(x) = r + \sqrt{Q(x)}\,b$ satisfies $Q_{\mathbb{W}}(f(x)) = -Q(x)$ and $f(0) = r \neq 0$: a null lift of increment $(0,+1)$ plus a degenerate direction. Theorem \claimref{transport.minimality} excludes it by fiat, and rightly so for present purposes: everything the completion is asked to do here (represent points as rays on a quadric, realise the inversion as a reflection, and read out answers by descent) runs on the versor machinery of Section \ref{subsec:groups}, which needs invertible generators and Cartan--Dieudonn\'e, both unavailable along a radical direction. The minimality theorem should therefore be read as: among completions whose adjoined structure is usable as geometry, the increment is $(+1,+1)$, always.

## technical
pending

## lay
pending

## one-liner
pending
