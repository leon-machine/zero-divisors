---
id: three-routes.imported-collar-data-coupling
kind: claim
version: 1
title: 'Imported: collar data and the coupling'
status: proved
region: three-routes
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
  source: 'authorship disclosure of T05-three-routes, the series'' standard disclaimer'
review: typed
about:
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
locators:
  paper: T05-three-routes
  number: Fact 1.1
  label: fact:coupling
  line: 102
extraction:
  typing:
    by: ai-typing-pass
    note: 'Restates a definition already in the store as an object, linked by about; no premise edges apply.'
  env: fact
  flags:
  - 'fact restating several series results: derived from them'
---

## formal
Collar data for $\Sig$ consist of a global spanning section $k$ of the radical line bundle $\shL$ (existing exactly when $w_1(\shL) = 0$, the standing hypothesis), a transversal vector field $u$ with $k(u) = 1$, a bump $\beta$ equal to $1$ on an inner collar, and constants $\mu, \nu \neq 0$. The coupling is the symmetric form $\kappa$ with $\kappa(\alpha, \nO) = \nu\beta\,\alpha(u)$ and $\kappa(\alpha, \nInf) = \mu\beta\,\alpha(u)$ for covectors $\alpha$, vanishing on covector pairs and on the adjoined plane; the ambient form is $h := G \perp H + \kappa$, with $H$ the hyperbolic plane form on $(\nO, \nInf)$, $\nO^2 = \nInf^2 = 0$, $\nO \cdot \nInf = -1$. On the inner collar $\beta = 1$, and every computation of this note is made there. \emph{Provenance:} \cite[Def.~4.1]{ButlerT4}, verbatim up to notation.

## technical
Collar data for $\Sig$ are a global section $k$ spanning the radical line bundle $\shL$, which exists exactly when $w_1(\shL) = 0$, a transversal vector field $u$ with $k(u) = 1$, a bump $\beta$ equal to $1$ on an inner collar, and nonzero constants $\mu, \nu$. The coupling $\kappa$ pairs a covector $\alpha$ with the adjoined null vectors by $\kappa(\alpha, \nO) = \nu\beta\,\alpha(u)$ and $\kappa(\alpha, \nInf) = \mu\beta\,\alpha(u)$, and vanishes on covector pairs and on the adjoined plane.

The ambient form is $h = G \perp H + \kappa$, with $H$ the hyperbolic plane form on $(\nO, \nInf)$: $Q(\nO) = Q(\nInf) = 0$ and $\nO \cdot \nInf = -1$. All computations are made on the inner collar, where $\beta = 1$.

## lay
To repair the degenerate geometry at the boundary, two extra directions are added and tied to the collapsing direction. The tie needs some auxiliary data: a choice of transverse direction, a cut-off function near the boundary and two constants. This fact records that recipe, carried over from earlier in the series.

## one-liner
Collar data, a global radical section $k$, a transversal $u$ with $k(u) = 1$, a bump and constants $\mu, \nu$, define the coupling $\kappa$ and the ambient form $h = G \perp H + \kappa$.
