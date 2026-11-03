---
id: obj.sheaf.collar-data-coupling
kind: object
version: 1
title: Collar data and the coupling
status: defined
region: sheaf
subject: walls
tags: [degenerate-algebras, hyperbolic-plane]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
locators:
  paper: T04
  number: Def 4.1
  label: def:coupling
  line: 548
extraction:
  env: definition
  context_refs:
  - sheaf.imported-real-line-bundles
  typing:
    by: ai-typing-pass
    note: "Object: levels only."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [sheaf.tame-wall-induction, singularity.imported-no-equivariant-value-wall, three-routes.change-transversal-canonical-isomorphism-completions, three-routes.it-sheaf-risk-resolves-into-standing, tower.wall-package, obj.three-routes.ladder-bundle-even-subbundle, obj.three-routes.candidates-base-unipotents, sheaf.wall-class]
    added_about: []
    verdict: connected
    note: 'About from the statements that use collar data, the coupling or its ambient form; the T5 Fact that speaks of a nondegenerate ambient form in the root-paper sense was left out.'
---

## formal
A choice of \emph{collar data} for the tame wall $\Sig$ consists of: a \emph{global} spanning section $k$ of $\shL$, extended to a covector field on a neighbourhood of $\Sig$; a vector field $u$ near $\Sig$ with $k(u) = 1$ (a transversal, in the sense that $u$ is not annihilated by the dying direction); a bump function $\beta$ supported in a collar neighbourhood of $\Sig$ and identically $1$ on a smaller collar; and real constants $\mu, \nu \neq 0$. Collar data exist exactly when the radical line bundle is trivial, $w_1(\shL) = 0$ (Fact \claimref{sheaf.imported-real-line-bundles}); this triviality is a standing hypothesis of the completion construction, and Section \ref{subsec:choices} records why it is genuinely needed and what the twisted variant would be. Write $e \in TM$ for the field $u$ regarded as the evaluation functional $\alpha \mapsto \alpha(u)$ on $T^*M$. The \emph{coupling} is the symmetric form $\kappa$ on $T$ determined by
\[
\kappa(\alpha, \nO) = \nu\beta\,\alpha(u), \qquad \kappa(\alpha, \nInf) = \mu\beta\,\alpha(u) \qquad (\alpha \in T^*M),
\]
with $\kappa$ vanishing on $T^*M \times T^*M$ and on the adjoined plane. The \emph{ambient form} is
\[
h \;:=\; G \perp H + \kappa .
\]
Outside the support of $\beta$ the coupling vanishes and $h = G \perp H$; the restriction of $h$ to $T^*M$ is $G$ identically, everywhere, since $\kappa$ pairs $T^*M$ only with the adjoined plane.

## technical
Collar data for a tame wall $\Sig$ consist of a global spanning section $k$ of the radical line bundle $\shL$, extended as a covector field near $\Sig$; a transversal vector field $u$ with $k(u) = 1$; a bump function $\beta$ supported in a collar of $\Sig$ and equal to $1$ on a smaller collar; and nonzero constants $\mu, \nu$. They exist exactly when $\shL$ is trivial, $w_1(\shL) = 0$, a standing hypothesis of the completion.

The coupling $\kappa$ pairs covectors with the adjoined plane, $\kappa(\alpha, \nO) = \nu\beta\,\alpha(u)$ and $\kappa(\alpha, \nInf) = \mu\beta\,\alpha(u)$, and vanishes on $T^*M \times T^*M$ and on the adjoined plane. The ambient form is $h = G \perp H + \kappa$: outside the support of $\beta$ it is $G \perp H$, and its restriction to $T^*M$ is $G$ everywhere.

## lay
To complete the geometry at a wall one adds a small extra plane of directions, and must then say how it is attached to the original ones. Collar data are the choices needed for that: a label for the dying direction, a direction pointing across the wall, a smooth switch that is on near the wall and off far from it, and two constants. The coupling uses them to link the extra plane to the original directions near the wall only, without changing how the original directions measure each other.

## one-liner
Collar data, a global radical section $k$, a transversal $u$ with $k(u) = 1$, a bump function and two constants, define the coupling $\kappa$ and the ambient form $h = G \perp H + \kappa$, and they exist exactly when $w_1(\shL) = 0$.
