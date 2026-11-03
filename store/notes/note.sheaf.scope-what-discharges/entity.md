---
id: note.sheaf.scope-what-discharges
kind: note
version: 1
title: Scope, and what this discharges
status: remark
subject: walls
proposed_by:
  kind: extraction
  session: notes-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
comments_on:
- sheaf.transversal-independence-wall
- sheaf.determinant-identity-blow-up-expansion
- sheaf.no-equivariant-value-wall
locators:
  paper: T04
  number: Rem 10.5
  label: rem:transversalscope
  line: 1384
---

## formal
The statements are pointwise on $\Sig$, every formula rational in the collar data and hence smooth in the point, so they hold over every open piece of the wall; the collar constants and bump are held fixed, their variation being the rescaling of Section \ref{sec:dictionary}. Off the wall the two ambient forms $h_u$ and $h_{u+v}$ need not be isometric, and Theorem \claimref{sheaf.transversal-independence-wall} does not say they are: by Lemma \claimref{sheaf.determinant-identity-blow-up-expansion}, $\det h = \det G \cdot (-(1 + 2\mu\nu\beta^2 s))$ with $s = G^{-1}(e,e)$ depending on the transversal, so the shadow wall of Section \ref{sec:wall} moves with the transversal, and on a far-side collar point one form can be degenerate while the other is not, or both nondegenerate with different signatures (the script exhibits both, on the model data $G = \operatorname{diag}(\lambda, 1, -1, -1)$ with $\mu\nu = 1$). The transversal independence proved here is a statement at the wall, and nothing off the wall is needed: the value question is a question at the wall. What Theorem \claimref{sheaf.no-equivariant-value-wall} discharges downstream is the boundary case that the singularity paper recorded as open in the scope of its no-repair import \cite{ButlerT5}: with the theorem in place, no classical value repairs the dying direction on the approach or at the boundary itself.

## technical
pending

## lay
pending

## one-liner
pending
