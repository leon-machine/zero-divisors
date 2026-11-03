---
id: obj.sheaf.extensions
kind: object
version: 2
title: Extensions
status: defined
region: sheaf
subject: walls
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
about:
- obj.sheaf.weighted-coframe-module
locators:
  paper: T04
  number: Def 8.17
  label: def:extension
  line: 1049
extraction:
  env: definition
  context_refs:
  - sheaf.rain-duality
  unresolved_refs:
  - rem:boundarytame
  typing:
    by: ai-typing-pass
    note: "Object: levels only."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [sheaf.uniqueness-weighted-module]
    added_about: [obj.sheaf.weighted-coframe-module]
    verdict: connected
    note: 'About from the uniqueness theorem, stated over rain-bounded extensions; the definition characterises rain-boundedness by containment in the weighted coframe module.'
---

## formal
An \emph{extension} is a locally free rank-four $C^\infty(\Mt_u)$-submodule $\mathcal{M}$ of the $u$-smooth one-forms which spans the full cotangent module over the interior and whose Gram $G|_{\mathcal{M}\times\mathcal{M}}$ extends smoothly to $E$. It is \emph{rain-bounded} if every element has bounded components in the infalling orthonormal frame, equivalently (Proposition \claimref{sheaf.rain-duality}(3)) if $\mathcal{M} \subseteq \shW$. The boundary-tameness conditions are those of Remark \ref{rem:boundarytame}, with (T3$\partial$) read on the eigenvalue: the dying \emph{eigenvalue} of the Gram, with respect to any auxiliary frame metric, vanishes to exactly first order in the defining function $r$.

## technical
An extension is a locally free rank-four $C^\infty(\Mt_u)$-submodule $\mathcal{M}$ of the $u$-smooth one-forms that spans the full cotangent module over the interior and whose Gram $G|_{\mathcal{M}\times\mathcal{M}}$ extends smoothly to the boundary $E$. It is rain-bounded if every element has bounded components in the infalling orthonormal frame, which is equivalent to $\mathcal{M} \subseteq \shW$. For boundary tameness the condition on the dying direction is read on the eigenvalue: the dying eigenvalue of the Gram, with respect to any auxiliary frame metric, vanishes to exactly first order in the defining function $r$.

## lay
Near the black hole singularity there are many ways to decide which one-forms count as well behaved at the boundary. An extension is any such choice that agrees with ordinary geometry inside, has the right size, and keeps the geometry's measurements smooth up to the boundary. It is called rain-bounded if everything in it stays finite as seen by observers falling freely inwards.

## one-liner
An extension is a locally free rank-four module of $u$-smooth one-forms, equal to the cotangent module in the interior, whose Gram extends smoothly to $E$; it is rain-bounded when it lies in $\shW$.
