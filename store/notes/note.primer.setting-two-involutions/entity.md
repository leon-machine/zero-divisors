---
id: note.primer.setting-two-involutions
kind: note
version: 1
title: The two involutions
status: setting
subject: clifford-structure
proposed_by:
  kind: extraction
  session: settings-2026-10-21
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
  number: Setting
  section: The two involutions
  line: 352
---

## formal
Two canonical symmetries act on every Clifford algebra, both fixed by what they do to vectors.

The \emph{grade involution} $x \mapsto \hat{x}$ sends every vector to its negative, $\hat{v} = -v$, and extends multiplicatively: $\widehat{xy} = \hat{x}\hat{y}$. On a blade of grade $k$ it gives the sign $(-1)^{k}$, so it fixes the even grades and negates the odd ones. It is the algebraic counterpart of the point reflection $x \mapsto -x$.

The \emph{reversion} $x \mapsto \tilde{x}$ fixes every vector, $\tilde{v} = v$, but reverses the order of products: $\widetilde{xy} = \tilde{y}\tilde{x}$. On a blade of grade $k$ it gives the sign $(-1)^{k(k-1)/2}$, the sign produced by reversing $k$ anticommuting factors. It plays the role that transposition plays for matrices and conjugation plays for complex numbers.

One consequence is used constantly. If a vector $v$ is orthogonal to every vector appearing in an element $x$, then moving $v$ past $x$ produces exactly a grade involution:
\[
v\,x \;=\; \hat{x}\,v .
\]
For a single orthogonal vector this is just anticommutation; the general case follows because both sides are multiplicative in $x$.

## technical
pending

## lay
pending

## one-liner
pending
