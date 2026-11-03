---
id: note.mass.setting-grip-composite-frozen-point-2
kind: note
version: 2
title: The grip of a composite on the frozen point
status: setting
subject: mass
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
comments_on:
- mass.grip-real
- mass.de-sitter-scale-frozen-point
- mass.imported-frozen-point-tractor-connection
- mass.five-broken-generators
locators:
  paper: T11
  number: Setting
  section: The exact join
  line: 675
  subsection: The grip of a composite on the frozen point
extraction:
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
---

## formal
Three properties follow at once. First, $\ip{P}{I} = M_{I\wedge I} = 0$: the grip lies in $I^{\perp}$. Second, $m^{2}$ is invariant under the stabiliser of $I$: for $\gamma$ with $\gamma I = I$, $\ip{P(\gamma Z)}{U} = M_{U\wedge I}(\gamma Z) = M_{\gamma^{-1}(U\wedge I)}(Z) = M_{\gamma^{-1}U\wedge I}(Z) = \ip{P(Z)}{\gamma^{-1}U} = \ip{\gamma P(Z)}{U}$, so $P(\gamma Z) = \gamma P(Z)$ and $Q(P)$ is unchanged; for the frozen point of Lemma \claimref{mass.de-sitter-scale-frozen-point} the stabiliser acts on the ambient space through $SO(1,4)$ (Fact \claimref{mass.imported-frozen-point-tractor-connection}; the Lie-algebra form of the surjection is Lemma \claimref{mass.five-broken-generators}), and $P$ is a de Sitter vector. Third, at $\Lambda = 0$, $I = n_{\infty}$ and $\ip{P}{x} = M_{x\wedge n_{\infty}}$ is, by Lemma \claimref{mass.chart-form-spin-isomorphism}(2), the value of the translation generator on the composite, that is, its total momentum in the direction $x$; the $x$-slot part of $P$ is therefore the momentum, the remaining part is $-d\,n_{\infty}$ with $d$ the dilation charge, and since $n_{\infty}$ is null and orthogonal to the $x$-slot, $m^{2}$ is the Poincar\'e Casimir $p^{2}$. Definition \claimref{obj.mass.grip-mass-composite} is the de Sitter extension of the mass of Proposition \claimref{mass.mass-symplectic-area-two-twistor-formula}: the composite's momentum is its grip on the point at infinity, and its mass is the length of that grip. Lemma \claimref{mass.five-broken-generators} below identifies the generators $A(e_{a}\wedge I)$, $e_{a} \in I^{\perp}$, whose charges are the components of $P$, with the five generators of $\mathfrak{su}(2,2)$ broken by $I$, the de Sitter translations, which is the representation-theoretic form of the same statement. That $P$ is a real vector, so that $Q(P)$ is a value of the real $(1,4)$ form on $I^{\perp}$, is the next lemma.

## technical
pending

## lay
pending

## one-liner
pending
