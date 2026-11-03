---
id: note.primer.setting-signature-arrival-null-vectors
kind: note
version: 1
title: Signature, and the arrival of null vectors
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
  section: Signature, and the arrival of null vectors
  line: 303
---

## formal
Over the reals, a nondegenerate quadratic form can be brought to a diagonal shape in which $p$ basis vectors square to $+1$ and $q$ square to $-1$; the pair $(p,q)$ is the \emph{signature}, and it is an invariant (Sylvester's law \cite{Lam2005}). Write $\Cl(p,q)$ for the corresponding algebra. Euclidean space is $(n, 0)$; the spacetime of physics is $(1,3)$: one time direction of positive square, three space directions of negative square.

Signatures with $p, q \geq 1$ are called \emph{mixed}, and something qualitatively new happens there. Positive and negative squares can cancel:
\[
v \;=\; e_1 + e_n, \qquad v^{2} \;=\; e_1^{2} + e_n^{2} \;=\; 1 - 1 \;=\; 0 \qquad (e_1^2 = 1,\ e_n^2 = -1).
\]
(The cross terms $e_1 e_n + e_n e_1 = 2\,e_1 \cdot e_n$ vanish because the basis is orthogonal.) A nonzero vector whose square is zero is called \emph{null} (or isotropic). Null vectors fill a cone, the \emph{null cone}, and in spacetime that cone is the light cone: the null directions are the paths light takes. In a definite signature there are no null vectors at all; $Q(v) = 0$ forces $v = 0$.

A vector with $Q(v) \neq 0$ has the inverse $v^{-1} = v / Q(v)$, since $v\,(v/Q(v)) = v^2/Q(v) = 1$; a null vector has none, and what that failure means, and what can be done about it, is the series' opening question. This primer stops here: the failure of division, its taxonomy, and its repair are assigned to T1, from the first definition onward.

## technical
pending

## lay
pending

## one-liner
pending
